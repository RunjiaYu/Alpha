#!/usr/bin/env Python
# 思路： rank((X - Y)) / rank((X + Y)))
# -*- coding:utf-8 -*-
# author: gejf
#Alpha#41: (((high * low)^0.5) - vwap)

import time

import numpy as np
import pandas as pd
import math
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t


class Factor(FactorBase):

    def __init__(self):
        super(Factor, self).__init__()
        self.neutral = True
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.VWAP, t.OPERREVLYR]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData  # 计算所需数据

        adjX = needData[t.VWAP]
        adjY = needData[t.OPERREVLYR]
        factor = -1 * ((adjX * adjY) ** 0.5 - self.calculator.Wma((adjX + adjY) / 2, 2))
        #factor = self.calculator.Decaylinear(result,2)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()


fct = Factor()
fct.run_factor()