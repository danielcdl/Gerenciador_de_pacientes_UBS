$(document).ready(function () {
    $('#tipo').on('change', function () {
        let tipo = this.value;
        let divDado = $('#div_dado');
        let divLbDado = $('#div_lb_dado');
        let label = $('#lb_dado');
        let input = $('#dado');
        let textoLabel = $('#tipo option:selected').text();

        if (tipo === 'todos' || tipo === '') {
            divDado.hide();
            divLbDado.hide();
        } else {
            divDado.show();
            divLbDado.show();
            label.text(textoLabel);

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
        let dados = $(this).serialize();
        $.ajax({
            url: "tabela/",
            type: "GET",
            data: dados,
            success: function (data) {
                let divTabela = $('#div_tabela');
                divTabela.html(data);
            },
            error: function (request, status, error) {
                console.log('erro')
                let divTabela = $('#div_tabela');
                divTabela.html('<h4>' + error + '. Tente Novamente.</h4>');
            }
        });
        return false;
    });
});
