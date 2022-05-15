from statistics import stdev
import math
import matplotlib.pyplot as plt
import numpy as np

# Input your datas
ls_x = [0, 5, 10, 12, 13, 14, 15, 16, 17, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
ls_y = [19.75, 43, 54, 58.7, 61.4, 64.6, 66.9, 68.3, 69.1, 69.3, 69.1, 69.2, 69.1, 69.1, 69, 69, 68, 68, 66, 65, 65, 64, 63, 62, 61.3, 60, 60]


class LinearRegression():
    def __init__(self, ls_x, ls_y, predictval):
        self.ls_x = ls_x
        self.ls_y = ls_y
        self.predictval = predictval
        self.xsubmeanx = []
        self.xsubmeanx2 = []
        self.ysubmeany = []
        self.ysubmeany2 = []
        self.xsmx_m_ysmy = []
        self.sum_xmy = 0
        self.sumxm2 = 0
        self.sumym2 = 0


    def CorrelationCoefficient(self):

        def Mean(ls):
            k = 0
            for i in range(len(ls)):
                k += ls[i]
            n = len(ls)
            mean = float(k / n)
            return mean

        mean_x = Mean(self.ls_x)
        mean_y = Mean(self.ls_y)


        for i in range(len(self.ls_x)):
            self.xsubmeanx.append(round((self.ls_x[i] - mean_x), 3))
            self.xsubmeanx2.append(round((float(self.ls_x[i] - mean_x) ** 2), 3))

        for i in range(len(self.ls_y)):
            self.ysubmeany.append(round((self.ls_y[i] - mean_y), 3))
            self.ysubmeany2.append(round((float(self.ls_y[i] - mean_y) ** 2), 3))

        for i in range(len(self.xsubmeanx)):
            self.xsmx_m_ysmy.append(round((float(self.xsubmeanx[i] * self.ysubmeany[i])), 3))

        for i in range(len(self.xsmx_m_ysmy)):
            self.sum_xmy += (self.xsmx_m_ysmy[i])

        for i in range(len(self.xsubmeanx2)):
            self.sumxm2 += (self.xsubmeanx2[i])

        for i in range(len(self.ysubmeany2)):
            self.sumym2 += (self.ysubmeany2[i])


        correlation_coefficient = round((float(self.sum_xmy) / float(math.sqrt(float(self.sumxm2 * self.sumym2)))), 3)

        return correlation_coefficient

    def slope_b(self):
        slp1 = stdev(self.ls_y)/stdev(self.ls_x)
        b = LinearRegression(self.ls_x, self.ls_y, self.predictval).CorrelationCoefficient() * slp1
        return round(b, 3)

    def intercept_a(self):
        b = LinearRegression(self.ls_x, self.ls_y, self.predictval).slope_b()
        def Mean(ls):
            k = 0
            for i in range(len(ls)):
                k += ls[i]
            n = len(ls)
            mean = float(k / n)
            return mean

        mean_x = Mean(self.ls_x)
        mean_y = Mean(self.ls_y)
        a = mean_y - float(b * mean_x)

        return round(a, 3)

    def equation(self):
        return (f"y = {LinearRegression(ls_x, ls_y, self.predictval).intercept_a()} + {LinearRegression(ls_x, ls_y, self.predictval).slope_b()}x")

    def predict(self):
        a = LinearRegression(self.ls_x, self.ls_y, self.predictval).intercept_a()
        b = LinearRegression(self.ls_x, self.ls_y, self.predictval).slope_b()
        y = a + float(b * self.predictval)
        return round(y, 3)

    def plot(self):
        b = LinearRegression(ls_x, ls_y, self.predictval).slope_b()
        a = LinearRegression(ls_x, ls_y, self.predictval).intercept_a()
        x = np.linspace(0, 100)
        y = LinearRegression(ls_x, ls_y, self.predictval).predict()
        plt.scatter(self.ls_x, self.ls_y)
        plt.plot(x, b*x+a, '-r', linestyle='solid')
        plt.plot(float(self.predictval), y, 'go')
        plt.xlabel('Age', color='#1C2833')
        plt.ylabel('Height', color='#1C2833')
        plt.legend("Scattered")
        plt.title("Chart")
        plt.show()


#                                                      |
#                                         Enter the x  V
studentlinearregression = LinearRegression(ls_x, ls_y, 60)
print('y = ' + str(studentlinearregression.predict()))
print('correlation_coefficient = ' + str(studentlinearregression.CorrelationCoefficient()))
studentlinearregression.plot()
