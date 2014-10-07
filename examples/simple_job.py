from carrera.job import Job
from carrera.steps.step import Step


class InputStep(Step):
    def run(self):
        self.outputs = self.inputs
        return True


class ConvertStep(Step):
    def run(self):
        print self.outputs[0]
        return True


class OutputStep(Step):
    def run(self):
        print "lalala"
        return True


if __name__ == '__main__':
    step1 = '{"stepName": "examples.simple_job.InputStep", "outputs": ["out1"], "inputs": ["lalala"]}'
    step2 = '{"stepName": "examples.simple_job.ConvertStep", "inputs": ["out1"], "outputs": ["out2"]}'
    step3 = '{"stepName": "examples.simple_job.OutputStep", "inputs": ["out2"]}'

    job_desc = '{"job": {"steps": [%s, %s, %s]}}' % (step1, step2, step3)

    job = Job(job_desc)

    job.run()


