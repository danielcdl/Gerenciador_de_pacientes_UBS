$(document).ready(function () {
    $('#id_sus').on('change', function () {
        if (this.value !== '') {
            $.ajax({
                url: "dados/",
                type: "GET",
                data: $(this).serialize(),
                success: function (dados) {
                    if (dados.encontrado === true) {
                        let botao = $('#botao');
                        let reset = $('#reset');
                        let msg = $('#msg');
                        $('#encontrado').attr('value', 'encontrado');
                        $('#id_nome').val(dados.nome);
                        $('#id_mae').val(dados.mae);
                        $('#id_nascimento').val(dados.nascimento);
                        $('#id_familia').val(dados.familia);
                        $('#id_observacao').val(dados.observacao);

                        msg.attr('class', 'alert alert-success');
                        msg.text('Paciente encontrado!');
                        msg.show();
                        botao.text('ATUALIZAR');
                        botao.show();
                        reset.show();
                    }
                },
                error: function (request, status, error) {
                    let msg = $('#msg');
                    msg.text(error + '. Tente Novamente');
                    msg.show();
                }
            });
        }
    });

    $('#id_nome').on('change', function () {
        if (this.value !== '' && $('#encontrado').val() !== 'encontrado') {
            $.ajax({
                url: "dados/",
                type: "GET",
                data: $(this).serialize(),
                success: function (dados) {
                    let botao = $('#botao');
                    if (dados.encontrado === true) {
                        let sus = $('#id_sus');
                        if (sus !== dados.sus) {
                            sus.val(dados.sus);
                        }
                        $('#id_mae').val(dados.mae);
                        $('#id_nascimento').val(dados.nascimento);
                        $('#id_familia').val(dados.familia);
                        $('#id_observacao').val(dados.observacao);
                        botao.text('ATUALIZAR');
                        let msg = $('#msg');
                        msg.attr('class', 'alert alert-success');
                        msg.text('Paciente encontrado!');
                        msg.show();
                    } else {
                        botao.text('CADASTRAR');
                    }
                    botao.show();
                },
                error: function (request, status, error) {
                    let msg = $('#msg');
                    msg.text(error + '. Tente Novamente');
                    msg.show();
                }
            });
        }
    });

    $('#reset').on('click', function () {
        $('#encontrado').val('')
    })
});
