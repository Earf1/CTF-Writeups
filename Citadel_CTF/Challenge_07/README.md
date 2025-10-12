# Randomly Accessed Memories

## Description

On your ascent to this floor, you hear these fragments being played back —

```
clone it, pull it, reset it, stage it, 
commit, push it, fork, rebase it. 
merge it, branch it, tag it, log it, 
add it, stash it, diff, untrack it … 
```
You look around and discover a chamber containing a vast archive of Daft Punk’s music, intertwined with cryptic commits left behind by other musicians. They seem ordinary at first glance, but not everything in the history is what it seems. The archive: https://github.com/evilcryptonite/daft-punk-archive

## Solution

I went through the commit history, and found 
- Remove secret chunk 3 file (history-only)
- Remove secret chunk 2 file (history-only)
- Remove secret chunk 1 file (history-only)

For chunk 1 there was `Y2l0YWRlbHt3M180cjM=` which is b64 and decoded to `citadel{w3_4r3`
For chunk 2 there was `X3VwXzRsbF9uMXQzXw==` which is b64 and decoded to `_up_4ll_n1t3_`
For chunk 3 there was `dDBfZzF0X2x1Y2t5fQ==` which is b64 and decoed to `t0_g1t_lucky}`


## Flag
`citadel{w3_4r3_up_4ll_n1t3_t0_g1t_lucky}`
