# VEHICLE PARKING MANAGEMENT SYSTEM:

import streamlit as st
from datetime import datetime
import math

class Parking:
    def __init__(self):
        self.slots = [None] * 100

    def park(self, vehicle_number, vehicle_type):
        for vehicle in self.slots:
            if vehicle is not None:
                if vehicle["number"] == vehicle_number:
                    return None, "Vehicle is already parked!"
                
        for i in range(100):
            if self.slots[i] is None:
                self.slots[i] = {
                    "number": vehicle_number,
                    "type": vehicle_type,
                    "entry_time": datetime.now()
                }
                return i + 1, "Vehicle parked successfully!"
        return None, "Parking is full!"

    def remove(self, vehicle_number):
        for i in range(100):
            vehicle = self.slots[i]

            if vehicle is not None:
                if vehicle["number"] == vehicle_number:
                    exit_time = datetime.now()
                    entry_time = vehicle["entry_time"]
                    time = exit_time - entry_time
                    seconds = time.total_seconds()
                    hours = math.ceil(seconds / 3600)


                    if hours < 1:
                        hours = 1
                    fee = 40
                    amount = hours * fee
                    receipt = {
                        "slot": i + 1,
                        "number": vehicle["number"],
                        "type": vehicle["type"],
                        "entry": entry_time,
                        "exit": exit_time,
                        "hours": hours,
                        "amount": amount
                    }
                    self.slots[i] = None
                    return receipt
        return None

    def search(self, vehicle_number):
        for i in range(100):
            vehicle = self.slots[i]
            if vehicle is not None:
                if vehicle["number"] == vehicle_number:
                    return i + 1, vehicle
        return None, None

    def available(self):
        return self.slots.count(None)

    def occupied(self):
        return 100 - self.available()

st.set_page_config(page_title="Vehicle Parking System", page_icon="🚗", layout="wide")

if "parking" not in st.session_state:
    st.session_state.parking = Parking()

parking = st.session_state.parking

st.sidebar.title("🚗 Parking System")
st.sidebar.write("Vehicle Parking Management")
st.sidebar.divider()

choice = st.sidebar.radio("Select Option", [
    "Dashboard",
    "Park Vehicle",
    "Remove Vehicle",
    "Search Vehicle",
    "Parking Slots"
])

st.sidebar.divider()
st.sidebar.write("💰 Parking Fee")
st.sidebar.write("₹40 per hour")
st.sidebar.write("🅿️ Total Slots")
st.sidebar.write("100")

st.title("🚗 Vehicle Parking Management System")

if choice == "Dashboard":
    st.header("📊 Dashboard")
    total = 100
    occupied = parking.occupied()
    available = parking.available()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Slots", total)
    with col2:
        st.metric("Occupied", occupied)
    with col3:
        st.metric("Available", available)

    st.divider()
    st.subheader("🚘 Currently Parked Vehicles")
    found = False

    for i in range(100):
        vehicle = parking.slots[i]
        if vehicle is not None:
            found = True
            st.write(
                "🅿️ Slot:", i + 1,
                "| 🚗 Vehicle:", vehicle["number"],
                "| Type:", vehicle["type"],
                "| Entry:", vehicle["entry_time"].strftime("%d-%m-%Y %I:%M:%S %p")
            )

    if found == False:
        st.info("No vehicles are currently parked.")

elif choice == "Park Vehicle":
    st.header("🅿️ Park Vehicle")
    st.write("Enter the vehicle details.")

    vehicle_number = st.text_input(
        "Enter Vehicle Number",
        placeholder="Example: KL11AB1234"
    )

    vehicle_type = st.selectbox(
        "Select Vehicle Type",
        ["Car", "Bike"]
    )

    st.info("💰 Parking Fee: ₹40 per hour")

    if st.button("Park Vehicle"):
        if vehicle_number == "":
            st.error("Please enter vehicle number.")
        else:
            vehicle_number = vehicle_number.upper()
            slot, message = parking.park(vehicle_number, vehicle_type)

            if slot is not None:
                st.success(message)
                st.success("🚗 Vehicle Number: " + vehicle_number)
                st.success("🅿️ Parking Slot: " + str(slot))
                st.write(
                    "🕐 Entry Time:",
                    datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
                )
            else:
                st.error(message)

