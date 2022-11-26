from cosmotic_ticket_num import cosmo_site
from medicine_ticket_num import medicine_site
from perfumes_ticket_num import perfumes_site
from count_down_timer_finish import countdown_finish
from count_down_timer_wrong_input import countdown_wrong

# variables used
cosmo_ticket_number = cosmo_site()
medicines_ticket_number = medicine_site()
perfumes_ticket_number = perfumes_site()
count = 0
exit_point = "Stop"

# using identification codes
idnum_dawit = "987654321"
idnum_yonas = "123456789"
id_list = [idnum_dawit, idnum_yonas]


# while exit_point != "stop" and count < 3:
def ticket_machine():
    global count
    while count < 3:
        idnum = input("Please Enter Valid Id: ")
        if idnum in id_list:
            from welcome_message import message_display
            customer = input("Please Choose Which Site you went to visit--> ")
            if customer == "c" or customer == "C" or customer == "cosmetic" or customer == "COSMETIC":
                print("\n\t\t\t\t Your Ticket Number is C-", next(cosmo_ticket_number))
                print("\t\t\t\t Please wait and someone will assist you shortly.")
                print("===================================================================================")
            elif customer == "p" or customer == "P" or customer == "perfume" or customer == "PERFUME":
                print("\n\t\t\t\t Your Ticket Number is P-", next(perfumes_ticket_number))
                print("\t\t\t\t Please wait and someone will assist you shortly.")
            elif customer == "m" or customer == "M" or customer == "medicine" or customer == "MEDICINE":
                print("\n\t\t\t\t Your Ticket Number is M-", next(medicines_ticket_number))
                print("\t\t\t\t Please wait and someone will assist you shortly.")
            elif customer == "":
                print(print("\t\t\t\t You didn't select a visited site"))
                # input("Please Choose Which Site you went to visit--> ")
            else:
                print("\t\t\t\t Please choose correct valid site you went to visit--> ")
                continue
            other_site = input("\nDo you went to continue seeing other sites yes/no: ")
            if other_site == "y" or other_site == "Y" or other_site == "Yes" or other_site == "YES":
                continue
            elif other_site == "":
                print("You didn't Enter valid input, Please enter valid value ")
                input("Do you went to continue seeing other sites y/n")
            else:
                countdown_finish()
                from exit_message import thank_you
                break
        else:
            count += 1
            continue
    else:
        print("\nYou Enter invalid ID so many time , please try other time")
        countdown_wrong()
        from exit_message import thank_you


# ticket_machine()
