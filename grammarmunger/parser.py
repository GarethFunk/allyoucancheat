from nltk.parse.stanford import StanfordDependencyParser
import re

from synon.synon import syn

dependency_parser = StanfordDependencyParser(path_to_jar='grammarmunger/stanford-parser/stanford-parser.jar',
                                             path_to_models_jar='grammarmunger/stanford-parser/stanford-parser-3.8.0-models.jar',
                                             corenlp_options='-outputFormatOptions includePunctuationDependencies')


class TreeNode:
    def __str__(self):
        return "(" + \
               "dependency = " + self.relation + \
               ", value = (" + str(self.value) + \
               "), side = " + ("left" if self.left else "right") + \
               ", children = " + self.list_children() + \
               ")"

    def list_children(self):
        s = "["
        first = True
        for child in self.children:
            if not first:
                s = s + ", "
            s = s + str(child)
            first = False
        s = s + "]"
        return s

    def __init__(self, left, value, relation, children, parent):
        self.left = left
        self.value = value
        self.relation = relation
        self.children = children
        self.parent = parent


def flatten_tree(tree):
    nodes_in_order = []
    get_all_nodes(tree, nodes_in_order)
    string = ""
    no_space_next = True
    for node in nodes_in_order:

        if node.value[0].startswith("'") or node.value[0] == ')' or node.value[0] == ',' or node.value[0] == ';' \
                or node.value[0].startswith(":") or node.value[0] == '%' or node.value[0] == '?':
            no_space_next = True

        if not no_space_next:
            string = string + " "

        string = string + format_node(node)

        if node.value[0] == '(':
            no_space_next = True
        else:
            no_space_next = False

    return string


def get_all_nodes(tree, node_list):
    for child in tree.children:
        if child.left:
            get_all_nodes(child, node_list)
    node_list.append(tree)
    for child in tree.children:
        if not child.left:
            get_all_nodes(child, node_list)


# paraphrase_with_structure_maps
def paraphrase_with_structure_maps(sentence):
    sent = pre_process(sentence)
    if sent == "":
        return post_process(sent)
    result = dependency_parser.raw_parse(sent)
    graph = next(result)
    tree = node_to_tree(graph.root, graph, 0)
    if flatten_tree(tree) != sent:
        re_lex(tree)
        return sentence
    re_plan_unit(tree)
    tree = get_top(tree)
    re_lex(tree)
    str = post_process(flatten_tree(tree))
    print(sent)
    print(str)
    return str


def get_top(tree):
    if tree.parent is None:
        return tree
    return get_top(tree.parent)


def get_node(id, graph):
    for nodeIndex in graph.nodes:
        if graph.nodes[nodeIndex]["address"] == id:
            return graph.nodes[nodeIndex]


# paraphrase_with_structure_maps
def node_to_tree(node, graph, parentIndex):
    children = []
    t = TreeNode(node["address"] < parentIndex, (node["word"], node["tag"]), node["rel"], children, None)
    for dep in node['deps']:
        for next_node_id in node["deps"][dep]:
            n = node_to_tree(get_node(next_node_id, graph), graph, node["address"])
            n.parent = t
            children.append(n)
    return t


def has_dependency(node, rel):
    has = False
    for child in node.children:
        if child.relation == rel:
            return True
    return has


def get_dependency(node, rel):
    for child in node.children:
        if child.relation == rel:
            return child
    return None


def get_dependency_from_pos(node, pos):
    for child in node.children:
        if child.value[1] == pos:
            return child
    return None


def re_lex(node):
    for child in node.children:
        re_lex(child)
    print(node)
    node.value = (syn(node.value[0], node.value[1]), node.value[1])


def re_plan_unit(node):
    for child in node.children:
        re_plan_unit(child)

    if has_dependency(node, "nmod:poss"):
        possessor = get_dependency(node, "nmod:poss")
        affix = get_dependency_from_pos(possessor, "POS")
        possessor.children.remove(affix)
        possessor.relation = 'nmod'
        possessor.left = False
        possessor.children.insert(0, TreeNode(True, ("of", "IN"), "case", [], possessor))
        node.children.insert(find_det_point(node), TreeNode(True, ("the", "DET"), "det", [], node))

    if has_dependency(node, "cop"):
        cop = get_dependency(node, "cop")
        if cop.value[0] == 'is':
            parent = node.parent
            other = get_dependency(node, "nsubj")
            rdet = get_dependency(node, "det")
            ldet = get_dependency(other, "det")

            if ((rdet is not None and rdet.value[0] == "the") or \
                    (ldet is not None and ldet.value[0] == "the")) and \
                    not (rdet is not None and (rdet.value[0] != "the")) or \
                    (ldet is not None and (ldet.value[0] != "the")):
                other.children.insert(0, cop)
                node.children.remove(cop)
                cop.parent = other

                rel = other.relation
                other.relation = node.relation
                node.relation = rel

                other.children.insert(0, node)
                node.children.remove(other)
                par = node.parent
                node.parent = other
                other.parent = par

                l = other.left
                other.left = node.left
                node.left = l

                if parent is not None:
                    index = parent.children.index(node)
                    parent.children.insert(index, other)
                    parent.children.remove(node)


def find_det_point(node):
    i = 0
    for child in node.children:
        if not child.left:
            continue
        if child.relation == 'case':
            i = i + 1
        else:
            break
    return i


def find_pos_point(node):
    i = 0
    for child in node.children:
        if child.left:
            continue
        if child.relation == 'case':
            i = i + 1
        else:
            break
    return i


def pre_process(text):
    if text.endswith("."):
        text = text[:-1]
    if text == "":
        return ""
    return text[0].lower() + text[1:]


def post_process(text):
    return text[0].upper() + text[1:]


def format_node(node):
    return node.value[0]
