---
url: https://docs.cloud.google.com/artifact-analysis/docs/secret-scanning/
title: Scan for secrets \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:52.393361+00:00
---

# Scan for secrets  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/secret-scanning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Scan for secrets Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Artifact Analysis vulnerability scans can identify secrets, such as service account keys and API keys, stored in scanned images. You can view information about these secrets in the vulnerability scan's occurrence report and take action to prevent exposing sensitive information. 

## Overview

When a vulnerability scan detects a secret, Artifact Analysis creates a secret-type occurrence with details about the secret. Artifact Analysis can detect the following secrets:

#### Secrets

  * Anthropic admin keys
  * Anthropic API keys
  * Azure access tokens
  * Azure ID tokens
  * Docker hub personal access tokens
  * GitHub app refresh tokens
  * GitHub app server-to-server tokens
  * GitHub app user-to-server tokens
  * GitHub classic personal access tokens
  * GitHub fine-grained personal access tokens
  * GitHub OAuth tokens
  * Google Cloud OAuth2 (client ID & secret) pairs
  * Google Cloud OAuth2 access tokens
  * Google Cloud service account keys
  * Google Cloud API keys
  * Huggingface API keys
  * OpenAI API keys
  * Perplexity API keys
  * Stripe restricted keys
  * Stripe secret keys
  * Stripe webhook secrets



For detailed information about the different types of secrets in occurrence reports, see [`SecretKind`](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.occurrences#secretkind) in the Artifact Analysis API documentation.

Artifact Analysis can detect only secrets stored as text files. The following file extensions are supported:

  * `.cer`
  * `.cfg`
  * `.crt`
  * `.der`
  * `.env`
  * `.html`
  * `.key`
  * `.ipynb`
  * `.json`
  * `.log`
  * `.md`
  * `.pem`
  * `.py`
  * `.pypirc`
  * `.textproto`
  * `.toml`
  * `.txt`
  * `.xml`
  * `.yaml`



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Artifact Registry and Container Scanning APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,containerscanning.googleapis.com&redirect=https%3A//console.cloud.google.com)

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

  10. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Artifact Registry and Container Scanning APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,containerscanning.googleapis.com&redirect=https%3A//console.cloud.google.com)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init


**Important:** When you enable the Artifact Analysis API, Artifact Analysis automatically begins scanning each new image as they are pushed to Artifact Registry repositories in your project. However, scanning is disabled by default for packages pushed to Artifact Registry repositories. To enable scanning in a repository, see [Control scanning settings for an individual repository](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning#disable-repo).

Enabling this API also enables language package scanning in Artifact Registry. See [supported package types](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#feature-support).

## Required roles

To get the permissions that you need to scan images for secrets during vulnerability scans, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`)
  * [Container Analysis Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View secrets

To view secrets after a vulnerability scan, do the following:

  1. [Push a Docker image to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images).

  2. Wait for the vulnerability scan to complete.

  3. Run the following command to list secret occurrences for the scanned image:
         
         $ curl -G -H "Content-Type: application/json"   -H "Authorization: Bearer $(gcloud auth print-access-token)" --data-urlencode "filter=(kind=\"SECRET\" AND resourceUrl=\"RESOURCE_URL\")" https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/occurrences
         

Where:

     * PROJECT_ID is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository.
     * RESOURCE_URL is the URL of the scanned image, in the format `https://LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_ID`.

The following sample response shows a possible result. In this case, a Google Cloud API key named `my_api_key.yaml` was identified the `documents` directory of an image. The `secret` attribute shows information about the discovered secret.
    
    {
      "occurrences": [
        {
          "name": "projects/my-project/locations/us-east1/occurrences/45619d23-66b1-4f5b-9b12-9060d7f97ff3",
          "resourceUri": "https://us-east1-docker.pkg.dev/my-project/my-images/test-image-0106@sha256:73cf5b9a788dc391c40e9cf1599144d03875b5d2dc935988ebfef8260bd2678e",
          "noteName": "projects/my-project/locations/us-east1/notes/secret_kind_gcp_api_key",
          "kind": "SECRET",
          "createTime": "2026-01-06T21:16:14.905851Z",
          "updateTime": "2026-01-06T21:16:14.905851Z",
          "secret": {
            "kind": "SECRET_KIND_GCP_API_KEY",
            "locations": [
              {
                "fileLocation": {
                  "filePath": "documents/my_api_key.yaml",
                  "layerDetails": {
                    "index": 2,
                    "diffId": "7b76df10d6d90391830392eac96b0ef2d2d43822c6ff4754aa6daea0fe14a8c5",
                    "command": "COPY . . # buildkit",
                    "chainId": "sha256:75df0c59982f47cc38e730e1a122b67fceaaf7797d91e1fa17ffffc5cfe7ff59"
                  }
                }
              }
            ]
          }
        }
      ]
    }
    




## Limitations

  * While secret scanning is in public preview, secret-type occurrences are viewable only in the Container Analysis API.
  * Artifact Analysis secret scanning reports on, at most, one occurrence per secret per image. At most 1000 file locations per occurrence are returned.
  * False positives may occur with identified secrets. Always verify each identified secret before taking any action on your images.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
