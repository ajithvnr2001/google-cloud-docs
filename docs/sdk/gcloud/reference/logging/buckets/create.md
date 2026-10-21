---
url: https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/create/
title: gcloud logging buckets create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:53:48.118975+00:00
---

# gcloud logging buckets create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud logging buckets create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud logging buckets create - create a bucket 
SYNOPSIS
    

`gcloud logging buckets create` `BUCKET_ID` `--location`=`LOCATION` [`--async`] [`--cmek-kms-key-name`=`CMEK_KMS_KEY_NAME`] [`--description`=`DESCRIPTION`] [`--enable-analytics`] [`--index`=[`KEY`=`VALUE`, …,…]] [`--restricted-fields`=[`RESTRICTED_FIELD`,…]] [`--retention-days`=`RETENTION_DAYS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     After creating a bucket, use a log sink to route logs into the bucket. 
EXAMPLES
     To create a bucket 'my-bucket' in location 'global', run: 
    
    
    gcloud logging buckets create my-bucket --location=global --description="my custom bucket"

To create a bucket with extended retention, run: 
    
    
    gcloud logging buckets create my-bucket --location=global --retention-days=365

To create a bucket in cloud region 'us-central1', run: 
    
    
    gcloud logging buckets create my-bucket --location=us-central1

To create a bucket with custom index of 'jsonPayload.foo', run: 
    
    
    gcloud logging buckets create my-bucket --index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_STRING

To create a bucket with custom CMEK, run: 
    
    
    gcloud logging buckets create my-bucket --location=us-central1 --cmek-kms-key-name=CMEK_KMS_KEY_NAME

To asynchronously create a bucket enrolled into Log Analytics, run: 
    
    
    gcloud logging buckets create my-bucket --location=global --async --enable-analytics

POSITIONAL ARGUMENTS
    

`BUCKET_ID`
     ID of the bucket to create. 
REQUIRED FLAGS
    

`--location`=`LOCATION`
     Location in which to create the bucket. Once the bucket is created, the location cannot be changed. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--cmek-kms-key-name`=`CMEK_KMS_KEY_NAME`
     A valid `kms_key_name` will enable CMEK for the bucket. 
`--description`=`DESCRIPTION`
     A textual description for the bucket. 
`--enable-analytics`
     Whether to opt the bucket into Log Analytics. Once opted in, the bucket cannot be opted out of Log Analytics. 
`--index`=[`KEY`=`VALUE`, …,…]
     Specify an index to be added to the log bucket. This flag can be repeated. The ``fieldPath`` and ``type`` attributes are required. For example: \--index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_STRING. The following keys are accepted: 

`fieldPath`
     The LogEntry field path to index. For example: jsonPayload.request.status. Paths are limited to 800 characters and can include only letters, digits, underscores, hyphens, and periods. 
`type`
     The type of data in this index. For example: INDEX_TYPE_STRING Supported types are INDEX_TYPE_STRING and INDEX_TYPE_INTEGER. 
`--restricted-fields`=[`RESTRICTED_FIELD`,…]
     Comma-separated list of field paths that require permission checks in this bucket. The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation. 
`--retention-days`=`RETENTION_DAYS`
     The period logs will be retained, after which logs will automatically be deleted. The default is 30 days. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha logging buckets create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/buckets/create)
    
    
    [gcloud beta logging buckets create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/buckets/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
