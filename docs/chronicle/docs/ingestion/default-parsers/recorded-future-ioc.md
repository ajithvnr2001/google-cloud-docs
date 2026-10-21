---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/recorded-future-ioc/
title: Collect Recorded Future IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:00:13.167373+00:00
---

# Collect Recorded Future IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/recorded-future-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Recorded Future IOC logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Recorded Future IOC logs by setting up a Google Security Operations feed using the Third Party API.

Recorded Future, a Mastercard company, is a threat intelligence platform that delivers real-time intelligence on indicators of compromise (IOCs) including malicious IP addresses, domains, URLs, and file hashes. Recorded Future aggregates and analyzes data from open, dark, and technical sources using machine learning to assign risk scores, enabling security teams to prioritize and respond to threats effectively.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Privileged access to the Recorded Future portal (`app.recordedfuture.com`).
  * A Recorded Future Enterprise account with API access enabled.



## Configure Recorded Future API access

To enable Google SecOps to retrieve IOC data, you need to generate an API token from the Recorded Future portal.

### Generate an API token

  1. Sign in to the **Recorded Future** portal at `app.recordedfuture.com`.
  2. Click your **avatar** in the top-right corner and select **User Settings**.
  3. In the left navigation pane, click **API Access**.
  4. Click **Generate New API Token**.
  5. Copy and save the API token (for example, `RF-1234567890abcdef`).

**Note:** Store the API token securely. You will not be able to view it again after closing the dialog. If you lose the token, you must generate a new one.**Important:** The API token authenticates all requests to the Recorded Future API using the `X-RFToken` HTTP header.

## Configure a feed in Google SecOps to ingest Recorded Future IOC logs

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Recorded Future IOC`).
  5. Select **Third Party API** as the **Source type**.
  6. Select **Recorded Future** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Authentication HTTP header** : Enter the authentication credentials in the following format:
           
           X-RFToken:your-api-token-value
           

Replace `your-api-token-value` with the API token generated in the Recorded Future portal.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve IOC data from the Recorded Future platform in chronological order.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Risk` | `confidence_score` | Directly mapped  
`Value` | `domain_and_ports.domain` | Directly mapped  
`Value` | `entity.file.sha256` | Directly mapped  
`Value` | `entity.hostname` | Directly mapped  
`ip` | `entity.ip` | Merged  
`Value` | `entity.url` | Directly mapped  
`ip` | `ip_and_ports.ip_address` | Directly mapped  
`Value` | `metadata.entity_type` | Mapped: `[a-f0-9]{64}` → `FILE`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`threat_det` | `metadata.threat` | Merged  
N/A | `feed_name` | Constant: `Recorded Future IOC`  
N/A | `metadata.entity_type` | Constant: `FILE`  
N/A | `metadata.vendor_name` | Constant: `RECORDED_FUTURE_IOC`  
`detail.FirstSeen` | `event.idm.entity.metadata.threat.first_discovered_time` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/recorded-future-ioc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
