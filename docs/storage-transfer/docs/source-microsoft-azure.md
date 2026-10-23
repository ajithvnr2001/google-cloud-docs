---
url: https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure/
title: Configure access to a source: Microsoft Azure Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:20.425352+00:00
---

# Configure access to a source: Microsoft Azure Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a source: Microsoft Azure Storage Stay organized with collections  Save and categorize content based on your preferences. 

Before transferring data from an Azure Storage bucket, you must configure access to that bucket so that Storage Transfer Service can retrieve its objects.

Storage Transfer Service supports the following Azure authentication methods:

  * [Shared access signature](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) (SAS) tokens. SAS tokens can be specified directly when creating a transfer job, or can be stored in Secret Manager.

  * [Azure Shared Keys](https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-with-shared-key) can be stored in Secret Manager and the secret passed when creating a transfer job.

  * [Federated credentials](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) are passed in a `federatedIdentityConfig` object during transfer job creation.




This document also includes information on adding Storage Transfer Service worker IP addresses to your Azure Storage firewall to allow access. See IP restrictions for details.

## Supported regions

Storage Transfer Service is able to transfer data from the following Microsoft Azure Storage regions: 

  * **Americas:** East US, East US 2, West US, West US 2, West US 3, Central US, North Central US, South Central US, West Central US, Canada Central, Canada East, Brazil South
  * **Asia-Pacific:** Australia Central, Australia East, Australia Southeast, Central India, South India, West India, Southeast Asia, East Asia, Japan East, Japan West, Korea South, Korea Central
  * **Europe, Middle East, Africa (EMEA):** France Central, Germany West Central, Norway East, Sweden Central, Switzerland North, North Europe, West Europe, UK South, UK West, Qatar Central, UAE North, South Africa North



## Option 1: Authenticate using an SAS token

Follow these steps to configure access to a Microsoft Azure Storage container using an SAS token. You can alternatively save your SAS token in Secret Manager; to do so, follow the instructions in Authenticate using an Azure Shared Key or SAS token in Secret Manager.

  1. Create or use an existing Microsoft Azure Storage user to access the storage account for your Microsoft Azure Storage Blob container.

  2. Create an SAS token at the container level. See [Grant limited access to Azure Storage resources using shared access signatures](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) for instructions.

     1. The **Allowed services** must include **Blob**.

     2. For **Allowed resource types** select both **Container** and **Object**.

     3. The **Allowed permissions** must include **Read** and **List**. If the transfer is configured to [delete objects from source](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#transferoptions), you must also include **Delete** permission.

     4. The default expiration time for SAS tokens is 8 hours. Set a reasonable expiration time that enables you to successfully complete your transfer.

     5. Do not specify any IP addresses in the **Allowed IP addresses** field. Storage Transfer Service uses various IP addresses and doesn't support IP address restriction.

     6. The **Allowed protocols** should be **HTTPS only**.

  3. Once the token is created, note the **SAS token** value that is returned. You need this value when configuring your transfer with Storage Transfer Service.


**Caution:** Basic SAS tokens can't be revoked, and the only way to invalidate a basic SAS token is to remove the storage access key of your account. We strongly recommend that you create SAS tokens from stored access policies, so that you can revoke a policy to invalidate an SAS token. For more information, see [Best practices when using SAS](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview#best-practices-when-using-sas). 

## Option 2: Authenticate using an Azure Shared Key or SAS token in Secret Manager

Secret Manager is a secure service that stores and manages sensitive data such as passwords. It uses strong encryption, role-based access control, and audit logging to protect your secrets.

Storage Transfer Service supports Secret Manager resource names that reference your securely stored Azure credentials.

To use an Azure Shared Key, you must save the key in Secret Manager. SAS tokens can be saved in Secret Manager or passed directly.

When you specify a Shared Key, Storage Transfer Service uses that key to generate a [service SAS](https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas) that is restricted in scope to the Azure container specified in the transfer job.

### Enable the API

Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com)

### Configure additional permissions

#### User permissions

The user creating the secret requires the following role:

  * Secret Manager Admin (`roles/secretmanager.admin`)



Learn how to [grant a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

#### Service agent permissions

The Storage Transfer Service [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) requires the following IAM role:

  * Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)



To grant the role to your service agent:

