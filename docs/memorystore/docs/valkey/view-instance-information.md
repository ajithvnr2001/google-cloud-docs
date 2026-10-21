---
url: https://docs.cloud.google.com/memorystore/docs/valkey/view-instance-information/
title: View instance information \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:18.005115+00:00
---

# View instance information  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/view-instance-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  View instance information Stay organized with collections  Save and categorize content based on your preferences. 

Viewing high-level information about Memorystore for Valkey instances is essential to obtain a comprehensive snapshot of the instance's state, configuration, and connectivity.

The following are sample use cases for viewing summary information about Memorystore for Valkey instances:

  * **Retrieve connection endpoints** : For Cluster Mode Enabled instances, you can retrieve the [discovery endpoint](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#discovery_endpoint), which consists of an IP address and port number. For Cluster Mode Disabled instances, you can obtain the [primary](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#primary_endpoint) and [reader](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#reader_endpoint) endpoints that you need to configure your client applications to connect to the instance.
  * **Verify custom configurations** : view configuration parameters that a user applies to an instance. For example, you can obtain the value that a user sets for the [`maxmemory-policy`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters) parameter.
  * **Check information about nodes and shards** : obtain information about the nodes and shards associated with an instance. This includes the number of shards, the node type, and the number of replicas that each shard has.
  * **Confirm data resiliency settings** : verify active [persistence](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview) modes for Redis Database (RDB) snapshots and Append-Only File (AOF) log files, as well as the status of whether an instance is protected from accidental deletion.



## View instance summary information

You can view summary information about an instance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of an instance about which you want to view summary information.




### gcloud

To view summary information about an instance, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command:
    
    
    gcloud memorystore instances describe INSTANCE_ID \
    --location=REGION_ID
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance about which you want to view summary information
  * REGION_ID: the region where the instance is located



For example:
    
    
    gcloud memorystore instances describe my-instance \
    --location=us-central1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
