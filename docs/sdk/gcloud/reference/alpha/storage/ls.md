---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ls/
title: gcloud alpha storage ls \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:46.920662+00:00
---

# gcloud alpha storage ls  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage ls Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage ls - list Cloud Storage buckets and objects 
SYNOPSIS
    

`gcloud alpha storage ls` [`PATH` …] [`--additional-headers`=`HEADER`=`VALUE`] [`--all-versions`, `-a`] [`--buckets`, `-b`] [`--etag`, `-e`] [`--exhaustive`] [`--fetch-encrypted-object-hashes`] [`--format`=`FORMAT`] [`--metadata-filter`=`METADATA_FILTER`] [`--next-page-token`=`NEXT_PAGE_TOKEN`] [`--read-paths-from-stdin`, `-I`] [`--readable-sizes`] [`--recursive`, `-R`, `-r`] [`--soft-deleted`] [`--full`, `-L` | `--json`, `-j` | `--long`, `-l`] [`--decryption-keys`=[`DECRYPTION_KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List your Cloud Storage buckets in a project and objects in a bucket. This command treats forward slashes in object names as directories. See below for examples of how to use wildcards to get the listing behavior you want. 
EXAMPLES
     The following command lists the buckets in the default project: 
    
    
    gcloud alpha storage ls

The following command lists the buckets in the specified project: 
    
    
    gcloud alpha storage ls --project=my-project

The following command lists the contents of a bucket: 
    
    
    gcloud alpha storage ls gs://my-bucket

You can use [wildcards](https://cloud.google.com/storage/docs/wildcards) to match multiple paths (including multiple buckets). Bucket wildcards are expanded to match only buckets contained in your current project. The following command matches ``.txt`` objects that begin with ``log`` and that are stored in buckets in your project that begin with ``my-b``: 
    
    
    gcloud alpha storage ls gs://my-b*/log*.txt

You can use double-star wildcards to match zero or more directory levels in a path. The following command matches all ``.txt`` objects in a bucket. 
    
    
    gcloud alpha storage ls gs://my-bucket/**/*.txt

The wildcard `**` retrieves a flat list of objects in a single API call and does not match prefixes. The following command would not match `gs://my-bucket/dir/log.txt`: 
    
    
    gcloud alpha storage ls gs://my-bucket/**/dir

Double-star expansion also can not be combined with other expressions in a given path segment and operates as a single star in that context. For example, the command `gs://my-bucket/dir**/log.txt` is treated as `gs://my-bucket/dir*/log.txt`. To get the recursive behavior, the command should instead be written the following way: 
    
    
    gs://my-bucket/dir*/**/log.txt

The following command lists all items recursively with formatting by using `--recursive`: 
    
    
    gcloud alpha storage ls --recursive gs://bucket

Recursive listings are similar to `**` except recursive listings include line breaks and header formatting for each subdirectory. 

The following command filters objects based on specified filter while listing. Note that the flag is only supported for Google Cloud Storage URLs and only applies to objects. This means that directories or buckets will still be listed even if they do not contain objects that match the filter. 
    
    
    gcloud alpha storage ls gs://my-bucket --metadata-filter='contexts."foo"="bar"'

POSITIONAL ARGUMENTS
    

[`PATH` …]
     The path of objects and directories to list. The path must begin with gs:// and is allowed to contain wildcard characters. 
FLAGS
    

`--additional-headers`=`HEADER`=`VALUE`
     Includes arbitrary headers in storage API calls. Accepts a comma separated list of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides the default `storage/additional_headers` property value for this command invocation. 
`--all-versions`, `-a`
     Include noncurrent object versions in the listing. This flag is typically only useful for buckets with [object versioning](https://cloud.google.com/storage/docs/object-versioning) enabled. If combined with the `--long` option, the metageneration for each listed object is also included. 
`--buckets`, `-b`
     When given a bucket URL, only return buckets. Useful for avoiding the rule that prints the top-level objects of buckets matching a query. Typically used in combination with `--full` to get the full metadata of buckets. 
`--etag`, `-e`
     Include ETag metadata in listings that use the `--long` flag. 
`--exhaustive`
     For features like soft delete, the API may return an empty list. If present, continue querying. This may incur costs from repeated LIST calls and may not return any additional objects. 
`--fetch-encrypted-object-hashes`
     API requests to the LIST endpoint do not fetch the hashes for encrypted objects by default. If this flag is set, a GET request is sent for each encrypted object in order to fetch hashes. This can significantly increase the cost of the command. 
`--format`=`FORMAT`
     Use "gsutil" to get the style of the older gsutil CLI. (e.g. "--format=gsutil"). Other format values (e.g. "json") do not work. See different ls flags and commands for alternative formatting. 
`--metadata-filter`=`METADATA_FILTER`
     Server side filtering for objects. Works only for Google Cloud Storage URLs. The filter only works for objects, and not directories or buckets, which means commands like `storage ls` and `storage du` will still list directories or buckets even if they do not contain any objects matching the filter. See <https://cloud.google.com/storage/docs/listing-objects#filter-by-object-contexts-syntax> for more details. 
`--next-page-token`=`NEXT_PAGE_TOKEN`
     Page token for resuming LIST calls. 
`--read-paths-from-stdin`, `-I`
     Read the list of URLs from stdin. 
`--readable-sizes`
     When used with `--long`, print object sizes in human readable format, such as 1 KiB, 234 MiB, or 2 GiB. 
`--recursive`, `-R`, `-r`
     Recursively list the contents of any directories that match the path expression. 
`--soft-deleted`
     Displays soft-deleted resources only. For objects, it will exclude live and noncurrent ones. 
At most one of these can be specified: 

`--full`, `-L`
     List all available metadata about items in rows. 
`--json`, `-j`
     List all available metadata about items as a JSON dump. 
`--long`, `-l`
     For objects only. List size in bytes, creation time, and URL. 
ENCRYPTION FLAGS
    

`--decryption-keys`=[`DECRYPTION_KEY`,…]
     A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4 base64-encoded AES256 strings) that will be used to decrypt Cloud Storage objects. Data encrypted with a customer-managed encryption key (CMEK) is decrypted automatically, so CMEKs do not need to be listed here. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage ls](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
