#initialization
#constants
FLOAT_SERVICE_CHARGE = 40.0
FLOAT_BATHROOM_CHARGE = 15.0
FLOAT_OTHER_ROOM_CHARGE = 10.0

stringCustomerLastName = ""
floatNumberOfBathrooms = 0.0
intNumberOfOtherRooms = 0
floatBathroomCost = 0.0
floatOtherRoomCost = 0.0
floatTotalCost = 0.0



#get data

stringCustomerLastName = input("Please enter customer last name?")

floatNumberOfBathrooms = float(input("Please enter the number of bathrooms to be cleaned: "))

intNumberOfOtherRooms = float(input("Please enter the number of other rooms to be cleaned: "))


#process data
floatBathroomCost = floatNumberOfBathrooms * FLOAT_BATHROOM_CHARGE
floatOtherRoomCost = intNumberOfOtherRooms * FLOAT_OTHER_ROOM_CHARGE
floatTotalCost = FLOAT_SERVICE_CHARGE + floatBathroomCost + floatOtherRoomCost

#output information
print("\nHazel's Housecleaning Service")
print(f"Base service fee: ${FLOAT_SERVICE_CHARGE}")
print(f"Number of bathrooms to be cleaned: {floatNumberOfBathrooms}     ${floatBathroomCost}")
print(f"Number of other rooms to be cleaned: {intNumberOfOtherRooms}     ${floatOtherRoomCost}")
print(f"Total cost: ${floatTotalCost}")
print("\nThank you for using Hazel's Housecleaning Service")
