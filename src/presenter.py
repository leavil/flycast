from model import OpenSkyApi


class Presenter:
    def __init__(self, view):
        self.view = view
        self.model = OpenSkyApi()

    def get_aircraft_data(self):
        aircraft_data = self.model.fetch_all_states()
        if aircraft_data:
            self.view.show_aircraft_data(aircraft_data)
        else:
            self.view.show_error_message("Failed to fetch aircraft data.")
