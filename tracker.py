import requests
from bs4 import BeautifulSoup
import smtplib 

URL="https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_2?crid=1YD3URC77512E&dchild=1&keywords=bose+headphones+original&qid=1590662107&sprefix=bose+he%2Caps%2C275&sr=8-2"
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

def price_tracker():

	page=requests.get(URL,headers=headers)
	
	soup=BeautifulSoup(page.content,'html.parser')
	
	title=soup.find(id="productTitle").get_text()
	
	price=soup.find(id='priceblock_ourprice').get_text()
	print(price)
	
	converted_price=price[2:]
	conv=converted_price.split(',')
	#print(conv)
	final_price=float(conv[0]+conv[1])

	#print(converted_price)
	print(final_price)
	
	if(final_price>17000 and final_price<20000):
		send_mail()


def send_mail():
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('varunverma.edu@gmail.com','python@4835')

	subject="Price dropped on Desired Product"
	body="Click  the Amazon Link for more information	https://www.amazon.in/Bose-SoundLink-Wireless-Around-Ear-Headphones/dp/B0117RGG8E/ref=sr_1_2?crid=1YD3URC77512E&dchild=1&keywords=bose+headphones+original&qid=1590662107&sprefix=bose+he%2Caps%2C275&sr=8-2 "

	message=f'Subject:{subject}\n\n\n{body}'

	server.sendmail('varunverma.edu@gmail.com','vverma22600@gmail.com',message)

	print('EMAIL HAS BEEN SUCCESSFULLY SENT!!!!')

	server.quit()

price_tracker()