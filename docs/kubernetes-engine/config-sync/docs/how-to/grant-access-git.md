---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git/
title: Grant Config Sync access to your Git repository \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:08.273167+00:00
---

# Grant Config Sync access to your Git repository  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Grant Config Sync access to your Git repository Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to authenticate Config Sync to your Git repository. Config Sync requires read-only access to your source of truth so it can read your configurations, apply them to your clusters, and keep them in sync.

## Choose an authentication method

The authentication method that you use depends on what is supported for your source type.

The following table summarizes the authentication methods you can use with Config Sync:

Method | Supported sources | Description | Limitations  
---|---|---|---  
**No authentication** | Git, OCI, Helm | No additional setup required. | Only works if your source of truth is public.  
**SSH key pair** | Git | Supported by most Git providers. | Requires key management. Not supported for OCI or Helm.  
**token** | Git, OCI, Helm | Supported by most Git providers. Good alternative if your organization doesn't permit the use of SSH keys. Supports username and password for OCI and Helm. | Requires token management. Tokens can expire.  
**Kubernetes service account** | OCI, Helm | Uses IAM to grant Artifact Registry access directly to a Kubernetes service account. Requires Workload Identity Federation for GKE to be enabled on your cluster. | Not supported for Git.  
**Google service account** | Git | Uses IAM, which avoids storing credentials in Kubernetes Secrets. Recommended for Secure Source Manager and Cloud Source Repositories. Requires Workload Identity Federation for GKE to be enabled on your cluster. | Requires configuration before and after installing Config Sync on your clusters. Not supported for repositories hosted outside of Secure Source Manager or Cloud Source Repositories.  
**GitHub App** | Git | Direct integration with GitHub. Allows fine-grained permissions. | Only supported for repositories hosted in GitHub.  
  
Config Sync also supports the following authentication methods; however, these methods are only recommended if you can't use one of the options listed in the preceding table:

  * **cookiefile:** might not be supported for all Git providers. Not supported for OCI or Helm.
  * **Compute Engine default service account (`gcenode`):** not recommended because this method only works if Workload Identity Federation for GKE is disabled. Supported for Git, OCI, and Helm.
  * **Google service account for Helm and OCI:** supported, but not recommended because the Kubernetes service account method requires less configuration.



## Authentication with fleet packages

If you use [fleet packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/fleet-packages), you don't need to complete the instructions on this page. Fleet packages uses Cloud Build to authenticate to Git, which lets you authenticate once per project so you don't need to grant access every time that you install Config Sync on a cluster.

## Before you begin

Before you grant Config Sync read-only access to your Git repository, complete the following tasks:

  * Prepare, or have access to, a Git repository where you store your configuration files that you want Config Sync to sync. For more information, see the following resources:

    * [Add configs to a source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs): conceptual information about configurations.
    * [GitOps best practices](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices): tips and general best practices for organizing and managing your repository.
    * [Use an unstructured repo](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo): recommendations for using and organizing an unstructured repository.
  * Create, or have access to, a GKE cluster. Before creating a cluster, [review cluster configuration requirements and recommendations for Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/cluster-requirements).


**Important:** Protect any Secrets or sensitive information created as part of the steps on this page. For example, you can delete the file if you don't need it, or store it in a secure way.

## Use an SSH key pair

An SSH key pair consists of two files, a public key and a private key. Config Sync does not support creating passphrases. Depending on your security and compliance requirements, you can use a single key pair for all clusters, or a key pair per cluster.

To grant Config Sync read-only access to your Git repository by using an SSH key pair, complete the following steps:

  1. Create, or ask your security administrator to provide, an SSH key pair. If you need to create an SSH key pair, create a 4096-bit RSA key by running the following command:
         
         ssh-keygen -t rsa -b 4096 \
           -C "GIT_REPOSITORY_USERNAME" \
           -N '' \
           -f /path/to/KEYPAIR_FILENAME
         

