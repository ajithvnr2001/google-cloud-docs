---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad/
title: Collect Microsoft Entra ID sign-in logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:35:39.718886+00:00
---

# Collect Microsoft Entra ID sign-in logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-ad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Entra ID sign-in logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Microsoft Entra ID (formerly Azure Active Directory) sign-in logs by setting up a Google Security Operations feed. You can configure ingestion using two methods: Azure Event Hub (recommended) or the Third Party API.

**Note:** An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `AZURE_AD` ingestion label.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to Microsoft Azure portal
  * **Security Administrator** or **Global Administrator** role in Microsoft Entra ID (required for diagnostic settings)
  * For the Third Party API method, one of the following roles for granting administrator consent: 
    * **Global Administrator** : can grant consent for any permission, for any API
    * **Privileged Role Administrator** : can grant consent for any permission, for any API
    * **Cloud Application Administrator** : can grant consent for any permission for any API, except Microsoft Graph app roles (application permissions)

**Note:** For Microsoft Graph application permissions (used in the API method), you need either the **Global Administrator** or **Privileged Role Administrator** role.

## Method 1: Azure Event Hub (recommended)

This method streams Microsoft Entra ID sign-in logs through Azure Event Hub using diagnostic settings. Google SecOps ingests the logs directly from the Event Hub using the Azure Event Hub feed type.

**Note:** This method provides near-real-time log delivery compared to the Third Party API method.

### Create an Event Hub namespace

An Event Hub namespace is a management container for one or more Event Hubs.

  1. In the **Azure portal** , search for **Event Hubs**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Namespace name** | Enter a unique name (for example, `secops-entraid-signin`)  
**Location** | Select the region closest to your Microsoft Entra tenant  
**Pricing tier** | Standard (recommended for production)  
**Throughput units** | Start with 1, enable Auto-inflate (recommended)  
  4. Click **Review + create**.

  5. Review the overview and click **Create**.

  6. Wait for the deployment to complete (1-2 minutes).

**Note:** **Throughput units** determine the namespace capacity. One throughput unit allows 1 MBps ingress and 2 MBps egress. Enable **Auto-inflate** to automatically scale up when traffic increases.



### Create the Event Hub

  1. After the namespace is deployed, go to the Event Hub namespace.
  2. In the left navigation, select **Event Hubs** under **Entities**.
  3. Click **\+ Event Hub**.
  4. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | Enter a unique name (for example, `entraid-signin-logs`)  
**Partition count** | **40** (recommended for optimal Google SecOps scaling)  
**Message retention** | 7 days (recommended minimum)  
**Capture** | Disabled (not needed for Google SecOps)  
  5. Click **Create**.

**Note:** **Partition count** of **40** is recommended for Google SecOps feeds for optimal scaling. This setting cannot be changed after creation, so make sure you set it correctly during initial setup.



### Get an Event Hub connection string

Google SecOps requires a connection string to authenticate to the Event Hub.

#### Option A: Namespace-level connection string (recommended)

  1. Go to the **Event Hub namespace**.
  2. In the left navigation, select **Shared access policies** under **Settings**.
  3. Click the default policy **RootManageSharedAccessKey**.
  4. Copy the **Connection string - primary key**.
  5. Save this connection string securely.

**Important:** When using a namespace-level connection string, you must remove the `EntityPath` parameter before providing it to Google SecOps.

  * **Example:**
        
        Original: Endpoint=sb://secops-entraid-signin.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=abc123==;EntityPath=entraid-signin-logs
        
        Remove EntityPath: Endpoint=sb://secops-entraid-signin.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=abc123==
        




#### Option B: Event Hub-level connection string

  1. Go to the **Event Hub** (not the namespace).
  2. In the left navigation, select **Shared access policies** under **Settings**.
  3. Click **\+ Add** to create a new policy.
  4. Provide the following configuration details: 
     * **Policy name** : Enter a descriptive name (for example, `chronicle-read`)
     * **Permissions** : Select **Listen** only (read-only access)
  5. Click **Create**.
  6. Click the newly created policy.
  7. Copy the **Connection string - primary key**.
  8. Save this connection string securely.

**Note:** Event Hub-level connection strings already include the `EntityPath` parameter, so no modification is needed.



### Configure Microsoft Entra ID diagnostic settings

  1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a **Security Administrator**.
  2. Browse to **Entra ID > Monitoring & health > Diagnostic settings**.
  3. Click **\+ Add diagnostic setting**.
  4. Provide the following configuration details:

     * **Diagnostic setting name** : Enter a descriptive name (for example, `signin-logs-to-eventhub`).
     * In the **Logs** section, select the sign-in log categories you want to export:

       * **SignInLogs** \- Interactive user sign-ins.
       * **NonInteractiveUserSignInLogs** \- Non-interactive user sign-ins (recommended).
       * **ServicePrincipalSignInLogs** \- Service principal sign-ins (optional).
       * **ManagedIdentitySignInLogs** \- Managed identity sign-ins (optional).
       * **ADFSSignInLogs** \- AD FS sign-in logs (optional, if AD FS is in use).
       * **RiskyUsers** \- Users flagged for risk by Microsoft Entra ID Protection (optional).
       * **UserRiskEvents** \- Risky sign-in event details (optional).
**Note:** Select **NonInteractiveUserSignInLogs** , **ServicePrincipalSignInLogs** , and **ManagedIdentitySignInLogs** if you need those sign-in types. They are the categories that Method 2 cannot collect. Plan for the volume: Microsoft states that non-interactive user and service principal sign-ins can be five to ten times larger than interactive sign-ins.
     * In the **Destination details** section, select **Stream to an event hub**.

     * **Subscription** : Select the subscription containing your Event Hub namespace.

     * **Event hub namespace** : Select the namespace you created (for example, `secops-entraid-signin`).

     * **Event hub name** : Select the Event Hub you created (for example, `entraid-signin-logs`).

     * **Event hub policy name** : Select **RootManageSharedAccessKey**.

  5. Click **Save**.

**Note:** Microsoft states that it can take up to three days for logs to start appearing at the destination after a diagnostic setting is created. Data usually arrives much sooner, but don't treat an empty Event Hub on the first day as a misconfiguration. You can also select **Export Settings** from the **Audit Logs** or **Sign-ins** page to reach diagnostic settings.



### (Optional) Configure Azure Blob Storage for checkpointing

Google SecOps can use Azure Blob Storage to store Event Hub checkpoints, which track which events have been processed. This prevents duplicate ingestion if the feed is temporarily interrupted.

#### Create a Storage Account for checkpointing

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Use the same resource group as Event Hub  
**Storage account name** | Enter a unique name (for example, `secopsaadsignin`)  
**Region** | Same region as Event Hub  
**Performance** | Standard  
**Redundancy** | LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Click **Create**.




#### Create the Blob Container

  1. Go to the Storage Account you created.
  2. In the left navigation, select **Containers** under **Data storage**.
  3. Click **\+ Container**.
  4. Provide the following configuration details: 
     * **Name** : Enter `checkpoints`
     * **Public access level** : Private (no anonymous access)
  5. Click **Create**.



#### Get Storage Account credentials

  1. In the Storage Account, select **Access keys** under **Security + networking**.
  2. Click **Show keys**.
  3. Copy and save: 
     * **Storage account name** : The name of your storage account.
     * **Key 1** : The access key value.



### (Optional) Create a dedicated consumer group

