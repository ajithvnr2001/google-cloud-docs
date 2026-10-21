---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo/
title: Create remote repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:18.936951+00:00
---

# Create remote repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Create remote repositories Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create Artifact Registry remote repositories.

_Remote repositories_ store artifacts from the following upstream sources:

  * Standard Artifact Registry repositories.
  * External sources such as the following: 
    * CentOS
    * Debian
    * Docker Hub
    * GitHub Container Registry (ghcr.io)
    * Maven Central
    * The Python Package Index (PyPI)



A remote repository acts as a proxy for the upstream source so that you have more control over your dependencies. The first time that you request a version of a package, Artifact Registry downloads and caches the package in the remote repository. The next time you request the same package version, Artifact Registry serves the cached copy.

If you request an artifact from an upstream source that doesn't exist, or doesn't contain the version you specified, then the request will fail.

For more details on how remote repositories work, see the [Remote repository overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview).

## Before you begin

  1. [Enable Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/enable-service), including enabling the Artifact Registry API and installing Google Cloud CLI.
  2. Optional: [configure defaults for the gcloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).
  3. If you require customer-managed-encryption keys (CMEK) to encrypt repository content, then [create and enable](https://docs.cloud.google.com/artifact-registry/docs/cmek) a key in Cloud KMS for the repository.
  4. If you want to authenticate to an upstream repository, then enable the Secret Manager API.
         
         gcloud services enable secretmanager.googleapis.com \
             --project=PROJECT_ID
         

  5. If Artifact Registry is in a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) service perimeter, then enable the Access Context Manager API if it is not already enabled.
         
         gcloud services enable accesscontextmanager.googleapis.com \
             --project=PROJECT_ID
         

  6. If you want to set an Artifact Registry repository as your upstream, and it's in a different project than your remote repository, then you need to grant the service account for the remote repository project access to the upstream repository project before creating the remote repository.

Grant the Service Agent role

