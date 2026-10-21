---
url: https://docs.cloud.google.com/workflows/docs/create-workflow-console/
title: Quickstart: Create a workflow by using the Google Cloud console \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:13.102232+00:00
---

# Quickstart: Create a workflow by using the Google Cloud console  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/create-workflow-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a workflow by using the Google Cloud console

Workflows lets you orchestrate and automate Google Cloud services and external APIs. In this quickstart, you create, deploy, and execute a workflow by using the Google Cloud console. The sample workflow sends a request to a public API and returns the response.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=workflows--workflows_quickstart)

* * *

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Workflows API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Workflows API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com)

  10. Set up authentication: 
     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Logging > Logs Writer** role to the service account. 

To grant the role, find the **Select a role** list, then select **Logging > Logs Writer**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

To learn more about service account roles and permissions, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Workflows Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.admin) (`roles/workflows.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create and deploy a workflow

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, click add**Create**.

  3. Enter a name for the new workflow, such as `myFirstWorkflow`.

  4. Choose **us-central1** for the region.

  5. For **service account** , select the service account you created earlier.

  6. Select **Next**.

  7. In the workflow editor, copy and paste the following workflow: 

### YAML
         
         main:
           params: [input]
           steps:
             - checkSearchTermInInput:
                 switch:
                   - condition: '${"searchTerm" in input}'
                     assign:
                       - searchTerm: '${input.searchTerm}'
                     next: readWikipedia
             - getLocation:
                 call: sys.get_env
                 args:
                   name: GOOGLE_CLOUD_LOCATION
                 result: location
             - setFromCallResult:
                 assign:
                   - searchTerm: '${text.split(location, "-")[0]}'
             - readWikipedia:
                 call: http.get
                 args:
                   url: 'https://en.wikipedia.org/w/api.php'
                   query:
                     action: opensearch
                     search: '${searchTerm}'
                 result: wikiResult
             - returnOutput:
                 return: '${wikiResult.body[1]}'

### JSON
         
         {
           "main": {
             "params": [
               "input"
             ],
             "steps": [
               {
                 "checkSearchTermInInput": {
                   "switch": [
                     {
                       "condition": "${\"searchTerm\" in input}",
                       "assign": [
                         {
                           "searchTerm": "${input.searchTerm}"
                         }
                       ],
                       "next": "readWikipedia"
                     }
                   ]
                 }
               },
               {
                 "getLocation": {
                   "call": "sys.get_env",
                   "args": {
                     "name": "GOOGLE_CLOUD_LOCATION"
                   },
                   "result": "location"
                 }
               },
               {
                 "setFromCallResult": {
                   "assign": [
                     {
                       "searchTerm": "${text.split(location, \"-\")[0]}"
                     }
                   ]
                 }
               },
               {
                 "readWikipedia": {
                   "call": "http.get",
                   "args": {
                     "url": "https://en.wikipedia.org/w/api.php",
                     "query": {
                       "action": "opensearch",
                       "search": "${searchTerm}"
                     }
                   },
                   "result": "wikiResult"
                 }
               },
               {
                 "returnOutput": {
                   "return": "${wikiResult.body[1]}"
                 }
               }
             ]
           }
         }
         

Unless you input your own search term, this workflow uses your Google Cloud location to construct a search term, which it passes to the [Wikipedia API](https://wikipedia.org/w/api.php). A list of related Wikipedia articles is returned.

  8. Select **Deploy**.




## Execute the workflow

Once your workflow has been successfully deployed, you can execute it for the first time. After deploying the workflow, you'll be taken to its **Workflow details** page.

  1. On the **Workflow details** page, click play_arrow**Execute**.

  2. On the **Execute workflow** page, click **Execute**.

  3. In the **Output** pane, your workflow's results are displayed.




You've deployed and executed your first workflow! 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. From the list of workflows, click a workflow to go to its **Workflow details** page.

  3. Click delete**Delete**.

  4. Type the name of the workflow and then click **Confirm**.




## What's next

  * [Update an existing workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#updating_a_workflow)

  * [Control the order of execution in a workflow](https://docs.cloud.google.com/workflows/docs/controlling-execution-order)

  * [Sample workflows](https://docs.cloud.google.com/workflows/docs/samples)

  * [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
