from enum import Enum

class aggregationTypes(Enum):
        ORTALAMA ='avg'
        EN_DUSUK ='min'
        EN_YUKSEK ='max' 
        BASLANGIC ='first'
        BITIS ='last' 
        KUMULATIF ='sum' 
 
 
class formulas(Enum):
        DUZEY =	0
        YUZDE_DEGISIM =1
        FARK =	2
        YILLIK_YUZDE_DEGISIM =	3
        YILLIK_FARK =	4
        BIR_ONCEKI_YILIN_SONUNA_GORE_YUZDE_DEGISIM =	5
        BIR_ONCEKI_YILIN_SONUNA_GORE_FARK = 6
        HARAKETLI_ORTALAMA  =	7
        HARAKETLI_TOPLAM =	8
 
class frequency(Enum):
        GUNLUK = 1
        ISGUNU = 2
        HAFTALIK = 3
        AYDA_2_KEZ = 4
        AYLIK =	5
        AYLIK_3 = 6
        AYLIK_6 = 7
        YILLIK = 8
 
class series(Enum):
        USD_ALIS = 'TP.DK.USD.A.YTL'
        EURO_ALIS = 'TP.DK.EUR.A.YTL'
        ORT_MEVDUAT_FAIZ_ORANI_1AY='TP.TRY.MT01'
        ORT_MEVDUAT_FAIZ_ORANI_3AY='TP.TRY.MT02'
        ORT_IHTIYAC_FAIZ_ORANI ='TP.KTF10'
        ORT_TASIT_FAIZ_ORANI ='TP.KTF11'
        ORT_KONUT_FAIZ_ORANI ='TP.KTF12'

 





MAIN_PART ='https://evds2.tcmb.gov.tr/service/evds/'
API_KEY ='s8k5DXFC3I'





	


