---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/field-mask/
title: Update data with a FieldMask \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:17.265706+00:00
---

# Update data with a FieldMask  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/field-mask/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Update data with a FieldMask Stay organized with collections  Save and categorize content based on your preferences. 

When updating agent data with the API, you can choose to overwrite the entire data type or to overwrite only specific fields of the data type. It is usually best to overwrite specific fields, so you avoid accidentally overwriting all of your data. To overwrite specific fields, supply a [`FieldMask`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask) to your update request.

The following examples show how to supply a `FieldMask` to update the display name for an [Intents](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#intents) type.

### REST

Supply the `updateMask` URL query parameter for the `patch` method. For example: 
    
    
    ?updateMask=displayName
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dialogflow.v2.[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.html);
    import com.google.cloud.dialogflow.v2.[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.html).Builder;
    import com.google.cloud.dialogflow.v2.[IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.html);
    import com.google.cloud.dialogflow.v2.[UpdateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateIntentRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateIntent {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String intentId = "my-intent-id";
        String location = "my-location";
        String displayName = "my-display-name";
        updateIntent(projectId, intentId, location, displayName);
      }
    
      // DialogFlow API Update Intent sample.
      public static void updateIntent(
          String projectId, String intentId, String location, String displayName) throws IOException {
        try ([IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.html) client = [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.html).create()) {
          String intentPath =
              "projects/" + projectId + "/locations/" + location + "/agent/intents/" + intentId;
    
          Builder intentBuilder = client.getIntent(intentPath).toBuilder();
    
          intentBuilder.setDisplayName(displayName);
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("display_name").build();
    
          [Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.html) intent = intentBuilder.build();
          [UpdateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateIntentRequest.html) request =
              [UpdateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateIntentRequest.html).newBuilder()
                  .setIntent(intent)
                  .setLanguageCode("en")
                  .setUpdateMask(fieldMask)
                  .build();
    
          // Make API request to update intent using fieldmask
          [Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.html) response = client.updateIntent(request);
          System.out.println(response);
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {IntentsClient} = require('[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)');
    
    const intentClient = new [IntentsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    const agentPath = intentClient.projectAgentPath(projectId);
    const intentPath = agentPath + '/intents/' + intentId;
    
    const intent = await intentClient.getIntent({name: intentPath});
    intent[0].displayName = displayName;
    const updateMask = {
      paths: ['display_name'],
    };
    
    const updateIntentRequest = {
      intent: intent[0],
      updateMask: updateMask,
      languageCode: 'en',
    };
    
    //Send the request for update the intent.
    const result = await intentClient.updateIntent(updateIntentRequest);
    console.log(result);

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.dialogflow_v2 import IntentsClient
    from google.protobuf import field_mask_pb2
    
    
    def update_intent(project_id, intent_id, display_name):
        intents_client = IntentsClient()
    
        intent_name = intents_client.[intent_path](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.intents.IntentsClient.html#google_cloud_dialogflow_v2_services_intents_IntentsClient_intent_path)(project_id, intent_id)
        intent = intents_client.[get_intent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.intents.IntentsClient.html#google_cloud_dialogflow_v2_services_intents_IntentsClient_get_intent)(request={"name": intent_name})
    
        intent.display_name = display_name
        update_mask = field_mask_pb2.FieldMask(paths=["display_name"])
        response = intents_client.[update_intent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.intents.IntentsClient.html#google_cloud_dialogflow_v2_services_intents_IntentsClient_update_intent)(intent=intent, update_mask=update_mask)
        return response
    
    

[ Previous arrow_back  Manage knowledge bases  ](https://docs.cloud.google.com/dialogflow/es/docs/how/knowledge-bases)

[ Next Detect intent with audio input file  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/how/detect-intent-audio)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