By default, Event Hub provides a consumer group named `$Default`. For production environments, it is recommended to create a dedicated consumer group for Google SecOps.

  1. Go to the **Event Hub** (not the namespace).
  2. In the left navigation, select **Consumer groups** under **Entities**.
  3. Click **\+ Consumer group**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `chronicle`)
  5. Click **Create**.

**Note:** If you create a dedicated consumer group, you must specify it when creating the feed in Google SecOps. Otherwise, use the default `$Default` consumer group.



### Configure a feed in Google SecOps to ingest Microsoft Entra ID sign-in logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Entra ID Sign-In Logs - Event Hub`).
  5. Select **Microsoft Azure Event Hub** as the **Source type**.
  6. Select **Microsoft Azure AD** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Event hub connection string** : Enter the Event Hub connection string you captured earlier.

**If using a namespace-level connection string:**

       * Make sure you **removed the`EntityPath` parameter**.
       * You must also provide the **Event hub name** in the next field.

**If using an event hub-level connection string:**

       * Use the connection string as-is (includes `EntityPath`).
       * The **Event hub name** field can be left blank.

       * **Event hub name** : Enter the Event Hub name (for example, `entraid-signin-logs`).

**Required if** using namespace-level connection string. **Optional if** using event hub-level connection string.

       * **Consumer group** (optional): Enter the consumer group name.
       * Leave blank to use the default `$Default` consumer group.
       * If you created a dedicated consumer group, enter its name (for example, `chronicle`).

       * **Blob storage container name** (optional): For checkpointing, enter the container name (for example, `checkpoints`).

**If providing blob storage for checkpointing:**

       * **Azure storage account name** : Enter the storage account name from checkpointing configuration.
       * **Azure storage account key** : Enter the access key from checkpointing configuration.

       * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

       * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

**Note:** After creating the feed, it may take 1-2 minutes before events start appearing in Google SecOps.



## Method 2: Third Party API

This method uses the Microsoft Graph API to retrieve Microsoft Entra ID sign-in logs directly from your Microsoft tenant.

**Important:** This method collects interactive and successful federated sign-ins only. Non-interactive user, service principal, and managed identity sign-ins are not returned by `graph.microsoft.com/v1.0/auditLogs/signIns`, and cannot be requested from it. The `signInEventTypes` property that selects those categories exists only in the beta version of Microsoft Graph, not in v1.0. To ingest those sign-in types, use **Method 1: Azure Event Hub** or Microsoft Azure Blob Storage V2, selecting the **NonInteractiveUserSignInLogs** , **ServicePrincipalSignInLogs** , and **ManagedIdentitySignInLogs** categories in the Microsoft Entra ID diagnostic setting.**Caution:** Google SecOps requires allowlisting for log types that ingest from third-party APIs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allow-lists). In practice this applies where the data source enforces IP-based restrictions: if the feed returns a 403 error, check whether allowlisting is enabled on the data source and add the ranges. Note that the published list is the all-Google `goog.json`, not a Google SecOps egress list, and Google SecOps cannot guarantee that a feed originates from a given region. To restrict access by a narrower range, open a support ticket.

### Configure IP allowlisting

Google SecOps requires allowlisting for log types that ingest from third-party APIs, so add the Google IP ranges in your Microsoft Azure network settings or Conditional Access policies before creating the feed. This matters where the data source enforces IP-based restrictions. If the feed returns a 403 error, verify that allowlisting is enabled there. Note that the published list is the all-Google `goog.json`, not a Google SecOps egress list, and Google SecOps cannot guarantee that a feed originates from addresses in a given region. To restrict access by a narrower range, open a support ticket.

#### Get Google SecOps IP ranges

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Note the IP ranges displayed in the feed creation interface.
  4. Alternatively, retrieve IP ranges programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api).



#### Configure Conditional Access for workload identities (if required)

If your organization uses Conditional Access policies that restrict access by location:

  1. In the **Microsoft Entra admin center** , go to **Protection > Conditional Access > Named locations**.
  2. Click **\+ New location**.
  3. Provide the following configuration details: 
     * **Name** : Enter `Google SecOps IP Ranges`.
     * **Mark as trusted location** : Optional, based on your security policy.
     * **IP ranges** : Add each Google SecOps IP range in CIDR notation.
  4. Click **Create**.
  5. Go to **Conditional Access > Policies**.
  6. For any policies that apply to workload identities, configure an exclusion for the `Google SecOps IP Ranges` named location or the specific service principal.



### Configure Microsoft Entra ID API access

