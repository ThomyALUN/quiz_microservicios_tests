import random

def generate_fake_record_labels(n):
    countries = ['USA', 'UK', 'Germany', 'France', 'Japan']
    labels = []
    for _ in range(n):
        labels.append({
            "name": f"Label_{random.randint(1000, 9999)}",
            "country": random.choice(countries)
        })
    return labels
