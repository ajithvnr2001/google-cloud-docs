---
url: https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count/
title: Scale replica count \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:47.913681+00:00
---

# Scale replica count  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Scale replica count Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to scale the number of replicas used by your instance.

## Update replica count for an existing instance

Updating the number of replicas for an instance allows you to enable replicas, disable replicas, and change the number of replicas per shard.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click your instance ID.

  3. In the **Configurations** section, click the pencil icon next to **Replica Count**.

  4. From the **Replicas** menu, select the number of replicas.

  5. Click **Update instance**.




### gcloud

To update the number of replicas, run the `update` command:
    
    
    gcloud memorystore instances update INSTANCE \
      --location=REGION_ID \
      --replica-count=REPLICA_COUNT
    

Replace the following:

  * INSTANCE is the ID of the Memorystore for Valkey instance.
  * REGION_ID is the region where the instance is located.
  * REPLICA_COUNT is the number of replicas (per shard) for your instance. Acceptable values are `0`-`5`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
