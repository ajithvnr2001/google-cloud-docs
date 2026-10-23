---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis/
title: Design and edit APIs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:01.424432+00:00
---

# Design and edit APIs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Design and edit APIs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page provides instructions on how to design and edit APIs in Apigee in Cloud Code.

## Before you begin

Before using the functionality in this guide, ensure you have completed the setup steps for [Setting up Apigee API Management in Cloud Code for VS Code](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/setup), including making sure your user account has the required roles listed in [ Required roles to use Apigee API hub with Apigee local development](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/setup#required-roles-to-use-apigee-api-hub-with-apigee-local-development). 

## Design APIs

You can add and edit Apigee API proxies and API hub APIs directly in Cloud Code.

  * Create an Apigee API proxy by following the steps in [ Create an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-create-proxy).
  * Create an API hub API by clicking the plus icon in the row for your API hub host. This opens a spec editing window and Swagger panel for the new API spec and allows you to publish the API to your API hub.

**Tip:** You can also use Gemini Code Assist chat to create an [ OpenAPI specification](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md) and then copy it for use in Apigee. For information, see [Code with Gemini Code Assist Standard and Enterprise](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini). After setup, enter a prompt like  
  
`Create an OpenAPI spec for an API that lets customers schedule appointments with a dental office.`  
  
Specs generated in this way do not incorporate enterprise context from your API hub. 

## Edit APIs

You can edit APIs you've saved locally or from your [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) catalog. Changes you make in Cloud Code can be  published to API hub or saved as an Apigee API proxy bundle. 

Regardless of the method you use to edit an API, you can manually update the spec, or use Gemini Code Assist Chat (if enabled) to iterate on the spec. Note that when using Gemini Code Assist Chat to iterate on the spec, Gemini Code Assist suggestions do not include enterprise context from your API hub.

### Edit an API spec from API hub

To edit an API spec that is stored in your API hub catalog, follow the instructions in this section. In order to integrate with API hub, your Apigee project must be provisioned with API hub. See Before you begin. 

  1. Make sure that the project you've selected in Cloud Code is the project with the API hub catalog containing the API you want to edit.
  2. In the left nav, expand the **API Hub** tree in the Apigee section.
  3. Select the API and version to edit from the list. You'll see the YAML file and the Swagger panel view for the API.



### Edit an API spec that is stored locally

To edit an API spec that is stored locally, open the file in Cloud Code.

If you've created an Apigee proxy bundle from the spec, you can open the proxy bundle file in Cloud Code by clicking the API proxy name under **apiproxies** in your Apigee workspace.

## Save APIs as API proxy bundles

You can save your API as an Apigee API proxy bundle so that you can work on it within your Apigee local development environment. For information on working with API proxies in Cloud Code, see [ Develop API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies). 

  1. Click **Create API proxy bundle** in the Swagger panel.
  2. In the prompt field, name your API proxy and continue.
  3. Your API proxy appears in the Apigee left menu in your local workspace, under **apiproxies**.



## Publish APIs to API hub

If you are using [API hub](https://docs.cloud.google.com/apigee/docs/api-hub/what-is-api-hub), you can make your APIs available to other developers by registering them with API hub: 

  1. In the Swagger panel for a new or edited API spec, click **Publish to API hub**.
  2. In the form, provide metadata for the API to improve its discoverability and organization of APIs within your API hub catalog. Most fields are autopopulated from the API spec, but you can change the values. See [Register an API](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-api#register-an-api) for information on registering with API hub and the information you need to provide. 
     * **API Display Name** (Required): A name of the API, visible to other developers. 
     * **API Description** (Optional): A description of the API for internal/developer reference.
     * **API Owner Name** (Optional): The name of the API owner.
     * **API Owner Email** (Optional): The owner's email address.
     * **API Version** (Required): The API version.
     * **Lifecycle Stage** (Optional): Select a stage from the list.
  3. Click **Publish** to publish the API to API hub.
  4. After a short delay, your changes should be visible in the **API Hub** tree in the Apigee section of Cloud Code. 



## Test APIs using a mock server

You can test your API using either a local mock server or a Google Cloud-based remote mock server. The local mock server is installed and available by default while you must set up and manage Google Cloud mock servers.

### Use the local mock server

The local mock server accepts requests to this API and emulates responses. It is usable only during the current session by the current user. However, unlike the remote mock server, it requires no setup or management and incurs no costs.

Also, local mock servers:

  * Do not work when using [Cloud Shell Editor](https://cloud.google.com/shell/docs/editor-overview) or [Cloud Workstations](https://cloud.google.com/workstations?e=48754805). 
  * Might not work correctly when using VS Code Remote Explorer. 



To use the local mock server:

  1. Select the local mock server in the **Servers** dropdown (if not already selected):  
![Cloud Code Gemini Code Assist local mock server in dropdown](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/cloudcode_mockserver_local.png)
  2. Open a path in the Swagger panel and click **Try it out**.  
![Cloud Code Gemini Code Assist prompt navigation](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/cloudcode_mockserver_tryitout.png)
  3. Fill out any request parameters and click **Execute**.  
![Cloud Code Gemini Code Assist prompt navigation](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/cloudcode_mockserver_execute.png)



### Use a remote mock server

A remote mock server provides the ability to create a persistent mock server instance that, unlike the local mock server, can be shared with and used by others within your organization to test the new API. Remote mock servers can only be used with APIs that are registered in API hub.

Remote mock servers do not automatically update for any changes you make to the API after deploying the mock server, so wait to add the mock server until you have fully created the API.

Deploying a Google Cloud remote mock server creates a new Cloud Run service. It builds a container image for the mock server using Cloud Build and uploads the container image to Cloud Artifact Registry in your Google project. See [What is Cloud Run?](https://cloud.google.com/run/docs/overview/what-is-cloud-run), [Managing Services](https://cloud.google.com/run/docs/managing/services), and the [Artifact Registry documentation](https://cloud.google.com/artifact-registry/docs).

You can either use the default service account or provide a more restricted service account to deploy the Cloud Run application to. See [Manage Cloud APIs and Cloud Client Libraries in Cloud Code for VS Code](https://cloud.google.com/code/docs/vscode/client-libraries#cloud-run_1) for information.

**Important:** You are responsible for any resulting costs and maintenance on the remote mock server after creation. You are also responsible for deleting it once it is no longer needed or in use. See [Cloud Run Pricing](https://cloud.google.com/run/pricing) for pricing information, including information on any free tier options.

To deploy a remote mock server:

  1. Select **Deploy mock server** from the Swagger panel.
  2. If your API is not already registered in API hub, register it when prompted.
  3. Specify details for the remote mock server: **Server Name** , **Secure Server** , **Service Account** (leave empty to use the default service account), and whether to add the server URL to the API spec. Click **Create** to create the remote mock server. **Important:** Do not create multiple remote mock servers with the same name, even though the user interface will not prevent you from doing so at this time.
  4. Remote mock server generation requires several minutes. You can watch the progress in the Cloud Code **OUTPUT** panel and through the notification pop up in the bottom right corner of their VS Code.
  5. Once the remote mock server creation process is complete, you'll see the remote server URL in the Swagger panel server list and the **OUTPUT** panel.
  6. To use the mock server, open a path and click **Try it out**.  
![Cloud Code Gemini Code Assist prompt navigation](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/cloudcode_mockserver_tryitout.png)  
  
Fill out any request parameters and click **Execute**.  
![Cloud Code Gemini Code Assist prompt navigation](https://docs.cloud.google.com/static/apigee/docs/api-platform/local-development/vscode/images/cloudcode_mockserver_execute.png)  
  
You can also submit requests using `curl` from a prompt. Use the server address and port from the **Servers** dropdown. 



To share access to the mock server with other users:

  1. Give other users the invoker role for the deployed service. See [Authenticate developers](https://cloud.google.com/run/docs/authenticating/developers).
  2. When making the request to the mock server, users follow the instructions in [Test your private service](https://cloud.google.com/run/docs/authenticating/developers#testing).



To manage deployed remote mock servers:

  1. Go to [ Apigee API hub](https://console.cloud.google.com/apigee/api-hub/).
  2. Find the API to see all the deployments for the API, which includes any remote mock servers.
  3. Use the **Resource URL** to go the deployment and manage it by stopping, deleting, and performing other actions on the mock server.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
