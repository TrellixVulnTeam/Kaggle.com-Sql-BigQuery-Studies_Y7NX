from google.oauth2 import service_account
from google.cloud import bigquery

# Task: create your first Client object and Access a table then list 5 rows.
# Task: create a Client object and Access a table then print table schema
# Project: bigquery-public-data
# Dataset: chicago_crime
# Table: crime

credentials = service_account.Credentials.from_service_account_file("C:/Users/muhem/Desktop/"
                                                                    "sqlbigquerytraining-836d50cb80ec.json")

client = bigquery.Client(credentials=credentials)

dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

dataset = client.get_dataset(dataset_ref)

table_ref = dataset_ref.table("full")

table_full = client.get_table(table_ref)

print(client.list_rows(table_full, selected_fields=table_full.schema[:3], max_results=5).to_dataframe())


"""tables = list(client.list_tables(dataset))

for tb in tables:
    print(tb.table_id)"""