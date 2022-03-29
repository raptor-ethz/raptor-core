import subprocess
import multiprocessing as mp
from colorama import Fore, Back, Style

ROOT_DIR = '../build/modules/reference_generator/apps/'
MOCAP_PUBLISHER_PATH = '../build/modules/mocap_publisher/app/mocap_publisher'
POS_CONTROL_INTERFACE_PATH = '../build/modules/position_ctrl_interface/apps/position_control/pos_ctrl_interface'


def launch_interface(usb_path):
    try:
        process = subprocess.Popen(
            [POS_CONTROL_INTERFACE_PATH, usb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for line in process.stdout:
            print(Fore.GREEN +
                  "Position Control Interface:    ", end='')
            print(Style.RESET_ALL, end='')
            print(line.decode(), end='')

        process.stdout.close()

    except Exception as e:
        print(e)


def launch_reference(application, arg=None):
    try:
        app = ROOT_DIR + application + '/' + application
        cmd = app if arg == None else [app, arg]
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for line in process.stdout:
            print(Fore.BLUE +
                  "Reference Generator:    ", end='')
            print(Style.RESET_ALL, end='')
            print(line.decode(), end='')

        process.stdout.close()

    except Exception as e:
        print(e)


def launch_mocap_publisher(objects=None):
    try:
        cmd = MOCAP_PUBLISHER_PATH if objects == None else [
            MOCAP_PUBLISHER_PATH, objects]
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for line in process.stdout:
            print(Fore.MAGENTA +
                  "MocCap Publisher:    ", end='')
            print(Style.RESET_ALL, end='')
            print(line.decode(), end='')

        process.stdout.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    publisher_objects = ('srl_quad',)
    interface_port = 'serial:///dev/ttyUSB0'
    reference_app = 'a_star'

    processes = [
        mp.Process(target=launch_mocap_publisher,
                   args=publisher_objects),

        mp.Process(
            target=launch_interface, args=(interface_port,)),

        mp.Process(target=launch_reference, args=(reference_app,)),
    ]

    try:
        # Possible TODO: wait before starting the reference generator
        for p in processes:
            p.start()

        for p in processes:
            p.join()
    except KeyboardInterrupt as e:
        print("Terminating all processes.")
        for p in processes:
            p.terminate()
            p.join()
