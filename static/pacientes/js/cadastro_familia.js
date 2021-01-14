$(document).ready(function () {
    $('#id_familia').on('change', function () {
        $.ajax({
            url: "/pacientes/familia/" + $(this).val(),
            type: "GET",
            success: function (dados) {
                if (dados.encontrado === true) {
                    $('#id_chave').val(dados.id)
                    $('#id_tipo_logradouro').val(dados.tipo_logradouro);
                    $('#id_nome_logradouro').val(dados.nome_logradouro);
                    $('#id_numero').val(dados.numero);
                    $('#id_bairro').val(dados.bairro);
                    $('#id_complemento').val(dados.complemento);
                    $('#id_cidade').val(dados.cidade);
                    $('#botao').text('ATUALIZAR');
                }
            }
        })
    });

    $('#reset').on('click', function () {
        $('#botao').text('CADASTRAR');
    })
});
