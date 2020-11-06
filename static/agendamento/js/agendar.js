$(document).ready(function () {
    let nome = $('#id_nome');
    nome.keyup(function () {
        if (this.value.length > 2) {
            $.ajax({
                url: "/pacientes/autocomplete/" + nome.val(),
                type: "GET",
                success: function (dados) {
                    let opcoes = '';
                    for (let paciente in dados) {
                        opcoes += "<option value='" + dados[paciente] + "'>";
                    }
                    $('#pacientes').html(opcoes)
                }
            });
        }
    });

    nome.on('blur', function () {
        $.ajax({
            url: "/pacientes/nome/" + nome.val(),
            type: "GET",
            success: function (dados) {
                let cadastrado = $('#cadastrado');
                let msg = $('#msg');
                if (dados.encontrado === true) {
                    cadastrado.prop('checked', true);
                    msg.attr('class', 'text-center alert alert-success');
                    msg.text('Paciente encontrado!');
                    msg.show();
                } else {
                    cadastrado.prop('checked', false);
                    msg.attr('class', 'text-center alert alert-danger');
                    msg.text('Paciente não cadastrado. Cadastrar!');
                    msg.show();
                }
            }
        });
    });

    $('#botao_agendar').on('click', function () {
        if ($('#cadastrado').prop('checked') !== true) {
            let msg = $('#msg');
            msg.text('Paciente não cadastrado. Cadastrar!');
            msg.show();
            return false
        }
    })
});