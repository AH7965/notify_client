import requests
import multiprocessing as mp
import time

class notify:
    def __init__(self, device_name="Unknown Device", project_name="Unknown Project", entry_point="http://c075e2d3f75a.ngrok.io"):
        self.device_name = device_name
        self.project_name = project_name
        self.entry_point = entry_point

        self.status_alive = 0

        self.params = {"device_name" : self.device_name,
                       "project_name": self.project_name}
    
    def start(self):
        if self.status_alive == 0:
            response = requests.get(f"{self.entry_point}/start", params=self.params)
            assert response.status_code == 200
            self.ticking = mp.Process(target=ticking, args=(self.device_name, self.entry_point))
            self.ticking.start()
            self.status_alive = 1   
    
    def quit(self):
        if self.status_alive == 1:
            response = requests.get(f"{self.entry_point}/quit", params=self.params)
            assert response.status_code == 200
            self.ticking.terminate()
            self.ticking.join()
            self.ticking.close()
            self.status_alive = 0

    def update_project_name(self, project_name):
        self.project_name = project_name

        self.params = {"device_name" : self.device_name,
                       "project_name": self.project_name}

    def notify(self, text=""):
        self.params["text"] = text
        response = requests.get(f"{self.entry_point}/slack_notify", params=self.params)
        assert response.status_code == 200
    
    def __del__(self):
        self.quit()


def ticking(device_name, entry_point, delay=15):
    while True:
        response = requests.get(f"{entry_point}/tick", params={"device_name":device_name})
        assert response.status_code == 200

        time.sleep(delay)
