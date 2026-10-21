---
url: https://docs.cloud.google.com/alloydb/docs/ai/migrate-data-from-langchain-vector-stores-to-alloydb/
title: Migrate data from a vector database to AlloyDB \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:00.316918+00:00
---

# Migrate data from a vector database to AlloyDB  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/migrate-data-from-langchain-vector-stores-to-alloydb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Migrate data from a vector database to AlloyDB Stay organized with collections  Save and categorize content based on your preferences. 

You can migrate vector embeddings and metadata from third-party vector databases to AlloyDB for PostgreSQL by using a [LangChain](https://www.langchain.com/) `VectorStore` integration. In this tutorial, you export existing vector data generated with LangChain and load it into an `AlloyDBVectorStore` table. If you ingested data into one of the following databases without using LangChain, modify the provided migration scripts to match your data schema. The following vector databases are supported:

  * [Pinecone](https://python.langchain.com/docs/integrations/vectorstores/pinecone/)
  * [Weaviate](https://python.langchain.com/docs/integrations/vectorstores/weaviate/)
  * [Chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma/)
  * [Qdrant](https://python.langchain.com/docs/integrations/vectorstores/qdrant/)
  * [Milvus](https://python.langchain.com/docs/integrations/vectorstores/milvus/)

**Note:** This tutorial uses default values from the supported LangChain vector stores. To migrate custom databases, you might need to update the data fields specified in this document.

This tutorial assumes that you're familiar with Google Cloud, AlloyDB, and asynchronous Python programming.

## Objectives

This tutorial shows you how to do the following:

  * Extract data from an existing vector database.
  * Connect to AlloyDB.
  * Initialize the AlloyDB table.
  * Initialize a vector store object.
  * Run the migration script to insert the data.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ AlloyDB for PostgreSQL](https://cloud.google.com/alloydb/pricing)



You might be eligible for a free trial cluster. For more information, see [AlloyDB free trial clusters overview](https://docs.cloud.google.com/alloydb/docs/free-trial-cluster).

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Make sure that you have one of the following LangChain third-party database vector stores:

  * [Pinecone](https://python.langchain.com/docs/integrations/vectorstores/pinecone/)
  * [Weaviate](https://python.langchain.com/docs/integrations/vectorstores/weaviate/)
  * [Chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma/)
  * [Qdrant](https://python.langchain.com/docs/integrations/vectorstores/qdrant/)
  * [Milvus](https://python.langchain.com/docs/integrations/vectorstores/milvus/)



### Enable billing and required APIs

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Note:** If you don't plan to keep the resources that you create in this tutorial, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

  3. Enable the Cloud APIs necessary to create and connect to AlloyDB for PostgreSQL.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,servicenetworking.googleapis.com,aiplatform.googleapis.com)

     1. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.
     2. In the **Enable APIs** step, click **Enable** to enable the following:

        * AlloyDB API
        * Compute Engine API
        * Service Networking API



### Required roles

To get the permissions that you need to complete the tasks in this tutorial, have the following Identity and Access Management (IAM) roles which allow for table creation and data insertion:

  * Owner (`roles/owner`) or Editor (`roles/editor`)
  * If the user is not an owner or editor, the following IAM roles and PostgreSQL privileges are required:

    * AlloyDB Instance Client ([`roles/alloydb.client`](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles))
    * Cloud AlloyDB Admin ([`roles/alloydb.admin`](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles))
    * Compute Network User ([`roles/compute.networkUser`](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser))



If you want to authenticate to your database using IAM authentication instead of using the built-in authentication in this tutorial, use the notebook that shows how to [use AlloyDB for PostgreSQL to store vector embeddings with the `AlloyDBVectorStore` class](https://github.com/googleapis/langchain-google-alloydb-pg-python/blob/main/docs/vector_store.ipynb).

## Create an AlloyDB cluster and user

  1. [Create an AlloyDB cluster and an instance](https://docs.cloud.google.com/alloydb/docs/cluster-create). 
     * Enable Public IP to run this tutorial from anywhere. If you're using Private IP, you must run this tutorial from within your VPC.
  2. [Create or select an AlloyDB database user](https://docs.cloud.google.com/alloydb/docs/database-users/about). 
     * When you create the instance, a `postgres` user is created with a password. This user has superuser permissions.
     * This tutorial uses built-in authentication to reduce any authentication friction. IAM authentication is possible using the [AlloyDBEngine](https://docs.cloud.google.com/python/docs/reference/langchain-google-alloydb-pg/latest/langchain_google_alloydb_pg.engine.AlloyDBEngine).



## Retrieve the code sample

  1. Copy the code sample from GitHub by cloning the repository:
         
         git clone https://github.com/googleapis/langchain-google-alloydb-pg-python.git

  2. Navigate to the `migrations` directory:
         
         cd langchain-google-alloydb-pg-python/samples/migrations




## Extract data from an existing vector database

**Note:** You might need to modify the code examples in this section based on your use case.

  1. Create a client.

### Pinecone
         
         from pinecone import Pinecone  # type: ignore
         
         pinecone_client = Pinecone(api_key=pinecone_api_key)
         pinecone_index = pinecone_client.Index(pinecone_index_name)

### Weaviate
         
         import weaviate
         
         # For a locally running weaviate instance, use `weaviate.connect_to_local()`
         weaviate_client = weaviate.connect_to_weaviate_cloud(
             cluster_url=weaviate_cluster_url,
             auth_credentials=weaviate.auth.AuthApiKey(weaviate_api_key),
         )

### Chroma
         
         from langchain_chroma import Chroma
         
         chromadb_client = Chroma(
             collection_name=chromadb_collection_name,
             embedding_function=embeddings_service,
             persist_directory=chromadb_path,
         )

### Qdrant
         
         from qdrant_client import QdrantClient
         
         qdrant_client = QdrantClient(path=qdrant_path)
         

### Milvus
         
         milvus_client = MilvusClient(uri=milvus_uri)

  2. Get all the data from the database.

### Pinecone

Retrieve vector IDs from the Pinecone index:
         
         results = pinecone_index.list_paginated(
             prefix="", namespace=pinecone_namespace, limit=pinecone_batch_size
         )
         ids = [v.id for v in results.vectors]
         if ids:  # Prevents yielding an empty list.
             yield ids
         
         # Check BOTH pagination and pagination.next
         while results.pagination is not None and results.pagination.get("next") is not None:
             pagination_token = results.pagination.get("next")
             results = pinecone_index.list_paginated(
                 prefix="",
                 pagination_token=pagination_token,
                 namespace=pinecone_namespace,
                 limit=pinecone_batch_size,
             )
         
             # Extract and yield the next batch of IDs
             ids = [v.id for v in results.vectors]
             if ids:  # Prevents yielding an empty list.
                 yield ids

And then fetch records by ID from the Pinecone index:
         
         import uuid
         
         # Iterate through the IDs and download their contents
         for ids_batch in id_iterator:
             all_data = pinecone_index.fetch(ids=ids_batch, namespace=pinecone_namespace)
             ids = []
             embeddings = []
             contents = []
             metadatas = []
         
             # Process each vector in the current batch
             for doc in all_data.vectors.values():
                 # You might need to update this data translation logic according to one or more of your field names
                 if pinecone_id_column_name in doc.metadata:
                     # pinecone_id_column_name stores the unqiue identifier for the content
                     ids.append(doc[pinecone_id_column_name])
                 else:
                     # Generate a uuid if pinecone_id_column_name is missing in source
                     ids.append(str(uuid.uuid4()))
                 # values is the vector embedding of the content
                 embeddings.append(doc.values)
                 # Check if pinecone_content_column_name exists in metadata before accessing
                 if pinecone_content_column_name in doc.metadata:
                     # pinecone_content_column_name stores the content which was encoded
                     contents.append(str(doc.metadata[pinecone_content_column_name]))
                     # Remove pinecone_content_column_name after processing
                     del doc.metadata[pinecone_content_column_name]
                 else:
                     # Handle the missing pinecone_content_column_name field appropriately
                     contents.append("")
                 # metadata is the additional context
                 metadatas.append(doc.metadata)
         
             # Yield the current batch of results
             yield ids, contents, embeddings, metadatas

### Weaviate
         
         # Iterate through the IDs and download their contents
         weaviate_collection = weaviate_client.collections.get(weaviate_collection_name)
         ids: list[str] = []
         content: list[Any] = []
         embeddings: list[list[float]] = []
         metadatas: list[Any] = []
         
         for item in weaviate_collection.iterator(include_vector=True):
             # You might need to update this data translation logic according to one or more of your field names
             # uuid is the unqiue identifier for the content
             ids.append(str(item.uuid))
             # weaviate_text_key is the content which was encoded
             content.append(item.properties[weaviate_text_key])
             # vector is the vector embedding of the content
             embeddings.append(item.vector["default"])  # type: ignore
             del item.properties[weaviate_text_key]  # type: ignore
             # properties is the additional context
             metadatas.append(item.properties)
         
             if len(ids) >= weaviate_batch_size:
                 # Yield the current batch of results
                 yield ids, content, embeddings, metadatas
                 # Reset lists to start a new batch
                 ids = []
                 content = []
                 embeddings = []
                 metadatas = []

**Note:** Update `WEAVIATE_COLLECTION_NAME` with the collection name and update `WEAVIATE_TEXT_KEY` with the field name in the Weaviate schema containing text content. If you have multiple collections, run the migration for each collection.

### Chroma
         
         # Iterate through the IDs and download their contents
         offset = 0
         while True:
             # You might need to update this data translation logic according to one or more of your field names
             # documents is the content which was encoded
             # embeddings is the vector embedding of the content
             # metadatas is the additional context
             docs = chromadb_client.get(
                 include=["metadatas", "documents", "embeddings"],
                 limit=chromadb_batch_size,
                 offset=offset,
             )
         
             if len(docs["documents"]) == 0:
                 break
         
             # ids is the unqiue identifier for the content
             yield docs["ids"], docs["documents"], docs["embeddings"].tolist(), docs[
                 "metadatas"
             ]
         
             offset += chromadb_batch_size
         

### Qdrant
         
         # Iterate through the IDs and download their contents
         offset = None
         while True:
             docs, offset = qdrant_client.scroll(
                 collection_name=qdrant_collection_name,
                 with_vectors=True,
                 limit=qdrant_batch_size,
                 offset=offset,
                 with_payload=True,
             )
         
             ids: List[str] = []
             contents: List[Any] = []
             embeddings: List[List[float]] = []
             metadatas: List[Any] = []
         
             for doc in docs:
                 if doc.payload and doc.vector:
                     # You might need to update this data translation logic according to one or more of your field names
                     # id is the unqiue identifier for the content
                     ids.append(str(doc.id))
                     # page_content is the content which was encoded
                     contents.append(doc.payload["page_content"])
                     # vector is the vector embedding of the content
                     embeddings.append(doc.vector)  # type: ignore
                     # metatdata is the additional context
                     metadatas.append(doc.payload["metadata"])
         
             yield ids, contents, embeddings, metadatas
         
             if not offset:
                 break
         

**Note:** Update `QDRANT_COLLECTION_NAME` with the collection name. If you have multiple collections, run the migration for each collection.

### Milvus
         
         # Iterate through the IDs and download their contents
         iterator = milvus_client.query_iterator(
             collection_name=milvus_collection_name,
             filter='pk >= "0"',
             output_fields=["pk", "text", "vector", "idv"],
             batch_size=milvus_batch_size,
         )
         
         while True:
             ids = []
             content = []
             embeddings = []
             metadatas = []
             page = iterator.next()
             if len(page) == 0:
                 iterator.close()
                 break
             for i in range(len(page)):
                 # You might need to update this data translation logic according to one or more of your field names
                 doc = page[i]
                 # pk is the unqiue identifier for the content
                 ids.append(doc["pk"])
                 # text is the content which was encoded
                 content.append(doc["text"])
                 # vector is the vector embedding of the content
                 embeddings.append(doc["vector"])
                 del doc["pk"]
                 del doc["text"]
                 del doc["vector"]
                 # doc is the additional context
                 metadatas.append(doc)
             yield ids, content, embeddings, metadatas

**Note:** Update `MILVUS_COLLECTION_NAME` with the collection name. If you have multiple collections, run the migration for each collection.




## Initialize the AlloyDB table

**Note:** You might need to modify the code examples in this section based on your use case.

  1. Define the embedding service.

The VectorStore interface requires an embedding service. This workflow doesn't generate new embeddings, so the `FakeEmbeddings` class is used to avoid any costs.

### Pinecone
         
         # The VectorStore interface requires an embedding service. This workflow does not
         # generate new embeddings, therefore FakeEmbeddings class is used to avoid any costs.
         from langchain_core.embeddings import FakeEmbeddings
         
         embeddings_service = FakeEmbeddings(size=vector_size)

### Weaviate
         
         # The VectorStore interface requires an embedding service. This workflow does not
         # generate new embeddings, therefore FakeEmbeddings class is used to avoid any costs.
         from langchain_core.embeddings import FakeEmbeddings
         
         embeddings_service = FakeEmbeddings(size=vector_size)

### Chroma
         
         # The VectorStore interface requires an embedding service. This workflow does not
         # generate new embeddings, therefore FakeEmbeddings class is used to avoid any costs.
         from langchain_core.embeddings import FakeEmbeddings
         
         embeddings_service = FakeEmbeddings(size=vector_size)

### Qdrant
         
         # The VectorStore interface requires an embedding service. This workflow does not
         # generate new embeddings, therefore FakeEmbeddings class is used to avoid any costs.
         from langchain_core.embeddings import FakeEmbeddings
         
         embeddings_service = FakeEmbeddings(size=vector_size)

### Milvus
         
         # The VectorStore interface requires an embedding service. This workflow does not
         # generate new embeddings, therefore FakeEmbeddings class is used to avoid any costs.
         from langchain_core.embeddings import FakeEmbeddings
         
         embeddings_service = FakeEmbeddings(size=vector_size)

  2. Prepare the AlloyDB table.

     1. Connect to AlloyDB using a public IP connection. For more information, see [Specifying IP Address Type](https://github.com/GoogleCloudPlatform/alloydb-python-connector?tab=readme-ov-file#specifying-ip-address-type).

### Pinecone
            
            from langchain_google_alloydb_pg import AlloyDBEngine
            
            alloydb_engine = await AlloyDBEngine.afrom_instance(
                project_id=project_id,
                region=region,
                cluster=cluster,
                instance=instance,
                database=db_name,
                user=db_user,
                password=db_pwd,
                ip_type=IPTypes.PUBLIC,  # Optionally use IPTypes.PRIVATE
            )

### Weaviate
            
            from langchain_google_alloydb_pg import AlloyDBEngine
            
            alloydb_engine = await AlloyDBEngine.afrom_instance(
                project_id=project_id,
                region=region,
                cluster=cluster,
                instance=instance,
                database=db_name,
                user=db_user,
                password=db_pwd,
                ip_type=IPTypes.PUBLIC,
            )

### Chroma
            
            from langchain_google_alloydb_pg import AlloyDBEngine
            
            alloydb_engine = await AlloyDBEngine.afrom_instance(
                project_id=project_id,
                region=region,
                cluster=cluster,
                instance=instance,
                database=db_name,
                user=db_user,
                password=db_pwd,
                ip_type=IPTypes.PUBLIC,
            )

### Qdrant
            
            from langchain_google_alloydb_pg import AlloyDBEngine
            
            alloydb_engine = await AlloyDBEngine.afrom_instance(
                project_id=project_id,
                region=region,
                cluster=cluster,
                instance=instance,
                database=db_name,
                user=db_user,
                password=db_pwd,
                ip_type=IPTypes.PUBLIC,
            )

### Milvus
            
            from langchain_google_alloydb_pg import AlloyDBEngine
            
            alloydb_engine = await AlloyDBEngine.afrom_instance(
                project_id=project_id,
                region=region,
                cluster=cluster,
                instance=instance,
                database=db_name,
                user=db_user,
                password=db_pwd,
                ip_type=IPTypes.PUBLIC,
            )

     2. Create a table to copy data into, if it doesn't already exist.

### Pinecone
            
            from langchain_google_alloydb_pg import Column
            
            await alloydb_engine.ainit_vectorstore_table(
                table_name=alloydb_table,
                vector_size=vector_size,
                # Customize the ID column types if not using the UUID data type
                # id_column=Column("langchain_id", "TEXT"),  # Default is Column("langchain_id", "UUID")
                # overwrite_existing=True,  # Drop the old table and Create a new vector store table
            )

### Weaviate
            
            await alloydb_engine.ainit_vectorstore_table(
                table_name=alloydb_table,
                vector_size=vector_size,
                # Customize the ID column types with `id_column` if not using the UUID data type
            )
            

### Chroma
            
            await alloydb_engine.ainit_vectorstore_table(
                table_name=alloydb_table,
                vector_size=vector_size,
                # Customize the ID column types with `id_column` if not using the UUID data type
            )

### Qdrant
            
            await alloydb_engine.ainit_vectorstore_table(
                table_name=alloydb_table,
                vector_size=vector_size,
                # Customize the ID column types with `id_column` if not using the UUID data type
            )

### Milvus
            
            await alloydb_engine.ainit_vectorstore_table(
                table_name=alloydb_table,
                vector_size=vector_size,
                # Customize the ID column types with `id_column` if not using the UUID data type
            )




## Initialize a vector store object

This code adds additional vector embedding metadata to the `langchain_metadata` column in a JSON format. To make filtering more efficient, organize this metadata into separate columns. For more information, see [Create a custom Vector Store](https://github.com/googleapis/langchain-google-alloydb-pg-python/blob/main/docs/vector_store.ipynb).

  1. To initialize a vector store object, run the following command:

### Pinecone
         
         from langchain_google_alloydb_pg import AlloyDBVectorStore
         
         vs = await AlloyDBVectorStore.create(
             engine=alloydb_engine,
             embedding_service=embeddings_service,
             table_name=alloydb_table,
         )

### Weaviate
         
         from langchain_google_alloydb_pg import AlloyDBVectorStore
         
         vs = await AlloyDBVectorStore.create(
             engine=alloydb_engine,
             embedding_service=embeddings_service,
             table_name=alloydb_table,
         )

### Chroma
         
         from langchain_google_alloydb_pg import AlloyDBVectorStore
         
         vs = await AlloyDBVectorStore.create(
             engine=alloydb_engine,
             embedding_service=embeddings_service,
             table_name=alloydb_table,
         )

### Qdrant
         
         from langchain_google_alloydb_pg import AlloyDBVectorStore
         
         vs = await AlloyDBVectorStore.create(
             engine=alloydb_engine,
             embedding_service=embeddings_service,
             table_name=alloydb_table,
         )

### Milvus
         
         from langchain_google_alloydb_pg import AlloyDBVectorStore
         
         vs = await AlloyDBVectorStore.create(
             engine=alloydb_engine,
             embedding_service=embeddings_service,
             table_name=alloydb_table,
         )

  2. Insert data into the AlloyDB table:

### Pinecone
         
         pending: set[Any] = set()
         for ids, contents, embeddings, metadatas in data_iterator:
             pending.add(
                 asyncio.ensure_future(
                     vs.aadd_embeddings(
                         texts=contents,
                         embeddings=embeddings,
                         metadatas=metadatas,
                         ids=ids,
                     )
                 )
             )
             if len(pending) >= max_concurrency:
                 _, pending = await asyncio.wait(
                     pending, return_when=asyncio.FIRST_COMPLETED
                 )
         if pending:
             await asyncio.wait(pending)

### Weaviate
         
         pending: set[Any] = set()
         for ids, contents, embeddings, metadatas in data_iterator:
             pending.add(
                 asyncio.ensure_future(
                     vs.aadd_embeddings(
                         texts=contents,
                         embeddings=embeddings,
                         metadatas=metadatas,
                         ids=ids,
                     )
                 )
             )
             if len(pending) >= max_concurrency:
                 _, pending = await asyncio.wait(
                     pending, return_when=asyncio.FIRST_COMPLETED
                 )
         if pending:
             await asyncio.wait(pending)

### Chroma
         
         pending: set[Any] = set()
         for ids, contents, embeddings, metadatas in data_iterator:
             pending.add(
                 asyncio.ensure_future(
                     vs.aadd_embeddings(
                         texts=contents,
                         embeddings=embeddings,
                         metadatas=metadatas,
                         ids=ids,
                     )
                 )
             )
             if len(pending) >= max_concurrency:
                 _, pending = await asyncio.wait(
                     pending, return_when=asyncio.FIRST_COMPLETED
                 )
         if pending:
             await asyncio.wait(pending)

### Qdrant
         
         pending: set[Any] = set()
         for ids, contents, embeddings, metadatas in data_iterator:
             pending.add(
                 asyncio.ensure_future(
                     vs.aadd_embeddings(
                         texts=contents,
                         embeddings=embeddings,
                         metadatas=metadatas,
                         ids=ids,
                     )
                 )
             )
             if len(pending) >= max_concurrency:
                 _, pending = await asyncio.wait(
                     pending, return_when=asyncio.FIRST_COMPLETED
                 )
         if pending:
             await asyncio.wait(pending)

### Milvus
         
         pending: set[Any] = set()
         for ids, contents, embeddings, metadatas in data_iterator:
             pending.add(
                 asyncio.ensure_future(
                     vs.aadd_embeddings(
                         texts=contents,
                         embeddings=embeddings,
                         metadatas=metadatas,
                         ids=ids,
                     )
                 )
             )
             if len(pending) >= max_concurrency:
                 _, pending = await asyncio.wait(
                     pending, return_when=asyncio.FIRST_COMPLETED
                 )
         if pending:
             await asyncio.wait(pending)




## Run the migration script

  1. [Set up the Python environment](https://docs.cloud.google.com/python/docs/setup).

  2. Install the sample dependencies:
         
         pip install -r requirements.txt

  3. Run the sample migration.

### Pinecone
         
         python migrate_pinecone_vectorstore_to_alloydb.py

Make the following replacements before you run the sample:

     * `PINECONE_API_KEY`: the Pinecone API key.
     * `PINECONE_NAMESPACE`: the Pinecone namespace.
     * `PINECONE_INDEX_NAME`: the name of the Pinecone index.
     * `PROJECT_ID`: the project ID.
     * `REGION`: the region in which the AlloyDB cluster is deployed.
     * `CLUSTER`: the name of the cluster.
     * `INSTANCE`: the name of the instance.
     * `DB_NAME`: the name of the database.
     * `DB_USER`: the name of the database user.
     * `DB_PWD`: the database secret password.

### Weaviate
    
    python migrate_weaviate_vectorstore_to_alloydb.py

Make the following replacements before you run the sample:

     * `WEAVIATE_API_KEY`: the Weaviate API key.
     * `WEAVIATE_CLUSTER_URL`: the Weaviate cluster URL.
     * `WEAVIATE_COLLECTION_NAME`: the Weaviate collection name.
     * `PROJECT_ID`: the project ID.
     * `REGION`: the region in which the AlloyDB cluster is deployed.
     * `CLUSTER`: the name of the cluster.
     * `INSTANCE`: the name of the instance.
     * `DB_NAME`: the name of the database.
     * `DB_USER`: the name of the database user.
     * `DB_PWD`: the database secret password.

### Chroma
    
    python migrate_chromadb_vectorstore_to_alloydb.py

Make the following replacements before you run the sample:

     * `CHROMADB_PATH`: the Chroma database path.
     * `CHROMADB_COLLECTION_NAME`: the name of the Chroma database collection.
     * `PROJECT_ID`: the project ID.
     * `REGION`: the region in which the AlloyDB cluster is deployed.
     * `CLUSTER`: the name of the cluster.
     * `INSTANCE`: the name of the instance.
     * `DB_NAME`: the name of the database.
     * `DB_USER`: the name of the database user.
     * `DB_PWD`: the database secret password.

### Qdrant
    
    python migrate_qdrant_vectorstore_to_alloydb.py

Make the following replacements before you run the sample:

     * `QDRANT_PATH`: the Qdrant database path.
     * `QDRANT_COLLECTION_NAME`: the name of the Qdrant collection name.
     * `PROJECT_ID`: the project ID.
     * `REGION`: the region in which the AlloyDB cluster is deployed.
     * `CLUSTER`: the name of the cluster.
     * `INSTANCE`: the name of the instance.
     * `DB_NAME`: the name of the database.
     * `DB_USER`: the name of the database user.
     * `DB_PWD`: the database secret password.

### Milvus
    
    python migrate_milvus_vectorstore_to_alloydb.py

Make the following replacements before you run the sample:

     * `MILVUS_URI`: the Milvus URI.
     * `MILVUS_COLLECTION_NAME`: the name of the Milvus collection.
     * `PROJECT_ID`: the project ID.
     * `REGION`: the region in which the AlloyDB cluster is deployed.
     * `CLUSTER`: the name of the cluster.
     * `INSTANCE`: the name of the instance.
     * `DB_NAME`: the name of the database.
     * `DB_USER`: the name of the database user.
     * `DB_PWD`: the database secret password.

A successful migration prints logs similar to the following without any errors:  
`Migration completed, inserted all the batches of data to AlloyDB`

  4. Open AlloyDB Studio to view your migrated data. For more information, see [Manage your data using AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource name** column, click the name of the cluster that you created.

  3. Click _delete_ **Delete cluster**.

  4. In **Delete cluster** , enter the name of your cluster to confirm that you want to delete your cluster.

  5. Click **Delete**.

If you created a private connection when you created a cluster, delete the private connection:

  6. Go to the Google Cloud console [Networking page](https://console.cloud.google.com/networking/networks/details/default) and click **Delete VPC network**.




## What's next

  * [Get started with vector embeddings using AlloyDB AI](https://codelabs.developers.google.com/alloydb-ai-embedding#0).
  * Learn how to [build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/docs/ai).
  * [Create a ScaNN index](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index).
  * [Tune your ScaNN indexes](https://docs.cloud.google.com/alloydb/docs/ai/tune-indexes).
  * [Learn how to build a smart shopping assistant with AlloyDB, pgvector, and model endpoint management](https://codelabs.developers.google.com/smart-shop-agent-alloydb#0).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
