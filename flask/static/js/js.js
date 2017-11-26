function plagiarise(essay) {
    $.ajax({
        type: "POST",
        url: "/plagiarise",
        data: {'essay': essay},
        success: function(r) {
            $(".spinner").hide();
            update(JSON.parse(r));

        }
    });
}

function update(essay) {
    editor.setValue(essay, 1);
}

$(function() {
    $("#pl-btn").click(function() {
        $(".spinner").show();
        plagiarise(editor.getValue());
    });

    $('#noise-level').slider({
        formatter: function(value) {
            return 'Noise Level: ' + value;
        }
    });

    $("#get-data").click(function() {
        $.ajax({
            type: "POST",
            url: "/getdata",
            data: {
                'graph-name': $("#graph-name").val(),
                'ideal-curve': $("#ideal-curve").val(),
                'x-min': $("#x-min").val(),
                'x-max': $("#x-max").val(),
                'x-interval-style': $("#x-interval-style").val(),
                'num-points': $("#num-points").val(),
                'noise-level': $("#noise-level").val()
            },
            success: function(r) {
                $("#data-box").html("");
                var resi = JSON.parse(r);

                var res = resi[0];
                var imgPath = resi[1];
                $.each(res, function(i, r) {
                    var row = $("<tr>");
                    row.append($("<td>").html(r[0].toFixed(3)));
                    row.append($("<td>").html(r[1].toFixed(3)));
                    $("#data-box").append(row);
                });

                $("#graph-img").attr("src", "/g/" + imgPath);
                $("#data-out").show();
            }
        });
    });
});