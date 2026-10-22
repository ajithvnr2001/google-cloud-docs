---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-keyvault-audit/
title: Collect Microsoft Azure Key Vault logging logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:11.030442+00:00
---

# Collect Microsoft Azure Key Vault logging logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-keyvault-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Azure Key Vault logging logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect the Azure Key Vault logging logs by setting up a Google Security Operations feed.

For more information, see [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `AZURE_KEYVAULT_AUDI` ingestion label.

## Before you begin

Ensure that you have the following prerequisites:

  * Azure subscription that you can sign in to
  * Azure Key Vault environment (tenant) in Azure
  * Global administrator or Azure Key Vault administrator role
  * Azure storage account to store the logs



## Configure a storage account

  1. Sign in to the **Azure** portal.
  2. In the **Azure** console, search for **Storage accounts**.
  3. Select the storage account that the logs must be pulled from, and then select **Access key**. To create a new storage account, do the following:

     1. Click **Create.**
     2. Enter a name for the new storage account.
     3. Select the subscription, resource group, region, performance, and redundancy for the account. We recommend setting the performance to _standard_ , and the redundancy to _GRS_ or _LRS_.

     4. Click **Review + create**.

     5. Review the overview of the account and click **Create.**

  4. Click **Show keys** and make a note of the shared key for the storage account.

  5. Select **Endpoints** and make a note of the **Blob service** endpoint.

For more information about creating a storage account, see the **Create an Azure storage account** section in the [Microsoft documentation](http://learn.microsoft.com/).




## Configure Azure Key Vault logging

  1. In the **Azure** portal, go to **Key vaults** and select the key vault that you want to configure for logging.
  2. In the **Monitoring** section, select **Diagnostic settings**.
  3. Select **Add diagnostic setting**. The **Diagnostics settings** window provides the settings for the diagnostic logs.
  4. In the **Diagnostic setting name** field, specify the name for diagnostic setting.
  5. In the **Category groups** section, select the **audit** checkbox.
  6. In the **Retention (days)** field, specify a log retention value that complies with your organization's policies. Google SecOps recommends a minimum of one day of log retention.

You can store the Azure Key Vault logging logs in a storage account or stream the logs to Event Hubs. Google SecOps supports log collection using a storage account.




### Archive to a storage account

  1. To store logs in storage account, in the **Diagnostics settings** window, select the **Archive to a storage account** checkbox.
  2. In the **Subscription** list, select the existing subscription.
  3. In the **Storage account** list, select the existing storage account.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Azure key vault logging feed

  1. Click the **Azure Platform** pack.
  2. Locate the **Azure Key Vault logging** log type and click **Add new feed**.
  3. Specify values for the following fields:

     * **Source Type** : **Microsoft Azure Blob Storage V2**.
     * **Azure URI** : specify the **Blob service** endpoint that you obtained previously along with one of the container names of that storage account. For example, `https://xyz.blob.core.windows.net/abc/`.
     * **Source deletion option** : specify the source deletion option.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.
     * **Key** : specify the shared key that you obtained previously.
**Caution:** To avoid **HTTP 429 (Too Many Requests)** errors and ingestion delays, don't reuse the same shared key or storage account across multiple feeds.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create feed**. 


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

For more information about Google SecOps feeds, see [Google SecOps feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). 

For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type).

## Supported Microsoft Azure Key Vault logging sample logs

  * **Azure Key Vault Audit**
        
        {
          "time": "2024-02-01T10:34:54.5732801Z",
          "category": "AuditEvent",
          "operationName": "Authentication",
          "resultType": "Success",
          "correlationId": "00000000-0000-0000-0000-000000000000",
          "callerIpAddress": "127.0.0.1",
          "identity": {},
          "properties": {
            "clientInfo": "azsdk-net-Security.KeyVault.Secrets/4.5.0 (.NET Framework 4.8.4645.0; Microsoft Windows 10.0.20348 )",
            "httpStatusCode": 401,
            "requestUri": "https://example-vault.vault.azure.net/secrets/?api-version=7.4",
            "tlsVersion": "TLS1_3"
          },
          "resourceId": "/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/EXAMPLE-RG/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/EXAMPLE-VAULT",
          "operationVersion": "7.4",
          "resultSignature": "Unauthorized",
          "durationMs": "17"
        }
        

  * **Azure Diagnostics**
        
        {
          "TenantId": "00000000-0000-0000-0000-000000000000",
          "TimeGenerated": "2025-01-07T20:00:00.0483028Z",
          "ResourceId": "/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/EXAMPLE-RG/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/EXAMPLE-VAULT",
          "Category": "AuditEvent",
          "ResourceGroup": "EXAMPLE-RG",
          "SubscriptionId": "00000000-0000-0000-0000-000000000000",
          "ResourceProvider": "MICROSOFT.KEYVAULT",
          "Resource": "EXAMPLE-VAULT",
          "ResourceType": "VAULTS",
          "OperationName": "SecretGet",
          "ResultType": "Success",
          "CorrelationId": "00000000-0000-0000-0000-000000000000",
          "ResultDescription": "",
          "requestUri_s": "https://example-vault.vault.azure.net/secrets/example-secret/?api-version=7.3",
          "DurationMs": 16,
          "CallerIPAddress": "127.0.0.1",
          "OperationVersion": "7.3",
          "ResultSignature": "OK",
          "id_s": "https://example-vault.vault.azure.net/secrets/example-secret/00000000000000000000000000000000",
          "clientInfo_s": "azsdk-net-Security.KeyVault.Secrets/4.3.0 (.NET 6.0.35; Microsoft Windows 10.0.14393)",
          "httpStatusCode_d": 200,
          "identity_claim_appid_g": "00000000-0000-0000-0000-000000000000",
          "isAccessPolicyMatch_b": true,
          "identity_claim_oid_g": "00000000-0000-0000-0000-000000000000",
          "identity_claim_appidacr_s": "2",
          "identity_claim_xms_az_nwperimid_s": "[]",
          "identity_claim_idtyp_s": "app",
          "tlsVersion_s": "TLS1_2",
          "Type": "AzureDiagnostics",
          "_ResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/example-rg/providers/microsoft.keyvault/vaults/example-vault"
        }
        

  * **Azure Resource Graph**
        
        {
          "value": [
            {
              "TenantId": "00000000-0000-0000-0000-000000000000",
              "TimeGenerated": "2024-11-02T09:12:25.0852453Z",
              "ResourceId": "/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/EXAMPLE-RG/PROVIDERS/MICROSOFT.KEYVAULT/VAULTS/EXAMPLE-VAULT",
              "Category": "AuditEvent",
              "ResourceGroup": "EXAMPLE-RG",
              "SubscriptionId": "00000000-0000-0000-0000-000000000000",
              "ResourceProvider": "MICROSOFT.KEYVAULT",
              "Resource": "EXAMPLE-VAULT",
              "ResourceType": "VAULTS",
              "OperationName": "VaultGet",
              "ResultType": "Success",
              "CorrelationId": "00000000-0000-0000-0000-000000000000",
              "ResultDescription": "",
              "requestUri_s": "https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example-rg/providers/Microsoft.KeyVault/vaults/example-vault?api-version=2023-07-01&MaskCMKEnabledProperties=true",
              "DurationMs": 30,
              "CallerIPAddress": "127.0.0.1",
              "OperationVersion": "2023-07-01",
              "ResultSignature": "OK",
              "id_s": "https://example-vault.vault.azure.net/",
              "clientInfo_s": "AzureResourceGraph.IngestionWorkerService.global/1.24.1.672",
              "httpStatusCode_d": 200,
              "identity_claim_appid_g": "00000000-0000-0000-0000-000000000000",
              "identity_claim_http_schemas_microsoft_com_identity_claims_objectidentifier_g": "00000000-0000-0000-0000-000000000000",
              "properties_sku_Family_s": "A",
              "properties_sku_Name_s": "standard",
              "properties_tenantId_g": "00000000-0000-0000-0000-000000000000",
              "properties_enabledForDeployment_b": false,
              "properties_enabledForTemplateDeployment_b": false,
              "properties_enabledForDiskEncryption_b": false,
              "properties_enableSoftDelete_b": true,
              "properties_enableRbacAuthorization_b": false,
              "properties_enablePurgeProtection_b": true,
              "Type": "AzureDiagnostics",
              "_ResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/example-rg/providers/microsoft.keyvault/vaults/example-vault"
            }
          ]
        }
        




## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-keyvault-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
