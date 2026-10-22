---
url: https://docs.cloud.google.com/eventarc/standard/docs/workflows/quickstart-pubsub/
title: Quickstart: Trigger Workflows using Pub/Sub messages (Google Cloud CLI) \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:38.290271+00:00
---

# Quickstart: Trigger Workflows using Pub/Sub messages (Google Cloud CLI)  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/workflows/quickstart-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trigger Workflows using Pub/Sub messages (gcloud CLI)

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This quickstart shows you how to execute a workflow using an [Eventarc trigger](https://docs.cloud.google.com/eventarc/docs/workflows/route-trigger-cloud-pubsub) that receives events using Pub/Sub. The trigger executes the workflow by passing events delivered through Pub/Sub as [runtime arguments](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments) to a destination workflow.

In this quickstart, you will: 

  1. Use Workflows to create and deploy a workflow that decodes and returns Pub/Sub messages.
  2. Create an Eventarc trigger that connects a Pub/Sub topic to a Workflows event receiver.
  3. Publish a message to the Pub/Sub topic to generate an event. This event is passed as a runtime argument to the destination workflow.
  4. View the Pub/Sub message as a result of the workflow execution.



## Before you begin

Make sure that you have access to this feature by [requesting to have your project added](https://docs.google.com/forms/d/e/1FAIpQLSdgwrSV8Y4xZv_tvI6X2JEGX1-ty9yizv3_EAOVHWVKXvDLEA/viewform) to private previews for Google Cloud Workflows.

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

  12. Update gcloud components: 
         
         gcloud components update

  13. Enable the Compute Engine, Eventarc, Pub/Sub, and Workflows APIs. 
         
         gcloud services enable \
         compute.googleapis.com \
         eventarc.googleapis.com \
         pubsub.googleapis.com \
         workflows.googleapis.com \
         workflowexecutions.googleapis.com

  14. Set the configuration variables used in this tutorial: 
         
         export WORKFLOW_LOCATION=us-central1
         export TRIGGER_LOCATION=us-central1
         export PROJECT_ID=PROJECT_ID
         gcloud config set project ${PROJECT_ID}
         gcloud config set workflows/location ${WORKFLOW_LOCATION}
         gcloud config set eventarc/location ${TRIGGER_LOCATION}

  15. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

#### Required permissions

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
     * [Workflows Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.admin) (`roles/workflows.admin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  16. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will attach it to an Eventarc trigger to represent the identity of the trigger for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  17. Grant the [Workflows Invoker role](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.invoker) (`roles/workflows.invoker`) on the project to the Compute Engine default service account so that the account has permission to trigger your workflow execution. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/workflows.invoker

  18. If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the service agent. Otherwise, this role is granted by default: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator




## Create and deploy a workflow

Create and deploy a workflow that gets executed when a message published to a Pub/Sub topic triggers a workflow with an HTTP request.

  1. Open a terminal or [Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true).
  2. In your home directory, create a new file called `myFirstWorkflow.yaml` or `myFirstWorkflow.json`.
  3. Copy and paste the following into the new file and save it: 

### YAML
         
         main:
           params: [event]
           steps:
             - decode_pubsub_message:
                 assign:
                    - base64: ${base64.decode(event.data.message.data)}
                    - message: ${text.decode(base64)}
             - return_pubsub_message:
                 return: ${message}

### JSON
         
         {
           "main": {
             "params": [
               "event"
             ],
             "steps": [
               {
                 "decode_pubsub_message": {
                   "assign": [
                     {
                       "base64": "${base64.decode(event.data.message.data)}"
                     },
                     {
                       "message": "${text.decode(base64)}"
                     }
                   ]
                 }
               },
               {
                 "return_pubsub_message": {
                   "return": "${message}"
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

When a message is published to the Pub/Sub topic, the event triggers the workflow.

  1. Create a trigger to listen for Pub/Sub messages: 

### New Pub/Sub topic
         
         gcloud eventarc triggers create events-pubsub-trigger \
             --destination-workflow=${MY_WORKFLOW} \
             --destination-workflow-location=${WORKFLOW_LOCATION} \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --service-account="PROJECT_NUMBER-compute@developer.gserviceaccount.com"

This creates a new Pub/Sub topic and a trigger for it called `events-pubsub-trigger`.

### Existing Pub/Sub topic
         
         gcloud eventarc triggers create events-pubsub-trigger \
             --destination-workflow=${MY_WORKFLOW} \
             --destination-workflow-location=${WORKFLOW_LOCATION} \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --service-account="PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --transport-topic=TOPIC_ID

Replace `TOPIC_ID` with the ID of the existing Pub/Sub topic.

This creates a trigger called `events-pubsub-trigger` for an existing Pub/Sub topic.

**Note:** By default, Pub/Sub subscriptions created for Eventarc persist regardless of activity and don't expire. To change the inactivity duration, see [Subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties). 

Note that when creating an Eventarc trigger for the first time in a Google Cloud project, there might be a delay in provisioning the Eventarc service agent. This issue can usually be resolved by attempting to create the trigger again. For more information, see [Permission denied errors](https://docs.cloud.google.com/eventarc/docs/troubleshooting#trigger-error).

  2. Confirm that the trigger was successfully created: 
         
         gcloud eventarc triggers describe events-pubsub-trigger --location=${TRIGGER_LOCATION}

The output should be similar to the following listing the time of creation and trigger location:
         
         createTime: '2021-10-14T15:15:43.872360951Z'
         [...]
         name: projects/PROJECT_ID/locations/us-central1/triggers/events-pubsub-trigger




## Generate and view an event

Publish a message to the Pub/Sub topic to generate an event and trigger the workflow. The generated event is passed as a [runtime argument](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments) to the workflow which returns the Pub/Sub message as a result of the workflow execution. Make sure that the [size of the events](https://docs.cloud.google.com/workflows/quotas#resource_limit) you pass to the workflow does not exceed 512 KB.

  1. If you created a trigger for a new Pub/Sub topic, find and set the Pub/Sub topic created, as an environment variable:
         
         export TOPIC_ID=$(basename $(gcloud eventarc triggers describe events-pubsub-trigger --format='value(transport.pubsub.topic)'))

  2. To trigger the workflow, send a message to the Pub/Sub topic:
         
         gcloud pubsub topics publish $TOPIC_ID --message "Hello there"

The generated event is passed as a runtime argument to the workflow which returns a "Hello there" message.

  3. To verify that a workflows execution was triggered, list the last five executions:
         
         gcloud workflows executions list ${MY_WORKFLOW} --limit=5

The output should be similar to the following, listing a NAME and STATE equal to `SUCCEEDED` for each workflow execution:
         
         NAME: projects/606789101455/locations/us-central1/workflows/myFirstWorkflow/executions/8c02b8f1-8836-4a6d-99d9-fc321eb9668f
         STATE: SUCCEEDED
         START_TIME: 2021-09-13T19:15:10.275677049Z
         END_TIME: 2021-09-13T19:15:10.963136883Z
         NAME: projects/606789101455/locations/us-central1/workflows/myFirstWorkflow/executions/**a6319d9d-36a6-4117-904e-3d1118bdc90a**
         STATE: SUCCEEDED
         START_TIME: 2021-09-13T17:28:51.492864252Z
         END_TIME: 2021-09-13T17:28:52.227212414Z
         

Note that in the `NAME` field in the preceding example, `a6319d9d-36a6-4117-904e-3d1118bdc90a` is the ID of the workflow execution. Copy your execution ID to use in the next step.

  4. To view the execution status, run the following command:
         
         gcloud workflows executions describe WORKFLOW_EXECUTION_ID --workflow=${MY_WORKFLOW}

Replace `WORKFLOW_EXECUTION_ID` with the ID of the workflow execution that corresponds to the publishing time of the Pub/Sub topic. The output is similar to the following:
         
         argument: [...]
         endTime: '2021-09-13T17:28:47.301012152Z'
         name: projects/1234567/locations/us-central1/workflows/myFirstWorkflow/executions/f72bc6d4-5ea0-4dfb-bb14-2dae82303120
         result: 'Hello there'
         startTime: '2021-09-13T17:28:51.492864252Z'
         state: SUCCEEDED

  5. Verify that the `publish_time` at which the Pub/Sub message was published and the `startTime` of the workflow execution correspond to each other.




Congratulations, you have successfully generated an event using a Pub/Sub topic that has triggered a Workflows event receiver using Eventarc.

## Clean up

  1. Delete the workflow you created: 
         
         gcloud workflows delete ${MY_WORKFLOW}

When asked if you want to continue, enter `y`. 
  2. Delete the trigger you created: 
         
         gcloud eventarc triggers delete events-pubsub-trigger

  3. Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project. **Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * [Control the order of execution in a workflow](https://docs.cloud.google.com/workflows/docs/controlling-execution-order)

  * [Create a trigger to route Pub/Sub events to Workflows](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-pubsub)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
