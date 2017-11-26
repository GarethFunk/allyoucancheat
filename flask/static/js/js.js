function plagiarise(essay) {
    $.ajax({
        type: "POST",
        url: "/plagiarise",
        data: {'essay': essay},
        success: function(r) {
            update(JSON.parse(r));

        }
    });
}

function update(essay) {
    editor.setValue(essay, 1);
}

$(function() {
    $("#pl-btn").click(function() {
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
                console.log(JSON.parse(r));

            }
        });
    });
});