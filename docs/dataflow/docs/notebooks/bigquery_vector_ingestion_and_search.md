---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/bigquery_vector_ingestion_and_search/
title: Embedding Ingestion and Vector Search with Apache Beam and BigQuery \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:49.723196+00:00
---

# Embedding Ingestion and Vector Search with Apache Beam and BigQuery  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/bigquery_vector_ingestion_and_search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Embedding Ingestion and Vector Search with Apache Beam and BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/bigquery_vector_ingestion_and_search.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/bigquery_vector_ingestion_and_search.ipynb)

# Introduction

This Colab demonstrates how to use the [Apache Beam RAG package](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.rag.html) to generate embeddings, ingest them into BigQuery, and perform [vector similarity search](https://cloud.google.com/bigquery/docs/reference/standard-sql/search_functions#vector_search). The notebook is divided into two main parts:

  1. **Basic Example** : Using the default schema for simple vector search
  2. **Advanced Example** : Using a custom schema and metadata filtering



## Example: Product Catalog

We'll work with a sample e-commerce dataset representing a product catalog. Each product has:

  * **Structured fields:** `id`, `name`, `category`, `price`, etc.
  * **Detailed text descriptions:** Longer text describing the product's features.
  * **Additional metadata:** `brand`, `features`, `dimensions`, etc.



# Setup and Prerequisites

This example requires:

  1. A Google Cloud project with BigQuery enabled
  2. Apache Beam 2.64.0 or later



## Install Packages and Dependencies

First, let's install the Python packages required for the embedding and ingestion pipeline:
    
    
    # Apache Beam with GCP support
    pip install apache_beam[interactive,gcp]>=2.64.0 --quiet
    # Huggingface sentence-transformers for embedding models
    pip install sentence-transformers --quiet

## Authenticate to Google Cloud

To connect to BigQuery, we authenticate with Google Cloud.
    
    
    PROJECT_ID = ""  # @param {type:"string"}
    
    # Authentication and project setup
    from google.colab import auth
    auth.authenticate_user(project_id=PROJECT_ID)
    
    
    
    
    

## Create BigQuery Dataset

Let's set up a BigQuery dataset and table to store our embeddings:
    
    
    DATASET_ID = "" # @param {type:"string"}
    TEMP_GCS_LOCATION = "gs://" # @param {type:"string"}
    
    
    
    
    
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Create BigQuery client
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(project=PROJECT_ID)
    
    # Create dataset
    dataset_ref = client.[dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_dataset)(DATASET_ID)
    try:
        client.[get_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_dataset)(dataset_ref)
        print(f"Dataset {DATASET_ID} already exists")
    except Exception:
        dataset = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html)(dataset_ref)
        dataset.location = "US"
        dataset = client.[create_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_dataset)(dataset)
        print(f"Created dataset {DATASET_ID}")
    
    
    
    
    

## Importing Pipeline Components

We import the following for configuring our embedding ingestion pipeline:

  * `Chunk`, the structured that represents embeddable content with metadata
  * `BigQueryVectorWriterConfig` for configuring write behavior


    
    
    # Embedding-specific imports
    from apache_beam.ml.rag.ingestion.bigquery import BigQueryVectorWriterConfig, SchemaConfig
    from apache_beam.ml.rag.ingestion.base import VectorDatabaseWriteTransform
    from apache_beam.ml.rag.types import Chunk, Content
    from apache_beam.ml.rag.embeddings.huggingface import HuggingfaceTextEmbeddings
    from apache_beam.ml.rag.enrichment.bigquery_vector_search import (
        BigQueryVectorSearchParameters,
        BigQueryVectorSearchEnrichmentHandler
    )
    
    # Apache Beam core
    import apache_beam as beam
    from apache_beam.options import pipeline_options
    from apache_beam.options.pipeline_options import PipelineOptions
    from apache_beam.ml.transforms.base import MLTransform
    from apache_beam.transforms.enrichment import Enrichment
    
    
    
    
    

## Define helper functions

To run streaming examples we define helper functions to

  * Create a PubSub topic
  * Publish messages to a PubSub topic in a background thread


    
    
    # Set up PubSub topic
    from google.api_core.exceptions import AlreadyExists
    from google.cloud import pubsub_v1
    import threading
    import time
    import datetime
    import json
    
    def create_pubsub_topic(project_id, topic):
      publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
      topic_path = publisher.topic_path(project_id, topic)
      try:
          topic = publisher.create_topic(request={"name": topic_path})
          print(f"Created topic: {topic.name}")
      except AlreadyExists:
          print(f"Topic {topic_path} already exists.")
      return topic_path
    
    def publisher_function(project_id, topic, sample_data):
      """Function that publishes sample queries to a PubSub topic.
    
      This function runs in a separate thread and continuously publishes
      messages to simulate real-time user queries.
      """
      publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
      topic_path = publisher.topic_path(project_id, topic)
      time.sleep(15)
      for message in sample_data:
    
          # Convert to JSON and publish
          data = json.dumps(message).encode('utf-8')
          try:
              [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data)
          except Exception:
              pass  # Silently continue on error
    
          # Wait 7 seconds before next message
          time.sleep(7)
    
    
    
    
    

