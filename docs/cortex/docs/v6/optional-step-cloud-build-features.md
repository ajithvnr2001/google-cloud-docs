---
url: https://docs.cloud.google.com/cortex/docs/v6/optional-step-cloud-build-features/
title: Cloud Build features \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:21.055341+00:00
---

# Cloud Build features  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/optional-step-cloud-build-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Build features

This page describes some optional configurations to build the Cortex Framework Data Foundation with Cloud Build features, such as building in a specific region or using a private worker pool. These configurations offer significant benefits in terms of data privacy, performance, security, and customization. The best approach depends on your specific requirements and the nature of your application.

## Build in a specific region

Regional Building ensures that your data remains within a specific geographic region. This can help you to comply with local data privacy regulation, availability and latency reduction. For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

To run the deployment through a specific [region](https://docs.cloud.google.com/build/docs/locations#selecting_the_region), add the substitution parameter `_CLOUD_BUILD_REGION` with `--region` bash parameter, as the following command:
    
    
    gcloud builds submit \
      --config=./cloudbuild.yaml \
      --substitutions=_GCS_BUCKET=BUCKET_FOR_LOGS,_CLOUD_BUILD_REGION=REGION \
      --region=REGION
    

Replace the following:

  * `BUCKET_FOR_LOGS` with the bucket name for the logs.
  * `REGION` with the region for your deployment. For more information about available regions, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).



## Build with a private worker pool

Using a [private worker pool](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool) provides a more secure environment for your builds. Private pools are private, dedicated pools of workers that offer customization over the build environment, including the ability to access resources in a private network. For more information, see [Private pools overview](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).

To configure a private worker, add the `_WORKER_POOL_NAME` with corresponding `_CLOUD_BUILD_REGION` parameter, as the following command:
    
    
    gcloud builds submit \
      --config=./cloudbuild.yaml
      --substitutions=_GCS_BUCKET=BUCKET_FOR_LOGS,_WORKER_POOL_NAME='projects/SOURCE_PROJECT/locations/us-central1/workerPools/YOUR_WORKER_POOL_NAME',_CLOUD_BUILD_REGION=REGION \
      --region=REGION
    

Replace the following:

  * `BUCKET_FOR_LOGS` with the bucket name for the logs.
  * `SOURCE_PROJECT` with the source project for Cortex Framework Data Foundation deployment.
  * `YOUR_WORKER_POOL_NAME` with the name for your worker pool.
  * `REGION` with the region for your deployment. For more information about available regions, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
