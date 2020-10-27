function pesqSus(sus) {
	if (sus !="") {
		$.get("dados?sus="+sus,
			function(dados,status){
				if (dados.encontrado == true) {
					document.getElementById('id_sus').onblur="";
					document.getElementById('id_nome').value=dados.nome;
					document.getElementById('id_mae').value=dados.mae;
					document.getElementById('id_nascimento').value=dados.nascimento;
					document.getElementById('id_familia').value=dados.familia;
					document.getElementById('id_observacao').value=dados.observacao;
				}
			}
		)
	}
}

function pesqNome(nome) {
	if (nome != "") {
		$.get("dados?nome="+nome,
			function(dados,status){
				if (dados.encontrado == true) {
					if (document.getElementById('id_sus').value == "") {
						document.getElementById('id_sus').value=dados.sus;
					}
					document.getElementById('id_nome').onblur="";
					document.getElementById('id_mae').value=dados.mae;
					document.getElementById('id_nascimento').value=dados.nascimento;
					document.getElementById('id_familia').value=dados.familia;
					document.getElementById('id_observacao').value=dados.observacao;
				}
			}
		)
	}
}

function inputTipo(tipo) {
	var input = document.getElementById('dado');
	switch (tipo) {
		case 'sus':
			if (input.type == "number" && input.max == "999999999999999") {
				return
			} else {
				input.setAttribute('type', "number");
				input.setAttribute('min', "100000000000000");
				input.setAttribute('max', "999999999999999");
			}
			break;
		case 'nome':
			input.removeAttribute('min');
			input.removeAttribute('max');
			input.setAttribute('type', "text");		
			break;
		case 'mae':
			input.removeAttribute('min');
			input.removeAttribute('max');
			input.setAttribute('type', "text");		
			break;
		case 'nascimento':
			input.removeAttribute('min');
			input.removeAttribute('max');
			input.setAttribute('type',"date");
			
			break;
		case 'familia':
			input.removeAttribute('min');
			input.setAttribute('type', "number");
			input.setAttribute('max', "999999");
			break;
	}
}

function tabelaTodos() {
	$.get(
		"tabela?"+$("#pesquisa").serialize(),
		function(pacientes,status) {
			var tabela = document.getElementById('corpoTabela');
			tabela.innerHTML = pacientes;
		}
	)
	return false
}

$(document).ready(
	function(){
		$("#pesquisa").submit(
			function() {
				$.get(
					"tabela?"+$("#pesquisa").serialize(),
					function(pacientes,status) {
						var tabela = document.getElementById('corpoTabela');
						tabela.innerHTML = pacientes;
					}
				)
				return false
			}
		)
	}
);	