# Imports
import time
import os
import pyotp
import qrcode
import pygame
import cv2
import face_recognition

#--------------------------------------------------------------
#                           GENERAL
#--------------------------------------------------------------
# Global variable that holds username
global username

# Function for "clearing" console
def clearConsole():
    print(50 * "\n")

# Function for generating seperation lines
def addLines():
    lines = 75 * "-"
    return lines

# Function for printing main menu text
def printMenu():
    clearConsole()
    print(addLines() + "\nUsername: " + username)
    print(addLines() + "\nMenu\n" + addLines())
    print("1. Multi-Factor")
    print("2. Graphical Password (1st factor)")
    print("3. Facial Recognition (2nd factor)")
    print("4. One-Time Password (3rd factor)")
    print("0. Exit")
    print(addLines())

# Function for printing submenu text
def printSubmenu(submenuText):
    clearConsole()
    print(addLines() + "\n" + submenuText + "\n" + addLines())
    print("1. Set up", submenuText)
    print("2. Test", submenuText)
    print("0. Exit")
    print(addLines())

# Function for printing text if the factor test succeded or failed
def printTest(checkSuccess):
    if(checkSuccess == True):
        input("Success! Press ENTER to continue...")
    elif(checkSuccess == False):
        input("Failed! Press ENTER to continue...")
                
#--------------------------------------------------------------
#                     GRAPHICAL PASSWORD
#--------------------------------------------------------------
# Function for appending value to graphical password set if not present already
def appendGraphicalPasswordSet(tmp, num):
    # If the number is not in the set of tmp, append the number
    if(num not in tmp):
        tmp.append(num)
    # Return the set
    return tmp

# Function for handling the GUI and pattern of graphical passwords
def guiGrahpicalPassword():
    # Initialize pygame
    pygame.init()
    
    # Window size
    SIZE = 600

    # Colors
    GREY = (192, 192, 192)
    BLUE = (150,200,250)
    BLACK = (32,32,32)

    # Window
    window = pygame.display.set_mode((SIZE,SIZE))
    window.fill(BLACK)
    pygame.display.set_caption("Graphical Password")

    # Dots
    # Top
    pygame.draw.circle(window, GREY, (100,100), 50)
    pygame.draw.circle(window, GREY, (300,100), 50)
    pygame.draw.circle(window, GREY, (500,100), 50)

    # Middle
    pygame.draw.circle(window, GREY, (100,300), 50)
    pygame.draw.circle(window, GREY, (300,300), 50)
    pygame.draw.circle(window, GREY, (500,300), 50)

    # Bottom
    pygame.draw.circle(window, GREY, (100,500), 50)
    pygame.draw.circle(window, GREY, (300,500), 50)
    pygame.draw.circle(window, GREY, (500,500), 50)

    # Set for appending graphical password values
    setGraphicalPassword = []

    # Graphical password loop variable
    loopBool = True

    # Graphical password GUI loop
    while(loopBool):
        # Update display
        pygame.display.update()
            
        # Exception handling for mouse out of window
        try:
            for event in pygame.event.get():
                # Exit window
                if(event.type == pygame.QUIT):
                    loopBool = False
                # Capture mouse movement while pressed
                if(pygame.mouse.get_pressed()[0]):
                    # ----- Top -----
                    # Left
                    if((50 <= event.pos[0] <= 150) and (50 <= event.pos[1] <= 150)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 1)
                        pygame.draw.circle(window, BLUE, (100,100), 50)
                    # Middle
                    elif((250 <= event.pos[0] <= 350) and (50 <= event.pos[1] <= 150)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 2)
                        pygame.draw.circle(window, BLUE, (300,100), 50)
                    # Right
                    elif((450 <= event.pos[0] <= 550) and (50 <= event.pos[1] <= 150)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 3)
                        pygame.draw.circle(window, BLUE, (500,100), 50)
                    # ----- Middle -----
                    # Left
                    elif((50 <= event.pos[0] <= 150) and (250 <= event.pos[1] <= 350)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 4)
                        pygame.draw.circle(window, BLUE, (100,300), 50)
                    # Middle
                    elif((250 <= event.pos[0] <= 350) and (250 <= event.pos[1] <= 350)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 5)
                        pygame.draw.circle(window, BLUE, (300,300), 50)
                    # Right
                    elif((450 <= event.pos[0] <= 550) and (250 <= event.pos[1] <= 350)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 6)
                        pygame.draw.circle(window, BLUE, (500,300), 50)
                    # ----- Bottom -----
                    # Left
                    elif((50 <= event.pos[0] <= 150) and (450 <= event.pos[1] <= 550)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 7)
                        pygame.draw.circle(window, BLUE, (100,500), 50)
                    # Middle
                    elif((250 <= event.pos[0] <= 350) and (450 <= event.pos[1] <= 550)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 8)
                        pygame.draw.circle(window, BLUE, (300,500), 50)
                    # Right
                    elif((450 <= event.pos[0] <= 550) and (450 <= event.pos[1] <= 550)):
                        setGraphicalPassword = appendGraphicalPasswordSet(setGraphicalPassword, 9)
                        pygame.draw.circle(window, BLUE, (500,500), 50)
                # If mouse click is released
                if(event.type == pygame.MOUSEBUTTONUP):
                    time.sleep(0.5)
                    loopBool = False
        # Exception handling for mouse out of window
        except:
            pass

    # Quit pygame
    pygame.quit()

    # String for complete graphical password value (merge set into string)
    stringGraphicalPassword = ""

    # Transform graphical password set to string
    for i in setGraphicalPassword:
        stringGraphicalPassword += str(i)

    # Return string
    return stringGraphicalPassword

