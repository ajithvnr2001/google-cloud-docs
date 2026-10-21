---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/cloudsql_mysql_product_catalog_embeddings/
title: Vector Embedding Ingestion with Apache Beam and CloudSQL MySQL \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:40:36.011486+00:00
---

# Vector Embedding Ingestion with Apache Beam and CloudSQL MySQL  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/cloudsql_mysql_product_catalog_embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Vector Embedding Ingestion with Apache Beam and CloudSQL MySQL Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/cloudsql_mysql_product_catalog_embeddings.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/cloudsql_mysql_product_catalog_embeddings.ipynb)

# Introduction

This Colab demonstrates how to generate embeddings from data and ingest them into [CloudSQL MySQL](https://cloud.google.com/sql/docs/mysql). We'll use Apache Beam and Dataflow for scalable data processing. The goal of this notebook is to make it easy for users to get started with generating embeddings at scale using Apache Beam and storing them in CloudSQL MySQL. We focus on building efficient ingestion pipelines that can handle various data sources and embedding models.

## Example: Furniture Product Catalog

We'll work with a sample e-commerce dataset representing a furniture product catalog. Each product has:

  * **Structured fields:** `id`, `name`, `category`, `price`
  * **Detailed text descriptions:** Longer text describing the product's features.
  * **Additional metadata:** `material`, `dimensions`



## Pipeline Overview

We will build a pipeline to:

  1. Read product data
  2. Convert unstructured product data, to `Chunk`[1] type
  3. Generate Embeddings: Use a pre-trained Hugging Face model (via MLTransform) to create vector embeddings
  4. Write to CloudSQL MySQL: Store the embeddings in a CloudSQL MySQL vector database

Here's a visualization of the data flow: | Stage | Data Representation | Notes  
---|---|---  
**1\. Ingest Data** | `{`  
`"id": "desk-001",`  
`"name": "Modern Desk",`  
`"description": "Sleek...",`  
`"category": "Desks",`  
`...`  
`}` | Supports:  
\- Reading from batch (e.g., files, databases)  
\- Streaming sources (e.g., Pub/Sub).  
**2\. Convert to Chunks** | `Chunk(`   
`id="desk-001",`   
`content=Content(`   
`text="Modern Desk"`   
`),`   
`metadata={...}`   
`)` | \- `Chunk` is the structured input for generating and ingesting embeddings.  
\- `chunk.content.text` is the field that is embedded.  
\- Converting to `Chunk` does not mean breaking data into smaller pieces,  
it's simply organizing your data in a standard format for the embedding pipeline.  
\- `Chunk` allows data to flow seamlessly throughout embedding pipelines.  
**3\. Generate Embeddings** | `Chunk(`   
`id="desk-001",`  
`embedding=[-0.1, 0.6, ...],`  
`...)` | Supports:  
\- Local Hugging Face models  
\- Remote Vertex AI models  
\- Custom embedding implementations.  
**4\. Write to CloudSQL MySQL** | **CloudSQL MySQL Table (Example Row):**  
`id: desk-001`  
`embedding: [-0.1, 0.6, ...]`  
`name = "Modern Desk"`,  
`Other fields ...` | Supports:  
\- Custom schemas  
\- Conflict resolution strategies for handling updates  
  
[1]: Chunk represents an embeddable unit of input. It specifies which fields should be embedded and which fields should be treated as metadata. Converting to Chunk does not necessarily mean breaking your text into smaller pieces - it's primarily about structuring your data for the embedding pipeline. For very long texts that exceed the embedding model's maximum input size, you can optionally [use Langchain TextSplitters](https://beam.apache.org/releases/pydoc/2.63.0/apache_beam.ml.rag.chunking.langchain.html) to break the text into smaller `Chunk`'s.

## Execution Environments

This notebook demonstrates two execution environments:

  1. **DirectRunner (Local Execution)** : All examples in this notebook run on DirectRunner by default, which executes the pipeline locally. This is ideal for development, testing, and processing small datasets.

  2. **DataflowRunner (Distributed Execution)** : The Run on Dataflow section demonstrates how to execute the same pipeline on Google Cloud Dataflow for scalable, distributed processing. This is recommended for production workloads and large datasets.




All examples in this notebook can be adapted to run on Dataflow by following the pattern shown in the "Run on Dataflow" section.

# Connecting Apache Beam to CloudSQL MySQL

Beam uses the [CloudSQL MySQL Java Connector](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc.md) to securely establish a connection to your database. Apache Beam supports any parameters that can be passed to the Java Connector e.g. IP types.

# Setup and Prerequisites

This example requires:

  1. A CloudSQL MySQL instance with [cloudsql_vector](https://cloud.google.com/sql/docs/mysql/vector-search#requirements) flag enabled
  2. Apache Beam 2.67.0 or later



## Install Packages and Dependencies

First, let's install the Python packages required for the embedding and ingestion pipeline:
    
    
    # Apache Beam with GCP support
    pip install apache_beam[interactive,gcp]>=2.67.0 --quiet
    # Huggingface sentence-transformers for embedding models
    pip install sentence-transformers --quiet
    
    
    pip show apache-beam

Next, let's install cloud-sql-python-connector to help set up our test database.
    
    
    pip install "cloud-sql-python-connector[pymysql]>=1.0.0,<2.0.0" sqlalchemy --quiet

## Database Setup

To connect to CloudSQL MySQL, you'll need:

  1. GCP project ID where the CloudSQL MySQL instance is located
  2. The CloudSQL MySQL connection URI. This is the fully qualified connection name of the CloudSQL MySQL instance found in the google cloud console under CloudSQL > Instances > Instance > Connect to this Instance > Connection name.
  3. Database name. This is the name of the mysql database within your CloudSQL MySQL instance. The default database name is mysql.
  4. Database credentials
  5. A CloudSQL MySQL instance with cloudsql_vector flag enabled



Replace these placeholder values with your actual CloudSQL MySQL connection details:
    
    
    PROJECT_ID = "" # @param {type:'string'}
    
    CONNECTION_NAME = "" # @param {type:'string'}
    
    DB_NAME = "" #  @param {type:'string'}
    
    DB_USER = "" # @param {type:'string'}
    
    DB_PASSWORD = "" # @param {type:'string'}
    

## Authenticate to Google Cloud

To connect to the CloudSQL MySQL instance via the language conenctor, we authenticate with Google Cloud.
    
    
    import sys
    if 'google.colab' in sys.modules:
      from google.colab import auth
      auth.authenticate_user(project_id=PROJECT_ID)
    
    
    
    # @title SQLAlchemy + CloudSQL MySQL Connector helpers for creating tables and verifying data
    
    import sqlalchemy
    from sqlalchemy import text
    from sqlalchemy.exc import SQLAlchemyError
    from google.cloud.sql.connector import Connector
    
    def get_db_engine(connection_name: str, user: str, password: str, db: str, **connect_kwargs) -> sqlalchemy.engine.Engine:
        """
        Creates a SQLAlchemy engine configured for CloudSQL MySQL.
    
        To use this function, you may need to install necessary libraries:
        'pip install google-cloud-sql-connector[pymysql] sqlalchemy'
    
        Args:
            connection_name: CloudSQL MySQL instance connection name (e.g., "project:region:instance").
            user: The database user.
            password: The database password.
            db: The name of the database.
            connect_kwargs: Additional keyword arguments for the connector (e.g., ip_type="PUBLIC").
    
        Returns:
            A SQLAlchemy engine instance.
        """
        connector = Connector()
    
        def get_conn() -> sqlalchemy.engine.base.Connection:
            """Helper function to create a database connection."""
            conn = connector.connect(
                connection_name,
                "pymysql",  # Use the PyMySQL driver for MySQL
                user=user,
                password=password,
                db=db,
                **connect_kwargs
            )
            return conn
    
        # Create the SQLAlchemy engine using the connection function
        engine = sqlalchemy.create_engine(
            "mysql+pymysql://",  # Use the MySQL+PyMySQL dialect
            creator=get_conn,
        )
    
        # This hook ensures the connector is closed when the engine is disposed
        engine.pool.dispose = lambda: connector.close()
    
        return engine
    
    def setup_db_table_sqlalchemy(connection_name: str,
                                     database: str,
                                     table_name: str,
                                     table_schema: str,
                                     user: str,
                                     password: str,
                                     **connect_kwargs):
        """
        Sets up a CloudSQL MySQL table using SQLAlchemy.
    
        This function will drop the table if it already exists and then create it
        based on the provided schema.
    
        Args:
            connection_name: CloudSQL MySQL instance connection name.
            database: The name of the database.
            table_name: The name of the table to create.
            table_schema: SQL string defining the table columns. For MySQL, use types like
                          'INT AUTO_INCREMENT PRIMARY KEY'. For embeddings, consider using
                          'JSON' or 'BLOB' to store the vector data.
                          Example: "id INT AUTO_INCREMENT PRIMARY KEY, embedding JSON"
            user: The database user.
            password: The database password.
            connect_kwargs: Additional keyword arguments for the connector.
        """
        engine = None
        try:
            engine = get_db_engine(connection_name, user, password, database, **connect_kwargs)
    
            with engine.connect() as connection:
                # Use autocommit for DDL statements
                with connection.execution_options(isolation_level="AUTOCOMMIT"):
                    print("Connected to MySQL DB successfully via SQLAlchemy!")
    
                    # Use backticks for table names for MySQL compatibility
                    print(f"Dropping table `{table_name}` if it exists...")
                    connection.execute(text(f"DROP TABLE IF EXISTS `{table_name}`;"))
    
                    print(f"Creating table `{table_name}`...")
                    create_sql = f"""
                    CREATE TABLE IF NOT EXISTS `{table_name}` (
                        {table_schema}
                    );
                    """
                    connection.execute(text(create_sql))
    
            print("MySQL table setup completed successfully!")
    
        except SQLAlchemyError as e:
            print(f"An SQLAlchemy error occurred during setup: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during setup: {e}")
        finally:
            if engine:
                engine.dispose()
    
    def test_db_connection_sqlalchemy(connection_name: str,
                                         database: str,
                                         table_name: str,
                                         user: str,
                                         password: str,
                                         **connect_kwargs):
        """
        Tests the CloudSQL MySQL connection and verifies table existence.
    
        Args:
            connection_name: CloudSQL MySQL instance connection name.
            database: The name of the database.
            table_name: The name of the table to check for.
            user: The database user.
            password: The database password.
            connect_kwargs: Additional keyword arguments for the connector.
        """
        engine = None
        try:
            engine = get_db_engine(connection_name, user, password, database, **connect_kwargs)
    
            with engine.connect() as connection:
                print("Testing MySQL connection...")
                connection.execute(text("SELECT 1"))
                print("✓ Connection successful")
    
                # Check if table exists using information_schema.
                # In MySQL, schema is the database, which can be found with DATABASE().
                table_exists_query = text("""
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = DATABASE() AND table_name = :tname
                    );
                """)
                table_exists = connection.execute(table_exists_query, {"tname": table_name}).scalar()
    
                if table_exists:
                    print(f"✓ Table `{table_name}` exists in database `{database}`.")
                else:
                    print(f"✗ Table `{table_name}` does NOT exist in database `{database}`.")
    
        except SQLAlchemyError as e:
            print(f"Connection test failed (SQLAlchemy error): {e}")
        except Exception as e:
            print(f"Connection test failed (Unexpected error): {e}")
        finally:
            if engine:
                engine.dispose()
    
    def verify_embeddings_sqlalchemy(connection_name: str,
                                     database: str,
                                     table_name: str,
                                     user: str,
                                     password: str,
                                     embedding_column: str = "embedding",
                                     **connect_kwargs):
        """
        Connects to a CloudSQL MySQL table and prints all of its rows.
    
        Args:
            connection_name: CloudSQL MySQL instance connection name.
            database: The name of the database.
            table_name: The name of the table to query.
            user: The database user.
            password: The database password.
            connect_kwargs: Additional keyword arguments for the connector.
        """
        engine = None
        try:
            engine = get_db_engine(connection_name, user, password, database, **connect_kwargs)
    
            with engine.connect() as connection:
                # Use backticks for the table name for MySQL best practice
                column_query = text(f"""
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE table_schema = :db_name
                      AND table_name = :t_name
                      AND COLUMN_NAME != '{embedding_column}'
                """)
    
                column_result = connection.execute(
                    column_query,
                    {"db_name": database, "t_name": table_name}
                )
    
                columns_to_select = [row[0] for row in column_result]
    
                if not columns_to_select:
                    print(f"No columns to display in `{table_name}` (after excluding '{embedding_column}').")
                    return
    
                # Construct the SELECT statement with the filtered columns, quoting them for safety
                select_columns_str = ", ".join([f"`{col}`" for col in columns_to_select])
                select_query = text(f"SELECT {select_columns_str}, vector_to_string({embedding_column}) as {embedding_column} FROM `{table_name}`;")
    
                # Execute the query to get the data
                result = connection.execute(select_query)
                rows = result.mappings().all()
    
                print(f"\nFound {len(rows)} rows in `{table_name}` (excluding '{embedding_column}' column):")
                print("-" * 80)
    
                if not rows:
                    print("Table is empty.")
                else:
                    # result.keys() will have the correct column names from the executed query
                    columns = result.keys()
                    for row in rows:
                        for col in columns:
                            print(f"{col}: {row[col]}")
                        print("-" * 80)
        except SQLAlchemyError as e:
            # Check specifically for ProgrammingError if the table might not exist
            if isinstance(e, sqlalchemy.exc.ProgrammingError):
                print(f"Failed to query table `{table_name}`. Does it exist? Error: {e}")
            else:
                print(f"Failed to verify data (SQLAlchemy error): {e}")
        except Exception as e:
            print(f"Failed to verify data (Unexpected error): {e}")
        finally:
            if engine:
                engine.dispose()
    

## Create Sample Product Catalog Data

We'll create a typical e-commerce catalog where you might want to:

  * Generate embeddings for product text
  * Store vectors alongside product data
  * Enable vector similarity features



Example product:
    
    
    {
        "id": "desk-001",
        "name": "Modern Minimalist Desk",
        "description": "Sleek minimalist desk with clean lines and a spacious work surface. "
                      "Features cable management system and sturdy steel frame. "
                      "Perfect for contemporary home offices and workspaces.",
        "category": "Desks",
        "price": 399.99,
        "material": "Engineered Wood, Steel",
        "dimensions": "60W x 30D x 29H inches"
    }
    

### Create sample data

Toggle code
    
    
    PRODUCTS_DATA = [
        {
            "id": "desk-001",
            "name": "Modern Minimalist Desk",
            "description": "Sleek minimalist desk with clean lines and a spacious work surface. "
                          "Features cable management system and sturdy steel frame. "
                          "Perfect for contemporary home offices and workspaces.",
            "category": "Desks",
            "price": 399.99,
            "material": "Engineered Wood, Steel",
            "dimensions": "60W x 30D x 29H inches"
        },
        {
            "id": "chair-001",
            "name": "Ergonomic Mesh Office Chair",
            "description": "Premium ergonomic office chair with breathable mesh back, "
                          "adjustable lumbar support, and 4D armrests. Features synchronized "
                          "tilt mechanism and memory foam seat cushion. Ideal for long work hours.",
            "category": "Office Chairs",
            "price": 299.99,
            "material": "Mesh, Metal, Premium Foam",
            "dimensions": "26W x 26D x 48H inches"
        },
        {
            "id": "sofa-001",
            "name": "Contemporary Sectional Sofa",
            "description": "Modern L-shaped sectional with chaise lounge. Upholstered in premium "
                          "performance fabric. Features deep seats, plush cushions, and solid "
                          "wood legs. Perfect for modern living rooms.",
            "category": "Sofas",
            "price": 1299.99,
            "material": "Performance Fabric, Solid Wood",
            "dimensions": "112W x 65D x 34H inches"
        },
        {
            "id": "table-001",
            "name": "Rustic Dining Table",
            "description": "Farmhouse-style dining table with solid wood construction. "
                          "Features distressed finish and trestle base. Seats 6-8 people "
                          "comfortably. Perfect for family gatherings.",
            "category": "Dining Tables",
            "price": 899.99,
            "material": "Solid Pine Wood",
            "dimensions": "72W x 42D x 30H inches"
        },
        {
            "id": "bed-001",
            "name": "Platform Storage Bed",
            "description": "Modern queen platform bed with integrated storage drawers. "
                          "Features upholstered headboard and durable wood slat support. "
                          "No box spring needed. Perfect for maximizing bedroom space.",
            "category": "Beds",
            "price": 799.99,
            "material": "Engineered Wood, Linen Fabric",
            "dimensions": "65W x 86D x 48H inches"
        }
    ]
    print(f"""✓ Created PRODUCTS_DATA with {len(PRODUCTS_DATA)} records""")
    

## Importing Pipeline Components

We import the following for configuring our embedding ingestion pipeline:

  * `apache_beam.ml.rag.types.Chunk`, the structured input for generating and ingesting embeddings
  * `apache_beam.ml.rag.ingestion.cloudsql.CloudSQLMySQLVectorWriterConfig` for configuring write behavior like schema mapping and conflict resolution
  * `apache_beam.ml.rag.ingestion.cloudsql.LanguageConnectorConfig` to connect using the [CloudSQL MySQL language connector](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc.md)
  * `apache_beam.ml.rag.ingestion.base import VectorDatabaseWriteTransform` to perform the write step using CloudSQL MySQL configs


    
    
    # CloudSQL imports
    from apache_beam.ml.rag.ingestion.cloudsql import CloudSQLMySQLVectorWriterConfig
    from apache_beam.ml.rag.ingestion.cloudsql import LanguageConnectorConfig
    
    
    from apache_beam.ml.rag.ingestion.base import VectorDatabaseWriteTransform
    from apache_beam.ml.rag.types import Chunk, Content
    from apache_beam.ml.rag.embeddings.huggingface import HuggingfaceTextEmbeddings
    
    # Apache Beam core
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    from apache_beam.ml.transforms.base import MLTransform
    
    # JDBC and MySQL utilities
    from apache_beam.ml.rag.ingestion.jdbc_common import WriteConfig
    from apache_beam.ml.rag.ingestion.mysql_common import ColumnSpecsBuilder, ConflictResolution
    

# What's next?

This colab covers several use cases that you can explore based on your needs after completing the Setup and Prerequisites:

🔰 **New to vector embeddings?**

  * Start with Quick Start
  * Uses simple out-of-box schema
  * Perfect for initial testing



🚀 **Need to scale to large datasets?**

  * Go to Run on Dataflow
  * Learn how to execute the same pipeline at scale
  * Fully managed
  * Process large datasets efficiently



🎯 **Have a specific schema?**

  * Go to Custom Schema
  * Learn to use different column names
  * Map metadata to individual columns



🔄 **Need to update embeddings?**

  * Check out Updating Embeddings
  * Handle conflicts
  * Selective field updates



🔗 **Need to generate and Store Embeddings for Existing CloudSQL MySQL Data??**

  * See Database Integration
  * Read data from your CloudSQL MySQL table.
  * Generate embeddings for the relevant fields.
  * Update your table (or a related table) with the generated embeddings.



🤖 **Want to use Google's AI models?**

  * Try Vertex AI Embeddings
  * Use Google's powerful embedding models
  * Seamlessly integrate with other Google Cloud services



🔄 Need real-time embedding updates?

  * Try Streaming Embeddings from PubSub
  * Process continuous data streams
  * Update embeddings in real-time as information changes



# Quick Start: Basic Vector Ingestion

This section shows the simplest way to generate embeddings and store them in CloudSQL MySQL.

## Create table with default schema

Before running the pipeline, we need a table to store our embeddings:
    
    
    table_name = "default_product_embeddings"
    table_schema = f"""
      id VARCHAR(255) PRIMARY KEY,
      embedding VECTOR(384) USING VARBINARY,
      content text,
      metadata JSON
    """
    setup_db_table_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name,table_schema, DB_USER, DB_PASSWORD)
    test_db_connection_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name, DB_USER, DB_PASSWORD)
    

## Configure Pipeline Components

Now define the components that control the pipeline behavior:

### Convert ingested product data to embeddable Chunks

  * Our data is ingested as product dictionaries
  * Embedding generation and ingestion processes `Chunks`
  * We convert each product dictionary to a `Chunk` to configure what text to embed and what to treat as metadata


    
    
    from typing import Dict, Any
    
    # The create_chunk function converts our product dictionaries to Chunks.
    # This doesn't split the text - it simply structures it in the format
    # expected by the embedding pipeline components.
    def create_chunk(product: Dict[str, Any]) -> Chunk:
        """Convert a product dictionary into a Chunk object.
    
           The pipeline components (MLTransform, VectorDatabaseWriteTransform)
           work with Chunk objects. This function:
           1. Extracts text we want to embed
           2. Preserves product data as metadata
           3. Creates a Chunk in the expected format
    
        Args:
            product: Dictionary containing product information
    
        Returns:
            Chunk: A Chunk object ready for embedding
        """
        return Chunk(
            content=Content(
                text=f"{product['name']}: {product['description']}"
            ), # The text that will be embedded
            id=product['id'],  # Use product ID as chunk ID
            metadata=product,  # Store all product info in metadata
        )
    

### Generate embeddings with HuggingFace

We use a local pre-trained Hugging Face model to create vector embeddings from the product descriptions.
    
    
    huggingface_embedder = HuggingfaceTextEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    

### Write to CloudSQL MySQL

The default CloudSQLMySQLVectorWriterConfig maps Chunk fields to database columns as:

Database Column | Chunk Field | Description  
---|---|---  
id | chunk.id | Unique identifier  
embedding | chunk.embedding.dense_embedding | Vector representation  
content | chunk.content.text | Text that was embedded  
metadata | chunk.metadata | Additional data as JSONB  
      
    
    # Configure the language connector so we can connect securely
    connector_config = LanguageConnectorConfig(
        username=DB_USER,
        password=DB_PASSWORD,
        database_name=DB_NAME,
        instance_name=CONNECTION_NAME
    )
    cloudsql_writer_config = CloudSQLMySQLVectorWriterConfig(
        connection_config=connector_config,
        table_name=table_name
    )
    

## Assemble and Run Pipeline

Now we can create our pipeline that:

  1. Takes our product data
  2. Converts each product to a Chunk
  3. Generates embeddings for each Chunk
  4. Stores everything in CloudSQL MySQL


    
    
    import tempfile
    
    # Executing on DirectRunner (local execution)
    with beam.Pipeline() as p:
        _ = (
                p
                | 'Create Products' >> beam.Create(PRODUCTS_DATA)
                | 'Convert to Chunks' >> beam.Map(create_chunk)
                | 'Generate Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
                  .with_transform(huggingface_embedder)
                | 'Write to CloudSQL' >> VectorDatabaseWriteTransform(
                    cloudsql_writer_config
                )
            )
    

## Verify Embeddings

Let's check what was written to our CloudSQL MySQL table:
    
    
    verify_embeddings_sqlalchemy(connection_name=CONNECTION_NAME, database=DB_NAME, table_name=table_name, user=DB_USER, password=DB_PASSWORD)
    

## Quick Start Summary

In this section, you learned how to:

  * Convert product data to the Chunk format expected by embedding pipelines
  * Generate embeddings using a HuggingFace model
  * Configure and run a basic embedding ingestion pipeline
  * Store embeddings and metadata in CloudSQL MySQL



This basic pattern forms the foundation for all the advanced use cases covered in the following sections.

# Quick Start: Run on Dataflow

This section demonstrates how to launch the Quick Start embedding pipeline on Google Cloud Dataflow from the colab. While previous examples used DirectRunner for local execution, Dataflow provides a fully managed, distributed execution environment that is:

  * Scalable: Automatically scales to handle large datasets
  * Fault-tolerant: Handles worker failures and ensures exactly-once processing
  * Fully managed: No need to provision or manage infrastructure



For more in-depth documentation to package your pipeline into a python file and launch a DataFlow job from the command line see [Create Dataflow pipeline using Python](https://cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python).

## Create the CloudSQL MySQL table with default schema

Before running the pipeline, we need a table to store our embeddings:
    
    
    table_name = "default_dataflow_product_embeddings"
    table_schema = f"""
      id VARCHAR(255) PRIMARY KEY,
      embedding VECTOR(384) USING VARBINARY,
      content text,
      metadata JSON
    """
    setup_db_table_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name,table_schema, DB_USER, DB_PASSWORD)
    test_db_connection_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name, DB_USER, DB_PASSWORD)
    

