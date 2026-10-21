---
url: https://docs.cloud.google.com/storage-transfer/docs/filter-by-last-modified/
title: Filter source objects by modification time \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:39.792057+00:00
---

# Filter source objects by modification time  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/filter-by-last-modified/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Filter source objects by modification time Stay organized with collections  Save and categorize content based on your preferences. 

You can filter which objects to transfer based on their last modification time. This lets you transfer only objects modified:

  * Before or after a specific date and time
  * Before or after a specified amount of elapsed time relative to the transfer job



This feature is useful for setting up incremental transfers or for skipping objects that fall outside of a time range.

Filtering by last modified time is supported for transfers from all sources except URL lists.

## Time-based filters

Filtering is defined with `last modified since`, `last modified before`, `minimum time elapsed since modified`, and `maximum time elapsed since modified` values. You can use the filters individually, or together to create a time window.

**Field** | **Description**  
---|---  
Last modified since  | Includes objects in the transfer that were last modified **on or after** this timestamp.   
Last modified before  | Includes objects in the transfer that were last modified **before** this timestamp.   
Minimum time elapsed since modified  | Includes objects in the transfer that were last modified at least this long ago. For example, this filter can be used to include only objects that were modified at least one month ago. Objects without a "last modification time" are also transferred.   
Maximum time elapsed since modified  | Includes objects in the transfer that were last modified no longer than this amount of time ago. For example, this filter can be used to include only objects that have been modified in the last 7 days. Objects without a "last modification time" are also transferred.   
  
## Specify a time-based filter

You can specify modification time filters when creating or updating a transfer job.

Timestamps must be in UTC and formatted as an [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) string (e.g., `2025-10-31T10:00:00Z`). Durations use the absolute duration format (e.g., `1m` for 1 month; `1h30m` for 1 hour 30 minutes).

###  Google Cloud console 

**Note:** The Google Cloud console does not support time-based filters for transfers from file systems. Use the gcloud CLI or REST API to filter file system transfers.

To specify a time filter in the Google Cloud console:

  1. Go to the **Create transfer job** or **Edit transfer job** page.
  2. In the **Choose data to transfer** section, select **Dates & times** as the **Filter type**.
  3. Enter a date and time for the **Absolute time range** or a duration for the **Relative time range**. Multiple filters can be specified together.



###  gcloud CLI 

To filter by modification time using the gcloud CLI, pass the time-based filter flags to the `gcloud transfer jobs create` or `gcloud transfer jobs update` command:
    
    
    gcloud transfer jobs create SOURCE DESTINATION \
      --include-modified-before-absolute="DATETIME" \
      --include-modified-after-absolute="DATETIME" \
      --include-modified-before-relative="DURATION" \
      --include-modified-after-relative="DURATION"
    

Where:

  * `--include-modified-before-absolute` includes objects last modified before an absolute date/time. For example, by specifying `2020-01-01`, the transfer includes objects last modified before January 1, 2020. Use the `%Y-%m-%dT%H:%M:%S%z` datetime format.
  * `--include-modified-after-absolute` includes objects last modified after an absolute date/time. For example, by specifying '2020-01-01', the transfer includes objects last modified after January 1, 2020. Use the `%Y-%m-%dT%H:%M:%S%z` datetime format.
  * `--include-modified-before-relative` includes objects that were modified outside of a specified amount of elapsed time. For example, specifying a duration of `10d` transfers objects last modified more than 10 days before the transfer start time. Use the absolute duration format. E.g., `1m` for 1 month; `1h30m` for 1 hour 30 minutes.
  * `--include-modified-after-relative` includes objects modified within a specified amount of time. For example, specifying a duration of `10d` transfers objects last modified less than 10 days before the transfer start time. Use the absolute duration format. E.g., `1m` for 1 month; `1h30m` for 1 hour 30 minutes.



**Example (modified after):**

The following command transfers only objects modified on or after October 1, 2025.
    
    
    gcloud transfer jobs create gs://my-source-bucket gs://my-sink-bucket
      --include-modified-after-absolute="2025-10-01T00:00:00Z"
    