# Function for setting up graphical password
def setupGraphicalPassword():
    # Set global graphical password
    global graphicalPassword

    # Loop variable
    checkSuccess = False

    # Loop while loop variable is false
    while(not checkSuccess):
        # Print menu
        clearConsole()
        print(addLines() + "\n" + "Instructions for setting up Graphical Password" + "\n" + addLines())
        print("1. Draw pattern with your mouse by clicking and dragging over the circles")
        print("2. Finish by releasing mouse click")
        print("3. Test Graphical Password")
        print(addLines())

        # Set up graphical password
        graphicalPassword = guiGrahpicalPassword()
        
        # If graphical password is shorter than 4
        if(int(len(graphicalPassword) < 4)):
            graphicalPassword = None
            checkSuccess = False
            input("Graphical password too short! Press ENTER to continue...")
        # Else set up complete
        else:
            checkSuccess = True
            input("Set up complete. Press ENTER to continue...")

# Function for testing graphical password
def testGraphicalPassword():
    # Print menu
    clearConsole()
    print(addLines() + "\n" + "Test Graphical Password" + "\n" + addLines())

    # Check if graphical password is empty
    if(graphicalPassword != ""):
        # Get temporary graphical password
        tmpGraphicalPassword = guiGrahpicalPassword()
        # Check if graphical passwords are identical (return true or false)
        if(tmpGraphicalPassword == graphicalPassword):
            return True
        else:
            return False

#--------------------------------------------------------------
#                      FACIAL RECOGNITION
#--------------------------------------------------------------
# Function for setting up facial recognition
def setupFacialRecognition():
    # Print menu
    clearConsole()
    print(addLines() + "\n" + "Instructions for setting up Facial Recognition" + "\n" + addLines())
    print("1. Look into the webcam")
    print("2. Press ENTER when ready")
    print("3. Test Facial Recognition")
    print(addLines())

    # Define webcam device
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Wait for user
    input("Press ENTER to continue...")

    # Loop for saving 15 images
    for count in range(15):
        # Set bool if getting webcam successfully and set webcam image variable
        checkImage, image = webcam.read()

        # Check if webcam is successfully read
        if(not checkImage):
            print("Failed to get webcam!")
            break

        # Display feed from webcam
        cv2.imshow("Facial Recognition", image)

        # Wait 100 milliseconds, then save image
        if(cv2.waitKey(100)):
            cv2.imwrite(username + str(count) + ".png", image)

    # Release webcam 
    webcam.release()

    # Close windows
    cv2.destroyAllWindows()

    # Set up complete
    input(addLines() + "\n" + "Set up complete. Press ENTER to continue...")

