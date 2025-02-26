import cv2

img = cv2.imread("screenshot.png")  
assert img is not None, "Image not found"

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

img[0, 0, 0] = len(msg)
img[0, 0, 1] = len(password)

n = m = 0
z = 2
for c in password:
    img[n, m, z] = ord(c)
    m += 1
    if m >= img.shape[1]:
        m = 0
        n += 1
    z = (z + 1) % 3

for c in msg:
    img[n, m, z] = ord(c)
    m += 1
    if m >= img.shape[1]:
        m = 0
        n += 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
print("Encryption complete! Encrypted image saved as 'encryptedImage.png'.")