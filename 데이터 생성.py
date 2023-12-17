import random
import pandas as pd

def generate_country_data(country_name):
    gdp = round((random.uniform(0, 1) ** 3) * (1e5 - 1e3) + 1e3)
    gdp_scale = (gdp - 1e3) / (1e5 - 1e3)

    birth_rate = round(2.5 - gdp_scale * 1 + random.uniform(-1, 1) * (1 - gdp_scale), 1)
    unemployment_rate = round(3 + (20 - 3) * gdp_scale + random.uniform(-1, 1) * (1 - gdp_scale), 1)
    gini_index = round(50 + (95 - 50) * gdp_scale + random.uniform(-5, 5) * gdp_scale, 2)
    poverty_rate = round(5 + (50 - 5) * gini_index/95 + random.uniform(-2, 2) * (1 - gdp_scale), 1)
    suicide_rate = round(3 + (50 - 3) * gdp_scale + random.uniform(-2, 2) * (1 - gdp_scale), 1)
    happiness_index = round(50 + (90 - 50) * (1 - gdp_scale) + random.uniform(-5, 5) * (1 - gdp_scale), 1)
    internet_usage = round(10 + (90 - 10) * gdp_scale + random.uniform(-5, 5) * gdp_scale, 1)
    college_rate = round(20 + (80 - 20) * gdp_scale + random.uniform(-5, 5) * gdp_scale, 1)
    crime_rate = round(5 + (90 - 5) * gdp_scale, 1)
    health_index = round(30 + (90 - 30) * (1 - gdp_scale) + random.uniform(-5, 5) * (1 - gdp_scale), 1)

    data = {
        '국가 이름': country_name,
        '평균 기온': round(random.uniform(10, 30), 1),
        '1인당 GDP': gdp,
        '출산률': max(min(birth_rate, 4), 1),
        '지니계수': gini_index,
        '면적': random.randint(50000, 2000000),
        '인터넷 이용률': internet_usage,
        '대학 진학률': college_rate,
        '행복지수': happiness_index,
        '실업률': unemployment_rate,
        '평균수명': round(max(min(40 + (85 - 40) * (1 - gdp_scale) + random.uniform(-5, 5) * (1 - gdp_scale), 85), 40), 1),
        '보건지표': health_index,
        '환경지표': round(random.uniform(70, 90), 1),
        '범죄율': crime_rate,
        '성평등지수': round(random.uniform(0.5, 1), 2),
        '빈곤율': max(min(poverty_rate, 50), 5),
        '자살율': suicide_rate
    }
    return data

groups = ['A', 'B', 'C', 'D', 'E']
country_data_list = []

for group in groups:
    for i in range(1, 11):
        country_name = f"{group}{i}"
        country_data = generate_country_data(country_name)
        country_data_list.append(country_data)

df = pd.DataFrame(country_data_list)
df.to_excel("country_data.xlsx", index=False)
