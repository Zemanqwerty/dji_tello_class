from drone import Drone

drone = Drone()


print(f'battery - {drone.drone.get_battery()}%')

drone.make_picture()

drone.drone.end()
