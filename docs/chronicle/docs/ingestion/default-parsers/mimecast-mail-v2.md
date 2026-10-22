---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mimecast-mail-v2/
title: Collect Mimecast Mail V2 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:08.783376+00:00
---

# Collect Mimecast Mail V2 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mimecast-mail-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Mimecast Mail V2 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Mimecast Mail V2 logs by setting up a Google Security Operations feed using the Third Party API. Mimecast Email Security Cloud Gateway is a cloud-based email security platform that provides advanced threat protection, data loss prevention, and email continuity services. The Mimecast Mail V2 log type uses Mimecast API 2.0 with OAuth 2.0 Client Credentials authentication to retrieve SIEM log data from your Mimecast tenant.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the Mimecast Administration Console
  * An administrator role in Mimecast with the **Manage Application Roles** security permission enabled, required to create and manage API 2.0 applications



## Configure Mimecast API 2.0 application

To enable Google SecOps to pull logs from Mimecast, you need to register an API 2.0 application in the Mimecast Administration Console and obtain OAuth 2.0 credentials.

**Note:** Mimecast Mail V2 uses **Mimecast API 2.0** , which is different from the legacy API 1.0. Make sure you are creating an API 2.0 application, not a legacy API application.

### Create API 2.0 application

  1. Sign in to the **Mimecast Administration Console**.
  2. Navigate to **Integrations > Integrations Hub**.
  3. If prompted, review and accept the **API Terms and Conditions**.
  4. Locate the **Mimecast API 2.0** tile and click **Configure New**.
  5. Under **Details** , provide the following configuration: 
     * **Application Name** : Enter a descriptive name (for example, `Google SecOps Integration`). This cannot be changed after saving.
     * **Products** : Select the API products that include SIEM log access (for example, **Threats, Security Events and Data for CG**). This cannot be changed after saving.
     * **Application Role** : Select or create a custom Administration Role with the minimum permissions required for log retrieval (see Required API permissions). Roles can be managed under **Account > Admin Roles**.
     * **Description** (optional): Enter a description for the application.
  6. Under **Notification Settings** , provide: 
     * **Technical Point of Contact** : Enter the name of the person or team responsible for this integration.
     * **Email** : Enter the contact email address.
  7. Click **Save**.

