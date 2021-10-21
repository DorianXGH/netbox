from django import forms
from django.utils.translation import gettext as _

from dcim.choices import LinkStatusChoices
from extras.forms import CustomFieldModelFilterForm
from utilities.forms import (
    add_blank_choice, BootstrapMixin, DynamicModelMultipleChoiceField, StaticSelect, TagFilterField,
)
from wireless.choices import *
from wireless.models import *

__all__ = (
    'WirelessLANFilterForm',
    'WirelessLANGroupFilterForm',
    'WirelessLinkFilterForm',
)


class WirelessLANGroupFilterForm(BootstrapMixin, CustomFieldModelFilterForm):
    model = WirelessLANGroup
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('All Fields')}),
        label=_('Search')
    )
    parent_id = DynamicModelMultipleChoiceField(
        queryset=WirelessLANGroup.objects.all(),
        required=False,
        label=_('Parent group'),
        fetch_trigger='open'
    )
    tag = TagFilterField(model)


class WirelessLANFilterForm(BootstrapMixin, CustomFieldModelFilterForm):
    model = WirelessLAN
    field_groups = [
        ('q', 'tag'),
        ('group_id',),
    ]
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('All Fields')}),
        label=_('Search')
    )
    ssid = forms.CharField(
        required=False,
        label='SSID'
    )
    group_id = DynamicModelMultipleChoiceField(
        queryset=WirelessLANGroup.objects.all(),
        required=False,
        null_option='None',
        label=_('Group'),
        fetch_trigger='open'
    )
    auth_type = forms.ChoiceField(
        required=False,
        choices=add_blank_choice(WirelessAuthTypeChoices),
        widget=StaticSelect()
    )
    auth_cipher = forms.ChoiceField(
        required=False,
        choices=add_blank_choice(WirelessAuthCipherChoices),
        widget=StaticSelect()
    )
    auth_psk = forms.CharField(
        required=False
    )
    tag = TagFilterField(model)


class WirelessLinkFilterForm(BootstrapMixin, CustomFieldModelFilterForm):
    model = WirelessLink
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('All Fields')}),
        label=_('Search')
    )
    ssid = forms.CharField(
        required=False,
        label='SSID'
    )
    status = forms.ChoiceField(
        required=False,
        choices=add_blank_choice(LinkStatusChoices),
        widget=StaticSelect()
    )
    auth_type = forms.ChoiceField(
        required=False,
        choices=add_blank_choice(WirelessAuthTypeChoices),
        widget=StaticSelect()
    )
    auth_cipher = forms.ChoiceField(
        required=False,
        choices=add_blank_choice(WirelessAuthCipherChoices),
        widget=StaticSelect()
    )
    auth_psk = forms.CharField(
        required=False
    )
    tag = TagFilterField(model)
