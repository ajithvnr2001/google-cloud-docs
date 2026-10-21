---
url: https://docs.cloud.google.com/workflows/docs/debug-steps/
title: View history of execution steps \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:12.605498+00:00
---

# View history of execution steps  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/debug-steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  View history of execution steps Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Detailed execution history (expected iterations, in-scope variables)**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can retrieve the history of a specified workflow execution as a list of _step entries_. Each step entry provides information that can assist you when analyzing, debugging, or optimizing a workflow. For example, you can confirm which steps actually executed, and you can determine the duration and success of a step. This can be particularly helpful when debugging a large or complicated non-linear workflow (one with many parallel branches, for example).

A step entry represents either an actual step in the source code (for example, `assign` or `call`) or an instruction block (for example, a `for` loop or a `try/retry/except` block). For a complete list of step types, see [StepType](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries#steptype).

**Note:** To enable step entries and their history for any pre-existing workflow, you must re-deploy the workflow.

## Execution history level

When [creating](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow) or [executing](https://docs.cloud.google.com/workflows/docs/executing-workflow#execute_a_workflow) a workflow, you can specify a **Basic** or **Detailed** execution history. You can apply this setting at either the workflow or execution level.

By default, no execution history level is specified and **Basic** step entries are returned.

If you want the execution history to include any in-scope variable values and, if applicable, the expected number of iterations (for example, when using a `for` loop, or a parallel branch or iteration), you must set the execution history level to **Detailed**.

If an execution history level is not specified for an execution, it is determined by the level applied to the workflow. If the levels are different, the setting applied at the execution level overrides the setting applied at the workflow level for that execution.

**Note:** Specifying a **Detailed** execution history level might have a slight impact on execution performance.

## How to retrieve step entries

You can retrieve step entries either by sending a request to the Workflow Executions REST API or through the Google Cloud console:

  * Google Cloud console—in this document, see View step entries in the console.

In addition to listing the step entries and their details, the console provides a graphical representation of the execution steps, making it easier to view and analyze the path of a workflow execution.

  * Workflow Executions REST API—in this document, see Retrieve a step entry and List step entries.




## Step entry information

A step entry includes the following information. Detailed step entries also include the basic step entry information.

For more information, in this document, see the Examples.

### Basic step entry information

Name | Full resource name of the step entry which is a unique ID with the following format, and where `STEPENTRY_ID` is an increasing counter: 
    
    
    projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/STEPENTRY_ID

For example: 
    
    
    projects/123456789012/locations/us-central1/workflows/myFirstWorkflow/executions/ae8a66a1-cefa-4d16-8a2f-d50c712d8ef1/stepEntries/2  
  
---|---  
Create and update times | Timestamps for the creation time of the step entry and its most recent update. If a step entry has completed, `updateTime` indicates the completion time.   
Routine and step names | Names of the routine and step that the step entry belongs to. A routine name is the subworkflow name defined in the YAML or JSON source code. The top level routine name is `main`.   
State and progress type | State of the step entry—for example, if the entry has succeeded or failed, or if a step entry is in progress and the type of progress. For a complete list of states and progress types, see [State](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries#state) and [ProgressType](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries#progresstype).   
Navigation information | Position of the step entry so that you can better understand the hierarchy and flow of the workflow—for example, what step entries come before or after the current step entry, or which are parents or children of the step entry. For details, see [NavigationInfo](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries#navigationinfo).   
Metadata | Data related to an iterative step entry, which can include the following:

  * An ID that indicates the child thread—for example, which `STEP_PARALLEL_BRANCH_ENTRY` in `STEP_PARALLEL_BRANCH`
  * The iteration of a `for` loop—for example, which `STEP_FOR_ITERATION` in `STEP_FOR`

For details, see [StepEntryMetadata](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries#stepentrymetadata).   
Exceptions | Payload related to any exceptions and that provides a description of why a step entry has failed.   
  
### Detailed step entry information

Metadata | If applicable, the expected number of iterations in the step's progress—for example, when using a `for` loop, a parallel branch, or an iteration. Note that the calculated count won't work as expected if the loop bounds include expressions that incorporate any of the following:

  * A nested expression depth that exceeds 10
  * Built-in functions other than `len()`
  * Evaluations that involve values such as `.inf`, `-.inf`, `.NAN`, `Infinity`, or `-Infinity`
  * Errors

For details, see [StepEntryMetadata](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries#stepentrymetadata).   
---|---  
Variable data | Data related to in-scope variable values associated with this step including the names and values of user‑defined local variables and the results of expression evaluations. Note that the scope excludes internal variables linked to Workflows built-in functions. For details, see [VariableData](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries#variabledata).   
  
## View step entries in the console

You can view the step entries for a specific workflow execution in the Google Cloud console.

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow to go to its **Workflow details** page.

  3. For details about a particular execution, click its execution ID.

**Note:** To access the **Execution details** page, you must have a role that contains the `workflows.workflows.get`, `workflows.executions.get`, and `workflows.stepEntries.list` permissions. For more information, see [Workflows roles and permissions](https://docs.cloud.google.com/workflows/docs/access-control) and [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

On the **Summary** tab, information about the overall execution is provided, including any exception that led to the failure of the execution. For more information, see [Execution error maps](https://docs.cloud.google.com/workflows/docs/access-execution-results#execution_errors).

  4. To view the workflow execution history as a list of step entries, click the **Steps** tab.

All step entries for the workflow execution are listed.

  5. To filter the step entries, use the **Filter** field at the top of the table to select a property and a value—for example, `State: Failed`.

  6. To display links for any **Parent** , **Children** , **Next** , and **Previous** step entries, click a specific step entry.

If you click a link, the other links automatically update. For example, **Parent** will link to the parent of the step entry that you clicked.

  7. The **Visualization** panel provides a graphical representation of the steps in the workflow and helps you understand the workflow path.

#### Visualization panel example

_Click diagram to enlarge it:_

[ ![Visualization panel displaying workflow with failed steps](https://docs.cloud.google.com/static/workflows/images/steps-history-screenshot.png)](https://docs.cloud.google.com/static/workflows/images/steps-history-screenshot.png)

Note that the visualization can differ from the step entries. For example, a `for` block is depicted as a single component in the visualization; however, depending on the number of iterations, there can be multiple step entries.

You can do the following in the panel:

     * Zoom in or out of the visualization
     * Collapse or expand parent step entries
     * Click a step entry and view its previous and next entries
     * Confirm successful and failed step entries as indicated by a green checkmark or red exclamation mark
     * Close the **Visualization** panel by clicking the last_pageexpander arrow; click it again to open the panel



## Before you retrieve a step entry

To get the permissions that you need to retrieve a step entry, ask your administrator to grant you the Workflows Admin (`workflows.stepEntries.get`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Retrieve a step entry

To retrieve a step entry for a given workflow execution, use the [`projects.locations.workflows.executions.stepEntries.get`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries/get) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number listed in the [IAM & Admin Settings](https://console.cloud.google.com/iam-admin/settings/project) page.
  * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) in which the workflow is deployed—for example, `us-central1`.
  * `WORKFLOW_ID`: the user-defined name for the workflow—for example, `myFirstWorkflow`.
  * `EXECUTION_ID`: the unique ID for a workflow execution which is returned after a workflow is executed.
  * `STEPENTRY_ID`: the unique ID for a step entry—for example, `1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/STEPENTRY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/STEPENTRY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/STEPENTRY_ID",
      "createTime": "2024-08-15T19:03:08.328851864Z",
      "updateTime": "2024-08-15T19:03:08.331099634Z",
      "routine": "main",
      "step": "checkSearchTermInInput",
      "stepType": "STEP_CONDITION",
      "state": "STATE_SUCCEEDED",
      "entryId": "2",
      "navigationInfo": {
        "children": [
          "3"
        ],
        "parent": "1",
        "next": "3",
        "previous": "1"
      },
      "variableData": {}
    }
    

## Before you list step entries

To get the permissions that you need to list step entries, ask your administrator to grant you the Workflows Admin (`workflows.stepEntries.list`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List step entries

To list the step entries for a given workflow execution, use the [`projects.locations.workflows.executions.stepEntries.list`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries/list) method. By default, results are returned in ascending order of the `createTime` of the step entries.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number listed in the [IAM & Admin Settings](https://console.cloud.google.com/iam-admin/settings/project) page.
  * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) in which the workflow is deployed—for example, `us-central1`.
  * `WORKFLOW_ID`: the user-defined name for the workflow—for example, `myFirstWorkflow`.
  * `EXECUTION_ID`: the unique ID for a workflow execution which is returned after a workflow is executed.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "stepEntries": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/1",
          "createTime": "2024-08-15T19:03:08.328807964Z",
          "updateTime": "2024-08-15T19:03:08.331099694Z",
          "routine": "main",
          "step": "checkSearchTermInInput",
          "stepType": "STEP_SWITCH",
          "state": "STATE_SUCCEEDED",
          "entryId": "1",
          "navigationInfo": {
            "children": [
              "2"
            ],
            "next": "2"
          },
          "variableData": {}
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/2",
          "createTime": "2024-08-15T19:03:08.328851864Z",
          "updateTime": "2024-08-15T19:03:08.331099634Z",
          "routine": "main",
          "step": "checkSearchTermInInput",
          "stepType": "STEP_CONDITION",
          "state": "STATE_SUCCEEDED",
          "entryId": "2",
          "navigationInfo": {
            "children": [
              "3"
            ],
            "parent": "1",
            "next": "3",
            "previous": "1"
          },
          "variableData": {}
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/3",
          "createTime": "2024-08-15T19:03:08.331037314Z",
          "updateTime": "2024-08-15T19:03:08.331099554Z",
          "routine": "main",
          "step": "checkSearchTermInInput.condition1",
          "stepType": "STEP_ASSIGN",
          "state": "STATE_SUCCEEDED",
          "entryId": "3",
          "navigationInfo": {
            "parent": "2",
            "next": "4",
            "previous": "2"
          },
          "variableData": {
            "variables": {
              "input": {
                "searchTerm": "asia"
              },
              "searchTerm": "asia"
            }
          }
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/4",
          "createTime": "2024-08-15T19:03:08.331100404Z",
          "updateTime": "2024-08-15T19:03:08.633741469Z",
          "routine": "main",
          "step": "readWikipedia",
          "stepType": "STEP_CALL",
          "state": "STATE_SUCCEEDED",
          "entryId": "4",
          "navigationInfo": {
            "next": "5",
            "previous": "3"
          },
          "variableData": {}
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_ID/executions/EXECUTION_ID/stepEntries/5",
          "createTime": "2024-08-15T19:03:08.633969694Z",
          "updateTime": "2024-08-15T19:03:08.634063018Z",
          "routine": "main",
          "step": "returnOutput",
          "stepType": "STEP_RETURN",
          "state": "STATE_SUCCEEDED",
          "entryId": "5",
          "navigationInfo": {
            "previous": "4"
          },
          "variableData": {
            "variables": {
              "wikiResult": {
                "headers": {
                  ...
                },
                "body": [
                  ...
                ],
                "code": 200
              },
              "input": {
                "searchTerm": "asia"
              },
              "searchTerm": "asia"
            }
          }
        }
      ],
      "totalSize": 5
    }
    

## Delete step entries

To delete all the step entries for a given workflow execution, use the [`projects.locations.workflows.executions.deleteExecutionHistory`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/deleteExecutionHistory) method.

Before using any of the request data, make the following replacements: 

  * `WORKFLOW_NAME`: the name of the workflow.
  * `PROJECT_NUMBER`: your Google Cloud project number.
  * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) in which the workflow is deployed—for example, `us-central1`.
  * `EXECUTION_ID`: the ID of the execution for which step entries should be deleted.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_NAME/executions/EXECUTION_ID:deleteExecutionHistory"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_NAME/executions/EXECUTION_ID:deleteExecutionHistory" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/deleteExecutionHistory). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body is empty. 

## Examples

#### Workflow with a `for` block

#### Workflow

### YAML
    
    
    - assignStep:
        assign:
          - sum: 0
    - forStep:
        for:
          range: [1, 2]
          value: v
          steps:
            - sumStep:
                assign:
                  - sum: ${sum + v}
    - returnStep:
        return: ${sum}

### JSON
    
    
    [
      {
        "assignStep": {
          "assign": [
            {
              "sum": 0
            }
          ]
        }
      },
      {
        "forStep": {
          "for": {
            "range": [
              1,
              2
            ],
            "value": "v",
            "steps": [
              {
                "sumStep": {
                  "assign": [
                    {
                      "sum": "${sum + v}"
                    }
                  ]
                }
              }
            ]
          }
        }
      },
      {
        "returnStep": {
          "return": "${sum}"
        }
      }
    ]

#### Diagram

[ ![Workflow with a for block](https://docs.cloud.google.com/static/workflows/images/debug-for-block.svg)](https://docs.cloud.google.com/static/workflows/images/debug-for-block.svg) **Figure 1.** Workflow with a `for` block (click diagram to enlarge).

#### Step entries
    
    
    {
      "stepEntries": [
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-for-block/executions/0bc47b85-a399-4101-b629-1f623802e32d/stepEntries/1",
          "createTime": "2024-08-15T19:32:18.119578307Z",
          "updateTime": "2024-08-15T19:32:18.119661828Z",
          "routine": "main",
          "step": "assignStep",
          "stepType": "STEP_ASSIGN",
          "state": "STATE_SUCCEEDED",
          "entryId": "1",
          "navigationInfo": {
            "next": "2"
          },
          "variableData": {
            "variables": {
              "sum": 0
            }
          }
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-for-block/executions/0bc47b85-a399-4101-b629-1f623802e32d/stepEntries/2",
          "createTime": "2024-08-15T19:32:18.119662643Z",
          "updateTime": "2024-08-15T19:32:18.120893531Z",
          "routine": "main",
          "step": "forStep",
          "stepType": "STEP_FOR",
          "state": "STATE_SUCCEEDED",
          "entryId": "2",
          "navigationInfo": {
            "children": [
              "3",
              "5"
            ],
            "next": "3",
            "previous": "1"
          },
          "stepEntryMetadata": {
            "progressType": "PROGRESS_TYPE_FOR",
            "expectedIteration": "2"
          },
          "variableData": {}
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-for-block/executions/0bc47b85-a399-4101-b629-1f623802e32d/stepEntries/3",
          "createTime": "2024-08-15T19:32:18.119732820Z",
          "updateTime": "2024-08-15T19:32:18.120463449Z",
          "routine": "main",
          "step": "forStep",
          "stepType": "STEP_FOR_ITERATION",
          "state": "STATE_SUCCEEDED",
          "entryId": "3",
          "navigationInfo": {
            "children": [
              "4"
            ],
            "parent": "2",
            "next": "4",
            "previous": "2"
          },
          "stepEntryMetadata": {
            "progressType": "PROGRESS_TYPE_FOR",
            "progressNumber": "1"
          },
          "variableData": {}
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-for-block/executions/0bc47b85-a399-4101-b629-1f623802e32d/stepEntries/4",
          "createTime": "2024-08-15T19:32:18.119737066Z",
          "updateTime": "2024-08-15T19:32:18.120463358Z",
          "routine": "main",
          "step": "sumStep",
          "stepType": "STEP_ASSIGN",
          "state": "STATE_SUCCEEDED",
          "entryId": "4",
          "navigationInfo": {
            "parent": "3",
            "next": "5",
            "previous": "3"
          },
          "stepEntryMetadata": {
            "progressType": "PROGRESS_TYPE_FOR",
            "progressNumber": "1"
          },
          "variableData": {
            "variables": {
              "sum": 1,
              "v": 1
            }
          }
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-for-block/executions/0bc47b85-a399-4101-b629-1f623802e32d/stepEntries/5",
          "createTime": "2024-08-15T19:32:18.120465172Z",
          "updateTime": "2024-08-15T19:32:18.120893471Z",
          "routine": "main",
          "step": "forStep",
          "stepType": "STEP_FOR_ITERATION",
          "state": "STATE_SUCCEEDED",
          "entryId": "5",
          "navigationInfo": {
            "children": [
              "6"
            ],
            "parent": "2",
            "next": "6",
            "previous": "4"
          },
          "stepEntryMetadata": {
            "progressType": "PROGRESS_TYPE_FOR",
            "progressNumber": "2"
          },
          "variableData": {}
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-for-block/executions/0bc47b85-a399-4101-b629-1f623802e32d/stepEntries/6",
          "createTime": "2024-08-15T19:32:18.120470187Z",
          "updateTime": "2024-08-15T19:32:18.120893389Z",
          "routine": "main",
          "step": "sumStep",
          "stepType": "STEP_ASSIGN",
          "state": "STATE_SUCCEEDED",
          "entryId": "6",
          "navigationInfo": {
            "parent": "5",
            "next": "7",
            "previous": "5"
          },
          "stepEntryMetadata": {
            "progressType": "PROGRESS_TYPE_FOR",
            "progressNumber": "2"
          },
          "variableData": {
            "variables": {
              "sum": 3,
              "v": 2
            }
          }
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-for-block/executions/0bc47b85-a399-4101-b629-1f623802e32d/stepEntries/7",
          "createTime": "2024-08-15T19:32:18.120894873Z",
          "updateTime": "2024-08-15T19:32:18.121003185Z",
          "routine": "main",
          "step": "returnStep",
          "stepType": "STEP_RETURN",
          "state": "STATE_SUCCEEDED",
          "entryId": "7",
          "navigationInfo": {
            "previous": "6"
          },
          "variableData": {
            "variables": {
              "sum": 3
            }
          }
        }
      ],
      "totalSize": 7
    }

#### Workflow with a subworkflow call

#### Workflow

### YAML
    
    
    main:
      steps:
        - callStep:
            call: square
            args:
              x: 10
            result: t
        - retStep:
            return: ${t}
    square:
      params: [x]
      steps:
        - assignStep:
            assign:
              - y: ${x*x}
        - retStep:
            return: ${y}

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "callStep": {
              "call": "square",
              "args": {
                "x": 10
              },
              "result": "t"
            }
          },
          {
            "retStep": {
              "return": "${t}"
            }
          }
        ]
      },
      "square": {
        "params": [
          "x"
        ],
        "steps": [
          {
            "assignStep": {
              "assign": [
                {
                  "y": "${x*x}"
                }
              ]
            }
          },
          {
            "retStep": {
              "return": "${y}"
            }
          }
        ]
      }
    }

#### Diagram

[ ![Workflow with a subworkflow call](https://docs.cloud.google.com/static/workflows/images/debug-subworkflow.svg)](https://docs.cloud.google.com/static/workflows/images/debug-subworkflow.svg) **Figure 2.** Workflow with a subworkflow call (click diagram to enlarge).

#### Step entries
    
    
    {
      "stepEntries": [
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-subworkflow-call/executions/e203bc96-a1cf-47ba-b6de-f3d1b0909664/stepEntries/1",
          "createTime": "2024-08-15T19:37:44.162778920Z",
          "updateTime": "2024-08-15T19:37:44.168683007Z",
          "routine": "main",
          "step": "callStep",
          "stepType": "STEP_CALL",
          "state": "STATE_SUCCEEDED",
          "entryId": "1",
          "navigationInfo": {
            "children": [
              "2",
              "3"
            ],
            "next": "2"
          },
          "variableData": {
            "variables": {
              "t": 100
            }
          }
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-subworkflow-call/executions/e203bc96-a1cf-47ba-b6de-f3d1b0909664/stepEntries/2",
          "createTime": "2024-08-15T19:37:44.168598736Z",
          "updateTime": "2024-08-15T19:37:44.168657969Z",
          "routine": "square",
          "step": "assignStep",
          "stepType": "STEP_ASSIGN",
          "state": "STATE_SUCCEEDED",
          "entryId": "2",
          "navigationInfo": {
            "parent": "1",
            "next": "3",
            "previous": "1"
          },
          "variableData": {
            "variables": {
              "y": 100,
              "x": 10
            }
          }
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-subworkflow-call/executions/e203bc96-a1cf-47ba-b6de-f3d1b0909664/stepEntries/3",
          "createTime": "2024-08-15T19:37:44.168659349Z",
          "updateTime": "2024-08-15T19:37:44.168676547Z",
          "routine": "square",
          "step": "retStep",
          "stepType": "STEP_RETURN",
          "state": "STATE_SUCCEEDED",
          "entryId": "3",
          "navigationInfo": {
            "parent": "1",
            "next": "4",
            "previous": "2"
          },
          "variableData": {
            "variables": {
              "x": 10,
              "y": 100
            }
          }
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-subworkflow-call/executions/e203bc96-a1cf-47ba-b6de-f3d1b0909664/stepEntries/4",
          "createTime": "2024-08-15T19:37:44.168693503Z",
          "updateTime": "2024-08-15T19:37:44.168702324Z",
          "routine": "main",
          "step": "retStep",
          "stepType": "STEP_RETURN",
          "state": "STATE_SUCCEEDED",
          "entryId": "4",
          "navigationInfo": {
            "previous": "3"
          },
          "variableData": {
            "variables": {
              "t": 100
            }
          }
        }
      ],
      "totalSize": 4
    }

#### Workflow with a failed step entry

#### Workflow

### YAML
    
    
    - tryStep:
        try:
          return: ${1 / 0}
        except:
          return: 0

### JSON
    
    
    [
      {
        "tryStep": {
          "try": {
            "return": "${1 / 0}"
          },
          "except": {
            "return": 0
          }
        }
      }
    ]

#### Diagram

[ ![Workflow with a failed step entry](https://docs.cloud.google.com/static/workflows/images/debug-failed-step.svg)](https://docs.cloud.google.com/static/workflows/images/debug-failed-step.svg) **Figure 3.** Workflow with a failed step entry (click diagram to enlarge).

#### Step entries
    
    
    {
      "stepEntries": [
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-failed-step/executions/a19d20d1-e446-4d37-b548-8005297b7d3d/stepEntries/1",
          "createTime": "2024-08-15T19:42:51.415433810Z",
          "updateTime": "2024-08-15T19:42:51.416106923Z",
          "routine": "main",
          "step": "tryStep",
          "stepType": "STEP_TRY_RETRY_EXCEPT",
          "state": "STATE_SUCCEEDED",
          "entryId": "1",
          "navigationInfo": {
            "children": [
              "2",
              "4"
            ],
            "next": "2"
          },
          "variableData": {}
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-failed-step/executions/a19d20d1-e446-4d37-b548-8005297b7d3d/stepEntries/2",
          "createTime": "2024-08-15T19:42:51.415439617Z",
          "updateTime": "2024-08-15T19:42:51.416065206Z",
          "routine": "main",
          "step": "tryStep",
          "stepType": "STEP_TRY",
          "state": "STATE_FAILED",
          "entryId": "2",
          "navigationInfo": {
            "children": [
              "3"
            ],
            "parent": "1",
            "next": "3",
            "previous": "1"
          },
          "variableData": {}
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-failed-step/executions/a19d20d1-e446-4d37-b548-8005297b7d3d/stepEntries/3",
          "createTime": "2024-08-15T19:42:51.415441815Z",
          "updateTime": "2024-08-15T19:42:51.416064665Z",
          "routine": "main",
          "step": "tryStep.try",
          "stepType": "STEP_RETURN",
          "state": "STATE_FAILED",
          "exception": {
            "payload": "{\"message\":\"ZeroDivisionError: division by zero\",\"tags\":[\"ZeroDivisionError\",\"ArithmeticError\"]}"
          },
          "entryId": "3",
          "navigationInfo": {
            "parent": "2",
            "next": "4",
            "previous": "2"
          },
          "variableData": {}
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-failed-step/executions/a19d20d1-e446-4d37-b548-8005297b7d3d/stepEntries/4",
          "createTime": "2024-08-15T19:42:51.416071869Z",
          "updateTime": "2024-08-15T19:42:51.416106840Z",
          "routine": "main",
          "step": "tryStep",
          "stepType": "STEP_EXCEPT",
          "state": "STATE_SUCCEEDED",
          "entryId": "4",
          "navigationInfo": {
            "children": [
              "5"
            ],
            "parent": "1",
            "next": "5",
            "previous": "3"
          },
          "variableData": {}
        },
        {
          "name": "projects/1051295516635/locations/us-central1/workflows/workflow-failed-step/executions/a19d20d1-e446-4d37-b548-8005297b7d3d/stepEntries/5",
          "createTime": "2024-08-15T19:42:51.416087217Z",
          "updateTime": "2024-08-15T19:42:51.416106742Z",
          "routine": "main",
          "step": "tryStep.except",
          "stepType": "STEP_RETURN",
          "state": "STATE_SUCCEEDED",
          "entryId": "5",
          "navigationInfo": {
            "parent": "4",
            "previous": "4"
          },
          "variableData": {}
        }
      ],
      "totalSize": 5
    }

## What's next

  * [Debugging overview](https://docs.cloud.google.com/workflows/docs/debug)
  * [Monitor workflows](https://docs.cloud.google.com/workflows/docs/monitor)
  * [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting)
  * [Known issues for Workflows](https://docs.cloud.google.com/workflows/docs/issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
