
import abbr as a
import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import json
from requests import Session
import pandas as pd

from datetime import datetime


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
        
    def convertTime(self,timestamp):
        time = datetime.fromtimestamp(int(timestamp)).strftime('%d-%m-%y')
        return time


    def get_data(self):
        temp={}
        url = a.MAIN_PART
        path ='{}series={}&startDate={}&endDate={}&type=json&key={}&aggregationTypes={}&Formulas={}&Frequency={}'.format(url,self.series,self.startDate,self.endDate,a.API_KEY,self.aggregationTypes,self.formulas,self.frequency)
        
        #data = pd.read_json(path)
        #df = pd.DataFrame(data)

        
        url_to_open = urllib.request.urlopen(path).read()
        data = json.loads(url_to_open)
        
        for i in data['items']:
            if i['TP_DK_EUR_A_YTL'] == None:
                continue
            tempTime = self.convertTime(i['UNIXTIME']['$numberLong'])
            tempValue = i['TP_DK_EUR_A_YTL']
            temp['Time']= tempTime
            temp['Value'] = tempValue
            #print('{} :  {}'.format( tempTime, tempValue))
    
        df = pd.DataFrame.from_dict(temp, orient='index')
        print(df)
        
        
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
        