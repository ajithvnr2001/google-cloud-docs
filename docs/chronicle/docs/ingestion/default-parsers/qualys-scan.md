---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-scan/
title: Collect Qualys Scan logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:41.762726+00:00
---

# Collect Qualys Scan logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-scan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Qualys Scan logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts fields from Qualys Scan JSON logs, normalizes timestamps, and maps them to the UDM. It handles various Qualys event types, including generic events and user logins, populating UDM fields with relevant security information and metadata.

## Before you begin

Ensure that you have the following prerequisites:

  * Google Security Operations instance.
  * Privileged access to Qualys VMDR console.



## Optional: Create a dedicated API User in Qualys

  1. Sign in to the Qualys console.
  2. Go to **Users**.
  3. Click **New** > **User**.
  4. Enter the **General Information** required for the user.
  5. Select the **User Role** tab.
  6. Make sure the role has the **API Access** checkbox selected.
  7. Click **Save**.



## Identify your specific Qualys API URL

### Option 1

Identify your URLs as mentioned in the [platform identification](https://www.qualys.com/platform-identification).

### Option 2

  1. Sign in to the Qualys console.
  2. Go to **Help** > **About**.
  3. Scroll to see this information under Security Operations Center (SOC).
  4. Copy the Qualys API URL.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Qualys Scan Logs**.
  5. Select **Third Party API** as the **Source type**.
  6. Select the **Qualys Scan** as the log type.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Username** : enter the username for the dedicated user.
     * **Secret** : enter the password for the dedicated user.
     * **API Full Path** : provide plain Qualys API server URL (for example, `qualysapi.qg2.apps.qualys.eu`).
     * **API Type** : select the scan type you want to ingest.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`Category` | `security_result.category_details` | Directly mapped from the `Category` field.  
`ID` | `metadata.product_log_id` | Directly mapped from the `ID` field. Converted to string.  
`LaunchDatetime` | `metadata.event_timestamp` | Used as event timestamp if `ScanInput.ScanDatetime` and `UpdateDate` are not present. Parsed in the "ISO8601" format.  
`Ref` | `additional.fields[1].key`   
`additional.fields[1].value.string_value` | Mapped to `additional.fields` with key "ScanReference" if `ScanReference` is not present.  
`ScanDetails.Status` | `security_result.detection_fields[0].key`   
`security_result.detection_fields[0].value` | Mapped to `security_result.detection_fields` with key "ScanDetails Status".  
`ScanInput.Network.ID` | `additional.fields[0].key`   
`additional.fields[0].value.string_value` | Mapped to `additional.fields` with key "ScanInput Network ID".  
`ScanInput.Network.Name` | `additional.fields[1].key`   
`additional.fields[1].value.string_value` | Mapped to `additional.fields` with key "ScanInput Network Name".  
`ScanInput.OptionProfile.ID` | `additional.fields[2].key`   
`additional.fields[2].value.string_value` | Mapped to `additional.fields` with key "ScanInput Option Profile ID".  
`ScanInput.OptionProfile.Name` | `additional.fields[3].key`   
`additional.fields[3].value.string_value` | Mapped to `additional.fields` with key "ScanInput Option Profile Name".  
`ScanInput.ScanDatetime` | `metadata.event_timestamp` | Used as event timestamp if present. Parsed in the "ISO8601" format.  
`ScanInput.Title` | `metadata.description` | Directly mapped from the `ScanInput.Title` field.  
`ScanInput.Username` | `principal.user.userid` | Directly mapped from the `ScanInput.Username` field.  
`ScanReference` | `additional.fields[4].key`   
`additional.fields[4].value.string_value` | Mapped to `additional.fields` with key "ScanReference".  
`Statement` | `metadata.description` | Directly mapped from the `Statement` field if `ScanInput.Title` and `Title` are not present.  
`Status` | `security_result.detection_fields[0].key`   
`security_result.detection_fields[0].value` | Mapped to `security_result.detection_fields` with key "Status".  
`SubCategory` | `security_result.description` | Directly mapped from the `SubCategory` field.  
`Technologies[].ID` | `security_result.detection_fields[0].value` | Directly mapped from the `Technologies[].ID` field. Converted to string. Part of a repeated `security_result` object.  
`Technologies[].Name` | `security_result.detection_fields[1].value` | Directly mapped from the `Technologies[].Name` field. Part of a repeated `security_result` object.  
`Technologies[].Rationale` | `security_result.detection_fields[2].value` | Directly mapped from the `Technologies[].Rationale` field. Part of a repeated `security_result` object.  
`Title` | `metadata.description` | Directly mapped from the `Title` field if `ScanInput.Title` and `Statement` are not present.  
`Type` | `additional.fields[2].key`   
`additional.fields[2].value.string_value` | Mapped to `additional.fields` with key "Type".  
`UpdateDate` | `metadata.event_timestamp` | Used as event timestamp if `ScanInput.ScanDatetime` is not present. Parsed in the "ISO8601" format.  
`Userlogin` | `target.user.userid` | Directly mapped from the `Userlogin` field. Set to "AUTHTYPE_UNSPECIFIED" if `Userlogin` is present. Set to "GENERIC_EVENT". Changed to "USER_LOGIN" if `Userlogin` is present. Changed to "USER_UNCATEGORIZED" if `metadata_event_type` is "GENERIC_EVENT" and `ScanInput.Username` is present. Set to "QUALYS_SCAN". Set to "QUALYS_SCAN". Set to "ID" for each technology. Part of a repeated `security_result` object. Set to "Name" for each technology. Part of a repeated `security_result` object. Set to "Rationale" for each technology. Part of a repeated `security_result` object.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-scan-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
