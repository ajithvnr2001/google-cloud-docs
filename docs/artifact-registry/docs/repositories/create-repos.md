---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos/
title: Create standard repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:18.312085+00:00
---

# Create standard repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Create standard repositories Stay organized with collections  Save and categorize content based on your preferences. 

_Standard repositories_ are repositories for your private artifacts. You upload artifacts to and download artifacts directly from these repositories.

The following repository modes are also available for some artifact formats:

  * [Remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo) store artifacts from external sources such as Docker Hub, Maven Central, or PyPI.


  * [Virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo) act as a single access point to download, install, or deploy artifacts that are in upstream standard or remote repositories.



Each repository can contain artifacts for a single [supported format](https://docs.cloud.google.com/artifact-registry/docs/supported-formats).

**Note:** Ruby and Conda repositories are in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## Before you begin

  1. [Enable Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/enable-service), including enabling the Artifact Registry API and installing Google Cloud CLI.
  2. (Optional) [Configure defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).
  3. If you require customer-managed-encryption keys (CMEK) to encrypt repository content, [create and enable](https://docs.cloud.google.com/artifact-registry/docs/cmek) a key in Cloud KMS for the repository.



### Required roles

To get the permissions that you need to create repositories, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on the Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Warning:** Granting the `artifact-registry.repositories.create` permission to end users through the `roles/artifactregistry.admin` role is highly privileged. Do not grant this role to lower-trust users.

## Create a standard repository

When you create a repository, you must configure the following settings that cannot be changed after the repository is created:

  * Artifact format.


  * Repository mode, if multiple modes are available for the selected format.


  * Repository [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations).
  * Encryption with Google-owned and Google-managed encryption keys or [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek). Artifact Registry uses Google-owned and Google-managed encryption keys by default.



Artifact Registry enforces [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that require CMEK to encrypt resources or limit which Cloud KMS keys can be used for CMEK protection.

### Create a repository using the Google Cloud console

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Specify the repository name. For each repository location in a project, repository names must be unique.

  4. Select the repository format.

  5. If multiple repository modes are available, select **Standard**.

  6. **Maven only** : Configure the version policy.

     1. Choose a version policy:

        * **None** \- No version policy. Store both release and snapshot packages.
        * **Release** \- Store only release packages.
        * **Snapshot** \- Store only snapshot packages.
     2. If you want a snapshot repository to accept non-unique snapshots that overwrite existing versions in the repository, select **Allow snapshot overwrites**.

**Note:** Maven 3 only supports unique snapshots. If you are using snapshot repositories, we recommend using unique snapshots only.
  7. Under **Location Type** , choose the location for the repository:

     1. Choose the location type: Region or Multi-Region. The list of locations changes to reflect your selection.

     2. In the **Region** or **Multi-region** list, select a location.

For information about location types and supported locations, see [Repository locations](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations)

  8. Add a description for the repository. Descriptions help to identify the purpose of the repository and the kind of artifacts it contains.

Don't include sensitive data, because repository descriptions aren't encrypted.

  9. If you want to use [labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos) to organize your repositories, click **Add Label** and enter the key-value pair for the label. You can add, edit, or remove labels after you create the repository.

  10. In the **Encryption** section, choose the encryption mechanism for the repository.

     * **Google-managed encryption key** \- Encrypt repository content with a Google-owned and Google-managed encryption key.
     * **Customer-managed key** \- Encrypt repository content with a key that you control through Cloud Key Management Service. For key setup instructions, see [Setting up CMEK for repositories](https://docs.cloud.google.com/artifact-registry/docs/cmek).

     * For Docker repositories, the **Immutable image tags** setting configures your repository to use image tags that always point to the same image digest. A user with the Artifact Registry administrator role can change this setting after the repository is created.

       * By default this setting is disabled. Image tags are mutable, meaning that the image digest that the tag points to can change.
       * If this setting is enabled, image tags are immutable. A tag must always point to the same image digest. To learn more about mutable and immutable image tags, see [Container image versions](https://docs.cloud.google.com/artifact-registry/docs/docker/names#versions).
  11. If you want to use cleanup policies to delete unused artifacts, in the **Cleanup policies** section:

     1. Select **Dry run** to test your policy before applying it.
     2. Click **Add policy** to add a keep or delete policy to your repository.
     3. Give your cleanup policy a descriptive name in the **Name** field.
     4. In the **Policy type** section, select one of:

        * **Conditional delete** : deletes artifacts based on conditions you define.
        * **Conditional keep** : keeps artifacts based on conditions you define.
        * **Keep most recent versions** : Keeps a set number of most recent versions per package.

**Caution:** if you set **Package prefixes** for this policy, only artifacts matching the package prefixes will be kept, up to the number set for most recent versions.

For more details on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  12. In the **Artifact Analysis** section, choose vulnerability scanning settings:

     * **Enabled** \- Allow scanning in this repository. The Container Scanning API must be enabled on your project.

When you enable the Container Scanning API, billing begins immediately. After you enable the Container Scanning API on a project, vulnerability scanning is enabled for all new and existing repositories. When you push an image to Artifact Registry it's automatically scanned by Artifact Analysis.

     * **Disabled** \- Prevent scanning in this repository. If the Container Scanning API is enabled on your project, scanning continues on other repositories; this repository will be excluded.

For more information on vulnerability scanning options, see [Enable and disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).

  13. Click **Create**.




Artifact Registry creates the repository and adds it to the list of repositories.

After you have created the repository:

  * [Grant access](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the repository.
  * Configure Docker, package managers, and other third-party clients to authenticate to repositories. 

    * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication)
    * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication), [Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication)
    * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure)
    * Other: [Kubeflow Pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)



### Create a repository using the Google Cloud CLI

Run the command to create a new repository.

### Apt
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=apt \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



### Docker
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=docker \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --immutable-tags \
          --async \
          --disable-vulnerability-scanning
    

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique. 

    * `LOCATION`: the regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default location](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command:
          
          gcloud artifacts locations list

    * `DESCRIPTION`: a description of the repository. Don't include sensitive data, because repository descriptions aren't encrypted.
    * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/cmek) to encrypt repository contents. The path is in the format:
          
          projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

      * `KMS-PROJECT`: the project where your key is stored.
      * `KMS-LOCATION`: the location of the key.
      * `KEY-RING`: the name of the key ring.
      * `KEY`: the name of the key.
    * `--immutable-tags` is an optional flag that configures your repository to use tags that always point to the same image digest.

By default, when the `--immutable-tags` flag isn't passed, a tag can be moved to another image digest. To learn more about immutable and mutable image tags, see [Container image versions](https://docs.cloud.google.com/artifact-registry/docs/docker/names#versions).

    * `--async` returns immediately, without waiting for the operation in progress to complete.

    * `--disable-vulnerability-scanning`: is an optional flag that configures your repository to disable automatic vulnerability scanning.
    * `--allow-vulnerability-scanning`: is an optional flag that configures your repository to permit automatic vulnerability scanning. For more information, see [Enable or disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).



### Generic
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=generic \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



### Conda
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=conda \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



### Go
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=go \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



### KubeFlow Pipelines
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=kfp \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



### Maven

By default, Maven repositories store both [snapshot and release versions](https://docs.cloud.google.com/artifact-registry/docs/java#versions) of packages. You can specify a version policy to create a snapshot or release repository.

To create a repository that stores snapshots and releases, run the command:
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=maven \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



To store snapshot and release versions in different repositories, specify the version policy in the command:
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=maven \
          [--location=LOCATION] \
          [--description="DESCRIPTION"] \
          [--kms-key=KMS-KEY] \
          [--version-policy=VERSION-POLICY] \
          [--allow-snapshot-overwrites] \
          [--async] \
    

The following flags are specific to Maven repositories:

`--version-policy=VERSION-POLICY`
    

Specifies the types of packages to store in the repository. You can set VERSION-POLICY to:

  * `None` \- No version policy. Store both release and snapshot packages. If you do not include the `--version-policy` flag in your command, this is the default setting.
  * `Release` \- Store only release packages.
  * `Snapshot` \- Store only snapshot packages.



`--allow-snapshot-overwrites`

    

For snapshot repositories only. If you specify this flag, you can publish non-unique snapshots that overwrite existing versions in the repository.

**Note:** Maven 3 only supports unique snapshots. If you are using snapshot repositories, we recommend using unique snapshots only. 

### npm
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=npm \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



### Python
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=python \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



### Ruby
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=ruby \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



### Yum
    
    
      gcloud artifacts repositories create REPOSITORY \
          --repository-format=yum \
          --location=LOCATION \
          --description="DESCRIPTION" \
          --kms-key=KMS-KEY \
          --async
      

Replace the following:

  * `REPOSITORY`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command: 
        
        gcloud artifacts locations list

  * `DESCRIPTION`: a description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  * `KMS-KEY`: the full path to the Cloud KMS encryption key, if you are using a [customer-managed encryption key](https://docs.cloud.google.com/artifact-registry/docs/repositories/cmek) to encrypt repository contents. The path is in the format: 
        
        projects/KMS-PROJECT/locations/KMS-LOCATION/keyRings/KEY-RING/cryptoKeys/KEY

Replace the following:

    * `KMS-PROJECT`: the project where your key is stored.
    * `KMS-LOCATION`: the location of the key.
    * `KEY-RING`: the name of the key ring.
    * `KEY`: the name of the key.
  * `--async`: returns immediately, without waiting for the operation in progress to complete.



Artifact Registry creates your repository. Run the following command to view a description of the repository:
    
    
    gcloud artifacts repositories describe REPOSITORY \
        --location=LOCATION
    

After you have created the repository:

  * [Grant access](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the repository. 
  * [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) to delete unused artifacts. 
  * Configure Docker, package managers, and other third-party clients to authenticate to repositories. 

    * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication)
    * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication), [Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication)
    * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure)
    * Other: [Kubeflow Pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)



### Create a repository using Terraform

Use the [google_artifact_registry_repository](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository) resource to create repositories. [`terraform-provider-google`](https://github.com/hashicorp/terraform-provider-google) version `5.0.0` or newer is required.

If you are new to using Terraform for Google Cloud, see the [Get Started - Google Cloud](https://learn.hashicorp.com/collections/terraform/gcp-get-started) page on the HashiCorp website.

The following example defines the provider and a repository with the Terraform resource name `my-repo`.

### Apt
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "apt"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.




### Docker
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "docker"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            tag_state    = "TAG_STATE"
            tag_prefixes = ["TAG_PREFIX", "TAG_PREFIX_N"]
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            tag_state             = "TAG_STATE"
            tag_prefixes          = ["TAG_PREFIX", "TAG_PREFIX_N"]
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

  * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.




### Generic
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "generic"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            tag_state    = "TAG_STATE"
            tag_prefixes = ["TAG_PREFIX", "TAG_PREFIX_N"]
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            tag_state             = "TAG_STATE"
            tag_prefixes          = ["TAG_PREFIX", "TAG_PREFIX_N"]
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

  * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.




### Go
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "go"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            tag_state    = "TAG_STATE"
            tag_prefixes = ["TAG_PREFIX", "TAG_PREFIX_N"]
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            tag_state             = "TAG_STATE"
            tag_prefixes          = ["TAG_PREFIX", "TAG_PREFIX_N"]
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

  * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.




### KubeFlow Pipelines
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "kfp"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            tag_state    = "TAG_STATE"
            tag_prefixes = ["TAG_PREFIX", "TAG_PREFIX_N"]
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            tag_state             = "TAG_STATE"
            tag_prefixes          = ["TAG_PREFIX", "TAG_PREFIX_N"]
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

  * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.




### Maven

If you do not specify a version policy, Artifact Registry creates a Maven repository that stores both [snapshot and release versions](https://docs.cloud.google.com/artifact-registry/docs/java#versions) of packages by default. 
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "maven"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            tag_state    = "TAG_STATE"
            tag_prefixes = ["TAG_PREFIX", "TAG_PREFIX_N"]
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            tag_state             = "TAG_STATE"
            tag_prefixes          = ["TAG_PREFIX", "TAG_PREFIX_N"]
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

  * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.

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
        




### npm
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "npm"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            tag_state    = "TAG_STATE"
            tag_prefixes = ["TAG_PREFIX", "TAG_PREFIX_N"]
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            tag_state             = "TAG_STATE"
            tag_prefixes          = ["TAG_PREFIX", "TAG_PREFIX_N"]
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

  * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.




### Python
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "python"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            tag_state    = "TAG_STATE"
            tag_prefixes = ["TAG_PREFIX", "TAG_PREFIX_N"]
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            tag_state             = "TAG_STATE"
            tag_prefixes          = ["TAG_PREFIX", "TAG_PREFIX_N"]
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

  * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.




### Yum
    
    
      provider "google" {
          project = "PROJECT-ID"
      }  
      resource "google_artifact_registry_repository" "my-repo" {
        location = "LOCATION"
        repository_id = "REPOSITORY"
        description = "DESCRIPTION"
        format = "yum"
        kms_key_name = "KEY"
        cleanup_policy_dry_run = DRY_RUN_STATUS
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "DELETE"
          condition { 
            older_than   = "TIME_SINCE_UPLOAD"
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          condition { 
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
          }
        }
        cleanup_policies {
          id     = "POLICY_NAME"
          action = "KEEP"
          most_recent_versions {
            package_name_prefixes = ["PKG_PREFIX", "PKG_PREFIX_N"]
            keep_count            = KEEP_COUNT
          }
        }
      }
      

Replace the following:

  * `PROJECT-ID` is the Google Cloud project ID.
  * `LOCATION` is the repository location.
  * `REPOSITORY` is the repository name.
  * `DESCRIPTION` is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-owned and Google-managed encryption keys 
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository.

    * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode.
    * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies.

For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  * `POLICY_NAME` is the name of the cleanup policy. 

  * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.

  * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `KEEP_COUNT` is the number of versions of an artifact to keep in your repository.




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



## What's next

  * [List repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/list-repos).
  * [Label repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos).


  * [Tag repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos)


  * [Delete repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/delete-repos)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
