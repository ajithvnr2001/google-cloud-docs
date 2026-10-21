---
url: https://docs.cloud.google.com/workflows/docs/creating-updating-workflow/
title: Create and manage workflows \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:14.102576+00:00
---

# Create and manage workflows  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/creating-updating-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Create and manage workflows Stay organized with collections  Save and categorize content based on your preferences. 

Workflows lets you orchestrate and automate multi-step processes across Google Cloud services and external APIs. You can deploy, update, and administer workflow definitions by using the Google Cloud console, the Google Cloud CLI in your local terminal or Cloud Shell, or the Workflows API.

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

### Console

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Workflows API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Workflows API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com)




### gcloud

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Workflows API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable workflows.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Workflows API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable workflows.googleapis.com




### REST

To manage workflows using the Workflows API, we recommend that you use the Google-provided [client libraries](https://docs.cloud.google.com/workflows/docs/reference/libraries) to call the `workflows.googleapis.com` service. For more information, see [Workflows API](https://docs.cloud.google.com/workflows/docs/reference/rest).

## Create a service account

A service account represents the identity of a workflow and determines what permissions the workflow has and which Google Cloud resources it can access. Create a service account if you don't already have one; then grant it the roles necessary for [managing workflows](https://docs.cloud.google.com/workflows/docs/access-control#workflows.editor) and [creating logs](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter).

If you don't specify a service account during the workflow's creation, the workflow uses the default Compute Engine service account for its identity. For more information, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).

We strongly recommend using a service account with the least privileges necessary to access the required resources.

