import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on stearns

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="stearns.wpi.edu")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def get_energy_by_region(connection):
    """Total energy consumption grouped by data center region.

        Args:
        connection (psycopg2.connection) - the connection to the database

        Returns:
        list - a list of (region, total_energy_kwh) tuples, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        query = """
            SELECT data_center_region, SUM(total_energy_kwh) as total
            FROM llm_energy
            WHERE total_energy_kwh IS NOT NULL
            GROUP BY data_center_region
            ORDER BY total DESC;
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print("Query error: ", e)
        return None
    
def get_top_models_by_parameters(connection) -> list:
    """Retrieves the top 5 models with the largest parameter counts.

    Args:
        connection (psycopg2.connection) - the connection to the database

    Returns:
        list - a list of (model_name, model_parameters_billion) tuples, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        query = """
            SELECT model_name, model_parameters_billion
            FROM llm_energy
            WHERE model_parameters_billion IS NOT NULL
            ORDER BY model_parameters_billion DESC
            LIMIT 5;
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        return None

def main():
    connection = connect()
    results1 = get_energy_by_region(connection)
    if results1 is not None:
        print("Energy consumption by region: ")
        for item in results1:
            print(f"{item[0]}: {item[1]:,.0f} kWh")
    
    results2 = get_top_models_by_parameters(connection)
    if results2 is not None:
        print("\nTop 5 models by parameter count: ")
        for item in results2:
            print(f"{item[0]}: {item[1]}B")
    
    connection.close()

if __name__ == "__main__":
    main()