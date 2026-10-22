---
url: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/subscribe-to-lacework/
title: Subscribe to events from Lacework \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:33.622946+00:00
---

# Subscribe to events from Lacework  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/subscribe-to-lacework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)



Send feedback 

#  Subscribe to events from Lacework Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Private preview**

Support for **Lacework as an event source** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This pre-GA feature is supported only in private preview. To request access to the preview, refer to the [ Lacework instructions](https://docs.lacework.com/onboarding/google-eventarc). 

Lacework supports sending events to Eventarc for delivery to interested subscribers.

The **Lacework Polygraph® Data Platform** delivers end-to-end visibility and automated insight on risks across multicloud environments, collecting, analyzing, and correlating data. Customers depend on Lacework to drive revenue, bring products to market faster and safer, and consolidate security solutions into a single platform. [Learn more about using Lacework](https://docs.lacework.com/).  | [ ![Lacework logo](https://docs.cloud.google.com/static/eventarc/images/third-parties/lacework-primary-dark.png)](https://www.lacework.com/)  
---|---  
**Note:** Eventarc is a fully managed platform for building event-driven systems and supports the ability for approved third-party vendors to generate events. The event sources are offered to you by the third-party vendor.

To subscribe to events from Lacework, complete the following steps:

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
         




## Retrieve the provider name used by Lacework

The provider name is required when creating and using a channel. You can list all Eventarc providers and retrieve their details, including supported event types, by running `gcloud` commands.

For example, you can list all third-party providers in any location:
    
    
    gcloud eventarc providers list --filter='eventTypes.type!~^google*' --location=-

The output includes something similar to the following:
    
    
    NAME: lacework
    LOCATION: us-central1
    

For details, see [List event providers](https://docs.cloud.google.com/eventarc/docs/list-providers).

## Retrieve the events supported by Lacework

An event type is needed when creating an Eventarc trigger. You can list Lacework's supported event types, by running a `gcloud` command:
    
    
    gcloud eventarc providers describe lacework \
        --location=LOCATION

Replace `LOCATION` with a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations).

For example:
    
    
    gcloud eventarc providers describe lacework --location=us-central1
    

The output is similar to the following:
    
    
    displayName: Lacework
    eventTypes:
    - type: lacework.polygraph.v1.application
    name: projects/project-id/locations/us-central1/providers/lacework
    [...]
    

Make note of the event type to use when creating an Eventarc trigger.

**Note:** If you run into a `Resource was not found` error, Lacework might not be available in the specified location. To verify the location, run `gcloud providers list --location=- --name=lacework`.

## Create a channel for Lacework events

To subscribe to events from Lacework, you must create a channel:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. Click add_box **Create channel**.

  3. Select a **Channel type** and **Provider**.

For example, select **Third-party** > **Lacework**.

  4. In the **Channel name** field, enter a name for the channel.

  5. In the **Region** list, select a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations).

  6. Optionally, select the **Use a customer-managed encryption key (CMEK)** checkbox and, in the **CMEK encryption key** list, select a key ring that you have created for the region.

For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/eventarc/docs/use-cmek).

  7. Click **Create**.




###  gcloud 
    
    
    gcloud eventarc channels create CHANNEL_NAME \
        --provider lacework \
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

## Retrieve specific details to convey to Lacework

After creating a channel, you can retrieve specific details to convey to Lacework:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. From the list of channels, click a channel to view its details.

The channel status should be **`Pending`**.

  3. Copy the Channel full name and Activation token value. Both will be needed later to convey to Lacework and activate the channel.




###  gcloud 
    
    
    gcloud eventarc channels describe CHANNEL_NAME \
        --project PROJECT_ID \
        --location LOCATION

The output is similar to the following:
    
    
    **activationToken: aS7dXs1b79AcXsf**
    createTime: '2021-11-15T15:20:31.582356065Z'
    **name: projects/project-id/locations/us-central1/channels/lacework-channel**
    provider: projects/project-id/locations/us-central1/providers/lacework
    pubsubTopic: projects/project-id/topics/eventarc-channel-us-central1-lacework-channel-077
    state: PENDING
    uid: c6703a91-ccd3-4c32-a729-967393f23a29
    updateTime: '2021-11-15T15:21:03.689597653Z'
    

Note that the channel is in a `PENDING` state. To activate the channel, you must provide the `activationToken` value and the channel `name` to Lacework.

