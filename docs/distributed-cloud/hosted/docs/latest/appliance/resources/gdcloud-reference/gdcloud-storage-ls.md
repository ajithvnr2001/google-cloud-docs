---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-storage-ls/
title: gdcloud storage ls \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:04.399544+00:00
---

# gdcloud storage ls  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-storage-ls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud storage ls Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage ls - List storage buckets and objects

## SYNOPSIS
    
    
    gdcloud storage ls [PATH ...]
        [--all-versions, -a]
        [--buckets, -b]
        [--readable-sizes]
        [--recursive, -r]
        [--full, -L | --json, -j | --long, -l]
        [--format=FORMAT]
        [--log-http]
        [--verbosity=VERBOSITY] [flags]
    

## DESCRIPTION

List your storage buckets and objects in your buckets. This command treats forward slashes in object names as directories.

### EXAMPLES
    
    
    The following command lists the contents of a bucket:
    
        gdcloud storage ls s3://my-bucket
    
    You can use wildcards to match multiple paths, including multiple buckets.
    Bucket wildcards are expanded to match only buckets contained in your
    current project. The following command matches .txt objects that begin with
    "log" and that are stored in buckets in your project that begin with "my-b":
    
        gdcloud storage ls s3://my-b*/log*.txt
    
    The following wildcards are valid and match only within the current
    directory:
    
        *: Matches zero or more characters
        ?: Matches zero or one characters
        []: Matches a character range (ex. [a-z] or [0-9])
    
    You can use double-star wildcards to match zero or more directory levels in
    a path. The following command matches all .txt objects in a bucket.
    
        gdcloud storage ls s3://my-bucket/**/*.txt
    
    Double-star expansion can not be combined with other expressions in a given
    path segment and operates as a single star in that context. For example:
    
        s3://my-bucket/dir**/log.txt
    
    is treated as:
    
        s3://my-bucket/dir*/log.txt
    
    and instead should be written as:
    
        s3://my-bucket/dir*/**/log.txt
    
    to get the recursive behavior.
    
    The following command lists all items recursively with formatting by using
    --recursive:
    
        gdcloud storage ls --recursive s3://bucket
    
    Recursive listings are similar to ** except recursive listings include
    line breaks and header formatting for each subdirectory.
    

### OPTIONAL FLAGS
    
    
      -a, --all-versions       Include non-current object versions in the listing. This flag is
                               typically only useful for buckets with object versioning enabled. If
                               combined with the --long option, the metageneration for each listed
                               object is also included.
      -b, --buckets            When given a bucket URL, only return buckets. Useful for avoiding the
                               rule that prints the top-level objects of buckets matching a query.
                               Typically used in combination with --full to get the full metadata of
                               buckets.
      -L, --full               List all available metadata about items in rows.
      -j, --json               List all available metadata about items as a JSON dump.
          --log-http           Log all HTTP server requests and responses to stderr.
      -l, --long               List objects only. List size in bytes, creation time, and URL.
      -r, --recursive          Recursively list the contents of any directories that match the path expression.
          --verbosity string   Override the default verbosity for this command. VERBOSITY must be one of:
                               debug, info, warning, error, critical, none. (default "warning")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
