---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-failure-policy/
title: Configure failure policy \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:50.822310+00:00
---

# Configure failure policy  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-failure-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Configure failure policy Stay organized with collections  Save and categorize content based on your preferences. 

You can use the `failure_policy` parameter of the [`aiplatform.PipelineJob`](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJob) class to configure whether a pipeline should fail immediately if one of the task fails.

The following failure policy configurations are supported in Gemini Enterprise Agent Platform Pipelines:

  * **Fail fast** (`failure_policy = 'fast'`): Choose this configuration if you want the pipeline to stop scheduling new tasks after a task fails. Tasks that are already scheduled continue running until they are completed.

  * **Fail slow** (`failure_policy = 'slow'`): Choose this configuration if you want the pipeline to continue to run even after a task fails. The pipeline continues to run until all tasks have been executed.

**Note:** If you don't specify the `failure_policy` parameter for a pipeline, the failure policy configuration is set to `slow`, by default.



Use the following code sample to configure the failure policy for a pipeline using the Agent Platform SDK for Python:
    
    
    job = aiplatform.PipelineJob(display_name = 'DISPLAY_NAME',
                                 template_path = 'COMPILED_PIPELINE_PATH',
                                 pipeline_root = 'PIPELINE_ROOT',
                                 project = 'PROJECT_ID',
                                 location = 'LOCATION',
                                 failure_policy = 'FAILURE_POLICY')
    

Replace the following:

  * DISPLAY_NAME: The name of the pipeline, this will show up in the Google Cloud console.

  * COMPILED_PIPELINE_PATH: The path to your compiled pipeline YAML file. It can be a local path or a Google Cloud Storage URI.

  * PIPELINE_ROOT: Specify a Cloud Storage URI that your pipelines service account can access. The artifacts of your pipeline runs are stored within the pipeline root.

  * PROJECT_ID: The Google Cloud project that this pipeline runs in.

  * LOCATION: The region that the pipeline runs in. For more information about the regions that Agent Platform Pipelines is available in, see the [Gemini Enterprise Agent Platform locations guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations#feature-availability). If you don't set this parameter, the default location set in `aiplatform.init` is used.

  * FAILURE_POLICY: Specify the failure policy for the entire pipeline. The following configurations are available:

    * To configure the pipeline to fail after one task fails, enter `fast`.

    * To configure the pipeline to continue scheduling tasks after one task fails, enter `slow`.

If you don't set this parameter, the failure policy configuration is set to `slow`, by default.




## What's next

  * Learn how to [configure retries for failed pipeline tasks](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-retries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
