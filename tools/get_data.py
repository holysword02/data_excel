import requests


def get_headers(token: str) -> dict:
    return {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/119.0.0.0 Safari/537.36",
        'token': token
    }


def getExcelData(token, url, data) -> bytes:
    try:
        response = requests.post(url=url, headers=get_headers(token), json=data, verify=False)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        return bytes(0)
    return bytes(0)


def brandExcelExport(token, plazaId, startDate, endDate, dateType="D"):
    """品牌级 日"""
    url = 'http://jyfx-svc.wandacm.cn/onemap-wanda/api/managementBrandDayController/brandExcelExport'
    data = {
        "categoryIds": "1,1000285,1000290,102,103,104,24,37,41,44,46,825",
        "dateType": dateType,
        "plazaIds": plazaId,
        "isDeleted": "0",
        "flowType": "1",
        "startDate": startDate,
        "endDate": endDate
    }
    return getExcelData(token, url, data)


def detailExport(token, plazaId, startDate, endDate, timeType="M"):
    """品牌级 月 年"""
    url = "http://jyfx-svc.wandacm.cn/onemap-wanda/api/brand/level/total/detailExport"
    data = {
        "industryId": "1,1000285,1000290,102,103,104,24,37,41,44,46,825",
        "timeType": timeType,
        "plazaId": plazaId,
        "flowType": 1,
        "startDate": startDate,
        "endDate": endDate
    }
    return getExcelData(token, url, data)


def priceToRent(token, plazaId, startDate, endDate):
    url = "http://jyfx-svc.wandacm.cn/onemap-wanda/api/brandReatDetail/detailExport"
    data = {
        "plazaId": plazaId,
        "startDate": startDate,
        "endDate": endDate
    }
    return getExcelData(token, url, data)
