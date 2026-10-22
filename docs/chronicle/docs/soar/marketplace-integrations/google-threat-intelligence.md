---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-threat-intelligence/
title: Integrate Google Threat Intelligence with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:10.680164+00:00
---

# Integrate Google Threat Intelligence with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-threat-intelligence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Google Threat Intelligence with Google SecOps

This document explains how to integrate Google Threat Intelligence with Google Security Operations.

## Before you begin

To use this integration, you need an API key. For more information, see [Google Threat Intelligence API keys](https://gtidocs.virustotal.com/docs/how-get-gti-api-keys).

## Integration parameters

The Google Threat Intelligence integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required.The API root of the Google Threat Intelligence instance.The default value is `https://www.virustotal.com`.  
`API Key` | Required.The Google Threat Intelligence API key.  
`ASM Project Name` | Optional.The Mandiant Attack Surface Management (ASM) project name to use in the integration. This parameter is required to run the **Search ASM Entities** , **Search ASM Issues** and **Update ASM Issue** actions. If no value is set, only alerts from collections in the primary project are returned.  
`Active Group` | Optional.The Active Group (Organization Context) identifier for multi-tenant environments. This is required if your ASM projects reside in a different organization than your primary one.  
`Verify SSL` | Required.If selected, the integration validates the SSL certificate when connecting to the Google Threat Intelligence server.Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add ASM Issue Note

Use the **Add ASM Issue Note** action to append a technical note to an Attack Surface Management (ASM) issue in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add ASM Issue Note** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | Required. The ID of the alert to update.  
`Text` | Required. The content of the analysis or note to append to the alert.  
  
#### Action outputs

The **Add ASM Issue Note** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add ASM Issue Note** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated the alert with the ID ALERT_ID in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Add ASM Issue Note". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add ASM Issue Note** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Comment To Entity

Use the **Add Comment To Entity** action to add comments to Google SecOps entities in Google Threat Intelligence.

This action only supports MD5, SHA-1, and SHA-256 hashes.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `URL`



#### Action inputs

The **Add Comment To Entity** action requires the following parameters:

Parameter | Description  
---|---  
`Comment` | Required. A comment to add to all supported entities.  
  
#### Action outputs

The **Add Comment To Entity** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Add Comment To Entity** action:
    
    
    {
       "Status": "Done"
    }
    
    
    
    {
       "Status": "Not done"
    }
    

##### Output messages

The **Add Comment To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added comments to the following entities in Google Threat Intelligence: ENTITY_ID.` `The action wasn't able to add comments to the following entities in Google Threat Intelligence: ENTITY_ID.` `No comments were added to the provided entities in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Add Comment To Entity". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Comment To Entity** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add Tag To DTM Alert

Use the **Add Tag To DTM Alert** to add tags to a Digital Threat Monitoring (DTM) alert in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Tag To DTM Alert** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | Required. The unique identifier of the alert to update.  
`Mode` | Optional. The operational logic for the tag update. The possible values are as follows:

  * `Append`: Adds the specified tags to the alert's existing tag list.
  * `Set`: Overwrites all existing alert tags with the tags provided in `Tags`.

The default value is `Append`.  
`Tags` | Required. A comma-separated list of tags to apply to the alert.  
  
#### Action outputs

The **Add Tag To DTM Alert** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add Tag To DTM Alert** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated the alert with the ID ALERT_ID in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Add Tag To DTM Alert". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Tag To DTM Alert** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Vote To Entity

Use the **Add Comment To Entity** action to add votes to Google SecOps entities in Google Threat Intelligence.

This action only supports MD5, SHA-1, and SHA-256 hashes.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `URL`



#### Action inputs

The **Add Vote To Entity** action requires the following parameters:

Parameter | Description  
---|---  
`Vote` | Required.A vote to add to all supported entities.The possible values are as follows:

  * `Harmless`
  * `Malicious`

The default value is `Malicious`.  
  
#### Action outputs

The **Add Vote To Entity** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Add Vote To Entity** action:
    
    
    {
       "Status": "Done"
    }
    
    
    
    {
       "Status": "Not done"
    }
    

##### Output messages

The **Add Vote To Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added votes to the following entities in Google Threat Intelligence: ENTITY_ID.` `Action wasn't able to add votess to the following entities in Google Threat Intelligence: ENTITY_ID.` `No votes were added to the provided entities in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Add Vote To Entity". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Vote To Entity** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Download File

Use the **Download File** action to download a file from Google Threat Intelligence.

This action runs on the Google SecOps `Hash` entity.

This action only supports MD5, SHA-1, and SHA-256 hashes.

#### Action inputs

The **Download File** action requires the following parameters:

Parameter | Description  
---|---  
`Download Folder Path` | Required. The path to the folder to store downloaded files.  
`Overwrite` | Required. If selected, the action overwrites an existing file with the new file if the filenames are identical.Enabled by default.  
  
#### Action outputs

The **Download File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Download File** action:
    
    
    {
        "absolute_file_paths": ["file_path_1","file_path_2"]
    }
    

##### Output messages

The **Download File** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully downloaded related files for the following entities in Google Threat Intelligence: ENTITY_ID.` `No related files were found for the following entities in Google Threat Intelligence: ENTITY_ID.` `No related files were found for the provided entities in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Download File". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
### Enrich Entities

Use the **Enrich Entities** action to enrich entities with information from Google Threat Intelligence.

This action supports the MD5, SHA-1, and SHA-256 hashes.

This action runs on the following Google SecOps entities:

  * `CVE`
  * `Domain`
  * `Hash` (including `CHILDHASH` and `PARENTHASH`)
  * `Hostname`
  * `IP Address`
  * `Threat Actor`
  * `URL`



#### Action inputs

The **Enrich Entities** action requires the following parameters:

Parameter | Description  
---|---  
`GTI Score` | Optional. The minimum Google Threat Intelligence score required to mark a Google SecOps entity as suspicious. This condition is validated alongside Google Threat Intelligence verdict information. This parameter only supports `IP Address`, `URL`, `Hostname`, `Domain`, and `Hash` entities. If no value is provided, the action ignores Google Threat Intelligence score values. The default value is `60`.  
`Engine Threshold` | Optional. The minimum number of security engines that must mark an entity as malicious or suspicious for Google SecOps to label it as suspicious. This condition is validated alongside Google Threat Intelligence verdict information. This parameter only supports `IP Address`, `URL`, `Hostname`, `Domain`, and `Hash` entities. If `Engine Allowlist` contains values, the action only counts results from those specific engines. If no value is provided, the action ignores engine calculations.  
`Engine Percentage Threshold` | Optional. The minimum percentage of security engines that must mark an entity as malicious or suspicious for Google SecOps to label it as suspicious. This parameter only supports `IP Address`, `URL`, `Hostname`, `Domain`, and `Hash` entities. If `Engine Allowlist` contains values, the action only calculates the percentage from those specific engines. If both `Engine Threshold` and `Engine Percentage Threshold` are provided, `Engine Threshold` takes precedence. If no value is provided, the action ignores engine calculations. The maximum value is `100`. The minimum value is `0`.  
`Engine Allowlist` | Optional. A comma-separated list of security engines used to retrieve maliciousness information (for example, `AlienVault,Kaspersky`). If no value is provided, the action retrieves results from every available engine. Engines that don't return information about an entity are excluded from `Engine Threshold` and `Engine Percentage Threshold` calculations.  
`Resubmit Entity` | Optional.If selected, the action resubmits entities for analysis instead of using the entity information from the previous action run.This parameter only supports the `URL` and `Hash` entities.Not selected by default.  
`Resubmit After (Days)` | Optional.The number of days for the action to wait before submitting the entity again. To use this parameter, select the `Resubmit Entity` parameter.The default value is `30`.This parameter only supports the `URL` and `Hash` entities.  
`Sandbox` | Optional.A comma-separated list of sandbox names to analyze, such as `VirusTotal Jujubox, VirusTotal ZenBox, Microsoft Sysinternals, Tencent HABO`.This parameter only supports the `Hash` entity.If you don't set this parameter, the action uses the default sandbox, which is `VirusTotal Jujubox`.  
`Retrieve Sandbox Analysis` | Optional.If selected, the action retrieves the sandbox analysis for the entity and creates a separate section for every sandbox in the JSON result.The action returns data for sandboxes that you configured in the `Sandbox` parameter.This parameter only supports the `Hash` entity.Not selected by default.  
`Fetch MITRE Details` | Optional.If selected, the action returns information about the related MITRE techniques and tactics.This parameter only supports the `Hash` entity.Not selected by default.  
`Lowest MITRE Technique Severity` | Optional.The lowest MITRE technique severity to return. The action treats the `Unknown` severity as `Info`. This parameter only supports the `Hash` entity.The possible values are as follows:

  * `High`
  * `Medium`
  * `Low`
  * `Info`

The default value is `Medium`.   
`Retrieve Comments` | Optional.If selected, the action retrieves comments about the entity.This parameter supports the following entities:

  * `Domain`
  * `Hash`
  * `Hostname`
  * `IP Address`
  * `URL`

  
`Widget Theme` | Optional. The visual style applied to the IOC augmented widget. The possible values are as follows:

  * `Dark`
  * `Dark Blue`
  * `Light`

The default value is `Dark Blue`.  
`Max Comments To Return` | Optional.The maximum number of comments to return for every action run.The default value is `10`.  
  
#### Action outputs

The **Enrich Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result. | Available  
  
##### Case wall link

The **Enrich Entities** action can return the following links:

  * IOC: `https://www.virustotal.com/gui/ENTITY_TYPE/ENTITY/detection`

  * Threat actor: `https://www.virustotal.com/gui/collection/threat-actor--ID`

  * Vulnerability: `https://www.virustotal.com/gui/collection/vulnerability--ID`




##### Entity enrichment table

  1. The **Enrich Entities** action support the following entity enrichment for **IP addresses** :
Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GTI_id` | `id` | When available in the JSON result.  
`GTI_owner` | `as_owner` | When available in the JSON result.  
`GTI_asn` | `asn` | When available in the JSON result.  
`GTI_continent` | `continent` | When available in the JSON result.  
`GTI_country` | `country` | When available in the JSON result.  
`GTI_harmless_count` | `last_analysis_stats/harmless` | When available in the JSON result.  
`GTI_malicious_count` | `last_analysis_stats/malicious` | When available in the JSON result.  
`GTI_suspicious_count` | `last_analysis_stats/suspicious` | When available in the JSON result.  
`GTI_undetected_count` | `last_analysis_stats/undetected` | When available in the JSON result.  
`GTI_certificate_valid_not_after` | `validity/not_after` | When available in the JSON result.  
`GTI_certificate_valid_not_before` | `validity/not_before` | When available in the JSON result.  
`GTI_reputation` | `reputation` | When available in the JSON result.  
`GTI_tags` | `Comma-separated list of tags` | When available in the JSON result.  
`GTI_malicious_vote_count` | `total_votes/malicious` | When available in the JSON result.  
`GTI_harmless_vote_count` | `total_votes/harmless` | When available in the JSON result.  
`GTI_report_link` | `report_link` | When available in the JSON result.  
`GTI_widget_link` | `widget_url` | When available in the JSON result.  
`GTI_threat_score` | `gti_assessment.threat_score.value` | When available in the JSON result.  
`GTI_severity` | `gti_assessment.severity.value` | When available in the JSON result.  
`GTI_normalised_categories` | `CSV of gti_assessment.contributing_factors.normalised_categories` | When available in the JSON result.  
`GTI_verdict` | `gti_assessment.verdict.value` | When available in the JSON result.  
`GTI_description` | `gti_assessment.description` | When available in the JSON result.  
  2. The **Enrich Entities** action support the following entity enrichment for **URL** :
Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GTI_id` | `id` | When available in the JSON result.  
`GTI_title` | `title` | When available in the JSON result.  
`GTI_last_http_response_code` | `last_http_response_code` | When available in the JSON result.  
`GTI_last_http_response_content_length` | `last_http_response_content_length` | When available in the JSON result.  
`GTI_threat_names` | `Comma-separated list of threat_names` | When available in the JSON result.  
`GTI_harmless_count` | `last_analysis_stats/harmless` | When available in the JSON result.  
`GTI_malicious_count` | `last_analysis_stats/malicious` | When available in the JSON result.  
`GTI_suspicious_count` | `last_analysis_stats/suspicious` | When available in the JSON result.  
`GTI_undetected_count` | `last_analysis_stats/undetected` | When available in the JSON result.  
`GTI_reputation` | `reputation` | When available in the JSON result.  
`GTI_tags` | `Comma-separated list of tags` | When available in the JSON result.  
`GTI_malicious_vote_count` | `total_votes/malicious` | When available in the JSON result.  
`GTI_harmless_vote_count` | `total_votes/harmless` | When available in the JSON result.  
`GTI_report_link` | `report_link` | When available in the JSON result.  
`GTI_widget_link` | `widget_url` | When available in the JSON result.  
`GTI_threat_score` | `gti_assessment.threat_score.value` | When available in the JSON result.  
`GTI_severity` | `gti_assessment.severity.value` | When available in the JSON result.  
`GTI_normalised_categories` | `CSV of gti_assessment.contributing_factors.normalised_categories` | When available in the JSON result.  
`GTI_verdict` | `gti_assessment.verdict.value` | When available in the JSON result.  
`GTI_description` | `gti_assessment.description` | When available in the JSON result.  
`GTI_category_{attributes/categories/json key}` | `{attributes/categories/json key value}` | When available in the JSON result.  
  3. The **Enrich Entities** action support the following entity enrichment for **Hash** :
Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GTI_id` | `id` | When available in the JSON result.  
`GTI_magic` | `magic` | When available in the JSON result.  
`GTI_md5` | `md5` | When available in the JSON result.  
`GTI_sha1` | `sha1` | When available in the JSON result.  
`GTI_sha256` | `sha256` | When available in the JSON result.  
`GTI_ssdeep` | `ssdeep` | When available in the JSON result.  
`GTI_tlsh` | `tlsh` | When available in the JSON result.  
`GTI_vhash` | `vhash` | When available in the JSON result.  
`GTI_meaningful_name` | `meaningful_name` | When available in the JSON result.  
`GTI_magic` | `Comma-separated list of names` | When available in the JSON result.  
`GTI_harmless_count` | `last_analysis_stats/harmless` | When available in the JSON result.  
`GTI_malicious_count` | `last_analysis_stats/malicious` | When available in the JSON result.  
`GTI_suspicious_count` | `last_analysis_stats/suspicious` | When available in the JSON result.  
`GTI_undetected_count` | `last_analysis_stats/undetected` | When available in the JSON result.  
`GTI_reputation` | `reputation` | When available in the JSON result.  
`GTI_tags` | `Comma-separated list of tags` | When available in the JSON result.  
`GTI_malicious_vote_count` | `total_votes/malicious` | When available in the JSON result.  
`GTI_harmless_vote_count` | `total_votes/harmless` | When available in the JSON result.  
`GTI_report_link` | `report_link` | When available in the JSON result.  
`GTI_widget_link` | `widget_url` | When available in the JSON result.  
`GTI_threat_score` | `gti_assessment.threat_score.value` | When available in the JSON result.  
`GTI_severity` | `gti_assessment.severity.value` | When available in the JSON result.  
`GTI_normalized_categories` | `CSV of gti_assessment.contributing_factors.normalised_categories` | When available in the JSON result.  
`GTI_verdict` | `gti_assessment.verdict.value` | When available in the JSON result.  
`GTI_description` | `gti_assessment.description` | When available in the JSON result.  
`GTI_exiftool_{json_key}` | `GTI_exiftool_{json_key.value}` |   
  4. The **Enrich Entities** action support the following entity enrichment for **Domain/Hostname** :
Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GTI_id` | `id` | When available in the JSON result.  
`GTI_harmless_count` | `last_analysis_stats/harmless` | When available in the JSON result.  
`GTI_malicious_count` | `last_analysis_stats/malicious` | When available in the JSON result.  
`GTI_suspicious_count` | `last_analysis_stats/suspicious` | When available in the JSON result.  
`GTI_undetected_count` | `last_analysis_stats/undetected` | When available in the JSON result.  
`GTI_reputation` | `reputation` | When available in the JSON result.  
`GTI_tags` | `Comma-separated list of tags` | When available in the JSON result.  
`GTI_malicious_vote_count` | `total_votes/malicious` | When available in the JSON result.  
`GTI_harmless_vote_count` | `total_votes/harmless` | When available in the JSON result.  
`GTI_report_link` | `report_link` | When available in the JSON result.  
`GTI_widget_link` | `widget_url` | When available in the JSON result.  
`GTI_threat_score` | `gti_assessment.threat_score.value` | When available in the JSON result.  
`GTI_severity` | `gti_assessment.severity.value` | When available in the JSON result.  
`GTI_normalized_categories` | `CSV of gti_assessment.contributing_factors.normalised_categories` | When available in the JSON result.  
`GTI_verdict` | `gti_assessment.verdict.value` | When available in the JSON result.  
`GTI_description` | `gti_assessment.description` | When available in the JSON result.  
`GGTI_category_{attributes/categories/json key}` | `{attributes/categories/json key value}` | When available in the JSON result.  
  5. The **Enrich Entities** action support the following entity enrichment for **Threat Actor** :
Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GTI_motivations` | `Csv of motivations/name` | When available in the JSON result.  
`GTI_aliases` | `Csv of alt_names_details/value` | When available in the JSON result.  
`GTI_industries` | `Csv of targeted_industries/value` | When available in the JSON result.  
`GTI_malware` | `Csv of malware/name` | When available in the JSON result.  
`GTI_source_region` | `CSV of source_regions_hierarchy/country` | When available in the JSON result.  
`GTI_target_region` | `Csv of targeted_regions_hierarchy/country` | When available in the JSON result.  
`GTI_origin` | `origin` | When available in the JSON result.  
`GTI_description` | `description` | When available in the JSON result.  
`GTI_last_activity_time` | `last_activity_time` | When available in the JSON result.  
`GTI_report_link` | `We craft it.` | When available in the JSON result.  
  6. The **Enrich Entities** action support the following entity enrichment for **Vulnerability** :
Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GTI_sources` | `Csv of source_name` | When available in the JSON result.  
`GTI_exploitation_state` | `exploitation_state` | When available in the JSON result.  
`GTI_date_of_disclosure` | `date_of_disclosure` | When available in the JSON result.  
`GTI_vendor_fix_references` | `vendor_fix_references/url` | When available in the JSON result.  
`GTI_exploitation_vectors` | `Csv of exploitation_vectors` | When available in the JSON result.  
`GTI_description` | `description` | When available in the JSON result.  
`GTI_risk_rating` | `risk_rating` | When available in the JSON result.  
`GTI_available_mitigation` | `CSV of available_mitigation` | When available in the JSON result.  
`GTI_exploitation_consequence` | `exploitation_consequence` | When available in the JSON result.  
`GTI_report_link` | `We craft it.` | When available in the JSON result.  



##### JSON result

The following example shows the JSON result output for IOCs (`IP`, `Hash`, `URL`, `Domain`, and `Hostname` entities) received when using the **Enrich Entities** action:
    
    
    {
       [
           {
               "Entity": "8b2e701e91101955c73865589a4c72999aeabc11043f7xxxxx",
               "EntityResult": {
                   "is_risky": true, 
                   "attributes": {
                       "authentihash": "ad56160b465f7bd1e7568640397f01fc4f8819ce6f0c141569xxxx",
                       "creation_date": 1410950077,
                       "downloadable": true,
                       "exiftool": {
                           "CharacterSet": "Unicode",
                           "CodeSize": "547xx",
                           "CompanyName": "MySQL, AB",
                           "EntryPoint": "0x39xx",
                           "FileDescription": "WinMerge Shell Integration",
                           "FileFlagsMask": "0x00xx",
                           "FileOS": "Windows NT 32-bit",
                           "FileSubtype": "0",
                           "FileType": "Win32 EXE",
                           "FileTypeExtension": "exe",
                           "FileVersion": "1.0.1.6",
                           "FileVersionNumber": "1.0.1.6",
                           "ImageFileCharacteristics": "Executable, 32-bit",
                           "ImageVersion": "0.0",
                           "InitializedDataSize": "199168",
                           "InternalName": "ShellExtension",
                           "LanguageCode": "English (U.S.)",
                           "LegalCopyright": "Copyright 2003-2013",
                           "LinkerVersion": "10.0",
                           "MIMEType": "application/octet-stream",
                           "MachineType": "Intel 386 or later, and compatibles",
                           "OSVersion": "5.1",
                           "ObjectFileType": "Executable application",
                           "OriginalFileName": "ShellExtension",
                           "PEType": "PE32",
                           "ProductName": "ShellExtension",
                           "ProductVersion": "1.0.1.6",
                           "ProductVersionNumber": "1.0.1.6",
                           "Subsystem": "Windows GUI",
                           "SubsystemVersion": "5.1",
                           "TimeStamp": "2014:09:17 10:34:37+00:00",
                           "UninitializedDataSize": "0"
                       },
                       "first_submission_date": 1411582812,
                       "last_analysis_date": 1606903659,
                       "last_analysis_results": {
                           "ALYac": {
                               "category": "malicious",
                               "engine_name": "ALYac",
                               "engine_update": "20201202",
                               "engine_version": "1.1.1.5",
                               "method": "blacklist",
                               "result": "Trojan.Foreign.Gen.2"
                           }
                       },
                       "last_analysis_stats": {
                           "confirmed-timeout": 0,
                           "failure": 0,
                           "harmless": 0,
                           "malicious": 61,
                           "suspicious": 0,
                           "timeout": 0,
                           "type-unsupported": 5,
                           "undetected": 10
                       },
                       "last_modification_date": 1606911051,
                       "last_submission_date": 1572934476,
                       "magic": "PE32 executable for MS Windows (GUI) Intel 80386 32-bit",
                       "md5": "9498ff82a64ff445398c8426exxxx",
                       "meaningful_name": "ShellExtension",
                       "names": [
                           "ShellExtension",
                           "ZeuS_binary_9498ff82a64ff445398c8426exxxx.exe",
                           "9498ff82a64ff445398c8426exxxx.exe",
                           "9498ff82a64ff445398c8426exxxx",
                           "2420800",
                           "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1xxxxx.exe",
                           "sigchxxx.exe",
                           "malwxxx.exe"
                       ],
                       "reputation": -49,
                       "sha1": "36f9ca40b3ce96fcee1cf1d4a722293553xxxx",
                       "sha256": "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1cxxxx",
                       "sigma_analysis_stats": {
                           "critical": 0,
                           "high": 0,
                           "low": 4,
                           "medium": 0
                       },
                       "sigma_analysis_summary": {
                           "Sigma Integrated Rule Set (GitHub)": {
                               "critical": 0,
                               "high": 0,
                               "low": 4,
                               "medium": 0
                           }
                       },
                       "signature_info": {
                           "copyright": "Copyright 2003-2013",
                           "description": "WinMerge Shell Integration",
                           "file version": "1.0.1.6",
                           "internal name": "ShellExtension",
                           "original name": "ShellExtension",
                           "product": "ShellExtension"
                       },
                       "size": 254976,
                       "ssdeep": "6144:Gz90qLc1zR98hUb4UdjzEwG+vqAWiR4EXePbix67CNzjX:Gz90qLc1lWhUbhVqxxxx",
                       "tags": [
                           "peexe",
                           "runtime-modules",
                           "direct-cpu-clock-access"
                       ],
                       "times_submitted": 8,
                       "tlsh": "T1DB44CF267660D833D0DF94316C75C3F9673BFC2123215A6B6A4417699E307Exxxx",
                       "total_votes": {
                           "harmless": 2,
                           "malicious": 7
                       },
                       "trid": [
                           {
                               "file_type": "Win32 Executable MS Visual C++ (generic)",
                               "probability": 54.3
                           },
                           {
                               "file_type": "Win16 NE executable (generic)",
                               "probability": 12.2
                           },
                           {
                               "file_type": "Win32 Dynamic Link Library (generic)",
                               "probability": 11.4
                           },
                           {
                               "file_type": "Win32 Executable (generic)",
                               "probability": 7.8
                           },
                           {
                               "file_type": "OS/2 Executable (generic)",
                               "probability": 3.5
                           }
                       ],
                       "type_description": "Win32 EXE",
                       "type_extension": "exe",
                       "type_tag": "peexe",
                       "unique_sources": 8,
                       "vhash": "025056657d755510804011z9005b9z25z1xxxx"
                   },
                   "id": "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdbxxxxx",
                   "links": {
                       "self": "https://www.virustotal.com/api/v3/files/8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdbxxxx"
                   },
                   "type": "file",
                   "comments": [
                       {
                           "attributes": {
                               "date": 1595402790,
                               "html": "#malware #Zeus<br /><br />Full genetic report from Intezer Analyze:<br />https://analyze.intezer.com/#/files/8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdbxxxx<br /><br />#IntezerAnalyze",
                               "tags": [
                                   "malware",
                                   "zeus",
                                   "intezeranalyze"
                               ],
                               "text": "#malware #Zeus\n\nFull genetic report from Intezer Analyze:\nhttps://analyze.intezer.com/#/files/8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdbxxxx\n\n#IntezerAnalyze",
                               "votes": {
                                   "abuse": 0,
                                   "negative": 0,
                                   "positive": 0
                               }
                           },
                           "id": "f-8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdbxxxx-9945xxxx",
                           "links": {
                               "self": "https://www.virustotal.com/api/v3/comments/f-8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdbxxxx-9945xxx"
                           },
                           "type": "comment"
                       }
                   ],
                   "widget_url": "https://www.virustotal.com/ui/widget/html/OGIyZTcwMWU5MTEwMTk1NWM3Mzg2NTU4OWE0YzcyOTk5YWVhYmMxMTA0M2Y3MTJlMDVmZGIxYzE3YzRhYjE5YXx8ZmlsZXx8eyJiZDEiOiAiIzRkNjM4NSIsICJiZzEiOiAiIzMxM2Q1YSIsICJiZzIiOiAiIzIyMmM0MiIsICJmZzEiOiAiI2ZmZmZmZiIsICJ0eXBlIjogImRlZmF1bHQifXx8ZnVsbHx8Zm91bmR8fDE2NDY2NzIzOTN8fGI5OWQ3MTY5MGIzZGY5MmVjMWExNTZlMmQ1MjM3OWJhMGMxYzgyZTAwMjVkMTJmZjg5MWM2YzdjNxxxxxxxxxx",
                   "related_mitre_tactics": [
                       {
                           "id": "TA0002",
                           "name": "Execution"
                       }
                   ],
                   "related_mitre_techniques": [
                       {
                           "id": "T1129",
                           "name": "Shared Modules",
                           "severity": "INFO"
                       }
                   ],
                   "sandboxes_analysis": {
                       "VirusTotal Jujubox": {
                           "attributes": {
                               "registry_keys_opened": [
                                   "HKCU\\\\SOFTWARE\\\\Microsoft",
                                   "SOFTWARE\\\\Microsoft\\\\Xuoc"
                               ],
                               "calls_highlighted": [
                                   "GetTickCount"
                               ],
                               "tags": [
                                   "DIRECT_CPU_CLOCK_ACCESS",
                                   "RUNTIME_MODULES"
                               ],
                               "files_written": [
                                   "C:\\\\Users\\\\<USER>\\\\AppData\\\\Roaming\\\\Uwcyi\\\\xeysv.exe"
                               ],
                               "mutexes_opened": [
                                   "Local\\\\{159989F5-EED2-E258-7F7B-44xxxxxxxxxx}"
                               ],
                               "modules_loaded": [
                                   "ADVAPI32.dll"
                               ],
                               "analysis_date": 1593005327,
                               "sandbox_name": "VirusTotal Jujubox",
                               "has_html_report": true,
                               "behash": "891a0af66a031b044dce08xxxxxxxxxx",
                               "has_evtx": false,
                               "text_highlighted": [
                                   "C:\\\\Windows\\\\system32\\\\cmd.exe"
                               ],
                               "last_modification_date": 1593005327,
                               "has_memdump": false,
                               "mutexes_created": [
                                   "Global\\\\{5995CC4B-E3B3-EBC8-9F85-4Bxxxxxxxxxx}"
                               ],
                               "has_pcap": true,
                               "files_opened": [
                                   "C:\\\\Windows\\\\system32\\\\SXS.DLL"
                               ]
                           },
                           "type": "file_behaviour",
                           "id": "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1xxxxxxxxxx_VirusTotal Jujubox",
                           "links": {
                               "self": "https://www.virustotal.com/api/v3/file_behaviours/8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1xxxxxxxxxx_VirusTotal Jujubox"
                           }
                       }
                   }
               }
           }
       ],
       "is_risky": true
    }
    

The following example shows the JSON result output for Vulnerabilities received when using the **Enrich Entities** action:
    
    
    {
       "Entity": "CVE-2024-49138",
       "EntityResult": {
           "targeted_regions": [],
           "cwe": {
               "title": "Heap-based Buffer Overflow",
               "id": "CWE-122"
           },
           "exploitation_consequence": "Privilege Escalation",
           "source_regions_hierarchy": [],
           "name": "CVE-2024-49138",
           "cisa_known_exploited": {
               "ransomware_use": "Unknown",
               "added_date": 1733788800,
               "due_date": 1735603200
           },
           "analysis": "\n\nOn Dec. 10, 2024, Microsoft stated exploitation of this vulnerability was detected in the wild. For more information, please see [Microsoft's advisory.](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-49138)\n\n",
           "workarounds": [],
           "last_modification_date": 1738271466,
           "description": "Windows Common Log File System Driver Elevation of Privilege Vulnerability",
           "sources": [
               {
                   "title": null,
                   "name": "Cybersecurity and Infrastructure Security Agency (CISA)",
                   "source_description": null,
                   "unique_id": null,
                   "url": "https://github.com/cisagov/vulnrichment/blob/develop/2024/49xxx/CVE-2024-49138.json",
                   "md5": "d6f2c868480ebbdb413eb2d57524b324",
                   "cvss": {
                       "cvssv2_0": null,
                       "cvssv3_x": {
                           "base_score": 7.8,
                           "temporal_score": null,
                           "vector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C"
                       },
                       "cvssv3_x_translated": null,
                       "cvssv4_x": null
                   },
                   "published_date": 1733852988
               },
               {
                   "title": "Microsoft Windows Common Log File System (CLFS) Driver Heap-Based Buffer Overflow Vulnerability",
                   "name": "CISA",
                   "source_description": "CISA's Known Exploited Vulnerabilities Catalog",
                   "unique_id": null,
                   "url": "https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
                   "md5": null,
                   "cvss": {
                       "cvssv2_0": null,
                       "cvssv3_x": null,
                       "cvssv3_x_translated": null,
                       "cvssv4_x": null
                   },
                   "published_date": 1733788800
               }
           ],
           "mitigations": [],
           "cve_id": "CVE-2024-49138",
           "creation_date": 1733853672,
           "detection_names": [],
           "risk_factors": [
               "Local Access Required",
               "User Permissions Required"
           ],
           "alt_names": [],
           "exploit_availability": "Publicly Available",
           "cpes": [
               {
                   "end_rel": "<",
                   "start_rel": null,
                   "start_cpe": null,
                   "end_cpe": {
                       "version": "10.0.10240.20857 x64",
                       "product": "Windows 10 1507",
                       "vendor": "Microsoft",
                       "uri": "cpe:2.3:o:microsoft:windows_10_1507:10.0.10240.20857:*:*:*:*:*:x64:*"
                   }
               }
           {
                   "end_rel": "<",
                   "start_rel": ">=",
                   "start_cpe": {
                       "version": "10.0.0",
                       "product": "Windows Server 2022",
                       "vendor": "Microsoft",
                       "uri": "cpe:2.3:o:microsoft:windows_server_2022:10.0.0:*:*:*:*:*:*:*"
                   },
                   "end_cpe": {
                       "version": "10.0.20348.2908",
                       "product": "Windows Server 2022",
                       "vendor": "Microsoft",
                       "uri": "cpe:2.3:o:microsoft:windows_server_2022:10.0.20348.2908:*:*:*:*:*:*:*"
                   }
               }
           ],
           "available_mitigation": [
               "Patch"
           ],
           "malware_roles": [],
           "counters": {
               "files": 1,
               "domains": 0,
               "ip_addresses": 0,
               "urls": 0,
               "iocs": 1,
               "subscribers": 1,
               "attack_techniques": 0
           },
           "collection_links": [],
           "domains_count": 0,
           "priority": "P0",
           "files_count": 1,
           "urls_count": 0,
           "alt_names_details": [],
           "affected_systems": [],
           "operating_systems": [],
           "first_seen_details": [],
           "targeted_informations": [],
           "recent_activity_summary": [
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0,
               0
           ],
           "merged_actors": [],
           "date_of_disclosure": 1733788800,
           "tags": [
               "media_attention",
               "observed_in_the_wild",
               "has_exploits",
               "was_zero_day"
           ],
           "last_seen_details": [],
           "epss": {
               "percentile": 0.25741,
               "score": 0.00054
           },
           "ip_addresses_count": 0,
           "autogenerated_tags": [],
           "private": true,
           "executive_summary": "\n\n* A Heap-based Buffer Overflow vulnerability exists that, when exploited, allows a local, privileged attacker to escalate privileges.\n* This vulnerability has been confirmed to be exploited in the wild. Weaponized code is publicly available.\n* Mandiant Intelligence considers this a Medium-risk vulnerability due to the potential for privilege escalation, offset by local access requirements and user permission requirements.\n* Mitigation options include a patch.\n",
           "summary_stats": {},
           "threat_scape": [],
           "exploitation_state": "Confirmed",
           "version_history": [
               {
                   "version_notes": [
                       "priority: Added"
                   ],
                   "date": 1739529103
               }
           ],
           "origin": "Google Threat Intelligence",
           "references_count": 0,
           "capabilities": [],
           "targeted_industries": [],
           "motivations": [],
           "predicted_risk_rating": "MEDIUM",
           "cvss": {
               "cvssv3_x": {
                   "base_score": 7.8,
                   "temporal_score": 6.8,
                   "vector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C"
               }
           },
           "mve_id": "MVE-2024-33694",
           "status": "COMPUTED",
           "exploitation_vectors": [
               "Unspecified Local Vector"
           ],
           "risk_rating": "MEDIUM",
           "tags_details": [
               {
                   "last_seen": null,
                   "description": null,
                   "value": "was_zero_day",
                   "confidence": "possible",
                   "first_seen": null
               }
           ],
           "mati_genids_dict": {
               "cve_id": "vulnerability--012f19f2-00d0-58c8-b981-8b6ce04a8f43",
               "mve_id": "vulnerability--c5ef5265-21d1-57ac-b960-5bf56f37d63f",
               "report_id": null
           },
           "technologies": [],
           "exploitation": {
               "exploit_release_date": 1736899200,
               "first_exploitation": 1733788800,
               "tech_details_release_date": null
           },
           "targeted_industries_tree": [],
           "subscribers_count": 1,
           "intended_effects": [],
           "collection_type": "vulnerability",
           "field_sources": [
               {
                   "field": "cvss.cvssv3_x",
                   "source": {
                       "sources": [],
                       "source_url": "",
                       "source_name": "Cybersecurity and Infrastructure Security Agency (CISA)",
                       "field_type": "Ranked"
                   }
               },
               {
                   "field": "exploitation_state",
                   "source": {
                       "sources": [],
                       "source_url": "",
                       "source_name": "Microsoft Corp.",
                       "field_type": "Severity"
                   }
               }
           ],
           "vendor_fix_references": [
               {
                   "title": "Windows Common Log File System Driver Elevation of Privilege Vulnerability",
                   "name": "Microsoft Corp.",
                   "source_description": null,
                   "unique_id": null,
                   "url": "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-49138",
                   "md5": null,
                   "cvss": null,
                   "published_date": 1733817600
               }
           ],
           "targeted_regions_hierarchy": [],
           "top_icon_md5": [],
           "aggregations": {}
       }
    }
    

The following example shows the JSON result output for Threat Actors received when using the **Enrich Entities** action:
    
    
    {
       "Entity": "APT42",
       "EntityResult": {
    "threat_actor_id": "123123"
           "affected_systems": [],
           "targeted_regions_hierarchy": [
               {
                   "region": "Oceania",
                   "sub_region": "Australia and New Zealand",
                   "country": "Australia",
                   "country_iso2": "AU",
                   "confidence": "confirmed",
                   "first_seen": 1630467976,
                   "last_seen": 1630467976,
                   "description": null,
                   "source": null
               },
               {
                   "region": "Europe",
                   "sub_region": "Western Europe",
                   "country": "Austria",
                   "country_iso2": "AT",
                   "confidence": "confirmed",
                   "first_seen": 1630467976,
                   "last_seen": 1705487116,
                   "description": null,
                   "source": null
               }
           ],
           "recent_activity_relative_change": -0.6340275969799531,
           "subscribers_count": 30,
           "version_history": [],
           "field_sources": [],
           "detection_names": [],
           "references_count": 82,
           "files_count": 1182,
           "workarounds": [],
           "threat_scape": [],
           "alt_names_details": [
               {
                   "description": null,
                   "first_seen": null,
                   "last_seen": null,
                   "confidence": "confirmed",
                   "value": "APT35 (Avertium)"
               },
               {
                   "description": null,
                   "first_seen": null,
                   "last_seen": null,
                   "confidence": "confirmed",
                   "value": "APT35 (Check Point)"
               }
           ],
           "description": "APT42 is an Iranian state-sponsored cyber espionage group tasked with conducting information collection and surveillance operations against individuals and organizations of strategic interest to the Iranian Government. The group's operations, which are designed to build trust and rapport with their victims, have included accessing the personal and corporate email accounts of government officials, former Iranian policymakers or political figures, members of the Iranian diaspora and opposition groups, journalists, and academics who are involved in research on Iran. The group has also deployed mobile malware capable of tracking victim locations, recording phone conversations, accessing videos and images, and extracting entire SMS inboxes.",
           "creation_date": 1428278400,
           "tags": [],
           "private": true,
           "available_mitigation": [],
           "name": "APT42",
           "origin": "Google Threat Intelligence",
           "mitigations": [],
           "merged_actors": [
               {
                   "description": "threat-actor--a5ccf0a6-79ab-57cc-98b3-f8ee2e123071",
                   "first_seen": 1691519658,
                   "last_seen": 1691519658,
                   "confidence": "confirmed",
                   "value": "UNC4391"
               },
               {
                   "description": "threat-actor--20ea26fa-d7ef-51c1-905f-28a2982a0bb5",
                   "first_seen": 1659365630,
                   "last_seen": 1659365630,
                   "confidence": "confirmed",
                   "value": "UNC788"
               },
               {
                   "description": "threat-actor--f3e232d1-dfea-55f5-b1f0-e8e09c035ee2",
                   "first_seen": 1704210115,
                   "last_seen": 1704210115,
                   "confidence": "confirmed",
                   "value": "UNC4980"
               },
               {
                   "description": "threat-actor--c7672fb1-f752-54fd-853e-5cbd49dc8187",
                   "first_seen": 1670883116,
                   "last_seen": 1670883116,
                   "confidence": "confirmed",
                   "value": "UNC4248"
               },
               {
                   "description": "threat-actor--e5f884bd-cb76-5bed-a351-7984d6023b4a",
                   "first_seen": 1682448032,
                   "last_seen": 1682448032,
                   "confidence": "confirmed",
                   "value": "UNC4689"
               },
               {
                   "description": "threat-actor--a28ebf5f-a384-55c0-a544-c5e4df56b136",
                   "first_seen": 1693336040,
                   "last_seen": 1693336040,
                   "confidence": "confirmed",
                   "value": "UNC4423"
               },
               {
                   "description": "threat-actor--feb78504-3e56-5217-ad21-7dc9dab8974b",
                   "first_seen": 1708987865,
                   "last_seen": 1708987865,
                   "confidence": "confirmed",
                   "value": "UNC2440"
               },
               {
                   "description": "threat-actor--d0f848d6-d92f-5147-9bf8-a3b5e93092ff",
                   "first_seen": 1605743032,
                   "last_seen": 1605743032,
                   "confidence": "confirmed",
                   "value": "UNC2013"
               },
               {
                   "description": "threat-actor--284c29d0-575d-5410-a7f2-dab16e2a5863",
                   "first_seen": 1605139211,
                   "last_seen": 1605139211,
                   "confidence": "confirmed",
                   "value": "UNC1896"
               },
               {
                   "description": "threat-actor--8d09d09c-6a09-56b5-86ad-c76f3a006d24",
                   "first_seen": 1605744560,
                   "last_seen": 1605744560,
                   "confidence": "confirmed",
                   "value": "UNC1137"
               },
               {
                   "description": "threat-actor--9d0ac442-9a26-54d7-9061-af1ff9080071",
                   "first_seen": 1605744040,
                   "last_seen": 1605744040,
                   "confidence": "confirmed",
                   "value": "UNC978"
               },
               {
                   "description": "threat-actor--1aa4e976-a6d0-57b8-861a-478d767f10f5",
                   "first_seen": 1605137808,
                   "last_seen": 1605137808,
                   "confidence": "confirmed",
                   "value": "UNC1900"
               },
               {
                   "description": "threat-actor--237842b5-7aa3-5674-8c06-257d0f38c4d6",
                   "first_seen": 1605136271,
                   "last_seen": 1605136271,
                   "confidence": "confirmed",
                   "value": "UNC2086"
               },
               {
                   "description": "threat-actor--bfdfb34f-5dea-5864-b80d-02b9cfeeb6d2",
                   "first_seen": 1605128797,
                   "last_seen": 1605128797,
                   "confidence": "confirmed",
                   "value": "UNC2087"
               },
               {
                   "description": "threat-actor--cf4e7cfa-2707-5a4a-a543-ef32cd4f5d66",
                   "first_seen": 1692622313,
                   "last_seen": 1692622313,
                   "confidence": "confirmed",
                   "value": "UNC4439"
               },
               {
                   "description": "threat-actor--60cccdf6-fad7-5706-92df-35aa6111923d",
                   "first_seen": 1728393601,
                   "last_seen": 1728393601,
                   "confidence": "confirmed",
                   "value": "UNC5246"
               }
           ],
           "intended_effects": [],
           "urls_count": 2617,
           "targeted_industries_tree": [
               {
                   "industry_group": "Chemicals & Materials",
                   "industry": null,
                   "confidence": "confirmed",
                   "first_seen": 1665304135,
                   "last_seen": 1683023019,
                   "description": null,
                   "source": null
               }
           ],
           "alt_names": [
               "APT35 (Google)",
               "Charmingcypress (Volexity)",
               "Voidbalaur (Trend Micro)",
               "Yellow Garuda (PwC)",
               "GreenCharlie (Recorded Future)",
               "Cobalt Illusion (Dell SecureWorks)",
               "UNC788 (Facebook)",
               "Charmingkitten (Kaspersky)",
               "Charming Kitten (Certfa)",
               "APT35 (Avertium)",
               "Charming Kitten (CrowdStrike)",
               "TA453 (Proofpoint)",
               "Charming Kitten (ClearSky)",
               "Charmingkitten (Bitdefender)",
               "TAG-56 (Recorded Future)",
               "ITG18 (IBM)",
               "Charmingkitten (Volexity)",
               "Phosphorus (Check Point)",
               "APT35 (Check Point)",
               "CALANQUE (Google TAG)",
               "Mint Sandstorm (Microsoft)"
           ],
           "first_seen": 1428278400,
           "counters": {
               "files": 1182,
               "domains": 3888,
               "ip_addresses": 1670,
               "urls": 2617,
               "iocs": 9357,
               "subscribers": 30,
               "attack_techniques": 127
           },
           "collection_type": "threat-actor",
           "motivations": [
               {
                   "description": null,
                   "first_seen": null,
                   "last_seen": null,
                   "confidence": "confirmed",
                   "value": "Espionage"
               },
               {
                   "description": null,
                   "first_seen": null,
                   "last_seen": null,
                   "confidence": "confirmed",
                   "value": "Surveillance"
               }
           ],
           "collection_links": [],
           "targeted_regions": [
               "GB",
               "BE",
               "AT",
               "IL",
               "LB",
               "UA",
               "EG",
               "AU",
               "AZ",
               "IT",
               "US",
               "IR",
               "BG",
               "TR",
               "AE",
               "NO",
               "MY"
           ],
           "source_regions_hierarchy": [
               {
                   "region": "Asia",
                   "sub_region": "Southern Asia",
                   "country": "Iran, Islamic Republic Of",
                   "country_iso2": "IR",
                   "confidence": "confirmed",
                   "first_seen": null,
                   "last_seen": null,
                   "description": null,
                   "source": null
               }
           ],
           "malware_roles": [],
           "last_seen_details": [
               {
                   "description": null,
                   "first_seen": null,
                   "last_seen": null,
                   "confidence": "confirmed",
                   "value": "2025-03-05T17:55:03.551Z"
               }
           ],
           "domains_count": 3888,
           "operating_systems": [],
           "source_region": "IR",
           "targeted_informations": [],
           "risk_factors": [],
           "tags_details": [],
           "ip_addresses_count": 1670,
           "capabilities": [],
           "targeted_industries": [],
           "vulnerable_products": "",
           "technologies": [],
           "recent_activity_summary": [
               1341,
               1083,
               839,
               656,
               852,
               1136,
               1693,
               1485,
               1304,
               767,
               893,
               772,
               1169,
               67
           ],
           "vendor_fix_references": [],
           "last_seen": 1741197303,
           "autogenerated_tags": [
               "upx",
               "cve-2004-0790",
               "contains-elf",
               "downloads-zip",
               "cve-2021-26084",
               "cve-1999-0016",
               "cve-2018-10561",
               "cve-2021-44228",
               "downloads-elf",
               "contains-embedded-js",
               "cve-2005-0068",
               "base64-embedded",
               "bobsoft",
               "cve-2022-30190",
               "opendir",
               "attachment",
               "cve-2014-3931",
               "cve-2020-7961",
               "contains-pe",
               "cve-2021-1675",
               "downloads-pe",
               "downloads-doc",
               "cve-2017-0199",
               "themida"
           ],
           "exploitation_vectors": [],
           "first_seen_details": [
               {
                   "description": null,
                   "first_seen": null,
                   "last_seen": null,
                   "confidence": "confirmed",
                   "value": "2015-04-06T00:00:00Z"
               }
           ],
           "last_modification_date": 1741314287,
           "summary_stats": {
               "first_submission_date": {
                   "min": 1234800101.0,
                   "max": 1741187401.0,
                   "avg": 1689528709.5449305
               },
               "last_submission_date": {
                   "min": 1366635040.0,
                   "max": 1741328711.0,
                   "avg": 1714984562.318413
               },
               "files_detections": {
                   "min": 0.0,
                   "max": 70.0,
                   "avg": 26.672566371681413
               },
               "urls_detections": {
                   "min": 0.0,
                   "max": 19.0,
                   "avg": 7.352873563218389
               }
           },
           "status": "COMPUTED",
           "top_icon_md5": [
               "b8fabacf5f0ce868656ac7a1d38c7c99",
               "4aa5f091c9e667deb2123284461493e7",
               "03234c84e6474d7cc9ecf39b9812fac4"
           ]
       }
    }
    

##### Output messages

The **Enrich Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following entities using Google Threat Intelligence: ENTITY_ID ` `The action wasn't able to enrich the following entities using Google Threat Intelligence: ENTITY_ID` `The action didn't enrich any of the provided entities.` | The action succeeded.  
`Error executing action "Enrich Entities". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Entities** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enrich IOCs

Use the **Enrich IOCs** action to enrich the indicators of compromise (IoCs) using information from Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Enrich IOCs** action requires the following parameters:

Parameter | Description  
---|---  
`IOC Type` | Optional. The type of the IOC to enrich. The possible values are as follows:

  * `Filehash`
  * `URL`
  * `Domain`
  * `IP Address`

The default value is `Filehash`.  
`IOCs` | Required. A comma-separated list of IOCs to ingest data.  
`Widget Theme` | Optional. The visual style applied to the IOC augmented widget. The possible values are as follows:

  * `Dark`
  * `Dark Blue`
  * `Light`

The default value is `Dark Blue`.  
  
#### Action outputs

The **Enrich IOCs** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Enrich IOCs** action can provide the following link for every enriched entity:

Name: **Report Link**

Value: URL

##### Case wall table

The **Enrich IOCs** action can provide the following table for every enriched entity:

Table name: **IOC_ID**

Table columns:

  * **Name**
  * **Category**
  * **Method**
  * **Result**



##### JSON result

The following example shows the JSON result output received when using the **Enrich IOCs** action:
    
    
    {
        "ioc": {
            "identifier": "203.0.113.1",
            "details": {
                "attributes": {
                    "categories": {
                        "Dr.Web": "known infection source/not recommended site",
                        "Forcepoint ThreatSeeker": "compromised websites",
                        "sophos": "malware repository, spyware and malware"
                    },
                    "first_submission_date": 1582300443,
                    "html_meta": {},
                    "last_analysis_date": 1599853405,
                    "last_analysis_results": {
                        "EXAMPLELabs": {
                            "category": "harmless",
                            "engine_name": "EXAMPLELabs",
                            "method": "blacklist",
                            "result": "clean"
                        },
                        "Example": {
                            "category": "harmless",
                            "engine_name": "Example",
                            "method": "blacklist",
                            "result": "clean"
                        }
                    },
                    "last_analysis_stats": {
                        "harmless": 64,
                        "malicious": 6,
                        "suspicious": 1,
                        "timeout": 0,
                        "undetected": 8
                    },
                    "last_final_url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event",
                    "last_http_response_code": 404,
                    "last_http_response_content_length": 204,
                    "last_http_response_content_sha256": "58df637d178e35690516bda9e41e245db836170f046041fdebeedd20eca61d9d",
                    "last_http_response_headers": {
                        "connection": "keep-alive",
                        "content-length": "204",
                        "content-type": "text/html; charset=iso-8859-1",
                        "date": "Fri, 11 Sep 2020 19:51:50 GMT",
                        "keep-alive": "timeout=60",
                        "server": "nginx"
                    },
                    "last_modification_date": 1599853921,
                    "last_submission_date": 1599853405,
                    "reputation": 0,
                    "tags": [
                        "ip"
                    ],
                    "targeted_brand": {},
                    "threat_names": [
                        "Mal/HTMLGen-A"
                    ],
                    "times_submitted": 3,
                    "title": "404 Not Found",
                    "total_votes": {
                        "harmless": 0,
                        "malicious": 0
                    },
                    "trackers": {},
                    "url": "http://203.0.113.1/input/?mark=20200207-example.com/31mawe&tpl=example&engkey=bar+chart+click+event"
                },
                "id": "ID",
                "links": {
                    "self": "https://www.virustotal.com/api/v3/urls/ID"
                },
                "type": "url",
            "report_link": "{generated report link}",
                "widget_url": "https: //www.virustotal.com/ui/widget/html/WIDGET_ID"
    "widget_html"
            }
        }
    }
    

##### Output messages

The **Enrich IOCs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following IOCs using Google Threat Intelligence: IOC_LIST` `No information found for the following IOCs using Google Threat Intelligence: IOC_LIST` `No information about IOCs was found.` | The action succeeded.  
`Error executing action "Enrich IOC". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich IOCs** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Execute IOC Search

Use the **Execute IOC Search** action to run the IOC search in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Execute IOC Search** action requires the following parameters:

Parameter | Description  
---|---  
`Search Query` | Required.A search query to run, such as `crowdsourced_yara_rule:*apt* and p:3+ and fs:2d+`.  
`Max Results To Return` | Optional.The maximum number of results to return for every action run.The maximum value is `200`.The default value is `50`.  
  
#### Action outputs

The **Execute IOC Search** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Execute IOC Search** action:
    
    
    {
        "attributes":{
          "type_description":"Android",
          "tlsh":"T156B6128BF7885D2BC0B78136899A1136B76A8D254B43A3473548772C3EB32D44F6DBD8",
          "vhash":"8d145b883d0a7f814ba5b130454fbf36",
          "exiftool":{
            "ZipRequiredVersion":"20",
            "MIMEType":"application/zip",
            "ZipCRC":"0xf27716ce",
            "FileType":"ZIP",
            "ZipCompression":"Deflated",
            "ZipUncompressedSize":"46952",
            "ZipCompressedSize":"8913",
            "FileTypeExtension":"zip",
            "ZipFileName":"Example.xml",
            "ZipBitFlag":"0x0800",
            "ZipModifyDate":"2023:06:11 17:54:18"
          },
          "type_tags":[
            "executable",
            "mobile",
            "android",
            "apk"
          ],
          "crowdsourced_yara_results":["RESULTS_OMITTED"]
          "magic":"Zip archive data, at least v1.0 to extract, compression method=store",
          "permhash":"a3e0005ad57d3ff03e09e0d055ad10bcf28a58a04a8c2aeccdad2b9e9bc52434",
          "meaningful_name":"Example",
          "reputation":0
        },
        "type":"file",
        "id":"FILE_ID",
        "links":{
          "self":"https://www.virustotal.com/api/v3/files/FILE_ID"
        }
    }
    

##### Output messages

The **Execute IOC Search** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found results for the provided query in Google Threat Intelligence.` `No results were found for the provided query in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Execute IOC Search". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute IOC Search** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get ASM Entity Details

Use the **Get ASM Entity Details** action to obtain information about an ASM entity in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get ASM Entity Details** action requires the following parameters:

Parameter | Description  
---|---  
`Entity ID` | Required.A comma-separated list of entity IDs to obtain details.  
  
#### Action outputs

The **Get ASM Entity Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get ASM Entity Details** action:
    
    
    {
     "uuid": "UUID",
     "dynamic_id": "Intrigue::Entity::Uri#http://192.0.2.73:80",
     "collection_name": "example_oum28bu",
     "alias_group": 8515,
     "aliases": [
       "http://192.0.2.73:80"
     ],
     "allow_list": false,
     "ancestors": [
       {
         "type": "Intrigue::Entity::NetBlock",
         "name": "192.0.2.0/24"
       }
     ],
     "category": null,
     "collection_naics": null,
     "confidence": null,
     "deleted": false,
     "deny_list": false,
     "details":
       <! CONTENT OMITTED >
       "http": {
         "code": 404,
         "title": "404 Not Found",
         "content": {
           "favicon_hash": null,
           "hash": null,
           "forms": false
         },
         "auth": {
           "any": false,
           "basic": false,
           "ntlm": false,
           "forms": false,
           "2fa": false
         }
       },
       "ports": {
         "tcp": [
           80
         ],
         "udp": [],
         "count": 1
       },
       "network": {
         "name": "Example, Inc.",
         "asn": 16509,
         "route": null,
         "type": null
       },
       "technology": {
         "cloud": true,
         "cloud_providers": [
           "Example Services"
         ],
         "cpes": [],
         "technologies": [],
         "technology_labels": []
       },
       "vulns": {
         "current_count": 0,
         "vulns": []
       }
     },
     {
     "tags": [],
     "id": 8620,
     "scoped_at": "2022-09-30 06:51:57 +0000",
     "detail_string": "Fingerprint: Nginx |  Title: 404 Not Found",
     "enrichment_tasks": [
       "enrich/uri",
       "sslcan"
     ],
     "generated_at": "2022-09-30T21:21:18Z"
    }
    

##### Output messages

The **Get ASM Entity Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details for the following entities using information from Google Threat Intelligence: ENTITY_ID` `The action wasn't able to return details for the following entities using information from Google Threat Intelligence: ENTITY_ID` | The action succeeded.  
`Error executing action "Get ASM Entity Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get ASM Entity Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Graph Details

Use the **Get Graph Details** action to obtain detailed information about graphs in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Graph Details** action requires the following parameters:

Parameter | Description  
---|---  
`Graph ID` | Required. A comma-separated list of graph IDs to retrieve details.  
`Max Links To Return` | Required. The maximum number of links to return for each graph. The default value is `50`.  
  
#### Action outputs

The **Get Graph Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Graph Details** action can provide the following table for every enriched entity:

Table name: **Graph GRAPH_ID Links**

Table columns:

  * **Source**
  * **Target**
  * **Connection Type**



##### JSON result

The following example shows the JSON result output received when using the **Get Graph Details** action:
    
    
    {
        "data": {
            "attributes": {
                "comments_count": 0,
                "creation_date": 1603219837,
                "graph_data": {
                    "description": "Example LLC",
                    "version": "api-5.0.0"
                },
                "last_modified_date": 1603219837,
                "links": [
                    {
                        "connection_type": "last_serving_ip_address",
                        "source": "ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "target": "relationships_last_serving_ip_address_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671"
                    },
                    {
                        "connection_type": "last_serving_ip_address",
                        "source": "relationships_last_serving_ip_address_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "target": "203.0.113.3"
                    },
                    {
                        "connection_type": "network_location",
                        "source": "ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "target": "relationships_network_location_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671"
                    },
                    {
                        "connection_type": "network_location",
                        "source": "relationships_network_location_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "target": "203.0.113.3"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "203.0.113.3",
                        "target": "relationships_communicating_files_20301133"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "4935cc8a4ff76d595e1bfab9fd2e6aa0f7c2fea941693f1ab4586eaba1528f47"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "c975794ff65c02b63fae1a94006a75294aac13277ca464e3ea7e40de5eda2b14"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "c7752154a2e894a4dec84833bee656357f4b84a9c7f601f586f79de667d8fe5c"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "692bb2ed1da43b0408c104b4ca4b4e97e15f3224e37dbea60214bcd991a2cfd3"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "74273ef55d8b7d23f7b058c7e47f3cbaf60c823a3e41ffb10e494917bad77381"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "f4f2f17c4df1b558cb80c8eab3edf5198970e9d87bd03943d4c2effafb696187"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "5edc8496869697aa229540bd6106b6679f6cfcbc6ee4837887183f470b49acb5"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "1582da57cb082d3f6835158133aafb5f3b8dcc880a813be135a0ff8099cf0ee8"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "be4ccb1ca71a987f481c22a1a43de491353945d815c89cbcc06233d993ac73cf"
                    },
                    {
                        "connection_type": "communicating_files",
                        "source": "relationships_communicating_files_20301133",
                        "target": "60bb6467ee465f23a15f17cd73f7ecb9db9894c5a3186081a1c70fdc6e7607d6"
                    }
                ],
                "nodes": [
                    {
                        "entity_attributes": {
                            "has_detections": false
                        },
                        "entity_id": "ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "index": 0,
                        "text": "",
                        "type": "url",
                        "x": 51.22276722115952,
                        "y": 65.7811310194184
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_last_serving_ip_address_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "index": 1,
                        "text": "",
                        "type": "relationship",
                        "x": 25.415664700492094,
                        "y": 37.66636498768037
                    },
                    {
                        "entity_attributes": {
                            "country": "US"
                        },
                        "entity_id": "203.0.113.3",
                        "fx": -19.03611541222395,
                        "fy": 24.958500220062717,
                        "index": 2,
                        "text": "",
                        "type": "ip_address",
                        "x": -19.03611541222395,
                        "y": 24.958500220062717
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_network_location_ea241b193c1bd89f999db9231359e7479bc2f05105ce43964955068c5d7c4671",
                        "index": 3,
                        "text": "",
                        "type": "relationship",
                        "x": 14.37403861978968,
                        "y": 56.85562691824892
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_communicating_files_20301133",
                        "index": 4,
                        "text": "",
                        "type": "relationship",
                        "x": -51.78097726144755,
                        "y": 10.087893225996158
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "peexe"
                        },
                        "entity_id": "4935cc8a4ff76d595e1bfab9fd2e6aa0f7c2fea941693f1ab4586eaba1528f47",
                        "index": 5,
                        "text": "",
                        "type": "file",
                        "x": -79.11606194776019,
                        "y": -18.475026322309112
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "peexe"
                        },
                        "entity_id": "c975794ff65c02b63fae1a94006a75294aac13277ca464e3ea7e40de5eda2b14",
                        "index": 6,
                        "text": "",
                        "type": "file",
                        "x": -64.80938048199627,
                        "y": 46.75892061191275
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "c7752154a2e894a4dec84833bee656357f4b84a9c7f601f586f79de667d8fe5c",
                        "index": 7,
                        "text": "",
                        "type": "file",
                        "x": -43.54064004476819,
                        "y": -28.547923020662786
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "692bb2ed1da43b0408c104b4ca4b4e97e15f3224e37dbea60214bcd991a2cfd3",
                        "index": 8,
                        "text": "",
                        "type": "file",
                        "x": -15.529860440278318,
                        "y": -2.068209789825876
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "74273ef55d8b7d23f7b058c7e47f3cbaf60c823a3e41ffb10e494917bad77381",
                        "index": 9,
                        "text": "",
                        "type": "file",
                        "x": -42.55971948293377,
                        "y": 46.937155845680415
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "html"
                        },
                        "entity_id": "f4f2f17c4df1b558cb80c8eab3edf5198970e9d87bd03943d4c2effafb696187",
                        "index": 10,
                        "text": "",
                        "type": "file",
                        "x": -62.447976875107706,
                        "y": -28.172418384729067
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "5edc8496869697aa229540bd6106b6679f6cfcbc6ee4837887183f470b49acb5",
                        "index": 11,
                        "text": "",
                        "type": "file",
                        "x": -89.0326649183805,
                        "y": -2.2638551448322484
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "1582da57cb082d3f6835158133aafb5f3b8dcc880a813be135a0ff8099cf0ee8",
                        "index": 12,
                        "text": "",
                        "type": "file",
                        "x": -26.35260716195174,
                        "y": -20.25669077264115
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "be4ccb1ca71a987f481c22a1a43de491353945d815c89cbcc06233d993ac73cf",
                        "index": 13,
                        "text": "",
                        "type": "file",
                        "x": -82.1415994911387,
                        "y": 34.89636762607467
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "android"
                        },
                        "entity_id": "ENTITY_ID",
                        "index": 14,
                        "text": "",
                        "type": "file",
                        "x": -90.87738694680043,
                        "y": 16.374462198116138
                    }
                ],
                "private": false,
                "views_count": 30
            },
            "id": "ID",
            "links": {
                "self": "https://www.virustotal.com/api/v3/graphs/ID"
            },
            "type": "graph"
        }
    }
    

##### Output messages

The **Get Graph Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about the following graphs in Google Threat Intelligence: GRAPH_IDS` `Action wasn't able to return details about the following graphs in Google Threat Intelligence: GRAPH_IDS` `No information about the provided graphs was found.` | The action succeeded.  
`Error executing action "Get Graph Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Graph Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Related Associations

Use the **Get Related Associations** action to get information about associations (reports, campaigns, collections, malware families, software toolkits, vulnerabilities, threat actors) related to entities in Google Threat Intelligence.

This action runs on the following Google SecOps entities:

  * `IP address`
  * `URL`
  * `File hash`
  * `Hostname`
  * `Domain`

**Note:** This action only supports MD5, SHA-1, and SHA-256 hashes.

#### Action inputs

The **Get Related Associations** action requires the following parameters:

Parameter | Description  
---|---  
`Association Types` | Optional. A comma-separated list of associations to return. Reports are processed after all other associations are complete. The possible values are as follows:

  * `Report`
  * `Campaign`
  * `Collection`
  * `Malware Family`
  * `Vulnerability`
  * `Threat Actor`

If no value is provided, the action returns all associations.  
`Create Entity` | Optional. If selected, the action creates an entity for related Threat Actors, Common Vulnerabilities and Exposures (CVEs), and Campaigns, linking it to the original entity. Only CVE, Threat Actor, and Campaign entities are created.  
`Max Associations To Return` | Optional. The maximum number of IoCs to return for every entity. The maximum value is `100`. The default value is `50`.  
  
#### Action outputs

The **Get Related Associations** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result. | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Related Associations** action:
    
    
    {
       "Entity": "",
       "EntityResult": 
           {
               "campaign": [
                   {
                       "id": "campaign--a1b2c3d4-e5f6-7g8h-9i0j-1k2l3m4n5o6p",
                       "type": "collection",
                       "links": {
                           "self": "https://www.virustotal.com/api/v3/collections/campaign--a1b2c3d4-e5f6-7g8h-9i0j-1k2l3m4n5o6p"
                       },
                       "attributes": {
                           "alt_names": [
                               "CAMPAIGN.ID.001"
                           ],
                           "alt_names_details": [
                               {
                                   "description": null,
                                   "last_seen": null,
                                   "value": "CAMPAIGN.ID.001",
                                   "first_seen": null,
                                   "confidence": "confirmed"
                               }
                           ],
                           "recent_activity_relative_change": 0.12215909090909083,
                           "description": "Security Research Team (SRT) has obtained intelligence surrounding an ongoing campaign involving the deployment of a Custom Infostealer followed by local reconnaissance and data exfiltration.\n\nBased on available intelligence, targeted organizations have been located in Western European countries, primarily within the Consulting and Manufacturing sectors; however, targeting appears opportunistic due to deployment methods. The campaign is being conducted by a threat actor SRT tracks as UNC9999 and assesses with high confidence to have financial motivations.",
                           "version_history": [],
                           "targeted_regions": [
                               "WE",
                               "NE"
                           ],
                           "private": true,
                           "subscribers_count": 0,
                           "last_seen": 1751241600,
                           "files_count": 2,
                           "first_seen_details": [
                               {
                                   "description": "Observed First Activity of Campaign",
                                   "last_seen": null,
                                   "value": "2024-10-09T00:00:00Z",
                                   "first_seen": null,
                                   "confidence": "unconfirmed"
                               }
                           ],
                           "detection_names": [],
                           "targeted_industries": [],
                           "technologies": [],
                           "source_regions_hierarchy": [],
                           "references_count": 5,
                           "domains_count": 70,
                           "name": "Financial Actor Campaign Involving Custom Stealer for Data Exfiltration",
                           "intended_effects": [],
                           "creation_date": 1751304756,
                           "malware_roles": [],
                           "available_mitigation": [],
                           "last_seen_details": [
                               {
                                   "description": null,
                                   "last_seen": null,
                                   "value": "2025-06-30T00:00:00Z",
                                   "first_seen": null,
                                   "confidence": "unconfirmed"
                               }
                           ],
                           "summary_stats": {
                               "first_submission_date": {
                                   "min": 1724454065.0,
                                   "max": 1750144019.0,
                                   "avg": 1736406949.275
                               },
                               "last_submission_date": {
                                   "min": 1724454065.0,
                                   "max": 1750312785.0,
                                   "avg": 1737423800.3916667
                               },
                               "files_detections": {
                                   "min": 23.0,
                                   "max": 23.0,
                                   "avg": 23.0
                               },
                               "urls_detections": {
                                   "min": 0.0,
                                   "max": 19.0,
                                   "avg": 3.9999999999999996
                               }
                           },
                           "is_content_translated": false,
                           "targeted_industries_tree": [
                               {
                                   "industry_group": "Consulting",
                                   "industry": null,
                                   "confidence": "confirmed",
                                   "first_seen": null,
                                   "last_seen": null,
                                   "description": null,
                                   "source": null
                               },
                               {
                                   "industry_group": "Legal Services",
                                   "industry": null,
                                   "confidence": "confirmed",
                                   "first_seen": null,
                                   "last_seen": null,
                                   "description": null,
                                   "source": null
                               },
                               {
                                   "industry_group": "Manufacturing & Logistics",
                                   "industry": null,
                                   "confidence": "confirmed",
                                   "first_seen": null,
                                   "last_seen": null,
                                   "description": null,
                                   "source": null
                               }
                           ],
                           "threat_scape": [],
                           "ip_addresses_count": 10,
                           "collection_links": [],
                           "targeted_informations": [],
                           "operating_systems": [],
                           "urls_count": 118,
                           "first_seen": 1728432000,
                           "status": "COMPUTED",
                           "collection_type": "campaign",
                           "campaign_type": "INDIVIDUAL",
                           "recent_activity_summary": [
                               70,
                               17,
                               29,
                               17,
                               24,
                               14,
                               15,
                               25,
                               23,
                               44,
                               37,
                               25,
                               19,
                               36
                           ],
                           "exploitation_vectors": [],
                           "mitigations": [],
                           "vendor_fix_references": [],
                           "risk_factors": [],
                           "field_sources": [],
                           "motivations": [
                               {
                                   "description": null,
                                   "last_seen": null,
                                   "value": "Monetary",
                                   "first_seen": null,
                                   "confidence": "confirmed"
                               }
                           ],
                           "tags": [],
                           "affected_systems": [],
                           "tags_details": [],
                           "top_icon_md5": [
                               "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d",
                               "6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a",
                               "3a4b5c6d1e2f3a4b5c6d1e2f3a4b5c6d"
                           ],
                           "counters": {
                               "files": 2,
                               "domains": 70,
                               "ip_addresses": 10,
                               "urls": 118,
                               "iocs": 200,
                               "subscribers": 0,
                               "attack_techniques": 22
                           },
                           "merged_actors": [],
                           "origin": "Security Research Team",
                           "capabilities": [],
                           "autogenerated_tags": [
                               "contains-sample-binary"
                           ],
                           "targeted_regions_hierarchy": [
                               {
                                   "region": "Europe",
                                   "sub_region": "Western Europe",
                                   "country": "Example Country 1",
                                   "country_iso2": "C1",
                                   "confidence": "confirmed",
                                   "first_seen": null,
                                   "last_seen": null,
                                   "description": null,
                                   "source": null
                               },
                               {
                                   "region": "Europe",
                                   "sub_region": "Northern Europe",
                                   "country": "Example Country 2",
                                   "country_iso2": "C2",
                                   "confidence": "confirmed",
                                   "first_seen": null,
                                   "last_seen": null,
                                   "description": null,
                                   "source": null
                               }
                           ],
                           "workarounds": [],
                           "last_modification_date": 1751406304
                       },
                       "context_attributes": {
                           "shared_with_me": false,
                           "role": "viewer"
                       }
                   }
               ]
           }
       
    }
    

##### Output messages

The **Get Related Associations** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found associations for the following entities in Google Threat Intelligence: ENTITY_ID.` `No related Associations were found for the following entities in Google Threat Intelligence: ENTITY_ID.` `No related associations were found for the provided entities in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Get Related Associations". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Related Associations** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Related IOCs

Use the **Get Related IOCs** action to get information about IOCs related to entities using information from Google Threat Intelligence.

This action only supports MD5, SHA-1, and SHA-256 hashes.

This action runs on the following Google SecOps entities:

  * `IP address`
  * `URL`
  * `Hostname`
  * `Domain`
  * `Hash`
  * `Threat Actor`



#### Action inputs

The **Get Related IOCs** action requires the following parameters:

Parameter | Description  
---|---  
`IOC Types` | Required.A comma-separated list of IOCs to extract.The possible values are as follows: `IP`, `Hash`, `URL`, `Domain`.  
`Max IOCs To Return` | Required.The maximum number of IOCs to return for selected IOC types for every entity.The default value is `40`.  
  
#### Action outputs

The **Get Related IOCs** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result. | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Related IOCs** action:
    
    
    {
       "Entity": "ENTITY",
       "EntityResult": {
           "hash": [
               "HASH"
           ],
           "url": [
               "URL"
           ],
           "domain": [
               "DOMAIN"
           ],
           "ip": [
               "IP_ADDRESS"
           ]
       }
    }
    

##### Output messages

The **Get Related IOCs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned related IOCs for the following entities in Google Threat Intelligence: ENTITY` `No related IOCs were found for the following entities in Google Threat Intelligence: ENTITY.` `No related IOCs were found for the provided entities.` | The action succeeded.  
`Error executing action "Get Related IOCs". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Related IOCs** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Google Threat Intelligence.

This action doesn't run on Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result. | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Google Threat Intelligence server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Google Threat Intelligence server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Private Submit URL

Use the **Private Submit URL** action to submit a URL for a private scan within Google Threat Intelligence.

This action runs on the following Google SecOps entity:

  * `URL`

**Note:** For a regular scan and entity enrichment, use the **Enrich Entities** action instead.

#### Action inputs

The **Private Submit URL** action requires the following parameters:

Parameter | Description  
---|---  
`URL` | Optional. A comma-separated list of URLs to scan. The system processes entered values alongside any URL entities that the operation discovers.   
`Check Existing Submissions First` | Optional. If selected, this action checks the URL for existing public or private submission information. If found, the action immediately returns the information, bypassing the submission flow. Disabled by default.  
`Resubmit After (Days)` | Optional. The minimum number of days that must pass after the URL's last public analysis date for the URL to become eligible for resubmission. **Note:** To use this parameter, you must enable `Check Existing Submissions First`. The default value is `30`.  
  
#### Action outputs

The **Private Submit URL** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Not available  
Enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result. | Available  
  
##### Case wall link

The **Private Submit URL** action can return the following link:

**Report Link` URL`**: `URL to the GTI UI displaying the submission details.`

##### Entity enrichment table

The **Private Submit URL** action supports the following entity enrichment for **URL** entities when data is retrieved from a public submission:

Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GTI_id` | `id` | When available in the JSON result.  
`GTI_title` | `title` | When available in the JSON result.  
`GTI_last_http_response_code` | `last_http_response_code` | When available in the JSON result.  
`GTI_last_http_response_content_length` | `last_http_response_content_length` | When available in the JSON result.  
`GTI_threat_names` | Comma-separated list of `threat_names` | When available in the JSON result.  
`GTI_harmless_count` | `last_analysis_stats/harmless` | When available in the JSON result.  
`GTI_malicious_count` | `last_analysis_stats/malicious` | When available in the JSON result.  
`GTI_suspicious_count` | `last_analysis_stats/suspicious` | When available in the JSON result.  
`GTI_undetected_count` | `last_analysis_stats/undetected` | When available in the JSON result.  
`GTI_reputation` | `reputation` | When available in the JSON result.  
`GTI_tags` | Comma-separated list of `tags` | When available in the JSON result.  
`GTI_malicious_vote_count` | `total_votes/malicious` | When available in the JSON result.  
`GTI_harmless_vote_count` | `total_votes/harmless` | When available in the JSON result.  
`GTI_report_link` | `report link` | When available in the JSON result.  
`GTI_widget_link` | `widget_url` | When available in the JSON result.  
`GTI_threat_score` | `gti_assessment.threat_score.value` | When available in the JSON result.  
`GTI_severity` | `gti_assessment.severity.value` | When available in the JSON result.  
`GTI_normalised_categories` | CSV of `gti_assessment.contributing_factors.normalised_categories` | When available in the JSON result.  
`GTI_verdict` | `gti_assessment.verdict.value` | When available in the JSON result.  
`GTI_description` | `gti_assessment.description` | When available in the JSON result.  
`GTI_category_{attributes/categories/json key}` | `{attributes/categories/json key value}` | When available in the JSON result.  
  
The **Private Submit URL** action supports the following entity enrichment for **URL** entities when data is retrieved from a private submission:

Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`GTI_id` | `id` | When available in the JSON result.  
`GTI_title` | `title` | When available in the JSON result.  
`GTI_last_http_response_code` | `last_http_response_code` | When available in the JSON result.  
`GTI_last_http_response_content_length` | `last_http_response_content_length` | When available in the JSON result.  
`GTI_tags` | Comma-separated list of `tags` | When available in the JSON result.  
`GTI_report_link` | `report link` | When available in the JSON result.  
`GTI_widget_link` | `widget_url` | When available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Private Submit URL** action:
    
    
    {
       "Entity": "",
       "EntityResult": [
           {
               "data": {
                   "id": "test_id_1234567890abcdef1234567890abcdef1234567890abcdef1234567890a",
                   "type": "private_url",
                   "links": {
                       "self": "https://www.googlethreatintelligence.com/api/v3/private/urls/test_id_1234567890abcdef1234567890abcdef1234567890abcdef1234567890a"
                   },
                   "attributes": {
                       "last_http_response_content_length": 23475,
                       "tags": [
                           "password-input",
                           "iframes",
                           "external-resources"
                       ],
                       "title": "Example Financial Institution",
                       "redirection_chain": [
                           "http://www.example-test-site.com/"
                       ],
                       "last_final_url": "https://www.example-test-site.com/",
                       "last_http_response_content_sha256": "test_sha256_000000000000000000000000000000000000000000000000000000000000",
                       "favicon": {
                           "raw_md5": "test_md5_0000000000000000000000000000",
                           "dhash": "075171c1878e82c0"
                       },
                       "last_http_response_code": 200,
                       "tld": "com",
                       "html_meta": {
                           "viewport": [
                               "width=device-width, initial-scale=1, shrink-to-fit=no"
                           ]
                       },
                       "expiration": 1760512221,
                       "last_http_response_headers": {
                           "cache-control": "no-store, no-cache, must-revalidate",
                           "content-encoding": "br",
                           "date": "Tue, 14 Oct 2025 07:10:28 GMT",
                           "expires": "Thu, 19 Nov 1981 08:52:00 GMT",
                           "platform": "hostinger",
                           "server": "LiteSpeed",
                           "vary": "Accept-Encoding",
                           "content-security-policy": "upgrade-insecure-requests",
                           "content-type": "text/html; charset=UTF-8",
                           "panel": "hpanel",
                           "pragma": "no-cache",
                           "x-powered-by": "PHP/7.3.33",
                           "alt-svc": "h3=\":443\"; ma=2592000, h3-29=\":443\"; ma=2592000, h3-Q050=\":443\"; ma=2592000, h3-Q046=\":443\"; ma=2592000, h3-Q043=\":443\"; ma=2592000, quic=\":443\"; ma=2592000; v=\"43,46\""
                       },
                       "url": "http://www.example-test-site.com/",
                       "outgoing_links": [
                           "https://www.jivochat.com/i_sa/?utm_source=www.solentrcu.com&utm_medium=link&utm_content=label_tooltip&utm_campaign=from_widget",
                           "https://code.jivosite.com/sounds/agent_message.mp3",
                           // ... other outgoing links maintained for structure
                       ]
                   }
               }
           }
       ]
    }
    

##### Output messages

The **Private Submit URL** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about the following URLs in Google Threat Intelligence: URLS. ` `Action couldn't find information about the following URLs in Google Threat Intelligence: URLS.` `None of the provided URLs were processed in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Private Submit URL". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Private Submit URL** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Search ASM Entities

Use the **Search ASM Entities** action to search for ASM entities in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search ASM Entities** action requires the following parameters:

Parameter | Description  
---|---  
`Project Name` | Optional.The name of the ASM project.If you don't set a value, the action uses the value that you configured for the `ASM Project Name` integration parameter.  
`Entity Name` | Optional.A comma-separated list of entity names to find entities.The action treats entity names that contain `/` forward slashes as invalid values.  
`Minimum Vulnerabilities Count` | Optional.The minimum number of vulnerabilities required for the action to return the entity.  
`Minimum Issues Count` | Optional.The minimum number of issues required for the action to return the entity.  
`Tags` | Optional.A comma-separated list of tag names to use when searching for entities.  
`Max Entities To Return` | Optional.The number of entities to return.The maximum value is `200`. The default value is `50`.  
`Critical or High Issue` | Optional.If selected, the action only returns issues with `High` and `Critical` severity.Not selected by default.  
  
#### Action outputs

The **Search ASM Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Search ASM Entities** action:
    
    
    {
     "id": "ID",
     "dynamic_id": "Intrigue::Entity::IpAddress#192.0.2.92",
     "alias_group": "1935953",
     "name": "192.0.2.92",
     "type": "Intrigue::Entity::IpAddress",
     "first_seen": "2022-02-02T01:44:46Z",
     "last_seen": "2022-02-02T01:44:46Z",
     "collection": "cpndemorange_oum28bu",
     "collection_type": "Intrigue::Collections::UserCollection",
     "collection_naics": [],
     "collection_uuid": "COLLECTION_UUID",
     "organization_uuid": "ORGANIZATION_UUID",
     "tags": [],
     "issues": [],
     "exfil_lookup_identifier": null,
     "summary": {
         "scoped": true,
         "issues": {
             "current_by_severity": {},
             "current_with_cve": 0,
             "all_time_by_severity": {},
             "current_count": 0,
             "all_time_count": 0,
             "critical_or_high": false
         },
         "task_results": [
             "search_shodan"
         ],
         "geolocation": {
             "city": "San Jose",
             "country_code": "US",
             "country_name": null,
             "latitude": "-121.8896",
             "asn": null
         },
         "ports": {
             "count": 0,
             "tcp": null,
             "udp": null
         },
         "resolutions": [
             "ec2-192-0-2-92.us-west-1.compute.example.com"
         ],
         "network": {
             "name": "EXAMPLE-02",
             "asn": "16509.0",
             "route": "2001:db8::/32",
             "type": null
         },
         "technology": {
             "cloud": true,
             "cloud_providers": [
                 "Cloud Provider Name"
             ]
         }
     }
    }
    

##### Output messages

The **Search ASM Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned entities based on the provided criteria in Google Threat Intelligence.` `No entities were found based on the provided criteria in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Search ASM Entities". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search ASM Entities** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search ASM Issues

Use the **Search ASM Issues** action to search for ASM issues in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search ASM Issues** action requires the following parameters:

Parameter | Description  
---|---  
`Project Name` | Optional.The name of the ASM project.If you don't set a value, the action uses the value that you configured for the `ASM Project Name` integration parameter.  
`Issue ID` | Optional.A comma-separated list of issue IDs to return the details.  
`Entity ID` | Optional.A comma-separated list of entity IDs to find related issues.  
`Entity Name` | Optional.A comma-separated list of entity names to find related issues.The action treats entity names that contain `/` forward slashes as invalid values.  
`Time Parameter` | Optional.A filter option to set the issue time. The possible values are `First Seen` and `Last Seen`.The default value is `First Seen`.  
`Time Frame` | Optional.A period to filter issues. If you select `Custom`, configure the `Start Time` parameter. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | Optional.The start time for the results.If you selected `Custom` for the `Time Frame` parameter, this parameter is required.Configure the value in the ISO 8601 format.  
`End Time` | Optional.The end time for the results.If you selected `Custom` for the `Time Frame` parameter and didn't set the end time, this parameter uses the current time as the end time. Configure the value in the ISO 8601 format.  
`Lowest Severity To Return` | Optional.The lowest severity of the issues to return. The possible values are as follows:

  * `Select One`
  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Informational`

The default value is `Select One`. If you select `Select One`, this filter doesn't apply to the search.  
`Status` | Optional.The status filter for the search. The possible values are `Open`, `Closed`, and `Select One`. The default value is `Select One`. If you select `Select One`, this filter doesn't apply to the search.  
`Tags` | Optional.A comma-separated list of tag names to use when searching for issues.  
`Max Issues To Return` | Required.The number of issues to return.The maximum value is `200`. The default value is `50`.  
  
#### Action outputs

The **Search ASM Issues** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Search ASM Issues** action:
    
    
    {
     "id": "ID",
     "uuid": "UUID",
     "dynamic_id": 20073997,
     "name": "exposed_ftp_service",
     "upstream": "intrigue",
     "last_seen": "2022-02-02T01:44:46.000Z",
     "first_seen": "2022-02-02T01:44:46.000Z",
     "entity_uid": "3443a638f951bdc23d3a089bff738cd961a387958c7f5e4975a26f12e544241f",
     "entity_type": "Intrigue::Entity::NetworkService",
     "entity_name": "192.0.2.204:24/tcp",
     "alias_group": "1937534",
     "collection": "example_oum28bu",
     "collection_uuid": "511311a6-6ff4-4933-8f5b-f1f7df2f6a3e",
     "collection_type": "user_collection",
     "organization_uuid": "21d2d125-d398-4bcb-bae1-11aee14adcaf",
     "summary": {
         "pretty_name": "Exposed FTP Service",
         "severity": 3,
         "scoped": true,
         "confidence": "confirmed",
         "status": "open_new",
         "category": "misconfiguration",
         "identifiers": null,
         "status_new": "open",
         "status_new_detailed": "new",
         "ticket_list": null
     },
     "tags": []
    }
    

##### Output messages

The **Search ASM Issues** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned issues based on the provided criteria in Google Threat Intelligence.` `No issues were found based on the provided criteria in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Search ASM Issues". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search ASM Issues** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Entity Graphs

Use the **Search Entity Graphs** action to search graphs that are based on Google SecOps entities in Google Threat Intelligence.

This action only supports MD5, SHA-1, and SHA-256 hashes.

This action runs on the following Google SecOps entities:

  * `Domain`
  * `File Hash`
  * `Hostname`
  * `IP Address`
  * `Threat Actor`
  * `URL`
  * `User`



#### Action inputs

The **Search Entity Graphs** action requires the following parameters:

Parameter | Description  
---|---  
`Sort Field` | Optional. The field value to sort the results. The possible values are as follows:

  * `Owner`
  * `Creation Date`
  * `Last Modified Date`
  * `Views Count`
  * `Comments Count`

The default value is `Owner`.  
`Max Graphs To Return` | Optional. The maximum number of graphs to return for every action run. The default value is `10`.  
  
#### Action outputs

The **Search Entity Graphs** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Search Entity Graphs** action:
    
    
    {
        "data": [
            {
                "attributes": {
                    "graph_data": {
                        "description": "EXAMPLE",
                        "version": "5.0.0"
                    }
                },
                "id": "ID"
            }
        ]
    }
    

##### Output messages

The **Search Entity Graphs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned graphs based on the provided entities in Google Threat Intelligence.` `Action wasn't able to successfully return graph based on the provided entities in Google Threat Intelligence. Reason: ERROR_REASON.` `No graphs were found for the provided entities.` | The action succeeded.  
`Error executing action "Search Entity Graphs". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
### Search Graphs

Use the **Search Graphs** action to search graphs based on custom filters in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search Graphs** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | Required.The query filter for the graph. For example, to search for graphs in the selected period, format the query as follows: `creation_date:2018-11-1+creation_date:2018-11-12`For more information about queries, see How to create queries, Graph-related modifiers, and Node-related modifiers.  
`Sort Field` | Optional. The field value to sort the VirusTotal graphs. The possible values are as follows:

  * `Comments Count`
  * `Creation Date`
  * `Last Modified Date`
  * `Owner`
  * `Views Count`

The default value is `Owner`.  
`Max Graphs To Return` | Optional. The maximum number of graphs to return for every action run. The default value is `10`.  
  
#### How to create queries

To refine search results from graphs, create queries that contain graph-related modifiers. To improve the search, you can combine modifiers with `AND`, `OR`, and `NOT` operators.

Date and numeric fields support the `+` plus and `-` minus suffixes. A plus suffix matches values greater than the provided value. A minus suffix matches values less than the provided value. Without a suffix, the query returns exact matches.

To define ranges, you can use the same modifier multiple times in a query. For example, to search graphs that are created between 2018-11-15 and 2018-11-20, use the following query:
    
    
    creation_date:2018-11-15+ creation_date:2018-11-20-
    

For dates or months that begin with `0`, remove the `0` character in the query. For example, format the date of 2018-11-01 as `2018-11-1`.

#### Graph-related modifiers

The following table lists graph-related modifiers which you can use to construct the search query:

Modifier name | Description | Example  
---|---|---  
`id` | Filters by graph identifier. | `id:g675a2fd4c8834e288af`  
`name` | Filters by graph name. | `name:Example-name`  
`owner` | Filters by graphs owned by the user. | `owner:example_user`  
`group` | Filters by graphs owned by a group. | `group:example`  
`visible_to_user` | Filters by graphs visible to the user. | `visible_to_user:example_user`  
`visible_to_group` | Filters by graphs visible to the group. | `visible_to_group:example`  
`private` | Filters by private graphs. | `private:true`, `private:false`  
`creation_date` | Filters by the graph creation date. | `creation_date:2018-11-15`  
`last_modified_date` | Filters by the latest graph modification date. | `last_modified_date:2018-11-20`  
`total_nodes` | Filters by graphs that contain a specific number of nodes. | `total_nodes:100`  
`comments_count` | Filters by the number of comments in the graph. | `comments_count:10+`  
`views_count` | Filters by the number of graph views. | `views_count:1000+`  
  
#### Node-related modifiers

The following table lists graph-related modifiers which you can use to construct the search query:

Modifier name | Description | Example  
---|---|---  
`label` | Filters by graphs that contain nodes with a specific label. | `label:Kill switch`  
`file` | Filters by graphs that contain the specific file. | `file:131f95c51cc819465fa17`  
`domain` | Filters by graphs that contain the specific domain. | `domain:example.com`  
`ip_address` | Filters by graphs that contain the specific IP address. | `ip_address:203.0.113.1`  
`url` | Filters by graphs that contain the specific URL. | `url:https://example.com/example/`  
`actor` | Filters by graphs that contain the specific actor. | `actor:example actor`  
`victim` | Filters by graphs that contain the specific victim. | `victim:example_user`  
`email` | Filters by graphs that contain the specific email address. | `email:user@example.com`  
`department` | Filters by graphs that contain the specific department. | `department:engineers`  
  
#### Action outputs

The **Search Graphs** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Search Graphs** action:
    
    
    {
        "data": [
            {
                "attributes": {
                    "graph_data": {
                        "description": "EXAMPLE",
                        "version": "5.0.0"
                    }
                },
                "id": "ID"
            }
        ]
    }
    

##### Output messages

The **Search Graphs** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned graphs for the provided query in Google Threat Intelligence.` `No graphs were found for the provided query.` | The action succeeded.  
`Error executing action "Search Graphs". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Graphs** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Set DTM Alert Analysis

Use the **Set DTM Alert Analysis** action to define an analysis for a Digital Threat Monitoring (DTM) alert in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set DTM Alert Analysis** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | Required. The ID of the alert to add the analysis to.  
`Text` | Required. The analysis to add to the alert.  
`Attachment File Paths` | Optional. A comma-separated list of file paths to attach to the alert. A maximum of 10 attachments is supported.  
  
#### Action outputs

The **Set DTM Alert Analysis** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result. | Available  
  
##### Output messages

The **Set DTM Alert Analysis** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated the alert with the ID ALERT_ID in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Set DTM Alert Analysis". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set DTM Alert Analysis** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Submit File

Use the **Submit File** action to submit a file and return results from Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

This action is asynchronous. Adjust the script timeout value in the Google SecOps integrated development environment (IDE) for the action as needed.

#### Action inputs

The **Submit File** action requires the following parameters:

Parameter | Description  
---|---  
`GTI Score` | Optional. The Google Threat Intelligence score used to set the `is_risky` property to `true` in the JSON result. This condition is validated alongside Google Threat Intelligence verdict information. If no value is provided, the action ignores the Google Threat Intelligence score. The default value is `60`.  
`Engine Threshold` | Optional. The minimum number of security engines that must mark an entity as malicious or suspicious to set the `is_risky` property to `true`. This condition is validated alongside Google Threat Intelligence verdict information. If `Engine Allowlist` contains values, only results from those specific engines are counted. If no value is provided, the action ignores engine count calculations.  
`Engine Percentage Threshold` | Optional. The minimum percentage of security engines that must mark an entity as malicious or suspicious to set the `is_risky` property to `true` (`0` and `100`). If `Engine Allowlist` contains values, the percentage is calculated only from those specific engines. If both `Engine Threshold` and `Engine Percentage Threshold` are provided, `Engine Threshold` takes precedence. If no value is provided, the action ignores percentage calculations.  
`Engine Allowlist` | Optional. A comma-separated list of security engines to use when determining maliciousness (for example, `AlienVault,Kaspersky`). Engines that don't return information about an entity are excluded from `Engine Threshold` and `Engine Percentage Threshold` calculations. If no value is provided, the action retrieves results from every available engine.  
`External URLs` | Optional.A comma-separated list of public URLs for the files to submit. If both "External URL" and "File Paths" are provided, the action will collect files from both inputs.  
`File Paths` | Optional.A comma-separated list of absolute file paths. If you configure the **Linux Server Address** parameter, the action attempts to retrieve the file from a remote server. If both "External URL" and "File Paths" are provided, the action will collect files from both inputs.  
`Check Hash First` | Optional. Default: Disabled.If enabled, action will first calculate the hashes for the files and search, if there is any available information for it. If available, it will return the information without the submission flow.  
`Resubmit After (Days)` | Optional. The number of days for the action to wait before resubmitting the file (even if the hash is available for the file in the GTI database). You must enable `Check Hash First` to use this parameter. The default value is `30`.  
`Fetch MITRE Details` | Optional.If selected, the action returns the information about the related MITRE techniques and tactics.Not selected by default.  
`Lowest MITRE Technique Severity` | Optional.The lowest MITRE technique severity to return. The action treats the `Unknown` severity as `Info`.This parameter only supports the Hash entity. The default value is `Low`.  
`Private Submission` | Optional.If selected, the action submits the file in a private mode.To submit files privately, the VirusTotal Premium API is required.  
`Retrieve Comments` | Optional.If selected, the action retrieves comments about the submitted file.  
`Max Comments To Return` | Optional.The maximum number of comments to return in every action run.  
`Linux Server Address` | Optional.The IP address of the remote Linux server where the file is located.  
`Linux Username` | Optional.The username of the remote Linux server where the file is located.  
`Linux Password` | Optional.The password of the remote Linux server where the file is located.  
`ZIP Password` | Optional.A password for the zipped folder that contains the files to submit.  
  
#### Action outputs

The **Submit File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result. | Available  
  
##### Case wall link

The **Submit File** action can return the following link:

**Report Link` PATH`**: `URL`

##### JSON result

The following example shows the JSON result output received when using the **Submit File** action:
    
    
    {
        "data": {
            "attributes": {
                "categories": {
                    "Dr.Web": "known infection source/not recommended site",
                    "Forcepoint ThreatSeeker": "compromised websites",
                    "sophos": "malware repository, spyware and malware"
                },
                "first_submission_date": 1582300443,
                "html_meta": {},
                "last_analysis_date": 1599853405,
                "last_analysis_results": {
                    "ADMINUSLabs": {
                        "category": "harmless",
                        "engine_name": "ADMINUSLabs",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "AegisLab WebGuard": {
                        "category": "harmless",
                        "engine_name": "AegisLab WebGuard",
                        "method": "blacklist",
                        "result": "clean"
                    },
                },
                "last_analysis_stats": {
                    "harmless": 64,
                    "malicious": 6,
                    "suspicious": 1,
                    "timeout": 0,
                    "undetected": 8
                },
                "last_final_url": "http://192.0.2.15/input/?mark=20200207-example.com/31mawe&tpl=ID&engkey=bar+chart+click+event",
                "last_http_response_code": 404,
                "last_http_response_content_length": 204,
                "last_http_response_content_sha256": "HASH_VALUE",
                "last_http_response_headers": {
                    "connection": "keep-alive",
                    "content-length": "204",
                    "content-type": "text/html; charset=iso-8859-1",
                    "date": "Fri, 11 Sep 2020 19:51:50 GMT",
                    "keep-alive": "timeout=60",
                    "server": "nginx"
                },
                "last_modification_date": 1599853921,
                "last_submission_date": 1599853405,
                "reputation": 0,
                "tags": [
                    "ip"
                ],
                "targeted_brand": {},
                "threat_names": [
                    "Mal/HTMLGen-A"
                ],
                "times_submitted": 3,
                "title": "404 Not Found",
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trackers": {},
                "url": "http://192.0.2.15/input/?mark=20200207-example.com/31mawe&tpl=ID&engkey=bar+chart+click+event"
            },
            "id": "ID",
            "links": {
                "self": "https://www.virustotal.com/api/v3/urls/ID"
            },
            "type": "url",
            "comments": [
    "text": "attributes/text",
    "date": "attributes/date"
    ]
        }
        "is_risky": true,
    "related_mitre_techniques": [{"id": "T1071", "name": "", "severity": ""}],
    "related_mitre_tactics": [{"id":"TA0011", "name": ""}],
    "generated_ai_summary" : "summary_text_here…"
    }
    

##### Output messages

The **Submit File** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about the following files using Google Threat Intelligence:PATHS. ` `The action wasn't able to return details about the following files using Google Threat Intelligence: PATHS.` `The action wasn't able to find the following files: PATHS.` `The action didn't retrieve any details about the files or none of the files were found.` `The action is waiting for results for the following files: PATHS.` `The action failed to fetch an AI summary for the following files: PATHS. To generate AI summary, check for sufficient permissions and try again.` | The action succeeded.  
`Error executing action "Submit File". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
`Error executing action "Submit File". Reason: ERROR_REASON` | No "File Paths" or "External URLs" valuesAt least one of "File Paths" or "External URLs" parameters should have a value.  
  
##### Script result

The following table lists the value for the script result output when using the **Submit File** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update ASM Issue

Use the **Update ASM Issue** action to update an ASM issue in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update ASM Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Issue ID` | Required.The ID of the issue to update.  
`Status` | Required.The new status to set for the issue. The possible values are as follows:

  * `Select One`
  * `New`
  * `Triaged`
  * `In Progress`
  * `Resolved`
  * `Duplicate`
  * `Out Of Scope`
  * `Not A Security Issue (Benign)`
  * `Risk Accepted`
  * `False Positive`
  * `Unable To Reproduce`
  * `Tracked Externally`
  * `Mitigated`

The default value is `Select One`. If you use the default value, the action fails.  
  
#### Action outputs

The **Update ASM Issue** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Update ASM Issue** action:
    
    
    {
        "success": true,
        "message": "Successfully reported status as open_new",
        "result": "open_new"
    }
    

##### Output messages

The **Update ASM Issue** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated issue with ID "ISSUE_ID" in Google Threat Intelligence.` | The action succeeded.  
`Error executing action "Update ASM Issue". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update ASM Issue** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update DTM Alert

Use the **Update DTM Alert** action to update a Mandiant Digital Threat Monitoring alert in Google Threat Intelligence.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update DTM Alert** action requires the following parameters:

Parameters | Description  
---|---  
`Alert ID` | Required.The ID of the alert to update.  
`Status` | Optional.The new status to set for the alert.The possible values are as follows:

  * `Select One`
  * `New`
  * `Read`
  * `Resolved`
  * `Escalated`
  * `In Progress`
  * `No Action Required`
  * `Duplicate`
  * `Not Relevant`
  * `Tracked Externally`

The default value is `Select One`. If you use the default value, the action fails.  
  
#### Action outputs

The **Update DTM Alert** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Update DTM Alert** action:
    
    
    {
       "id": "ID",
       "monitor_id": "MONITOR_ID",
       "topic_matches": [
           {
               "topic_id": "4a6ffb0f-e90d-46ce-b10a-3a1e24fbe70d",
               "value": "ap-southeast-1.example.com",
               "term": "lwd",
               "offsets": [
                   26,
                   29
               ]
           },
           {
               "topic_id": "doc_type:domain_discovery",
               "value": "domain_discovery"
           }
       ],
       "label_matches": [],
       "doc_matches": [],
       "tags": [],
       "created_at": "2024-05-31T12:27:43.475Z",
       "updated_at": "2024-05-31T12:43:20.399Z",
       "labels_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/ID/labels",
       "topics_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/ID/topics",
       "doc_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/ID",
       "status": "closed",
       "alert_type": "Domain Discovery",
       "alert_summary": "See alert content for details",
       "title": "Suspicious domain \"ap-southeast-1.example.com\" similar to \"lwd\"",
       "email_sent_at": "",
       "severity": "medium",
       "confidence": 0.5,
       "has_analysis": false,
       "monitor_version": 2
    }
    

##### Output messages

The **Update DTM Alert** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated alert with ID INCIDENT_ID in Google Threat Monitoring.` | Action succeeded.  
`Error executing action "Update DTM Alert". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update DTM Alert** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Google Threat Intelligence - DTM Alerts Connector

Use the **Google Threat Intelligence - DTM Alerts Connector** to retrieve alerts from Google Threat Intelligence. To work with a dynamic list, use the `alert_type` parameter.

#### Connector inputs

The **Google Threat Intelligence - DTM Alerts Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype). The default value is `event_type`.  
`Environment Field Name` | Optional.The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout` | Required.The timeout limit, in seconds, for the Python process that runs the current script.The default value is `180`.  
`API Root` | Required.The API root of the Google Threat Intelligence instance.The default value is `https://www.virustotal.com`.  
`API Key` | Required.The Google Threat Intelligence API key.  
`Lowest Severity To Fetch` | Optional.The lowest severity of the alerts to retrieve.If you don't configure this parameter, the connector ingests alerts with all severity levels.The possible values are as follows:

  * `Low`
  * `Medium`
  * `High`

  
`Monitor ID Filter` | Optional.A comma-separated list of monitor IDs to retrieve the alerts.  
`Monitor Name Filter` | Optional. A comma-separated list of monitor names from which to retrieve alerts. If multiple monitors share the same name, the connector ingests from all of them. This parameter is evaluated alongside Monitor ID values using OR logic.  
`Event Type Filter` | Optional.A comma-separated list of event types to return. The input is case insensitive. If no value is provided, the connector processes all event types. To exclude a specific type, prefix it with an exclamation mark (such as, `!event_type`).  
`Disable Overflow` | Optional.If selected, the connector ignores the Google SecOps overflow mechanism.Enabled by default.  
`Max Hours Backwards` | Required. The number of hours prior to now to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The default value is `1`.  
`Max Alerts To Fetch` | Required. The number of alerts to process in every connector iteration. The maximum value is `25`. The default value is `25`.  
`Use dynamic list as a blocklist` | Required.If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google Threat Intelligence server. Enabled by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
`Anonymize Passwords` | Optional. If selected, the connector anonymizes password fields in the alert data by replacing the characters with asterisks, leaving only the first and last characters visible.  
  
#### Connector rules

The **Google Threat Intelligence - DTM Alerts Connector** supports proxies.

#### Connector events

There are two types of events for the **Google Threat Intelligence - DTM Alerts Connector** : an event that is based on the main alert and an event that is based on a topic.

An example of the connector event based on the main alert is as follows:
    
    
    {
       "id": "ID",
       "event_type": "Main Alert",
       "monitor_id": "MONITOR_ID",
       "doc": {
           "__id": "6ed37932-b74e-4253-aa69-3eb4b00d0ea2",
           "__type": "account_discovery",
           "ingested": "2024-05-20T16:15:53Z",
           "service_account": {
               "login": "user@example.com",
               "password": {
                   "plain_text": "********"
               },
               "profile": {
                   "contact": {
                       "email": "user@example.com",
                       "email_domain": "example.com"
                   }
               },
               "service": {
                   "inet_location": {
                       "domain": "www.example-service.com",
                       "path": "/signin/app",
                       "protocol": "https",
                       "url": "https://www.example-service.com/signin/app"
                   },
                   "name": "www.example-service.com"
               }
           },
           "source": "ccmp",
           "source_file": {
               "filename": "urlloginpass ap.txt",
               "hashes": {
                   "md5": "c401baa01fbe311753b26334b559d945",
                   "sha1": "bf700f18b6ab562afb6128b42a34ae088f9c7434",
                   "sha256": "5e6302d95a7e7edb28d68926cede0c44babded720ad1cc9a72c12d8c6d66153f"
               },
               "size": 84161521407
           },
           "source_url": "https://example.com",
           "timestamp": "2023-11-14T20:09:04Z"
       },
       "labels": "Label",
       "topic_matches": [
           {
               "topic_id": "doc_type:account_discovery",
               "value": "account_discovery"
           }
       ],
       "label_matches": [],
       "doc_matches": [
           {
               "match_path": "service_account.profile.contact.email_domain",
               "locations": [
                   {
                       "offsets": [
                           0,
                           9
                       ],
                       "value": "example.com"
                   }
               ]
           }
       ],
       "tags": [],
       "created_at": "2024-05-20T16:16:52.439Z",
       "updated_at": "2024-05-30T12:10:56.691Z",
       "labels_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/account_discovery/ID/labels",
       "topics_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/account_discovery/ID/topics",
       "doc_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/account_discovery/ID",
       "status": "read",
       "alert_type": "Compromised Credentials",
       "alert_summary": "ccmp",
       "title": "Leaked Credentials found for domain \"example.com\"",
       "email_sent_at": "",
       "indicator_mscore": 60,
       "severity": "high",
       "confidence": 0.9999995147741939,
       "aggregated_under_id": "ID",
       "monitor_name": "Compromised Credentials - Example",
       "has_analysis": false,
       "meets_password_policy": "policy_unset",
       "monitor_version": 1
    }
    

An example of the connector event based on a topic is as follows:
    
    
    {
       "id": "ID",
       "event_type": "location_name",
       "location_name": "LOCATION_NAME",
       "timestamp": "2024-05-25T10:56:17.201Z",
       "type": "location_name",
       "value": "LOCATION_NAME",
       "extractor": "analysis-pipeline.nerprocessor-nerenglish-gpu",
       "extractor_version": "4-0-2",
       "confidence": 100,
       "entity_locations": [
           {
               "element_path": "body",
               "offsets": [
                   227,
                   229
               ]
           }
       ]
    }
    

### Google Threat Intelligence - GTI Alerts Connector

Use the **Google Threat Intelligence - GTI Alerts Connector** to retrieve Google Threat Intelligence dark web intelligence alerts, findings, documents, and associated entities from Google Threat Intelligence.

This connector uses the dynamic list to filter `detailType` values.

#### Use case

The **Google Threat Intelligence - GTI Alerts Connector** helps security operations teams automate the ingestion and triage of Dark Web Intelligence (DWI) and threat alerts into Google SecOps. For each ingested alert, the connector maps the main alert, related findings, dark web documents, and multi-value indicators of compromise (IOCs) into discrete Google SecOps events for automated investigation and response.

#### Connector inputs

Configure this connector using the following parameters:

Parameter | Description  
---|---  
`DeviceProductField` | Required. The name of the field that determines the device product. The default value is `Product Name`.  
`EventClassId` | Required. The name of the field that determines the event name (subtype). The default value is `eventType`.  
`PythonProcessTimeout` | Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`API Root` | Required. The API root of the Google Threat Intelligence instance, including the Google Cloud project path (for example, `https://threatintelligence.googleapis.com/v1beta/projects/YOUR_PROJECT_ID`). The default value is `https://threatintelligence.googleapis.com`.  
`API Key` | Required. The Google Threat Intelligence API key.  
`Lowest Severity To Fetch` | Optional. The lowest severity of the alerts to retrieve.If you don't configure this parameter, the connector ingests alerts with all severity levels. The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Informational`

  
`Alert Type Filter` | Optional. A comma-separated list of dark web alert `detailType` values to fetch (for example, `data_leak, insider_threat, initial_access_broker, target_technology`).  
`Max Hours Backwards` | Required. The number of hours before the initial connector iteration to retrieve alerts from. The default value is `1`.  
`Max Alerts To Fetch` | Required. The maximum number of alerts to process per connector iteration. The maximum value is `100`. The default value is `25`.  
`Use dynamic list as a blocklist` | Required. If selected, the connector uses the dynamic list as a blocklist.  
`Verify SSL` | Required. If selected, the connector verifies that the SSL certificate for connecting to Google Threat Intelligence is valid. Enabled by default.  
`Disable Overflow` | Optional. If selected, the connector ignores the Google SecOps overflow mechanism. Enabled by default.  
`Proxy Server Address` | Optional. The address of the proxy server to use.  
`Proxy Username` | Optional. The proxy username to authenticate with.  
`Proxy Password` | Optional. The proxy password to authenticate with.  
  
#### Proxy support

The connector supports proxies.

#### Connector events

The following example shows a custom event generated by the **Google Threat Intelligence - GTI Alerts Connector** :
    
    
    {
      "name": "projects/gti-project/alerts/alert-123",
      "displayName": "Leaked Credentials Alert",
      "detail_detailType": "leaked_credentials",
      "detail_leakedCredentials_severity": "HIGH",
      "severityAnalysis_severityLevel": "SEVERITY_LEVEL_HIGH",
      "priorityAnalysis_priorityLevel": "PRIORITY_LEVEL_HIGH",
      "aiSummary": "Leaked credentials detected for Cymbal Bank.",
      "audit_createTime": "2026-09-15T10:00:00Z",
      "audit_updateTime": "2026-09-15T10:00:00Z",
      "eventType": "Alert",
      "id": "projects/gti-project/alerts/alert-123",
      "title": "Leaked Credentials Alert",
      "alert_type": "leaked_credentials",
      "severity": "HIGH",
      "priority": "HIGH",
      "ai_summary": "Leaked credentials detected for Cymbal Bank.",
      "created_at": "2026-09-15T10:00:00Z"
    }
    

### Google Threat Intelligence - ASM Issues Connector

Use the **Google Threat Intelligence - ASM Issues Connector** to retrieve information about the ASM issues from Google Threat Intelligence. To work with the dynamic list filter, use the `category` parameter.

#### Connector inputs

The **Google Threat Intelligence - ASM Issues Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype). The default value is `entity_type`.  
`Environment Field Name` | Optional.The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout` | Required.The timeout limit, in seconds, for the Python process that runs the current script.The default value is `180`.  
`API Root` | Required.The API root of the Google Threat Intelligence instance.The default value is `https://www.virustotal.com`.  
`API Key` | Required.The Google Threat Intelligence API key.  
`Project Name` | Optional.The name of the ASM project. If you don't set a value, only alerts from collections in the primary project are returned.  
`Active Group` | Optional.The Active Group (Organization Context) identifier for multi-tenant environments. This is required if your ASM projects reside in a different organization than your primary one.  
`Lowest Severity To Fetch` | Optional.The lowest severity of the alerts to retrieve.If you don't configure this parameter, the connector ingests alerts with all severity levels.The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Informational`

  
`Issue Name Filter` | Optional.A comma-separated list of issues to ingest. The input is case sensitive. If names are listed directly, the connector uses an inclusion filter, ingesting only those matching issues. To exclude specific issues, prefix the name with an exclamation mark (such as, `!issue_name`). If no value is provided, the filter isn't applied, and all issues are ingested.  
`Status Filter` | Optional.A comma-separated list of issue statuses to ingest. If no value is provided, the connector only processes open issues. The possible values are as follows:

  * `Open`
  * `Closed`

