---
url: https://docs.cloud.google.com/eventarc/standard/docs/workflows/quickstart-cal/
title: Quickstart: Trigger Workflows using Cloud Audit Logs (Google Cloud CLI) \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:27.391303+00:00
---

# Quickstart: Trigger Workflows using Cloud Audit Logs (Google Cloud CLI)  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/workflows/quickstart-cal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trigger Workflows using Cloud Audit Logs (gcloud CLI)

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This quickstart shows you how to execute a workflow using an Eventarc trigger that receives Cloud Audit Logs events from BigQuery. BigQuery hosts [public datasets](https://docs.cloud.google.com/bigquery/public-data) that you can access and integrate into your applications. The trigger executes the workflow by listening for a BigQuery job that queries a public dataset. It then passes the events as runtime arguments to the destination workflow.

You can complete this quickstart using the Google Cloud CLI.

  1. Use Workflows to create and deploy a workflow that extracts and returns data from an event.
  2. Create an Eventarc trigger that connects a BigQuery job to a Workflows event receiver.
  3. Generate an event by running a BigQuery job using the bq command-line tool. This event is passed as a runtime argument to the destination workflow.
  4. View the event data in the workflow execution output.



## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

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

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Update `gcloud` components: 
         
         gcloud components update

  13. Sign in using your account: 
         
         gcloud auth login

  14. Enable the Compute Engine, Eventarc, Pub/Sub, and Workflows APIs. 
         
         gcloud services enable \
         compute.googleapis.com \
         eventarc.googleapis.com \
         pubsub.googleapis.com \
         workflows.googleapis.com \
         workflowexecutions.googleapis.com

  15. Set the configuration variables used in this quickstart: 
         
         export WORKFLOW_LOCATION=us-central1
         export TRIGGER_LOCATION=us-central1
         export PROJECT_ID=PROJECT_ID
         gcloud config set project ${PROJECT_ID}
         gcloud config set workflows/location ${WORKFLOW_LOCATION}
         gcloud config set eventarc/location ${TRIGGER_LOCATION}

  16. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

#### Required permissions

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
     * [Workflows Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.admin) (`roles/workflows.admin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  17. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will attach it to an Eventarc trigger to represent the identity of the trigger for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  18. Grant the [Eventarc Event Receiver role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) on the project to the Compute Engine default service account so that the Eventarc trigger can receive events from event providers. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/eventarc.eventReceiver

  19. Grant the [Workflows Invoker role](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.invoker) (`roles/workflows.invoker`) on the project to the Compute Engine default service account so that the account has permission to trigger your workflow execution. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/workflows.invoker

  20. Grant the [Logging Logs Writer role](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the project to the Compute Engine default service account so that the workflow can send logs to Cloud Logging. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/logging.logWriter

  21. If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the service agent. Otherwise, this role is granted by default: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator




##  Create and deploy a workflow

Create and deploy a workflow that is executed when a BigQuery job completion triggers the workflow with an HTTP request.

  1. Open a terminal or [Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true). 
  2. In your home directory, create a new file called `myFirstWorkflow.yaml` or `myFirstWorkflow.json`.
  3. Copy and paste the following into the new file and save it: 

### YAML
         
         main:
           params: [event]
           steps:
               - log_event:
                   call: sys.log
                   args:
                       text: ${event}
                       severity: INFO
               - extract_data:
                   assign:
                   - data: ${event.data.protoPayload}
               - return_data:
                       return:
                           data: ${data}

### JSON
         
         {
           "main": {
             "params": [
               "event"
             ],
             "steps": [
               {
                 "log_event": {
                   "call": "sys.log",
                   "args": {
                     "text": "${event}",
                     "severity": "INFO"
                   }
                 }
               },
               {
                 "extract_data": {
                   "assign": [
                     {
                       "data": "${event.data.protoPayload}"
                     }
                   ]
                 }
               },
               {
                 "return_data": {
                   "return": {
                     "data": "${data}"
                   }
                 }
               }
             ]
           }
         }

  4. Deploy the workflow: 
         
         export MY_WORKFLOW=myFirstWorkflow
         gcloud workflows deploy ${MY_WORKFLOW} --source=myFirstWorkflow.yaml

Replace `.yaml` with `.json` if you copied the JSON version of the example workflow.




## Create an Eventarc trigger

To create an Eventarc trigger that routes events from BigQuery to a Workflows destination, run the [`gcloud eventarc triggers create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/create) command.

  1. Create a trigger that filters BigQuery events:
         
         gcloud eventarc triggers create events-cal-trigger \
             --destination-workflow=${MY_WORKFLOW} \
             --destination-workflow-location=${WORKFLOW_LOCATION} \
             --event-filters="type=google.cloud.audit.log.v1.written" \
             --event-filters="serviceName=bigquery.googleapis.com" \
             --event-filters="methodName=google.cloud.bigquery.v2.JobService.InsertJob" \
             --service-account="PROJECT_NUMBER-compute@developer.gserviceaccount.com"

This creates a trigger called `events-cal-trigger`.

Note that when creating an Eventarc trigger for the first time in a Google Cloud project, there might be a delay in provisioning the Eventarc service agent. This issue can usually be resolved by attempting to create the trigger again. For more information, see [Permission denied errors](https://docs.cloud.google.com/eventarc/docs/troubleshooting#trigger-error).

  2. To confirm `events-cal-trigger` was successfully created, run:
         
         gcloud eventarc triggers describe events-cal-trigger --location=${TRIGGER_LOCATION}

The output lists the trigger creation time and location and should be similar to the following:
         
         createTime: '2021-10-14T15:15:43.872360951Z'
         [...]
         name: projects/PROJECT_ID/locations/us-central1/triggers/events-cal-trigger
         


**Note:** Although your trigger is created immediately, it can take up to two minutes for a trigger to be fully functional.

## Generate and view an event

Run a BigQuery job using the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool) to generate events and trigger the workflow.

  1. To trigger the workflow, run a BigQuery job that accesses a public dataset and retrieves information from it:
         
         bq query --nouse_legacy_sql \
         'SELECT
         COUNT(*)
         FROM
         `bigquery-public-data`.samples.shakespeare'

The generated events are passed as [runtime arguments](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments) to the workflow which returns the payload data as a result of the workflow execution.

  2. To verify that the workflow was triggered, list its last two executions:
         
         gcloud workflows executions list ${MY_WORKFLOW} --limit=2

Two workflow executions are triggered by the BigQuery job. (One event signals the job change; the other, the job insertion itself.) The output lists a `NAME` and a `STATE` equal to `SUCCEEDED` for each of the executions, and should be similar to the following:
         
         NAME: projects/218898424763/locations/us-central1/workflows/myFirstWorkflow/executions/**a073ad6a-c76b-4437-8d39-2ab3ade289d2**
         STATE: SUCCEEDED
         START_TIME: 2024-02-06T14:16:14.390549813Z
         END_TIME: 2024-02-06T14:16:14.870102511Z
         NAME: projects/218898424763/locations/us-central1/workflows/myFirstWorkflow/executions/35d7c730-7ba5-4055-afee-c04ed706b179
         STATE: SUCCEEDED
         START_TIME: 2024-02-06T14:16:14.389882601Z
         END_TIME: 2024-02-06T14:16:14.829942525Z

Note that in the output, `a073ad6a-c76b-4437-8d39-2ab3ade289d2` from the `NAME` field is the ID of the workflow execution. Copy your execution ID to use in the next step.

  3. To view the execution status, run the following command:
         
         gcloud workflows executions describe WORKFLOW_EXECUTION_ID --workflow=${MY_WORKFLOW}

Replace `WORKFLOW_EXECUTION_ID` with the ID of the workflow execution that corresponds to the time at which the BigQuery job completed.

The output should be similar to the following:
         
         argument: [...]
         duration: 0.277917625s
         endTime: '2024-02-06T14:16:14.870102511Z'
         name: projects/218898424763/locations/us-central1/workflows/myFirstWorkflow/executions/a073ad6a-c76b-4437-8d39-2ab3ade289d2
         result: '{"data": [...]}'
         startTime: '2024-02-06T14:16:14.390549813Z'
         state: SUCCEEDED

  4. Verify that the `startTime` at which the BigQuery job completed and the `START_TIME` of the workflow execution correspond to each other.




You've successfully generated a BigQuery event that has triggered a Workflows event receiver using Eventarc.

## Clean up

  1. Delete the workflow you created: 
         
         gcloud workflows delete ${MY_WORKFLOW}

When asked if you want to continue, enter `y`. 
  2. Delete the trigger you created: 
         
         gcloud eventarc triggers delete events-cal-trigger

  3. Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project. **Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * [Control the order of execution in a workflow](https://docs.cloud.google.com/workflows/docs/controlling-execution-order)
  * [Determine events filters for Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/determining-filters-cal)
  * [Route Cloud Audit Logs events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-audit-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
