import os
import json

def adding(details, new):
    details.append(new)

def deleting(details, info):
    details.remove(info)
            
def store_data(details, file_name):
    file_path = os.path.dirname(file_name)
    file_path += file_name
    if os.path.exists(file_path):
        file = open(file_name, 'r+')
        try:
            data = json.load(file)
            file.close()
            data.update(details)
            with open(file_path, 'w') as fp:
                json.dump(data, fp, indent=4)
        except:
            print('Unable to stored!')
        else:
            print('Info successfully stored!')
        finally:
            file.close()

    else:
        file = open(file_path, 'w')
        try:
            json.dump(details, file, indent=4)
        except:
            print('Unable to store data!')
        else:
            print('Data successfully stored!')
        finally:
            file.close()

def add_file(key, value, file_name):
    file_path = os.path.dirname(file_name)
    file_path += file_name
    file = open(file_name, 'r+')
    name = [ky for ky in value.keys()][0]
    try:
        data = json.load(file)
        file.close()
        if name not in [k for k in data.keys()]:
            data[key].update(value)
            with open(file_path, 'w') as fp:
                json.dump(data, fp, indent=4)
    except:
        print(f'{name} is already listed.')
    else:
        print(f'{name} has been updated in the system.')
    finally:
        file.close()

def delete_event(key, file_name):
    try:
        file_path = os.path.dirname(file_name)
        file_path += file_name
        with open(file_path, 'r') as f:
            data = json.load(f)
            f.close()
            del data[key]
            js = json.dumps(data, indent=4)

        with open(file_path, 'w') as f:
            f.write(js)
    except:
        raise KeyError
    else:
        print('Info successfully deleted!')
    finally:
        f.close()

def delete_attendee(key, attendee, file_name):
    try:
        file_path = os.path.dirname(file_name)
        file_path += file_name
        with open(file_path, 'r') as f:
            data = json.load(f)
            f.close()
            del data[key][attendee]
            js = json.dumps(data, indent=4)

        with open(file_path, 'w') as fp:
            fp.write(js)    
    except:
        raise KeyError
    else:
        print('Info successfully deleted!')
    finally:
        fp.close()
        
        
def access_json(file_name):
    with open(file_name, 'r+') as file:
        data = json.load(file)
    return data

