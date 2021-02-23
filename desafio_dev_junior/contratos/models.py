from django.db import models
from django.utils.translation import ugettext_lazy as _
from localflavor.br.models import BRCNPJField, BRPostalCodeField


class Empresa(models.Model):
    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    razao_social = models.CharField(_("Razão Social"), max_length=50)

    cnpj = BRCNPJField(_("CNPJ"))

    end_cep = BRPostalCodeField(_("CEP"))

    end_logradouro = models.CharField(_("Logradouro"), max_length=250)

    end_numero = models.CharField(_("Número"), max_length=50)

    end_bairro = models.CharField(_("Bairro"), max_length=50)

    telefone = models.CharField(_("Telefone"), max_length=50)

    def __str__(self):
        return f"{self.razao_social} ({self.cnpj})"


class TipoContrato(models.IntegerChoices):
    EMPRÉSTIMOS = 1, _("Empréstimos")
    ARRENDAMENTO = 2, _("Arrendamento")
    SEGURO = 3, _("Seguro")
    LOCAÇÃO_DE_SERVIÇOS = 4, _("Locação de Serviços")
    EQUIPAMENTOS = 5, _("Equipamentos")


class Contrato(models.Model):
    class Meta:
        verbose_name = _("contrato")
        verbose_name_plural = _("contratos")

    class Status(models.TextChoices):
        EM_EDIÇÃO = "E", _("Em Edição")
        ATIVO = "A", _("Ativo")
        CANCELADO = "C", _("Cancelado")

    contratante = models.ForeignKey(
        "contratos.Empresa",
        verbose_name=_("Contratante"),
        on_delete=models.PROTECT,
        related_name="empresa_contratante",
    )

    contratada = models.ForeignKey(
        "contratos.Empresa",
        verbose_name=_("Contratada"),
        on_delete=models.PROTECT,
        related_name="empresa_contratada",
    )

    objeto = models.TextField(_("Objeto"))

    tipo = models.PositiveSmallIntegerField(_("tipo"), choices=TipoContrato.choices)

    carencia = models.BooleanField(_("Carência"))

    dt_inicio_vigencia = models.DateField(
        _("Dt. Inicio Vigência"), auto_now=False, auto_now_add=False
    )

    dt_fim_vigencia = models.DateField(
        _("Dt. Fim Vigência"), auto_now=False, auto_now_add=False
    )

    status = models.CharField(
        _("Status"), max_length=1, choices=Status.choices, default=Status.EM_EDIÇÃO
    )

    valores = models.TextField(_("Valores"))

    prazos = models.TextField(_("Prazos"))

    def __str__(self):
        seq = str(self.pk).zfill(4)
        return f"{self.get_tipo_display()} ({seq})"
