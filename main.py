from re import A
from my_manager import My_Manager
import abbr as a



if __name__ == '__main__':
    
    dolar_alis = a.EURO_ALIS
    startDate ='01-01-2020'
    endDate ='01-03-2021'
    formulas = a.formulas.FARK.value
    freguency = a.frequency.AYLIK_6.value
    aggregation = a.aggregationTypes.BITIS.value
    
    deneme = My_Manager(_series=dolar_alis, start_Date=startDate,end_Date=endDate, aggregation_Types=aggregation,_formulas =formulas,_frequency = freguency)
    print(deneme.get_data())
    
    

  
  
  
    
    