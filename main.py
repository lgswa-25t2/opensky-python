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
