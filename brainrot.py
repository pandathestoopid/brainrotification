# Let's code some brainrot chat

# ALL THE BRAINROTS
hawkTuah = {
    'name': 'hawk tuah',
    'id': 'hawk',
    'description': 'replaces "hawk" with your given word',
    'example': 'walk -> walk tuah',
    'multiword': True,
    'blackwords': ['huzz', 'rizzler', 'ussy']
}

huzz = {
    'name': 'huzz',
    'id': 'huzz',
    'description': 'appends "uzz" to your given word',
    'example': 'fish -> fuzz',
    'multiword': False
}

rizzler = {
    'name': 'rizzler',
    'id': 'rizz',
    'description': 'appends "izzler" to your given word',
    'example': 'autism -> tizzler',
    'multiword': False
}

tsPmo = {
    'name': 'ts pmo',
    'id': 'ts',
    'description': 'WIP',
    'example': 'WIP',
    'multiword': True
}

ussy = {
    'name': 'ussy',
    'description': 'appends "ussy" to your given word',
    'example': 'automaton -> automatussy',
    'multiword': True,
}

skibidi = {
    'name': 'skibidi dop dop yes yes',
    'id': 'skibidi',
    'description': 'turns your word into a skibidi dop dop yes yes song',
    'example': 'chess.com -> chess.com dop dop yes yes',
    'multiword': True,
    'preferences': True,
    'lengths': ('short', 'full', 'essay')
}

rotiender = {
    'name': 'rotiender',
    'id': 'rot',
    'description': 'turns your word into a oh nein rotiender meme',
    'example': 'low taper fade -> oh nein, ein vertikal rotiender low taper fade',
    'multiword': True,
    'preferences': True,
    'orientations': ('horizontal', 'vertikal', 'diagonal')
}

slur = {
    'name': 'slur',
    'id': 'slur',
    'description': 'turns your word into an n word variant',
    'example': 'fly -> fligger',
    'multiword': False,
}

allBrainrots = [hawkTuah, huzz, rizzler, ussy, skibidi, rotiender, slur]

singleWords = list(brainrot['name'] for brainrot in allBrainrots if brainrot['multiword'] == False)

# Gets the input word
def getInput():
    validInput = False
    while not validInput:
        # Input
        userInput = input('Enter the word you would like to brainrotify, or turn on AUTOROT by typing "auto": ')

        # Checker
        if userInput == '':
            print('You did not enter a word. Please try again, or alternatively, get a job.\n')

        # If the user has typed a brainrot word that does not support multi-word inputs
        elif userInput in singleWords:
            resume = input('It looks like you have put a brainrot word inside your input that does not support multi-word inputs. Type "auto" to continue with AUTOROT or type a different word. If you would like to continue anyway, type "continue".\n')
            if resume == 'auto':
                autoRot = True
                print('AUTOROT activated. If you wish to turn it off, do so when you next enter a brainrotify word.')
                return userInput, autoRot
            elif resume == 'continue':
                return userInput, autoRot
        elif userInput == 'auto':
            autoRot = True
            print('AUTOROT activated. Type your brainrot phrase to auto-format it into peak, Tik-Tok ready brainrot. If you wish to turn it off, type "manual".')
            print('Note: AUTOROT is not supported for all brainrot phrases.')
        elif userInput == 'manual':
            autoRot = False
            print('AUTOROT deactivated.')
        else:
            validInput = True
    return userInput, autoRot

# Checks the user input to compile a list of available brainrots
# def validateBrainrots():

# Gets the user to choose which brainrot to use
def selectBrainrot(userInput):
    validInput = False
    print('Here are all the options for brainrotifying your word:')
    for brainrot in availBrainrots:
        print(brainrot)
    print('To learn more about a specific brainrot, type "help <option name>"')
    print('If the brainrot method you wanted did not show up, type "why" to see the reasoning or type "back" to try a different word.')
    while not validInput:
        userInput = input('Select how you would like to turn your word into brainrot: ')
        if userInput == '':
            print('You did not enter a word. Type "back" if you want to try a different word.\n')
        elif userInput == 'why':
            print(logs)
        elif userInput == 'back':
            print('\n')
            return 'redo'
        # WIPWIPWIPWIPWIPWIP
        elif 'help' in userInput:
            newInput = userInput.replace('help ', '')
            print(allBrainrots[0]['name'])
        elif userInput in allBrainrots and userInput not in availBrainrots:
            print('This brainrot is not compatible with your word. Please try a different method or enter a new word.')
        elif userInput not in allBrainrots:
            print('You did not select a brainrot. Please try again.')
        else:
            validInput = True
    return userInput



# Main code
rotMethod = 'back'

print('Welcome to Brainrotifier.')
print(singleWords)

while rotMethod == 'back':
    wordToRot, autoRot = getInput()
    rotMethod = selectBrainrot(wordToRot)
