# -*- coding: utf-8 -*-
from unittest import TestCase
from carrera.job import Job
from carrera.steps.step import Step


class TestJob(TestCase):

    class TestStep(Step):
        pass

    def setUp(self):
        self.job = Job()

    def test_one_step_job(self):
        step = self.TestStep([], [])

        self.job.add_step(step)

        self.job.run()

    def test_two_step_job(self):
        step1 = self.TestStep([], [], name='step1')
        step2 = self.TestStep([], [], name='step2')

        self.job.add_step(step1)
        self.job.add_step(step2)

        self.job.run()
