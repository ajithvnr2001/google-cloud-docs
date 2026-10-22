---
url: https://docs.cloud.google.com/build/docs/securing-builds/build-log-storage/
title: Build log storage options \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:48.750612+00:00
---

# Build log storage options  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/build-log-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build log storage options Stay organized with collections  Save and categorize content based on your preferences. 

When you run builds, Cloud Build collects and stores your build logs in a log bucket. Based on build config file settings, your build logs are stored in Cloud Logging buckets, Cloud Storage buckets, or in both locations. You can also configure the type of Logging or Cloud Storage bucket that contains your logs. Your bucket's location and type affect your ability to analyze the build logs and the amount of control you have over bucket settings.

## Overview

When you set up your build config file, consider the following:

  * If you want to control the retention period of your stored build logs, then send them to Logging. The Logs Viewer in Logging also provides more options to search a bucket for specific build logs when compared to Cloud Storage. However, when you use Logging, there may be delay between when a build log is generated and when Logging receives it.

  * If you want reduced latency between when a build log is generated and when it is available in Cloud Storage, send your build logs to a bucket in Cloud Storage.




The ownership of your bucket also affects how you can interact with stored build logs. For example, a user-owned bucket lets you configure the settings of your bucket, while Google Cloud-owned buckets are created by Google Cloud and can't be changed by users. Logging and Cloud Storage have several options for configuring the type of bucket that receives your build logs.

## Bucket locations

Set up the [`logging`](https://docs.cloud.google.com/build/docs/build-config-file-schema#logging) field in your build config file to determine where your build logs are sent:

  * `GCS_ONLY`: Build logs are sent to Cloud Storage buckets.
  * `CLOUD_LOGGING_ONLY`: Build logs are sent to Logging buckets.
  * `LEGACY`: Build logs are sent to buckets in both locations. If `logging` is undefined, Cloud Build uses this value.
  * `NONE`: Build logs aren't stored.



If you send your build logs to Logging, see [Cloud Logging routing configuration](https://docs.cloud.google.com/logging/docs/routing/overview) for information about Logging bucket options. If you send your build logs to Cloud Storage, see the following section for information about available Cloud Storage buckets. The [Considerations for bucket ownership](https://docs.cloud.google.com/build/docs/securing-builds/build-log-storage#bucket-types) section describes benefits and considerations for buckets based on bucket ownership regardless of bucket location.

### Bucket options in Cloud Storage

If your build logs are sent to Cloud Storage, then Cloud Build evaluates the [`logsBucket`](https://docs.cloud.google.com/build/docs/build-config-file-schema#logs-bucket) and [`defaultLogsBucketBehavior`](https://docs.cloud.google.com/build/docs/build-config-file-schema#default-bucket) fields in your build config file to determine the type of Cloud Storage bucket that receives the build logs.

The `logsBucket` field can have any type of bucket. If `logsBucket` is defined, logs are always sent to that bucket in Cloud Storage, regardless of the `defaultLogsBucketBehavior` value. If `logsBucket` is undefined, then the value of `defaultLogsBucketBehavior` is used as follows:

  * `REGIONAL_USER_OWNED_BUCKET`: Build logs are sent to the Cloud Build-created and user-owned bucket in Cloud Storage. This bucket is in the user's project and uses the same region as the build.
  * `LEGACY_BUCKET`: Build logs are sent to the Cloud Build-created and Google Cloud-owned bucket in a Google Cloud-owned project. This value is the same as leaving this field undefined.



### Log storage when building from Dockerfiles

To set up build log storage when building from a Dockerfile, include one of the `default-buckets-behavior` flag values when running [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit):

  * `regional-user-owned-bucket`: Build logs are sent to the Cloud Build-created and user-owned bucket in Cloud Storage. This bucket is in the user's project and uses the same region as the build.
  * `legacy-bucket`: Build logs are sent to the Cloud Build-created and Google Cloud-owned bucket in a Google Cloud-owned project. This value is the same as leaving this field undefined.



## Considerations for bucket ownership

Regardless of whether you use Cloud Storage or Logging, we recommend sending your build logs to a bucket that's user-owned. This can be either a user-created bucket (for example, if you set `logsBucket` to a bucket you created), or a bucket that's Cloud Build-created but user-owned (for example, if you configured settings for a regional user-owned bucket). This way, you can edit certain properties of your bucket and view the logs in the bucket at any time. Because Google Cloud-owned buckets are in Google Cloud-owned projects, their buckets can't be viewed or edited, and their build logs can be viewed only in the **Build log** section of your **Build details** page.

**Note:** You will incur a cost for storing build logs in your own bucket. For pricing details, see [Cloud Storage pricing](https://cloud.google.com/storage/pricing) and [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing).

In general, user-created buckets provide the most flexibility in terms of configuring bucket settings both during and after bucket creation. However, in this case, you must always ensure that your user-created bucket aligns with the needs of your build. In some cases, such as managing bucket regions, using a Cloud Build-created and user-owned bucket lets you send build logs to a bucket that's available in Cloud Storage by default and always in the same region as your build. The following section provides more information about this use case:

## Considerations for bucket regions

We recommend configuring your build bucket to align with the region of your build, as this setup may help you comply with data residency requirements. If you want to align your regions this way, consider the following:

  * User-created buckets in Logging and Cloud Storage use the region defined during bucket creation. If you set a user-created bucket as your build's `logging` value, ensure that its region matches your build region.

  * If you configured your build log to use regional user-owned buckets in Cloud Storage, then your build logs are always sent to a bucket in the same region as your build.

  * Google Cloud-owned buckets are set to a Google Cloud-defined region. As a result, this region may not always align with your build's region.




## Adding `defaultLogsBucketBehavior` to existing build config files

If you're adding the `defaultLogsBucketBehavior` option to an existing build config file where you've previously configured `logging` or `logsBucket`, we recommend evaluating all of your log storage settings to ensure that your logs are stored as intended. Cloud Build ignores `defaultLogsBucketBehavior` if either of the following are true:

  * `logging` is set to `CLOUD_LOGGING_ONLY` or `NONE`.
  * `logging` is set to `GCS_ONLY` or `LEGACY`, and `logsBucket` is defined.



If you run a build with no log storage fields defined in your build config file, then Cloud Build sets `logging` to `LEGACY`.

## What's next

  * Learn how to [store, view, and delete build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs)
  * Learn about [audit logs created by Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/audit-logs).
  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn more about [Cloud Build IAM permissions](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
