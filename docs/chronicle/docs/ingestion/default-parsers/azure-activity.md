---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-activity/
title: Collect Microsoft Azure Activity and Entra ID logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:14.510960+00:00
---

# Collect Microsoft Azure Activity and Entra ID logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-activity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Azure Activity and Entra ID logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Microsoft Azure Activity and Entra ID logs by setting up Google Security Operations feeds. You can configure ingestion using two methods:

  * **Method 1: Microsoft Azure Event Hub (recommended)** : Azure diagnostic settings stream Activity and Entra ID logs to an Azure Event Hub namespace, from where Google SecOps ingests them in near real time. This is the preferred method.
  * **Method 2: Microsoft Azure Blob Storage V2** : Azure diagnostic settings archive logs to an Azure Storage Account, and Google SecOps polls the blob containers on a schedule.



Microsoft Azure Activity logs provide insight into subscription-level operations performed on Azure resources, such as creating storage accounts, deleting event hubs, or modifying virtual machines. Microsoft Entra ID (formerly Azure Active Directory) logs capture identity and access management events, including user sign-ins, audit logs, provisioning activities, and security risk detections.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **Microsoft Azure** portal with permissions to: 
    * Create Event Hub namespaces (Method 1) or Storage Accounts (Method 2)
    * Configure diagnostic settings for Azure Monitor and Entra ID
    * Manage Event Hub access policies (Method 1) or storage access keys (Method 2)
  * Security Administrator role or higher in Entra ID (for Entra ID diagnostic settings)

**Note:** You can create up to 10 Azure Event Hub feeds per Google SecOps instance, including both active and inactive feeds. Grouping log categories by Google SecOps log type, as described in Method 1, keeps the number of Event Hubs and feeds within this limit. For details on the canonical Azure Event Hub feed setup, see [Create an Azure Event Hub feed](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed).

## Method 1: Microsoft Azure Event Hub (recommended)

With this method, Azure diagnostic settings stream Microsoft Azure Activity and Entra ID logs to an Azure Event Hub namespace, and Google SecOps ingests them directly from the Event Hub in near real time.

Each Google SecOps feed maps a single Event Hub to a single log type. Create one Event Hub per Google SecOps log type and route the matching Azure log categories to it:

Event Hub | Azure log categories | Google SecOps log type  
---|---|---  
`azure-activity` | Azure Activity log | Microsoft Azure Activity  
`entra-id` | SignInLogs, NonInteractiveUserSignInLogs, ServicePrincipalSignInLogs, ManagedIdentitySignInLogs, ProvisioningLogs, RiskyUsers, UserRiskEvents | Azure AD  
`entra-id-audit` | AuditLogs | Azure AD Directory Audit  
`entra-id-graph` | MicrosoftGraphActivityLogs | Microsoft Graph Activity Logs  
  
### Create an Event Hub namespace

An Event Hub namespace is a management container for one or more Event Hubs.

  1. In the **Azure portal** , search for **Event Hubs**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Namespace name** | Enter a unique name (for example, `secops-azure-logs`)  
**Location** | Select the same region as your Google SecOps instance (deploying in a different region reduces ingestion throughput)  
**Pricing tier** | Standard or higher (Basic supports only one Event Hub per namespace)  
**Throughput Units** | Start with 1 and enable **Auto-inflate**  
  4. Click **Review + create** , and then click **Create**.

  5. Wait for the deployment to complete.

**Note:** The Event Hub namespace should be in the same region as your Google SecOps instance; deploying in a different region can reduce ingestion throughput. One throughput unit (TU) supports up to 1 MB per second of ingress. Enable **Auto-inflate** so the namespace scales up as log volume grows and events are not lost before they reach Google SecOps.



### Create Event Hubs

Create one Event Hub for each Google SecOps log type listed in the previous table.

  1. After the namespace is deployed, go to the **Event Hub namespace**.
  2. In the left navigation, select **Event Hubs** under **Entities**.
  3. Click **\+ Event Hub** and create an Event Hub with the following settings:

Setting | Value  
---|---  
**Name** | `azure-activity`  
**Partition count** | **40** (recommended for optimal Google SecOps scaling; cannot be changed after creation in the Standard and Basic tiers)  
**Message retention** | 7 days minimum (set the longest retention you can afford so logs are not deleted before ingestion resumes after a quota throttle)  
**Capture** | Disabled (not needed for direct Event Hub ingestion)  
  4. Click **Review + create** , and then click **Create**.

  5. Repeat to create the `entra-id`, `entra-id-audit`, and `entra-id-graph` Event Hubs.

