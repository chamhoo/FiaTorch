# FiaTorch

FiaTorch, containing a serise of feesible lightweight components, is an open-source package builded up for Kaggle competition. 

## File Structure

----|--train  
    |  
    |--stacking  
    |  
    |--analysis  
    |  
    |--demo.ipynb  
    |  
    |-README.md  

## Prerequisite of package

numpy  
pandas  
scikit-learn  
matplotlib  
pytorch  
pytorchvision  
hyperopt  

## What is a complete training procedure?

> Block  

|Train         |Merge     |
|--------------|----------|
|model['Name0']|\|        |
|model['Name1']|+ merge --|
|model['Name2']|\|        |

> Pipeline

|||||
|:-------|:-------------------------|:---------------------------|-------------|
|        |\|-**if y == 0:** block 1-|                            |\|           |
|block 0-|\|-**if y == 1:** block 2-|                            |\|           |
|        |\|-**if y == 2:** block 3-|\|- **if y <= 0:** block 4- |\|-**Result**|
|        |                          |\|- **if y >= 0:** block 5- |\|           |
|        |                          |\|- **if y >= 10:** block 6-|\|           |

> Path

..\/task_path  
├─module1  
│&emsp;├─model1  
│&emsp;│&emsp;├─parameter  
│&emsp;│&emsp;├─output  
│&emsp;│&emsp;└─model1.log  
│&emsp;│&emsp;&emsp;&emsp;└─statue  
│&emsp;├─model2  
│&emsp;└─stacking_model  
│&emsp;&emsp;&emsp;└─parameter  
├─module2  
└─task.log  
&emsp;└─distributional_rules.log  

## API

>### **CLASS** fiat.Block  

+ **\_\_x_data\_\_:**
+ **\_\_y_data\_\_:**
+ **\_\_name\_\_:**
+ **\_\_model_dic\_\_:**

>#### fiat.Block.data.loader(x, y, batch_size=64, cv=5)  

#### Parameters  

+ **x:** dtype in [str, numpy.array, [list of str], [list of numpy.array]]
+ **y:** dtype in [str, numpy.array, [list of str], [list of numpy.array]]

+ **batch_size:**

+ **cv:**

#### Return

None

#### Print

"The shape of x is {x_shape}"  
"The shape of y is {y_shape}"

>>fiat.Block.add_model(model, name)  

#### Parameters

+ **model:** 

+ **name:** str

#### Return

None

>>fiat.Block.save()  

>>fiat.Block.load()  

>>fiat.Block.merge()  

>>>Parameters



### Model

>fiat.model  

>>fiat.model.feature_engineering  

>>fiat.model.search  

>>fiat.model.save  

>>fiat.model.load  

### task

>fiat.task(path)

+ **\_\_rules:\_\_**

>>> Parameters  

+ **\_\_path\_\_:**, str, default = './task{eight random number}'  

>>> Return  

None

>>fiat.task.add_rule()

>>fiat.task.predict(x, cuda=True)  

>>> Parameters

+ **x:** 

+ **cuda:** 

>>> Return

perdiction, numpy.array

>>fiat.task.show()  

>>> Parameters

None

>>> Return

None

>>fiat.task.isbreak()

>>> Parameters

None

>>> Return

None