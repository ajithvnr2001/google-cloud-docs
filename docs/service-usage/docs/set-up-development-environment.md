---
url: https://docs.cloud.google.com/service-usage/docs/set-up-development-environment/
title: Quickstart: Set up Service Usage for a development environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:13.029137+00:00
---

# Quickstart: Set up Service Usage for a development environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/set-up-development-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Service Usage for a development environment

This page describes how to set up your development environment to use the Service Usage API.

  * For most operational use cases, the simplest way to enable and disable services is to use Google Cloud console.
  * If you need to create scripts, you can use the Google Cloud CLI.
  * If you need to program against the Service Usage API, use one of the [client libraries](https://docs.cloud.google.com/service-usage/docs/libraries).
  * To experiment with the API, you can follow the alternative setup instructions in this guide and use the `curl` command to test the API without setting up a full application development environment.



## Set up to call the API directly

This section describes the basic steps necessary to set up your local environment to experiment with the Service Usage API using the `curl` command. It is aimed at developers who need to program against the Service Usage API.

**Note:** You don't need to complete the instructions in this section if you want to list, enable, or disable services using Google Cloud console or the `gcloud` command line interface.

### Enable the Service Usage API

To use the Service Usage API, you must first enable it in your Google Cloud project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Service Usage API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=serviceusage.googleapis.com)

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Service Usage API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=serviceusage.googleapis.com)

  6. Ensure that your user account has been granted the [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage) role. 



### Test with curl

  1. Set an environment variable `PROJECT_ID` with the identifier of your project:
         
         PROJECT_ID=PROJECT_ID
         

Replace PROJECT_ID with your Google Cloud project ID or number.

  2. Ensure that you are logged into 'gcloud':
         
         gcloud auth login
         

  3. List the enabled APIs and services in this project:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://serviceusage.googleapis.com/v1/projects/${PROJECT_ID}/services?filter=state:ENABLED&fields=services.config.title,services.config.name"
         

If you see output like this, then your setup is successful:
         
         {
         "services": [
           {
             "config": {
               "name": "bigquery.googleapis.com",
               "title": "BigQuery API"
             }
           },
           {
             "config": {
               "name": "bigquerystorage.googleapis.com",
               "title": "BigQuery Storage API"
             }
           },
           ...
         




## Next steps

To list the APIs and services that are enabled or available in your Google Cloud projects, see [List services](https://docs.cloud.google.com/service-usage/docs/list-services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