## Save our Pipeline to a python file

To launch our pipeline job on DataFlow, we

  1. Add command line arguments for passing pipeline options like CloudSQL MySQL credentioals
  2. Save our pipeline code to a local file `basic_ingestion_pipeline.py`


    
    
    file_content = """
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    import argparse
    import tempfile
    
    from apache_beam.ml.transforms.base import MLTransform
    from apache_beam.ml.rag.types import Chunk, Content
    from apache_beam.ml.rag.ingestion.base import VectorDatabaseWriteTransform
    from apache_beam.ml.rag.ingestion.cloudsql import CloudSQLMySQLVectorWriterConfig, LanguageConnectorConfig
    from apache_beam.ml.rag.embeddings.huggingface import HuggingfaceTextEmbeddings
    from apache_beam.options.pipeline_options import SetupOptions
    
    PRODUCTS_DATA = [
        {
            "id": "desk-001",
            "name": "Modern Minimalist Desk",
            "description": "Sleek minimalist desk with clean lines and a spacious work surface. "
                          "Features cable management system and sturdy steel frame. "
                          "Perfect for contemporary home offices and workspaces.",
            "category": "Desks",
            "price": 399.99,
            "material": "Engineered Wood, Steel",
            "dimensions": "60W x 30D x 29H inches"
        },
        {
            "id": "chair-001",
            "name": "Ergonomic Mesh Office Chair",
            "description": "Premium ergonomic office chair with breathable mesh back, "
                          "adjustable lumbar support, and 4D armrests. Features synchronized "
                          "tilt mechanism and memory foam seat cushion. Ideal for long work hours.",
            "category": "Office Chairs",
            "price": 299.99,
            "material": "Mesh, Metal, Premium Foam",
            "dimensions": "26W x 26D x 48H inches"
        }
    ]
    
    def run(argv=None):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--connection_name',
            required=True,
            help='CloudSQL MySQL instance uri'
        )
        parser.add_argument(
            '--cloudsql_database',
            default='mysql',
            help='CloudSQL MySQL database name'
        )
        parser.add_argument(
            '--cloudsql_table',
            required=True,
            help='CloudSQL MySQL table name'
        )
        parser.add_argument(
            '--cloudsql_username',
            required=True,
            help='CloudSQL MySQL user name'
        )
        parser.add_argument(
            '--cloudsql_password',
            required=True,
            help='CloudSQL MySQL password'
        )
        known_args, pipeline_args = parser.parse_known_args(argv)
    
        pipeline_options = PipelineOptions(pipeline_args)
        pipeline_options.view_as(SetupOptions).save_main_session = True
    
        with beam.Pipeline(options=pipeline_options) as p:
            _ = (
                  p
                  | 'Create Products' >> beam.Create(PRODUCTS_DATA)
                  | 'Convert to Chunks' >> beam.Map(lambda product: Chunk(
                        content=Content(
                            text=f"{product['name']}: {product['description']}"
                        ), # The text that will be embedded
                        id=product['id'],  # Use product ID as chunk ID
                        metadata=product,  # Store all product info in metadata
                    )
                  )
                  | 'Generate Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
                    .with_transform(
                        HuggingfaceTextEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                    )
                  | 'Write to CloudSQL MySQL' >> VectorDatabaseWriteTransform(
                      CloudSQLMySQLVectorWriterConfig(
                          connection_config=LanguageConnectorConfig(
                            username=known_args.cloudsql_username,
                            password=known_args.cloudsql_password,
                            database_name=known_args.cloudsql_database,
                            instance_name=known_args.connection_name
                          ),
                          table_name=known_args.cloudsql_table
                      )
                  )
              )
    
    if __name__ == '__main__':
        run()
    """
    
    with open("basic_ingestion_pipeline.py", "w") as f:
        f.write(file_content)
    

