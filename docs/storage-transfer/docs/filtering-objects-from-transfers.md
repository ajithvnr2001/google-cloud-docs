---
url: https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers/
title: Filter source objects by prefix \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:31.248947+00:00
---

# Filter source objects by prefix  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Filter source objects by prefix Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to use include and exclude prefixes to control which files are transferred.

## Overview

Storage Transfer Service supports filtering data from Amazon S3, Microsoft Azure Blob Storage and Cloud Storage sources using prefixes. A prefix is a string of characters at the beginning of a path that specifies a set of objects.

You can use prefix filters in three ways:

  * **Include prefixes** : Only objects matching the specified prefixes are transferred.

  * **Exclude prefixes** : Objects matching the specified prefixes are omitted from the transfer.

  * **Both together** : You can use include and exclude prefixes simultaneously for more granular control. When used together, every exclude prefix must begin with one of the specified include prefixes.




If you don't specify any prefixes, all objects in the source bucket are transferred.

Prefix filters can be combined with [glob patterns](https://docs.cloud.google.com/storage-transfer/docs/filter-by-glob-pattern), [last modified time filters](https://docs.cloud.google.com/storage-transfer/docs/filter-by-last-modified), and [S3 storage class filters](https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class).

## Rules

The following rules apply to prefixes:

  * **No leading slashes** : Do not include a leading slash in a prefix. For the path `s3://my-bucket/logs/2025/requests.gz`, the correct prefix is `logs/2025/requests.gz`.

  * **Partial matches** : Prefixes work by partial matching. For example, the prefix `path` matches both `path_1/` and `path_2/`.

  * **No wildcards** : Wildcards are not supported.

  * **Relative to source folder** : If your transfer source includes a path or folder, prefixes are relative to that path or folder. See Interaction with source path or folder for details.

  * **Distinct include prefixes** : Each include prefix must define a unique part of the object namespace. You cannot use an include prefix that is already covered by another include prefix. For example, you cannot specify both `data/` and `data/reports/` as include prefixes.

  * **Exclude prefix dependency** : When using include and exclude prefixes together, every exclude prefix must begin with one of the specified include prefixes. For example, if `path` is an include prefix, valid exclude prefixes could be `path/b` or `pathway`. This rule does not apply if you are only using exclude prefixes.

  * **Maximum of 1000 prefixes** : A single transfer job supports up to 1000 prefixes. You can split a transfer into multiple jobs if additional prefixes are required.




For more general information about prefixes, see [Listing Keys Hierarchically Using a Prefix and Delimiter](https://docs.aws.amazon.com/AmazonS3/latest/dev/ListingKeysHierarchy.html) in the Amazon S3 documentation or the [Objects list method](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) for Cloud Storage.

## Interaction with other filter types

When you use multiple filters, Storage Transfer Service applies them in the following order:

  1. **Include prefixes** : Narrows down the objects to consider.

  2. **Object conditions** (glob pattern, last modified time, and S3 storage class): Filters the objects that matched the include prefix. An object must match all specified object conditions to be included in the transfer.

  3. **Exclude prefixes** : Removes objects from the result.




Learn more about filtering with [glob patterns](https://docs.cloud.google.com/storage-transfer/docs/filter-by-glob-pattern), [last modified time](https://docs.cloud.google.com/storage-transfer/docs/filter-by-last-modified), and [S3 storage class](https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class).

## Interaction with source path or folder

Include and exclude filters are relative to any path or folder that you specify for the source.

For example, if your source is `gs://bucketA/alpha`, and you want to specify a filter for `gs://bucketA/alpha/beta`:

**Correct**

  * Source path: `gs://bucketA/alpha`
  * Exclude prefix: `beta/`
  * Result: This correctly excludes `gs://bucketA/alpha/beta`



**Incorrect**

  * Source path: `gs://bucketA/alpha`
  * Exclude prefix: `alpha/beta/`
  * Result: This incorrectly defines a filter for `gs://bucketA/alpha/alpha/beta`



## Specify prefixes

###  Cloud console 

To specify include and exclude prefixes using the Google Cloud console, enter the values when [creating a new transfer](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) or when [updating an existing transfer](https://docs.cloud.google.com/storage-transfer/docs/manage-transfers#update-job).

###  gcloud CLI 

To specify include and exclude prefixes using the `gcloud` CLI, pass the `--include-prefixes` and `--exclude-prefixes` flags to the `gcloud transfer jobs create` command or the `gcloud transfer jobs update` command:
    
    
    gcloud transfer jobs create SOURCE DESTINATION \
      --include-prefixes="path_1/,path_2/" --exclude-prefixes="path_1/subpath_2/"
    

Separate multiple prefixes with commas, omitting spaces after the commas. For example, `--include-prefixes="foo,bar"`.

###  REST 

To specify include and exclude prefixes using the REST API, use the `includePrefixes[]` and `excludePrefixes[]` fields:
    
    
    {
        "description": "Transfer with prefixes",
        "status": "ENABLED",
        "projectId": "PROJECT_ID",
        "schedule": {
            "scheduleStartDate": {
                "day": 1,
                "month": 1,
                "year": 2015
            },
            "startTimeOfDay": {
                "hours": 1,
                "minutes": 1
            }
        },
        "transferSpec": {
            "gcsDataSource": {
                "bucketName": "SOURCE_BUCKET"
            },
            "gcsDataSink": {
                "bucketName": "DESTINATION_BUCKET"
            },
            "transferOptions": {
                "deleteObjectsFromSourceAfterTransfer": true
            },
            "objectConditions": {
                "includePrefixes": [
                    "path_1/",
                    "path_2/"
                ],
                "excludePrefixes": [
                    "path_1/subpath_2/object_5"
                ]
            }
        }
    }
    

For more information, refer to the [`ObjectConditions`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#objectconditions) reference.

## Example objects and paths

The following examples use this sample list of objects:
    
    
    xx://bucketname/object_1
    xx://bucketname/object_2
    xx://bucketname/path_1/object_3
    xx://bucketname/path_1/subpath_1/object_4
    xx://bucketname/path_1/subpath_2/object_5
    xx://bucketname/path_2/object_6
    xx://bucketname/path_2/subpath_3/object_7
    xx://bucketname/path_2/subpath_4/object_8
    

## Use include prefixes

To transfer only objects under `path_1/`, use the following prefix:
    
    
    path_1/
    

This includes objects under `path_1/`. The following objects are included in the transfer:
    
    
    ~~xx://bucketname/object_1~~
    ~~xx://bucketname/object_2~~
    xx://bucketname/path_1/object_3
    xx://bucketname/path_1/subpath_1/object_4
    xx://bucketname/path_1/subpath_2/object_5
    ~~xx://bucketname/path_2/object_6~~
    ~~xx://bucketname/path_2/subpath_3/object_7~~
    ~~xx://bucketname/path_2/subpath_4/object_8~~
    

You can specify multiple paths to include. For example, you can pass the following:
    
    
    path_1/subpath_2/
    path_1/subpath_3/
    

In this case, the transfer includes the following objects:
    
    
    ~~xx://bucketname/object_1~~
    ~~xx://bucketname/object_2~~
    ~~xx://bucketname/path_1/object_3~~
    ~~xx://bucketname/path_1/subpath_1/object_4~~
    xx://bucketname/path_1/subpath_2/object_5
    ~~xx://bucketname/path_2/object_6~~
    xx://bucketname/path_2/subpath_3/object_7
    ~~xx://bucketname/path_2/subpath_4/object_8~~
    

Partial matches are supported. For example:
    
    
    path
    

The following objects are transferred:
    
    
    ~~xx://bucketname/object_1~~
    ~~xx://bucketname/object_2~~
    xx://bucketname/path_1/object_3
    xx://bucketname/path_1/subpath_1/object_4
    xx://bucketname/path_1/subpath_2/object_5
    xx://bucketname/path_2/object_6
    xx://bucketname/path_2/subpath_3/object_7
    xx://bucketname/path_2/subpath_4/object_8
    

When you use include prefixes, paths that you don't specifically include aren't transferred to the Cloud Storage destination bucket.

## Exclude prefixes

Using exclude prefixes when creating a transfer instructs Storage Transfer Service to ignore the listed paths for transfer.

To exclude objects under `path_1/`, pass the following prefix:
    
    
    path_1/
    

This excludes objects under `path_1/`. In this case, the following objects are included in the transfer:
    
    
    xx://bucketname/object_1
    xx://bucketname/object_2
    ~~xx://bucketname/path_1/object_3~~
    ~~xx://bucketname/path_1/subpath_1/object_4~~
    ~~xx://bucketname/path_1/subpath_2/object_5~~
    xx://bucketname/path_2/object_6
    xx://bucketname/path_2/subpath_3/object_7
    xx://bucketname/path_2/subpath_4/object_8
    

You can specify multiple paths to exclude. For example, you can pass the following:
    
    
    path_1/subpath_2/
    path_2/subpath_3/
    

In this case, the transfer includes the following objects:
    
    
    xx://bucketname/object_1
    xx://bucketname/object_2
    xx://bucketname/path_1/object_3
    xx://bucketname/path_1/subpath_1/object_4
    ~~xx://bucketname/path_1/subpath_2/object_5~~
    xx://bucketname/path_2/object_6
    ~~xx://bucketname/path_2/subpath_3/object_7~~
    xx://bucketname/path_2/subpath_4/object_8
    

## Including and excluding paths simultaneously

You can apply an exclude prefix and an include prefix together, in which case the exclude prefix limits what the include prefix includes in the transfer.

When specifying both types of prefix, each exclude prefix must start with a path that is specified in an include prefix.

For example, to include objects under `path_1/` and exclude objects under `subpath_1/` pass the following:
    
    
    include: path_1/
    exclude: path_1/subpath_1/
    

In this case, the transfer includes the following objects:
    
    
    ~~xx://bucketname/object_1~~
    ~~xx://bucketname/object_2~~
    xx://bucketname/path_1/object_3
    ~~xx://bucketname/path_1/subpath_1/object_4~~
    xx://bucketname/path_1/subpath_2/object_5
    ~~xx://bucketname/path_2/object_6~~
    ~~xx://bucketname/path_2/subpath_3/object_7~~
    ~~xx://bucketname/path_2/subpath_4/object_8~~
    

To include all objects under `path_1/` and `path_2/`, except items in either `path_1/subpath_1/` or `path_2/subpath_3/`, pass the following:
    
    
    include: path_1/
             path_2/
    exclude: path_1/subpath_1/
             path_2/subpath_3/
    

In this case, the transfer includes the following objects:
    
    
    ~~xx://bucketname/object_1~~
    ~~xx://bucketname/object_2~~
    xx://bucketname/path_1/object_3
    ~~xx://bucketname/path_1/subpath_1/object_4~~
    xx://bucketname/path_1/subpath_2/object_5
    xx://bucketname/path_2/object_6
    ~~xx://bucketname/path_2/subpath_3/object_7~~
    xx://bucketname/path_2/subpath_4/object_8
    

## Common mistakes to avoid

Here are examples of incorrect configurations and how to fix them.

### Including a path that is used in another include prefix

An include prefix cannot be a subdirectory of another include prefix.

**Incorrect** : The prefix path_1/subpath_1 is already covered by path_1/.
    
    
    include: path_1/
             path_1/subpath_1
    

**Correct** : To fix this, remove the redundant, more specific prefix.
    
    
    include: path_1/
    

### The exclude prefix doesn't match an include prefix

When used together, an exclude prefix must start with one of the include prefixes.

**Incorrect** : The subpath_1 prefix does not start with either `path_1/` or `path_2/`.
    
    
    include: path_1/
             path_2/
    exclude: subpath_1
    

**Correct** : Ensure the exclude prefix contains the full path from an include prefix.
    
    
    include: path_1/
             path_2/
    exclude: path_1/subpath_1/
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
