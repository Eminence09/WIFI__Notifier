# from plyer import notification


# import time
# notification.notify(
#     title='My Notification',
#     message='This is a desktop notification from Python!',
#     app_name='From yash',
#     timeout=10  # Notification will disappear after 10 seconds
# )
# time.sleep(11) # Give time for the notification to display


# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("Python Notification", "Hello from Python!", duration=5)

# import platform

# print(platform.system())
# print(platform.release())
# print(platform.architecture())
# # print(platform.freedesktop_os_release())
# print(platform.machine())
# print(platform.platform())
# print(platform.processor())
# print(platform.python_build())


from plyer import notification
import subprocess
import time

SSIDS = set()


while True: 
    time.sleep(10)
    
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks']).decode('utf-8')
    for line in output.split("\n"):
        
        if "SSID" in line:
            ssid = line.split(":")[1].strip()
            SSIDS.update([ssid])
            
    
    if 'realme narzo 50A Prime' in SSIDS:
        time.sleep(10)
        print(SSIDS)
        
        notification.notify(
            title='Network Info',
            message='reamle Has turned on the hotspot!',
            app_name='From Python',
            timeout=10 
        )
        
        
    else:
        notification.notify(
                                title='Network Info',
                                message='No network Identified',
                                app_name='From Python',
                                timeout=10 
                            )