## Authenticate with Google Cloud

To launch a pipeline on Google Cloud, authenticate this notebook. Replace `<PROJECT_ID>` with your Google Cloud project ID
    
    
    PROJECT_ID = "<project_id_>" # @param {type:'string'}
    import os
    os.environ['PROJECT_ID'] = PROJECT_ID
    
    
    
    import sys
    if 'google.colab' in sys.modules:
      from google.colab import auth
      auth.authenticate_user(project_id=PROJECT_ID)
    

## Configure the Pipeline options

To run the pipeline on DataFlow we need

  * A gcs bucket for staging DataFlow files. Replace `<BUCKET_NAME>`: the name of a valid Google Cloud Storage bucket.
  * Optionally set the Google Cloud region that you want to run Dataflow in. Replace `<REGION>` with the desired location.
  * Optionally provide `NETWORK` and `SUBNETWORK` for dataflow workers to run on.


    
    
    import os
    BUCKET_NAME = '' # @param {type:'string'}
    REGION = 'us-central1' # @param {type:'string'}
    
    NETWORK = '' # @param {type:'string'}
    SUBNETWORK = '' # @param {type:'string'}
    

## Provide additional Python dependencies to be installed on Worker VM's

We are making use of the HuggingFace `sentence-transformers` package to generate embeddings. Since this package is not installed on Worker VM's by default, we create a requirements.txt file with the additional dependencies to be installed on worker VM's.