# Quick start: Embedding Generation and Ingestion with Default Schema

## Create Sample Product Catalog Data

First, we create a sample product catalog with descriptions to be embedded

### Create product catalog data with rich descriptions for semantic search

Toggle code
    
    
    PRODUCTS_DATA = [
        {
            "id": "laptop-001",
            "name": "UltraBook Pro X15",
            "description": "Powerful ultralight laptop featuring a 15-inch 4K OLED display, 12th Gen Intel i9 processor, 32GB RAM, and 1TB SSD. Perfect for creative professionals, developers, and power users who need exceptional performance in a slim form factor. Includes Thunderbolt 4 ports, all-day battery life, and advanced cooling system.",
            "category": "Electronics",
            "subcategory": "Laptops",
            "price": 1899.99,
            "brand": "TechMaster",
            "features": ["4K OLED Display", "Intel i9", "32GB RAM", "1TB SSD", "Thunderbolt 4"],
            "weight": "3.5 lbs",
            "dimensions": "14.1 x 9.3 x 0.6 inches"
        },
        {
            "id": "phone-001",
            "name": "Galaxy Ultra S23",
            "description": "Flagship smartphone with a stunning 6.8-inch Dynamic AMOLED display, 200MP camera system, and 5nm processor. Features 8K video recording, 5G connectivity, and all-day battery life. Water and dust resistant with IP68 rating. Perfect for photography enthusiasts, mobile gamers, and professionals who need reliable performance.",
            "category": "Electronics",
            "subcategory": "Smartphones",
            "price": 1199.99,
            "brand": "Samsung",
            "features": ["200MP Camera", "6.8-inch AMOLED", "5G", "IP68 Water Resistant", "8K Video"],
            "weight": "8.2 oz",
            "dimensions": "6.4 x 3.1 x 0.35 inches"
        },
        {
            "id": "headphones-001",
            "name": "SoundSphere Pro",
            "description": "Premium wireless noise-cancelling headphones with spatial audio technology and adaptive EQ. Features 40 hours of battery life, memory foam ear cushions, and voice assistant integration. Seamlessly switch between devices with multi-point Bluetooth connectivity. Ideal for audiophiles, frequent travelers, and professionals working in noisy environments.",
            "category": "Electronics",
            "subcategory": "Audio",
            "price": 349.99,
            "brand": "AudioTech",
            "features": ["Active Noise Cancellation", "Spatial Audio", "40hr Battery", "Bluetooth 5.2", "Voice Assistant"],
            "weight": "9.8 oz",
            "dimensions": "7.5 x 6.8 x 3.2 inches"
        },
        {
            "id": "coffee-001",
            "name": "BrewMaster 5000",
            "description": "Smart coffee maker with precision temperature control, customizable brewing profiles, and app connectivity. Schedule brewing times, adjust strength, and receive maintenance alerts from your smartphone. Features a built-in grinder, 12-cup capacity, and thermal carafe to keep coffee hot for hours. Perfect for coffee enthusiasts and busy professionals.",
            "category": "Home & Kitchen",
            "subcategory": "Appliances",
            "price": 199.99,
            "brand": "HomeBarista",
            "features": ["Smart App Control", "Built-in Grinder", "Thermal Carafe", "Customizable Brewing", "12-cup Capacity"],
            "weight": "12.5 lbs",
            "dimensions": "10.5 x 8.2 x 14.3 inches"
        },
        {
            "id": "chair-001",
            "name": "ErgoFlex Executive Chair",
            "description": "Ergonomic office chair with dynamic lumbar support, adjustable armrests, and breathable mesh back. Features 5-point adjustability, premium cushioning, and smooth-rolling casters. Designed to reduce back pain and improve posture during long work sessions. Ideal for home offices, professionals, and anyone who sits for extended periods.",
            "category": "Furniture",
            "subcategory": "Office Furniture",
            "price": 329.99,
            "brand": "ComfortDesign",
            "features": ["Lumbar Support", "Adjustable Armrests", "Mesh Back", "5-point Adjustment", "Premium Cushioning"],
            "weight": "45 lbs",
            "dimensions": "28 x 25 x 45 inches"
        },
        {
            "id": "sneakers-001",
            "name": "CloudStep Running Shoes",
            "description": "Lightweight performance running shoes with responsive cushioning, breathable knit upper, and carbon fiber plate for energy return. Features adaptive arch support, reflective elements for visibility, and durable rubber outsole. Designed for marathon runners, daily joggers, and fitness enthusiasts seeking comfort and performance.",
            "category": "Apparel",
            "subcategory": "Footwear",
            "price": 159.99,
            "brand": "AthleteElite",
            "features": ["Responsive Cushioning", "Carbon Fiber Plate", "Breathable Knit", "Adaptive Support", "Reflective Elements"],
            "weight": "8.7 oz",
            "dimensions": "12 x 4.5 x 5 inches"
        },
        {
            "id": "blender-001",
            "name": "NutriBlend Pro",
            "description": "High-performance blender with 1200W motor, variable speed control, and pre-programmed settings for smoothies, soups, and nut butters. Features stainless steel blades, 64oz BPA-free container, and pulse function. Includes personal blending cups for on-the-go nutrition. Perfect for health-conscious individuals, busy families, and culinary enthusiasts.",
            "category": "Home & Kitchen",
            "subcategory": "Appliances",
            "price": 149.99,
            "brand": "KitchenPro",
            "features": ["1200W Motor", "Variable Speed", "Pre-programmed Settings", "64oz Container", "Personal Cups"],
            "weight": "11.8 lbs",
            "dimensions": "8.5 x 9.5 x 17.5 inches"
        },
        {
            "id": "camera-001",
            "name": "ProShot X7 Mirrorless Camera",
            "description": "Professional mirrorless camera with 45MP full-frame sensor, 8K video recording, and advanced autofocus system with subject recognition. Features in-body stabilization, weather sealing, and dual card slots. Includes a versatile 24-105mm lens. Ideal for professional photographers, videographers, and serious enthusiasts seeking exceptional image quality.",
            "category": "Electronics",
            "subcategory": "Cameras",
            "price": 2499.99,
            "brand": "OptiView",
            "features": ["45MP Sensor", "8K Video", "Advanced Autofocus", "In-body Stabilization", "Weather Sealed"],
            "weight": "1.6 lbs (body only)",
            "dimensions": "5.4 x 3.8 x 3.2 inches"
        },
        {
            "id": "watch-001",
            "name": "FitTrack Ultra Smartwatch",
            "description": "Advanced fitness smartwatch with continuous health monitoring, GPS tracking, and 25-day battery life. Features ECG, blood oxygen monitoring, sleep analysis, and 30+ sport modes. Water-resistant to 50m with a durable sapphire crystal display. Perfect for athletes, fitness enthusiasts, and health-conscious individuals tracking wellness metrics.",
            "category": "Electronics",
            "subcategory": "Wearables",
            "price": 299.99,
            "brand": "FitTech",
            "features": ["ECG Monitor", "GPS Tracking", "25-day Battery", "Blood Oxygen", "30+ Sport Modes"],
            "weight": "1.6 oz",
            "dimensions": "1.7 x 1.7 x 0.5 inches"
        },
        {
            "id": "backpack-001",
            "name": "Voyager Pro Travel Backpack",
            "description": "Premium travel backpack with anti-theft features, expandable capacity, and dedicated laptop compartment. Features water-resistant materials, hidden pockets, and ergonomic design with padded straps. Includes USB charging port and luggage pass-through. Ideal for business travelers, digital nomads, and adventure seekers needing secure, organized storage.",
            "category": "Travel",
            "subcategory": "Luggage",
            "price": 129.99,
            "brand": "TrekGear",
            "features": ["Anti-theft Design", "Expandable", "Laptop Compartment", "Water Resistant", "USB Charging Port"],
            "weight": "2.8 lbs",
            "dimensions": "20 x 12 x 8 inches"
        }
    ]
    
    print(f"Created product catalog with {len(PRODUCTS_DATA)} products")
    
    
    
    
    

