---
url: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/test-event-subscription-flow/
title: Test the configuration \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:30.867234+00:00
---

# Test the configuration  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/test-event-subscription-flow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Test the configuration Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Third-party events in Eventarc**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Test a third-party configuration and ensure that the event subscription and publishing flow is working as expected. The following is a recommended way to approach this task.

## Prerequisites

  1. You will need the following values that you specified when [registering as a provider](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/register-provider):

     * `PROVIDER_NAME`: the provider name that subscribers will specify when subscribing to events.

     * `PUBLISHER_PROJECT_ID`: the provider's Google Cloud project that is used to publish events.

     * `SUBSCRIBER_PROJECT_ID`: the subscriber's Google Cloud project ID used to subscribe to events for testing or during any alpha period.

     * `EVENT_TYPE`: the event types published by the event provider.

  2. Use the Google Cloud CLI to enable the Eventarc API in your subscriber project, and to enable the Eventarc Publishing API in both your publisher and subscriber projects:
         
         gcloud services enable eventarc.googleapis.com --project=SUBSCRIBER_PROJECT_ID
         gcloud services enable eventarcpublishing.googleapis.com --project=PUBLISHER_PROJECT_ID
         gcloud services enable eventarcpublishing.googleapis.com --project=SUBSCRIBER_PROJECT_ID
         




## Event subscription and publishing test

This test includes creating a channel, a channel connection, and a trigger. To ensure that an event is delivered to the trigger's destination, an event receiver is deployed: a Workflows workflow that logs received events. All steps in the test must succeed.

Note that you must use a service account that has been granted the appropriate roles to access your Google Cloud project resources.

### Subscriber tasks

In the subscriber project, do the following:

  1. Create a channel to support the interaction with the provider.
         
         gcloud eventarc channels create CHANNEL_NAME \
             --provider PROVIDER_NAME \
             --project SUBSCRIBER_PROJECT_ID \
             --location LOCATION
         

Replace the following:

     * `CHANNEL_NAME`: a name for the channel
     * `PROVIDER_NAME`: the provider's name; see [List event providers](https://docs.cloud.google.com/eventarc/docs/list-providers)
     * `SUBSCRIBER_PROJECT_ID`: the subscriber's Google Cloud project ID
     * `LOCATION`: a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations)

For details, see [Create a channel](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels#create-channel).

  2. Retrieve specific channel properties.
         
         gcloud eventarc channels describe CHANNEL_NAME \
             --project SUBSCRIBER_PROJECT_ID \
             --location LOCATION
         

In the output, note the `activationToken` value and the channel `name`.

For details, see [Retrieve channel details](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels#describe-channel).

  3. Enable the Workflows APIs:
         
         gcloud services enable workflows.googleapis.com workflowexecutions.googleapis.com
         

  4. Create a service account and give it a name:
         
         gcloud iam service-accounts create MY_SERVICE_ACCOUNT
         

Replace `MY_SERVICE_ACCOUNT` with a name for your service account.

  5. Grant the `roles/workflows.invoker` and `roles/logging.logWriter` roles to the service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --role="roles/workflows.invoker" \
           --role="roles/logging.logWriter" \
           --member="serviceAccount:MY_SERVICE_ACCOUNT@SUBSCRIBER_PROJECT_ID.iam.gserviceaccount.com"
         

For more information about how to control access to Workflows resources, see [Use IAM to control access](https://docs.cloud.google.com/workflows/docs/use-iam-for-access).

  6. Create and deploy a workflow that logs a received event:

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
            
            gcloud workflows deploy logEventsWorkflow --source=logEventsWorkflow.yaml
            

  7. Create a trigger for an event type. The following command creates a trigger for a specified event type supported by the provider, and for the `logEventsWorkflow` target workflow.
         
         gcloud eventarc triggers create TRIGGER \
             --location=LOCATION \
             --destination-workflow=logEventsWorkflow  \
             --event-filters=type=EVENT_TYPE \
             --channel=CHANNEL_NAME \
             --project=SUBSCRIBER_PROJECT_ID \
             --service-account="MY_SERVICE_ACCOUNT@SUBSCRIBER_PROJECT_ID.iam.gserviceaccount.com"
         

Replace `TRIGGER` with the ID of the trigger or a fully qualified identifier. For example, `my-event-trigger`.

For more information, see [Create a trigger for a third-party provider](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-trigger-thirdparty).




### Provider tasks

In the provider project, do the following:

  1. Create a channel connection. You can do this through your own code. You can also use the gcloud CLI.
         
         gcloud eventarc channel-connections create CHANNEL_CONNECTION \
             --project PUBLISHER_PROJECT_ID \
             --location REGION \
             --channel CHANNEL_NAME \
             --activation-token ACTIVATION_TOKEN
         

For details, see [Create a channel connection](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/configure-your-source#create-connection).

  2. Once a channel connection exists, you can publish events using the Eventarc Publishing API. Publish an event that matches the trigger's filter. To test this, you can use cURL and the gcloud CLI. For example:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -H "X-Goog-User-Project: {publisher_project_id}" -X POST -d '{
         "channelConnection": "projects/{publisher_project_id}/locations/us-central1/channelConnections/test-connection-123",
         "events": [
          {
            "@type": "type.googleapis.com/io.cloudevents.v1.CloudEvent",
            "id": "12345",
            "source": "//companyname/example",
            "specVersion": "1.0",
            "type": "{event_type}",
            "attributes": {
              "time": {
                "ceTimestamp": "1970-01-01T00:00:01Z"
              },
              "datacontenttype": {
                "ceString": "application/json"
              }
            },
            "textData": "{\"message\": \"test message 123\"}"
          }
         ]
         }' https://eventarcpublishing.googleapis.com/v1/projects/{publisher_project_id}/locations/us-central1/channelConnections/test-connection-123:publishEvents
         

For details, see [Publish events](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/configure-your-source#publish-events).




### Verify results

As a subscriber, to test the configuration, verify that the event is delivered as expected to the trigger's destination. An execution of the workflow should have been triggered by the publishing of the event.

  1. To verify that a workflow execution was triggered, list the last five executions:
         
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
         

  2. Each workflow execution automatically triggers at least two execution logs: one at the start of an execution and one at the end. To view the logs do the following:

     1. In the Google Cloud console, go to the **Workflows** page:   
[Go to Workflows](https://console.cloud.google.com/workflows)

     2. To access a workflow's **Details** page, click the workflow's name.

     3. To view the logs, click **Logs**. The output should be similar to the following:
            
            2022-06-10 13:49:50.019 BST {data: {…}, datacontenttype: application/json,[...]
            {
              "eventCategory": "TestEvent",
              "id": "a91ca1a5-85e7-4dad-a329-cf7deba8e14d",
              "severity": "0",
              "source": "//provider/providerChannel/test",
              "type": "companyname.fooProcess.v1.resourceUpdated",
              "link": "https://www.example.com",
              "eventName": "Test Event",
              "datacontenttype": "application/json",
              "resource": "TestEvent",
              "specversion": "1.0",
              "data": {
                "EVENT_ID": "0",
                "EVENT_TYPE": "TestEvent",
                "START_TIME": "10 Jun 2022 12:49 GMT",
                "LINK": "https://www.example.com",
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

  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)
  * [Learn about third-party events in Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-parties-overview)
  * [Troubleshoot event publishing errors](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/troubleshoot-providers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
