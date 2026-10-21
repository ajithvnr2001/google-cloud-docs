---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/du/
title: gcloud alpha storage du \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:39.691972+00:00
---

# gcloud alpha storage du  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/du/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage du Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage du - displays the amount of space in bytes used by storage resources 
SYNOPSIS
    

`gcloud alpha storage du` [`URL` …] [`--additional-headers`=`HEADER`=`VALUE`] [`--all-versions`, `-a`] [`--exclude-name-pattern`=`EXCLUDE_NAME_PATTERN`, `-e` `EXCLUDE_NAME_PATTERN`] [`--exclude-name-pattern-file`=`EXCLUDE_NAME_PATTERN_FILE`, `-X` `EXCLUDE_NAME_PATTERN_FILE`] [`--metadata-filter`=`METADATA_FILTER`] [`--readable-sizes`, `-r`] [`--summarize`, `-s`] [`--total`, `-c`] [`--zero-terminator`, `-0`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Displays the amount of space in bytes used by the objects in a bucket, subdirectory, or project. This command calculates the current space usage by making a series of object listing requests, which can take a long time for large buckets. If your bucket contains hundreds of thousands of objects, or if you want to monitor your bucket size over time, use Monitoring instead, as described in [Get bucket size](https://cloud.google.com/storage/docs/getting-bucket-size)
EXAMPLES
     To list the size of each object in a bucket: 
    
    
    gcloud alpha storage du gs://bucketname

To list the size of each object in the prefix subdirectory: 
    
    
    gcloud alpha storage du gs://bucketname/prefix/*

To print the total number of bytes in a bucket in human-readable form: 
    
    
    gcloud alpha storage du -c gs://bucketname

To see a summary of the total number of bytes in two given buckets: 
    
    
    gcloud alpha storage du -s gs://bucket1 gs://bucket2

To list the size of each object in a bucket with Object Versioning enabled, including noncurrent objects: 
    
    
    gcloud alpha storage du -a gs://bucketname

To list the size of each object in a bucket, except objects that end in ".bak", with each object printed ending in a null byte: 
    
    
    gcloud alpha storage du -e "*.bak" -0 gs://bucketname

To list the size of each bucket in a project and the total size of the project: 
    
    
    gcloud alpha storage du --summarize --readable-sizes --total

The following command summarizes the size of objects that match the specified filter. 
    
    
    gcloud alpha storage du gs://my-bucket --metadata-filter='contexts."foo"="bar"' --summarize

POSITIONAL ARGUMENTS
    

[`URL` …]
     The url of objects to list. 
FLAGS
    

`--additional-headers`=`HEADER`=`VALUE`
     Includes arbitrary headers in storage API calls. Accepts a comma separated list of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides the default `storage/additional_headers` property value for this command invocation. 
`--all-versions`, `-a`
     Includes noncurrent object versions for a bucket with Object Versioning enabled. Also prints the generation and metageneration number for each listed object. 
`--exclude-name-pattern`=`EXCLUDE_NAME_PATTERN`, `-e` `EXCLUDE_NAME_PATTERN`
     Exclude a pattern from the report. Example: `-e "*.o"` excludes any object that ends in ".o". Can be specified multiple times. 
`--exclude-name-pattern-file`=`EXCLUDE_NAME_PATTERN_FILE`, `-X` `EXCLUDE_NAME_PATTERN_FILE`
     Similar to -e, but excludes patterns from the given file. The patterns to exclude should be listed one per line. 
`--metadata-filter`=`METADATA_FILTER`
     Server side filtering for objects. Works only for Google Cloud Storage URLs. The filter only works for objects, and not directories or buckets, which means commands like `storage ls` and `storage du` will still list directories or buckets even if they do not contain any objects matching the filter. See <https://cloud.google.com/storage/docs/listing-objects#filter-by-object-contexts-syntax> for more details. 
`--readable-sizes`, `-r`
     Prints object sizes in human-readable format. For example, 1 KiB, 234 MiB, or 2GiB. 
`--summarize`, `-s`
     Displays only the summary for each argument. 
`--total`, `-c`
     Includes a total size of all input sources. 
`--zero-terminator`, `-0`
     Ends each output line with a 0 byte rather than a newline. You can use this to make the output machine-readable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage du](https://docs.cloud.google.com/sdk/gcloud/reference/storage/du)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
