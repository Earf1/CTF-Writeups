# Field Day

## Description

Deep within the fortified citadel, ancient UNIVAC mainframes hum with classified transmissions. You have spent days infiltrating the Citadel's military grade communication defenses and manage to intercept a FIELDATA transmission encoded onto one of the first methods of storing data. However the data is trapped behind a peculiar digital representation of the FIELDATA encoding, different from the usual 6 bit pairing. Decode the 12 bit transmission to uncover the resistance's secret message.

Attachments: `transmission.txt` Flag Format: citadel`{decodedtransmission}`

## Solution
Looking for FIELDATA encoding led me to `https://www.fourmilab.ch/documents/univac/fieldata.html`

Using the lookup table provided here, i wrote a script to decode the transmission and got `]R3B3LL10N$&[BU1]LT:0N[H0]P3`

I was stuck on this output for quite a while, but looking closely at the lookup table again i found

<img width="421" height="44" alt="image" src="https://github.com/user-attachments/assets/842485a2-1130-46db-accb-18dd52418d3f" />

Thus, i performed the case shift operations and got the message as `r3b3ll10n$&BU1lt:0nH0p3`

## Flag
`citadel{r3b3ll10n$&BU1lt:0nH0p3}`
