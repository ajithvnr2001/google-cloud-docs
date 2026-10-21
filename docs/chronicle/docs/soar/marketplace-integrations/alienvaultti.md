---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alienvaultti/
title: Integrate AlienVault OTX with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:16:14.205232+00:00
---

# Integrate AlienVault OTX with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alienvaultti/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate AlienVault OTX with Google SecOps 

This document describes how to integrate AlienVault Open Threat Exchange (OTX) with Google Security Operations (Google SecOps).

**Important:** AlienVaultTI became AlientVault OTX by LevelBlue. In the Google SecOps platform, the integration for AlienVault OTX is called _AlienVaultTI_.

## Before you begin

To obtain API key, complete the following steps:

  1. Sign in to your [AlienVault OTX account](https://otx.alienvault.com/).

  2. Go to **Username > Settings** and copy the generated API key.




### Network

Function | Default port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Key | String | N/A | Yes | API key generated in AlienVault's console.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Enriches Entities

Enrich external IPs, hosts, URLs, and hashes with information from AlienVault Threat Intelligence (TI).

#### Parameters

N/A

#### Run on

This action runs on the following entities:

  * IP Address
  * Filehash
  * URL
  * Hostname



#### Action results

##### Entity enrichment

Enrichment field name | Logic - When to apply  
---|---  
analysis | Returns if it exists in JSON result  
general | Returns if it exists in JSON result  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
is_enriched | True or False | is_enriched:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": {
                "analysis": {
                    "analysis": {
                        "hash": "555a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd55",
                        "info": {
                            "results": {
                                "file_class": "None",
                                "file_type": "ASCII text, with no line terminators",
                                "md5": "55d88612fea8a8f36de82e1278abb02f",
                                "sha1": "1235856ce81f2b7382dee72602f798b642f14123",
                                "ssdeep": " ",
                                "filesize": "68",
                                "sha256": "37dhr21bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf65hdgsu"
                            }},
                        "_id": "52b1200214ad667e85105707",
                        "metadata": {
                            "tlp": "WHITE"
                        },
                        "datetime_int": "2013 - 12 - 18T04: 09: 37",
                        "plugins": {
                            "exiftool": {
                                "process_time": "0.083348989486694336",
                                "results": {
                                    "Error": "Unknown file type"
                                }},
                            "avg": {
                                "process_time": "0.92721199989318848",
                                "results": {
                                    "detection": "EICAR_Test",
                                    "alerts": [" Malware infection"]
                                }},
                            "clamav": {
                                "process_time": "0.00052618980407714844",
                                "results": {
                                    "detection": "Eicar - Test - Signature",
                                    "alerts": ["Malware detected"]
                                }}}},
                    "malware": {},
                    "page_type": "None"
                },
                "general": {
                    "type_title": " FileHash - SHA256",
                    "sections": ["general", "analysis"],
                    "indicator": "555a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd55",
                    "base_indicator": {
                        "title": " ",
                        "access_type": "public",
                        "description": " ",
                        "content": " ",
                        "indicator": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                        "access_reason": " ",
                        "type": "FileHash - SHA256",
                        "id": 22822
                    },
                    "type": "sha256",
                    "pulse_info": {
                        "count": 11,
                        "pulses": [{
                            "pulse_source": "api",
                            "references": ["https://metadefender.opswat.com/threat-intelligence-feeds"],
                            "subscriber_count": 568,
                            "modified_text": "95 days ago",
                            "is_subscribing": "None",
                            "votes_count": 0,
                            "vote": 0,
                            "id": "5bbf59f5d47a1b46ca035bde",
                            "industries": [],
                            "author": {
                                "username": "Metadefender",
                                "is_subscribed": 0,
                                "avatar_url": "https://otx20-web-media.s3.amazonaws.com/media/avatars/user/resized/80/avatar.png",
                                "is_following": 0,
                                "id": "32153"
                            },
                            "cloned_from": "None",
                            "comment_count": 0,
                            "follower_count": 0,
                            "public": 1,
                            "indicator_type_counts": {
                                "FileHash-SHA1": 1000,
                                "FileHash-MD5": 1000,
                                "FileHash-SHA256": 1000
                            },
                            "TLP": "green",
                            "description": "Production malware has shown the following behaviors: injector,trojan,adware,sms,backdoor",
                            "tags": ["html", "win32", "js"],
                            "in_group": "False",
                            "is_modified": "False",
                            "upvotes_count": 0,
                            "targeted_countries": [],
                            "groups": [],
                            "validator_count": 0,
                            "threat_hunter_scannable": "True",
                            "is_author": "False",
                            "adversary": " ",
                            "name": "Production malware on Metadefender.com",
                            "locked": 0,
                            "observation": {
                                "pulse_source": "api",
                                "references": ["https://metadefender.opswat.com/threat-intelligence-feeds"],
                                "subscriber_count": 2,
                                "is_subscribed": 0,
                                "author_name": "Metadefender",
                                "is_subscribing": "None",
                                "is_following": 0,
                                "vote": 0,
                                "id": "5bbf59f5d47a1b46ca035bde",
                                "industries": [],
                                "cloned_from": "None",
                                "comment_count": 0,
                                "avatar_url": "https://otx20-web-media.s3.amazonaws.com/media/avatars/user/resized/80/avatar.png",
                                "follower_count": 0,
                                "public": 1,
                                "revision": 1,
                                "indicator_type_counts": {
                                    "FileHash-SHA1": 1000,
                                    "FileHash-MD5": 1000,
                                    "FileHash-SHA256": 1000
                                },
                                "description": "Production malware has shown the following behaviors: injector,trojan,adware,sms,backdoor",
                                "tags": ["html", "win32", "js"],
                                "upvotes_count": 0,
                                "targeted_countries": [],
                                "groups": [],
                                "validator_count": 0,
                                "adversary": " ",
                                "tlp": "green",
                                "locked": 0,
                                "name": "Production malware on Metadefender.com",
                                "created": "2018-10-11T14:11:01.432000",
                                "downvotes_count": 0,
                                "modified": "2018-10-11T14:11:01.432000",
                                "export_count": 3,
                                "extract_source": [],
                                "votes_count": 0,
                                "author_id": 32153,
                                "user_subscriber_count": 566
                            },
                            "created": "2018-10-11T14:11:01.432000",
                            "downvotes_count": 0,
                            "modified": "2018-10-11T14:11:01.432000",
                            "export_count": 3,
                            "indicator_count": 3000,
                            "is_following": 0
                        }],
                        "references": ["https: //metadefender.opswat.com/results?utm_medium=reference&amp"]
                    }}},
            "Entity": "123a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fasd"
        }
    ]
    

### Ping

Test the connectivity.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