###  Cloud console 

  1. Follow the instructions to [retrieve your service agent email](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage#find).

  2. Go to the **IAM** page in the Google Cloud console.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  3. Click **Grant access**.

  4. In the **New principals** text box, enter the service agent email.

  5. In the **Select a role** drop-down, search for and select **Secret Manager Secret Accessor**.

  6. Click **Save**.




###  gcloud 

Use the `gcloud projects add-iam-policy-binding` command to add the IAM role to your service agent.

  1. Follow the instructions to [retrieve your service agent email](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage#find).

  2. From the command line, enter the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='serviceAccount:SERVICE_AGENT_EMAIL' \
           --role='roles/secretmanager.secretAccessor'
         




### Create a secret

Create a secret with Secret Manager:

###  Cloud console 

  1. Go to the **Secret Manager** page in the Google Cloud console.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Create secret**.

  3. Enter a name.

  4. In the **Secret value** text box, enter your credentials in one of the following formats.
         
         {
           "sas_token" : "SAS_TOKEN_VALUE"
         }
         

Or:
         
         {
           "access_key" : "ACCESS_KEY"
         }
         

  5. Click **Create secret**.

  6. Once the secret has been created, note the secret's full resource name:

     1. Select the **Overview** tab.

     2. Copy the value of **Resource name**. It uses the following format:

`projects/1234567890/secrets/SECRET_NAME`




###  gcloud 

To create a new secret using the gcloud command-line tool, pass the JSON-formatted credentials to the `gcloud secrets create` command:
    
    
    printf '{
      "sas_token" : "SAS_TOKEN_VALUE"
    }' | gcloud secrets create SECRET_NAME --data-file=-
    

Or:
    
    
    printf '{
      "access_key" : "ACCESS_KEY"
    }' | gcloud secrets create SECRET_NAME --data-file=-
    

Retrieve the secret's full resource name:
    
    
    gcloud secrets describe SECRET_NAME
    

Note the value of `name` in the response. It uses the following format:

`projects/1234567890/secrets/SECRET_NAME`