The default value is `Open`.  
`Event Type Filter` | Optional.A comma-separated list of event types to return. The input is case insensitive. If no value is provided, the connector processes all event types. To exclude a specific type, prefix it with an exclamation mark (such as, `!event_type`).  
`Max Hours Backwards` | Required. The number of hours prior to now to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The default value is `1`.  
`Max Issues To Fetch` | Required. The number of issues to process in every connector iteration. The maximum value is `100`. The default value is `10`.  
`Disable Overflow` | Optional.If selected, the connector ignores the Google SecOps overflow mechanism.Enabled by default.  
`Use dynamic list as a blocklist` | Required.If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google Threat Intelligence server. Enabled by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
  
#### Connector events

The example of the **Google Threat Intelligence - ASM Issues Connector** event is as follows:
    
    
    {
       "uuid": "UUID",
       "dynamic_id": 25590288,
       "entity_uid": "9bae9d6f931c5405ad95f0a51954cf8f7193664f0808aadc41c8b25e08eb9bc3",
       "alias_group": null,
       "category": "vulnerability",
       "confidence": "confirmed",
       "description": "A crafted request uri-path can cause mod_proxy to forward the request to an origin server chosen by the remote user. This issue affects Apache HTTP Server 2.4.48 and earlier.",
       "details": {
           "added": "2021-10-15",
           "proof": "The following resolver IP Address: 203.0.113.132:50408 invoked a DNS Lookup with the following data <empty> at 2023-02-03T03:41:48Z using the UUID associated with this entity.",
           "status": "confirmed",
           "severity": 1,
           "references": [
               {
                   "uri": "https://example.com/vuln/detail/CVE-2021-40438",
                   "type": "description"
               },
               {
                   "uri": "https://httpd.example.org/security/vulnerabilities_24.html",
                   "type": "description"
               },
               {
                   "uri": "https://example.com/cve-2021-40438",
                   "type": "description"
               }
           ],
           "remediation": null
       },
       "first_seen": "2022-11-28T03:24:48.000Z",
       "identifiers": [
           {
               "name": "CVE-2021-40438",
               "type": "CVE"
           }
       ],
       "last_seen": "2023-02-03T03:41:48.000Z",
       "name": "cve_2021_40438",
       "pretty_name": "Apache HTTP Server Side Request Forgery (CVE-2021-40438)",
       "scoped": true,
       "severity": 1,
       "source": null,
       "status": "open_in_progress",
       "ticket_list": null,
       "type": "standard",
       "uid": "UID",
       "upstream": "intrigue",
       "created_at": "2022-11-28T03:34:31.124Z",
       "updated_at": "2023-02-03T04:03:44.126Z",
       "entity_id": 298912419,
       "collection_id": 117139,
       "collection": "example_oum28bu",
       "collection_type": "user_collection",
       "collection_uuid": "511311a6-6ff4-4933-8f5b-f1f7df2f6a3e",
       "organization_uuid": "21d2d125-d398-4bcb-bae1-11aee14adcaf",
       "entity_name": "http://192.0.2.73:80",
       "entity_type": "Intrigue::Entity::Uri",  
    
    
       "Intrigue::Entity::Uri": "http://192.0.2.73:80",
    
    
       "summary": {
           "pretty_name": "Apache HTTP Server Side Request Forgery (CVE-2021-40438)",
           "severity": 1,
           "scoped": true,
           "confidence": "confirmed",
           "status": "open_in_progress",
           "category": "vulnerability",
           "identifiers": [
               {
                   "name": "CVE-2021-40438",
                   "type": "CVE"
                   "CVE": "CVE-2021-40438"
               }
           ],
           "status_new": "open",
           "status_new_detailed": "in_progress",
           "ticket_list": null
       },
       "tags": []
    }
    