See [Managing Python Pipeline Dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/) for more details.
    
    
    echo "sentence-transformers" > ./requirements.txt
    cat ./requirements.txt

## Run Pipeline on Dataflow

We launch the pipeline via the command line, passing

  * CloudSQL MySQL pipeline arguments defined in `basic_ingestion_pipeline.py`
  * GCP Project ID
  * Job Region
  * The runner (DataflowRunner)
  * Temp and Staging GCS locations for Pipeline artifacts
  * Requirement file location for additional dependencies
  * (Optional) The VPC network and Subnetwork that has access to the CloudSQL MySQL instance



Once the job is launched, you can monitor its progress in the Google Cloud Console:

  1. Go to <https://console.cloud.google.com/dataflow/jobs>
  2. Select your project
  3. Click on the job named "cloudsql-dataflow-basic-embedding-ingest"
  4. View detailed execution graphs, logs, and metrics


    
    
    command_parts = [
        "python ./basic_ingestion_pipeline.py",
        f"--project={PROJECT_ID}",
        f"--cloudsql_username={DB_USER}",
        f"--connection_name={CONNECTION_NAME}",
        f"--cloudsql_password={DB_PASSWORD}",
        f"--cloudsql_table=default_dataflow_product_embeddings",
        f"--cloudsql_database={DB_NAME}",
        f"--job_name=cloudsql-dataflow-basic-embedding-ingest",
        f"--region={REGION}",
        "--runner=DataflowRunner",
        f"--temp_location=gs://{BUCKET_NAME}/temp",
        f"--staging_location=gs://{BUCKET_NAME}/staging",
        "--requirements_file=requirements.txt",
    ]
    
    if NETWORK:
        command_parts.append(f"--network={NETWORK}")
    
    if SUBNETWORK:
        command_parts.append(f"--subnetwork=regions/{REGION}/subnetworks/{SUBNETWORK}")
    
    final_command = " ".join(command_parts)
    
    print("Generated command:\n", final_command)
    !{final_command}
    

## Verify the Written Embeddings

Let's check what was written to our CloudSQL MySQL table:
    
    
    verify_embeddings_sqlalchemy(connection_name=CONNECTION_NAME, database=DB_NAME, table_name='default_dataflow_product_embeddings', user=DB_USER, password=DB_PASSWORD)
    

# Advanced Use Cases

This section demonstrates more complex scenarios for using CloudSQL MySQL with Apache Beam for vector embeddings.

🎯 **Have a specific schema?**

  * Go to Custom Schema
  * Learn to use different column names and transform values
  * Map metadata to individual columns



🔄 **Need to update embeddings?**

  * Check out Updating Embeddings
  * Handle conflicts
  * Selective field updates



🔗 **Need to generate and Store Embeddings for Existing CloudSQL MySQL Data??**

  * See Database Integration
  * Read data from your CloudSQL MySQL table.
  * Generate embeddings for the relevant fields.
  * Update your table (or a related table) with the generated embeddings.



