import requests


class API():
    def __init__(self):
        self.url = "https://webapi.bps.go.id/v1/api/"
        self.key = "2ff0d1794d793a4be0a72124a029172f"

    def get_list_infographic(self, **kwargs):
        "https://webapi.bps.go.id/v1/api/list/model/infographic/lang/ind/domain/0000/page/1/key/2ff0d1794d793a4be0a72124a029172f/"
        model = "infographic"
        domain = kwargs.get("domain")
        url = f"{self.url}list/model/{model}/domain/{domain}/key/{self.key}"
        return requests.get(url).json()

    def get_list(self, **kwargs):
        model = kwargs.get("model")
        page = kwargs.get("page")
        domain = kwargs.get("domain")
        keyword = kwargs.get("keyword")

        match model:
            case "infographic":
                if page:
                    url = f"{self.url}list/model/{model}/domain/{domain}/page/{page}/key/{self.key}"
                    data = requests.get(url).json()
                    dt = self.data_transform(data)
                    return dt
                else:
                    url = f"{self.url}list/model/{model}/domain/{domain}/key/{self.key}"
                    data = requests.get(url).json()
                    dt = self.data_transform(data)
                    return dt

            case 'pressrelease':
                url = f"{self.url}list/model/{model}/domain/{domain}/page/{page}/key/{self.key}"
                data = requests.get(url).json()
                dt = self.data_transform(data)
                return dt
            case "news":
                pass

    def get_view(self, **kwargs):
        id_data = kwargs.get("id")
        model = kwargs.get("model")
        domain = kwargs.get("domain")
        print(id_data, domain)
        "https://webapi.bps.go.id/v1/api/view/domain/0000/model/pressrelease/lang/ind/id/2006/key/2ff0d1794d793a4be0a72124a029172f/"
        match model:
            case "pressrelease":
                url = f"{self.url}view/model/{model}/domain/{domain}/lang/ind/id/{id_data}/key/{self.key}"
                data = requests.get(url).json()
                return data

    def data_transform(self, data):
        dt = {
            "draw": data["data"][0]["page"],
            "recordsTotal": data["data"][0]["total"],
            "recordsFiltered": data["data"][0]["total"],
            "data": data["data"][1],
        }
        return dt
