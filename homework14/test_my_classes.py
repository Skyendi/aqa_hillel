import pytest
from homework14.homework_14 import *

team_lead = TeamLead(
    name="Dmytro",
    salary= 80000,
    department="AQA",
    programming_language="Python",
    team_size=3
)

def test_attributes(lead):
    assert hasattr(lead, "name")
    assert hasattr(lead, "salary")
    assert hasattr(lead, "department")
    assert hasattr(lead, "programming_language")
    assert hasattr(lead,  "team_size")





if __name__ == "__main__":
    test_attributes(team_lead)

