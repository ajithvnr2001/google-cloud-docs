---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/beam_rag_notebook/
title: For now Reading json data locally \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:50:52.629315+00:00
---

# For now Reading json data locally  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/beam_rag_notebook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  For now Reading json data locally Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    #installing dependencies
    pip install pandas==1.4.4
    pip install numpy==1.24.4
    pip install apache_beam[interactive]==2.56.0
    pip install redis==5.0.1
    pip install langchain==0.1.14 #used for chunking
    
    
    #Imports Required for the notebook
    import pandas as pd
    import numpy as np
    import apache_beam as beam
    from apache_beam.ml.transforms.base import MLTransform
    from apache_beam.transforms.enrichment import Enrichment
    from apache_beam.ml.transforms.embeddings.huggingface import SentenceTransformerEmbeddings
    import tempfile
    import redis
    import redis_connector
    import redis_enrichment
    from redis_connector import *
    from redis_enrichment import *
    from redis.commands.search.indexDefinition import (IndexDefinition,IndexType)
    from redis.commands.search.query import Query
    from redis.commands.search.field import (TextField,VectorField)
    from chunks_generation import *
    
    
    
    #To check beam version installed 
    beam.__version__
    
    
    
    '2.56.0'
    
    
    
    import json
    
    with open('hf_small_wikipedia.json', 'r') as j:
         contents = json.loads(j.read())
    
    
    
    import json
    
    with open('hf_small_wikipedia.json', 'r') as j:
         contents = json.loads(j.read())
    
    
    print(contents[:1])
    
    
    
    [{'id': '12', 'url': 'https://en.wikipedia.org/wiki/Anarchism', 'title': 'Anarchism', 'text': 'Anarchism is a political philosophy and movement that is skeptical of all  ... \nSocial theories\nSocialism'}]
    
    
    
    type(contents)
    
    
    
    list
    

# Create Redis Client for connecting to Redis Vector Database
    
    
    REDIS_HOST =  "localhost"
    REDIS_PORT = 6379
    REDIS_PASSWORD = "" # default for passwordless Redis
    
    # Connect to Redis
    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD
    )
    redis_client.ping()
    
    
    
    True
    

# Creating a Search Index

Below cells will show how to specify and create a search index in Redis vector DB. Below are the following steps:

1) Set some constants for defining our index like the distance metric and the index name 2) Define the index schema with RediSearch fields 3) Create the index
    
    
    #Constants
    EMBEDDING_MODEL = 'all-MiniLM-L6-v2' # Embedding model name to be use with ML Transform
    VECTOR_DIM = 384                     # length of the vector for above embedding model
    VECTOR_NUMBER = 2                    # initial number of vectors
    INDEX_NAME = "embeddings-index"      # name of the search index      
    PREFIX = "doc"                       # prefix for the document keys           
    DISTANCE_METRIC = "COSINE"           # distance metric for the vectors (ex. COSINE, IP, L2)
    
    
    
    # Define RediSearch fields for each of the columns in the dataset
    url = TextField(name="url")
    title = TextField(name="title")
    title_embedding = VectorField("title_vector",
        "FLAT", {
            "TYPE": "FLOAT32",
            "DIM": VECTOR_DIM,
            "DISTANCE_METRIC": DISTANCE_METRIC,
            "INITIAL_CAP": VECTOR_NUMBER,
        }
    )
    
    text = TextField(name="text")
    text_embedding = VectorField("text_vector",
        "FLAT", {
            "TYPE": "FLOAT32",
            "DIM": VECTOR_DIM,
            "DISTANCE_METRIC": DISTANCE_METRIC,
            "INITIAL_CAP": VECTOR_NUMBER,
        }
    )
    fields = [url, title, title_embedding, text, text_embedding]
    
    
    
    # Check if index exists
    try:
        redis_client.ft(INDEX_NAME).info()
        print("Index already exists")
    except:
        # Create RediSearch Index
        redis_client.ft(INDEX_NAME).create_index(
            fields = fields,
            definition = IndexDefinition(prefix=[PREFIX], index_type=IndexType.HASH)
    )
    
    
    
    Index already exists
    

