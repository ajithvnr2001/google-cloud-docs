---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/perform-vector-search/
title: Perform vector search in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:56.446565+00:00
---

# Perform vector search in AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/perform-vector-search/

This page documents AlloyDB Omni version **15.15.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)



Send feedback 

#  Perform vector search in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.15.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/perform-vector-search)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/perform-vector-search)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/perform-vector-search)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/perform-vector-search)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/perform-vector-search)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/perform-vector-search)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/perform-vector-search)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/perform-vector-search)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/perform-vector-search)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/perform-vector-search)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/perform-vector-search)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/perform-vector-search)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/perform-vector-search)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/perform-vector-search)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/perform-vector-search)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/perform-vector-search)

This tutorial describes how to set up and perform a vector search in AlloyDB Omni. You run queries using exact nearest neighbor search (KNN) and approximate nearest neighbor (ANN)-based ScaNN index. You also learn how to run filtered vector search queries efficiently using the ScaNN index. **Note:** The examples in this tutorial, which show vector search capabilities, are intended for demonstration purposes only.

## Objectives

  * Install AlloyDB AI in AlloyDB Omni.
  * Connect to your database and install required extensions.
  * Create a `product` and `product inventory` table.
  * Insert data to the `product` and `product inventory` tables and perform a basic vector search.
  * Create a ScaNN index on the products table.
  * Perform a vector search.
  * Perform a complex vector search with a filter and a join.



## Costs