### Google Threat Intelligence - Livehunt Connector

Use the **Google Threat Intelligence - Livehunt Connector** to retrieve information about the Livehunt notifications and their related files from Google Threat Intelligence. To work with the dynamic list, use the `rule_name` parameter.

#### Connector inputs

The **Google Threat Intelligence - Livehunt Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype). The default value is `type`.  
`Environment Field Name` | Optional.The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout` | Required.The timeout limit, in seconds, for the Python process that runs the current script.The default value is `180`.  
`API Root` | Required.The API root of the Google Threat Intelligence instance.The default value is `https://www.virustotal.com`.  
`API Key` | Required.The Google Threat Intelligence API key.  
`Entity Type Filter` | Optional. A comma-separated list of entity types to filter notifications by (for example: `file`, `url`, `domain`, `ip_address`). If left empty, all entity types are ingested. The default value is `file`.  
`Max Hours Backwards` | Required. The number of hours prior to now to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The default value is `1`.  
`Max Notifications To Fetch` | Required. The number of notifications to process in every connector iteration. The default value is `40`.  
`Disable Overflow` | Optional.If selected, the connector ignores the Google SecOps overflow mechanism.Enabled by default.  
`Use dynamic list as a blocklist` | Required.If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google Threat Intelligence server. Enabled by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
  
