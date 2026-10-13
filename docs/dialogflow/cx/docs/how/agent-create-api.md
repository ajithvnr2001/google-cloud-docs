---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/agent-create-api/
title: Manage agents with the API \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:58.544545+00:00
---

# Manage agents with the API  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/agent-create-api/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Manage agents with the API Stay organized with collections  Save and categorize content based on your preferences. 

Normally, you create and delete agents using the console. However, in certain advanced scenarios, you may find it easier to use the API.

## Create an agent

The following examples show how to call the `Create` method for the `Agent` type. Go to the Agent API reference

**Select a protocol and version for the Agent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents) |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents)  
RPC |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Agents) |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Agents)  
C++ |  [AgentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1AgentsClient.html) |  Not available   
C# |  [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) |  Not available   
Go |  [AgentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient) |  Not available   
Java |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AgentsClient)  
Node.js |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.AgentsClient.html) |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.AgentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.agents.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)  
Ruby |  Not available  |  Not available   
  
Close

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * REGION_ID: your [region ID](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)



HTTP method and URL: 
    
    
    POST https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents

Request JSON body: 
    
    
    {
      "displayName": "My display name",
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
         "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents"

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
        -Uri "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID",
      "displayName": "My display name",
      "defaultLanguageCode": "en",
      "timeZone": "America/New_York",
      "startFlow": "projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID/flows/00000000-0000-0000-0000-000000000000",
      "advancedSettings": {
        "loggingSettings": {}
      }
    }
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dialogflow.cx.v3.[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent.html);
    import com.google.cloud.dialogflow.cx.v3.[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent.html).Builder;
    import com.google.cloud.dialogflow.cx.v3.[AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsSettings.html);
    import java.io.IOException;
    
    public class CreateAgent {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String displayName = "my-display-name";
    
        createAgent(projectId, displayName);
      }
    
      public static [Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent.html) createAgent(String parent, String displayName) throws IOException {
    
        String apiEndpoint = "global-dialogflow.googleapis.com:443";
    
        [AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsSettings.html) agentsSettings = [AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
        // Note: close() needs to be called on the AgentsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.html) client = [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.html).create(agentsSettings)) {
          // Set the details of the Agent to create
          Builder build = [Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent.html).newBuilder();
    
          build.[setDefaultLanguageCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent.Builder.html#com_google_cloud_dialogflow_cx_v3_Agent_Builder_setDefaultLanguageCode_java_lang_String_)("en");
          build.setDisplayName(displayName);
          // Correct format for timezone is location/city
          // For example America/Los_Angeles, Europe/Madrid, Asia/Tokyo
          build.setTimeZone("America/Los_Angeles");
    
          [Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent.html) agent = build.build();
          String parentPath = String.format("projects/%s/locations/%s", parent, "global");
    
          // Calls the create agent api and returns the created Agent
          [Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent.html) response = client.createAgent(parentPath, agent);
          System.out.println(response);
          return response;
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const parent = 'projects/' + projectId + '/locations/global';
    
    const api_endpoint = 'global-dialogflow.googleapis.com';
    
    const agent = {
      displayName: displayName,
      defaultLanguageCode: 'en',
      timeZone: 'America/Los_Angeles',
    };
    
    const {AgentsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    
    const client = new [AgentsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)({apiEndpoint: api_endpoint});
    
    async function setAgentSample() {
      const request = {
        agent,
        parent,
      };
    
      const [response] = await client.createAgent(request);
      console.log(`response: ${JSON.stringify(response, null, 2)}`);
    
      // Delete created agent resource
      client.deleteAgent({name: response.name});
    }
    await setAgentSample();

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.dialogflowcx_v3.services.agents.client import AgentsClient
    from google.cloud.dialogflowcx_v3.types.agent import Agent
    
    
    def create_agent(project_id, display_name):
        parent = "projects/" + project_id + "/locations/global"
    
        agents_client = AgentsClient()
    
        agent = Agent(
            display_name=display_name,
            default_language_code="en",
            time_zone="America/Los_Angeles",
        )
    
        response = agents_client.create_agent(request={"agent": agent, "parent": parent})
    
        return response
    
    

## Delete an agent

The following examples show how to call the `Delete` method for the `Agent` type. Go to the Agent API reference

**Select a protocol and version for the Agent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents) |  [Agent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents)  
RPC |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Agents) |  [Agent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Agents)  
C++ |  [AgentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1AgentsClient.html) |  Not available   
C# |  [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) |  Not available   
Go |  [AgentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient) |  Not available   
Java |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AgentsClient)  
Node.js |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.AgentsClient.html) |  [AgentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.AgentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.agents.AgentsClient) |  [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)  
Ruby |  Not available  |  Not available   
  
Close

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * REGION_ID: your [region ID](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)
  * AGENT_ID: your agent ID, found in the agent creation response



HTTP method and URL: 
    
    
    DELETE https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/agents/AGENT_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

[ Previous arrow_back  Implement webhooks  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/webhook)

[ Next Manage pages with the API  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/page-manage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
