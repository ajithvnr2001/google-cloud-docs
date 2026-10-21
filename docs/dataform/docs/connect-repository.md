---
url: https://docs.cloud.google.com/dataform/docs/connect-repository/
title: Connect to a third-party Git repository \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:01:23.396731+00:00
---

# Connect to a third-party Git repository  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/connect-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Connect to a third-party Git repository Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to connect a remote repository to a Dataform repository. After you connect the repositories, the changes you make in a Dataform development workspace can be pushed to and pulled from the remote Git repository.

You can connect a remote repository through Developer Connect, HTTPS, or SSH.

The following table lists supported Git providers and connection methods that are available for their repositories:

Git provider | Connection method  
---|---  
Azure DevOps Services | SSH  
Bitbucket | Developer Connect (recommended), SSH  
GitHub | Developer Connect (recommended), SSH, or HTTPS  
GitLab | Developer Connect (recommended), SSH, or HTTPS  
Secure Source Manager [(Preview)](https://cloud.google.com/products#product-launch-stages) | Developer Connect  
  
## Before you begin

  1. If your organization or project restricts remote Git repositories with the `dataform.restrictGitRemotes` Organization Policy, ensure that the remote Git repository is added to the allowlist in the policy before you create the Dataform repository that you want to connect to a remote repository. For more information, see [Restrict remote repositories](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes).
  2. Select or [create a Dataform repository](https://docs.cloud.google.com/dataform/docs/create-repository). You need the repository later to share a secret with your default [Dataform service agent](https://docs.cloud.google.com/dataform/docs/access-control#about-service-accounts).

**Note:** The Dataform repositories list includes only repositories created for Dataform workflow development. Repositories for BigQuery Studio assets, such as notebooks or saved queries, are managed separately and don't appear in this list.
  3. Ensure that you have the necessary permissions in your Git provider and that your Dataform repository is in a supported region.

  4. [Enable the Developer Connect API](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com).

  5. If you're connecting Developer Connect to a Bitbucket repository, ensure that your authorizer access token has write access to your repositories so that Dataform can push changes. For more information, see [Create access tokens](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-cloud#tokens).

  6. If you're connecting Developer Connect to a Secure Source Manager [(Preview)](https://cloud.google.com/products#product-launch-stages) instance, ensure that you have an [operational Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/enable-disable) and grant the Developer Connect service agent the `roles/securesourcemanager.developerConnectLinker` role on the Secure Source Manager instance's project. For more information, see [Connect to Secure Source Manager](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager#ssm-requirements).




### Network connectivity requirements and limitations

Before you connect your remote Git repository to Dataform, ensure that your network configuration meets the requirements for your chosen connection method.

#### Private network connections

Dataform doesn't support direct connections to [private IP addresses](https://en.wikipedia.org/wiki/IP_address) (for example, `10.x.x.x`, `172.16.x.x-172.31.x.x`, or `192.168.x.x`) of on-premises Git hosts or repositories in private networks using HTTPS or SSH. This includes access using a virtual private cloud (VPC), VPN, or Cloud Interconnect.

To connect to a repository in a private network, or if your Git host is behind a firewall, you must connect using Developer Connect.

#### Public network connections

To connect a remote Git repository using HTTPS or SSH, your Git host must have a [public IP address](https://en.wikipedia.org/wiki/IP_address#Public_address).

If you connect to a protected remote repository that has a public IP address using HTTPS or SSH, you must add the required [Dataform egress IP address ranges](https://docs.cloud.google.com/dataform/docs/locations) to your firewall rules.

#### VPC Service Controls requirements

If your project uses VPC Service Controls, you must set the `dataform.restrictGitRemotes` Organization Policy to connect to any third-party Git repository. For more information, see [Restrict remote repositories](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes).

### Required roles

To get the permissions that you need to connect a Dataform repository to a remote Git repository, ask your administrator to grant you the following IAM roles on repositories: 

  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`)
  * [Developer Connect Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.admin) (`roles/developerconnect.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To connect a remote repository using Developer Connect, grant the [Developer Connect Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.tokenAccessor) (`roles/developerconnect.tokenAccessor`) and [Developer Connect Git Proxy User](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.gitProxyUser) (`roles/developerconnect.gitProxyUser`) roles to the default Dataform service agent. Your default Dataform service agent ID is in the following format:
    
    
    service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com
    

**Important:** When granting roles to the default Dataform service agent, ensure you grant only the specific predefined roles required (such as Developer Connect Token Accessor and Git Proxy User). Granting overly permissive roles is a security risk.

## Connect a remote repository using Developer Connect

[Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview) streamlines the integration of external Git providers with Dataform repositories by providing a guided interface that removes the need for manual secrets management.

By using Developer Connect, you can connect to remote repositories in privately hosted networks—such as on-premises environments or virtual private clouds (VPCs)—without exposing them to the public internet.

**Important:** The Developer Connect proxy is required to connect to Git repositories in private networks and to Secure Source Manager [(Preview)](https://cloud.google.com/products#product-launch-stages) instances. When you create a new connection in the Google Cloud console, the proxy is enabled by default. For connections to publicly accessible Git repositories, the proxy is enabled by default but can be optionally disabled. For Secure Source Manager connections, the proxy must remain enabled. Dataform cannot access a Secure Source Manager repository if the proxy is disabled. To access a repository in a private network or in Secure Source Manager when using an existing connection created with the gcloud CLI or Developer Connect API, ensure that the proxy is enabled.**Note:** If the Dataform repository and Developer Connect connection are in different regions, additional cross-region data transfer costs might apply when the Developer Connect proxy is enabled. For more information, see [Developer Connect pricing](https://cloud.google.com/developer-connect/pricing).

### Prepare for private network connections

If you're connecting to a remote repository in a private network, ensure you have the following information and resources ready before starting the setup:

  * The namespace and service name of the [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview) service that points to your internal Git host.
  * A certification authority certificate in PEM format (with a maximum size of 10 KB) if your host uses a private or self-signed certificate authority.
  * Verification that your Git host's SSL certificate includes a subject alternative name (SAN) that matches the host URI.



For more information on configuring connections for privately hosted networks, see the following:

  * [Configure and use Developer Connect proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy)
  * [Connect to GitHub Enterprise in a private network](https://docs.cloud.google.com/developer-connect/docs/connect-github-enterprise-private)
  * [Connect to GitLab Enterprise repositories in a private network](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab-enterprise-private)
  * [Connect to Bitbucket Data Center repositories hosted in a private network](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-data-center-private)
  * [Connect to Secure Source Manager](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager) [(Preview)](https://cloud.google.com/products#product-launch-stages)



### Create a new Developer Connect connection

To connect a remote repository to a new Developer Connect connection, select one of the following options:

###  Bitbucket 

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select your repository.

  3. Go to **Settings** , and then click **Connect with Git**.

  4. In the **Link to remote repository** pane, in the **Remote Git repository protocol** section, select **Developer Connect**.

  5. In the repository selection menu, click **Link new repository**.

  6. In the **Link Git repositories via Developer Connect** pane, select **Create new connection**.

  7. Select **Bitbucket** as your provider.

  8. Specify the connection region and connection name.

  9. Provide the workspace name, authorizer access token, and read access token.

  10. Click **Continue** , then select the remote repositories to link and click **Link**.

  11. In Dataform, select your remote repository and the default branch.

  12. To complete the setup, click **Link**.




###  GitHub 

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select your repository.

  3. Go to **Settings** , and then click **Connect with Git**.

  4. In the **Link to remote repository** pane, in the **Remote Git repository protocol** section, select **Developer Connect**.

  5. In the repository selection menu, click **Link new repository**.

  6. In the **Link Git repositories via Developer Connect** pane, select **Create new connection**.

  7. Select **GitHub** as your provider.

  8. Specify the connection region and connection name.

  9. To trigger the OAuth authentication flow, click **Continue** , and then do the following:

     1. Click **I understand and continue**.
     2. Select **Install the GitHub App on another GitHub account** and follow the prompts to authorize access to your GitHub account and specific repositories.
     3. Select the account on which you want to install the Dataform GitHub application.
     4. In the **Repository access** section, select if you want to give access to all repositories or only a selection of repositories.
     5. Click **Save**.
  10. Select the remote repositories to link and click **Link**.

  11. In Dataform, select your remote repository and the default branch.

  12. To complete the setup, click **Link**.




###  GitLab 

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select your repository.

  3. Go to **Settings** , and then click **Connect with Git**.

  4. In the **Link to remote repository** pane, in the **Remote Git repository protocol** section, select **Developer Connect**.

  5. In the repository selection menu, click **Link new repository**.

  6. In the **Link Git repositories via Developer Connect** pane, select **Create new connection**.

  7. Select **GitLab** as your provider.

  8. Specify the connection region and connection name.

  9. Provide the API access token and the read API access token. For information on how to do this, see [Create access tokens](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab#tokens).

  10. Click **Continue** , then select the remote repositories to link and click **Link**.

  11. In Dataform, select your remote repository and the default branch.

  12. To complete the setup, click **Link**.




###  Secure Source Manager 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select your repository.

  3. Go to **Settings** , and then click **Connect with Git**.

  4. In the **Link to remote repository** pane, in the **Remote Git repository protocol** section, select **Developer Connect**.

  5. In the repository selection menu, click **Link new repository**.

  6. In the **Link Git repositories via Developer Connect** pane, select **Create new connection**.

  7. Select **Secure Source Manager** as your provider.

  8. Specify the connection region and connection name. The connection region must be the same region as your Secure Source Manager instance.

  9. In the **Instance** list, select your Secure Source Manager instance.

  10. Ensure that the Developer Connect proxy is enabled. The proxy is enabled by default under **Show more** and is required for Dataform to access Secure Source Manager repositories.

  11. Click **Continue** , then select the remote repositories to link and click **Link**.

  12. In Dataform, select your remote repository and the default branch.

  13. To complete the setup, click **Link**.




### Use an existing Developer Connect connection

To connect a remote repository to an existing Developer Connect connection, do the following:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select your repository.

  3. Go to **Settings** then click **Connect with Git**.

  4. In the **Link to remote repository** pane, in the **Remote Git repository protocol** section, select **Developer Connect**.

  5. In the repository selection menu, select a repository connected through an existing Developer Connect connection.

**Note:** If you select a repository connected through a Secure Source Manager [(Preview)](https://cloud.google.com/products#product-launch-stages) connection, the connection must have the Developer Connect proxy enabled. If the proxy is disabled on the connection, Dataform displays an error and cannot access the repository.
  6. In Dataform, select your remote repository and the default branch.

  7. To complete the setup, click **Link**.




## Connect a remote repository through SSH

To connect a remote repository through SSH, you need to generate an SSH key and a Secret Manager secret. The SSH key consists of a public SSH key and a private SSH key. You need to share the public SSH key with your Git provider, and create a Secret Manager secret with the private SSH key. Then, share the secret with your default Dataform service agent.

Dataform uses the secret with the private SSH key to sign in to your Git provider to commit changes on behalf of the developers. Dataform makes these commits using the developer's Google Cloud email address so you can tell who made each commit.

**Warning:** The private SSH key is shared among all Dataform users who have [act-as permissions](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) on the custom service account. We recommend that you create a machine user with your Git provider and limit its access to the remote Git repositories that you plan to use with Dataform. Only Google Cloud project owners and Dataform users with the [Dataform Admin role](https://docs.cloud.google.com/dataform/docs/access-control#dataform.admin) (`roles/dataform.admin`) can use the SSH key to connect repositories. Dataform users aren't able to see the SSH key itself.

To connect a remote repository to a Dataform repository through SSH, follow these steps:

  1. In your Git provider, do one of the following:

###  Azure DevOps Services 

     1. In Azure DevOps Services, [create a private SSH key](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#step-1-create-your-ssh-keys).
     2. [Upload the public SSH key](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#step-2-add-the-public-key-to-azure-devops) to your Azure DevOps Services repository.

###  Bitbucket 

     1. In Bitbucket, [create a private SSH key](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/).
     2. [Upload the public SSH key](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) to your Bitbucket repository.

###  GitHub 

     1. In GitHub, [create a private SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
     2. [Upload the GitHub public SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to your GitHub repository.

###  GitLab 

     1. In GitLab, [create a private SSH key](https://docs.gitlab.com/ee/user/ssh.html#generate-an-ssh-key-pair).
     2. [Upload the GitLab public SSH key](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account) to your GitLab repository.

  2. In Secret Manager, [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create) and set your private SSH key as the secret value.

     1. [Grant access to the secret to your default Dataform service agent](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

Your default Dataform service agent is in the following format:
            
            service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com
            

     2. Grant the [`roles/secretmanager.secretAccessor` role](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor) to the service account.

  3. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  4. Select the Dataform repository that you want to connect to the remote repository.

  5. On the repository page, click **Settings > Connect with Git**.

  6. In the **Link to remote repository** pane, in the **Remote Git repository URL** field, enter the URL of the remote Git repository, ending with `.git`.

The URL of the remote Git repository must be in one of the following formats:

     * Absolute URL: `ssh://git@{host_name}[:{port}]/{repository_path}`, `port` is optional.
     * SCP-like URL: `git@{host_name}:{repository_path}`.
  7. In the **Default remote branch name** field, enter the name of the main development branch of the remote Git repository.

  8. In the **Secret** drop-down, select your secret for the remote Git repository.

  9. In the **SSH public host key value** field, enter the public host key of your Git provider.

### Azure DevOps Services

     1. To retrieve the Azure DevOps Services public host key, run the following command in the terminal:
            
            ssh-keyscan -t rsa ssh.dev.azure.com
            

     2. Copy one of the outputted keys, omitting `ssh.dev.azure.com` from the beginning of the line. The value that you copy must be in the following format:
            
            ALGORITHM BASE64_KEY_VALUE
            

For example:
            
            ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7Hr1oTWqNqOlzGJOfGJ4NakVyIzf1rXYd4d7wo6jBlkLvCA4odBlL0mDUyZ0/QUfTTqeu+tm22gOsv+VrVTMk6vwRU75gY/y9ut5Mb3bR5BV58dKXyq9A9UeB5Cakehn5Zgm6x1mKoVyf+FFn26iYqXJRgzIZZcZ5V6hrE0Qg39kZm4az48o0AUbf6Sp4SLdvnuMa2sVNwHBboS7EJkm57XQPVU3/QpyNLHbWDdzwtrlS+ez30S3AdYhLKEOxAG8weOnyrtLJAUen9mTkol8oII1edf7mWWbWVf0nBmly21+nZcmCTISQBtdcyPaEno7fFQMDD26/s0lfKob4Kw8H
            

Verify this key is still up-to-date with Azure DevOps Services.

### Bitbucket

     1. To retrieve the Bitbucket public host key, run the following command in the terminal:
            
            curl https://bitbucket.org/site/ssh
            

     2. The command returns a list of public host keys. Choose one of the keys from the list, and copy it, omitting `bitbucket.org` from the beginning of the line. The value that you copy must be in the following format:
            
            ALGORITHM BASE64_KEY_VALUE
            

For example:
            
            ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIazEu89wgQZ4bqs3d63QSMzYVa0MuJ2e2gKTKqu+UUO
            

Verify this key is still up-to-date with Bitbucket.

### GitHub

     1. To retrieve the GitHub public host key, see [GitHub's SSH key fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints).
     2. The page contains a list of public host keys. Choose one of them, and copy it, omitting `github.com` from the beginning of the line. The value that you copy must be in the following format:
            
            ALGORITHM BASE64_KEY_VALUE
            

For example:
            
            ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl
            

Verify this key is still up-to-date with GitHub.

### GitLab

     1. To retrieve the GitLab public host key, see [SSH `known_hosts` entries](https://docs.gitlab.com/ee/user/gitlab_com/#ssh-known_hosts-entries).
     2. The page contains a list of public host keys. Choose one of them, and copy it, omitting `gitlab.com` from the beginning of the line. The value that you copy must be in the following format:
            
            ALGORITHM BASE64_KEY_VALUE
            

For example:
            
            ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAfuCHKVTjquxvt6CM6tdG4SLp1Btn/nOeHHE5UOzRdf
            

Verify this key is still up-to-date with GitLab.

  10. Click **Link**.




## Connect a remote repository through HTTPS

To connect a remote repository through HTTPS, you need to create a Secret Manager secret with a personal access token, and share the secret with your default Dataform service agent.

Dataform then uses the access token to sign in to your Git provider to commit changes on behalf of the developers. Dataform makes these commits using the developer's Google Cloud email address so you can tell who made each commit.

**Warning:** The private access token is shared among all Dataform users who have [act-as permissions](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) on the custom service account. We recommend that you create a machine user with your Git provider and limit its access to the remote Git repositories that you plan to use with Dataform. Only Google Cloud project owners and Dataform users with the [Dataform Admin role](https://docs.cloud.google.com/dataform/docs/access-control#dataform.admin) (`roles/dataform.admin`) can use the access token to connect repositories. Dataform users aren't able to see the access token itself.

To connect a remote repository to a Dataform repository through HTTPS, follow these steps:

  1. In your Git provider, do the following:

###  GitHub 

     1. In GitHub, create a [fine-grained personal access token](https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/) or a [classic personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#about-personal-access-tokens).

        * For a fine-grained GitHub personal access token, do the following:
        1. Select repository access to only selected repositories, then select the repository that you want to connect to.

        2. Grant read and write access on contents of the repository.

        3. Set a token expiration time appropriate to your needs.

        * For a classic GitHub personal access token, do the following:
        1. Grant Dataform the `repo` permission.

        2. Set a token expiration time appropriate to your needs.

     2. If your organization uses SAML single sign-on (SSO), [authorize the token](https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

###  GitLab 

     1. In GitLab, create a [GitLab personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

     2. Name the token `dataform`.

The GitLab personal access token must be named `dataform`.

     3. Grant Dataform the `api`, `read_repository`, and `write_repository` permissions.

     4. Set a token expiration time appropriate to your needs.

  2. In Secret Manager, [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create) containing the personal access token of your remote repository.

  3. [Grant access to the secret to your default Dataform service agent](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

Your default Dataform service agent is in the following format:
         
         service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com
         

     1. Grant the [`roles/secretmanager.secretAccessor` role](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor) to the service agent.
  4. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  5. Select the Dataform repository that you want to connect to the remote repository.

  6. On the repository page, click **Settings > Connect with Git**.

  7. In the **Link to remote repository** pane, in the **Remote Git repository URL** field, enter the URL of the remote Git repository, ending with `.git`.

The URL of the remote Git repository cannot contain usernames or passwords.

  8. In the **Default remote branch name** field, enter the name of the main development branch of the remote Git repository.

  9. In the **Secret** drop-down, select your secret for the remote Git repository.

  10. Click **Link**.




## Edit the remote repository connection

To edit a connection between a Dataform repository and a remote Git repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click the repository that you want to edit.

  3. On the repository page, click **Settings > Edit Git connection**.

  4. On the **Link to remote repository** pane, edit connection settings.

  5. Click **Update**.




## What's next

  * To learn more about Dataform repositories, see [Create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  * To create a development workspace, see [Create a workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  * To learn how to troubleshoot issues with remote repository connections, see [Troubleshoot Dataform](https://docs.cloud.google.com/dataform/docs/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
