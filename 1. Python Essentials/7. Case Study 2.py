
# John and Paul went to watch a movie in theatre where they need to buy two tickets. There are two types of tickets, 
# one Golden category and other as silver category. If they buy tickets for silver category, then per person a 
# ticket should cost Rs.150 and for golden category ticket should cost them Rs.200 each. 
# Considering this scenario, write a program for theatre ticket booking application scenario.

def case_study_2(ticket_count, ticket_type):
    
    ticket_pricing = {
        'gold': 200,
        'silver': 150
    }
    
    if ticket_count > 10:
        total_price = (ticket_pricing.get(ticket_type) * ticket_count) * 0.9
    else:
        total_price = (ticket_pricing.get(ticket_type) * ticket_count)

    return total_price
        
