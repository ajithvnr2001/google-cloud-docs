---
url: https://docs.cloud.google.com/cloud-ftp/create-external-sftp-server/
title: Create an external SFTP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:17:49.855219+00:00
---

# Create an external SFTP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/create-external-sftp-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Create an external SFTP server Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to create an external SFTP server by using Cloud FTP. An external SFTP server can be accessed over the internet. Partners who are outside of your network can use the server to securely transfer files to and from Cloud Storage.

You can restrict access to an external SFTP server based on the IP addresses of your users.

For steps to create an internal server, which can be accessed only within your Virtual Private Cloud (VPC) network, see [Create an internal SFTP server](https://docs.cloud.google.com/cloud-ftp/create-internal-sftp-server). You can't change whether a server is external or internal after the server has been created.

## Before you begin

###  Console 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud FTP API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ftp.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud FTP API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=ftp.googleapis.com)

  10. If you want to restrict access to the server based on your users' IP addresses, collect a list of CIDR blocks that are allowed to access the server.



###  gcloud 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud FTP API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable ftp.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Cloud FTP API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable ftp.googleapis.com

  16. If you want to restrict access to the server based on your users' IP addresses, collect a list of CIDR blocks that are allowed to access the server.



### Required roles

To get the permission that you need to create an SFTP server, ask your administrator to grant you the [Cloud FTP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/ftp#ftp.admin) (`roles/ftp.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `ftp.servers.create` permission, which is required to create an SFTP server. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an external server

###  Console 

  1. In the Google Cloud console, go to the **Cloud FTP** page. 

[Go to Cloud FTP](https://console.cloud.google.com/transfer/ftp-servers)

  2. Click **Create server**.

  3. On the **Server configuration** tab, enter basic details for the server:

     1. In the **Server ID** field, enter a unique ID for the server.

     2. In the **Region** list, select the [Google Cloud location](https://docs.cloud.google.com/cloud-ftp/locations) for the server.

For the fastest data transfer speeds, create the server in the same location as the Cloud Storage bucket that stores your data. If the bucket's location isn't supported by Cloud FTP, then select the nearest available location.

     3. (Optional) Enter a display name for the server.

     4. Click **Continue**.

  4. On the **Networking and security** tab, configure connectivity for the server:

     1. Select **External (Public IP)**.

     2. In the **Allowed IP ranges** field, provide a CIDR block that is allowed to access the server, and then press `Enter`. For example, `192.0.2.0/24`. You must provide at least one value, and can provide a maximum of 500 CIDR blocks. To allow connections from all IP addresses, use `0.0.0.0/0`.

  5. Click **Create**.

It takes about 10 minutes for the server to be created.




###  gcloud 

To create an external server, run the [`gcloud alpha storage ftp servers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ftp/servers/create) and provide the `--access-type=EXTERNAL` flag.

Before using any of the command data below, make the following replacements: 

  * SERVER_ID: a unique ID for the server. Must start with a lowercase letter, and end with a lowercase letter or number. Can contain lowercase letters, numbers, and hyphens. Maximum length is 30 characters.
  * LOCATION_ID: the [Google Cloud location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.

For the fastest data transfer speeds, create the server in the same location as the Cloud Storage bucket that stores your data. If the bucket's location isn't supported by Cloud FTP, then select the nearest available location.

  * CIDR_BLOCK: a CIDR block that is allowed to access the server. For example, `192.0.2.0/24`. You must provide at least one value, and can provide a maximum of 500 CIDR blocks in a comma-separated list. To allow connections from all IP addresses, use `0.0.0.0/0`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp servers create SERVER_ID --access-type=EXTERNAL \
        --location=LOCATION_ID --allowed-cidr-blocks=CIDR_BLOCK

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp servers create SERVER_ID --access-type=EXTERNAL `
        --location=LOCATION_ID --allowed-cidr-blocks=CIDR_BLOCK

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha storage ftp servers create SERVER_ID --access-type=EXTERNAL ^
        --location=LOCATION_ID --allowed-cidr-blocks=CIDR_BLOCK

It takes about 10 minutes for the server to be created.

###  REST 

To create an external server, use the [`servers.create` method](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/create) and provide an `externalConfig` access configuration.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID of the server.
  * LOCATION_ID: the [Google Cloud location](https://docs.cloud.google.com/cloud-ftp/locations) of the server, such as `us-west1`.

For the fastest data transfer speeds, create the server in the same location as the Cloud Storage bucket that stores your data. If the bucket's location isn't supported by Cloud FTP, then select the nearest available location.

  * SERVER_ID: a unique ID for the server. Must start with a lowercase letter, and end with a lowercase letter or number. Can contain lowercase letters, numbers, and hyphens. Maximum length is 30 characters.
  * CIDR_BLOCK: a CIDR block that is allowed to access the server. For example, `192.0.2.0/24`. You must provide at least one value, and can provide a maximum of 500 CIDR blocks . To allow connections from all IP addresses, use `0.0.0.0/0`.



HTTP method and URL: 
    
    
    POST https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers?serverId=SERVER_ID

Request JSON body: 
    
    
    {
      "accessType": "EXTERNAL",
      "externalConfig": {
        "allowedCidrBlocks": [
          "CIDR_BLOCK"
          ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers?serverId=SERVER_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://ftp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/servers?serverId=SERVER_ID" | Select-Object -Expand Content

The response identifies a [long-running operation](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.operations). 

It takes about 10 minutes for the server to be created.

## What's next

  * [Add users to the server](https://docs.cloud.google.com/cloud-ftp/add-sftp-users)
  * [Connect to an external server](https://docs.cloud.google.com/cloud-ftp/connect-to-external-server)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
