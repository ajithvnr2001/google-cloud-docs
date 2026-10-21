---
url: https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/delete/
title: gcloud storage buckets notifications delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:03.675973+00:00
---

# gcloud storage buckets notifications delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud storage buckets notifications delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud storage buckets notifications delete - delete notification configurations from a bucket 
SYNOPSIS
    

`gcloud storage buckets notifications delete` `URLS` [`URLS` …] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud storage buckets notifications delete` deletes notification configurations from a bucket. If a notification configuration name is passed as a parameter, that configuration alone is deleted. If a bucket name is passed, all notification configurations associated with the bucket are deleted. 

Cloud Pub/Sub topics associated with this notification configuration are not deleted by this command. Those must be deleted separately, for example with the command "gcloud pubsub topics delete". 

EXAMPLES
     Delete a single notification configuration (with ID 3) in the bucket `example-bucket`: 
    
    
    gcloud storage buckets notifications delete projects/_/buckets/example-bucket/notificationConfigs/3

Delete all notification configurations in the bucket `example-bucket`: 
    
    
    gcloud storage buckets notifications delete gs://example-bucket

POSITIONAL ARGUMENTS
    

`URLS` [`URLS` …]
     Specifies notification configuration names or buckets. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha storage buckets notifications delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/buckets/notifications/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
