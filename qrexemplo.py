import qrcode

# criar um codigo QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# adicionar dados ao código
data = 'https://sites.google.com/view/rasanhiiteste/in%C3%ADcio'
qr.add_data(data)
qr.make(fit=True)

# criar imagem do dado QR
img = qr.make_image(fill_color='black', back_color='white')

# salvar imagem em um arquivo
img.save('meusite.png')