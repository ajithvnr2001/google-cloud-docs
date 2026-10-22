---
url: https://docs.cloud.google.com/artifact-analysis/docs/view-sboms-dependencies/
title: View and filter SBOMs \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:55.275450+00:00
---

# View and filter SBOMs  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/view-sboms-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  View and filter SBOMs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to access your software bill of materials (SBOM) records and related dependency metadata to help you understand the components of your container images stored in Artifact Registry.

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

  14. Have SBOMs stored in Cloud Storage. See instructions on [generating SBOMs](https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sbom).



### Required roles

To get the permissions that you need to view SBOM data and filter results, ask your administrator to grant you the following IAM roles on the project: 

  * [Container Analysis Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`)
  * To verify SBOMS: Storage Object Viewer (`roles/storage.objectViewer`) - a specific Cloud Storage bucket 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View SBOMs in the Google Cloud console

To view SBOMs and related dependency metadata for container images stored in Artifact Registry:

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



### SBOM

The **SBOM** summary section displays the following information:

  * **File** : A clickable SBOM filename, which opens the location where your SBOM is saved in Cloud Storage.
  * **Type** : The type of SBOM standard used, such as Software Package Data Exchange (SPDX) or Cyclone.
  * **Version** : The version of the SBOM standard used.
  * **Generated by** : The origin of the SBOM data, whether generated by Artifact Analysis or uploaded manually.



### Licenses

The **Licenses** summary section displays a bar graph called **Most common licenses**. This represents the types of licenses that appear most often in your dependency information. When you hold the pointer over a bar in the graph, the console displays the exact count for instances of that license type.

### Dependencies

The list of dependencies displays the contents of your image digest including:

  * Package name
  * Package version
  * Package type
  * License type



You can filter the list of dependencies by any of these categories.

## View SBOMs in Cloud Build

If you're using Cloud Build, you can view image metadata in the **Security insights** side panel within the Google Cloud console.

The **Security insights** side panel provides a high-level overview of build security information for artifacts stored in Artifact Registry. To learn more about the side panel and how you can use Cloud Build to help protect your software supply chain, see [View build security insights](https://docs.cloud.google.com/build/docs/view-build-security-insights).

## View SBOMs with the gcloud CLI

Use the gcloud [`artifacts sbom list`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list) command to search for SBOMs stored in Cloud Storage. This search applies to all of your SBOMs in Cloud Storage, including those generated by Artifact Analysis and any you choose to upload from another source using a supported format.

You can use filters with the gcloud command to narrow results and focus on SBOMs most relevant to a specific security concern or compliance request.

For example, the following command demonstrates how to obtain information about the SBOM for a Docker image `my-image` stored in Artifact Registry:
    
    
    gcloud artifacts sbom list \
        --resource="us-east1-docker.pkg.dev/my-project/my-repo/my-image:1.0"
    

Where:

  * `--resource` specifies the image resource URI to list SBOM file references for.



Output includes the following:

  * The Cloud Storage location for the SBOM. Using the Cloud Storage location, you can view the SBOM in the gcloud CLI by running the [gcloud storage cat](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cat) command.
  * Whether the SBOM is still in the Cloud Storage bucket or has been removed.
  * A hash of the SBOM which you can use to verify that it wasn't modified.



### Filters

You can filter for specific SBOMs by using any of the following optional flags:

Flag | Purpose | Input value  
---|---|---  
`--dependency` | List all SBOM file references where a resource has the specified package installed. See [supported package types](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview#supported-pkgs). | The name of an installed package  
`--resource` | List SBOM file references related to a specific image. | The resource URI  
`--resource-prefix` | List SBOM file references related to the resource path prefix. | A resource path, which will be used as a prefix for the search  
  
### Filtering examples

Filter results by resource URI:
    
    
    gcloud artifacts sbom list \
    --resource="us-east1-docker.pkg.dev/project/repo/my-image@sha256:88b205d7995332e10e836514fbfd59ecaf8976fc15060cd66e85cdcebe7fb356"
    

Filter by resource prefix:
    
    
    gcloud artifacts sbom list \
    --resource-prefix="us-east1-docker.pkg.dev/project/repo"
    

## Limitations

  * License information is only provided for OS packages and [supported language packages](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#feature-support).



## What's next

  * [Generate SBOMs](https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms).
  * Learn how to use [VEX statements](https://docs.cloud.google.com/artifact-analysis/docs/create-vex) to provide additional security information. See [Generate and store SBOMs](https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms) for the formats Artifact Analysis supports.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
