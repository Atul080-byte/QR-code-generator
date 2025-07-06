import qrcode

#taking upi id as input
upi = input("Enter your UPI ID: ")
amount = input("Enter amount: ")
name = input("Enter recipient name: ")
note = input("Enter note/message: ")

#payment url format :
# upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

#defining the payment URL based on the UPI ID and the payment app
#we can modify these URLs

phonpe_URL = f'upi://pay?pa={upi}&pn={name}&am={amount}&cu=INR&tn={note}'
paytm_URL = f'upi://pay?pa={upi}&pn={name}&am={amount}&cu=INR&tn={note}'
gpay_URL = f'upi://pay?pa={upi}&pn={name}&am={amount}&cu=INR&tn={note}'

#create QR code for each payment app
phonpe_qr = qrcode.make(phonpe_URL)
paytm_qr = qrcode.make(paytm_URL)
gpay_qr = qrcode.make(gpay_URL)

#save the QR code to img files(optional)
phonpe_qr.save('phonpe_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

#display the qr codes (u may need to install PIL/pillow library)
# phonpe_qr.show()
# paytm_qr.show()
gpay_qr.show()


#refferal link: https://youtu.be/y_I2YOP91Is?si=F3S5gkt1Y66aKWbr 