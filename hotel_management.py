import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Trenton02$',
    database='hotel_management'
)

# Create cursor
cursor = connection.cursor()

# Function to make reservation
def make_reservation(guest_info, check_in, check_out, room_preference):
    try:
        # Retrieve available rooms based on preferences
        cursor.execute("SELECT room_number FROM Rooms WHERE room_type = %s AND availability = 'available'", (room_preference,))
        available_rooms = cursor.fetchall()
        if not available_rooms:
            print("No available rooms matching your preferences.")
            return

        # Reserve first available room
        room_number = available_rooms[0][0]

        # Insert reservation record
        cursor.execute("INSERT INTO Reservations (guest_id, room_number, check_in, check_out) VALUES (%s, %s, %s, %s)",
                       (guest_info['guest_id'], room_number, check_in, check_out))
        connection.commit()

        print("Reservation successfully made!")
    except mysql.connector.Error as err:
        print("Error making reservation:", err)

# Function to display reservation details
def reservation_details(guest_id):
    try:
        # Retrieve reservation details for the guest
        cursor.execute("SELECT * FROM Reservations WHERE guest_id = %s", (guest_id,))
        reservations = cursor.fetchall()

        if not reservations:
            print("No reservations found for the guest.")
            return

        for reservation in reservations:
            print("Reservation ID:", reservation[0])
            print("Room Number:", reservation[2])
            print("Check-in Date:", reservation[3])
            print("Check-out Date:", reservation[4])
            print()
    except mysql.connector.Error as err:
        print("Error fetching reservation details:", err)

# Close cursor and connection
cursor.close()
connection.close()

# Example usage:
# Replace 'your_username' and 'your_password' with your MySQL username and password
# Replace 'guest_info' with guest information dictionary
# Replace 'check_in' and 'check_out' with check-in and check-out dates
# Replace 'room_preference' with room type preference (e.g., 'Single', 'Double', 'Suite')

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Trenton02$',
    database='hotel_management'
)

# Create cursor
cursor = connection.cursor()

# Example usage of functions
guest_info = {'guest_id': 1}  # Assuming guest ID 1 exists in the database
check_in = '2024-06-01'
check_out = '2024-06-05'
room_preference = 'Single'

make_reservation(guest_info, check_in, check_out, room_preference)

# Assuming the guest wants to view their reservation details
reservation_details(guest_info['guest_id'])

# Close cursor and connection
cursor.close()
connection.close()
