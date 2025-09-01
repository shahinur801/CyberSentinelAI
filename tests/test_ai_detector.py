import pandas as pd
from src.ai_detector import detect_anomalies

def test_detect_anomalies():
    test_data = pd.DataFrame({
        "event_value": [10, 12, 99, 11, 9]
    })
    test_data.to_csv("test_logs.csv", index=False)
    anomalies = detect_anomalies("test_logs.csv")
    assert len(anomalies) == 1  # Should flag 99 as anomaly

if __name__ == "__main__":
    test_detect_anomalies()
    print("All tests passed!")
