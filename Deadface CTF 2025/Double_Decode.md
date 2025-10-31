# Challenge: Double Decode
- Category: Forensics

## Description

<img width="571" height="775" alt="image" src="https://github.com/user-attachments/assets/37a862b6-3766-4235-b5c8-0c20762dd567" />


## Flag: 
`deadface{EZpngH1d1ng}`

## Solution
Scanning the qr gives `Not the flag... keep guessing`

following my standard procedure i ran exiftool on it and got
```
advay@DESKTOP-MASF3ES:/mnt/c/Users/advay/Downloads/deadface$ exiftool -v qr_flag.png
  ExifToolVersion = 12.76
  FileName = qr_flag.png
  Directory = .
  FileSize = 774
  FileModifyDate = 1761430613
  FileAccessDate = 1761430613
  FileInodeChangeDate = 1761430634
  FilePermissions = 33279
  FileType = PNG
  FileTypeExtension = PNG
  MIMEType = image/png
PNG IHDR (13 bytes):
  + [BinaryData directory, 13 bytes]
  | ImageWidth = 330
  | ImageHeight = 330
  | BitDepth = 1
  | ColorType = 0
  | Compression = 0
  | Filter = 0
  | Interlace = 0
PNG IDAT (1 chunk, total 530 bytes)
PNG IEND (end of image)
  Warning = [minor] Trailer data after PNG IEND chunk
```

The warning made me run strings on it which gave 
```
IHDR
IDATx
PTY?
lb3b=u
d .[
mh23
vWi|\
<"r_
Ak&4
a5A     u
m;y&<
Es`th
IEND
#df#
IyBwYXlsb2FkLnB5CgpkYXRhID0gIjY0IDY1IDYxIDY0IDY2IDYxIDYzIDY1IDdiIDQ1IDVhIDcwIDZlIDY3IDQ4IDMxIDY0IDMxIDZlIDY3IDdkIgoKZmxhZyA9IGJ5dGVzLmZyb21oZXgoZGF0YSkuZGVjb2RlKCkKcHJpbnQoZmxhZykK
```

The string in the end looked like b64, and decoding it gave
```python
# payload.py

data = "64 65 61 64 66 61 63 65 7b 45 5a 70 6e 67 48 31 64 31 6e 67 7d"

flag = bytes.fromhex(data).decode()
print(flag)
```
converting the hex to ascii gave me the flag
