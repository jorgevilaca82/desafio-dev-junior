from django.contrib import admin

from .models import Contrato, Empresa


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    search_fields = (
        "tipo",
        "contratante__razao_social",
        "contratada__razao_social",
        "status",
    )
    autocomplete_fields = ("contratante", "contratada")
    list_display = ("tipo", "contratante", "contratada", "status")


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    search_fields = ("razao_social", "cnpj")
    list_display = ("razao_social", "cnpj", "telefone")
