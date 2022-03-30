
from my_manager import My_Manager
import abbr as a




if __name__ == '__main__':
    
    dolar_alis = a.series.ORT_MEVDUAT_FAIZ_ORANI_1AY.value
    startDate ='01-01-2020'
    endDate ='01-04-2022'
    formulas = a.formulas.DUZEY.value
    frequency = a.frequency.YILLIK.value
    aggregation = a.aggregationTypes.BITIS.value
    
    deneme = My_Manager(_series=dolar_alis, start_Date=startDate,end_Date=endDate, aggregation_Types=aggregation,_formulas =formulas,_frequency = frequency)
    my_data =deneme.get_data()
    deneme.exportToExcel(my_data)
    
    
    
    
    
   
    
 
    
    

  
  
  
    
    