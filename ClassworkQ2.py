def word_freq(sent):
    sent_words = sent.split()
    dict_freq = {}
    for word in sent_words:
        if word in dict_freq:
            dict_freq[word] += 1 
        else:
            dict_freq[word] = 1 
    
    print(dict_freq)

sen = input('Enter a sentence:')
word_freq(sen)