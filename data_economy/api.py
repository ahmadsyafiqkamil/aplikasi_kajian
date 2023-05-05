import requests
import pandas as pd


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

            case 'subject':
                "https://webapi.bps.go.id/v1/api/list/model/subject/domain/0000/key/2ff0d1794d793a4be0a72124a029172f/"
                url = f"{self.url}list/model/{model}/domain/{domain}/page/{page}/key/{self.key}"
                print(url)
                data = requests.get(url).json()
                dt = self.data_transform(data)
                return dt

            case 'var':
                "https://webapi.bps.go.id/v1/api/list/model/var/domain/0000/subject/23/page/1/key/2ff0d1794d793a4be0a72124a029172f/"
                subject = kwargs.get("subject")
                url = f"{self.url}list/model/{model}/domain/{domain}/subject/{subject}/page/{page}/key/{self.key}"
                print(url)
                data = requests.get(url).json()
                dt = self.data_transform(data)
                return dt

            case 'turvar':
                "https://webapi.bps.go.id/v1/api/list/model/turvar/domain/0000/var/56/page/1/key/2ff0d1794d793a4be0a72124a029172f/"
                id_var = kwargs.get("id_var")
                url = f"{self.url}list/model/{model}/domain/{domain}/var/{id_var}/page/{page}/key/{self.key}"
                print(url)
                data = requests.get(url).json()
                dt = self.data_transform(data)
                return dt

            case 'turth':
                "https://webapi.bps.go.id/v1/api/list/model/turth/domain/0000/var/56/page/1/key/2ff0d1794d793a4be0a72124a029172f/"
                id_var = kwargs.get("id_var")
                url = f"{self.url}list/model/{model}/domain/{domain}/var/{id_var}/page/{page}/key/{self.key}"
                print(url)
                data = requests.get(url).json()
                dt = self.data_transform(data)
                return dt

            case 'th':
                "https://webapi.bps.go.id/v1/api/list/model/th/domain/0000/var/457/key/2ff0d1794d793a4be0a72124a029172f/"
                id_var = kwargs.get("id_var")
                url = f"{self.url}list/model/{model}/domain/{domain}/var/{id_var}/page/{page}/key/{self.key}"
                print(url)
                data = requests.get(url).json()
                dt = self.data_transform(data)
                return dt

            case "vervar":
                "https://webapi.bps.go.id/v1/api/list/model/vervar/domain/0000/var/56/page/1/key/2ff0d1794d793a4be0a72124a029172f/"
                id_var = kwargs.get("id_var")
                url = f"{self.url}list/model/{model}/domain/{domain}/var/{id_var}/page/{page}/key/{self.key}"
                print(url)
                data = requests.get(url).json()
                dt = self.data_transform(data)
                return dt

            case "data":
                "https://webapi.bps.go.id/v1/api/list/model/data/domain/0000/var/1/turvar/1/vervar/1/th/1/turth/1/key/2ff0d1794d793a4be0a72124a029172f/"
                domain = kwargs.get('domain')
                subject = kwargs.get('subject')
                var_id = kwargs.get('var_id')
                turth_id = kwargs.get('turth_id')
                turvar_id = kwargs.get('turvar_id')
                th_id = kwargs.get('th_id')
                vervar_id = kwargs.get('vervar_id')

                path = ""
                if turvar_id is not "0":
                    path += f"turvar/{turvar_id}/"
                if turth_id is not "0":
                    path += f"turth/{turth_id}/"
                if vervar_id is not "0":
                    path += f"vervar/{vervar_id}/"
                if th_id is not "0":
                    path += f"th/{th_id}/"

                url = f"{self.url}list/model/{model}/domain/{domain}/var/{var_id}/{path}key/{self.key}"
                data = requests.get(url).json()
                if data["data-availability"] == "available":
                    # dt = self.data_dinamis_transform(data)
                    return data
                else:
                    return None

            case "news":
                pass

    def get_view(self, **kwargs):
        id_data = kwargs.get("id")
        model = kwargs.get("model")
        domain = kwargs.get("domain")
        match model:
            case "pressrelease":
                url = f"{self.url}view/model/{model}/domain/{domain}/lang/ind/id/{id_data}/key/{self.key}"
                data = requests.get(url).json()
                return data

    def data_transform(self, data):
        if data["data-availability"] == "available":
            dt = {
                "recordsTotal": data["data"][0]["total"],
                "recordsFiltered": data["data"][0]["total"],
                "data": data["data"][1],
            }
            return dt

        else:
            dt = {
                "data": "no_data"
            }
            return dt

    def data_dinamis_transform_to_pd(self, response):
        result = {}

        vervar_labels = {v["val"]: v["label"] for v in response["vervar"]}
        tahun_labels = {t["val"]: t["label"] for t in response["tahun"]}
        bulan_labels = {b["val"]: b["label"] for b in response["turtahun"]}
        karakteristik_labels = {k["val"]: k["label"] for k in response["turvar"]}
        var_val = response["var"][0]["val"]

        # Mengisi data ke dalam result dictionary
        for t in response["tahun"]:
            tahun = tahun_labels[t["val"]]
            if tahun not in result:
                result[tahun] = {}

            for tt in response["turtahun"]:
                bulan = bulan_labels[tt["val"]]
                if bulan not in result[tahun]:
                    result[tahun][bulan] = {}

                for v in response["vervar"]:
                    vervar = vervar_labels[v["val"]]
                    if vervar not in result[tahun][bulan]:
                        result[tahun][bulan][vervar] = {}

                        for tv in response["turvar"]:
                            turvar = karakteristik_labels[tv["val"]]
                            if turvar not in result[tahun][bulan][vervar]:
                                result[tahun][bulan][vervar][turvar] = {}

                                for k, d in response["datacontent"].items():
                                    if k not in result[tahun][bulan][vervar][turvar]:
                                        result[tahun][bulan][vervar][turvar][k] = {}
                                    result[tahun][bulan][vervar][turvar][k] = d

        # Mengubah dictionary menjadi pandas dataframe
        dfs = []
        for tahun, bulan_dict in result.items():
            for bulan, vervar_dict in bulan_dict.items():
                for vervar, karakteristik_dict in vervar_dict.items():
                    for karakteristik, data_dict in karakteristik_dict.items():
                        df = pd.DataFrame(data_dict.items(), columns=["data_key", "data"])
                        df["tahun"] = tahun
                        df["bulan"] = bulan
                        df["vervar"] = vervar
                        df["karakteristik"] = karakteristik
                        df.set_index(["tahun", "bulan", "vervar", "karakteristik", "data_key"], inplace=True)
                        dfs.append(df)

        # Menggabungkan semua dataframe menjadi satu dataframe dengan pd.concat()
        df = pd.concat(dfs)
        return df
