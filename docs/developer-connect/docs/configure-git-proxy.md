---
url: https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy/
title: Configure and use Developer Connect proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:51.300514+00:00
---

# Configure and use Developer Connect proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Configure and use Developer Connect proxy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Developer Connect proxy.

Developer Connect proxy enhances how Developer Connect handles authentication and network access to source code management systems (SCMs), arbitrary HTTP endpoints ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), and connections to providers of non-Google developer tools, using [account connectors](https://docs.cloud.google.com/developer-connect/docs/account-connectors) .

When you enable the proxy for a system connection or an account connector, Developer Connect uses the proxy server to issue Git requests, such as `git clone`, or API calls to HTTP endpoints ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). When you create a connection using Google Cloud console, the proxy is enabled by default. This way, you only need to grant IAM permissions to a user or service account instead of managing an access token in Secret Manager.

For example, enabling Developer Connect proxy on a connection lets you do the following:

  * Use [Gemini Code Assist](https://developers.google.com/gemini-code-assist/docs/overview) code customization with SCMs in privately-hosted networks, including on-premise networks.
  * Clone source code from an external SCM using Google Cloud authentication and Identity and Access Management permissions.

  * Use Gemini Code Review Agent with SCMs in privately-hosted networks, including on-premise networks ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).




Developer Connect supports two types of proxy:

  * Proxy on system connections

System-connection proxy includes the following:

    * Git proxy

