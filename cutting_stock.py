def cutting_stock (material_type, material_unit,material_size,height,weight,stencil_array,plot_cutting=0):
    
    #import matplotlib.pyplot as plt
    #%matplotlib inline
    import pylab as pl
    import numpy as np
    #validate inputs
    if material_unit == "M":
        measure = "meters"
    else:
        measure = "feets"
    quantity_param = False
    total_stencil=0
    var_plot=[]
    temp_plot= np.empty(1)
    constraint=[]
    length = (len(stencil_array))
    if isinstance(stencil_array,list) and  isinstance(stencil_array[0],tuple) :#len(stencil_array) != 1
        
        if (len(stencil_array[0])>2 and material_type =="2D") or (len(stencil_array[0])>1 and material_type =="1D"):
            
            quantity_param = True    
    demand_material=0
    area_stencil_list =[]
    rest = []
    if material_type == "1D":
        source_area=material_size
    else:
        source_area=height*weight
        
    for i in xrange(length):
        
        if quantity_param == False: 
            if material_type == "1D":
                area_stencil = stencil_array[i]
            else:
                area_stencil = stencil_array[i][0]*stencil_array[i][1]
            
            quantity = source_area/area_stencil 
            area_stencil_list.append(int(quantity))
            var_plot.append(int(area_stencil))
            
            rest.append(round(source_area - area_stencil*(int(quantity)),2))
            
        else:
            if material_type == "1D":
                area_stencil = stencil_array[i][0]
                qty_x_stencil = stencil_array[i][1]
            else:
                area_stencil = stencil_array[i][0]*stencil_array[i][1]
                qty_x_stencil = stencil_array[i][2]
            area_stencil_qty= qty_x_stencil*area_stencil
            var_plot.append(int(area_stencil_qty))
            total_stencil= total_stencil + (area_stencil_qty)
            if source_area >= total_stencil:
                constraint.append(stencil_array[i])
    
    #Plot
    if plot_cutting !=0 and length>1:
       
        source_plot = np.linspace(0,source_area,length)
        
        b = np.arange(1, 2, 3)
        pl.bar(var_plot, source_plot)
        
        
    if quantity_param == True:    
        
        if  total_stencil <= source_area:
            surplus= round(source_area-total_stencil,2)
            print "You need to buy zero times the quantity of source material that you have."
            print "You still have ",surplus," ",measure," of source material."
            return 0
        else:
            buy_material=int(total_stencil/source_area)
            print "You need to buy ", buy_material," more times the quantity of source material that you have."
            print "Stencil material that fits in the material source ",constraint
            return buy_material #return source material
    print "Qty per source material ", area_stencil_list, "Surplus ",rest
    
    return area_stencil_list#,0 ,rest