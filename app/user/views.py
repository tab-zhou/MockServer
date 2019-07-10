# coding: utf-8
from app.user import user
from flask import jsonify
import json
user_data = [
    {
        'id': 1,
        'name': '张三'
    },
    {
        'id': 2,
        'name': '李四'
    }
]


@user.route('/<int:id>', methods=['GET', ])
def get(id):
    for user in user_data:
        if user['id'] == id:
            return jsonify(code=200, user=user)
