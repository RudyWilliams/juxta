import datetime
from faker import Faker
import pandas as pd

fake = Faker()
Faker.seed(1)

data_len = 10
intake_range = [
    datetime.date(year=2018, month=1, day=1),
    datetime.date(year=2019, month=12, day=31),
]
exit_range = [
    datetime.date(year=2019, month=1, day=1),
    datetime.date(year=2019, month=12, day=31),
]  # for this purpose, we don't care if the exit date is before the intake date

first_names = [fake.first_name() for _ in range(data_len)]
last_names = [fake.last_name() for _ in range(data_len)]
intake_dts = [
    fake.date_between_dates(intake_range[0], intake_range[1]) for _ in range(data_len)
]
exit_dts = [
    fake.date_between_dates(exit_range[0], exit_range[1]) for _ in range(data_len)
]
release_reasons = [fake.random_element() for _ in range(data_len)]

# repeat a person
n_repeats = 2

f_name = [first_names[3]] * n_repeats + [first_names[2]]
l_name = [last_names[3]] * n_repeats + [last_names[2]]

new_intakes = [
    fake.date_between_dates(intake_range[0], intake_range[1])
    for _ in range(n_repeats + 1)
]
new_exits = [
    fake.date_between_dates(exit_range[0], exit_range[1]) for _ in range(n_repeats + 1)
]
new_release_reasons = ["b"] * (n_repeats + 1)

first_names.extend(f_name)
last_names.extend(l_name)
intake_dts.extend(new_intakes)
exit_dts.extend(new_exits)
release_reasons.extend(new_release_reasons)

df1 = pd.DataFrame(
    {
        "last_name": last_names,
        "first_name": first_names,
        "intake_dt": intake_dts,
        "exit_dt": exit_dts,
        "release_reason": release_reasons,
    }
)

df2 = df1.copy()
# make some changes
df2.iloc[3, 4] = "a"
df2.iloc[10, 4] = "a"
df2.iloc[11, 3] = datetime.date(year=2019, month=11, day=20)
df2.iloc[7, 3] = datetime.date(year=2019, month=4, day=6)

df2 = df2.sample(frac=1, random_state=5)

# print(df1)
# print("------------")
# print(df2)
classification = "mismatches"
df1.to_csv(
    f"juxta/tests/data/{classification}/many-to-many/many_to_many-A1.csv", index=False,
)
df2.to_csv(
    f"juxta/tests/data/{classification}/many-to-many/many_to_many-A2.csv", index=False,
)
