---
url: https://docs.cloud.google.com/memorystore/docs/redis/scale-instances/
title: Scale Redis instances \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:50.450123+00:00
---

# Scale Redis instances  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/scale-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Scale Redis instances Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are looking for the Memorystore for Redis Cluster documentation, see [Scale instance capacity](https://docs.cloud.google.com/memorystore/docs/cluster/scale-instance-capacity).

This page describes how to scale Memorystore for Redis instances. For more information about an instance's behavior during scaling, see [Instance scaling behavior](https://docs.cloud.google.com/memorystore/docs/redis/scaling-behavior).

## Best practices for scaling an instance

  * We recommend [exporting](https://docs.cloud.google.com/memorystore/docs/redis/export-data) your instance data before scaling your operation.

  * For Standard Tier instances, to increase the speed and reliability of your scaling operation, scale your instance during periods of low instance traffic. To learn how to monitor instance traffic, see [Monitoring Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances).

  * When reducing a Standard Tier instance's capacity, you must choose a size greater than the amount of data being stored or scaling fails.

    * For example, if you have a 10 GB instance that has 5.5 GB of data stored in it, you can resize the instance to a minimum of 6 GB. The amount of storage your instance uses is visible on its details page in the Google Cloud console.



## Instance scaling instructions

### Console

  1. Go to the Memorystore for Redis page in the Google Cloud console.   
[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)
  2. Click the Instance ID of the instance you want to resize.
  3. Click **Edit**.
  4. Under **Capacity** , enter a new size in the field to update the instance's capacity.
  5. Click **Save**.



### Gcloud

Enter the following command, replacing variables with appropriate values:
    
    
    gcloud redis instances update instance-id --region=region-id --size=size

Where:

  * instance-id is your instance ID.
  * region-id is the region ID.
  * size is the desired instance size in gibibytes (GiB).



For example:
    
    
     gcloud redis instances update myinstance --region=us-central1 --size=100
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
