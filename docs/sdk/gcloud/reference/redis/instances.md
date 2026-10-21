---
url: https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/
title: gcloud redis instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:17:57.839539+00:00
---

# gcloud redis instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud redis instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud redis instances - manage Cloud Memorystore Redis instances 
SYNOPSIS
    

`gcloud redis instances` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create an instance with the name `my-redis-instance`, run: 
    
    
    [gcloud redis instances create](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/create) my-redis-instance

To delete an instance with the name `my-redis-instance`, run: 
    
    
    [gcloud redis instances delete](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/delete) my-redis-instance

To display the details for an instance with the name `my-redis-instance`, run: 
    
    
    [gcloud redis instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/describe) my-redis-instance

To list all the instances, run: 
    
    
    [gcloud redis instances list](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/list)

To set the label `env` to `prod` for an instance with the name `my-redis-instance`, run: 
    
    
    gcloud redis instances my-redis-instance --update-labels=env=prod

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/create)`
     Create a Memorystore Redis instance. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/delete)`
     Delete a Redis instance. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/describe)`
     Show metadata for a Memorystore Redis instance. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/export)`
     Export data from a Memorystore Redis instance to Google Cloud Storage. 
`[failover](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/failover)`
     Failover a standard tier Cloud Memorystore for Redis instance from the master node to its replica. 
`[get-auth-string](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/get-auth-string)`
     Show AUTH string for a Memorystore Redis instance. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/import)`
     Import data to a Memorystore Redis instance from Google Cloud Storage. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/list)`
     List Memorystore Redis instances. 
`[reschedule-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance)`
     Reschedule maintenance window for a Redis instance. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/update)`
     Update Memorystore Redis instances. 
`[upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/upgrade)`
     Upgrade a Memorystore for Redis instance to a specified Redis version. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha redis instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/instances)
    
    
    [gcloud beta redis instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/redis/instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
