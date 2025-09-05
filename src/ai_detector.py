import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(csv_file_path):
    """
    Detect anomalies in event data using Isolation Forest algorithm.
    
    Args:
        csv_file_path (str): Path to CSV file containing event data
        
    Returns:
        list: List of anomaly indices
    """
    # Load data from CSV
    data = pd.read_csv(csv_file_path)
    
    # Check if event_value column exists
    if 'event_value' not in data.columns:
        raise ValueError("CSV must contain 'event_value' column")
    
    # Prepare data for anomaly detection
    X = data[['event_value']].values
    
    # Use Isolation Forest for anomaly detection
    clf = IsolationForest(contamination=0.1, random_state=42)
    anomaly_predictions = clf.fit_predict(X)
    
    # Get indices of anomalies (where prediction is -1)
    anomaly_indices = np.where(anomaly_predictions == -1)[0]
    
    return anomaly_indices.tolist()
