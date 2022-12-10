import socket
import time


class Drone(object):
    def __init__(self, name):
        self.name = name

        # set local data
        self.local_ip = ''
        self.local_port = 8889

        # set socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        # set drone data
        self.drone_ip = '192.168.10.1'
        self.drone_port = 8889
        self.drone_address = (self.drone_ip, self.drone_port)


    def send_command(self, command):
        try:
            self.socket.sendto(command.encode('utf-8'), self.drone_address)
            print(f'sent command {command} to {self.drone_ip}:{self.drone_port}')
        except Exception as e:
            print(e)


def start(file_name):
    with open(file_name, 'r') as f:
        commands = f.readlines()

    drone = Drone('drone №1')

    for command in commands:
        if command != '' and command != '\n':
            command = command.rstrip()

            if command.find('delay') != -1:
                seconds = float(command.partition('delay')[2])

                print(f'delay {seconds}...')

                time.sleep(seconds)
                pass
            else:
                drone.send_command(command)


if __name__ == '__main__':
    start('commands.txt')



