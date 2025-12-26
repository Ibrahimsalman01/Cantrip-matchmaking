from src.main import *

# Test 1: Successfully adding user to queue
def add_user_to_queue_1():
    user = create_user(1, 'cleo')
    world = 'wallaru'

    add_user(world, user=user)

    return user in QUEUE_MAP[world]
