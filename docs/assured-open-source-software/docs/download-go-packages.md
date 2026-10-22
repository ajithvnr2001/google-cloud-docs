---
url: https://docs.cloud.google.com/assured-open-source-software/docs/download-go-packages/
title: Download Go packages using direct repository access for the free tier \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:17.404444+00:00
---

# Download Go packages using direct repository access for the free tier  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/download-go-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Download Go packages using direct repository access for the free tier Stay organized with collections  Save and categorize content based on your preferences. 

In the free tier, Assured Open Source Software packages are hosted in a Google-managed Artifact Registry repository.

This document explains how you can connect to the Artifact Registry repository for Assured OSS to directly access and download the Go packages.

This document applies to the free tier only. For the premium tier, see [Download Go packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-go-packages).

## Before you begin

  1. To get the permissions that you need to get the base64-encoded string of the service account key, ask your administrator to grant you the [Service Account Key Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. [Enable the Assured OSS free tier](https://docs.cloud.google.com/assured-open-source-software/docs/enable).

  3. [Validate connectivity](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection) to Assured OSS for the requested service accounts.

  4. [Enable the Artifact Registry API](https://docs.cloud.google.com/artifact-registry/docs/enable-service) for the parent Google Cloud project of the service accounts used to access Assured OSS.

  5. Install the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  6. If you've installed the Google Cloud CLI previously, check that you have the latest version by running this command:
         
         gcloud components update




## Set up authentication

To set up authentication, see [Set up authentication for Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication).

## Install Go packages

To install packages, see [Use a module as a dependency](https://docs.cloud.google.com/artifact-registry/docs/go/manage-modules#use_a_module_as_a_dependency).

## Access packages that aren't available in Assured OSS

You can configure access to packages that aren't available in the Artifact Registry repository for Assured OSS.

To configure access, when you set up authentication, configure the `GOPROXY` environment variable to include `https://proxy.golang.org`. Add `https://proxy.golang.org` directly to the comma-separated list after the Artifact Registry repository URL.

For example:
    
    
    export GOPROXY=https://us-go.pkg.dev/cloud-aoss/assuredoss-go-free,https://proxy.golang.org,direct
    

## List all Go packages available in Assured OSS

To use an [API](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts/list) to get a list of all the Go packages in the Artifact Registry repository, see [List all Go packages available in Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#list-go-packages).

## What's next

  * [Set up virtual repository access](https://docs.cloud.google.com/assured-open-source-software/docs/virtual-repository-access)
  * [Supported Go packages](https://docs.cloud.google.com/assured-open-source-software/docs/supported-packages-go)
  * [Access security metadata using Cloud Storage](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-cloud-storage)
  * [Access security metadata using Artifact Analysis API](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
