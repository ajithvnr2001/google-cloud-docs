---
url: https://docs.cloud.google.com/workflows/docs/debug/
title: Debugging overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:12.337663+00:00
---

# Debugging overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/debug/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Debugging overview Stay organized with collections  Save and categorize content based on your preferences. 

The following information can help you when debugging Workflows and can assist you in deploying a reliable, predictable, and optimized workflow.

Projects and environments| 

  * Ideally, to protect your production resources, use separate projects for each of your environments: a project for development tasks; a project for application testing; a staging project where development can be merged into the built system; and a project for your production environment where finalized builds are available.
  * Alternatively, use separate workflows.

  
---|---  
Workflow creation| 

  * You can write your workflow in the Google Cloud console editor or by using a preferred IDE or source code editor.
  * Editing YAML files can be error-prone. [Set up autocompletion in your IDE](https://docs.cloud.google.com/workflows/docs/use-workflows-json-schema-with-ide) or editor to reduce typos and other common errors when developing your workflow. The Google Cloud console editor for Workflows does provide some YAML and syntax validation, and autocompletion; however, there could be syntax errors that must be fixed and that are only caught at deployment. See [YAML indentation](https://docs.cloud.google.com/workflows/docs/troubleshooting#indentation). 

  
Workflow deployment| 

  * You must [ deploy your workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow) from a Google Cloud project to execute it for testing.

  
Workflow execution| 

  * When testing a workflow, you can execute it by using the gcloud CLI or in the Google Cloud console: 
    * Use [`gcloud workflows run`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/run) to execute your workflow from the command line and see the results.
    * Use the [ Google Cloud console](https://docs.cloud.google.com/workflows/docs/executing-workflow#console) to execute your workflow and view the results in the **Output** pane.
  * You can [access the workflow execution results](https://docs.cloud.google.com/workflows/docs/access-execution-results) in the Google Cloud console or by using the gcloud CLI. If testing from the command line, you'll likely want to view the logs in the Google Cloud console on the **Workflow details** page.
  * You can [retrieve the history of a specified workflow execution](https://docs.cloud.google.com/workflows/docs/debug-steps) as a list of step entries, each entry providing information that can assist you in determining the source of an error or optimizing the performance of a workflow.
  * You can access a workflow's environment information (such as its location or project identifier) using built-in [environment variables](https://docs.cloud.google.com/workflows/docs/reference/environment-variables). Built-in environment variables require no declaration and are available in every workflow execution.
  * Errors thrown during a workflow execution contain [tags to help you identify what caused the error](https://docs.cloud.google.com/workflows/docs/access-execution-results#error-tags).
  * You can [ check the status of any long-running execution](https://docs.cloud.google.com/workflows/docs/executing-workflow#check_the_status_of_executions).
  * Each workflow execution automatically triggers at least two execution logs: one at the start of an execution and one at the end. You can view logs in Workflows or in Cloud Logging. To view the logs for a single workflow, [use the **Logs** tab in Workflows](https://docs.cloud.google.com/workflows/docs/log-workflow#viewing-logs-workflows). To get an aggregate view of the logs for all of your workflows, [use the **Logs Explorer** page in Cloud Logging](https://docs.cloud.google.com/workflows/docs/log-workflow#viewing-logs-logging).
  * You can send logs to Cloud Logging:
    * By enabling [call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) which lets you set a flag so that each call step or exception during the execution of your workflow is logged.
    * By creating [custom logs](https://docs.cloud.google.com/workflows/docs/log-workflow#custom_logs) that use the `sys.log` function in your source.

  
  
## What's next

  * [Known issues for Workflows](https://docs.cloud.google.com/workflows/docs/issues)
  * [Monitor workflows](https://docs.cloud.google.com/workflows/docs/monitor)
  * [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting)
  * [View history of execution steps](https://docs.cloud.google.com/workflows/docs/debug-steps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