For more details about creating and managing secrets, refer to the [Secret Manager documentation](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

### Pass your secret to the job creation command

Using Secret Manager with Storage Transfer Service requires using the REST API to create a transfer job.

Pass the Secret Manager resource name as the value of the [`transferSpec.azureBlobStorageDataSource.credentialsSecret`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#azureblobstoragedata) field:
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    
    {
      "description": "Transfer with Secret Manager",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "azureBlobStorageDataSource": {
          "storageAccount": "AZURE_STORAGE_ACCOUNT_NAME",
          "container": "AZURE_CONTAINER_NAME",
          "credentialsSecret": "SECRET_RESOURCE_ID",
        },
        "gcsDataSink": {
          "bucketName": "CLOUD_STORAGE_BUCKET_NAME"
        }
      }
    }
    

See [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) for full details about creating a transfer.

## Option 3: Authenticate using federated identity

Storage Transfer Service supports Azure workload identity federation with Google Cloud. Storage Transfer Service can issue requests to Azure Storage through registered Azure applications, eliminating the need to pass credentials to Storage Transfer Service directly.

To configure federated identity, follow these instructions.

### Configure Google Cloud credentials

To allow Storage Transfer Service to create OpenID Connect (OIDC) ID tokens:

###  Service agent 

If your transfer job doesn't specify a `serviceAccount` (i.e., you are not [delegating service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions)), grant the **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) role to the service agent:

  1. Retrieve the `accountEmail` of the service agent:

     1. Go to the [`googleServiceAccounts.get` reference page](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get).
     2. Under **Request parameters** , enter your [project ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).
     3. Click **Execute**. The `accountEmail` and `subjectId` are returned.
  2. Grant the **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) role to the service agent on itself. Follow the instructions in [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#single-role).




###  User-managed service account 

If you are [delegating service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions), your Google credentials are configured when you [set up permission delegation](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions#set_up_permission_delegation). No additional steps are required.

### Configure Microsoft credentials

First, register an application and add a federated credential:

  1. Sign in to <https://portal.azure.com>.
  2. Go to the **App registrations** page.
  3. Click **New registration**.
  4. Enter a name. For example, `azure-transfer-app`.
  5. Select **Accounts in this organizational directory only**.
  6. Click **Register**. The application is created. Note the `Application (client) ID` and the `Directory (tenant) ID`. You can also retrieve these later from the application's **Overview** page.
  7. Click **Certificates & secrets** and select the **Federated credentials** tab.
  8. Click **Add credential**.
  9. Select **Other issuer** as the scenario and enter the following information:

     * Issuer: `https://accounts.google.com`
     * Subject identifier: Depending on whether you're using the default service agent, or a [user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions), either:

       * The `subjectId` of your service agent, that you retrieved in Configure Google Cloud credentials.
       * The `uniqueId` of your user-managed service account. See [Retrieve a service account's unique ID](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions#retrieve-unique-id) for details on retrieving this value.
     * A unique name for the federated credential.

     * Audience must remain as `api://AzureADTokenExchange`.

  10. Click **Add**.




Next, grant the application access to your Azure Storage container:

  1. Go to the **Storage Accounts** page in your Azure account.
  2. Select your storage account and select **Containers** from the **Data storage** section.
  3. Click the bucket to which to grant access.
  4. Click **Access Control (IAM)** from the left menu and select the **Roles** tab.
  5. Click the overflow (`...`) menu next to any role and select **Clone**.
  6. Enter a name for this custom role and select **Start from scratch**. Click **Next**.
  7. Click **Add permissions** and search for `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`.
  8. Click the **Microsoft Storage** card that appears.
  9. Select the **Data actions** radio button.
  10. Select **Read : Read Blob**.
  11. Click **Add**.
  12. If you will be deleting objects at source after transfer, click **Add permissions** again and search for `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/delete`.
  13. Click the **Microsoft Storage** card that appears, select **Data actions** , and select **Delete : Delete blob**.
  14. Click **Add**.
  15. Click **Review + create** , then **Create**. You are returned to the bucket's **Access Control (IAM)** page.
  16. Click **Add** and select **Add role assignment**.
  17. From the list of roles, select your custom role and click **Next**.
  18. Click **Select members**.
  19. In the **Select** field, enter the name of the application that you previously registered. For example, `azure-transfer-app`.
  20. Click the application tile and click **Select**.
  21. Click **Review + assign**.



### Pass your application identifiers to the job creation command

Your application's identifiers are passed to the job creation command using a `federatedIdentityConfig` object. Copy the **Application (client) ID** and the **Directory (tenant) ID** that you saved during the Configure Microsoft credentials steps into the `client_id` and `tenant_id` fields.
    
    
    "federatedIdentityConfig": {
      "client_id": "efghe9d8-4810-800b-8f964ed4057f",
      "tenant_id": "abcd1234-c8f0-4cb0-b0c5-ae4aded60078"
    }
    

An example job creation request looks like the following:
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    
    {
      "description": "Transfer with Azure Federated Identity",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "azureBlobStorageDataSource": {
          "storageAccount": "AZURE_STORAGE_ACCOUNT_NAME",
          "container": "AZURE_CONTAINER_NAME",
          "federatedIdentityConfig": {
            "client_id": "AZURE_CLIENT_ID",
            "tenant_id": "AZURE_TENANT_ID"
          }
        },
        "gcsDataSink": {
          "bucketName": "CLOUD_STORAGE_BUCKET_NAME"
        }
      }
    }
    

See [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) for full details about creating a transfer.

## IP restrictions

If you restrict access to your Azure resources using an Azure Storage firewall, you must add the IP ranges used by Storage Transfer Service workers to your list of allowed IPs.

Because these IP ranges can change, we publish the current values as a JSON file at a permanent address:

[`https://www.gstatic.com/storage-transfer-service/ipranges.json`](https://www.gstatic.com/storage-transfer-service/ipranges.json)

When a new range is added to the file, we'll wait at least 7 days before using that range for requests from Storage Transfer Service.

We recommend that you pull data from this document at least weekly to keep your security configuration up to date. For a sample Python script that fetches IP ranges from a JSON file, [see this article from the Virtual Private Cloud documentation](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults).

To add these ranges as allowed IPs, follow the instructions in the Microsoft Azure article, [Configure Azure Storage firewalls and virtual networks](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security#grant-access-from-an-internet-ip-range).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
