---
url: https://docs.cloud.google.com/storage-transfer/docs/filter-by-glob-pattern/
title: Filter source objects using wildcards \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:18.494022+00:00
---

# Filter source objects using wildcards  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/filter-by-glob-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Filter source objects using wildcards Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service jobs support search strings with wildcard characters like `*` and `?` to match filenames or paths. These search strings are called glob patterns.

You can use glob patterns to specify which source objects to include in a transfer. This allows for more fine-grained control than filtering by prefix alone.

Filtering with glob patterns is supported for transfers from AWS S3 and Azure.

## Glob syntax

A glob pattern uses the following syntax to match object paths:

Syntax | Description  
---|---  
`?` | Matches any single character, excluding `/`.  
`*` | Matches zero or more characters, excluding `/`.  
`**` | Matches zero or more characters, including `/`.  
`[abc]` | Matches exactly one of the characters (e.g., `a`, `b`, or `c`).  
`[a-z]` | Matches exactly one character in the inclusive range (e.g., `a` through `z`).  
`[!abc]` or `[^abc]` | Matches exactly one character that is not `a`, `b`, or `c`.  
`{abc,xyz}` | Matches one of the strings (e.g., `abc` or `xyz`). Cannot contain forward slashes (`/`) or double asterisks (`**`).  
`\?` | Matches the literal character after the backslash (e.g., `\?` matches a literal `?`).  
  
### Example patterns

Match all `.log` files from `december` directories:
    
    
    logs_by_year/**/december/*.log
    

Transfer all files in the `data_analytics/` directory that do not begin with a `.` (dot) or `_` (underscore):
    
    
    data_analytics/[!._]*
    

To make the previous example recursive:
    
    
    data_analytics/**/[!._]*
    

Transfer all PDF files from exactly two specific directories:
    
    
    quarterly_reports/2025/{q1-final,q4-final}/*.pdf
    

## Specify a glob pattern

You can specify a glob pattern when creating or updating a transfer job.

###  gcloud CLI 

To filter by glob pattern using the `gcloud` CLI, pass the `--match-glob` flag to the `gcloud transfer jobs create` or `gcloud transfer jobs update` command:
    
    
    gcloud transfer jobs create SOURCE DESTINATION \
      --match-glob="GLOB_PATTERN"
    

**Example:**

The following command creates a job that transfers only `.log` files from `december` directories:
    
    
    gcloud transfer jobs create s3://my-source-bucket gs://my-sink-bucket \
      --match-glob="logs_by_year/**/december/*.log"
    

###  REST 

To filter by glob pattern using the REST API, specify the `matchGlob` field in the `objectConditions` of your `transferSpec`.
    
    
    {
      "description": "Transfer December logs from all years",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "awsS3DataSource": {
          "bucketName": "AWS_SOURCE_NAME",
          "awsAccessKey": {
            "accessKeyId": "AWS_ACCESS_KEY_ID",
            "secretAccessKey": "AWS_SECRET_ACCESS_KEY"
          }
        },
        "gcsDataSink": {
          "bucketName": "DESTINATION_BUCKET"
        },
        "objectConditions": {
          "matchGlob": "logs_by_year/**/december/*.log"
        }
      }
    }
    

For more information, see the [`ObjectConditions`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#objectconditions) reference.

###  Google Cloud console 

Filtering by glob pattern is not supported in the Google Cloud console.

## Interaction with other filters

When you use a glob pattern filter with prefix filters or last modified time filters, Storage Transfer Service applies the filters in the following order:

  1. **Include prefixes** : Narrows down the objects to consider.

  2. **Object conditions** (glob pattern and last modified time): Filters the objects that matched the include prefix. An object must match both the glob filter and the last modified time filter to be included in the result.

  3. **Exclude prefixes** : Removes objects from the result.




Learn more about [filtering by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers) and [filtering by last modified time](https://docs.cloud.google.com/storage-transfer/docs/filter-by-last-modified).

### Include prefixes

The glob pattern is applied only to objects that match at least one include prefix.

Storage Transfer Service returns an error if your glob pattern contradicts all include prefix patterns.

> **Example: Valid combination**
> 
>   * `include_prefix`: `["foo/"]`
>   * `match_glob`: `"foo/bar/**"`
> 

> 
> **Result:** Valid. The service first lists objects under `foo/` and then applies the glob pattern to that list.

> **Example: Valid combination**
> 
>   * `include_prefix`: `["logs/2024/", "logs/2025/"]`
>   * `match_glob`: `"**/*.json"`
> 

> 
> **Result:** Valid. The service lists all objects in the `2024` and `2025` directories and then transfers only the files that end with `.json`.

> **Example: Contradiction**
> 
>   * `include_prefix`: `["foo/"]`
>   * `match_glob`: `"bar/**"`
> 

> 
> **Result:** Error. The `match_glob` pattern cannot match any objects selected by the `include_prefix`.

### Exclude prefixes

The exclude prefix filter is applied _after_ both the include prefix filter and the glob pattern filter.

No contradiction check is performed. Any object that matches an exclude prefix is removed from the transfer list, even if it matched the glob pattern.

> **Example**
> 
>   * `include_prefix`: `["logs/"]`
>   * `match_glob`: `"**/*.log"`
>   * `exclude_prefix`: `["logs/temp/"]`
> 

> 
> **Result:** The service transfers all objects under `logs/` that end with `.log`, _except_ for those in the `logs/temp/` directory.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
