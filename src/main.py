from src.models.group import Group
from src.models.user import User

# need to create parties
# need to be able to queue up
# one problem might be that everyone creates a party, or everyone queues up?
# maybe default we can queue up and if there's no existing lobby we can create one
# or we just match make 3 people who need to queue up instead, i handle the party creation

QUEUE_MAP = {
    "celestia": [],
    "zafaria": [],
    "avalon": [],
    "zzteca": [],
    "khrysalis": [],
    "polaris": [],
    "novus": [],
    "wallaru": [],
    "selenopolis": [],
    "darkmoor": [],
}

USER_LIST = []

def create_user(id, name):
    # Sanitization should be done here
    # Can create user when they queue up, but this would be intensive
    # Should I register users? Probably not because that would require storing them
    return User(
        id=id,
        name=name
    )

def get_world_queue(world):
    try:
        return QUEUE_MAP[world.lower()]
    except Exception as e:
        print(f"Error: {world} does not exist in the world queue map.")
        # base_log?

def add_user(world, user):
    world_queue = get_world_queue(world)
    
    # add user here
    world_queue.append(user)

    # if world queue is greater than or equal to 3, we make a group
    if len(world_queue) >= 3:
        member_list = []
        for i in range(3):
            member_list.append(world_queue.pop(0))
        
        group = Group(
            world=world,
            members=member_list
        )

        return group

def remove_user(world, user):
    world_queue = get_world_queue(world)

    if user in world_queue:
        world_queue.remove(user)
        return True
    return False

def create_group(world, users):
    pass
