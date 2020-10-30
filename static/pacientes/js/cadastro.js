$(document).ready(function () {
	$('#sus').on('blur',function () {
		if (this.value) {
			$.ajax({
				url: "dados/",
				type: "GET",
				data: $(this).serialize(),
				success: function (dados) {
					if (dados.encontrado === true) {
					    let botao = $('#botao');
						$('#nome').val(dados.nome);
						$('#mae').val(dados.mae);
						$('#nascimento').val(dados.nascimento);
						$('#familia').val(dados.familia);
						$('#observacao').val(dados.observacao);
						$('#sus_encontrado').attr('value', 'encontrado');
						let msg = $('#msg');
						msg.attr('class', 'alert alert-success');
						msg.text('Paciente encontrado!');
						msg.show();
                        botao.text('ATUALIZAR');
                        botao.show();
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

	$('#nome').on('blur',function () {
		if (this.value != '' && $('#sus_encontrado').val() !== 'encontrado') {
			$.ajax({
				url: "dados/",
				type: "GET",
				data: $(this).serialize(),
				success: function (dados) {
				    let botao = $('#botao');
					if (dados.encontrado === true) {
						let sus = $('#sus');
						if (sus !== dados.sus){
							sus.val(dados.sus);
						}
						$('#mae').val(dados.mae);
						$('#nascimento').val(dados.nascimento);
						$('#familia').val(dados.familia);
						$('#observacao').val(dados.observacao);
						botao.text('ATUALIZAR');
					} else {
					    botao.text('CADASTRAR');
                    }
					let msg = $('#msg');
					msg.attr('class', 'alert alert-success')
					msg.text('Paciente encontrado!');
					msg.show();
					botao.show();
				},
				error: function (request, status, error) {
					let msg = $('#msg');
					msg.text(error + '. Tente Novamente');
					msg.show();
				}
			});
		}
	})
});
