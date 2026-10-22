---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-built-in-index-queries/
title: Query index \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:13.408973+00:00
---

# Query index  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-built-in-index-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Query index Stay organized with collections  Save and categorize content based on your preferences. 

Query index using internal datastore features

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Optimizing Indexes](https://docs.cloud.google.com/datastore/docs/concepts/optimize-indexes)



## Code sample

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    # For help authenticating your client, visit
    # https://cloud.google.com/docs/authentication/getting-started
    client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)()
    
    query_owner_id = client.[query](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_query)(kind="Photo", filters=[("owner_id", "=", "user1234")])
    
    query_size = client.[query](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_query)(kind="Photo", filters=[("size", "=", 2)])
    
    query_coloration = client.[query](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_query)(kind="Photo", filters=[("coloration", "=", 2)])

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
