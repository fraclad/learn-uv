import pandas as pd

data = {
    "name": ["hello", "world"],
    "notes": ["this is a note", "this is another note"]
}

df = pd.DataFrame(data)

print(df)