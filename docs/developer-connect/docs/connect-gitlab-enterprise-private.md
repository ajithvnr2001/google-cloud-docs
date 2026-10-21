---
url: https://docs.cloud.google.com/developer-connect/docs/connect-gitlab-enterprise-private/
title: Connect to GitLab Enterprise repositories in a private network \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:27:11.409214+00:00
---

# Connect to GitLab Enterprise repositories in a private network  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/connect-gitlab-enterprise-private/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Connect to GitLab Enterprise repositories in a private network Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect to GitLab Enterprise repositories hosted in a private network by using Developer Connect and Service Directory. You can complete these tasks using the Google Cloud console, or the Google Cloud CLI. 

These instructions are for application developers, platform administrators, and security managers who want to use GitLab Enterprise source code repositories with Google. Specifically, you can use GitLab Enterprise repositories with [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview).

**Note:** Developer Connect also supports GitLab Community Edition. The steps in this document are for both GitLab Enterprise repositories and GitLab Community Edition repositories.

To learn more about Developer Connect, see [Developer Connect overview](https://docs.cloud.google.com/developer-connect/docs/overview).

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Developer Connect, Secret Manager, and Service Directory APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com,secretmanager.googleapis.com,servicedirectory.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Developer Connect, Secret Manager, and Service Directory APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com,secretmanager.googleapis.com,servicedirectory.googleapis.com)

  8. Ensure that you have access to an account on [GitLab Enterprise.](https://about.gitlab.com)

To help keep your team's work secure, we recommend that you complete the tasks in this guide using a [service account](https://docs.gitlab.com/ee/user/profile/service_accounts.html) or an account shared by your team, not a personal account.

  9. Ensure that you own a GitLab Enterprise repository, or have admin-level permissions on a shared repository. 
  10. Ensure that you have a Service Directory service resource for connecting to private networks, or [create a Service Directory service resource](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access). You can create the Service Directory service resource in the same project that you're using with Developer Connect, or you can use a different project.   


For connections to networks outside of Google Cloud, you might need to configure Service Directory differently. See Use Service Directory to reach hosts outside Google Cloud.

  11. Optional: Create a [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/create-key) (CMEK) for encrypting the authentication secrets that Developer Connect creates.
  12. Optional: To use the command-line instructions in this guide, complete the following steps: 
     1. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk). If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
     2. Create a [Developer Connect service account](https://docs.cloud.google.com/developer-connect/docs/access-control#sa) by running the following command, where PROJECT_ID is your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects): 
            
            gcloud beta services identity create \
                        --service=developerconnect.googleapis.com \
                        --project=PROJECT_ID
                    




### Host requirements

If you haven't installed a GitLab Enterprise Edition Server instance, see [the installation guide from GitLab Enterprise Edition](https://about.gitlab.com/install/) for instructions.

When following the instructions to install a GitLab Enterprise Edition Server instance, note the following:

  * You **must** configure your host to handle `HTTPS` protocol. Hosts configured with `HTTP` protocol are not supported.

  * You must configure your host with the same URL that is used to reach your host from Google Cloud. To learn more, see the GitLab documentation for [configuring the external URL](https://docs.gitlab.com/omnibus/settings/configuration.html#configure-the-external-url-for-gitlab). 




### Required roles

To get the permissions that you need to create connections and links, ask your administrator to grant you the following IAM roles: 

  * If you aren't the project owner: [Developer Connect Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.admin) (`roles/developerconnect.admin`) on your user account. 
  * If you plan to use a CMEK to encrypt the secrets that Developer Connect creates: [Cloud KMS CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the Secret Manager Service Account. 
  * If you plan to use the gcloud CLI to complete the steps in this guide: [Secret Manager Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) on the Developer Connect Service Account. 
  * If you plan to use the Google Cloud console to complete the steps in this guide: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on your user account. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** When you have the Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) role, the Google Cloud console can automatically grant necessary permissions on your behalf. If your administrator won't allow you to have the Project IAM Admin role, then ask your administrator to grant Secret Manager Admin (`roles/secretmanager.admin`) on the Developer Connect Service Account (`service-{projectNumber}@gcp-sa-devconnect.iam.gserviceaccount.com`). 

## Grant permissions to use Service Directory

Complete the following steps to let Developer Connect use Service Directory, and to let Service Directory access your VPC network resource.

  1. Grant permissions for the Developer Connect service account to use Service Directory by running the following commands:
         
         PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         
         SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-devconnect.iam.gserviceaccount.com"
         
         gcloud projects add-iam-policy-binding SERVICE_DIRECTORY_RESOURCE_PROJECT_ID \
             --member="serviceAccount:${SERVICE_ACCOUNT}" \
             --role="roles/servicedirectory.viewer"
         

Replace the following:

     * PROJECT_ID: your Google Cloud project ID.
     * SERVICE_DIRECTORY_RESOURCE_PROJECT_ID: the project ID for the Google Cloud project that contains your Service Directory service resource.
  2. Grant permissions for Service Directory to access your VPC network resource. The network resource can be in a different project.
         
         gcloud projects add-iam-policy-binding NETWORK_RESOURCE_PROJECT_ID \
             --member="serviceAccount:${SERVICE_ACCOUNT}" \
             --role="roles/servicedirectory.pscAuthorizedService"
         

Replace NETWORK_RESOURCE_PROJECT_ID with the project ID for the project that contains your VPC network resource.




## Use Service Directory to reach hosts outside Google Cloud

Service Directory uses the IP address range `35.199.192.0/19` to connect your host outside of Google Cloud. You must add this range to an allowlist in your firewall. Additionally, your private network needs to be configured to route this range through the Cloud VPN or Cloud Interconnect connection.

If your connection uses a Cloud Router, you can configure your connection to [communicate](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) the range to your private network.

To learn more, see [Configure private network access](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access).

### Use Cloud Load Balancing to reach hosts outside Google Cloud

If your network configuration does not allow you to route the Service Directory IP address range `35.199.192.0/19` to the Cloud VPN or Cloud Interconnect, you can [create a load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) using Cloud Load Balancing that directs traffic to your host.

When you create the Service Directory endpoint, make sure to use the IP address of the forwarding rule of the load balancer instead of the IP address of your host. You can use an [internal HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-int-https-hybrid) or an [internal transmission control protocol (TCP) load balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid) when creating your endpoint.

When creating your TCP load balancer, consider the following:

  * Only a hybrid connectivity network endpoint group (NEG) is required to reach your host.
  * The TCP load balancer does not require the unencrypted private key for your SSL certificate.
  * Your Cloud VPN setup needs to use Cloud Router with global dynamic routing. If your Cloud VPN uses static routing, you can use a proxy that uses Cloud Service Mesh instead. To learn more, see [Set up network edge services for hybrid deployments](https://docs.cloud.google.com/traffic-director/tutorials/network-edge-services-multi-environment).



To learn more about creating an HTTPS load balancer, see [Set up an internal Application Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-int-https-hybrid). To learn more about creating a TCP load balancer, see [Set up a regional internal proxy Network Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid).

## Create access tokens

To create access tokens in GitLab, complete the following steps:

  1. [Sign in to GitLab](https://gitlab.com/users/sign_in).

  2. Follow the instructions in the GitLab documentation to [create personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token), [group access tokens](https://docs.gitlab.com/user/group/settings/group_access_tokens/), or [project access tokens](https://docs.gitlab.com/user/project/settings/project_access_tokens/) with the following permissions:

     * One token with `api` scope for connecting and disconnecting repositories.
     * One token with `read_api` scope to allow Developer Connect to read source code in your repositories.
     * For group access tokens and project access tokens, the tokens must have a role of Maintainer or greater.



## Create a connection

This section describes how to create a connection between Developer Connect and GitLab Enterprise. If you're using the Google Cloud console, then you can also start adding links to repositories as you finish setting up your connection.

To create a new GitLab Enterprise connection, select one of the following options:

###  Console 

Initiate a connection by completing the following steps:

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

Developer Connect displays the **Git repositories** page.

     * **If you see a list of source code management providers:** Start configuring your first connection by selecting a source code management provider. Click **Connect** on the GitLab Enterprise card.
     * **If you see a table listing existing connections** : Set the source code management provider by clicking **Create connection** > **GitLab Enterprise**.

The **Create Connection** page opens.

  2. For **Region** , choose a [region](https://docs.cloud.google.com/developer-connect/docs/locations) for your connection resources.

     1. For **Name** , enter a name for your new connection.
  3. In the **Access Tokens** section, enter the [tokens](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab#tokens) for your account:

     * **API access token** : Enter the access token with `api` scope.
     * **Read API access token** : Enter the access token with `read_api` scope.

You are responsible for ensuring your GitLab tokens remain valid. GitLab tokens have a maximum lifetime of 365 days, unless otherwise specified by the token creator or an administrator. To learn how to manage token expiration settings and notifications, see the GitLab documentation on [personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html), [group access tokens](https://docs.gitlab.com/user/group/settings/group_access_tokens/), and [project access tokens](https://docs.gitlab.com/user/project/settings/project_access_tokens/).

  4. For **Host URL** , enter the URL of the host you want to connect to.

  5. Click **Show more** to see optional configuration settings.

     1. The **Enable Developer Connect proxy** checkbox is selected by default so that Developer Connect can act as a proxy for Git calls to GitLab Enterprise.

     2. In the **Networking** section, for **Network type** , choose **Private network**.

     3. For **CA Certificate** , click **Browse** to upload your self-signed certificate.

Your certificate must not exceed 10 KB in size and should be in PEM format (.pem, .cer, or .crt). If this section is left blank, a default set of certificates will be used in place.

     4. In the **Service Directory service** section, select the location of your service:

        * **In project`your-project`**
        * **In another project**
        * **Enter manually**

If you select **In another project** or **Enter manually** , specify your Google Cloud project ID. Select the project in the drop-down menu, or enter the project ID manually.

     5. **Region** : Select the region of your Service Directory service. The region specified for your service must match the region associated with your connection.

     6. **Namespace** : Select the namespace of your Service Directory service.

     7. **Service** : Select the Service Directory service name in your namespace.

     8. Optional: In the **Encryption** section, select a [CMEK key](https://docs.cloud.google.com/kms/docs/key-management-service) to encrypt Secret Manager secrets that Developer Connect creates.

  6. Click **Continue**.




Once the connection is created, the **Link repositories** page appears.

Complete the following steps to link repositories to your connection:

  1. In the list of available repositories, select the repositories you want to use.

  2. Click **OK**.

  3. Click **Link**.




Your connection is added to the **Connections** page and your repository links are added to the **Repositories** page in the Google Cloud console. You can add more links to existing connections at any time.

If you're setting up Gemini Code Assist, continue the process by following the steps in [Configure and use Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

###  gcloud 

  1. Create a webhook secret in Secret Manager by running the following command, where WEBHOOK_SECRET_NAME is a name for your webhook secret:
         
         cat /proc/sys/kernel/random/uuid | tr -d '\n' | gcloud secrets create WEBHOOK_SECRET_NAME
         

  2. Store your access tokens in Secret Manager by running the following commands:
         
         gcloud secrets create API_SECRET_NAME
         
         echo -n API_SECRET_DATA | gcloud secrets versions add API_SECRET_NAME --data-file=-
         
         gcloud secrets create READ_SECRET_NAME
         
         echo -n READ_SECRET_DATA | gcloud secrets versions add READ_SECRET_NAME --data-file=-
         

Replace the following:

     * API_SECRET_NAME: a name for the secret that stores the token with `api` scope.
     * API_SECRET_DATA: the token with `api` scope, similar to `glpat-XXXXXXXXXXXXXXXX`.
     * READ_SECRET_NAME: a name for the secret that stores the token with `read_api` scope.
     * READ_SECRET_DATA: the token with `read_api` scope, similar to `glpat-XXXXXXXXXXXXXXXX`.
  3. Run the [gcloud developer-connect connections create](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create) command to create a connection to GitLab Enterprise:
         
         gcloud beta developer-connect connections create CONNECTION_NAME \
             --location=REGION \
             --gitlab-config-read-authorizer-credential-user-token-secret-version=projects/PROJECT_ID/secrets/READ_SECRET_NAME/versions/VERSION \
             --gitlab-config-authorizer-credential-user-token-secret-version=projects/PROJECT_ID/secrets/API_SECRET_NAME/versions/VERSION \
             --gitlab-enterprise-config-host-uri=HOST_URI \
             --gitlab-enterprise-config-webhook-secret-version=projects/PROJECT_ID/secrets/WEBHOOK_SECRET_NAME/versions/VERSION \
             --git-proxy-config-enabled
         

Replace the following:

     * CONNECTION_NAME: the name of your connection.
     * REGION: the region for your connection.
     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project).
     * READ_SECRET_NAME: the name of the Secret Manager secret that contains the token with `read_api` scope.
     * API_SECRET_NAME: the name of the Secret Manager secret that contains the token with `api` scope.
     * VERSION: the version number of each secret. This can be `latest` to use the most recent version number.
     * HOST_URI: the URI for the host you want to connect to.
     * WEBHOOK_SECRET_NAME: the name of the Secret Manager secret that contains your webhook secret.
     * `--git-proxy-config-enabled` is an optional flag that allows Developer Connect to as a proxy for Git calls to GitLab Enterprise. You must enable this feature when running [Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview) on GitLab Enterprise source code repositories hosted in private networks.
     * `--gitlab-enterprise-config-ssl-ca-certificate` is an optional flag to add an SSL certificate, in the format `$HOME/my-ssl-ca.txt`.

Developer Connect completes the connection to GitLab. Next, link to repositories.




## Link to repositories using an existing connection

Once you have established a connection to GitLab Enterprise, you can link to repositories. You can repeat these steps later to link additional repositories as needed.

To create repository links on an existing GitLab Enterprise connection, select one of the following options:

###  Console 

Create links to repositories by completing the following steps:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the **Repositories** page](https://console.cloud.google.com/developer-connect/git-repository-links)

  2. Click **Link repository**.

The **Link Git repositories** pane opens.

  3. In the connections list, choose a connection.

  4. Click **Continue**.

  5. In the repositories list, select the repositories you want to link to.

Developer Connect displays suggested names for your repository resources.

  6. Select a repository resource naming option:

     * **Generated** : Use the generated repository resource names.
     * **Manual** : Input names of your own.
  7. Click **Create**.




Developer Connect creates the repository links and displays them in the Google Cloud console.

###  gcloud 

Link to a GitLab repository by running the following command:
    
    
    gcloud beta developer-connect connections git-repository-links create REPO_NAME \
        --clone-uri=REPO_URI \
        --connection=CONNECTION_NAME \
        --location=REGION
    

Replace the following:

  * REPO_NAME: the name for your repository link.
  * REPO_URI: the link to your repository, similar to `https://gitlab.com/my-project/test-repo.git`.
  * CONNECTION_NAME: the name of your connection.
  * REGION: the region of your connection.



Developer Connect creates the repository links.

To list linked repositories, run the [`developer-connect connections git-repository-links list`](https://cloud.google.com/sdk/gcloud/reference/beta/developer-connect/connections/git-repository-links/list) command.

If you're setting up Gemini Code Assist, continue the process by following the steps in [Configure and use Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

## What's next

  * [Finish setting up Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).
  * [Learn how Gemini Code Assist helps you accelerate software development](https://docs.cloud.google.com/gemini/docs/codeassist/overview).
  * [Explore other integrations available through Developer Connect.](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
