#-*- coding:utf8
#author:fangshu.chang

"""
股票定投公式计算
"""
import math
import decimal

class Compute():
    def __init__(self):
        pass
    """
    计算当前月需要投入的资金
    """
    def curInvestFund(self, n, base, p, alt, stockPrice, marketValue):
        """
        n:定投第几次
        base:基准价格
        p:设定收益率
        alt:当月投入上限
        stockPrice:股价
        marketValue:已买股票市值
        """
        #amount = base * (1 + p) ** n
        amount = base * ((1 + p) ** n - 1)/p
        result = min((decimal.Decimal(amount) - marketValue), base * alt)
        num =  int(math.floor(result/(stockPrice * 100)))
        return int(num * stockPrice * 100), num
    def curInvestFundPe(self, n, base, p, pe1, pe2, stockPrice):
        """
        n:定投第几次
        base:基准价格
        p:设定收益率
        pe1:当前pe值
        pe2:参考pe值
        stockPrice:股价
        """
        num = int(base * (1 + p) ** n * pe1/pe2 /(stockPrice * 100))
        return int(num * stockPrice * 100), num
    def backTest(self, stockPriceList, base, alt = 5, p = 0.01, type = 0, pe1 = 0.0, pe2 =0.0):
        """
        stockPriceList:股价列表
        base:基准价格
        alt:当月投入上限
        p:设定收益率
        type:公式类型，0基本公式，1PE公式
        pe1:当前pe值
        pe2:参考pe值
        """
        result = []
        n = len(stockPriceList) - 1
        preAmount, preNum, outAmount = 0.0, 0, 0
        i = 1
        for sp in stockPriceList:
            if type ==0:
                curInvest, num = self.curInvestFund(i, base, p, alt, sp, preNum * sp * 100)
            else:
                curInvest, num = self.curInvestFundPe(i, base, p, pe1, pe2, sp)
            curNum = preNum + num
            if(curInvest < 0):
                curAmount = preAmount
                outAmount = outAmount - curInvest
            else:
                curAmount = preAmount + curInvest
            curIncome = int(curNum * sp * 100) + outAmount - curAmount
            curIncomeRate = round(float(curIncome)/curAmount, 2)
            result.append((curInvest, int(curNum * sp * 100), curAmount, curIncome, curIncomeRate, outAmount))
            i += 1
            preAmount, preNum = curAmount, curNum
        return result
        #当约投资额，股票市值, 总投入, 纯利润， 利润率， 卖出额
if __name__=="__main__":
    test = Compute()
    print test.backTest([1.1,1.3,1.4,1,0.9,2.3,2.4,2.7,3.6,0.8,0.1], 1000, p = 0.01, type = 1, pe1 = 3.4, pe2 = 2.7)
