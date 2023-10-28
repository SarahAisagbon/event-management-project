from Project1Classes import *
from Project1Functions import *
def event_list(events):
    eventlist = []
    for key in events:
        eventinfo = [key] + list(events[key].values())
        event = Event(*eventinfo)
        eventlist.append(event)
    return eventlist

def menu():
    print ("\nExample menu")
    print ("-----------------")
    print('1) List all events')
    print('2) List an individual event')
    print('3) Add an event')
    print('4) Edit an event')
    print('5) Delete an event')
    print('6) List attendees of an event')
    print('7) Add an attendee to an event')
    print('8) Delete an attendee from an event')
    print('Q) Quit')
    
    events = dict(access_json("events.json"))
    all_events = All_Events(event_list(events))
    
    while True:   
        task = (input('Enter the number to perform the corresponding task: ')).lower()

        if task == '1':
            print(events)
        elif task == '2':
            id = str(input("What's the event id? "))
            
            try:
                if id in list(events.keys()):
                    print(events[id])
                else:
                    raise KeyError(f"There is no event with id: {id}!")
            except KeyError as err:
                print(err)
                
        elif task == '3':
            eventinfo = input("Enter the event's id, event name, start time, end time, location, budget? ").split(",")
            
            try:
                if eventinfo[0] in events.events.keys():
                    raise ValueError("This event id is already in use.")
                else:
                    event = Event(*eventinfo)
                    all_events.add_event(event)
            except ValueError as err:
                print(err)
                
        elif task == '4':
            eventid = input("What's the event id? ")
            feature = ((input("What do you want to edit? Name, starttime, endtime, location, budget? ").lower())).replace(" ", "")
            new = input(f"What do you want to change the {feature} to? ")
            
            try:
                if eventid in list(events.keys()):
                    events[eventid][feature] = new
                    with open("events.json", 'w') as file:
                        json.dump(events, file, indent=4)
                else:
                    raise ValueError(f"There is no event with id: {event_id}!")
            except ValueError as err:
                print(err)
                
        elif task == '5':
            eventid = input("What's the event id? ")
            all_events.remove_event(eventid)
        
        elif task == '6':
            event = str(input("What's the event id? "))
            print(all_events.get_attendees(event))
        
        elif task == '7':
            event = str(input("What's the event id? "))
            person = Person(*input("What's the person's id, name, email, number? ").split(','))
            print(all_events.get_attendees_object(event))
            attendee = Attendees(event, all_events.get_attendees_object(event))
            attendee.add(person)
            attendee.store_attendees_info("attendees.json")
            
        elif task == '8':
            event = str(input("What's the event id? "))
            person = Person(*input("What's the person's id, name, email, number? ").split(','))
            print(all_events.get_attendees_object(event))
            attendee = Attendees(event, all_events.get_attendees_object(event))
            attendee.delete(person)
            attendee.store_attendees_info("attendees.json")
            #"Sarah Galenda": [
            #"10001",
            #"sgalenda@gmail.com",
            #"07393906455"
        elif task == 'q':
            return
        else:
            print(f'Not a correct choice: <{task}>,try again')

if __name__ == '__main__':
    menu()
    
"""
a1 = Person('10001', 'Sarah Galenda', 'sgalenda@gmail.com', '07393906455')
a2 = Person('10002', 'Sarah Aisagbon', 'saisagbon@yahoo.com', '07393906456')
a3 = Person('10003', 'Justin Bieber', 'jbieber@gmail.com', '07757720249')
a4 = Person('10004', 'Anita Victor', 'avictor@yahoo.co.uk', '07523186400')
a5 = Person('10005', 'Assana Mahmoud', 'assana@gmail.com', '07986341975')
a6 = Person('10006', 'Rachel Smith', 'rachelsmith@yahoo.co.uk', '07747734509')
#a7 = Person(*list(input("Enter person id, name, email and number:").split(",")))
#10007, Ben Nott, bnott@live.co.uk , 07985241849

e1 = Attendees("e0001", a1, a2, a4)
e2 = Attendees("e0002", a1, a2, a3)
e3 = Attendees("e0003", a1, a2, a4, a5)

e1.store_attendees_info("attendees.json")
e2.store_attendees_info("attendees.json")
e3.store_attendees_info("attendees.json")

event1 = Event("e0001", "Ben's Wedding", '12:00', '22:00', e1.attendees_list, "Royal Hospital Chelsea", 1000)
event2 = Event("e0002", "Emily's Christening", '10:00', '16:00', e2.attendees_list, "St Pauls", 2500)
event3 = Event("e0003", "Sarah's Birthday", "14:00", "23:00", e2.attendees_list, "LSO",3000)

events = All_Events(event1, event2)
events.store_event_info("all_events.json")
"""



"""
#Get all the attendees for Ben's Wedding
benwed_attendees = events.get_attendees("e0001")
print(benwed_attendees)

#Add attendee to event1
e1.add(a1)
e1.store_attendees_info("attendees.json")

#add event to the system
events.add_event(event3)

new_attendees1 = events.get_attendees("e0002")
print(new_attendees1)
#Delete person from attendee list for event1
e1.delete(a1)
#Update e1's event dictionary
e1.store_attendees_info("attendees.json")

#Get info about all events in the system.
all_events = events.get_events_dict()
print(all_events)

#Get list of events in the system
event_names = events.get_event_names()
print(event_names)

#Get info about an individual event with the event_id = e0002
print(all_events["e0002"])

#To edit the start time of event 1 in the class and on the system
event1.start_time = '11:30'
events.edit_file()

#To remove event from system
events.remove_event("e0002")
event_names = events.get_event_names()
"""