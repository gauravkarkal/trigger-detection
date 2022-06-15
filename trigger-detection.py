import re

def get_input_text():
    input = open("input.txt", "r")
    text = input.read()
    input.close()
    return text


def detect_trigger(words):
    index = 0
    go_links = []
    while index < len(words):
        if (words[index] == "go" and words[index+1] == "slash") or (words[index] == "go" and words[index+1] == "/"):
            index, go_link = get_go_link(words, index + 2)
            if go_link is not None:
                go_links.append('https://go/' + go_link)
        index = index + 1

    return go_links

def get_go_link(words, index):
    alpha_numeric_regex = "^[a-zA-Z0-9_-]*$"
    numeric_regex = "^[0-9]*$"
    go_link = []
    done = False
    while not done:
        done = True
        word = words[index]
        
        
        if not re.match(alpha_numeric_regex, word):
            print('Not Alpha Numeric: ', re.match(alpha_numeric_regex, word), word)
            return index, None


        go_link.append(word)
            

        if len(word) == 1 and index + 1 < len(words) and len(words[index + 1]) == 1 and words[index + 1] != "-": # Current and Next are Characters
            index = index + 1
            done = False

        elif index + 1 < len(words) and (words[index + 1] == "dash" or words[index + 1] == "-"):
            go_link.append("-")
            index = index + 2
            done = False

        elif index + 1 < len(words) and re.match(numeric_regex, words[index + 1]):
            go_link.append(words[index + 1])
            index = index + 1


    return index, ''.join(go_link)
        
        


def run_main():
    text = get_input_text()
    words = text.split()
    go_links = detect_trigger(words)
    print("Suggested go links: ")
    print('\n'.join(go_links))



if __name__ == "__main__":
    run_main()  