🤖 **Want to use Google's AI models?**

  * Try Vertex AI Embeddings
  * Use Google's powerful embedding models
  * Seamlessly integrate with other Google Cloud services



🔄 Need real-time embedding updates?

  * Try Streaming Embeddings from PubSub
  * Process continuous data streams
  * Update embeddings in real-time as information changes



## Custom Schema with Column Mapping 

In this example, we'll create a custom schema that:

  * Uses different column names
  * Maps metadata to individual columns
  * Uses functions to transform values



### ColumnSpec and ColumnSpecsBuilder

ColumnSpec specifies how to map data to a database column. For example:
    
    
    from apache_beam.ml.rag.ingestion.mysql_common import ColumnSpecsBuilder
    
    ColumnSpec(
        column_name="price",          # Database column
        python_type=float,            # Python Type for the value
        value_fn=lambda c: c.metadata['price'],  # Extract price from Chunk metadata to get actual value
        placeholder="ROUND(?, 2)"      # Optional SQL cast or function
    )
    

creates an INSERT statement like:
    
    
    INSERT INTO table (price) VALUES (?::decimal)
    

where the `?` placeholder is poulated with the value from our ingested data.

`ColumnSpecsBuilder` provides a builder and convenience methods to create these `ColumnSpecs`:

  1. Core Field Mapping

     * `with_id_spec()` => Insert chunk.id as text in "id" column
     * `with_embedding_spec()` => Insert chunk.embedding casted to `VECTOR` via `string_to_vector(?)` in "embedding" column
     * `with_content_spec()` => Insert `chunk.content`.text as text in "content" column
**Note:** All `with_id_spec`, `with_embedding_spec`, etc. methods allow overriding `column_name`, `python_type`, and `value_fn`.
  2. Metadata Extraction

     * `add_metadata_field`: Creates a column from a `chunk.metadata` field
     * Handles type conversion based on specified SQL type
  3. Custom Fields

     * `add_custom_column_spec`: Grants complete control over mapping `Chunk` data to database rows using `ColumnSpec`



Now, lets the table to store our embeddings:

### Create Custom Schema Table
    
    
    table_name = "custom_product_embeddings"
    table_schema = """
        product_id VARCHAR(255) PRIMARY KEY,
        vector_embedding VECTOR(384) USING VARBINARY,
        product_name VARCHAR(255),
        description TEXT,
        price DECIMAL,
        category VARCHAR(255),
        display_text VARCHAR(255),
        model_name VARCHAR(255),
        created_at TIMESTAMP
    """
    setup_db_table_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name,table_schema, DB_USER, DB_PASSWORD)
    test_db_connection_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name, DB_USER, DB_PASSWORD)
    

### Configure Pipeline Components

#### Write to custom schema using ColumnSpecsBuilder

We configure ConlumnSpecsBuilder to map data as:

Database Column | Chunk Field  
---|---  
`product_id` | `chunk.id`  
`vector_embedding` | `chunk.embedding.dense_embedding`  
`description` | `chunk.content.text`  
`product_name` | `chunk.metadata['name']`  
`price` | `chunk.metadata['price']`  
`category` | `chunk.metadata['category']`  
`display_text` | _Function that combines product name and price_  
`model_name` | _Function that returns the model name: "all-MiniLM-L6-v2"_  
`created_at` | _Function that returns the current timestamp cast to a SQL timestamp_  
      
    
    from apache_beam.ml.rag.ingestion.mysql_common import ColumnSpecsBuilder
    from apache_beam.ml.rag.ingestion.mysql_common import ColumnSpec
    from datetime import datetime
    
    column_specs = (
        ColumnSpecsBuilder()
        # Write chunk.id to a column named "product_id"
        .with_id_spec(column_name='product_id')
        # Write chunk.embedding.dense_embedding to a column named "vector_embedding"
        .with_embedding_spec(column_name='vector_embedding')
        # Write chunk.content.text to a column named "description"
        .with_content_spec(column_name='description')
        # Write chunk.metadata.['product_name'] to a column named "product_name"
        .add_metadata_field(
            field='name',
            column_name='product_name',
            python_type=str
        )
        # Write chunk.metadata.['price'] to a column named "price"
        .add_metadata_field(
            field='price',
            column_name='price',
            python_type=float
        )
        # Write chunk.metadata.['category'] to a column named "category"
        .add_metadata_field(
            field='category',
            column_name='category',
            python_type=str
        )
        # Write custom field using value_fn to column named "display_text" using
        # ColumnSpec.text convenience method
        .add_custom_column_spec(
            ColumnSpec.text(
              column_name='display_text',
            value_fn=lambda chunk: \
              f"{chunk.metadata['name']} - ${chunk.metadata['price']:.2f}"
            )
        )
        # Store model used to generate embedding using ColumnSpec constructor
        .add_custom_column_spec(
            ColumnSpec(
              column_name='model_name',
              python_type=str,
              value_fn=lambda _: "all-MiniLM-L6-v2"
            )
        )
        .add_custom_column_spec(
            ColumnSpec(
              column_name='created_at',
              python_type=str,
              value_fn=lambda _: datetime.now().isoformat()
            )
        )
        .build()
    )
    

### Assemble and Run Pipeline

Now we can create our pipeline that will:

  1. Take our product data
  2. Convert each product to a Chunk
  3. Generate embeddings for each Chunk
  4. Store everything in CloudSQL MySQL with our custom schema configuration


    
    
    import tempfile # For storing MLTransform artifacts
    
    # Executing on DirectRunner (local execution)
    with beam.Pipeline() as p:
        _ = (
                p
                | 'Create Products' >> beam.Create(PRODUCTS_DATA)
                | 'Convert to Chunks' >> beam.Map(lambda product: Chunk(
                        content=Content(
                            text=f"{product['name']}: {product['description']}"
                        ), # The text that will be embedded
                        id=product['id'],  # Use product ID as chunk ID
                        metadata=product,  # Store all product info in metadata
                    )
                  )
                | 'Generate Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
                  .with_transform(HuggingfaceTextEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
                | 'Write to CloudSQL MySQL' >> VectorDatabaseWriteTransform(
                    CloudSQLMySQLVectorWriterConfig(
                        connection_config=LanguageConnectorConfig(
                            username=DB_USER,
                            password=DB_PASSWORD,
                            database_name=DB_NAME,
                            instance_name=CONNECTION_NAME
                        ),
                        table_name=table_name,
                        column_specs=column_specs
                    )
                )
            )
    

### Verify the Written Embeddings

Let's check what was written to our CloudSQL MySQL table:
    
    
    verify_embeddings_sqlalchemy(connection_name=CONNECTION_NAME, database=DB_NAME, table_name=table_name, user=DB_USER, password=DB_PASSWORD, embedding_column="vector_embedding")
    

## Update Embeddings and Metadata with Conflict Resolution 

This section demonstrates how to handle periodic updates to product descriptions and their embeddings using the default schema. We'll show how embeddings and metadata get updated when product descriptions change.

### Create table with desired schema

Let's use the same default schema as in Quick Start:
    
    
    table_name = "mutable_product_embeddings"
    table_schema = f"""
      id VARCHAR(255) PRIMARY KEY,
      embedding VECTOR(384) USING VARBINARY,
      content text,
      metadata JSON,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    """
    setup_db_table_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name,table_schema, DB_USER, DB_PASSWORD)
    test_db_connection_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name, DB_USER, DB_PASSWORD)
    

### Sample Data: Day 1 vs Day 2
    
    
    PRODUCTS_DATA_DAY1 = [
        {
            "id": "desk-001",
            "name": "Modern Minimalist Desk",
            "description": "Sleek minimalist desk with clean lines and a spacious work surface. "
                          "Features cable management system and sturdy steel frame.",
            "category": "Desks",
            "price": 399.99,
            "update_timestamp": "2024-02-18"
        }
    ]
    
    PRODUCTS_DATA_DAY2 = [
        {
            "id": "desk-001",  # Same ID as Day 1
            "name": "Modern Minimalist Desk",
            "description": "Updated: Sleek minimalist desk with built-in wireless charging. "
                          "Features cable management system, sturdy steel frame, and Qi charging pad. "
                          "Perfect for modern tech-enabled workspaces.",
            "category": "Smart Desks",  # Category changed
            "price": 449.99,  # Price increased
            "update_timestamp": "2024-02-19"
        }
    ]
    

