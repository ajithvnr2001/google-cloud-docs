---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/migrate-kfp/
title: Migrate from Kubeflow Pipelines to Gemini Enterprise Agent Platform Pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:11.191273+00:00
---

# Migrate from Kubeflow Pipelines to Gemini Enterprise Agent Platform Pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/migrate-kfp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Migrate from Kubeflow Pipelines to Gemini Enterprise Agent Platform Pipelines Stay organized with collections  Save and categorize content based on your preferences. 

For developers with experience building Kubeflow pipelines it is important to understand the following ways that Agent Platform Pipelines is different from Kubeflow Pipelines.

### Data passing (inputs/outputs)

  * Data passing using inputs and outputs differs from Kubeflow Pipelines SDK v1 to Kubeflow Pipelines SDK v2. Kubeflow Pipelines SDK v2 has the separation of parameters and artifacts, and they can't be passed into one another. For more detailed information, see [Kubeflow Pipelines Pipelines Basics](https://www.kubeflow.org/docs/components/pipelines/v2/pipelines/pipeline-basics/) and [Kubeflow Pipelines Data Types](https://www.kubeflow.org/docs/components/pipelines/v2/data-types/).



### Domain-specific language (DSL) version usage

  * Agent Platform Pipelines can run pipelines that were built using TFX v0.30.0 or later, _or_ the Kubeflow Pipelines SDK v2 domain-specific language (DSL).

The Kubeflow Pipelines SDK v2 DSL is available in Kubeflow Pipelines SDK v1.6 or later.

Kubeflow Pipelines can run pipelines that were built using the Kubeflow Pipelines SDK. Kubeflow Pipelines v1.6 or later can also run pipelines built using the Kubeflow Pipelines SDK v2 DSL.




### Storage

  * Kubeflow Pipelines and Agent Platform Pipelines handle storage differently. In Kubeflow Pipelines you can make use of Kubernetes resources such as persistent volume claims. In Agent Platform Pipelines your data is stored on Cloud Storage, and mounted into your components using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse).

In Agent Platform Pipelines, you can use Google Cloud services to make resources available — for example, you can use Cloud Storage FUSE to access a Cloud Storage bucket as a mounted volume in a pipeline step. If your Cloud Storage URI is `gs://example-bucket/example-pipeline`, then your pipeline component's container can use Cloud Storage FUSE to access that URI as the following path: `/gcs/example-bucket/example-pipeline`.

**Important:** It's best practice that you avoid hardcoding the paths to external resources into your pipeline. Instead, pass the paths to external resources into your pipeline as a parameter. This makes it easier for you to run your pipeline in different environments, and to change the location of the resources used in a pipeline run.
  * When you run a pipeline using Agent Platform Pipelines, the pipeline root must have been specified in the `@pipeline` annotation or when you created the pipeline run.

In Kubeflow Pipelines, specifying the pipeline root is optional. The artifacts of a pipeline run are stored using [MinIO](https://min.io/) by default.




### Features not supported in Agent Platform Pipelines

  * The following Kubeflow Pipelines features are not supported in Agent Platform Pipelines.

    * **Cache Expiration** : In Kubeflow Pipelines, you can specify that cached component executions expire after a specified amount of time using the Kubeflow Pipelines SDK v1 DSL.

You can't specify that component executions expire after a specified amount of time using the Kubeflow Pipelines SDK v2 DSL.

In Agent Platform Pipelines, when you run a pipeline using `create_run_from_job_spec` you can use the `enable_caching` argument to specify that this pipeline run does not use caching.

    * **Recursion** : In Kubeflow Pipelines, you can specify pipeline components that are called recursively.

Agent Platform Pipelines doesn't support pipeline components that are called recursively.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
