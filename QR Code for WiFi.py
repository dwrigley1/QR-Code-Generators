'''
create a QR Code for others to scan to join your WiFi network!
'''

from wifi_qrcode_generator import wifi_qrcode
qr_code = wifi_qrcode("<Enter SSID Here>", hidden=False,
                      authentication_type="WPA", password="<Enter Password Here>")

qr_code_img = qr_code.make_image()

qr_code_img.save("wifi_qr_code.png")