---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-with-alloydb-ai/
title: Install AlloyDB Omni with AlloyDB AI \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:33.508774+00:00
---

# Install AlloyDB Omni with AlloyDB AI  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-with-alloydb-ai/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Install AlloyDB Omni with AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-with-alloydb-ai)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install-with-alloydb-ai)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/install-with-alloydb-ai)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/install-with-alloydb-ai)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/install-with-alloydb-ai)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/install-with-alloydb-ai)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-with-alloydb-ai)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-with-alloydb-ai)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/install-with-alloydb-ai)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/install-with-alloydb-ai)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/install-with-alloydb-ai)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install-with-alloydb-ai)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/install-with-alloydb-ai)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/install-with-alloydb-ai)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install-with-alloydb-ai)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install-with-alloydb-ai)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install-with-alloydb-ai)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/install-with-alloydb-ai)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/install-with-alloydb-ai)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-with-alloydb-ai)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/install-with-alloydb-ai)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-with-alloydb-ai)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-with-alloydb-ai)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-with-alloydb-ai)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This page shows you how to download and install AlloyDB Omni with AlloyDB AI. [AlloyDB AI](https://cloud.google.com/alloydb/ai) is a suite of features included with AlloyDB Omni that let you build enterprise generative AI applications.

To install AlloyDB Omni, see the following:

  * [Install AlloyDB Omni on Debian or Ubuntu](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/quickstart).

  * [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install).




You can enable AlloyDB AI when you install AlloyDB Omni. AlloyDB Omni lets you integrate with Vertex AI to query cloud-based ML models. Both editions of AlloyDB Omni let you work with online predictions and vector embeddings generated from ML models.

For more information about the ML functionality of AlloyDB, see [Build generative AI applications](https://docs.cloud.google.com/alloydb/docs/vertex-ai).

## Configure your AlloyDB Omni installation to query cloud-based models

To install AlloyDB Omni with the ability to query cloud-based models using Vertex AI, follow these steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with Google Cloud.

  2. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating), in JSON format, and download it.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  3. Store the key in a permanent location on your file system. It resides at this location for the lifetime of your AlloyDB Omni server.

Note its location on your file system; you need it for the next step.

  4. Add Vertex AI Identity and Access Management (IAM) permissions to the appropriate project and service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role="roles/aiplatform.user"

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `SERVICE_ACCOUNT_ID`: the ID of the service account that you created in the previous step. This includes the full `@PROJECT_ID.iam.gserviceaccount.com` suffix. For example: `my-service@my-project.iam.gserviceaccount.com`.

  5. Follow all of the steps in [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install), substituting the following for the `sudo alloydb database-server install` command:
         
         sudo alloydb database-server install \
             --data-dir=DATA_DIR \
             --enable-alloydb-ai=true \
             --private-key-file-path=KEY_PATH \
             --vertex-ai-region="LOCATION"

Replace the following:

     * `DATA_DIR`: the file system path that you want AlloyDB Omni to use for its data directory.

     * `KEY_PATH`: the file system path to the service account key that you downloaded in the previous step.

     * `LOCATION`: a Google Cloud region—for example, `us-central1`. For a list of regions that support generative AI, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/learn/locations-genai).




## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/run-connect)
  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage)
  * [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/model-endpoint-overview)
  * [Register and call remote AI models](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/model-endpoint-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
