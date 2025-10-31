#file CRUD operations

def create_file(file_path,content):
    with open(file_path,'w')as file:
        file.write(content)

#create the create_file funtion

create_file('gods.text','lord ganesh\n lord shiva\n lord vishnu')        