#### Connector rules

The **Google Threat Intelligence - Livehunt Connector** supports proxies.

#### Connector events

The example of the **Google Threat Intelligence - Livehunt Connector** event is as follows:
    
    
    {
        "attributes": {
            "type_description": "Win32 DLL",
            "tlsh": "T1E6A25B41AF6020B3EAF508F135F6D913A930B7110AA4C957774B86511FB4BC3BE7AA2D",
            "vhash": "124056651d15155bzevz36z1",
            <! CONTENT OMITTED >
            "last_analysis_date": 1645620534,
            "unique_sources": 8,
            "first_submission_date": 1562871116,
            "sha1": "3de080d32b14a88a5e411a52d7b43ff261b2bf5e",
            "ssdeep": "384:wBvtsqUFEjxcAfJ55oTiwO5xOJuqn2F9BITqGBRnYPLxDG4y8jm+:e1YOcAfGnOmJuqn2LBITqGfWDG4yR+",
            "md5": "6a796088cd3d1b1d6590364b9372959d",
            "magic": "PE32 executable for MS Windows (DLL) (GUI) Intel 80386 32-bit",
            "last_analysis_stats": {
                "harmless": 0,
                "type-unsupported": 5,
                "suspicious": 0,
                "confirmed-timeout": 0,
                "timeout": 14,
                "failure": 4,
                "malicious": 0,
                "undetected": 49
            },
            "reputation": 0,
            "first_seen_itw_date": 1536433291
        },
        "type": "file",
        "id": "ID",
        "links": {
            "self": "https://www.virustotal.com/api/v3/files/ID"
        },
        "context_attributes": {
            "notification_id": "6425310189355008-7339e39660589ca2ec996c1c15ca5989-ID-1645620534",
            "notification_source_key": "KEY",
            "notification_tags": [
                "cve_pattern",
                "ID",
                "cverules"
            ],
            "ruleset_name": "cverules",
            "notification_source_country": "KR",
            "rule_name": "cve_pattern",
            "notification_snippet": "",
            "ruleset_id": "6425310189355008",
            "rule_tags": [],
            "notification_date": 1645620832,
            "match_in_subfile": false
        }
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
