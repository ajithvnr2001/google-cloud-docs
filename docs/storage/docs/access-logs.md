---
url: https://docs.cloud.google.com/storage/docs/access-logs/
title: Usage logs & storage logs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:39.028408+00:00
---

# Usage logs & storage logs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Usage logs & storage logs Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses how to download and review usage logs and storage information for your Cloud Storage buckets, and analyze the logs using [Google BigQuery](https://docs.cloud.google.com/bigquery).

## Introduction

Cloud Storage offers usage logs and storage logs in the form of CSV files that you can download and view. _Usage logs_ provide information for all of the requests made on a specified bucket and are created hourly. _Storage logs_ provide information about the storage consumption of that bucket for the last day and are created daily.

Once set up, both usage logs and storage logs are automatically generated for the specified bucket and stored as new objects in a bucket that you specify.

Usage logs and storage logs are subject to the same [pricing](https://docs.cloud.google.com/storage/pricing) as other objects stored in Cloud Storage.

**Caution:** Timeliness and completeness of usage and storage logs delivery is not guaranteed.

### Should you use usage logs or Cloud Audit Logs?

In most cases, [Cloud Audit Logs](https://docs.cloud.google.com/storage/docs/audit-logging) is the recommended method for generating logs that track API operations performed in Cloud Storage:

  * Cloud Audit Logs tracks access on a continuous basis, with delivery of events within seconds of their occurrence.
  * Cloud Audit Logs produces logs that are easier to work with.
  * Cloud Audit Logs can monitor many of your Google Cloud services, not just Cloud Storage.
  * Cloud Audit Logs can, optionally, log detailed request and response information.



In some cases, you might want to use usage logs instead of or in addition to using Cloud Audit Logs. You most likely want to use usage logs if:

  * You want to track access that occurs because a resource has `allUsers` or `allAuthenticatedUsers` in its access control settings, such as access to assets in a bucket that you've configured to be a static website.
  * You want to track changes made by the [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) features.
  * You want your logs to include latency information, the request and response size of individual HTTP requests, or the full URL path and every query parameter.
  * You want to track access to only certain buckets in your project and so do not want to enable Data Access audit logs, which tracks access to all buckets in your project.

**Note:** While usage logs are generated hourly, they might be delayed, especially for buckets that experience high request rates. Logs are generated at least every six hours.

### Should you use storage logs or Monitoring?

Generally, you should not use storage logs. The recommended tool for measuring storage consumption is Monitoring, which provides visualization tools as well as additional metrics related to storage consumption that storage logs do not. See the [Console tab for determining a bucket's size](https://docs.cloud.google.com/storage/docs/getting-bucket-size#get-bucket-size-console) for step-by-step instructions on using Monitoring.

## Set up log delivery

Before setting up log delivery, you must have a bucket for storing logs. This bucket must meet the following requirements, or else logging fails:

  * The bucket storing the logs must exist within the same [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) as the bucket being logged.

    * If the bucket being logged is not contained in any organization, the bucket storing the logs must exist within the same project as the bucket being logged.
  * The bucket storing the logs must exist in the same [location](https://docs.cloud.google.com/storage/docs/locations) (region, dual-region, or multi-region) as the bucket being logged.

  * If you use or enable [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), the bucket storing the logs must reside within the same security perimeter as the bucket being logged.




If you don't already have a bucket that meets these requirements, [create the bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

The following steps describe how to set up log delivery for a bucket:

### Command line

  1. Grant Cloud Storage the `roles/storage.objectCreator` role for the bucket:
         
         gcloud storage buckets add-iam-policy-binding _gs://example-logs-bucket_ --member=group:cloud-storage-analytics@google.com --role=roles/storage.objectCreator

The role gives Cloud Storage, in the form of the group `cloud-storage-analytics@google.com`, permission to create and store your logs as new objects.

Log objects have the [default object acl](https://docs.cloud.google.com/storage/docs/access-control/lists#defaultobjects) of the log bucket, unless [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) is enabled on the bucket.

  2. Enable logging for your bucket using the [`--log-bucket` flag](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update#--log-bucket):
         
         gcloud storage buckets update _gs://example-bucket_ --log-bucket=_gs://example-logs-bucket_ [--log-object-prefix=_log_object_prefix_]

Optionally, you can set an object prefix for your log objects by using the `--log-object-prefix` flag. The object prefix forms the beginning of the log object name. It can be at most 900 characters and must be a [valid object name](https://docs.cloud.google.com/storage/docs/objects#naming). By default, the object prefix is the name of the bucket for which the logs are enabled.




### REST APIs

### JSON API

  1. Grant Cloud Storage the `roles/storage.objectCreator` role for the bucket. If there are additional bucket-level IAM bindings for the bucket, be sure to include them in the request.
         
         POST /storage/v1/b/_example_ -logs-bucket/iam
         Host: storage.googleapis.com
         {
           "bindings":[
             {
               "role": "roles/storage.objectCreator",
               "members":[
                 "group-cloud-storage-analytics@google.com"
               ]
             }
           ]
         }

The role gives Cloud Storage, in the form of the group `cloud-storage-analytics@google.com`, permission to create and store your logs as new objects.

Log objects have the [default object acl](https://docs.cloud.google.com/storage/docs/access-control/lists#defaultobjects) of the log bucket, unless [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) is enabled on the bucket.

  2. Enable logging for your bucket using the following request:
         
         PATCH /storage/v1/b/_example_ -bucket
         Host: storage.googleapis.com
         
         {
          "logging": {
           "logBucket": "_example-logs-bucket_ ",
           "logObjectPrefix": "_log_object_prefix_ "
          }
         }




### XML API

**Note:** If you use [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) on the bucket storing your logs, you cannot use the XML API to set access permission on it. Use a different tool instead.

  1. Set permissions to allow Cloud Storage `WRITE` permission to the bucket in order to create and store your logs as new objects. You must add an ACL entry for the bucket that grants the group `cloud-storage-analytics@google.com` write access. Be sure to include all existing ACLs for the bucket, in addition to the new ACL, in the request.
         
         PUT /_example-logs-bucket_?acl HTTP/1.1
         Host: storage.googleapis.com
         
         <AccessControlList>
           <Entries>
             <Entry>
               <Scope type="GroupByEmail">
                 <EmailAddress>cloud-storage-analytics@google.com</EmailAddress>
               </Scope>
              <Permission>WRITE</Permission>
             </Entry>
             <!-- include other existing ACL entries here-->
           </Entries>
         </AccessControlList>
         

  2. Enable logging for your bucket using the logging query parameter:
         
         PUT /_example-bucket_?logging HTTP/1.1
         Host: storage.googleapis.com
         
         <Logging>
             <LogBucket>_example-logs-bucket_ </LogBucket>
             <LogObjectPrefix>_log_object_prefix_ </LogObjectPrefix>
         </Logging>
         




## Check logging status

### Command line

Check logging by using the `buckets describe` command with the `--format` flag:
    
    
    gcloud storage buckets describe _gs://example-bucket_ --format="default(logging_config)"

You can also save the logging configurations to a file:
    
    
    gcloud storage buckets describe gs://example-bucket > _your_logging_configuration_file_ --format="default(logging_config)"

If logging is enabled, the server returns the logging configuration in the response:
    
    
    logging:
      logBucket: example-logs-bucket
      logObjectPrefix: log_object_prefix

If logging is not enabled, the following is returned:
    
    
    null

### REST APIs

### JSON API

Send a [GET](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request for the bucket's logging configuration as shown in the following example:
    
    
    GET /storage/v1/b/_example_ -bucket?fields=logging
    Host: storage.googleapis.com

If logging is enabled, the server sends the configuration in the response. A response might look similar to the following:
    
    
    {
     "logging": {
      "logBucket": "example-logs-bucket",
      "logObjectPrefix": "log_object_prefix"
      }
    }
    

If logging is not enabled, an empty configuration is returned:
    
    
    {}

### XML API

Send a [GET Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata) request for the bucket's logging configuration as shown in the following example:
    
    
    GET /_example-bucket_?logging HTTP/1.1
    Host: storage.googleapis.com
    

If logging is enabled, the server sends the configuration in the response. A response might look similar to the following:
    
    
    <?xml version="1.0" ?>
    <Logging>
        <LogBucket>
            example-logs-bucket
        </LogBucket>
        <LogObjectPrefix>
            log_object_prefix
        </LogObjectPrefix>
    </Logging>
    

If logging is not enabled, an empty configuration is returned:
    
    
    <?xml version="1.0" ?>
    <Logging/>
    

## Download logs

Storage logs are generated once a day and contain the amount of storage used for the previous day. They are typically created before 10:00 am PST.

Usage logs are generated hourly when there is activity to report in the monitored bucket. Usage logs are typically created 15 minutes after the end of the hour.

**Note:**

  * Any log processing of usage logs should take into account the possibility that they may be delivered later than 15 minutes after the end of an hour.
  * Usually, hourly usage log object(s) contain records for all access that occurred during that hour. Occasionally, an hourly usage log object contains records for an earlier hour, but never for a later hour.
  * Cloud Storage may write multiple log objects for the same hour.
  * Occasionally, a single record may appear twice in the usage logs. While we make our best effort to remove duplicate records, your log processing should be able to remove them if it is critical to your log analysis. You can use the `s_request_id` field to detect duplicates.



The easiest way to download your usage logs and storage logs from the bucket in which they are stored is either through the [Google Cloud console](https://docs.cloud.google.com/storage/docs/cloud-console) or the [`gcloud storage` CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage). Your usage logs are in CSV format and have the following naming convention:
    
    
    OBJECT_PREFIX_usage_TIMESTAMP_ID_v0

Similarly, storage logs are named using the following convention:
    
    
    OBJECT_PREFIX_storage_TIMESTAMP_ID_v0

For example, the following is the name of a usage log object that uses the default object prefix, reports usage for the bucket named `example-bucket`, and was created on June 18, 2022 at 14:00 UTC:
    
    
    example-bucket_usage_2022_06_18_14_00_00_1702e6_v0

Similarly, the following is the name of the storage log object that uses the default object prefix and was created on June 18, 2022 for the same bucket:
    
    
    example-bucket_storage_2022_06_18_07_00_00_1702e6_v0

To download logs:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Select the bucket in which your logs are stored.

  3. Download or view your logs by clicking on the appropriate log object.




### Command line

Run the following command:
    
    
    gcloud storage cp gs://BUCKET_NAME/LOGS_OBJECT DESTINATION

Where:

  * `BUCKET_NAME` is the name of the bucket in which the logs are stored. For example, `example-logs-bucket`.

  * `LOGS_OBJECT` is the name of the usage log or storage log that you are downloading. For example, `example-bucket_usage_2022_06_18_14_00_00_1702e6_v0`.

  * `DESTINATION` is the location to which the log is being downloaded. For example, `Desktop/Logs`.




## Analyze logs in BigQuery

To query your Cloud Storage usage and storage logs, you can use [Google BigQuery](https://docs.cloud.google.com/bigquery) which enables fast, SQL-like queries against append-only tables. The BigQuery Command-Line Tool, `bq`, is a Python-based tool that allows you to access BigQuery from the command line. For information about downloading and using bq, see the [bq Command-Line Tool](https://docs.cloud.google.com/bigquery/bq-command-line-tool) reference page.

### Load logs into BigQuery

  1. Select a default project.

For details about selecting a project, see [Working With Projects](https://docs.cloud.google.com/bigquery/bq-command-line-tool#projects).

  2. Create a new dataset.
         
         $ bq mk storageanalysis
         Dataset 'storageanalysis' successfully created.
         

  3. List the datasets in the project:
         
         $ bq ls
          
         datasetId
         -----------------
         storageanalysis
         

  4. Save the usage and storage schemas to your local computer for use in the load command.

You can find the schemas to use at these locations: [ cloud_storage_usage_schema_v0](https://storage.googleapis.com/pub/cloud_storage_usage_schema_v0.json) and [ cloud_storage_storage_schema_v0](https://storage.googleapis.com/pub/cloud_storage_storage_schema_v0.json). The schemas are also described in the section Usage and Storage Logs Format.

  5. Load the usage logs into the dataset.
         
         $ bq load --skip_leading_rows=1 --allow_jagged_rows=true --ignore_unknown_values=true \
               storageanalysis.usage \
               gs://example-logs-bucket/example-bucket_usage_2014_01_15_14_00_00_1702e6_v0 \
               ./cloud_storage_usage_schema_v0.json
         $ bq load --skip_leading_rows=1 --allow_jagged_rows=true --ignore_unknown_values=true \
               storageanalysis.storage \
               gs://example-logs-bucket/example-bucket_storage_2014_01_05_14_00_00_091c5f_v0 \
               ./cloud_storage_storage_schema_v0.json
         

These commands do the following:

     * Load usage and storage logs from the bucket `example-logs-bucket`.
     * Create tables `usage` and `storage` in the dataset `storageanalysis`.
     * Read schema data (.json file) from the same directory where the bq command runs.
     * Skip the first row of each log file because it contains column descriptions.
     * Allow missing trailing optional columns and load rows with extra column values that don't match the table schema, but ignore these extra columns. This makes the pipeline resilient to schema additions and mixed historical and new files.

Because this was the first time you ran the load command in the example here, the tables `usage` and `storage` were created. You could continue to append to these tables with subsequent load commands with different usage log file names or using wildcards. For example, the following command appends data from all logs that start with "bucket_usage_2014", to the `storage` table:
    
    $ bq load --skip_leading_rows=1 --allow_jagged_rows=true --ignore_unknown_values=true \
          storageanalysis.usage \
          **gs://example-logs-bucket/bucket_usage_2014*** \
          ./cloud_storage_usage_schema_v0.json
    

When using wildcards, you might want to move logs already uploaded to BigQuery to another directory (e.g., `gs://example-logs-bucket/processed`) to avoid uploading data from a log more than once.




BigQuery functionality can also be accessed through the [BigQuery Browser Tool](https://docs.cloud.google.com/bigquery/bigquery-browser-tool). With the browser tool, you can load data through the create table process.

For additional information about loading data from Cloud Storage, including programmatically loading data, see [Loading data from Cloud Storage](https://docs.cloud.google.com/bigquery/loading-data-into-bigquery#loaddatagcs).

### Modify the usage log schema

In some scenarios, you may find it useful to pre-process usage logs before loading into BigQuery. For example, you can add additional information to the usage logs to make your query analysis easier in BigQuery. In this section, we'll show how you can add the file name of each storage usage log to the log. This requires modifying the existing schema and each log file.

  1. Modify the existing schema, [ cloud_storage_storage_schema_v0](http://storage.googleapis.com/pub/cloud_storage_storage_schema_v0.json), to add file name as shown below. Give the new schema a new name, for example, **cloud_storage_storage_schema_custom.json** , to distinguish from the original.
         
         [  {"name": "bucket", "type": "string", "mode": "REQUIRED"},
         {"name": "storage_byte_hours","type": "integer","mode": "REQUIRED"},
         **{"name": "filename","type": "string","mode": "REQUIRED"}**
         ]
         

  2. Pre-process storage usage log files based on the new schema, before loading them into BigQuery.

For example, the following commands can be used in a Linux, macOS, or Windows (Cygwin) environment:
         
         gcloud storage cp gs://example-logs-bucket/example-bucket_storage\* .
         for f in example-bucket_storage\*; do sed -i -e "1s/$/,\"filename\"/" -e "2s/$/,\""$f"\"/" $f; done
         

The `gcloud storage` command copies the files into your working directory. The second command loops through the log files and adds "filename" to the description row (first row) and the actual file name to the data row (second row). Here's an example of a modified log file:
         
         "bucket","storage_byte_hours","filename"
         "example-bucket","5532482018","example-bucket_storage_2014_01_05_08_00_00_021fd_v0"
         

  3. When you load the storage usage logs into BigQuery, load your locally modified logs and use the customized schema.
         
         for f in example-bucket_storage\*; \
         do ./bq.py load --skip_leading_rows=1 storageanalysis.storage $f ./cloud_storage_storage_schema_custom.json; done
         




### Query logs in BigQuery

Once your logs are loaded into BigQuery, you can query your usage logs to return information about your logged bucket(s). The following example shows you how to use the bq tool in a scenario where you have usage logs for a bucket over several days and you have loaded the logs as shown in Loading usage logs into BigQuery. You can also execute the queries below using the [BigQuery Browser Tool](https://docs.cloud.google.com/bigquery/bigquery-browser-tool).

  1. In the bq tool, enter the interactive mode.
         
         $ bq shell
         

  2. Run a query against the storage log table.

For example, the following query shows how the storage of a logged bucket changes in time. It assumes that you modified the storage usage logs as described in Modifying the usage log schema and that the log files are named "log _storage_ *".
         
         project-name>SELECT SUBSTRING(filename, 13, 10) as day, storage_byte_hours/24 as size FROM [storageanalysis.storage] ORDER BY filename LIMIT 100
         

Example output from the query:
         
         Waiting on bqjob_r36fbf5c164a966e8_0000014379bc199c_1 ... (0s) Current status: DONE
         +------------+----------------------+
         |    day     |         size         |
         +------------+----------------------+
         | 2014_01_05 | 2.3052008408333334E8 |
         | 2014_01_06 | 2.3012297245833334E8 |
         | 2014_01_07 | 3.3477797120833334E8 |
         | 2014_01_08 | 4.4183686058333334E8 |
         +-----------------------------------+
         

If you did not modify the schema and are using the default schema, you can run the following query:
         
         project-name>SELECT storage_byte_hours FROM [storageanalysis.storage] LIMIT 100
         

  3. Run a query against the usage log table.

For example, the following query shows how to summarize the request methods that clients use to access resources in the logged bucket.
         
         project-name>SELECT cs_method, COUNT(*) AS count FROM [storageanalysis.usage] GROUP BY cs_method
         

Example output from the query:
         
         Waiting on bqjob_r1a6b4596bd9c29fb_000001437d6f8a52_1 ... (0s) Current status: DONE
         +-----------+-------+
         | cs_method | count |
         +-----------+-------+
         | PUT       |  8002 |
         | GET       | 12631 |
         | POST      |  2737 |
         | HEAD      |  2173 |
         | DELETE    |  7290 |
         +-----------+-------+
         

  4. Quit the interactive shell of the bq tool.
         
         project-name> quit
         




## Disable logging

### Command line

Disable logging with the `--clear-log-bucket` flag in the `buckets update` command:
    
    
    gcloud storage buckets update _gs://example-bucket_ --clear-log-bucket

To check that logging was successfully disabled, use the `buckets describe` command:
    
    
    gcloud storage buckets describe _gs://example-bucket_ --format="default(logging_config)"

If logging is disabled, the following is returned:
    
    
    null

### REST APIs

### JSON API

Disable logging by sending a [PATCH](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request to the bucket's logging configuration as shown in the following example.
    
    
    PATCH /_example_ -bucket?logging HTTP/1.1
    Host: storage.googleapis.com
    
    {
     "logging": null
    }

### XML API

Disable logging by sending a [PUT](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) request to the bucket's logging configuration as shown in the following example:
    
    
    PUT /_example-bucket_?logging HTTP/1.1
    Host: storage.googleapis.com
    
    <Logging/>
    

## Usage and storage log format

The usage logs and storage logs can provide an overwhelming amount of information. You can use the following tables to help you identify the information provided in these logs.

**Note:** Google Cloud might occasionally append new optional (`NULLABLE`) columns to the end of usage log and storage log CSV files. Because of this, we recommend that your ingestion pipelines avoid hardcoding a fixed column count, and instead parse by the header row or allow trailing columns. 

**Usage log fields:**

Field | Type | Description | `time_micros` | integer | The time that the request was completed, in microseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_epoch).  
---|---|---  
`c_ip` | string | The IP address from which the request was made. The "c" prefix indicates that this is information about the client.  
`c_ip_type` | integer | The type of IP in the c_ip field: 

  * A value of **1** indicates an IPV4 address.
  * A value of **2** indicates an IPV6 address.

  
`c_ip_region` | string | Reserved for future use.  
`cs_method` | string | The HTTP method of this request. The "cs" prefix indicates that this information was sent from the client to the server.  
`cs_uri` | string | The URI of the request.  
`sc_status` | integer | The HTTP status code the server sent in response. The "sc" prefix indicates that this information was sent from the server to the client.  
`cs_bytes` | integer | The number of bytes sent in the request.  
`sc_bytes` | integer | The number of bytes sent in the response.  
`time_taken_micros` | integer | The time it took to serve the request in microseconds, measured from when the first byte is received to when the response is sent. Note that for resumable uploads, the ending point is determined by the response to the final upload request that was part of the resumable upload.  
`cs_host` | string | The host in the original request.  
`cs_referer` | string | The [HTTP referrer](https://en.wikipedia.org/wiki/HTTP_referrer) for the request.  
`cs_user_agent` | string | The [User-Agent](https://datatracker.ietf.org/doc/html/rfc1945#section-10.15) of the request. The value is `GCS Lifecycle Management` for requests made by [lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle).  
`s_request_id` | string | The request identifier.  
`cs_operation` | string | The Cloud Storage operation e.g. `GET_Object`. This can be null.  
`cs_bucket` | string | The bucket specified in the request.  
`cs_object` | string | The object specified in this request. This can be null.  
  
**Storage log fields:**

Field | Type | Description | `bucket` | string | The name of the bucket.  
---|---|---  
`storage_byte_hours` | integer | Average size in byte-hours over a 24 hour period of the bucket. To get the total size of the bucket, divide byte-hours by 24.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
