---
url: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/subscribe-to-datadog/
title: Subscribe to events from Datadog \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:31.220039+00:00
---

# Subscribe to events from Datadog  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/subscribe-to-datadog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Subscribe to events from Datadog Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Third-party events in Eventarc**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Datadog supports sending events to Eventarc for delivery to interested subscribers.

**Datadog** is an observability service for cloud-scale applications, providing monitoring of servers, databases, tools, and services, through a SaaS-based data analytics platform. [ Learn more about using Datadog](https://docs.datadoghq.com/).  | [ ![Datadog logo](https://docs.cloud.google.com/static/eventarc/images/third-parties/datadog-logo.svg)](https://www.datadoghq.com/)  
---|---  
**Note:** Eventarc is a fully managed platform for building event-driven systems and supports the ability for approved third-party vendors to generate events. The event sources are offered to you by the third-party vendor.

To subscribe to events from Datadog, complete the following steps:

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
         




## Retrieve the provider name used by Datadog

The provider name is required when creating and using a channel. You can list all Eventarc providers and retrieve their details, including supported event types, by running `gcloud` commands.

For example, you can list all third-party providers in any location:
    
    
    gcloud eventarc providers list --filter='eventTypes.type!~^google*' --location=-

The output includes something similar to the following:
    
    
    NAME: datadog
    LOCATION: us-central1
    

For details, see [List event providers](https://docs.cloud.google.com/eventarc/docs/list-providers).

## Retrieve the events supported by Datadog

An event type is needed when creating an Eventarc trigger. You can list Datadog's supported event types, by running a `gcloud` command:
    
    
    gcloud eventarc providers describe datadog \
        --location=LOCATION

Replace `LOCATION` with a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations).

For example:
    
    
    gcloud eventarc providers describe datadog --location=us-central1
    

The output is similar to the following:
    
    
    displayName: Datadog
    eventTypes:
    - type: datadog.v1.alert
    name: projects/project-id/locations/us-central1/providers/datadog
    [...]
    

Make note of the event type to use when creating an Eventarc trigger.

**Note:** If you run into a `Resource was not found` error, Datadog might not be available in the specified location. To verify the location, run `gcloud providers list --location=- --name=datadog`.

## Create a channel for Datadog events

To subscribe to events from Datadog, you must create a channel:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. Click add_box **Create channel**.

  3. Select a **Channel type** and **Provider**.

For example, select **Third-party** > **Datadog**.

  4. In the **Channel name** field, enter a name for the channel.

  5. In the **Region** list, select a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations).

  6. Optionally, select the **Use a customer-managed encryption key (CMEK)** checkbox and, in the **CMEK encryption key** list, select a key ring that you have created for the region.

For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/eventarc/docs/use-cmek).

  7. Click **Create**.




###  gcloud 
    
    
    gcloud eventarc channels create CHANNEL_NAME \
        --provider datadog \
        --project PROJECT_ID \
        --location LOCATION

Replace the following:

  * `CHANNEL_NAME`: a name for the channel
  * `PROJECT_ID`: your Google Cloud project ID

You can find your project ID on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.

  * `LOCATION`: a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations)

**Note:** For this Pre-GA feature, only `us-central1` is supported as a location. You cannot create a channel in any other location.



