import pyupbit

access = "NEXhZrgQRjEKpVayR73rPsiQHLv6lydJ7k1c5LsS"          # 본인 값으로 변경
secret = "Dx40Zd1dKq0vlDhqyxZnx0ncSki7htEZLooXOGiN"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

current_price = get_current_price("KRW-ETH")
krw=upbit.get_balance("KRW")
print(current_price)
print(krw)

ret = upbit.buy_limit_order("KRW-XRP", 100, 50)
print(ret)