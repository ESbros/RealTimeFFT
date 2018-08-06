#  * To change this license header, choose License Headers in Project Properties.
#  * To change this template file, choose Tools | Templates
#  * and open the template in the editor.
#  
# package: com.speakliz.audiocapturespeaklizsoundenv
#
#  *
#  * @author speakliz
#
class RealTimeFFT(object):
    """ generated source for class RealTimeFFT """
    n = int()
    m = int()

    #  Lookup tables. Only need to recompute when size of FFT changes.
    cos = []
    sin = []
    window = []
    x = []
    y = []

    def __init__(self, nl):
        """ generated source for method __init__ """
        #         double exp = floor(log(nl) / log(2));
        #         double l = pow(2,exp);
        #
        #         this.n = (int)l;
        #         this.m = (int) (log(n) / log(2));
        self.n = nl
        self.m = int((log(self.n) / log(2)))
        #  Make sure n is a power of 2
        if self.n != (1 << self.m):
            raise RuntimeException("FFT length must be power of 2")
        #  precompute tables
        self.cos = [None] * n / 2
        self.sin = [None] * n / 2
        i = 0
        while i < self.n / 2:
            self.cos[i] = cos(-2 * PI * i / self.n)
            self.sin[i] = sin(-2 * PI * i / self.n)
            i += 1
        makeWindow()
        self.x = [None] * n
        self.y = [None] * n

    def makeWindow(self):
        """ generated source for method makeWindow """
        #  Make a blackman window:
        #  w(n)=0.42-0.5cos{(2*PI*n)/(N-1)}+0.08cos{(4*PI*n)/(N-1)};
        self.window = [None] * n
        i = 0
        while len(window):
            self.window[i] = 0.42 - 0.5 * cos(2 * PI * i / (self.n - 1)) + 0.08 * cos(4 * PI * i / (self.n - 1))
            i += 1

    def getWindow(self):
        """ generated source for method getWindow """
        return self.window

    def fft(self, in_):
        """ generated source for method fft """
        self.x = in_
        self.y = [None] * n
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
        out = [None] * n / 2
        o = 0
        while o < self.n / 2:
            out[o] = (hypot(self.x[o], self.y[o]) / (self.n / 2))
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