Note that to create a resource and attach a service account, you need permissions to create that resource and to impersonate the service account that you will attach to the resource. For more information, see [Service account permissions](https://docs.cloud.google.com/workflows/docs/authentication#sa-permissions).

### Console

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project and then click **Create service account**.

  3. In the **Service account name** field, enter a name.

The name must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes. After you create a service account, you can't change its name.

  4. Click **Create and continue**.

  5. Click **Select a role**.

  6. Select the following roles, clicking **Add another role** as required:

     1. To create, update, and execute workflows, select **Workflows > Workflows Editor**.
     2. To send logs to Cloud Logging, select **Logging > Logs Writer**.
**Important:** For production environments, Google strongly recommends creating a new service account and granting it one or more IAM roles that contain the minimum permissions required for managing workflows. To learn more about which permissions and roles are available in Workflows, see [Access control](https://docs.cloud.google.com/workflows/docs/access-control).
  7. Click **Done** to finish creating the service account.




### gcloud

  1. Create the service account.
         
         gcloud iam service-accounts create SERVICE_ACCOUNT

  2. Grant permissions to the service account by assigning roles.

     1. To create, update, and execute workflows, assign the `roles/workflows.editor` role:
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member "serviceAccount:SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com" \
                --role "roles/workflows.editor"

     2. To send logs to Cloud Logging, assign the `roles/logging.logWriter` role:
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member "serviceAccount:SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com" \
                --role "roles/logging.logWriter"

Replace the following:

     * `SERVICE_ACCOUNT`: the name of the service account. It must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes. After you create a service account, you can't change its name.

     * `PROJECT_ID`: your project's ID.

**Important:** For production environments, Google strongly recommends creating a new service account and granting it one or more IAM roles that contain the minimum permissions required for managing workflows. To learn more about which permissions and roles are available in Workflows, see [Access control](https://docs.cloud.google.com/workflows/docs/access-control).



### REST

You can use the [`serviceAccounts.create`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/create) method to create a service account. For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

You can programmatically grant multiple roles by modifying and setting the allow policy for a resource using the [`setIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy) method. For more information, see [Grant or revoke multiple roles programmatically](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#multiple-roles-programmatic).

## Create a workflow

A workflow definition is made up of a series of steps described using the [Workflows syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax), which can be written in either YAML or JSON format. After defining a workflow, you deploy it to make it available for execution. The deploy step also validates that the source file can be executed. It fails if the source file doesn't contain a valid workflow definition.

Editing YAML files can be error-prone. You can create your workflow by using a preferred IDE or source code editor and [setting up autocompletion and syntax validation](https://docs.cloud.google.com/workflows/docs/use-workflows-json-schema-with-ide) to reduce errors.

**Note:** YAML indentation is meaningful and should be at least two spaces per indentation level. Insufficient indentation can cause errors, and a new level should be at least two spaces in from the _start of the text_ in the previous line. For more details, see [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting#indentation). 

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter a name for the workflow, such as `myFirstWorkflow`. The name can contain letters, numbers, underscores, and hyphens. It must start with a letter and end with a number or letter.

  4. Optionally, add a description of the workflow.

  5. In the **Region** list, select an appropriate [location](https://docs.cloud.google.com/workflows/docs/locations) to deploy your workflow in; for example, **us-central1**.

  6. In the **Service account** list, select a service account that your workflow will use to access other Google Cloud services. For more information, in this document, see Create a service account. 

  7. Optionally, do any of the following:

     1. Specify the level of [call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) that you want to apply to the workflow definition. In the **Call log level** list, select one of:

        * **Not specified** : no logging level is specified. This is the default. An execution log level takes precedence over any workflow log level, unless the execution log level is not specified (the default); in that case, the workflow log level applies. 
        * **Errors only** : log all caught exceptions; or when a call is stopped due to an exception. 
        * **All calls** : log all calls to subworkflows or library functions and their results. 
        * **No logs** : no call logging. 
     2. Specify the level of [execution history](https://docs.cloud.google.com/workflows/docs/debug-steps) that you want to apply to the workflow definition. In the **Execution history** list, select one of:

        * **Basic** : enable basic execution history. This is the default. 
        * **Detailed** : enable detailed execution history including any in-scope variable values and the expected number of iterations. 
     3. Specify a Cloud Key Management Service key that the workflow should use for data encryption: select **Customer-managed encryption key (CMEK)**. For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/workflows/docs/use-cmek).

     4. Specify an environment variable that is accessible by your workflow at runtime. For more information, see [Use environment variables](https://docs.cloud.google.com/workflows/docs/use-environment-variables).

     5. Add a label: labels are key-value pairs that help you organize your Google Cloud instances. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels) Workflow labels are inherited by executions of the workflow. To view execution labels, use the `workflows.executions.list` method to [list and filter workflow executions](https://docs.cloud.google.com/workflows/docs/executing-workflow#filter_executions).

**Note:** It can take up to 10 minutes for the new label to take effect.
     6. Schedule your workflow: select **Add new trigger > Cloud Scheduler**. For more information, see [Schedule a workflow using Cloud Scheduler](https://docs.cloud.google.com/workflows/docs/schedule-workflow).

     7. Trigger your workflow through an event or Pub/Sub message: select **Add new trigger > Eventarc**. For more information, see [Trigger a workflow with events or Pub/Sub messages](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc).

  8. Click **Next**.

  9. In the workflow editor, enter the definition for your workflow. See an [example workflow](https://docs.cloud.google.com/workflows/docs/create-workflow-console#workflow-example).

  10. Click **Deploy**.




### gcloud

  1. Make sure that your workflow's source code is saved in a YAML or JSON file, such as `MY_WORKFLOW.YAML` or `MY_WORKFLOW.JSON`. See an [example workflow](https://docs.cloud.google.com/workflows/docs/create-workflow-gcloud#create_deploy_and_execute_a_workflow).

  2. Open a terminal.

  3. You can create and deploy a workflow using the [`gcloud workflows deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/deploy) command:
         
         gcloud workflows deploy WORKFLOW_NAME \
             --location=LOCATION \
             --call-log-level=CALL_LOGGING_LEVEL \
             --description="DESCRIPTION" \
             --execution-history-level="EXECUTION_HISTORY_LEVEL" \
             --labels="LABEL_KEY=LABEL_VALUE" \
             --set-env-vars="ENV_KEY=ENV_VALUE" \
             --kms-key=ENCRYPT_KEY \
             --service-account=SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com \
             --source=YAML_OR_JSON_SOURCE_FILE

Replace the following:

     * `WORKFLOW_NAME`: the name of your workflow—for example, `myFirstWorkflow`. The name can contain letters, numbers, underscores, and hyphens. It must start with a letter and end with a number or letter.

     * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) to deploy your workflow in; for example, `us-central1`.

     * `CALL_LOGGING_LEVEL`: optional. Level of [call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) to apply during execution. Can be one of:

       * `none`: no logging level is specified. This is the default. An execution log level takes precedence over any workflow log level, unless the execution log level is not specified (the default); in that case, the workflow log level applies. 
       * `log-errors-only`: log all caught exceptions; or when a call is stopped due to an exception. 
       * `log-all-calls`: log all calls to subworkflows or library functions and their results. 
       * `log-none`: no call logging. 
     * `DESCRIPTION`: optional. A description of the workflow.

     * `EXECUTION_HISTORY_LEVEL`: optional. Level of [execution history](https://docs.cloud.google.com/workflows/docs/debug-steps) to apply during execution. Can be one of:

       * `none`: no execution history level is specified. This is the default. If an execution history level is not specified for an execution, it is determined by the level applied to the workflow. If the levels are different, the setting applied at the execution level overrides the setting applied at the workflow level for this execution. 
       * `execution-history-basic`: enable basic execution history. 
       * `execution-history-detailed`: enable detailed execution history including any in-scope variable values and the expected number of iterations. 
     * `LABEL_KEY=LABEL_VALUE`: optional. List of label key-value pairs that helps you organize your Google Cloud instances; for example, `name=wrench`. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels) Workflow labels are inherited by executions of the workflow. To view execution labels, use the `workflows.executions.list` method to [list and filter workflow executions](https://docs.cloud.google.com/workflows/docs/executing-workflow#filter_executions).

**Note:** It can take up to 10 minutes for the new label to take effect.
     * `ENV_KEY=ENV_VALUE`: optional. List of environment variable key-value pairs; for example, `MONTH=January`. For more information, see [Use environment variables](https://docs.cloud.google.com/workflows/docs/use-environment-variables).

     * `ENCRYPT_KEY`: optional. A Cloud KMS key that the workflow should use for data encryption in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`. For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/workflows/docs/use-cmek).

     * `SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com`: optional. The service account your workflow will use to access other Google Cloud services. For more information, in this document, see Create a service account. 

     * `YAML_OR_JSON_SOURCE_FILE`: the source file for the workflow definition. For example: `myFirstWorkflow.yaml`.




### REST

To create a new workflow with a specified name, use the [`projects.locations.workflows.create`](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/create) method, and use the `workflowId` query parameter to specify an ID for the workflow.

Before using any of the request data, make the following replacements: 

  * `WORKFLOW_NAME`: the name of your workflow—for example, `myFirstWorkflow`. The name can contain letters, numbers, underscores, and hyphens. It must start with a letter and end with a number or letter.
  * `DESCRIPTION`: optional. A description of your workflow. Must be no longer than 1000 Unicode characters.
  * `LABEL_KEY` and `LABEL_VALUE`: optional. A map of label key and value pairs that help you organize your Google Cloud instances. For example: `{"name": "wrench", "mass": "1kg", "count": "3"}` For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels) Workflow labels are inherited by executions of the workflow. To view execution labels, use the `workflows.executions.list` method to [list and filter workflow executions](https://docs.cloud.google.com/workflows/docs/executing-workflow#filter_executions). **Note:** It can take up to 10 minutes for the new label to take effect. 
  * `SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com`: optional. The service account your workflow will use to access other Google Cloud services. The project ID is your Google Cloud project ID. For more information, in this document, see Create a service account.
  * `ENCRYPT_KEY`: optional. A Cloud KMS key that the workflow should use for data encryption in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`. For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/workflows/docs/use-cmek).
  * `CALL_LOGGING_LEVEL`: optional. The call logging level to apply during execution. The default is that no logging level is specified and the workflow log level applies instead. For more information, see [Send Logs to Logging](https://docs.cloud.google.com/workflows/docs/log-workflow). One of the following: 
    * `CALL_LOG_LEVEL_UNSPECIFIED`: no logging level is specified and the workflow log level applies instead. This is the default. Otherwise, the execution log level applies and takes precedence over the workflow log level.
    * `LOG_ERRORS_ONLY`: log all caught exceptions; or when a call is stopped due to an exception.
    * `LOG_ALL_CALLS`: log all calls to subworkflows or library functions and their results.
    * `LOG_NONE`: no call logging.
  * `EXECUTION_HISTORY_LEVEL`: optional. The execution history level to apply during execution. For more information, see [View history of execution steps](https://docs.cloud.google.com/workflows/docs/debug-steps). One of the following: 
    * `EXECUTION_HISTORY_LEVEL_UNSPECIFIED`: no execution history level is specified. This is the default. If an execution history level is not specified for an execution, it is determined by the level applied to the workflow. If the levels are different, the setting applied at the execution level overrides the setting applied at the workflow level for this execution.
    * `EXECUTION_HISTORY_BASIC`: enable basic execution history.
    * `EXECUTION_HISTORY_ADVANCED`: enable detailed execution history including any in-scope variable values and the expected number of iterations.
  * `ENV_KEY` and `ENV_VALUE`: optional. A map of environment variable key and value pairs; for example, `{ "month": "January", "day": "Monday"}`. For more information, see [Use environment variables](https://docs.cloud.google.com/workflows/docs/use-environment-variables).
  * `SOURCE_CODE`: the workflow definition. You must escape new lines in YAML. For example: `main:\n params:\n - input\n steps:\n - returnOutput:\n return: Hello`

You must escape quotation marks in JSON. For example: `{\"main\":{\"params\":[\"input\"],\"steps\":[{\"returnOutput\":{\"return\":\"Hello\"}}]}}`

  * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) in which the workflow is to be deployed—for example, `us-central1`.



Request JSON body: 
    
    
    {
      "name": "WORKFLOW_NAME",
      "description": "DESCRIPTION",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "cryptoKeyName": "ENCRYPT_KEY",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
      "userEnvVars": {"ENV_KEY":"ENV_VALUE"},
      "sourceContents": "SOURCE_CODE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "name": "WORKFLOW_NAME",
      "description": "DESCRIPTION",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "cryptoKeyName": "ENCRYPT_KEY",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
      "userEnvVars": {"ENV_KEY":"ENV_VALUE"},
      "sourceContents": "SOURCE_CODE"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://workflows.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/workflows?workflowId=WORKFLOW_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "name": "WORKFLOW_NAME",
      "description": "DESCRIPTION",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "cryptoKeyName": "ENCRYPT_KEY",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
      "userEnvVars": {"ENV_KEY":"ENV_VALUE"},
      "sourceContents": "SOURCE_CODE"
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
        -Uri "https://workflows.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/workflows?workflowId=WORKFLOW_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/workflows/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.workflows.v1.OperationMetadata",
        "createTime": "2023-12-05T14:06:06.338390918Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME",
        "verb": "create",
        "apiVersion": "v1"
      },
      "done": false
    }
    

If the value of `"done"` is `false`, the operation is still in progress.

## List workflows

You can list workflows or use filters to retrieve a specific workflow.

###  Console 

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

This page lists your workflows in all locations, and includes details such as names, regions, latest revisions, and more.

  2. To filter your workflows:

     1. Click filter_list **Filter** or the **Filter workflows** field.
     2. In the **Properties** list, select an option to filter the workflows by.

You can select a single property or use the logical operator `OR` to add more properties.

  3. To sort your workflows, beside any supported column heading, click arrow_upward **Sort**.




###  gcloud 

List workflows using the [`gcloud workflows list`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/list) command:
    
    
    gcloud workflows list --location=LOCATION

Replace `LOCATION` with the ID or fully qualified identifier for the location of your workflow.

This command lists your workflows in the specified location, and includes details such as a workflow's `NAME`, `STATE`, `REVISION_ID`, and `UPDATE_TIME`.

###  REST 

To list workflows in a given project and location, use the [`projects.locations.workflows.list`](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/list) method.

Alternatively, to retrieve the details of a single workflow, use the [`projects.locations.workflows.get`](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/get) method.

**Note:** When listing workflows, paging might be applied before or after filtering. The service might return fewer resources than the number requested through the `pageSize` parameter, even if not at the end of the collection.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) in which the workflows are deployed—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://workflows.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/workflows"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://workflows.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/workflows" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body contains instances of [`Workflow`](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows#resource:-workflow) and the response should be similar to the following: 
    
    
    {
      "workflows": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME",
          "state": "ACTIVE",
          "revisionId": "000001-0ce",
          "createTime": "2023-12-08T13:56:59.306770745Z",
          "updateTime": "2023-12-08T13:56:59.547021939Z",
          "revisionCreateTime": "2023-12-08T13:56:59.340161044Z",
          "serviceAccount": "projects/PROJECT_ID/serviceAccounts/PROJECT_NUMBER-compute@developer.gserviceaccount.com",
          "sourceContents": "main:\n    params: [input]\n [...] return: '${wikiResult.body[1]}'\n"
        },
        {
          object (Workflow)
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }
    

## Update a workflow

You can update an existing workflow. You must specify the name of the workflow you want to update and its source. Note that you can't change a workflow's name or location.

Updating a workflow does not affect in-progress executions. Only future executions of the workflow will use the updated configuration.

Each time you update a workflow, its `versionID` is updated. The `versionID` consists of two parts, separated by a hyphen:

  * A number, starting at one, that increments each time you update a workflow.

  * A random, three-character, alphanumeric string.




For example, `000001-27f` indicates the initial version of a workflow and `000002-d52` indicates a workflow that has been updated once.

**Note:** If you remove a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/workflows/docs/use-cmek) from the current workflow revision, any subsequent executions are created without CMEK encryption. However, existing workflow revisions and executions remain encrypted with the keys with which they were previously encrypted.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow you want to update. Note that you can't change the workflow's name.

The **Workflow details** page appears.

  3. You can edit the workflow in the following ways:

     * To edit the source:

       1. Click the **Source** tab.
       2. Click **Edit**.
       3. To save your changes, click **Save**. The updated workflow is deployed.
     * To update the description, the service account the workflow uses for authentication, the call log level, environment variables, labels, or the encryption key:

       1. Click the **Details** tab.
       2. Click the appropriate edit icon.
       3. If you are updating the call log level, select one of: 
          * **Not specified** : no logging level is specified. This is the default. An execution log level takes precedence over any workflow log level, unless the execution log level is not specified (the default); in that case, the workflow log level applies. 
          * **Errors only** : log all caught exceptions; or when a call is stopped due to an exception. 
          * **All calls** : log all calls to subworkflows or library functions and their results. 
          * **No logs** : no call logging. 
       4. If you are updating the execution history level, select one of: 
          * **Basic** : enable basic execution history. This is the default. 
          * **Detailed** : enable detailed execution history including any in-scope variable values and the expected number of iterations. 
       5. If you update an existing label, or add a new one, it can take up to 10 minutes for the new label to take effect. Workflow labels are inherited by executions of the workflow. To view execution labels, use the `workflows.executions.list` method to [list and filter workflow executions](https://docs.cloud.google.com/workflows/docs/executing-workflow#filter_executions).
       6. To save your changes, click **Save**. The updated workflow is deployed.
     * To edit the previous fields at the same time, or add or update a trigger:

       1. Click edit **Edit**.
       2. To edit the source, click **Next**.
       3. To save your changes and deploy the updated workflow, click **Deploy**.
  4. If you want to update the roles for your service account, click the **Permissions** tab.

     1. Principals are users, groups, domains, or service accounts. To update an existing principal:

        1. Find a row containing the principal.
        2. Click edit **Edit principal** in that row.
        3. Click add **Add another role** or click delete **Delete role**.
     2. If you are adding a role, in the **Select a role** list, select an appropriate role.

     3. To add another role, click **Add another role**.

     4. Click **Save**.

**Note:** To change the service account the workflow uses for authentication, you must still edit the workflow and modify the service account as detailed in the previous step. For more information, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).



### gcloud

  1. Open a terminal.

  2. Find the name of the workflow you want to update. If you don't know the workflow's name, you can enter the following command to list all your workflows:
         
         gcloud workflows list

  3. Locate the YAML or JSON file where your workflow source is saved, such as `WORKFLOW_NAME.YAML` or `WORKFLOW_NAME.JSON`.

  4. You can update an existing workflow to change its source, description, labels, environment variables, the call log level, encryption key, or its associated service account using the [`gcloud workflows deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/deploy) command.

You must specify the name of the workflow you want to update and its source; however, the rest of the flags are optional. To [remove a customer-managed encryption key](https://docs.cloud.google.com/workflows/docs/use-cmek#disable-cmek), use the `--clear-kms-key` flag.
         
         gcloud workflows deploy WORKFLOW_NAME \
             --call-log-level=CALL_LOGGING_LEVEL \
             --description="DESCRIPTION" \
             --execution-history-level="EXECUTION_HISTORY_LEVEL" \
             --labels="LABEL_KEY=LABEL_VALUE" \
             --set-env-vars="ENV_KEY=ENV_VALUE" \
             --kms-key=ENCRYPT_KEY \
             --service-account=SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com \
             --source=YAML_OR_JSON_SOURCE_FILE

Replace the following:

     * `WORKFLOW_NAME`: required. The name of your workflow.

     * `CALL_LOGGING_LEVEL`: optional. Level of [call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) to apply during execution. Can be one of:

       * `none`: no logging level is specified. This is the default. An execution log level takes precedence over any workflow log level, unless the execution log level is not specified (the default); in that case, the workflow log level applies. 
       * `log-errors-only`: log all caught exceptions; or when a call is stopped due to an exception. 
       * `log-all-calls`: log all calls to subworkflows or library functions and their results. 
       * `log-none`: no call logging. 
     * `DESCRIPTION`: optional. A description of the workflow.

     * `EXECUTION_HISTORY_LEVEL`: optional. Level of [execution history](https://docs.cloud.google.com/workflows/docs/debug-steps) to apply during execution. Can be one of:

       * `none`: no execution history level is specified. This is the default. If an execution history level is not specified for an execution, it is determined by the level applied to the workflow. If the levels are different, the setting applied at the execution level overrides the setting applied at the workflow level for this execution. 
       * `execution-history-basic`: enable basic execution history. 
       * `execution-history-detailed`: enable detailed execution history including any in-scope variable values and the expected number of iterations. 
     * `LABEL_KEY=LABEL_VALUE`: optional. List of label key-value pairs that helps you organize your Google Cloud instances; for example, `name=wrench`. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels) Workflow labels are inherited by executions of the workflow. To view execution labels, use the `workflows.executions.list` method to [list and filter workflow executions](https://docs.cloud.google.com/workflows/docs/executing-workflow#filter_executions).

**Note:** If you update an existing label, or add a new one, it can take up to 10 minutes for the new label to take effect.
     * `ENV_KEY=ENV_VALUE`: optional. List of environment variable key-value pairs; for example, `MONTH=January`. For more information, see [Use environment variables](https://docs.cloud.google.com/workflows/docs/use-environment-variables).

     * `ENCRYPT_KEY`: optional. A Cloud KMS key that the workflow should use for data encryption in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`. For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/workflows/docs/use-cmek).

     * `SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com`: optional. The service account your workflow will use to access other Google Cloud services. If you want to update the roles for your service account, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

     * `YAML_OR_JSON_SOURCE_FILE`: required. The source file for the workflow in either YAML or JSON format. For example: `myFirstWorkflow.yaml`.




###  REST 

To update an existing workflow, use the [projects.locations.workflows.patch](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/patch) method and optionally use the `updateMask` query parameter to specify a list of fields to be updated.

Before using any of the request data, make the following replacements: 

  * `WORKFLOW_NAME`: the name of your workflow—for example, `myFirstWorkflow`.
  * `DESCRIPTION`: optional. A description of your workflow. Must be no longer than 1000 Unicode characters.
  * `LABEL_KEY` and `LABEL_VALUE`: optional. A map of label key and value pairs that help you organize your Google Cloud instances. For example: `{"name": "wrench", "mass": "1kg", "count": "3"}` For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels) Workflow labels are inherited by executions of the workflow. To view execution labels, use the `workflows.executions.list` method to [list and filter workflow executions](https://docs.cloud.google.com/workflows/docs/executing-workflow#filter_executions). **Note:** If you update an existing label, or add a new one, it can take up to 10 minutes for the new label to take effect. 
  * `SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com`: optional. The service account your workflow will use to access other Google Cloud services. The project ID is your Google Cloud project ID. For more information, in this document, see Create a service account.
  * `ENCRYPT_KEY`: optional. A Cloud KMS key that the workflow should use for data encryption in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`. For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/workflows/docs/use-cmek).
  * `CALL_LOGGING_LEVEL`: optional. The call logging level to apply during execution. The default is that no logging level is specified and the workflow log level applies instead. For more information, see [Send Logs to Logging](https://docs.cloud.google.com/workflows/docs/log-workflow). One of the following: 
    * `CALL_LOG_LEVEL_UNSPECIFIED`: no logging level is specified and the workflow log level applies instead. This is the default. Otherwise, the execution log level applies and takes precedence over the workflow log level.
    * `LOG_ERRORS_ONLY`: log all caught exceptions; or when a call is stopped due to an exception.
    * `LOG_ALL_CALLS`: log all calls to subworkflows or library functions and their results.
    * `LOG_NONE`: no call logging.
  * `EXECUTION_HISTORY_LEVEL`: optional. The execution history level to apply during execution. For more information, see [View history of execution steps](https://docs.cloud.google.com/workflows/docs/debug-steps). One of the following: 
    * `EXECUTION_HISTORY_LEVEL_UNSPECIFIED`: no execution history level is specified. This is the default. If an execution history level is not specified for an execution, it is determined by the level applied to the workflow. If the levels are different, the setting applied at the execution level overrides the setting applied at the workflow level for this execution.
    * `EXECUTION_HISTORY_BASIC`: enable basic execution history.
    * `EXECUTION_HISTORY_ADVANCED`: enable detailed execution history including any in-scope variable values and the expected number of iterations.
  * `ENV_KEY` and `ENV_VALUE`: optional. A map of environment variable key and value pairs; for example, `{ "month": "January", "day": "Monday"}`. For more information, see [Use environment variables](https://docs.cloud.google.com/workflows/docs/use-environment-variables).
  * `SOURCE_CODE`: the minified workflow definition. For example: `{\"main\":{\"params\":[\"input\"],\"steps\":[{\"returnOutput\":{\"return\":\"Hello\"}}]}}`
  * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) in which the workflow is deployed—for example, `us-central1`.
  * `UPDATE_FIELDS`: optional. A comma-separated list of fields to be updated. If not provided, the entire workflow is updated. For example `description,callLogLevel`.



Request JSON body: 
    
    
    {
      "name": "WORKFLOW_NAME",
      "description": "DESCRIPTION",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "cryptoKeyName": "ENCRYPT_KEY",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
      "userEnvVars": {"ENV_KEY":"ENV_VALUE"},
      "sourceContents": "SOURCE_CODE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "name": "WORKFLOW_NAME",
      "description": "DESCRIPTION",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "cryptoKeyName": "ENCRYPT_KEY",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
      "userEnvVars": {"ENV_KEY":"ENV_VALUE"},
      "sourceContents": "SOURCE_CODE"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://workflows.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME?updateMask="UPDATE_FIELDS""

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "name": "WORKFLOW_NAME",
      "description": "DESCRIPTION",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "serviceAccount": "SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com",
      "cryptoKeyName": "ENCRYPT_KEY",
      "callLogLevel": "CALL_LOGGING_LEVEL",
      "executionHistoryLevel": "EXECUTION_HISTORY_LEVEL"
      "userEnvVars": {"ENV_KEY":"ENV_VALUE"},
      "sourceContents": "SOURCE_CODE"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://workflows.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME?updateMask="UPDATE_FIELDS"" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/workflows/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.workflows.v1.OperationMetadata",
        "createTime": "2023-12-05T14:06:06.338390918Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME",
        "verb": "update",
        "apiVersion": "v1"
      },
      "done": false
    }
    

If the value of `"done"` is `false`, the operation is still in progress.

## Delete a workflow

You can delete an existing workflow. Deleting a workflow also deletes its executions and cancels any active executions for the workflow.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow you want to delete and then click delete **Delete**.

  3. At the prompt to confirm the deletion, enter the workflow name.

  4. Click **Confirm**.




### gcloud

  1. Open a terminal.

  2. Find the name of the workflow you want to delete. If you don't know the workflow's name, you can enter the following command to list all your workflows:
         
         gcloud workflows list

  3. Delete a workflow using the [`gcloud workflows delete`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/delete) command:
         
         gcloud workflows delete WORKFLOW_NAME

Replace `WORKFLOW_NAME` with the name of your workflow.




###  REST 

To delete a workflow with a specified name, use the [`projects.locations.workflows.delete`](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/delete) method.

Before using any of the request data, make the following replacements: 

  * `WORKFLOW_NAME`: the name of the workflow you want to delete.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/workflows/docs/locations) in which the workflow is deployed—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://workflows.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://workflows.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body contains an instance of [`Operation`](https://docs.cloud.google.com/workflows/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.workflows.v1.OperationMetadata",
        "createTime": "2023-12-05T14:06:06.338390918Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/workflows/WORKFLOW_NAME",
        "verb": "delete",
        "apiVersion": "v1"
      },
      "done": false
    }
    

If the value of `"done"` is `false`, the operation is still in progress.

## What's next

  * [Execute a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow)

  * [Control the order of execution in a workflow](https://docs.cloud.google.com/workflows/docs/controlling-execution-order)

  * [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
