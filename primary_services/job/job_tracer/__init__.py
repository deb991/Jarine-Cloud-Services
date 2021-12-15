import wmi
import subprocess

flow = wmi.WMI()

class Process_List():
    def __init__(self):
        pass

    def process_list(self):
        print("PID:\tProcess Name")

        for process in flow.Win32_process():
            print(f"{process.ProcessId:<10} {process.Name}")

    def process_list_subprocess(self):
        data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
        a = str(data)
        try:
            for i in range(len(a)):
                print(a.split("\\r\\r\\n")[i])
        except IndexError as e:
            print("All Done")


if __name__ == '__main__':
    pl = Process_List()
    #pl.process_list()
    pl.process_list_subprocess()