from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin  # 👈 Importar la clase
from .models import Cliente, Tecnico, Zona, Estado, Equipo, OrdenTrabajo, Bateria, CambioBateria

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):  # 👈 Cambiar admin.ModelAdmin por ImportExportModelAdmin
    list_display = ('id_cliente', 'nombre_cliente', 'apellido_cli', 'email_cliente', 'telefono')
    search_fields = ('nombre_cliente', 'apellido_cli', 'email_cliente', 'telefono')

@admin.register(Tecnico)
class TecnicoAdmin(ImportExportModelAdmin):
    list_display = ('id_tecnico', 'nombre_tecnico', 'apellido_tec')
    search_fields = ('nombre_tecnico', 'apellido_tec')

@admin.register(Zona)
class ZonaAdmin(ImportExportModelAdmin):
    list_display = ('id_zona', 'zona')
    search_fields = ('zona',)

@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin):
    list_display = ('id_estado', 'estado')
    search_fields = ('estado',)

@admin.register(Equipo)
class EquipoAdmin(ImportExportModelAdmin):  # 👈 Cambiar admin.ModelAdmin por ImportExportModelAdmin
    list_display = ('id_equipo', 'numero_serie', 'id_anam', 'marca', 'modelo')
    search_fields = ('numero_serie', 'id_anam', 'marca', 'modelo')

@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(ImportExportModelAdmin):  # 👈 Cambiar admin.ModelAdmin por ImportExportModelAdmin
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
        return f"{obj.id_equipo.id_anam}"
    get_equipo.short_description = 'Equipo'

    def get_zona(self, obj):
        return obj.id_zona.zona if obj.id_zona else "-"
    get_zona.short_description = 'Zona'

    def get_tecnico(self, obj):
        return f"{obj.id_tecnico.nombre_tecnico} {obj.id_tecnico.apellido_tec}" if obj.id_tecnico else "-"
    get_tecnico.short_description = 'Técnico'

    def get_estado(self, obj):
        return obj.id_estado.estado if obj.id_estado else "-"
    get_estado.short_description = 'Estado'

@admin.register(Bateria)
class BateriaAdmin(ImportExportModelAdmin):  # 👈 Cambiar admin.ModelAdmin por ImportExportModelAdmin
    list_display = ("id_bateria", "num_bateria", "marca", "modelo")
    search_fields = ("num_bateria", "marca", "modelo")

@admin.register(CambioBateria)
class CambioBateriaAdmin(ImportExportModelAdmin):
    list_display = ("ot_bateria", "num_bateria", "id_cliente", "id_zona", "id_tecnico", "fecha_solicitud_bateria", "fecha_retiro_bateria")
    list_filter = ("id_zona", "id_tecnico")
    search_fields = ("num_bateria", "id_cliente__nombre_cliente")

# 1. Definir Resources especificando import_id_fields
class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        import_id_fields = ('id_cliente',)  # 👈 Le indica a import-export usar id_cliente
        fields = ('id_cliente', 'nombre_cliente', 'apellido_cli', 'email_cliente', 'telefono')

class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo
        import_id_fields = ('id_equipo',)
        fields = ('id_equipo', 'numero_serie', 'id_anam', 'marca', 'modelo', 'descripcion')

class BateriaResource(resources.ModelResource):
    class Meta:
        model = Bateria
        import_id_fields = ('id_bateria',)
        fields = ('id_bateria', 'num_bateria', 'marca', 'modelo', 'descripcion')

# 2. Vincular los Resources en el Admin mediante resource_classes
@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):
    resource_classes = [ClienteResource]  # 👈 Vinculación aquí
    list_display = ('id_cliente', 'nombre_cliente', 'apellido_cli', 'email_cliente', 'telefono')
    search_fields = ('nombre_cliente', 'apellido_cli', 'email_cliente', 'telefono')

@admin.register(Equipo)
class EquipoAdmin(ImportExportModelAdmin):
    resource_classes = [EquipoResource]
    list_display = ('id_equipo', 'numero_serie', 'id_anam', 'marca', 'modelo')
    search_fields = ('numero_serie', 'id_anam', 'marca', 'modelo')

@admin.register(Bateria)
class BateriaAdmin(ImportExportModelAdmin):
    resource_classes = [BateriaResource]
    list_display = ("id_bateria", "num_bateria", "marca", "modelo")
    search_fields = ("num_bateria", "marca", "modelo")

# (Mantener los demás modelos como Tecnico, Zona, Estado, OrdenTrabajo, etc.)