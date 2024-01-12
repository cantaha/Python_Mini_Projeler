import requests
import json
import freecurrencyapi


api_url = "https://api.freecurrencyapi.com/v1/latest"
client = freecurrencyapi.Client("fca_live_kLBtk4UalvilbQpr4hb18bzacvMDP2cZ0vWPOjz4")

# print(client.status())
# result = client.currencies()
# print(type(result))
# print(result["data"]["TRY"])
# result2 = client.latest()
# print(result2)



bozulan_doviz = input("Bozulacak Doviz Cinsi: ")
alinan_doviz = input("Alınacak Doviz Cinsi: ")
miktar = int(input("Bozulacak Döviz Miktarı: "))

result = client.latest()
# result = json.loads(result)

print(f"1 {bozulan_doviz} = {result["data"][alinan_doviz]} {alinan_doviz}")
print(f"{miktar} {bozulan_doviz} = {miktar * result["data"][alinan_doviz]} {alinan_doviz}")