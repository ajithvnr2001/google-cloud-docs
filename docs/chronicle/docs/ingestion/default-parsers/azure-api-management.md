---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-api-management/
title: Collect Azure API Management logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:10.794312+00:00
---

# Collect Azure API Management logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-api-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Azure API Management logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to create an Azure Event Hub feed to ingest Azure API Management logs to Google Security Operations.

Azure API Management is a hybrid, multicloud management platform for APIs across all environments. It helps organizations publish APIs to external, partner, and internal developers to unlock the potential of their data and services. API Management provides tools for API discovery, gateway functionality, security policies, analytics, and developer engagement. The diagnostic logs capture detailed information about API gateway operations, including requests, responses, and errors.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Microsoft Azure** portal with permissions to: 
    * Create Event Hub namespaces
    * Create Event Hubs
    * Configure Diagnostic Settings for Azure API Management
    * Manage access policies
  * An existing Azure API Management service instance

**Note:** Azure Event Hub charges are based on throughput units and ingested events. Review [Azure Event Hub pricing](https://azure.microsoft.com/en-us/pricing/details/event-hubs/) before proceeding.



## Create Event Hub namespace

An Event Hub namespace is a management container for one or more Event Hubs.

  1. In the **Azure portal** , search for **Event Hubs**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Namespace name** | Enter a unique name (for example, `secops-apim-eventhub`)  
**Location** | Select the region (for example, `East US`)  
**Pricing tier** | Standard (recommended for production)  
**Throughput units** | Start with 1, enable Auto-inflate (recommended)  
  4. Click **Review + create**.

  5. Review the overview and click **Create**.

  6. Wait for the deployment to complete (1-2 minutes).

**Note:** **Throughput units** determine the namespace capacity. One throughput unit allows 1 MB/s ingress and 2 MB/s egress. Enable **Auto-inflate** to automatically scale up to a maximum number of throughput units when traffic increases.



## Create Event Hub

  1. After the namespace is deployed, go to the Event Hub namespace.
  2. In the left navigation, select **Event Hubs** under **Entities**.
  3. Click **\+ Event Hub**.
  4. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | Enter a unique name (for example, `apim-logs`)  
**Partition count** | **40** (recommended for optimal Google SecOps scaling)  
**Message retention** | 7 days (recommended minimum)  
**Capture** | Disabled (not needed for Google SecOps)  
  5. Click **Create**.

**Note:** **Partition count** of **40** is recommended for Google SecOps feeds for optimal scaling. This setting cannot be changed after creation, so set it correctly during initial setup.



## Get Event Hub connection string

Google SecOps requires a connection string to authenticate to the Event Hub.

### Option A: Namespace-level connection string (recommended)

  1. Go to the **Event Hub namespace**.
  2. In the left navigation, select **Shared access policies** under **Settings**.
  3. Click on the default policy **RootManageSharedAccessKey**.
  4. Copy the **Connection string-primary key**.
  5. Save this connection string securely.

**Important:** When using a namespace-level connection string, you must remove the `EntityPath` parameter before providing it to Google SecOps.

  * **Example:**
        
        Original: Endpoint=sb://secops-apim-eventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=abc123==;EntityPath=apim-logs
        
        Remove EntityPath: Endpoint=sb://secops-apim-eventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=abc123==
        




### Option B: Event Hub-level connection string

  1. Go to the **Event Hub** (not the namespace).
  2. In the left navigation, select **Shared access policies** under **Settings**.
  3. Click **\+ Add** to create a new policy.
  4. Provide the following configuration details: 
     * **Policy name** : Enter a descriptive name (for example, `chronicle-read`)
     * **Permissions** : Select **Listen** only (read-only access)
  5. Click **Create**.
  6. Click on the newly created policy.
  7. Copy the **Connection string-primary key**.
  8. Save this connection string securely.

**Note:** Event Hub-level connection strings already include the `EntityPath` parameter, so no modification is needed.



## Configure Azure API Management to stream to Event Hub

  1. In the **Azure portal** , search for **API Management services**.
  2. Select your API Management service instance.
  3. In the left navigation, select **Diagnostic settings** under **Monitoring**.
  4. Click **\+ Add diagnostic setting**.
  5. Provide the following configuration details: 
     * **Diagnostic setting name** : Enter a descriptive name (for example, `apim-to-secops`).
     * In the **Logs** section, select the following categories: 
       * **GatewayLogs** : API gateway request and response logs
       * **WebSocketConnectionLogs** : WebSocket connection logs (if applicable)
       * **DeveloperPortalAuditLogs** : Developer portal audit logs (if applicable)
       * **GatewayLlmLogs** : Generative AI gateway logs (if applicable)
       * **GatewayMCPLogs** : Model Context Protocol (MCP) server logs (if applicable)
     * In the **Destination details** section, select the **Stream to an event hub** checkbox.
     * **Subscription** : Select the subscription containing your Event Hub namespace.
     * **Event hub namespace** : Select the namespace you created earlier (for example, `secops-apim-eventhub`).
     * **Event hub name** : Select the Event Hub you created (for example, `apim-logs`).
     * **Event hub policy name** : Select **RootManageSharedAccessKey** or a custom policy with Send permissions.
  6. Click **Save**.

**Note:** Logs will now stream continuously to the Event Hub. You may see a short delay (1-2 minutes) before the first events appear.



## (Optional) Configure Azure Blob Storage for checkpointing

Google SecOps can use Azure Blob Storage to store Event Hub checkpoints, which track which events have been processed. This prevents duplicate ingestion if the feed is temporarily interrupted.

### Create Storage Account for checkpointing

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Use the same resource group as Event Hub  
**Storage account name** | Enter a unique name (for example, `secopsapimcheckpoint`)  
**Region** | Same region as Event Hub  
**Performance** | Standard  
**Redundancy** | LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Click **Create**.




### Create Blob Container

  1. Go to the Storage Account you just created.
  2. In the left navigation, select **Containers** under **Data storage**.
  3. Click **\+ Container**.
  4. Provide the following configuration details: 
     * **Name** : Enter `checkpoints`
     * **Public access level** : Private (no anonymous access)
  5. Click **Create**.



### Get Storage Account credentials

  1. In the Storage Account, select **Access keys** under **Security + networking**.
  2. Click **Show keys**.
  3. Copy and save: 
     * **Storage account name** : The name of your storage account
     * **Key 1** : The access key value



You will provide these values when creating the Google SecOps feed.

## (Optional) Create dedicated consumer group

By default, Event Hub provides a consumer group named `$Default`. For production environments, it is recommended to create a dedicated consumer group for Google SecOps.

  1. Go to the **Event Hub** (not the namespace).
  2. In the left navigation, select **Consumer groups** under **Entities**.
  3. Click **\+ Consumer group**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `chronicle`)
  5. Click **Create**.