### Configure Pipeline Components

#### Writer with Conflict Resolution
    
    
    from apache_beam.ml.rag.ingestion.cloudsql import (
        CloudSQLMySQLVectorWriterConfig,
        LanguageConnectorConfig,
    )
    from apache_beam.ml.rag.ingestion.mysql_common import ConflictResolution
    
    # Define how to handle conflicts - update all fields when ID matches
    conflict_resolution = ConflictResolution(
        action="UPDATE",         # Update existing records
        update_fields=["embedding", "content", "metadata"]
    )
    
    # Create writer config with conflict resolution
    cloudsql_writer_config = CloudSQLMySQLVectorWriterConfig(
        connection_config=LanguageConnectorConfig(
            username=DB_USER,
            password=DB_PASSWORD,
            database_name=DB_NAME,
            instance_name=CONNECTION_NAME
        ),
        table_name=table_name,
        conflict_resolution=conflict_resolution,
    )
    
    
    
    huggingface_embedder = HuggingfaceTextEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    

### Run Day 1 Pipeline

First, let's ingest our initial product data:
    
    
    # Executing on DirectRunner (local execution)
    with beam.Pipeline() as p:
        _ = (
            p
            | 'Create Day 1 Products' >> beam.Create(PRODUCTS_DATA_DAY1)
            | 'Convert Day 1 to Chunks' >> beam.Map(lambda product: Chunk(
                    content=Content(
                        text=f"{product['name']}: {product['description']}"
                    ), # The text that will be embedded
                    id=product['id'],  # Use product ID as chunk ID
                    metadata=product,  # Store all product info in metadata
                )
              )
            | 'Generate Day1 Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
              .with_transform(HuggingfaceTextEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
            | 'Write Day 1 to CloudSQL MySQL' >> VectorDatabaseWriteTransform(
                cloudsql_writer_config
            )
        )
    

#### Verify Initial Data
    
    
    print("\nAfter Day 1 ingestion:")
    verify_embeddings_sqlalchemy(connection_name=CONNECTION_NAME, database=DB_NAME, table_name=table_name, user=DB_USER, password=DB_PASSWORD)
    

### Run Day 2 Pipeline

Now let's process our updated product data:
    
    
    # Executing on DirectRunner (local execution)
    with beam.Pipeline() as p:
        _ = (
            p
            | 'Create Day 2 Products' >> beam.Create(PRODUCTS_DATA_DAY2)
            | 'Convert Day 2 to Chunks' >> beam.Map(lambda product: Chunk(
                        content=Content(
                            text=f"{product['name']}: {product['description']}"
                        ), # The text that will be embedded
                        id=product['id'],  # Use product ID as chunk ID
                        metadata=product,  # Store all product info in metadata
                    )
                  )
            | 'Generate Day 2 Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
              .with_transform(HuggingfaceTextEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
            | 'Write Day 2 to CloudSQL MySQL' >> VectorDatabaseWriteTransform(
                cloudsql_writer_config
            )
        )
    

#### Verify Updated Data
    
    
    print("\nAfter Day 2 ingestion:")
    verify_embeddings_sqlalchemy(connection_name=CONNECTION_NAME, database=DB_NAME, table_name=table_name, user=DB_USER, password=DB_PASSWORD)
    

### What Changed?

Key points to notice:

  1. The embedding vector changed because the product description was updated
  2. The metadata JSON field contains the updated category, price, and timestamp
  3. The content field reflects the new description
  4. The original ID remained the same



This pattern allows you to:

  * Update embeddings when source text changes
  * Maintain referential integrity with consistent IDs
  * Track changes through the metadata field
  * Handle conflicts gracefully using CloudSQL MySQL's conflict resolution



## Adding Embeddings to Existing Database Records 

This section demonstrates how to:

  1. Read existing product data from a database
  2. Generate embeddings for that data
  3. Write the embeddings back to the database


    
    
    table_name = "existing_products"
    table_schema = """
        id VARCHAR(255) PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        price DECIMAL,
        embedding VECTOR(384) USING VARBINARY
    """
    

### MySQL helper for inserting initial records

Toggle code
    
    
    import sqlalchemy
    from sqlalchemy import text
    from sqlalchemy.exc import SQLAlchemyError
    # The google.cloud.sql.connector and a driver like PyMySQL (`pip install pymysql`)
    # are required for this to connect to Cloud SQL.
    from google.cloud.sql.connector import Connector
    
    # Assume get_db_engine is defined elsewhere to connect using a MySQL dialect,
    # e.g., 'mysql+pymysql'
    # from your_utils import get_db_engine
    
    def setup_initial_data_sqlalchemy(connection_name: str,
                                      database: str,
                                      table_name: str,
                                      table_schema: str,
                                      user: str,
                                      password: str,
                                      **connect_kwargs):
        """Sets up a table and inserts sample data into a MySQL database using SQLAlchemy.
    
        This function will drop the specified table if it exists, recreate it based on the
        provided schema, and insert a predefined set of sample products.
    
        Args:
            connection_name: Cloud SQL MySQL instance connection name string.
            database: Name of the database.
            table_name: Name of the table to create and populate.
            table_schema: A string containing MySQL-compatible column definitions
                          (e.g., "id VARCHAR(255) PRIMARY KEY, title VARCHAR(255)").
            user: Database username.
            password: Database password.
            connect_kwargs: Additional keyword arguments for the Cloud SQL connector.
        """
        engine = None
        try:
            # Assumes get_db_engine returns a SQLAlchemy engine configured for MySQL
            engine = get_db_engine(connection_name, user, password, database, **connect_kwargs)
    
            with engine.connect() as connection:
                print("✅ Connected to Cloud SQL MySQL successfully via SQLAlchemy!")
    
                # DDL operations (DROP/CREATE) in MySQL cause an implicit commit,
                # so they are run outside an explicit transaction block.
                print(f"Dropping table `{table_name}` if it exists...")
                connection.execute(text(f"DROP TABLE IF EXISTS `{table_name}`;"))
    
                print(f"Creating table `{table_name}`...")
                # Note: Ensure the table_schema and sample data columns match.
                create_sql = f"CREATE TABLE `{table_name}` ({table_schema});"
                connection.execute(text(create_sql))
                print(f"Table `{table_name}` created.")
    
                # Define the sample data to be inserted.
                sample_products_dicts = [
                     {
                        "id": "lamp-001", "title": "Artisan Table Lamp",
                        "description": "Hand-crafted ceramic...", "price": 129.99
                     },
                     {
                        "id": "mirror-001", "title": "Floating Wall Mirror",
                        "description": "Modern circular mirror...", "price": 199.99
                     },
                     {
                         "id": "vase-001", "title": "Contemporary Ceramic Vase",
                         "description": "Minimalist vase...", "price": 79.99
                     }
                ]
    
                # The INSERT statement uses named placeholders matching the dictionary keys.
                insert_sql = text(f"""
                    INSERT INTO `{table_name}` (id, title, description, price)
                    VALUES (:id, :title, :description, :price)
                """)
    
                print(f"Inserting sample data into `{table_name}`...")
                # SQLAlchemy executes the insert for each dictionary in the list.
                # This runs within a new transaction block started by the `connect()` context.
                connection.execute(insert_sql, sample_products_dicts)
    
                # Explicitly commit the transaction that contains the INSERT statements.
                connection.commit()
                print("✓ Sample products inserted successfully.")
    
        except SQLAlchemyError as e:
            print(f"❌ An SQLAlchemy error occurred during setup: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred during setup: {e}")
        finally:
            if engine:
                # Dispose of the engine to close all connections in the pool.
                engine.dispose()
                print("Database engine pool disposed.")
    
    
    
    setup_initial_data_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name, table_schema, DB_USER, DB_PASSWORD)
    

### Read from Database and Generate Embeddings

Now let's create a pipeline to read the existing data, generate embeddings, and write back:
    
    
    from apache_beam.io.jdbc import ReadFromJdbc
    from apache_beam.io.jdbc import WriteToJdbc
    from apache_beam.ml.rag.ingestion.mysql_common import ColumnSpecsBuilder
    
    # Configure database writer
    cloudsql_writer_config = CloudSQLMySQLVectorWriterConfig(
        connection_config=LanguageConnectorConfig(
            username=DB_USER,
            password=DB_PASSWORD,
            database_name=DB_NAME,
            instance_name=CONNECTION_NAME
        ),
        table_name=table_name,
        column_specs=(
            ColumnSpecsBuilder()
              .with_id_spec()
              .with_embedding_spec()
              # Add a placeholder value for the title column, because it has a
              # NOT NULL constraint. Insert with Conflict resolution statements in
              # MySQL requires all NOT NULL fields to have a value, even if the
              # value will not be updated (the original title is preserved).
              .add_custom_column_spec(
                ColumnSpec.text("title", value_fn=lambda x: "")
               )
              .build()
        ),
        conflict_resolution=ConflictResolution(
            action="UPDATE",
            update_fields=["embedding"]  # Update the embedding field
        )
    )
    
    # Create and run pipeline  on DirectRunner (local execution)
    with beam.Pipeline() as p:
        # Read existing products
        rows = (
            p
            | "Read Products" >> ReadFromJdbc(
                table_name=table_name,
                driver_class_name="com.mysql.cj.jdbc.Driver",
                jdbc_url=cloudsql_writer_config.connector_config.to_connection_config(
                  ).jdbc_url,
                username=DB_USER,
                password=DB_PASSWORD,
                query=f"SELECT id, title, description FROM {table_name}",
                classpath=cloudsql_writer_config.connector_config.additional_jdbc_args()['classpath']
            )
        )
    
        # Generate and write embeddings
        _ = (
            rows
            | "Convert to Chunks" >> beam.Map(lambda row: Chunk(
                  id=row.id,
                  content=Content(text=f"{row.title}: {row.description}")
                )
              )
            | "Generate Embeddings" >> MLTransform(
                write_artifact_location=tempfile.mkdtemp()
            ).with_transform(HuggingfaceTextEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
            | "Write Back to CloudSQL MySQL" >> VectorDatabaseWriteTransform(
                cloudsql_writer_config
            )
        )
    

### Verify Data
    
    
    print("\nAfter embedding generation:")
    verify_embeddings_sqlalchemy(connection_name=CONNECTION_NAME, database=DB_NAME, table_name=table_name, user=DB_USER, password=DB_PASSWORD)
    

What Happened?

  1. We started with a table containing product data but no embeddings
  2. Read the existing records using ReadFromJdbc
  3. Converted rows to Chunks, combining title and description for embedding
  4. Generated embeddings using our model
  5. Wrote back to the same table, updating only the embedding field Preserved all other fields (price, etc.)



This pattern is useful when:

  * You have an existing product database
  * You want to add embeddings without disrupting current data
  * You need to maintain existing schema and relationships



## Generate Embeddings with VertexAI Text Embeddings

This section demonstrates how to use use the Vertex AI text-embeddings API to generate text embeddings that use Googles large generative artificial intelligence (AI) models.

Vertex AI models are subject to [Rate Limits and Quotas](https://cloud.google.com/vertex-ai/generative-ai/docs/quotas#view-the-quotas-by-region-and-by-model) and Dataflow automatically retries throttled requests with exponential backoff.

For more information, see [Get text embeddings](https://cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings) in the Vertex AI documentation.

### Authenticate with Google Cloud

To use the Vertex AI API, we authenticate with Google Cloud.
    
    
    # Replace <PROJECT_ID> with a valid Google Cloud project ID.
    PROJECT_ID = '' # @param {type:'string'}
    
    import sys
    if 'google.colab' in sys.modules:
      from google.colab import auth
      auth.authenticate_user(project_id=PROJECT_ID)
    

### Create CloudSQL MySQL table with default schema

First we create a table to store our embeddings:
    
    
    table_name = "vertex_product_embeddings"
    table_schema = f"""
      id VARCHAR(255) PRIMARY KEY,
      embedding VECTOR(768) USING VARBINARY,
      content text,
      metadata JSON
    """
    setup_db_table_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name,table_schema, DB_USER, DB_PASSWORD)
    test_db_connection_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name, DB_USER, DB_PASSWORD)
    

### Configure Embedding Handler

Import the `VertexAITextEmbeddings` handler, and specify the desired `textembedding-gecko` model.
    
    
    from apache_beam.ml.rag.embeddings.vertex_ai import VertexAITextEmbeddings
    
    vertexai_embedder = VertexAITextEmbeddings(model_name="text-embedding-005")
    

### Run the Pipeline
    
    
    import tempfile
    
    # Executing on DirectRunner (local execution)
    with beam.Pipeline() as p:
        _ = (
                p
                | 'Create Products' >> beam.Create(PRODUCTS_DATA)
                | 'Convert to Chunks' >> beam.Map(lambda product: Chunk(
                        content=Content(
                            text=f"{product['name']}: {product['description']}"
                        ), # The text that will be embedded
                        id=product['id'],  # Use product ID as chunk ID
                        metadata=product,  # Store all product info in metadata
                    )
                  )
                  | 'Generate Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
                    .with_transform(
                        vertexai_embedder
                    )
                  | 'Write to CloudSQL MySQL' >> VectorDatabaseWriteTransform(
                      CloudSQLMySQLVectorWriterConfig(
                        connection_config=LanguageConnectorConfig(
                            username=DB_USER,
                            password=DB_PASSWORD,
                            database_name=DB_NAME,
                            instance_name=CONNECTION_NAME
                        ),
                        table_name=table_name
                      )
                  )
              )
    

### Verify Embeddings
    
    
    print("\nAfter embedding generation:")
    verify_embeddings_sqlalchemy(connection_name=CONNECTION_NAME, database=DB_NAME, table_name=table_name, user=DB_USER, password=DB_PASSWORD)
    

## Streaming Embeddings Updates from PubSub

This section demonstrates how to build a real-time embedding pipeline that continuously processes product updates and maintains fresh embeddings in CloudSQL MySQL. This approach is ideal data that changes frequently.

This example runs on Dataflow because streaming with DirectRunner and writing via JDBC is not supported.

### Authenticate with Google Cloud

To use the PubSub, we authenticate with Google Cloud.
    
    
    # Replace <PROJECT_ID> with a valid Google Cloud project ID.
    PROJECT_ID = '' # @param {type:'string'}
    
    import sys
    if 'google.colab' in sys.modules:
      from google.colab import auth
      auth.authenticate_user(project_id=PROJECT_ID)
    

### Setting Up PubSub Resources

First, let's set up the necessary PubSub topics and subscriptions:
    
    
    from google.cloud import pubsub_v1
    from google.api_core.exceptions import AlreadyExists
    import json
    
    # Define pubsub topic
    TOPIC = "product-updates" # @param {type:'string'}
    
    # Create publisher client and topic
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC)
    try:
        topic = publisher.create_topic(request={"name": topic_path})
        print(f"Created topic: {topic.name}")
    except AlreadyExists:
        print(f"Topic {topic_path} already exists.")
    

### Create CloudSQL MySQL Table for Streaming Updates

Next, create a table to store the embedded data.
    
    
    table_name = "streaming_product_embeddings"
    table_schema = """
      id VARCHAR(255) PRIMARY KEY,
      embedding VECTOR(384) USING VARBINARY,
      content text,
      metadata JSON,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    """
    
    
    
    setup_db_table_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name,table_schema, DB_USER, DB_PASSWORD)
    test_db_connection_sqlalchemy(CONNECTION_NAME, DB_NAME, table_name, DB_USER, DB_PASSWORD)
    