**Note:** Always stream Azure logs to an existing Event Hub. If you leave the **Event hub name** blank in a diagnostic setting, Azure creates a separate Event Hub for each log category (named `insights-logs-<category>`), which can exhaust the namespace Event Hub quota and your Google SecOps feed quota.



### Get an Event Hub connection string

Google SecOps requires a connection string to authenticate to the Event Hub. Use a namespace-level connection string so that one credential works for all of the Event Hubs you created.

  1. Go to the **Event Hub namespace**.
  2. In the left navigation, select **Shared access policies** under **Settings**.
  3. Click the **RootManageSharedAccessKey** policy, or click **\+ Add** to create a dedicated policy with the **Listen** permission.
  4. Copy the **Connection string-primary key**.
  5. Save this connection string securely.

**Note:** A namespace-level connection string does not include the `EntityPath` parameter. You specify the target Event Hub separately in the **Event Hub Name** field of each feed, so the same connection string is reused across all feeds.



### Configure Azure Activity logs diagnostic settings (Event Hub)

To stream Azure Activity logs to the `azure-activity` Event Hub:

  1. In the **Azure portal** , search for **Monitor**.
  2. Click **Activity log** in the left navigation.
  3. Click **Export Activity Logs** at the top of the window.
  4. Click **Add diagnostic setting**.
  5. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `activity-logs-to-eventhub`).
     * In the **Logs** section, select the following categories: 
       * **Administrative**
       * **Security**
       * **Service Health**
       * **Alert**
       * **Recommendation**
       * **Policy**
       * **Autoscale**
       * **Resource Health**
     * In the **Destination details** section, select the **Stream to an event hub** checkbox.
     * **Subscription** : Select the subscription containing your Event Hub namespace.
     * **Event hub namespace** : Select the namespace you created earlier (for example, `secops-azure-logs`).
     * **Event hub name** : Select `azure-activity`.
     * **Event hub policy name** : Select the shared access policy (for example, `RootManageSharedAccessKey`).
  6. Click **Save**.



### Configure Entra ID diagnostic settings (Event Hub)

Each diagnostic setting streams to a single Event Hub, so create one diagnostic setting per Entra ID Event Hub and group the categories by Google SecOps log type.

  1. In the **Azure portal** , search for **Microsoft Entra ID** or **Azure Active Directory**.
  2. In the left navigation, go to **Monitoring & health > Diagnostic settings**.
  3. Click **Add diagnostic setting** and create the following settings, one at a time:

**Diagnostic setting for the`entra-id` Event Hub (log type Azure AD):**

     * **Diagnostic setting name** : `entraid-azuread-to-eventhub`
     * In the **Logs** section, select the following categories: 
       * **SignInLogs**
       * **NonInteractiveUserSignInLogs**
       * **ServicePrincipalSignInLogs**
       * **ManagedIdentitySignInLogs**
       * **ProvisioningLogs**
       * **RiskyUsers**
       * **UserRiskEvents**
     * In the **Destination details** section, select **Stream to an event hub** , your Event Hub namespace, and the `entra-id` Event Hub with its shared access policy.

**Diagnostic setting for the`entra-id-audit` Event Hub (log type Azure AD Directory Audit):**

     * **Diagnostic setting name** : `entraid-audit-to-eventhub`
     * In the **Logs** section, select **AuditLogs**.
     * In the **Destination details** section, select **Stream to an event hub** , your Event Hub namespace, and the `entra-id-audit` Event Hub.

**Diagnostic setting for the`entra-id-graph` Event Hub (log type Microsoft Graph Activity Logs):**

     * **Diagnostic setting name** : `entraid-graph-to-eventhub`
     * In the **Logs** section, select **MicrosoftGraphActivityLogs**.
     * In the **Destination details** section, select **Stream to an event hub** , your Event Hub namespace, and the `entra-id-graph` Event Hub.
  4. After configuring each setting, click **Save**.


**Note:** Configure only the categories you want to ingest. If you do not need a category, omit it from the diagnostic setting and skip the corresponding feed. It may take several minutes for logs to begin streaming to the Event Hubs.

### (Optional) Create dedicated consumer groups