**Note:** If you create a dedicated consumer group, you must specify it when creating the feed in Google SecOps. Otherwise, use the default `$Default` consumer group.



## Configure a feed in Google SecOps to ingest Azure API Management logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Azure API Management Logs`).
  5. Select **Microsoft Azure Event Hub** as the **Source type**.
  6. Select **Azure API Management** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Event hub connection string** : Enter the Event Hub connection string you captured earlier

     * **If using namespace-level connection string:**

       * Ensure you **removed the`EntityPath` parameter**
       * You must also provide the **Event hub name** in the next field
     * **If using event hub-level connection string:**

       * Use the connection string as-is (includes `EntityPath`)
       * The **Event hub name** field can be left blank
     * **Event hub name** : Enter the Event Hub name (for example, `apim-logs`)

       * **Required if** using namespace-level connection string.
       * **Optional if** using event hub-level connection string.
     * **Consumer group** (optional): Enter the consumer group name

       * Leave blank to use the default `$Default` consumer group
       * If you created a dedicated consumer group, enter its name (for example, `chronicle`)
     * **Blob storage container name** (optional): For checkpointing, enter the container name (for example, `checkpoints`)

**If providing blob storage for checkpointing:**

     * **Azure storage account name** : Enter the storage account name from checkpointing configuration
     * **Azure storage account key** : Enter the access key from checkpointing configuration

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

**Note:** After creating the feed, it may take 1-2 minutes before events start appearing in Google SecOps.



For more information about Google SecOps feeds, see [Google SecOps feed documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-api-management).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Level_label` | `additional.fields` | Merged  
`Sku_label` | `additional.fields` | Merged  
`apiId_label` | `additional.fields` | Merged  
`apiRevision_label` | `additional.fields` | Merged  
`apimSubscriptionId_label` | `additional.fields` | Merged  
`backendMethod_label` | `additional.fields` | Merged  
`backendProtocol_label` | `additional.fields` | Merged  
`backendResponseCode_label` | `additional.fields` | Merged  
`backendTime_label` | `additional.fields` | Merged  
`cache_label` | `additional.fields` | Merged  
`clientProtocol_label` | `additional.fields` | Merged  
`durationMs_label` | `additional.fields` | Merged  
`eventName_label` | `additional.fields` | Merged  
`eventid_label` | `additional.fields` | Merged  
`functionInvocationId_label` | `additional.fields` | Merged  
`functionName_label` | `additional.fields` | Merged  
`hostInstanceId_label` | `additional.fields` | Merged  
`hostVersion_label` | `additional.fields` | Merged  
`isRequestSuccess_label` | `additional.fields` | Merged  
`operationId_label` | `additional.fields` | Merged  
`productId_label` | `additional.fields` | Merged  
`properties.message` | `metadata.description` | Directly mapped  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`operationName` | `metadata.product_event_type` | Directly mapped  
`DeploymentVersion` | `metadata.product_version` | Directly mapped  
`properties.method` | `network.http.method` | Directly mapped  
`properties.responseCode` | `network.http.response_code` | Directly mapped  
`properties.responseSize` | `network.received_bytes` | Directly mapped  
`properties.requestSize` | `network.sent_bytes` | Directly mapped  
`correlationId` | `network.session_id` | Directly mapped  
`properties.clientTlsCipherSuite` | `network.tls.cipher` | Directly mapped  
`properties.clientTlsVersion` | `network.tls.version` | Directly mapped  
`callerIpAddress` | `principal.asset.ip` | Merged  
`callerIpAddress` | `principal.ip` | Merged  
`location` | `principal.location.name` | Directly mapped  
`properties.url` | `principal.url` | Directly mapped  
`properties.userId` | `principal.user.userid` | Directly mapped  
`action` | `security_result.action` | Merged  
`resultType` | `security_result.action` | Mapped: `Succeeded` → `action`  
`category` | `security_result.category_details` | Merged  
`properties.category` | `security_result.category_details` | Merged  
`level` | `security_result.severity` | Directly mapped  
`resultType` | `security_result.summary` | Directly mapped  
`properties.appName` | `target.application` | Directly mapped  
`properties.processId` | `target.process.pid` | Directly mapped  
`roleInstance_label` | `target.resource.attribute.labels` | Merged  
`resourceId` | `target.resource.product_object_id` | Directly mapped  
`properties.backendUrl` | `target.url` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `AZURE API MANAGEMENT`  
N/A | `metadata.vendor_name` | Constant: `AZURE_API_MANAGEMENT`  
N/A | `network.tls.version_protocol` | Constant: `HTTP`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-api-management-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
