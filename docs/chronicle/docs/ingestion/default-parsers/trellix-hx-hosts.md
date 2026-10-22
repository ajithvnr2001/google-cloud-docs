---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-hosts/
title: Collect Trellix Endpoint Security (HX) host inventory logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:32.567132+00:00
---

# Collect Trellix Endpoint Security (HX) host inventory logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-hosts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix Endpoint Security (HX) host inventory logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Trellix Endpoint Security (HX) host inventory logs by setting up a Google Security Operations feed using the Third-Party API.

Trellix Endpoint Security (HX) maintains an inventory of all managed hosts including hostname, operating system, agent version, domain membership, and last check-in status. Collecting host inventory data in Google SecOps enables asset tracking, compliance monitoring, and correlation of endpoint context with security events.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the Trellix Endpoint Security (HX) management console
  * Trellix Endpoint Security (HX) with API access enabled
  * One of the following authentication credentials configured (see next section)



## Configure Trellix HX API access

To enable Google SecOps to pull host inventory data, you need API credentials from your Trellix HX environment. 

  1. Sign in to the Endpoint Security (HX) Web UI as an administrator.
  2. Go to **Admin > Appliance Settings > User Accounts**.
  3. Add a new user account with the `api_analyst` role for use with Google SecOps. Do not reuse the built-in `api_analyst` account.
  4. Copy and save the following values: 
     * **Username** : The local HX account username.
     * **Password** : The local HX account password.



## Configure a feed in Google SecOps to ingest Trellix HX host inventory logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Trellix HX Hosts`).
  5. Select **Third-Party API** as the **Source type**.
  6. Select **Trellix HX Hosts** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **HX Device URL** : The URL of your HX device (for example, `https://xxxxxxxx-hx-webui-1.hex03.apps.xdr.trellix.com`).
     * **Authentication** : **Trellix Local Auth**

       * **Username** : Enter the local HX account username created for this integration.
       * **Password** : Enter the password for the username.
       * **Token API Endpoint Path** : `/hx/api/v3/token`
       * **Token Header** : `X-FeApi-Token`
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve host inventory logs from the Trellix HX instance in chronological order.

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`domain` | `entity.administrative_domain` | Directly mapped  
`asset_id` | `entity.asset.asset_id` | Directly mapped  
`ad_common_names` | `entity.asset.attribute.labels.value` | Directly mapped  
`ad_org_units` | `entity.asset.attribute.labels.value` | Directly mapped  
`agent_version` | `entity.asset.attribute.labels.value` | Directly mapped  
`containment_missing_software` | `entity.asset.attribute.labels.value` | Directly mapped  
`containment_queued` | `entity.asset.attribute.labels.value` | Directly mapped  
`containment_state` | `entity.asset.attribute.labels.value` | Directly mapped  
`excluded_from_containment` | `entity.asset.attribute.labels.value` | Directly mapped  
`last_poll_ip` | `entity.asset.attribute.labels.value` | Directly mapped  
`reported_clone` | `entity.asset.attribute.labels.value` | Directly mapped  
`sysinfo.url` | `entity.asset.attribute.labels.value` | Directly mapped  
`timezone` | `entity.asset.attribute.labels.value` | Directly mapped  
`initial_agent_checkin` | `entity.asset.first_discover_time` | Parsed as `ISO8601`  
`hostname` | `entity.asset.hostname` | Directly mapped  
`primary_ip_address` | `entity.asset.ip` | Merged  
`last_poll_timestamp` | `entity.asset.last_discover_time` | Parsed as `ISO8601`  
`primary_mac` | `entity.asset.mac` | Merged  
`os.patch_level` | `entity.asset.platform_software.platform_patch_level` | Directly mapped  
`os.product_name` | `entity.asset.platform_software.platform_version` | Directly mapped  
`_id` | `entity.asset.product_object_id` | Directly mapped  
`asset_id` | `entity.asset_id` | Directly mapped  
`hostname` | `entity.hostname` | Directly mapped  
`primary_ip_address` | `entity.ip` | Merged  
`primary_mac` | `entity.mac` | Merged  
`os.patch_level` | `entity.platform_patch_level` | Directly mapped  
`os.product_name` | `entity.platform_version` | Directly mapped  
`url` | `entity.url` | Directly mapped  
`interval_end_time` | `metadata.interval.end_time` | Parsed as `ISO8601`  
`interval_start_time` | `metadata.interval.start_time` | Parsed as `ISO8601`  
N/A | `entity.asset.attribute.labels.key` | Constant: `reported_clone`  
N/A | `entity.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `entity.platform` | Constant: `WINDOWS`  
N/A | `metadata.entity_type` | Constant: `ASSET`  
N/A | `metadata.product_name` | Constant: `HX`  
N/A | `metadata.vendor_name` | Constant: `Trellix`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-hosts-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
