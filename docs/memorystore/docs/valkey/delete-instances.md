---
url: https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances/
title: Delete instances \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:46.489498+00:00
---

# Delete instances  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Delete instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete instances in Memorystore for Valkey.

## Delete an instance

You can delete instances by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : If you delete an instance and create another instance with the same name, then Memorystore for Valkey assigns different IP addresses to the instance. If you hardcode the IP addresses from the instance that you delete into your client applications, then the clients can't connect to the instance. You must update the IP addresses to point to the instance's new [ discovery endpoints](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#discovery_endpoint).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance that you want to delete.

  3. **Optional**. If the instance that you want to delete is a secondary instance, then do the following:

     1. Click the expander arrow next to the primary instance that's the parent of the secondary instance.
     2. Click the link of the secondary instance.
  4. Click **Delete**.

  5. In the dialog, enter the instance ID, and then click **Delete**.




### gcloud

To delete an instance, use the [`gcloud memorystore instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/delete) command.
    
    
    gcloud memorystore instances delete INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance that you want to delete
  * PROJECT_ID: your project ID
  * REGION_ID: the region where your instance is located



For example:
    
    
    gcloud memorystore instances delete my-instance \
    --project=my-project \
    --location=us-central1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
