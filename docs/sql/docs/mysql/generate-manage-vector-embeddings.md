---
url: https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings/
title: Generate and manage vector embeddings \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:55.339296+00:00
---

# Generate and manage vector embeddings  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Generate and manage vector embeddings Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/generate-manage-vector-embeddings "View this page for the PostgreSQL database engine") | SQL Server

**Note** : To use the general availability ([GA](https://cloud.google.com/products#product-launch-stages)) version of MySQL vector search, the maintenance version of your instance must be version `MYSQL_8_0_36.R20241208.01_00` or later. For information about how to upgrade your instance to a later version that supports GA vector embeddings, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).   
  
For information about the syntax and behavior of vector embeddings for the [Preview](https://cloud.google.com/products#product-launch-stages) version of this feature, see [Work with vector embeddings (Preview)](https://docs.cloud.google.com/sql/docs/mysql/work-with-vectors-preview).   
  
If you're already using the GA version of vector search in Cloud SQL for MySQL 8.0 or 8.4 and want to upgrade to Cloud SQL for MySQL 9.7, then review the [differences in MySQL vector support in Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/vector-search#version-differences) before you [perform the major version upgrade to Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). 

This page describes how to generate and store vector embeddings. For an overview, see [Vector embedding storage](https://docs.cloud.google.com/sql/docs/mysql/vector-search#vector_embedding_storage).

### Before you begin

If you're using Cloud SQL for MySQL 8.4 or earlier, then you need a Cloud SQL instance with the [`cloudsql_vector` database flag enabled](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search#enable-cloudsql-vector-flag) to generate and store vector embeddings.

If you're using Cloud SQL for MySQL 9.7 or later, you can generate and store vector embeddings without setting the `cloudsql_vector` database flag on your Cloud SQL instance. However, you can't create vector indexes or perform [ANN searches](https://docs.cloud.google.com/sql/docs/mysql/vector-search#ann_search) on your vector data.

### Generate vector embeddings based on row data

You can generate a vector embedding for a given row's data by using a text embedding API such as [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings) or [OpenAI](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings). You can use any text embedding API with Cloud SQL vector embeddings. However, you must use the same text embedding API for query string vector generation. You can't combine different APIs for source data and query vectorization.

For example, you can [generate a vector embedding from Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings):
    
    
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

This section provides example statements for storing vector embeddings in Cloud SQL.

### Create a new table with a vector embedding column

Use the `CREATE TABLE` statement with a column that uses the `VECTOR` data type.

Use the following syntax to create the table.

For Cloud SQL for MySQL 8.4 and earlier, use the following syntax:
    
    
    CREATE TABLE TABLE_NAME(
      id INTEGER
      PRIMARY KEY
        AUTO_INCREMENT,
        title VARCHAR(60),
        EMBEDDING_COLUMN_NAME
          VECTOR(VECTOR_DIMENSIONS)
      USING VARBINARY);
    

Replace the following parameters:

  * `TABLE_NAME`: the name of the table where you want to store the embeddings.
  * `EMBEDDING_COLUMN_NAME`: the name of the column that stores the embedding.
  * `VECTOR_DIMENSIONS`: the number of dimensions to use for the embedding.



In the following example, the embedding column has a vector with three dimensions. The data stored in this column has the `VARBINARY` data type.
    
    
    CREATE TABLE books(
      id INTEGER PRIMARY KEY AUTO_INCREMENT, title VARCHAR(60), embedding VECTOR(3) USING VARBINARY);
    

For Cloud SQL for MySQL 9.7 and later, declaring the `VARBINARY` keyword is optional and supported for backward compatibility. You also don't need to specify the dimensions for the vector, which defaults to `2048`.

For Cloud SQL for MySQL 9.7 and later, you can use the following syntax:
    
    
    CREATE TABLE TABLE_NAME(
      id INTEGER
      PRIMARY KEY
        AUTO_INCREMENT,
        title VARCHAR(60),
        EMBEDDING_COLUMN_NAME
          VECTOR([VECTOR_DIMENSIONS])
      [USING VARBINARY]);
    

For more information, see [The VECTOR Type](https://dev.mysql.com/doc/refman/9.7/en/vector.html) in the MySQL documentation.

### Add a vector embedding column to an existing table

Use the `ALTER TABLE` statement to add a vector embedding column to an existing table. The column must use the `VECTOR` data type to hold the embedding.

In the following example, an embedding column that has a vector with three dimensions is inserted into the table.
    
    
    ALTER TABLE books
    ADD COLUMN embedding
      VECTOR(3)
    USING VARBINARY;
    

For MySQL 9.7:
    
    
    ALTER TABLE books
    ADD COLUMN embedding
      VECTOR(3);
    

### Insert a vector embedding

Use `INSERT` with the [`string_to_vector` function](https://docs.cloud.google.com/sql/docs/mysql/functions#vector_conversion_functions) to insert a vector embedding values into a table.

In the following example, a vector with three dimensions is inserted into the embedding column.
    
    
    INSERT INTO books
      (
        title,
        embedding)
    VALUES (('book title', string_to_vector('[1,2,3]')));
    

### Insert multiple vector embeddings

Use `INSERT` with the [`string_to_vector` function](https://docs.cloud.google.com/sql/docs/mysql/functions#vector_conversion_functions) to insert a comma-separated list of vector embeddings.

In the following statement, two embeddings, each containing a vector with three dimensions and is inserted into the embedding column.
    
    
    INSERT INTO books
      (
        title,
        embedding)
    VALUES
      (
        (
          'book title',
          string_to_vector('[1,2,3]')),
        ('book title', string_to_vector('[4,5,6]')));
    

### Upsert a vector embedding

Use an `INSERT` or `UPDATE` operation on a table with the [`string_to_vector` function](https://docs.cloud.google.com/sql/docs/mysql/functions#vector_conversion_functions) to add a vector embedding column, using the following syntax.

In the following statement, an upsert is used to insert or update the embedding column with an embedding that contains a vector with three dimensions.
    
    
    INSERT INTO books
      (
        id,
        title,
        embedding)
    VALUES
      (
        (
          1,
          'book title',
          string_to_vector('[1,2,3]')))
    ON DUPLICATE KEY UPDATE embedding = string_to_vector('[1,2,3]');
    

### Update a vector embedding

Use `UPDATE` with the [`string_to_vector` function](https://docs.cloud.google.com/sql/docs/mysql/functions#vector_conversion_functions) to update a vector embedding.

In the following statement, `UPDATE` is used to update the embedding column with a vector with three dimensions.
    
    
    UPDATE books
    SET embedding = string_to_vector('[7,8,9]')
    WHERE id = 1;
    

## Retrieve vector embeddings

To retrieve vector embeddings, use the Cloud SQL [`vector_to_string` function](https://docs.cloud.google.com/sql/docs/mysql/functions#vector_conversion_functions) along with the name of the embedding.

In the following statement, the embedding column is retrieved to view.
    
    
    SELECT vector_to_string(embedding) FROM books WHERE id = 1;
    

## Delete a vector embedding

Use `DELETE` with the [`string_to_vector` function](https://docs.cloud.google.com/sql/docs/mysql/functions#vector_conversion_functions) to remove a vector embedding from a table. If there's a vector index, then you must first delete it. For more information, see [Drop a vector index](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes#drop_a_vector_index).

In the following statement, `DELETE` is used to delete the value in the embedding column.
    
    
    DELETE FROM books
    WHERE embedding = string_to_vector('[1,2,3]');
    

## What's next

  * Read the [overview about vector search on Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/vector-search).
  * Learn how to [enable and disable vector embeddings on your instance](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search).
  * Learn how to [create vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes).
  * Learn how to [perform searches on vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
