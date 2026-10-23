---
url: https://docs.cloud.google.com/artifact-analysis/docs/package-scan-automatic/
title: Scan packages automatically \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:46.961380+00:00
---

# Scan packages automatically  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/package-scan-automatic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Scan packages automatically Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to enable the Container Scanning API, push an image to Artifact Registry, and see the list of vulnerabilities found in the image.

Artifact Analysis stores vulnerability information as [notes](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#note). An [occurrence](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#occurrence) is created for each instance of a note associated with an image. See the [overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) and [pricing](https://docs.cloud.google.com/artifact-analysis/pricing) documents for more information.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry and Container Scanning APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,containerscanning.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

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

  10. Enable the Artifact Registry and Container Scanning APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,containerscanning.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. [Create a repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) in Artifact Registry and push a package with your application code to the repository. If you are not familiar with managing packages in Artifact Registry, see the following topics: 
     1. [Store Java packages in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/java/store-java)
     2. [Store Node.js packages in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/nodejs/store-nodejs)
     3. [Store Python packages in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/python/store-python)



Enabling this API also enables language package scanning in Artifact Registry. See [supported package types](https://docs.cloud.google.com/artifact-analysis/docs/package-scanning-overview#feature-support).

**Important:** When you enable the Artifact Analysis API, Artifact Analysis automatically begins scanning each new image as they are pushed to Artifact Registry repositories in your project. However, scanning is disabled by default for packages pushed to Artifact Registry repositories. To enable scanning in a repository, see [Control scanning settings for an individual repository](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning#disable-repo).

### Required roles

To get the permissions that you need to View package scan results, ask your administrator to grant you the following IAM roles on the project: 

  * [Container Scanner Service Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`)
  * [Container Analysis Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`)
  * [Container Analysis Notes Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.viewer) (`roles/containeranalysis.notes.viewer`)
  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View the package vulnerabilities

Artifact Analysis scans new packages when they're uploaded to Artifact Registry. This scan extracts information about the package and its dependencies.

You can view vulnerability occurrences for your images in Artifact Registry using the Google Cloud console, Google Cloud CLI, or the Container Analysis API. If an image has vulnerabilities, you can then obtain the details.

Artifact Analysis continues to scan images and packages as long as they have been pulled within the last 30 days. After 30 days, metadata for scanned images and packages will no longer be updated, and the results will be stale.

Artifact Analysis archives metadata that has been stale for more than 90 days. This archived metadata can be evaluated only by using the API. You can re-scan an image with stale or archived metadata by pulling that image. Refreshing metadata can take up to 24 hours. Packages with stale or archived metadata can't be rescanned.

### View occurrences in the Google Cloud console

To see the vulnerabilities in a package:

  1. Get the list of repositories.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, click a repository.

  3. In the packages list, click a package name.

Vulnerability totals for each package are displayed in the **Vulnerabilities** column.

![A scanned package with vulnerabilities](https://docs.cloud.google.com/artifact-analysis/images/vulns-tab-package-summary.png)

  4. To view the list of vulnerabilities for a package, click the link in the **Vulnerabilities** column.

The **Scan results** section displays a summary of the package types scanned, total vulnerabilities, vulnerabilities with fixes available, vulnerabilities without fixes, and effective severity.

![The Scan results page listing vulnerabilities, fixes, and effective severity](https://docs.cloud.google.com/artifact-analysis/images/vulns-tab-package-expanded.png)

The table of vulnerabilities lists the Common Vulnerabilities and Exposures (CVE) name for each vulnerability found, the [effective severity](https://docs.cloud.google.com/artifact-analysis/docs/severity-levels), Common Vulnerability Scoring System (CVSS) score, fixes (when available), the name of the package that contains the vulnerability, and the package type. You can filter and sort these files to check a specific file, directory, or type of file by file extension. Google Cloud console displays up to 1200 vulnerabilities per page in this table.

  5. For details about a specific CVE, click the CVE name.

  6. To view vulnerability occurrence details such as version number and affected location, in the row with the name of the vulnerability, click **View** or **View Fixed** in the row with the name of the vulnerability. The link text is **View** for vulnerabilities without a fix, and **View Fixed** for vulnerabilities where a fix has been applied.




### View occurrences using gcloud

To view occurrences for packages in Artifact Registry, run the [`gcloud artifacts versions describe`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/versions/describe) command:
    
    
    gcloud artifacts versions describe VERSION \
        --location=LOCATION --repository=REPOSITORY --package=PACKAGE --show-package-vulnerability
    

Where:

  * VERSION is the version of the package for which you are viewing occurrences.
  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * REPOSITORY is the name of the repository where the package is stored.
  * PACKAGE is the name of the package in the repository. You cannot specify a package tag with this command.



### View occurrences using the API

To get a list of occurrences in your project:
    
    
     curl -X GET -H "Content-Type: application/json" -H \
        "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences
    

To get a summary of vulnerabilities in your project:
    
    
     curl -X GET -H "Content-Type: application/json" -H \
        "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences:vulnerabilitySummary
    

To get details on a specific occurrence:
    
    
     curl -X GET -H "Content-Type: application/json" -H \
        "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences/OCCURRENCE_ID
    

## Filter occurrences

You can use filter strings in the `gcloud` commands and the Artifact Analysis API to filter occurrences before viewing them. The following sections describe the supported search filters.

### View occurrences of a specific type

You can use the `kind` value to filter by occurrence type. See available [kinds](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/NoteKind).

The following examples demonstrate how to filter package vulnerability occurrences:

###  gcloud 

Filtering occurrences isn't supported in the Google Cloud CLI for package-based scanning.

###  API 

In your API query, use the following filter expression:
    
    
    kind="PACKAGE_VULNERABILITY" AND resourceUrl="RESOURCE_URL"

Where:

  * `PACKAGE_VULNERABILITY` is the [kind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/NoteKind) of occurrence.
  * RESOURCE_URL is the complete URL of the package in the format `projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/packages/PACKAGE_ID/PACKAGE_TYPE/VERSION_ID`: 
    * PROJECT_ID is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
    * REPOSITORY is the name of the repository where the image is stored.
    * PACKAGE_ID is the name of the package where the image is stored.
    * PACKAGE_TYPE is the application language package type. Available types are: `pythonPackages`, `mavenArtifacts`, and `npmPackages`.
    * VERSION is the version number of the package.



You can use the `hasPrefix` function to filter with a wider scope.

For example, the following filters to occurrences of a specific kind across multiple versions of the same package:
    
    
    kind="NOTE_KIND" AND has_prefix(resourceUrl, "RESOURCE_URL_PREFIX")

Where:

  * RESOURCE_URL_PREFIX specifies a substring from a resource URL. 
    * To filter for all versions of a package, omit the version. Use the format:`projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID`
    * To filter for all packages in a project, only specify the resource location and project. Use the format: `projects/PROJECT_ID/locations/LOCATION`



### View vulnerability occurrences

You can view lists of vulnerability occurrences by using the gcloud CLI or the Artifact Analysis API.

###  gcloud 

To retrieve a list of vulnerability occurrences for a package, use the `--show-package-vulnerability` flag:
    
    
    gcloud artifacts versions describe VERSION_ID --repository=REPOSITORY_ID
      --package=GROUP_ID:ARTIFACT_ID --show-package-vulnerability
    

Where:

  * VERSION is the version number of the package.
  * REPOSITORY is the name of the repository where the package is stored.
  * GROUP_ID is the group identifier of your package.
  * ARTIFACT_ID is the artifact identifier of your package.



###  API 

In your API query, use the following filter expression:
    
    
    GET https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences?filter=kind%3D%22VULNERABILITY%22%20AND%20resourceUrl%3D%22ENCODED_RESOURCE_URL%22

Where:

  * ENCODED_RESOURCE_URL is the encoded path to your image. To learn about encoding, see [URL encoding](https://en.wikipedia.org/wiki/URL_encoding).



For more information on using the API, see [`projects.occurrences.get`](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences/get).

### View images associated with a specific note

You can retrieve a list of resources that are associated with a specific _note ID_. For example, you can list images with a specific CVE vulnerability.

To list all images within a project that are associated with a particular note, use the following filter expression:

###  gcloud 

Filtering occurrences isn't supported in the Google Cloud CLI for package-based scanning.

###  API 
    
    
    GET https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences?filter=noteProjectId%3D%22goog-vulnz%22%20AND%20resourceUrl%3D%22ENCODED_RESOURCE_URL%22%20AND%20noteId%3D%22NOTE_ID%22

Where:

  * `goog-vulnz` is the `PROVIDER_PROJECT_ID` for Artifact Analysis vulnerability analysis. If you are using Artifact Analysis in a custom project, you can replace this value with your own provider project ID.
  * ENCODED_RESOURCE_URL is the encoded path to your image. To learn about encoding, see [URL encoding](https://en.wikipedia.org/wiki/URL_encoding).
  * NOTE_ID is the ID of the note. For example, when you see a vulnerability in Artifact Analysis scanning results, it will often use [CVE ID formatting](https://www.cve.org/ResourcesSupport/Glossary?activeTerm=glossaryRecord) similar to `CVE-2019-12345`.



To check a specific image for a specific note, use the following filter expression:

###  gcloud 

Filtering occurrences isn't supported in the Google Cloud CLI for package-based scanning.

###  API 

In your API query, add the following filter expression:
    
    
    resourceUrl="RESOURCE_URL" AND noteProjectId="goog-vulnz" \
    AND noteId="NOTE_ID"

Where:

  * RESOURCE_URL is the complete URL of the package in the format `projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID/packages/PACKAGE_ID/PACKAGE_TYPE/VERSION_ID`.
  * `goog-vulnz` is the `PROVIDER_PROJECT_ID` for Artifact Analysis vulnerability analysis.
  * NOTE_ID is the ID of the note. Security related notes are often formatted as `CVE-2019-12345`.



## What's next

  * [Use Pub/Sub notifications](https://docs.cloud.google.com/artifact-analysis/docs/pub-sub-notifications) to get notifications about vulnerabilities and other metadata.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
