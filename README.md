# markov_chain
Simple markov chain for tweet generator 


![](https://github.com/s3nh/markov_chain/blob/master/imgs/markov_chains.png)


Based on reddit r/machinelearning and r/deeplearning headers.

thanks to [Adrian](https://github.com/xadrianzetx) for informative dataset 


## To do

- tweepy

- /html template


in progress


# examples 


```

mchain = MarkovChainGen(16, 120, 'dataset.txt)
model = mchain.build()
mchain.generate_text(model)

```

Some results 

#Update 


I connect this model into twitter account so you can see some of the results. 

![](https://github.com/s3nh/markov_chain/blob/master/imgs/Przechwytywania.png)


You can use it by yourself by using load_and_gen.py file with your own configuration. 
PM me please if you are interested in songdick.pkl file. 
It is too large to upload it on git ;)

# TO do 

```


Next - CharRNN in Pytorch. 


Source: [Eli Bendersky's website](https://eli.thegreenplace.net/)
