# opensky-python

한줄 결론 : 폐급 API

```python
from pyopensky.trino import Trino

trino = Trino()

def test_history() -> None:
    df = trino.history(
        "2025-01-01 00:00",
        "2025-01-02 00:00",
        #departure_airport="MMUN", # Cancun, Mexico
        #arrival_airport="KBWI", # Baltimore, US
        callsign="SWA1608",
        compress=True,
    )
    if df is not None:
        df.to_csv('output.csv', index=False, encoding='utf-8-sig')
        print("Complete")
    else:
        print("No data")

if __name__ == "__main__":
    test_history()
```

IFTA RUI 에서 항공기 callsign 과, 출발/도착 공항 나오는 비행기 골라서 테스트함

- `history` 함수에 파라미터가 엄청나게 많음 [링크](https://mode-s.org/pyopensky/trino.html#pyopensky.trino.Trino.history)
- 기본적인 `start_time`, `end_time` 은 UTC 로 적당히 기입
- `departure_airport`, "arrival_airport" 는 잘 동작하면 쿼리 속도 빨라질거 같은데, 동작을 안함. 주석처리해야 결과 나왔음
- `callsign` 은 일반적인 KE35 같은 코드는 아니지만, IFTA RUI 에서 어차피 보이니 상관 없음

## 결론
- `output.csv` 를 보면 매 초마다 위경도, 속도, 방향, 고도가 나와서 좋아보이지만 ADS-B 관측 데이터를 하는지 바다에 있을때는 나오지 않음
  - 예시 비행기는 칸쿤에서 볼티모어 가는 비행기인데, 마이애미 근처 와서야 관측이 시작됨. 또 해당 비행기의 정확한 출발/도착 시간을 모르면 데이터 구간이 매우 곤란해짐
- 가장 큰 문제는 느림
  - 대략 인터벌 24 hours 에 `callsign` 만 넣으면 `compress=False` (용량 더 먹고 속도 빠른 모드) 로 해도 **7.6859 초** 소요되었음