## Create BigQuery Table
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Create BigQuery client
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(project=PROJECT_ID)
    
    DEFAULT_TABLE_ID = f"{PROJECT_ID}.{DATASET_ID}.default_product_embeddings"
    default_schema = [
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("id", "STRING", mode="REQUIRED"),
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("embedding", "FLOAT64", mode="REPEATED"),
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("content", "STRING"),
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("metadata", "RECORD", mode="REPEATED", fields=[
            [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("key", "STRING"),
            [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("value", "STRING")
        ])
    ]
    
    default_table = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html)(DEFAULT_TABLE_ID, schema=default_schema)
    try:
        client.[get_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table)(default_table)
        print(f"Table {DEFAULT_TABLE_ID} already exists")
    except Exception:
        default_table = client.[create_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_table)(default_table)
        print(f"Created table {DEFAULT_TABLE_ID}")
    
    
    
    
    

## Define Pipeline components

Next, we define pipeline components that

  1. Convert product data to `Chunk` type
  2. Generate Embeddings using a pre-trained model
  3. Write to BigQuery



### Map products to Chunks

We define a function convert each ingested product dictionary to a `Chunk` to configure what text to embed and what to treat as metadata.
    
    
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
        # Combine name and description for embedding
        text_to_embed = f"{product['name']}: {product['description']}"
    
        return Chunk(
            content=Content(text=text_to_embed),  # The text that will be embedded
            id=product['id'],                     # Use product ID as chunk ID
            metadata=product,                     # Store all product info in metadata
        )
    
    
    
    
    

### Generate embeddings with HuggingFace

We configure a local pre-trained Hugging Face model to create vector embeddings from the product descriptions.
    
    
    # Configure the embedding model
    huggingface_embedder = HuggingfaceTextEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    
    
    
    

### Write to BigQuery

The default BigQueryVectorWriterConfig maps Chunk fields to database columns as: | Database Column | Chunk Field | Description  
---|---|---  
id | chunk.id | Unique identifier  
embedding | chunk.embedding.dense_embedding | Vector representation  
content | chunk.content.text | Text that was embedded  
metadata | chunk.metadata | Additional data as RECORD  
      
    
    # Configure BigQuery writer with default schema
    bigquery_writer_config = BigQueryVectorWriterConfig(
        write_config={
            'table': DEFAULT_TABLE_ID,
            'create_disposition': 'CREATE_IF_NEEDED',
            'write_disposition': 'WRITE_TRUNCATE'  # Overwrite existing data
        }
    )
    
    
    
    
    

## Assemble and Run Pipeline

Now we can create our pipeline that:

  1. Ingests our product data
  2. Converts each product to a Chunk
  3. Generates embeddings for each Chunk
  4. Stores everything in BigQuery


    
    
    import tempfile
    
    options = pipeline_options.PipelineOptions([f"--temp_location={TEMP_GCS_LOCATION}"])
    
    # Run batch pipeline
    with beam.Pipeline(options=options) as p:
        _ = (
            p
            | 'Create Products' >> beam.Create(PRODUCTS_DATA)
            | 'Convert to Chunks' >> beam.Map(create_chunk)
            | 'Generate Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
              .with_transform(huggingface_embedder)
            | 'Write to BigQuery' >> VectorDatabaseWriteTransform(bigquery_writer_config)
        )
    
    
    
    
    

## Verify Embeddings

Let's check what was written to our BigQuery table:
    
    
    # Query to verify the embeddings
    query = f"""
    SELECT
      id,
      ARRAY_LENGTH(embedding) as embedding_dimensions,
      content,
      (SELECT COUNT(*) FROM UNNEST(metadata)) as metadata_count
    FROM
      `{DEFAULT_TABLE_ID}`
    LIMIT 5
    """
    
    # Run the query
    query_job = client.query(query)
    results = query_job.result()
    
    # Display results
    for row in results:
        print(f"Product ID: {row.id}")
        print(f"Embedding Dimensions: {row.embedding_dimensions}")
        print(f"Content: {row.content[:100]}...")  # Show first 100 chars
        print(f"Metadata Count: {row.metadata_count}")
        print("-" * 80)
    
    
    
    
    

# Quick start: Vector Search

Prerequisites:

  * Quick start: Basic Vector Generation and Ingestion



In this section we create a streaming pipeline that

  * Reads queries from PubSub
  * Embeds the queries
  * Performs Vector Search on the ingested product catalog data
  * Logs the queries enriched with product catalog data



## Define Sample Queries
    
    
    SAMPLE_QUERIES = [
        {"query": "I need a powerful laptop for video editing and programming"},
        {"query": "Looking for noise-cancelling headphones for travel"},
        {"query": "What's a good ergonomic office chair for long work hours?"},
        {"query": "I want a waterproof portable speaker for the beach"},
        {"query": "Need a professional camera for wildlife photography"}
    ]
    
    
    
    
    

## Setup PubSub Steaming Source

We create a PubSub topic for our pipeline's data source.
    
    
    # Create pubsub topic
    TOPIC = "" # @param {type:'string'}
    
    topic_path = create_pubsub_topic(PROJECT_ID, TOPIC)
    
    
    
    
    

## Define pipeline components

Next, we define pipeline components.

### Process PubSub messages
    
    
    def process_query(message):
        """Convert a pubsub message to a Chunk for embedding and search."""
        message_data = json.loads(message.decode('utf-8'))
        return Chunk(
            content=Content(text=message_data['query']),
            metadata={"query_type": "product_search"}
        )
    
    
    
    
    

### Configure embedding model
    
    
    # Configure the embedding model
    huggingface_embedder = HuggingfaceTextEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    
    
    
    

### Configure vector search
    
    
    # Configure vector search parameters (no filters)
    vector_search_params = BigQueryVectorSearchParameters(
        project=PROJECT_ID,
        table_name=DEFAULT_TABLE_ID,
        embedding_column="embedding",
        columns=["content", "metadata"],
        neighbor_count=1  # Return top match
    )
    
    # Create search handler
    search_handler = BigQueryVectorSearchEnrichmentHandler(
        vector_search_parameters=vector_search_params,
        min_batch_size=1,
        max_batch_size=5
    )
    
    
    
    
    

### Log the enriched query
    
    
    def log_results(chunk):
        """Format search results for display."""
        # Extract results from enrichment_data
        results = chunk.metadata.get("enrichment_data", {}).get("chunks", [])
    
        # Log the query
        print(f"\n=== QUERY: \"{chunk.content.text}\" ===")
    
        # Log the results
        print(f"Found {len(results)} matching products:")
    
        if results:
            for i, result in enumerate(results, 1):
                # Convert metadata array to dictionary
                product_metadata = {}
                if "metadata" in result:
                    for item in result.get("metadata", []):
                        product_metadata[item["key"]] = item["value"]
    
                # Print product details
                print(f"\nResult {i}:")
                print(f"  Product: {product_metadata.get('name', 'Unknown')}")
                print(f"  Brand: {product_metadata.get('brand', 'Unknown')}")
                print(f"  Category: {product_metadata.get('category', 'Unknown')} > {product_metadata.get('subcategory', 'Unknown')}")
                print(f"  Price: ${product_metadata.get('price', 'Unknown')}")
                print(f"  Description: {product_metadata.get('description', 'Unknown')[:100]}...")
        else:
            print("  No matching products found.")
    
        print("=" * 80)
    
        return chunk
    
    
    
    
    

## Run the Basic Search Pipeline

Now we'll start publishing messages to PubSub in the background, and run our pipeline to:

  1. Process the sample queries
  2. Generate embeddings for each query
  3. Perform vector search in BigQuery
  4. Format and display the results

**Note:** This pipeline will keep running until the execution is interrupted.
    
    
    print("Starting publisher thread...")
    publisher_thread = threading.Thread(
        target=publisher_function,
        args=(PROJECT_ID, TOPIC, SAMPLE_QUERIES),
        daemon=True
    )
    publisher_thread.start()
    print(f"Publisher thread started with ID: {publisher_thread.ident}")
    
    import tempfile
    from apache_beam.transforms import trigger
    
    options = pipeline_options.PipelineOptions()
    options.view_as(pipeline_options.StandardOptions).streaming = True
    # Run the streaming pipeline
    print(f"Running pipeline...")
    with beam.Pipeline(options=options) as p:
        results = (
            p
            | 'Read from PubSub' >> beam.io.ReadFromPubSub(topic=topic_path)
            | 'Process Messages' >> beam.Map(process_query)
            | 'Window' >> beam.WindowInto(beam.window.GlobalWindows(),
                                 trigger=trigger.Repeatedly(
                                    trigger.AfterProcessingTime(
                                        1)),
                                 accumulation_mode=trigger.AccumulationMode\
                                     .DISCARDING)
            | 'Generate Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
              .with_transform(huggingface_embedder)
            | 'Vector Search' >> Enrichment(search_handler)
            | 'Log Results' >> beam.Map(log_results)
        )
    
    
    
    
    

# Advanced: Embedding Generation and Ingestion with Custom Schema

In this part, we create pipelines to

  * Write embeddings to a BigQuery table with a custom schema
  * Perform Vector Search with metadata filters.



## Create Product Dataset with Multiple Items per Category

Let's create a more focused product dataset with multiple items in each category to better demonstrate filtering:
    
    
    FILTERED_PRODUCTS_DATA = [
        # Electronics - Laptops (3 items with different price points)
        {
            "id": "laptop-001",
            "name": "UltraBook Pro X15",
            "description": "Powerful ultralight laptop featuring a 15-inch 4K OLED display, 12th Gen Intel i9 processor, 32GB RAM, and 1TB SSD. Perfect for creative professionals, developers, and power users who need exceptional performance in a slim form factor.",
            "category": "Electronics",
            "subcategory": "Laptops",
            "price": 1899.99,
            "brand": "TechMaster"
        },
        {
            "id": "laptop-002",
            "name": "UltraBook Air 13",
            "description": "Thin and light laptop with 13-inch Retina display, M2 chip, 16GB RAM, and 512GB SSD. Ideal for students, travelers, and professionals who need portability without sacrificing performance.",
            "category": "Electronics",
            "subcategory": "Laptops",
            "price": 1299.99,
            "brand": "TechMaster"
        },
        {
            "id": "laptop-003",
            "name": "PowerBook Gaming Pro",
            "description": "High-performance gaming laptop with 17-inch 144Hz display, RTX 3080 graphics, Intel i7 processor, 32GB RAM, and 1TB SSD. Designed for serious gamers and content creators who need desktop-class performance in a portable package.",
            "category": "Electronics",
            "subcategory": "Laptops",
            "price": 2199.99,
            "brand": "GameTech"
        },
    
        # Electronics - Headphones (3 items with different price points)
        {
            "id": "headphones-001",
            "name": "SoundSphere Pro",
            "description": "Premium wireless noise-cancelling headphones with spatial audio technology and adaptive EQ. Features 40 hours of battery life, memory foam ear cushions, and voice assistant integration.",
            "category": "Electronics",
            "subcategory": "Headphones",
            "price": 349.99,
            "brand": "AudioTech"
        },
        {
            "id": "headphones-002",
            "name": "SoundSphere Sport",
            "description": "Wireless sport earbuds with sweat and water resistance, secure fit, and 8-hour battery life. Perfect for workouts, running, and active lifestyles.",
            "category": "Electronics",
            "subcategory": "Headphones",
            "price": 129.99,
            "brand": "AudioTech"
        },
        {
            "id": "headphones-003",
            "name": "BassBoost Studio",
            "description": "Professional studio headphones with high-fidelity sound, premium materials, and exceptional comfort for long sessions. Designed for audio engineers, musicians, and audiophiles.",
            "category": "Electronics",
            "subcategory": "Headphones",
            "price": 249.99,
            "brand": "SoundPro"
        },
    
        # Home & Kitchen - Coffee Makers (3 items with different price points)
        {
            "id": "coffee-001",
            "name": "BrewMaster 5000",
            "description": "Smart coffee maker with precision temperature control, customizable brewing profiles, and app connectivity. Schedule brewing times, adjust strength, and receive maintenance alerts from your smartphone.",
            "category": "Home & Kitchen",
            "subcategory": "Coffee Makers",
            "price": 199.99,
            "brand": "HomeBarista"
        },
        {
            "id": "coffee-002",
            "name": "BrewMaster Espresso",
            "description": "Semi-automatic espresso machine with 15-bar pressure pump, milk frother, and programmable settings. Make cafe-quality espresso, cappuccino, and latte at home.",
            "category": "Home & Kitchen",
            "subcategory": "Coffee Makers",
            "price": 299.99,
            "brand": "HomeBarista"
        },
        {
            "id": "coffee-003",
            "name": "BrewMaster Basic",
            "description": "Simple, reliable drip coffee maker with 12-cup capacity, programmable timer, and auto-shutoff. Perfect for everyday coffee drinkers who want convenience and consistency.",
            "category": "Home & Kitchen",
            "subcategory": "Coffee Makers",
            "price": 49.99,
            "brand": "HomeBarista"
        },
    
        # Furniture - Office Chairs (3 items with different price points)
        {
            "id": "chair-001",
            "name": "ErgoFlex Executive Chair",
            "description": "Ergonomic office chair with dynamic lumbar support, adjustable armrests, and breathable mesh back. Features 5-point adjustability, premium cushioning, and smooth-rolling casters.",
            "category": "Furniture",
            "subcategory": "Office Chairs",
            "price": 329.99,
            "brand": "ComfortDesign"
        },
        {
            "id": "chair-002",
            "name": "ErgoFlex Task Chair",
            "description": "Mid-range ergonomic task chair with fixed lumbar support, height-adjustable armrests, and mesh back. Perfect for home offices and everyday use.",
            "category": "Furniture",
            "subcategory": "Office Chairs",
            "price": 179.99,
            "brand": "ComfortDesign"
        },
        {
            "id": "chair-003",
            "name": "ErgoFlex Budget Chair",
            "description": "Affordable office chair with basic ergonomic features, armrests, and fabric upholstery. A practical choice for occasional use or budget-conscious shoppers.",
            "category": "Furniture",
            "subcategory": "Office Chairs",
            "price": 89.99,
            "brand": "ComfortDesign"
        }
    ]
    
    
    
    
    

## Create BigQuery Table with Custom Schema

Now, let's create a BigQuery table with a custom schema that unnests metadata fields:
    
    
    # Create table with custom schema for vector embeddings
    CUSTOM_TABLE_ID = f"{PROJECT_ID}.{DATASET_ID}.custom_product_embeddings"
    custom_schema = [
        bigquery.SchemaField("id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("embedding", "FLOAT64", mode="REPEATED"),
        bigquery.SchemaField("content", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("category", "STRING"),
        bigquery.SchemaField("subcategory", "STRING"),
        bigquery.SchemaField("price", "FLOAT64"),
        bigquery.SchemaField("brand", "STRING")
    ]
    
    custom_table = bigquery.Table(CUSTOM_TABLE_ID, schema=custom_schema)
    try:
        client.get_table(custom_table)
        print(f"Table {CUSTOM_TABLE_ID} already exists")
    except Exception:
        custom_table = client.create_table(custom_table)
        print(f"Created table {CUSTOM_TABLE_ID}")
    
    
    
    
    

## Define Pipeline components

Our pipeline

  * Ingests product data as dictionaries
  * Converts product dictionaries to `Chunk`
  * Generates embeddings
  * Writes embeddings and metadata to a BigQuery with a custom schema



### Convert product dictionary

We define a function convert each ingested product dictionary to a Chunk to configure what text to embed and what to treat as metadata.
    
    
    from typing import Dict, Any
    
    def create_chunk(product: Dict[str, Any]) -> Chunk:
        """Convert a product dictionary into a Chunk object.
    
        Args:
            product: Dictionary containing product information
    
        Returns:
            Chunk: A Chunk object ready for embedding
        """
        # Combine name and description for embedding
        text_to_embed = f"{product['name']}: {product['description']}"
    
        return Chunk(
            content=Content(text=text_to_embed),  # The text that will be embedded
            id=product['id'],                     # Use product ID as chunk ID
            metadata=product,                     # Store all product info in metadata
        )
    
    
    
    
    

### Generate embeddings with HuggingFace

We configure a local pre-trained Hugging Face model to create vector embeddings from the product descriptions.
    
    
    # Configure the embedding model
    huggingface_embedder = HuggingfaceTextEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    
    
    
    

### Configure BigQuery Vector Writer

To write embedded data to a BigQuery table with a custom schema we need to

  * Provide the BigQuery table schema
  * Define a function to convert the embedded `Chunk` to a dictionary that matches our BigQuery schema


    
    
    # Define BigQuery schema
    SCHEMA = {
        'fields': [
            {'name': 'id', 'type': 'STRING'},
            {'name': 'embedding', 'type': 'FLOAT64', 'mode': 'REPEATED'},
            {'name': 'content', 'type': 'STRING'},
            {'name': 'name', 'type': 'STRING'},
            {'name': 'category', 'type': 'STRING'},
            {'name': 'subcategory', 'type': 'STRING'},
            {'name': 'price', 'type': 'FLOAT64'},
            {'name': 'brand', 'type': 'STRING'}
        ]
    }
    
    # Define function to convert Chunk to dictionary with the custom schema
    def chunk_to_dict_custom(chunk: Chunk) -> Dict[str, Any]:
        """Convert a Chunk to a dictionary matching our custom schema."""
        # Extract metadata
        metadata = chunk.metadata
    
        # Map to custom schema
        return {
            'id': chunk.id,
            'embedding': chunk.embedding.dense_embedding,
            'content': chunk.content.text,
            'name': metadata.get('name', ''),
            'category': metadata.get('category', ''),
            'subcategory': metadata.get('subcategory', ''),
            'price': float(metadata.get('price', 0)),
            'brand': metadata.get('brand', '')
        }
    
    
    
    
    

Now we create a `BigQueryVectorWriterConfig` with a `SchemaConfig` parameter
    
    
    custom_writer_config = BigQueryVectorWriterConfig(
        write_config={
            'table': CUSTOM_TABLE_ID,
            'create_disposition': 'CREATE_IF_NEEDED',
            'write_disposition': 'WRITE_TRUNCATE'  # Overwrite existing data
        },
        schema_config=SchemaConfig(
            schema=SCHEMA,
            chunk_to_dict_fn=chunk_to_dict_custom
        )
    )
    
    
    
    
    

## Assemble and Run pipeline
    
    
    import tempfile
    
    options = pipeline_options.PipelineOptions([f"--temp_location={TEMP_GCS_LOCATION}"])
    
    
    # Run batch pipeline with custom schema
    with beam.Pipeline(options=options) as p:
        _ = (
            p
            | 'Create Products' >> beam.Create(FILTERED_PRODUCTS_DATA)
            | 'Convert to Chunks' >> beam.Map(create_chunk)
            | 'Generate Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
              .with_transform(huggingface_embedder)
            | 'Write to BigQuery' >> VectorDatabaseWriteTransform(custom_writer_config)
        )
    
    
    
    
    

## Verify Custom Schema Embeddings

Let's check what was written to our custom schema table:
    
    
    # Query to verify the custom schema embeddings
    query = f"""
    SELECT
      id,
      name,
      category,
      subcategory,
      price,
      brand,
    FROM
      `{CUSTOM_TABLE_ID}`
    ORDER BY category, subcategory, price
    LIMIT 5
    """
    
    # Run the query
    query_job = client.query(query)
    results = query_job.result()
    
    # Display results
    print("First 5 Products in Custom Schema Table:")
    print("-" * 80)
    for row in results:
        print(f"ID: {row.id}")
        print(f"Name: {row.name}")
        print(f"Category: {row.category} > {row.subcategory}")
        print(f"Price: ${row.price}")
        print(f"Brand: {row.brand}")
        print("-" * 80)
    
    
    
    
    

# Advanced: Vector Search with Metadata Filter

Prerequisites:

  * Advanced: Example with Custom Schema



Now let's demonstrate how to perform vector search with filtering using our custom schema.

Our pipeline:

  * Reads messages from PubSub that contains a `query` and `max_price` filter
  * Generates embeddings for the `query`
  * Performs vector search with additional `max_price` metadata filter



## Sample Queries with Filter Requirements

We define a list of messages to be published to PubSub. This is the data ingested to our pipeline.
    
    
    FILTERED_QUERIES = [
        {"query": "I need a powerful laptop for video editing", "max_price": 2000},
        {"query": "Looking for noise-cancelling headphones", "max_price": 300},
        {"query": "What's a good ergonomic office chair?", "max_price": 200},
        {"query": "I want an affordable coffee maker", "max_price": 100},
        {"query": "Need a premium laptop with good specs", "max_price": 1500}
    ]
    
    
    
    
    

### Create PubSub Topic

We create a PubSub topic to be used as our pipeline data source
    
    
    # Define pubsub topic for filtered queries
    TOPIC = "" # @param {type:'string'}
    
    topic_path = create_pubsub_topic(PROJECT_ID, TOPIC)
    
    
    
    
    

## Define Pipeline components

### Process PubSub messages
    
    
    def process(message):
        """Convert a filtered query message to a Chunk for embedding and search."""
        message_data = json.loads(message.decode('utf-8'))
        return Chunk(
            content=Content(text=message_data['query']),
            metadata={
                "max_price": message_data['max_price']
            }
        )
    
    
    
    
    

### Configure embedding model
    
    
    # Configure the embedding model
    huggingface_embedder = HuggingfaceTextEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    
    
    
    

### Configure Vector Search with Metadata Filter

Vector search will return the two most semantically similar product with an upper price limit of `max_price`
    
    
    # Configure vector search parameters with metadata_restriction_template
    vector_search_params = BigQueryVectorSearchParameters(
        project=PROJECT_ID,
        table_name=CUSTOM_TABLE_ID,
        embedding_column="embedding",
        columns=["id", "name", "category", "subcategory", "price", "brand", "content"],
        neighbor_count=1,
        metadata_restriction_template="price <= {max_price}"
    )
    
    # Create search handler
    search_handler = BigQueryVectorSearchEnrichmentHandler(
        vector_search_parameters=vector_search_params,
        min_batch_size=1,
        max_batch_size=5
    )
    
    
    
    
    

### Log the enriched query
    
    
    def format_filtered_results(chunk):
        """Format filtered search results for display."""
        # Extract results from enrichment_data
        results = chunk.metadata.get("enrichment_data", {}).get("chunks", [])
        max_price = chunk.metadata.get("max_price")
    
        # Log the query
        print(f"\n=== PRICE-FILTERED QUERY ===")
        print(f"Query: \"{chunk.content.text}\"")
        print(f"Max Price: ${max_price}")
    
        # Log the results
        print(f"\nFound {len(results)} matching products under ${max_price}:")
    
        if results:
            for i, result in enumerate(results, 1):
                # Print product details
                print(f"\nResult {i}:")
                print(f"  Product: {result.get('name', 'Unknown')}")
                print(f"  Category: {result.get('category', 'Unknown')} > {result.get('subcategory', 'Unknown')}")
                print(f"  Price: ${result.get('price', 'Unknown')}")
                print(f"  Brand: {result.get('brand', 'Unknown')}")
                print(f"  Description: {result.get('content', 'Unknown')}")
                print(f"  Similarity distance: {result.get('distance', 'Unknown')}")
    
                # Verify price is under max
                price = float(result.get('price', 0))
                print(f"  Price Check: {'✓' if price <= max_price else '✗'}")
        else:
            print("  No matching products found.")
    
        print("=" * 80)
    
        return chunk
    
    
    
    
    

## Run Vector Search with metadata filter Pipeline
    
    
    import tempfile
    from apache_beam.transforms import trigger
    
    print("Starting publisher thread...")
    publisher_thread = threading.Thread(
        target=publisher_function,
        args=(PROJECT_ID, TOPIC, FILTERED_QUERIES),
        daemon=True
    )
    publisher_thread.start()
    print(f"Publisher thread started with ID: {publisher_thread.ident}")
    
    options = pipeline_options.PipelineOptions()
    options.view_as(pipeline_options.StandardOptions).streaming = True
    # Run the streaming pipeline with price filtering
    with beam.Pipeline(options=options) as p:
        results = (
            p
            | 'Read from PubSub' >> beam.io.ReadFromPubSub(topic=topic_path)
            | 'Process Messages' >> beam.Map(process)
            | 'Window' >> beam.WindowInto(beam.window.GlobalWindows(),
                                 trigger=trigger.Repeatedly(
                                    trigger.AfterProcessingTime(
                                        30)),
                                 accumulation_mode=trigger.AccumulationMode\
                                     .DISCARDING)
            | 'Generate Embeddings' >> MLTransform(write_artifact_location=tempfile.mkdtemp())
              .with_transform(huggingface_embedder)
            | 'Price-Filtered Vector Search' >> Enrichment(search_handler)
            | 'Format Filtered Results' >> beam.Map(format_filtered_results)
        )
    
    
    
    
    

# Whats next?

  * Check out the [Apache Beam RAG package documentation](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.rag.html)
  * [Configure BigQueryVectorSearchParameters](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.rag.enrichment.bigquery_vector_search.html#apache_beam.ml.rag.enrichment.bigquery_vector_search.BigQueryVectorSearchParameters.options) further by specifying `options` or `distance_type`, as specified by [BigQuery VECTOR_SEARCH documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/search_functions#vector_search)
  * Split large documents into smaller `Chunk's` with [LangChain](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.rag.chunking.langchain.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
