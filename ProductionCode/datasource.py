import psycopg2 as ps
from psycopg2 import sql as psql
import psqlConfig as config


def connect():
    """Connect to the PostgreSQL database."""
    try:
        connection = ps.connect(
            database=config.database,
            user=config.user,
            password=config.password
        )
        return connection
    except Exception as e:
        print("Connection error: ", e)
        exit()


def get_energy_by_region(connection):
    """Total energy consumption grouped by data center region.

    Args:
        connection: psycopg2 database connection

    Returns:
        list - a list of (region, total_energy_kwh) tuples, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        query = """
            SELECT
                data_center_region,
                SUM(total_energy_kwh::numeric) AS total_energy_kwh
            FROM llm_energy
            WHERE data_center_region IS NOT NULL
              AND data_center_region <> ''
              AND total_energy_kwh IS NOT NULL
              AND total_energy_kwh <> ''
              AND total_energy_kwh NOT IN ('Not disclosed', 'Not specified')
            GROUP BY data_center_region
            ORDER BY total_energy_kwh DESC;
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print("Query error: ", e)
        return None
    finally:
        cursor.close()


def get_top_models_by_parameters(connection):
    """Retrieves the top 5 models with the largest parameter counts.

    Args:
        connection: psycopg2 database connection

    Returns:
        list - a list of (model_name, model_parameters_billion) tuples, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        query = """
            SELECT
                model_name,
                model_parameters_billion::numeric AS model_parameters_billion
            FROM llm_energy
            WHERE model_name IS NOT NULL
              AND model_name <> ''
              AND model_parameters_billion IS NOT NULL
              AND model_parameters_billion <> ''
              AND model_parameters_billion NOT IN ('Not disclosed', 'Not specified')
            ORDER BY model_parameters_billion DESC
            LIMIT 5;
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        return None
    finally:
        cursor.close()


def main():
    connection = connect()

    results1 = get_energy_by_region(connection)
    if results1 is not None:
        print("Energy consumption by region: ")
        for region, total in results1:
            print(f"{region}: {total:,.0f} kWh")

    results2 = get_top_models_by_parameters(connection)
    if results2 is not None:
        print("\nTop 5 models by parameter count: ")
        for model, params in results2:
            print(f"{model}: {params}B")

    connection.close()


if __name__ == "__main__":
    main()
