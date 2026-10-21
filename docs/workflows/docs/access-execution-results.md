---
url: https://docs.cloud.google.com/workflows/docs/access-execution-results/
title: Access workflow execution results \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:15.857635+00:00
---

# Access workflow execution results  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/access-execution-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Access workflow execution results Stay organized with collections  Save and categorize content based on your preferences. 

Workflows lets you inspect execution output, check the status of steps, and diagnose runtime errors. After you [execute a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow), you can view these results in the Google Cloud console or by using the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. To access a workflow's execution results, click the workflow's name to go to its **Workflow details** page.

  3. For details about a particular execution, on the **Executions** tab, click the execution ID in the list to go to its **Execution details** page.

**Note:** To access the **Execution details** page, you must have a role that contains the `workflows.workflows.get`, `workflows.executions.get`, and `workflows.stepEntries.list` permissions. For more information, see [Workflows roles and permissions](https://docs.cloud.google.com/workflows/docs/access-control) and [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  4. On the **Summary** tab, each execution has the following information:

     * **Execution ID** : the unique identifier of the workflow execution.
     * **Execution state** : indicates the workflow's end state, including the current or final workflow step.
     * **Execution created** : when the execution was initiated.
     * **Execution start** : when the execution began running and executing steps.
     * **Execution end** : when the execution ended.
     * **Execution duration** : total time elapsed. This can be an indication of network errors or connectivity problems.
     * **Workflow name** : the workflow name.
     * **Workflow revision** : the current revision at the time of execution.
     * **Call log level** : the level of call logging applied during the execution. For more information, see [Call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging). 
     * **Input** : the runtime arguments passed to the workflow, if any.
     * **Output** : the workflow's output. If the execution failed, includes the exception that led to the execution's failure. In this document, see Execution error maps.
  5. To view the workflow execution history as a list of step entries, click the **Steps** tab. For more information, see [View history of execution steps](https://docs.cloud.google.com/workflows/docs/debug-steps).

  6. To view the logs for a workflow execution, click the **Logs** tab.

  7. To filter the execution logs, use the **Filter** field at the top of the table. For example, to display only failed execution attempts, enter `failed` in the filter's text field.




### gcloud

  1. To see a full list of a workflow's executions, enter the following command:
         
         gcloud workflows executions list WORKFLOW_NAME
         

Replace `WORKFLOW_NAME` with your workflow's name. Copy the execution ID of the execution you're interested in.

  2. To view a workflow's execution logs, enter the following command:
         
         gcloud workflows executions describe \
             --workflow=WORKFLOW_NAME \
             EXECUTION_ID
         

Replace the following:

     * `WORKFLOW_NAME`: the workflow's name
     * `EXECUTION_ID`: the execution's unique ID

This command returns output similar to the following: 
    
    argument: 'null'
    endTime: '2022-07-19T12:40:07.070039707Z'
    error:
     context: |-
        The argument of 'in' must be a dict or an array; got: null
        in step "checkSearchTermInInput", routine "main", line: 12
     payload: "{"message":"The argument of 'in' must be a dict or an array; got: null"  
        ,"tags":["TypeError"]}"
     stackTrace:
        elements:
        - position:
           column: '26'
           length: '24'
           line: '12'
           routine: main
           step: checkSearchTermInInput
    name: projects/1051295516635/locations/us-central1/workflows/myFirstWorkflow/executions/17ffc89c-0a27-4d2f-8356-e681d949a3d3
    startTime: '2022-07-19T12:40:07.024823663Z'
    state: FAILED
    status:
     currentSteps:
     - routine: main
        step: checkSearchTermInInput
    workflowRevisionId: 000001-ac2

The output contains the following information: 
     * `argument`: the runtime arguments passed to the workflow, if any
     * `endTime`: when the execution ended
     * `error`: the error message thrown as a part of the exception that resulted in the execution's failure
     * `name`: the full name of the execution, including the name of the project, the location of the workflow, the name of the workflow, and the execution ID
     * `startTime`: when the execution began
     * `state`: indicates the workflow's end state
     * `status`: the current or final workflow step of the execution
     * `workflowRevisionID`: the current revision at the time of the execution



### Execution error maps

When a workflow throws an error during execution that isn't caught in a [`try/except` block](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors), the execution fails, and an error map (a JSON dictionary) describing the error is returned.

You can also [raise custom errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors) using the `raise` syntax.

## What's next

  * [Debugging overview](https://docs.cloud.google.com/workflows/docs/debug)
  * [Known issues for Workflows](https://docs.cloud.google.com/workflows/docs/issues)
  * [Send execution logs to Cloud Logging](https://docs.cloud.google.com/workflows/docs/log-workflow)
  * [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
