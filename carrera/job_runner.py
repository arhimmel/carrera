# -*- coding: utf-8 -*-


class JobRunnerParams(object):
    """
    Class to parse and hold parameters for the job runner
    """
    def __init__(self, sys_params):
        self.inputs = sys_params


class JobRunner(object):
    """
    Class that will create the Job object and make it run
    """
    def __init__(self, params):
        self.params = params

    def run(self):
        pass

if __name__ == '__main__':
    import sys

    JobRunner(JobRunnerParams(sys.argv)).run()
