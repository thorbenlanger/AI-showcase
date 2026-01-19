import random
import argparse
import pandas as pd
from datetime import datetime, timedelta

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--rows", type=int, default=1000)
    args = ap.parse_args()

    rows = []
    for i in range(args.rows):
        rows.append({
            "customer_id": i if random.random() > 0.02 else i-1,
            "email": f"user{i}@example.com" if random.random() > 0.05 else "invalid_mail",
            "country_code": random.choice(["DE","AT","CH","XX"]),
            "age": random.choice([random.randint(18,80), -1, 999]),
            "revenue_eur": random.choice([round(random.uniform(10,2000),2), -50])
        })

    pd.DataFrame(rows).to_csv(args.out, index=False)

if __name__ == "__main__":
    main()