# Function for testing facial recognition
def testFacialRecognition():
    # Print menu
    clearConsole()
    print(addLines() + "\n" + "Test Facial Recognition" + "\n" + addLines())
    print("Testing in progress..." + "\n" + addLines())
    
    # Array for holding face encodings from set up
    userEncoding = []

    # Populate array with face encodings based on username + filenames in folder
    for file in os.listdir():
        if(file.startswith(username)):       
            userEncoding.append(face_recognition.face_encodings(face_recognition.load_image_file(str(file)))[0])

    # Define webcam device
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Counts
    totalCount = 0
    matchCount = 0

    # Loops until unknown face has been matched 10 times or total number of loops exceed 20
    while(matchCount < 10 and totalCount < 20):
        # Set bool if getting webcam successfully and webcam image variable
        checkImage, image = webcam.read()

        # Check if webcam is successfully read
        if(not checkImage):
            print("Failed to get webcam!")
            break

        # Display feed from webcam
        cv2.imshow("Facial Recognition", image)

        # Get webcam image every 1 millisecond
        if(cv2.waitKey(1)):
            # Variable for encodings of face from live webcam
            unknownEncoding = face_recognition.face_encodings(image, face_recognition.face_locations(image))

            # For each face from images in folder, compare live face from webcam
            for i in userEncoding:
                # Compare faces
                try:
                    match = face_recognition.compare_faces(i, unknownEncoding)[0]
                # Catch exception when no face is detected
                except:
                    match = False

        # Count matches
        if(match == True):
            matchCount += 1
        
        # Count total
        totalCount += 1

    # Release webcam 
    webcam.release()

    # Close windows
    cv2.destroyAllWindows()

    # Return True if number of matched images was 10
    if(matchCount == 10):
        return True
    elif(matchCount == 10 and totalCount == 20):
        return True
    else:
        return False

#--------------------------------------------------------------
#                    ONE-TIME PASSWORD
#--------------------------------------------------------------
# Function for setting up one-time password
def setupOneTimePassword():
    # Set global one-time password
    global oneTimePassword
   
    # Print menu
    clearConsole()
    print(addLines() + "\n" + "Instructions for setting up One-Time Password" + "\n" + addLines())
    print("1. Scan QR code from 'qrcode.png' with authenticator application")
    print("2. Test One-Time Password")
    
    # Generate one-time password with random secret key
    oneTimePassword = pyotp.TOTP(pyotp.random_base32())

    # Generate one-time password URI
    uriOneTimePassword = oneTimePassword.provisioning_uri(name=username)

    # Generate QR code from the URI
    img = qrcode.make(uriOneTimePassword)

    # Save QR code as image
    img.save('qrcode.png')

    # Open generated QR code image
    os.startfile("qrcode.png")

    # Set up complete
    input(addLines() + "\n" + "Set up complete. Press ENTER to continue...")

# Function for testing one-time password
def testOneTimePassword():
    # Print menu
    clearConsole()
    print(addLines() + "\n" + "Test One-Time Password" + "\n" + addLines())

    # Check if one-time password is not empty
    if(oneTimePassword != ""):
        # Wait for user input
        textInput = input("Enter One-Time Password: ")
        print(addLines())

        # Check if one-time password is identical (return true or false)
        if(textInput == oneTimePassword.now()):
            return True
        else:
            return False

#--------------------------------------------------------------
#                           MAIN
#--------------------------------------------------------------
# Set username
clearConsole()
print(addLines())
username = input("Enter username: ")
print(addLines())

