---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/long-running-operation/
title: Long-running operations \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:41.976876+00:00
---

# Long-running operations  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/long-running-operation/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

Some methods of the Dialogflow CX API return a long-running operation. These methods are asynchronous, and the operation may not be completed when the method returns a response. You can check on the status, wait for completion, or cancel operations.

## Wait for an operation to complete

The following shows how to wait for an operation to complete.

### REST

To poll an operation's status, call the `get` method for the [`Operations`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations) resource. When the operation has completed, the `done` field is set to true.

**Note:** If you have many operations to check, you should rate limit your calls or use the `list` method instead.

Before using any of the request data, make the following replacements: 

  * REGION_ID: your [region ID](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)
  * PROJECT_ID: your Google Cloud project ID
  * OPERATION_ID: your operation ID



HTTP method and URL: 
    
    
    GET https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://REGION_ID-dialogflow.googleapis.com/v3/projects/PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.dialogflow.v3.SomeOperationType",
        "state": "DONE"
      },
      "done": true,
      ...
    }
    

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.dialogflow.cx.v3.[AgentName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentName.html);
    import com.google.cloud.dialogflow.cx.v3.[AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.html);
    import com.google.cloud.dialogflow.cx.v3.[AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsSettings.html);
    import com.google.cloud.dialogflow.cx.v3.[ExportAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[ExportAgentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentResponse.html);
    import com.google.protobuf.[Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class ExportAgent {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String agentId = "my-agent-id";
        String location = "my-location";
    
        exportAgent(projectId, agentId, location);
      }
    
      public static void exportAgent(String projectId, String agentId, String location)
          throws IOException, InterruptedException, ExecutionException {
    
        // Sets the api endpoint to specified location
        String apiEndpoint = String.format("%s-dialogflow.googleapis.com:443", location);
    
        [AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsSettings.html) agentsSettings = [AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
        // Note: close() needs to be called on the AgentsClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.html) agentsClient = [AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.html).create(agentsSettings)) {
          [ExportAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentRequest.html) request =
              [ExportAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentRequest.html).newBuilder()
                  .setName([AgentName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentName.html).of(projectId, location, agentId).toString())
                  .build();
    
          // Returns a future of the operation
          OperationFuture<ExportAgentResponse, Struct> future =
              agentsClient.[exportAgentOperationCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.html#com_google_cloud_dialogflow_cx_v3_AgentsClient_exportAgentOperationCallable__)().futureCall(request);
    
          // get the export agent response after the operation is completed
          [ExportAgentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentResponse.html) response = future.get();
          System.out.println(response);
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {AgentsClient, protos} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)');
    
    const api_endpoint = `${location}-dialogflow.googleapis.com`;
    
    const client = new [AgentsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)({apiEndpoint: api_endpoint});
    
    const exportAgentRequest =
      new protos.google.cloud.dialogflow.cx.v3.[ExportAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.exportagentrequest-class.html)();
    
    exportAgentRequest.name = `projects/${projectId}/locations/${location}/agents/${agentId}`;
    
    // exportAgent call returns a promise to a long running operation
    const [operation] = await client.exportAgent(exportAgentRequest);
    
    // Waiting for the long running opporation to finish
    const [response] = await operation.promise();
    
    // Prints the result of the operation when the operation is done
    console.log(response);
    

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.dialogflowcx_v3.services.agents.client import AgentsClient
    from google.cloud.dialogflowcx_v3.types.agent import ExportAgentRequest
    
    
    def export_long_running_agent(project_id, agent_id, location):
        api_endpoint = f"{location}-dialogflow.googleapis.com:443"
        client_options = {"api_endpoint": api_endpoint}
    
        agents_client = AgentsClient(client_options=client_options)
    
        export_request = ExportAgentRequest()
    
        export_request.name = (
            f"projects/{project_id}/locations/{location}/agents/{agent_id}"
        )
    
        # export_agent returns a long running operation
        operation = agents_client.export_agent(request=export_request)
    
        # Returns the result of the operation when the operation is done
        return operation.result()
    
    

[ Previous arrow_back  List data with a filter  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/filter)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
