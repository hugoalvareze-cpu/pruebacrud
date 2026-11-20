from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from .models import (
    Cliente, Tecnico, Zona, Estado, Equipo, 
    OrdenTrabajo, Bateria, CambioBateria
)

# ==========================================
# 1. RECURSOS DE IMPORTACIÓN / EXPORTACIÓN
# ==========================================

class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        import_id_fields = ('id_cliente',)
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

# Resource para OrdenTrabajo mapeando claves foráneas y la clave primaria 'ot'
class OrdenTrabajoResource(resources.ModelResource):
    id_cliente = fields.Field(
        column_name='id_cliente',
        attribute='id_cliente',
        widget=ForeignKeyWidget(Cliente, 'id_cliente')
    )
    id_equipo = fields.Field(
        column_name='id_equipo',
        attribute='id_equipo',
        widget=ForeignKeyWidget(Equipo, 'id_equipo')
    )
    id_zona = fields.Field(
        column_name='id_zona',
        attribute='id_zona',
        widget=ForeignKeyWidget(Zona, 'id_zona')
    )
    id_tecnico = fields.Field(
        column_name='id_tecnico',
        attribute='id_tecnico',
        widget=ForeignKeyWidget(Tecnico, 'id_tecnico')
    )
    id_estado = fields.Field(
        column_name='id_estado',
        attribute='id_estado',
        widget=ForeignKeyWidget(Estado, 'id_estado')
    )

    class Meta:
        model = OrdenTrabajo
        import_id_fields = ('ot',)  # 👈 Define 'ot' como la clave primaria
        fields = (
            'ot', 'id_cliente', 'id_equipo', 'id_zona', 'id_tecnico', 
            'id_estado', 'observacion', 'diagnostico', 'materiales', 
            'info_retiro', 'fecha_ingreso', 'fecha_termino', 'fecha_retiro'
        )

# ==========================================
# 2. REGISTRO DE MODELOS EN EL ADMIN
# ==========================================

@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(ImportExportModelAdmin):
    resource_classes = [OrdenTrabajoResource]  # 👈 Asigna el recurso de importación
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