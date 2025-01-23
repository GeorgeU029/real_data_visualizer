import pycountry

def get_country_code(country_name):
    """Return the 2-letter country code for a given country."""
    try:
        country = pycountry.countries.get(name=country_name)
        if country:
            return country.alpha_2.lower()  # Use .lower() to convert the code to lowercase
    except KeyError:
        pass
    return None  # Return None if the country is not found

