class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def __repr__(self):
        return (f"name = {self.name}, "
                f"salary = {self.salary} "
                f"department = {self.department} "
                f"programming_language = {self.programming_language} "
                f"team_size = {self.team_size} ")


lead = TeamLead(name="Dmytro", salary=80000, department="AQA", programming_language="Python", team_size=3)

print(lead)
