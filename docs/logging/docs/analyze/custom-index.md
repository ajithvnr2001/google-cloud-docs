---
url: https://docs.cloud.google.com/logging/docs/analyze/custom-index/
title: Improve query time with custom indexing \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:11.458423+00:00
---

# Improve query time with custom indexing  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/custom-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Improve query time with custom indexing Stay organized with collections  Save and categorize content based on your preferences. 

Custom indexes in Cloud Logging let you index frequently queried [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields in your [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries) to speed up queries over high-volume log data. In addition to the fields that Logging indexes automatically, you can configure custom indexes on string or integer fields for new or existing buckets.

## Overview

Query performance is critical to any logging solution. As workloads scale up and the corresponding log volumes increase, indexing your most-used logs data can reduce query time.

To improve query performance, Logging automatically indexes the following [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields:

  * [resource.type](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
  * [resource.labels.*](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
  * [logName](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
  * [severity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
  * [timestamp](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.timestamp)
  * [insertId](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
  * [operation.id](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogEntryOperation)
  * [trace](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
  * [httpRequest.status](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest)
  * [labels.*](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
  * [split.uid](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)



Besides those fields that Logging automatically indexes, you can also direct a log bucket to index other [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields by creating a custom index for the bucket.

For example, suppose your query expressions often include the field `jsonPayload.request.status`. You could configure a custom index for a bucket that includes `jsonPayload.request.status`; any subsequent query on that bucket's data would reference the indexed `jsonPayload.request.status` data if the query expression includes that field.

By using the Google Cloud CLI or Logging API, you can add custom indexes to existing or new log buckets. As you select additional fields to include in the custom index, note the following limitations:

  * You can add up to 20 fields per custom index.
  * After you configure or update a bucket's custom index, you must wait for an hour for the changes to apply to your queries. This latency ensures query-result correctness and accepts logs that are written in the past.
  * Logging applies custom indexing to data that is stored in log buckets after the index was created or changed; changes to custom indexes don't apply to logs retroactively.



## Before you begin

Before you start configuring a custom index, do the following:

  * Verify that you're using the latest version of the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). For more information, see [Managing Google Cloud CLI components](https://docs.cloud.google.com/sdk/docs/components).

**Note:** The gcloud CLI examples in this document assume that you've configured gcloud CLI to update the correct project. If you want to specify the project in the command, then include the `--project` flag and specify a Google Cloud project ID.
  * Verify that you have an Identity and Access Management role with the following permissions:

    * [`roles/logging.admin`](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles)
    * [`roles/logging.configWriter`](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles)

For details about these roles, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).




## Define the custom index

For each field that you add to a bucket's custom index, you define two attributes: a field path and a field type:

  * `fieldPath`: Describes the specific path to the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) field in your log entries. For example, `jsonPayload.req_status`.
  * `type`: Indicates whether the field is of the string or integer type. The possible values are `INDEX_TYPE_STRING` and `INDEX_TYPE_INTEGER`.



A custom index can be added either by creating a new bucket or by updating an existing bucket. For more information about configuring buckets, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets).

To configure a custom index when creating a bucket, do the following:

###  gcloud 

Use the [`gcloud logging buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/create) command and set the `--index` flag:
    
    
    gcloud logging buckets create BUCKET_NAME \
    --location=LOCATION \
    --description="DESCRIPTION" \
    --index=fieldPath=INDEX_FIELD_NAME,type=INDEX_TYPE
    

Example command:
    
    
    gcloud logging buckets create int_index_test_bucket \
    --location=global \
    --description="Bucket with integer index" \
    --index=fieldPath=jsonPayload.req_status,type=INDEX_TYPE_INTEGER
    

###  API 

To create a bucket, use [`projects.locations.buckets.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/create) in the Logging API. Prepare the arguments to the method as follows:

  1. Set the `parent` parameter to be the resource in which to create the bucket: `projects/PROJECT_ID/locations/LOCATION`

The variable LOCATION refers to the [region](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions) in which you want your logs to be stored.

For example, if you want to create a bucket for project `my-project` in the in the `asia-east2` region, your `parent` parameter would look like this: `projects/my-project/locations/asia-east2`

  2. Set the `bucketId` parameter; for example, `my-bucket`.

  3. In the `LogBucket` request body, configure the [`IndexConfig`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexConfig) object to create the custom index.

  4. Call `projects.locations.buckets.create` to create the bucket.




To update an existing bucket to include a custom index, do the following:

###  gcloud 

Use the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command and set the `--add-index` flag:
    
    
    gcloud logging buckets update BUCKET_NAME \
    --location=LOCATION \
    --add-index=fieldPath=INDEX_FIELD_NAME,type=INDEX_TYPE
    

Example command:
    
    
    gcloud logging buckets update int_index_test_bucket \
    --location=global \
    --add-index=fieldPath=jsonPayload.req_status,type=INDEX_TYPE_INTEGER
    

###  API 

Use [`projects.locations.buckets.patch`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch) in the Logging API. In the [`LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets) request body, configure the [`IndexConfig`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexConfig) object to include the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields that you want to index.

## Delete a custom indexed field

To delete a field from a bucket's custom index, do the following:

###  gcloud 

Use the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command and set the `--remove-indexes` flag :
    
    
    gcloud logging buckets update BUCKET_NAME \
    --location=LOCATION \
    --remove-indexes=INDEX_FIELD_NAME
    

Example command:
    
    
    gcloud logging buckets update int_index_test_bucket \
    --location=global \
    --remove-indexes=jsonPayload.req_status
    

###  API 

Use [`projects.locations.buckets.patch`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch) in the Logging API. In the [`LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets) request body, remove [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields from the [`IndexConfig`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexConfig) object.

## Update the custom indexed field's data type

If you need to fix the data type of a custom indexed field, do the following:

###  gcloud 

Use the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command and set the `--update-index` flag:
    
    
    gcloud logging buckets update BUCKET_NAME \
    --location=LOCATION \
    --update-index=fieldPath=INDEX_FIELD_NAME,type=INDEX_TYPE
    

Example command:
    
    
    gcloud logging buckets update int_index_test_bucket \
    --location=global \
    --update-index=fieldPath=jsonPayload.req_status,type=INDEX_TYPE_INTEGER
    

###  API 

Use [`projects.locations.buckets.patch`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch) in the Logging API. In the [`LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets) request body, update the [`IndexConfig`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexConfig) object to provide the correct data type for a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) field.

## Update a custom indexed field's path

If you need to fix the field path of a custom indexed field, do the following:

###  gcloud 

Use the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command and set the `--remove-indexes` and `--update-index` flags:
    
    
    gcloud logging buckets update BUCKET_NAME \
    --location=LOCATION \
    --remove-indexes=OLD_INDEX_FIELD_NAME \
    --update-index=fieldPath=NEW_INDEX_FIELD_NAME,type=INDEX_TYPE
    

Example command:
    
    
    gcloud logging buckets update int_index_test_bucket \
    --location=global \
    --remove-indexes=jsonPayload.req_status_old_path \
    --add-index=fieldPath=jsonPayload.req_status_new_path,type=INDEX_TYPE_INTEGER
    

###  API 

Use [`projects.locations.buckets.patch`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch) in the Logging API. In the [`LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets) request body, update the [`IndexConfig`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexConfig) object to provide the correct field path for a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) field.

## List all indexed fields for a bucket

To list a bucket's details, including its custom indexed fields, do the following:

###  gcloud 

Use the [`gcloud logging buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/describe) command:
    
    
    gcloud logging buckets describe BUCKET_NAME \
    --location=LOCATION
    

Example command:
    
    
    gcloud logging buckets describe indexed-bucket \
    --location global
    

###  API 

Use [`projects.locations.buckets.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/get) in the Logging API.

## Clear custom indexed fields

To remove all custom indexed fields from a bucket, do the following:

###  gcloud 

Use the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command and add the `--clear-indexes` flag:
    
    
    gcloud logging buckets update BUCKET_NAME \
    --location=LOCATION \
    --clear-indexes
    

Example command:
    
    
    gcloud logging buckets update int_index_test_bucket \
    --location=global \
    --clear-indexes
    

###  API 

Use [`projects.locations.buckets.patch`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/patch) in the Logging API. In the [`LogBucket`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets) request body, delete the [`IndexConfig`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexConfig) object.

## Query and view indexed data

To query the data included in custom indexed fields, restrict the scope of your query to the bucket that contains the custom indexed fields and specify the appropriate [log view](https://docs.cloud.google.com/logging/docs/logs-views):

###  gcloud 

To read logs from a log bucket, use the [gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command and add a [`LOG_FILTER`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#LOG_FILTER) to include your indexed data:
    
    
    gcloud logging read LOG_FILTER --bucket=BUCKET_ID --location=LOCATION --view=LOG_VIEW_ID
    

###  API 

To read logs from a log bucket, use the [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method. Set `resourceNames` to specify the appropriate bucket and log view, and set `filter` select your indexed data.

For detailed information about the filtering syntax, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

## Indexing and field types

How you configure custom field indexing can affect how logs are stored in log buckets and how queries are processed.

### At write time

Logging attempts to use the custom index on data that is stored in log buckets after the index was created.

Indexed fields are typed, which has implications for the timestamp on the log entry. When the log entry is stored in the log bucket, the log field is evaluated against the index type by using these rules:

  * If a field's type is the same as the index's type, then the data is added to the index verbatim.
  * If the field's type is different than the index's type, then Logging attempts to coerce it into the index's type (for example, integer to string). 
    * If type coercion fails, the data isn't indexed. When type coercion succeeds, the data is indexed.



### At query time

Enabling an index on a field changes how you must query that field. By default, Logging applies filter constraints to fields based on the type of the data in each log entry that is being evaluated. When indexing is enabled, filter constraints on a field are applied based on the type of the index. Adding an index on a field imposes a schema on that field.

When a custom index is configured for a bucket, schema matching behaviors differ when both of these conditions are met:

  * The source data type for a field doesn't match the index type for that field.
  * The user applies a constraint on that field.



Consider the following JSON payloads:
    
    
    {"jsonPayload": {"name": "A", "value": 12345}}
    {"jsonPayload": {"name": "B", "value": "3"}}
    

Now apply this filter to each:
    
    
    jsonPayload.value > 20
    

If the `jsonPayload.value` field lacks custom indexing, then Logging applies flexible-type matching:

  * For "A", Logging observes that the value of the "value" key is actually an integer, and that the constraint, "20", can be converted to an integer. Logging then evaluates `12345 > 20` and returns "true" because this is the case numerically.

  * For "B", Logging observes that the value of the "value" key is actually a string. It then evaluates `"3" > "20"` and returns "true", since this is the case alphanumerically.




If the field `jsonPayload.value` is included in the custom index, then Logging evaluates this constraint using the index instead of the usual Logging logic. The behavior changes:

  * If the index is string-typed, then all comparisons are string comparisons. 
    * The "A" entry doesn't match, since "12345" isn't greater than "20" alphanumerically. The "B" entry matches, since the string "3" is greater than "20".
  * If the index is integer-typed, then all comparisons are integer comparisons. 
    * The "B" entry doesn't match, since "3" isn't greater than "20" numerically. The "A" entry matches, since "12345" is greater than "20".



This behavior difference is subtle and should be considered when defining and using custom indexes.

#### Filtering edge case

For the `jsonPayload.value` integer-type index, suppose a string value is filtered:
    
    
    jsonPayload.value = "hello"
    

If the query value can't be coerced to the index type, the index is ignored.

However, suppose for a string-type index, you pass an integer value:
    
    
    jsonPayload.value > 50
    

Neither A nor B matches, as neither "12345" nor "3" is alphanumerically greater than "50".

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
