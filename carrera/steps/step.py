# -*- coding: utf-8 -*-


class Step(object):
    """
    Base step definition for all steps
    """
    def __init__(self, inputs=None, outputs=None, name=None):
        if not name:
            self.name = self.__class__.__name__
        else:
            self.name = name

        self.inputs = inputs
        self.outputs = outputs

    def __repr__(self):
        return "%s".format(self.name)

    def run(self):
        """
        Override this method for custom Steps
        :return: True if successful else False
        """
        return True
