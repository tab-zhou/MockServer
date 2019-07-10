# coding:utf-8
from flask import Blueprint
test = Blueprint('test', __name__,)
from app.test import views
