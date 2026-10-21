---
url: https://docs.cloud.google.com/vision-ai/docs/model-event-notification/
title: Enable model event notification with Cloud Functions and Pub/Sub \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:58.339450+00:00
---

# Enable model event notification with Cloud Functions and Pub/Sub  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/model-event-notification/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Enable model event notification with Cloud Functions and Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

In Gemini Enterprise Agent Platform Vision, models receive media data from devices like cameras, run AI predictions on the data, and produce annotations continuously. Frequently you send that processed data to a data destination ("data sink") such as a media warehouse or BigQuery for further analytic jobs. However, you may have a case where some annotations must be handled differently, or the annotation needs are time-sensitive. Integrations with Cloud Run functions and Pub/Sub help you address these needs. To be able to enable model event notifications, you need to do the following: 

  1. Listen to the model data and generate events from it using Cloud Run functions.
  2. Send the Cloud Run functions generated events through the Pub/Sub event channel. 



#### Supported models

The following models offer Cloud Run functions event generation and Pub/Sub event notification integrations:

  * [Occupancy analytics](https://docs.cloud.google.com/vision-ai/docs/occupancy-analytics-model) model
  * Vertex AI custom-trained models



## Before you begin

  * Create an app with, at minimum, a stream node and a supported model node.
  * Optional. [Install the Gemini Enterprise Agent Platform Vision SDK](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#get-source-code) and [ingest data](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams#ingest-videos) into your app. If you don't do this before you set up event notification you must do it after.
  * Optional. [Create a Cloud Run function](https://docs.cloud.google.com/functions/docs/create-deploy-gcloud-1st-gen) to use. If you don't create your Cloud Run function before you configure Cloud Run functions to process model output, you must create it during that process.
  * Optional. [Create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic) to use. If you don't create your Pub/Sub topic before you enable model event notification with Pub/Sub, you must create it during that process.
  * Optional. [Choose and create a Pub/Sub subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription). If you don't create your Pub/Sub subscription before you enable model event notification with Pub/Sub, you must create it after to read messages from a topic.



### Configure Cloud Run functions to process model output

To trigger event-based notifications, you must first set up Cloud Run functions to process model output and generate events.

Your Cloud Run function connects to the model and listens to its output as its post-processing action. The Cloud Run function you should return an [`AppPlatformCloudFunctionResponse`](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#appplatformcloudfunctionresponse). The events ([`appplatformeventbody`](https://docs.cloud.google.com/vision-ai/docs/reference/rpc/google.cloud.visionai.v1#appplatformeventbody)) are sent to the Pub/Sub topic you configure in the next step.

#### Sample Cloud Run function (occupancy analytics model)

###  Sample Cloud Run function 
    
    
    /**
    * Responds to any HTTP request.
    *
    * @param {!express:Request} req HTTP request context.
    * @param {!express:Response} res HTTP response context.
    */
    exports.hello_http = (req, res) => {
    // Logging statement can be read with cmd `gcloud functions logs read {$functionName}`.
    // For more about logging, please see https://cloud.google.com/functions/docs/monitoring
    
    // The processor output will be stored in req.body.
    const messageString = constructMessage(req.body);
    
    // Send your message to operator output with res HTTP response context.
    res.status(200).send(messageString);
    };
    
    function constructMessage(data) {
    // Typically, your processor output should contains appPlatformMetadata & it's designed output.
    // Here we will use the occupancy analytics model as an example.
    const appPlatformMetadata = data.appPlatformMetadata;
    const annotations = data.annotations;
    const events = [];
    for(const annotation of annotations) {
       events.push({
          "event_message": "Event message goes here",
          "payload" : {
             "attr_key_goes_here" : "val_goes_here"
          },
          "event_id" : "event_id_goes_here"
       });
    }
    
    // Typically, your cloud function should return a string represent a JSON which has two fields:
    // "annotations" must follow the specification of the target model.
    // "events" should be of type "AppPlatformEventBody".
    const messageJson = {
       "annotations": annotations,
       "events": events,
    };
    return JSON.stringify(messageJson);
    }
    

Use the following instructions to to send the model output stream to your Cloud Run function:

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Select schema**View app** next to the name of your application from the list.

  3. Click on the supported model to open the model details side panel.

  4. In the **post-processing** list of the **Event notification** section, select your existing Cloud Run function, or create a new one.

![Select postprocessing Cloud Function image in Cloud Console](https://docs.cloud.google.com/static/vision-ai/docs/images/select-postprocessing-cloud-function.png)




### Enable model event notification with Pub/Sub

After you have set up Cloud Run functions to process model output and generate events, you can set up event notification with Pub/Sub. To read messages from a topic, you also need to [Choose and create a Pub/Sub subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription).

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Select schema**View app** next to the name of your application from the list.

  3. Click on the supported model to open the model details side panel.

  4. In the **Event notification** section, select **Set up event notification**.

  5. In the **Set up Pub/Sub for event notifications** option window that opens, choose your existing Pub/Sub topic, or create a new one.

  6. In the **Frequency** field, set an integer value for the frequency value in seconds a notification for the same type of event can be sent.

![Set up event notification image in Cloud Console](https://docs.cloud.google.com/static/vision-ai/docs/images/setup-event-notification-button.png)

  7. Click **Set up**.




## What's next

  * Read instructions about how to deploy your app to test model event notification in [Deploy and undeploy an application](https://docs.cloud.google.com/vision-ai/docs/deploy-app).
  * Work through the [Gemini Enterprise Agent Platform Vision Occupancy Analytics app with event management](https://codelabs.developers.google.com/vertex-ai-event-management#0) codelab.
  * Learn more about Pub/Sub and Cloud Run functions in [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview) and the [Cloud Run functions overview](https://docs.cloud.google.com/functions/docs/concepts/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
