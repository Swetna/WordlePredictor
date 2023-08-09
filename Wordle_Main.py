import wordle
import re
import Levenshtein


def main():  
              
               
    print("----------- Welcome to the Wordle Game-----------")

    while(True):
        
        file_path = "/Users/swetna/Desktop/Tribhuvan_Swetna_ProjectB/wordle_words.txt"
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
            
            
            # take input for the word to be guessed
        #  = wordle_word.lower()
    
        # if len(wordle_word) < 5 :
        #     print("Enter a 5 letter word:")
        
        matching_letters = {}
        possible_word = ['','','','','']
        impossible_chars = set()
        wrong_pos_chars = {}
        
        
        
        # decision tree implimentation for number of tries to guess word for each try
       
    #    first try
        word_feedback = []
        pick = wordle.pick_word(words_list,wordle.char_freq(words_list))
        
        pick = pick[0][0]
            
        print("Tries: ",1)
        print("Next word is: ",pick)
        
        letter_count = 1
        while letter_count < 6:
            word_feedback.append(int(input()))
            letter_count += 1 
        
        if len(set(word_feedback)) == 1 and word_feedback[0] == 2:
            print("Yayaya you guessed the correct word: ", pick , "in", 1 , "tries.")
        
        else:
            # second try
            matching_letters , possible_word , impossible_chars, wrong_pos_chars = compute_word(pick, matching_letters, possible_word ,  impossible_chars, wrong_pos_chars,word_feedback)
            words_list = filter_list(words_list,matching_letters,possible_word,impossible_chars,wrong_pos_chars)
            wrong_pos_chars = {}
            
            word_feedback = []
            pick = wordle.pick_word(words_list,wordle.char_freq(words_list))
            
            pick = pick[0][0]
                
            print("Tries: ",2)
            print("Next word is: ",pick)
            
            letter_count = 1
            while letter_count < 6:
                word_feedback.append(int(input()))
                letter_count += 1 
        
            if len(set(word_feedback)) == 1 and word_feedback[0] == 2:
                print("Yayaya you guessed the correct word: ", pick , "in", 2, "tries.")
            else:
                # third try
                matching_letters , possible_word , impossible_chars, wrong_pos_chars = compute_word(pick, matching_letters, possible_word ,  impossible_chars, wrong_pos_chars,word_feedback)
                words_list = filter_list(words_list,matching_letters,possible_word,impossible_chars,wrong_pos_chars)
                wrong_pos_chars = {}
                
                word_feedback = []
                pick = wordle.pick_word(words_list,wordle.char_freq(words_list))
                
                pick = pick[0][0]
                    
                print("Tries: ",3)
                print("Next word is: ",pick)
                
                letter_count = 1
                while letter_count < 6:
                    word_feedback.append(int(input()))
                    letter_count += 1 
            
                if len(set(word_feedback)) == 1 and word_feedback[0] == 2:
                    print("Yayaya you guessed the correct word: ", pick , "in", 3, "tries.")
                    
                else:
                    # fourth try
                    matching_letters , possible_word , impossible_chars, wrong_pos_chars = compute_word(pick, matching_letters, possible_word ,  impossible_chars, wrong_pos_chars,word_feedback)
                    words_list = filter_list(words_list,matching_letters,possible_word,impossible_chars,wrong_pos_chars)
                    wrong_pos_chars = {}
                    
                    word_feedback = []
                    pick = wordle.pick_word(words_list,wordle.char_freq(words_list))
                    
                    pick = pick[0][0]
                        
                    print("Tries: ",4)
                    print("Next word is: ",pick)
                    
                    letter_count = 1
                    while letter_count < 6:
                        word_feedback.append(int(input()))
                        letter_count += 1 
                
                    if len(set(word_feedback)) == 1 and word_feedback[0] == 2:
                        print("Yayaya you guessed the correct word: ", pick , "in", 4, "tries.")   
                    else:
                        
                        # 5th try
                        matching_letters , possible_word , impossible_chars, wrong_pos_chars = compute_word(pick, matching_letters, possible_word ,  impossible_chars, wrong_pos_chars,word_feedback)
                        words_list = filter_list(words_list,matching_letters,possible_word,impossible_chars,wrong_pos_chars)
                        wrong_pos_chars = {}
                        
                        word_feedback = []
                        pick = wordle.pick_word(words_list,wordle.char_freq(words_list))
                        
                        pick = pick[0][0]
                            
                        print("Tries: ",5)
                        print("Next word is: ",pick)
                        
                        letter_count = 1
                        while letter_count < 6:
                            word_feedback.append(int(input()))
                            letter_count += 1 
                    
                        if len(set(word_feedback)) == 1 and word_feedback[0] == 2:
                            print("Yayaya you guessed the correct word: ", pick , "in", 5, "tries.")  
                        else:
                            
                            # 6th try
                            matching_letters , possible_word , impossible_chars, wrong_pos_chars = compute_word(pick, matching_letters, possible_word ,  impossible_chars, wrong_pos_chars,word_feedback)
                            words_list = filter_list(words_list,matching_letters,possible_word,impossible_chars,wrong_pos_chars)
                            wrong_pos_chars = {}
                            
                            word_feedback = []
                            pick = wordle.pick_word(words_list,wordle.char_freq(words_list))
                            
                            pick = pick[0][0]
                                
                            print("Tries: ",6)
                            print("Next word is: ",pick)
                            
                            letter_count = 1
                            while letter_count < 6:
                                word_feedback.append(int(input()))
                                letter_count += 1 
                        
                            if len(set(word_feedback)) == 1 and word_feedback[0] == 2:
                                print("Yayaya you guessed the correct word: ", pick , "in", 6, "tries.")    
                                
                            else:
                                # out of tries
                                print("You are out of tries.")       
                
         
        continued = input("Do you want to continue? (Yes/No/y/n) :-")  
        
        if continued == 'no' or continued == 'No' or continued == 'n' or continued == 'N':
            print("Goodbye!")
            break
        
            
        
    
