# Challenge: Creepy Resume
- Category: Forensics

## Description

<img width="478" height="616" alt="image" src="https://github.com/user-attachments/assets/3271c8ce-a61d-447c-8280-df1c074a9e52" />


## Flag: 
`deadface{Look_@_m3!!!}`

## Solution

Running exiftool on the image gave

<img width="927" height="555" alt="image" src="https://github.com/user-attachments/assets/1023dc62-d8c0-4dc7-b545-439de398b16c" />

The weird comment turned out to be "🥰󠅔󠅕󠅑󠅔󠅖󠅑󠅓󠅕󠅫󠄼󠅟󠅟󠅛󠅏󠄰󠅏󠅝󠄣󠄑󠄑󠄑󠅭". 

A thread on GhostTown was talking about `https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/` which led me to a decoder `https://emoji.paulbutler.org/?mode=decode`

<img width="494" height="815" alt="image" src="https://github.com/user-attachments/assets/58319bd2-50ee-4616-9c3b-8f61a0ace6f8" />