By default, each Event Hub provides a consumer group named `$Default`. For production environments, it is recommended to create a dedicated consumer group for Google SecOps on each Event Hub.

  1. Go to an **Event Hub** (not the namespace).
  2. In the left navigation, select **Consumer groups**.
  3. Click **\+ Consumer group** , enter a name (for example, `chronicle`), and click **Create**.
  4. Repeat for each Event Hub.

**Caution:** Do not create additional subscribers on the Google SecOps consumer group, and do not retrieve data programmatically through the Azure portal **Data Explorer** tab while it is in use. Either action may cause data loss because Event Hub consumer-group offsets advance as data is read.



### Configure feeds in Google SecOps (Event Hub)

Create one feed for each Event Hub. All feeds use the same namespace-level connection string and differ only by **Event Hub Name** and **Log type** :

Feed name | Event Hub Name | Google SecOps log type  
---|---|---  
`Microsoft Azure Activity Logs` | `azure-activity` | Microsoft Azure Activity  
`Azure AD Logs` | `entra-id` | Azure AD  
`Azure AD Directory Audit Logs` | `entra-id-audit` | Azure AD Directory Audit  
`Microsoft Graph Activity Logs` | `entra-id-graph` | Microsoft Graph Activity Logs  
  
For each row in the table:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter the feed name (for example, `Azure Activity Logs`).
  5. Select **Microsoft Azure Event Hub** as the **Source type**.
  6. Select the corresponding **Log type** (for example, `Microsoft Azure Activity`).
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Event Hub Name** : Enter the Event Hub name from the table (for example, `azure-activity`).
     * **Event Hub Consumer Group** : Enter `$Default`, or the dedicated consumer group you created (for example, `chronicle`).
     * **Event Hub Connection String** : Enter the namespace-level connection string you captured earlier.
     * **Azure Storage Connection String** (optional): Legacy field for Event Hub checkpointing storage; leave blank.
     * **Azure Storage Container Name** (optional): Legacy field for Event Hub checkpointing storage; leave blank.
     * **Azure SAS Token** (optional): Alternative authentication to the Event Hub when your security policy forbids sharing the **Event Hub Connection String** ; leave blank when you provide the connection string above.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
**Note:** Google SecOps manages its own checkpointing for Azure Event Hub feeds. Only the **Event Hub Connection String** (or, in its place, **Azure SAS Token**) is required; the **Azure Storage Connection String** and **Azure Storage Container Name** fields are legacy checkpointing fields that do not affect ingestion and should be left blank in standard deployments.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

**Note:** Create only the feeds for the log categories you enabled in the diagnostic settings.



## Method 2: Microsoft Azure Blob Storage V2

With this method, Azure diagnostic settings archive Azure Activity and Entra ID logs to an Azure Storage Account, and Google SecOps polls the blob containers on a schedule. Use this method when near-real-time ingestion is not required or when your environment standardizes on Blob Storage.

### Configure an Azure Storage account

#### Create the Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `secops-azure-logs`)  
**Region** | Select the region (for example, `East US`)  
**Performance** | Standard (recommended)  
**Redundancy** | GRS (Geo-redundant storage) or LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Review the overview of the account and click **Create**.

  6. Wait for the deployment to complete.




#### Get Storage Account credentials

  1. Go to the **Storage Account** you just created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following for later use: 
     * **Storage account name** : Your storage account name (for example, `secops-azure-logs`)
     * **Key 1** or **Key 2** : The shared access key (a 512-bit random string in base-64 encoding)



#### Get the Blob Service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://secops-azure-logs.blob.core.windows.net/`



### Configure Azure Activity log diagnostic settings

To export Azure Activity logs to the storage account:

  1. In the **Azure portal** , search for **Monitor**.
  2. Click **Activity log** in the left navigation.
  3. Click **Export Activity Logs** at the top of the window.
  4. Click **Add diagnostic setting**.
  5. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `activity-logs-to-secops`).
     * In the **Logs** section, select the following categories: 
       * **Administrative**
       * **Security**
       * **Service Health**
       * **Alert**
       * **Recommendation**
       * **Policy**
       * **Autoscale**
       * **Resource Health**
     * In the **Destination details** section, select the **Archive to a storage account** checkbox.
     * **Subscription** : Select the subscription containing your storage account.
     * **Storage account** : Select the storage account you created earlier (for example, `secops-azure-logs`).
  6. Click **Save**.

**Note:** After configuration, logs will be automatically exported to a container named `insights-activity-logs`. It may take up to 15 minutes for the first logs to appear.