Learn more about the [channel state](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels#channel-state).

## Send the channel details to Lacework

Use the form available at <https://eventarc.laceworkalliances.com> to convey to Lacework the following channel details.

  * **Lacework instance** : a name for the instance. This is used to name the Pub/Sub topic and is required when configuring the alert channel. We suggest using the Eventarc channel short name.

For example: `lacework-alerts`

  * **Channel** : the full channel name, including the Google Cloud project ID and location of the resource. For example:
        
        projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_ID

  * **Activation token** : the token is valid for 24 hours after the channel's creation. After 24 hours, the channel becomes INACTIVE.

For example: `aS7dXs1b79AcXsf`




After completing the form, submit it.

## Configure the Lacework alert channel

After you have submitted the channel details, follow the [Lacework instructions](https://docs.lacework.com/onboarding/google-eventarc) to configure the alert channel.

Once Lacework receives the required information, and has initialized the connection between their ecosystem and the channel, the state of the channel changes from PENDING to ACTIVE.

Lacework can now send events to your project and you can start consuming the events.

## Deploy an event receiver

To test the configuration, deploy an event receiver—in this case, a Workflows workflow that logs received events—and create an Eventarc trigger that routes events from Lacework to the event receiver. You must use a service account that has been granted the appropriate roles to access your Google Cloud project resources.

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

  4. Create an Eventarc trigger to route events from Lacework to the target workflow: 

### Console

     1. In the Google Cloud console, go to the **Eventarc** > **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

     2. Click add_box **Create trigger**.

     3. Type a **Trigger name**.

This is the ID of the trigger and it must start with a letter. For example, `my-event-channel-trigger`.

     4. Select a **Trigger type** and **Event provider**.

This is the partner service that is the source of events. For example, select **Third-party** > **Lacework**.

     5. Select the appropriate **Channel**.

     6. Select an **Event**.

For example: **lacework.polygraph.v1.application**

     7. Optionally, in the **Filters** section, specify an appropriate attribute and value.

     8. Select the **Service account** you previously created to invoke your workflow.

     9. For the **Event destination** , select **Workflows** , and then select the workflow you previously created.

     10. Click **Create**.

###  gcloud 
    
    gcloud eventarc triggers create TRIGGER \
        --location=LOCATION \
        --destination-workflow=logEventsWorkflow  \
        --event-filters=type=lacework.polygraph.v1.application \
        --channel=CHANNEL_NAME \
        --project=PROJECT_ID \
        --service-account="MY_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com"
    

Replace `TRIGGER` with the ID of the trigger or a fully qualified identifier. For example, `my-event-channel-trigger`.

For more information, see [Create a trigger for a third-party provider](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty). 




## Test the routing of events

You can now test the entire configuration and ensure that an event from Lacework is routed to the workflow event receiver which logs the received event.

  1. From the Lacework Console, in the list of alert channels, find your channel and, in Integration, click **Test**.

This triggers an execution of the workflow and you should see an `Integration test was successful` message.

  2. To verify that a workflow execution was triggered, list the last five executions:
         
         gcloud workflows executions list ${MY_WORKFLOW} --limit=5
         

The output should be similar to the following, listing a NAME and STATE equal to `SUCCEEDED` for each workflow execution.
         
         NAME: projects/606789101455/locations/us-central1/workflows/logEventsWorkflow/executions/8c02b8f1-8836-4a6d-99d9-fc321eb9668f
         STATE: SUCCEEDED
         START_TIME: 2021-09-13T19:15:10.275677049Z
         END_TIME: 2021-09-13T19:15:10.963136883Z
         NAME: projects/606789101455/locations/us-central1/workflows/logEventsWorkflow/executions/a6319d9d-36a6-4117-904e-3d1118bdc90a
         STATE: SUCCEEDED
         START_TIME: 2021-09-13T17:28:51.492864252Z
         END_TIME: 2021-09-13T17:28:52.227212414Z
         

  3. Every time a workflow executes a single run of the logic contained in a workflow's definition, it automatically triggers at least two execution logs: one at the start of an execution and one at the end. To view the logs do the following:

     1. In the Google Cloud console, go to the **Workflows** page:   
[Go to Workflows](https://console.cloud.google.com/workflows)

     2. To access a workflow's **Details** page, click the workflow's name.

     3. To view the logs, click **Logs**. The output should be similar to the following:
    
    2022-06-10 13:49:50.019 BST {data: {…}, datacontenttype: application/json,[...]
    {
      "eventCategory": "TestEvent",
      "id": "a91ca1a5-85e7-4dad-a329-cf7deba8e14d",
      "severity": "0",
      "source": "//lacework/alertChannel/test",
      "type": "lacework.polygraph.v1.application",
      "link": "https://login.lacework.net",
      "eventName": "Test Event",
      "datacontenttype": "application/json",
      "resource": "TestEvent",
      "specversion": "1.0",
      "data": {
        "EVENT_ID": "0",
        "EVENT_TYPE": "TestEvent",
        "START_TIME": "10 Jun 2022 12:49 GMT",
        "LINK": "https://login.lacework.net",
        "EVENT_DETAILS": {
          "data": null
        },
        "SEVERITY": 0,
        "SUMMARY": "This is a test Message.",
        "EVENT_CATEGORY": "TestEvent",
        "EVENT_NAME": "Test Event"
      }
    }
    




## What's next

  * Learn more about [third-party events](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-parties-overview)
  * Learn more about [Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)
  * Learn more about [Workflows](https://docs.cloud.google.com/workflows/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
