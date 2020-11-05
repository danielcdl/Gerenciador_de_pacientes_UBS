$(document).ready(function () {
    let nome = $('#id_nome');
    nome.keyup(function () {
        if (this.value.length > 2) {
            $.ajax({
                url: "autocomplete/",
                type: "GET",
                data: $(this).serialize(),
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
            url: "busca/",
            type: "GET",
            data: $(this).serialize(),
            success: function (dados) {
                let cadastrado = $('#cadastrado');
                let msg = $('#msg');
                if (dados.encontrado === true) {
                    cadastrado.attr('checked', 'checked');
                    $('#id_profissional').removeAttr('disabled');
                    $('#id_data').removeAttr('disabled');
                    $('#id_turno').removeAttr('disabled');
                    msg.attr('class', 'text-center alert alert-success');
                    msg.text('Paciente encontrado!');
                    msg.show();
                } else {
                    cadastrado.removeAttr('value');
                    msg.text('Paciente não cadastrado. Cadastrar!');
                    msg.show();
                }
            }
        });
    });

    $('#id_data').on('click', function () {
        let data = new Date;

        $.ajax({
            url: 'calendario/',
            type: 'GET',
            data: 'mes='+ (data.getMonth() + 1) +'&ano=' + data.getFullYear(),
            success: function (tabela) {
                $('#calendario').html(tabela);
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