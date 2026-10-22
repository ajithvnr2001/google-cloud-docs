---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/spycloud/
title: SpyCloud \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:35.623559+00:00
---

# SpyCloud  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/spycloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SpyCloud

This document provides guidance on how to integrate SpyCloud with Google SecOps.

## Use Cases

Perform enrichment of entities.

## Configure SpyCloud integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https:/{{api root}} | Yes | API root of the SpyCloud instance.  
API Key | Password | N/A | Yes | API Key of the SpyCloud instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the SpyCloud server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to SpyCloud with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** "Successfully connected to the SpyCloud server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:****if not successful:** "Failed to connect to the SpyCloud server! Error is {0}".format(exception.stacktrace) | General  
  
### List Catalogs

#### Description

List available catalogs in SpyCloud.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDLEqualContains | No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. "Equal" works with "title" parameter, while "Contains" works with all values in response. If nothing is provided in this parameter, the filter will not be applied.  
Time Frame | DDL | Last WeekPossible Values:Last WeekLast MonthLast YearCustom | Yes | Specify a time frame for the search. If "Custom" is selected, you also need to provide "Start Time".  
Start Time | String |  | No | Specify the start time for the search. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String |  | No | Specify the end time for the search. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.  
Max Catalogs To Return | Integer | 50 | No | Specify how many catalogs to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
        "site_description": "unifort.com.br was allegedly breached along with over 23,000 other sites and shared as part of the Cit0Day leak in November, 2020. Cit0Day is a now-defunct criminal databroker that was shuttered in September 2020.",
        "media_urls": [
            "https://www.zdnet.com/article/23600-hacked-databases-have-leaked-from-a-defunct-data-breach-index-site/"
        ],
        "confidence": 3,
        "title": "unifort.com.br",
        "description": "In November 2020, a collection of over 23,000 breached sites was leaked on several hacking forums and Telegram channels. These breached sites originated from Cit0Day, a now-defunct private subscription service marketed towards criminals. The leaked data primarily includes email addresses and passwords that Cit0Day offered for a daily or monthly subscription fee.",
        "acquisition_date": "2020-11-05T00:00:00Z",
        "site": "unifort.com.br",
        "id": 18679,
        "type": "PRIVATE",
        "num_records": 4226,
        "uuid": "0c87e8f6-d686-46c9-8ce4-5d9785917c0a",
        "spycloud_publish_date": "2020-12-10T00:00:00Z",
        "assets": {
            "email": 4226,
            "password": 4220
        }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available(is_success = true):** "Successfully found catalogs for the provided criteria in SpyCloud".  
******If data is not available (is_success=false):** "No catalogs were found for the provided criteria in SpyCloud".  
******The action should fail and stop a playbook execution:**  
**If fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Catalogs". Reason: {0}''.format(error.Stacktrace)******If Start Time is empty, when "Time Frame" is "Custom":** "Error executing action "List Catalogs". Reason: "Start Time" should be provided, when "Custom" is selected in "Time Frame" parameter." | General  
Case Wall Table | **Name:** Available Catalogs**Columns:** TitleType Number of records Site | General  
  
### List Entity Breaches

#### Description

Return information about breaches related to entities. Supported entity types: IP Address, Username, Email Address (Username entity that matches email regex), Domain (action will strip domain part from URL entity).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Catalog Filter | String |  | No | Specify the name of the category in which you want to search for breaches.  
Time Frame | DDL | Last WeekPossible Values:Last WeekLast MonthLast YearCustom | Yes | Specify a time frame for the search. If "Custom" is selected, you also need to provide "Start Time".  
Start Time | String |  | No | Specify the start time for the search. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601. Note: action will only take the datetime for action execution.  
End Time | String |  | No | Specify the end time for the search. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time. Note: action will only take the datetime for action execution.  
Max Breaches To Return | Integer | 1 | No | Specify how many breaches to return per entity. Default: 1. Maximum: 1000.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Username
  * Email Address
  * Domain



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "user_browser": "Google Chrome New",
        "password": "password",
        "ip_addresses": [
            "118.71.221.126"
        ],
        "infected_path": "C:\\Users\\TOAN\\AppData\\Local\\Temp\\7ZipSfx.000\\Nei.exe.com",
        "user_os": "Windows 10 Enterprise LTSC 2019 64-bit(x64) build: 17763 release: 1809",
        "infected_machine_id": "011c55b5-5951-42d8-aefa-dad3c206a032",
        "source_id": 37592,
        "target_url": "127.0.0.1",
        "email": "zena19@example.com",
        "user_sys_registered_owner": "TOAN",
        "user_hostname": "DELL",
        "infected_time": "2021-05-23T11:38:44Z",
        "spycloud_publish_date": "2021-06-03T00:00:00Z",
        "email_domain": "example.com",
        "email_username": "zena19",
        "domain": "example.com",
        "password_type": "plaintext",
        "password_plaintext": "password",
        "severity": 25,
        "document_id": "31f3bdff-564c-4c52-a0e5-3cd7f00b6655",
        "sighting": 1
    }
    

##### Enrichment Table

Enrichment Field Name | Logic - When to apply  
---|---  
was_breached | When available in JSON  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available for one entity (is_success = true):** "Successfully found breaches for the following entities in SpyCloud: {entity.identifier}".  
******If data is not available for one entity (is_success=true):** "Action wasn't able to find breaches for the following entities in SpyCloud: {entity.identifier}"  
******If data is not available for all (is_success=false):** No information about breaches was found for the provided entities.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Entity Breaches". Reason: {0}''.format(error.Stacktrace)******if Start Time is empty, when "Time Frame" is "Custom":** "Error executing action "List Entity Breaches". Reason: "Start Time" should be provided, when "Custom" is selected in "Time Frame" parameter."******If "Catalog Filter" is not found (fail):** "Error executing action "List Entity Breaches". Reason: Catalog {catalog name} was not found in SpyCloud. Please check the spelling. ''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
