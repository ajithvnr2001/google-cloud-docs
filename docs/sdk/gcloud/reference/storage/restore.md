---
url: https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore/
title: gcloud storage restore \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:26:01.677150+00:00
---

# gcloud storage restore  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/storage/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud storage restore Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud storage restore - restore one or more soft-deleted objects 
SYNOPSIS
    

`gcloud storage restore` [`URLS` …] [`--all-versions`, `-a`] [`--async`] [`--[no-]preserve-acl`, `-p`] [`--read-paths-from-stdin`, `-I`] [`--allow-overwrite` `--created-after-time`=`CREATED_AFTER_TIME` `--created-before-time`=`CREATED_BEFORE_TIME` `--deleted-after-time`=`DELETED_AFTER_TIME` `--deleted-before-time`=`DELETED_BEFORE_TIME`] [`--if-generation-match`=`GENERATION` `--if-metageneration-match`=`METAGENERATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The restore command restores soft-deleted resources: 
    
    
    gcloud storage restore url…

EXAMPLES
     Restore soft-deleted version of bucket with generations: 
    
    
    gcloud storage restore gs://bucket#123

Restore several soft-deleted buckets with generations: 
    
    
    gcloud storage restore gs://bucket1#123 gs://bucket2#456

Restore latest soft-deleted version of object in a bucket. 
    
    
    gcloud storage restore gs://bucket/file1.txt

Restore a specific soft-deleted version of object in a bucket by specifying the generation. 
    
    
    gcloud storage restore gs://bucket/file1.txt#123

Restore all soft-deleted versions of object in a bucket. 
    
    
    gcloud storage restore gs://bucket/file1.txt --all-versions

Restore several objects in a bucket (with or without generation): 
    
    
    gcloud storage restore gs://bucket/file1.txt gs://bucket/file2.txt#456

Restore the latest soft-deleted version of all text objects in a bucket: 
    
    
    gcloud storage restore gs://bucket/**.txt

Restore a list of objects read from stdin (with or without generation): 
    
    
    cat list-of-files.txt | gcloud storage restore --read-paths-from-stdin

Restore object with its original ACL policy: 
    
    
    gcloud storage restore gs://bucket/file1.txt --preserve-acl

Restore all objects in a bucket asynchronously: 
    
    
    gcloud storage restore gs://bucket/** --async

Restore all text files in a bucket asynchronously: 
    
    
    gcloud storage restore gs://bucket/**.txt --async

Restore objects created within a specific time range: 
    
    
    gcloud storage restore gs://bucket/** --async --created-after-time="2023-01-01T00:00:00Z" --created-before-time="2023-01-31T23:59:59Z"

Restore objects soft-deleted within a specific time range: 
    
    
    gcloud storage restore gs://bucket/** --async --deleted-after-time="2023-01-01T00:00:00Z" --deleted-before-time="2023-01-31T23:59:59Z"

Restore objects using a combination of creation and deletion time filters: 
    
    
    gcloud storage restore gs://bucket/** --async --allow-overwrite --created-after-time="2023-01-01T00:00:00Z" --deleted-after-time="2023-01-01T00:00:00Z"

This command filters the objects that were live at 2023-01-01T00:00:00Z and then soft-deleted afterwards. This combination of filters is especially helpful if there is a period of erroneous overwrites. They allow you to go back to the point just before the overwrites began. You will also need to set the `--allow-overwrite` option to true. 

POSITIONAL ARGUMENTS
    

[`URLS` …]
     The url of objects to list. 
FLAGS
    

SYNCHRONOUS RESTORE OPTIONS 
`--all-versions`, `-a`
     Restores all versions of soft-deleted objects. 

This flag is only useful for buckets with [object versioning] (https://cloud.google.com/storage/docs/object-versioning) enabled. In this case, the latest soft-deleted version will become live and the previous generations will become noncurrent. 

If versioning is disabled, the latest soft-deleted version will become live and previous generations will be soft-deleted again. 

This flag disables parallelism to preserve version order. 

`--async`
     Initiates an asynchronous bulk restore operation on the specified bucket. 
`--[no-]preserve-acl`, `-p`
     Preserves ACLs when copying in the cloud. This option is Cloud Storage-only, and you need OWNER access to all copied objects. If all objects in the destination bucket should have the same ACL, you can also set a default object ACL on that bucket instead of using this flag. Preserving ACLs is the default behavior for updating existing objects. Use `--preserve-acl` to enable and `--no-preserve-acl` to disable. 
`--read-paths-from-stdin`, `-I`
     Read the list of URLs from stdin. 
BULK RESTORE OPTIONS 
`--allow-overwrite`
     If included, live objects will be overwritten. If versioning is enabled, this will result in a noncurrent object. If versioning is not enabled, this will result in a soft-deleted object. 
`--created-after-time`=`CREATED_AFTER_TIME`
     Restores only the objects that were created after this time. 
`--created-before-time`=`CREATED_BEFORE_TIME`
     Restores only the objects that were created before this time. 
`--deleted-after-time`=`DELETED_AFTER_TIME`
     Restores only the objects that were soft-deleted after this time. 
`--deleted-before-time`=`DELETED_BEFORE_TIME`
     Restores only the objects that were soft-deleted before this time. 
PRECONDITION FLAGS
    

`--if-generation-match`=`GENERATION`
     Execute only if the generation matches the generation of the requested object. 
`--if-metageneration-match`=`METAGENERATION`
     Execute only if the metageneration matches the metageneration of the requested object. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha storage restore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/restore)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
