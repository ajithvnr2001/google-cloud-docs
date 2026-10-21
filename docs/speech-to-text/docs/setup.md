---
url: https://docs.cloud.google.com/speech-to-text/docs/setup/
title: Set up Cloud Speech-to-Text for your Google Cloud project \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:03.932227+00:00
---

# Set up Cloud Speech-to-Text for your Google Cloud project  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Set up Cloud Speech-to-Text for your Google Cloud project Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Speech-to-Text is an API that converts speech to text by taking audio data as input and outputting a text transcription by using Google's AI technology. This page shows you how to set up the Cloud Speech-to-Text API for your project so you can start making calls to the API.

This document covers the following:

  * Enabling and disabling the Cloud Speech-to-Text API for a Google Cloud project
  * Enabling billing for Cloud Speech-to-Text
  * Optional: Creating a new Google Cloud Storage bucket to store your audio data for large file sizes



This document does not cover how to start sending and receiving requests using the Cloud Speech-to-Text API. For information on how to start integrating Cloud Speech-to-Text into your actual code, see our [overview page](https://docs.cloud.google.com/speech-to-text/docs/overview).

## Before you begin

There are two ways to access the service: by using the REST API, or by using the Google Cloud console.

This guide covers the steps necessary to start sending requests to the REST API. If you are new to coding, we recommend that you start with the [step-by-step in-console tutorials in Google Cloud Platform](https://docs.cloud.google.com/speech-to-text/docs/quickstarts/console-tutorials) before beginning these steps.

## Enable the Cloud Speech-to-Text API for your Google Cloud project

  1. Sign in to [Google Cloud console](https://console.cloud.google.com/).

  2. Open the [project selector page](https://console.cloud.google.com/projectselector2/home/dashboard) and either choose an existing project or create a new one. For more information about creating a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  3. If you create a new project, you will be prompted to link a billing account to this project. If you are using a pre-existing project, make sure that you have billing enabled.

[Learn how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

**Note:** You must enable billing to use Cloud Speech-to-Text API, however you won't be charged unless you exceed the free quota. See the [pricing](https://cloud.google.com/speech-to-text/pricing) page for more details.
  4. Enable the Cloud Speech-to-Text API. Click the **Search products and resources** text field at the top of the page and type in **"speech"**. Select the **Cloud Speech-to-Text API** from the list of results.

  5. To enable the Cloud Speech-to-Text API for use with your project, click **Enable**. To try Cloud Speech-to-Text without linking it to your project, click **Try this API**.

  6. Optional: (API V1 only) Enable data logging. By opting in to data logging, you allow Google to record any audio data that you send to Cloud Speech-to-Text. This data is used to improve the Cloud Speech-to-Text models. Users who opt in to data logging benefit from lower pricing. See the [pricing](https://cloud.google.com/speech-to-text/pricing) and data logging [terms and conditions](https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging-terms) pages for more information.




## Optional: Create a Cloud Storage bucket

If you intend to transcribe audio longer than 60 seconds or with a file size larger than 10 MB, you must store the audio data in a Cloud Storage bucket before you can transcribe it using Cloud Speech-to-Text.

To create a new Cloud Storage bucket:

  * In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  * Click add_box **Create**. 
  * On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
    1. For **Name your bucket** , enter a unique bucket name. Don't include sensitive information in the bucket name, because the bucket namespace is global and publicly visible. 
    2. In the **Choose where to store your data** section, do the following: 
       1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
       2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
          * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
       3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

          1. In the **Bucket** menu, select a bucket.
          2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

             * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
             * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
             * Click **Done**.

    3. In the **Choose how to store your data** section, do the following: 
       1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.
       2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
    4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
    5. In the **Choose how to protect object data** section, do the following: 
       * Select any of the options under **Data protection** that you want to set for your bucket. 
         * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
         * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
         * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
           * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
           * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
       * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
  * Click **Create**. 



## Disable the Cloud Speech-to-Text API

If you no longer need to use the Cloud Speech-to-Text API with your project:

  1. Navigate to your Google Cloud dashboard and click **Go to APIs overview**.
  2. Select **Cloud Speech-to-Text API**.
  3. Click **Disable API**.



## What's next

Learn how to send a transcription request to the Cloud Speech-to-Text API using [client libraries](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-client-libraries), [gcloud](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-client-libraries), the [command line](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-client-libraries), or the [Speech-to-Text UI](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-console).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
