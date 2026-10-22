---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-repo/
title: Create connector repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:28.512718+00:00
---

# Create connector repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Create connector repositories Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Connector repositories act as proxies to upstream sources and help ensure that all requests are handled by the upstream source. Unlike [remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo), connector repositories don't cache artifacts. As a result, connector repositories are useful if you require full auditability of upstream sources or if you must comply with third-party policies that prevent artifact caching.

This page describes how to create Artifact Registry connector repositories.

## Supported connector formats

Artifact Registry supports only Docker-format connector repositories.

## Before you begin

  1. [Enable the Artifact Registry API](https://docs.cloud.google.com/artifact-registry/docs/enable-service), and install the Google Cloud CLI.
  2. Optional: [configure defaults for the gcloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).
  3. If you require customer-managed-encryption keys (CMEK) to encrypt repository content, then [create and enable](https://docs.cloud.google.com/artifact-registry/docs/cmek) a key in Cloud KMS for the repository.
  4. Enable the Secret Manager API.
         
         gcloud services enable secretmanager.googleapis.com \
             --project=PROJECT_ID
         

  5. If Artifact Registry is in a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) service perimeter, then enable the Access Context Manager API if it is not already enabled.
         
         gcloud services enable accesscontextmanager.googleapis.com \
             --project=PROJECT_ID
         




### Required roles

To get the permissions that you need to manage repositories, ask your administrator to grant you the following IAM roles: 

  * Create connector repositories and grant access to individual repositories: [Artifact Registry Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) on the project 
  * Save your upstream repository credentials in a secret version: [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) on the project 
  * Grant access to upstream sources outside a VPC Service Controls service perimeter: [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) on on the organization of the resource where the access policy is applied 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Warning:** Granting the `artifact-registry.repositories.create` permission to end users through the `roles/artifactregistry.admin` role is highly privileged. Do not grant this role to lower-trust users.

## Create a connector repository

When you create a connector repository, you must configure the following settings, which can't be changed after the repository is created:

  * The artifact format, which can only be Docker.
  * Repository [mode](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode) set to connector.
  * Connector repository upstream source.
  * Repository [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations).
  * Encryption with Google-owned and Google-managed encryption keys or [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek). Artifact Registry uses Google-owned and Google-managed encryption keys by default.



Artifact Registry enforces [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that require CMEK to encrypt resources or limit which Cloud KMS keys can be used for CMEK protection.

###  console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Specify the repository name. For each repository location in a project, repository names must be unique.

  4. In the **Format** section, select **Docker**.

  5. In the **Repository mode** section, select **Connector**.

  6. In the **Connector repository source** section, select one of the following options:

     * **Docker Hub** : The connector uses Docker Hub (`https://docker.io`) as the upstream repository.
     * **Custom** : The connector uses a different Docker upstream URL for the upstream repository.
  7. If you select **Custom** , then in the **Custom repository** field, enter the full repository URL. The URL cannot be changed after the repository is created.

For examples of some common upstream URLs, see [Custom upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview#ar-upstreams).

  8. In the **Connector repository authentication mode** section, enter the following:

     1. A username for your upstream repository.
     2. A secret to store your credentials in Secret Manager.

You can edit these values after you create the repository.

**Note:** You can add authentication to an unauthenticated repository after you create the repository, but you can't change an authenticated repository to an unauthenticated repository after you create it.
  9. In the **Location Type** section, choose the location for the repository:

     1. Choose the location type: Region or Multi-Region. The list of locations changes to reflect your selection.

     2. In the **Region** or **Multi-region** list, select a location.

For information about location types and supported locations, see [Repository locations](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations)

  10. Add a description for the repository. Descriptions help you to identify the purpose of the repository and the kind of artifacts it contains.

Don't include sensitive data, since repository descriptions are not encrypted.

  11. If you want to use [labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos) to organize your repositories, click **Add Label** and enter the key-value pair for the label. You can add, edit, or remove labels after you create the repository.

  12. In the **Encryption** section, choose the encryption mechanism for the repository.

     * **Google-managed encryption key** \- Encrypt repository content with a Google-owned and Google-managed encryption key.
     * **Customer-managed key** \- Encrypt repository content with a key that you control through Cloud Key Management Service. For key setup instructions, see [Setting up CMEK for repositories](https://docs.cloud.google.com/artifact-registry/docs/cmek).
  13. In the **Artifact Analysis** section, choose vulnerability scanning settings:

     * **Enabled** \- Allow scanning in this repository. The Container Scanning API must be enabled on your project.

When you enable the Container Scanning API, billing begins immediately. After you enable the Container Scanning API on a project, vulnerability scanning is enabled for all new and existing repositories. When you push an image to Artifact Registry it's automatically scanned by Artifact Analysis.

     * **Disabled** \- Prevent scanning in this repository. If the Container Scanning API is enabled on your project, scanning continues on other repositories; this repository will be excluded.

For more information on vulnerability scanning options, see [Enable and disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).

  14. Click **Create**.




Artifact Registry creates the repository and adds it to the list of repositories.

###  gcloud CLI 

To create a connector repository, run the command to create either a Docker connector repository or a custom connector repository.
    
    
      gcloud artifacts repositories create CONNECTOR-REPOSITORY-NAME \
          --project=PROJECT_ID \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --repository-format=docker \
          --mode=connector-repository \
          --remote-docker-repo="UPSTREAM-NAME" \
          --remote-username="USERNAME" \
          --remote-password-secret-version="PASSWORD" \
    

The `--mode=connector-repository` flag is required to define the repository as a connector repository. The `--repository-format` must be `docker`.

Replace the following:

  * `CONNECTOR-REPOSITORY-NAME`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `PROJECT_ID`: the project ID. If this flag is omitted, the current or default project is used.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * `DESCRIPTION`: optional. A description of the connector repository. Don't include sensitive data, because repository descriptions aren't encrypted.
  * `UPSTREAM-NAME`: the preset upstream name or user-defined URL of the upstream repository.
  * `USERNAME`: optional. Your username for authenticating to the upstream repository.
  * `PASSWORD`: optional. The secret version containing your upstream repository password.



For example, the following command creates a connector repository named `my-connector-repo`, which connects an upstream Jfrog repository to the Google Cloud project `my-project`. The full URL of the upstream repository is `https://my-account.jfrog.io/scoped-repo`.
    
    
    gcloud artifacts repositories create my-connector-repo \
        --project=my-project \
        --location=us-east1 \
        --repository-format=docker \
        --mode=connector-repository \
        --remote-docker-repo=https://my-account.jfrog.io/scoped-repo \
        --remote-username=my-username \
        --remote-password-secret-version=projects/my-project/secrets/my-secret/versions/1
    

For more information about authenticating to upstream repositories, see [Authenticate connector repositories to upstream sources](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-connector-authentication).

###  Terraform 

Use the [google_artifact_registry_repository](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository) resource to create repositories. [`terraform-provider-google`](https://github.com/hashicorp/terraform-provider-google) version `5.0.0` or newer is required.

If you are new to using Terraform for Google Cloud, see the [Get Started - Google Cloud](https://learn.hashicorp.com/collections/terraform/gcp-get-started) page on the HashiCorp website.

The following example defines the provider and a connector repository with the [Terra](https://terrapkg.com/) resource name `my-repo`.
    
    
    ```hcl
    provider "google" {
        project = "PROJECT-ID"
    }
    
    resource "google_artifact_registry_repository" "NAME" {
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "DESCRIPTION"
      format        = "docker"
      mode          = "REMOTE_REPOSITORY"
    
      # Setting mode="REMOTE_REPOSITORY" and no_cache() together configures the repository as a connector-type repository.
      remote_repository_config {
        description = "CONFIG_DESCRIPTION"
        docker_repository {
          public_repository = "DOCKER_HUB"
        }
        no_cache {}
      }
    }
    ```
    
    Replace the following:
    
      * `PROJECT-ID`: the Google Cloud project ID.
      * `NAME`: the name of your repository.
      * `LOCATION`: the repository location.
      * `REPOSITORY_ID`: the repository ID.
      * `DESCRIPTION`: optional. A description for the repository.
        Do not include sensitive data. Repository descriptions are
        not encrypted.
      * `KEY`: the name of the Cloud Key Management Service key, if you are using
        [customer-managed encryption keys][cmek] (CMEK) for encryption. Omit
        this argument to use the default setting, Google-managed encryption
        keys.
      * `CONFIG_DESCRIPTION`: optional. A description of the remote
        source.
    

After you have created the repository, do the following:

  * [Grant access](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the repository.
  * Configure Docker, package managers, and other third-party clients to authenticate to repositories. 
    * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication)
    * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication), [Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication)
    * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure)
    * Other: [Kubeflow Pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)
  * Configure Artifact Registry connector repositories to [authenticate to their upstream sources](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-connector-authentication).



## Edit repository descriptions

You can change the repository description from Google Cloud console or the gcloud CLI.

### Console

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the repository and click **Edit Repository**.

  3. Edit the repository description and then click **Save**.




### gcloud

To update the repository description, run the command:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT \
        --location=LOCATION \
        --description="DESCRIPTION"
    

Replace the following:

  * `REPOSITORY`: the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, then you can omit this flag to use the default.
  * `PROJECT`: the Google Cloud project ID. If this flag is omitted, then the current or default project is used.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, then you can omit this flag to use the default.
  * `DESCRIPTION`: a description for the repository.



## Access to upstream sources in a service perimeter

Services in a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) service perimeter have restricted access to resources outside the perimeter.

You can allow or deny access to upstream sources within a specified Google Cloud project and location.

By default, Artifact Registry denies access to upstream sources if you have not explicitly granted access.

For Artifact Registry the required role is the Artifact Registry Administrator (`roles/artifactregistry.admin`).

### View settings for upstream sources

To view the configuration for a specific project and location combination, run the following command:
    
    
    gcloud artifacts vpcsc-config describe \
        --project=PROJECT_ID \
        --location=LOCATION
    

For example, use the following command to view settings for connector repositories in `us-east1` in the project `my-project`:
    
    
    gcloud artifacts vpcsc-config describe \
        --project=my-project \
        --location=us-east1
    

### Allow access to upstream sources

To allow access to upstream sources in a specified location, run the command:
    
    
    gcloud artifacts vpcsc-config allow \
        --project=PROJECT_ID \
        --location=LOCATION
    

For example, use the following command to allow all connector repositories in `us-east1` in the project `my-project` to access their upstream sources outside of the perimeter:
    
    
    gcloud artifacts vpcsc-config allow \
        --project=my-project \
        --location=us-east1
    

### Deny access to upstream sources

To deny access to upstream sources in a specified location, run the command:
    
    
    gcloud artifacts vpcsc-config deny \
        --project=PROJECT_ID \
        --location=LOCATION
    

For example, use the following command to block access to upstream sources outside of the perimeter for all connector repositories in `us-west1` in the project `my-project`:
    
    
    gcloud artifacts vpcsc-config deny \
        --project=my-project \
        --location=us-west1
    

## What's next

  * Learn more about Artifact Registry [connector repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview).
  * [Authenticate connector repositories to upstream sources](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-connector-authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
