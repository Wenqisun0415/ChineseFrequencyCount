#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:05:00 2017
Analyse an Chinese article and output a txt file with frequency for each word
@author: wenqisun
"""
import jieba
import os

def File_to_Word():
    '''
    Input: None
    Returns a list containing all the words in the article except the words
    whose length is one
    '''
    with open(os.path.expanduser("~/Desktop/text.txt"), encoding='gb18030') as FileHandle:
        Word_List = []                                 #encoding could be gbk
                                                       #depending on the input file
        for line in FileHandle.readlines():
            line = line.replace(' ','')
            line = line.strip('\n')
            word_list = jieba.lcut(line, cut_all=False)
            Word_List = Word_List + word_list
        FileHandle.close()
    temp = Word_List[:] #Avoiding aliasing since list is mutable
    for word in temp:
        if len(word) == 1:
            Word_List.remove(word)
    return Word_List

def Word_to_Dict(List):
    '''
    Input: List, a word list
    Returns a dictionary containing the words and its frequency
    '''
    myDict = {}
    for word in List:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def Most_Common_Words(Dict):
    '''
    Input: Dict, a dictionary containing the words and its frequency
    Returns words with the highest frequency
    '''
    values = Dict.values()
    Max = max(values)
    words = []
    for i in Dict:
        if Dict[i] == Max:
            words.append(i)
    return (words, Max)

def Dict_to_File(Dict):
    '''
    Input: Dict, a dictionary
    Outputs a FrequencyCount file in a degressive order
    '''
    with open(os.path.expanduser("~/Desktop/FreqCount.txt"), encoding='gbk', mode='w+') as f:
        while len(Dict) >0:
            temp = Most_Common_Words(Dict)
            for w in temp[0]:
                f.write(w)
                f.write(' ')
                f.write(str(temp[1]))
                f.write('\n')
                del(Dict[w])
        f.close()


if __name__ == '__main__':
    Dict_to_File(Word_to_Dict(File_to_Word()))