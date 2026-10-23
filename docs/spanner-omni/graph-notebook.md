---
url: https://docs.cloud.google.com/spanner-omni/graph-notebook/
title: Explore graph data with the Spanner Graph notebook \u00a0|\u00a0 Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:13.422652+00:00
---

# Explore graph data with the Spanner Graph notebook  |  Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/graph-notebook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Explore graph data with the Spanner Graph notebook Stay organized with collections  Save and categorize content based on your preferences. 

The Spanner Graph notebook lets you explore your data visually in a notebook environment (such as Jupyter Notebook or JupyterLab). Using [Graph Query Language](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/graph-intro) (GQL) query syntax, you can extract graph insights and relationship patterns, including node and edge properties and neighbor expansion analysis. The tool also provides graph schema metadata visualization, tabular results inspection, and diverse layout topologies.

The Spanner Graph notebook supports plain text, TLS, and mutual TLS (mTLS) connections.

## Install the Spanner Graph notebook

To install the [Spanner Graph notebook](https://github.com/cloudspannerecosystem/spanner-graph-notebook) package (version 1.1.11 or later) in your Python or Jupyter environment, run the following `pip` command:
    
    
    pip install "spanner-graph-notebook>=1.1.11"
    

## Load the Spanner Graph extension

To load the Spanner Graph extension in your Jupyter notebook, use the following command:
    
    
    %load_ext spanner_graphs
    

## Connect to your database

To connect to your Spanner Omni database, make sure you've loaded the extension, then use the `%%spanner_graph` cell command:

###  Plain text 

To establish a plain-text connection, run the following:
    
    
    %%spanner_graph --instance_type omni --endpoint OMNI_ENDPOINT:PORT --database DATABASE_NAME --use_plain_text
    

Replace the following:

  * `OMNI_ENDPOINT`: the hostname or IP address of your Spanner Omni instance.

  * `PORT`: the port number of your Spanner Omni instance.

  * `DATABASE_NAME`: the name of your Spanner Omni database.




###  TLS 

To establish a TLS connection, specify the path to the CA certificate:
    
    
    %%spanner_graph --instance_type omni --endpoint OMNI_ENDPOINT:PORT --database DATABASE_NAME --ca_certificate PATH_TO_CA_CERT
    

Replace the following:

  * `OMNI_ENDPOINT`: the hostname or IP address of your Spanner Omni instance.

  * `PORT`: the port number of your Spanner Omni instance.

  * `DATABASE_NAME`: the name of your Spanner Omni database.

  * `PATH_TO_CA_CERT`: the path to your CA certificate file.




###  mTLS 

To establish an mTLS connection, specify the CA certificate, client certificate, and private client key:
    
    
    %%spanner_graph --instance_type omni --endpoint OMNI_ENDPOINT:PORT --database DATABASE_NAME --ca_certificate PATH_TO_CA_CERT --client_certificate PATH_TO_CLIENT_CERT --client_key PATH_TO_CLIENT_KEY
    

Replace the following:

  * `OMNI_ENDPOINT`: the hostname or IP address of your Spanner Omni instance.

  * `PORT`: the port number of your Spanner Omni instance.

  * `DATABASE_NAME`: the name of your Spanner Omni database.

  * `PATH_TO_CA_CERT`: the path to your CA certificate file.

  * `PATH_TO_CLIENT_CERT`: the path to your client certificate file.

  * `PATH_TO_CLIENT_KEY`: the path to your client private key file.




## Visualize a query

To visualize graph query results in the notebook, your queries must return graph elements in JSON format using the `SAFE_TO_JSON` or `TO_JSON` function. Full graph paths are recommended for data completeness and ease of visualization.

### Example: Return a path as JSON

The following example visualizes the path connecting a person to the accounts they own:
    
    
    %%spanner_graph --instance_type omni --endpoint OMNI_ENDPOINT:PORT --database DATABASE_NAME --use_plain_text
    
    GRAPH FinGraph
    MATCH query_path = (person:Person {id: 5})-[owns:Owns]->(accnt:Account)
    RETURN SAFE_TO_JSON(query_path) AS path_json
    

### Example: Multi-hop graph query

The following example visualizes a variable-length path (1 to 3 hops) of transfers between accounts:
    
    
    %%spanner_graph --instance_type omni --endpoint OMNI_ENDPOINT:PORT --database DATABASE_NAME --use_plain_text
    
    GRAPH FinGraph
    MATCH query_path = (src:Account {id: 9})-[edge:Transfers]->{1,3}(dst:Account)
    RETURN SAFE_TO_JSON(query_path) AS path_json
    

### Example: Return multiple paths

The following example returns and visualizes multiple graph paths in a single query:
    
    
    %%spanner_graph --instance_type omni --endpoint OMNI_ENDPOINT:PORT --database DATABASE_NAME --use_plain_text
    
    GRAPH FinGraph
    MATCH path_1 = (person:Person {id: 5})-[:Owns]->(accnt:Account),
          path_2 = (src:Account {id: 9})-[:Transfers]->(dst:Account)
    RETURN SAFE_TO_JSON(path_1) AS path_1,
            SAFE_TO_JSON(path_2) AS path_2
    

## What's next

  * [Use the Python client library with Spanner Omni](https://docs.cloud.google.com/spanner-omni/python).

  * [Learn about using Spanner Graph with Spanner Omni](https://docs.cloud.google.com/spanner-omni/spanner-graph-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
