import re
import requests


def calculate_marginal_tax(income, marginal_tax_brackets):
    assert isinstance(marginal_tax_brackets, list)

    total_tax = 0.
    for marginal_tax_rate, marginal_income in marginal_tax_brackets:
        marginal_taxable_income = min(marginal_income, income)
        income -= marginal_taxable_income
        total_tax += marginal_taxable_income * marginal_tax_rate
    return round(total_tax, 2)


def calculate_inflation(start_date, end_date, amount):
    url = 'https://www.statbureau.org/calculate-inflation-price-jsonp?'
    params = {'country': 'united-states',
              'start': start_date,
              'end': end_date,
              'amount' : amount}

    result = requests.get(url, params=params)
    formatted_result = re.sub(r'[^\d.]+', '', result.text)

    return float(formatted_result)