Replace the following:

     * `GIT_REPOSITORY_USERNAME`: the username that you want Config Sync to use to authenticate to the repository. If you use a third-party Git repository host like GitHub, or you want to use a service account with Secure Source Manager, we recommend that you use a separate account for authentication.
     * `/path/to/KEYPAIR_FILENAME`: the path to the key pair file.
  2. Configure your repository to recognize the newly created public key. Refer to the documentation for your Git hosting provider. You can find instructions for some common Git hosting providers in the following list:

     * [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/ssh-keys)
     * [Bitbucket](https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html)
     * [GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
     * [GitLab](https://docs.gitlab.com/ee/user/ssh)
  3. Create the `git-creds` Secret with the private key:
         
         kubectl create ns config-management-system && \
         kubectl create secret generic git-creds \
             --namespace=config-management-system \
             --from-file=ssh=/path/to/KEYPAIR_PRIVATE_KEY_FILENAME
         

**Note:** If you need to use a proxy, pass the `--from-literal=https_proxy=HTTPS_PROXY_URL` flag.

Replace `/path/to/KEYPAIR_PRIVATE_KEY_FILENAME` with the name of the private key.

  4. Optional, but recommended: To configure known hosts checking when using SSH authentication, add the known hosts key to the `data.known_hosts` field in the `git_creds` Secret.

     1. To add the known hosts key, run the following command:
            
            kubectl edit secret git-creds --namespace=config-management-system
            

     2. To add the `known_hosts` entry under `data`, run the following command:
            
            known_hosts: KNOWN_HOSTS_KEY
            

Replace `KNOWN_HOSTS_KEY` with the known hosts key.

To disable `known_hosts` checking, remove the `known_hosts` field from the Secret.




When you install Config Sync, use SSH key pair (`ssh`) as the authentication type.

When you enter the URL of your Git repository, the URL must use SSH protocol format. The format of the URL differs depending on the Git provider.

## Use a cookiefile

The process for acquiring a `cookiefile` depends on the configuration of your repository. Generally, credentials are stored in a `.gitcookies` file in a home directory, or a security administrator provides them.

To grant Config Sync read-only access to your Git repository by using a `cookiefile`, complete the following steps:

After you create or obtain the `cookiefile`, add it to a new Secret in the cluster. We recommend that you use HTTPS for security reasons:
    
    
    kubectl create ns config-management-system && \
    kubectl create secret generic git-creds \
      --namespace=config-management-system \
      --from-file=cookie_file=/path/to/COOKIEFILE
    

Replace `/path/to/COOKIEFILE` with your path and filename.

**Note:** If you need to use a proxy, pass the `--from-literal=https_proxy=HTTPS_PROXY_URL` flag.

When you install Config Sync, use cookiefile (`cookiefile`) as the authentication type.

## Use a token

If your organization does not permit the use of SSH keys, you might prefer to use a token.

To grant Config Sync read-only access to your Git repository by using a token, complete the following steps:

  1. Generate a token from your Git provider. Refer to the documentation for your Git hosting provider for instructions. You can find instructions for some common Git hosting providers in the following list:

     * **GitHub:** [Create a PAT](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line). Grant the token the `repo` scope so that it can read from private repositories. Because you bind a PAT to a GitHub account, we also recommend that you create a [machine user](https://developer.github.com/v3/guides/managing-deploy-keys/#machine-users) and bind your PAT to the machine user.
     * **GitLab** : [Create a PAT](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) or [create a deploy token](https://docs.gitlab.com/ee/user/project/deploy_tokens/).
     * **Bitbucket:** [Create an app password](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/).
  2. After you create or obtain a token, add it to a new Secret in the cluster. We recommend that you use HTTPS for security reasons:
         
         kubectl create ns config-management-system && \
         kubectl create secret generic git-creds \
           --namespace=config-management-system \
           --from-literal=username=USERNAME \
           --from-literal=token=TOKEN
         

**Note:** If you need to use a proxy, pass the `--from-literal=https_proxy=HTTPS_PROXY_URL` flag.

Replace the following:

     * `USERNAME`: the username that you want to use.
     * `TOKEN`: the token that you created in the previous step.



When you install Config Sync, use token (`token`) as the authentication type.

## Use a Google service account

You can grant Config Sync access to a repository in the same project as your managed cluster by using a Google service account. You must meet the following requirements:

  * Your repository is in [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview) or [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs).
  * Your cluster has [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) enabled.

**Note:** Although granting Identity and Access Management (IAM) roles directly to a Kubernetes ServiceAccount principal (`principal://`) is the recommended best practice for [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), Config Sync Git authentication requires IAM service account impersonation because the `RootSync` and `RepoSync` `spec.git.gcpServiceAccountEmail` field requires an IAM service account email address.

To grant Config Sync read-only access to your Git repository by using a Google service account, complete the following steps:

  1. To get the permissions that you need to create a policy binding, ask your administrator to grant you the [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) IAM role on the service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. If you don't already have a service account, [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

  3. Grant the IAM role to the Google service account, depending on the repository type that you're using:

###  Secure Source Manager 

Grant the Secure Source Manager Instance Accessor (`roles/securesourcemanager.instanceAccessor`) and Secure Source Manager Repo Reader (`roles/securesourcemanager.repoReader`) IAM roles to the Google service account:

     * Grant project-wide permission if the same permissions apply to all repositories in the project:
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --role=roles/securesourcemanager.instanceAccessor \
             --member="serviceAccount:GSA_NAME@PROJECT_ID.iam.gserviceaccount.com"
           
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --role=roles/securesourcemanager.repoReader \
             --member="serviceAccount:GSA_NAME@PROJECT_ID.iam.gserviceaccount.com"
           

Replace the following:

       * `PROJECT_ID`: your project ID.
       * `GSA_NAME`: the name of the Google service account that you want to connect to Secure Source Manager.
     * To grant repository-specific permission, see the Secure Source Manager documentation for [Granting users repository-level roles](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-repository-access#grant_users_repository-level_roles).

When you install Config Sync, use **Workload Identity** (`gcpserviceaccount`) as the authentication type. You must also add your service account email.

Secure Source Manager requires a specific format for the repository URL: `https://SSM_INSTANCE_ID-PROJECT_NUMBER-git.INSTANCE_LOCATION.sourcemanager.dev/PROJECT_ID/REPO_NAME.git`.

###  Cloud Source Repositories 

Grant the Cloud Source Repositories Reader (`roles/source.reader`) IAM role to the Google service account:

     * Grant project-wide permission if the same permissions apply to all repositories in the project:
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --role=roles/source.reader \
             --member="serviceAccount:GSA_NAME@PROJECT_ID.iam.gserviceaccount.com"
           

Replace the following:

       * `PROJECT_ID`: your project ID.
       * `GSA_NAME`: the name of the Google service account that you want to connect to Cloud Source Repositories.
     * Grant repository-specific permission when you want service accounts to have different levels of access for each repository in your project:
           
           gcloud source repos set-iam-policy REPOSITORY POLICY_FILE --project=PROJECT_ID
           

Replace the following:

       * `PROJECT_ID`: your project ID.
       * `REPOSITORY`: the name of the repository.
       * `POLICY_FILE`: the JSON or YAML file that contains the Identity and Access Management policy.

When you install Config Sync, use **Workload Identity** (`gcpserviceaccount`) as the authentication type. You must also add your service account email.




The following step must be completed **after** configuring Config Sync because the Kubernetes ServiceAccount is not created until you configure Config Sync for the first time. You only need to do this once per fleet. To create the binding that lets the Kubernetes ServiceAccount act as the Google service account, run the following command:
    
    
    gcloud iam service-accounts add-iam-policy-binding \
        GSA_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --role=roles/iam.workloadIdentityUser \
        --member="serviceAccount:FLEET_HOST_PROJECT_ID.svc.id.goog[config-management-system/KUBERNETES_SERVICEACCOUNT]" \
        --project=PROJECT_ID
    

Replace the following:

  * `FLEET_HOST_PROJECT_ID`: if you use Workload Identity Federation for GKE, the value is the same as `PROJECT_ID`. If you use fleet Workload Identity Federation for GKE, use the project ID of the fleet that your cluster is registered to as the value.
  * `GSA_NAME`: the custom Google service account that you want to use to connect to Secure Source Manager or Cloud Source Repositories.
  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler. In most cases, the value is `root-reconciler` because Config Sync automatically creates a `RootSync` object named `root-sync` when installed with the Google Cloud console or the Google Cloud CLI. Otherwise, use `root-reconciler-ROOT_SYNC_NAME` as the value.



If you have issues connecting to Config Sync with a Google service account, refer to [Troubleshooting permission issues with a Google service account](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/permission-service-account).

## Use a Compute Engine default service account

As an alternative to a Google service account, if you don't have Workload Identity Federation for GKE enabled, you can use a Compute Engine service account to authenticate. This method is supported only for repositories in Secure Source Manager and Cloud Source Repositories.

To grant Config Sync read-only access to your repository by using a Compute Engine default service account, grant the default service account the `roles/source.reader` role:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --role=roles/source.reader \
      --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com"
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `PROJECT_NUMBER`: with your project number.



When you install Config Sync, use **Google Cloud Repository** (`gcenode`) as the authentication type.

## Use a GitHub App

If your repository is in GitHub, you can use the GitHub App to connect your repository to Config Sync:

  1. Follow the [instructions on GitHub](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app#authentication-as-a-github-app) to provision a GitHub App and give it permission to read from your repository.

  2. Add the GitHub App configuration to a new Secret in the cluster by using either the client or application ID:

###  client ID 
         
         kubectl create ns config-management-system && \
         kubectl create secret generic git-creds \
           --namespace=config-management-system \
           --from-literal=github-app-client-id=CLIENT_ID \
           --from-literal=github-app-installation-id=INSTALLATION_ID \
           --from-file=github-app-private-key=/path/to/GITHUB_PRIVATE_KEY \
           --from-literal=github-app-base-url=BASE_URL
         

     * Replace `CLIENT_ID` with the client ID for the GitHub App.
     * Replace `INSTALLATION_ID` with the installation ID for the GitHub App.
     * Replace `/path/to/GITHUB_PRIVATE_KEY` with the name of the file containing the private key.
     * Replace `BASE_URL` with the base URL for the GitHub API endpoint. This value is only needed when the repository is not hosted at www.github.com. The argument can otherwise be omitted and defaults to `https://api.github.com/`.

###  application ID 
    
    kubectl create ns config-management-system && \
    kubectl create secret generic git-creds \
        --namespace=config-management-system \
        --from-literal=github-app-application-id=APPLICATION_ID \
        --from-literal=github-app-installation-id=INSTALLATION_ID \
        --from-file=github-app-private-key=/path/to/GITHUB_PRIVATE_KEY \
        --from-literal=github-app-base-url=BASE_URL
    

     * Replace `APPLICATION_ID` with the application ID for the GitHub App.
     * Replace `INSTALLATION_ID` with the installation ID for the GitHub App.
     * Replace `/path/to/GITHUB_PRIVATE_KEY` with the name of the file containing the private key.
     * Replace `BASE_URL` with the base URL for the GitHub API endpoint. This value is only required if the repository is not hosted at www.github.com. The argument can otherwise be omitted and defaults to `https://api.github.com/`.




When you install Config Sync, use GitHub app (`githubapp`) as the authentication type.

## Troubleshooting

For help troubleshooting issues related to connecting Config Sync to your source of truth, review the following troubleshooting topics:

  * [Connecting to the source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/connection-source-of-truth)
  * [Permission issues with a Google service account](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/permission-service-account)



## What's next

  * [Install Config Sync with default settings](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default)
  * [Customize your Config Sync installation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
