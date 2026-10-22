---
url: https://docs.cloud.google.com/application-design-center/docs/design-deploy-antigravity-cli/
title: Design and deploy an application using Antigravity CLI \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:56.505864+00:00
---

# Design and deploy an application using Antigravity CLI  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/design-deploy-antigravity-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Design and deploy an application using Antigravity CLI Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Integrating Gemini Cloud Assist with third-party tools using MCP is in private preview. To request access, contact your Google Cloud account team.   
  
Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805).

Use the Gemini Cloud Assist and Application Design Center Model Context Protocol (MCP) servers to design, deploy, and troubleshoot Google Cloud infrastructure directly in the [Antigravity CLI](https://antigravity.google/docs/cli/overview).

## Objectives

This tutorial helps you do the following:

  * Set up the Antigravity CLI to use Gemini Cloud Assist and App Design Center MCP servers.
  * Design and deploy Google Cloud infrastructure that is optimized to run your existing application code.
  * Analyze and troubleshoot technical issues.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [App Design Center.](https://cloud.google.com/products/application-design-center/pricing)
  * Google Cloud resources that you create as part of your application infrastructure.



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. To access Gemini Cloud Assist through MCP, you must be in the Trusted Tester program. Reach out to your account team to request access.
  13. Install the [Antigravity CLI](https://antigravity.google/docs/cli/install)
  14. To deploy and run Antigravity CLI commands, ask your administrator to grant you the necessary roles inside your project boundary, as listed in the following table: Task | Required roles  
---|---  
Set up App Design Center in your project | Application Design Center Admin (`roles/designcenter.admin`)  
Access and call Gemini Cloud Assist through MCP | Gemini Cloud Assist Admin (`roles/geminicloudassist.admin`), or  
Gemini Cloud Assist Editor (`roles/geminicloudassist.editor`), or  
Gemini Cloud Assist User (`roles/geminicloudassist.user`)  



## Prepare the environment

To prepare your environment, authenticate to Google Cloud and enable required services.

### Authenticate to Google Cloud

Authenticate to Google Cloud by running the following command in your terminal:

  1. Set up Application Default Credentials to let the MCP servers make API calls.
         
         gcloud auth application-default login
         




### Enable APIs

Enable the Gemini Cloud Assist and Application Design Center services in your project.

  1. Enable the Gemini Cloud Assist service in your project:
         
         gcloud services enable geminicloudassist.googleapis.com
         

  2. Enable the App Design Center service in your project:
         
         gcloud services enable designcenter.googleapis.com
         




### Configure the MCP servers

The Gemini Cloud Assist and App Design Center MCP servers help you design, assess, deploy, and troubleshoot Google Cloud infrastructure using natural language prompts. To connect to the MCP servers, configure your Antigravity settings.

To configure Antigravity CLI to use MCP servers, do the following:

  1. Open your MCP configuration file in one of the following locations:

     * _User scope_ : To apply settings across all of your Antigravity CLI projects, open `~/.gemini/config/mcp_config.json`.
     * _Workspace scope_ : To apply settings for a specific Antigravity CLI project, open `.agents/mcp_config.json`.

If your configuration file doesn't exist, create a new file.

  2. In `mcp_config.json`, add or merge the following configuration block under the `mcpServers` key.
         
         {
             "mcpServers": {
               "gemini-cloud-assist": {
                 "serverUrl": "https://geminicloudassist.googleapis.com/mcp",
                 "authProviderType": "google_credentials"
               },
               "application-design-center": {
                 "serverUrl": "https://designcenter.googleapis.com/mcp",
                 "authProviderType": "google_credentials"
               }
             }
           }
         

This configuration automatically uses your Application Default Credentials.

  3. Save and close your configuration file.

  4. Start the Antigravity CLI.
         
         agy
         

  5. Verify that the MCP servers are connected.
         
         /mcp list
         




### Install `SKILL.md` files

`SKILL.md` files provide the App Design Center and Gemini Cloud Assist MCP servers instructions and workflows for infrastructure design, deployment, and troubleshooting.

To add `SKILL.md` files to Antigravity CLI, do the following:

  1. Create a `skills/design-and-deploy` directory in one of the following locations:

     * _User scope_ : To apply settings across all of your Antigravity CLI projects, create `~/.gemini/config/skills/design-and-deploy/`.
     * _Workspace scope_ : To apply settings for a specific Antigravity CLI project, create `.agents/skills/design-and-deploy/`.
  2. In the `skills/design-and-deploy/` directory, create a `SKILL.md` file using the content from [designing-and-deploying-infrastructure](https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp/blob/main/skills/designing-and-deploying-infrastructure/SKILL.md?plain=1).

  3. Create a `skills/google-gemini-cloud-assist` directory in one of the following locations:

     * _User scope_ : To apply settings across all of your Antigravity CLI projects, create `~/.gemini/config/skills/google-gemini-cloud-assist/`.
     * _Workspace scope_ : To apply settings for a specific Antigravity CLI project, create `.agents/skills/google-gemini-cloud-assist/`.
  4. In the `skills/google-gemini-cloud-assist/` directory, create a `SKILL.md` file using the content from [operating-google-cloud](https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp/blob/main/skills/operating-google-cloud/SKILL.md?plain=1).

  5. Exit and restart the Antigravity CLI session.
         
         /quit
         

When you start the Antigravity CLI again with `agy`, it automatically discovers your skill files.

  6. Verify that the skill files were automatically discovered.
         
         /skills list
         




You successfully configured Antigravity CLI to connect to the App Design Center and Gemini Cloud Assist MCP servers and created skill files.

## Design your Google Cloud infrastructure

Design infrastructure tailored to store and execute your application code.

  1. Set the project that you want to use:
         
         gcloud config set project PROJECT_ID
         

  2. Ask for the Google Cloud infrastructure design.
         
         My application code is in REPOSITORY_URL. Design the Google Cloud infrastructure required for my application.
         

The agent asks to activate the skills you configured. The agent creates an infrastructure design plan and asks for your approval.

  3. Approve the plan.
         
         Continue with the plan.
         

The agent identifies tools to use to create the infrastructure, The agent asks to use the `setup_adc` tool, which sets up App Design Center in your project.

  4. Allow Gemini Cloud Assist to use the proposed tools.

The agent proposes a design and asks if you're ready to deploy.

  5. Iterate on the proposed design.
         
         The infrastructure looks good, but I want to add a cache for frequently accessed data.
         

The agent updates the design to integrate your requirement. The agent asks if you want an explanation of the changes, or if you want to test the changes.




You created your initial infrastructure design, and iterated to improve the design.

## Assess compliance with security standards

Administrators in your organization have likely configured specific security frameworks that inform infrastructure design and deployment. In this section, verify that your design is compliant with configured security standards.

  1. Make sure that the infrastructure design is compliant with your organization's security standards.
         
         I want to make sure that infrastructure design is compliant with my organization's security standards.
         

The agent analyzes the infrastructure design based on the security frameworks your organization's administrator has specified in Security Command Center. If the audit finds compliance issues, the agent suggest security enhancements and asks for your approval.

  2. Apply the recommended security enhancements
         
         Apply the recommended security enhancements.
         

The agent applies the changes and asks if you're ready to approve the design.




Your infrastructure design is compliant with your organization's security frameworks.

## Deploy the infrastructure design

Deploy the infrastructure design to Google Cloud.

  1. Approve the design and deploy.
         
         Deploy the infrastructure design to my Google Cloud project.
         

The agent deploys the final design to your Google Cloud project. The agent asks you to approve changes to your project. For example, you might need to enable an API.

If the application successfully deploys, The agent displays deployment details, architecture components, and steps to use the application.

  2. If your deployment fails, get help with troubleshooting. For example, you might need to fix component configuration details or Identity and Access Management (IAM) permissions.
         
         Fix the component configuration errors.
         

The agent provides recommendations for component configurations and creates a diff view for you to review and accept.

  3. To try the deployment again after you make changes, repeat the steps in this section.




You deployed your application code and the infrastructure design to Google Cloud.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * Learn to [monitor application health and performance](https://docs.cloud.google.com/application-design-center/docs/monitor-applications).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
