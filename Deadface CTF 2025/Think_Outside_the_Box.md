# Challenge: Think Outside the Box
- Category: Forensics

## Description



## Flag: 
`DEADFACE{JP3G_ALT3RED_HE1GHT}`

## Solution
I first followed my standard procedure of running exiftool,binwalk,foremost,strings,zsteg on the file but found nothing suspicious in the outputs of any of these cmds
```
 @advay  exiftool -v thinkoutsidethebox.jpg 
  ExifToolVersion = 13.36
  FileName = thinkoutsidethebox.jpg
  Directory = .
  FileSize = 87296
  FileModifyDate = 1761421564
  FileAccessDate = 1761880120
  FileInodeChangeDate = 1761879350
  FilePermissions = 33261
  FileType = JPEG
  FileTypeExtension = JPG
  MIMEType = image/jpeg
JPEG APP0 (14 bytes):
  + [BinaryData directory, 9 bytes]
  | JFIFVersion = 1 1
  | ResolutionUnit = 0
  | XResolution = 1
  | YResolution = 1
  | ThumbnailWidth = 0
  | ThumbnailHeight = 0
JPEG DQT (130 bytes):
JPEG SOF2 (15 bytes):
  ImageWidth = 500
  ImageHeight = 377
  EncodingProcess = 2
  BitsPerSample = 8
  ColorComponents = 3
  YCbCrSubSampling = 2 2
JPEG DHT (54 bytes):
JPEG SOS
```

```
 @advay  binwalk thinkoutsidethebox.jpg 

                      /home/advay/Desktop/deadface/thinkoutsidethebox.jpg
----------------------------------------------------------------------------------------------
DECIMAL                            HEXADECIMAL                        DESCRIPTION
----------------------------------------------------------------------------------------------
0                                  0x0                                JPEG image, total size: 
                                                                      87296 bytes
----------------------------------------------------------------------------------------------

Analyzed 1 file for 85 file signatures (187 magic patterns) in 3.0 milliseconds
```

Looking at the name being `thinkoutsidethebox.jpg` and then the image having only half of the meme template being used (very guessy ikr), but considering ive seen similiar stuff before where the height of a png has to be increased by editing the relevant hex and recalculating the crc32 checksum, i went down the same route for this and made a script to automate it
```python
import struct

def patch(filename, height):
    with open(filename, 'rb') as f:
        data = bytearray(f.read())

    i = 0
    while i < len(data) - 9:
        if data[i] == 0xFF and (data[i+1] & 0xF0) == 0xC0:
            segment = data[i+1]
            if segment not in (0xC4, 0xC8, 0xCC):
                height_offset = i + 5
                data[offset:offset+2] = struct.pack('>H', height)
                break
        i += 1

    with open('boxed.jpg', 'wb') as out:
        out.write(data)

patch('thinkoutsidethebox.jpg', 800)
```

Running this gave me the complete image with the flag

<img width="500" height="800" alt="image" src="https://github.com/user-attachments/assets/0a883c22-990d-41e9-854e-41a1df19aab7" />