### Configure the Pipeline options

To run the pipeline on DataFlow we need

  * A gcs bucket for staging DataFlow files. Replace `<BUCKET_NAME>`: the name of a valid Google Cloud Storage bucket. Don't include a gs:// prefix or trailing slashes
  * Optionally set the Google Cloud region that you want to run Dataflow in. Replace `<REGION>` with the desired location


    
    
    from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions, SetupOptions, GoogleCloudOptions, WorkerOptions
    
    options = PipelineOptions()
    options.view_as(StandardOptions).streaming = True
    
    # Provide required pipeline options for the Dataflow Runner.
    options.view_as(StandardOptions).runner = "DataflowRunner"
    
    # Set the Google Cloud region that you want to run Dataflow in.
    REGION = 'us-central1' # @param {type:'string'}
    options.view_as(GoogleCloudOptions).region = REGION
    
    NETWORK = '' # @param {type:'string'}
    if NETWORK:
      options.view_as(WorkerOptions).network = NETWORK
    
    SUBNETWORK = '' # @param {type:'string'}
    if SUBNETWORK:
      options.view_as(WorkerOptions).subnetwork = f"regions/{REGION}/subnetworks/{SUBNETWORK}"
    
    options.view_as(GoogleCloudOptions).project = PROJECT_ID
    
    BUCKET_NAME = '' # @param {type:'string'}
    dataflow_gcs_location = "gs://%s/dataflow" % BUCKET_NAME
    
    # The Dataflow staging location. This location is used to stage the Dataflow pipeline and the SDK binary.
    options.view_as(GoogleCloudOptions).staging_location = '%s/staging' % dataflow_gcs_location
    
    # The Dataflow temp location. This location is used to store temporary files or intermediate results before outputting to the sink.
    options.view_as(GoogleCloudOptions).temp_location = '%s/temp' % dataflow_gcs_location
    
    import random
    options.view_as(GoogleCloudOptions).job_name = f"cloudsql-streaming-embedding-ingest{random.randint(0,1000)}"
    
    # options.view_as(SetupOptions).save_main_session = True
    options.view_as(SetupOptions).requirements_file = "./requirements.txt"
    

