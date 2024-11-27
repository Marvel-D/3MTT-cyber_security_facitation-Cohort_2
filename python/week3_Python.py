# threat_level = 200 

# if threat_level < 250:
#     print("low")
# elif threat_level > 700:
#     print("severe")
# else:
#     print("Scan for Threat")

    
# def display_investigation_message():
#     print("Investigation successful")
#     print("Investigation successful twice")


# application_status = "potential concern"
# email_status = "potential concern"
# if application_status == "potential concern":
#     print("application_log")
#     display_investigation_message()
# if email_status == "potential concern":
#     print("email log:")
#     display_investigation_message()
    




fellow_id = input("Provide fellow ID:")

pluto_fellows = ["FE12232", "FE31223", "111"]

# for fellow in pluto_fellows:
if fellow_id in pluto_fellows:
    print("welcome fellow", fellow_id)
else:
    print("unauthorized fellow")