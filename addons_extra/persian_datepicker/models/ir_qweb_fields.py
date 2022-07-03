# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import babel
import locale as _locale
import jdatetime
from persiantools import digits

from odoo import api, fields, models
from odoo.tools import posix_to_ldml, pycompat
from odoo.tools.misc import get_lang, babel_locale_parse


class DateConverter(models.AbstractModel):
    _inherit = 'ir.qweb.field.date'

    @api.model
    def value_to_html(self, value, options):
        front_lang = 'en_US'
        if 'template_options' in options:
            template_options = options['template_options']
            if template_options.get('lang'):
                front_lang = template_options.get('lang')

        if front_lang != 'fa_IR':
            return super(DateConverter, self).value_to_html(value, options)

        jformat = '%Y/%m/%d'
        _locale.setlocale(_locale.LC_ALL, jdatetime.FA_LOCALE)
        return jdatetime.date.fromgregorian(date=value).strftime(jformat)


class DateTimeConverter(models.AbstractModel):
    _inherit = 'ir.qweb.field.datetime'

    @api.model
    def value_to_html(self, value, options):
        if not value:
            return ''
        options = options or {}

        front_lang = 'en_US'
        if 'template_options' in options:
            template_options = options['template_options']
            if template_options.get('lang'):
                front_lang = template_options.get('lang')

        if front_lang != 'fa_IR':
            return super(DateTimeConverter, self).value_to_html(value, options)

        # ******************************************
        # Remove the following line
        # gd = super(DateTimeConverter, self).value_to_html(value, options)
        # ******************************************

        if options.get('time_only'):
            return digits.en_to_fa(super(DateTimeConverter, self).value_to_html(value, options))

        lang = self.user_lang()
        locale = babel_locale_parse(lang.code)
        format_func = babel.dates.format_datetime

        if isinstance(value, str):
            value = fields.Datetime.from_string(value)
        # value = fields.Datetime.context_timestamp(self, value)

        if 'format' in options:
            pattern = options['format']
        else:
            if options.get('time_only'):
                strftime_pattern = ("%s" % (lang.time_format))
            elif options.get('date_only'):
                strftime_pattern = ("%s" % (lang.date_format))
            else:
                strftime_pattern = ("%s %s" %
                                    (lang.date_format, lang.time_format))

            pattern = posix_to_ldml(strftime_pattern, locale=locale)

        if options.get('hide_seconds'):
            pattern = pattern.replace(":ss", "").replace(":s", "")

        if pattern == 'yyyy/MM/dd HH:mm:ss':
            jformat = '%Y/%m/%d %H:%M:%S'
        elif pattern == 'yyyy/MM/dd HH:mm':
            jformat = '%Y/%m/%d %H:%M'
        elif pattern == 'MMM d, yyyy':
            jformat = '%d %B %Y'
        elif pattern == 'd MMMM, yyyy':
            jformat = '%d %B %Y'
        elif pattern == 'MMM yyyy':
            jformat = '%B %Y'
        elif pattern == 'short':
            jformat = '%y/%m/%d'
        elif pattern == 'long':
            jformat = '%d %B %Y'
        elif pattern == 'LLL':
            jformat = '%b'
        elif pattern == 'EEEE':
            jformat = '%A'
        elif pattern == 'dd':
            jformat = '%d'
        else:
            jformat = '%Y/%m/%d'

        _locale.setlocale(_locale.LC_ALL, jdatetime.FA_LOCALE)
        jd = jdatetime.datetime.fromgregorian(datetime=value).strftime(jformat)
        return digits.en_to_fa(jd)
