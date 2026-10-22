---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rh-isac-ioc/
title: Collect RH-ISAC IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:59.448919+00:00
---

# Collect RH-ISAC IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rh-isac-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect RH-ISAC IOC logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect RH-ISAC IOC (Indicators of Compromise) logs by setting up a Google Security Operations feed using the Third party API.

An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `RH_ISAC_IOC` ingestion label.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Active RH-ISAC Core Membership with access to the MISP platform
  * Privileged access to the RH-ISAC MISP instance at https://misp.rhisac.org

**Note:** RH-ISAC membership is limited to organizations within the consumer-facing sector, including retailers, restaurants, hotels, gaming casinos, food retailers, consumer products, and other hospitality companies. If you are not a member, visit [RH-ISAC Membership](https://rhisac.org/membership/) to apply.

## Generate RH-ISAC MISP API authentication key

To enable Google SecOps to retrieve IOCs from RH-ISAC MISP, you need to generate an API authentication key.

### Access your MISP profile

  1. Sign in to the **RH-ISAC MISP instance** at <https://misp.rhisac.org>.
  2. Go to **My Profile** by clicking your username in the top right corner.
  3. Alternatively, navigate directly to: <https://misp.rhisac.org/users/view/me>.



### Create authentication key

  1. In your profile page, select the **Auth Keys** tab.
  2. Click **Add authentication key**.
  3. Provide the following configuration details:

     * **Comment** : Enter a descriptive comment to identify the key (for example, `Google SecOps Integration`).
     * **Read only** : Select this option (recommended).

**Note:** Since Google SecOps only reads IOC data and does not write back to RH-ISAC MISP, using a read-only key follows the principle of least privilege.
     * **Allowed IPs** : Optional. Enter Google SecOps IP ranges if you want to restrict key usage to specific IPs.

  4. Click **Submit**.




### Save authentication key

After creating the key, a new authentication key is displayed **only once**.

  1. Copy and save*the authentication key immediately in a secure location.
  2. The key format is a long hexadecimal string (for example, `abc123def456...`).

**Important:** This key cannot be retrieved again after you leave this page. If you lose the key, you must generate a new one.

## Required API permissions

The RH-ISAC MISP API authentication key provides the following access based on your RH-ISAC membership role:

Permission | Access Level | Purpose  
---|---|---  
**Read IOCs** | Read | Retrieve indicators of compromise  
**Read Events** | Read | Retrieve MISP events with IOC data  
**Read Attributes** | Read | Retrieve specific IOC attributes  
**Read Tags** | Read | Retrieve taxonomy tags (e.g., rhisac:vetted)  
**Note:** Read-only keys cannot modify or create MISP data. This ensures Google SecOps integration does not alter shared threat intelligence.

## Understanding RH-ISAC IOC data

RH-ISAC provides curated, high-confidence threat intelligence through their MISP platform:

  * **Vetted Indicators** : IOCs tagged with `rhisac:vetted` are high-fidelity indicators validated by retail and hospitality sector members.
  * **Enriched Data** : All IOCs are automatically enriched using RH-ISAC's PyOTI (Python Open Threat Intelligence) framework.
  * **MITRE ATT &CK Mapping**: Events include MITRE ATT&CK framework mappings for tactics, techniques, and procedures.
  * **Threat Actor Context** : Galaxy clusters provide threat actor attribution and tool relationships.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `RH-ISAC IOC Feed`).
  5. Select **Third party API** as the **Source type**.
  6. Select **RH-ISAC** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **OAuth token endpoint** : Contact RH-ISAC support to obtain the OAuth token endpoint URL for your organization.
     * **OAuth client ID** : Contact RH-ISAC support to obtain your organization's OAuth client ID.
     * **OAuth client secret** : Contact RH-ISAC support to obtain your organization's OAuth client secret.
**Note:** Google SecOps uses OAuth authentication to connect to RH-ISAC MISP. The MISP API authentication key you generated earlier is used as part of the OAuth configuration. Contact RH-ISAC support for assistance with OAuth credentials setup.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve IOCs from the RH-ISAC MISP instance in chronological order.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Event.uuid` | `metadata.event_id` | MISP event unique identifier  
`Attribute.type` | `security_result.category` | IOC type (e.g., ip-dst, domain, md5)  
`Attribute.value` | `security_result.detection_fields` | IOC value (e.g., IP address, domain name, hash)  
`Attribute.comment` | `security_result.description` | Analyst comment or context  
`Event.info` | `security_result.summary` | Event description or title  
`Event.timestamp` | `metadata.event_timestamp` | Event creation or modification time  
`Attribute.category` | `security_result.rule_name` | MISP attribute category (e.g., Network activity, Payload)  
`Tag.name` | `security_result.detection_fields.tags` | Taxonomy tags (e.g., rhisac:vetted, tlp:amber)  
`GalaxyCluster.value` | `security_result.threat_name` | Threat actor or tool name  
`value` | `event.idm.entity.entity.file.full_path` | Mapped from changelog  
`event.idm.entity.metadata.interval.start_time` | `1` | Mapped from changelog  
`value` | `event.idm.entity.entity.hostname` | Mapped from changelog  
`uuid` | `event.idm.entity.metadata.product_entity_id` | Mapped from changelog  
`comment` | `event.idm.entity.metadata.threat.summary` | Mapped from changelog  
`category` | `event.idm.entity.metadata.threat.category_details` | Mapped from changelog  
`id` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`object_id` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`uuid` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rh-isac-ioc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
