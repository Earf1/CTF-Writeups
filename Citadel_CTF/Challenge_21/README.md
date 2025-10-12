# Case Sensitivity

## Description

You step into a constricted floor where every movement and operation is limited. Commands are few, space is tight, and options are restricted.

A guardian looms over the floor, its body shifting like liquid metal, enforcing these constraints. It watches your every move, daring you to make do with what you have and uncover the passcode to the next floor despite the restrictions.

## Solution

so this was a pyjail challenge, so i knew i had to use the `exec` cmd in this, and also had to figure out how to bypass the restrictions put in place

at first i ran `exec(print(open("flag.txt")))`, because i thought the flag might be in a .txt file on the system

This gave me
```
ERROR:
Traceback (most recent call last):
  File "/home/user/pyjail_challenge.py", line 26, in <module>
    exec('from os import *; ' + clean(user_input))
  File "/home/user/pyjail_challenge.py", line 18, in clean
    raise ValueError(f"NUH UH, {word} is not allowed!{although}")
ValueError: NUH UH, print is not allowed! (although print is very close)
```
Since the name of the challenge mentions case sensitivity, i tried running `exec(PRINT(OPEN("flag.txt")))

This gave me
```
ERROR:
Traceback (most recent call last):
  File "/home/user/pyjail_challenge.py", line 26, in <module>
    exec('from os import *; ' + clean(user_input))
  File "/home/user/pyjail_challenge.py", line 18, in clean
    raise ValueError(f"NUH UH, {word} is not allowed!{although}")
ValueError: NUH UH, OPEN is not allowed!
```
Ok so, if it says (although the `cmd` is very close), the cmd can be bypassed by using it in all caps, otherwise its just completely blacklisted
So, i cant use open which means the flag is probably not stored in a .txt file, 

After some trial and error i figured out that flag is probably an environ variable and that 'flag' is blocked but 'FLAG' works

My final working payload was `exec('PRINT(ENVIRON'.lower() + '['FLAG'])')`

```
exec("PRINT(ENVIRON".lower() + "['FLAG'])")
citadel{d34th_d035_n07_fr33_y0u_fr0m_7h3_gu17ar15t}
```
## Flag
`citadel{d34th_d035_n07_fr33_y0u_fr0m_7h3_gu17ar15t}`
