---
url: https://docs.cloud.google.com/artifact-analysis/docs/scan-go-on-demand/
title: Scan Go packages manually \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:39.764915+00:00
---

# Scan Go packages manually  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/scan-go-on-demand/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Scan Go packages manually Stay organized with collections  Save and categorize content based on your preferences. 

The On-Demand Scanning API lets you scan images stored locally on your computer or remotely in Artifact Registry. You can use On-Demand Scanning to scan images in your CI/CD pipeline, for system vulnerabilities and [Go](https://go.dev/doc/) package vulnerabilities before deciding whether to store them in a registry. See the [Pricing page](https://cloud.google.com/artifact-analysis/pricing#ods) for pricing information.

This page describes how to manually scan container images for system vulnerabilities and Go packages vulnerabilities.

**Note:** On-Demand Scanning runs in a Linux environment and in macOS. On-Demand Scanning is not supported on Windows.

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

  10. Enable the On-Demand Scanning API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ondemandscanning.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Add the **local-extract** component to your Google Cloud CLI installation

**Using the Google Cloud CLI Component Manager**

The component manager will prompt you to install the required components the first time you run the scanning command.

**Using your system package manager**

     * For Debian/Ubuntu: 
           
           sudo apt install google-cloud-sdk-local-extract
               

     * For Red Hat/Fedora/CentOS: 
           
           sudo dnf install google-cloud-sdk-local-extract
               

Alternatively, you can replace `dnf` with `yum` in the previous command.

  15. [Grant the IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) **On-Demand Scanning Admin** to the user or service account that you are going to use with On-Demand Scanning. If you are using the owner account of the project to run the scans, you can skip this step. 



### Required roles

To get the permissions that you need to View package scan results, ask your administrator to grant you the following IAM roles on the project: 

  * [Container Scanner Service Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/containerscanning#containerscanning.ServiceAgent) (`roles/containerscanning.ServiceAgent`)
  * [Container Analysis Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`)
  * [Container Analysis Notes Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.viewer) (`roles/containeranalysis.notes.viewer`)
  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Scan a container image

  * Local scan:
        
        gcloud artifacts docker images scan IMAGE_URI \
            [--location=(us,europe,asia)] [--async]
        

For a local image, use one of the following formats for the IMAGE_URI:

    * `REPOSITORY:TAG`
    * `REPOSITORY`
  * Remote scan:
        
        gcloud artifacts docker images scan IMAGE_URI \
            --remote [--location=(us,europe,asia)] [--async]
        

For a remote image, use one of the following formats for the IMAGE_URI:

    * `HOSTNAME/PROJECT_ID/REPOSITORY_ID/IMAGE_ID@sha256:HASH`
    * `HOSTNAME/PROJECT_ID/REPOSITORY_ID/IMAGE_ID:HASH`
    * `HOSTNAME/PROJECT_ID/REPOSITORY_ID/IMAGE_ID`
    * `HOSTNAME/PROJECT_ID/IMAGE_ID@sha256:HASH`
    * `HOSTNAME/PROJECT_ID/IMAGE_ID:HASH`
    * `HOSTNAME/PROJECT_ID/IMAGE_ID`

For images in Artifact Registry the IMAGE_URI must include the `REPOSITORY_ID`.




For both local and remote scans, you can use the following optional flags:

  * `--location` is an optional flag to manually select the multi-region where the scanning takes place. Choosing a multi-region closer to your physical location minimizes latency. The available locations are: `us`, `europe` and `asia`. The default location is `us`.

  * `--async` is an optional flag to run the scanning process asynchronously. If you omit this flag, your terminal will block until the scanning process is complete.




### Synchronous scanning

The following example shows the output of a synchronous scan, without the `--async` flag:
    
    
    $ gcloud artifacts docker images scan golang:1.17.6-alpine
    
    ✓ Scanning container image
      ✓ Locally extracting packages and versions from local container image
      ✓ Remotely initiating analysis of packages and versions
      ✓ Waiting for analysis operation to complete [projects/my-project/locations/us/operations/87d2e137-1d1c-4790-8e5e-daf6c96ae7d7]
    Done.
    done: true
    metadata:
      '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesMetadata
      createTime: '2022-01-11T16:58:11.711487Z'
      resourceUri: golang:1.16.13-alpine
    name: projects/my-project/locations/us/operations/87d2e137-1d1c-4790-8e5e-daf6c96ae7d7
    response:
      '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesResponse
      **scan: projects/my-project/locations/us/scans/2fe2bfb8-f0c5-4dd6-a8c8-38961869767a**
    

Use the scan name to retrieve the vulnerability results. The scan name is the value of `scan` in the last line of the output message.

### Asynchronous scanning

The following example shows the output of performing an asynchronous scan:
    
    
    $ gcloud artifacts docker images scan golang:1.17.6-alpine --async
    
    ✓ Scanning container image
      ✓ Locally extracting packages and versions from local container image
      ✓ Remotely initiating analysis of packages and versions
    Done.
    Check operation [projects/my-project/locations/us/operations/2e1a6b1f-16e5-4427-ac86-72c998a3dd16] for status.
    metadata:
      '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesMetadata
      createTime: '2022-01-11T16:58:11.711487Z'
      resourceUri: golang:1.16.13-alpine
    **name: projects/my-project/locations/us/operations/2e1a6b1f-16e5-4427-ac86-72c998a3dd16**
    

This launches a long-running operation and returns its ID without blocking your terminal. Use the operation ID, the value of `name` in the last line of the output message, to poll the operation.

### Poll the long-running operation

Use the operation ID from the output of they asynchronous scanning command to check the operation status:
    
    
    gcloud artifacts docker images get-operation LRO_ID
    

Where LRO_ID is the long-running operation ID.

Continuing with the example of the asynchronous scanning section, to check the status of the operation:
    
    
    $ gcloud artifacts docker images get-operation \
      projects/my-project/locations/us/operations/2e1a6b1f-16e5-4427-ac86-72c998a3dd16
    
    **done: true**
    metadata:
      '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesMetadata
      createTime: '2022-01-11T16:58:11.711487Z'
      resourceUri: golang:1.16.13-alpine
    name: projects/my-project/locations/us/operations/2e1a6b1f-16e5-4427-ac86-72c998a3dd16
    response:
      '@type': type.googleapis.com/google.cloud.ondemandscanning.v1.AnalyzePackagesResponse
      **scan: projects/my-project/locations/us/scans/2fe2bfb8-f0c5-4dd6-a8c8-38961869767a**
    

If the output includes the line `done: true`, the scanning operation is completed. Use the scan name to retrieve the vulnerability results. The name is the value of `scan` in the last line of the output message.

## Retrieve the scan results

To retrieve the scanning results after the scanning operation is completed, use the following command:
    
    
    gcloud artifacts docker images list-vulnerabilities SCAN_NAME [--limit=X]
    

Where:

  * SCAN_NAME is the scan name. You can find it in the last line of the output when you either run a synchronous scan or poll the long-running operation, after the scanning is finished.

  * `--limit=X` is an optional flag that limits the number of occurrences shown in the output. `X` is a numeric value.




For example:
    
    
    createTime: '2022-01-11T16:58:11.972043Z'
    kind: VULNERABILITY
    name: projects/my-project/locations/us/occurrences/0c607d9b-aff4-4cde-86b7-e2c0a865aadd
    noteName: projects/goog-vulnz/notes/CVE-2021-38297
    resourceUri: golang:1.16.13-alpine
    updateTime: '2022-01-11T16:58:11.972043Z'
    vulnerability:
      cvssScore: 7.5
      effectiveSeverity: CRITICAL
      longDescription: Go before 1.16.9 and 1.17.x before 1.17.2 has a Buffer Overflow
        via large arguments in a function invocation from a WASM module, when GOARCH=wasm
        GOOS=js is used.
      packageIssue:
      - affectedCpeUri: cpe:/o:alpine:alpine_linux:3.15
        affectedPackage: go
        affectedVersion:
          fullName: 1.16.13
          kind: NORMAL
          name: 1.16.13
        effectiveSeverity: CRITICAL
        fixedCpeUri: cpe:/o:alpine:alpine_linux:3.15
        fixedPackage: go
        fixedVersion:
          fullName: 1.17.2
          kind: NORMAL
          name: 1.17.2
        packageType: GO_STDLIB
      relatedUrls:
      - label: More Info
        url: https://security-tracker.debian.org/tracker/CVE-2021-38297
      - label: More Info
        url: https://access.redhat.com/security/cve/CVE-2021-38297
      - label: More Info
        url: https://nvd.nist.gov/vuln/detail/CVE-2021-38297
      severity: HIGH
      shortDescription: CVE-2021-38297
    

The output of this command is a [list of occurrences in the Grafeas format](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.occurrences#Occurrence.VulnerabilityOccurrence). In this case, it shows one high-level severity vulnerability found in the image.

On-Demand Scanning identifies two types of Go package vulnerabilities:

  * `packageType:GO_STDLIB`. Go standard library vulnerabilities. This indicates that the vulnerability was found either in the Go toolchain used to build the binary, or in the standard library bundled with the toolchain. A possible fix is to upgrade your build toolchain.

  * `packageType:GO`. Go package vulnerabilities. This indicates that the vulnerability was found in a third-party package. A possible fix is to upgrade your dependent modules.




The scanning results are available for 48 hours after the scanning operation is completed.

## What's next

  * [Use the On-Demand Scanning API in your Cloud Build pipeline](https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild).
  * [Use Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) to scan and continuously update vulnerability information for your images stored in Artifact Registry.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
