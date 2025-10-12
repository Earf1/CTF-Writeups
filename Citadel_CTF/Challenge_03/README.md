# Omniscient Flag's Metadata


## Description

As you step into the second chamber, a figure manifests before you. Before you stands a forgotten deity, a dead god spoken of only in whispers. Known by countless names: “Apostle of Epilogue and Eternity,” “Lone Messiah” and many more lost to time.

They leave nothing but a single image, a relic carrying his final secret. Hidden within its layers lies the key to ascend to the next chamber.

## Solution
I ran `exiftool -v challenge.jpg` on this
```
└─$ exiftool -v challenge.jpg
  ExifToolVersion = 13.25
  FileName = challenge.jpg
  Directory = .
  FileSize = 371263
  FileModifyDate = 1759776247
  FileAccessDate = 1759776247
  FileInodeChangeDate = 1759993463
  FilePermissions = 33279
  FileType = JPEG
  FileTypeExtension = JPG
  MIMEType = image/jpeg
JPEG APP1 (2855 bytes):
  + [XMP directory, 2826 bytes]
  | XMPToolkit = Image::ExifTool 12.57
  | Author = kdj had a habit of hiding images within images
JPEG DQT (130 bytes):
JPEG SOF0 (15 bytes):
  ImageWidth = 640
  ImageHeight = 1017
  EncodingProcess = 0
  BitsPerSample = 8
  ColorComponents = 3
  YCbCrSubSampling = 2 2
JPEG DHT (416 bytes):
JPEG SOS
``` 
Here "kdj had a habit of hiding images within images", made me open the image in hxd, where i found another ``FF D8 FF E9`` header, which i carved out till the EOF i.e. ``FF D9``.

This gave me another image which had the flag.


<img width="640" height="613" alt="Untitled3" src="https://github.com/user-attachments/assets/08429ec2-03cf-410a-94a2-d6983ee8f50b" />


## Flag
`citadel{th1s_ch4ll3ng3_1s_f0r_th4t_0n3_ex1ft00l_4nd_b1nw4lk_enthus14st}`

