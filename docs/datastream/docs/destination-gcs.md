---
url: https://docs.cloud.google.com/datastream/docs/destination-gcs/
title: Configure a Cloud Storage destination \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:59.651520+00:00
---

# Configure a Cloud Storage destination  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/destination-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a Cloud Storage destination Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Datastream to write data to a Cloud Storage bucket.

Cloud Storage is a service for storing data in Google Cloud. You store the data as objects, in containers called _buckets_. When you stream to Cloud Storage, Datastream organizes data by object name and timestamp. You can then consume your data using the Cloud Storage API. For more information, see [About Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets).

## Enable the API

Enabling the Datastream API is sufficient when the destination Cloud Storage bucket is in the same project as Datastream.

If you're writing to a bucket in a different project, then you must give the [service account](https://cloud.google.com/docs/authentication#service_accounts) associated with the Datastream permission to access the bucket.

  1. Obtain the email address used for the service account. To do so, find the **Project number** in the Google Cloud console home page. The email address of the service account will be `service-[project_number]@gcp-sa-datastream.iam.gserviceaccount.com`.
  2. Give this email address the required permissions to write to the destination bucket (typically the `roles/storage.objectViewer`, `roles/storage.objectCreator` and `roles/storage.legacyBucketReader` permissions).



## Specify the destination bucket and prefix

Provide the project name, bucket name, and optional file prefix in the stream configuration to determine where the data is written.

## Write behavior

  * The data for a given stream is written to the provided bucket or file prefix at: `[bucket]/[prefix]/[object name]/yyyy/mm/dd/hh/mm/[filename(idempotent)]`.
  * The object name in the path for database sources is the schema name followed by the table name (separated by an underscore '_').
  * The timestamp in the path (hh/mm) is the source timestamp from the event metadata. 
    * For backfill events, the timestamp represents the time when the data was fetched from the source. For the Salesforce source, the timestamp represents the time when the record was last changed.
    * For CDC events, the timestamp represents when the record was changed on the source.
  * Files are rotated whenever either the maximum file size or maximum timeout is reached, whichever comes first. You can adjust the maximum file size and maximum timeout values using the [Datastream API](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams#gcsdestinationconfig).
  * Additionally, files are rotated each time a source schema change is detected (For example, a new column is added.).
  * There can be multiple files within the same path for the same minute.
  * Consuming the data can be done according to the [Cloud Storage API](https://docs.cloud.google.com/storage/docs/json_api/v1).
  * The maximum event size when you stream data into Cloud Storage is 100 MB.
  * Each non-alphanumeric character in a source column name is replaced by an underscore (`_`) in the destination file.



In some cases, most commonly when a stream first starts running, there is an overlap between backfill and CDC, resulting in duplicate events. This happens when Datastream starts reading from the current database log file (which was created before the stream was started), and this log file includes some events that are also captured by the backfill. This is anticipated behavior, and duplicate events can be eliminated using the [event metadata](https://docs.cloud.google.com/datastream/docs/events-and-streams#events), if necessary.

## What's next

  * Learn how to [stream changes to data in near real-time with Datastream](https://docs.cloud.google.com/datastream/docs/quickstart-change-streaming-to-gcs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
