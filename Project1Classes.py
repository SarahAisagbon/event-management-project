from abc import ABC, abstractmethod
from Project1Functions import *

class Person:
    def __init__(self, id, name, email, number):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__number = number

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number
    
class Attendees:
    def __init__(self, event_id, *attendees):
        self.__event_id = event_id
        self.__attendees_list = [*attendees]
    
    @property
    def attendees_list(self):
        return self.__attendees_list
    
    @property
    def event_id(self):
        return self.__event_id
    
    @event_id.setter
    def event_id(self, event_id):
        self.__event_id = event_id
           
    def add(self, attendee):
        """_summary_
            This function adds an person to the attendees list.
        Args:
            attendee (_obj_): object with an id, name, email and number attribute.
        Returns:
            it prints a string saying if the person has been added or not.
        """

        try:
            adding(list(self.__attendees_list), attendee)
            print('There is a new attendee.')
        except:
            print('Attendee information is incomplete.')
        else:
            print(f'{attendee.name} has been updated in the system.')
    
    def delete(self, attendee):
        """_summary_
            This function delete an person from the attendees list.
        Args:
            attendee (_obj_): object with an id, name, email and number attribute.
        Returns:
            it prints a string saying if the person has been added or not.
        """

        try:
            deleting(self.__attendees_list, attendee)
            print(f'{attendee.name} has been deleted from the class.')
        except:
            print(f'{attendee.name} was never attending this event.')
        else:
            print(f'{attendee.name} is no longer attending this event.')
        finally:
            print("Info has been successfully updated!")

    def get_attendees_names(self):
        """_summary_
            This function returns a list of all the attendees.
        Return:
            names (_lst_): list of attendee names
        """
        
        names = []
        for each_obj in self.__attendees_list:
            names.append(each_obj.name)
        return names
        
    def get_attendees_dict(self):
        """_summary_
            This function returns a dictionary with the key as the attendee's names and their id, email and number as the values.
        Return:
            attendee_dict (_dict_): key=names, values = [id, email, number]
        """
        attendee_dict = {}
        for each_obj in self.__attendees_list:
            attendee_dict[each_obj.name] = [each_obj.id, each_obj.email, each_obj.number]
        return attendee_dict

    def store_attendees_info(self, file_name):
        """_summary_
            This function stores the attendee dictionary in file_name.
        Args:
            file_name (_str_): name of file 
        """
        details = self.get_attendees_dict()
        event_attendees = {self.event_id: details}
        store_data(event_attendees, file_name)
        
    def num_of_attendees(self):
        """_summary_
            This function returns the number of attendees 
        Returns:
            number (_int_): number of people in the attendees_list
        """
        number = len(self.__attendees_list)
        return number

#Abstract Class
class Event:
    def __init__(self, id, name, start_time, end_time, location, budget):
        self.__id = id
        self.__name = name
        self.__start_time = start_time
        self.__end_time = end_time
        self.__location = location
        self.__budget = budget
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time):
        self.__end_time = end_time
    
    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        self.__budget = budget

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location
    
    @abstractmethod
    def get_attendees(self):
        pass
    
    @abstractmethod
    def add_event(self):
        pass
    
    @abstractmethod
    def remove_event(self):
        pass
    
        
#Implementation Class
class All_Events(Event):
    def __init__(self, events):
        self.__events = events
    
    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, events):
        self.__events = events

    @abstractmethod
    def get_attendees(self, event):
        """_summary_
            This function returns the names of all the attendees of a specified event.
        Args:
            event (string): name of event

        Returns:
            attendees_names (_lst_): listof all the attendees of a specified event.
        """
        self.__attendee_names = []
        data = access_json("attendees.json")
        for key, value in data[event].items():
            self.__attendee_names.append(key)

        return self.__attendee_names
    
    def get_attendees_object(self, event):
        self.__attendee_list = []
        data = access_json("attendees.json")
        for key in data:
            if event == key:
                for key, value in data[event].items():
                    person = Person(value[0], key, value[1], value[2])
                    self.__attendee_list.append(person)
        return self.__attendee_list
    
    def get_event_names(self):
        """_summary_
            This function gets the names of all events in the system.
        Returns:
            event_names (_lst_): list of event names
        """
        self.__event_names = []
        for each_obj in self.__events:
            adding(self.__event_names, each_obj.name)
        return self.__event_names
    
    def get_events_dict(self):
        """_summary_
            This function gets a dictionary of a dictionary of all events
        Returns:
            event_dict (_dict_): key = event id, values = {event name, start_time, end_time, location, budget}
        """
        event_dict = {}
        for each_obj in self.__events:
            event_dict[each_obj.id] = {"name": each_obj.name, "starttime": each_obj.start_time, "endtime": each_obj.end_time, "location": each_obj.location, "budget": each_obj.budget}
        return event_dict   
    
    def add_event(self, event):
        """_summary_
            This function adds an event dictionary to the dictionary of all events in the system.
            If the event is already listed, it informs us.
        Args:
            event (_obj_): an event as an object
        """
        try:
            if event in self.__events:
                raise Duplicate
        except:
            print(f'{event.name} is already listed.')
        else:
            details = self.get_events_dict()
            print(f'{event.name} has been added to the system.')
            self.__events.append(Event(event))
            store_data(details, "events.json")
    
    def remove_event(self, id):
        """_summary_
            This function removes a specified event from the system and the Events class list.
        Args:
            id (_str_): the event id
        """
        try:
            for each_obj in self.__events:
                if each_obj.id == id:
                    try:
                        delete_event(each_obj.id, "events.json")
                    except KeyError:
                        print(f'Incorrect event id!')
                    else:
                        print(f'{each_obj.name} is no longer happening!')
                    finally:
                        self.__events.remove(each_obj)
        except:
            print(f'There was no event with id: {id}!')
    
    def store_event_info(self, file_name):
        """_summary_
            This function gets the name of a json file and stores the event dictionary in this file.
        Args:
            file_name (_str_): name of file that will store the event info
        """
        details = self.get_events_dict()
        store_data(details, file_name)
        
    def edit_file(self):
        """_summary_
            This function saves the new event information in the all_event.json file.
        """
        file_path = os.path.dirname("all_event.json")
        file_path += "all_events.json"
        details = self.get_events_dict()
        file = open(file_path, 'w')
        try:
            json.dump(details, file, indent=4)
        except:
            print('Unable to edit')
        else:
            print('Edit successfully')
        finally:
            file.close()

    
    
    

