---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/page-manage/
title: Manage pages with the API \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:58.449581+00:00
---

# Manage pages with the API  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/page-manage/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Manage pages with the API Stay organized with collections  Save and categorize content based on your preferences. 

In most cases, you will use the console to manage pages. In advanced scenarios, you may wish to use the API to manage pages. This guide describes how to create, list, and delete pages using the API.

## Create page

To create a page for your agent, call the `create` method on the `Page` type. Go to the Page API reference

**Select a protocol and version for the Page reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Page resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages) |  [Page resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.pages)  
RPC |  [Page interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Pages) |  [Page interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Pages)  
C++ |  [PagesClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1PagesClient.html) |  Not available   
C# |  [PagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClient) |  Not available   
Go |  [PagesClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_PagesClient) |  Not available   
Java |  [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient) |  [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.PagesClient)  
Node.js |  [PagesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.PagesClient.html) |  [PagesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.PagesClient.html)  
PHP |  Not available  |  Not available   
Python |  [PagesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.pages.PagesClient) |  [PagesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.pages.PagesClient)  
Ruby |  Not available  |  Not available   
  
Close

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dialogflow.cx.v3.[CreatePageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePageRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Page.html);
    import com.google.cloud.dialogflow.cx.v3.[PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html);
    import java.io.IOException;
    
    public class CreateSimplePage {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String agentId = "my-agent-id";
        String flowId = "my-flow-id";
        String location = "my-location";
        String displayName = "my-display-name";
    
        createPage(projectId, agentId, flowId, location, displayName);
      }
    
      // DialogFlow API Create Page Sample.
      // Creates a page from the provided parameters
      public static [Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Page.html) createPage(
          String projectId, String agentId, String flowId, String location, String displayName)
          throws IOException {
        [Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Page.html) response;
        [CreatePageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePageRequest.html).Builder createRequestBuilder = [CreatePageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePageRequest.html).newBuilder();
        [Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Page.html).Builder pageBuilder = [Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Page.html).newBuilder();
    
        pageBuilder.setDisplayName(displayName);
    
        createRequestBuilder
            .setParent(
                "projects/"
                    + projectId
                    + "/locations/"
                    + location
                    + "/agents/"
                    + agentId
                    + "/flows/"
                    + flowId)
            .setPage(pageBuilder);
    
        // Make API request to create page
        // Note: close() needs to be called on the PagesClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html) client = [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html).create()) {
          response = client.createPage(createRequestBuilder.build());
          System.out.println("Successfully created page!");
          return response;
        }
      }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function createPage(projectId, agentId, flowId, location, displayName) {
      const pagesClient = new PagesClient();
    
      const createPageRequest = {
        parent: `projects/${projectId}/locations/${location}/agents/${agentId}/flows/${flowId}`,
        page: {
          displayName: displayName,
        },
      };
    
      const response = await pagesClient.createPage(createPageRequest);
      console.log(response);
    }

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async def create_page(project_id, agent_id, flow_id, location, displayName):
        pages_client = PagesAsyncClient()
    
        page = Page()
        page.display_name = displayName
    
        request = CreatePageRequest()
        request.parent = (
            "projects/"
            + project_id
            + "/locations/"
            + location
            + "/agents/"
            + agent_id
            + "/flows/"
            + flow_id
        )
        request.page = page
    
        response = await pages_client.create_page(request=request)
        return response
    
    

## List pages

To list the pages for your agent, call the `list` method on the `Page` type. Go to the Page API reference

**Select a protocol and version for the Page reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Page resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages) |  [Page resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.pages)  
RPC |  [Page interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Pages) |  [Page interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Pages)  
C++ |  [PagesClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1PagesClient.html) |  Not available   
C# |  [PagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClient) |  Not available   
Go |  [PagesClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_PagesClient) |  Not available   
Java |  [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient) |  [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.PagesClient)  
Node.js |  [PagesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.PagesClient.html) |  [PagesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.PagesClient.html)  
PHP |  Not available  |  Not available   
Python |  [PagesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.pages.PagesClient) |  [PagesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.pages.PagesClient)  
Ruby |  Not available  |  Not available   
  