**Example (time window):**

The following command transfers only objects modified _during_ the month of October 2025.
    
    
    gcloud transfer jobs create gs://my-source-bucket gs://my-sink-bucket
      --include-modified-after-absolute="2025-10-01T00:00:00Z"
      --include-modified-before-absolute="2025-11-01T00:00:00Z"
    

**Example (elapsed time):**

The following command transfers only objects modified in the last 7 days.
    
    
    gcloud transfer jobs create gs://my-source-bucket gs://my-sink-bucket
      --include-modified-after-relative="7d"
    

###  REST 

To filter by modification time using the REST API, specify the time-based filter fields in the `objectConditions` of your `transferSpec`.
    
    
    {
      "description": "DESCRIPTION",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "gcsDataSource": {
          "bucketName": "SOURCE_BUCKET"
        },
        "gcsDataSink": {
          "bucketName": "DESTINATION_BUCKET"
        },
        "objectConditions": {
          "lastModifiedBefore": "DATETIME",
          "lastModifiedSince": "DATETIME",
          "minTimeElapsedSinceLastModification": "DURATION",
          "maxTimeElapsedSinceLastModification": "DURATION",
    
        }
      }
    }
    

Where:

  * `lastModifiedBefore` includes objects last modified before an absolute date/time. For example, by specifying `2020-01-01`, the transfer includes objects last modified before January 1, 2020. Use the `%Y-%m-%dT%H:%M:%S%z` datetime format.
  * `lastModifiedSince` includes objects last modified after an absolute date/time. For example, by specifying '2020-01-01', the transfer includes objects last modified after January 1, 2020. Use the `%Y-%m-%dT%H:%M:%S%z` datetime format.
  * `minTimeElapsedSinceLastModification` includes objects that were modified outside of a specified amount of elapsed time. For example, specifying a duration of `10d` transfers objects last modified more than 10 days before the transfer start time. Use the absolute duration format. E.g., `1m` for 1 month; `1h30m` for 1 hour 30 minutes.
  * `maxTimeElapsedSinceLastModification` includes objects modified within a specified amount of time. For example, specifying a duration of `10d` transfers objects last modified less than 10 days before the transfer start time. Use the absolute duration format. E.g., `1m` for 1 month; `1h30m` for 1 hour 30 minutes.



**Example (time window):**

The following JSON body configures a job to transfer only objects modified during October 2025.
    
    
    {
      "description": "Transfer October 2025 data",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "gcsDataSource": {
          "bucketName": "SOURCE_BUCKET"
        },
        "gcsDataSink": {
          "bucketName": "DESTINATION_BUCKET"
        },
        "objectConditions": {
          "lastModifiedSince": "2025-10-01T00:00:00Z",
          "lastModifiedBefore": "2025-11-01T00:00:00Z"
        }
      }
    }
    

For more information, see the [ObjectConditions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec%23objectconditions) reference.

## Interaction with other filters

When you use multiple filters, Storage Transfer Service applies them in the following order:

  1. **Include prefixes** : Narrows down the objects to consider.

  2. **Object conditions** (glob pattern and last modified time): Filters the objects that matched the include prefix. An object must match both the glob filter and the last modified filter to be included in the result.

  3. **Exclude prefixes** : Removes objects from the result.




Learn more about [filtering by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers) and [filtering with glob patterns](https://docs.cloud.google.com/storage-transfer/docs/filter-by-glob-pattern).

### Example: Combining all filters

Imagine you have the following filter configuration for a transfer from AWS S3 or Azure:

  * include_prefix: "logs/"
  * match_glob: "**/*.log"
  * lastModifiedSince: "2025-10-31T00:00:00Z"
  * exclude_prefix: "logs/temp/"



**Result:** The service will execute the transfer as follows:

  1. First, it considers only objects under the `logs/` directory.
  2. Next, it looks for objects that both end in `.log` AND were modified on or after October 31, 2025.
  3. Finally, it removes any objects from that list that are in the `logs/temp/` directory.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
