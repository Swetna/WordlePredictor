import re 
import numpy as np
 
 
def main():
    file_path = "/Users/swetna/Desktop/Tribhuvan_Swetna_ProjectA/wordle_words.txt"
    with open(file_path) as f:
#    list to store all words from the file
        words_list = []
        for line in f:
            #  removing special character from word
            line = re.sub(r'\W+', '', line)
            # removing the words containing non alphabetic characters
            if not re.match(r"[^a-zA-Z]+",line):
                line = re.sub(r"[^a-zA-Z]+", "", line)
                words_list.append(line.strip().lower())
                
   
    
#    ----first word based on cost function------
    
    alphabet_freq = char_freq(words_list) 
    
    first_pick_cost_list = pick_word(words_list,alphabet_freq)  
    
    print("-------First Pick-----------")
    
    
    
    first_pick = first_pick_cost_list[0]
    # print("First pick based on cost function:-  ",first_pick[0])
    
    # Top 20 picks for 1st word
    print("Top 20 picks for 1st word:- ",first_pick_cost_list[0:21])
    
    # if there is a tie
    pos = 1
    tie = []
    tie.append(first_pick[0])
    while first_pick_cost_list[pos][1] == first_pick[1]:
        tie.append(first_pick_cost_list[pos][0])
        pos +=1
    
    if len(tie) > 1 :
        first_pick = tie_breaker(tie,alphabet_freq,words_list) 
    
    print("First pick based on cost function:-  ",first_pick[0])
          
    
    
    # ----------------------------------#
    
    
    #--------- Second pick ------------ #
    second_pick_word_list = []
    for word in words_list:
        if not set(word).intersection(set(first_pick[0])):
            second_pick_word_list.append(word)
            
    # alphabet_freq = char_freq(second_pick_word_list)         
            
    second_pick_cost_list = pick_word(second_pick_word_list,char_freq(second_pick_word_list) )  
    
    print("-------Second Pick-----------")
    
    second_pick = second_pick_cost_list[0]
   
    
    # Top 20 picks for 1st word
    print("Top 20 picks for 2nd word:- ",second_pick_cost_list[0:21])
      
    pos = 1
    tie = []
    tie.append(second_pick[0])
    while second_pick_cost_list[pos][1] == second_pick[1]:
        tie.append(second_pick_cost_list[pos][0])
        pos +=1
    
    if len(tie) > 1 :
        second_pick = tie_breaker(tie,alphabet_freq,words_list) 
    
    print("Second pick based on cost function:-  ",second_pick[0])
          
            
    #-----------------------------------# 
    
    #------------ Third pick --------------#
    third_pick_word_list = []
    for word in second_pick_word_list:
        if not set(word).intersection(set(second_pick[0])):
            third_pick_word_list.append(word)
            
    # alphabet_freq = char_freq(third_pick_word_list)         
            
    third_pick_cost_list = pick_word(third_pick_word_list,char_freq(third_pick_word_list)  )  
    
    print("-------Third Pick-----------")
    
    
    third_pick = third_pick_cost_list[0]
    
    
    # Top 20 picks for 1st word
    print("Top 20 picks for 3rd pick word:- ",third_pick_cost_list[0:21])
    
    
    
    pos = 1
    tie = []
    tie.append(third_pick[0])
    while third_pick_cost_list[pos][1] == third_pick[1]:
        tie.append(third_pick_cost_list[pos][0])
        pos +=1
    
    if len(tie) > 1 :
        third_pick = tie_breaker(tie,alphabet_freq,words_list) 
    
    print("Third pick based on cost function:-  ",third_pick[0])
    
    # -------------------------------------
 

# function to pick the best word from a list of words based on cost function
def pick_word(words_list,alphabet_freq):
    cost_list = {}
    
    for word in words_list:
        cost_list[word] = cost_function(alphabet_freq,word)
    
    cost_sorted_words = sorted(cost_list.items(), key=lambda x: x[1],reverse=True)
    
    return cost_sorted_words
 
#  function used to break ties based on chances
def tie_breaker(list_tie,alphabet_list,word_list):
    chances = {}  
    for word in list_tie:
        chances[word] = chance(alphabet_list,word,word_list)
    sorted_words = sorted(chances.items(), key=lambda x: x[1],reverse=True)
    
    return sorted_words[0]    
        
        
           
#  chance of each word is probabilty of first, last and all biagrams
# divided by no of values in this case 6
def chance(alphabet_list,word,word_list):
    total_chance = 0 
    n = 6
    
    first_pos_chance = (alphabet_list[word[0]][0]/len(word_list))
    last_pos_chance =  (alphabet_list[word[-1]][-1]/len(word_list))
    
    # all possible biagram list
    bigram_list=[]
    
    for word in word_list:
        for pos in range(len(word)-1):
            bigram_word = ''
            bigram_word =  (word[pos]  + word[pos+1])
            bigram_list.append(bigram_word)
   
#    addding biagram of word to a list
    word_bigram =[]
    
    for char_pos in range(0,4):
        bi_char = word[char_pos]+ word[char_pos+1]
        word_bigram.append(bi_char)
    
        
    for values in word_bigram:
        total_chance += (bigram_list.count(values)/ len(bigram_list))
        
    total_chance += (first_pos_chance + last_pos_chance)
    total_chance = total_chance/n   
    
    
    return total_chance
        
        
    
 
 # function created to find the max used alphabets at each position     
def char_freq(word_list):
    # dict for all alphabet counts since there are only 5 letter words here last value is the total
    alphabet_freq_dict = {chr(i): [0,0,0,0,0] for i in range(ord('a'), ord('z')+1)}   
        
    for word in word_list:
        for char in range(len(word)):
            # here we update the dict of all the characters at the respective position
            alphabet_freq_dict[word[char]][char] += 1         
    
    return alphabet_freq_dict    
 
 
 
# cost function : Here the objective function is considered to be letter freq and 
# regularization is considered to be 1st char
# Here the higher the cost funtion the better it is

def cost_function(alphabet_freq,word):
    new_word = ''
    if len(word) != len(set(word)):
        set_val = set(word)
        for val in set_val:
            new_word += val
        word = new_word    

    cost =  get_letter_freq_val(alphabet_freq,word) + get_start_value(alphabet_freq,word[0]) 
    
    return cost
    

# getting the frequency of each letter based on the total occurence of each letter in the wordlist
def get_letter_freq_val(alphabet_freq,word):
    total_freq = 0
    for char_pos in range(len(word)):
        total_freq += sum(alphabet_freq[word[char_pos]])
    return total_freq
    
   
# value of 1st char occuring in the entire word list 
def get_start_value(alphabet_freq,word):
    return alphabet_freq[word[0]][0]       
    
if __name__ == '__main__':
    main()
        