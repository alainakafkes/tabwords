# tabwords

tabwords is a Chrome extension that displays a randomly chosen word from Other-Wordly - a logophile's treasure trove of obscure words - on each new tab. Check out the [demo](https://twitter.com/alainakafkes/status/882699871446343683).

## How I Built tabwords

1. Compiled list of image URLs from all Other-Wordly posts using the Tumblr API via ```main.py```.
2. Pulled random image URL from list in ```main.js```, and displayed it in ```index.html```.
3. Set up Chrome extension framework in ```manifest.json```.
4. Created icons using Canva.
