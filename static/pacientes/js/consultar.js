$(document).ready(function () {

    $('#tipo').on('change', function () {
        let tipo = this.value;
        let divDado = $('#div_dado');
        let divLbDado = $('#div_lb_dado');
        let label = $('#lb_dado');
        let input = $('#dado');
        let textoLabel = $('#tipo option:selected').text();

        if (tipo === 'todos' || tipo === '') {
            input.removeAttr('required');
            divDado.hide();
            divLbDado.hide();
        } else {
            divDado.show();
            divLbDado.show();
            label.text(textoLabel);
            input.attr('required', 'required');
        }
        if (tipo === 'sus' || tipo === 'familia') {
            input.attr('type', "number");
        } else if (tipo === 'nascimento') {
            input.attr('type', "date");
        } else {
            input.attr('type', "text");
        }
    });


    $("#form_pesquisa").submit(function () {
        $.ajax({
            url: "tabela/",
            type: "GET",
            data: $(this).serialize(),
            success: function (data) {
                $('#div_tabela').html(data);
            },
            error: function (request, status, error) {
                $('#div_tabela').html('<h5>' + error + '. Tente Novamente.</h5>');
            }
        });
        return false;
    });
});
