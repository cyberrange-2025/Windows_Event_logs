import pandas as pd

df = pd.read_csv('logs/Security.csv')
suspicious = df[df['Id'] == 4625]  # Failed Logon
print("Suspicious Logons:")
print(suspicious[['TimeCreated', 'TargetUserName', 'IpAddress']])