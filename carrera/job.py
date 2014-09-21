# -*- coding: utf-8 -*-


class JobRunner(object):
    pass


class Job(object):
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run(self):
        for step in self.steps:
            try:
                print "running {}".format(step.name)
                step()
            except Exception as e:
                pass
            finally:
                # should exit maybe roll back jobs
                pass
