#  * To change this license header, choose License Headers in Project Properties.
#  * To change this template file, choose Tools | Templates
#  * and open the template in the editor.
#
# package: com.speakliz.audiocapturespeaklizsoundenv
#
#  *
#  * @author speakliz
#
import math

class RealTimeFFT(object):
    n = int()
    m = int()
     #  Lookup tables. Only need to recompute when size of FFT changes.
    cos = []
    sin = []
    window = []
    x = []
    y = []
    def __init__(self, nl):
        #         double exp = floor(log(nl) / log(2));
        #         double l = pow(2,exp);
        #
        #         this.n = (int)l;
        #         this.m = (int) (log(n) / log(2));
        self.n = nl
        self.m = int((math.log(self.n) / math.log(2)))
        #  Make sure n is a power of 2
        if self.n != (1 << self.m):
            raise RuntimeException("FFT length must be power of 2")
        #  precompute tables
        self.cos = [None] * int(self.n / 2)
        self.sin = [None] * int(self.n / 2)
        i = 0
        while i < self.n / 2:
            self.cos[i] = math.cos(-2 * math.pi * i / self.n)
            self.sin[i] = math.sin(-2 * math.pi * i / self.n)
            i += 1
        #makeWindow()
        self.window = [None] * int(self.n)
        i = 0
        while i < len(self.window):
            self.window[i] = 0.42 - 0.5 * math.cos(2 * math.pi * i / (self.n - 1)) + 0.08 * math.cos(4 * math.pi * i / (self.n - 1))
            i += 1
        #makeWindow

        self.x = [None] * self.n
        self.y = [None] * self.n

    def makeWindow(self):
        #  Make a blackman window:
        #  w(n)=0.42-0.5cos{(2*PI*n)/(N-1)}+0.08cos{(4*PI*n)/(N-1)};
        self.window = [None] * self.n
        i = 0
        while len(self.window):
            self.window[i] = 0.42 - 0.5 * math.cos(2 * math.pi * i / (self.n - 1)) + 0.08 * math.cos(4 * math.pi * i / (self.n - 1))
            i += 1

    def getWindow(self):
        return self.window

    def fft(self, in_):
        x = in_
        y = [0.0] * self.n                  # float, so 0.0 or 0 instead of None
        i = int()
        j = int()
        k = int()
        n1 = int()
        n2 = int()
        a = int()
        c = float()
        s = float()
        t1 = float()
        t2 = float()
        #  Bit-reverse
        j = 0
        n2 = self.n / 2
        while i < self.n - 1:
            n1 = n2
            while j >= n1:
                j = j - n1
                n1 = n1 / 2
            j = j + n1
            if i < j:
                t1 = self.x[i]
                self.x[i] = self.x[j]
                self.x[j] = t1
                t1 = self.y[i]
                self.y[i] = self.y[j]
                self.y[j] = t1
            i += 1
        #  FFT
        n1 = 0
        n2 = 1
        while i < self.m:
            n1 = n2
            n2 = n2 + n2
            a = 0
            while j < n1:
                c = self.cos[a]
                s = self.sin[a]
                a += 1 << (self.m - i - 1)
                while k < self.n:
                    t1 = c * self.x[k + n1] - s * self.y[k + n1]
                    t2 = s * self.x[k + n1] + c * self.y[k + n1]
                    self.x[k + n1] = self.x[k] - t1
                    self.y[k + n1] = self.y[k] - t2
                    self.x[k] = self.x[k] + t1
                    self.y[k] = self.y[k] + t2
                    k = k + n2
                j += 1
            i += 1
        out = [None] * (self.n / 2)
        o = 0
        while o < len(out):
            out[o] = (math.hypot(x[o], y[o]) / (self.n / 2))
            #             out[o] = 10 * log10( pow(x[o],2) + pow(y[o],2));
            o += 1
        #         System.out.print("Re: [");
        #         for (int o = 0; o < x.length; o++) {
        #             System.out.print(((int) (x[o] * 1000) / 1000.0) + " ");
        #         }
        #
        #         System.out.print("]\nIm: [");
        #         for (int o = 0; o < y.length; o++) {
        #             System.out.print(((int) (y[o] * 1000) / 1000.0) + " ");
        #         }
        #
        #
        #          System.out.print("]\nAbs: [");
        #         for (int o = 0; o < y.length; o++) {
        #             System.out.print(((int) (out[o] * 1000) / 1000.0) + " ");
        #         }
        #
        #         print("]");
        return out

#Exm
#object = RealTimeFFT(8)
#res = object.fft([1.5,2.1,3.9,4.0])
#print(res)
