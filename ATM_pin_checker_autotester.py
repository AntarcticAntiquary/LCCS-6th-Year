def load_pins_from_file(filename):
    """
    Load PIN data from external text file.
    File format: Each line contains account_number,pin
    Example: 12345678,1234
    
    Returns a dictionary with account numbers as keys and PINs as values.
    """
    pins = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    account, pin = line.split(',')
                    pins[account] = pin
        return pins
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def validate_pin_format(pin):
    """
    Validate that PIN meets format requirements.
    PIN must be exactly 4 digits.
    
    Returns True if valid, False otherwise.
    """
    if len(pin) != 4:
        return False
    if not pin.isdigit():
        return False
    return True


def verify_pin(account_number, filename='pins.txt'):
    """
    Verify ATM PIN with the following rules:
    - PINs are 4 digits long
    - Allow 3 attempts to enter correct PIN
    - Card locked after 3 failed attempts
    - Uses loop and counter for attempt tracking
    - PINs stored in external text file
    
    Returns True if PIN verified successfully, False if card locked.
    """
    # Load PINs from file
    pins_database = load_pins_from_file(filename)
    
    if pins_database is None:
        print("Unable to verify PIN. System error.")
        return False
    
    # Check if account exists
    if account_number not in pins_database:
        print("Account not found.")
        outputs[test][0] = False
        return False
    
    outputs[test][0] = True
    
    stored_pin = pins_database[account_number]
    
    # Initialize counter for failed attempts
    attempt_counter = 0
    max_attempts = 3
    
    print(f"Welcome! You have {max_attempts} attempts to enter your PIN.")
    
    # Loop to allow multiple PIN entry attempts
    while attempt_counter < max_attempts:
        # Get PIN from user
        #entered_pin = input(f"\nAttempt {attempt_counter + 1}/{max_attempts} - Enter your 4-digit PIN: ")
        entered_pin = currentInputs[attempt_counter]
        
        # Validate PIN format
        if not validate_pin_format(entered_pin):
            print("Invalid PIN format. PIN must be exactly 4 digits.")
            outputs[test][attempt_counter + 1] = 'I'
            attempt_counter += 1
            remaining_attempts = max_attempts - attempt_counter
            
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempt(s) remaining.")
            continue
        
        # Check if PIN matches
        if entered_pin == stored_pin:
            print("\n✓ PIN verified successfully!")
            print("Access granted. Welcome to your account.")
            outputs[test][attempt_counter + 1] = 'P'
            return True
        else:
            # Increment counter for failed attempt
            outputs[test][attempt_counter + 1] = 'F'
            attempt_counter += 1
            remaining_attempts = max_attempts - attempt_counter
            
            if remaining_attempts > 0:
                print(f"✗ Incorrect PIN. You have {remaining_attempts} attempt(s) remaining.")
            else:
                print("\n✗ Incorrect PIN.")
    
    # If loop completes without successful verification, card is locked
    print("\n⚠ CARD LOCKED ⚠")
    print("You have exceeded the maximum number of attempts.")
    print("Please contact your bank to unlock your card.")
    return False


def main():
    """
    Main function to run the ATM PIN verification system.
    """
    print("=" * 50)
    print("ATM PIN VERIFICATION SYSTEM")
    print("=" * 50)
    
    #account_number = input("\nEnter your account number: ")
    account_number = currentAccountNo
    
    # Verify PIN
    success = verify_pin(account_number)
    
    if success:
        print("\nYou may now proceed with your transaction.")
    else:
        print("\nTransaction cancelled.")

# Testing variables
inputs = {0: ['12345678', '1234', '1234', '1234'],
          1: ['87654321', '5678', '1234', '1234'],
          2: ['11223344', '0000', '1234', '1234'],
          3: ['99887766', '9999', '1234', '1234'],
          4: ['55667788', '1111', '1234', '1234'],
          5: ['12345678', '5049', '5049', '5049'],
          6: ['12345678', '0105', '1234', '1234'],
          7: ['12345678', '4321', '2905', '1234'],
          8: ['12345678', '1121', '9882', '8601'],
          9: ['12345678', '5o49', '54o9', '549o'],
          10: ['12345678', '3.141', '31.41', '314.1'],
          11: ['12345678', '105', '105', '105'],
          12: ['12345678', '31415', '31415', '31415'],
          13: ['12345678', '', '', ''],
          14: ['12345678', '1334', '2234', '1233'],
          15: ['13456789', '1234', '1234', '1234'],
          16: ['1234567', '1234', '1234', '1234'],
          17: ['123456789', '1234', '1234', '1234'],
         }

expectedoutputs = {0: [True, 'P', None, None],
                   1: [True, 'P', None, None],
                   2: [True, 'P', None, None],
                   3: [True, 'P', None, None],
                   4: [True, 'P', None, None],
                   5: [True, 'F', 'F', 'F'],
                   6: [True, 'F', 'P', None],
                   7: [True, 'F', 'F', 'P'],
                   8: [True, 'F', 'F', 'F'],
                   9: [True, 'I', 'I', 'I'],
                   10: [True, 'I', 'I', 'I'],
                   11: [True, 'I', 'I', 'I'],
                   12: [True, 'I', 'I', 'I'],
                   13: [True, 'I', 'I', 'I'],
                   14: [True, 'F', 'F', 'F'],
                   15: [False, None, None, None],
                   16: [False, None, None, None],
                   17: [False, None, None, None],
                   }

outputs = {}

currentAccountNo = 0
currentInputs = []

# Run the program
if __name__ == "__main__":
    for test in inputs:
        outputs[test] = [None, None, None, None]
        currentAccountNo = inputs[test][0]
        currentInputs = inputs[test][1:]
        main()
    print()
    print()
    print()
    for test in outputs:
        print(f'{test}: {outputs[test]}\t{expectedoutputs[test]}')
    
