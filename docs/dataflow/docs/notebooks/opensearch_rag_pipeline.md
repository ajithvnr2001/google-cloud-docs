---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/opensearch_rag_pipeline/
title: RAG Demo on Opensearch \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:04:37.988824+00:00
---

# RAG Demo on Opensearch  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/opensearch_rag_pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  RAG Demo on Opensearch Stay organized with collections  Save and categorize content based on your preferences. 

This notebook provides an example of using opensearch vector Database as a knowledge Base for building RAG based AI Application. This notebook provides a custom IO python client for Ingestion and Enrichment pipeline using opensearch vector DB which can be used for building RAG applications. Please follow step by step instructions to be able to write custom IO class for python client for opensearch vector database.
    
    
    #installing dependencies
    pip install pandas==1.4.4
    pip install numpy==1.24.4
    pip install apache_beam[interactive]==2.56.0
    pip install opensearch==2.1.0
    #used for chunking
    pip install langchain==0.1.14
    
    
    import apache_beam as beam
    import pandas as pd
    from apache_beam.ml.transforms.base import MLTransform
    from apache_beam.transforms.enrichment import Enrichment
    from apache_beam.ml.transforms.embeddings.huggingface import SentenceTransformerEmbeddings
    import tempfile
    import json
    
    from opensearchpy import OpenSearch
    

Below imports are the python files which are present in the same folder as the notebook. These imports are not part of any beam module.
    
    
    from opensearch_connector import *
    from opensearch_enrichment import *
    from chunks_generation import *
    
    
    
    #To check beam version installed 
    beam.__version__
    
    
    
    '2.56.0'
    

Usually users should have their credentials file setup but for completeness here we generate the file to be later consumed through right channels.
    
    
    cell_str='''OPENSEARCH_USERNAME="<REPLACE_WITH_YOUR_USERNAME>"
    OPENSEARCH_PASSWORD="<REPLACE_WITH_YOUR_PASSWORD>"
    '''
    
    with open('credentials.env', 'w') as f:
      f.write(cell_str)
    

Next we load the Opensearch credentials that will be needed in access during following steps. It reads credentials from environment. Please replace the values in the file before running this.
    
    
    from dotenv import load_dotenv
    
    load_dotenv('credentials.env')
    

# Reading json data
    
    
    with open('hf_small_wikipedia.json', 'r') as j:
         contents = json.loads(j.read())
    
    
    
    type(contents)
    
    
    
    list
    

# Creating a Search Index¶

### Specify and create a search index in OpenSearch vector DB.

  1. Set some constants for defining our index like the distance metric and the index name.

  2. Define the index schema with OpenSearchSearch fields.

  3. Create the index.

  4. Index creation is needed only once.



    
    
    http_auth = [os.environ['OPENSEARCH_USERNAME'], os.environ['OPENSEARCH_PASSWORD']]
    client = OpenSearch(hosts = ['https://localhost:9200'],
                        http_auth = http_auth,
                        verify_certs = False
                        )
    
    index_name = 'embeddings-index'
    
    index_body = {
      "settings": {
          "index.knn": True
       },
       "mappings": {
          "properties": {
             "title_vector": {
                "type": "knn_vector",
                "dimension": 384,
                "method": {
                   "engine": "faiss",
                   "name": "hnsw"
                }
             },
             "text_vector": {
                "type": "knn_vector",
                "dimension": 384,
                "method": {
                   "engine": "faiss",
                   "name": "hnsw"
                }
             },
             "id": {
                "type": "long"
             },
             "url": {
                "type": "text"
             },
             "title": {
                "type": "text"
             },
             "text": {
                "type": "text"
             },
             "section_id": {
                "type": "long"
             }
        }
    } }
    
    response = client.indices.create(index_name, body=index_body)
    
    # Command for deleting an index
    # response = client.indices.delete(index = index_name)
    
    
    
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:PUT https://localhost:9200/embeddings-index [status:200 request:0.351s]
    

# Creating Knowledge Base in OpenSearch Vector Database¶

