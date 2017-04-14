#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''


import config_default

class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override):     # 整合两个字典
    r = {}
    for k, v in defaults.items():
        if k in override:         
            r[k] = override[k]	# 如果两个字典中有key相同，则用override中的value覆盖defaults中的value
        else:
            r[k] = v
    return r

def toDict(d):	# 将dict类型的参数转换为自定义的 Dict 类型，这样就可以通过 x.y 的方式来使用参数
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)