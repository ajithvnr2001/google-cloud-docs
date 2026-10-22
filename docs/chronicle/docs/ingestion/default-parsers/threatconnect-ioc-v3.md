---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc-v3/
title: Collect ThreatConnect IOC logs using the v3 API \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:28.060405+00:00
---

# Collect ThreatConnect IOC logs using the v3 API  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc-v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ThreatConnect IOC logs using the v3 API

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

The ThreatConnect feed in Google Security Operations lets you automatically fetch Indicators of Compromise (IOCs) such as IP addresses, domains, URLs, and file hashes, along with their context (for example, threat type, confidence score, tags) from your ThreatConnect account. Ingesting these IOCs enriches your security data in Google Security Operations, enhancing threat detection and investigation capabilities.

This document describes how to configure Google SecOps to ingest IOCs from your ThreatConnect instance using the ThreatConnect v3 API connector. This version of the connector utilizes the ThreatConnect [v3 REST API](https://threatconnect.readme.io/reference/introduction), and is an updated version of the [existing connector](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc) that uses the ThreatConnect v2 REST API.

## Before you begin

Ensure that you have the following prerequisites:

  * An active ThreatConnect instance and user account with sufficient permissions to access the required indicators using the v3 API. This typically involves permissions to read indicators and their attributes
  * A Google Security Operations instance
  * Sufficient Identity and Access Management permissions in your Google Cloud project to manage Google SecOps feeds



## Configuration Steps

Follow these steps to set up the ThreatConnect IOC feed:

### Obtain ThreatConnect v3 API Credentials

  1. Log in to your ThreatConnect instance.
  2. Go to the **API user management** section to create a new API user or use an existing one designated for your Google SecOps integration.
  3. To create a new API user:

     1. Go to **Settings** > **Org Settings**.
     2. Go to the **Membership** tab in the **Organization Settings** page.
     3. Click **Create API User**.
     4. Fill out the fields on the **API User Administration** window:

        * **First Name** : enter the API user's first name.
        * **Last Name** : enter the API user's last name.
        * **System Role** : select the **Api User** or **Exchange Admin** System role.

**Note:** API users with the **Api User** role can use all ThreatConnect v2 and v3 API endpoints except for the v3 API TC Exchange™ administration endpoints, while the **Exchange Admin** role grants access to all v2 and v3 endpoints.
        * **Organization Role** : select the API user's Organization role.

        * **Include in Observations and False Positives** : select the checkbox to allow data provided by the API user to be included in counts.

        * **Disabled** : click the checkbox to disable an API user's account in the event that the Administrator wants to retain log integrity.

  4. Copy and securely store the **Access ID** and **Secret Key**.

  5. Click **Save**.

  6. Retrieve the Access ID and Secret Key for the relevant API user, and proceed to the next step.




### Configure the ThreatConnect feed in Google Security Operations

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ThreatConnect Logs`).
  5. For **Source Type** , select **Third-party API**.
  6. For **Log Type** , select **ThreatConnect IOC V3**.
  7. Click **Next**.
  8. Enter the following details for the ThreatConnect v3 API: 
     * **Username** : enter the ThreatConnect Access ID obtained in Step 1.
     * **Secret** : enter the ThreatConnect Secret Key obtained in Step 1.
     * **API Hostname** : your ThreatConnect instance's FQDN (for example: `<myinstance>.threatconnect.com`).
     * **Owners** : Specify the ThreatConnect Organization, Community, or Source to pull indicators from. Enter one owner per line. For more information, see the [Owners Overview](https://threatconnect.readme.io/reference/owners-overview).
     * **TQL** : The required TQL query to fetch IoCs based on your ingestion requirements (see How to write TQL Queries).
     * **Fields** : Names of additional fields to fetch, that are not fetched by default. Enter one field per line (see List of default and additional fields).
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.



### Validate ingestion

  1. After submitting the configuration, allow some time for the initial data pull.
  2. Check the feed status in the **Feeds** list. The status should eventually show as **Completed** or **Active**.
  3. Verify that data is being ingested by querying logs in the Google Security Operations search page: 
     * Use the query: `log_type = "THREATCONNECT_IOC_V3"`
  4. Examine the ingested logs to ensure fields are parsed as expected.



## How to write TQL Queries

In ThreatConnect, you can build structured queries with a SQL-like query language called ThreatConnect Query Language (TQL) to perform highly targeted searches of your data. A TQL query includes a parameter name, an operator, and a value or list of values, and you can combine multiple queries with parentheses and AND/OR logic.

  * The following example TQL query searches for high-confidence network indicators (IPs, Hosts, URLs) added in the last 30 days that are associated with Cobalt Strike, APTs, or Phishing. It also explicitly filters out known false positives and internal test data.
        
        typeName IN ("Address", "Host", "URL")
        AND confidence > 75
        AND dateAdded > "NOW() - 30 DAYS"
        AND (summary CONTAINS "cobalt" OR tag STARTSWITH "APT" OR tag ENDSWITH "Phish")
        AND NOT tag = "False_Positive"
        AND source != "Internal_Testing"
        




For more information on TQL, see the [ThreatConnect TQL documentation](https://training.threatconnect.com/learn/articles/6770516-threatconnect-query-language-tql-indicator-search).

## List of default and additional fields

This section details the specific data points retrieved from the ThreatConnect API, categorized by whether they are included by default or require manual configuration.

### Default fields

The following default fields are fetched by the API by default and don't require any additional configuration:

# | Field | Description | Type | Example Value(s)  
---|---|---|---|---  
1 | `active` | Indicates whether the Indicator is active | Boolean | `true`, `false`  
2 | `activeLocked` | Indicates whether the active Indicator Status is locked | Boolean | `true`, `false`  
3 | `confidence` | The Indicator's Confidence Rating | Integer | `1`, `2`, `3`, ... `100`  
4 | `dateAdded` | The date and time when the Indicator was created externally | DateTime | `"2023-10-04T12:34:56Z"`  
5 | `id` | The ID of the Indicator | Integer | `1`, `2`, `3`, ... `100`  
6 | `ip` | The IP address associated with the Address Indicator | String | `"107.180.48.66"`  
7 | `lastModified` | The date and time when the Indicator was last modified externally | DateTime | `"2023-10-04T12:34:56Z"`  
8 | `legacyLink` | Legacy URL (gated) to access details about the Indicator on the ThreatConnect app | URL | `"https://app.threatconnect.com/auth/indicators/..."`  
9 | `ownerId` | The ID of the owner to which the Indicator belongs | Integer | `1`, `2`, `3`, ... `100`  
10 | `ownerName` | The name of the owner to which the Indicator belongs | String | `"Demo Community"`  
11 | `privateFlag` | Indicates whether the Indicator is private | Boolean | `true`, `false`  
12 | `rating` | The Indicator's Threat Rating | Big Decimal | `1.0`, `2.0`, `3.0`, `4.0`, `5.0`  
13 | `summary` | The value of the Indicator | based on Indicator Type | `"type": "Host","summary": "zayla.co" ; "type": "Address","summary": "107.180.48.66"`  
14 | `type` | The type of Indicator being created | String | `"Address"`, `"Host"`, `"Registry Key"` ([list of accepted values](https://docs.threatconnect.com/en/latest/rest_api/v3/indicators/indicators.html#id5))  
15 | `webLink` | URL (gated) to access details about the Indicator on the ThreatConnect app | URL | `"https://app.threatconnect.com/#/details/indicators/10/overview"`  
  
### Additional fields

When retrieving data, you can use the **Fields** input field to include additional fields that are not included in the list of Default Fields.

To include one or more additional fields in the API response, populate the field value in separate lines in the **Field** input box while setting up your feed. For example, to include data for associated Groups and Tags in an API response, type in `associatedGroups` in line 1, press `Enter`, and then enter `tags` in line 2.

For more information about Indicator Attributes, see [Indicators Overview](https://training.threatconnect.com/learn/articles/indicators/indicator-attributes). For more information about Additional Fields, see [Include Additional Fields in API Responses](https://training.threatconnect.com/learn/articles/api/v3/indicators#additional-fields).

## Troubleshoot common issues

  * **Authentication Failed** : Double-check the API Host, Access ID, and Secret Key. Ensure the API user has the correct permissions for the v3 API and is not locked. Verify there are no network firewalls blocking Google SecOps' access to your ThreatConnect API host.
  * **No Data Ingested** : 
    * Confirm the filters you set (e.g., confidence, tags, types) match indicators available in your ThreatConnect instance.
    * Check the ThreatConnect API user's permissions.
    * Check the latest feed status in the Google SecOps UI for error messages.
  * **API Rate Limits** : ThreatConnect may enforce API rate limits. The connector should handle standard rate limits, but excessive fetching could cause delays. Check ThreatConnect API documentation for limit details.
  * **Data Parsing Issues** : If logs are ingested but not parsed correctly, compare the raw log from Google SecOps with the expected JSON output from the ThreatConnect v3 API for indicators. Contact Google Cloud support if you suspect a parser issue.



## Migrate from the v2 Connector

If you were using the previous ThreatConnect feed based on the v2 API, consider the following:

  * **Key differences** : The v3 API might have a different data structure, different filtering parameters, or new capabilities. Review the ThreatConnect v3 API documentation to understand changes relevant to the indicators you are ingesting.
  * **Setup v3 feed** : Configure the new feed (as described above) using your v3 API credentials. You can run both the v2 and v3 feeds simultaneously for a transition period.
  * **Validate data** : Compare the data ingested by the v3 feed with the data from the old v2 feed to ensure completeness and correctness. Note any field changes or improvements.
  * **Disable old feed** : Once you are confident the v3 feed is working as expected, you can disable or delete the old feed configuration that uses the v2 API to avoid duplicate data and reduce API calls.



## Learn more

For more information about the ThreatConnect v3 REST API, see the [ThreatConnect documentation](https://threatconnect.readme.io/reference/introduction).

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`id` | `entity.asset.product_object_id` | Directly mapped  
`md5` | `entity.file.md5` | Directly mapped  
`sha1` | `entity.file.sha1` | Directly mapped  
`sha256` | `entity.file.sha256` | Directly mapped  
`hostName` | `entity.hostname` | Directly mapped  
`ip` | `entity.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `ip`  
`type` | `entity.ip` | Mapped: `Address` → `ip`  
`active` | `entity.labels.value` | Directly mapped  
`activeLocked` | `entity.labels.value` | Directly mapped  
`associatedindicators_active` | `entity.labels.value` | Directly mapped  
`associatedindicators_rating` | `entity.labels.value` | Directly mapped  
`calScore` | `entity.labels.value` | Directly mapped  
`dnsActive` | `entity.labels.value` | Directly mapped  
`fileActions.count` | `entity.labels.value` | Directly mapped  
`observations` | `entity.labels.value` | Directly mapped  
`privateFlag` | `entity.labels.value` | Directly mapped  
`rating` | `entity.labels.value` | Directly mapped  
`threatAssessConfidence` | `entity.labels.value` | Directly mapped  
`threatAssessRating` | `entity.labels.value` | Directly mapped  
`threatAssessScoreFalsePositive` | `entity.labels.value` | Directly mapped  
`threatAssessScoreObserved` | `entity.labels.value` | Directly mapped  
`webLink` | `entity.labels.value` | Directly mapped  
`whoisActive` | `entity.labels.value` | Directly mapped  
`security_result` | `entity.security_result` | Merged  
`legacyLink` | `entity.url` | Directly mapped  
`address` | `entity.user.email_addresses` | Merged  
`type` | `entity.user.email_addresses` | Mapped: `EmailAddress` → `address`  
`has_file` | `metadata.entity_type` | Mapped: `true` → `FILE`  
`has_host` | `metadata.entity_type` | Mapped: `true` → `DOMAIN_NAME`  
`has_url` | `metadata.entity_type` | Mapped: `true` → `URL`  
`associatedgroups_dateAdded` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`associatedgroups_lastModified` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`associatedindicators_dateAdded` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`associatedindicators_lastModified` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`attributesdata_dateAdded` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`attributesdata_lastModified` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`tag_lastUsed` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`lastModified` | `metadata.interval.end_time` | Parsed as `ISO8601`  
`dateAdded` | `metadata.interval.start_time` | Parsed as `ISO8601`  
`confidence` | `metadata.threat.confidence_score` | Directly mapped  
`threatAssessScore` | `metadata.threat.risk_score` | Directly mapped  
`ownerName` | `metadata.threat.threat_feed_name` | Directly mapped  
`ownerId` | `metadata.threat.threat_id` | Directly mapped  
N/A | `entity.labels.key` | Constant: `rating`  
N/A | `metadata.entity_type` | Constant: `FILE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatconnect-ioc-v3-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
