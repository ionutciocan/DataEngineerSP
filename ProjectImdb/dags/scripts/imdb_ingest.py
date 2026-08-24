import duckdb
import os


def load_imdb_data():
    print("Connecting to the Duckdb database...")
    con = duckdb.connect('warehouse.duckdb')

    imdb_files = [
        "title.basics",
        "title.ratings",
        "title.crew",
        "title.principals",
        "name.basics",
        "title.akas"
    ]

    source_folder = "data"
    os.makedirs("raw", exist_ok=True)

    for file_name in imdb_files:
        locale_route = f"{source_folder}/{file_name}.tsv.gz"
        dest_parquet = f"raw/{file_name}.parquet"

        query = f"""
            COPY (
                SELECT * FROM read_csv_auto('{locale_route}', sep='\t', header=True, nullstr='\\N', sample_size=-1)
            ) TO '{dest_parquet}' (FORMAT PARQUET);
        """

        con.execute(query)
        print(f"The file: {file_name} was saved in raw/")

    con.close()
    print("The Ingestion successfully completed!")