Close

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dialogflow.cx.v3.[ListPagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPagesRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[ListPagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPagesRequest.html).Builder;
    import com.google.cloud.dialogflow.cx.v3.[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Page.html);
    import com.google.cloud.dialogflow.cx.v3.[PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html);
    import java.io.IOException;
    
    public class ListPages {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String agentId = "my-agent-id";
        String flowId = "my-flow-id";
        String location = "my-location";
    
        listPages(projectId, agentId, flowId, location);
      }
    
      // DialogFlow API List Pages Sample.
      // Lists all pages from the provided parameters
      public static void listPages(String projectId, String agentId, String flowId, String location)
          throws IOException {
        // Note: close() needs to be called on the PagesClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html) client = [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html).create()) {
          Builder listRequestBuilder = [ListPagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPagesRequest.html).newBuilder();
    
          String parentPath =
              String.format(
                  "projects/%s/locations/%s/agents/%s/flows/%s", projectId, location, agentId, flowId);
          listRequestBuilder.setParent(parentPath);
          listRequestBuilder.setLanguageCode("en");
    
          // Make API request to list all pages in the project
          for ([Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Page.html) element : client.listPages(listRequestBuilder.build()).iterateAll()) {
            System.out.println(element);
          }
        }
      }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function listPages(projectId, agentId, flowId, location) {
      const pagesClient = new PagesClient();
      const listPageRequest = {
        parent: `projects/${projectId}/locations/${location}/agents/${agentId}/flows/${flowId}`,
        languageCode: 'en',
      };
    
      const response = await pagesClient.listPages(listPageRequest);
      console.log(response);
    }

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async def list_page(project_id, agent_id, flow_id, location):
        pages_client = PagesAsyncClient()
    
        request = ListPagesRequest()
        request.parent = (
            f"projects/{project_id}/locations/{location}/agents/{agent_id}/flows/{flow_id}"
        )
    
        request.language_code = "en"
    
        response = await pages_client.list_pages(request=request)
        return response
    
    

## Delete pages

To delete a page for your agent, call the `delete` method on the `Page` type. Go to the Page API reference

**Select a protocol and version for the Page reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Page resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages) |  [Page resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.pages)  
RPC |  [Page interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Pages) |  [Page interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Pages)  
C++ |  [PagesClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1PagesClient.html) |  Not available   
C# |  [PagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClient) |  Not available   
Go |  [PagesClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_PagesClient) |  Not available   
Java |  [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient) |  [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.PagesClient)  
Node.js |  [PagesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.PagesClient.html) |  [PagesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.PagesClient.html)  
PHP |  Not available  |  Not available   
Python |  [PagesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.pages.PagesClient) |  [PagesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.pages.PagesClient)  
Ruby |  Not available  |  Not available   
  
Close

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dialogflow.cx.v3.[DeletePageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePageRequest.html);
    import com.google.cloud.dialogflow.cx.v3.[DeletePageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePageRequest.html).Builder;
    import com.google.cloud.dialogflow.cx.v3.[PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html);
    import java.io.IOException;
    
    public class DeletePage {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String agentId = "my-agent-id";
        String flowId = "my-flow-id";
        String pageId = "my-page-id";
        String location = "my-location";
    
        deletePage(projectId, agentId, flowId, pageId, location);
      }
    
      // DialogFlow API Delete Page Sample.
      // Deletes a page from the provided parameters
      public static void deletePage(
          String projectId, String agentId, String flowId, String pageId, String location)
          throws IOException {
    
        // Note: close() needs to be called on the PagesClient object to clean up resources
        // such as threads. In the example below, try-with-resources is used,
        // which automatically calls close().
        try ([PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html) client = [PagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PagesClient.html).create()) {
          Builder deleteRequestBuilder = [DeletePageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePageRequest.html).newBuilder();
    
          deleteRequestBuilder.setName(
              "projects/"
                  + projectId
                  + "/locations/"
                  + location
                  + "/agents/"
                  + agentId
                  + "/flows/"
                  + flowId
                  + "/pages/"
                  + pageId);
    
          // Make API request to delete page
          client.deletePage(deleteRequestBuilder.build());
          System.out.println("Successfully deleted page!");
        }
      }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function deletePage(projectId, agentId, flowId, pageId, location) {
      const pagesClient = new PagesClient();
    
      const req = {
        name: `projects/${projectId}/locations/${location}/agents/${agentId}/flows/${flowId}/pages/${pageId}`,
      };
    
      const response = await pagesClient.deletePage(req);
      console.log(response);
    }

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async def delete_page(project_id, agent_id, flow_id, page_id, location):
        pages_client = PagesAsyncClient()
    
        request = DeletePageRequest()
        request.name = f"projects/{project_id}/locations/{location}/agents/{agent_id}/flows/{flow_id}/pages/{page_id}"
    
        response = await pages_client.delete_page(request=request)
        return response
    
    

[ Previous arrow_back  Manage agents with the API  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/agent-create-api)

[ Next Manage intents with the API  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/intent-manage-api)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
