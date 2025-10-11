# Challenge: Never Gonna Solve You
- Category: Forensics

## Description

<img width="572" height="339" alt="image" src="https://github.com/user-attachments/assets/0b6e39a4-4ce5-43c6-bbcb-e6c656db705e" />


## Flag: 
`EnXp{y0u_r34lly_d1dnt_g1v3_up}`

## Solution
We were given a .jpg file, but it was unsually large for its resolution at 2.51MB, so i ran strings on it and saw mentions of `flag.mp4`

<img width="183" height="165" alt="image" src="https://github.com/user-attachments/assets/70927d00-49bd-48d2-8686-834900b97e42" />

So i ran binwalk on the image, and got a .rar file which was password encrypted, i tried `weknowthegameandweregonnaplayit` which was given in the chall desc. and it extracted the archive

Inside of it was `flag.mp4` which was another shitty rickroll. Running strings on this again, i saw `giveup.pcapng`.

<img width="191" height="413" alt="image" src="https://github.com/user-attachments/assets/5033db39-68dc-46dd-8186-1d488e1d95ae" />

Running binwalk again, i was able to extract the pcapng file. Opening it in WireShark

<img width="1624" height="234" alt="image" src="https://github.com/user-attachments/assets/d5be5b1b-13a7-409c-8a11-3297507d38b3" />

All of the FTP-Data and HTTP requests were redd herrings, except one which was

<img width="1333" height="222" alt="image" src="https://github.com/user-attachments/assets/41f96648-9a43-4340-8e34-01136ae940cc" />

The link led me to a gdrive folder which had `lyrics.txt`, which looked normal at first but opening it in notepad showed weird characters

<img width="866" height="172" alt="image" src="https://github.com/user-attachments/assets/f8111691-18b2-486b-944a-09140841f97d" />

This is common in zerowidth unicode steg, so i went to `https://stegzero.com/` and pasted the starting into it and got the flag

<img width="1200" height="639" alt="image" src="https://github.com/user-attachments/assets/2bf37211-6abf-48d9-a242-847e514b0d83" />

