
import abbr as a
import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import json
from requests import Session


series = None
startDate = None
endDate = None 
aggregationTypes = None
formulas =None
frequency = None


class My_Manager:
    def __init__(self,_series,start_Date, end_Date, aggregation_Types,_formulas,_frequency):
        self.series = _series
        self.startDate = start_Date
        self.endDate =end_Date
        self.aggregationTypes =aggregation_Types
        self.formulas = _formulas
        self.frequency = _frequency
        


    def get_data(self):
        url = a.MAIN_PART
        path ='{}series={}&startDate={}&endDate={}&type=json&key={}&aggregationTypes={}&Formulas={}&Frequency={}'.format(url,self.series,self.startDate,self.endDate,a.API_KEY,self.aggregationTypes,self.formulas,self.frequency)
        
        url_to_open = urllib.request.urlopen(path).read()
        data = json.loads(url_to_open)
        #if url_to_open.ok:
        #    pass
        #else:
        #    if url_to_open.status_code == 400:
        #        pass
        #    else:
        #        raise ConnectionError
        
        
        
        #url_to_open = urllib.request.urlopen(path).read()
        #tree = ET.fromstring(url_to_open)
        
        
        #url_to_open = urllib.request.urlopen(path).read()
        #tree = ET.parse(url_to_open)
        #root_node = tree.getroot()
        #lst = root_node.findall('TP_DK_USD_A_YTL')  
        return data