### Provide additional Python dependencies to be installed on Worker VM's

We are making use of the HuggingFace `sentence-transformers` package to generate embeddings. Since this package is not installed on Worker VM's by default, we create a requirements.txt file with the additional dependencies to be installed on worker VM's.

See [Managing Python Pipeline Dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/) for more details.
    
    
    echo "sentence-transformers" > ./requirements.txt
    cat ./requirements.txt

### Configure and Run Pipeline

Our pipeline contains these key components:

  1. **Source** : Continuously reads messages from PubSub
  2. **Windowing** : Groups messages into 10-second windows for batch processing
  3. **Transformation** : Converts JSON messages to Chunk objects for embedding
  4. **ML Processing** : Generates embeddings using HuggingFace models
  5. **Sink** : Writes results to CloudSQL MySQL with conflict resolution


    
    
    import apache_beam as beam
    import tempfile
    import json
    
    from apache_beam.ml.transforms.base import MLTransform
    from apache_beam.ml.rag.types import Chunk, Content
    from apache_beam.ml.rag.ingestion.base import VectorDatabaseWriteTransform
    from apache_beam.ml.rag.ingestion.cloudsql import CloudSQLMySQLVectorWriterConfig
    from apache_beam.ml.rag.ingestion.cloudsql import LanguageConnectorConfig
    
    from apache_beam.ml.rag.ingestion.mysql_common import ConflictResolution
    
    from apache_beam.ml.rag.embeddings.huggingface import HuggingfaceTextEmbeddings
    from apache_beam.transforms.window import FixedWindows
    
    def parse_message(message):
      #Parse a message containing product data.
      product_json = json.loads(message.decode('utf-8'))
      return Chunk(
          content=Content(
              text=f"{product_json.get('name', '')}: {product_json.get('description', '')}"
          ),
          id=product_json.get('id', ''),
          metadata=product_json
      )
    
    pipeline = beam.Pipeline(options=options)
    # Streaming pipeline
    _ = (
        pipeline
        | "Read from PubSub" >> beam.io.ReadFromPubSub(
            topic=f"projects/{PROJECT_ID}/topics/{TOPIC}"
        )
        | "Window" >> beam.WindowInto(FixedWindows(10))
        | "Parse Messages" >> beam.Map(parse_message)
        | "Generate Embeddings" >> MLTransform(write_artifact_location=tempfile.mkdtemp())
            .with_transform(HuggingfaceTextEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
        | "Write to CloudSQL MySQL" >> VectorDatabaseWriteTransform(
            CloudSQLMySQLVectorWriterConfig(
                connection_config=LanguageConnectorConfig(
                    username=DB_USER,
                    password=DB_PASSWORD,
                    database_name=DB_NAME,
                    instance_name=CONNECTION_NAME
                ),
                table_name=table_name,
                conflict_resolution=ConflictResolution(
                    on_conflict_fields="id",
                    action="UPDATE",
                    update_fields=["embedding", "content", "metadata"]
                )
            )
        )
    )
    

### Create Publisher Subprocess

The publisher simulates real-time product updates by:

  * Publishing sample product data to the PubSub topic every 5 seconds
  * Modifying prices and descriptions to represent changes
  * Adding timestamps to track update times
  * Running for 25 minutes in the background while our pipeline processes the data



### Define PubSub publisher function

Toggle code
    
    
    import threading
    import time
    import json
    import logging
    from google.cloud import pubsub_v1
    import datetime
    import os
    import sys
    log_file = os.path.join(os.getcwd(), "publisher_log.txt")
    
    print(f"Log file will be created at: {log_file}")
    
    def publisher_function(project_id, topic):
        """Function that publishes sample product updates to a PubSub topic.
    
        This function runs in a separate thread and continuously publishes
        messages to simulate real-time product updates.
        """
        time.sleep(300)
        thread_id = threading.current_thread().ident
    
        process_log_file = os.path.join(os.getcwd(), f"publisher_{thread_id}.log")
    
        file_handler = logging.FileHandler(process_log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - ThreadID:%(thread)d - %(levelname)s - %(message)s'))
    
        logger = logging.getLogger(f"worker.{thread_id}")
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
    
        logger.info(f"Publisher thread started with ID: {thread_id}")
        file_handler.flush()
    
        publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
        topic_path = publisher.topic_path(project_id, topic)
    
        logger.info("Starting to publish messages...")
        file_handler.flush()
        for i in range(300):
            message_index = i % len(PRODUCTS_DATA)
            message = PRODUCTS_DATA[message_index].copy()
    
    
            dynamic_factor = 1.05 + (0.1 * ((i % 20) / 20))
            message["price"] = round(message["price"] * dynamic_factor, 2)
            message["description"] = f"PRICE UPDATE (factor: {dynamic_factor:.3f}): " + message["description"]
    
            message["published_at"] = datetime.datetime.now().isoformat()
    
            data = json.dumps(message).encode('utf-8')
            publish_future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data)
    
            try:
                logger.info(f"Publishing message {message}")
                file_handler.flush()
                message_id = publish_future.result()
                logger.info(f"Published message {i+1}: {message['id']} (Message ID: {message_id})")
                file_handler.flush()
            except Exception as e:
                logger.error(f"Error publishing message: {e}")
                file_handler.flush()
    
            time.sleep(5)
    
        logger.info("Finished publishing all messages.")
        file_handler.flush()
    

#### Start publishing to PuBSub in background
    
    
    # Launch publisher in a separate thread
    print("Starting publisher thread in 5 minutes...")
    publisher_thread = threading.Thread(
        target=publisher_function,
        args=(PROJECT_ID, TOPIC),
        daemon=True
    )
    publisher_thread.start()
    print(f"Publisher thread started with ID: {publisher_thread.ident}")
    print(f"Publisher thread logging to file: publisher_{publisher_thread.ident}.log")
    

### Run Pipeline on Dataflow

We launch the pipeline to run remotely on Dataflow. Once the job is launched, you can monitor its progress in the Google Cloud Console:

  1. Go to <https://console.cloud.google.com/dataflow/jobs>
  2. Select your project
  3. Click on the job named "cloudsql-streaming-embedding-ingest"
  4. View detailed execution graphs, logs, and metrics

**Note:** This streaming pipeline runs indefinitely until manually stopped. Be sure to monitor usage and terminate the job in the [dataflow job console](https://console.cloud.google.com/dataflow/jobs) when finished testing to avoid unnecessary costs.

### What to Expect

After running this pipeline, you should see:

  * Continuous updates to product embeddings in the CloudSQL MySQL table
  * Price and description changes reflected in the metadata
  * New embeddings generated for updated product descriptions
  * Timestamps showing when each record was last modified


    
    
    # Run pipeline
    pipeline.run().wait_until_finish()
    

### Verify data
    
    
    # Verify the results
    print("\nAfter embedding generation:")
    verify_embeddings_sqlalchemy(connection_name=CONNECTION_NAME, database=DB_NAME, table_name=table_name, user=DB_USER, password=DB_PASSWORD)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
