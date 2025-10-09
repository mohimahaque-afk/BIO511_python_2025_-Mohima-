# Example code

# Make a list
print("Exercises")
mylist = ["A", "list", "can", "contain", "strings", "and", "numbers", 2]
# You can double check if it's a list
print(type(mylist))

# print your list
print(mylist)

# print the first item in your list
print(mylist[0])
#############################################################################################################
print("\n", "Task: 3.1 - Simple Loops")

quotes_list = ["Just Do It!", 
               "Alla är lika värda.", 
               "You only live once.", 
               "Do not let anybody tell you what to do.", 
               "It is what it is.", 
               "Ignorance is bliss.", 
               "Breakfast is the most important meal of the day."]
print("Here are some quotes hyped in current global village of social media regardless of how correct they may or may not be:\n")
for n, i in enumerate(quotes_list):
    print(f"{n+1}. {i}")
    if n >= 4:
        break

print("\n", "Task: 3.2 - Nested Loops")

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['CCA', 'TGT', 'GTA', 'TAG']
for sequence in sequences:
  for codon in codons:
    if codon in sequence:
      print(codon + " is in " + sequence)

print("3.2.1: Nested for loop that looks for start and stop codons in the sequences list.")
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
start_codon = 'ATG'
stop_codons =  ['TAA', 'TAG', 'TGA']
for nr, sequence in enumerate(sequences):
    for stop_codon in stop_codons:
        if stop_codon in sequence: 
            print(f"Stop Codon {stop_codon} is in {nr+1} {sequence}.")
        elif start_codon in sequence:
            print(f"Start Codon {start_codon} is in {nr+1} {sequence}") 
        elif start_codon and stop_codon in sequence:
            print(f"Start codon {start_codon} and Stop Codon {stop_codon} is in {nr+1} {sequence}.")

print("\n")
print("3.2.1: Where start codon is before stop codon")
print("\n")


for nr, sequence in enumerate(sequences):
    start_pos = sequence.find('ATG')
    stop_codon1_pos = sequence.find('TAA')
    stop_codon2_pos = sequence.find('TAG')
    stop_codon3_pos = sequence.find('TGA')
    if start_pos < stop_codon1_pos or start_pos < stop_codon2_pos or start_pos < stop_codon3_pos:
        print(f"Start codon comes before stop codon in {nr+1}th sequence{sequence}.")

        
print("\n")

print("3.2.2 Dictionary")
data = dict({'pat_001': ['bacZZt98', 'bac889Ytd'], 'pat_002': ['bac0GFrr'], 'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']})

bac_list= []

for bac in data.values():
    if bac not in bac_list:
        bac_list.append(bac)

bac_list = [item for sublist in bac_list for item in sublist]
bac_list = list(dict.fromkeys(bac_list))
bac_list

bac_dict = {key: '' for key in bac_list}
bac_dict


value_list = ['pat_001', 'pat_003'], ['pat_001', 'pat_003'], ['pat_002'], ['pat_003']

for i in range(len(bac_list)):
    bac_dict[bac_list[i]] = value_list[i]

bac_dict