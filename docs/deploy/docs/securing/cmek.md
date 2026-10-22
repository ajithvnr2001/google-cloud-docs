---
url: https://docs.cloud.google.com/deploy/docs/securing/cmek/
title: Use customer-managed encryption keys \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:06.580025+00:00
---

# Use customer-managed encryption keys  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/securing/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Use customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Deploy, along with its dependent services, lets you manage your own encryption keys for storage and transit of any user data.

## Cloud Deploy data

Cloud Deploy stores resource data encrypted. This storage does not include any user data.

Cloud Deploy dependent services can use customer-managed encryption keys. The sections that follow address the practices of each dependent service.

## Cloud Build

Render and deploy operations are performed through Cloud Build, which is CMEK compliant. For more information on configuring Cloud Build to be CMEK compliant, see the [Cloud Build documentation](https://cloud.google.com/build/docs/securing-builds/cmek).

Rendering source and rendered manifests are stored in Cloud Storage buckets. Cloud Build stores its logs using Cloud Logging, and Cloud Deploy explicitly turns off Cloud Storage logging for use with Cloud Deploy.

## Cloud Storage

To use CMEK with Cloud Deploy, you need to use custom Cloud Storage buckets and [configure those buckets for CMEK](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).

To specify your custom, CMEK-managed Cloud Storage buckets for use with Cloud Deploy:

  * Include the [`--gcs-source-staging-dir`](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--gcs-source-staging-dir) flag on the `gcloud deploy releases create` command.

This flag identifies the Cloud Storage bucket in which to store the rendering source files.

  * [Change the storage location](https://docs.cloud.google.com/deploy/docs/execution-environment#changing_the_storage_location) in your Cloud Deploy execution environment.

This setting identifies the Cloud Storage bucket in which to store your rendered manifests.




## Pub/Sub topics

Cloud Deploy [uses Pub/Sub to publish notifications to topics](https://docs.cloud.google.com/deploy/docs/subscribe-deploy-notifications). You can [configure these topics to use customer-managed encryption keys](https://docs.cloud.google.com/pubsub/docs/encryption#using-cmek).

## Logging

Cloud Deploy and its dependent services publish logs to Cloud Logging, part of Google Cloud Observability.

You can [configure Logging for CMEK](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
