# An Amusement park company wants one application for their billing counter to enable ticket sale.
# Assume the Amusement park authorities approached Max to get this application developed. 
# This application should have ticket prize as Rs.400 per person and if a person buysmore than 10 tickets 
# then person is eligible for 10 percent discount. Calculate the total bill or amount according to the number of tickets 
# that are sold.

def case_study_1(ticket_count):
    
    ticket_price = 400
    
    if ticket_count > 10:
        total_price = (ticket_price * ticket_count) * 0.9
    else:
        total_price = (ticket_price * ticket_count)

    return total_price

case_study_1(11)