For connections to source code management systems (SCMs)

    * HTTP proxy ([Preview](https://docs.cloud.google.com/products#product-launch-stages))

For connections to arbitrary HTTP endpoints

  * Proxy for account connectors

The Developer Connect proxy can be used with [account connectors](https://docs.cloud.google.com/developer-connect/docs/account-connectors).




All of these are enabled using the same setting.

## Before you begin

Ensure that you have at least one system connection in Developer Connect (to an SCM such as GitHub, GitLab, or Bitbucket, or to an HTTP endpoint) or an account connector.

To get the permissions that you need to configure Developer Connect proxy for a connection, ask your administrator to grant you the Developer Connect Admin (`developerconnect.admin`) IAM role on the user that enables or disables the Developer Connect proxy. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To get the permissions that you need to issue requests to the proxy for a connection, ask your administrator to grant you the following IAM roles on the user account or service account that issues Git requests: 

  * Make Git read requests such as `git clone`, for system connections: [Git Proxy Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.gitProxyReader) (`roles/developerconnect.gitProxyReader`) 
  * Make Git write requests such as `git push`, for system connections: [Git Proxy User ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.gitProxyUser) (`roles/developerconnect.gitProxyUser`) 
  * Make Git read and write requests for account connectors: Account Connector OAuth User (`roles/developerconnect.oauthUser`) 



## Enable and disable Developer Connect proxy settings for system connections

When you create a system connection using the Google Cloud console, the proxy is enabled by default. When it's enabled, both Git proxy and HTTP proxy are enabled.

To view and update proxy settings, do the following:

###  Console 

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

  2. Click the **Connections** tab, and then click the name of the connection that you want to use.

  3. On the **Connection details** page, click the **Additional configuration** tab.

  4. Click the **Developer Connect proxy** toggle to disable or re-enable the Developer Connect proxy feature.

Developer Connect proxy is enabled by default.




###  Google Cloud CLI 

### Enable the Developer Connect proxy setting for a connection

To enable Developer Connect proxy for a connection, enable the proxy setting by running the `gcloud developer-connect connections update` command:
    
    
    gcloud developer-connect connections update CONNECTION_NAME \
    --location=REGION \
    --git-proxy-config-enabled
    

### Disable the Developer Connect proxy for a connection

To disable Developer Connect proxy for a connection, disable the proxy setting by running the `gcloud developer-connect connections update` command:
    
    
    gcloud developer-connect connections update CONNECTION_NAME \
    --location=REGION \
    --no-git-proxy-config-enabled
    

### View the proxy setting for a connection

To view details about the Developer Connect proxy setting for a connection, run the `gcloud developer-connect connections describe` command:
    
    
    gcloud developer-connect connections describe CONNECTION_NAME \
    --location=REGION
    

Replace the following:

  * CONNECTION_NAME with the name of your connection.
  * REGION with the [region](https://docs.cloud.google.com/developer-connect/docs/locations) of your connection.



The rest of this document includes instructions Git proxy only.

## Enable and disable Developer Connect proxy settings for account connectors

When you create an account connector using the Google Cloud console, the proxy is enabled by default. When it's enabled, both Git proxy and HTTP proxy are enabled.

To view and update proxy settings, do the following:

###  Console 

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

  2. Click the **Account Connectors** tab, and then click the name of the account connector that you want to use.

  3. On the **Connector details** page, click the **Configuration** tab.

  4. Click the **Developer Connect proxy** toggle to disable or re-enable the Developer Connect proxy feature.

Developer Connect proxy is enabled by default.




###  Google Cloud CLI 

### Enable the Developer Connect proxy setting for an account connector

To enable Developer Connect proxy for an account connector, run the following command:
    
    
    gcloud alpha developer-connect account-connectors update CONNECTOR_NAME \
      --location=REGION \
      --proxy-config-enabled
    

### Disable the Developer Connect proxy for an account connector

To disable Developer Connect proxy for a connection, run the following command:
    
    
    gcloud alpha developer-connect account-connectors update CONNECTOR_NAME \
      --location=REGION \
      --no-proxy-config-enabled
    

### View the proxy setting for an account connector

To view details about the Developer Connect proxy setting for a connection, run following command:
    
    
    gcloud alpha developer-connect account-connectors describe CONNECTOR_NAME \
      --location=REGION
    

Replace the following:

  * CONNECTOR_NAME with the name of your account connector.
  * REGION with the [region](https://docs.cloud.google.com/developer-connect/docs/locations) of your account connector.



## Find the Git proxy URI

### For system connections

With Developer Connect proxy enabled, you can find the Git proxy URI for your system connection by doing the following:

###  Console 

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

  2. Click the **Connections** tab, and then click the name of the connection that you want to use.

  3. In the **Connection details** page, click the **Repositories** tab.

  4. Find the repository for your connection, and then click **Copy git proxy URL**.




###  Google Cloud CLI 

To get the Git proxy URI, run the `gcloud developer-connect connections git-repository-links describe` command:
    
    
    gcloud developer-connect connections git-repository-links describe REPOSITORY_NAME \
    --connection=CONNECTION_NAME \
    --location=REGION
    

Replace the following:

  * REPOSITORY_NAME with the name of your repository.
  * CONNECTION_NAME with the name of your connection.
  * REGION with the [region](https://docs.cloud.google.com/developer-connect/docs/locations) of your connection.



###  Developer Connect API 

The Git proxy URI is located in the `git_proxy_url` field of the [GitRepositoryLink](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks#GitRepositoryLink) for your connection.

### For account connectors

With Developer Connect proxy enabled, you can construct the Git proxy URI for your account connector using the following format:
    
    
    https://REGION-git.developerconnect.dev/a/PROJECT_ID/CONNECTOR_NAME/REPO_PATH
    

Where:

  * `REGION` is the region in which you created your account connector.

  * `PROJECT_ID` is the ID of the project in which you created your account connector.

  * `CONNECTOR_NAME` is the name of the account connector in which you've enabled Git proxy.

  * `REPO_PATH` is everything after the domain in the git URL for your repository.

For example, if the repository URL is `https://github.com/myusername/test-repo.git`, the `REPO_PATH` is `myusername/test-repo`.




## Issue requests to the Git proxy

After you have your Git proxy URI, you can issue requests to the Git proxy by doing the following:

  1. Configure the Git CLI to use the Google Cloud CLI credential helper:

`git config --global credential.'https://*.developerconnect.dev'.helper gcloud.sh`

  2. Issue a request to the Git proxy. This example is a `git clone` request.

For account connectors:
         
         git clone https://REGION-git.developerconnect.dev/a/PROJECT_ID/ACCOUNT_CONNECTOR_NAME/REPO_PATH
         

If you don't want to use a credential helper, then you can embed the cloud access token into the request instead:
         
         git clone https://unused:$(gcloud auth print-access-token)@REGION-git.developerconnect.dev/a/PROJECT_ID/ACCOUNT_CONNECTOR_NAME/REPO_PATH
         
         

For system connections:
         
         git clone https://REGION-git.developerconnect.dev/PROJECT_ID/CONNECTION_NAME/REPOSITORY_NAME
         

If you don't want to use a credential helper, then you can embed the cloud access token into the request instead:
         
         git clone https://unused:$(gcloud auth print-access-token)@REGION-git.developerconnect.dev/PROJECT_ID/CONNECTION_NAME/REPOSITORY_NAME
         

Replace the following:

     * REGION with the [region](https://docs.cloud.google.com/developer-connect/docs/locations) of your account connector.
     * PROJECT_ID with the ID of the project in which you created your account connector.
     * ACCOUNT_CONNECTOR_NAME with the name of your account connector.
     * CONNECTION_NAME with the name of your system connection.
     * REPOSITORY_NAME with the name of your repository.
     * REPO_PATH with the path to your repository, for example `my-org/my-repo`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