# Creating Knowledge Base in Redis Vector Database

After creating a search index, we can load documents into it. We will use the same documents we used in the previous cell.
    
    
    #Insertion Pipeline
    
    artifact_location = tempfile.mkdtemp()
    generate_embedding_fn = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2',
                                                                   columns=['title','text'])
    with beam.Pipeline() as p:
        embeddings = (
            p  
            | "Read data" >> beam.Create(contents) 
            | "Generate text chunks" >> ChunksGeneration(chunk_size = 500, chunk_overlap = 0, chunking_strategy = ChunkingStrategy.SPLIT_BY_TOKENS)
            | "Insert document in Redis" >> InsertDocInRedis(host='127.0.0.1',port=6379, batch_size=10)
            | "Generate Embeddings" >> MLTransform(write_artifact_location=artifact_location).with_transform(generate_embedding_fn) 
            | "Insert Embedding in Redis" >> InsertEmbeddingInRedis(host='127.0.0.1',port=6379, batch_size=10,embedded_columns=['title','text'])
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
    2024-08-09 13:01:57.330902: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
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
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:redis_connector:Inserting documents in Redis. Total docs: 10
    INFO:redis_connector:Inserting documents complete.
    INFO:redis_connector:Inserting documents in Redis. Total docs: 9
    INFO:redis_connector:Inserting documents complete.
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    Batches:   0%|          | 0/1 [00:00<?, ?it/s]
    INFO:root:BatchElements statistics: element_count=349 batch_count=35 next_batch_size=20 timings=[(1, 0.14947915077209473), (2, 0.4767780303955078), (1, 0.1831817626953125), (2, 0.2000288963317871), (1, 0.14716172218322754), (2, 0.19555902481079102), (4, 0.568000078201294), (3, 0.49921202659606934), (1, 0.15181899070739746), (2, 0.2397456169128418), (2, 0.19758391380310059), (3, 0.259962797164917), (6, 0.6725080013275146), (7, 0.7242469787597656), (7, 0.6019473075866699), (7, 0.47342967987060547), (10, 0.9236979484558105), (13, 1.1121737957000732), (14, 1.130352258682251), (12, 0.9904649257659912), (19, 1.336167812347412), (13, 0.8261549472808838), (15, 1.156790018081665), (17, 1.272038221359253), (15, 1.0295050144195557), (14, 0.973175048828125), (16, 1.2297940254211426), (15, 0.8902089595794678), (23, 1.609447956085205), (19, 1.1090152263641357), (22, 1.5956041812896729), (18, 1.3837130069732666), (25, 1.715193748474121), (17, 1.1607699394226074)]
    

## Pipeline Steps:

Now that we have ingested the documents in Redis, we will create a embeddings transform, which is used for storing the text and its embedding in redis vector db

# Running Search Queries/ Perform Enrichment

## Pipeline Steps:

Create a search transform, which emits the document Id, vector score along with the matching text from knowledge base
    
    
    #  Enchriment Pipeline 
    
    
    data = [{'text':'What is Anarchy ?'}]
    
    artifact_location = tempfile.mkdtemp()
    generate_embedding_fn = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2',
                                                                     columns=['text'])
    
    redis_handler = RedisEnrichmentHandler(redis_host='127.0.0.1', redis_port=6379)
    
    
    with beam.Pipeline() as p:
      _ = (
          p
          | "Create" >> beam.Create(data)
          | "Generate Embedding" >> MLTransform(write_artifact_location=artifact_location).with_transform(generate_embedding_fn)
          | "Enrich W/ Redis" >> Enrichment(redis_handler)
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
    INFO:root:BatchElements statistics: element_count=1 batch_count=1 next_batch_size=1 timings=[]
    Row(text=[0.004666077438741922, 0.05869913473725319, -0.07399024069309235, 0.022393187507987022, 0.039686284959316254, -0.034507881850004196, 0.064857617020607, -0.047807302325963974, -0.03489216789603233, 0.06350446492433548, 0.0360037162899971, 0.03880435600876808, 0.0589592307806015, -0.0789710283279419, -0.032882459461688995, -0.045789338648319244, -0.021030493080615997, -0.05721370130777359, -0.01570642925798893, 0.06773950159549713, 0.0477975532412529, 0.02080758847296238, -0.07664106041193008, 0.04821384325623512, -0.052367933094501495, 0.07436149567365646, -0.024946363642811775, -0.03843500837683678, -0.05065334215760231, -0.008651865646243095, 0.016191929578781128, -0.05380123108625412, 0.04309113323688507, 0.0409851111471653, -0.01066699717193842, 0.021276379004120827, 0.06583339720964432, -0.05280669033527374, -0.01774919219315052, -0.061985645443201065, -0.02252737060189247, -0.012123598717153072, -0.011422254145145416, -0.029680127277970314, -0.05887051299214363, 0.0390109047293663, -0.007984216324985027, -0.05453580990433693, 0.004903809633105993, -0.06199903041124344, 0.006124422885477543, -0.02969948574900627, -0.027403226122260094, 0.059209130704402924, 0.019371695816516876, 0.029584478586912155, 0.03337220102548599, 0.000216050204471685, -0.038550231605768204, -0.1277540922164917, 0.11660053580999374, 0.005125461611896753, -0.062354106456041336, 0.06569217145442963, 0.12326736748218536, 0.01854224130511284, 0.01594136282801628, 0.032180577516555786, -0.011718189343810081, -0.047588005661964417, -0.029363591223955154, -0.09647595137357712, 0.048424072563648224, 0.034841254353523254, 0.0022684866562485695, -0.06725143641233444, 0.0011366262333467603, -0.020027248188853264, 0.006062033120542765, 0.015627486631274223, -0.0924009308218956, 0.07149998098611832, -0.05066332593560219, -0.046360649168491364, 0.013088884763419628, -0.03764544427394867, -0.023997198790311813, -0.003329708008095622, 0.10378119349479675, -0.011796935461461544, -0.037390902638435364, 0.06075884774327278, 0.03466855362057686, -0.0025003429036587477, -0.04471913352608681, 0.05830719694495201, 0.022835878655314445, 0.005220250226557255, -0.02225373685359955, 0.1170453280210495, -0.02088114246726036, 0.006051725707948208, -0.012271308340132236, -0.011464528739452362, -0.03261090815067291, -0.03229975327849388, -0.03807772696018219, -0.02704131416976452, -0.01243546511977911, -0.018037425354123116, -0.08699967712163925, 0.01640823669731617, 0.0333375483751297, 0.03401600569486618, 0.08737698197364807, 0.02666822448372841, 0.07001851499080658, -0.011303948238492012, -0.014235888607800007, 0.029571382328867912, 0.051306724548339844, -0.03789466992020607, -0.012402428314089775, 0.04955461621284485, 0.04979461431503296, 0.04865849018096924, -0.08606445789337158, -7.48271067654703e-33, -0.06290460377931595, -0.06735390424728394, 0.03379411622881889, 0.03793416544795036, 0.001887491554953158, 0.008819608949124813, -0.04555787146091461, -0.04757940396666527, 0.02495495229959488, 0.110148124396801, 0.023693304508924484, -2.0244651750545017e-05, 0.08616331219673157, -0.042689669877290726, 0.05224208906292915, -0.016693517565727234, -0.06554078310728073, 0.0528477281332016, 0.06257053464651108, 0.019625652581453323, -0.048396799713373184, 0.1296025514602661, 0.008417169563472271, -0.046129945665597916, -0.012217260897159576, 0.015625368803739548, -0.025218265131115913, -0.03641138970851898, 0.04740137979388237, 0.01555641833692789, 0.08771637082099915, 0.13161638379096985, -0.07359347492456436, -0.0018345718272030354, -0.03810210898518562, 0.000992951332591474, 0.011857913807034492, -0.05040539801120758, 0.036811888217926025, -0.08308660984039307, -0.06461762636899948, -0.034412797540426254, 0.023122554644942284, -0.0027934794779866934, 0.014656861312687397, 0.06785327196121216, 0.038474131375551224, 0.0172354057431221, -0.0594635084271431, -0.03704370558261871, 0.03840631619095802, -0.09339816868305206, 0.07145838439464569, -0.013790507800877094, -0.04922572523355484, -0.05025532469153404, -0.07166589796543121, 0.047785788774490356, -0.00871171336621046, 0.00961771234869957, 0.06259235739707947, -0.05327753722667694, 0.035217367112636566, 0.02551940083503723, 0.02714036963880062, -0.05368731543421745, -0.004992792382836342, 0.04293801262974739, 0.0696093738079071, 0.0355013832449913, -0.0037727756425738335, -0.0014957308303564787, -0.053488053381443024, 0.15978889167308807, 0.0061986190266907215, -0.010946657508611679, 0.08086379617452621, -0.01744343340396881, -0.10256429016590118, 0.060528095811605453, -0.12491439282894135, -0.02091016247868538, 0.035100989043712616, -0.03428236395120621, 0.032945405691862106, 0.006501795724034309, -0.05623633414506912, -7.247104804264382e-05, 0.06887488812208176, -0.028165919706225395, -0.05296119675040245, -0.0521245114505291, 0.0020046995487064123, 0.039513569325208664, -0.058962032198905945, 3.9188645361392806e-33, -0.016041874885559082, -0.09901542216539383, -0.11019805818796158, 0.028895391151309013, 0.06076628342270851, 0.04387689754366875, -0.0607643760740757, 0.029573094099760056, -0.08418785780668259, -0.06700398027896881, -0.0038920093793421984, -0.03733440116047859, 0.06021302565932274, 0.07674328237771988, 0.12819066643714905, -0.05707727372646332, 0.07890237867832184, -0.07170261442661285, 0.005376893561333418, 0.04370340704917908, -0.030689824372529984, -0.005202469881623983, -0.05956199765205383, -0.005707382690161467, -0.0030950375366955996, 0.010882874950766563, -0.06622341275215149, 0.013915101066231728, -0.04128726199269295, 0.030529843643307686, 0.026121536269783974, 0.015823667868971825, -0.022394195199012756, -0.017022009938955307, -0.0017925086431205273, 0.07489118725061417, -0.009440217167139053, -0.052385471761226654, 0.02417312189936638, 0.002648930763825774, -0.06126844510436058, -0.04241601377725601, 0.025891954079270363, 0.0632123276591301, -0.051637470722198486, 0.029158173128962517, 0.07598704099655151, 0.018526427447795868, -0.09949029982089996, 0.011564004234969616, 0.04594141244888306, 0.003376895794644952, 0.05097722262144089, -0.03941746801137924, 0.0001736470585456118, -0.040061403065919876, -0.07590603828430176, 0.016973042860627174, -0.028994012624025345, 0.08828837424516678, -0.0024176640436053276, 0.06853476911783218, -0.09440020471811295, 0.07837890833616257, -0.042359255254268646, -0.015529068186879158, -0.07989171892404556, -0.10349376499652863, 0.017352605238556862, 0.027474619448184967, 0.03889119252562523, -0.03486671298742294, -0.07837577909231186, 0.09446392208337784, 0.03137386962771416, 0.009404155425727367, 0.058410923928022385, 0.014444328844547272, -0.01881902851164341, -0.04984214901924133, -0.056680843234062195, 0.0035722495522350073, 0.00012525652709882706, -0.000638884783256799, -0.024240082129836082, -0.019495511427521706, 0.011342530138790607, 0.01606130413711071, 0.011781197972595692, -0.010379692539572716, -0.012258544564247131, -0.06899338960647583, -0.01737949252128601, 0.03971114754676819, -0.028151415288448334, -1.4196542608146956e-08, 0.05519683659076691, 0.0032584595028311014, 0.12491472065448761, -0.01476595364511013, -0.021644294261932373, 0.08167381584644318, 0.10918232053518295, -0.03663909062743187, -0.049210142344236374, -0.0015691033331677318, -0.01405260618776083, 0.03538493439555168, 0.04648015275597572, -0.014656341634690762, -0.06434938311576843, 0.009127220138907433, 0.04072323068976402, 0.06892682611942291, -0.08311998099088669, 0.031564366072416306, 0.07844635099172592, -0.019379964098334312, -0.01581992767751217, -0.03225895017385483, 0.048312392085790634, 0.004448889289051294, 0.02831929363310337, 0.029994582757353783, 0.00010915406164713204, -0.00044170342152938247, 0.044296737760305405, 0.006084990222007036, -0.02064436301589012, -0.003432636382058263, -0.10695135593414307, 0.12328752130270004, 0.004867409821599722, -0.04044206812977791, 0.049144402146339417, -0.1185329332947731, -0.05621146038174629, 0.08382154256105423, 0.035927340388298035, -0.026798876002430916, -0.008891892619431019, 0.01957395300269127, -0.07074403017759323, -0.0033123537432402372, 0.059811096638441086, -0.07722742110490799, -0.012372042052447796, 0.04984291270375252, 0.026960525661706924, -0.016759676858782768, 0.008442522957921028, -0.12283991277217865, 0.029091667383909225, 0.05893566831946373, -0.02916647493839264, 0.03887897729873657, 0.07376956939697266, -0.022076599299907684, 0.05269448831677437, -0.04350380226969719], docs=[Document {'id': 'doc_12_section_31', 'payload': None, 'title': 'Anarchism', 'url': 'https://en.wikipedia.org/wiki/Anarchism', 'text': ', among others, are functions which could hardly be performed in a community in which there was no central government. " another common criticism of anarchism is that it fits a world of isolation in which only the small enough entities can be self - governing ; a response would be that major anarchist thinkers advocated anarchist federalism. another criticism of anarchism is the belief that it is inherently unstable : that an anarchist society would inevitably evolve back into a state. thomas hobbes and other early social contract theorists argued that the state emerges in response to natural anarchy in order to protect the people\'s interests and keep order. philosopher robert nozick argued that a " night - watchman state ", or minarchy, would emerge from anarchy through the process of an invisible hand, in which people would exercise their liberty and buy protection from protection agencies, evolving into a minimal state. anarchists reject these criticisms by arguing that humans in a state of nature would not just be in a state of war. anarcho - primitivists in particular argue that humans were better off in a state of nature in small tribes living close to the land, while anarchists in general argue that the negatives of state organization, such as hierarchies, monopolies and inequality'}, Document {'id': 'doc_12_section_34', 'payload': None, 'title': 'Anarchism', 'url': 'https://en.wikipedia.org/wiki/Anarchism', 'text': 'a revolution is by itself authoritarian. academic john molyneux writes in his book anarchism : a marxist criticism that " anarchism cannot win ", believing that it lacks the ability to properly implement its ideas. the marxist criticism of anarchism is that it has a utopian character because all individuals should have anarchist views and values. according to the marxist view, that a social idea would follow directly from this human ideal and out of the free will of every individual formed its essence. marxists state that this contradiction was responsible for their inability to act. in the anarchist vision, the conflict between liberty and equality was resolved through coexistence and intertwining. see also anarchism by country governance without government list of anarchist political ideologies list of books about anarchism references explanatory notes citations general and cited sources primary sources secondary sources tertiary sources further reading criticism of philosophical anarchism. a defence of philosophical anarchism, stating that " both kinds of\'anarchism\'[ i. e. philosophical and political anarchism ] are philosophical and political claims. " ( p. 137 ) anarchistic popular fiction novel. an argument for philosophical anarchism. external links anarchy archives – an online research center on the history'}])
    

# Conclusion

Here we have demonstrated how we can implement Ingestion and Enrichment pipeline using redis vector DB by using ML Transfrom's SentenceTransformerEmbeddings for generating the embeddings of the text chunks.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
