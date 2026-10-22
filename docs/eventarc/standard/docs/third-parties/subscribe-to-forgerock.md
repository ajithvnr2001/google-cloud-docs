---
url: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/subscribe-to-forgerock/
title: Subscribe to events from ForgeRock \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:31.024477+00:00
---

# Subscribe to events from ForgeRock  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/subscribe-to-forgerock/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Subscribe to events from ForgeRock Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Third-party events in Eventarc**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

ForgeRock supports sending events to Eventarc for delivery to interested subscribers.

**ForgeRock** offers an end-to-end, AI-driven platform purpose-built for all identities and for any environment—on-prem, multicloud, or hybrid. A single, unified platform offers access management, identity management, user-managed access, directory services, and an identity gateway. [ Learn more about using ForgeRock](https://backstage.forgerock.com/marketplace/entry/HLnLJoIBikSWLjD7QI1T).  | [ ![ForgeRock logo](https://docs.cloud.google.com/static/eventarc/images/third-parties/forgerock-logo.png)](https://www.forgerock.com/)  
---|---  
**Note:** Eventarc is a fully managed platform for building event-driven systems and supports the ability for approved third-party vendors to generate events. The event sources are offered to you by the third-party vendor.

To subscribe to events from ForgeRock, complete the following steps:

## Before you begin

  1. Ensure that you have enabled the Eventarc and Eventarc Publishing APIs:

###  Console 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com)

###  gcloud 
         
         gcloud services enable \
           eventarc.googleapis.com \
           eventarcpublishing.googleapis.com
         

  2. If you are [enabling a customer-managed encryption key (CMEK)](https://docs.cloud.google.com/eventarc/docs/use-cmek#enable-cmek-thirdparty-channel) for a channel, enable the Cloud Key Management Service API.

###  Console 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

###  gcloud 
         
         gcloud services enable cloudkms.googleapis.com
         




## Create a channel for ForgeRock events

To subscribe to events from ForgeRock, you must create a channel:
    
    
    gcloud eventarc channels create CHANNEL_NAME \
        --location LOCATION

Replace the following:

  * `CHANNEL_NAME`: a name for the channel
  * `LOCATION`: a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations)

**Note:** For this Pre-GA feature, only `us-central1` is supported as a location. You cannot create a channel in any other location.



You can optionally use a `--crypto-key` flag to specify a fully qualified Cloud KMS key name in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`.

For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/eventarc/docs/use-cmek).

**Note:** The channel must be created in the same project and [region](https://docs.cloud.google.com/eventarc/docs/locations) as the Eventarc trigger. The trigger can route events to services in other regions but only within the same project.

## Confirm that the channel is active

After creating a channel, you can retrieve the channel properties and confirm that it is active:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Eventarc](https://console.cloud.google.com/eventarc/channels)

  2. From the list of channels, click a channel to view its details.

The channel status should be **`Active`**.




###  gcloud 
    
    
    gcloud eventarc channels describe CHANNEL_NAME \
      --location LOCATION

Replace `LOCATION` with a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations).

The output is similar to the following:
    
    
    createTime: '2022-04-26T20:46:06.113533183Z'
    name: projects/PROJECT_NAME/locations/LOCATION/channels/CHANNEL_NAME
    pubsubTopic: projects/PROJECT_NAME/topics/eventarc-channel-LOCATION-CHANNEL_NAME-465
    state: ACTIVE
    uid: 86391a0b-a264-4172-a3b5-a893179f1d1a
    updateTime: '2022-04-26T20:46:10.106938915Z'
    

## Deploy an event receiver

To test the configuration, deploy an event receiver—in this case, a Workflows workflow that logs received events—and create an Eventarc trigger that routes events from ForgeRock to the event receiver. You must use a service account that has been granted the appropriate roles to access your Google Cloud project resources.

  1. Enable the Workflows and Workflow Executions APIs:

###  Console 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com,workflowexecutions.googleapis.com)

###  gcloud 
         
         gcloud services enable \
             workflows.googleapis.com \
             workflowexecutions.googleapis.com
         

  2. Create a service account and grant it the `roles/logging.logWriter` and `roles/workflows.invoker` roles:

###  Console 

     1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. Select your project.

     3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. Optionally, add a description.

     4. Click **Create and continue**.

     5. In the **Select a role** list, select **Logging** > **Logs Writer**.

     6. Click add **Add another role** and select **Workflows** > **Workflows Invoker**.

     7. Click **Continue**.

     8. To finish creating the service account, click **Done**.

###  gcloud 
    
    gcloud iam service-accounts create MY_SERVICE_ACCOUNT
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="roles/workflows.invoker" \
        --member="serviceAccount:MY_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="roles/logging.logWriter" \
        --member="serviceAccount:MY_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com"
    

Replace `MY_SERVICE_ACCOUNT` with a name for your service account.

For more information about how to control access to Workflows resources, see [Use IAM to control access](https://docs.cloud.google.com/workflows/docs/use-iam-for-access).

  3. Create and deploy a workflow that logs a received event:

### Console

     1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

     2. Click **Create**.

     3. Name your workflow `logEventsWorkflow`.

     4. Choose a supported Workflows [region](https://docs.cloud.google.com/workflows/docs/locations); for example, **us-central1**.

     5. Select the **Service account** you previously created.

     6. Click **Next**.

     7. In the workflow editor, enter the following definition for your workflow:
            
            main:
              params: [event]
              steps:
              - logStep:
                  call: sys.log
                  args:
                    data: ${event}
            

     8. Click **Deploy**.

### gcloud

     1. Open a terminal or [Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true).
     2. In your home directory, create a new file called `logEventsWorkflow.yaml`.
     3. Copy and paste the following into the new file and save it:
            
            main:
              params: [event]
              steps:
              - logStep:
                  call: sys.log
                  args:
                    data: ${event}
            

     4. Deploy the workflow:
            
            gcloud workflows deploy logEventsWorkflow \
                --source=logEventsWorkflow.yaml \
                --location LOCATION
            

Replace `LOCATION` with a supported Workflows [region](https://docs.cloud.google.com/workflows/docs/locations); for example, `us-central1`.

  4. Create an Eventarc trigger to route events from ForgeRock to the target workflow: 
         
         gcloud eventarc triggers create TRIGGER \
             --location=LOCATION \
             --destination-workflow=logEventsWorkflow  \
             --event-filters=type=forgerock.v1.event \
             --channel=CHANNEL_NAME \
             --service-account="MY_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com"
         

Replace `TRIGGER` with the ID of the trigger or a fully qualified identifier. For example, `my-event-channel-trigger`.

For more information, see [Publish and route custom events](https://docs.cloud.google.com/eventarc/docs/custom-events/route-custom-events#trigger-gcloud). 




## Create a service account for publishing events

Create a service account for the publishing of events and grant it the `roles/eventarc.publisher` role.

###  Console 

  1. In the Google Cloud console, go to the **Create service account** page.

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

  2. Select your project.

  3. In the **Service account name** field, enter a name. For example, **forgerock-sa**. The Google Cloud console fills in the **Service account ID** field based on this name. Optionally, add a description. For example, **ForgeRock service account**.

  4. Click **Create and continue**.

  5. In the **Select a role** list, select **Eventarc** > **Publisher**.

  6. Click **Continue**.

  7. To finish creating the service account, click **Done**.




###  gcloud 
    
    
      gcloud iam service-accounts create PUBLISHING_SERVICE_ACCOUNT
      gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="roles/eventarc.publisher" \
        --member="serviceAccount:PUBLISHING_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com"
    

Replace `PUBLISHING_SERVICE_ACCOUNT` with a name for your service account. For example, `forgerock-sa`.

## Create and download a service account key

Create and download a service account key that can be used to authenticate as your service account. This key is required when configuring an audit event handler for ForgeRock. For more information, see [Create and manage service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).

###  Console 

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select your project.

  3. Find the row of the ForgeRock service account that you previously created and that you want to create a key for. In that row, click  **More** more_vert and then select **Manage keys**.

  4. On the **Keys** page, click **Add key** > **Create new key**.

  5. For the **Key type** , select **JSON**.

  6. Click **Create**.




###  gcloud 
    
    
    gcloud iam service-accounts keys create SERVICE_ACCOUNT_KEY \
        --iam-account PUBLISHING_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com
    

Replace the following:

  * `SERVICE_ACCOUNT_KEY`: the path to an output file for the private key; for example, `~/forgerock-sa-key.json`.
  * `PUBLISHING_SERVICE_ACCOUNT`: the ForgeRock service account name you created previously.



The service account key is downloaded to your machine. After you download the key file, you cannot download it again. You will need to copy the contents of this file in the following step.

Make sure to store the key file securely because it can be used to authenticate as your service account. You can move and rename this file.

## Configure the audit event handler

A ForgeRock audit event handler manages audit events, sends audit output to a defined location, and controls the output format. You can use the audit event handler to confirm that events triggered through ForgeRock are being routed by Eventarc to the workflow that logs the received events.

  1. Log into ForgeRock's Identity Management (IDM) console. For details about logging in, refer to [Downloading and starting the server](https://backstage.forgerock.com/docs/idm/6/getting-started/#download-and-start).
  2. Select **Configure System Preferences** and then click the **Audit** tab.
  3. In the **Event Handlers** list, select **EventarcAuditEventHandler**.
  4. Click **Add Event Handler**.
  5. In the **Add Audit Event Handler** dialog, complete the following: 
     1. Give your audit event handler a unique **Name**.
     2. In the **Audit Events** list, select the items that will generate events. (For testing purposes, select them all.)
     3. Confirm that the **Enabled** toggle is on.
     4. In the **jsonCredentials** field, paste the contents of the service account key that you copied previously.
     5. Specify the remaining fields appropriately. For the **Event type** field, type **forgerock.v1.event**.
     6. Click **Submit**.
     7. Click **Save**.



## Test the routing of events

You can now test the entire configuration by accessing ForgeRock to trigger an event, and ensuring that the event from ForgeRock is routed to the workflow event receiver which logs the received event.

  1. Log into ForgeRock's Identity Management (IDM) console.
  2. Select **Configure** > **System Preferences** and then click the **Audit** tab.

This triggers the `access` audit event.

  3. To verify that a workflow execution was triggered by the received event, list the last five executions:
         
         gcloud workflows executions list ${MY_WORKFLOW} --limit=5
         

The output should be similar to the following, listing a NAME and STATE equal to `SUCCEEDED` for each workflow execution.
         
         NAME: projects/1051295516635/locations/us-central1/workflows/logEventsWorkflow/executions/674b5783-deec-4d1b-be1d-b067f7b32971
         STATE: SUCCEEDED
         START_TIME: 2022-07-13T22:01:06.314980819Z
         END_TIME: 2022-07-13T22:01:06.637825944Z
         

  4. Every time a workflow executes a single run of the logic contained in a workflow's definition, it automatically triggers at least two execution logs: one at the start of an execution and one at the end. To view the logs do the following:

     1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

     2. To access a workflow's **Details** page, click the workflow's name.

     3. To view the execution details, in the **Executions** tab, click a specific **Execution ID**.




## What's next

  * Learn more about [third-party events](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-parties-overview) and [custom events](https://docs.cloud.google.com/eventarc/docs/custom-events/route-custom-events).
  * Learn more about [Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
