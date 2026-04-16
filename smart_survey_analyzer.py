#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random

scores = []

while len(scores) <20:
    score = random.randint(0,6)

    if score ==0:
        break

    if score ==6:
        continue

    scores.append(score)



# In[13]:


print("toplam geçerli puan sayısı:", len(scores))
# while kullanıyoruz çünkü rastgele gelen sayılardan kaçıncı denemede liste boyutu 20 olacak bilmiyoruz.


# In[20]:


ortalama= sum(scores)/len(scores)
print(f"ortalama:  {round(ortalama,2)}")


# In[27]:


minPuan=min(scores)
maxPuan=max(scores)
print(f"minimum puan: {minPuan}")
print(f"maximum puan: {maxPuan}")


# In[32]:


memnun=0
kararsiz=0
memnunDegil=0
for puan in scores:
    if puan==4 or puan==5:
        memnun=memnun+1
    if puan==3:
        kararsiz=kararsiz+1
    if puan==2 or puan==1:
        memnunDegil=memnunDegil+1
print(f"memnun: {memnun}")    
print(f"kararsiz: {kararsiz}")
print(f"menunDegıl: {memnunDegil}")


# In[34]:


sayac=0
for puan in scores:
    if puan==1:
        sayac=sayac+1
    else:
        sayac=0
    if sayac==3:
        print("⚠️ Kritik memnuniyetsizlik tespit edildi")
        break
        


# In[37]:


print("toplam geçerli puan sayısı:", len(scores))
print(f"ortalama:  {round(ortalama,2)}")
print(f"minimum puan: {minPuan}")
print(f"maximum puan: {maxPuan}")
print(f"memnun: {memnun}")    
print(f"kararsiz: {kararsiz}")


# In[ ]:




