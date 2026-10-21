---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/check-point-threat-reputation/
title: Check Point Threat Reputation \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:07.090364+00:00
---

# Check Point Threat Reputation  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/check-point-threat-reputation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Check Point Threat Reputation

**Important:** This integration refers to the Check Point Reputation Service.

This document describes how to integrate Check Point Reputation Service with Google Security Operations.

## Use Cases

Threat Intel service.

## Configure Check Point Threat Reputation integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | rep.checkpoint.com | Yes | Specify the Check Point Reputation Service API root URl.  
API Key | Password | N/A | Yes | Specify the Check Point Reputation Service API key.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verifies that the SSL certificate for the connection to the Check Point Reputation Service server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Check Point Reputation Service with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Playbook Use Cases Examples

The action is used to test connectivity at the integration configuration page in the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully connected to the Check Point Reputation Service with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Check Point Reputation Service! Error is {0}".format(exception.stacktrace) | General  
  
### Get File Hash Reputation

#### Description

Enrich Google SecOps File hash entity based on the information from the Check Point Reputation Service. Action accepts file hashes in md5, sha1, and sha256 formats.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Threshold | Integer | 0 | Yes | Mark entity as suspicious if the returned risk value for the entity is above a given threshold.  
Create Insight? | Checkbox | Unchecked | No | Specify whether the Google SecOps Insight should be created based on the action result.  
  
#### Playbook Use Cases Examples

Enrich the Google SecOps filehash entity with information from Check Point Reputation Service: During the processing of a possible malware infection alert, the user can benefit from having enrichment data from Check Point Reputation Service about particular filehashes that are associated with alert in question for investigative reasons.

#### Run On

This action runs on the FILEHASH (md5/sha1/sha256) entity.

#### Action Results

##### Entity Enrichment

The action should use all values from the API response for entity enrichment except for the "status" node of response.

##### Insights

Insight Logic | Type | Title (String) | Message  
---|---|---|---  
Create if the respective checkbox was checked. | Entity | Check Point Threat Reputation | **Classification:** value from API response**Confidence:** value from API response**Severity:** value from API response**Risk:** value from API response  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