After creating a search index, we can load documents into it. We will use the same documents we used in the previous cell. 
    
    
    #Insertion Pipeline
    import os
    
    artifact_location = tempfile.mkdtemp()
    generate_embedding_fn = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2',
                                                                   columns=['title','text'])
    with beam.Pipeline() as p:
        embeddings = (
            p  
            | "Read data" >> beam.Create(contents)
            | "Generate text chunks" >> ChunksGeneration(chunk_size = 500, chunk_overlap = 0, chunking_strategy = ChunkingStrategy.SPLIT_BY_TOKENS)
            | "Insert document in openSearch" >> InsertDocInOpenSearch(host='https://localhost', username=os.environ['OPENSEARCH_USERNAME'], password=os.environ['OPENSEARCH_PASSWORD'], port=9200, batch_size = 10)
            | "Generate Embeddings" >> MLTransform(write_artifact_location=artifact_location).with_transform(generate_embedding_fn) 
            | "Insert Embedding in openSearch" >> InsertEmbeddingInOpenSearch(host='https://localhost', username=os.environ['OPENSEARCH_USERNAME'], password=os.environ['OPENSEARCH_PASSWORD'], port=9200, batch_size = 10, embedded_columns=['title','text'])
        )
    
    
    
    INFO:root:Missing pipeline option (runner). Executing pipeline using the default runner: DirectRunner.
    WARNING:apache_beam.runners.interactive.interactive_environment:Dependencies required for Interactive Beam PCollection visualization are not available, please use: `pip install apache-beam[interactive]` to install necessary dependencies to enable all data visualization features.
    WARNING:root:This output type hint will be ignored and not used for type-checking purposes. Typically, output type hints for a PTransform are single (or nested) types wrapped by a PCollection, PDone, or None. Got: Union[Tuple[apache_beam.pvalue.PCollection[~MLTransformOutputT], apache_beam.pvalue.PCollection[apache_beam.pvalue.Row]], apache_beam.pvalue.PCollection[~MLTransformOutputT]] instead.
    WARNING:root:This output type hint will be ignored and not used for type-checking purposes. Typically, output type hints for a PTransform are single (or nested) types wrapped by a PCollection, PDone, or None. Got: Union[Tuple[apache_beam.pvalue.PCollection[~MLTransformOutputT], apache_beam.pvalue.PCollection[apache_beam.pvalue.Row]], apache_beam.pvalue.PCollection[~MLTransformOutputT]] instead.
    WARNING:root:This output type hint will be ignored and not used for type-checking purposes. Typically, output type hints for a PTransform are single (or nested) types wrapped by a PCollection, PDone, or None. Got: Union[Tuple[apache_beam.pvalue.PCollection[~MLTransformOutputT], apache_beam.pvalue.PCollection[apache_beam.pvalue.Row]], apache_beam.pvalue.PCollection[~MLTransformOutputT]] instead.
    WARNING:root:This output type hint will be ignored and not used for type-checking purposes. Typically, output type hints for a PTransform are single (or nested) types wrapped by a PCollection, PDone, or None. Got: Union[Tuple[apache_beam.pvalue.PCollection[~MLTransformOutputT], apache_beam.pvalue.PCollection[apache_beam.pvalue.Row]], apache_beam.pvalue.PCollection[~MLTransformOutputT]] instead.
    INFO:apache_beam.runners.worker.statecache:Creating state cache with size 104857600
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    2024-08-17 12:28:49.961311: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
    To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    /usr/local/lib/python3.10/site-packages/opensearchpy/connection/http_urllib3.py:208: UserWarning: Connecting to https://localhost:9200 using SSL with verify_certs=False is insecure.
      warnings.warn(
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:1.352s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.071s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.070s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.065s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.073s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.059s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.088s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.091s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.098s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.078s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.103s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.079s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.084s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.093s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.075s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.076s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.079s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.165s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.089s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.088s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.077s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.060s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.067s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.067s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.082s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.054s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.063s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.057s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.066s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.057s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.070s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.086s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.064s]
    INFO:opensearch_connector:Adding Docs in DB: 10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.083s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:opensearch_connector:Adding Docs in DB: 9
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk?refresh=true [status:200 request:0.066s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:root:BatchElements statistics: element_count=349 batch_count=27 next_batch_size=4 timings=[(1, 0.18766427040100098), (2, 0.5434770584106445), (1, 0.18743109703063965), (2, 0.28671717643737793), (1, 0.180436372756958), (2, 0.2946739196777344), (1, 0.23954296112060547), (2, 0.2287900447845459), (4, 0.6388511657714844), (6, 0.7156858444213867), (7, 0.8332958221435547), (13, 1.1533119678497314), (12, 1.2309019565582275), (14, 1.1411330699920654), (19, 1.4424619674682617), (19, 1.1780219078063965), (24, 1.7884211540222168), (19, 1.191762924194336), (26, 1.8830091953277588), (32, 2.3361740112304688), (29, 1.9658150672912598), (26, 1.5100517272949219), (26, 1.811798095703125), (32, 2.051542043685913), (26, 1.5136959552764893), (2, 0.44672513008117676)]
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.075s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.087s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.084s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.083s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.076s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.071s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.067s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.074s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.082s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.085s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.071s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.082s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.071s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.067s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.068s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.065s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.068s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.076s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.069s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.062s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.079s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.071s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.065s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.089s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.088s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.072s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.083s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.074s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.066s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.087s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.091s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.096s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.111s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=10
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.149s]
    INFO:opensearch_connector:Insert Embeddings done
    INFO:opensearch_connector:Insert Embeddings in opensearch DB, count=9
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/_bulk [status:200 request:0.155s]
    INFO:opensearch_connector:Insert Embeddings done
    

