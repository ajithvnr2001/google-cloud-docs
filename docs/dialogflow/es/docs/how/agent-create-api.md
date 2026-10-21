---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/agent-create-api/
title: Manage agents with the API \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:47.314086+00:00
---

# Manage agents with the API  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/agent-create-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Manage agents with the API Stay organized with collections  Save and categorize content based on your preferences. 

Normally, you create and delete agents using the console. However, in certain advanced scenarios, you may find it easier to use the API.

**Note:** You must have a [role with full or edit access](https://docs.cloud.google.com/dialogflow/es/docs/access-control#roles) in order to create or delete an agent.

## Create an agent

The following examples show how to call the `SetAgent` method for the [Agent](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#agents) type. These examples are creating agents, but the same methods can be used to update agent settings, like agent edition.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent

Request JSON body: 
    
    
    {
      "displayName": "My-display-name",
      "defaultLanguageCode": "en",
      "timeZone": "America/New_York"
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "parent": "projects/PROJECT_ID",
      "displayName": "My display name",
      "defaultLanguageCode": "en",
      "timeZone": "America/New_York",
      "apiVersion": "API_VERSION_V2"
    }
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dialogflow.v2.[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Agent.html);
    import com.google.cloud.dialogflow.v2.[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Agent.html).Builder;
    import com.google.cloud.dialogflow.v2.[AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AgentsClient.html);
    import com.google.cloud.dialogflow.v2.[AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AgentsSettings.html);
    import java.io.IOException;
    
    public class SetAgent {
    
      public static void main(String[] args) throws IOException {
        String projectId = "my-project-id";
    
        // The display name will set the name of your agent
        String displayName = "my-display-name";
    
        setAgent(projectId, displayName);
      }
    
      public static [Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Agent.html) setAgent(String parent, String displayName) throws IOException {
    
        [AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AgentsSettings.html) agentsSettings = [AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AgentsSettings.html).newBuilder().build();
        try ([AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AgentsClient.html) client = [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AgentsClient.html).create(agentsSettings)) {
          // Set the details of the Agent to create
          Builder build = [Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Agent.html).newBuilder();
    
          build.[setDefaultLanguageCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Agent.Builder.html#com_google_cloud_dialogflow_v2_Agent_Builder_setDefaultLanguageCode_java_lang_String_)("en");
          build.setDisplayName(displayName);
    
          [Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Agent.html) agent = build.build();
    
          // Make API request to create agent
          [Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Agent.html) response = client.setAgent(agent);
          System.out.println(response);
          return response;
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {AgentsClient} = require('[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)');
    
    // make sure to pass projectID as the input parameter
    const parent = 'projects/' + parentId + '/locations/global';
    
    const agent = {
      parent: parent,
      displayName: displayName,
      defaultLanguageCode: 'en',
      timeZone: 'America/Los_Angeles',
    };
    
    const client = new [AgentsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
    async function setAgent() {
      const request = {
        agent,
      };
    
      const [response] = await client.setAgent(request);
      console.log(`response: ${JSON.stringify(response, null, 2)}`);
    }
    await setAgent();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.dialogflow_v2 import Agent, AgentsClient, [SetAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SetAgentRequest.html)
    import google.protobuf.field_mask_pb2
    
    
    def set_agent(project_id, display_name):
        agents_client = AgentsClient()
    
        parent = agents_client.[common_project_path](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.agents.AgentsClient.html#google_cloud_dialogflow_v2_services_agents_AgentsClient_common_project_path)(project_id)
    
        agent = Agent(
            parent=parent,
            display_name=display_name,
            default_language_code="en",
            time_zone="America/Los_Angeles",
        )
    
        update_mask = google.protobuf.field_mask_pb2.FieldMask()
        update_mask.FromJsonString("displayName,defaultLanguageCode,timeZone")
    
        request = SetAgentRequest(
            agent=agent,
            update_mask=update_mask,
        )
    
        return agents_client.[set_agent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.agents.AgentsClient.html#google_cloud_dialogflow_v2_services_agents_AgentsClient_set_agent)(request=request)
    
    

## Delete an agent

The following examples show how to call the `DeleteAgent` method for the [Agent](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#agents) type.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID



HTTP method and URL: 
    
    
    DELETE https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/agent" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

[ Previous arrow_back  Data application levels  ](https://docs.cloud.google.com/dialogflow/es/docs/data-level)

[ Next Manage intents with the API  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/how/manage-intents)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
