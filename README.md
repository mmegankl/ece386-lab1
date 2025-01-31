# ece386-lab01

Serving handwritten digit inference with FastAPI.

See [USAFA ECE 386: AI Hardware Applications - Lab 1](https://usafa-ece.github.io/ece386-book/b1-prediction/lab-digits-api.html)

**GitHub Actions are enabled in this repository!** The workflow currently:

- Runs [Black](https://black.readthedocs.io/en/stable/index.html) format checker against client and server
- Runs [Pyright](https://microsoft.github.io/pyright/#/) type checker against client and server

## Writeup

*Answer the following questions. Strive to be articulate.*

### What strategies did you use to ensure that your client and server where communicating with the same schema?
We were able to determine functionality with the return code in the server's terminal. A 200 meant successful communcation, a 400s error meant there was an issue on the client side, and a 500s number meant there was an issue on the server side. From there, we were able to isolate, diagnose, and debug potential issues with the code. 

Another strategy was the use of pyright. With pyright, we were able to see any discrepancies with our code and helped verify variable and return types.

### In regard to preprocessing your digit images, how well do you think your server would scale to *any* picture of a digit?
While we have not attempted a variety of digit pictures, I think the model would need to be trained with a wider range of pictures for it to work with more robust pictures of digits. That said, we think our server would do poorly.

### Does the client/server architecture make sense for this problem? Why or why not?
The client server architecture does not make sense for this particular application because it is easier to create a prediction model without a server. The only exception to this would be if there was a high volume of people who wanted to run the keras model but did not have the technical background to do it on their own.

## Documentation

*Documentation statement. Pay special attention to the LLM policy.*
We received EI from Capt Yarbrough on lessons 8 and 9, as well as on 1/30/25. Capt Yarbrough helped us understand what we were doing conceptually as well as provide us resources online to complete the lab. Additionally, he helped fix small errors in both the digits.py and client.py files. C1C Flachman also led us in the right direction by explaining how the GET and POST worked and helped us get a better understanding of the input parameters and what it was actually doing.
