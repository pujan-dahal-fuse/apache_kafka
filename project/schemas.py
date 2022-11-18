country_prize_category_schema = {
    "type": "struct",
    "optional": "false",
    "fields": [
        {
            "type": "string",
            "optional": "false",
            "field": "country"
        },
        {
            "type": "int64",
            "optional": "false",
            "field": "chemistry"
        },
        {
            "type": "int64",
            "optional": "false",
            "field": "economics"
        },
        {
            "type": "int64",
            "optional": "false",
            "field": "literature"
        },
        {
            "type": "int64",
            "optional": "false",
            "field": "medicine"
        },
        {
            "type": "int64",
            "optional": "false",
            "field": "peace"
        },
        {
            "type": "int64",
            "optional": "false",
            "field": "physics"
        }
    ]
}

country_prize_gender_schema = {
    "type": "struct",
    "optional": "false",
    "fields": [
        {
            "type": "string",
            "optional": "false",
            "field": "country"
        },
        {
            "type": "int64",
            "optional": "false",
            "field": "female_count"
        },
        {
            "type": "int64",
            "optional": "false",
            "field": "male_count"
        },
        {
            "type": "float",
            "optional": "false",
            "field": "female_pct"
        },
        {
            "type": "float",
            "optional": "false",
            "field": "male_pct"
        },
        {
            "type": "float",
            "optional": "false",
            "field": "female_avg_age"
        },
        {
            "type": "float",
            "optional": "false",
            "field": "male_avg_age"
        },
        {
            "type": "float",
            "optional": "false",
            "field": "country_avg_age"
        }
    ]
}


year_category_laureates_schema = {
    "type": "struct",
    "optional": "false",
    "fields": [
        {
            "type": "int64",
            "optional": "false",
            "field": "prize_year"
        },
        {
            "type": "array",
            "optional": "false",
            "field": "chemistry",
            "items": {
                "type": "string"
            }
        },
        {
            "type": "array",
            "optional": "false",
            "field": "economics",
            "items": {
                "type": "string"
            }
        },
        {
            "type": "array",
            "optional": "false",
            "field": "literature",
            "items": {
                "type": "string"
            }
        },
        {
            "type": "array",
            "optional": "false",
            "field": "medicine",
            "items": {
                "type": "string"
            }
        },
        {
            "type": "array",
            "optional": "false",
            "field": "peace",
            "items": {
                "type": "string"
            }
        },
        {
            "type": "array",
            "optional": "false",
            "field": "physics",
            "items": {
                "type": "string"
            }
        }
    ]
}
