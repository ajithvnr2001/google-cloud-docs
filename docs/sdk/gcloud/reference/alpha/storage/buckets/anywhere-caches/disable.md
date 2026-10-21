---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/buckets/anywhere-caches/disable/
title: gcloud alpha storage buckets anywhere-caches disable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:09:41.712713+00:00
---

# gcloud alpha storage buckets anywhere-caches disable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/buckets/anywhere-caches/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage buckets anywhere-caches disable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage buckets anywhere-caches disable - disable Anywhere Cache instances 
SYNOPSIS
    

`gcloud alpha storage buckets anywhere-caches disable` `ID` [`ID` …] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Disables one or more Anywhere Cache instances. 

The cache instance will be set to DISABLED state. The existing entries can be read from the cache but new entries will not be written to the cache. The L4 SSD cache would not be deleted by the cache manager until the min TTL (1h) has been reached (cache instance is kept for at least 1h). Google Cloud Storage defines the min TTL which is applied to all cache instances. Cach disablement could be canceled by using anywhere-caches resume command before the instance is deleted. 

EXAMPLES
     The following command disables the anywhere cache instance of bucket ``my-bucket`` having anywhere_cache_id ``my-cache-id``: 
    
    
    gcloud alpha storage buckets anywhere-caches disable my-bucket/my-cache-id

POSITIONAL ARGUMENTS
    

`ID` [`ID` …]
     Identifiers for a Anywhere Cache instance. They are combination of bucket_name/anywhere_cache_id. For example : test-bucket/my-cache-id. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage buckets anywhere-caches disable](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/disable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
