$(document).ready(function () {
    $('#tipo').on('change', function () {
        let tipo = this.value;
        let input = $('#dado');

        $('#lb_dado').text($('#tipo option:selected').text());

        if (tipo === 'sus' || tipo === 'familia') {
            input.attr('type', "number");
        } else if (tipo === 'nascimento') {
            input.attr('type', "date");
        } else {
            input.attr('type', "text");
        }
    });
});