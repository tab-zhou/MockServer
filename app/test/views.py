# coding:utf-8
from app.test import test
from flask import jsonify, request
# 请求方式错误
method_err = {
    "code": 301,
    "msg": u"请求方式错误，只支持POST请求"
}
# 参数错误
param_err = {
    "code": 302,
    "msg": u"请求参数错误，请检查入参"
}
# 成功信息
success_msg = {
    "code": 200,
    "msg": u"调用成功"
}
@test.route('/testid', methods=['POST', 'GET'])
def testid():
    if request.method != 'POST':
        return jsonify(method_err)
    else:
        user_id = request.values.get("user_id")
        if user_id:
            return jsonify(success_msg)
        else:
            return jsonify(param_err)