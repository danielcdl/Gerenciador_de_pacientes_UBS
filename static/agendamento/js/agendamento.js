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
                if (dados.encontrado === true) {
                    console.log('encontrado');
                    cadastrado.attr('checked', 'checked');
                    $('#id_profissional').removeAttr('disabled');
                    $('#id_data').removeAttr('disabled');
                    $('#id_turno').removeAttr('disabled');
                } else {
                    cadastrado.removeAttr('checked');
                }
            }
        });
    })
});