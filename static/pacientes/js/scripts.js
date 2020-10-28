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
