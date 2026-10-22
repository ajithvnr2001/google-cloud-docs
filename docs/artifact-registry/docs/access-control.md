---
url: https://docs.cloud.google.com/artifact-registry/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:23.330657+00:00
---

# Access control with IAM  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Use Identity and Access Management (IAM) to grant roles to control who can access and manage data in Artifact Registry. Artifact Registry contains [predefined roles](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles) that may help streamline CI/CD pipeline configuration. If you need additional access control, or are integrating Artifact Registry with a [third-party tool](https://docs.cloud.google.com/artifact-registry/docs/access-control#third-party), you can also configure custom roles.

If you use Artifact Analysis to scan images for vulnerabilities, see the [Artifact Analysis documentation](https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control) for information about granting access to container metadata. 

## Before you begin

  1. [Enable Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/enable-service), including enabling the API and installing the Google Cloud CLI.
  2. If you want to apply repository-specific permissions, then [create an Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) for your packages.



## Overview

IAM [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions) and [roles](https://docs.cloud.google.com/iam/docs/overview#roles) determine your ability to create, view, edit, or delete data in an Artifact Registry repository.

A role is a collection of permissions. You can't grant a principal permissions directly; instead, you grant them a role. When you grant a role to a principal, you grant them all the permissions that the role contains. You can grant multiple roles to the same principal.

### Google Cloud default permissions

By default, the following permissions apply to Google Cloud CI/CD services in the same project as Artifact Registry:

  * Cloud Build [permissions](https://docs.cloud.google.com/build/docs/cloud-build-service-account) include permissions to upload and download artifacts.


  * Compute Engine, [supported Google Kubernetes Engine versions](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke), and Cloud Run use the Compute Engine [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which has read-only access to storage.



If all your services are in the same Google Cloud project and the default permissions meet your needs, you don't need to configure permissions.

You must configure Artifact Registry permissions for these services if:

  * You want to use these services to access Artifact Registry in another project. In the project with Artifact Registry, grant the [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) or service account for each service the required role. If connecting to Cloud Run, grant the [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/service-agents) the required role.


  * You're using a GKE version that does not have built-in support for pulling images from Artifact Registry. See the [GKE](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke) section for configuration instructions.
  * You want the default service account to have read and write access to repositories. See the following information for details: 
    * Compute Engine
    * GKE
  * You're using a user-provided service account for your runtime environments instead of the default service account. In the project with Artifact Registry, grant your service account the required role.



### Third-party integration

For third-party clients, you must configure both permissions and authentication.

Traditionally, applications running outside Google Cloud use [service account keys](https://docs.cloud.google.com/iam/docs/service-account-creds#key-types) to access Google Cloud resources. However, service account keys are powerful credentials, and can present a security risk if they are not managed correctly.

Workload Identity Federation lets you use Identity and Access Management to grant external identities [IAM roles](https://docs.cloud.google.com/iam/docs/overview#roles), including the ability to impersonate service accounts. This approach eliminates the maintenance and security burden associated with service account keys.

**Use Workload Identity Federation** :

  1. [Create a Workload Identity Federation pool](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers#create-pools).
  2. [Create a Workload Identity Federation provider](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers#create-provider).
  3. Grant the appropriate Artifact Registry role to the workload identity pool to allow repository access. For more information, see [Allow your external workload to access Google Cloud resources](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#access).
  4. If you need to access Artifact Registry for longer periods of time, then configure the OIDC token expiration time to a longer period in your [credential configuration](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#create-credential-config).
  5. Configure your third-party client to authenticate with Artifact Registry.

     * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication)
     * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication), [Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication)
     * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure)
     * Other: [Kubeflow Pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)



**Use a service account** :

  1. [Create](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) a service account to act on behalf of your application, or choose an existing service account that use for your CI/CD automation.
  2. Grant the appropriate Artifact Registry role to the service account to provide repository access.
  3. Configure your third-party client to authenticate with Artifact Registry.

     * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication)
     * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication), [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication), [Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication)
     * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure)
     * Other: [Kubeflow Pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)



#### GitLab on Google Cloud

The GitLab on Google Cloud integration uses [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) for authorization and authentication for GitLab workloads on Google Cloud without the need for service accounts or service account keys. For more information on how Workload Identity Federation is used in this partnership, see [Google Cloud Workload Identity Federation and IAM policies](https://docs.gitlab.com/ee/integration/google_cloud_iam.html).

To set up Workload Identity Federation and the necessary IAM roles for the GitLab on Google Cloud, see the GitLab tutorial [Google Cloud Workload Identity Federation and IAM policies](https://docs.gitlab.com/ee/integration/google_cloud_iam.html).

To connect your Artifact Registry repository, follow the GitLab tutorial [Google Artifact Registry](https://docs.gitlab.com/ee/user/project/integrations/google_artifact_registry.html). 

## Roles and permissions

Every Artifact Registry API method requires that the [principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity) making the request has the required permissions to use the resource. Permissions are given to principals by setting policies that grant the principal a predefined role on the resource.

You can grant roles on the Google Cloud project or the Artifact Registry repository.

### Predefined Artifact Registry roles

IAM provides [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) that grant access to specific Google Cloud resources.

Use the following predefined roles for repositories on the `pkg.dev` domain: Role | Description  
---|---  
Artifact Registry Reader  
(`roles/artifactregistry.reader`) | View and get artifacts, view repository metadata.   
Artifact Registry Writer  
(`roles/artifactregistry.writer`) | Read and write artifacts.   
Artifact Registry Repository Administrator  
(`roles/artifactregistry.repoAdmin`) | Read, write, and delete artifacts.   
Artifact Registry Administrator  
(`roles/artifactregistry.admin`) | Create and manage repositories and artifacts.   
The following additional predefined roles contain permissions required to [migrate from Container Registry to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar). Role | Description  
---|---  
Container Registry -> Artifact Registry Migration Admin (`roles/artifactregistry.containerRegistryMigrationAdmin`) | Includes all permissions required to run migration tooling   
Artifact Registry Create-on-push Writer (`roles/artifactregistry.createOnPushWriter`) | Read and write artifacts. Create gcr.io repositories when you push to `gcr.io` URLs.   
Artifact Registry Create-on-push Repository Administrator (`roles/artifactregistry.createOnPushRepoAdmin`) | Read, write, and delete artifacts. Create gcr.io repositories.   
For a full list of the individual permissions in each role, refer to [Artifact Registry roles](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry). You can also use the [`gcloud iam roles describe`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/describe) command to view a list of permissions in each role. 

### Basic IAM roles

Basic roles are highly permissive roles that existed prior to the introduction of IAM. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment.

Use predefined roles for repository access whenever possible so that users and service accounts only have the permissions that are required.

For more information on basic roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Granting roles

Grant roles at the project level if the same roles apply to all repositories in the project. If some accounts require different levels of access, grant roles at the repository level.

If you're granting roles on a [virtual repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo), those roles apply to all upstream repositories available through the virtual repository, regardless of individual repository permissions. 

If you're granting roles using the `gcloud` command, you can specify a single role binding for a principal or you can make large-scale policy changes by getting a resource's allow policy, modifying it, and then setting the modified allow policy. For more information, see [Grant or revoke multiple roles programmatically](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#multiple-roles-programmatic).

### Granting project-wide roles

Grant a role at the project level if the same permissions apply to all repositories in the project.

**Note:** When managing access for users in [external identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), replace instances of Google Account principal identifiers—like `user:kiran@example.com`, `group:support@example.com`, and `domain:example.com`—with appropriate [Workforce Identity Federation principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 

To add a user or service account to a project and grant them an Artifact Registry role:

###  Console 

  1. Open the IAM page in the Google Cloud console. 

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Select a project** , choose the project where Artifact Registry is running, and click **Open**.

  3. Click **Add**.

  4. Enter an email address. You can add individuals, service accounts, or Google Groups as principals.

  5. Select a role for the principal. In accordance with the security principle of least privilege, consider granting the least amount of privilege needed to access the required Artifact Registry resources. For information on Artifact Registry predefined roles and permissions, see [Predefined Artifact Registry roles](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles).

  6. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To grant a role to a single principal, run the following command:
         
         gcloud projects add-iam-policy-binding PROJECT \
            --member=PRINCIPAL \
            --role=ROLE

where

     * PROJECT is the ID of the project where Artifact Registry is running.
     * PRINCIPAL is the principal to add the binding for. Use the form `user|group|serviceAccount:email` or `domain:domain`.

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`.

     * ROLE is the [role](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles) that you want to grant.

For more information, see the [add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) documentation.

To grant roles using a policy file, see [Grant or revoke multiple roles programmatically](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#multiple-roles-programmatic)




### Granting repository-specific roles

Grant repository-level roles when you want users or service accounts to have different levels of access for each repository in your project.

###  Console 

To grant access to a specific repository:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Select the appropriate repository.

  3. If the info panel is not displayed, click **Show Info Panel** in the menu bar.

  4. On the Permissions tab, click **Add Principal**.

  5. Enter an email address. You can add individuals, service accounts, or Google Groups as principals.

  6. Select a role for the principal. In accordance with the security principle of least privilege, consider granting the least amount of privilege needed to access the required Artifact Registry resources. For information on Artifact Registry predefined roles and permissions, see [Predefined Artifact Registry roles](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles).

  7. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. You can set an IAM set of individual policy bindings or use a policy file.

To grant a role to a single principal, run the following command:
         
         gcloud artifacts repositories add-iam-policy-binding REPOSITORY \
            --location=LOCATION \
            --member=PRINCIPAL \
            --role=ROLE

where

     * REPOSITORY is the ID of the repository.
     * PRINCIPAL is the principal to add the binding for. Use the form `user|group|serviceAccount:email` or `domain:domain`.

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`.

     * ROLE is the role that you want to grant.

     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.

For example, to add an IAM policy binding for the role `roles/artifactregistry.writer` for the user `write@gmail.com` with the repository `my-repo` in the location `--us-west1`, run:
    
    gcloud artifacts repositories add-iam-policy-binding my-repo \
    --location=us-west1 --member=user:write@gmail.com --role=roles/artifactregistry.writer

To grant roles using a policy file, use the procedure described in [Grant or revoke multiple roles programmatically](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#multiple-roles-programmatic) with the [gcloud artifacts repositories get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/get-iam-policy) and [gcloud artifacts repositories set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-iam-policy) commands.




###  Terraform 

Use the [google_artifact_registry_repository_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository_iam) resource to configure an IAM policy. The following example defines a service account with the resource name `repo-account` and grants it read access to a repository with the resource name `my-repo`.

If you're new to using Terraform for Google Cloud, see the [Get Started - Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started) page on the HashiCorp website.
    
    
    provider "google" {
        project = "PROJECT-ID"
    }
    
    resource "google_artifact_registry_repository" "my-repo"     {
      provider = google-beta
    
      location = "LOCATION"
      repository_id = "REPOSITORY"
      description = "DESCRIPTION"
      format = "FORMAT"
    }
    
    resource "google_service_account" "repo-account" {
      provider = google-beta
    
      account_id   = "ACCOUNT-ID"
      display_name = "Repository Service Account"
    }
    
    resource "google_artifact_registry_repository_iam_member" "repo-iam" {
      provider = google-beta
    
      location = google_artifact_registry_repository.my-repo.location
      repository = google_artifact_registry_repository.my-repo.name
      role   = "roles/artifactregistry.reader"
      member = "serviceAccount:${google_service_account.repo-account.email}"
    }
    

ACCOUNT-ID is the ID of the service account. This is the the part of the service account email field before the `@` symbol.

For additional examples, see the documentation for the [google_artifact_registry_repository_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository_iam) resource.

### Configuring public access to a repository

If you have artifacts that you want to make available to anyone on the internet without authentication, store them in a repository that you make public.

To configure a repository for public read-only access, grant the Artifact Registry Reader role to the principal `allUsers`. We also recommend [capping user request quotas](https://docs.cloud.google.com/artifact-registry/quotas#user-quota) so that a single user can't use up your project's overall quota.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Select the appropriate repository.

  3. If the info panel is not displayed, click **Show Info Panel** in the menu bar.

  4. On the Permissions tab, click **Add Principal**.

  5. In **New principals** field, enter `allUsers`.

  6. Select the role **Artifact Registry Reader**.

  7. Set a per-user limit on Artifact Registry API requests to prevent misuse by unauthenticated users. For instructions, see [Capping usage](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage).




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following command:
         
         gcloud artifacts repositories add-iam-policy-binding REPOSITORY \
         --location=LOCATION --member=allUsers --role=ROLE

where

     * REPOSITORY is the ID of the repository.

     * ROLE is the role that you want to grant. 

     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.

For example, configure the repository `my-repo` in the location `--us-west1` as public, run:
    
    gcloud artifacts repositories add-iam-policy-binding my-repo \
     --location=us-west1 --member=allUsers --role=roles/artifactregistry.reader

  3. Set a per-user limit on Artifact Registry API requests to prevent misuse by unauthenticated users. For instructions, see [Capping usage](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage).




### Revoking roles

To revoke access to a repository, remove the principal from the list of authorized principals.

To remove public access from a repository, remove the `allUsers` principal.

###  Console 

To revoke permissions:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Select the appropriate repository.

  3. If the info panel is not displayed, click **Show Info Panel** in the menu bar.

  4. On the Permissions tab, expand the appropriate principal. If you are making a public repository private, expand the `allUsers` principal.

  5. Click **Remove principal** to revoke access.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To revoke a role at the project level, run the following command:
         
         gcloud projects remove-iam-policy-binding PROJECT \
            --member=PRINCIPAL \
            --role=ROLE

     * PROJECT is the project ID.
     * PRINCIPAL is the principal to remove the binding for. Use the form `user|group|serviceAccount:email` or `domain:domain`.

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`.

     * ROLE is the role that you want to revoke.

To revoke a role for a repository, run the following command:
    
    gcloud artifacts repositories remove-iam-policy-binding REPOSITORY
       --location=LOCATION \
       --member=PRINCIPAL \
       --role=ROLE

where

     * REPOSITORY is the ID of the repository.
     * PRINCIPAL is the principal to remove the binding for. Use the form `user|group|serviceAccount:email` or `domain:domain`.

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`.

To revoke public access to the repository, specify the principal `allUsers`.

     * ROLE is the role that you want to revoke.

For example, to remove a policy binding for the role `roles/artifactregistry.writer` for the user `write@gmail.com` with the repository `my-repo` in the location `--us-west1`, run:
    
    gcloud artifacts repositories remove-iam-policy-binding my-repo \
       --location=us-west1 \
       --member=user:write@gmail.com \
       --role=roles/artifactregistry.writer

To revoke public access to `my-repo` in the location `--us-west1`, run:
    
    gcloud artifacts repositories remove-iam-policy-binding my-repo \
       --location=us-west1 \
       --member=allUsers \
       --role=roles/artifactregistry.reader




## Granting conditional access with tags

Project administrators can create tags for resources across Google Cloud and manage them in [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). When you attach a tag to a Artifact Registry repository, administrators can use the tag with IAM conditions to grant conditional access to the repository.

You cannot attach tags to individual artifacts.

For more information see the following documentation:

  * Administrators setting up tags and access control 
    * [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing)
    * [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control).
  * Developers attaching tags to repositories 
    * [Tagging repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos)



## Integrating with Google Cloud services

For most Google Cloud service accounts, configuring access to a registry only requires granting the appropriate IAM roles.

### Default service accounts for Google Cloud services

Google Cloud services such as Cloud Build or Google Kubernetes Engine use a [default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) or [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#default) to interact with resources within the same project.

You must configure or modify permissions yourself if:

  * The Google Cloud service is in a different project than Artifact Registry.
  * The default permissions don't meet your needs.
  * You're using a user-provided service account to interact with Artifact Registry instead of the default service account.
  * Your organizational policy configuration prevents automatic role grants to default service accounts.



The following service accounts typically access Artifact Registry. The email address for the service account includes the Google Cloud [project ID or project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where the service is running.

Service | Service account | Email address  
---|---|---  
App Engine flexible environment | [App Engine service account](https://docs.cloud.google.com/appengine/docs/standard/python/service-account) | PROJECT-ID@appspot.gserviceaccount.com  
Compute Engine | [ Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) | PROJECT-NUMBER-compute@developer.gserviceaccount.com  
Cloud Build | [Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)  
or   
[Legacy Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) | Depending on your organizational settings, the default service account email address is one of the following:  


  * Compute Engine: PROJECT-NUMBER-compute@developer.gserviceaccount.com
  * Cloud Build: PROJECT-NUMBER@cloudbuild.gserviceaccount.com

**Note:** The Cloud Build default service account used to run builds has changed from the legacy Cloud Build service account to the Compute Engine default service account. For more information, see [Cloud Build service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).   
Cloud Run | [ Cloud Run service agent](https://docs.cloud.google.com/iam/docs/service-agents)  
The service agent for `run.googleapis.com`. | service-PROJECT-NUMBER@serverless-robot-prod.iam.gserviceaccount.com  
GKE | [ Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)  
The default service account for nodes. | PROJECT-NUMBER-compute@developer.gserviceaccount.com  
  
Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Granting access to Compute Engine instances

VM instances that access repositories must have both Artifact Registry permissions and storage _access scope_ configured.

While a service account's access level is determined by the IAM roles granted to the service account, _access scopes_ on a VM instance determine the default OAuth scopes for requests made through the gcloud CLI and client libraries on the instance. As a result, access scopes potentially further limit access to API methods when authenticating with [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

Compute Engine uses the following defaults:

  * The [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is the identity for VM instances. The service account email address has the suffix **@developer.gserviceaccount.com**.
  * The default service account has the IAM basic Editor role, if you have not [disabled this behavior](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants).
  * Instances you create with the default service account have the Compute Engine [default access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_scopes), including read-only access to storage. While the Editor role generally grants write access, the `read-only` storage access scope limits the instance service account to downloading artifacts only from any repository in the same project.



You must configure the access scope of the service account if:

  * The VM service account needs to access a repository in a different project.
  * The VM service account needs to perform actions other than reading artifacts from repositories. This typically applies third-party tools on a VM that need to push images or run Artifact Registry `gcloud` commands.



To configure roles and set the access scope:

  1. In the project with your VM instance, get the name of the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). The service account email address has the suffix **@developer.gserviceaccount.com**.

  2. In the project with the repository, grant permissions so that the service account can access the repository.

  3. Set the access scope with the [\--scopes](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--scopes) option.

     1. Stop the VM instance. See [Stopping an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

     2. Set the access scope with the following command:
            
            gcloud compute instances set-service-account INSTANCE --scopes=SCOPE
            

Replace SCOPE with the appropriate value.

        * For Docker, the following options are supported:

          * `storage-ro` \- Grants read permission only for pulling images.
          * `storage-rw` \- Grants read and write permission for pushing or pulling images.
          * `cloud-platform` \- View and manage data, including metadata, across Google Cloud service.
        * For other formats, you must use the `cloud-platform` scope.

     3. Restart the VM instance. See [Starting a stopped instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance).




### Granting access to Google Kubernetes Engine clusters

GKE clusters and node pools can pull containers without any additional configuration if all the following requirements are met:

  * GKE is in the same project as Artifact Registry
  * Nodes are using the default service account, the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)
  * Nodes were created with read access to storage by: 
    * Using the Compute Engine [default access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_scopes).
    * Granting the `cloud-platform` access scope or another scope that includes read access to storage.
  * You're running a [supported version](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke) of GKE



If your GKE environment does not meet these requirements the instructions to grant access depend on whether you're using the Compute Engine default service account or a user-provided service account as the identity for your nodes.

Default service account
    

The following configuration requirements apply to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account):

  1. If GKE is in a different project than Artifact Registry, grant the required permissions to the service account.

  2. To push images, interact with repositories for formats other than containers, or run `gcloud` commands from your cluster, you must set access scopes for the service account when you create the cluster or node pool.

  3. If you're not using a [supported version](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke) of GKE, configure [imagePullSecrets](https://docs.cloud.google.com/artifact-registry/docs/access-control#pullsecrets).



User-provided service account
    

If you want to use a user-provided [service account](https://docs.cloud.google.com/iam/docs/service-accounts) as the identity for a cluster, you must:

  1. Grant the required permissions to the service account from the Google Cloud project where Artifact Registry is running.

  2. By default, creating a cluster or node pool with a user-provided service account grants the `cloud-platform` access scope.

If you use the `--scopes` flag with the [gcloud container clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) or [gcloud container node-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) command, you must include the appropriate access scopes for use with Artifact Registry.




#### Setting access scopes

Access scopes are the legacy method of specifying authorization for Compute Engine VMs. To pull images from Artifact Registry repositories, GKE nodes must have the storage read-only access scope or another storage access scope that includes storage read access.

You can only set access scopes when you create a cluster or node pool. You cannot change access scopes on existing nodes.

  * If you're using the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), GKE creates nodes with the Compute Engine [default access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_scopes), which includes read-only access to storage.
  * If you're using a user-provided service account, GKE creates nodes with the `cloud-platform` scope, the scope required for most Google Cloud services.



To specify access scopes when creating a cluster, run the following command:
    
    
    gcloud container clusters create NAME --scopes=SCOPES
    

To specify access scopes when creating a node pool, run the following command:
    
    
    gcloud container node-pools create NAME --scopes=SCOPES
    

Replace the following values:

  * NAME is the name of the cluster or node pool.
  * SCOPES is a comma-separated list of access scopes to grant.

    * To access Docker repositories, use one of the following scopes:

    * `storage-ro` \- Grants read-only permission for pulling images.

    * `storage-rw` \- Grants read and write permission for pushing or pulling images.

    * `cloud-platform` \- View and manage data, including metadata, across Google Cloud service.

    * To access other repositories, you must use the `cloud-platform` scope.

For a full list of scopes, see the documentation for [gcloud container clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) or [gcloud container node-pools create](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create).




For more information about scopes you can set when creating a new cluster, refer to the documentation for the command [gcloud container clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create).

#### Configuring an `imagePullSecret`

To configure an `imagePullSecret`:

  1. In the project with GKE, find Compute Engine default service account. The account email address has the suffix **@developer.gserviceaccount.com**.

  2. [Download the service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for the service account.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  3. In the project with the repository, verify that you have granted permissions to the repository.

  4. In the project with your cluster, create an `imagePullSecret` secret called `artifact-registry` with the service account key.
         
         kubectl create secret docker-registry artifact-registry \
         --docker-server=https://LOCATION-docker.pkg.dev \
         --docker-email=SERVICE-ACCOUNT-EMAIL \
         --docker-username=_json_key \
         --docker-password="$(cat KEY-FILE)"
         

Replace the following:

     * LOCATION is the regional or multi-regional location of the repository.
     * SERVICE-ACCOUNT-EMAIL is the email address of the Compute Engine service account.
     * KEY-FILE is the name of your service account key file. For example `key.json`.
  5. Open your default service account:
         
         kubectl edit serviceaccount default --namespace default

Every [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in your Kubernetes cluster has a default service account called `default`. This default service account is used to pull your container image.

  6. Add the newly created `imagePullSecret` secret to your default service account:
         
         imagePullSecrets:
         - name: artifact-registry
         

Your service account should now look like this:
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: default
           namespace: default
           ...
         secrets:
         - name: default-token-zd84v
         # The secret you created:
         imagePullSecrets:
         - name: artifact-registry
         




Now, any new pods created in the current `default` namespace will have the `imagePullSecret` secret defined.

## Artifact Registry Service Agent

The Artifact Registry Service Agent is a Google-managed service account that acts on behalf of Artifact Registry when interacting with Google Cloud services. For more information about the account and its permissions, see [Artifact Registry Service Agent](https://docs.cloud.google.com/artifact-registry/docs/ar-service-account).

## What's next

After you have set up permissions, learn more about working with your artifacts.

  * Container images: [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker), [Helm](https://docs.cloud.google.com/artifact-registry/docs/helm)
  * Language packages: [Java](https://docs.cloud.google.com/artifact-registry/docs/java), [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs), [Python](https://docs.cloud.google.com/artifact-registry/docs/python), [Go](https://docs.cloud.google.com/artifact-registry/docs/go)
  * OS packages: [Debian](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian), [RPM](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm)

You can also [restrict artifact downloads with download rules](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