Artifact Registry remote repositories use the [Artifact Registry Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#artifact-registry-service-agent) to authenticate to Artifact Registry upstream repositories. You must grant the service agent read access to the upstream repository. 

To grant the service agent the [Artifact Registry Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.serviceAgent) on the upstream repository, run the following command: 
         
           gcloud artifacts repositories add-iam-policy-binding UPSTREAM_REPOSITORY \
               --member serviceAccount:service-REMOTE_PROJECT_NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com \
               --location=LOCATION \
               --project=UPSTREAM_PROJECT_ID \
               --role roles/artifactregistry.serviceAgent
           

Replace the following: 

     * UPSTREAM_REPOSITORY is the ID of the upstream repository. Artifact Registry upstream repositories must be standard mode repositories.
     * REMOTE_PROJECT_NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project for your remote repository.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
     * UPSTREAM_PROJECT_ID is the ID of the Google Cloud project with the upstream repository.



### Required roles

To get the permissions that you need to manage repositories, ask your administrator to grant you the following IAM roles: 

  * Create remote repositories and grant access to individual repositories: [Artifact Registry Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) on the project 
  * Save your upstream repository credentials in a secret version: [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) on the project 
  * Grant access to upstream sources outside a VPC Service Controls service perimeter: [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) on on the organization of the resource where the access policy is applied 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Warning:** Granting the `artifact-registry.repositories.create` permission to end users through the `roles/artifactregistry.admin` role is highly privileged. Do not grant this role to lower-trust users.

## Create a remote repository

When you create a remote repository, you must configure the following settings, which can't be changed after the repository is created:

  * Artifact [format](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-formats).
  * Repository [mode](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode) set to remote.
  * Remote repository upstream source.
  * Repository [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations).
  * Encryption with Google-owned and Google-managed encryption keys or [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek). Artifact Registry uses Google-owned and Google-managed encryption keys by default.



Artifact Registry enforces [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that require CMEK to encrypt resources or limit which Cloud KMS keys can be used for CMEK protection.

###  console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Specify the repository name. For each repository location in a project, repository names must be unique.

  4. In the **Format** section, select the repository format.

  5. In the **Repository mode** section, select **Remote**.

  6. In the **Remote repository source** section, select one of the following ways to enter your upstream repository URL:

     * Select the listed [preset upstream](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#preset-upstreams) source for your format type.
     * Select **Custom** to specify the full URL to a public or private repository for [supported formats](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-formats).
     * Select **Artifact Registry repository** to select a standard Artifact Registry repository.
  7. If you selected **Custom** , then in the **Custom repository** field, enter the full repository URL. The URL must use HTTPS and cannot be changed after the repository is created.

For examples of some common upstream URLs, see [Custom upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#user-defined-upstreams).

  8. If you selected **Artifact Registry repository** :

     1. In the **Artifact Registry repository** field, enter the full name of the repository you want to use as your upstream, or click **Browse** to view a list of repositories that you have access to view. Only repositories of the same format as your remote repository are listed.
     2. Click the name of the repository you want to use as an upstream.
     3. Click **Select**.
  9. If you selected one of the preset upstreams or entered a full URL using the **Custom** button, then in the **Remote repository authentication mode** choose one of:

     * **Authenticated** : to enter your username and secret for authentication to your upstream repository.
     * **Unauthenticated** : to skip authentication to the upstream repository.
  10. If you selected **Authenticated** , enter the following:

     * In the **Username** field, enter your username for the upstream repository.
     * In the **Secret** field, enter the secret version where you saved your password for the upstream repository.

You can edit these values after you create the repository. For more information about authentication to remote repository upstreams, see [Configure authentication to remote repository upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-remote-authentication).

**Note:** You can add authentication to an unauthenticated repository after you create the repository, but you can't change an authenticated repository to an unauthenticated repository after you create it.
  11. In the **Location Type** section, choose the location for the repository:

     1. Choose the location type: Region or Multi-Region. The list of locations changes to reflect your selection.

     2. In the **Region** or **Multi-region** list, select a location.

For information about location types and supported locations, see [Repository locations](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations)

  12. Add a description for the repository. Descriptions help to identify the purpose of the repository and the kind of artifacts it contains.

Don't include sensitive data, because repository descriptions aren't encrypted.

  13. If you want to use [labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos) to organize your repositories, click **Add Label** and enter the key-value pair for the label. You can add, edit, or remove labels after you create the repository.

  14. In the **Encryption** section, choose the encryption mechanism for the repository.

     * **Google-managed encryption key** \- Encrypt repository content with a Google-owned and Google-managed encryption key.
     * **Customer-managed key** \- Encrypt repository content with a key that you control through Cloud Key Management Service. For key setup instructions, see [Setting up CMEK for repositories](https://docs.cloud.google.com/artifact-registry/docs/cmek).
  15. If you want to use cleanup policies to delete unused artifacts, in the **Cleanup policies** section:

     1. Select **Dry run** to test your policy before applying it.
     2. Click **Add policy** to add a keep or delete policy to your repository.
     3. Give your cleanup policy a descriptive name in the **Name** field.
     4. In the **Policy type** section, select one of:

        * **Conditional delete** : deletes artifacts based on conditions you define.
        * **Conditional keep** : keeps artifacts based on conditions you define.
        * **Keep most recent versions** : Keeps a set number of most recent versions per package.

**Caution:** if you set **Package prefixes** for this policy, only artifacts matching the package prefixes will be kept, up to the number set for most recent versions.

For more details on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

  16. In the **Artifact Analysis** section, choose vulnerability scanning settings:

     * **Enabled** \- Allow scanning in this repository. The Container Scanning API must be enabled on your project.

When you enable the Container Scanning API, billing begins immediately. After you enable the Container Scanning API on a project, vulnerability scanning is enabled for all new and existing repositories. When you push an image to Artifact Registry it's automatically scanned by Artifact Analysis.

     * **Disabled** \- Prevent scanning in this repository. If the Container Scanning API is enabled on your project, scanning continues on other repositories; this repository will be excluded.

For more information on vulnerability scanning options, see [Enable and disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).

  17. Click **Create**.




Artifact Registry creates the repository and adds it to the list of repositories.

###  gcloud CLI 

To create a repository, run the command for the appropriate repository format:

###  Docker 
    
    
    gcloud artifacts repositories create REMOTE-REPOSITORY-NAME \
        --project=PROJECT_ID \
        --repository-format=docker \
        --location=LOCATION \
        --description="DESCRIPTION" \
        --mode=remote-repository \
        --remote-repo-config-desc="REMOTE-REPOSITORY-DESCRIPTION" \
        --disable-vulnerability-scanning \
        --remote-docker-repo=UPSTREAM \
        --remote-username="USERNAME" \
        --remote-password-secret-version="PASSWORD"
    

Replace the following:

  * `REMOTE-REPOSITORY-NAME`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `PROJECT_ID`: the project ID. If this flag is omitted, the current or default project is used.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * `DESCRIPTION`: optional. A description of the repository. Don't include sensitive data, because repository descriptions aren't encrypted.
  * `REMOTE-REPOSITORY-DESCRIPTION`: optional. A description for the external repository configuration for this remote repository.
  * `USERNAME`: optional. Your username for authenticating to the upstream repository.
  * `PASSWORD`: optional. The secret version containing your upstream repository password.
  * `UPSTREAM` with the preset upstream name, Artifact Registry repository path, or user-defined URL of the upstream repository.   
  
For Artifact Registry upstream repositories, format the repository path similar to the following: `projects/UPSTREAM_PROJECT_ID/locations/REGION/repositories/UPSTREAM_REPOSITORY`.   
  
For information on available preset upstreams and supported user-defined upstreams, see [Supported formats](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-formats).

  * `--disable-vulnerability-scanning`: is an optional flag that configures your repository to disable automatic vulnerability scanning.

  * `--allow-vulnerability-scanning`: is an optional flag that configures your repository to permit automatic vulnerability scanning. For more information, see [Enable or disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).




For example, the following command creates a remote repository named `my-repo` in the region `us-east1` in the Google Cloud project `my-project` and can authenticate to the upstream repository using the username `my-username` and secret version `projects/my-project/secrets/my-secret/versions/1`.
    
    
    gcloud artifacts repositories create my-repo \
        --project=my-project \
        --repository-format=docker \
        --location=us-east1 \
        --description="Remote Docker repository" \
        --mode=remote-repository \
        --remote-repo-config-desc="Docker Hub" \
        --remote-username=my-username \
        --remote-password-secret-version=projects/my-project/secrets/my-secret/versions/1 \
        --remote-docker-repo=DOCKER-HUB
    

For more information about authenticating to Docker Hub upstream repositories, see [Configure remote repository authentication to Docker Hub](https://docs.cloud.google.com/artifact-registry/docs/docker/configure-remote-auth-docker-hub).

###  Maven 
    
    
    gcloud artifacts repositories create REMOTE-REPOSITORY-NAME \
        --project=PROJECT_ID \
        --repository-format=maven \
        --location=LOCATION \
        --description="DESCRIPTION" \
        --mode=remote-repository \
        --remote-repo-config-desc="REMOTE-REPOSITORY-DESCRIPTION" \
        --disable-vulnerability-scanning \
        --remote-mvn-repo=UPSTREAM \
        --remote-username="USERNAME" \
        --remote-password-secret-version="PASSWORD"
    

Replace the following:

  * `REMOTE-REPOSITORY-NAME`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `PROJECT_ID`: the project ID. If this flag is omitted, the current or default project is used.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * `DESCRIPTION`: optional. A description of the repository. Don't include sensitive data, because repository descriptions aren't encrypted.
  * `REMOTE-REPOSITORY-DESCRIPTION`: optional. A description for the external repository configuration for this remote repository.
  * `USERNAME`: optional. Your username for authenticating to the upstream repository.
  * `PASSWORD`: optional. The secret version containing your upstream repository password.
  * `UPSTREAM` with the preset upstream name, Artifact Registry repository path, or user-defined URL of the upstream repository.   
  
For Artifact Registry upstream repositories, format the repository path similar to the following: `projects/UPSTREAM_PROJECT_ID/locations/REGION/repositories/UPSTREAM_REPOSITORY`.   
  
For information on available preset upstreams and supported user-defined upstreams, see [Supported formats](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-formats).

  * `--disable-vulnerability-scanning`: is an optional flag that configures your repository to disable automatic vulnerability scanning.

  * `--allow-vulnerability-scanning`: is an optional flag that configures your repository to permit automatic vulnerability scanning. For more information, see [Enable or disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).




For example, the following command creates a remote repository named `my-repo` in the region `us-east1` in the Google Cloud project `my-project` and can authenticate to the upstream repository using the username `my-username` and secret version `projects/my-project/secrets/my-secret/versions/1`.
    
    
    gcloud artifacts repositories create my-repo \
        --project=my-project \
        --repository-format=maven \
        --location=us-east1 \
        --description="Remote Maven repository" \
        --mode=remote-repository \
        --remote-repo-config-desc="Maven Central" \
        --remote-username=my-username \
        --remote-password-secret-version=projects/my-project/secrets/my-secret/versions/1 \
        --remote-mvn-repo=MAVEN-CENTRAL
    

###  npm 
    
    
    gcloud artifacts repositories create REMOTE-REPOSITORY-NAME \
        --project=PROJECT_ID \
        --repository-format=npm \
        --location=LOCATION \
        --description="DESCRIPTION" \
        --mode=remote-repository \
        --remote-repo-config-desc="REMOTE-REPOSITORY-DESCRIPTION" \
        --disable-vulnerability-scanning \
        --remote-npm-repo=UPSTREAM \
        --remote-username="USERNAME" \
        --remote-password-secret-version="PASSWORD"
    

Replace the following:

  * `REMOTE-REPOSITORY-NAME`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `PROJECT_ID`: the project ID. If this flag is omitted, the current or default project is used.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * `DESCRIPTION`: optional. A description of the repository. Don't include sensitive data, because repository descriptions aren't encrypted.
  * `REMOTE-REPOSITORY-DESCRIPTION`: optional. A description for the external repository configuration for this remote repository.
  * `USERNAME`: optional. Your username for authenticating to the upstream repository.
  * `PASSWORD`: optional. The secret version containing your upstream repository password.
  * `UPSTREAM` with the preset upstream name, Artifact Registry repository path, or user-defined URL of the upstream repository.   
  
For Artifact Registry upstream repositories, format the repository path similar to the following: `projects/UPSTREAM_PROJECT_ID/locations/REGION/repositories/UPSTREAM_REPOSITORY`.   
  
For information on available preset upstreams and supported user-defined upstreams, see [Supported formats](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-formats).

  * `--disable-vulnerability-scanning`: is an optional flag that configures your repository to disable automatic vulnerability scanning.

  * `--allow-vulnerability-scanning`: is an optional flag that configures your repository to permit automatic vulnerability scanning. For more information, see [Enable or disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).




For example, the following command creates a remote repository named `my-repo` in the region `us-east1` in the Google Cloud project `my-project` and can authenticate to the upstream repository using the username `my-username` and secret version `projects/my-project/secrets/my-secret/versions/1`.
    
    
    gcloud artifacts repositories create my-repo \
        --project=my-project \
        --repository-format=npm \
        --location=us-east1 \
        --description="Remote npm repository" \
        --mode=remote-repository \
        --remote-repo-config-desc="Public npm registry" \
        --remote-username=my-username \
        --remote-password-secret-version=projects/my-project/secrets/my-secret/versions/1 \
        --remote-npm-repo=NPMJS
    

###  Python 
    
    
    gcloud artifacts repositories create REMOTE-REPOSITORY-NAME \
        --project=PROJECT_ID \
        --repository-format=python \
        --location=LOCATION \
        --description="DESCRIPTION" \
        --mode=remote-repository \
        --remote-repo-config-desc="REMOTE-REPOSITORY-DESCRIPTION" \
        --disable-vulnerability-scanning \
        --remote-python-repo=UPSTREAM \
        --remote-username="USERNAME" \
        --remote-password-secret-version="PASSWORD"
    

Replace the following:

  * `REMOTE-REPOSITORY-NAME`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `PROJECT_ID`: the project ID. If this flag is omitted, the current or default project is used.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * `DESCRIPTION`: optional. A description of the repository. Don't include sensitive data, because repository descriptions aren't encrypted.
  * `REMOTE-REPOSITORY-DESCRIPTION`: optional. A description for the external repository configuration for this remote repository.
  * `USERNAME`: optional. Your username for authenticating to the upstream repository.
  * `PASSWORD`: optional. The secret version containing your upstream repository password.
  * `UPSTREAM` with the preset upstream name, Artifact Registry repository path, or user-defined URL of the upstream repository.   
  
For Artifact Registry upstream repositories, format the repository path similar to the following: `projects/UPSTREAM_PROJECT_ID/locations/REGION/repositories/UPSTREAM_REPOSITORY`.   
  
For information on available preset upstreams and supported user-defined upstreams, see [Supported formats](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-formats).

  * `--disable-vulnerability-scanning`: is an optional flag that configures your repository to disable automatic vulnerability scanning.

  * `--allow-vulnerability-scanning`: is an optional flag that configures your repository to permit automatic vulnerability scanning. For more information, see [Enable or disable automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning).




For example, the following command creates a remote repository named `my-repo` in the region `us-east1` in the Google Cloud project `my-project` and can authenticate to the upstream repository using the username `my-username` and secret version `projects/my-project/secrets/my-secret/versions/1`.
    
    
    gcloud artifacts repositories create my-repo \
        --project=my-project \
        --repository-format=python \
        --location=us-east1 \
        --description="Remote Python repository" \
        --mode=remote-repository \
        --remote-repo-config-desc="PyPI" \
        --remote-username=my-username \
        --remote-password-secret-version=projects/my-project/secrets/my-secret/versions/1 \
        --remote-python-repo=PYPI
    

###  Apt (preview) 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    
    gcloud artifacts repositories create REMOTE_REPOSITORY_NAME \
        --project=PROJECT_ID \
        --repository-format=apt \
        --location=LOCATION \
        --description="DESCRIPTION" \
        --mode=remote-repository \
        --remote-repo-config-desc="REMOTE_REPOSITORY_DESCRIPTION" \
        --remote-apt-repo=APT_REPOSITORY_BASE \
        --remote-apt-repo-path="APT_REPOSITORY_PATH"
    

Replace the following:

  * REMOTE_REPOSITORY_NAME: the name of the repository. For each repository location in a project, repository names must be unique.
  * PROJECT_ID: the project ID. If this flag is omitted, the current or default project is used.
  * LOCATION: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * DESCRIPTION with an optional description of the repository. Don't include sensitive data, because repository descriptions are not encrypted.
  * REMOTE_REPOSITORY_DESCRIPTION optional: A description of the external repository configuration for this remote repository.
  * APT_REPOSITORY_BASE: one of the supported repository base names listed in the [OS package supported upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-os-upstreams) for Apt remote repositories.
  * APT_REPOSITORY_PATH: the remainder of the URL of the upstream repository that you want to cache in your remote repository after the repository base.



For example, the following command creates a remote repository named `my-repo` to cache the Debian stable repository in the region `us-east1` in the Google Cloud project `my-project`. The full URL of the upstream repository is `http://deb.debian.org/debian/dists/stable`.
    
    
    gcloud artifacts repositories create my-repo \
        --project=my-project \
        --repository-format=apt \
        --location=us-east1 \
        --description="Apt remote repository" \
        --mode=remote-repository \
        --remote-repo-config-desc="Debian stable distribution" \
        --remote-apt-repo=DEBIAN \
        --remote-apt-repo-path="debian/dists/stable"
    
    

###  Ruby (Preview) 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    
    gcloud artifacts repositories create REMOTE_REPOSITORY_NAME \
        --project=PROJECT_ID \
        --repository-format=ruby \
        --location=LOCATION \
        --description="DESCRIPTION" \
        --mode=remote-repository \
        --remote-repo=https://rubygems.org \
        --remote-repo-config-desc="REMOTE_REPOSITORY_DESCRIPTION" \
    

Replace the following:

  * REMOTE_REPOSITORY_NAME: the name of the repository. For each repository location in a project, repository names must be unique.
  * PROJECT_ID with the ID of the project containing the repository.
  * LOCATION: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * DESCRIPTION: optional. A description of the repository. Don't include sensitive data, because repository descriptions aren't encrypted.
  * REMOTE_REPOSITORY_DESCRIPTION optional. A description of the external repository configuration for this remote repository.



For example, the following command creates a remote repository named `my-ruby-repo` in the region `us-central1` in the Google Cloud project `my-project`. The full URL of the upstream repository is `https://rubygems.org`.
    
    
    gcloud artifacts repositories create my-ruby-repo \
        --project=my-project \
        --repository-format=ruby \
        --location=us-central1 \
        --description="Ruby remote repository" \
        --mode=remote-repository \
        --remote-repo=https://rubygems.org
    

###  Yum (preview) 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    
    gcloud artifacts repositories create REMOTE_REPOSITORY_NAME \
        --project=PROJECT_ID \
        --repository-format=yum \
        --location=LOCATION \
        --description="DESCRIPTION" \
        --mode=remote-repository \
        --remote-repo-config-desc="REMOTE_REPOSITORY_DESCRIPTION" \
        --remote-yum-repo=YUM_REPOSITORY_BASE \
        --remote-yum-repo-path="YUM_REPOSITORY_PATH"
    

Replace the following:

  * REMOTE_REPOSITORY_NAME: the name of the repository. For each repository location in a project, repository names must be unique.
  * PROJECT_ID: the project ID. If this flag is omitted, the current or default project is used.
  * LOCATION: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * DESCRIPTION: optional. A description of the repository. Don't include sensitive data, because repository descriptions aren't encrypted.
  * REMOTE_REPOSITORY_DESCRIPTION: optional. A description of the external repository configuration for this remote repository.
  * YUM_REPOSITORY_BASE: one of the supported repository base names listed in the [OS package supported upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview#supported-os-upstreams) for Yum remote repositories.
  * YUM_REPOSITORY_PATH: the remainder of the URL of the upstream repository that you want to cache in your remote repository after the repository base.



For example, the following command creates a remote repository for Yum packages named `my-repo` in the region `us-east1` in the Google Cloud project `my-project` for the upstream repository `9-stream/BaseOs/x86_64/os`. The full URL of the repository is `https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os`
    
    
    gcloud artifacts repositories create my-repo \
        --project=my-project \
        --repository-format=yum \
        --location=us-east1 \
        --description="Yum remote repository" \
        --mode=remote-repository \
        --remote-repo-config-desc="CentOS 8 x86" \
        --remote-yum-repo=CENTOS_STREAM \
        --remote-yum-repo-path="9-stream/BaseOs/x86_64/os"
    
    

###  Go 

Artifact Registry Go remote repositories only support the public upstream `https://proxy.golang`.
    
    
    gcloud artifacts repositories create REMOTE-REPOSITORY-NAME \
        --project=PROJECT_ID \
        --repository-format=go \
        --location=LOCATION \
        --description="DESCRIPTION" \
        --mode=remote-repository \
        --remote-repo-config-desc="REMOTE-REPOSITORY-DESCRIPTION" \
        --remote-go-repo=https://proxy.golang.org
    

Replace the following:

  * `REMOTE-REPOSITORY-NAME`: the name of the repository. For each repository location in a project, repository names must be unique.
  * `PROJECT_ID`: the project ID. If this flag is omitted, the current or default project is used.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * `DESCRIPTION`: optional. A description of the repository. Do not include sensitive data. Repository descriptions are not encrypted.
  * `REMOTE-REPOSITORY-DESCRIPTION`: optional. A description for the external repository configuration for this remote repository.



For example, the following command creates a remote repository named `my-repo` in the region `us-east1` in the Google Cloud project `my-project`.
    
    
    gcloud artifacts repositories create my-repo \
        --project=my-project \
        --repository-format=go \
        --location=us-east1 \
        --description="Remote Go repository" \
        --mode=remote-repository \
        --remote-repo-config-desc="Go proxy" \
        --remote-go-repo=https://proxy.golang.org
    

Artifact Registry creates your repository. Run the following command to view a description of the repository:
    
    
    gcloud artifacts repositories describe REMOTE_REPOSITORY_NAME \
        --location=LOCATION
    

###  Terraform 

Use the [google_artifact_registry_repository](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository) resource to create repositories. [`terraform-provider-google`](https://github.com/hashicorp/terraform-provider-google) version `5.0.0` or newer is required.

If you are new to using Terraform for Google Cloud, see the [Get Started - Google Cloud](https://learn.hashicorp.com/collections/terraform/gcp-get-started) page on the HashiCorp website.

The following example defines the provider and a remote repository with the Terraform resource name `my-repo`.

###  Docker 
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "DESCRIPTION"
      format        = "docker"
      kms_key_name = "KEY"
      mode          = "REMOTE_REPOSITORY"
      remote_repository_config {
        description = "CONFIG_DESCRIPTION"
        docker_repository {
          public_repository = "DOCKER_HUB"
        }
      }
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
    

Where

  * `PROJECT-ID`is the Google Cloud project ID.
  * `LOCATION`is the repository location.
  * `REPOSITORY_ID`is the repository ID.
  * `DESCRIPTION`is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-managed encryption keys.
  * `CONFIG_DESCRIPTION`is the optional description of the remote source.
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository. * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode. * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies. For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy). 
    * `POLICY_NAME` is the name of the cleanup policy.
    * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.
    * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to.
    * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.
    * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.
    * `KEEP_COUNT` is the number of versions per package of an artifact to keep in your repository.



###  Maven 

If you don't specify a version policy, Artifact Registry creates a Maven repository that stores both [snapshot and release versions](https://docs.cloud.google.com/artifact-registry/docs/java#versions) of packages by default.
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "DESCRIPTION"
      format        = "maven"
      kms_key_name = "KEY"
      mode          = "REMOTE_REPOSITORY"
      remote_repository_config {
        description = "CONFIG_DESCRIPTION"
        maven_repository {
          public_repository = "MAVEN_CENTRAL"
        }
      }
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
    

Where

  * `PROJECT-ID`is the Google Cloud project ID.
  * `LOCATION`is the repository location.
  * `REPOSITORY_ID`is the repository ID.
  * `DESCRIPTION`is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-managed encryption keys.
  * `CONFIG_DESCRIPTION`is the optional description of the remote source.
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository. * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode. * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies. For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy). 
    * `POLICY_NAME` is the name of the cleanup policy.
    * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.
    * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to.
    * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.
    * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.
    * `KEEP_COUNT` is the number of versions per package of an artifact to keep in your repository.



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
    
    location = "LOCATION"
    repository_id = "my-repo"
    description = "Maven repository"
    format = "MAVEN"
    mode = "REMOTE_REPOSITORY"
    maven_config {
      version_policy = "RELEASE"
    }
    }
    

###  npm 
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "DESCRIPTION"
      format        = "npm"
      kms_key_name = "KEY"
      mode          = "REMOTE_REPOSITORY"
      remote_repository_config {
        description = "CONFIG_DESCRIPTION"
        npm_repository {
          public_repository = "NPMJS"
        }
      }
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
    

Where

  * `PROJECT-ID`is the Google Cloud project ID.
  * `LOCATION`is the repository location.
  * `REPOSITORY_ID`is the repository ID.
  * `DESCRIPTION`is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-managed encryption keys.
  * `CONFIG_DESCRIPTION`is the optional description of the remote source.
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository. * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode. * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies. For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy). 
    * `POLICY_NAME` is the name of the cleanup policy.
    * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.
    * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to.
    * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.
    * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.
    * `KEEP_COUNT` is the number of versions per package of an artifact to keep in your repository.



###  Python 
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "DESCRIPTION"
      format        = "python"
      kms_key_name = "KEY"
      mode          = "REMOTE_REPOSITORY"
      remote_repository_config {
        description = "CONFIG_DESCRIPTION"
        python_repository {
          public_repository = "PYPI"
        }
      }
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
    

Where

  * `PROJECT-ID`is the Google Cloud project ID.
  * `LOCATION`is the repository location.
  * `REPOSITORY_ID`is the repository ID.
  * `DESCRIPTION`is the optional description for the repository. Do not include sensitive data, since repository descriptions are not encrypted.
  * `KEY`is the name of the Cloud Key Management Service key, if you are using [customer-managed encryption keys](https://docs.cloud.google.com/artifact-registry/docs/cmek) (CMEK) for encryption. Omit this argument to use the default setting, Google-managed encryption keys.
  * `CONFIG_DESCRIPTION`is the optional description of the remote source.
  * `DRY_RUN_STATUS` determines if cleanup policies delete artifacts, or only log which artifacts would be deleted if setting cleanup policies on the repository. Omit if you don't want to add cleanup policies to the repository. * `true`: sets the policies to run in dry run mode. No artifacts are deleted in dry run mode. * `false`: applies the cleanup policies. Artifacts are deleted or kept depending on the policies. For more information on cleanup policies, see [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy). 
    * `POLICY_NAME` is the name of the cleanup policy.
    * `TAG_STATE` is the tag state to apply the policy to. Values are `tagged`, `untagged`, and `any`. `any` applies to both tagged and untagged artifacts. If a repository has immutable tags enabled, tagged artifacts can't be deleted.
    * `TAG_PREFIX`, `TAG_PREFIX_N` are tag prefixes to apply the policy to.
    * `PKG_PREFIX`, `PKG_PREFIX_N` are package prefixes to apply the policy to.
    * `TIME_SINCE_UPLOAD` is the time since an artifact version was uploaded to the repository, specified as a duration. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.
    * `KEEP_COUNT` is the number of versions per package of an artifact to keep in your repository.



###  Apt (Preview)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    
      provider "google" {
      project = "PROJECT_ID"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "DESCRIPTION"
      format        = "APT"
      mode          = "REMOTE_REPOSITORY"
      remote_repository_config {
        description = "CONFIG_DESCRIPTION"
        apt_repository {
          public_repository {
            repository_base = "REPOSITORY_BASE"
            repository_path = "REPOSITORY_PATH"
          }
        }
      }
    }
    

Replace the following:

  * PROJECT_ID: the Google Cloud project ID.
  * LOCATION: the repository location.
  * REPOSITORY_ID: the repository ID.
  * DESCRIPTION: optional. A description for the repository. Don't include sensitive data, because repository descriptions aren't encrypted.
  * CONFIG_DESCRIPTION: optional. A description of the remote source.
  * REPOSITORY_BASE: the preset public repository base for Apt. Possible values are `DEBIAN` and `UBUNTU`.
  * REPOSITORY_PATH: the specific repository from the base. For example `debian/dists/stable`.



###  Yum (Preview)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    
      provider "google" {
      project = "PROJECT_ID"
    }
    
    resource "google_artifact_registry_repository" "my-repo" {
      location      = "LOCATION"
      repository_id = "REPOSITORY_ID"
      description   = "DESCRIPTION"
      format        = "YUM"
      mode          = "REMOTE_REPOSITORY"
      remote_repository_config {
        description = "CONFIG_DESCRIPTION"
        yum_repository {
          public_repository {
            repository_base = "REPOSITORY_BASE"
            repository_path = "REPOSITORY_PATH"
          }
        }
      }
    }
    

Where

  * PROJECT_ID: the Google Cloud project ID.
  * LOCATION: the repository location.
  * REPOSITORY_ID: the repository ID.
  * DESCRIPTION: optional. A description for the repository. Don't include sensitive data, because repository descriptions aren't not encrypted.
  * CONFIG_DESCRIPTION: optional. A description of the remote source.
  * REPOSITORY_BASE: the preset public repository base for Yum. Possible values are `CENTOS`, `CENTOS_DEBUG`, `CENTOS_VAULT`, `CENTOS_STREAM`, `ROCKY`, and `EPEL`.
  * REPOSITORY_PATH: the specific repository from the base. For example `"centos/8-stream/BaseOS/x86_64/os`.



Artifact Registry creates your repository. Run the following command to view a description of the repository:
    
    
    gcloud artifacts repositories describe REPOSITORY \
        --location=LOCATION
    

After you have created the repository:

  * [Grant access](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) to the repository.
  * Optional: [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) to delete unused artifacts.
  * Configure Docker, package managers, and other third-party clients to authenticate to repositories. 
    * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication)
    * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication), [Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication)
    * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure)
    * Other: [Kubeflow Pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)
  * Configure Artifact Registry remote repositories to authenticate to their upstream sources. 
    * Container images: [Configure remote repository authentication to Docker Hub](https://docs.cloud.google.com/artifact-registry/docs/docker/configure-remote-auth-docker-hub)
    * Language packages: 
      * [Configure remote repository authentication to Maven Central](https://docs.cloud.google.com/artifact-registry/docs/java/configure-remote-auth-maven-central)
      * [Configure remote repository authentication to the npm registry](https://docs.cloud.google.com/artifact-registry/docs/nodejs/configure-remote-auth-npm-registry)
      * [Configure remote repository authentication to PyPI](https://docs.cloud.google.com/artifact-registry/docs/python/configure-remote-auth-pypi)
    * User-defined custom upstreams: [Configure authentication to remote repository upstreams](https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-remote-authentication)



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
    

For example, use the following command to view settings for remote repositories in `us-east1` in the project `my-project`:
    
    
    gcloud artifacts vpcsc-config describe \
        --project=my-project \
        --location=us-east1
    

### Allow access to upstream sources

To allow access to upstream sources in a specified location, run the command:
    
    
    gcloud artifacts vpcsc-config allow \
        --project=PROJECT_ID \
        --location=LOCATION
    

For example, use the following command to allow all remote repositories in `us-east1` in the project `my-project` to access their upstream sources outside of the perimeter:
    
    
    gcloud artifacts vpcsc-config allow \
        --project=my-project \
        --location=us-east1
    

### Deny access to upstream sources

When you deny access to upstream sources, existing cached artifacts in remote repositories are still available.

To deny access to upstream sources in a specified location, run the command:
    
    
    gcloud artifacts vpcsc-config deny \
        --project=PROJECT_ID \
        --location=LOCATION
    

For example, use the following command to block access to upstream sources outside of the perimeter for all remote repositories in `us-west1` in the project `my-project`:
    
    
    gcloud artifacts vpcsc-config deny \
        --project=my-project \
        --location=us-west1
    

## What's next

  * [Create a Docker Hub remote repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-dockerhub-remote-repository).
  * Learn more about Artifact Registry [remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview).
  * [Configure remote repository authentication to Docker Hub](https://docs.cloud.google.com/artifact-registry/docs/docker/configure-remote-auth-docker-hub).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
