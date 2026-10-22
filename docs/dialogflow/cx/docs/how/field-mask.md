---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/field-mask/
title: Update data with a FieldMask \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:09.046874+00:00
---

# Update data with a FieldMask  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/field-mask/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Update data with a FieldMask Stay organized with collections  Save and categorize content based on your preferences. 

When updating agent data with the API, you can choose to overwrite the entire data type or to overwrite only specific fields of the data type. It is usually best to overwrite specific fields, so you avoid accidentally overwriting all of your data. To overwrite specific fields, supply a [`FieldMask`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask) to your update request.

The following examples show how to supply a `FieldMask` to update the display name for an `Intent` type. Go to the Intent API reference

**Select a protocol and version for the Intent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents) |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.intents)  
RPC |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Intents) |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Intents)  
C++ |  [IntentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1IntentsClient.html) |  Not available   
C# |  [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClient) |  Not available   
Go |  [IntentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_IntentsClient) |  Not available   
Java |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.IntentsClient)  
Node.js |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.IntentsClient.html) |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.IntentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.intents.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.intents.IntentsClient)  
Ruby |  Not available  |  Not available   
  
Close

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * AGENT_ID: your agent ID
  * REGION_ID: your [region ID](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)
  * INTENT_ID: your intent ID
  * DISPLAY_NAME: your desired display name



HTTP method and URL: 
    
    
    PATCH https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents/INTENT_ID?updateMask=displayName

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents/INTENT_ID?updateMask=displayName"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents/INTENT_ID?updateMask=displayName" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents/INTENT_ID",
      "displayName": "DISPLAY_NAME",
      ...
    }
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dialogflow.cx.v3.[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Intent.html);
    import com.google.cloud.dialogflow.cx.v3.[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Intent.html).Builder;
    import com.google.cloud.dialogflow.cx.v3.[IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[UpdateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateIntentRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateIntent {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String agentId = "my-agent-id";
        String intentId = "my-intent-id";
        String location = "my-location";
        String displayName = "my-display-name";
        updateIntent(projectId, agentId, intentId, location, displayName);
      }
    
      // DialogFlow API Update Intent sample.
      public static void updateIntent(
          String projectId, String agentId, String intentId, String location, String displayName)
          throws IOException {
    
        // Note: close() needs to be called on the IntentsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentsClient.html) client = [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentsClient.html).create()) {
          String intentPath =
              "projects/"
                  + projectId
                  + "/locations/"
                  + location
                  + "/agents/"
                  + agentId
                  + "/intents/"
                  + intentId;
    
          Builder intentBuilder = client.getIntent(intentPath).toBuilder();
    
          intentBuilder.setDisplayName(displayName);
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("display_name").build();
    
          [Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Intent.html) intent = intentBuilder.build();
          [UpdateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateIntentRequest.html) request =
              [UpdateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateIntentRequest.html).newBuilder()
                  .setIntent(intent)
                  .setLanguageCode("en")
                  .setUpdateMask(fieldMask)
                  .build();
    
          // Make API request to update intent using fieldmask
          [Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Intent.html) response = client.updateIntent(request);
          System.out.println(response);
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {IntentsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    
    const intentClient = new [IntentsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    //TODO(developer): Uncomment these variables before running the sample.
    //  const projectId = 'your-project-id';
    //  const agentId = 'your-agent-id';
    //  const intentId = 'your-intent-id';
    //  const location = 'your-location';
    //  const displayName = 'your-display-name';
    
    async function updateIntent() {
      const agentPath = intentClient.projectPath(projectId);
      const intentPath = `${agentPath}/locations/${location}/agents/${agentId}/intents/${intentId}`;
    
      //Gets the intent from intentPath
      const intent = await intentClient.getIntent({name: intentPath});
      intent[0].displayName = displayName;
    
      //Specifies what is being updated
      const updateMask = {
        paths: ['display_name'],
      };
    
      const updateIntentRequest = {
        intent: intent[0],
        updateMask,
        languageCode: 'en',
      };
    
      //Send the request for update the intent.
      const result = await intentClient.updateIntent(updateIntentRequest);
      console.log(result);
    }
    
    updateIntent();
    

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.dialogflowcx_v3.services.intents import IntentsClient
    from google.protobuf import field_mask_pb2
    
    
    def update_intent(project_id, agent_id, intent_id, location, displayName):
        intents_client = IntentsClient()
    
        intent_name = intents_client.intent_path(project_id, location, agent_id, intent_id)
    
        intent = intents_client.get_intent(request={"name": intent_name})
    
        intent.display_name = displayName
        update_mask = field_mask_pb2.FieldMask(paths=["display_name"])
        response = intents_client.update_intent(intent=intent, update_mask=update_mask)
        return response
    
    

[ Previous arrow_back  Manage intents with the API  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/intent-manage-api)

[ Next List data with a filter  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/filter)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
