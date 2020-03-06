print("URL: "+(url))
json_data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]
if json_status==0:
    print("API Status. " + str(json_status)+"=A successful route call.\n")
