---
url: https://docs.cloud.google.com/container-analysis/docs/ods-quickstart/
title: Quickstart: Scan OS packages manually \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:25.440768+00:00
---

# Quickstart: Scan OS packages manually  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-analysis/docs/ods-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Scan OS packages manually

This quickstart shows you how to pull a container image, manually scan it for operating system vulnerabilities with the On-Demand Scanning API, and retrieve identified vulnerabilities. To follow this quickstart you will use Cloud Shell and an example Ubuntu image.

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

  2. Use docker to pull the latest Ubuntu image.
         
         docker pull ubuntu:latest
         

  3. Run the scan.
         
         gcloud artifacts docker images scan ubuntu:latest
         

This triggers that scanning process and returns the scan name when finished:
         
         ✓ Scanning container image
           ✓ Locally extracting packages and versions from local container image
           ✓ Remotely initiating analysis of packages and versions
           ✓ Waiting for analysis operation to complete [projects/my-project/locations/us/operations/OPERATION_ID]
         Done.
         
         done: true
         metadata:
           '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesMetadata
           createTime: '2021-01-26T13:43:53.112123Z'
           resourceUri: ubuntu:latest
         name: projects/my-project/locations/us/operations/OPERATION_ID
         response:
           '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesResponse
           **scan: projects/my-project/locations/us/scans/ SCAN_ID**
         

  4. Use the scan name, the value of `scan` from the output, to fetch the scan results.
         
         gcloud artifacts docker images list-vulnerabilities \
         projects/my-project/locations/us/scans/SCAN_ID
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you created a new project for this guide, you can now delete the project. 

## What's next

  * [Explore all the On-Demand Scanning API options](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-on-demand).
  * [Enable automated scanning](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-automatically).
  * [Understand container scanning concepts](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
