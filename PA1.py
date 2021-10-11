#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os

dirname = os.path.dirname("__file__")
filename = os.path.join(dirname, 'input/raw_2004car.csv')
#abs_path = os.path.abspath("__file__"+"/../../other-dir")


# In[2]:


df = pd.read_csv(filename)
df.head()


# ### Cleaning Dataframe

# In[3]:


vehicles = df['Vehicle Name']


# In[4]:


vehicles[105] = 'GMC Yukon 1500 SLE'
vehicles[246] = 'Mazda i 4dr'
vehicles[247] = 'Mazda s 4dr'
vehicles[248] = 'Mazda i 4dr'
vehicles[90] = 'Chrysler PT Cruiser GT 4dr'


# In[5]:


df1 = df.drop(['Vehicle Name'], axis = 1)
df1.insert(0, 'Vehicle Name', vehicles)


# In[6]:


df1


# In[7]:


drop_index = []
for idx in df1.index:
    for col in df1.columns[15:]:
        if df1[col][idx] == '*':
            drop_index.append(idx)
            break


# In[8]:


df1 = df1.drop(drop_index)


# In[9]:


vehicles = df1['Vehicle Name']


# In[10]:


car_brand = []
for i in vehicles:
    car_brand.append(i.split()[0])
print(car_brand)


# In[11]:


len(car_brand)


# In[12]:


GER = ['Porsche','Audi','BMW','Mercedes-Benz','Mini', 'Volkswagen']
JPN = ['Acura', 'Honda','Infiniti','Isuzu','Lexus','Mazda','Mitsubishi','Nissan','Scion','Subaru','Suzuki','Toyota']
KOR = ['Hyundai','Kia']
SWD = ['Saab', 'Volvo']
IND = ['Jaguar', 'Land']
USA = ['Buick','Cadillac','Chevrolet','Chrysler','Dodge','Ford','GMC','Hummer' ,'Jeep','Lincoln' ,'Mercury' ,'Oldsmobile' ,'Pontiac' ,'Saturn']

Continent = []
Nationality = []
for i in car_brand:
    if i in GER:
        Nationality.append('GER')
        Continent.append('Europe')
    elif i in JPN:
        Nationality.append('JPN')
        Continent.append('Asia')
    elif i in KOR:
        Nationality.append('KOR')
        Continent.append('Asia')
    elif i in SWD:
        Nationality.append('SWD')
        Continent.append('Europe')
    elif i in IND:
        Nationality.append('IND')
        Continent.append('Asia')
    elif i in USA:
        Nationality.append('USA')
        Continent.append('North America')
    else:
        Nationality.append('NaN')
        Continent.append('NaN')


# In[13]:


for i in Continent:
    if i == 'NaN':
        print(Continent.index(i))


# In[14]:


new_column = []
for idx in df1.index:
    for col in df1.columns[1:7]:
            if df1[col][idx] == 1:
                if col == 'Small/Sporty/ Compact/Large Sedan':
                    new_column.append('Sedan')
                    break
                new_column.append(col)
new_column


# In[15]:


new_column1 = []
flag = 1
for idx in df1.index:
    for col in df1.columns:
        if (col == 'AWD'):
            if df1[col][idx] == 1:
                new_column1.append(col)
            else:
                flag = 0
        elif (col == 'RWD'):
            if df1[col][idx] == 1:
                new_column1.append(col)
                flag = 1
            elif flag == 0:
                new_column1.append('N/A')
                flag = 1;
        else:
            continue
        


# In[16]:


len(new_column1)


# In[17]:


MPG = []
for idx in df1.index:
    city_mpg = int(df1['City MPG'][idx])*0.55
    hwy_mpg = int(df1['Hwy MPG'][idx])*0.45
    MPG.append(city_mpg + hwy_mpg)


# In[18]:


MPG


# In[19]:


drop_list = ['Small/Sporty/ Compact/Large Sedan','Sports Car','SUV','Wagon','Minivan','Pickup','AWD','RWD']


# In[20]:


df1 = df1.drop(drop_list, axis = 1)


# In[21]:


df1.insert(0, "Nationality", Nationality, True)
df1.insert(1, "Continent", Continent, True)
df1.insert(3, "Vehicle Type", new_column, True)
df1.insert(1, "Wheel Drive Type", new_column1, True)
df1.insert(1, "Cobined MPG", MPG, True)


# In[22]:


df1


# In[30]:


path = os.path.join(dirname, 'output')
os.mkdir(path, 0o666)


# In[33]:


output_path = os.path.join(path, 'refined_2004car.csv')


# In[34]:


df1.to_csv(output_path)


# In[ ]:




