function plagiarise(essay) {
    $.ajax({
        type: "POST",
        url: "/plagiarise",
        data: {'essay': essay},
        success: function(r) {
            update(JSON.parse(r).join(". "));

        }
    });
}

function update(essay) {
    editor.setValue(essay, 1);
}

$(function() {
    ace.edit("editor");

    $("#pl-btn").click(function() {
        plagiarise(editor.getValue());
    });
});