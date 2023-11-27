import logging

DATE_FILTERS = [
    "fromYear",
    "toYear",
]

EXPERIENCE_AVAILABLE_FILTERS = [
    "companyName",
    "locationType"
]
EXPERIENCE_AVAILABLE_FILTERS.extend(DATE_FILTERS)


def is_valid_experience(experience: dict, filters: dict) -> bool:
    print(filters)

    for filter_key, filter_value in filters.items():
        try:
            if filter_key in DATE_FILTERS:
                if filter_key == "fromYear":
                    value = int(experience.get("startDate").get("year"))
                if filter_key == "toYear":
                    value = int(experience.get("endDate").get("year"))

                filter_value = int(filter_value)
            else:
                filter_value = filter_value.lower()
                value = experience.get(filter_key)
                value = value.lower().strip()
        except ValueError as e:
            logging.error(f"Something went wrong while parsing query paramenters: {str(e)}")
            raise e

        if filter_key == "companyName" and value != filter_value:
            print("DADA")
            return False

        if filter_key == "fromYear" and value < filter_value:
            return False

        if filter_key == "toYear" and value > filter_value:
            return False

        if filter_key == "locationType" and value != filter_value: 
            return False

    return True
