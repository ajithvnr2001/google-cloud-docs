---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc/
title: Collect ThreatConnect IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:01.832343+00:00
---

# Collect ThreatConnect IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ThreatConnect IOC logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts IOC data from ThreatConnect JSON logs and transforms it into the UDM format. It handles various IOC types such as Host, Address, File, and URL, mapping fields like confidence scores, descriptions, and entity details to their corresponding UDM equivalents, and categorizes threats based on keywords within the log data.

**Note:** A newer version of this connector is available. To ingest logs using the ThreatConnect v3 API and the `THREATCONNECT_IOC_V3` log type, see [Collect ThreatConnect IOC logs using the v3 API](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc#ingest-threatconnect-v3).

## Before you begin

Ensure that you have the following prerequisites:

  * Google Security Operations instance.
  * Privileged access to ThreatConnect.



## Configure API User on ThreatConnect

  1. Sign in to ThreatConnect.
  2. Go to **Settings** > **Org Settings**.
  3. Go to the **Membership** tab in the **Organization Settings**.
  4. Click **Create API User**.
  5. Fill out the fields on the API User Administration window:

     * **First Name** : enter the API user's first name.
     * **Last Name** : enter the API user's last name
     * **System Role** : select the **Api User** or **Exchange Admin** System role.
**Note:** Available System roles for API users include the following:  
Api User: API users with this role can use all ThreatConnect v2 and v3 API endpoints, with the exception of the v3 API TC Exchange™ administration endpoints.  
Exchange Admin: API users with this role can use all ThreatConnect v2 and v3 API endpoints, including the v3 AP.
     * **Organization Role** : select the API user's Organization role.
     * **Include in Observations and False Positives** : select the checkbox to allow data provided by the API user to be included in observation and false-positive counts.
     * **Disabled** : click the checkbox to disable an API user's account in the event that the Administrator wants to retain log integrity.
     * Copy and save the **Access ID** and **Secret Key**.
  6. Click **Save**.




## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **ThreatConnect Logs**.
  5. Select **Third Party API** as the **Source type**.
  6. Select the **ThreatConnect** as the log type.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Username** : enter the ThreatConnect Access ID to authenticate as.
     * **Secret** : enter the ThreatConnect Secret Key for the specified user.
     * **API Hostname** : Fully Qualified Domain Name (FQDN) of your ThreatConnect instance (for example, `<myinstance>.threatconnect.com`).
     * **Owners** : all owner names, where the owner identifies a collection of IOCs.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`ownerName` | `categorization` | Directly mapped  
`confidence` | `confidence_score` | Directly mapped  
`webLink` | `description` | Directly mapped  
`summary` | `domain_and_ports.domain` | Directly mapped  
`summary` | `entity.file.md5` | Directly mapped  
`summary` | `entity.hostname` | Directly mapped  
`summary` | `entity.ip` | Merged  
`type` | `entity.ip` | Mapped: `Address` → `summary`  
`summary` | `entity.url` | Directly mapped  
`webLink` | `entity.url` | Directly mapped  
`summary` | `entity.user.email_addresses` | Merged  
`ownerName` | `feed_name` | Directly mapped  
`summary` | `ip_and_ports.ip_address` | Directly mapped  
`type` | `metadata.entity_type` | Mapped: `File` → `FILE`, `Host` → `DOMAIN_NAME`, `Address` → `IP_ADDRESS`  
`dateAdded` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`dateAdded` | `metadata.interval.start_time` | Parsed as `ISO8601`  
`id` | `metadata.product_entity_id` | Directly mapped  
`webLink` | `metadata.threat.about.url` | Directly mapped  
`threat_cat` | `metadata.threat.category` | Merged  
`ownerName` | `metadata.threat.category_details` | Merged  
`confidence` | `metadata.threat.confidence_details` | Directly mapped  
`description` | `metadata.threat.description` | Directly mapped  
`threat_description` | `metadata.threat.description` | Directly mapped  
`id` | `metadata.threat.rule_id` | Directly mapped  
`rule_id` | `metadata.threat.rule_name` | Directly mapped  
`rule_type` | `metadata.threat.rule_type` | Directly mapped  
`threat_summary` | `metadata.threat.summary` | Directly mapped  
N/A | `metadata.entity_type` | Constant: `FILE`  
N/A | `metadata.vendor_name` | Constant: `THREATCONNECT_IOC`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