### Configure Entra ID diagnostic settings

To export Entra ID logs to the storage account:

  1. In the **Azure portal** , search for **Microsoft Entra ID** or **Azure Active Directory**.
  2. In the left navigation, go to **Monitoring & health > Diagnostic settings**.
  3. Click **Add diagnostic setting**.
  4. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `entraid-logs-to-secops`).
     * In the **Logs** section, select the log categories you want to export: 
       * **SignInLogs** : Interactive user sign-ins
       * **NonInteractiveUserSignInLogs** : Non-interactive user sign-ins (service principals, managed identities acting on behalf of users)
       * **ServicePrincipalSignInLogs** : Service principal and application sign-ins
       * **ManagedIdentitySignInLogs** : Managed identity sign-ins
       * **AuditLogs** : Audit trail of all changes in Entra ID (user creation, role assignments, etc.)
       * **ProvisioningLogs** : User and group provisioning events
       * **RiskyUsers** : Users flagged by Identity Protection
       * **UserRiskEvents** : Risk detections for user accounts
       * **MicrosoftGraphActivityLogs** : Microsoft Graph API activity logs
     * In the **Destination details** section, select the **Archive to a storage account** checkbox.
     * **Subscription** : Select the subscription containing your storage account.
     * **Storage account** : Select the storage account you created earlier (for example, `secops-azure-logs`).
  5. Click **Save**.

**Note:** It may take up to 72 hours for Entra ID logs to start appearing in the storage account. Each selected log category will create a separate container with the naming pattern `insights-logs-{category-name}`.



### Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Azure Blob Storage. You must grant this service account access to your storage account.

#### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a temporary name.
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select any log type (you can change this later).
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address. You will use it in the next step.

  10. Click **Cancel** to exit the feed creation (you will create the actual feeds later).


**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.

### Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Blob Data Reader** role on your storage account.

  1. In the **Azure portal** , go to **Storage accounts**.
  2. Click on your storage account name (for example, `secops-azure-logs`).
  3. Go to the **Access Control (IAM)** tab.
  4. Click **\+ Add > Add role assignment**.
  5. In the **Role** tab, search for and select **Storage Blob Data Reader**.
  6. Click **Next**.
  7. In the **Members** tab, click **\+ Select members**.
  8. In the search box, paste the Google SecOps service account email.
  9. Select the service account from the results.
  10. Click **Select**.
  11. Click **Review + assign**.
  12. Review the assignment and click **Review + assign** again.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Blob Data Contributor** role instead of Storage Blob Data Reader.



### Configure feeds in Google SecOps

You must create a separate feed for each log type and container. The following table shows the mapping between Azure containers and Google SecOps log types:

Container Name | Chronicle Log Type | Data Source  
---|---|---  
`insights-activity-logs` | Microsoft Azure Activity | Azure Activity Logs  
`insights-logs-signinlogs` | Azure AD | Entra ID Interactive Sign-ins  
`insights-logs-noninteractiveusersigninlogs` | Azure AD | Entra ID Non-interactive Sign-ins  
`insights-logs-serviceprincipalsigninlogs` | Azure AD | Entra ID Service Principal Sign-ins  
`insights-logs-managedidentitysigninlogs` | Azure AD | Entra ID Managed Identity Sign-ins  
`insights-logs-auditlogs` | Azure AD Directory Audit | Entra ID Audit Logs  
`insights-logs-provisioninglogs` | Azure AD | Entra ID Provisioning Logs  
`insights-logs-riskyusers` | Azure AD | Entra ID Risky Users  
`insights-logs-userriskevents` | Azure AD | Entra ID User Risk Events  
`insights-logs-microsoftgraphactivitylogs` | Microsoft Graph Activity Logs | Microsoft Graph Activity  
  
#### Create a feed for Microsoft Azure Activity Logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter `Microsoft Azure Activity Logs`.
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft Azure Activity** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
           
           https://secops-azure-logs.blob.core.windows.net/insights-activity-logs/
           

Replace `secops-azure-logs` with your Azure storage account name.

**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted the **Storage Blob Data Contributor** role to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * From the authentication drop-down (defaults to **Access/Shared key**), select the method you want to use and provide the corresponding credential:

       * **Access/Shared key** : In the **Key** field, paste a storage account access key (**Key 1** or **Key 2**) captured earlier.
       * **SAS token** : In the **Token** field, paste a shared access signature (SAS) token issued for the container.
       * **Azure V2 Workload Identity Federation** : Enter the Microsoft Entra application **Client ID** and **Tenant ID**. Copy the read-only **Subject ID** that the feed displays and grant the matching identity access to the storage account on the Azure side.