#### Create app registration

  1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or [Azure portal](https://portal.azure.com/).
  2. Go to **Identity > Applications > App registrations**.
  3. Click **New registration**.
  4. Provide the following configuration details:

     * **Name** : Enter a descriptive name (for example, `Google SecOps Sign-In Logs Integration`).
     * **Supported account types** : Select **Accounts in this organizational directory only (Single tenant)**.
**Note:** Single tenant is the correct choice for third-party API integrations. Google SecOps will access sign-in logs from your specific Microsoft Entra tenant only. Choose multi-tenant only if you intentionally need to access logs from multiple tenants in a managed service provider scenario.
     * **Redirect URI** : Leave blank (not required for service principal authentication).
  5. Click **Register**.

  6. After registration, copy and save the following values:

     * **Application (client) ID**
     * **Directory (tenant) ID**



#### Configure API permissions

The integration requires the following Microsoft Graph application permissions:

  1. In the app registration, go to **API permissions**.
  2. Click **Add a permission**.
  3. Select **Microsoft Graph > Application permissions**.
  4. Select the following permissions: 
     * **AuditLog.Read.All** : Required to read sign-in logs.
     * **Directory.Read.All** : Required by Microsoft Graph API for sign-in log access (known issue).
     * **SecurityEvents.Read.All** : Required by Google SecOps.
  5. Optional: to also capture the Conditional Access policies applied to each sign-in, add a Conditional Access read permission: 
     * **Policy.Read.ConditionalAccess** : Recommended (least privileged). Lets the feed populate the `appliedConditionalAccessPolicies` field on each sign-in record.
  6. Click **Add permissions**.
  7. Click **Grant admin consent for [Your Organization]**.
  8. Verify that the **Status** column shows **Granted for [Your Organization]** for every permission you added.

**Note:** If the **Grant admin consent** button is disabled, make sure you have either the **Global Administrator** or **Privileged Role Administrator** role. Cloud Application Administrator and Application Administrator roles cannot grant consent for Microsoft Graph application permissions.**Note:** **Policy.Read.ConditionalAccess** is optional. Without a Conditional Access read permission, Microsoft Graph omits the `appliedConditionalAccessPolicies` property from each sign-in record (sign-in logs still flow with **AuditLog.Read.All** alone). Grant it when you want to see which Conditional Access policies were evaluated per login and to build Conditional Access gap-detection use cases in Google Security Operations. If your organization prefers a broader scope, **Policy.Read.All** or **Policy.ReadWrite.ConditionalAccess** also satisfy the requirement.Permission | Type | Description  
---|---|---  
**AuditLog.Read.All** | Application | Read all sign-in and audit log data  
**Directory.Read.All** | Application | Read directory data (required for API access)  
**SecurityEvents.Read.All** | Application | Read security events  
**Policy.Read.ConditionalAccess** | Application | Optional. Read Conditional Access policies so `appliedConditionalAccessPolicies` is included in sign-in logs  
  
#### Create a client secret

  1. Go to **Certificates & secrets**.
  2. Click **New client secret**.
  3. Provide the following configuration details:

     * **Description** : Enter a descriptive name (for example, `Google SecOps Feed`).
     * **Expires** : Select an expiration period.
**Note:** Microsoft recommends setting an expiration value of **less than 12 months**. The maximum allowed is 24 months. For enhanced security, consider using **certificate credentials** or **federated identity credentials** instead of client secrets. See [Migrate applications from secret-based authentication](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migrate-applications-from-secrets).
  4. Click **Add**.

  5. **Important** : Copy the client secret **Value** immediately. This value is displayed only once and cannot be retrieved later.




#### Verify API access before creating feed

Before creating the Google SecOps feed, verify that the service principal can successfully authenticate and access the Microsoft Graph API.

  * **Test authentication using PowerShell**
        
        # Replace with your actual values
        $tenantId = "your-tenant-id"
        $clientId = "your-client-id"
        $clientSecret = "your-client-secret"
        
        # Token request parameters (must be lowercase)
        $tokenBody = @{
            grant_type    = "client_credentials"
            client_id     = $clientId
            client_secret = $clientSecret
            scope         = "https://graph.microsoft.com/.default"
        }
        
        # Request access token
        $tokenEndpoint = "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token"
        $tokenResponse = Invoke-RestMethod -Method Post -Uri $tokenEndpoint -Body $tokenBody -ContentType "application/x-www-form-urlencoded"
        
        if ($tokenResponse.access_token) {
            Write-Host "✓ Successfully obtained access token" -ForegroundColor Green
        
            # Test API call to sign-ins endpoint
            $apiUrl = "https://graph.microsoft.com/v1.0/auditLogs/signIns?`$top=1"
            $headers = @{
                Authorization = "Bearer $($tokenResponse.access_token)"
            }
        
            try {
                $signInResponse = Invoke-RestMethod -Method Get -Uri $apiUrl -Headers $headers
                Write-Host "✓ Successfully accessed sign-ins API" -ForegroundColor Green
                Write-Host "Sample sign-in log retrieved successfully" -ForegroundColor Green
            }
            catch {
                Write-Host "✗ Failed to access sign-ins API" -ForegroundColor Red
                Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
            }
        }
        else {
            Write-Host "✗ Failed to obtain access token" -ForegroundColor Red
        }
        

  * Expected output:
        
        ✓ Successfully obtained access token
        ✓ Successfully accessed sign-ins API
        Sample sign-in log retrieved successfully
        

  * **Test authentication using curl**
        
        # Replace with your actual values
        TENANT_ID="your-tenant-id"
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        
        # Request access token
        curl -X POST "https://login.microsoftonline.com/$TENANT_ID/oauth2/v2.0/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials" \
          -d "client_id=$CLIENT_ID" \
          -d "client_secret=$CLIENT_SECRET" \
          -d "scope=https://graph.microsoft.com/.default"
        
        # Test API access
        curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
          "https://graph.microsoft.com/v1.0/auditLogs/signIns?\$top=1"
        




### Configure a feed in Google SecOps to ingest Microsoft Entra ID sign-in logs

#### Set up the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Entra ID Sign-In Logs`).
  5. Select **Third party API** as the **Source type**.
  6. Select **Microsoft Azure AD** as the **Log type**.
  7. Click **Next**.



#### Configure feed parameters

  1. Specify values for the following input parameters:

     * **OAuth client ID** : The Application (client) ID from the app registration.
     * **OAuth client secret** : The client secret value you copied earlier.
     * **Tenant ID** : Your Microsoft tenant ID from the app registration (UUID format, for example, `0fc279f9-fe30-41be-97d3-abe1d7681418`).
     * **API Full Path** : Microsoft Graph REST API endpoint URL:
           
           graph.microsoft.com/v1.0/auditLogs/signIns
           

**Note:** Do NOT include the `https://` prefix. The feed will add the protocol automatically.
     * **API Authentication Endpoint** : Microsoft Active Directory Authentication Endpoint:
           
           login.microsoftonline.com
           

**Note:** Do NOT include the `https://` prefix or the `/oauth2/v2.0/token` path. The feed will construct the full authentication URL automatically using your Tenant ID.

**Advanced Options:**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Source Type** : Third party API (mechanism for collecting the logs into Google SecOps).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces) that the feed will be associated with.
     * **Ingestion Labels** : Labels will be added to all the events from this feed.
  2. Click **Next**.

  3. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

**Note:** After creating the feed, it may take 5-10 minutes before logs start appearing in Google SecOps.



### Regional endpoints

For Microsoft Entra ID deployments in sovereign clouds, use the appropriate regional endpoints:

Cloud Environment | API Full Path | API Authentication Endpoint  
---|---|---  
**Global** | `graph.microsoft.com/v1.0/auditLogs/signIns` | `login.microsoftonline.com`  
**US Government L4** | `graph.microsoft.us/v1.0/auditLogs/signIns` | `login.microsoftonline.us`  
**US Government L5 (DOD)** | `dod-graph.microsoft.us/v1.0/auditLogs/signIns` | `login.microsoftonline.us`  
**China (21Vianet)** | `microsoftgraph.chinacloudapi.cn/v1.0/auditLogs/signIns` | `login.chinacloudapi.cn`  
**Note:** Google SecOps documents the API hostname only as an optional override with a commercial default, and does not document support for sovereign-cloud hosts. For the Azure Blob Storage and Event Hub feed types it states that sovereign clouds are not supported. Confirm with Support before relying on a sovereign endpoint here.

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`CertSerialNumber` | `about.artifact.last_https_certificate.serial_number` | Directly mapped  
`modifiedProperty.newValue` | `about.location.city` | Directly mapped  
`modifiedProperty.newValue` | `about.location.country_or_region` | Directly mapped  
`modifiedProperty.newValue` | `about.location.state` | Directly mapped  
`modifiedProperty.newValue` | `about.user.department` | Merged  
`modifiedProperty.newValue` | `about.user.email_addresses` | Merged  
`modifiedProperty.newValue` | `about.user.first_name` | Directly mapped  
`modifiedProperty.newValue` | `about.user.last_name` | Directly mapped  
`modifiedProperty.newValue` | `about.user.phone_numbers` | Merged  
`modifiedProperty.newValue` | `about.user.product_object_id` | Directly mapped  
`modifiedProperty.newValue` | `about.user.title` | Directly mapped  
`modifiedProperty.newValue` | `about.user.user_display_name` | Directly mapped  
`modifiedProperty.newValue` | `about.user.userid` | Directly mapped  
`C_DeviceId_label` | `additional.fields` | Merged  
`C_Iat_label` | `additional.fields` | Merged  
`C_Idtyp_label` | `additional.fields` | Merged  
`C_Sid_label` | `additional.fields` | Merged  
`CorrelationId_label` | `additional.fields` | Merged  
`CrossTenantAccessType_label` | `additional.fields` | Merged  
`ImpersonationLevel_label` | `additional.fields` | Merged  
`KeyLength_label` | `additional.fields` | Merged  
`aadtenant_label` | `additional.fields` | Merged  
`additionalDetails_label` | `additional.fields` | Merged  
`additional_crossTenantAccessType` | `additional.fields` | Merged  
`additional_detail_label` | `additional.fields` | Merged  
`additional_detectedDateTime` | `additional.fields` | Merged  
`additional_detectionTimingType` | `additional.fields` | Merged  
`additional_durationMs` | `additional.fields` | Merged  
`additional_fields` | `additional.fields` | Merged  
`additional_isDeleted` | `additional.fields` | Merged  
`additional_isGuest` | `additional.fields` | Merged  
`additional_isProcessing` | `additional.fields` | Merged  
`additional_lastUpdatedDateTime` | `additional.fields` | Merged  
`additional_resultSignature` | `additional.fields` | Merged  
`additional_source` | `additional.fields` | Merged  
`additional_tokenIssuerName` | `additional.fields` | Merged  
`additional_tokenIssuerType` | `additional.fields` | Merged  
`additional_userType` | `additional.fields` | Merged  
`altitude_loc` | `additional.fields` | Merged  
`appServicePrincipalId_label` | `additional.fields` | Merged  
`atContentH_label` | `additional.fields` | Merged  
`atContentP_label` | `additional.fields` | Merged  
`auth_detail_label` | `additional.fields` | Merged  
`auth_id_label` | `additional.fields` | Merged  
`authentication` | `additional.fields` | Merged  
`authenticationDetail_label` | `additional.fields` | Merged  
`authenticationProtocol_label` | `additional.fields` | Merged  
`authentication_app_device_details_label` | `additional.fields` | Merged  
`authentication_requirement_label` | `additional.fields` | Merged  
`auto_label` | `additional.fields` | Merged  
`autonomousSystemNumber_label` | `additional.fields` | Merged  
`cert_issuer_name_label` | `additional.fields` | Merged  
`cert_thumbprint_label` | `additional.fields` | Merged  
`clientCredentialType_label` | `additional.fields` | Merged  
`client_credential_type` | `additional.fields` | Merged  
`client_credential_type_label` | `additional.fields` | Merged  
`conditionalAccessStatus_label` | `additional.fields` | Merged  
`cribl_pipe_label` | `additional.fields` | Merged  
`crossTenantAccessType_label` | `additional.fields` | Merged  
`cross_tenant_access_type_label` | `additional.fields` | Merged  
`domain_hint_present_label` | `additional.fields` | Merged  
`durationMs_label` | `additional.fields` | Merged  
`error_number_label` | `additional.fields` | Merged  
`federated_credential_id_label` | `additional.fields` | Merged  
`flaggedForReview_label` | `additional.fields` | Merged  
`flagged_for_review_label` | `additional.fields` | Merged  
`hometenant_label` | `additional.fields` | Merged  
`incomingTokenType_label` | `additional.fields` | Merged  
`incoming_token_type_label` | `additional.fields` | Merged  
`isTenantRestricted_label` | `additional.fields` | Merged  
`isThroughGlobalSecureAccess_label` | `additional.fields` | Merged  
`is_interactive_label` | `additional.fields` | Merged  
`is_tenant_restricted_label` | `additional.fields` | Merged  
`latitude_label` | `additional.fields` | Merged  
`login_hint_present_label` | `additional.fields` | Merged  
`longitude_label` | `additional.fields` | Merged  
`mfa_details_label` | `additional.fields` | Merged  
`name_list` | `additional.fields` | Merged  
`networkName_label` | `additional.fields` | Merged  
`networkType_additional_fields` | `additional.fields` | Merged  
`networkType_label` | `additional.fields` | Merged  
`network_location_label` | `additional.fields` | Merged  
`network_names_additional_fields` | `additional.fields` | Merged  
`originalRequestId_label` | `additional.fields` | Merged  
`originalTransferMethod_label` | `additional.fields` | Merged  
`original_transfer_method_label` | `additional.fields` | Merged  
`processing_time_in_milliseconds_label` | `additional.fields` | Merged  
`properties_incomingTokenType` | `additional.fields` | Merged  
`properties_isInteractive` | `additional.fields` | Merged  
`properties_location_geoCoordinates_altitude` | `additional.fields` | Merged  
`properties_processingTimeInMilliseconds` | `additional.fields` | Merged  
`properties_rngcStatus` | `additional.fields` | Merged  
`proxy_restriction_target_tenant_name_label` | `additional.fields` | Merged  
`prp_networkType_additional_fields` | `additional.fields` | Merged  
`prp_network_names_additional_fields` | `additional.fields` | Merged  
`ram_recommended_action_label` | `additional.fields` | Merged  
`ram_recommender_label` | `additional.fields` | Merged  
`record_properties_id_label` | `additional.fields` | Merged  
`resultReason_label` | `additional.fields` | Merged  
`resultType_label` | `additional.fields` | Merged  
`resultstatus_label` | `additional.fields` | Merged  
`rngcStatus_label` | `additional.fields` | Merged  
`service_principal_credential_key_id_label` | `additional.fields` | Merged  
`service_principal_credential_thumbprint_label` | `additional.fields` | Merged  
`service_principal_name_label` | `additional.fields` | Merged  
`signInActivityId_label` | `additional.fields` | Merged  
`signInSessionStatusCode_label` | `additional.fields` | Merged  
`signInSessionStatus_label` | `additional.fields` | Merged  
`signInTokenProtectionStatus_label` | `additional.fields` | Merged  
`sign_in_identifier_type_label` | `additional.fields` | Merged  
`sign_in_token_protection_status_label` | `additional.fields` | Merged  
`ssoExtensionVersion_label` | `additional.fields` | Merged  
`status_additionalDetails_label` | `additional.fields` | Merged  
`tokenIssuedAt_label` | `additional.fields` | Merged  
`tokenIssuerType_label` | `additional.fields` | Merged  
`token_issuer_name_label` | `additional.fields` | Merged  
`token_issuer_type_label` | `additional.fields` | Merged  
`token_protection_status_details_label` | `additional.fields` | Merged  
`token_protection_status_details_signInSessionStatus_label` | `additional.fields` | Merged  
`type_list` | `additional.fields` | Merged  
`uniqueTokenIdentifier_label` | `additional.fields` | Merged  
`unique_token_identifier_label` | `additional.fields` | Merged  
`userType_label` | `additional.fields` | Merged  
`user_type_label` | `additional.fields` | Merged  
`wids_label` | `additional.fields` | Merged  
`workload_label` | `additional.fields` | Merged  
`LogonType` | `extensions.auth.auth_details` | Directly mapped  
`properties.SignInBondData.ProtocolDetails.AuthenticationMethodsUsed` | `extensions.auth.auth_details` | Directly mapped  
`properties_clientAuthMethod` | `extensions.auth.auth_details` | Directly mapped  
`record_properties_clientAuthMethod` | `extensions.auth.auth_details` | Directly mapped  
`auth_mechanism` | `extensions.auth.mechanism` | Merged  
`ext_mech` | `extensions.auth.mechanism` | Merged  
`mechanism` | `extensions.auth.mechanism` | Merged  
`operationName` | `extensions.auth.type` | Mapped: `Sign-in activity` → `SSO`  
`record_operationName` | `extensions.auth.type` | Mapped: `Sign-in activity` → `AUTHTYPE_UNSPECIFIED`  
`category` | `metadata.description` | Directly mapped  
`record_category` | `metadata.description` | Directly mapped  
`CreationTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`activityDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`date` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`properties.activityDateTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSZ`  
`record_CreatedDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`record_time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`when` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`category` | `metadata.event_type` | Mapped: `(?i)AccountManagement` → `USER_CHANGE_PERMISSIONS`  
`event_type` | `metadata.event_type` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`has_resource` | `metadata.event_type` | Mapped: `true` → `USER_RESOURCE_ACCESS`  
`has_target` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`  
`has_target_user` | `metadata.event_type` | Mapped: `true` → `USER_LOGOUT`, `true` → `USER_CHANGE_PERMISSIONS`, `true` → `USER_LOGIN`  
`record_tenantId` | `metadata.product_deployment_id` | Directly mapped  
`tenantId` | `metadata.product_deployment_id` | Directly mapped  
`Operation` | `metadata.product_event_type` | Directly mapped  
`activityDisplayName` | `metadata.product_event_type` | Directly mapped  
`operationName` | `metadata.product_event_type` | Directly mapped  
`record_OperationName` | `metadata.product_event_type` | Directly mapped  
`record_operationName` | `metadata.product_event_type` | Directly mapped  
`type` | `metadata.product_event_type` | Directly mapped  
`EventRecordID` | `metadata.product_log_id` | Directly mapped  
`Id` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`properties.id` | `metadata.product_log_id` | Directly mapped  
`record_Id` | `metadata.product_log_id` | Directly mapped  
`record_correlationId` | `metadata.product_log_id` | Directly mapped  
`Version` | `metadata.product_version` | Directly mapped  
`operationVersion` | `metadata.product_version` | Directly mapped  
`record_operationVersion` | `metadata.product_version` | Directly mapped  
`properties.SignInBondData.ProtocolDetails.Protocol` | `network.application_protocol` | Directly mapped  
`properties_requestMethod` | `network.http.method` | Directly mapped  
`record_properties_requestMethod` | `network.http.method` | Directly mapped  
`browser` | `network.http.parsed_user_agent` | Directly mapped  
`deviceDetail.browser` | `network.http.parsed_user_agent` | Directly mapped  
`properties.deviceDetail.browser` | `network.http.parsed_user_agent` | Directly mapped  
`properties.userAgent` | `network.http.parsed_user_agent` | Directly mapped  
`record_UserAgent` | `network.http.parsed_user_agent` | Directly mapped  
`record_properties_userAgent` | `network.http.parsed_user_agent` | Directly mapped  
`userAgent` | `network.http.parsed_user_agent` | Directly mapped  
`user_agent` | `network.http.parsed_user_agent` | Directly mapped  
`value` | `network.http.parsed_user_agent` | Directly mapped  
`value1` | `network.http.parsed_user_agent` | Renamed/mapped  
`properties_requestUri` | `network.http.referral_url` | Directly mapped  
`record_properties_requestUri` | `network.http.referral_url` | Directly mapped  
`properties_responseStatusCode` | `network.http.response_code` | Directly mapped  
`record_properties_responseStatusCode` | `network.http.response_code` | Directly mapped  
`browser` | `network.http.user_agent` | Directly mapped  
`deviceDetail.browser` | `network.http.user_agent` | Directly mapped  
`properties.deviceDetail.browser` | `network.http.user_agent` | Directly mapped  
`properties.userAgent` | `network.http.user_agent` | Directly mapped  
`record_UserAgent` | `network.http.user_agent` | Directly mapped  
`record_properties_userAgent` | `network.http.user_agent` | Directly mapped  
`userAgent` | `network.http.user_agent` | Directly mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`value` | `network.http.user_agent` | Directly mapped  
`value1` | `network.http.user_agent` | Directly mapped  
`properties_responseSizeBytes` | `network.received_bytes` | Directly mapped  
`record_properties_responseSizeBytes` | `network.received_bytes` | Directly mapped  
`originalRequestId` | `network.session_id` | Directly mapped  
`properties.originalRequestId` | `network.session_id` | Directly mapped  
`properties.sessionId` | `network.session_id` | Directly mapped  
`record_OriginalRequestId` | `network.session_id` | Directly mapped  
`record_properties_sessionId` | `network.session_id` | Directly mapped  
`sessionId` | `network.session_id` | Directly mapped  
`value` | `network.session_id` | Directly mapped  
`loggedByService` | `observer.application` | Directly mapped  
`properties.loggedByService` | `observer.application` | Directly mapped  
`SubjectDomainName` | `principal.administrative_domain` | Directly mapped  
`domain` | `principal.administrative_domain` | Directly mapped  
`initiatedBy_app_displayName` | `principal.application` | Directly mapped  
`record_ClientAppUsed` | `principal.application` | Directly mapped  
`deviceId` | `principal.asset.asset_id` | Directly mapped  
`properties_deviceDetail_deviceId` | `principal.asset.asset_id` | Directly mapped  
`record_DeviceDetail_deviceId` | `principal.asset.asset_id` | Directly mapped  
`record_properties_C_DeviceId` | `principal.asset.asset_id` | Directly mapped  
`record_properties_deviceDetail_deviceId` | `principal.asset.asset_id` | Directly mapped  
`additional_fields` | `principal.asset.attribute.labels` | Merged  
`device_trust_type_label` | `principal.asset.attribute.labels` | Merged  
`isManaged_label` | `principal.asset.attribute.labels` | Merged  
`is_managed_label` | `principal.asset.attribute.labels` | Merged  
`trustType_label` | `principal.asset.attribute.labels` | Merged  
`deviceDetail.displayName` | `principal.asset.hostname` | Directly mapped  
`displayName` | `principal.asset.hostname` | Directly mapped  
`properties.deviceDetail.displayName` | `principal.asset.hostname` | Directly mapped  
`ActorIpAddress` | `principal.asset.ip` | Merged  
`IpAddress` | `principal.asset.ip` | Merged  
`SourceIpAddress` | `principal.asset.ip` | Merged  
`initiatedBy.user.ipAddress` | `principal.asset.ip` | Merged  
`principal_ip` | `principal.asset.ip` | Merged  
`properties.initiatedBy.user.ipAddress` | `principal.asset.ip` | Merged  
`properties_ip_address` | `principal.asset.ip` | Merged  
`record.IPAddress` | `principal.asset.ip` | Merged  
`record_callerIpAddress` | `principal.asset.ip` | Merged  
`deviceId` | `principal.asset_id` | Directly mapped  
`record_DeviceDetail_deviceId` | `principal.asset_id` | Directly mapped  
`record_properties_deviceDetail_deviceId` | `principal.asset_id` | Directly mapped  
`value` | `principal.asset_id` | Directly mapped  
`deviceDetail.displayName` | `principal.hostname` | Directly mapped  
`displayName` | `principal.hostname` | Directly mapped  
`properties.deviceDetail.displayName` | `principal.hostname` | Directly mapped  
`ActorIpAddress` | `principal.ip` | Merged  
`IpAddress` | `principal.ip` | Merged  
`SourceIpAddress` | `principal.ip` | Merged  
`initiatedBy.user.ipAddress` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`properties.initiatedBy.user.ipAddress` | `principal.ip` | Merged  
`properties_ip_address` | `principal.ip` | Merged  
`record_IPAddress` | `principal.ip` | Merged  
`record_callerIpAddress` | `principal.ip` | Merged  
`location_city` | `principal.location.city` | Directly mapped  
`record_properties_location_city` | `principal.location.city` | Directly mapped  
`location_countryOrRegion` | `principal.location.country_or_region` | Directly mapped  
`properties.tenantGeo` | `principal.location.country_or_region` | Directly mapped  
`record_properties_location_countryOrRegion` | `principal.location.country_or_region` | Directly mapped  
`location_name` | `principal.location.name` | Directly mapped  
`record_location` | `principal.location.name` | Directly mapped  
`location_geo_latitude` | `principal.location.region_coordinates.latitude` | Directly mapped  
`record_LocationDetails_geoCoordinates_latitude` | `principal.location.region_coordinates.latitude` | Directly mapped  
`record_properties_location_geoCoordinates_latitude` | `principal.location.region_coordinates.latitude` | Directly mapped  
`location_geo_longitude` | `principal.location.region_coordinates.longitude` | Directly mapped  
`record_LocationDetails_geoCoordinates_longitude` | `principal.location.region_coordinates.longitude` | Directly mapped  
`record_properties_location_geoCoordinates_longitude` | `principal.location.region_coordinates.longitude` | Directly mapped  
`location_state` | `principal.location.state` | Directly mapped  
`record_properties_location_state` | `principal.location.state` | Directly mapped  
`operatingSystem` | `principal.platform` | Mapped: `Win` → `WINDOWS`, `Mac` → `MAC`, `Lin` → `LINUX`  
`properties_deviceDetail_operatingSystem` | `principal.platform` | Mapped: `Win` → `WINDOWS`, `Mac` → `MAC`, `Lin` → `LINUX`  
`record_properties_deviceDetail_operatingSystem` | `principal.platform` | Mapped: `Win` → `WINDOWS`, `Mac` → `MAC`, `Lin` → `LINUX`  
`operatingSystem` | `principal.platform_version` | Directly mapped  
`properties_deviceDetail_operatingSystem` | `principal.platform_version` | Directly mapped  
`record_properties_deviceDetail_operatingSystem` | `principal.platform_version` | Directly mapped  
`IpPort` | `principal.port` | Directly mapped  
`CallerProcessName` | `principal.process.file.full_path` | Directly mapped  
`CallerProcessId` | `principal.process.pid` | Directly mapped  
`actor_label` | `principal.resource.attribute.labels` | Merged  
`actor_type_label` | `principal.resource.attribute.labels` | Merged  
`autonomousSystemNumber_label` | `principal.resource.attribute.labels` | Merged  
`autonomous_system_number_label` | `principal.resource.attribute.labels` | Merged  
`clientRequestId_label` | `principal.resource.attribute.labels` | Merged  
`displayName` | `principal.resource.attribute.labels` | Mapped: `(?i)(iphone.*)` → `displayName_label`  
`displayName_label` | `principal.resource.attribute.labels` | Merged  
`ip_address_from_resource_provider_label` | `principal.resource.attribute.labels` | Merged  
`properties_label` | `principal.resource.attribute.labels` | Merged  
`subject_logon_id_label` | `principal.resource.attribute.labels` | Merged  
`record_properties_resourceDisplayName` | `principal.resource.name` | Directly mapped  
`ObjectId` | `principal.resource.product_object_id` | Directly mapped  
`OrganizationId` | `principal.resource.product_object_id` | Directly mapped  
`initializedBy_app_servicePrincipalId` | `principal.resource.product_object_id` | Directly mapped  
`record_properties_UserPrincipalObjectID` | `principal.resource.product_object_id` | Directly mapped  
`userType_label` | `principal.user.attribute.labels` | Merged  
`user_key_label` | `principal.user.attribute.labels` | Merged  
`role_to_merge` | `principal.user.attribute.roles` | Merged  
`roles_to_merge` | `principal.user.attribute.roles` | Merged  
`initiatedBy.user.userPrincipalName` | `principal.user.email_addresses` | Merged  
`operationName` | `principal.user.email_addresses` | Mapped: `Add member to group` → `properties.initiatedBy.user.userPrincipalName`  
`properties.SignInBondData.DisplayDetails.AttemptedUsername` | `principal.user.email_addresses` | Merged  
`properties.initiatedBy.user.userPrincipalName` | `principal.user.email_addresses` | Merged  
`record_UserPrincipalName` | `principal.user.email_addresses` | Merged  
`mfaDetail.authDetail` | `principal.user.phone_numbers` | Merged  
`properties.mfaDetail.authDetail` | `principal.user.phone_numbers` | Merged  
`properties.appId` | `principal.user.product_object_id` | Directly mapped  
`identity` | `principal.user.user_display_name` | Directly mapped  
`initiatedBy.user.displayName` | `principal.user.user_display_name` | Directly mapped  
`properties.initiatedBy.app.displayName` | `principal.user.user_display_name` | Directly mapped  
`properties.initiatedBy.user.displayName` | `principal.user.user_display_name` | Directly mapped  
`properties.userDisplayName` | `principal.user.user_display_name` | Renamed/mapped  
`record_UserDisplayName` | `principal.user.user_display_name` | Directly mapped  
`record_properties_deviceDetail_displayName` | `principal.user.user_display_name` | Directly mapped  
`userDisplayName` | `principal.user.user_display_name` | Directly mapped  
`value` | `principal.user.user_display_name` | Directly mapped  
`SubjectUserName` | `principal.user.userid` | Directly mapped  
`UserId` | `principal.user.userid` | Directly mapped  
`first_user_id` | `principal.user.userid` | Directly mapped  
`initiatedBy.user.id` | `principal.user.userid` | Directly mapped  
`properties.initiatedBy.user.userPrincipalName` | `principal.user.userid` | Directly mapped  
`properties.userPrincipalName` | `principal.user.userid` | Directly mapped  
`record_SignInIdentifier` | `principal.user.userid` | Directly mapped  
`record_UserId` | `principal.user.userid` | Directly mapped  
`record_properties_servicePrincipalId` | `principal.user.userid` | Directly mapped  
`SubjectUserSid` | `principal.user.windows_sid` | Directly mapped  
`properties.initiatedBy.user.id` | `principal.user.windows_sid` | Directly mapped  
`auth_sec_res` | `security_result` | Merged  
`sec_res` | `security_result` | Merged  
`sr_result` | `security_result` | Merged  
`AuthenticationPackageName` | `security_result.about.resource.name` | Directly mapped  
`action` | `security_result.action` | Merged  
`errorCode` | `security_result.action` | Mapped: `0` → `action`  
`operationName` | `security_result.action` | Mapped: `Sign-in activity` → `action`, `Add member to group` → `action`  
`properties_status_errorCode` | `security_result.action` | Mapped: `0` → `action`  
`record_properties_status_errorCode` | `security_result.action` | Mapped: `0` → `action`  
`record_resultType` | `security_result.action` | Mapped: `0` → `action`  
`result` | `security_result.action` | Mapped: `success` → `action`  
`resultType` | `security_result.action` | Mapped: `0` → `action`  
`operationType` | `security_result.action_details` | Directly mapped  
`properties.result` | `security_result.action_details` | Directly mapped  
`Category` | `security_result.category` | Merged  
`operationName` | `security_result.category` | Mapped: `Sign-in activity` → `Category`  
`properties.category` | `security_result.category_details` | Merged  
`failureReason` | `security_result.description` | Directly mapped  
`operationName` | `security_result.description` | Mapped: `Add member to group` → `Group membership modified`  
`resultDescription` | `security_result.description` | Directly mapped  
`AuthenticationProtocol_label` | `security_result.detection_fields` | Merged  
`NewSd_label` | `security_result.detection_fields` | Merged  
`OldSd_label` | `security_result.detection_fields` | Merged  
`agent_agentType_label` | `security_result.detection_fields` | Merged  
`apiVersion_label` | `security_result.detection_fields` | Merged  
`associated_admin_units_label` | `security_result.detection_fields` | Merged  
`auth_label` | `security_result.detection_fields` | Merged  
`authenticationContextClassReference_detail_label` | `security_result.detection_fields` | Merged  
`authenticationContextClassReference_id_label` | `security_result.detection_fields` | Merged  
`authenticationProcessingDetails_label` | `security_result.detection_fields` | Merged  
`authenticationProtocol_label` | `security_result.detection_fields` | Merged  
`correlationId_label` | `security_result.detection_fields` | Merged  
`correlationId_label2` | `security_result.detection_fields` | Merged  
`correlationId_label3` | `security_result.detection_fields` | Merged  
`detail_label` | `security_result.detection_fields` | Merged  
`detection_ActorContextId` | `security_result.detection_fields` | Merged  
`detection_ApplicationId` | `security_result.detection_fields` | Merged  
`detection_InterSystemsId` | `security_result.detection_fields` | Merged  
`detection_IntraSystemId` | `security_result.detection_fields` | Merged  
`device_property_label` | `security_result.detection_fields` | Merged  
`error_code_label` | `security_result.detection_fields` | Merged  
`expirationRequirement_label` | `security_result.detection_fields` | Merged  
`extended_property_label` | `security_result.detection_fields` | Merged  
`logon_guid_label` | `security_result.detection_fields` | Merged  
`method_label` | `security_result.detection_fields` | Merged  
`modified_property_label` | `security_result.detection_fields` | Merged  
`name_label` | `security_result.detection_fields` | Merged  
`namespace_label` | `security_result.detection_fields` | Merged  
`network_type_label` | `security_result.detection_fields` | Merged  
`prop_risk_event_label` | `security_result.detection_fields` | Merged  
`prop_risk_event_v2_label` | `security_result.detection_fields` | Merged  
`properties.status.errorCode_label` | `security_result.detection_fields` | Merged  
`protocol_label` | `security_result.detection_fields` | Merged  
`record_type_label` | `security_result.detection_fields` | Merged  
`requestId_label` | `security_result.detection_fields` | Merged  
`requirement_provider_label` | `security_result.detection_fields` | Merged  
`riskDetail_label` | `security_result.detection_fields` | Merged  
`riskEventType_label` | `security_result.detection_fields` | Merged  
`riskEventTypes_label` | `security_result.detection_fields` | Merged  
`riskLastUpdatedDateTime_label` | `security_result.detection_fields` | Merged  
`riskLevelAggregated_label` | `security_result.detection_fields` | Merged  
`riskLevelDuringSignIn_label` | `security_result.detection_fields` | Merged  
`riskLevel_label` | `security_result.detection_fields` | Merged  
`riskState_label` | `security_result.detection_fields` | Merged  
`riskType_label` | `security_result.detection_fields` | Merged  
`risk_event_label` | `security_result.detection_fields` | Merged  
`risk_event_label_v2` | `security_result.detection_fields` | Merged  
`risk_level_aggregated_label` | `security_result.detection_fields` | Merged  
`risk_level_during_sign_in_label` | `security_result.detection_fields` | Merged  
`scopes_label` | `security_result.detection_fields` | Merged  
`signInSessionStatus_label` | `security_result.detection_fields` | Merged  
`status_label` | `security_result.detection_fields` | Merged  
`step_date_label` | `security_result.detection_fields` | Merged  
`step_detail_label` | `security_result.detection_fields` | Merged  
`step_requirement_label` | `security_result.detection_fields` | Merged  
`support_ticket_id_label` | `security_result.detection_fields` | Merged  
`target_displayName_label` | `security_result.detection_fields` | Merged  
`target_label` | `security_result.detection_fields` | Merged  
`target_type` | `security_result.detection_fields` | Mapped: `Policy` → `target_displayName_label`, `Policy` → `target_label`, `Policy` → `modifi...  
`ticket_encryption_type_label` | `security_result.detection_fields` | Merged  
`ticket_options_label` | `security_result.detection_fields` | Merged  
`transmitted_services_label` | `security_result.detection_fields` | Merged  
`operationName` | `security_result.priority` | Mapped: `Sign-in activity` → `MEDIUM_PRIORITY`  
`additional_fields` | `security_result.rule_labels` | Merged  
`isCompliant_label` | `security_result.rule_labels` | Merged  
`is_compliant_label` | `security_result.rule_labels` | Merged  
`level` | `security_result.severity` | Mapped: `"INFORMATION", "INFORMATIONAL", "0", "4"` → `INFORMATIONAL`, `"WARNING", "1", "3"` ...  
`operationName` | `security_result.severity` | Mapped: `Sign-in activity` → `ERROR`  
`record_Level` | `security_result.severity` | Mapped: `"INFORMATION", "INFORMATIONAL", "0", "4"` → `INFORMATIONAL`, `"WARNING", "1", "3"` ...  
`record_level` | `security_result.severity` | Mapped: `"INFORMATION", "INFORMATIONAL", "0", "4"` → `INFORMATIONAL`, `"WARNING", "1", "3"` ...  
`level` | `security_result.severity_details` | Directly mapped  
`record_Level` | `security_result.severity_details` | Directly mapped  
`record_level` | `security_result.severity_details` | Directly mapped  
`AzureActiveDirectoryEventType` | `security_result.summary` | Mapped: `0` → `Account Logon`, `1` → `Azure Application AuditEvent`  
`activityDisplayName` | `security_result.summary` | Directly mapped  
`errorCode` | `security_result.summary` | Mapped: `0` → `Successful login occurred`  
`operationName` | `security_result.summary` | Mapped: `Sign-in activity` → `Successful login occurred`, `Sign-in activity` → `Failed login...  
`properties.activity` | `security_result.summary` | Directly mapped  
`properties.activityDisplayName` | `security_result.summary` | Directly mapped  
`properties.result` | `security_result.summary` | Directly mapped  
`properties_status_errorCode` | `security_result.summary` | Mapped: `0` → `Successful login occurred`  
`record_properties_status_errorCode` | `security_result.summary` | Mapped: `0` → `Successful login occurred`  
`record_resultType` | `security_result.summary` | Mapped: `0` → `Successful login occurred`  
`resultType` | `security_result.summary` | Mapped: `0` → `Successful login occurred`  
`TargetDomainName` | `target.administrative_domain` | Directly mapped  
`ServiceName` | `target.application` | Directly mapped  
`properties.appDisplayName` | `target.application` | Directly mapped  
`record_AppDisplayName` | `target.application` | Directly mapped  
`record_properties_appDisplayName` | `target.application` | Directly mapped  
`record_AppId` | `target.asset.asset_id` | Directly mapped  
`modified_property_label` | `target.asset.attribute.labels` | Merged  
`target_displayName_label` | `target.asset.attribute.labels` | Merged  
`target_label` | `target.asset.attribute.labels` | Merged  
`target_type` | `target.asset.attribute.labels` | Mapped: `Device` → `target_displayName_label`, `Device` → `target_label`, `Device` → `modifi...  
`WorkstationName` | `target.asset.hostname` | Directly mapped  
`authenticationDetail.value` | `target.asset.hostname` | Directly mapped  
`ClientIP` | `target.asset.ip` | Merged  
`modifiedProperty.newValue` | `target.group.group_display_name` | Directly mapped  
`modifiedProperty.newValue` | `target.group.product_object_id` | Directly mapped  
`properties.targetResources.modifiedProperties.0.newValue` | `target.group.product_object_id` | Directly mapped  
`WorkstationName` | `target.hostname` | Directly mapped  
`authenticationDetail.value` | `target.hostname` | Directly mapped  
`ClientIP` | `target.ip` | Merged  
`ip` | `target.ip` | Merged  
`properties_regionScope` | `target.location.country_or_region` | Directly mapped  
`record_properties_UDI_RequiredFields_RegionScope` | `target.location.country_or_region` | Directly mapped  
`record_properties_location` | `target.location.name` | Directly mapped  
`ProcessName` | `target.process.file.full_path` | Directly mapped  
`LogonProcessName` | `target.process.file.names` | Merged  
`ProcessId` | `target.process.pid` | Directly mapped  
`__UDI_RequiredFields_EventTime` | `target.resource.attribute.labels` | Merged  
`__UDI_RequiredFields_TenantId` | `target.resource.attribute.labels` | Merged  
`__UDI_RequiredFields_UniqueId` | `target.resource.attribute.labels` | Merged  
`_label` | `target.resource.attribute.labels` | Merged  
`add_label` | `target.resource.attribute.labels` | Merged  
`additional_homeTenantId` | `target.resource.attribute.labels` | Merged  
`additional_resourceServicePrincipalId` | `target.resource.attribute.labels` | Merged  
`app_owner_tenant_id_label` | `target.resource.attribute.labels` | Merged  
`conditionalAccessStatus` | `target.resource.attribute.labels` | Merged  
`detection_TargetContextId` | `target.resource.attribute.labels` | Merged  
`handleId` | `target.resource.attribute.labels` | Merged  
`homeTenantId_label` | `target.resource.attribute.labels` | Merged  
`homeTenantName_label` | `target.resource.attribute.labels` | Merged  
`home_tenant_id_label` | `target.resource.attribute.labels` | Merged  
`home_tenant_name_label` | `target.resource.attribute.labels` | Merged  
`internal_workspace_label` | `target.resource.attribute.labels` | Merged  
`item_id_label` | `target.resource.attribute.labels` | Merged  
`label` | `target.resource.attribute.labels` | Merged  
`lmPackageNameLabel_label` | `target.resource.attribute.labels` | Merged  
`modified_property_label` | `target.resource.attribute.labels` | Merged  
`objectServer` | `target.resource.attribute.labels` | Merged  
`old_label` | `target.resource.attribute.labels` | Merged  
`operationId_label` | `target.resource.attribute.labels` | Merged  
`operationName` | `target.resource.attribute.labels` | Mapped: `Add member to group` → `add_label`  
`operationType_label` | `target.resource.attribute.labels` | Merged  
`properties_resourceTenantId_label` | `target.resource.attribute.labels` | Merged  
`record_properties_appId_label` | `target.resource.attribute.labels` | Merged  
`requestId_label` | `target.resource.attribute.labels` | Merged  
`resourceOwnerTenantId_label` | `target.resource.attribute.labels` | Merged  
`resource_display_name_label` | `target.resource.attribute.labels` | Merged  
`resource_group_label` | `target.resource.attribute.labels` | Merged  
`resource_id_label` | `target.resource.attribute.labels` | Merged  
`resource_identity_label` | `target.resource.attribute.labels` | Merged  
`resource_label` | `target.resource.attribute.labels` | Merged  
`resource_owner_tenant_id_label` | `target.resource.attribute.labels` | Merged  
`resource_service_principal_id_label` | `target.resource.attribute.labels` | Merged  
`resource_tenant_id_label` | `target.resource.attribute.labels` | Merged  
`resultSignature_label` | `target.resource.attribute.labels` | Merged  
`resultSignature_label1` | `target.resource.attribute.labels` | Merged  
`service_principal_id_label` | `target.resource.attribute.labels` | Merged  
`source_label` | `target.resource.attribute.labels` | Merged  
`target_displayName_label` | `target.resource.attribute.labels` | Merged  
`target_label` | `target.resource.attribute.labels` | Merged  
`target_logon_id_label` | `target.resource.attribute.labels` | Merged  
`target_type_label` | `target.resource.attribute.labels` | Merged  
`temp_resourceId` | `target.resource.attribute.labels` | Merged  
`tenant_id_label` | `target.resource.attribute.labels` | Merged  
`tokenIssuerType_label` | `target.resource.attribute.labels` | Merged  
`uniqueTokenIdentifier_label` | `target.resource.attribute.labels` | Merged  
`user_type_label` | `target.resource.attribute.labels` | Merged  
`ObjectName` | `target.resource.name` | Directly mapped  
`properties.SignInBondData.DisplayDetails.ResourceDisplayName` | `target.resource.name` | Directly mapped  
`properties.resourceDisplayName` | `target.resource.name` | Renamed/mapped  
`resourceDisplayName` | `target.resource.name` | Renamed/mapped  
`field.newValue` | `target.resource.product_object_id` | Directly mapped  
`record_resourceId` | `target.resource.product_object_id` | Directly mapped  
`resourceId` | `target.resource.product_object_id` | Directly mapped  
`ObjectType` | `target.resource.resource_subtype` | Directly mapped  
`target.type` | `target.resource.type` | Directly mapped  
`%{ServiceSid}` | `target.resource.user.windows_sid` | Merged  
`record_properties_identityProvider` | `target.url` | Directly mapped  
`value` | `target.url` | Directly mapped  
`modified_property_label` | `target.user.attribute.labels` | Merged  
`target_label` | `target.user.attribute.labels` | Merged  
`target_type` | `target.user.attribute.labels` | Mapped: `User` → `target_label`, `User` → `modified_property_label`  
`user_display_name_label` | `target.user.attribute.labels` | Merged  
`record_properties_userPrincipalName` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `record_properties_userPrincipalName`  
`target_displayName` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `target_displayName`  
`target_userPrincipalName` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `target_userPrincipalName`  
`userPrincipalName` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `userPrincipalName`  
`groupInfo` | `target.user.group_identifiers` | Merged  
`operationName` | `target.user.group_identifiers` | Mapped: `Add member to group` → `groupInfo`  
`properties.servicePrincipalId` | `target.user.product_object_id` | Directly mapped  
`properties.targetResources.0.id` | `target.user.product_object_id` | Directly mapped  
`properties.userId` | `target.user.product_object_id` | Directly mapped  
`record_properties_userId` | `target.user.product_object_id` | Directly mapped  
`userId` | `target.user.product_object_id` | Directly mapped  
`record_Identity` | `target.user.user_display_name` | Directly mapped  
`record_identity` | `target.user.user_display_name` | Directly mapped  
`targetUser` | `target.user.user_display_name` | Directly mapped  
`target_displayName` | `target.user.user_display_name` | Directly mapped  
`target_userPrincipalName` | `target.user.user_display_name` | Directly mapped  
`TargetUserName` | `target.user.userid` | Directly mapped  
`properties.alternateSignInName` | `target.user.userid` | Directly mapped  
`properties.servicePrincipalName` | `target.user.userid` | Directly mapped  
`properties.userId` | `target.user.userid` | Directly mapped  
`properties.userPrincipalName` | `target.user.userid` | Directly mapped  
`record_AlternateSignInName` | `target.user.userid` | Directly mapped  
`signInIdentifier` | `target.user.userid` | Directly mapped  
`userPrincipalName` | `target.user.userid` | Directly mapped  
`TargetSid` | `target.user.windows_sid` | Directly mapped  
`TargetUserSid` | `target.user.windows_sid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `metadata.product_name` | Constant: `Azure AD`  
N/A | `metadata.vendor_name` | Constant: `Microsoft`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `security_result.description` | Constant: `Group membership modified`  
N/A | `security_result.priority` | Constant: `MEDIUM_PRIORITY`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `security_result.summary` | Constant: `Successful login occurred`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-ad-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
