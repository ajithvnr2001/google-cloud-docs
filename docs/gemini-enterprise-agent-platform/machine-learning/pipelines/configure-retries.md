---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-retries/
title: Configure retries for a pipeline task \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:03.922919+00:00
---

# Configure retries for a pipeline task  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-retries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Configure retries for a pipeline task Stay organized with collections  Save and categorize content based on your preferences. 

You can specify whether a pipeline task must be rerun if it fails, by configuring the retries for that task. You can set the number of attempts to rerun the task on failure and the delay between subsequent retries.

Use the following code sample to configure the failure policy of a pipeline task named `train_op` by using the [`set_retry`](https://kubeflow-pipelines.readthedocs.io/page/source/dsl.html#kfp.dsl.PipelineTask.set_retry) method in the Kubeflow Pipelines SDK:
    
    
    from kfp import dsl
    
    @dsl.pipeline(name='custom-container-pipeline')
    def pipeline():
      generate = generate_op()
      train = (
        train_op(
          training_data=generate.outputs['training_data'],
          test_data=generate.outputs['test_data'],
          config_file=generate.outputs['config_file'])
        .set_retry(
          num_retries=NUMBER_OF_RETRIES,
          backoff_duration='BACKOFF_DURATION',
          backoff_factor=BACKOFF_FACTOR,
          backoff_max_duration='BACKOFF_MAX_DURATION'
        )
    

Replace the following:

  * NUMBER_OF_RETRIES: The number of times to retry the task upon failure.

  * BACKOFF_DURATION: Optional. The duration of time wait after the task fails before retrying. If you don't set this parameter, the duration is set to `0s`, by default.

  * BACKOFF_FACTOR: Optional. The factor by which the backoff duration is multiplied for each subsequent retry. If you don't set this parameter, the backoff factor is set to `2.0`, by default.

  * BACKOFF_MAX_DURATION: Optional. The maximum backoff duration between subsequent retries. If you don't set this parameter, the maximum duration is set to `3600s`, by default.


**Caution:** You can't pass output parameters from other pipeline tasks or pipeline input parameters as parameter values for the set_retry method. These values must be available when you compile the pipeline.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