# Main loop for menu
while(True):
    # Print main menu
    printMenu()
    choice = input("Enter your choice [0-4]: ") 

    # Multi-factor 
    if choice == "1":     
        # Loop for multi-factor
        while(True):
            # Print submenu
            printSubmenu("Multi-Factor")
            choice = input("Enter your choice [0-2]: ")

            # Set up multi-factor factors
            if choice == "1":
                setupGraphicalPassword()
                setupFacialRecognition()
                setupOneTimePassword()
            # Test multi-factor
            elif choice == "2":
                # Loop for testing multi-factor
                while(True):
                    # Holds return value
                    checkSuccess = ""

                    # Exception handling for graphical password not set up
                    try:
                        checkSuccess = testGraphicalPassword()
                    except:
                        input("Please set up the Graphical Password factor. Press ENTER to continue...")
                        break
                    # Print text based on boolean
                    printTest(checkSuccess)
                    # If false, print message and exit loop
                    if(checkSuccess == False):
                        clearConsole()
                        print(addLines() + "\n" + "Test Multi-Factor")
                        input(addLines() + "\nFailed! Press ENTER to continue...")
                        break

                    # Exception handling for facial recognition not set up
                    try:
                        checkSuccess = testFacialRecognition()
                    except:
                        input("Please set up the Facial Recognition factor. Press ENTER to continue...")
                        break
                    # Print text based on boolean
                    printTest(checkSuccess)
                    # If false, print message and exit loop
                    if(checkSuccess == False):
                        clearConsole()
                        print(addLines() + "\n" + "Test Multi-Factor")
                        input(addLines() + "\nFailed! Press ENTER to continue...")
                        break

                    # Exception handling for one-time password not set up
                    try:
                        checkSuccess = testOneTimePassword()
                    except:
                        input("Please set up the One-Time Password factor. Press ENTER to continue...")
                        break
                    # Print text based on boolean
                    printTest(checkSuccess)
                    # If false, print message and exit loop
                    if(checkSuccess == False):
                        clearConsole()
                        print(addLines() + "\n" + "Test Multi-Factor")
                        input(addLines() + "\nFailed! Press ENTER to continue...")
                        break
                    
                    # Print message when test was successfully completed
                    clearConsole()
                    print(addLines() + "\n" + "Test Multi-Factor")
                    input(addLines() + "\nSuccess! Press ENTER to continue...")

                    # Exit loop
                    break
            # Exit submenu
            elif choice == "0":
                print(addLines() + "\n" + "Exiting...")
                time.sleep(0.5)
                break
            # Invalid input handling
            else:
                input(addLines() + "\n" + "Invalid input. Press ENTER to continue...")
    # Graphical password
    elif choice == "2":
        # Loop for graphical password
        while(True):
            # Print submenu
            printSubmenu("Graphical Password")
            choice = input("Enter your choice [0-2]: ")

            # Set up graphical password
            if choice == "1":
                setupGraphicalPassword()
            # Test graphical password
            elif choice == "2":
                # Holds return value
                checkSuccess = ""
                # Exception handling for graphical password not set up
                try:
                    checkSuccess = testGraphicalPassword()
                except:
                    input("Please set up Graphical Password. Press ENTER to continue...")

                # Print text based on boolean
                printTest(checkSuccess)
            # Exit submenu
            elif choice == "0":
                print(addLines() + "\n" + "Exiting...")
                time.sleep(0.5)
                break
            # Invalid input handling
            else:
                input(addLines() + "\n" + "Invalid input. Press ENTER to continue...")
    # Facial recognition
    elif choice == "3":
        # Loop for facial recognition
        while(True):
            # Print submenu
            printSubmenu("Facial Recognition")
            choice = input("Enter your choice [0-2]: ")

            # Set up facial recognition
            if choice == "1":
                setupFacialRecognition()
            # Test facial recognition
            elif choice == "2":
                # Holds return value
                checkSuccess = ""
                # Exception handling for facial recognition not set up
                try:
                    checkSuccess = testFacialRecognition()
                except:
                    input("Please set up Facial Recognition. Press ENTER to continue...")

                # Print text based on boolean
                printTest(checkSuccess)
            # Exit submenu
            elif choice == "0":
                print(addLines() + "\n" + "Exiting...")
                time.sleep(0.5)
                break
            # Invalid input handling
            else:
                input(addLines() + "\n" + "Invalid input. Press ENTER to continue...")
    # One-time password
    elif choice == "4":
        # Loop for one-time password
        while(True):
            # Print submenu
            printSubmenu("One-Time Password")
            choice = input("Enter your choice [0-2]: ")

            # Set up one-time password
            if choice == "1":
                setupOneTimePassword()
            # Test one-time password
            elif choice == "2":
                # Holds return value
                checkSuccess = ""
                # Exception handling for one-time password not set up
                try:
                    checkSuccess = testOneTimePassword()
                except:
                    input("Please set up One-Time Password. Press ENTER to continue...")

                # Print text based on boolean
                printTest(checkSuccess)
            # Exit submenu
            elif choice == "0":
                print(addLines() + "\n" + "Exiting...")
                time.sleep(0.5)
                break
            # Invalid input handling
            else:
                input(addLines() + "\n" + "Invalid input. Press ENTER to continue...")
    # Exit loop
    elif choice == "0":
        print(addLines() + "\n" + "Exiting...")
        # Delete image files in folder
        for file in os.listdir():
            if(file.endswith(".png")):
                os.remove(file)
        time.sleep(0.5)
        break
    # Invalid input handling
    else:
        input(addLines() + "\n" + "Invalid input. Press ENTER to continue...")