#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install db-sqlite3


# In[2]:


import sqlite3


# In[3]:


conn = sqlite3.connect('exp2.db')
cur = conn.cursor()
conn = sqlite3.connect('test.db')
print("Opened database successfully");


# In[7]:


conn.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME            TEXT NOT NULL,
AGE             INT  NOT NULL,
ADDRESS         CHAR(50),
SALARY          REAL);''')
print("Table Created succesfully");


# In[10]:


conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)               VALUES (1,'paul',32,'California',20000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)              VALUES (2,'Allen',25,'Texas',15000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)               VALUES (3,'Smith',28,'LosAngeles',65000.00)");
conn.commit()
print("Records inserted successfully");


# In[11]:


for row in conn.execute('select * from COMPANY'):
    print(row)


# In[12]:


conn.commit()


# In[13]:


conn.close()


# In[ ]:




