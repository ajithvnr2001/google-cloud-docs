---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/area1/
title: Cloudflare Email Security with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:54.092514+00:00
---

# Cloudflare Email Security with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/area1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloudflare Email Security with Google SecOps 

This document explains how to integrate Cloudflare Email Security (formerly Area 1) with Google Security Operations (Google SecOps).

**Important:** This document refers to Cloudflare Email Security (formerly Area 1). In the Google SecOps platform, the integration for Cloudflare Email Security is called _Area 1_.

## Integration parameters

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | https://HOST:PORT | Yes | Address of the Area 1 instance.  
Username | String | N/A | Yes | The email address of the user which should be used to connect to Area 1.  
Password | Password | N/A | Yes | The password of the according user.  
Verify SSL | Checkbox | Checked | No | Use this checkbox, if your Area 1 connection requires an SSL verification.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Get Recent Indicators

Get recent malicious indicators from Cloudflare Email Security that can be related to phishing.

#### Parameters

Parameter | Type | Default value | Description  
---|---|---|---  
Seconds Back | String | N/A | N/A  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
Is_Success | True/False | Is_Success:False  
  
##### JSON result
    
    
    [
        {
            "threat_categories":
            [{
                "classification_disposition": ["Unclassified"]
            }],
            "threat_name": "Microsoft Favicon Impersonation",
            "item_name": "example.com/nc_assets/css/12/",
            "item_type": "url",
            "first_seen": 1550127499097,
            "last_seen": 1550134395800
        }, {
            "threat_categories":
            [{
                "category": ["Universal"],
                "threat_type": ["Actor Tool"],
                "classification_disposition": ["Unclassified"]
            }],
            "threat_name": "Area 1 Identified Malicious",
            "item_name": "e039e82c00e4ae0ddc92908c705350ec",
            "item_type": "filehash",
            "first_seen": 1550125103575,
            "last_seen": 1550125103575
        }
    ]
    

### Ping

Test the connectivity to Cloudflare Email Security.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
### Search Indicator

Search for indicators in Cloudflare Email Security by hash, URL, domain, IP address, or email address.

#### Run on

This action runs on all entities.

#### Action results

##### Entity enrichment

Enrichment rield name | Logic - When to apply  
---|---  
AREA1_category | Returns if it exists in JSON result  
AREA1_threat_type | Returns if it exists in JSON result  
AREA1_classification_disposition | Returns if it exists in JSON result  
AREA1_confidence_rating | Returns if it exists in JSON result  
AREA1_intervals | Returns if it exists in JSON result  
AREA1_value | Returns if it exists in JSON result  
AREA1_type | Returns if it exists in JSON result  
AREA1_name | Returns if it exists in JSON result  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": "85f321d7f27916de21992c5284ff632db3db3481",
            "Entity": "indicator"
        }, {
            "EntityResult": "red",
            "Entity": "tlp"
        }, {
            "EntityResult": 80,
            "Entity": "overall_confidence"
        }, {
            "EntityResult": "85f321d7f27916de21992c5284ff632db3db3481",
            "Entity": "name"
        }, {
            "EntityResult": [
                {
                    "category": ["Universal"],
                    "threat_type": ["Actor Tool"],
                    "classification_disposition": ["Unclassified"]
                }],
            "Entity": "threat_categories"
        }, {
            "EntityResult": "drizzle",
            "Entity": "author"
        }, {
            "EntityResult": "85f321d7f27916de21992c5284ff632db3db3481",
            "Entity": "filehash"
        }, {
            "EntityResult": 1550125103522,
            "Entity": "first_detected"
        }, {
            "EntityResult": "85f321d7f27916de21992c5284ff632db3db3481",
            "Entity": "Hash_SHA1"
        }, {
            "EntityResult": "Area 1 Identified Malicious",
            "Entity": "threat_name"
        }, {
            "EntityResult": "85f321d7f27916de21992c5284ff632db3db3481",
            "Entity": "query_term"
        }, {
            "EntityResult": "MAICIOUS",
            "Entity": "disposition"
        }, {
            "EntityResult": "file",
            "Entity": "family"
        }, {
            "EntityResult": [
                {
                    "category": "Indicator Category",
                    "confidence_rating": 80,
                    "intervals": [
                        {
                            "start": 1550120952000,
                            "end": "current"
                        }],
                    "value": "Universal"
                }],
            "Entity": "tag_histories"
        }, {
            "EntityResult": 1550125103522,
            "Entity": "first_seen"
        }, {
            "EntityResult": [
                {
                    "type": "Hash_MD5",
                    "name": "e412341be78003526999f77e8728526e"
                }, {
                    "type": "Hash_SHA256",
                    "name": "61f006012d2bd7f43bc14ecbeb6a7e690f9d68b4b6b396dab5805be2da75c717"
                }],
            "Entity": "aliases"
        }, {
            "EntityResult": "Hash_SHA1", "Entity": "type"
        }, {
            "EntityResult": 1550120950000,
            "Entity": "last_seen"
        }
    ]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
