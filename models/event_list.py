from models.Event import Event

event_1 = Event(
    "2/22/2222", "Apocalypse", 1444, "Earth", "Welcome to the end of the world."
)

event_2 = Event(
    "1/1/1111", "Jesus 2.0", 3, "Some stable", "He's back and wants revenge"
)

events = [event_1, event_2]


def add_new_event(event):
    events.append(event)


def you_submitted():
    return "Entry submitted!"