You can optionally use a `--crypto-key` flag to specify a fully qualified Cloud KMS key name in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`.

For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/eventarc/docs/use-cmek).

For details, see [Create a channel](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels#create-channel).

## Retrieve specific details to convey to Datadog

After creating a channel, you can retrieve specific details to convey to Datadog:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. From the list of channels, click a channel to view its details.

The channel status should be **`Pending`**.

  3. Copy the Channel full name and Activation token value. Both will be needed later to convey to Datadog and activate the channel.




###  gcloud 
    
    
    gcloud eventarc channels describe CHANNEL_NAME \
        --project PROJECT_ID \
        --location LOCATION

The output is similar to the following:
    
    
    **activationToken: aS7dXs1b79AcXsf**
    createTime: '2021-11-15T15:20:31.582356065Z'
    **name: projects/project-id/locations/us-central1/channels/datadog-channel**
    provider: projects/project-id/locations/us-central1/providers/datadog
    pubsubTopic: projects/project-id/topics/eventarc-channel-us-central1-datadog-channel-077
    state: PENDING
    uid: c6703a91-ccd3-4c32-a729-967393f23a29
    updateTime: '2021-11-15T15:21:03.689597653Z'
    

Note that the channel is in a `PENDING` state. To activate the channel, you must provide the `activationToken` value and the channel `name` to Datadog.

Learn more about the [channel state](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels#channel-state).

## Send the channel details to Datadog

Before you can start consuming events, Datadog must initialize the connection between their ecosystem and the channel.

  1. Log into Datadog at [https://www.datadoghq.com](https://www.datadoghq.com/).
  2. In the navigation menu, select **Integrations**.
  3. From the list of integrations, select **Google Eventarc**. 

A green checkmark confirms the installation:

![Installed](https://docs.cloud.google.com/static/eventarc/images/datadog-installed.png)
  4. Click **Configuration**. 
  5. In the Add New Channels section, click **Add New**.
  6. Enter the following channel details: 
     * **Channel full name** : the channel name, including the Google Cloud project ID and location of the resource.

For example: 
           
           projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME

     * **Activation token** : the token is valid for 24 hours after the channel's creation. After 24 hours, the channel becomes INACTIVE.

For example: `aS7dXs1b79AcXsf`

  7. To save the configuration, click the checkmark ![Save](https://docs.cloud.google.com/static/eventarc/images/datadog-save.png). 

The new channel is now listed.




Once Datadog receives the required information, and has initialized the connection between their ecosystem and the channel, the state of the channel changes from PENDING to ACTIVE. Datadog can now send events to your project and you can start consuming the events.

## Deploy an event receiver

To test the configuration, deploy an event receiver—in this case, a Workflows workflow that logs received events—and create an Eventarc trigger that routes events from Datadog to the event receiver. You must use a service account that has been granted the appropriate roles to access your Google Cloud project resources.

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

  4. Create an Eventarc trigger to route events from Datadog to the target workflow: 

### Console

     1. In the Google Cloud console, go to the **Eventarc** > **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

     2. Click add_box **Create trigger**.

     3. Type a **Trigger name**.

This is the ID of the trigger and it must start with a letter. For example, `my-event-channel-trigger`.

     4. Select a **Trigger type** and **Event provider**.

This is the partner service that is the source of events. For example, select **Third-party** > **Datadog**.

     5. Select the appropriate **Channel**.

     6. Select an **Event**.

For example: **datadog.v1.alert**

     7. Optionally, in the **Filters** section, specify an appropriate attribute and value.

     8. Select the **Service account** you previously created to invoke your workflow.

     9. For the **Event destination** , select **Workflows** , and then select the workflow you previously created.

     10. Click **Create**.

###  gcloud 
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-workflow=logEventsWorkflow  \
        --event-filters=type=datadog.v1.alert \
        --channel=CHANNEL_NAME \
        --project=PROJECT_ID \
        --service-account="MY_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com"
    

Replace `TRIGGER` with the ID of the trigger or a fully qualified identifier. For example, `my-event-channel-trigger`.

For more information, see [Create a trigger for a third-party provider](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty). 




## Test the routing of events

You can now test the entire configuration and ensure that an event from Datadog is routed to the workflow event receiver which logs the received event.

  1. To create a Datadog monitor, [log into Datadog](https://www.datadoghq.com/):

     1. In the navigation menu, select **Monitors** > **New Monitor**.
     2. From the list of **Custom** monitor types, select **Metric**.
     3. Accept the following default settings: 
        1. **Choose the detection method**
        2. **Define the metric**
     4. **Set alert conditions** : for the Alert threshold, enter **1**.
     5. **Notify your team** : give your monitor a name and, from the **Notify your services and your team members** list, select the appropriate value. The message should be similar to the following:

`@eventarc-PROJECT_ID_LOCATION_CHANNEL_NAME`

     6. **Define permissions and audit notifications** : select the appropriate values.

  2. Click **Test Notifications**.

  3. In the Test notifications for this monitor dialog, click **Run Test**.

This triggers an execution of the workflow.




For more information about configuring a Datadog monitor, see the [Datadog documentation](https://docs.datadoghq.com/monitors/).

* To verify that a workflow execution was triggered, list the last five executions:
    
    
    gcloud workflows executions list ${MY_WORKFLOW} --limit=5
    

The output should be similar to the following, listing a NAME and STATE equal to `SUCCEEDED` for each workflow execution.
    
    
    NAME: projects/1051295516635/locations/us-central1/workflows/logEventsWorkflow/executions/674b5783-deec-4d1b-be1d-b067f7b32971
    STATE: SUCCEEDED
    START_TIME: 2022-07-13T22:01:06.314980819Z
    END_TIME: 2022-07-13T22:01:06.637825944Z
    

* Every time a workflow executes a single run of the logic contained in a workflow's definition, it automatically triggers at least two execution logs: one at the start of an execution and one at the end. To view the logs do the following:

  1. In the Google Cloud console, go to the **Workflows** page:   
[Go to Workflows](https://console.cloud.google.com/workflows)

  2. To access a workflow's **Details** page, click the workflow's name.

  3. To view the logs, click **Logs**. The output should be similar to the following:



    
    
    {
      "alert_type": "error",
      "data": {
        "message": "@eventarc-test-project_us-central1_datadog-channel\nTest notification"
      },
      "datacontenttype": "application/json",
      "id": 6601612988428281000,
      "monitor": "monitor",
      "monitor_id": "1234567",
      "msg_title": "Triggered on 'TEST' Test monitor for Eventarc",
      "priority": "None",
      "source": "//datadog/alert",
      "specversion": "1.0",
      "time": "2022-07-13T22:01:03Z",
      "type": "datadog.v1.alert"
    }
    

## What's next

  * Get started using events from Datadog through the [codelab](https://codelabs.developers.google.com/codelabs/cloud-route-datadog-eventarc-part-one#0)
  * Learn more about [third-party events](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-parties-overview)
  * Learn more about [Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