# returns a list with all words that could be possible for the guess word
def filter_list(word_list,matching_letters,possible_word,impossible_char,wrong_pos_chars):
    possible_word_str =   ''.join(str(chars) for chars in possible_word) 
    updated_word_list = []
    
   
#    for each word in word list we will keep only those words which match our criterios
    for word in word_list:
        # removing words containing words that are not in the guess word
        if not set(word).intersection(set(impossible_char)):
            if bool(wrong_pos_chars):
                for charsKey,posVal in wrong_pos_chars.items():
                    if word[posVal] != charsKey:
                        updated_word_list.append(word)
            else:
                updated_word_list.append(word)
                          
                    
                    
    final_updated_list = []   
    # matching with possible words 
    if not possible_word_str == '':
        for word in updated_word_list:
            for pos in range(0,5):
                if word[pos] == possible_word[pos]:
                    final_updated_list.append(word)
    else:
        return updated_word_list
                    
                    
                    
    return final_updated_list                
            
                        
                    
                    
# this function is analysing the word and comparing with a word feedback
        
def compute_word(pick, matching_letters, possible_word ,  impossible_chars,wrong_pos_words,word_feedback ):
    if len(set(word_feedback)) == 1 and word_feedback[0] == 2:
        print("Wordle word found: ",pick)
   
    else:   
        for pos in range(0,5):
            if word_feedback[pos] == 2:
                matching_letters[pick[pos]] = [2,pos]
                possible_word[pos] = pick[pos]
            elif word_feedback[pos] == 1:
                matching_letters[pick[pos]] = [1,pos] 
                wrong_pos_words[pick[pos]] = pos
            else: 
                impossible_chars.add(pick[pos])
                          
    return matching_letters,possible_word,impossible_chars,wrong_pos_words                      
      

# function to compute levenstein dist
def levin_dist(words_list,impossible_chars,possible_word_str):
    levin_distance = {}  
    for word in words_list:
        if not set(word).intersection(impossible_chars):
            distance = Levenshtein.distance(possible_word_str, word) 
            levin_distance[word] = distance  
    
    levin_distance = sorted(levin_distance.items(), key=lambda x: x[1],reverse= False)   
    
    return levin_distance
    
    
if __name__ == '__main__':
    main()
        