---
url: https://docs.cloud.google.com/workflows/docs/reference/environment-variables/
title: Built-in environment variables \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:35.282863+00:00
---

# Built-in environment variables  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Built-in environment variables Stay organized with collections  Save and categorize content based on your preferences. 

You can access a workflow's environment information using built-in environment variables. Built-in environment variables require no declaration and are available in every workflow execution.

[User-defined environment variables](https://docs.cloud.google.com/workflows/docs/use-environment-variables) are also supported.

## List of built-in environment variables

You can use the following built-in environment variables:

  * `GOOGLE_CLOUD_LOCATION`: The location of the workflow.
  * `GOOGLE_CLOUD_PROJECT_ID`: The project identifier of the workflow.
  * `GOOGLE_CLOUD_PROJECT_NUMBER`: The project number of the workflow.
  * `GOOGLE_CLOUD_SERVICE_ACCOUNT_NAME`: The name of the workflow execution's service account.
  * `GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID`: The identifier of the workflow execution.
  * `GOOGLE_CLOUD_WORKFLOW_ID`: The identifier of the workflow.
  * `GOOGLE_CLOUD_WORKFLOW_REVISION_ID`: The identifier of the workflow revision.



## Access built-in environment variables

To access an environment variable, make a call to the `sys.get_env()` function in an expression, passing the name of the environment variable as a parameter. The name of the environment variable must be passed as a string.

For example, the following step assigns the value of the environment variable `GOOGLE_CLOUD_PROJECT_ID` to a workflow variable called `projectID`: 
    
    
    - getProjectID:
        assign:
          - projectID: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
