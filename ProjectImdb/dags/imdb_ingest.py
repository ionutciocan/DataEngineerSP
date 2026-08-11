import duckdb
import os


def load_imdb_data():
    print("Connecting to the Duckdb database...")
    con=duckdb.connect('warehouse.duckdb')
    con.execute("Install httpfs;") #duckdb are nevoie de asta ca sa citeasca fisiere de pe internet
    con.execute("Load httpfs;")
    #asta e lista de fisiere cerute
    imdb_files = [
        "title.basics",
        "title.ratings",
        "title.crew",
        "title.principals",
        "name.basics",
        "title.akas"
    ]
    base_url = "https://datasets.imdbws.com" #url-ul paginii de unde instalez fisierele
    os.makedirs("raw", exist_ok=True) #verifica daca directorul raw exista si daca nu il creaza el

    for file_name in imdb_files:
        url=f"{base_url}/{file_name}.tsv.gz" #asta e sursa de unde am luat-o are extensia.tsv.gz
        dest_parquet=f"raw/{file_name}.parquet" #asta e locul unde punem informatia
        query=f"""COPY(SELECT * FROM read_csv_auto('{url}',sep='\t',header=True,nullstr='\\N',sample_size=-1))TO '{dest_parquet}' (FORMAT PARQUET);"""#read_csv_auto ii spune query ului sa se duca direct pe linkul de pe internet si sa citeasca de acolo, sep ul ala ii spune ca in fisierele de tip tsv separatorii sunt taburile, header true ii spune ca primul rand e titlul coloanei acel \N ii spune ca atunci cand nu stie o informatie sa nu pune\N sa pune null acel -1 forteaza duckdb sa citeasca tot fisierul si dupa sa hotarasca ce tip de date contine        con.execute(query)
    con.close()
    print("The Ingestion successfully completed!")
