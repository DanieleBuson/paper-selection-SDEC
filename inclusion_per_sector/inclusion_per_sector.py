import pandas as pd
import re


acm = pd.read_csv("inclusionStep/acm_inclusion_final.csv")
ieee = pd.read_csv("inclusionStep/ieee_inclusion_final.csv")
philpapers = pd.read_csv("inclusionStep/philpapers_inclusion_final.csv")
springer = pd.read_csv("inclusionStep/springer_inclusion_final.csv")


def remove_special_characters_lower(input_string):

    pattern = re.compile('[^A-Za-z0-9 ]+')
    result_string = pattern.sub('', input_string).lower()
    return result_string


def get_score(cleaned_string, keywords):
    
    count = 0
    total_count = 0
    word_list = cleaned_string.split(" ")
    for word in word_list:
        if word in keywords:
            count += keywords[word]
            total_count += 1
        else:
            total_count += 1
    score = count/total_count
    return score

def get_count_library(library, keywords):
    count = 0
    for i in library.index:
        
        score = 0
        
        string_1 = library.loc[i, "Title"]
        string_2 = library.loc[i, "Abstract"]

        cleaned_string_1 = remove_special_characters_lower(string_1)
        cleaned_string_2 = remove_special_characters_lower(string_2)

        score += get_score(cleaned_string_1, keywords)
        score += get_score(cleaned_string_2, keywords)

        if score > 0:
            count += 1

    return count


# keywords

service_dict = {
    'smart-cities': 1,
    'healthcare': 1,
    'government': 1,
    'education': 1,
    'transportation': 1,
    'security': 1,
    'finance': 1
}

technology_field_dict = {
    'AI': 1,
    'gaming': 1,
    'media': 1,
    'blockchain': 1,
    'robotics': 1,
    'analytics': 1,
    'cybersecurity': 1
}

sector_dict = {
    'industrial': 1,
    'NGO': 1,
    'public': 1,
    'academic': 1,
    'private': 1,
    'non-profit': 1,
    'health': 1
}

reflections_analysis_dict = {
    'sustainability': 1,
    'privacy': 1,
    'responsibility': 1,
    'equity': 1,
    'transparency': 1,
    'regulation': 1
}

# ACM 
    
print(f"\nACM - service count: {get_count_library(acm, service_dict)}")
print(f"ACM - technology/field count: {get_count_library(acm, technology_field_dict)}")
print(f"ACM - sector count: {get_count_library(acm, sector_dict)}")
print(f"ACM - reflections/analysis count: {get_count_library(acm, reflections_analysis_dict)}")


# IEEE

print(f"\nIEEE- service count: {get_count_library(ieee, service_dict)}")
print(f"IEEE- technology/field count: {get_count_library(ieee, technology_field_dict)}")
print(f"IEEE- sector count: {get_count_library(ieee, sector_dict)}")
print(f"IEEE- reflections/analysis count: {get_count_library(ieee, reflections_analysis_dict)}")


# Philpapers

print(f"\nPhilpapers - service count: {get_count_library(philpapers, service_dict)}")
print(f"Philpapers - technology/field count: {get_count_library(philpapers, technology_field_dict)}")
print(f"Philpapers - sector count: {get_count_library(philpapers, sector_dict)}")
print(f"Philpapers - reflections/analysis count: {get_count_library(philpapers, reflections_analysis_dict)}")


# Springer

print(f"\nSpringer - service count: {get_count_library(springer, service_dict)}")
print(f"Springer - technology/field count: {get_count_library(springer, technology_field_dict)}")
print(f"Springer - sector count: {get_count_library(springer, sector_dict)}")
print(f"Springer - reflections/analysis count: {get_count_library(springer, reflections_analysis_dict)}")