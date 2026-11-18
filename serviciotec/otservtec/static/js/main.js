$(document).ready(function() {
    // Activa Select2 en el campo de equipo
    $('#id_equipo').select2({
        placeholder: "Escribe para buscar un equipo...",
        allowClear: true,
        width: '100%'
    });

    // También puedes activar en cliente y técnico
    $('#id_cliente').select2({
        placeholder: "Buscar cliente...",
        allowClear: true,
        width: '100%'
    });

    $('#id_tecnico').select2({
        placeholder: "Buscar técnico...",
        allowClear: true,
        width: '100%'
    });

    $('.select2').select2({
        width: '100%'
    });
});
