from ast import Pass
from configparser import NoOptionError
import abbr as a
from requests import Session
import xml.etree.ElementTree as et

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
        


    def get_crypto_prices(self):
        output = {}
        url = a.MAIN_PART
        parameters = {
            'series':self.series,
            'key': a.API_KEY,
            'startDate' :self.startDate,
            'endDate': self.endDate,
            'type': 'xml',
            'aggregationTypes':self.aggregationTypes,
            'Formulas': self.formulas,
            'Frequency': self.frequency,
        }
        headers = {
            'Accepts': 'application/xml',
           
        }

        session = Session()
        session.headers.update(headers)
        response = session.get(url, params=parameters)
        data = et.parse(response.text)

        if response.ok:
           pass
        else:
            if response.status_code == 400:
               pass
            else:
                raise ConnectionError

        return output