---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo/
title: Create virtual repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:22.309668+00:00
---

# Create virtual repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Create virtual repositories Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create Artifact Registry virtual repositories.

Virtual repositories act as a single access point to download, install, or deploy artifacts in the same format from one or more _upstream repositories_. An upstream repository can be a Artifact Registry standard or remote repository.

For more information about how virtual repositories work, see the [Virtual repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview).

## Before you begin

[Enable Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/enable-service), including enabling the Artifact Registry API and installing the latest version of Google Cloud CLI.

### Required roles

To get the permissions that you need to manage repositories, ask your administrator to grant you the following IAM roles: 

  * Create virtual repositories and grant access to individual repositories: [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) on the Google Cloud project 
  * Grant access to repositories at the project level: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the Google Cloud project 
  * Grant access to repositories at the folder level: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) on the folder 
  * Grant access to repositories at the organization level: [Organization Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) on the Google Cloud organization 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Warning:** Granting the `artifact-registry.repositories.create` permission to end users through the `roles/artifactregistry.admin` role is highly privileged. Do not grant this role to lower-trust users.

If upstream repositories are in other projects, an administrator in the projects with upstream repositories must have permissions to manage access to those repositories.

## Create upstream repositories

Before setting up a virtual repository, create the upstream repositories that you want to make available with the virtual repository.

  1. Create the upstream repositories in the same Google Cloud region where you plan to create the virtual repository.

     * [Create a standard repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos)
     * [Create a remote repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo)
  2. Virtual repositories use the [Artifact Registry Service Agent](https://docs.cloud.google.com/artifact-registry/docs/ar-service-account) to authenticate to upstream repositories. You must grant the service agent read access to upstream repositories.

You can grant the Artifact Registry Reader role to the Artifact Registry service agent at the project level so that you do not need to grant access to individual upstream repositories.

In each project with upstream repositories, run the following command:
         
         gcloud projects add-iam-policy-binding UPSTREAM_PROJECT_ID \
             --member serviceAccount:service-VIRTUAL-REPO-PROJECT_NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com \
             --role roles/artifactregistry.reader
         

Where

     * UPSTREAM_PROJECT_ID is the ID of the Google Cloud project with the upstream repository.
     * VIRTUAL_REPO_PROJECT_NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project for your virtual repository.

Alternatively, if you want to grant more narrowly-scoped role to the service agent, add the permission `artifactregistry.repositories.readViaVirtualRepository` to a custom role and then grant that role to the service agent.

For more information about granting permissions, see the [access control](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) documentation.




## Create a virtual repository

When you create a repository, you must configure the following settings that cannot be changed after the repository is created:

  * Artifact format.
  * Repository mode, if multiple modes are available for the selected format.
  * Repository [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations).
  * Encryption with Google-owned and Google-managed encryption keys or [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek). Artifact Registry uses Google-owned and Google-managed encryption keys by default.



Artifact Registry enforces [organization policy constraints](https://docs.cloud.google.com/kms/docs/cmek-org-policy) that require CMEK to encrypt resources or limit which Cloud KMS keys can be used for CMEK protection.

###  Google Cloud console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Specify the repository name. For each repository location in a project, repository names must be unique.

  4. Select the repository format.

  5. Under **Repository mode** , select **Virtual**.

  6. Under **Virtual Repository Upstreams** , click **Add Upstream** to add an upstream repository.

     * An upstream repository can be a standard, remote, or virtual repository.
     * An upstream repository must be in the same location as the virtual repository, but can be in a different Google Cloud project.
     * An upstream repository must be the same artifact format as the virtual repository.

Specify a [priority](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview#repo-priority) and policy name for each upstream repository. Higher priority values take precedence over lower values. For example, a value of `10` is treated as higher priority than a value of `1`. Leave space between priority values so that there is flexibility to add upstream repositories with priorities that are in between existing values.

  7. Under **Location Type** , choose the location for the repository:

     1. Choose the location type: Region or Multi-Region. The list of locations changes to reflect your selection.

     2. In the **Region** or **Multi-region** list, select a location.

For information about location types and supported locations, see [Repository locations](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations)

  8. Add a description for the repository. Descriptions help to identify the purpose of the repository and the kind of artifacts it contains.

Do not include sensitive data, because repository descriptions aren't encrypted.

  9. If you want to use [labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos) to organize your repositories, click **Add Label** and enter the key-value pair for the label. You can add, edit, or remove labels after you create the repository.

  10. In the **Encryption** section, choose the encryption mechanism for the repository.

     * **Google-managed encryption key** \- Encrypt repository content with a Google-owned and Google-managed encryption key.
     * **Customer-managed key** \- Encrypt repository content with a key that you control through Cloud Key Management Service. For key setup instructions, see [Setting up CMEK for repositories](https://docs.cloud.google.com/artifact-registry/docs/cmek).
  11. Click **Create**.




Artifact Registry creates the repository and adds it to the list of repositories.

After you have created the repository:

  * [Grant access](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the repository.
  * Configure Docker, package managers, and other third-party clients to authenticate to repositories.

    * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication)
    * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication), [Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication)
    * Other: [Kubeflow Pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)



###  gcloud CLI 

To create a virtual repository, you define your upstream repositories in a policy file and then create the repository using the policy file.

  1. Create an upstream policy file in JSON format with the following settings:
         
         [{
         "id" : "POLICY_ID",
         "repository" : "UPSTREAM_REPOSITORY_RESOURCE_NAME",
         "priority" : PRIORITY
         }, {...}]
         

Replace the following:

     * `POLICY_ID`: a name for the policy. Each upstream repository in the policy must have a unique policy ID.
     * `UPSTREAM_REPO_RESOURCE_NAME`: the name of the upstream repository in the format:
           
           projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY
           

       * An upstream repository can be a standard, remote, or virtual repository.
       * An upstream repository must be in the same location as the virtual repository, but can be in a different Google Cloud project.
       * An upstream repository must be the same artifact format as the virtual repository.
     * `PRIORITY` is an integer that indicates the [priority](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview#repo-priority) for the upstream repository. Higher priority values take precedence over lower values. For example, a value of `10` is treated as higher priority than a value of `1`.

The following example shows a policy file named `policies.json` with four upstream repositories. `upstream1` has the highest value for `priority`, so Artifact Registry will search it first. `upstream-test` has the lowest `priority` value, so Artifact Registry will search it last. `upstream2` and `upstream3` have the same priority. If Artifact Registry finds a requested package in repositories with the same priority, it can serve the package from either repository.
    
    [{
    "id" : "upstream1",
    "repository" : "projects/myproject/locations/us-west1/repositories/python-repo1",
    "priority" : 100
    }, {
    "id" : "upstream2",
    "repository" : "projects/myproject/locations/us-west1/repositories/python-repo2",
    "priority" : 80
    }, {
    "id" : "upstream3",
    "repository" : "projects/myproject/locations/us-west1/repositories/python-repo2",
    "priority" : 80
    }, {
    "id" : "upstream-test",
    "repository" : "projects/myproject/locations/us-west1/repositories/python-test-repo",
    "priority" : 20
    }]
    

This example also leaves space between the priority values. These gaps provide flexibility to add upstream repositories with priorities that are in between existing values. For example, you can add an `upstream-3` repository with a priority of `70` so that Artifact Registry searches it before `upstream-test`.

Consider storing your upstream policy file in your source control system so that you can reuse it later to make changes to upstream repository settings and track historical changes.

  2. In the directory with your upstream policy file, run the following command to create the virtual repository:
         
         gcloud artifacts repositories create VIRTUAL-REPOSITORY-NAME \
             --project=PROJECT_ID \
             --repository-format=FORMAT \
             --mode=virtual-repository \
             --location=LOCATION \
             --description="DESCRIPTION" \
             --upstream-policy-file=UPSTREAM_POLICY_FILE
         

Replace the following:

     * `VIRTUAL-REPOSITORY-NAME`: the name of the virtual repository.
     * `PROJECT_ID`: the ID of the project where you are creating the virtual repository. If this flag is omitted, the current or default project is used.
     * `FORMAT`: the format of the repository. The following values are available: 
       * `apt` (private preview)
       * `docker`
       * `go`
       * `maven`
       * `npm`
       * `python`
       * `yum` (private preview)
     * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command:
           
           gcloud artifacts locations list
           

     * `DESCRIPTION`: optional. a description of the repository. Do not include sensitive data, Repository descriptions aren't encrypted.

     * `UPSTREAM_POLICY_FILE`: the path to the upstream policy file.

For example the following command creates a virtual repository named `virtual-repo` for Python packages in the region `us-west1` with settings in `policies.json`.
    
    gcloud artifacts repositories create virtual-repo \
    --repository-format=python \
    --mode=virtual-repository \
    --location=us-west1 \
    --description="Python virtual repository" \
    --upstream-policy-file=policies.json
    




Artifact Registry creates the virtual repository.

###  Terraform 

Use the [google_artifact_registry_repository](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository) resource to create repositories. [`terraform-provider-google`](https://github.com/hashicorp/terraform-provider-google) version `5.0.0` or newer is required.

If you are new to using Terraform for Google Cloud, see the [Get Started - Google Cloud](https://learn.hashicorp.com/collections/terraform/gcp-get-started) page on the HashiCorp website.

The following example defines the provider, a virtual repository with the Terraform resource name `my-repo` and an upstream repository with the Terraform resource name `my-repo-upstream`.

###  Docker 
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    resource "google_artifact_registry_repository" "my-repo-upstream" {
      location      = "UPSTREAM_LOCATION"
      repository_id = "UPSTREAM_REPOSITORY_ID"
      description   = "UPSTREAM_REPOSITORY_DESCRIPTION"
      format        = "docker"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      depends_on    = []
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "VIRTUAL_REPOSITORY_DESCRIPTION"
      format        = "docker"
      kms_key_name = "KEY"
      mode          = "VIRTUAL_REPOSITORY"
      virtual_repository_config {
        upstream_policies {
          id          = "UPSTREAM_REPOSITORY_ID"
          repository  = google_artifact_registry_repository.my-repo-upstream.id
          priority    = PRIORITY
        }
      }
    }
    

Where

  * PROJECT-ID is the Google Cloud project ID.
  * UPSTREAM_LOCATION is the upstream repository location. Note that the virtual repository and upstream must be in the same region or multi-region.
  * UPSTREAM_REPOSITORY_ID is the upstream repository ID.
  * UPSTREAM_REPOSITORY_DESCRIPTION is the optional description of the upstream repository.
  * LOCATION is the virtual repository location.
  * REPOSITORY_ID is the virtual repository ID.
  * DESCRIPTION is the optional description for the virtual repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * KEY is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys.
  * PRIORITY is the optional priority value. Artifact Registry evaluates priorities in descending order. For example, a value of `10` is treated as higher priority than a value of `1`. Entries with a higher priority value take precedence in the pull order.



###  Maven 

If you do not specify a version policy, Artifact Registry creates a Maven repository that stores both [snapshot and release versions](https://docs.cloud.google.com/artifact-registry/docs/java#versions) of packages by default.
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    resource "google_artifact_registry_repository" "my-repo-upstream" {
      location      = "UPSTREAM_LOCATION"
      repository_id = "UPSTREAM_REPOSITORY_ID"
      description   = "UPSTREAM_REPOSITORY_DESCRIPTION"
      format        = "maven"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      depends_on    = []
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "VIRTUAL_REPOSITORY_DESCRIPTION"
      format        = "maven"
      kms_key_name = "KEY"
      mode          = "VIRTUAL_REPOSITORY"
      virtual_repository_config {
        upstream_policies {
          id          = "UPSTREAM_REPOSITORY_ID"
          repository  = google_artifact_registry_repository.my-repo-upstream.id
          priority    = PRIORITY
        }
      }
    }
    

Where

  * PROJECT-ID is the Google Cloud project ID.
  * UPSTREAM_LOCATION is the upstream repository location. Note that the virtual repository and upstream must be in the same region or multi-region.
  * UPSTREAM_REPOSITORY_ID is the upstream repository ID.
  * UPSTREAM_REPOSITORY_DESCRIPTION is the optional description of the upstream repository.
  * LOCATION is the virtual repository location.
  * REPOSITORY_ID is the virtual repository ID.
  * DESCRIPTION is the optional description for the virtual repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * KEY is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys.
  * PRIORITY is the optional priority value. Artifact Registry evaluates priorities in descending order. For example, a value of `10` is treated as higher priority than a value of `1`. Entries with a higher priority value take precedence in the pull order.



To store snapshot and release versions in different repositories, specify a version policy for the repository using a `maven_config` block. This block supports the following settings:

  * `version_policy` sets the version policy with one of the following values: 
    * `VERSION_POLICY_UNSPECIFIED`: Store snapshot and release packages. This is the default setting.
    * RELEASE: Store release packages only.
    * SNAPSHOT: Store snapshot packages only.
  * `allow_snapshot_overwrites` configures a repository with a `SNAPSHOT` version policy to accept non-unique snapshots that overwrite existing versions in the repository.

**Note:** Maven 3 only supports unique snapshots. If you are using snapshot repositories, we recommend using unique snapshots only.

The following example defines a Maven repository with a release version policy.
    
    
    provider "google" {
    project = "my-project"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
    provider = google-beta
    
    location = "us-central1"
    repository_id = "my-repo"
    description = "Maven repository"
    format = "MAVEN"
    maven_config {
      version_policy = "RELEASE"
    }
    }
    

###  npm 
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    resource "google_artifact_registry_repository" "my-repo-upstream" {
      location      = "UPSTREAM_LOCATION"
      repository_id = "UPSTREAM_REPOSITORY_ID"
      description   = "UPSTREAM_REPOSITORY_DESCRIPTION"
      format        = "npm"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      depends_on    = []
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "VIRTUAL_REPOSITORY_DESCRIPTION"
      format        = "npm"
      kms_key_name = "KEY"
      mode          = "VIRTUAL_REPOSITORY"
      virtual_repository_config {
        upstream_policies {
          id          = "UPSTREAM_REPOSITORY_ID"
          repository  = google_artifact_registry_repository.my-repo-upstream.id
          priority    = PRIORITY
        }
      }
    }
    

Where

  * PROJECT-ID is the Google Cloud project ID.
  * UPSTREAM_LOCATION is the upstream repository location. Note that the virtual repository and upstream must be in the same region or multi-region.
  * UPSTREAM_REPOSITORY_ID is the upstream repository ID.
  * UPSTREAM_REPOSITORY_DESCRIPTION is the optional description of the upstream repository.
  * LOCATION is the virtual repository location.
  * REPOSITORY_ID is the virtual repository ID.
  * DESCRIPTION is the optional description for the virtual repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * KEY is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys.
  * PRIORITY is the optional priority value. Artifact Registry evaluates priorities in descending order. For example, a value of `10` is treated as higher priority than a value of `1`. Entries with a higher priority value take precedence in the pull order.



###  Python 
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    resource "google_artifact_registry_repository" "my-repo-upstream" {
      location      = "UPSTREAM_LOCATION"
      repository_id = "UPSTREAM_REPOSITORY_ID"
      description   = "UPSTREAM_REPOSITORY_DESCRIPTION"
      format        = "python"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      depends_on    = []
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "VIRTUAL_REPOSITORY_DESCRIPTION"
      format        = "python"
      kms_key_name = "KEY"
      mode          = "VIRTUAL_REPOSITORY"
      virtual_repository_config {
        upstream_policies {
          id          = "UPSTREAM_REPOSITORY_ID"
          repository  = google_artifact_registry_repository.my-repo-upstream.id
          priority    = PRIORITY
        }
      }
    }
    

Where

  * PROJECT-ID is the Google Cloud project ID.
  * UPSTREAM_LOCATION is the upstream repository location. Note that the virtual repository and upstream must be in the same region or multi-region.
  * UPSTREAM_REPOSITORY_ID is the upstream repository ID.
  * UPSTREAM_REPOSITORY_DESCRIPTION is the optional description of the upstream repository.
  * LOCATION is the virtual repository location.
  * REPOSITORY_ID is the virtual repository ID.
  * DESCRIPTION is the optional description for the virtual repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * KEY is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys.
  * PRIORITY is the optional priority value. Artifact Registry evaluates priorities in descending order. For example, a value of `10` is treated as higher priority than a value of `1`. Entries with a higher priority value take precedence in the pull order.



Artifact Registry creates your repository. Run the following command to view a description of the repository:
    
    
    gcloud artifacts repositories describe REPOSITORY \
        --location=LOCATION
    

After you have created the repository:

  * [Grant access](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the repository.
  * Configure Docker, package managers, and other third-party clients to authenticate to repositories.

    * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication)
    * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication), [Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication)
    * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure)
    * Other: [Kubeflow Pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)



## Update upstream repositories

You can change the list of upstream repositories or adjust the priority of upstream repositories.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the virtual repository and click **Edit Repository**.

  3. In the **Virtual Repository Upstream** list, make the required changes. You can add and remove repositories or change the priority of repositories in the list

  4. Click **Save**.




###  gcloud 

  1. Edit your upstream policy file with your changes. For example, you might want to add an upstream repository or adjust priority settings.

If you want to remove all upstream repositories, your policy file should contain an empty set of repositories.
         
         []
         

  2. Run the following command to apply your changes to the virtual repository.
         
         gcloud artifacts repositories update REPOSITORY \
             --upstream-policy-file=UPSTREAM_POLICY_FILE
         

Replace `UPSTREAM_POLICY_FILE` with the path to the upstream policy file.

For more information about the command, see the [gcloud artifacts repositories update](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update) reference documentation.




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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
