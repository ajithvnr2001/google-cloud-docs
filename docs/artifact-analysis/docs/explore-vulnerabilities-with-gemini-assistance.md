---
url: https://docs.cloud.google.com/artifact-analysis/docs/explore-vulnerabilities-with-gemini-assistance/
title: Explore vulnerabilities with Gemini assistance \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:51:39.474250+00:00
---

# Explore vulnerabilities with Gemini assistance  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/explore-vulnerabilities-with-gemini-assistance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Explore vulnerabilities with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview —[Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use Gemini Cloud Assist to learn about the state of your artifacts, get information about repositories and artifact metadata, and use Artifact Analysis information to answer questions about artifact vulnerabilities and your software bill of materials (SBOMs).

## Before you begin

  1. Ensure you have set up Gemini Cloud Assist in your Google Cloud project.

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Artifact Registry and Container Scanning APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,containerscanning.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the Artifact Registry and Container Scanning APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,containerscanning.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  12. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  13. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  14. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

To get the permissions that you need to prompt Gemini Cloud Assist for information about your artifacts, ask your administrator to grant you the following IAM roles: 

  * [Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`) on the project or repository
  * [Gemini Cloud Assist User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Open Gemini Cloud Assist

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

You can open the Gemini Cloud Assist chat from anywhere in the Google Cloud console.

  1. In the Google Cloud console, select a project in which you have container images stored in Artifact Registry.  


[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. To open the **Cloud Assist** panel, click spark **Open or close Gemini AI chat**.

  3. To enter a prompt, type the prompt and click send **Send**.



## Prompt Considerations

The following is a list of Artifact Analysis specific considerations you should be aware of when generating Gemini Cloud Assist prompts. For more details on general prompt writing advice, visit [Write better prompts for Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).

  * All prompts default to the selected project, however you can direct your prompt to filter by location, repository, or image.
  * Any query based on a container image name treats the container image name as a prefix. This lets you filter within a project, repository, or specific image (across different SHAs), but does not allow you to filter by tag.
  * To get more specific results, include a scope. For example, to get results for a specific image, include the image name in the scope. You can filter by adding project, repository, image, or image@digest details to the container image name.
  * Region qualifiers aren't needed for Artifact Analysis prompts as Artifact Analysis provides combined results from all regions. You can specify a region qualifier to filter the results.



## List my top known vulnerabilities

You can prompt Gemini Cloud Assist to list the top known vulnerabilities in your current project. Vulnerabilities are sorted by their Common Vulnerability Scoring System (CVSS) score in descending order, and grouped by their vulnerability ID. Only the top 10 vulnerabilities are displayed. The results include vulnerabilities from all images scanned in the last 30 days.

You can filter the response by the container image name.

To list the top known vulnerabilities, in the **Gemini Cloud Assist Chat** , enter the following prompt:
    
    
    List artifact vulnerabilities for `CONTAINER_IMAGE_NAME`.
    

Replace `CONTAINER_IMAGE_NAME` with the container image name that includes your repository—for example, `us-central1-docker.pkg.dev/my-project/my-repository`.

Including more detail in your container image name returns a more precise response. For example— `LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE` would provide vulnerability details on a specific image.

The following prompt asks Gemini Cloud Assist to list the top known vulnerabilities for the repository `us-central1-docker.pkg.dev/my-project/my-repository`:
    
    
    List artifact vulnerabilities for
    `us-central1-docker.pkg.dev/my-project/my-repository`.
    

The response includes a list of up to 10 vulnerabilities sorted by their CVSS score in descending order for the specified repository.

To view all of your vulnerabilities, use the [artifacts vulnerabilities list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/list) gcloud CLI command. You can include the unqualified image name, or provide a Secure Hash Algorithm (SHA) to view vulnerabilities.

## List images by vulnerability

You can prompt Gemini Cloud Assist to display all of your images that include a specified vulnerability. The response is sorted in descending order from the most recent creation date and includes images scanned in the last 30 days. This prompt displays a maximum of 10 images and only includes images that have been scanned by Artifact Analysis.

You can filter the response by the following:

  * Vulnerability ID
  * Container image name



To list your images that include a specific vulnerability, in the **Cloud Assist** chat, enter the following prompt:
    
    
    List docker container images that contain vulnerability
    `VULNERABILITY_ID`.
    

Replace `VULNERABILITY_ID` with the ID of the vulnerability you want to locate—for example, `CVE-2024-01234`.

The following prompt asks Gemini Cloud Assist to list images that contain the vulnerability `CVE-2024-01234`:
    
    
    List artifact vulnerabilities for `CVE-2024-01234`.
    

The response includes a list of up to 10 images that contain the specified vulnerability, sorted by their CVSS score in descending order for the specified repository.

## List images by package

You can prompt Gemini Cloud Assist to return a list of images that include a specified package. The images are sorted in descending order from their date of creation and include images scanned in the last 30 days. This prompt displays a maximum of 10 images and only includes images that have been scanned by Artifact Analysis.

You can filter the response by the container image name.

To list your images that include a specific package, in the **Cloud Assist** chat, enter the following prompt:
    
    
    List docker container images that contain package
    `PACKAGE_ID`.
    

Replace `PACKAGE_ID` with the ID of the package you want to locate.

For example, the following prompt asks Gemini Cloud Assist to list images that contain the package `my-package-name`:
    
    
    List images that contain package `my-package-name`.
    

The response includes a list of up to 10 images that contain the specified package.

## List build provenance

You can prompt Gemini Cloud Assist to return the 10 latest build provenance details for a specified project and scope. Results are sorted by creation date in descending order with the most recently created items at the top of the list. Up to 10 builds are shown. To be listed, builds must have been created in the last 30 days. This prompt only supports builds with [SLSA 1.0 provenance](https://security.googleblog.com/2021/06/introducing-slsa-end-to-end-framework.html).

You can filter the response by the container image name.

To list your build provenance, in the **Cloud Assist** chat, enter the following prompt:
    
    
    List build provenance for CONTAINER_IMAGE_NAME.
    

Replace CONTAINER_IMAGE_NAME with the ID of the image you want to learn the provenance of.

For example, the following prompt asks Gemini Cloud Assist to list the build provenance for `us-central1-docker.pkg.dev/my-project/my-image`:
    
    
    List build provenance for `us-central1-docker.pkg.dev/my-project/my-image`.
    

You can remove the location, project, or image details from your container image name to return a broader set of results. The response includes build provenance details for the 10 latest builds.

To view your builds in the Google Cloud console, visit the [**Build History**](https://console.cloud.google.com/cloud-build/builds) page.

## List SBOMs

You can prompt Gemini Cloud Assist to return the latest SBOMs in your repository. Results are sorted by creation date in descending order with the most recently created items at the top of the list. Up to 10 builds can be displayed that were created in the last 30 days.

You can filter the response by the container image name, including image@digest details.

To list your SBOMs, in the **Cloud Assist** chat, enter the following prompt:
    
    
    List SBOMs for `CONTAINER_IMAGE_NAME`.
    

Replace `CONTAINER_IMAGE_NAME` with the container image name you want to search—for example, `us-central1-docker.pkg.dev/my-project/my-repo`.

The following prompt asks Gemini Cloud Assist to list the SBOMs for the repository `us-central1-docker.pkg.dev/my-project/my-repo`:
    
    
    List SBOMs for `us-central1-docker.pkg.dev/my-project/my-repo`.
    

The response includes SBOM details for the 10 latest repositories. You can remove the location, project, or image details from your container image name to return a broader set of results.

You can see all of the SBOMs using the [artifacts SBOM list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list) gcloud CLI command.

## Additional prompts

The following prompts demonstrate the capabilities of using variables to filter with Gemini Cloud Assist.

To list vulnerabilities by a specific variable, enter the following in the **Cloud Assist** chat:
    
    
    List vulnerabilities for `SCOPE`.
    

In this prompt `SCOPE` can be set to a project, repository, image, or image and digest.

To list images that contain a specific package, enter the following in the **Cloud Assist** chat:
    
    
    List images that contain the log4j package.
    

To list images that contain a specific vulnerability, enter the following in the **Cloud Assist** chat:
    
    
    List images that contain `VULNERABILITY_ID`.
    

In this prompt, replace `VULNERABILITY_ID` with a CVE number.

## What's next

  * Learn more about [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview).

  * Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
