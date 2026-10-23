---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-quickstart/
title: Quickstart: Google Cloud Pipeline Components \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:21.512348+00:00
---

# Quickstart: Google Cloud Pipeline Components  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Quickstart: Google Cloud Pipeline Components Stay organized with collections  Save and categorize content based on your preferences. 

This quickstart guides you through the installation of the Google Cloud Pipeline Components (GCPC) SDK.

## Install latest release

Use the following command to install the Google Cloud SDK from the Python Package Index (PyPI):
    
    
    pip install --upgrade google-cloud-pipeline-components
    

## Import a prebuilt component by using the Google Cloud SDK

After you install the Google Cloud SDK, you can use it to import a prebuilt component.

For SDK reference information for supported components, see the [Google Cloud SDK documentation](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/index.html).

For example, you can use the following code to import and use the [Dataflow component](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataflow.html) in a pipeline.
    
    
    from google_cloud_pipeline_components.v1.dataflow import DataflowPythonJobOp
    from kfp import dsl
    
    @dsl.pipeline(
        name=PIPELINE_NAME,
        description='Dataflow launch python pipeline'
    )
    def pipeline(
        python_file_path:str = 'gs://ml-pipeline-playground/samples/dataflow/wc/wc.py',
        project_id:str = PROJECT_ID,
        location:str = LOCATION,
        staging_dir:str = PIPELINE_ROOT,
        requirements_file_path:str = 'gs://ml-pipeline-playground/samples/dataflow/wc/requirements.txt',
    ):
        dataflow_python_op = DataflowPythonJobOp(
            project=project_id,
            location=location,
            python_module_path=python_file_path,
            temp_location = staging_dir,
            requirements_file_path = requirements_file_path,
            args = ['--output', OUTPUT_FILE],
        )
    

## What's next

  * Read the [Introduction to Google Cloud Pipeline Components](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction).
  * See all [tutorials that use the `google_cloud_pipeline_components` SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/notebooks).
  * Get started with [Dataflow components](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/dataflow-component).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
