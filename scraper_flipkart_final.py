
# coding: utf-8

# In[19]:


from bs4 import BeautifulSoup
import urllib
import requests
import  csv


# In[20]:


t = input()
t = t.replace(' ','+')


# In[21]:


x="https://www.flipkart.com/search?q="+t+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
print(x)


# In[22]:


url = (x)
r = requests.get(url)
#r.content


# In[23]:


soup = BeautifulSoup(r.content)
#print (soup.prettify())


# In[24]:



with open('product.csv','w',newline='') as f:
    colnames = ['product','price','ratings']
    writer = csv.DictWriter(f,fieldnames=colnames)
    writer.writeheader()

    
    #colnames = ['product','price','ratings']
    #writerz = csv.DictWriter(f,fieldnames=colnames)
    #writerz.writeheader()






    x1="https://www.flipkart.com/search?q="+t+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    url = (x1)
    r = requests.get(url)
    #r.content
    soup = BeautifulSoup(r.content)
    tproducts = soup.find_all("div",{"class": "_3wU53n"})
    #print(tproducts[0].text)
    price = soup.find_all("div",{"class": "_1vC4OE _2rQ-NK"})
    ratings = soup.find_all("div",{"class": "hGSR34 _2beYZw"})
    #print(len(tproducts))
    #print(ratings[0].text)
    #print(price[0].text)
    #for x in container:
    #   print(x.text)
    #thewriter.writerow([tproducts[0].text,price[0].text,ratings[0].text])

    i=0
    while(i<len(tproducts)):
        str1 = tproducts[i].text
        str2 = price[i].text[1:]
        str3 =ratings[i].text
        str3 = str3.replace('\u2605','')
        print(tproducts[i].text+"|   "+price[i].text[1:]+" |    "+ratings[i].text[0:3])
        writer.writerow({'product':str1,'price':str2, 'ratings': str3})

        i+=1
    
    
    for m in range(2,6):    
    
        x2="https://www.flipkart.com/search?q="+t+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(m)
        url = (x2)
        #print(url)
        r = requests.get(url)
        #r.content
        soup = BeautifulSoup(r.content)
        tproducts = soup.find_all("div",{"class": "_3wU53n"})
        #print(tproducts[0].text)
        price = soup.find_all("div",{"class": "_1vC4OE _2rQ-NK"})
        ratings = soup.find_all("div",{"class": "hGSR34 _2beYZw"})
        #print(len(tproducts))
        #print(ratings[0].text)
        #print(price[0].text)
        #for x in container:
        #   print(x.text)
        i=0
        while(i<len(tproducts)):
            str1 = tproducts[i].text
            str2 = price[i].text[1:]
            str3 =ratings[i].text
            str3 = str3.replace('\u2605','')
            print(tproducts[i].text+"|   "+price[i].text[1:]+" |    "+ratings[i].text[0:3])
            writer.writerow({'product':str1,'price':str2, 'ratings': str3})

            i+=1
    
    
    
    
    
    
    
    
    

  

