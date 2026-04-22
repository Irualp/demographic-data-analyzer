import pandas as pd


def calculate_demographic_data(print_data=True):
    # data from file
    df = pd.read_csv("adult.data.csv", names=[
        "age","workclass","fnlwgt","education","education-num",
        "marital-status","occupation","relationship","race","sex",
        "capital-gain","capital-loss","hours-per-week","native-country","salary"
    ], skipinitialspace=True)

    # Fix data typ
    df["age"] = pd.to_numeric(df["age"])
    df["hours-per-week"] = pd.to_numeric(df["hours-per-week"])

    # 1. Number of
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4. Percentage with advanced education earning >50K
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round(
        (df[higher_education]["salary"] == ">50K").mean() * 100, 1
    )

    # 5. Percentage without advanced education earning >50K
    lower_education = ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_education_rich = round(
        (df[lower_education]["salary"] == ">50K").mean() * 100, 1
    )

    # 6. Min hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of rich among those who work fewest hours
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (min_workers["salary"] == ">50K").mean() * 100, 1
    )

    # 8. Country with highest percentage of >50K
    country_rich = df.groupby("native-country")["salary"].apply(
        lambda x: (x == ">50K").mean() * 100
    )
    highest_earning_country = country_rich.idxmax()
    highest_earning_country_percentage = round(country_rich.max(), 1)

    # 9. Most popular occupation in India (>50K)
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]
    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Rich percentage among min workers:", rich_percentage)
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest % of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }


# Run program
if __name__ == "__main__":
    calculate_demographic_data()
