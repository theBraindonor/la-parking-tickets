/*
Copyright 2019, John Hoff <john.hoff@braindonor.net>
Creative Commons Attribution-ShareAlike 4.0 International License
*/

export const TicketTypes = {
    0: {
        name: 'Street Cleaning',
        description: 'Look for Street Cleaning Signs.  These will only apply to certain days and times.'
    },
    1: {
        name: 'Meter Expired',
        description: 'Be sure to check that your parking meter is not expired.'
    },
    2: {
        name: 'Red Zone',
        description: 'Be sure to check for a red-colored curb.  There is no stopping, parking or standing at these curbs.'
    },
    3: {
        name: 'Preferred Parking',
        description: 'Be sure to check for Permit Parking signs.  Parking may be restricted unless a vehicle displays the proper permit.'
    },
    4: {
        name: 'Display of Tabs/Plate',
        description: 'Be sure to double check your license plate and/or registration sticker.'
    },
    5: {
        name: 'No Parking',
        description: 'Be sure to check for No Parking signs.  Be sure to check if this only applies to certain days and times.'
    },
    6: {
        name: 'Parking Over Time Limit',
        description: 'Be sure to check for Time Limit Parking signs.  Time limit areas may also have meters.'
    },
    7: {
        name: 'White Zone',
        description: 'Be sure to check for a white-colored curb.  These are for passenger loading and unloading, but only for a maximum of five minutes.'
    },
    8: {
        name: 'No Stopping/Standing',
        description: 'Be sure to check for No Stopping signs.  May only apply to certain times and/or days.  Applies to residential and commercial vehicles.'
    },
    9: {
        name: 'Yellow Zone',
        description: 'Be sure to check for a yellow-colored curb.  Vehicles without a commercial license plate may load and unload passengers, but only for a maximum of five minutes.'
    },
    10: {
        name: 'Improperly Parked',
        description: 'General parking rules. No parking in alleys, sidewalks, crosswalks, bus stop, tunnel, etc.'
    },
    11: {
        name: 'Fire Hydrant',
        description: 'Be sure to check for a hydrant or fire station driveway.  Stopping, standing or parking are prohibited within 15 feet.'
    },
    12: {
        name: 'Disabled Parking',
        description: 'Be sure to check for a handicap parking sign and/or a blue-colored curb.  Vehicles not displaying a disabled parking placard or disabled license place are prohibited.'
    },
    13: {
        name: 'Private Property',
        description: 'Be sure to check for any private property signs.'
    }
}

export const Months = [
    { value: '0.0', label: 'January' },
    { value: '1.0', label: 'Feburary' },
    { value: '2.0', label: 'March' },
    { value: '3.0', label: 'April' },
    { value: '4.0', label: 'May' },
    { value: '5.0', label: 'June' },
    { value: '6.0', label: 'July' },
    { value: '7.0', label: 'August' },
    { value: '8.0', label: 'September' },
    { value: '9.0', label: 'October' },
    { value: '10.0', label: 'November' },
    { value: '11.0', label: 'December' }
]

export const Weekdays = [
    { value: '0.0', label: 'Monday' },
    { value: '1.0', label: 'Tuesday' },
    { value: '2.0', label: 'Wednesday' },
    { value: '3.0', label: 'Thursday' },
    { value: '4.0', label: 'Friday' },
    { value: '5.0', label: 'Saturday' },
    { value: '6.0', label: 'Sunday' }
]

export const Hours = [
    { value: '0.0', label: '12 AM' },
    { value: '1.0', label: '1 AM' },
    { value: '2.0', label: '2 AM' },
    { value: '3.0', label: '3 AM' },
    { value: '4.0', label: '4 AM' },
    { value: '5.0', label: '5 AM' },
    { value: '6.0', label: '6 AM' },
    { value: '7.0', label: '7 AM' },
    { value: '8.0', label: '8 AM' },
    { value: '9.0', label: '9 AM' },
    { value: '10.0', label: '10 AM' },
    { value: '11.0', label: '11 AM' },
    { value: '12.0', label: '12 PM' },
    { value: '13.0', label: '1 PM' },
    { value: '14.0', label: '2 PM' },
    { value: '15.0', label: '3 PM' },
    { value: '16.0', label: '4 PM' },
    { value: '17.0', label: '5 PM' },
    { value: '18.0', label: '6 PM' },
    { value: '19.0', label: '7 PM' },
    { value: '20.0', label: '8 PM' },
    { value: '21.0', label: '9 PM' },
    { value: '22.0', label: '10 PM' },
    { value: '23.0', label: '11 PM' }
]

