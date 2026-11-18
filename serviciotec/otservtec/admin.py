from django.contrib import admin
from .models import Cliente, Tecnico, Zona, Estado, Equipo, OrdenTrabajo, Bateria, CambioBateria

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre_cliente', 'apellido_cli', 'email_cliente', 'telefono')
    search_fields = ('nombre_cliente', 'apellido_cli', 'email_cliente', 'telefono')


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('id_tecnico', 'nombre_tecnico', 'apellido_tec')
    search_fields = ('nombre_tecnico', 'apellido_tec')


@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('id_zona', 'zona')
    search_fields = ('zona',)


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id_estado', 'estado')
    search_fields = ('estado',)


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id_equipo', 'numero_serie', 'id_anam', 'marca', 'modelo')
    search_fields = ('numero_serie', 'id_anam', 'marca', 'modelo')


@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display = (
        'ot', 'get_cliente', 'get_equipo', 'get_zona',
        'get_tecnico', 'get_estado', 'fecha_ingreso',
        'fecha_termino', 'fecha_retiro'
    )
    list_filter = ('id_zona', 'id_estado', 'fecha_ingreso')
    search_fields = ('ot', 'observacion', 'diagnostico', 'materiales')

    def get_cliente(self, obj):
        return f"{obj.id_cliente.nombre_cliente} {obj.id_cliente.apellido_cli}"
    get_cliente.short_description = 'Cliente'

    def get_equipo(self, obj):
        return f"{obj.id_equipo.id_anam} "
    get_equipo.short_description = 'Equipo'

    def get_zona(self, obj):
        return obj.id_zona.zona if obj.id_zona else "-"
    get_zona.short_description = 'Zona'

    def get_tecnico(self, obj):
        return f"{obj.id_tecnico.nombre_tecnico} {obj.id_tecnico.apellido_tec}" if obj.id_tecnico else  "-"
    def get_estado(self, obj):
        return obj.id_estado.estado if obj.id_estado else "-"
    get_estado.short_description = 'Estado'

@admin.register(Bateria)
class BateriaAdmin(admin.ModelAdmin):
    list_display = ("id_bateria", "num_bateria", "marca", "modelo")
    search_fields = ("num_bateria", "marca", "modelo")

@admin.register(CambioBateria)
class CambioBateriaAdmin(admin.ModelAdmin):
    list_display = ("ot_bateria", "num_bateria", "id_cliente", "id_zona", "id_tecnico", "fecha_solicitud_bateria", "fecha_retiro_bateria")
    list_filter = ("id_zona", "id_tecnico")
    search_fields = ("num_bateria", "id_cliente__nombre_cliente")