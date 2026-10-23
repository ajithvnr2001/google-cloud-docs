---
url: https://docs.cloud.google.com/logging/docs/field-level-acl/
title: Configure field-level access \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:58.750240+00:00
---

# Configure field-level access  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/field-level-acl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure field-level access Stay organized with collections  Save and categorize content based on your preferences. 

This document describes field-level access controls and how to set them on a Logging [bucket](https://docs.cloud.google.com/logging/docs/store-log-entries). Field-level access controls let you hide individual `LogEntry` fields from users of a Google Cloud project, providing you a more granular way to control the logs data a user can access.

**Note:** If you configure field-level access controls on a log bucket, then to query the log entries in the log bucket you must use the **Logs Explorer** page or you must query a [linked BigQuery dataset](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset). You can't use the **Observability Analytics** page. Because BigQuery doesn't honor field-level access controls, if you query linked BigQuery dataset, then you can query all fields in the log entries.

## Overview

Logging uses field-level access control to hide [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields from users of a Google Cloud project who don't have the required permissions to view the fields. Compared to [logs views](https://docs.cloud.google.com/logging/docs/logs-views), which hide the entire `LogEntry`, field-level access controls hide individual fields of the `LogEntry`. You can set both field-level access controls and log views permissions on a Logging bucket. You restrict and manage field-level access control using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).

To restrict access to log fields, you do the following:

  * Configure the restricted `LogEntry` fields on a log bucket.
  * Give only those users who need to view the restricted fields the `logging.fieldAccessor` IAM role for that field path, or a role that contains similar permissions.



Logging checks IAM permissions when a user queries logs from a bucket that has restricted fields set. Any fields with ACLs configured are denied to users without the corresponding `logging.FieldAccessor` for that field, meaning:

  * The user receives a permission-denied error if they attempt to directly query the restricted fields.
  * Global searches don't consider the contents of the denied fields.
  * Any returned [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) results omit the restricted fields.



## Restricted fields

You can restrict access to the [`jsonPayload`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.json_payload) field, which also restricts access to its nested paths.

You can also restrict access to the leaf fields of the following:

  * [`jsonPayload`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.json_payload)
  * [`textPayload`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.text_payload)
  * [`protoPayload`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.proto_payload)
  * [`httpRequest`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.http_request)
  * [`labels`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.labels)
  * [`sourceLocation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.source_location)



For example, you can restrict access to the `labels.check_id` field.

## Before you begin

Before you get started with setting field-level access controls, do the following:

  * Verify that `gcloud --version` reports version 362.0.0 or later.

To install the latest version of the gcloud CLI, run the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command:
        
        gcloud components update
        

For instructions on how to install the gcloud CLI, see [Installing Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  * Run the [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) to configure the default Google Cloud project for your Google Cloud CLI commands. Before running the command, make the following replacement:

    * PROJECT_ID: The identifier of the project.

Command:
    
    gcloud config set project PROJECT_ID
    

  * Verify that you have one of the following [IAM](https://docs.cloud.google.com/iam/docs) roles for the Google Cloud project that contains the bucket:

    * [`roles/logging.configWriter`](https://docs.cloud.google.com/logging/docs/access-control#logging.configWriter)
    * [`roles/logging.admin`](https://docs.cloud.google.com/iam/docs/roles-overview#basic)
    * [`roles/owner`](https://docs.cloud.google.com/iam/docs/roles-overview#basic)

For information on setting IAM roles, see the Logging [Access control guide](https://docs.cloud.google.com/logging/docs/access-control).




## Set field-level access control

Field-level restrictions are configured at the [log bucket](https://docs.cloud.google.com/logging/docs/store-log-entries) level, and can be applied to an existing log bucket or when creating a new log bucket.

**Note:** [Live tailing](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) isn't supported for buckets with field-level access controls.

### Restrict fields on a new bucket

To restrict log fields when creating a new log bucket, run the [`gcloud logging buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/create) command. Before running the command, make the following replacements:

  * BUCKET_ID: The name or ID of the log bucket.
  * LOCATION: The location of the log bucket.
  * DESCRIPTION: The description of the log bucket.
  * RESTRICTED_FIELDS: The comma-separated list of fields being restricted.



Command:
    
    
    gcloud logging buckets create BUCKET_ID --location=LOCATION  \
    --description=DESCRIPTION --restricted-fields=RESTRICTED_FIELDS
    

Example command:
    
    
    gcloud logging buckets create **new-log-bucket** --location=**global** \
    --description=**"New bucket with restricted fields"** --restricted-fields=**"jsonPayload.data.ssn,httpRequest.status"**
    

### Restrict fields on an existing bucket

To restrict log fields on an existing log bucket, run the [`gcloud logging buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/update) command:
    
    
    gcloud logging buckets update BUCKET_ID --location=LOCATION  \
    --restricted-fields=RESTRICTED_FIELDS
    

Example command:
    
    
    gcloud logging buckets update **my-existing-log-bucket** --location=**global** \
    --restricted-fields=**"jsonPayload.data.ssn,httpRequest.status"**
    

If you want to add fields to your existing restrictions, your update command must relist the entire set of restricted fields. Building on the previous example, if you wanted to restrict access to the field `jsonPayload.data.entryDate` in addition to the already-restricted fields `jsonPayload.data.ssn` and `httpRequest.status`, your command would look like this:
    
    
    gcloud logging buckets update **my-existing-log-bucket** --location=**global** \
    --restricted-fields=**"jsonPayload.data.ssn,jsonPayload.data.entryDate,httpRequest.status"**
    

If you didn't relist the already-restricted fields, and just listed `jsonPayload.data.entryDate`, then both `jsonPayload.data.ssn` and `httpRequest.status` would be removed as restricted fields.

## Managing access to restricted fields

By default, Logging hides all restricted fields from users who don't have the `logging.fieldAccessor` role or a role with similar permissions. Logging exposes the restricted fields to users who have both the permission to view logs in the bucket and the `logging.fieldAccessor` role.

You can modify the default behavior to limit subsets of restricted fields to specific users.

### Granting permission on all restricted fields

To grant users permission to all restricted fields, give users the `logging.fieldAccessor` role or a custom role that contains the `logging.fieldAccessor` role.

###  Console 

To give users the `logging.fieldAccessor` role using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Select the principal, and click **Edit**.
  3. In the **Edit permissions** pane, select **Log Field Accessor** for the role.
  4. Select **Add IAM Condition**.
  5. Enter a title and description in the **Title** and **Description** fields.
  6. Select the **Condition editor** tab and enter the following expression:
         
         resource.name.extract("locations/global/buckets/{bucket}/") == "BUCKET_ID"
         

  7. Select **Save**.




The Identity and Access Management permissions are updated immediately.

###  gcloud 

To give users the `logging.fieldAccessor` role using the gcloud CLI, complete the following steps:

  1. To save the current IAM policy information in a file, run the [`gcloud projects get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy) command and save the output in a file:
         
         gcloud projects get-iam-policy PROJECT_ID --format=json > policy.json
         

The previous command saves the information in a file called `policy.json`.

  2. Update the `policy.json` file with additional bindings.

In the following, the `expression` field only lists a log bucket. Therefore, all fields for log entries stored in that log bucket are accessible to principals listed in the `members` section.
         
         "bindings": [
             {
               "condition": {
                 "description": "DESCRIPTION",
                 "expression": "resource.name.extract(\"locations/global/buckets/{bucket}/\") == 'BUCKET_ID'",
                 "title": "TITLE"
               },
               "members": [
                 PRINCIPAL
               ],
               "role": "roles/logging.fieldAccessor"
             }
         ]
         

In the previous sample, the fields have the following meanings:

     * PRINCIPAL: An identifier for the principal that you want to grant the role to. Principal identifiers usually have the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com`. For a full list of the formats that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). In the `members` field of the `policy.json` file, use the format `"PRINCIPAL-TYPE":"ID"`. 
     * DESCRIPTION: A description of the condition.
     * TITLE: A title for the condition.
  3. To apply the updated `policy.json` file, run the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command:
         
         gcloud projects set-iam-policy PROJECT_ID policy.json
         




The Identity and Access Management permissions are updated immediately.

### Granting permissions on a subset of restricted fields

To grant users permissions on a subset of the restricted fields, set the fields users can access when granting them the `logging.fieldAccessor` role or when setting a custom role that contains the `logging.fieldAccessor`.

Note the following:

  * The spelling and capitalization of the restricted field as it appears in the bucket configuration must match the spelling and capitalization of the restricted field in the IAM permission name. For example, if you set the restricted field as `jsonPayload`, you must grant permission on the `jsonPayload` field, not the `Jsonpayload` field.

  * Field paths, including map-key strings, are case-sensitive, but protobuf field paths can be expressed either as case-insensitive snake case (snake_case) or case-sensitive camel case (camelCase).

For example, `logName` is a field in the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) protobuf; `log_name` refers to the same field. The field `jsonPayload.fooBar` refers to a different field than `jsonPayload.foo_bar`, since field names beneath `jsonPayload` are map string keys; however, it does refer to `json_payload.fooBar`.

Even if field paths are valid references to the same field, you must match the spelling, capitalization, and case when you configure restrictions and IAM permissions. If, for example, you specify a restriction on `jsonPayload.foo`, then you must configure IAM permissions for `jsonPayload.foo` and not for `json_payload.foo`.




For further information on valid log field types, see [Logging query launguage: values and conversions](https://docs.cloud.google.com/logging/docs/view/logging-query-language#values_conversions).

###  Console 

To give users access to a restricted field using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Select the principal, and click **Edit**.
  3. In the **Edit permissions** pane, select **Log Field Accessor** for the role.
  4. Select **Add IAM Condition**.
  5. Enter a title and description in the **Title** and **Description** fields.
  6. Select the **Condition editor** tab and enter the following expression:
         
         resource.name.extract("locations/global/buckets/BUCKET_ID/fields/{field}") == "RESTRICTED_FIELDS"
         

  7. Select **Save**.




The Identity and Access Management permissions are updated immediately.

###  gcloud 

To give users access to a restricted field using the gcloud CLI, complete the following steps:

  1. To save the IAM information in a file, run the [`gcloud projects get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy) command and save the output in a file:
         
         gcloud projects get-iam-policy PROJECT_ID --format=json > policy.json
         

The previous command saves the information in a file called `policy.json`.

  2. Update the `policy.json` file with additional bindings.

In the following, the `expression` field lists specific fields. Therefore, only principals listed in the `members` section have access to those fields of the log entries that are stored in the specified log bucket.
         
         "bindings": [
             {
               "condition": {
                 "description": "DESCRIPTION",
                 "expression": "resource.name.extract(\"locations/global/buckets/BUCKET_ID/fields/{field}\") == 'RESTRICTED_FIELDS'",
                 "title": "TITLE"
               },
               "members": [
                 PRINCIPAL
               ],
               "role": "roles/logging.fieldAccessor"
             }
         ]
         

In the previous sample, the fields have the following meanings:

     * PRINCIPAL: An identifier for the principal that you want to grant the role to. Principal identifiers usually have the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com`. For a full list of the formats that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). In the `members` field of the `policy.json` file, use the format `"PRINCIPAL-TYPE":"ID"`. 
     * DESCRIPTION: A description of the condition.
     * TITLE: A title for the condition.
  3. To apply the updated `policy.json` file, run the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command:
         
         gcloud projects set-iam-policy PROJECT_ID policy.json
         




The Identity and Access Management permissions are updated immediately.

### Example

Assume a log bucket restricts the `jsonPayload` field, a specific label, and a specific `httpRequest` subfield. The following occurs when a user is examining their log entries

  * For users with permission to access all the restricted fields, all fields in a log entry are visible.

  * For users with permission to access only the restricted `jsonPayload` `LogEntry` field, all unrestricted fields are visible, and the `jsonPayload` field is visible.

  * For users without permission to view any of the restricted fields, only the unrestricted fields are visible.




If a user writes a query with a [global restriction](https://docs.cloud.google.com/logging/docs/view/logging-query-language#global_restrictions), then log entries that contain a restricted field are omitted from the response.

## Listing restricted fields

To list the restricted fields on a log bucket, run the following [`gcloud logging buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/describe):
    
    
    gcloud logging buckets describe BUCKET_ID --location=LOCATION
    

Example command:
    
    
    gcloud logging buckets describe **my-log-bucket** --location=**global**
    

## Quotas and limits

When setting up and using field-level access control, note the following:

  * Number of restricted fields: You can restrict up to 20 fields for each log bucket.
  * Size of restricted fields: The restricted field path must be smaller than 800 B in length.



For more information on the limits that might apply to your usage of Cloud Logging, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
