import pandas as pd
df = pd.read_csv("customer_churn.csv")

# Sample random 2000 rows if dataset length exceeds 100,000
if len(df) > 100000:
    print(f"\nDataset contains {len(df)} rows. Sampling 2000 rows randomly...")
    df = df.sample(n=2000, random_state=42)
    print(f"Sampled dataset shape: {df.shape}")

df.to_csv("sampled_churn_data.csv", index=False, encoding="utf-8")
print("Data exported to 'sampled_churn_data.csv'")

