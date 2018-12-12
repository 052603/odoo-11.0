# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SpiderMovies(models.Model):
    _name = 'spider.movies'
    _rec_name = 'name'

    source = fields.Char(string='Source Url')
    name = fields.Char(string='Movie Name')
    url = fields.Char(string='Movie Url')
    description = fields.Text(string='描述')