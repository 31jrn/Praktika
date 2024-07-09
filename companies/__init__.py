import os
import importlib


def load_companies():
    companies = {}
    for file in os.listdir(os.path.dirname(__file__)):
        if file.endswith(".py") and not file.startswith("_"):
            module_name = file[:-3]
            module = importlib.import_module(f'companies.{module_name}')
            class_name = ''.join([word.capitalize() for word in module_name.split('_')])
            company_class = getattr(module, class_name)
            companies[module_name] = company_class()
    return companies