### Pipeline Steps:

Now that we have ingested the documents in OpenSearch, we will create a embeddings transform, which is used for storing the text and its embedding in openSearch vector db

# Running Search Queries/ Perform Enrichment

### Pipeline Steps:

Create a search transform, which emits the document Id, vector score along with the matching text from knowledge base
    
    
    # Enchriment Pipeline
    
    data = [{'text':'What is climate ?'}]
    
    artifact_location = tempfile.mkdtemp()
    generate_embedding_fn = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2',
                                                                    columns=['text'])
    
    opensearch_handler = OpenSearchEnrichmentHandler(opensearch_host='https://localhost', 
                                                     opensearch_port=9200, 
                                                     username=os.environ['OPENSEARCH_USERNAME'], 
                                                     password=os.environ['OPENSEARCH_PASSWORD'])
    
    
    with beam.Pipeline() as p:
      _ = (
          p
          | "Create" >> beam.Create(data)
          | "Generate Embedding" >> MLTransform(write_artifact_location=artifact_location).with_transform(generate_embedding_fn)
          | "Enrich W/ OpenSearch" >> Enrichment(opensearch_handler)
          | "Print" >> beam.Map(print)
      )
    
    
    
    INFO:root:Missing pipeline option (runner). Executing pipeline using the default runner: DirectRunner.
    WARNING:root:This output type hint will be ignored and not used for type-checking purposes. Typically, output type hints for a PTransform are single (or nested) types wrapped by a PCollection, PDone, or None. Got: Union[Tuple[apache_beam.pvalue.PCollection[~MLTransformOutputT], apache_beam.pvalue.PCollection[apache_beam.pvalue.Row]], apache_beam.pvalue.PCollection[~MLTransformOutputT]] instead.
    WARNING:root:This output type hint will be ignored and not used for type-checking purposes. Typically, output type hints for a PTransform are single (or nested) types wrapped by a PCollection, PDone, or None. Got: Union[Tuple[apache_beam.pvalue.PCollection[~MLTransformOutputT], apache_beam.pvalue.PCollection[apache_beam.pvalue.Row]], apache_beam.pvalue.PCollection[~MLTransformOutputT]] instead.
    WARNING:root:This output type hint will be ignored and not used for type-checking purposes. Typically, output type hints for a PTransform are single (or nested) types wrapped by a PCollection, PDone, or None. Got: Union[Tuple[apache_beam.pvalue.PCollection[~MLTransformOutputT], apache_beam.pvalue.PCollection[apache_beam.pvalue.Row]], apache_beam.pvalue.PCollection[~MLTransformOutputT]] instead.
    WARNING:root:This output type hint will be ignored and not used for type-checking purposes. Typically, output type hints for a PTransform are single (or nested) types wrapped by a PCollection, PDone, or None. Got: Union[Tuple[apache_beam.pvalue.PCollection[~MLTransformOutputT], apache_beam.pvalue.PCollection[apache_beam.pvalue.Row]], apache_beam.pvalue.PCollection[~MLTransformOutputT]] instead.
    INFO:apache_beam.runners.worker.statecache:Creating state cache with size 104857600
    INFO:sentence_transformers.SentenceTransformer:Load pretrained SentenceTransformer: all-MiniLM-L6-v2
    INFO:sentence_transformers.SentenceTransformer:Use pytorch device_name: mps
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    /usr/local/lib/python3.10/site-packages/urllib3/connectionpool.py:1095: InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
      warnings.warn(
    INFO:opensearch:POST https://localhost:9200/embeddings-index/_search [status:200 request:0.315s]
    INFO:opensearch_enrichment:Enrichment_results
    INFO:root:BatchElements statistics: element_count=1 batch_count=1 next_batch_size=1 timings=[]
    Row(text=[...], docs={'took': 268, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 0.49309593, 'hits': [{'_index': 'embeddings-index', '_id': '39', '_score': 0.49309593, '_source': {'url': 'https://en.wikipedia.org/wiki/Albedo', 'title': 'Albedo', 'text': 'climate forcing climatology electromagnetic radiation meteorological quantities radiometry scattering, absorption and radiative transfer ( optics ) radiation 1760s neologisms', 'section_id': 21, 'text_vector': [...]} }]} })
    

# Conclusion

Here we have demonstrated how we can implement Ingestion and Enrichment pipeline using OpenSearch vector DB by using ML Transfrom's SentenceTransformerEmbeddings for generating the embeddings of the text chunks.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
