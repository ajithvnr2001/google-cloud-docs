---
url: https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-java-manually/
title: Quickstart: Scan Java packages manually \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:08.805497+00:00
---

# Quickstart: Scan Java packages manually  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-java-manually/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Scan Java packages manually

This quickstart shows you how to pull a container image, manually scan it with On-Demand Scanning, and retrieve identified vulnerabilities for system and Maven packages. To follow this quickstart you will use Cloud Shell and an example Alpine image.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the On-Demand Scanning API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ondemandscanning.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the On-Demand Scanning API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ondemandscanning.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)




## Download and scan an image

  1. Open a Cloud Shell in your project.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

This opens a terminal with all the required tools to follow this guide.

  2. Use docker to pull the container image:
         
         docker pull jenkins:2.60.3-alpine
         

  3. Run the scan:
         
         gcloud artifacts docker images scan jenkins:2.60.3-alpine --additional-package-types=MAVEN
         

This triggers that scanning process and returns the scan name when finished:
         
         ✓ Scanning container image 
           ✓ Locally extracting packages and versions from local container image
           ✓ Remotely initiating analysis of packages and versions
           ✓ Waiting for analysis operation to complete [projects/my-project/locations/us/operations/1a6fd941-b997-4e5f-ba4f-6351f30e7dad]
         Done.
         
         done: true
         metadata:
           '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesMetadata
           createTime: '2021-01-26T13:43:53.112123Z'
           resourceUri: jenkins:2.60.3-alpine
         name: projects/my-project/locations/us/operations/1a6fd941-b99f-4eaf-ba4f-6e5af30e7dad
         response:
           '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesResponse
           **scan: projects/my-project/locations/us/scans/893c91ce-7fe6-4f1a-a69a-d6ca1b465160**
         

  4. Use the scan name, the value of `scan` from the output, to fetch the scan results:
         
         gcloud artifacts docker images list-vulnerabilities \
         projects/my-project/locations/us/scans/893c91ce-7fe6-4f1a-a69a-d6ca1b465160
         

The output contains a list of Maven and Linux package vulnerabilities. Maven package vulnerabilities can be identified by the field `packageType:MAVEN`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you created a new project for this guide, you can now delete the project. 

  * Open the Settings page (found under IAM & Admin) in the Google Cloud console. 

[Open the Settings page](https://console.cloud.google.com/iam-admin/settings)

  * Click **Select a project**.

  * Select a project you want to delete, and click **Open**.

  * Click **Shut down**.

  * Enter the Project ID, then click **Shut down**.




## What's next

  * [Explore all the Java package scanning options](https://docs.cloud.google.com/artifact-analysis/docs/scan-java-on-demand).
  * [Understand container scanning concepts](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
