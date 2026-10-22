---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-caching/
title: Configure execution caching \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:43:55.105116+00:00
---

# Configure execution caching  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Configure execution caching Stay organized with collections  Save and categorize content based on your preferences. 

When Gemini Enterprise Agent Platform Pipelines runs a pipeline, it checks to see whether or not an _execution_ exists in Vertex ML Metadata with the interface (cache key) of each pipeline step.

The step's interface is defined as the combination of the following:

  1. The **pipeline step's inputs**. These inputs include the input parameters' value (if any) and the input artifact ID (if any).

  2. The **pipeline step's output definition**. This output definition includes output parameter definition (name, if any) and output artifact definition (name, if any).

  3. The **component's specification**. This specification includes the image, commands, arguments and environment variables being used, as well as the order of the commands and arguments.




Additionally, only the pipelines with the same pipeline name will share the cache.

If there is a matching execution in Vertex ML Metadata, the outputs of that execution are used and the step is skipped. This helps to reduce costs by skipping computations that were completed in a previous pipeline run.

You can turn off execution caching at task level by setting the following:
    
    
    eval_task.set_caching_options(False)
    

You can turn off execution caching for an entire pipeline job. When you run a pipeline using `PipelineJob()`, you can use the `enable_caching` argument to specify that this pipeline run does not use caching. All steps within the pipeline job won't use caching. [Learn more about creating pipeline runs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/run-pipeline).

Use the following sample to turn off caching:
    
    
    pl = PipelineJob(
        display_name="My first pipeline",
    
        # Whether or not to enable caching
        # True = enable the current run to use caching results from previous runs
        # False = disable the current run's use of caching results from previous runs
        # None = defer to cache option for each pipeline component in the pipeline definition
        enable_caching=False,
    
        # Local or Cloud Storage path to a compiled pipeline definition
        template_path="pipeline.yaml",
    
        # Dictionary containing input parameters for your pipeline
        parameter_values=parameter_values,
    
        # Cloud Storage path to act as the pipeline root
        pipeline_root=pipeline_root,
    )
    
    

**Important:** Pipeline components should be built to be deterministic. A given set of inputs should always produce the same output. Depending on their interface, non-deterministic pipeline components can be unexpectedly skipped due to execution caching.

The following limitations apply to this feature:

  * The cached result doesn't have a time to live (TTL), and can be reused as long as the entry is not deleted from the Vertex ML Metadata. If the entry is deleted from Vertex ML Metadata, the task will rerun to regenerate the result again.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
