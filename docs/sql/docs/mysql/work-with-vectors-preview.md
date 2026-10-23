---
url: https://docs.cloud.google.com/sql/docs/mysql/work-with-vectors-preview/
title: Work with vector embeddings (Preview) \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:51.419054+00:00
---

# Work with vector embeddings (Preview)  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/work-with-vectors-preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Work with vector embeddings (Preview) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview — Cloud SQL for MySQL vector search and storage**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides information about the Preview version of vector embeddings. If you want to use the GA version of this feature, the instance maintenance version must be version `MYSQL_8_0_36.R20241208.01_00` or later. For information about how to upgrade your instance to a newer version that supports GA vector embeddings, see [Upgrade your instance](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). 

For information about the syntax and behavior of vector embeddings for the GA version of this feature, see [Vector search](https://docs.cloud.google.com/sql/docs/mysql/vector-search). 

This page details how you can interact with Cloud SQL to build applications that use vector embeddings.

Cloud SQL for MySQL supports the storage of vector embeddings. You can then create vector search indexes and perform similarity searches on these vector embeddings along with the rest of the data that you store in Cloud SQL.

## Vector embedding storage

You can use Cloud SQL for MySQL to store vector embeddings by creating a vector embedding column in a table. The special vector embedding column maps to the `VARBINARY` data type. Like other relational data in the table, you can access vector embeddings in the table with existing transactional guarantees. A table that has a vector embedding column is a regular InnoDB table and is therefore compliant with atomicity, consistency, isolation, and durability (ACID) properties. ACID properties deviate only for vector search index lookups.

**Note:** To distinguish the vector embedding column from other columns, Cloud SQL for MySQL uses a special `COMMENT` and `CONSTRAINT`. The constraint is required for input validation, and the vector embedding column annotation is visible as a `COMMENT`. You can't modify or delete the comment or the constraint.

Consider the following when setting up a table for vector embeddings:

  * You can create a maximum of one vector embedding column in a table and one vector search index per table. Each vector embedding stored in the same column must have exactly the same dimensions that you specified when you defined the column. A vector embedding has an upper limit of 16,000 dimensions. If you have enough storage and memory available, then you can have separate tables with different vector embedding columns and vector search indexes on the same instance.

  * While there's no hard limit to the number of vector embeddings that you can store in a table, vector search indexes require memory. For this reason, we recommend that you store no more than 10 million vector embeddings in a table.

  * Also see the list of Limitations.




Replication works the same way for the vector embedding column as it does for other MySQL InnoDB columns.

## Similarity search

Cloud SQL supports similarity search using both K-nearest neighbor (KNN) and approximate nearest neighbor (ANN) search queries. You can use both types of vector searches in your Cloud SQL instances. You can create a vector search index for ANN searches only.

**Important:** The SQL syntax provided for performing operations on vector search indexes is subject to change prior to the GA release of this feature based on Preview feedback.

### K-nearest neighbor (KNN) search

Cloud SQL supports querying using KNN vector search, also referred to as exact nearest neighbor search. Performing a KNN vector search provides perfect recall. You can perform KNN searches without having to create a vector search index. KNN search is based on performing a table scan algorithm.

For KNN search, Cloud SQL also supports the following vector distance search functions:

  * Cosine
  * Dot product
  * L2 squared distance



For more information about using vector search distance functions, see Query the distance of a vector embedding.

### Approximate nearest neighbor (ANN) search

Cloud SQL supports creating and querying ANN searches through the creation of vector search indexes. An ANN vector search index lets you optimize for fast performance instead of perfect recall. For ANN search, Cloud SQL supports the following index types:

  * `BRUTE_FORCE`: the default vector search index type for a base table that has fewer than 10,000 rows. This type is best suited for searches within a smaller subset of an original dataset. The memory used by the index is equal to the size of the dataset. This index type isn't persisted to disk.
  * `TREE_SQ`: the default vector search index type for a base table that has 10,000 or more rows. This type uses the least amount of memory or approximately 25% of the size of the dataset. `TREE_SQ` indexes are persisted to disk.
  * `TREE_AH`: a vector search index type that provides an asymmetric hashing search type algorithm. As implemented in Cloud SQL, this index type isn't optimized for memory footprint and isn't persisted.



### Update vector search indexes

Cloud SQL for MySQL updates vector search indexes in real time. Any transaction that performs Data Manipulation Language (DML) operations on the base table also propagates changes to the associated vector search indexes. The changes in a vector search index are visible immediately to all other transactions, which means an isolation level of `READ_UNCOMMITTED`.

If you roll back a transaction, then the corresponding rollback changes also occur in the vector search index.

### Replication of vector search indexes

Cloud SQL for MySQL replicates vector search indexes to all read replicas. Replication filters and the replication of vector search indexes to cascading replicas aren't supported.

## Configure an instance to support vector embeddings

This section describes how to configure your Cloud SQL instance to support the storage, indexing, and querying of vector embeddings.

Both Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition instances support vector embeddings.

### Before you begin

  * Your instance must be running Cloud SQL for MySQL MySQL version `8.0.36.R20240401.03_00` or later.
  * Your instance must have [sufficient disk space to allocate memory](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes#configure_memory_allocation_for_vector_indexes) for the total number of vector embeddings on the instance.



### Enable vector embeddings

To turn on support for vector embeddings, you must configure MySQL database flags.
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --database-flags=FLAGS

Replace INSTANCE_NAME with the name of the instance on which you want to enable vector embedding support.

In FLAGS, configure the following MySQL flags on your instance:

  * `cloudsql_vector`: set this flag to `on` to enable vector embedding storage and search support. You can create new vector embedding columns and vector search indexes on the instance.
  * `cloudsql_vector_max_mem_size`: optional. Specify the maximum memory allocation in bytes for all vector search indexes on the instance. If you don't specify this flag, then the default memory allocation is 1 GB, which is the minimum memory allocation. For more information about how to calculate the amount to specify, see Configure the memory allocation for vector search indexes.

This dedicated memory comes from the memory allocated to your `innodb_buffer_pool_size`. Your available buffer pool is reduced by the same amount. The maximum allowed value for this flag is **50%** of your total `innodb_buffer_pool_size`.

If you specify a value that's greater than 50% of your total `innodb_buffer_pool_size`, then Cloud SQL reduces the effective value to 50% of the available size and logs a warning message for the instance.




After you configure the flags, your command might look similar to the following:
    
    
    gcloud sql instances patch my-instance \
      --database-flags=cloudsql_vector=on,cloudsql_vector_max_mem_size=4294967296

The flags to configure vector embeddings support in Cloud SQL for MySQL are static flags. After you update the instance with the flags, your instance restarts automatically in order for the configuration changes to take effect.

For more information about how to configure database flags for MySQL, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags#set_flags).

### Disable vector embeddings

To disable vector embeddings, set the `cloudsql_vector` flag to `off`.

For example:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --database-flags=cloudsql_vector=off

Replace INSTANCE_NAME with the name of the instance on which you're turning off vector embedding support.

Setting `cloudsql_vector` to `off` prevents you from creating new vector embedding columns and vector search indexes. After you configure this static flag, the instance restarts automatically for the configuration change to take effect.

After the restart of the instance, Cloud SQL for MySQL does the following:

  * Removes all persisted `TREE_SQ` vector search indexes from the persistent disk.
  * Keeps the data dictionary table entries for the vector search indexes that have been built. However, Cloud SQL for MySQL doesn't rebuild the indexes and any search queries to these indexes return an error.
  * Continues to store the vector embeddings in the base tables. The vector embeddings remain accessible.



If you later re-enable the `cloudsql_vector` flag for the instance, then Cloud SQL attempts to rebuild the indexes while the instance restarts based on the entries in the data dictionary table.

## Read replica configuration

If the instance meets the maintenance version and flag enablement criteria, then Cloud SQL fully supports vector embeddings on a read replica.

If you create a replica from a primary instance that has vector embedding support enabled, then the read replica inherits the vector embedding support settings from the primary instance. You must enable vector embedding support individually on already existing read replica instances.

In terms of impact to replication lag, creating and maintaining of vector search indexes operates in the same way as regular MySQL indexes.

Vector search indexes aren't supported on cascading replicas.

## Example: An ANN vector search index and query

The following example walkthrough provides steps to create an ANN-based vector search index and query in Cloud SQL.

  1. Generate vector embeddings. You can create vector embeddings manually or use a text embedding API of your choice. For an example that uses Vertex AI, see Generate vector embeddings based on row data.

  2. Create a table in Cloud SQL for MySQL that contains a vector embedding column with three dimensions.
         
         CREATE TABLE books (
         id   INTEGER PRIMARY KEY AUTO_INCREMENT,
         title VARCHAR(60),
         embedding VECTOR(3) USING VARBINARY
         );
         

  3. Insert a vector embedding into the column.
         
         INSERT INTO books VALUES (
         1,
         'book title',
          string_to_vector('[1,2,3]')
         );
         

  4. Commit the changes.
         
         commit;
         

  5. Create the vector search index. If you're creating a `TREE_SQ` or a `TREE_AH` index, then your table must have at least 1,000 rows.
         
         CALL mysql.create_vector_index('vectorIndex',
                                        'dbname.books',
                                        'embedding',
                                        'index_type=BRUTE_FORCE, distance_measure=L2_SQUARED'
                                        );
         

  6. Get the nearest neighbors.
         
         SELECT title FROM books
         WHERE
         NEAREST(embedding) TO (string_to_vector('[1,2,3]'));
         




### Generate vector embeddings based on row data

You can generate a vector embedding for a given row's data by using a text embedding API such as [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings) or [OpenAI](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings). You can use any text embedding API with Cloud SQL vector embeddings. However, you must use the same text embedding API for query string vector generation. You can't combine different APIs for source data and query vectorization.

For example, you can generate a vector embedding from Vertex AI:
    
    
    from vertexai.language_models import TextEmbeddingModel
    
    def text_embedding() -> list:
        """Text embedding with a Large Language Model."""
        model = TextEmbeddingModel.from_pretrained("text-embedding-004")
        embeddings = model.get_embeddings(["What is life?"])
        for embedding in embeddings:
            vector = embedding.values
            print(f"Length of Embedding Vector: {len(vector)}")
        return vector
    
    if __name__ == "__main__":
        text_embedding()
    

## Store vector embeddings

This section provides examples statements for storing vector embeddings in Cloud SQL.

### Create a new table with a vector embedding column
    
    
    CREATE TABLE books (
      id INTEGER PRIMARY KEY AUTO_INCREMENT,
      title VARCHAR(60),
      embedding VECTOR(3) USING VARBINARY
      );
    

### Add a vector embedding column to an existing table
    
    
    ALTER TABLE books
    ADD COLUMN embedding
    VECTOR(3) USING VARBINARY;
    

### Insert a vector embedding
    
    
    INSERT INTO books (
      title,
      embedding
      ) VALUES (
        'book title',
        string_to_vector('[1,2,3]')
    );
    

### Insert multiple vector embeddings
    
    
    INSERT INTO books (
      title,
      embedding
      ) VALUES (
        'book title',
        string_to_vector('[1,2,3]')),
         ('book title', string_to_vector('[4,5,6]')
    );
    

### Upsert a vector embedding
    
    
    INSERT INTO books (
      id,
      title,
      embedding
      ) VALUES (
        1,
        'book title',
         string_to_vector('[1,2,3]')
         )
    ON DUPLICATE KEY UPDATE embedding = string_to_vector('[1,2,3]');
    

### Update a vector embedding
    
    
    UPDATE books
    SET embedding = string_to_vector('[1,2,3]')
    WHERE id = 1;
    

### Delete a vector embedding
    
    
    DELETE FROM books
    WHERE embedding = string_to_vector('[1,2,3]');
    

## Work with vector search indexes

By default, you can perform the exact nearest neighbor search, which provides the perfect recall. You can also add an index to use ANN search, which trades some recall for speed. Unlike typical indexes, after you add an approximate index, you see different results for queries.

**Important:** If a vector search index is present on a table, then you can't perform any data definition language (DDL) operations on the table. Before performing the DDL operation, drop the vector search index on the base table.

### Recommendations

This section provides best practices for working with vector search indexes. Every workload is different, and you might need to adjust accordingly.

  * _Before_ you create a vector search index, you must load data into the table. Your base table must have at least 1,000 rows. These requirements apply only to the `TREE_SQ` and `TREE_AH` search index types. If you have more data points available, then you'll have better partitioning and training of the index.
  * Monitor the memory usage of indexes. If the instance runs out of memory, then you can't create or build any indexes. For existing indexes, after reaching the threshold, Cloud SQL writes warnings to the MySQL error log periodically. You can view memory usage in the `information_schema.innodb_vector_indexes` table.
  * If the underlying base table has undergone major DML changes, then rebuild the vector search indexes. To get the initial size of the index at build time and the current size of the index, query the `information_schema.innodb_vector_indexes` table.
  * Generally, it's acceptable to leave the number of partitions to be computed internally. If you have a use case where you want to specify the number of partitions, then you must have _at least_ 100 data points _per partition_.



### Read-only base table during vector search index operations

For the duration of all three vector search index operations—create, alter, and drop— the base table is put into a read-only mode. During these operations, no DMLs are allowed on the base table.

### Persistence, shutdown, and impact on maintenance

Only vector search indexes that use the `TREE_SQ` type persist to disk on a clean shutdown of an instance shutdown. Vector search indexes that use the `TREE_AH` and `BRUTE_FORCE` types are in-memory only.

After a clean shutdown of an instance, Cloud SQL reloads vector search indexes as the instance restarts. However, after a crash or an unclean shutdown, Cloud SQL must rebuild the vector search indexes. For example, any time that your instance undergoes a crash and recovery from backup and restore, point-in-time recovery (PITR), or high-availability (HA) failover, Cloud SQL rebuilds your vector search indexes. For these events, the following occurs:

  * The rebuild happens in the background automatically.
  * During the rebuild, the base table is in read-only mode.
  * If the automatic rebuild can't get a lock on the table within a specific timeout period, then the rebuild fails. You might need to rebuild the index manually instead.



The time required for an index rebuild might increase the time required for a shutdown, which might also increase the required maintenance and update time for an instance.

### Configure the memory allocation for vector search indexes

Cloud SQL builds and maintains vector search indexes in memory. The `TREE_SQ` index type persists on a clean shutdown and reloads after the instance restarts. During runtime, all vector search indexes need to stay in memory.

To make sure that Cloud SQL has enough memory available to keep all vector search indexes in memory, configure the Cloud SQL instance with a `cloudsql_vector_max_mem_size` database flag. `cloudsql_vector_max_mem_size` governs how much memory the Cloud SQL instance dedicates for vector search indexes. When you configure the value for the flag, keep the following in mind:

  * The default and minimum value is 1 GB. The upper limit is 50% of the buffer pool size.
  * After you set this flag, your instance automatically restarts for the configuration change to take effect.
  * If your instance has used up all its configured memory, you can't create or alter any vector search indexes.

**Important:** The memory that you allocate to vector search indexes is used outside of the buffer pool. When you enable `cloudsql_vector`, Cloud SQL reduces the buffer pool size by the value you assign to the `cloudsql_vector_max_mem_size` flag.

To update the memory allocated for vector search indexes on the instance, change the value of the `cloudsql_vector_max_mem_size` flag.
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --database-flags= cloudsql_vector_max_mem_size=NEW_MEMORY_VALUE

Replace the following:

  * INSTANCE_NAME: the name of the instance on which you are changing the memory allocation.
  * NEW_MEMORY_VALUE: the updated memory allocation, in bytes, for your vector search indexes.



This change restarts your instance automatically so that the change can take effect.

#### Calculate required memory

The amount of memory that an index requires depends on the index type, the number of vector embeddings, and the dimensionality of the embeddings. There are two memory requirements to consider:

  * **Build time memory:** the memory required during the build of the index.
  * **Index memory** : the memory that the index occupies after the index is built.



For a given index, its dataset size is the memory needed to read all the vector embeddings in memory. Given that each dimension is represented by a float which uses 4 bytes of memory, you can determine the dataset_size as follows:
    
    
    dataset_size = <num_embeddings> * (4 * <dimensions>)
    

For example, if you have one million embeddings of 768 dimensions, your `dataset_size` is 3 GB.

Based on the previous example, the memory requirements for the different index types are as follows:

Index type | Build time memory | Index memory  
---|---|---  
`TREE_SQ` | 4 GB | 1 GB  
`TREE_AH` | 3.5 GB | 3.5 GB  
`BRUTE_FORCE` | 3 GB | 3 GB  
  
If you're using `TREE_SQ` vector search indexes, then you must also factor in the memory required for persistence at runtime. To the total amount of memory in your configuration, add the amount of index memory used by the largest active `TREE_SQ` vector search index.

Whenever the base table where the vector embeddings are stored undergoes DML operations, the vector search index is updated in real time. These updates change the memory footprint of the index, which can shrink or expand depending on the DML operation. You can monitor the memory footprint of an index by querying the `information_schema.innodb_vector_indexes` table. For information about monitoring the size of your vector search index, see Monitor vector search indexes.

### Create a vector search index

The statement to create a vector search index uses the following syntax:
    
    
    CALL mysql.create_vector_index('INDEX_NAME',
                                    'DB_NAME.TABLE_NAME',
                                    'COLUMN_NAME',
                                    'PARAMETERS'
                                  );
    

For example:
    
    
    CALL mysql.create_vector_index('vectorIndex',
                                    'db.books',
                                    'embedding',
                                    'index_type=TREE_SQ, distance_measure=l2_squared'
                                   );
    

The index name that you specify must be unique within the database.

#### Vector search index parameters

The `mysql.create_vector_index` and `mysql.alter_vector_index` functions support multiple parameters that you can specify with comma-separated key-value pairs. All `mysql.create_vector_index` function parameters are optional. If you specify an empty string or NULL, then the default parameter values are configured for the index.

  * `distance_measure`: the supported values are: `L2_SQUARED`, `COSINE`, and `DOT_PRODUCT`. `L2_SQUARED` is the default.
  * `num_neighbors`: the number of neighbors to return from an ANN query. You can also override this parameter when performing the search query. The default is `10`.
  * `index_type`: specifies the type of index to be built. Valid values are: `BRUTE_FORCE`, `TREE_SQ`, and `TREE_AH`.

    * `BRUTE_FORCE` is the default for a table that has fewer than 10,000 rows
    * `TREE_SQ` is the default for a table that has 10,000 or more rows

To specify the `TREE_AH` or `TREE_SQ` index type, the size of your base table must be greater than 1,000 rows.

  * `num_parititions`: specifies the number of K-means clusters to build. This parameter is only allowed if you have configured an `index_type`. This option isn't applicable to `BRUTE_FORCE`. If you specify the `TREE_SQ` or `TREE_AH` index type, then the size of your base table must be greater than or equal to **num_partitions** * 100.


**Note:** The size of your base table is calculated by scanning the table for the number of rows with non-NULL entries in the vector embeddings column.

### Alter a vector search index
    
    
    CALL mysql.alter_vector_index('DB_NAME.INDEX_NAME', 'PARAMETERS');
    

The `alter_vector_index` function is used explicitly to rebuild a vector search index. To use this function, the index must already exist. You might want to rebuild an index for the following use cases:

  * To rebuild the index with different options. For example, you might want to use a different index type or different distance measure.
  * To rebuild the index because the base table has undergone major DML changes. For example, you need to retrain the vector search index based on the data in the base table.



All parameters for rebuilding the index are identical to the ones available for creating the index and are also optional. If you specify an empty string or NULL when you rebuild the index, then the index is rebuilt based on the parameters specified at the time of index creation. If no parameters are provided at the time of index creation, then the default parameter values are used.

The existing vector search index is available during the `alter_vector_index` operation. You can still perform search queries against the index.

### Drop a vector search index

You can't perform a DDL operation on a table that has a vector search index. Before performing the DDL operation on the table, you must drop the vector search index.
    
    
    CALL mysql.drop_vector_index('DB_NAME.INDEX_NAME');
    

## Query vector embeddings

This section provides examples for the different ways that you can query vector embeddings.

### View the vector embeddings
    
    
    SELECT vector_to_string(embedding) FROM books;
    

### Get the exact neighbor search to a vector embedding
    
    
    SELECT id,cosine_distance(embedding,
       string_to_vector('[1,2,3]')) dist
    FROM books
    ORDER BY dist
    LIMIT 10;
    

### Get the approximate neighbor search to a vector embedding
    
    
    SELECT title FROM books
    WHERE
    NEAREST(embedding) TO (string_to_vector('[1,2,3]'), 'num_neighbors=10');
    

Performing an ANN search supports two parameters. Both are optional.

  * **num_partitions** : specify the number of partitions to probe for an ANN vector search. If you don't specify the number of partitions, then the search uses a value generated based on the size of the table, number of partitions in the vector search index, and other factors.
  * **num_neighbors** : specify the number of neighbors to return. This value overrides the value set at the time of creation of the vector search index.



## Filter vector embeddings

Use extra columns as predicates to fine tune the filtering of your vector embedding query results. For example, if you add a `printyear` column, then you can add a specific year value as a filter to your query.
    
    
    SELECT title FROM books
    WHERE
    NEAREST(embedding) TO (string_to_vector('[1,2,3]'))
    AND printyear > 1991;
    

## Query the distance of a vector embedding

This section provides examples of vector distance functions that are available for KNN search.

### Get the Cosine distance
    
    
    SELECT cosine_distance(embedding, string_to_vector('[3,1,2]'))
    AS distance FROM books WHERE id=10;
    

### Get the Dot Product distance
    
    
    SELECT dot_product(embedding, string_to_vector('[3,1,2]'))
    AS distance FROM books WHERE id=10;
    

### Get the L2 Squared distance
    
    
    SELECT l2_squared_distance(embedding, string_to_vector('[3,1,2]'))
    AS distance FROM books WHERE id=10;
    

### Get rows within a certain distance
    
    
    SELECT * FROM books
    WHERE l2_squared_distance(embedding, string_to_vector('[1,2,3]')) < 10;
    

You can combine with `ORDER BY` and `LIMIT`
    
    
    SELECT id, vector_to_string(embedding),
           l2_squared_distance(embedding, string_to_vector('[1,2,3]')) dist
    FROM books ORDER BY dist LIMIT 10;
    

## Monitor vector search indexes

To get real-time information about all the vector search indexes in the instance, use the `information_schema.innodb_vector_indexes` table.

To view the table, run the following command:
    
    
    SELECT * FROM information_schema.innodb_vector_indexes;
    

Sample output might look like the following:
    
    
    *************************** 1. row ***************************
           INDEX_NAME: test.t4_index
           TABLE_NAME: test.t4_bf
           INDEX_TYPE: BRUTE_FORCE
         DIST_MEASURE: SquaredL2Distance
               STATUS: Ready
                STATE: INDEX_READY_TO_USE
           PARTITIONS: 0
    SEARCH_PARTITIONS: 0
         INITIAL_SIZE: 40000
         CURRENT_SIZE: 40000
              QUERIES: 0
            MUTATIONS: 0
         INDEX_MEMORY: 160000
       DATASET_MEMORY: 0

In the `information_schema.innodb_vector_indexes` table, you can view the following:

  * The options that are potentially generated. In other words, `num_partitions` or the number of partitions to probe for a query.
  * The `STATE` and `STATUS` columns tell you the current state of the index. During the build phase, the status column gives information about how far the vector search index is in the build phase.
  * The `INITIAL_SIZE` column provides the table size during index creation. You can compare this size with `CURRENT_SIZE` to get an idea on how much the index has changed since its creation due to DMLs on the base table.
  * The `QUERIES` and `MUTATIONS` columns provide you with real-time insights into how busy the index is.
  * The `INDEX_MEMORY` and `DATASET_MEMORY` columns provide information about memory consumption of the index. `INDEX_MEMORY` indicates how much memory is consumed by the index and `DATASET_MEMORY` indicates how much additional memory is consumed during build time.



To get a list of the search vector indexes created on the instance, you can view the `mysql.vector_indexes` data dictionary table.

To view the table, run the following command:
    
    
    SELECT * FROM mysql.vector_indexes;
    

Sample output:
    
    
    *************************** 1. row ***************************
       index_name: test.index1
       table_name: test.t1
      column_name: j
    index_options: index_type=BRUTE_FORCE, distance_measure=L2_SQUARED
           status: ACTIVE
      create_time: 2024-04-08 22:46:21
      update_time: 2024-04-08 22:46:21
    1 row in set (0.00 sec)

## Limitations

  1. There can only be one vector embedding column per table.
  2. There can only be one vector search index per table.
  3. A vector embedding can have up to 16,000 dimensions.
  4. InnoDB table-level partitioning on tables with vector embedding columns isn't supported.
  5. If the instance restarts from an unclean shutdown, then Cloud SQL rebuilds the vector search index automatically. 
     1. While rebuilding the vector search index, the base table is read-only.
     2. If Cloud SQL can't acquire a lock on the table within the specified time, then the automatic rebuild of the index might fail.
     3. If automatic rebuilding of the index fails, then you must rebuild the index manually.
  6. To add a vector embedding column, the table must have a primary key. Cloud SQL doesn't support primary keys of the type `BIT`, `BINARY`, `VARBINARY`, `JSON`, `BLOB`, `TEXT`, or spatial data types. Composite primary keys can't include any of these types.
  7. If a vector search index is present on a table, then DDL operations aren't allowed. The vector search index must be dropped before performing DDL operations on the base table.
  8. Vector embeddings aren't supported on non-InnoDB tables or on temporary tables.
  9. The vector embedding column can't be a generated column.
  10. The `NEAREST..TO` predicate can be combined with other "scalar" predicates by using `AND` or `OR`. The scalar predicates on the table are evaluated after the vector predicates are applied.
  11. The `NEAREST..TO` predicate is supported only in a `SELECT` statement. Other DML statements don't support `NEAREST..TO`.
  12. Subqueries aren't supported with `NEAREST..TO`. A constraint can't be added to the primary key of the base table if a vector search index is present.
  13. Pre-filtering is feasible only through distance functions and by using `ORDER BY` with `LIMIT`.

For example, if you create the following table:
         
         CREATE TABLE books
         (
         bookid          INT PRIMARY KEY,
         title           VARCHAR(1000),
         author          VARCHAR(100),
         printyear       int,
         country         VARCHAR(100),
         bvector         VECTOR(1536) USING VARBINARY
         //bvector is embedding vector of book's plot,genre,reviews etc
         );
         

Then you might use the following query to achieve pre-filtering.
         
         //select query to obtain books by specific author and having similar plot-genre-reviews
         SELECT bookid, title, author,l2_squared_distance(bvector, qvector) dist
         FROM books where author='cloudsql' ORDER BY dist LIMIT 10
         

Post-filtering is supported with `NEAREST..TO` and distance functions.




## Troubleshoot

In the event of a crash, the index is rebuilt automatically. When a rebuild is in progress, there are two restrictions:

  1. During index creation, the base table is in read-only mode.
  2. While the index is being rebuilt, ANN queries against existing indexes fail.



## What's next

  * [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/mysql/manage-data-using-studio)
  * [Write SQL with Gemini assistance](https://docs.cloud.google.com/sql/docs/mysql/write-sql-gemini)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
