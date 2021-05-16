import time
import pyupbit
import datetime

access = "NEXhZrgQRjEKpVayR73rPsiQHLv6lydJ7k1c5LsS"          # 본인 값으로 변경
secret = "Dx40Zd1dKq0vlDhqyxZnx0ncSki7htEZLooXOGiN"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute3", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price



def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]



# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:

        target_price = get_target_price("KRW-XLM", 0.5)
        current_price = get_current_price("KRW-XLM")
        if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XLM", krw*0.9995) 
                    print("구매완료")
                    btc = get_balance("XLM")
                    t_end=time.time() + 180
                    while time.time() < t_end:
                        if(get_current_price("KRW-XLM")>(current_price)*1.01):
                            upbit.sell_market_order("KRW-XLM",btc)
                    if(btc>(5000/get_current_price("KRW-XLM"))):
                        upbit.sell_market_order("KRW-XLM", btc)
                        print("팔았땅")
                    else:print("잘 팔림!")

                else: print("이미 삼") #사면 여기로 바로 넘어옴.. 이유 알아낼 것.
                    

        #XLM = get_balance("XLM")
        #if XLM > 0.00008:
            #upbit.sell_market_order("KRW-XLM", XLM*0.9995)
    except Exception as e:
        print(e)
        time.sleep(1)