---
url: https://docs.cloud.google.com/workflows/docs/executing-workflow/
title: Execute a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:03.236407+00:00
---

# Execute a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/executing-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Execute a workflow Stay organized with collections  Save and categorize content based on your preferences. 

Workflow executions let you orchestrate and automate multi-step tasks across Google Cloud services and external APIs. Starting an execution runs the current workflow definition associated with the workflow. You can pass runtime arguments in an execution request and access those arguments using workflow variables. For more information, see [Pass runtime arguments in an execution request](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments).

After a workflow execution completes, its history and results are retained for a limited time. For more information, see [Quotas and limits](https://docs.cloud.google.com/workflows/quotas).

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. If a workflow accesses other Google Cloud resources, make sure it is associated with a service account that has the correct permissions to do so. To learn what service account is associated with an existing workflow, see [Verify a workflow's associated service account](https://docs.cloud.google.com/workflows/docs/authentication#verify-service-account). 

Note that to create a resource and attach a service account, you need permissions to create that resource and to impersonate the service account that you will attach to the resource. For more information, see [Service account permissions](https://docs.cloud.google.com/workflows/docs/authentication#sa-permissions).

  7. Deploy a workflow using the [Google Cloud console](https://docs.cloud.google.com/workflows/docs/create-workflow-console) or the [Google Cloud CLI](https://docs.cloud.google.com/workflows/docs/create-workflow-gcloud).

**Note:** To send logs to Cloud Logging, make sure the service account executing the workflow has been granted a role that includes the `logging.logEntries.create` permission (for example, the `Logs Writer` role). 

## Execute a workflow

You can execute a workflow in the following ways:

  * In the Google Cloud console
  * By using the Google Cloud CLI in either your terminal or Cloud Shell
  * By sending a direct request to the Workflows API



You can also execute a workflow by using the Cloud Client Libraries. For more information, see [Execute a workflow using the Cloud Client Libraries](https://docs.cloud.google.com/workflows/docs/execute-workflow-client-libraries).

### Console

  1. To execute a workflow, in the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, select a workflow to go to its details page.

  3. On the **Workflow details** page, click _play_arrow_ **Execute**.

  4. On the **Execute workflow** page, in the **Input** pane, you can enter optional [runtime arguments](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments) to pass to your workflow before execution. Arguments must be in JSON format; for example, `{"animal":"cat"}`. If your workflow doesn't use runtime arguments, leave this blank.

  5. Optionally, specify the level of [call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) that you want to apply to the execution of the workflow. In the **Call log level** list, select one of:

     * **Not specified** : no logging level is specified. This is the default. An execution log level takes precedence over any workflow log level, unless the execution log level is not specified (the default); in that case, the workflow log level applies. 
     * **Errors only** : log all caught exceptions; or when a call is stopped due to an exception. 
     * **All calls** : log all calls to subworkflows or library functions and their results. 
     * **No logs** : no call logging. 
  6. Optionally, specify the level of [execution history](https://docs.cloud.google.com/workflows/docs/debug-steps) that you want to apply to the execution of the workflow. In the **Execution history** list, select one of:

     * **Inherit from workflow** : apply the execution history setting of the workflow. This is the default. 
     * **Basic** : enable basic execution history. 
     * **Detailed** : enable detailed execution history including any in-scope variable values and the expected number of iterations. 
  7. Click **Execute**.

  8. On the **Execution details** page, you can view the results of the execution including any output, the execution ID and state, and the current or final step of the workflow execution. For more information, see [Access workflow execution results](https://docs.cloud.google.com/workflows/docs/access-execution-results).

**Note:** To access the **Execution details** page, you must have a role that contains the `workflows.workflows.get`, `workflows.executions.get`, and `workflows.stepEntries.list` permissions. For more information, see [Workflows roles and permissions](https://docs.cloud.google.com/workflows/docs/access-control) and [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 



###  gcloud 

  1. Open a terminal.

  2. Find the name of the workflow you want to execute. If you don't know the workflow's name, you can enter the following command to list all your workflows:
         
         gcloud workflows list

  3. You can execute the workflow using either the [`gcloud workflows run`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/run) command or the [`gcloud workflows execute`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/execute) command:

     * Execute the workflow and wait for the execution to complete:
           
           gcloud workflows run WORKFLOW_NAME \
               --call-log-level=CALL_LOGGING_LEVEL \
               --execution-history-level="EXECUTION_HISTORY_LEVEL" \
               --data=DATA

     * Execute the workflow without waiting for the execution attempt to finish:
           
           gcloud workflows execute WORKFLOW_NAME \
               --call-log-level=CALL_LOGGING_LEVEL \
               --execution-history-level="EXECUTION_HISTORY_LEVEL" \
               --data=DATA

Replace the following:

       * `WORKFLOW_NAME`: the name of the workflow.
       * `CALL_LOGGING_LEVEL` (optional): level of [call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) to apply during execution. Can be one of:

         * `none`: no logging level is specified. This is the default. An execution log level takes precedence over any workflow log level, unless the execution log level is not specified (the default); in that case, the workflow log level applies. 
         * `log-errors-only`: log all caught exceptions; or when a call is stopped due to an exception. 
         * `log-all-calls`: log all calls to subworkflows or library functions and their results. 
         * `log-none`: no call logging. 
       * `EXECUTION_HISTORY_LEVEL` (optional): level of [execution history](https://docs.cloud.google.com/workflows/docs/debug-steps) to apply during execution. Can be one of:

         * `none`: no execution history level is specified. This is the default. If an execution history level is not specified for an execution, it is determined by the level applied to the workflow. If the levels are different, the setting applied at the execution level overrides the setting applied at the workflow level for this execution. 
         * `execution-history-basic`: enable basic execution history. 
         * `execution-history-detailed`: enable detailed execution history including any in-scope variable values and the expected number of iterations. 
       * `DATA` (optional): runtime arguments for your workflow in JSON format.

  4. If you ran `gcloud workflows execute`, the unique ID of the workflow execution attempt is returned and the output is similar to the following:
         
         To view the workflow status, you can use following command:
          gcloud workflows executions describe b113b589-8eff-4968-b830-8d35696f0b33 --workflow workflow-2 --location us-central1

To view the status of the execution, enter the command returned by the previous step.




If the execution attempt is successful, the output is similar to the following, with a `state` indicating the workflow's success, and a `status` that specifies the final workflow step of the execution. 
    
    
    argument: '{"searchTerm":"Friday"}'
    endTime: '2022-06-22T12:17:53.086073678Z'
    name: projects/1051295516635/locations/us-central1/workflows/myFirstWorkflow/executions/c4dffd1f-13db-46a0-8a4a-ee39c144cb96
    result: '["Friday","Friday the 13th (franchise)","Friday Night Lights (TV series)","Friday
        the 13th (1980 film)","Friday the 13th","Friday the 13th (2009 film)","Friday the
        13th Part III","Friday the 13th Part 2","Friday (Rebecca Black song)","Friday Night
        Lights (film)"]'
    startTime: '2022-06-22T12:17:52.799387653Z'
    state: SUCCEEDED
    status:
        currentSteps:
        - routine: main
            step: returnOutput
    workflowRevisionId: 000001-ac2

### REST API

To create a new execution using the latest revision of a given workflow, use the [`projects.locations.workflows.executions.create`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/create) method.

**Note:** To authenticate, you will need a service account with sufficient privileges to execute the workflow. For example, you can grant a service account the [Workflows Invoker role](https://docs.cloud.google.com/workflows/docs/access-control#roles) (`roles/workflows.invoker`) so that the account has permission to trigger your workflow execution. For more information, see [Invoke Workflows](https://docs.cloud.google.com/workflows/docs/use-iam-for-access#invoke-workflows).

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number listed in the [IAM & Admin Settings](https://console.cloud.google.com/iam-admin/settings/project) page.
  * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) in which the workflow is deployed—for example, `us-central1`.
  * `WORKFLOW_NAME`: the user-defined name for the workflow—for example, `myFirstWorkflow`.
  * `PARAMETER`: optional. If the workflow you are executing can receive runtime arguments that you pass it as part of an execution request, you can add to the request body a JSON-formatted string whose value is one or more escaped parameter-value pairs—for example, `"{\"searchTerm\":\"asia\"}"`.
  * `VALUE`: optional. The value of a parameter-value pair that your workflow can receive as a runtime argument.
  * `CALL_LOGGING_LEVEL`: optional. The call logging level to apply during execution. The default is that no logging level is specified and the workflow log level applies instead. For more information, see [Send Logs to Logging](https://docs.cloud.google.com/workflows/docs/log-workflow). One of the following: 
    * `CALL_LOG_LEVEL_UNSPECIFIED`: no logging level is specified and the workflow log level applies instead. This is the default. Otherwise, the execution log level applies and takes precedence over the workflow log level.
    * `LOG_ERRORS_ONLY`: log all caught exceptions; or when a call is stopped due to an exception.
    * `LOG_ALL_CALLS`: log all calls to subworkflows or library functions and their results.
    * `LOG_NONE`: no call logging.
  * `BACKLOG_EXECUTION`: optional. If set to `true`, the execution is not backlogged when the concurrency quota is exhausted. For more information, see Manage execution backlogging. 
  * `EXECUTION_HISTORY_LEVEL`: optional. The execution history level to apply during execution. For more information, see [View history of execution steps](https://docs.cloud.google.com/workflows/docs/debug-steps). One of the following: 
    * `EXECUTION_HISTORY_LEVEL_UNSPECIFIED`: no execution history level is specified. This is the default. If an execution history level is not specified for an execution, it is determined by the level applied to the workflow. If the levels are different, the setting applied at the execution level overrides the setting applied at the workflow level for this execution.
    * `EXECUTION_HISTORY_BASIC`: enable basic execution history.
    * `EXECUTION_HISTORY_ADVANCED`: enable detailed execution history including any in-scope variable values and the expected number of iterations.



Request JSON body: 
    
    
    {
      "argument": "{\"PARAMETER\":\"VALUE\"}",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "disableConcurrencyQuotaOverflowBuffering": "BACKLOG_EXECUTION",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "argument": "{\"PARAMETER\":\"VALUE\"}",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "disableConcurrencyQuotaOverflowBuffering": "BACKLOG_EXECUTION",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_NAME/executions"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "argument": "{\"PARAMETER\":\"VALUE\"}",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "disableConcurrencyQuotaOverflowBuffering": "BACKLOG_EXECUTION",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://workflowexecutions.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_NAME/executions" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains a newly created instance of `Execution`: 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/workflows/WORKFLOW_NAME/executions/EXECUTION_ID",
      "startTime": "2023-11-07T14:35:27.215337069Z",
      "state": "ACTIVE",
      "argument": "{\"PARAMETER\":\"VALUE\"}",
      "workflowRevisionId": "000001-2df",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL",
      "status": {}
    }
    

## Check the status of executions

There are several commands to help you check the status of a workflow execution.

  * To retrieve a list of a workflow's execution attempts and their IDs, enter the following command:
        
        gcloud workflows executions list WORKFLOW_NAME

Replace `WORKFLOW_NAME` with the name of the workflow.

The command returns a `NAME` value that is similar to the following:

`projects/PROJECT_NUMBER/locations/REGION/workflows/WORKFLOW_NAME/executions/EXECUTION_ID`

Copy the execution ID to use in the next command.

  * To check the status of an execution attempt and wait for the attempt to finish, enter the following command:
        
        gcloud workflows executions wait EXECUTION_ID

Replace `EXECUTION_ID` with the execution attempt's ID.

The command waits for the execution attempt to finish and then returns the results.

  * To wait until the last execution is complete and then return the result of the completed execution, enter the following command:
        
        gcloud workflows executions wait-last

If you made a previous execution attempt in the same `gcloud` session, the command waits for the prior execution attempt to finish and then returns the results of the completed execution. If no previous attempt exists, `gcloud` returns the following error:
        
        ERROR: (gcloud.workflows.executions.wait-last) [NOT FOUND] There are no cached executions available.
        

  * To get the status of the last execution, enter the following command:
        
        gcloud workflows executions describe-last

If you made a previous execution attempt in the same `gcloud` session, the command returns the results of the last execution even if it is running. If no previous attempt exists, `gcloud` returns the following error:
        
        ERROR: (gcloud.beta.workflows.executions.describe-last) [NOT FOUND] There are no cached executions available.
        




## Filter executions

You can apply filters to the list of workflow executions returned by the [`workflows.executions.list` method](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/list).

You can filter on the following fields:

  * `createTime`
  * `disableOverflowBuffering`
  * `duration`
  * `endTime`
  * `executionId`
  * `label`
  * `startTime`
  * `state`
  * `stepName`
  * `workflowRevisionId`



For example, to filter on a label (`labels."fruit":"apple"`), you can make an API request similar to the following:
    
    
    GET https://workflowexecutions.googleapis.com/v1/projects/MY_PROJECT/locations/MY_LOCATION/workflows/MY_WORKFLOW/executions?**view =full&filter=labels.%22fruit%22%3A%22apple%22**"
    

Where:

  * `view=full` specifies a view defining which fields should be filled in the returned executions; in this case, all the data
  * `labels.%22fruit%22%3A%22apple%22`is the URL-encoded filter syntax



For more information, see [AIP-160 Filtering](https://google.aip.dev/160).

## Manage execution backlogging

You can use execution backlogging to avoid client-side retries, remove execution delays, and maximize throughput. Backlogged executions automatically run as soon as execution concurrency quota becomes available.

**Best practice:** If running your workflow executions is time-constrained or sensitive, execution backlogging is **not** recommended, and you should consider disabling the feature. 

There is a [maximum number](https://docs.cloud.google.com/workflows/quotas#quotas) of active workflow executions that can run concurrently. Once this quota is exhausted, and if execution backlogging is disabled, or if the quota for backlogged executions is reached, any new executions fail with an HTTP `429 Too many requests` status code. With execution backlogging enabled, the new executions succeed and are created in a `QUEUED` state. As soon as execution concurrency quota becomes available, the executions automatically run and enter an `ACTIVE` state.

By default, execution backlogging is enabled for all requests (including those triggered by Cloud Tasks) with the following exceptions:

  * When creating an execution using an [`executions.run`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/v1/projects.locations.workflows.executions/run) or [`executions.create`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/v1/projects.locations.workflows.executions/create) connector in a workflow, execution backlogging is disabled by default. You can configure it by explicitly setting the execution's `disableConcurrencyQuotaOverflowBuffering` field to `false`.
  * For executions triggered by Pub/Sub, execution backlogging is disabled and _can't_ be configured.



Note the following:

  * Queued executions are started in a first-in-first-out (FIFO) order, on a best-effort basis.
  * A `createTime` timestamp field indicates when an execution is created. The `startTime` timestamp indicates when an execution is automatically popped from the backlog queue and starts running. For executions that are not backlogged, both timestamp values are identical.
  * The limit for backlogged executions can be observed using the `workflowexecutions.googleapis.com/executionbacklogentries` quota metric. For more information, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).



### Disable execution backlogging

You can disable execution backlogging by setting a flag when using the the Google Cloud CLI. For example:
    
    
    gcloud workflows execute WORKFLOW_NAME
        --disable-concurrency-quota-overflow-buffering

Or, you can disable execution backlogging by setting the `disableConcurrencyQuotaOverflowBuffering` field to `true` in the request JSON body when sending an execution request to the Workflows REST API. For example:
    
    
    {
      "argument": {"arg1":"value1"},
      "callLogLevel": "LOG_NONE",
      "disableConcurrencyQuotaOverflowBuffering": true
    }

For more information, see Execute a workflow.

## What's next

  * [Access workflow execution results](https://docs.cloud.google.com/workflows/docs/access-execution-results)
  * [Control the order of execution in a workflow](https://docs.cloud.google.com/workflows/docs/controlling-execution-order)
  * [Send execution logs to Cloud Logging](https://docs.cloud.google.com/workflows/docs/log-workflow)
  * [Update an existing workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#update_a_workflow)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
