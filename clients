import requests

class DashAPI:
    def __init__(self, base_url, token=None):
        """
        Initialize the DashAPI class.
        :param base_url: The base URL of the API.
        :param token: Optional token for authentication.
        """
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}" if token else "",
            "Content-Type": "application/json"
        }

    def get_plot_plan_data_services(self):
        url = f"{self.base_url}/api/dashboard/PlotPlanDataServices"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_plot_plan_data(self):
        url = f"{self.base_url}/api/dashboard/PlotPlanData"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_errors_by_time(self):
        url = f"{self.base_url}/api/dashboard/GetErrorsByTime"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_requests_by_time(self):
        url = f"{self.base_url}/api/dashboard/GetRequestsByTime"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def filter_service(self, service_type="ALL"):
        url = f"{self.base_url}/api/dashboard/FilterFService"
        params = {"serviceType": service_type}
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def get_by_token(self, token):
        url = f"{self.base_url}/api/dashboard/GetByToken/{token}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_by_subscription_id(self, subscription_id):
        url = f"{self.base_url}/api/dashboard/GetBySubscriptionId/{subscription_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_spaces_by_ram_async(self, ram):
        url = f"{self.base_url}/api/dashboard/GetSpacesByRamAsync/{ram}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        """
        Handle the API response.
        :param response: The response object from requests.
        :return: The JSON data or error details.
        """
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return {
                "error": True,
                "status_code": response.status_code,
                "details": response.json() if response.headers.get("Content-Type") == "application/json" else response.text
            }