elif choice == "Remove Vehicle":
    st.header("🚪 Remove Vehicle")
    parked_vehicles = []

    for i in range(100):
        vehicle = parking.slots[i]
        if vehicle is not None:
            parked_vehicles.append(
                vehicle["number"] + " - Slot " + str(i + 1)
            )

    if len(parked_vehicles) == 0:
        st.info("No vehicles are currently parked.")
    else:
        selected_vehicle = st.selectbox(
            "Select Vehicle",
            parked_vehicles
        )

        vehicle_number = selected_vehicle.split(" - Slot")[0]

        if st.button("Remove Vehicle"):
            receipt = parking.remove(vehicle_number)

            if receipt is not None:
                st.success("✅ Vehicle removed successfully!")
                st.divider()
                st.subheader("🧾 Parking Receipt")

                st.write("🅿️ Parking Slot:", receipt["slot"])
                st.write("🚗 Vehicle Number:", receipt["number"])
                st.write("🚘 Vehicle Type:", receipt["type"])
                st.write(
                    "🕐 Entry Time:",
                    receipt["entry"].strftime("%d-%m-%Y %I:%M:%S %p")
                )
                st.write(
                    "🕐 Exit Time:",
                    receipt["exit"].strftime("%d-%m-%Y %I:%M:%S %p")
                )
                st.write(
                    "⏱️ Parking Duration:",
                    receipt["hours"],
                    "hour(s)"
                )
                st.write("💰 Parking Rate: ₹40/hour")
                st.success(
                    "💵 Total Amount: ₹" + str(receipt["amount"])
                )
            else:
                st.error("Vehicle not found!")

elif choice == "Search Vehicle":
    st.header("🔍 Search Vehicle")
    parked_vehicles = []

    for i in range(100):
        vehicle = parking.slots[i]
        if vehicle is not None:
            parked_vehicles.append(
                vehicle["number"] + " - Slot " + str(i + 1)
            )

    if len(parked_vehicles) == 0:
        st.info("No vehicles are currently parked.")
    else:
        selected_vehicle = st.selectbox(
            "Select Vehicle",
            parked_vehicles
        )

        vehicle_number = selected_vehicle.split(" - Slot")[0]

        if st.button("Search Vehicle"):
            slot, vehicle = parking.search(vehicle_number)

            if vehicle is not None:
                st.success("✅ Vehicle found!")
                st.divider()

                st.write("🚗 Vehicle Number:", vehicle["number"])
                st.write("🚘 Vehicle Type:", vehicle["type"])
                st.write("🅿️ Parking Slot:", slot)
                st.write(
                    "🕐 Entry Time:",
                    vehicle["entry_time"].strftime("%d-%m-%Y %I:%M:%S %p")
                )

                time = datetime.now() - vehicle["entry_time"]
                minutes = int(time.total_seconds() / 60)

                st.write("⏱️ Parked For:", minutes, "minute(s)")
                st.write("💰 Parking Rate: ₹40/hour")
            else:
                st.error("Vehicle not found!")

elif choice == "Parking Slots":
    st.header("🅿️ Parking Slots")
    st.write("🟢 Available = Empty Slot")
    st.write("🔴 Occupied = Vehicle Parked")
    st.divider()

    for i in range(100):
        vehicle = parking.slots[i]

        if vehicle is None:
            st.success("Slot " + str(i + 1) + " - 🟢 Available")
        else:
            st.error(
                "Slot " + str(i + 1) + " - 🔴 " + vehicle["number"]
            )