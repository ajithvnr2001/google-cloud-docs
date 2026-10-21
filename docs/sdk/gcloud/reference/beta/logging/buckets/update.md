---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/buckets/update/
title: gcloud beta logging buckets update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:55:25.866943+00:00
---

# gcloud beta logging buckets update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/buckets/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta logging buckets update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta logging buckets update - update a bucket 
SYNOPSIS
    

`gcloud beta logging buckets update` `BUCKET_ID` `--location`=`LOCATION` [`--add-index`=[`KEY`=`VALUE`, …,…]] [`--async`] [`--clear-indexes`] [`--cmek-kms-key-name`=`CMEK_KMS_KEY_NAME`] [`--description`=`DESCRIPTION`] [`--enable-analytics`] [`--locked`] [`--remove-indexes`=[`FIELD` `PATH`,…]] [`--restricted-fields`=[`RESTRICTED_FIELD`,…]] [`--retention-days`=`RETENTION_DAYS`] [`--update-index`=[`KEY`=`VALUE`, …,…]] [`--billing-account`=`BILLING_ACCOUNT_ID` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update the properties of a bucket. 
EXAMPLES
     To update a bucket in your project, run: 
    
    
    gcloud beta logging buckets update my-bucket --location=global --description=my-new-description

To update a bucket in your project and remove all indexes, run: 
    
    
    gcloud beta logging buckets update my-bucket --location=global --clear-indexes

To update a bucket in your project and remove an index, run: 
    
    
    gcloud beta logging buckets update my-bucket --location=global --remove-indexes=jsonPayload.foo2

To update a bucket in your project and add an index, run: 
    
    
    gcloud beta logging buckets update my-bucket --location=global --add-index=fieldPath=jsonPayload.foo2,type=INDEX_TYPE_STRING

To update a bucket in your project and update an existing index, run: 
    
    
    gcloud beta logging buckets update my-bucket --location=global --update-index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_INTEGER

To update a bucket in your project and update existing cmek, run: 
    
    
    gcloud beta logging buckets update my-bucket --location=global --cmek-kms-key-name=CMEK_KEY_NAME

To asynchronously enroll a bucket in your project into Log Analytics, run: 
    
    
    gcloud beta logging buckets update my-bucket --location=global --async --enable-analytics

POSITIONAL ARGUMENTS
    

`BUCKET_ID`
     The id of the bucket to update. 
REQUIRED FLAGS
    

`--location`=`LOCATION`
     Location of the bucket. 
OPTIONAL FLAGS
    

`--add-index`=[`KEY`=`VALUE`, …,…]
     Add an index to be added to the log bucket. This flag can be repeated. The ``fieldPath`` and ``type`` attributes are required. For example: \--index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_STRING. The following keys are accepted: 

`fieldPath`
     The LogEntry field path to index. For example: jsonPayload.request.status. Paths are limited to 800 characters and can include only letters, digits, underscores, hyphens, and periods. 
`type`
     The type of data in this index. For example: INDEX_TYPE_STRING Supported types are strings and integers. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--clear-indexes`
     Remove all logging indexes from the bucket. 
`--cmek-kms-key-name`=`CMEK_KMS_KEY_NAME`
     A valid `kms_key_name` will enable CMEK for the bucket. 
`--description`=`DESCRIPTION`
     A new description for the bucket. 
`--enable-analytics`
     Whether to opt the bucket into Log Analytics. Once opted in, the bucket cannot be opted out of Log Analytics. 
`--locked`
     Lock the bucket and prevent it from being modified or deleted (unless it is empty). 
`--remove-indexes`=[`FIELD` `PATH`,…]
     Specify the field path of the logging index(es) to delete. 
`--restricted-fields`=[`RESTRICTED_FIELD`,…]
     A new set of restricted fields for the bucket. 
`--retention-days`=`RETENTION_DAYS`
     A new retention period for the bucket. 
`--update-index`=[`KEY`=`VALUE`, …,…]
     Update an index to be added to the log bucket. This will update the type of the index, and also update its createTime to the new update time. This flag can be repeated. The ``fieldPath`` and ``type`` attributes are required. For example: \--index=fieldPath=jsonPayload.foo,type=INDEX_TYPE_STRING. The following keys are accepted: 

`fieldPath`
     The LogEntry field path to index. For example: jsonPayload.request.status. Paths are limited to 800 characters and can include only letters, digits, underscores, hyphens, and periods. 
`type`
     The type of data in this index. For example: INDEX_TYPE_STRING Supported types are strings and integers. 
At most one of these can be specified: 

`--billing-account`=`BILLING_ACCOUNT_ID`
     Billing account of the bucket to update. 
`--folder`=`FOLDER_ID`
     Folder of the bucket to update. 
`--organization`=`ORGANIZATION_ID`
     Organization of the bucket to update. 
`--project`=`PROJECT_ID`
     Project of the bucket to update. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud logging buckets update](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update)
    
    
    [gcloud alpha logging buckets update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/buckets/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
