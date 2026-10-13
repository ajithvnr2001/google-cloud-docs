---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/intent-manage-api/
title: Manage intents with the API \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:57.125454+00:00
---

# Manage intents with the API  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/intent-manage-api/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Manage intents with the API Stay organized with collections  Save and categorize content based on your preferences. 

Normally, you create and delete intents using the console. However, in certain advanced scenarios, you may find it easier to use the API.

## Create an intent

The following examples show how to call the `Create` method for the `Intent` type. Go to the Intent API reference

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
  * REGION_ID: your [region ID](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)
  * AGENT_ID: your agent ID



HTTP method and URL: 
    
    
    POST https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents

Request JSON body: 
    
    
    {
      "displayName": "My intent display name"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents/INTENT_ID",
      "displayName": "My intent display name",
      "priority": 500000
    }
    

## Update an intent

The [field mask guide](https://docs.cloud.google.com/dialogflow/cx/docs/how/field-mask) shows how to update individual fields of an intent.

## Delete an intent

The following examples show how to call the `Delete` method for the `Intent` type. Go to the Intent API reference

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
  * REGION_ID: your [region ID](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)
  * AGENT_ID: your agent ID
  * INTENT_ID: your intent ID, found in the create response



HTTP method and URL: 
    
    
    DELETE https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents/INTENT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents/INTENT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/intents/INTENT_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

[ Previous arrow_back  Manage pages with the API  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/page-manage)

[ Next Update data with a FieldMask  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/field-mask)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
