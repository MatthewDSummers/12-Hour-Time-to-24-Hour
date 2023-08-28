"""""""""""""""""""""""""""""""""""""""""""""
Converts 12 hour time to 24 hour time 
"""""""""""""""""""""""""""""""""""""""""""""

import re
def timeConversion(s):
    if isinstance(s, str):
        time_regex = r"^(1[0-2]|0?[1-9]):[0-5][0-9]:[0-5][0-9]([ap]m)?$"
        matches = re.findall(time_regex, s, re.IGNORECASE)

        if matches:
            time = s.split(":")
            hour = time[0]
            time_mark = time[2][2:].upper()

            if time_mark == "PM":
                if hour != "12":
                    hour = int(hour)
                    hour += 12
                    time[0] = str(hour)
            elif time_mark == "AM":
                if hour == "12":
                    time[0] = "00"

            new_time = ":".join(time)
            return new_time[:-2]

    else:
        return "Time string should be formatted as '00:00:00AM' / '00:00:00PM'"


if __name__ == "__main__":
    # n = input('Provide the time as a string in the format of "12:03:24AM"\n')
    # print(timeConversion(n))
    print(timeConversion(2))
# Sample cases 
    # input_time_1 = "03:45:30PM"
    # input_time_2 = "12:30:15AM"
    # input_time_3 = "06:15:00AM"
    # input_time_4 = "07:00:00PM"
    # input_time_5 = "10:30:45AM"
    # input_time_6 = "11:59:59PM"

    # print(timeConversion(input_time_1))  # Output: "15:45:30"
    # print(timeConversion(input_time_2)) # Output: "00:30:15"
    # print(timeConversion(input_time_3))  # Output: "06:15:00"
    # print(timeConversion(input_time_4))  # Output: "19:00:00"
    # print(timeConversion(input_time_5))  # Output: "10:30:45"
    # print(timeConversion(input_time_6))  # Output: "23:59:59"