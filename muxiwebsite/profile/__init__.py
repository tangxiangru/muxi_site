# coding: utf-8

from flask import Blueprint

profile = Blueprint(
    'profile',
    __name__,
    template_folder = 'templates',
    subdomain = 'profile',
    static_folder = 'static'
)

from . import views, forms

