---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl/
title: Install Config Sync manually using kubectl \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:36.142803+00:00
---

# Install Config Sync manually using kubectl  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Install Config Sync manually using kubectl Stay organized with collections  Save and categorize content based on your preferences. 

When your environment requires direct, command-line Kubernetes resource management, installing Config Sync with `kubectl` commands lets you synchronize cluster configurations from a central source of truth. Although this installation method is supported, it isn't compatible with the Google Cloud console or the Google Cloud CLI. To manage Config Sync using those tools instead, see [Customize your Config Sync installation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync).

## Before you begin

This section describes prerequisites you must meet before installing Config Sync using `kubectl`.

### Prepare your local environment

Before you install Config Sync, make sure you have prepared your local environment by completing the following tasks:

  * Create, or have access to a source of truth.

  * Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud`, `kubectl`, and `nomos` commands used in these instructions. If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works), Google Cloud CLI comes pre-installed.

  * `kubectl` is not installed by default by Google Cloud CLI. To install `kubectl`, use the following command:
        
        gcloud components install kubectl
        

  * Authenticate to Google Cloud using the `gcloud auth login` command so that you can download components of Config Sync.




### Prepare your clusters

Create, or have access to, a Google Kubernetes Engine cluster that meets the [requirements for Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#cluster-requirements).

### Prepare permissions

The Google Cloud user installing Config Sync needs IAM permissions to create new roles in your cluster. If needed, grant these roles with the following commands:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME
    
    kubectl create clusterrolebinding cluster-admin-binding \
        --clusterrole cluster-admin --user USER_ACCOUNT
    

Replace the following:

  * `CLUSTER_NAME`: your cluster name
  * `USER_ACCOUNT`: your Google Cloud account's email address



Depending on how you configured the Google Cloud CLI on your local system, you might need to add the `--project` and `--zone` fields.

If you need to grant Config Sync access to OCI using `gcpserviceaccount` as your authentication type, to create a policy binding, you must also have the `iam.serviceAccounts.setIamPolicy` permission. You can get this permission by granting the Service Account Admin (`roles/iam.serviceAccountAdmin`) IAM role. You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Enroll a cluster

To enroll a cluster in Config Sync, complete the following steps:

  1. Deploy Config Sync
  2. Grant Config Sync read-only access to one of the following: 
     * Git
     * OCI
     * Helm
  3. Configure Config Sync



### Deploy Config Sync

After ensuring that you meet all the prerequisites, you can deploy Config Sync by downloading and applying a YAML manifest:

  1. Download the latest version of the Config Sync manifests using the following command. To download a specific version instead, see [Downloads](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/downloads).
         
         gcloud storage cp gs://config-management-release/released/latest/config-sync.tar.gz config-sync.tar.gz
         

  2. Extract the archive:
         
         tar -xzvf config-sync.tar.gz

  3. In the archive you extracted in the previous step, follow the instructions in the provided `README.md` file to edit the kustomization.

  4. To update the Config Sync installation, apply the rendered manifest that you built following the `README.md` instructions: 
         
         kubectl apply -f CONFIG_SYNC_MANIFEST
         

Replace `CONFIG_SYNC_MANIFEST` with the name of the rendered manifest.

  5. Replace the `nomos` command on all clients with the new version. This change ensures that the `nomos` command can always get the status of all enrolled clusters and can validate configs for them.




If this fails because of a problem with Config Sync that is not due to a YAML or JSON syntax error, the object might be instantiated in the cluster, but might not work correctly. In this situation, you can use the `nomos status` command to check for errors in the object.

A valid installation with no problems has a status of `PENDING` or `SYNCED`.

An invalid installation has a status of `NOT CONFIGURED` and lists one of the following errors:

  * `missing git-creds Secret`
  * `git-creds Secret is missing the key specified by secretType`



To fix the problem, correct the configuration error. Depending on the type of error, you might need to re-apply the Config Sync manifest to the cluster.

If the problem is that you forgot to create the `git-creds` Secret, Config Sync detects the Secret as soon as you create it, and you don't need to re-apply the configuration.

### Grant Config Sync read-only access

If you store your configs in Git, you must grant Config Sync read-only access to Git. If you store your configs as [OCI images](https://opencontainers.org/), you must grant Config Sync read-only access to OCI. If you store your configs in [Helm](https://helm.sh/), you must grant Config Sync read-only access to Helm.

#### Grant Config Sync read-only access to Git

Config Sync needs read-only access to your Git repository so that it can read the configs committed to the repository and apply them to your clusters.

If your repository does not require authentication for read-only access, you can continue to [configure Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#configuring-config-sync) and use `none` as your authentication type. For example, if you can browse the repository using a web interface without logging in, or if you can use `git clone` to create a clone of the repository locally without providing credentials or using saved credentials, then you don't need to authenticate. In this case, you don't need to create a Secret.

However, most users need to create credentials because read access to their repository is restricted. If credentials are required, they are stored in the `git-creds` Secret on each enrolled cluster (unless you are using a Google service account). The Secret must be named `git-creds` because this is a fixed value.

Config Sync supports the following mechanisms for authentication:

  * SSH key pair (`ssh`)
  * Cookiefile (`cookiefile`)
  * Token (`token`)
  * Google service account (`gcpserviceaccount`)
  * Compute Engine default service account (`gcenode`)
  * GitHub App (`githubapp`)



The mechanism that you choose depends on what your repository supports. Generally, we recommend using an SSH key pair. GitHub and Bitbucket both support using an SSH key pair. However, if you are using a repository in Cloud Source Repositories or Secure Source Manager, we recommend that you use a Google service account instead as the process is simpler. If your organization hosts your repository and you don't know which authentication methods are supported, contact your administrator.

To use a repository in Cloud Source Repositories as your Config Sync repository, complete the following steps to retrieve your Cloud Source Repositories URL:

  1. List all repositories:
         
         gcloud source repos list
         

  2. From the output, copy the URL from the repository that you want to use. For example:
         
         REPO_NAME  PROJECT_ID  URL
         my-repo    my-project  **https://source.developers.google.com/p/my-project/r/my-repo-csr**
         

You need to use this URL when you configure Config Sync in the following section. If you configure Config Sync using the Google Cloud console, you add the URL in the **URL** field. If you configure Config Sync using the Google Cloud CLI, you add the URL to the `syncRepo` field of your configuration file.




### SSH key pair

An SSH key pair consists of two files, a public key and a private key. The public key typically has a `.pub` extension.

**Warning:** Protect the files created by this command. They grant the ability to read from your repository.

To use an SSH key pair, complete the following steps:

  1. Create an SSH key pair to allow Config Sync to authenticate to your Git repository. This step is necessary if you need to authenticate to the repository to clone it or read from it. Skip this step if a security administrator provides you with a key pair. You can use a single key pair for all clusters, or a key pair per cluster, depending on your security and compliance requirements.

The following command creates a 4096-bit RSA key. Lower values are not recommended:
         
         ssh-keygen -t rsa -b 4096 \
         -C "GIT_REPOSITORY_USERNAME" \
         -N '' \
         -f /path/to/KEYPAIR_FILENAME
         

Replace the following:

     * `GIT_REPOSITORY_USERNAME`: the username that you want Config Sync to use to authenticate to the repository
     * `/path/to/KEYPAIR_FILENAME`: a path to the key pair

If you are using a third-party Git repository host such as GitHub, or you want to use a service account with Cloud Source Repositories, we recommend that you use a separate account.

**Note:** You must create the SSH key without a passphrase. Config Sync does not support SSH key passphrases.
  2. Configure your repository to recognize the newly created _public key_. Refer to the documentation for your Git hosting provider. Instructions for some popular Git hosting providers are included for convenience:

     * [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs/authentication#ssh)
     * [Bitbucket](https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html)
     * [GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) We recommend that you create separate [deploy keys](https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys) to provide read-only access to a single GitHub repository.
     * [GitLab](https://docs.gitlab.com/ee/user/ssh)
  3. Add the _private key_ to a new Secret in the cluster:
         
         kubectl create ns config-management-system && \
         kubectl create secret generic git-creds \
          --namespace=config-management-system \
          --from-file=ssh=/path/to/KEYPAIR_PRIVATE_KEY_FILENAME
         

Replace `/path/to/KEYPAIR_PRIVATE_KEY_FILENAME` with the name of the private key (the one without the `.pub` suffix).

  4. (Recommended) To configure _known hosts_ checking using SSH authentication, you can add the known hosts key to the `data.known_hosts` field in the `git_creds` secret. To disable `known_hosts` checking, you can remove the `known_hosts` field from the secret. To add the known hosts key, run:
         
         kubectl edit secret git-creds \
          --namespace=config-management-system
         

Then, under `data`, add the known hosts entry:
         
         known_hosts: KNOWN_HOSTS_KEY
         

  5. Delete the private key from the local disk or otherwise protect it.

  6. When you configure Config Sync and add the URL for your Git repository, use the SSH protocol. If you are using a repository in Cloud Source Repositories, you must use the following format when you enter your URL:
         
         ssh://EMAIL@source.developers.google.com:2022/p/PROJECT_ID/r/REPO_NAME
         

Replace the following:

     * `EMAIL`: your Google Cloud username
     * `PROJECT_ID`: the ID of the Google Cloud project where the repository is located
     * `REPO_NAME`: the name of the repository



### Cookiefile

**Note:** Using `cookiefile` credentials is only supported with [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories). If you would like to use GitHub with `cookiefile` authentication, you can use Cloud Source Repositories to [mirror](https://docs.cloud.google.com/source-repositories/docs/mirroring-a-github-repository) your GitHub repository.

The process for acquiring a `cookiefile` depends on the configuration of your repository. For an example, see [Generate static credentials](https://docs.cloud.google.com/source-repositories/docs/adding-repositories-as-remotes#generate_static_credentials) in the Cloud Source Repositories documentation. The credentials are usually stored in the `.gitcookies` file in your home directory, or they might be provided to you by a security administrator.

To use a `cookiefile`, complete the following steps:

  1. After you create and obtain the `cookiefile`, add it to a new Secret in the cluster.

If you don't use an HTTPS proxy, create the Secret with the following command:
         
         kubectl create ns config-management-system && \
         kubectl create secret generic git-creds \
          --namespace=config-management-system \
          --from-file=cookie_file=/path/to/COOKIEFILE
         

If you need to use an HTTPS proxy, add it to the Secret together with `cookiefile` by running the following command:
         
         kubectl create ns config-management-system && \
         kubectl create secret generic git-creds \
          --namespace=config-management-system \
          --from-file=cookie_file=/path/to/COOKIEFILE \
          --from-literal=https_proxy=HTTPS_PROXY_URL
         

Replace the following:

     * `/path/to/COOKIEFILE`: the appropriate path and filename
     * `HTTPS_PROXY_URL`: the URL for the HTTPS proxy that you use when communicating with the Git repository
**Note:** We don't recommend using an HTTP proxy for security reasons.
  2. Protect the contents of the `cookiefile` if you still need it locally. Otherwise, delete it.




### Token

If your organization does not permit the use of SSH keys, you might prefer to use a token. With Config Sync, you can use GitHub's personal access tokens (PATs), GiLab's PATs or deploy keys, or Bitbucket's app password as your token.

To create a Secret using your token, complete the following steps:

  1. Create a token using GitHub, GitLab, or Bitbucket:

     * **GitHub:** [Create a PAT](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line). Grant the token the `repo` scope so that it can read from private repositories. Because you bind a PAT to a GitHub account, we also recommend that you create a [machine user](https://developer.github.com/v3/guides/managing-deploy-keys/#machine-users) and bind your PAT to the machine user.
     * **GitLab** : [Create a PAT](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) or [create a deploy token](https://docs.gitlab.com/ee/user/project/deploy_tokens/)
     * **Bitbucket:** [Create an app password](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/).
  2. After you create and obtain the token, add it to a new Secret in the cluster.

If you don't use an HTTPS proxy, create the Secret with the following command:
         
         kubectl create ns config-management-system && \
         kubectl create secret generic git-creds \
           --namespace="config-management-system" \
           --from-literal=username=USERNAME \
           --from-literal=token=TOKEN
         

Replace the following:

     * `USERNAME`: the username that you want to use.
     * `TOKEN`: the token that you created in the previous step.

If you need to use an HTTPS proxy, add it to the Secret together with `username` and `token` by running the following command:
    
    kubectl create ns config-management-system && \
    kubectl create secret generic git-creds \
     --namespace=config-management-system \
     --from-literal=username=USERNAME \
      --from-literal=token=TOKEN \
     --from-literal=https_proxy=HTTPS_PROXY_URL
    

Replace the following:

     * `USERNAME`: the username that you want to use.
     * `TOKEN`: the token that you created in the previous step.
     * `HTTPS_PROXY_URL`: the URL for the HTTPS proxy that you use when communicating with the Git repository.
**Note:** We don't recommend using an HTTP proxy for security reasons.
  3. Protect the token if you still need it locally. Otherwise, delete it.




### Google service account

If your repository is in [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs) or in [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs), and your cluster uses [GKE Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity), you can give Config Sync access to a repository in the same project as your managed cluster by using a Google service account.

**Note:** Although granting IAM roles directly to a Kubernetes ServiceAccount principal (`principal://`) is the recommended best practice for [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), Config Sync Git authentication requires IAM service account impersonation because the `RootSync` and `RepoSync` `spec.git.gcpServiceAccountEmail` field requires an IAM service account email address.

  1. If you don't already have a service account, [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  2. Grant the correct IAM roles to the service account so it can access the repository:

