class SimpleDatabase:
    def __init__(self):
        self.database = {}

    def add_data(self, ip, domain, data):
        key = (ip, domain)
        self.database[key] = data

    def get_data(self, ip):
        result = []
        for key, value in self.database.items():
            if key[0] == ip:
                result.append((key[1], value))
        return result

    def remove_data(self, ip, domain, data):
        key = (ip, domain)
        if key in self.database and self.database[key] == data:
            del self.database[key]
            return True
        return False

    def print_database(self):
        print("Database Contents:")
        for key, value in self.database.items():
            print(f"IP: {key[0]}, Domain: {key[1]}, Data: {value}")


