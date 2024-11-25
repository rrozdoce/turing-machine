class TuringMachine:
    def __init__(self, states=None, alphabet=None, transitions=None, initial_state=None, acceptance_states=None):
        self.states = states
        self.alphabet = alphabet if alphabet is not None else []
        self.transitions = transitions if transitions is not None else {}
        self.initial_state = initial_state
        self.acceptance_states = acceptance_states
        self.tape = []  # Tape symbols for the machine's head
        self.current_tape_index = 0
        self.tape_length = 0
        self.current_state = self.initial_state
        self.current_symbol = None
        self.input_word = None
    
    def main(self):
        self.read_user_inputs()
        option = 'YES'
        while option != 'NO':
            print("\n")
            self.reset()
            self.input_word = list(input("Enter the word to be verified: "))  # Get the word for verification
            self.write_word_to_tape()

            print('\nTuring Machine tape: ')
            response = self.read_tape()

            if response:
                print(f"The Turing machine accepted the word {''.join(self.input_word)}")
            else:
                print(f"The Turing machine rejected the word {''.join(self.input_word)}")
            
            option = input('Do you want to test more words on the same TM (YES or NO)?')
        
    def get_word(self):
        return self.input_word

    def read_user_inputs(self):
        self.states = input("Enter the states (comma-separated): ").split(",")
        self.alphabet = input("Enter the alphabet (comma-separated): ").split(",")
        self.transitions = {}

        print("Enter the transitions in the format 'next_state,new_symbol,direction' (e.g., 'q1,1,R'). Use '_' to keep the same symbol:")
        for state in self.states:
            for symbol in self.alphabet:
                entry = input(f"D({state},{symbol}): ").strip()
                if entry:  # Add transition only if input is provided
                    try:
                        next_state, new_symbol, direction = entry.split(',')
                        self.transitions[(state, symbol)] = (next_state, new_symbol, direction)
                    except ValueError:
                        print(f"Error: Invalid transition for D({state},{symbol}). Ignored.")
                else:
                    # Empty transitions are not recorded
                    continue

        self.initial_state = input("Enter the initial state: ").strip()
        self.acceptance_states = input("Enter the acceptance state(s) (comma-separated): ").split(",")

    def reset(self):
        self.tape = []  # Tape symbols for the machine's head
        self.current_tape_index = 0
        self.tape_length = 0
        self.current_state = self.initial_state
        self.current_symbol = None
        self.input_word = None
    
    def write_word_to_tape(self):
        for letter in self.input_word:
            self.tape.append(letter)
        self.tape.append('L|')  # 'L|' represents the end of the tape
    
    def move_right(self):
        if self.current_tape_index + 1 < len(self.tape):
            self.tape[self.current_tape_index] = self.current_symbol
            self.current_tape_index += 1  # Move to the right
            self.current_symbol = self.tape[self.current_tape_index]  # Update to the next symbol

    def move_left(self):
        if self.current_tape_index - 1 >= 0:
            self.tape[self.current_tape_index] = self.current_symbol
            self.current_tape_index -= 1  # Move to the left
            self.current_symbol = self.tape[self.current_tape_index]  # Update to the next symbol

    def read_tape(self) -> bool:
        # Read the first symbol before starting the loop
        self.current_symbol = self.tape[0]
        self.current_state = self.initial_state

        while True:
            if self.current_tape_index < 0 or self.current_tape_index >= len(self.tape):
                return False  # Machine rejects the word

            # Check if the current state is an acceptance state
            if self.current_state in self.acceptance_states:
                # Machine accepted the input!
                return True

            # Check for a valid transition
            if (self.current_state, self.current_symbol) not in self.transitions:
                # Machine rejects the input! No valid transition.
                return False

            # Execute the transition
            next_state, new_symbol, direction = self.transitions[(self.current_state, self.current_symbol)]
            print(f"Transition: ({self.current_state}, {self.current_symbol}) => {next_state}, {new_symbol}, {direction}")
            print(f"{self}")
            print()
            
            self.current_state = next_state  # Update to the next state
            if new_symbol != '_':
                self.current_symbol = new_symbol
            
            if direction == 'R':
                self.move_right()
            elif direction == 'L':
                self.move_left()

    def __str__(self):
        return f"Current symbol: {self.current_symbol}, Tape: {"".join(map(str, self.tape))}"

turing = TuringMachine()
turing.main()