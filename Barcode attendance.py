import cv2
from pyzbar import pyzbar
import csv
import time
import winsound

def scan_barcode(ip_address, csv_file):
    # Create the video stream URL using the IP address and port of the IP Webcam app
    video_url = f"http://{ip_address}:8080/video"

    # Initialize the video capture device using the video stream URL
    cap = cv2.VideoCapture(video_url)

    scanned_barcodes = set()

    while True:
        # Read frame from the video capture device
        _, frame = cap.read()

        # Convert the frame to grayscale for barcode detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect barcodes in the frame
        barcodes = pyzbar.decode(gray)

        # Process each detected barcode
        for barcode in barcodes:
            # Extract the barcode value
            barcode_value = barcode.data.decode("utf-8")

            if barcode_value not in scanned_barcodes:
                # Add the barcode to the set of scanned barcodes
                scanned_barcodes.add(barcode_value)

                # Display the scanned barcode
                print("Scanned barcode:", barcode_value)

                # Write the barcode to the CSV file
                add_to_csv(barcode_value, csv_file)

                # Play a beep sound
                winsound.Beep(1000, 200)  # Frequency: 1000Hz, Duration: 200ms

                # Wait for 2 seconds before scanning the next barcode
                time.sleep(5)
            else:
                # Barcode has already been scanned
                print("You are in.")

        # Display the frame with barcode detection
        cv2.imshow("Barcode Scanner", frame)

        # Check for the "q" key to quit the program
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video capture device
    cap.release()

    # Close the OpenCV windows
    cv2.destroyAllWindows()

def add_to_csv(barcode_value, csv_file):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([barcode_value])

# Prompt the user to enter the IP address of the mobile device running the IP Webcam app
ip_address = input("Enter the IP address of the mobile device: ")

# Specify the CSV file path
csv_file = 'C:/Users/ZF-10/Desktop/MAchine learning/scanned_barcodes.csv'

# Call the scan_barcode function with the IP address and CSV file provided
scan_barcode(ip_address, csv_file)






import csv

def mark_attendance(strength_file, presentees_file, output_file):
    # Read the student strength and roll numbers from the strength file
    strength_data = read_csv(strength_file)
    strength_roll_numbers = [row[0] for row in strength_data]

    # Read the presentees roll numbers from the presentees file
    presentees_data = read_csv(presentees_file)
    presentees_roll_numbers = [row[0] for row in presentees_data]

    # Create a new CSV file for attendance
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(["Roll Number", "Attendance"])

        # Mark attendance for each roll number
        for roll_number in strength_roll_numbers:
            if roll_number in presentees_roll_numbers:
                attendance = "Present"
            else:
                attendance = "Absent"

            # Write the attendance record
            writer.writerow([roll_number, attendance])

def read_csv(file):
    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
    return data

# Specify the file paths for student strength, presentees, and output attendance
strength_file = "C:/Users/ZF-10/Desktop/MAchine learning/Bar code no..csv"
presentees_file = 'C:/Users/ZF-10/Desktop/MAchine learning/scanned_barcodes.csv'
output_file = 'C:/Users/ZF-10/Desktop/MAchine learning/attendance.csv'

# Mark the attendance based on the given files and save it to the output file
mark_attendance(strength_file, presentees_file, output_file)

print("Attendance has been generated and saved to", output_file)

