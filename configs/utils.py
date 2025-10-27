import os

from numpy import dtype
import polars as pl

dog_move_data_schema = {
        'DogID': pl.Int64,
        'TestNum': pl.Int64,
        't_sec': pl.Float64,
        'ABack_x': pl.Float64, 
        'ABack_y': pl.Float64, 
        'ABack_z': pl.Float64, 
        'ANeck_x': pl.Float64, 
        'ANeck_y': pl.Float64, 
        'ANeck_z': pl.Float64, 
        'GBack_x': pl.Float64, 
        'GBack_y': pl.Float64, 
        'GBack_z': pl.Float64, 
        'GNeck_x': pl.Float64, 
        'GNeck_y': pl.Float64, 
        'GNeck_z': pl.Float64, 
        'Task': pl.Utf8, 
        'Behavior_1': pl.Utf8, 
        'Behavior_2': pl.Utf8, 
        'Behavior_3': pl.Utf8, 
        'PointEvent': pl.Utf8
}

dog_move_data_widowed_schema = {
        'DogID':       pl.Int64,
        'TestNum':     pl.Int64,
        't_dt':        pl.Datetime,
        'n_samples':   pl.UInt32,
        't_sec':       pl.List(pl.Float64),
        'ABack_x':     pl.List(pl.Float64),
        'ABack_y':     pl.List(pl.Float64),
        'ABack_z':     pl.List(pl.Float64),
        'ANeck_x':     pl.List(pl.Float64),
        'ANeck_y':     pl.List(pl.Float64),
        'ANeck_z':     pl.List(pl.Float64),
        'GBack_x':     pl.List(pl.Float64),
        'GBack_y':     pl.List(pl.Float64),
        'GBack_z':     pl.List(pl.Float64),
        'GNeck_x':     pl.List(pl.Float64),
        'GNeck_y':     pl.List(pl.Float64),
        'GNeck_z':     pl.List(pl.Float64),
        'Behavior_1':  pl.List(pl.Utf8),
    }

dog_info_schema = {'DogID': pl.Int64, 
                   'Breed': pl.Utf8, 
                   'Weight': pl.Int64, 
                   'Age months': pl.Int64, 
                   'Gender': pl.Int64, 
                   'NeuteringStatus': pl.Int64}

def load_data(dir_path: str, file_name: str, n_rows: int = None) -> pl.DataFrame:
    """
    Carrega um arquivo CSV em um DataFrame do Polars.

    Args:
        dir_path (str): Caminho do diretório onde o arquivo está localizado.
        file_name (str): Nome do arquivo CSV.
        n_rows (int, optional): Número de linhas a serem carregadas. Se None, carrega todas as linhas.

    Returns:
        pl.DataFrame: DataFrame contendo os dados carregados.
    """
    file_path = os.path.join(dir_path, file_name)
    return pl.read_csv(file_path, n_rows=n_rows)

def load_large_data(dir_path: str, file_name: str, schema: dict = {}) -> pl.LazyFrame:
    """
    Carrega um arquivo CSV grande em um LazyFrame do Polars.

    Args:
        dir_path (str): Caminho do diretório onde o arquivo está localizado.
        file_name (str): Nome do arquivo CSV.
        schema (dict, optional): Dicionário definindo o esquema das colunas. Se None, o esquema será inferido automaticamente.
        
    Returns:
        pl.LazyFrame: LazyFrame contendo planos de carregamento dos dados.
    """
    file_path = os.path.join(dir_path, file_name)
    if schema:
        return pl.scan_csv(file_path, dtypes=schema)
    return pl.scan_csv(file_path)

def load_parquet(dir_path: str, file_name: str, schema: dict = {}) -> pl.LazyFrame:
    """
    Carrega um arquivo parquet grande em um LazyFrame do Polars.

    Args:
        dir_path (str): Caminho do diretório onde o arquivo está localizado.
        file_name (str): Nome do arquivo parquet.
        schema (dict, optional): Dicionário definindo o esquema das colunas. Se None, o esquema será inferido automaticamente.
        
    Returns:
        pl.LazyFrame: LazyFrame contendo planos de carregamento dos dados.
    """

    file_path = os.path.join(dir_path, file_name)
    if schema:
        return pl.scan_parquet(file_path, schema=schema)
    return pl.scan_parquet(file_path)


