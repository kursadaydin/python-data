from re import A
from my_manager import My_Manager
import abbr as a



if __name__ == '__main__':
    
    dolar_alis = a.series.USD_ALIS.value
    startDate ='01-01-2020'
    endDate ='01-01-2022'
    formulas = a.formulas.DUZEY.value
    frequency = a.frequency.AYLIK.value
    aggregation = a.aggregationTypes.BITIS.value
    
    deneme = My_Manager(_series=dolar_alis, start_Date=startDate,end_Date=endDate, aggregation_Types=aggregation,_formulas =formulas,_frequency = frequency)
    print(deneme.get_data())
    
    

  
  
  
    
    