export const VehicleMakes = [
    { value: '0.0', label: 'Other' },
    { value: '25.0', label: 'Acura' },
    { value: '54.0', label: 'Alfa Romeo' },
    { value: '55.0', label: 'Aston-Martin' },
    { value: '13.0', label: 'Audi' },
    { value: '52.0', label: 'Bentley' },
    { value: '9.0', label: 'BMW' },
    { value: '33.0', label: 'Buick' },
    { value: '12.0', label: 'Cadillac' },
    { value: '8.0', label: 'Chevrolet' },
    { value: '19.0', label: 'Chrysler' },
    { value: '45.0', label: 'Daewoo' },
    { value: '47.0', label: 'Datsun' },
    { value: '6.0', label: 'Dodge' },
    { value: '53.0', label: 'Ferrari' },
    { value: '37.0', label: 'Fiat' },
    { value: '5.0', label: 'Ford' },
    { value: '39.0', label: 'Geo' },
    { value: '27.0', label: 'GMC' },
    { value: '42.0', label: 'Grumman' },
    { value: '2.0', label: 'Honda' },
    { value: '31.0', label: 'Hummer' },
    { value: '11.0', label: 'Hyundai' },
    { value: '20.0', label: 'Infinity' },
    { value: '16.0', label: 'Isuzu' },
    { value: '21.0', label: 'Jaguar' },
    { value: '10.0', label: 'Jeep' },
    { value: '46.0', label: 'Kawasaki' },
    { value: '24.0', label: 'KIA' },
    { value: '51.0', label: 'Lamborghini' },
    { value: '17.0', label: 'Lexus' },
    { value: '28.0', label: 'Lincoln' },
    { value: '38.0', label: 'Maserati' },
    { value: '7.0', label: 'Mazda' },
    { value: '15.0', label: 'Mercedes Benz' },
    { value: '26.0', label: 'MINI' },
    { value: '22.0', label: 'Mitsubishi' },
    { value: '18.0', label: 'Nissan' },
    { value: '1.0', label: 'Oldsmobile' },
    { value: '36.0', label: 'Plymouth' },
    { value: '32.0', label: 'Pontiac' },
    { value: '44.0', label: 'Porsche' },
    { value: '4.0', label: 'Range Rover' },
    { value: '57.0', label: 'Renault' },
    { value: '56.0', label: 'Rolls-Royce' },
    { value: '34.0', label: 'Saab' },
    { value: '35.0', label: 'Saturn' },
    { value: '30.0', label: 'Scion' },
    { value: '43.0', label: 'Smart' },
    { value: '50.0', label: 'Sterling' },
    { value: '23.0', label: 'Subaru' },
    { value: '40.0', label: 'Suzuki' },
    { value: '41.0', label: 'Tesla' },
    { value: '3.0', label: 'Toyota' },
    { value: '48.0', label: 'Triumph' },
    { value: '14.0', label: 'Volkswagen' },
    { value: '29.0', label: 'Volvo' },
    { value: '49.0', label: 'Yamaha' }
]

export const VehilceColors = [
    { value: '0.0', label: 'Other' },
    { value: '13.0', label: 'Beige' },
    { value: '4.0', label: 'Black' },
    { value: '6.0', label: 'Blue' },
    { value: '9.0', label: 'Brown' },
    { value: '7.0', label: 'Gold' },
    { value: '1.0', label: 'Green' },
    { value: '5.0', label: 'Grey' },
    { value: '11.0', label: 'Orange' },
    { value: '8.0', label: 'Red' },
    { value: '3.0', label: 'Silver' },
    { value: '10.0', label: 'Tan' },
    { value: '2.0', label: 'White' },
    { value: '12.0', label: 'Yellow' },
]
