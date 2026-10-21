---
url: https://docs.cloud.google.com/artifact-analysis/docs/view-licenses-dependencies/
title: View licenses and dependencies \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:20.758826+00:00
---

# View licenses and dependencies  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/view-licenses-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  View licenses and dependencies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view and filter dependency metadata that Artifact Analysis detects with automatic scanning.

When you enable the scanning API to to identify vulnerabilities in container images, Artifact Analysis also gathers information about the dependencies and licenses used in your images.

You can use this metadata to understand the components of your container images and remediate security issues.

Artifact Analysis provides dependency and license detection for OS packages and [supported language packages](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#feature-support) within container images stored in stored in a Docker format Artifact Registry repository. For more information, see [Container scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).

Like vulnerability information, license and dependency metadata is generated each time you push an image to Artifact Registry, then stored in Artifact Analysis.

Artifact Analysis continues to scan images and packages as long as they have been pulled within the last 30 days. After 30 days, metadata for scanned images and packages will no longer be updated, and the results will be stale.

Artifact Analysis archives metadata that has been stale for more than 90 days. This archived metadata can be evaluated only by using the API. You can re-scan an image with stale or archived metadata by pulling that image. Refreshing metadata can take up to 24 hours. Packages with stale or archived metadata can't be rescanned.

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Container Analysis, Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=https://containeranalysis.googleapis.com,https://artifactregistry.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Container Analysis, Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=https://containeranalysis.googleapis.com,https://artifactregistry.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Have a Docker repository in Artifact Registry . See instructions on [generating SBOMs](https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms).



### Required roles

To get the permissions that you need to view SBOM data and filter results, ask your administrator to grant you the following IAM roles on the project: 

  * [Container Analysis Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View licenses and dependencies in the Google Cloud console

  1. Open the Artifact Registry **Repositories** page.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

The page displays a list of your repositories.

  2. In the repositories list, click a repository name.

The **Repository details** page opens and displays a list of your images.

  3. In the images list, click an image name.

The page displays a list of your image digests.

  4. In the image digest list, click a digest name.

The page displays a row of tabs where the **Overview** tab is open, showing details such as format, location, repository, virtual size, and tags.

  5. In the row of tabs, click the **Dependencies** tab.

The dependencies tab opens and displays the following information:

     * SBOM section
     * Licenses section
     * A filterable list of dependencies



## SBOMs

If you generate or upload a software bill of materials (SBOM) with Artifact Analysis, your SBOM details are displayed in this section. SBOMs aren't generated automatically like license and dependency information. Learn how to add SBOMs in [SBOM overview](https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms).

### Licenses

The **Licenses** summary section displays a bar graph called **Most common licenses**. This represents the types of licenses that appear most often in your dependency information. When you hold the pointer over a bar in the graph, the console displays the exact count for instances of that license type.

### Dependencies

The list of dependencies displays the contents of your image digest including:

  * Package name
  * Package version
  * Package type
  * License type



You can filter the list of dependencies by any of these categories.

## View licenses and dependencies in Cloud Build

If you're using Cloud Build, you can view image metadata in the **Security insights** side panel within the Google Cloud console.

The **Security insights** side panel provides a high-level overview of build security information for artifacts stored in Artifact Registry. To learn more about the side panel and how you can use Cloud Build to help protect your software supply chain, see [View build security insights](https://docs.cloud.google.com/build/docs/view-build-security-insights).

## Limitations

Information about licenses and dependencies is only available with automatic scanning. On-demand scanning does not support this feature.

## What's next

  * [Generate a software bill of materials (SBOM)](https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms) to support compliance requirements.
  * [Investigate vulnerabilities](https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities) using common query patterns.
  * [Create VEX statements](https://docs.cloud.google.com/artifact-analysis/docs/create-vex) to attest to the security posture of your images.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
