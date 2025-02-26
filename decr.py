import cv2

img = cv2.imread("encryptedImage.png")
assert img is not None, "Encrypted image not found"

msg_len = img[0, 0, 0]
pass_len = img[0, 0, 1]

password = []
n = m = 0
z = 2
for _ in range(pass_len):
    password.append(chr(img[n, m, z]))
    m += 1
    if m >= img.shape[1]:
        m = 0
        n += 1
    z = (z + 1) % 3
password = ''.join(password)

user_pass = input("Enter passcode for decryption: ")
if user_pass == password:
    message = []
    for _ in range(msg_len):
        message.append(chr(img[n, m, z]))
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
        z = (z + 1) % 3
    message = ''.join(message)
    print("Decrypted message:", message)
else:
    print("Authentication failed!")