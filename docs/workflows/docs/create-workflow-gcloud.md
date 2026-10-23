---
url: https://docs.cloud.google.com/workflows/docs/create-workflow-gcloud/
title: Quickstart: Create a workflow by using the gcloud CLI \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:15.617420+00:00
---

# Quickstart: Create a workflow by using the gcloud CLI  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/create-workflow-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a workflow by using the gcloud CLI

This quickstart shows you how to create, deploy, and execute your first workflow using the Google Cloud CLI. The sample workflow sends a request to a public API and then returns the API's response.

For a list of all Workflows gcloud CLI commands, see the Workflows gcloud CLI [reference page](https://docs.cloud.google.com/sdk/gcloud/reference/workflows). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

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

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Workflows API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable workflows.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Workflows API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable workflows.googleapis.com

  16. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant the `roles/logging.logWriter` IAM role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=roles/logging.logWriter

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 

To learn more about service account roles and permissions, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Workflows Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.admin) (`roles/workflows.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create, deploy, and execute a workflow

  1. In your home directory, create a new file called `myFirstWorkflow.yaml` or `myFirstWorkflow.json`.

  2. Copy and paste the following workflow into the new file, then save it:

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

  3. Deploy the workflow and associate it with the specified service account:
         
         gcloud workflows deploy myFirstWorkflow --source=myFirstWorkflow.EXTENSION \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         

Replace the following:

     * `EXTENSION`: the file extension for your workflow; use `yaml` for the YAML version or use `json` for the JSON version
     * `PROJECT_ID`: your project ID
**Note:** In production environments, we strongly recommend creating a new service account, then granting it the least permissive roles that allow the service account to access the required resources. To learn more, see [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts). For a list of Workflows roles, see [Workflows roles and permissions](https://docs.cloud.google.com/workflows/docs/access-control).
  4. Execute the workflow:
         
         gcloud workflows run myFirstWorkflow \
             --data='SEARCH_TERM'
         

Replace `SEARCH_TERM` with your search term; for example, `{"searchTerm":"North"}`. If you enter `{}`, your Google Cloud location is used to construct a search term.

This returns the results of the execution attempt. The output is similar to the following:
         
         argument: '{"searchTerm":"North"}'
         duration: 0.210616856s
         endTime: '2023-05-10T21:56:39.465899376Z'
         name: projects/734581694262/locations/us-central1/workflows/workflow-1/executions/eae31f11-a5c3-47e2-8014-05b400820a79
         result: '["North","North America","Northern Ireland","North Korea","North Macedonia","North
           Carolina","Northrop Grumman B-2 Spirit","Northrop F-5","Northern Cyprus","North
           Dakota"]'
         startTime: '2023-05-10T21:56:39.255282520Z'
         state: SUCCEEDED
         status:
           currentSteps:
           - routine: main
             step: returnOutput
         workflowRevisionId: 000001-ac2
         




You've deployed and executed your first workflow!

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. Delete the workflow you created:
         
         gcloud workflows delete myFirstWorkflow
         

  2. When asked if you want to continue, enter `y`.




The workflow is deleted.

## What's next

  * [Update an existing workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#updating_a_workflow)

  * [Control the order of execution in a workflow](https://docs.cloud.google.com/workflows/docs/controlling-execution-order)

  * [Sample workflows](https://docs.cloud.google.com/workflows/docs/samples)

  * [Workflows syntax reference](https://docs.cloud.google.com/workflows/docs/reference/syntax)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