In this document, you use the following billable component of Google Cloud:

  * [Vertex AI](https://cloud.google.com/vertex-ai/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator).

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Prerequisites

Complete the following prerequisites before performing a vector search.

### Install AlloyDB AI in AlloyDB Omni based on your computing environment

Based on the computing environment that you're using, complete the instructions in [Install AlloyDB AI in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/install-with-alloydb-ai) to install AlloyDB Omni.

### Connect to your database using psql

Connect to your database using psql:
    
    
        export DBPOD=`kubectl get pod --selector=alloydbomni.internal.dbadmin.goog/dbcluster=my-db-cluster,alloydbomni.internal.dbadmin.goog/task-type=database -o jsonpath='{.items[0].metadata.name}'`
        kubectl exec -ti $DBPOD -c database -- psql -h localhost -U postgres

### Install required extensions

Run the following query to install the `vector`, `alloydb_scann`, and the `google_ml_integration` extensions:
    
    
      CREATE EXTENSION IF NOT EXISTS vector;
      CREATE EXTENSION IF NOT EXISTS alloydb_scann;
      CREATE EXTENSION IF NOT EXISTS google_ml_integration CASCADE;
    

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Insert product and product inventory data and perform a basic vector search

The `product_inventory` and `product` tables are used in this tutorial to run complex vector search queries.

  1. Run the following statement to create a `product` table that does the following:

     * Stores basic product information.
     * Includes an `embedding` vector column that computes and stores an embedding vector for a product description of each product.
**Note:** If you have more than 100k rows in a table, we recommend that you use the `embedding()` function for inline embedding generation. Don't use the `embedding()` function in this case to generate stored embeddings on existing data in a table.
    
    CREATE TABLE product (
        id INT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        category VARCHAR(255),
        color VARCHAR(255),
        embedding vector(768) GENERATED ALWAYS AS (embedding('text-embedding-004', description)) STORED
      );
    

  2. Run the following query to create a `product_inventory` table that stores information about available inventory and corresponding prices.
         
         CREATE TABLE product_inventory (
           id INT PRIMARY KEY,
           product_id INT REFERENCES product(id),
           inventory INT,
           price DECIMAL(10,2)
         );
         

  3. Run the following query to insert product data into the `product` table:
         
         INSERT INTO product (id, name, description,category, color) VALUES
         (1, 'Stuffed Elephant', 'Soft plush elephant with floppy ears.', 'Plush Toys', 'Gray'),
         (2, 'Remote Control Airplane', 'Easy-to-fly remote control airplane.', 'Vehicles', 'Red'),
         (3, 'Wooden Train Set', 'Classic wooden train set with tracks and trains.', 'Vehicles', 'Multicolor'),
         (4, 'Kids Tool Set', 'Toy tool set with realistic tools.', 'Pretend Play', 'Multicolor'),
         (5, 'Play Food Set', 'Set of realistic play food items.', 'Pretend Play', 'Multicolor'),
         (6, 'Magnetic Tiles', 'Set of colorful magnetic tiles for building.', 'Construction Toys', 'Multicolor'),
         (7, 'Kids Microscope', 'Microscope for kids with different magnification levels.', 'Educational Toys', 'White'),
         (8, 'Telescope for Kids', 'Telescope designed for kids to explore the night sky.', 'Educational Toys', 'Blue'),
         (9, 'Coding Robot', 'Robot that teaches kids basic coding concepts.', 'Educational Toys', 'White'),
         (10, 'Kids Camera', 'Durable camera for kids to take pictures and videos.', 'Electronics', 'Pink'),
         (11, 'Walkie Talkies', 'Set of walkie talkies for kids to communicate.', 'Electronics', 'Blue'),
         (12, 'Karaoke Machine', 'Karaoke machine with built-in microphone and speaker.', 'Electronics', 'Black'),
         (13, 'Kids Drum Set', 'Drum set designed for kids with adjustable height.', 'Musical Instruments', 'Blue'),
         (14, 'Kids Guitar', 'Acoustic guitar for kids with nylon strings.', 'Musical Instruments', 'Brown'),
         (15, 'Kids Keyboard', 'Electronic keyboard with different instrument sounds.', 'Musical Instruments', 'Black'),
         (16, 'Art Easel', 'Double-sided art easel with chalkboard and whiteboard.', 'Arts & Crafts', 'White'),
         (17, 'Finger Paints', 'Set of non-toxic finger paints for kids.', 'Arts & Crafts', 'Multicolor'),
         (18, 'Modeling Clay', 'Set of colorful modeling clay.', 'Arts & Crafts', 'Multicolor'),
         (19, 'Watercolor Paint Set', 'Watercolor paint set with brushes and palette.', 'Arts & Crafts', 'Multicolor'),
         (20, 'Beading Kit', 'Kit for making bracelets and necklaces with beads.', 'Arts & Crafts', 'Multicolor'),
         (21, '3D Puzzle', '3D puzzle of a famous landmark.', 'Puzzles', 'Multicolor'),
         (22, 'Race Car Track Set', 'Race car track set with cars and accessories.', 'Vehicles', 'Multicolor'),
         (23, 'RC Monster Truck', 'Remote control monster truck with oversized tires.', 'Vehicles', 'Green'),
         (24, 'Train Track Expansion Set', 'Expansion set for wooden train tracks.', 'Vehicles', 'Multicolor');
         

  4. Optional: To verify that the data is inserted in the `product` table, run the following query:
         
         SELECT * FROM product;
         

  5. Run the following query to insert inventory data into the `product_inventory` table:
         
         INSERT INTO product_inventory (id, product_id, inventory, price) VALUES
         (1, 1, 9, 13.09),
         (2, 2, 40, 79.82),
         (3, 3, 34, 52.49),
         (4, 4, 9, 12.03),
         (5, 5, 36, 71.29),
         (6, 6, 10, 51.49),
         (7, 7, 7, 37.35),
         (8, 8, 6, 10.87),
         (9, 9, 7, 42.47),
         (10, 10, 3, 24.35),
         (11, 11, 4, 10.20),
         (12, 12, 47, 74.57),
         (13, 13, 5, 28.54),
         (14, 14, 11, 25.58),
         (15, 15, 21, 69.84),
         (16, 16, 6, 47.73),
         (17, 17, 26, 81.00),
         (18, 18, 11, 91.60),
         (19, 19, 8, 78.53),
         (20, 20, 43, 84.33),
         (21, 21, 46, 90.01),
         (22, 22, 6, 49.82),
         (23, 23, 37, 50.20),
         (24, 24, 27, 99.27);
         

  6. Run the following vector search query to search for products that are similar to the word `music`. Even though the word `music` isn't explicitly mentioned in the product description, the result shows products that are relevant to the query:
         
         SELECT * FROM product
         ORDER BY embedding <=> embedding('text-embedding-005', 'music')::vector
         LIMIT 3;
         

If you perform a basic vector search without creating an index, AlloyDB AI uses KNN, which provides efficient recall; however, at scale, using KNN might impact performance. For better query performance, we recommend that you use the ScaNN index for ANN search, which provides high recall with low latencies.

If you don't create an index, then by default AlloyDB Omni uses KNN.




## Create a ScaNN index on the products table

**Important:** The examples in this tutorial are intended for demonstration purposes only. We recommend that you only create ScaNN indexes on tables that are larger than 10K.

Run the following query to create a `product_index` ScaNN index on the `product` table:
    
    
      CREATE INDEX product_index ON product
      USING scann (embedding cosine)
      WITH (num_leaves=5);
    

The `num_leaves` parameter indicates the number of leaf nodes that the tree-based index builds the index with. For more information about how to tune this parameter, see [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes).

## Perform a vector search

Run the following vector search query that tries to find products that are similar to the natural language query `music`. Even though the word `music` isn't included in the product description, the result shows products that are relevant to the query:
    
    
    SET LOCAL scann.num_leaves_to_search = 2;
    
    SELECT * FROM product
    ORDER BY embedding <=> embedding('text-embedding-005', 'music')::vector
      LIMIT 3;
    

The `scann.num_leaves_to_search` query parameter controls the number of leaf nodes that are searched during a similarity search. The `num_leaves` and `scann.num_leaves_to_search` parameter values help to balance query performance and recall.

## Perform a vector search that uses a filter and a join

Run the following complex vector search query, which returns relevant results that satisfy the query conditions, even with filters:
    
    
    SET LOCAL scann.num_leaves_to_search = 2;
    
    SELECT * FROM product p
    JOIN product_inventory pi ON p.id = pi.product_id
    WHERE pi.price < 80.00
    ORDER BY embedding <=> embedding('text-embedding-005', 'music')::vector
    LIMIT 3;
    

## Clean up

### Delete your database cluster
    
    
          kubectl patch dbclusters.alloydbomni.dbadmin.goog my-db-cluster -p '{"spec":{"isDeleted":true}}' --type=merge

### Uninstall the AlloyDB Omni operator

To uninstall the AlloyDB Omni Kubernetes operator from your Kubernetes cluster, complete these steps:

  1. Delete all of your database clusters:
         
         for ns in $(kubectl get dbclusters.alloydbomni.dbadmin.goog --all-namespaces -o=jsonpath='{range .items[*]}{.metadata.namespace}{"\n"}{end}'); do
               for cr in $(kubectl get dbclusters.alloydbomni.dbadmin.goog -n $ns -o=jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'); do
               kubectl patch dbclusters.alloydbomni.dbadmin.goog $cr -n $ns --type=merge -p '{"spec":{"isDeleted":true}}'
               done
               done
           ```

  2. Verify that the AlloyDB Omni Kubernetes operator deleted all of your database clusters by running the following command:
         
         kubectl get dbclusters.alloydbomni.dbadmin.goog --all-namespaces

  3. Delete other resources that the AlloyDB Omni Kubernetes operator created:
         
         kubectl delete failovers.alloydbomni.dbadmin.goog --all --all-namespaces
             kubectl delete restores.alloydbomni.dbadmin.goog --all --all-namespaces
             kubectl delete switchovers.alloydbomni.dbadmin.goog --all --all-namespaces

  4. Uninstall the AlloyDB Omni Kubernetes operator:
         
         helm uninstall alloydbomni-operator --namespace alloydb-omni-system

  5. Clean up secrets, custom resource descriptions, and namespaces related to the AlloyDB Omni Kubernetes operator:
         
         kubectl delete certificate -n alloydb-omni-system --all
             kubectl get secrets --all-namespaces -o custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name,ANNOTATION:.metadata.annotations.cert-manager\.io/issuer-name | grep -E 'alloydbomni|dbs-al' | awk '{print $1 " " $2}' | xargs -n 2 kubectl delete secret -n
             kubectl delete crd -l alloydb-omni=true
             kubectl delete ns alloydb-omni-system




## What's next

  * Learn how to [build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai).
  * [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/store-index-query-vectors). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
