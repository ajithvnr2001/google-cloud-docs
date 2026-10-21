---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/install-sdk/
title: Install the Agent Platform SDK for Python \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:03.548995+00:00
---

# Install the Agent Platform SDK for Python  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/install-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Install the Agent Platform SDK for Python Stay organized with collections  Save and categorize content based on your preferences. 

Use the Agent Platform SDK for Python to automate your machine learning (ML) workflows. This page shows you how to install the Agent Platform SDK for Python. For more information about the Agent Platform SDK, see the following resources:

  * To learn about the Agent Platform SDK for Python, see [Introduction to the Agent Platform SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/use-python-sdk).
  * To learn how to train a model using the Agent Platform SDK for Python, see the [Train a model using Gemini Enterprise Agent Platform and the Python SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction).
  * To learn about the classes and methods in the Agent Platform SDK for Python, see the [Agent Platform SDK reference](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform).



Installation of the Agent Platform SDK for Python includes the following steps:

  1. Create an isolated Python environment
  2. Install the Agent Platform SDK package
  3. Initialize the Agent Platform SDK



## Create an isolated Python environment

A Python best practice is to install the Agent Platform SDK in an isolated Python environment for each project. This helps prevent dependency, version, and permissions conflicts. You can create an isolated environment for using the command line in a shell or for using a notebook.

To create an isolated environment when you use the command line, [activate a `venv` environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv). After the `venv` environment is activated, you're ready to install the Agent Platform SDK and run your Python scripts. For more information, see [Use `venv` to isolate dependencies](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv) and [Set up a Python development environment](https://docs.cloud.google.com/python/docs/setup).

To use a notebook in an isolated environment, you can create a Gemini Enterprise Agent Platform Workbench instance. Then, install the Agent Platform SDK and run your Python scripts from a notebook on your Gemini Enterprise Agent Platform Workbench instance. For more information, see [Create a Agent Platform Workbench instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create).

## Install or update the Agent Platform SDK package

To install or update the Agent Platform SDK, run the following command in your virtual environment:
    
    
    pip install --upgrade google-cloud-aiplatform
    

## Initialize the Agent Platform SDK

After you install the Agent Platform SDK for Python, you must initialize the SDK with your Gemini Enterprise Agent Platform and Google Cloud details. For example, when you initialize the SDK, you specify information such as your project name, region, and your staging Cloud Storage bucket. The following method is an example of a method that initializes the Agent Platform SDK.
    
    
    def init_sample(
        project: Optional[str] = None,
        location: Optional[str] = None,
        experiment: Optional[str] = None,
        staging_bucket: Optional[str] = None,
        credentials: Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: Optional[str] = None,
        service_account: Optional[str] = None,
    ):
    
        import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    
        [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
            project=project,
            location=location,
            experiment=experiment,
            staging_bucket=staging_bucket,
            credentials=credentials,
            encryption_spec_key_name=encryption_spec_key_name,
            service_account=service_account,
        )
    
    

## What's next

  * Learn more about the [Agent Platform SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/use-python-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
