def check_validity(text: str) -> str:
    bracket_groups = {'(': ')', '{': '}', '[': ']', '<': '>'}
    starting_bracket = set(bracket_groups.keys())
    ending_bracket = set(bracket_groups.values())
    tracker = []  

    for i in text:
        if i in starting_bracket:
            tracker.append(i)
        elif i in ending_bracket:
            if len(tracker)==0:
                return "Imbalanced count"
            last_char = tracker[-1]
            if bracket_groups[last_char] != i:
                return "No proper use of brackets."
            tracker.pop()
    if len(tracker)!=0:
        return "Imbalanced count"
    return "Valid"
def get_valid_invalid_text_count(texts):
    count_valid = 0
    count_invalid = 0
    
    for item in texts:
        if isinstance(item, str):
            if check_validity(item) == "Valid":
                count_valid += 1
            else:
                count_invalid += 1
    
    return count_valid, count_invalid
    
print(get_valid_invalid_text_count(["[" , "45{]" , "5[]{}"]))