Action should return JSON results compatible with the Expression Builder.
    
    
    {
        "response": [
            {
                "status": {
                    "code": 2001,
                    "label": "SUCCESS",
                    "message": "Succeeded to generate reputation"
                },
                "resource": "2c527d980eb30daa789492283f9bf69e",
                "reputation": {
                    "classification": "Riskware",
                    "severity": "Medium",
                    "confidence": "High"
                },
                "risk": 50,
                "context": {
                    "malware_family": "Mimikatz",
                    "protection_name": "HackTool.Win32.Mimikatz.TC.lc",
                    "malware_types": [
                        "Riskware"
                    ],
                    "metadata": {
                        "company_name": "gentilkiwi (Benjamin DELPY)",
                        "product_name": "mimikatz",
                        "copyright": "Copyright (c) 2007 - 2017 gentilkiwi (Benjamin DELPY)",
                        "original_name": "mimikatz.exe"
                    }
                }
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one of the provided entities is enriched:_ "Successfully enriched entities: {0}".format([entity.Identifier]).****_If failed to enrich all of the provided entities: "No entities were enriched."_****_If failed to find data in Check Point Reputation Service to enrich specific entities:_ "Action was not able to find Check Point Reputation Service info to enrich the following entities: {0}".format([entity.identifier])**The action should fail and stop a playbook execution:******_If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Check Point Reputation Service! Error is {0}".format(exception.stacktrace) | General  
Table | **Table name:** Check Point Reputation Service results for {0}.format(entity.Identifier)******Table columns:**

  * Classification
  * Confidence
  * Severity
  * Risk
  * Malware Family - context.malware_family
  * File Name - context.protection_name
  * Malware Type - context.malware_types (could be multiple comma separated values)
  * Company Name - metadata.company_name
  * Product Name - metadata.product_name
  * Copyright - metadata.copyright
  * Original File Name - metadata.original_name

| Entity  
  
### Get IP Reputation

#### Description

Enrich Google SecOps IP entity based on the information from the Check Point Reputation Service.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Threshold | Integer | 0 | Yes | Mark entity as suspicious if the returned risk value for the entity is above a given threshold.  
Create Insight? | Checkbox | Unchecked | No | Specify whether the Google SecOps Insight should be created based on the action result.  
  
#### Playbook Use Cases Examples

Enrich the Google SecOps IP entity with information from Check Point Threat Reputation service: During the processing of a possible malware infection alert, the user can benefit from having enrichment data from the Check Point Threat Reputation service about particular ips that are associated with the alert in question for investigative reasons.

#### Run On

This action runs on the IP entity.

#### Action Results

##### Entity Enrichment

The action should use all values from the API response for entity enrichment except for the "status" node of response.

##### Insights

Insight Logic | Type | Title (String) | Message  
---|---|---|---  
Create if the respective checkbox was checked. | Entity | Check Point Threat Reputation | **Classification:** value from API response**Confidence:** value from API response**Severity:** value from API response**Risk:** value from API response  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

Action should return JSON results compatible with the Expression Builder.
    
    
    {
        "response": [
            {
                "status": {
                    "code": 2001,
                    "label": "SUCCESS",
                    "message": "Succeeded to generate reputation"
                },
                "resource": "8.8.8.8",
                "reputation": {
                    "classification": "Benign",
                    "severity": "N/A",
                    "confidence": "High"
                },
                "risk": 0,
                "context": {
                    "location": {
                        "countryCode": "US",
                        "countryName": "United States",
                        "region": null,
                        "city": null,
                        "postalCode": null,
                        "latitude": 37.751007,
                        "longitude": -97.822,
                        "dma_code": 0,
                        "area_code": 0,
                        "metro_code": 0
                    },
                    "asn": 15169,
                    "as_owner": "Google LLC"
                }
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one of the provided entities is enriched:_ "Successfully enriched entities: {0}".format([entity.Identifier]).****_If failed to enrich all of the provided entities: "No entities were enriched."_****_If failed to find data in Check Point Reputation Service to enrich specific entities:_ "Action was not able to find Check Point Reputation Service info to enrich the following entities: {0}".format([entity.identifier])**The action should fail and stop a playbook execution:******_If a critical error, like wrong credentials or lost connectivity is reported:_ print "Failed to connect to the Check Point Reputation Service! Error is {0}".format(exception.stacktrace) | General  
Table  | **Table name:** Check Point Threat Reputation results for {0}.format(entity.Identifier) **Table columns:**

  * Classification
  * Confidence
  * Severity
  * Risk
  * Country Code - context.countryCode
  * Country - context.countryName
  * Region - context.region
  * City - context.city
  * Postal Code - context.postalCode
  * Latitude -context.latitude
  * Longitude - context.longitude
  * DMA Code - context.dma_code
  * Area Code -context.area_code
  * Metro Code -context.metro_code
  * ASN
  * Owner

| Entity  
  
### Get Host Reputation

#### Description

Enrich the Google SecOps Host entity based on the information from the Check Point Reputation Service.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Threshold | Integer | 0 | Yes | Mark entity as suspicious if the returned risk value for the entity is above a given threshold.  
Create Insight? | Checkbox | Unchecked | No | Specify whether the Google SecOps Insight should be created based on the action result.  
  
#### Playbook Use Cases Examples

Enrich the Google SecOps host entity with information from Check Point Threat Reputation service: During the processing of a possible malware infection alert, the user can benefit from having enrichment data from Check Point Threat Reputation service about particular hosts that are associated with the alert in question for investigative reasons.

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

The action should use all values from the API response for entity enrichment except for the "status" node of response.

##### Insights

Insight Logic | Type | Title (String) | Message  
---|---|---|---  
Create if the respective checkbox was checked. | Entity | Check Point Threat Reputation | **Classification:** value from API response**Confidence:** value from API response**Severity:** value from API response**Risk:** value from API response  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

Action should return JSON results compatible with the Expression Builder.
    
    
    {
        "response": [
            {
                "status": {
                    "code": 2001,
                    "label": "SUCCESS",
                    "message": "Succeeded to generate reputation"
                },
                "resource": "ynet.co.il",
                "reputation": {
                    "classification": "Benign",
                    "severity": "N/A",
                    "confidence": "High"
                },
                "risk": 0,
                "context": {
                    "categories": [
                        {
                            "id": 24,
                            "name": "News / Media"
                        }
                    ],
                    "indications": [
                        "The domain has good reputation",
                        "The domain is popular among websites with good reputation",
                        "The domain is popular in the world",
                        "The domain's Alexa rank is 1262",
                        "Check Point's URL Filtering category is News / Media",
                        "VirusTotal vendors detected benign URLs of the domain"
                    ],
                    "vt_positives": 0,
                    "alexa_rank": 1262,
                    "safe": true,
                    "creation_date": "2001:01:07 00:00:00"
                }
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful and at least one of the provided entities is enriched:_ "Successfully enriched entities: {0}".format([entity.Identifier]).****_If failed to enrich all of the provided entities: "No entities were enriched."_****_If failed to find data in Check Point Reputation Service to enrich specific entities:_ "Action was not able to find Check Point Reputation Service info to enrich the following entities: {0}".format([entity.identifier])**The action should fail and stop a playbook execution:******_If a_ ****_critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Check Point Reputation Service! Error is {0}".format(exception.stacktrace) | General  
Table | **Table name:** Check Point Threat Reputation results for {0}.format(entity.Identifier) **Table columns:**

  * Classification
  * Confidence
  * Severity
  * Risk
  * Categories - context.categories
  * Indications - context.indications
  * Virus Total Positives Count
  * Alexa Rank
  * Safe?
  * Creation Date

| Entity   
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
