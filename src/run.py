from frontend.dashboard import Dashboard

dashboard = Dashboard(size="500x450", title="Dashboard")

class Run():
    def __init__(self):
        self.run()

    def run(self) -> None:
        dashboard.frame_settings()

run = Run()