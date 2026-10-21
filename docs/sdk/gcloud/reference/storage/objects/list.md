---
url: https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/list/
title: gcloud storage objects list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:18:19.871578+00:00
---

# gcloud storage objects list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud storage objects list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud storage objects list - lists Cloud Storage objects 
SYNOPSIS
    

`gcloud storage objects list` `URLS` [`URLS` …] [`--additional-headers`=`HEADER`=`VALUE`] [`--exhaustive`] [`--fetch-encrypted-object-hashes`] [`--metadata-filter`=`METADATA_FILTER`] [`--next-page-token`=`NEXT_PAGE_TOKEN`] [`--raw`] [`--soft-deleted`] [`--stat`] [`--decryption-keys`=[`DECRYPTION_KEY`,…]] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     List Cloud Storage objects. 

Bucket URLs like `gs://bucket` match all the objects inside a bucket, but `gs://b*` fails because it matches a list of buckets. 

EXAMPLES
     List all objects in bucket ``my-bucket`` within current directory level: 
    
    
    gcloud storage objects list gs://my-bucket

List all objects across nested directories using wildcards (https://cloud.google.com/storage/docs/wildcards): 
    
    
    gcloud storage objects list gs://my-bucket/**

List all objects in bucket beginning with ``o´´, including objects across nested directories: 
    
    
    gcloud storage objects list gs://my-bucket/**/o*

List all objects within current directory of bucket with JSON formatting, only returning the value of the ``name`` metadata field: 
    
    
    gcloud storage objects list gs://my-bucket --format="json(name)"

List only contexts attached to objects as key value pairs. 
    
    
    gcloud storage objects list gs://my-bucket --format=contextsonly

POSITIONAL ARGUMENTS
    

`URLS` [`URLS` …]
     Specifies URL of objects to list. 
FLAGS
    

`--additional-headers`=`HEADER`=`VALUE`
     Includes arbitrary headers in storage API calls. Accepts a comma separated list of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides the default `storage/additional_headers` property value for this command invocation. 
`--exhaustive`
     For features like soft delete, the API may return an empty list. If present, continue querying. This may incur costs from repeated LIST calls and may not return any additional objects. 
`--fetch-encrypted-object-hashes`
     API requests to the LIST endpoint do not fetch the hashes for encrypted objects by default. If this flag is set, a GET request is sent for each encrypted object in order to fetch hashes. This can significantly increase the cost of the command. 
`--metadata-filter`=`METADATA_FILTER`
     Server side filtering for objects. Works only for Google Cloud Storage URLs. The filter only works for objects, and not directories or buckets, which means commands like `storage ls` and `storage du` will still list directories or buckets even if they do not contain any objects matching the filter. See <https://cloud.google.com/storage/docs/listing-objects#filter-by-object-contexts-syntax> for more details. 
`--next-page-token`=`NEXT_PAGE_TOKEN`
     Page token for resuming LIST calls. 
`--raw`
     Shows metadata in the format returned by the API instead of standardizing it. 
`--soft-deleted`
     Displays soft-deleted resources only. For objects, it will exclude live and noncurrent ones. 
`--stat`
     Emulates gsutil stat-style behavior. Does not show past object versions and changes output format. 
ENCRYPTION FLAGS
    

`--decryption-keys`=[`DECRYPTION_KEY`,…]
     A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4 base64-encoded AES256 strings) that will be used to decrypt Cloud Storage objects. Data encrypted with a customer-managed encryption key (CMEK) is decrypted automatically, so CMEKs do not need to be listed here. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha storage objects list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/objects/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
