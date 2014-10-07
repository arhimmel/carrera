# -*- coding: utf-8 -*-


class Job(object):
    def __init__(self, job_description):
        self.job_description = job_description
        self.steps = self._populate_steps()

    def _populate_steps(self):
        import json
        import importlib

        try:
            json_description = json.loads(self.job_description)
        except ValueError as e:
            print "check job config: %s" % e.message
            raise e

        steps = []

        for str_step in json_description.get('job').get('steps'):
            names = str_step.get('stepName').split('.')

            inputs = str_step.get('inputs')
            outputs = str_step.get('outputs')

            step_name = names[-1]
            path = str.join('.', names[:-1])

            module = importlib.import_module(path)

            steps.append(getattr(module, step_name)(inputs=inputs, outputs=outputs))

            # somehow import the class we want and load it
            # print step_name

        return steps

    def _add_step(self, step):
        self.steps.append(step)

    def run(self):
        for step in self.steps:
            try:
                # print "running {}".format(step.name)
                succeeded = step.run()
                if not succeeded:
                    raise StepFailedException
            except Exception as e:
                print e.message
                return 1
            finally:
                # should exit, maybe roll back jobs
                pass


class StepFailedException(Exception):
    pass
