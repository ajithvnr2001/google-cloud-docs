---
url: https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-go-manually/
title: Quickstart: Scan Go packages manually \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:09.848462+00:00
---

# Quickstart: Scan Go packages manually  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-go-manually/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Scan Go packages manually

This quickstart shows you how to pull a container image, manually scan it with On-Demand Scanning, and retrieve identified vulnerabilities for system and Go packages. To follow this quickstart you will use Cloud Shell and an example Alpine image.

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
         
         docker pull golang:1.17.6-alpine
         

  3. Run the scan:
         
         gcloud artifacts docker images scan golang:1.17.6-alpine --additional-package-types=GO
         

This triggers that scanning process and returns the scan name when finished:
         
         ✓ Scanning container image
           ✓ Locally extracting packages and versions from local container image
           ✓ Remotely initiating analysis of packages and versions
           ✓ Waiting for analysis operation to complete [projects/my-project/locations/us/operations/849db1f8-2fb2-4559-9fe0-8720d8cd347c]
         Done.
         done: true
         metadata:
           '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesMetadata
           createTime: '2022-01-11T16:58:11.711487Z'
           resourceUri: golang:1.16.13-alpine
         name: projects/my-project/locations/us/operations/f4adb1f8-20b2-4579-9fe0-8720d8cd347c
         response:
           '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesResponse
           **scan: projects/my-project/locations/us/scans/a54f12b0-ca2d-4d93-8da5-5cf48e9e20ef**
         

  4. Use the scan name, the value of `scan` from the output, to fetch the scan results:
         
         gcloud artifacts docker images list-vulnerabilities \
         projects/my-project/locations/us/scans/a54f12b0-ca2d-4d93-8da5-5cf48e9e20ef
         

The output contains a list of Go, Go standard library, and Linux package vulnerabilities. The following labels indicate the type of Go vulnerabilities:

     * `packageType:GO_STDLIB`. Go standard library vulnerabilities. This indicates that the vulnerability was found either in the Go toolchain used to build the binary, or in the standard library bundled with the toolchain. A possible fix is to upgrade your build toolchain.

     * `packageType:GO`. Go package vulnerabilities. This indicates that the vulnerability was found in a third-party package. A possible fix is to upgrade your dependent modules.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Explore all the Go package scanning options](https://docs.cloud.google.com/artifact-analysis/docs/scan-go-on-demand).
  * [Understand container scanning concepts](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
