#_______________________-TIEMPO-__________________________________#
class Tiempo:
    def min_hr(self,min):
        hr = min / 60
        return hr

    def min_s(self,min):
        s = min * 60
        return s

    def hr_min(self,hr):
        min = hr * 60
        return min

    def hr_s(self,hr):
        s = hr * 360
        return s

    def s_min(self,s):
        min = s / 60
        return min

    def s_hr(self,s):
        hr = s / 360
        return hr

#___________________-VELOCIDAD-_________________________________#

class Velocidad:
    def m_s__km_h(self,m_s):
        km_h = m_s * 3.6
        return km_h

    def km_h__m_s(self,km_h):
        m_s = km_h / 3.6
        return m_s