**Note:** For more information on managing API 2.0 applications, see [Managing API 2.0 for Cloud Gateway](https://mimecastsupport.zendesk.com/hc/en-us/articles/34000360548755-API-Integrations-Managing-API-2-0-for-Cloud-Gateway).



### Record API credentials

After clicking **Save** , a dialog displays the following credentials:

  * **Client ID** : Your OAuth 2.0 client identifier.
  * **Client Secret** : Your OAuth 2.0 client secret.

**Important:** Copy and save both values to a secure location immediately. The Client Secret will not be shown again. If you lose it, you must regenerate keys from the Integrations Hub (**Integrations > Integrations Hub > API 2.0 tile > View >** select application **> Reset Keys**).

## Required API permissions 

Create a custom Administration Role with the minimum permissions required for the integration. The role must have **read-only** access to SIEM log data and audit events.

**Note:** Follow the principle of least privilege. Only read permissions are required; write permissions are not needed for log ingestion.

## Configure a feed in Google SecOps to ingest Mimecast Mail V2 logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Mimecast Mail V2 Logs`).
  5. Select **Third Party API** as the **Source type**.
  6. Select **Mimecast Mail V2** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **OAuth client ID** : The Client ID from the API 2.0 application.
     * **OAuth client secret** : The Client Secret from the API 2.0 application.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve logs from your Mimecast tenant in chronological order.

**Note:** The Mimecast Mail V2 feed does not expose a field for specifying the API regional endpoint. The integration uses the Mimecast API 2.0 global gateway (`api.services.mimecast.com`), which automatically routes requests to the nearest Mimecast instance. Unlike the legacy Mimecast Mail (V1) feed, you do not need to manually specify a regional hostname.

## Mimecast API 2.0 gateway

Mimecast API 2.0 offers three gateway options:

Gateway | URL | Description  
---|---|---  
**Global** (default) | `api.services.mimecast.com` | Routes traffic to the nearest instance with automatic failover.  
**UK Instance** | `uk-api.services.mimecast.com` | Processes traffic exclusively through the UK instance. Use for UK data residency compliance.  
**US Instance** | `us-api.services.mimecast.com` | Processes traffic exclusively through the US instance. Use for US data residency compliance.  
**Note:** The Google SecOps Mimecast Mail V2 feed uses the global gateway URL by default. If your organization has data residency requirements that conflict with this, contact Google SecOps support.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`aCode` | additional_fields.aCode | Value taken from `aCode`.  
`Att_AV` | additional_fields.Att_AV | Value taken from `Att_AV`.  
`Att_Det` | additional_fields.Att_Det | Value taken from `Att_Det`.  
`Att_Enc` | additional_fields.Att_Enc | Value taken from `Att_Enc`.  
`Att_Key` | additional_fields.Att_Key | Value taken from `Att_Key`.  
`Att_Mod` | additional_fields.Att_Mod | Value taken from `Att_Mod`.  
`Att_Orig` | additional_fields.Att_Orig | Value taken from `Att_Orig`.  
`Att_Rem` | additional_fields.Att_Rem | Value taken from `Att_Rem`.  
`Att_State` | additional_fields.Att_State | Value taken from `Att_State`.  
`Att_Type` | additional_fields.Att_Type | Value taken from `Att_Type`.  
`CKS` | additional_fields.CKS | Value taken from `CKS`.  
`Date` | additional_fields.Date | Value taken from `Date`.  
`Delivered` | additional_fields.Delivered | Value taken from `Delivered`.  
`dlp` | additional_fields.dlp | Value taken from `dlp`.  
`Dmarc` | additional_fields.Dmarc | Value taken from `Dmarc`.  
`Enc` | additional_fields.Enc | Value taken from `Enc`.  
`Error_Code` | additional_fields.Error_Code | Value taken from `Error_Code`.  
`Error_Type` | additional_fields.Error_Type | Value taken from `Error_Type`.  
`Grey` | additional_fields.Grey | Value taken from `Grey`.  
`header_id` | additional_fields.header_id | Value taken from `header_id`.  
`Hold_For` | additional_fields.Hold_For | Value taken from `Hold_For`.  
`Hold_Reason` | additional_fields.Hold_Reason | Value taken from `Hold_Reason`.  
`Latency` | additional_fields.Latency | Value taken from `Latency`.  
`Malware_Hash` | additional_fields.Malware_Hash | Value taken from `Malware_Hash`.  
`Malware_Name` | additional_fields.Malware_Name | Value taken from `Malware_Name`.  
`Msg_Key` | additional_fields.Msg_Key | Value taken from `Msg_Key`.  
`MsgSize` | additional_fields.MsgSize | Value taken from `MsgSize`.  
`Policy` | additional_fields.Policy | Value taken from `Policy`.  
`Processing_Time` | additional_fields.Processing_Time | Value taken from `Processing_Time`.  
`Queue_ID` | additional_fields.Queue_ID | Value taken from `Queue_ID`.  
`rcpt_type` | additional_fields.rcpt_type | Value taken from `rcpt_type`.  
`Receipt` | additional_fields.Receipt | Value taken from `Receipt`.  
`sCode` | additional_fields.sCode | Value taken from `sCode`.  
`Sent` | additional_fields.Sent | Value taken from `Sent`.  
`Snt` | additional_fields.Snt | Value taken from `Snt`.  
`spamLimit` | additional_fields.spamLimit | Value taken from `spamLimit`.  
`spamScore` | additional_fields.spamScore | Value taken from `spamScore`.  
`SpamRef` | additional_fields.SpamRef | Value taken from `SpamRef`.  
`Tarpit` | additional_fields.Tarpit | Value taken from `Tarpit`.  
`Time` | additional_fields.Time | Value taken from `Time`.  
`datetime` | metadata.event_timestamp | Value taken from `datetime`. The original `datetime` field is also parsed to set the event's primary `@timestamp`.  
| metadata.event_type | Set to `NETWORK_EMAIL`.  
| metadata.product_event_type | Set to `processed_email`.  
`dir` | network.direction | Derived from `dir`: `In` -> INBOUND; `Out` -> OUTBOUND; `Int` -> UNKNOWN.  
`sender`, `route`, `hdr_from` | network.email.from | Value taken from `sender`, then `route`. If still empty, value is taken from `hdr_from`.  
`MsgID` | network.email.message_id | Value taken from `MsgID`.  
`subject` | network.email.subject | Value taken from `subject`.  
`rcpt` | network.email.to | Value taken from `rcpt` and split by ',' into an array.  
`IP` | principal.ip | Value taken from `IP` and split by ',' into an array.  
`hdr_from` | principal.user.email_addresses | Value taken from `hdr_from` and split by ',' into an array.  
`act` | security_result.action | Derived from `act`: `Rej`, `T`, `Hld`, `Bnc` -> BLOCK; `U`, `A` -> ALLOW; else UNKNOWN.  
`Att_Hash` | target.file.md5 | Value taken from `Att_Hash`.  
`Att_Name` | target.file.name | Value taken from `Att_Name`.  
`Att_Size` | target.file.size | Value taken from `Att_Size` and converted to integer.  
`URL` | target.url | Value taken from `URL`.  
`rcpt_to` | target.user.email_addresses | Value taken from `rcpt_to` and split by ',' into an array.  
| metadata.product_name | Set to `Mail V2`.  
| metadata.vendor_name | Set to `Mimecast`.  
`new_fileName` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`new_fileMime` | `event.idm.read_only_udm.target.file.mime_type` | Mapped from changelog  
`new_sha256` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`new_md5` | `event.idm.read_only_udm.target.file.md5` | Mapped from changelog  
`new_sha1` | `event.idm.read_only_udm.target.file.sha1` | Mapped from changelog  
`data.accountId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`route` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`new_delivered` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`new_deliveryErrors` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`new_urlCategory` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`new_asset_category` | `event.idm.read_only_udm.principal.asset.category` | Mapped from changelog  
`new_blockReason` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`new_route` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-mail-v2-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
