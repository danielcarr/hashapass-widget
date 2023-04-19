import base64
import hmac


def generate(parameter, password, length):
    key = password.encode('utf-8')
    parameter_bytes = parameter.encode('utf-8')
    digest = hmac.new(key, parameter_bytes, digestmod='sha1').digest()
    return base64.b64encode(digest)[:length].decode('utf-8')
