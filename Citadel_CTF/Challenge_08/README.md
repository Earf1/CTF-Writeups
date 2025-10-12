# Selected Ambient Work

## Description

The symphonic adventure does not end here. On the next floor, a single song keeps echoing through the floor, repeating in a haunting loop. Amid the sound, you find a note left by a past candidate. It hints that the song holds a secret message, hidden in plain sight, much like how Aphex Twin concealed his face within his music with the help of spectrograms.

To move forward, you must find the message hidden in this sound.

Note: Separate the words in the flag with _ and make it UPPERCASE. Example: citadel{S3L3CT3D_AMB13NT_W0RK}

## Solution

The .wav file has morse code playing continously through it, but theres also an instrumental playing which makes morse code audio decoders redundant.

Listening to it i heard a weird screech at `1:00` and `1:12`, so i opened this part in a spectogram analyser and got

<img width="517" height="213" alt="image" src="https://github.com/user-attachments/assets/6c6403e7-8fc8-4e52-8027-bea2807c4e8d" />


Then i got the morse from the middle of citadel{} to be `.----   .-.. ----- ...- ...--   .---- -.. --` which translates to `1 L0V3 1DM`

## Flag
`citadel{1_L0V3_1DM}`