**Note:** The **Chronicle service account** shown on the right side of the feed is read-only. When you use **Azure V2 Workload Identity Federation** , configure your Microsoft Entra federated credential to trust this service account.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




#### Create feeds for Entra ID logs

Repeat the following steps for each Entra ID log type you configured in the diagnostic settings:

**For Interactive Sign-in Logs:**

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter `Azure AD Interactive Sign-in Logs`.
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Azure AD** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** :
           
           https://secops-azure-logs.blob.core.windows.net/insights-logs-signinlogs/
           

**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select according to your preference.
     * **Maximum File Age** : 180 days (default).
     * From the authentication dropdown (defaults to **Access/Shared key**), select the method you want to use and provide the corresponding credential:

       * **Access/Shared key** : In the **Key** field, paste a storage account access key (**Key 1** or **Key 2**) captured earlier.
       * **SAS token** : In the **Token** field, paste a shared access signature (SAS) token issued for the container.
       * **Azure V2 Workload Identity Federation** : Enter the Microsoft Entra application **Client ID** and **Tenant ID**. Copy the read-only **Subject ID** that the feed displays and grant the matching identity access to the storage account on the Azure side.
**Note:** The **Chronicle service account** shown on the right side of the feed is read-only. When you use **Azure V2 Workload Identity Federation** , configure your Microsoft Entra federated credential to trust this service account.
     * **Asset namespace** : The asset namespace.

     * **Ingestion labels** : The label to be applied.

  9. Click **Next** and then **Submit**.




**For Non-interactive Sign-in Logs:**

Create another feed with the following settings:

  * **Feed name** : `Azure AD Non-interactive Sign-in Logs`
  * **Log type** : `Azure AD`
  * **Azure URI** : `https://secops-azure-logs.blob.core.windows.net/insights-logs-noninteractiveusersigninlogs/`



**For Service Principal Sign-in Logs:**

Create another feed with the following settings:

  * **Feed name** : `Azure AD Service Principal Sign-in Logs`
  * **Log type** : `Azure AD`
  * **Azure URI** : `https://secops-azure-logs.blob.core.windows.net/insights-logs-serviceprincipalsigninlogs/`



**For Managed Identity Sign-in Logs:**

Create another feed with the following settings:

  * **Feed name** : `Azure AD Managed Identity Sign-in Logs`
  * **Log type** : `Azure AD`
  * **Azure URI** : `https://secops-azure-logs.blob.core.windows.net/insights-logs-managedidentitysigninlogs/`



**For Audit Logs:**

Create another feed with the following settings:

  * **Feed name** : `Azure AD Audit Logs`
  * **Log type** : `Azure AD Directory Audit`
  * **Azure URI** : `https://secops-azure-logs.blob.core.windows.net/insights-logs-auditlogs/`



**For Provisioning Logs:**

Create another feed with the following settings:

  * **Feed name** : `Azure AD Provisioning Logs`
  * **Log type** : `Azure AD`
  * **Azure URI** : `https://secops-azure-logs.blob.core.windows.net/insights-logs-provisioninglogs/`



**For Risky Users:**

Create another feed with the following settings:

  * **Feed name** : `Azure AD Risky Users`
  * **Log type** : `Azure AD`
  * **Azure URI** : `https://secops-azure-logs.blob.core.windows.net/insights-logs-riskyusers/`



**For User Risk Events:**

Create another feed with the following settings:

  * **Feed name** : `Azure AD User Risk Events`
  * **Log type** : `Azure AD`
  * **Azure URI** : `https://secops-azure-logs.blob.core.windows.net/insights-logs-userriskevents/`



**For Microsoft Graph Activity Logs:**

Create another feed with the following settings:

  * **Feed name** : `Microsoft Graph Activity Logs`
  * **Log type** : `Microsoft Graph Activity Logs`
  * **Azure URI** : `https://secops-azure-logs.blob.core.windows.net/insights-logs-microsoftgraphactivitylogs/`

**Note:** Only create feeds for the log categories you selected in the Entra ID diagnostic settings. If you did not enable a specific log category, skip creating the corresponding feed.



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-activity-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
