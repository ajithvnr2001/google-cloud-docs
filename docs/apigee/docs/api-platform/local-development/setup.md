---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/setup/
title: Set up Apigee API Management in Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:33.436661+00:00
---

# Set up Apigee API Management in Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Set up Apigee API Management in Cloud Code for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page provides instructions for creating an Apigee API Management local development environment in [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode). See [ Overview of local development with Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview) for features in the local development environment. 

The setup process requires completion of both of these sections of this guide:

  * Before you begin
  * Install VS Code and the Cloud Code extension



Depending on your use cases, also complete Set up API proxy development for Apigee local development

## Before you begin

To set up and use Apigee in VS Code, you need:

  1. A Google Cloud project to log into in your local development environment. The project needs to be provisioned for Apigee to create an Apigee local workspace where you can develop and test API proxies.
  2. (Recommended) [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) provisioned on your project. API hub integration allows you to access and edit APIs across your ecosystem from within Cloud Code. API hub is also required for creation of a [ remote mock server](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis#use-remote-mock-server) for testing API specs.  
  
If you do not want to add API hub to your project, you could associate the project with another project that has API hub enabled instead. See [ Attach a runtime project to an API hub](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project) for information on attaching a project to an API hub.   
  
See the Required roles to use API hub with Apigee local development for actions you plan to perform. 
  3. Familiarity with VS Code, how to manage VS Code, and how to perform common actions such as accessing settings and installing extensions. See the [VS Code documentation](https://code.visualstudio.com/docs). 



### Required roles to use Apigee API hub with Apigee local development

You'll need the roles listed below to perform API design and testing steps using Apigee API hub APIs:

Task | Required Role(s)  
---|---  
[ View and edit API hub APIs](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis#update-your-api-hub-apis-from-cloud-code) | [Cloud API Hub Admin or Cloud API Hub Editor](https://docs.cloud.google.com/apigee/docs/apihub/iam-roles)  
[ Publish APIs to API hub](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis#publish-the-api-to-api-hub) | [Cloud API Hub Admin or Cloud API Hub Editor](https://docs.cloud.google.com/apigee/docs/apihub/iam-roles)  
Set up and manage a [ remote mock server](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis#use-remote-mock-server) to test APIs | Artifact Registry Administrator  
Cloud Build Service Account  
Cloud Run Admin  
Service Usage Admin  
  
See [ Identity and Access Management (IAM) basic and predefined roles reference](https://cloud.google.com/iam/docs/understanding-roles).  
  
You must also have the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) installed.  
  
## Install VS Code and the Cloud Code extension

This section provides the installation instructions for installing VS Code and the Cloud Code extension in VS Code. This is the first step in setting up local development for Apigee and is required to use any of the Apigee local development features

To install VS Code and the Cloud Code extension: 

  1. Download and install **[Visual Studio Code (VS Code)](https://code.visualstudio.com)** on your local machine, if it is not already installed.
  2. Install the Cloud Code extension, as described in [ Install the Cloud Code extension](https://docs.cloud.google.com/code/docs/vscode/install). If you plan to manage [ API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#howdoyoucreateanapiproxy) in your local environment, install Docker as part of the process.
  3. (Recommended) Enable automatic updates for the Cloud Code extension. In **Settings** , search for **Extensions: Auto Update** and enable it for all extensions or for the Cloud Code extension individually.
  4. Restart VS Code.



## Set up API proxy development for Apigee local development

Complete the steps in this section if you want to use your local development environment for Apigee API proxy development and testing. Also complete these steps to be able to create an API proxy from an OpenAPI spec.

  1. [ Create an Apigee workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#creating_an_apigee_workspace).
  2. [ Install the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#install).
  3. [ Add a container](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#adding_a_container_for_the_apigee_emulator) for deploying to the Apigee Emulator.



## What's next

After completing the installation and setup steps, get started using Cloud Code:

  * [ Access and explore API Management in Cloud Code](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/explore)
  * [ Build and deploy your first API proxy in local development](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/get-started)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
