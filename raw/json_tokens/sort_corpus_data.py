import json
from unidecode import unidecode


test_code_raw = open('so16.tag.vert','r')
all_lines = test_code_raw.readlines()
adjectives_set = set()
nouns_set = set()
verbs_set = set()
pronouns_set = set()
prepositions_set = set()
determiners_set = set()
adverbs_set = set()
misc_set = set()



def remove_breaks_and_clean(line):
    if "<" in line:
        pass
    if "http" in line:
        pass 
    else:
        line_content = line.rsplit()
        word_tuple = tuple(line_content[::-1])
        return word_tuple

for line in all_lines:
     word_tuple = remove_breaks_and_clean(line)
     if word_tuple == None:
         pass
     else:
         if "ADJ" in word_tuple[0] and word_tuple[1].isalnum() == True:
             adjectives_set.add(unidecode(word_tuple[1]))
         if "NOUN" in word_tuple[0] and word_tuple[1].isalnum() == True:
             nouns_set.add(unidecode(word_tuple[1].lower()))
         if "VERB" in word_tuple[0] and word_tuple[1].isalnum() == True:
             verbs_set.add(unidecode(word_tuple[1].lower()))
         if "PRON" in word_tuple[0] and word_tuple[1].isalnum() == True:
             pronouns_set.add(unidecode(word_tuple[1].lower()))
         if "PREP" in word_tuple[0] and word_tuple[1].isalnum() == True:
             prepositions_set.add(unidecode(word_tuple[1].lower()))
         if "DET" in word_tuple[0] and word_tuple[1].isalnum() == True:
             determiners_set.add(unidecode(word_tuple[1].lower()))
         if "ADV" in word_tuple[0] and word_tuple[1].isalnum() == True:
             adverbs_set.add(unidecode(word_tuple[1].lower()))
         else:
             if len(word_tuple) > 1 and word_tuple[1].isalnum() == True:
                misc_set.add(unidecode(word_tuple[1].lower()))


adj_dict = {'adjectives': list(adjectives_set)}
with open('adjectives.json', 'w') as adj_file:
    json.dump(adj_dict, adj_file)

nouns_dict = {'nouns': list(nouns_set)}
with open('nouns.json', 'w') as nouns_file:
    json.dump(nouns_dict, nouns_file)

verbs_dict = {'verbs': list(verbs_set)}
with open('verbs.json', 'w') as verbs_file:
    json.dump(verbs_dict, verbs_file)

pronouns_dict = {'pronouns': list(pronouns_set)}
with open('pronouns.json', 'w') as pronouns_file:
    json.dump(pronouns_dict, pronouns_file)

preps_dict = {'prepositions': list(prepositions_set)}
with open('preposition.json', 'w') as prepositions_file:
    json.dump(preps_dict, prepositions_file)

determs_dict = {'determiners': list(determiners_set)}
with open('determiners.json', 'w') as determiners_file:
    json.dump(determs_dict, determiners_file)

adverbs_dict = {'adverbs': list(adverbs_set)}
with open('adverbs.json', 'w') as adverbs_file:
    json.dump(adverbs_dict, adverbs_file)

misc_dict = {'misc': list(misc_set)}
with open('misc.json', 'w') as misc_file:
    json.dump(misc_dict, misc_file)