###  Cloud Source Repositories 

Grant the Cloud Source Repositories Reader (`roles/source.reader`) IAM role to the Google service account. For more information about Cloud Source Repositories roles and permissions, see [Grant permissions to view repositories](https://docs.cloud.google.com/source-repositories/docs/granting-users-access#grant_permissions_to_view_repositories).

     * Grant project-wide permission if the same permissions apply to all repositories in the project.
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --role=roles/source.reader \
             --member="serviceAccount:GSA_NAME@PROJECT_ID.iam.gserviceaccount.com"
           

     * Grant repository-specific permission when you want service accounts to have different levels of access for each repository in your project.
           
           gcloud source repos set-iam-policy REPOSITORY POLICY_FILE --project=PROJECT_ID
           

###  Secure Source Manager 

Grant the Secure Source Manager Instance Accessor (`roles/securesourcemanager.instanceAccessor`) and Secure Source Manager Repo Reader (`roles/securesourcemanager.repoReader`) IAM roles to the Google service account. For more information about Secure Source Manager roles and permissions, see [Repository role management](https://docs.cloud.google.com/secure-source-manager/docs/access-control#view_a_repository).

     * Grant project-wide permission if the same permissions apply to all repositories in the project.
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --role=roles/securesourcemanager.instanceAccessor \
             --member="serviceAccount:GSA_NAME@PROJECT_ID.iam.gserviceaccount.com"
           
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --role=roles/securesourcemanager.repoReader \
             --member="serviceAccount:GSA_NAME@PROJECT_ID.iam.gserviceaccount.com"
           

     * To grant repository-specific permissions, you can use the Secure Source Manager web interface for the repository. For more information see [Grant users repository-level roles](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-repository-access#grant_users_repository-level_roles).

  3. If you configure Config Sync using the Google Cloud console, select **Workload Identity Federation for GKE** as the **Authentication Type** and then add your service account email.

If you configure Config Sync using the Google Cloud CLI, add `gcpserviceaccount` as the `secretType` and then add your service account email to `gcpServiceAccountEmail`.

  4. If you are using a repository in Secure Source Manager, you must use the following format when you configure Config Sync and add the URL for your Git repository:
         
         https://INSTANCE_ID-PROJECT_NUMBER-git.LOCATION.sourcemanager.dev/PROJECT_ID/REPO_NAME.git
         

Replace the following:

     * `INSTANCE_ID`: the name of your Secure Source Manager instance.
     * `PROJECT_ID`: the ID of the Google Cloud project where the instance is located.
     * `PROJECT_NUMBER`: the Google Cloud project number where the instance is located.
     * `LOCATION`: the region where your instance is located.
     * `REPO_NAME`: the name of the repository.
  5. _After_ configuring Config Sync, create an [IAM policy binding](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) between the Kubernetes service account and the Google service account. The Kubernetes service account is not created until you configure Config Sync for the first time.

If you are using clusters that are registered to a fleet, you only have to create the policy binding once per fleet. All clusters registered in a fleet share the same [Workload Identity Federation for GKEpool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools). With fleet's concept of [sameness](https://docs.cloud.google.com/anthos/multicluster-management/fleets#sameness), if you add the IAM policy to your Kubernetes service account in one cluster, then the Kubernetes service account from the same namespace on other clusters in the same fleet also get the same IAM policy.

This binding lets the Config Sync Kubernetes ServiceAccount act as the Google service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
             GSA_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/iam.workloadIdentityUser \
             --member="serviceAccount:FLEET_HOST_PROJECT_ID.svc.id.goog[config-management-system/KUBERNETES_SERVICEACCOUNT]" \
             --project=PROJECT_ID
         




Replace the following:

  * `PROJECT_ID`: the organization's project ID.
  * `FLEET_HOST_PROJECT_ID`: if you're using GKE Workload Identity Federation for GKE, this is the same as `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project ID of the fleet that your cluster is registered to.
  * `GSA_NAME`: the custom Google service account that you want to use to connect to Secure Source Manager or Cloud Source Repositories.
  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler: 
    * For root repositories, if the `RootSync` name is `root-sync`, use `root-reconciler`. Otherwise, use `root-reconciler-ROOT_SYNC_NAME`. If you install Config Sync using the Google Cloud console or the Google Cloud CLI, Config Sync automatically creates a `RootSync` object named `root-sync`.
  * `REPOSITORY`: the name of the repository.
  * `POLICY_FILE`: the JSON or YAML file with the Identity and Access Management policy.

**Note:** Creating this policy binding requires the `iam.serviceAccounts.setIamPolicy` permission.

###  Compute Engine default service account 

If your repository is in [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs), and your cluster is GKE with Workload Identity Federation for GKE disabled, you can use `gcenode` as your authentication type.

If you configure Config Sync using the Google Cloud console, select **Google Cloud Repository** as the **Authentication Type**.

If you configure Config Sync using the Google Cloud CLI, add `gcenode` as the `secretType`.

Selecting either **Google Cloud Repository** or `gcenode` lets you use the Compute Engine default service account. You must grant the Cloud Source Repositories Reader (`roles/source.reader`) IAM role to the Compute Engine default service account. For more information about Cloud Source Repositories roles and permissions, see [Grant permissions to view repositories](https://docs.cloud.google.com/source-repositories/docs/granting-users-access#grant_permissions_to_view_repositories).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --role=roles/source.reader \
      --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com"
    

Replace `PROJECT_ID` with your organization's project ID, and replace `PROJECT_NUMBER` with your organization's project number.

###  GitHub App 

If your repository is in GitHub, you can use `githubapp` as your authentication type.

To use a GitHub App, complete the following steps:

  1. Follow the [instructions on GitHub](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app#authentication-as-a-github-app) to provision a GitHub App and give it permission to read from your repository.

  2. Add the GitHub App configuration to a new Secret in the cluster:

###  Using Client ID 
         
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
     * Replace `BASE_URL` with the base URL for the GitHub API endpoint. This is only needed when the repository is not hosted at www.github.com. The argument can otherwise be omitted and will default to `https://api.github.com/`.

###  Using Application ID 
    
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
     * Replace `BASE_URL` with the base URL for the GitHub API endpoint. This is only needed when the repository is not hosted at www.github.com. The argument can otherwise be omitted and will default to `https://api.github.com/`.

  3. Delete the private key from the local disk or otherwise protect it.

  4. When you configure Config Sync and add the URL for your Git repository, use the `githubapp` auth type.




#### Grant Config Sync read-only access to OCI

Config Sync needs read-only access to your OCI image stored in Artifact Registry so that it can read the configs included in the image and apply them to your clusters.

If your image does not require authentication for read-only access, you can continue to configure Config Sync and use `none` as your authentication type. For example, if your image is public and can be accessed by anyone on the internet, then you don't need to authenticate.

However, most users need to create credentials to access restricted images. Config Sync supports the following mechanisms for authentication:

  * Kubernetes ServiceAccount (`k8sserviceaccount`)
  * Compute Engine default service account (`gcenode`)




### Kubernetes ServiceAccount

You can use a Kubernetes ServiceAccount as your authentication type if you store your OCI image in Artifact Registry and your cluster uses [GKE Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity).

Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) on the project or repository to the Kubernetes ServiceAccount. For more information about Artifact Registry roles and permissions, see [Configure roles and permissions for Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions).

  * Grant project-wide permission if the same permissions apply to all repositories in the project:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --role=roles/artifactregistry.reader \
            --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
            --condition=None
        

  * Grant repository-specific permission when you want service accounts to have different levels of access for each repository in your project:
        
        gcloud artifacts repositories add-iam-policy-binding REPOSITORY \
            --location=LOCATION \
            --role=roles/artifactregistry.reader \
            --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
            --project=PROJECT_ID \
            --condition=None
        




Replace the following:

  * `PROJECT_ID`: the organization's project ID.
  * `FLEET_HOST_PROJECT_NUMBER`: if you're using GKE Workload Identity Federation for GKE, this is the same as the project number for `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project number of the fleet that your cluster is registered to.
  * `FLEET_HOST_PROJECT_ID`: if you're using GKE Workload Identity Federation for GKE, this is the same as `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project ID of the fleet that your cluster is registered to.
  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler:
  * For root repositories, if the `RootSync` name is `root-sync`, use `root-reconciler`. Otherwise, use `root-reconciler-ROOT_SYNC_NAME`. If you install Config Sync using the Google Cloud console or the Google Cloud CLI, Config Sync automatically creates a `RootSync` object named `root-sync`.
  * `REPOSITORY`: the ID of the repository.
  * `LOCATION`: the regional or multi-regional location of the repository.

**Note:** Creating this policy binding requires the `resourcemanager.projects.setIamPolicy` permission (for project-wide access) or the `artifactregistry.repositories.setIamPolicy` permission (for repository-specific access).

###  Compute Engine default service account 

If you store your OCI image in Artifact Registry and your cluster is GKE with Workload Identity Federation for GKE disabled, you can use `gcenode` as your authentication type. Config Sync uses the Compute Engine default service account. You must grant your Compute Engine default service account reader access to Artifact Registry.

Grant the Compute Engine service account read permission to Artifact Registry by running the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
       --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
       --role=roles/artifactregistry.reader
    

Replace `PROJECT_ID` with your organization's project ID, and replace `PROJECT_NUMBER` with your organization's project number.

### Configure Config Sync for a Certificate Authority

For servers configured with certificates from a Certificate Authority (CA) that is not already trusted, Config Sync can be configured to use a CA certificate to verify HTTPS connections to the server. This is supported for Git, Helm, or OCI servers. The CA certificate must include full SSL certificates (Root/Intermediate/Leaf). If your server is already using a trusted CA or you are not connecting over HTTPS, you can skip this step and leave `caCertSecretRef` unset.

### `RootSync`

  1. Fetch the CA certificate which was used to issue the certificate for your Git server and save it to a file.

  2. For `RootSync` objects, the Secret must be created in the `config-management-system` namespace. For example: 
         
         kubectl create ns config-management-system &&   
         
         kubectl create secret generic ROOT_CA_CERT_SECRET_NAME   
         
          --namespace=config-management-system   
         
          --from-file=cert=/path/to/CA_CERT_FILE
         

  3. When you configure Config Sync, set the value of the `caCertSecretRef.name` field in the `RootSync` object to ROOT_CA_CERT_SECRET_NAME.




### `RepoSync`

  1. Fetch the CA certificate which was used to issue the certificate for your Git server and save it to a file.

  2. For `RepoSync` objects, the Secret must be created in the same namespace as the RepoSync. For example: 
         
         kubectl create ns REPO_SYNC_NAMESPACE &&   
         
         kubectl create secret generic NAMESPACE_CA_CERT_SECRET_NAME   
         
          --namespace=REPO_SYNC_NAMESPACE   
         
          --from-file=cert=/path/to/CA_CERT_FILE
         

  3. When you [configure the `RepoSync`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#manage-namespace-repos-in-namespace), set the value of the `caCertSecretRef.name` field in the `RepoSync` object to NAMESPACE_CA_CERT_SECRET_NAME.




#### Grant Config Sync read-only access to Helm

Config Sync needs read-only access to your Helm repository so that it can read the Helm charts in your repository and install them in your clusters.

If your repository does not require authentication for read-only access, you can continue to configure Config Sync and use `none` as your authentication type. For example, if your Helm repository is public and can be accessed by anyone on the internet, then you don't need to authenticate.

However, most users need to create credentials to access private Helm repositories. Config Sync supports the following mechanisms for authentication:

  * Token (`token`)
  * Kubernetes ServiceAccount (`k8sserviceaccount`)
  * Compute Engine default service account (`gcenode`)

**Note:** Config Sync doesn't support configuring `helm` as the source type using the Google Cloud console or the Google Cloud CLI. You can configure your `RootSync` or `RepoSync` object to sync from a Helm repository using the [Kubernetes API](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#kubernetes-api), or [declare it in another source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#managed-control). See [Configuration for the Helm repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository) for more information.

### Token

Create a Secret with a Helm repository username and password:
    
    
    kubectl create secret generic SECRET_NAME \
        --namespace=config-management-system \
        --from-literal=username=USERNAME \
        --from-literal=password=PASSWORD
    

Replace the following:

  * `SECRET_NAME`: the name that you want to give your Secret.
  * `USERNAME`: the Helm repository username.
  * `PASSWORD`: the Helm repository password.



When you Configure Config Sync, you will use the Secret name you chose for `spec.helm.secretRef.name`.

### Kubernetes ServiceAccount

You can use a Kubernetes ServiceAccount as your authentication type if you store your Helm chart in Artifact Registry and your cluster uses [GKE Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity).

Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) on the project or repository to the Kubernetes ServiceAccount. For more information about Artifact Registry roles and permissions, see [Configure roles and permissions for Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions).

  * Grant project-wide permission if the same permissions apply to all repositories in the project:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
           --role=roles/artifactregistry.reader \
           --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
           --condition=None
        

  * Grant repository-specific permission when you want service accounts to have different levels of access for each repository in your project:
        
        gcloud artifacts repositories add-iam-policy-binding REPOSITORY \
           --location=LOCATION \
           --role=roles/artifactregistry.reader \
           --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
           --project=PROJECT_ID \
           --condition=None
        




Replace the following:

  * `PROJECT_ID`: the organization's project ID.
  * `FLEET_HOST_PROJECT_NUMBER`: if you're using GKE Workload Identity Federation for GKE, this is the same as the project number for `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project number of the fleet that your cluster is registered to.
  * `FLEET_HOST_PROJECT_ID`: if you're using GKE Workload Identity Federation for GKE, this is the same as `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project ID of the fleet that your cluster is registered to.
  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler:
  * For root repositories, if the `RootSync` name is `root-sync`, use `root-reconciler`. Otherwise, use `root-reconciler-ROOT_SYNC_NAME`.
  * `REPOSITORY`: the ID of the repository.
  * `LOCATION`: the regional or multi-regional location of the repository.

**Note:** Creating this policy binding requires the `resourcemanager.projects.setIamPolicy` permission (for project-wide access) or the `artifactregistry.repositories.setIamPolicy` permission (for repository-specific access).

###  Compute Engine default service account 

If you store your Helm chart in Artifact Registry and your cluster is GKE with Workload Identity Federation for GKE disabled, you can use `gcenode` as your authentication type. Config Sync uses the Compute Engine default service account. You must grant your Compute Engine default service account reader access to Artifact Registry. You might need to [grant the `storage-ro` access scope](https://docs.cloud.google.com/artifact-registry/docs/access-control#gke-scope) to grant read-only permission to pull images.

Grant the Compute Engine service account read permission to Artifact Registry:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
        --role=roles/artifactregistry.reader
    

Replace `PROJECT_ID` with your organization's project ID, and replace `PROJECT_NUMBER` with your organization's project number.

### Configure Config Sync

To configure syncing from the root repository, you need to create a RootSync object that syncs your root repository to the cluster. You can only create one root repository per cluster and the root repository can be either an [unstructured repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo) or an [hierarchical repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo).

  1. If you're using the Config Sync admission webhook (the admission webhook is disabled by default) and are installing Config Sync in a private cluster, [add a firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#step_3_add_a_firewall_rule) to allow port `10250`. The Config Sync admission webhook uses port `10250` for drift prevention.

  2. Wait for the `RootSync` and `RepoSync` CRDs to be available:
         
         until kubectl get customresourcedefinitions rootsyncs.configsync.gke.io reposyncs.configsync.gke.io; do date; sleep 1; echo ""; done
         

  3. Save one of the following manifests as `root-sync.yaml`. Use the manifest version that corresponds to the source type for your configs.

### Git
         
         # root-sync.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
           name: ROOT_SYNC_NAME
           namespace: config-management-system
         spec:
           sourceType: git
           sourceFormat: unstructured
           git:
             repo: ROOT_REPOSITORY
             revision: ROOT_REVISION
             branch: ROOT_BRANCH
             dir: ROOT_DIRECTORY
             auth: ROOT_AUTH_TYPE
             gcpServiceAccountEmail: ROOT_EMAIL
             secretRef:
               name: ROOT_SECRET_NAME
             noSSLVerify: ROOT_NO_SSL_VERIFY
             caCertSecretRef:
               name: ROOT_CA_CERT_SECRET_NAME
         

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_REPOSITORY`: add the URL of the Git repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `ROOT_REVISION`: add the Git revision (tag or hash) or branch to sync from. This field is optional and the default value is `HEAD`. When using a hash, it must be a full hash, and not an abbreviated form.
     * `ROOT_BRANCH`: add the branch of the repository to sync from. This field is optional and the default value is `master`. We recommend using the `revision` field to specify a branch name for simplicity. If both the `revision` field and the `branch` field are specified, `revision` takes precedence over `branch`.
     * `ROOT_DIRECTORY`: add the path in the Git repository to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the repository.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `ssh`: Use a SSH key pair
       * `cookiefile`: Use a `cookiefile`
       * `token`: Use a token
       * `gcpserviceaccount`: Use a Google service account to access a Cloud Source Repositories.
       * `gcenode`: Use a Google service account to access a Cloud Source Repositories. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.

For more information on these authentication types, see [Granting Config Sync read-only access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_SECRET_NAME`: add the name of your Secret. If this field is set, you must add the Secret's public key to the Git provider. This field is optional.

     * `ROOT_NO_SSL_VERIFY`: To disable the SSL certificate verification, set this field to `true`. The default value is `false`.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Git provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses Git as the source.

### OCI
    
    # root-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: ROOT_SYNC_NAME
      namespace: config-management-system
    spec:
      sourceType: oci
      sourceFormat: unstructured
      oci:
        image: ROOT_IMAGE
        dir: ROOT_DIRECTORY
        auth: ROOT_AUTH_TYPE
        gcpServiceAccountEmail: ROOT_EMAIL
        caCertSecretRef:
          name: ROOT_CA_CERT_SECRET_NAME
    

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_IMAGE`: the URL of the OCI image to use as the root repository, for example `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`. By default, the image is pulled from the `latest` tag, but you can pull in images by `TAG` or `DIGEST` instead. Specify `TAG` or `DIGEST` in the `PACKAGE_NAME`: 
       * To pull by `TAG`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME:TAG`
       * To pull by `DIGEST`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME@sha256:DIGEST`
**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`**. Other formats (for example, `tar+bz2`) will not be recognized by Config Sync. Switching from a valid REPO to an OCI image with an unsupported format will cause managed resources to be pruned without an error.
     * `ROOT_DIRECTORY`: add the path in the repository to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the repository.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your OCI provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses an OCI image as the source.

### Helm
    
    # root-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: ROOT_SYNC_NAME
      namespace: config-management-system
    spec:
      sourceType: helm
      sourceFormat: unstructured
      helm:
        repo: ROOT_HELM_REPOSITORY
        chart: HELM_CHART_NAME
        version: HELM_CHART_VERSION
        releaseName: HELM_RELEASE_NAME
        namespace: HELM_RELEASE_NAMESPACE
        values:
          foo:
            bar: VALUE_1
          baz:
          - qux: VALUE_2
            xyz: VALUE_3
        includeCRDs: HELM_INCLUDE_CRDS
        auth: ROOT_AUTH_TYPE
          gcpServiceAccountEmail: ROOT_EMAIL
          secretRef:
            name: ROOT_SECRET_NAME
        caCertSecretRef:
          name: ROOT_CA_CERT_SECRET_NAME
    

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_HELM_REPOSITORY`: the URL of the Helm repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `HELM_CHART_NAME`: add the name of your Helm chart. This field is required.
     * `HELM_CHART_VERSION`: the version of your chart. This field is optional. If no value is specified, the latest version is used.
     * `HELM_RELEASE_NAME`: the name of the Helm release. This field is optional.
     * `HELM_RELEASE_NAMESPACE`: the target namespace for a release. It only sets a namespace for resources that contain `namespace: {{ .Release.Namespace }}` in their templates. This field is optional. If no value is specified, the default namespace `config-management-system` is used.
     * `HELM_INCLUDE_CRDS`: set to `true` if you want the Helm template to also generate a CustomResourceDefinition. This field is optional. If no value is specified, the default is `false` and a CRD won't be generated.
     * `VALUE`: values to use instead of default values that accompany the Helm chart. Format this field the same way as [helm chart's values.yaml](https://helm.sh/docs/chart_best_practices/values/) file. This field is optional.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `token`: Use a username and password to access a private Helm repository.
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_SECRET_NAME`: add the [name of your Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#helm-access) if `token` is the `ROOT_AUTH_TYPE`. This field is optional.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Helm provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses Helm as the source.

  4. Apply the changes:
         
         kubectl apply -f root-sync.yaml
         




### Provide a cluster name for cluster selectors (optional)

If you want to use [cluster-name-selectors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#limiting-configs), you must provide a cluster name to Config Sync. This step is optional and required only if you use cluster name selectors.

To provide a cluster name, complete the following steps:

  1. Add the `CLUSTER_NAME` environment variable to the `reconciler-manager` deployment:
         
         kubectl set env deployment/reconciler-manager -n config-management-system CLUSTER_NAME=CLUSTER_NAME
         

Replace `CLUSTER_NAME` with your cluster name or membership name.

  2. To propagate the cluster name to both RootSync and RepoSync reconcilers, restart the `reconciler-manager` deployment:
         
         kubectl rollout restart deployment/reconciler-manager -n config-management-system
         




## Verify the sync status of the root repository

You can use the [`nomos status` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command) to inspect the sync status of the root repository:
    
    
    nomos status
    

You should see output similar to the following example:
    
    
    my_managed_cluster-1
      --------------------
      <root>   git@github.com:foo-corp/acme/admin@main
      SYNCED   f52a11e4
    

## Verify the RootSync installation

When you create a RootSync object, Config Sync creates a reconciler with the `root-reconciler` prefix. A reconciler is a Pod that is deployed as a Deployment. It syncs manifests from a Git repository to a cluster.

You can verify that the RootSync object is working correctly by checking the status of the root-reconciler Deployment:
    
    
    kubectl get -n config-management-system deployment \
        -l configsync.gke.io/sync-name=ROOT_SYNC_NAME
    

Replace `ROOT_SYNC_NAME` with the name of RootSync.

You should see output similar to the following example:
    
    
    NAME              READY   UP-TO-DATE   AVAILABLE   AGE
    root-reconciler   1/1     1            1           3h42m
    

For further ways to explore the status of your RootSync object, see [Monitoring RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync).

After you have finished configuring your root repository, you can optionally choose to [configure syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories). These repositories are helpful if you want a repository that contains namespace-scoped configs synced to a particular namespace across clusters.

## Upgrade Config Sync

The steps to upgrade Config Sync depend on the version you're upgrading to and from. Starting in version 1.20.0, Config Sync is provided as a standalone install without the ConfigManagement Operator. If you're upgrading from a version before 1.20.0 to version 1.20.0 or later, you must first uninstall the ConfigManagement Operator before upgrading.

To upgrade from an unsupported version, perform a step-by-step upgrade with increments of no more than three minor versions at a time. For example, if the current Config Sync version is 1.16.0, first upgrade to version 1.19.0, and then to version 1.22.0.

### Uninstall the ConfigManagement Operator

If you're upgrading from a version before 1.20.0 to version 1.20.0 or later, you must first uninstall the ConfigManagement Operator before upgrading.

You can check if Config Management is installed on your cluster by running the following command:
    
    
    kubectl get configmanagement
    

If the output is not empty, Config Management is installed on the cluster. To uninstall Config Management, complete the following steps to uninstall Config Management but leave Config Sync installed on the cluster. We recommend using the `nomos CLI` to uninstall the ConfigManagement Operator because it has a richer interface and more robust error handling. You should only use the shell script if you don't have access to the `nomos CLI`.

**Caution:** Ensure [Hierarchy Controller is disabled](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-hierarchy-controller#kubectl) before proceeding.

### nomos (recommended)

  1. Make sure the [nomos CLI](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command) is on the latest version.

  2. Run the following command to update the cluster in your current kubectl context:
         
         nomos migrate --remove-configmanagement
         




### shell script

Copy the following shell script to a file and then run it to update the cluster in your current kubectl context.
    
    
     #!/bin/bash
    
     set -euox pipefail
    
     hnc_enabled="$(kubectl get configmanagements.configmanagement.gke.io config-management -o=jsonpath="{.spec.hierarchyController.enabled}" --ignore-not-found)"
    
     if [[ "${hnc_enabled}" == "true" ]]; then
       echo "Hierarchy Controller is enabled on the ConfigManagement object. It must be disabled before migrating."
       echo "This can be done by unsetting the spec.hierarchyController field on ConfigManagement."
       exit 1
     fi
    
     kubectl delete deployment -n config-management-system config-management-operator --ignore-not-found --cascade=foreground
    
     if kubectl get configmanagement config-management &> /dev/null ; then
       kubectl patch configmanagement config-management --type="merge" -p '{"metadata":{"finalizers":[]}}'
       kubectl delete configmanagement config-management --cascade=orphan --ignore-not-found
     fi
    
     kubectl delete clusterrolebinding config-management-operator --ignore-not-found
     kubectl delete clusterrole config-management-operator --ignore-not-found
     kubectl delete serviceaccount -n config-management-system config-management-operator --ignore-not-found
     kubectl delete customresourcedefinition configmanagements.configmanagement.gke.io --ignore-not-found
    

### Install the new Config Sync version

To upgrade Config Sync, complete the following steps for each enrolled cluster:

  1. [Download](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/downloads) the Config Sync manifest and `nomos` commands for the new version.

  2. Extract the archive:
         
         tar -xzvf config-sync.tar.gz

  3. In the archive you extracted in the previous step, follow the instructions in the provided `README.md` file to edit the kustomization.

**Note:** Editing the `kustomization.yaml` is required for some settings, for example [setting a cluster name for use with a ClusterSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#limiting-configs) or including the `admission-webhook.yaml` file for use with [drift prevention](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift).
  4. To update the Config Sync installation, apply the rendered manifest that you built following the `README.md` instructions: 
         
         kubectl apply -f CONFIG_SYNC_MANIFEST
         

Replace `CONFIG_SYNC_MANIFEST` with the name of the rendered manifest.

  5. Replace the `nomos` command on all clients with the new version. This change ensures that the `nomos` command can always get the status of all enrolled clusters and can validate configs for them.




## Uninstall Config Sync

**Caution:** Deleting a RootSync or RepoSync object does not clean up Config Sync annotations and labels, and the Config Sync admission webhook denies requests trying to delete these resources if Config Sync is still enabled in the cluster. The workaround is to unmanage or delete these managed resources before deleting the corresponding RootSync or RepoSync object.

To uninstall Config Sync, complete the following steps:

  1. A central administrator should remove the root repo:

     1. If you've [enabled the webhook](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift) and want to keep your resources, [disable drift prevention for abandoned resources](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift#disable_drift_prevention_for_abandoned_resources). If you haven't enabled the webhook, you don't have to take any additional steps to keep your resources.

     2. Delete the `RootSync` object by running the following command:
            
            kubectl delete -f root-sync.yaml
            

  2. [Remove any repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#remove).

  3. With the manifests you used to install Config Sync, you can also uninstall Config Sync.
         
         kubectl delete -f CONFIG_SYNC_MANIFEST --ignore-not-found
         


**Note:** Disabling this feature does not affect any configurations that Config Sync previously applied to your clusters.

## What's next

  * Discover how to [configure syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
