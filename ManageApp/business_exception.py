# -*- coding: utf-8 -*-
class BusinessException(Exception):

    def __init__(self, code=9999, message=u'未知错误'):
        super(Exception, self).__init__()
        self.code = code
        self.message = message

    def __repr__(self):
        return '<%(cls)s code=%(code)d, "%(message)s">' % {
            'cls': self.__class__.__name__,
            'code': self.code,
            'message': self.message}