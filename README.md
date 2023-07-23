# CMC-Unicode-s2023
Containing unicode based software using python for language purposes. 
Sources: KPS9566 encoding wikapedia page: https://en.wikipedia.org/wiki/KPS_9566#:~:text=The%20syllables%20for%20Kim%20and,%2D78%20to%2004%2D80.
        
Source for encoding table : https://unicode.org/Public/MAPPINGS/VENDORS/MISC/KPS9566.TXT
         
Redstar OS : https://archiveos.org/redstar/
         
Virtual box: https://www.virtualbox.org/
         
         

  There are several key differences between the South Korean and North Korean languages. For starters, one key difference is how the alphabet is ordered. For example, the North  Korean alphabet has its double consonants  towards the end of the initial consonant ordering, with ㅇ as the vary last character. For vowels, the combination vowels come at the end. However, the South Korean alphabet has the double characters come after their corresponding single characters, for consonants. For vowels, the South Korean orders the combination vowels based on which vowel comes first. 

  In August 1999, the North Korean national body submitted a document to WG2, or the Working Group 2), which is the ISO body responsible for ISO/IEC 10646, the international standard corresponding to Unicode. This document requested that the KPS9566 encodings be added to the CJK Unified Ideographs Unicode block, which contains containing the most common CJK ideographs used in modern Chinese, Japanese, Korean and Vietnamese characters. It also requested the  addition of 80 symbol characters from KPS 9566, which did not have existing Unicode mappings, and 8 combining Jamo. It also requested for WG2 to reclassify the block names with the term “Korean Character” instead of “Hangul’ and to resolve the differences in the  collation order of the Korean alphabet between Unicode, which had ordered the Korean letters in the South Korean style, and KPS9566 encodings, which had ordered the Korean letters in the North Korean style.
  
  However, the DPRK’s proposal for additional characters also included separate encodings for its three leaders. Kim Il Sung, Kim Jong Il, and later, Kim Jong Un. This is because in North Korean texts, each character of the three leaders has their own encoding, from encoding A4E8 to A470. 
This proposal was rejected by WG2. In March of 2000, the Swedish representative wrote a detailed response, explaining why Sweeden voted against the proposal. It stated that most of the requests in that proposal could cause major disruptions if they were to be implemented. Regarding the collation issue, the representative recommended that North Korea provide a   machine-readable mapping file between Unicode and KPS 9566. For the additional characters, the response stated that logos, including political party logos, and special names of people should not be added to the Unicode. 

  To this day, several characters from KPS9566 haven’t been added to Unicode. It also is very difficult for people outside of North Korea to utilize these characters, since these characters only exist on north Korean software like Redstar OS. It is also impossible to run Redstar OS without a virtual machine. However, both Vmware and QEmu cannot read the iso type, while Virtual box was able to. Even still, finding the KPS9566 encoding files was equally as difficult. 

  Included in this repo are those encoding files, a text file that contains the correlation between KPS9566 and Unicode, a encoding table python file that houses the created table, and a python file that allows the defined encoding and decoding techniques to be used on any given text file. 


