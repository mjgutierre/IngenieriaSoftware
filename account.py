class Account:
    id = int;
    name = str;
    password = str;
    document = str;
    email = str;

    def __init__(self, id, name, document, password, email):
        self.name = name;
        self.document = document;
        self.password = password;
        self.email = email;
        self.id = id;
