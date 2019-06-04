# Brodie Heywood
# May 16, 2019

"""
csv_reader.py
Get list of MPs from Commons (csv format)
Select and manipulate data for visualization
"""

# TODO: scrape name of parliament (eg. 42nd Parliament) and refactor CSV to this name
# TODO: list possible criteria to group by, allow user/program to select (df.columns or df.iloc?) - allow multiple
# TODO: setup to automatically determine csv encoding
# TODO: aggregate scores to get average https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm
# TODO: provide aggregation options (allow user/program to select)
# TODO: write unittests, doctests where applicable
# TODO: more CSVs (ministry, secretaries, by-election candidates(?))

import numpy
import os
import pandas
import requests


def download_file(url):
    """Downloads file from website.

    :param url: must be direct download link
    :return: file object
    """
    downloaded_file = requests.get(url)
    return downloaded_file


def save_file(filename, file_object):
    """Saves file to script's parent directory."""
    with open(filename, 'wb') as reader:
        reader.write(file_object.content)


def rename_file(old_filename, new_filename):
    """Rename file."""
    os.rename(old_filename, new_filename)


def rename_and_overwrite_file(source_filename, destination_filename):
    """Rename source file to destination filename; replace destination file."""
    os.replace(source_filename, destination_filename)


def create_dataframe_from_csv(filename, file_encoding):
    """Creates dataframe from CSV."""
    dataframe = pandas.read_csv(filename, encoding=file_encoding)
    return dataframe


def group_data_by_selection(dataframe, grouping_selection_list):
    """Groups data by selected criteria (cf. groupby method).

    :param dataframe: dataframe created by Pandas package from CSV
    :param grouping_selection_list: must be list containing criteria names
    defined by first row of CSV (column headers)
    :return: dataframe
    """
    grouped_data = dataframe.groupby(grouping_selection_list)
    return grouped_data


def aggregate_by_size(dataframe):
    """Aggregates data in dataframe to show number of entities.

    Counts number of entities, rather than listing them (cf. agg method).
    :return: dataframe
    """
    size_aggregation = dataframe.agg(numpy.size)['First Name']
    return size_aggregation


def main():
    """Execute the program."""

    # Provide URL of CSV download link (right-click on CSV button and copy link address)
    mp_csv_url = 'https://www.ourcommons.ca/Parliamentarians/en/members/export?output=CSV&listSeperator=,'
    # Provide name of CSV (it's default name, when the CSV is downloaded from the website)
    mp_csv_filename = 'Export.csv'
    # Specify file encoding (usually UTF-8)
    mp_csv_encoding = 'windows-1252'

    # Download CSV file
    mp_csv = download_file(mp_csv_url)
    # Save CSV file into parent directory
    save_file(mp_csv_filename, mp_csv)

    # Downloaded CSVs have filename "Export.csv"; rename the file:
    # Choose new filename
    new_mp_csv_filename = 'List_of_MPs.csv'
    # Rename file and replace older version
    rename_and_overwrite_file(mp_csv_filename, new_mp_csv_filename)
    # Associate mp_csv_filename object with new name
    mp_csv_filename = new_mp_csv_filename

    # Create dataframe from CSV
    mp_dataframe = create_dataframe_from_csv(mp_csv_filename, mp_csv_encoding)

    print(mp_dataframe)

    # Choose criteria to group data by
    grouping_selections = ['Political Affiliation', 'Province / Territory']
    # Group data
    grouped_data = group_data_by_selection(mp_dataframe, grouping_selections)
    # Aggregate data to find size of each group
    size_grouped_data = aggregate_by_size(grouped_data)
    # Display grouped and aggregated data
    print(size_grouped_data)

    size_grouped_data.to_csv("Test.csv", sep='\t', encoding='utf-8')


"""
Other methods that might be helpful:

view entry
print(df['Last Name'][2])

find unique entries for given column, count number of each
print(df['Political Affiliation'].value_counts())

describes numeric columns with mean, std dev, etc.
print(df.describe())

for average (code below is example only):
df_education_scores = df.groupby('education_sentiment')
print(df_education_scores['score'].mean().sort_values(ascending=False))
"""

if __name__ == '__main__':
    main()
