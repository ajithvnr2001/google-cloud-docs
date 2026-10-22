---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/threatq/
title: ThreatQ \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:21.757949+00:00
---

# ThreatQ  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/threatq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ThreatQ

This document provides guidance on how to integrate ThreatQ with Google SecOps.

## Release Notes

Customers who have a PS version of the ThreatQ integration will have to update their playbooks to align with the new integration version. "Get incident details" will not enrich entities. Instead, we have other actions for this purpose.

## Configure ThreatQ integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | Unchecked | No | Name of the Instance you intend to configure integration for.  
Description | String | Unchecked | No | Description of the Instance.  
ServerAddress | String | xx.xx.xx.xx | Yes | Address of the ThreatQ instance.  
ClientId | String | N/A | Yes | ClientId for ThreatQ API  
Username | String | N/A | Yes | Email of the user.  
Password | Password | N/A | Yes | The password of the according user.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### EnrichCVE

#### Description

Enrich a CVE using ThreatQ information.

#### Parameters

**Name** | **Type** | **Default** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Score Threshold | Integer | 5 | No | Set the acceptable score threshold for the entity. If the score exceeds the specified threshold, the entity will be marked as suspicious.  
Show Sources | Checkbox | Checked | No | If enabled, action will return an additional table with related sources.  
Show Comments | Checkbox | Checked | No | If enabled, action will return an additional table with related comments.  
Show Attributes | Checkbox | Checked | No | If enabled, action will return an additional table with related attributes.  
Mark Whitelisted Entities As Suspicious | Checkbox | Checked | Yes | If enabled, action will mark entities as suspicious if they passed the allowed threshold, even if the entity is whitelisted in ThreatQ.  
  
#### Run On

This action runs on the CVE entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "total": 1,
                "data": [{
                    "status": {
                        "description": "No longer poses a serious threat.",
                        "name": "Expired",
                        "id": 2
                    },
                    "hash": "f74ee458b6e12452a04c6595bb3cd2d9",
                    "adversaries": [],
                    "status_id": 2,
                    "created_at": "2020-04-15 13:37:43",
                    "type_id": 5,
                    "updated_at": "2020-04-15 13:37:43",
                    "value": "star@star.star",
                    "id": 36,
                    "touched_at": "2020-04-15 13:37:43",
                    "sources": [{
                        "name": "Domain Tools",
                        "source_type": "plugins",
                        "creator_source_id": 8,
                        "created_at": "2020-04-15 13:37:43",
                        "indicator_type_id": 5,
                        "updated_at": "2020-04-15 13:37:43",
                        "indicator_status_id": 2,
                        "indicator_id": 36,
                        "published_at": "2020-04-15 13:37:43",
                        "reference_id": 1,
                        "source_id": 5,
                        "id": 44
                    }],
                    "published_at": "2020-04-15 13:37:43",
                    "score": 0,
                    "type": {
                        "class": "network",
                        "name": "Email Address",
                        "id": 5
                    },
                    "class": "network",
                    "expired_at": "2020-04-15 13:37:43"
                }]},
            "Entity": "email@example.com"
        }
    ]
    

### EnrichEmail

#### Description

Enrich an email address using ThreatQ information.

#### Parameters

**Name** | **Type** | **Default** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Score Threshold | Integer | 5 | No | Set the acceptable score threshold for the entity. If the score exceeds the specified threshold, the entity will be marked as suspicious.  
Show Sources | Checkbox | Checked | No | If enabled, action will return an additional table with related sources.  
Show Comments | Checkbox | Checked | No | If enabled, action will return an additional table with related comments.  
Show Attributes | Checkbox | Checked | No | If enabled, action will return an additional table with related attributes.  
Mark Whitelisted Entities As Suspicious | Checkbox | Checked | Yes | If enabled, action will mark entities as suspicious if they passed the allowed threshold, even if the entity is whitelisted in ThreatQ.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "total": 1,
                "data": [{
                    "status": {
                        "description": "No longer poses a serious threat.",
                        "name": "Expired",
                        "id": 2
                    },
                    "hash": "f74ee458b6e12452a04c6595bb3cd2d9",
                    "adversaries": [],
                    "status_id": 2,
                    "created_at": "2020-04-15 13:37:43",
                    "type_id": 5,
                    "updated_at": "2020-04-15 13:37:43",
                    "value": "star@star.star",
                    "id": 36,
                    "touched_at": "2020-04-15 13:37:43",
                    "sources": [{
                        "name": "Domain Tools",
                        "source_type": "plugins",
                        "creator_source_id": 8,
                        "created_at": "2020-04-15 13:37:43",
                        "indicator_type_id": 5,
                        "updated_at": "2020-04-15 13:37:43",
                        "indicator_status_id": 2,
                        "indicator_id": 36,
                        "published_at": "2020-04-15 13:37:43",
                        "reference_id": 1,
                        "source_id": 5,
                        "id": 44
                    }],
                    "published_at": "2020-04-15 13:37:43",
                    "score": 0,
                    "type": {
                        "class": "network",
                        "name": "Email Address",
                        "id": 5
                    },
                    "class": "network",
                    "expired_at": "2020-04-15 13:37:43"
                }]},
            "Entity": "email@example.com"
        }
    ]
    

### EnrichHash

#### Description

Enrich a Hash using ThreatQ information.

#### Parameters

**Name** | **Type** | **Default** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Score Threshold | Integer | 5 | No | Set the acceptable score threshold for the entity. If the score exceeds the specified threshold, the entity will be marked as suspicious.  
Show Sources | Checkbox | Checked | No | If enabled, action will return an additional table with related sources.  
Show Comments | Checkbox | Checked | No | If enabled, action will return an additional table with related comments.  
Show Attributes | Checkbox | Checked | No | If enabled, action will return an additional table with related attributes.  
Mark Whitelisted Entities As Suspicious | Checkbox | Checked | Yes | If enabled, action will mark entities as suspicious if they passed the allowed threshold, even if the entity is whitelisted in ThreatQ.  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "total": 1,
                "data": [{
                    "status": {
                        "description": "Poses a threat and is being exported to detection tools.",
                        "name": "Active",
                        "id": 1
                    },
                    "hash": "8b168f614b40150266d304dbd5c78036",
                    "adversaries": [],
                    "status_id": 1,
                    "created_at": "2020-03-11 11:26:32",
                    "tags": ["malware", "trojan"],
                    "updated_at": "2020-04-07 13:08:42",
                    "value": "d41d8cd98f00b204e9800998ecf8427e",
                    "id": 2,
                    "touched_at": "2020-04-07 13:08:42",
                    "sources": [{
                        "name": "Domain Tools",
                        "source_type": "plugins",
                        "creator_source_id": 8,
                        "created_at": "2020-03-15 15:04:31",
                        "indicator_type_id": 18,
                        "updated_at": "2020-03-15 15:04:31",
                        "indicator_status_id": 1,
                        "indicator_id": 2,
                        "published_at": "2020-03-15 15:04:31",
                        "reference_id": 1,
                        "source_id": 5,
                        "id": 7
                    }, {
                        "name": "tip.labops@siemplify.co",
                        "source_type": "users",
                        "creator_source_id": 8,
                        "created_at": "2020-03-11 11:26:32",
                        "indicator_type_id": 18,
                        "updated_at": "2020-03-11 12:25:17",
                        "indicator_status_id": 1,
                        "indicator_id": 2,
                        "published_at": "2020-03-11 11:26:32",
                        "reference_id": 1,
                        "source_id": 8,
                        "id": 2
                    }],
                    "published_at": "2020-03-11 11:26:32",
                    "score": 10,
                    "comments": [{
                        "source_name": "tip.labops@siemplify.co",
                        "creator_source_id": 8,
                        "created_at": "2020-03-11 12:32:22",
                        "updated_at": "2020-03-11 12:32:22",
                        "value": "Comment",
                        "indicator_id": 2,
                        "id": 1
                    }],
                    "type_id": 18,
                    "attributes": [{
                        "name": "Category",
                        "created_at": "2020-03-11 11:28:58",
                        "updated_at": "2020-03-11 11:28:58",
                        "value": "Malware",
                        "touched_at": "2020-03-11 11:28:58",
                        "indicator_id": 2,
                        "attribute_id": 1,
                        "id": 1
                    }, {
                        "name": "VirusTotal: Permalink",
                        "created_at": "2020-03-11 12:34:47",
                        "updated_at": "2020-03-11 12:34:47",
                        "value": "https:\/\/www.virustotal.com\/file\/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\/analysis\/1583929494\/",
                        "touched_at": "2020-03-11 12:34:47",
                        "indicator_id": 2,
                        "attribute_id": 3,
                        "id": 2
                    }],
                    "type": {
                        "class": "host",
                        "name": "MD5",
                        "id": 18
                    },
                    "class": "host"
                }]},
            "Entity": "d41d8cd98f00b204e9800998ecf8427e"
        }, {
            "EntityResult": {
                "total": 1,
                "data": [{
                    "status": {
                        "description": "No longer poses a serious threat.",
                        "name": "Expired",
                        "id": 2
                    },
                    "hash": "4ca64ed42f6f4e49f1775e5c63d371cd",
                    "description": "<p>Test&nbsp;\u05D3 \u05DE\u05D5\u05E0\u05D7\u05D9\u05DD \u05DE\u05D5\u05E2\u05DE\u05D3\u05D9\u05DD \u05E9\u05DC, \u05D3\u05EA \u05D3\u05E4\u05D9\u05DD \u05DE\u05D0\u05DE\u05E8\u05E9\u05D9\u05D7\u05D4\u05E6\u05E4\u05D4 \u05D6\u05D0<\/p>",
                    "adversaries": [],
                    "status_id": 2,
                    "created_at": "2020-04-08 12:47:35",
                    "type_id": 23,
                    "updated_at": "2020-04-09 08:00:35",
                    "value": "8e545e1c31f91f777c894b3bd2c2e7d7044cc9dd",
                    "id": 25,
                    "touched_at": "2020-04-09 08:01:42",
                    "sources": [{
                        "name": "Investigation1",
                        "source_type": "other_sources",
                        "creator_source_id": 8,
                        "created_at": "2020-04-08 12:47:35",
                        "indicator_type_id": 23,
                        "updated_at": "2020-04-08 12:47:35",
                        "indicator_status_id": 2,
                        "indicator_id": 25,
                        "published_at": "2020-04-08 12:47:35",
                        "reference_id": 1,
                        "source_id": 9,
                        "id": 27
                    }, {
                        "name": "\u05D3\u05EA \u05D3\u05E4\u05D9\u05DD \u05DE\u05D0\u05DE\u05E8\u05E9\u05D9\u05D7\u05D4\u05E6\u05E4",
                        "source_type": "other_sources",
                        "creator_source_id": 8, "created_at": "2020-04-09 08:01:42",
                        "indicator_type_id": 23,
                        "updated_at": "2020-04-09 08:01:42",
                        "indicator_status_id": 2,
                        "indicator_id": 25,
                        "published_at": "2020-04-09 08:01:42",
                        "reference_id": 2,
                        "source_id": 10,
                        "id": 32
                    }],
                    "published_at": "2020-04-08 12:47:35",
                    "score": 0,
                    "type": {
                        "class": "host",
                        "name": "SHA-1",
                        "id": 23
                    },
                    "class": "host",
                    "expired_at": "2020-04-08 12:47:35"
                }]},
            "Entity": "8e545e1c31f91f777c894b3bd2c2e7d7044cc9dd"
        }
    ]
    

### Enrich IP

#### Description

Enrich an IP using ThreatQ information.

#### Parameters

**Name** | **Type** | **Default** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Score Threshold | Integer | 5 | No | Set the acceptable score threshold for the entity. If the score exceeds the specified threshold, the entity will be marked as suspicious.  
Show Sources | Checkbox | Checked | No | If enabled, action will return an additional table with related sources.  
Show Comments | Checkbox | Checked | No | If enabled, action will return an additional table with related comments.  
Show Attributes | Checkbox | Checked | No | If enabled, action will return an additional table with related attributes.  
Mark Whitelisted Entities As Suspicious | Checkbox | Checked | Yes | If enabled, action will mark entities as suspicious if they passed the allowed threshold, even if the entity is whitelisted in ThreatQ.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "total": 1,
                "data": [{
                    "status": {
                        "description": "No longer poses a serious threat.",
                        "name": "Expired",
                        "id": 2
                    },
                    "hash": "cb8036b0a7a0ebeeff97a5fe620c4b2c",
                    "description": "<p>\u05D3\u05EA \u05D3\u05E4\u05D9\u05DD \u05DE\u05D0\u05DE\u05E8\u05E9\u05D9\u05D7\u05D4\u05E6\u05E4<\/p>",
                    "adversaries": [],
                    "status_id": 2,
                    "created_at": "2020-04-08 13:09:02",
                    "type_id": 15,
                    "updated_at": "2020-04-09 08:46:43",
                    "value": "8.8.8.8",
                    "id": 27,
                    "touched_at": "2020-04-09 08:46:50",
                    "sources": [{
                        "name": "\u05D3\u05EA \u05D3\u05E4\u05D9\u05DD \u05DE\u05D0\u05DE\u05E8\u05E9\u05D9\u05D7\u05D4\u05E6\u05E4",
                        "source_type": "other_sources",
                        "creator_source_id": 8,
                        "created_at": "2020-04-08 13:09:02",
                        "indicator_type_id": 15,
                        "updated_at": "2020-04-08 13:10:11",
                        "indicator_status_id": 2,
                        "indicator_id": 27,
                        "published_at": "2020-04-08 13:09:02",
                        "reference_id": 2,
                        "source_id": 10,
                        "id": 30
                    }],
                    "published_at": "2020-04-08 13:09:02",
                    "score": 0,
                    "comments": [{
                        "source_name": "example@mail.com",
                        "creator_source_id": 8,
                        "created_at": "2020-04-09 08:46:50",
                        "updated_at": "2020-04-09 08:46:50",
                        "value": "\u05D3\u05EA \u05D3\u05E4\u05D9\u05DD \u05DE\u05D0\u05DE\u05E8\u05E9\u05D9\u05D7\u05D4\u05E6\u05E4awdwqwq",
                        "indicator_id": 27,
                        "id": 5
                    }],
                    "attributes": [{
                        "name": "\u05D3\u05EA \u05D3\u05E4\u05D9\u05DD \u05DE\u05D0\u05DE\u05E8\u05E9\u05D9\u05D7\u05D4\u05E6\u05E4",
                        "created_at": "2020-04-09 08:46:26",
                        "updated_at": "2020-04-09 08:46:26",
                        "value": "hvvhv",
                        "touched_at": "2020-04-09 08:46:26",
                        "indicator_id": 27,
                        "attribute_id": 4,
                        "id": 6
                    }],
                    "type": {
                        "class": "network",
                        "name": "IP Address",
                        "id": 15
                    },
                    "class": "network",
                    "expired_at": "2020-04-08 13:10:11"
                }]},
            "Entity": "8.8.8.8"
        }
    ]
    

### Enrich URL

#### Description

Enrich an URL using ThreatQ information.

#### Parameters

**Name** | **Type** | **Default** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Score Threshold | Integer | 5 | No | Set the acceptable score threshold for the entity. If the score exceeds the specified threshold, the entity will be marked as suspicious.  
Show Sources | Checkbox | Checked | No | If enabled, action will return an additional table with related sources.  
Show Comments | Checkbox | Checked | No | If enabled, action will return an additional table with related comments.  
Show Attributes | Checkbox | Checked | No | If enabled, action will return an additional table with related attributes.  
Mark Whitelisted Entities As Suspicious | Checkbox | Checked | Yes | If enabled, action will mark entities as suspicious if they passed the allowed threshold, even if the entity is whitelisted in ThreatQ.  
  
#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "total": 1,
                "data": [{
                    "status": {
                        "description": "Poses a threat and is being exported to detection tools.",
                        "name": "Active",
                        "id": 1
                    },
                    "hash": "e216253c1198b44c99c6841899c68418",
                    "adversaries": [],
                    "status_id": 1,
                    "created_at": "2020-04-08 08:59:59",
                    "type_id": 30,
                    "updated_at": "2020-04-08 08:59:59",
                    "value": "example2.sk",
                    "id": 19,
                    "touched_at": "2020-04-08 08:59:59",
                    "sources": [{
                        "name": "tip.labops@siemplify.co",
                        "source_type": "users",
                        "creator_source_id": 8,
                        "created_at": "2020-04-08 08:59:59",
                        "indicator_type_id": 30,
                        "updated_at": "2020-04-08 08:59:59",
                        "indicator_status_id": 1,
                        "indicator_id": 19,
                        "published_at": "2020-04-08 08:59:59",
                        "reference_id": 1,
                        "source_id": 8,
                        "id": 21
                    }],
                    "published_at": "2020-04-08 08:59:59",
                    "score": 0,
                    "expires_calculated_at": "2020-04-08 09:00:01",
                    "type": {
                        "class": "network",
                        "name": "URL",
                        "id": 30
                    },
                    "class": "network"
                }]},
            "Entity": "example2.sk"
        }, {
            "EntityResult": {
                "total": 1,
                "data": [{
                    "status": {
                        "description": "Poses a threat and is being exported to detection tools.",
                        "name": "Active",
                        "id": 1
                    },
                    "hash": "69d4269b838ce143e6f0656384c58ff8",
                    "description": "<p>URL<\/p>",
                    "adversaries": [],
                    "status_id": 1,
                    "created_at": "2020-03-15 15:49:04",
                    "tags": ["URL"],
                    "updated_at": "2020-03-15 15:51:13",
                    "value": "www.example.com",
                    "id": 7,
                    "touched_at": "2020-03-15 15:51:13",
                    "sources": [{
                        "name": "Emerging Threats",
                        "source_type": "plugins",
                        "creator_source_id": 8,
                        "created_at": "2020-03-15 15:49:04",
                        "indicator_type_id": 30,
                        "updated_at": "2020-03-15 15:49:04",
                        "indicator_status_id": 1,
                        "indicator_id": 7,
                        "published_at": "2020-03-15 15:49:04",
                        "reference_id": 2,
                        "source_id": 6,
                        "id": 9
                    }],
                    "published_at": "2020-03-15 15:49:04",
                    "score": 0,
                    "expires_calculated_at": "2020-03-15 15:50:02",
                    "type_id": 30,
                    "attributes": [{
                        "name": "Category",
                        "created_at": "2020-03-15 15:51:03",
                        "updated_at": "2020-03-15 15:51:03",
                        "value": "Malware",
                        "touched_at": "2020-03-15 15:51:03",
                        "indicator_id": 7,
                        "attribute_id": 1,
                        "id": 5
                    }],
                    "type": {
                        "class": "network",
                        "name": "URL",
                        "id": 30
                    },
                    "class": "network"
                }]},
            "Entity": "www.example.com"
        }
    ]
    

### Get Indicator Details

#### Description

Get the details for an IP address in a CSV format.

#### Parameters

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
null | N/A | N/A  
  
### Ping

#### Description

Verifies that the user has a connection to ThreatQ via the user's device.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_connect | True/False | is_connect:False  
  
### Create Indicator

#### Description

Create an indicator in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Indicator Type | DDL | ASNPossible Values:ASNBinary StringCIDR BlockCVEEmail AddressEmail AttachmentEmail SubjectFile MappingFile PathFile nameFQDNFuzzy HashGOST HashHash IONIPv4 AddressIPv6 AddressMAC AddressMD5MutexPasswordRegistry KeyService NameFile HashSHA-1SHA-256SHA-384SHA-512StringURLURL PathUser-agentUsernameX-Mailerx509 Serialx509 Subject | Yes | Specify the type of the new indicator.  
Status | DDL | ActivePossible values:ActiveExpiredIndirectReviewWhitelisted | Yes | Specify the status of the new indicator.  
Description | String | N/A | No | Specify description of the new indicator.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "total": 1,
        "data": [
            {
                "id": 24,
                "type_id": 7,
                "status_id": 1,
                "class": "network",
                "hash": "ee8c2ae6818a9bb8c3b644ab1d3b2777",
                "value": "115.47.67.161",
                "description": "Kek",
                "last_detected_at": null,
                "expires_at": null,
                "expired_at": null,
                "expires_needs_calc": "Y",
                "expires_calculated_at": null,
                "created_at": "2020-07-20 07:26:52",
                "updated_at": "2020-07-20 07:35:06",
                "touched_at": "2020-07-20 07:35:06",
                "existing": "Y",
                "type": {
                    "id": 7,
                    "name": "Email Subject",
                    "class": "network",
                    "score": null,
                    "wildcard_matching": "Y",
                    "created_at": "2020-06-29 17:13:29",
                    "updated_at": "2020-06-29 17:13:29"
                }
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _if successful and at least one of the provided entities successfully created an indicator (is_success = true):_ print "Successfully created indicators in ThreatQ based on the following entities: \n {0}".format(entity.identifier list)  _If fail to create indicators based on the specific entities(is_success = true):_ print "Action was not able to create indicators in ThreatQ based on the following entities: \n{0}".format([entity.identifier]) _If fail to enrich for all entities (is_success = false):_ print: "No indicators were created." **The action should fail and stop a playbook execution:** _if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Create Indicator". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Adversary

#### Description

Create an adversary in ThreatQ.

#### Parameters

N/A

#### Run On

This action runs on the User entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "name": "Adversary Nameaa",
            "updated_at": "2020-07-20 08:21:34",
            "created_at": "2020-07-20 08:21:34",
            "id": 11
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided entities successfully created an adversary (is_success = true):_  
print "Successfully created adversaries in ThreatQ based on the following entities: \n {0}".format(entity.identifier list)___If fail to create adversaries based on the specific entities(is_success = true):_  
print "Action was not able to create adversaries in ThreatQ based on the following entities:\n {0}".format([entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ Print: "No adversaries were enriched."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Create Adversary". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Event

#### Description

Create an event in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Title | String | N/A | Yes | Specify the title of the event.  
Event Type | DDL | SpearphishPossible Values:SpearphishWatering HoleSQL Injection AttackDoS AttackMalwareWatchlistCommand and ControlAnonymizationExfiltrationHost CharacteristicsCompromised PKI CertificateLogin CompromiseIncidentSighting | Yes | Specify the type of the event.  
Happened At | String | N/A | Yes | Specify when the event happened. If nothing is entered in this field, action will use current time. Format: YYYY-MM-DD hh:mm:ss  
  
#### Run On

This action doesn't run on entity types.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "title": "Event Name",
            "type_id": 3,
            "happened_at": "2017-03-20 01:43:05",
            "hash": "e59c3274f3156b10aca1c8962a5880cb",
            "updated_at": "2020-07-20 08:40:53",
            "created_at": "2020-07-20 08:40:53",
            "touched_at": "2020-07-20 08:40:53",
            "id": 3,
            "type": {
                "id": 3,
                "name": "SQL Injection Attack",
                "user_editable": "N",
                "created_at": "2020-06-29 17:13:28",
                "updated_at": "2020-06-29 17:13:28"
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful (is_success = true):_  
print "Successfully created event '{0}' in ThreatQ".format(title)_If fail to create event (is_success = false):_ Print: "Event '{0}' was not created in ThreatQ. Reason: {1}".format(title, errors/[0].value)  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Create Event". Reason: {0}''.format(error.Stacktrace)  
_If incorrect time format is used:_ print "Error executing action "Create Event". Reason: Incorrect time format was passed to 'Happened At' action parameter. Should be YYYY-MM-DD hh:mm:ss.'' | General  
  
### Add Attribute

#### Description

Action adds an attribute to the object.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Object Type | DDL | AdversaryPossible Values:AdversaryAttack PatternCampaignCourse of ActionEventExploit TargetFileIdentityIncidentIndicatorIntrusion SetMalwareReportSignatureTTPVulnerability | Yes | Specify to which object type attribute should be added.  
Object Identifier | String | N/A | Yes | Specify the identifier of the object. For example, it can be an MD5 hash, title of the event, name of the adversary, etc.  
Indicator Type | DDL | ASNPossible Values:ASNBinary StringCIDR BlockCVEEmail AddressEmail AttachmentEmail SubjectFile MappingFile PathFile nameFQDNFuzzy HashGOST HashHash IONIPv4 AddressIPv6 AddressMAC AddressMD5MutexPasswordRegistry KeyService NameSHA-1SHA-256SHA-384SHA-512StringURLURL PathUser-agentUsernameX-Mailerx509 Serialx509 Subject | Yes | Specify the type of the indicator. This parameter is only used if Object Type is "Indicator"  
Attribute Name | String | N/A | Yes | Specify the name of the attribute.  
Attribute Value | String | N/A | Yes | Specify the value of the attribute  
Attribute Source | String | N/A | No | Specify the source of the attribute.  
  
#### Run On

This action doesn't run on entity types.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            {
                "attribute_id": 4,
                "value": "4012",
                "incident_id": 1,
                "id": 1,
                "created_at": "2020-07-20 13:29:29",
                "updated_at": "2020-07-20 13:29:29",
                "touched_at": "2020-07-20 13:29:29",
                "name": "321",
                "attribute": {
                    "id": 4,
                    "name": "321",
                    "created_at": "2020-07-20 13:21:09",
                    "updated_at": "2020-07-20 13:21:09"
                },
                "sources": [
                    {
                        "id": 10,
                        "type": "other_sources",
                        "reference_id": 2,
                        "name": "123 User",
                        "tlp_id": null,
                        "created_at": "2020-07-20 13:29:29",
                        "updated_at": "2020-07-20 13:29:29",
                        "published_at": null,
                        "pivot": {
                            "incident_attribute_id": 1,
                            "source_id": 10,
                            "id": 1,
                            "creator_source_id": 8
                        }
                    }
                ]
            }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful (is_success = true):_  
print "Successfully added attribute '{0}' to '{1}' object in ThreatQ".format(Attribute Name, Object Type)_If the object was not found (is_success = false):_ Print: "'{0}' object with value '{1}' was not found in ThreatQ.".format(Object Type, Object identifier)  
_If general error (is_success = false):_ Print "Action was not able to add attribute {0} to the ThreatQ object.".format(Attribute Name)**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "Add Attribute". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Source

#### Description

Action adds a source to the object.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Object Type | DDL | AdversaryPossible Values:AdversaryAttack PatternCampaignCourse of ActionEventExploit TargetFileIdentityIncidentIndicatorIntrusion SetMalwareReportSignatureTTPVulnerability | Yes | Specify to which object type source should be added.  
Object Identifier | String | N/A | Yes | Specify the identifier of the object. For example, it can be an MD5 hash, title of the event, name of the adversary, etc.  
Indicator Type | DDL | ASNPossible Values:ASNBinary StringCIDR BlockCVEEmail AddressEmail AttachmentEmail SubjectFile MappingFile PathFile nameFQDNFuzzy HashGOST HashHash IONIPv4 AddressIPv6 AddressMAC AddressMD5MutexPasswordRegistry KeyService NameSHA-1SHA-256SHA-384SHA-512StringURLURL PathUser-agentUsernameX-Mailerx509 Serialx509 Subject | Yes | Specify the type of indicator. This parameter is only used if Object Type is "Indicator".  
Source Name | String | N/A | Yes | Specify the name of the source.  
  
#### Run On

This action doesn't run on entity types.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "total": 1,
        "data": [
            {
                "id": 3,
                "incident_id": 1,
                "source_id": 11,
                "creator_source_id": 8,
                "tlp_id": null,
                "created_at": "2020-07-20 14:12:52",
                "updated_at": "2020-07-20 14:12:52",
                "published_at": null,
                "deleted_at": null,
                "existing": 0,
                "name": "321"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful (is_success = true):_  
print "Successfully added source '{0}' to '{1}' object in ThreatQ".format(Source Name, Object Type)_If the object was not found (is_success = false):_ Print: "'{0}' object with value '{1}' was not found in ThreatQ.".format(Object Type, Object Value)  
_If general error (is_success = false):_ Print "Action was not able to add source {0} to the ThreatQ object.".format(Source Name)**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "Add Source". Reason: {0}''.format(error.Stacktrace) | General  
  
### Link Entities

#### Description

Action links all of the entities in ThreatQ.

#### Run On

This action runs on the following entities:

  * CVE
  * IP Address
  * URL
  * Filehash
  * User
  * All entities matching email regex



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "id": 1,
            "type_id": 18,
            "status_id": 2,
            "class": "host",
            "hash": "6677d693422fbeb541397fb8554f4664",
            "value": "7815696ecbf1c96e6894b779456d330e",
            "description": null,
            "last_detected_at": null,
            "expires_at": null,
            "expired_at": "2020-07-21 09:05:56",
            "expires_needs_calc": "N",
            "expires_calculated_at": "2020-07-21 07:35:02",
            "created_at": "2020-07-19 09:17:20",
            "updated_at": "2020-07-21 09:05:56",
            "touched_at": "2020-07-21 09:05:56"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful and at least one of the provided entities successfully linked (is_success = true):_  
print "Successfully linked the following entities in ThreatQ: \n {1}".format(entity.identifier list)___If fail to list related objects for specific entities(is_success = true):_ print "Action was not able to link the following entities in ThreatQ: \n{0}".format([entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ Print: "No entities were linked."  
_If only one entity is provided:_  
Print "No entities were linked. Reason: Only one entity was provided."  
  
**The action should fail and stop a playbook execution:**_If fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Link Entities". Reason: {0}''.format(error.Stacktrace) | General  
  
### Link Entities To Object

#### Description

Action links all of the entities in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Object Type | DDL | AdversaryPossible Values:AdversaryAttack PatternCampaignCourse of ActionEventExploit TargetFileIdentityIncidentIndicatorIntrusion SetMalwareReportSignatureTaskToolTTPVulnerability | Yes | Specify the type of the object to which you want to link entities.  
Object Identifier | String | N/A | Yes | Specify identifier of the object to which you want to link entities. For example, it can be an MD5 hash, title of the event, name of the adversary etc.  
Indicator Type | DDL | ASNPossible Values:ASNBinary StringCIDR BlockCVEEmail AddressEmail AttachmentEmail SubjectFile MappingFile PathFile nameFQDNFuzzy HashGOST HashHash IONIPv4 AddressIPv6 AddressMAC AddressMD5MutexPasswordRegistry KeyService NameSHA-1SHA-256SHA-384SHA-512StringURLURL PathUser-agentUsernameX-Mailerx509 Serialx509 Subject | No | Specify the type of the indicator to which you want to link entities. This parameter is only used, if Source Object Type is "Indicator"**.**  
  
#### Run On

This action runs on the following entities:

  * CVE
  * IP Address
  * URL
  * Filehash
  * User
  * All entities matching email regex



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "id": 1,
            "type_id": 18,
            "status_id": 2,
            "class": "host",
            "hash": "6677d693422fbeb541397fb8554f4664",
            "value": "7815696ecbf1c96e6894b779456d330e",
            "description": null,
            "last_detected_at": null,
            "expires_at": null,
            "expired_at": "2020-07-21 09:05:56",
            "expires_needs_calc": "N",
            "expires_calculated_at": "2020-07-21 07:35:02",
            "created_at": "2020-07-19 09:17:20",
            "updated_at": "2020-07-21 09:05:56",
            "touched_at": "2020-07-21 09:05:56"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If object was not found (is_success = false):_ Print: "No entities were linked to object '{0}' with value '{1}'. Reason: '{0}' object with value '{1}' was not found in ThreatQ.".format(Object Type, Object Value)  
_If successful and at least one of the provided entities successfully linked (is_success = true):_  
print "Successfully linked the following entities to object '{0}' with value '{1}' in ThreatQ: \n {2}".format(Object Type, Object Identifier, entity.identifier list)_If fail to list related objects for specific entities(is_success = true):_ print "Action was not able to link the following entities to object '{0}' with value '{1}' in ThreatQ: \n{2}".format(Object Type, Object Identifier, [entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ Print: "No entities were linked to object '{0}' with value '{1}'.".format(Object Type, Object Identifier)  
  
**The action should fail and stop a playbook execution:**_If fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Link Entities To Object". Reason: {0}''.format(error.Stacktrace)  
| General  
  
### Link Objects

#### Description

Action links two objects in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Source Object Type | DDL | AdversaryPossible Values:AdversaryAttack PatternCampaignCourse of ActionEventExploit TargetFileIdentityIncidentIndicatorIntrusion SetMalwareReportSignatureTaskToolTTPVulnerability | Yes | Specify the type of the source object.  
Source Object Identifier | String | N/A | Yes | Specify identifier of the source object. For example, it can be an MD5 hash, title of the event, name of the adversary etc.  
Source Indicator Type | DDL | ASNPossible Values:ASNBinary StringCIDR BlockCVEEmail AddressEmail AttachmentEmail SubjectFile MappingFile PathFile nameFQDNFuzzy HashGOST HashHash IONIPv4 AddressIPv6 AddressMAC AddressMD5MutexPasswordRegistry KeyService NameSHA-1SHA-256SHA-384SHA-512StringURLURL PathUser-agentUsernameX-Mailerx509 Serialx509 Subject | No | Specify the type of the source indicator. This parameter is only used, if Source Object Type is "Indicator".  
Destination Object Type | DDL | AdversaryPossible Values:AdversaryAttack PatternCampaignCourse of ActionEventExploit TargetFileIdentityIncidentIndicatorIntrusion SetMalwareReportSignatureTaskToolTTPVulnerability | Yes | Specify the type of the destination object.  
Destination Object Identifier | String | N/A | Yes | Specify the identifier of the destination object. For example, it can be an MD5 hash, title of the event, name of the adversary, etc.  
Destination Indicator Type | DDL | ASNPossible Values:ASNBinary StringCIDR BlockCVEEmail AddressEmail AttachmentEmail SubjectFile MappingFile PathFile nameFQDNFuzzy HashGOST HashHash IONIPv4 AddressIPv6 AddressMAC AddressMD5MutexPasswordRegistry KeyService NameSHA-1SHA-256SHA-384SHA-512StringURLURL PathUser-agentUsernameX-Mailerx509 Serialx509 Subject | No | Specify the type of the destination indicator. This parameter is only used if Destination Object Type is "Indicator".  
  
#### Run On

This action doesn't run on entity types.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
                "id": 2,
                "value": "123123",
                "status_id": null,
                "type_id": null,
                "description": null,
                "started_at": "2020-07-20 12:27:00",
                "ended_at": "2020-07-20 12:27:00",
                "created_at": "2020-07-20 12:27:10",
                "updated_at": "2020-07-20 12:27:10",
                "touched_at": "2020-07-20 14:50:14",
                "object_id": 4,
                "object_code": "incident",
                "object_name": "Incident",
                "object_name_plural": "Incidents",
                "pivot": {
                    "id": 18,
                    "created_at": "2020-07-20 14:50:14",
                    "updated_at": "2020-07-20 14:50:14"
                }
            }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful (is_success = true):_  
print "Successfully linked objects in ThreatQ"___If object was not found (is_success = false):_ Print: "'{0}' object with value '{1}' was not found in ThreatQ.".format(Object Type, Object Value)  
_If general error (is_success = false):_ print "Action was not able to link objects in ThreatQ."**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "Link Objects". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Related Objects

#### Description

Action lists related objects in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Source Object Type | DDL | AdversaryPossible Values:AdversaryAttack PatternCampaignCourse of ActionEventExploit TargetFileIdentityIncidentIndicatorIntrusion SetMalwareReportSignatureTaskToolTTPVulnerability | Yes | Specify the type of the source object.  
Source Object Identifier | String | N/A | Yes | Specify the identifier of the source object. For example, it can be an MD5 hash, title of the event, name of the adversary, etc.  
Source Indicator Type | DDL | ASNPossible Values:ASNBinary StringCIDR BlockCVEEmail AddressEmail AttachmentEmail SubjectFile MappingFile PathFile nameFQDNFuzzy HashGOST HashHash IONIPv4 AddressIPv6 AddressMAC AddressMD5MutexPasswordRegistry KeyService NameSHA-1SHA-256SHA-384SHA-512StringURLURL PathUser-agentUsernameX-Mailerx509 Serialx509 Subject | No | Specify the type of the source indicator. This parameter is only used, if Source Object Type is "Indicator".  
Related Object Type | DDL | AdversaryPossible Values:AdversaryAttack PatternCampaignCourse of ActionEventExploit TargetFileIdentityIncidentIndicatorIntrusion SetMalwareReportSignatureTaskToolTTPVulnerability | Yes | Specify the type of the related object that needs to be returned.  
Max Related Objects To Return | Integer | 50 | No | Specify how many related objects to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "total": 2,
        "data": [
            {
                "id": 1,
                "value": "Incident 1",
                "status_id": null,
                "type_id": null,
                "description": null,
                "started_at": "2020-07-09 06:15:00",
                "ended_at": "2020-07-09 06:15:00",
                "created_at": "2020-07-09 06:16:10",
                "updated_at": "2020-07-09 06:16:10",
                "touched_at": "2020-07-21 06:53:33",
                "deleted_at": null,
                "pivot": {
                    "id": 20,
                    "src_type": "indicator",
                    "src_object_id": 1,
                    "dest_type": "incident",
                    "dest_object_id": 1,
                    "created_at": "2020-07-21 06:53:33",
                    "updated_at": "2020-07-21 06:53:33"
                }
            },
            {
                "id": 2,
                "value": "123123",
                "status_id": null,
                "type_id": null,
                "description": null,
                "started_at": "2020-07-20 12:27:00",
                "ended_at": "2020-07-20 12:27:00",
                "created_at": "2020-07-20 12:27:10",
                "updated_at": "2020-07-20 12:27:10",
                "touched_at": "2020-07-21 06:53:49",
                "deleted_at": null,
                "pivot": {
                    "id": 21,
                    "src_type": "indicator",
                    "src_object_id": 1,
                    "dest_type": "incident",
                    "dest_object_id": 2,
                    "created_at": "2020-07-21 06:53:49",
                    "updated_at": "2020-07-21 06:53:49"
                }
            }
        ],
        "limit": 2,
        "offset": 0
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful (is_success = true):_  
print "Successfully listed related objects in ThreatQ."_If Source object was not found (is_success = false):_ print: "'{0}' object with value '{1}' was not found in ThreatQ.".format(Object Type, Object Value)  
_If no there are no related objects for the Related Object Type : (is_success=false):_ Print "No related {0} object were found.".format(Related Object Type)_If general error (is_success = false):_ Print "Action was not able to list related objects in ThreatQ."******The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to the_ ****_server, other:_ print "Error executing action "List Related Objects". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table (Object type=Event) | **Table name:** Related 'Event' objects**Table Columns:**

  * ID (mapped as id)
  * Title (mapped as title)
  * Description (mapped as description)
  * Created At (mapped as created_at)
  * Updated At (mapped as updated_at)

| General  
Case Wall Table (Object type=File) | **Table name:** Related 'File' objects**Table Columns:**

  * ID (mapped as id)
  * Title (mapped as title)
  * Description (mapped as description)
  * Created At (mapped as created_at)
  * Updated At (mapped as updated_at)

| General  
Case Wall Table (Object type=Adversary) | **Table name:** Related 'Adversary' objects**Table Columns:**

  * ID (mapped as id)
  * Name (mapped as name)
  * Description (mapped as description)
  * Created At (mapped as created_at)
  * Updated At (mapped as updated_at)

| General  
Case Wall Table (Every other object type) | **Table name:** "Related '{0}' objects".format(Destination Object Type)**Table Columns:**

  * ID (mapped as id)
  * Name (mapped as value)
  * Description (mapped as description)
  * Created At (mapped as created_at)
  * Updated At (mapped as updated_at)

| General  
  
### List Entity Related Objects

#### Description

Action lists related objects for entities in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Related Object Type | DDL | AdversaryPossible Values:AdversaryAttack PatternCampaignCourse of ActionEventExploit TargetFileIdentityIncidentIndicatorIntrusion SetMalwareReportSignatureTaskToolTTPVulnerability | Yes | Specify the type of related object that needs to be returned.  
Max Related Objects To Return | Integer | 50 | No | Specify how many related objects to return. Maximum is 1000. This is a ThreatQ limitation.  
  
#### Run On

This action runs on all entity types.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
TQ_related_{0}_id.format(Related object type) | id | If available in JSON Result.  
TQ_related_{0}_value.format(Related object type) | value.If related object type = event and file:titleIf related object type = adversary:name | If available in JSON Result.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "total": 2,
        "data": [   
            {
                "id": 1,
                "value": "Incident 1",
                "status_id": null,
                "type_id": null,
                "description": null,
                "started_at": "2020-07-09 06:15:00",
                "ended_at": "2020-07-09 06:15:00",
                "created_at": "2020-07-09 06:16:10",
                "updated_at": "2020-07-09 06:16:10",
                "touched_at": "2020-07-21 06:53:33",
                "deleted_at": null,
                "pivot": {
                    "id": 20,
                    "src_type": "indicator",
                    "src_object_id": 1,
                    "dest_type": "incident",
                    "dest_object_id": 1,
                    "created_at": "2020-07-21 06:53:33",
                    "updated_at": "2020-07-21 06:53:33"
                }
            },
            {
                "id": 2,
                "value": "123123",
                "status_id": null,
                "type_id": null,
                "description": null,
                "started_at": "2020-07-20 12:27:00",
                "ended_at": "2020-07-20 12:27:00",
                "created_at": "2020-07-20 12:27:10",
                "updated_at": "2020-07-20 12:27:10",
                "touched_at": "2020-07-21 06:53:49",
                "deleted_at": null,
                "pivot": {
                    "id": 21,
                    "src_type": "indicator",
                    "src_object_id": 1,
                    "dest_type": "incident",
                    "dest_object_id": 2,
                    "created_at": "2020-07-21 06:53:49",
                    "updated_at": "2020-07-21 06:53:49"
                }
            }
        ],
        "limit": 2,
        "offset": 0
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided entities successfully created an indicator (is_success = true):_  
print "Successfully listed related '{0}' objects in ThreatQ for the following entities: \n {1}".format(related object type, entity.identifier list)_If fail to list related objects for specific entities(is_success = true):_  
print "Action was not able to list related '{0}' objects in ThreatQ for the following entities: \n{0}".format(related object type, [entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ Print: "No related objects were listed."**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "List Related Objects". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table (Object type=Event) | **Table name:** Related 'Event' objects for {entity identifier}**Table Columns:**

  * ID (mapped as id)
  * Title (mapped as title)
  * Created At (mapped as created_at)
  * Updated At (mapped as updated_at)

| General  
Case Wall Table (Object type=File) | **Table name:** Related 'File' objects for {entity identifier}**Table Columns:**

  * ID (mapped as id)
  * Title (mapped as title)
  * Description (mapped as description)
  * Created At (mapped as created_at)
  * Updated At (mapped as updated_at)

| General  
Case Wall Table (Object type=Adversary) | **Table name:** Related 'Adversary' objects for {entity identifier}**Table Columns:**

  * ID (mapped as id)
  * Name (mapped as name)
  * Description (mapped as description)
  * Created At (mapped as created_at)
  * Updated At (mapped as updated_at)

| General  
Case Wall Table (Every other object type) | **Table name:** "Related '{0}' objects for {entity identifier}".format(Destination Object Type)**Table Columns:**

  * ID (mapped as id)
  * Name (mapped as value)
  * Description (mapped as description)
  * Created At (mapped as created_at)
  * Updated At (mapped as updated_at)

| General  
  
### Create Object

#### Description

Create an object in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Object Type | DDL | Attack PatternPossible Values:Attack PatternCampaignCourse of ActionExploit TargetIdentityIncidentIntrusion SetMalwareReportToolTTPVulnerability | Yes | Specify the type of the object.  
Value | String | N/A | Yes | Specify the value of the new object.  
Description | String | N/A | No | Specify description to the new object.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
TQ_related_{0}_id.format(Related object type) | id | If available in JSON Result.  
TQ_related_{0}_value.format(Related object type) | value.If related object type = event and file:titleIf related object type = adversary:name | If available in JSON Result.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "value": "Adversary Nameaaa",
            "description": "Koko",
            "updated_at": "2020-07-21 08:46:55",
            "created_at": "2020-07-21 08:46:55",
            "id": 2,
            "object_id": 1,
            "object_code": "campaign",
            "object_name": "Campaign",
            "object_name_plural": "Campaigns"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful (is_success = true):_  
print "Successfully created new {0} object in ThreatQ.".format(object_type,)  
_If fail to create new action (is_success = false):_ Print: "Action was not able to create new {0} object in ThreatQ.".format(object_type)  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "Create Object". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Malware Details

#### Description

Action returns information about malware based on entities from ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Additional Information | String | N/A | No | Specify what additional fields should be included in the response. Possible values: adversaries, attackPattern, campaign, courseOfAction, attachments, attributes, comments, events, indicators, signatures, sources, status, tags, type, watchlist, exploitTarget, identity, incident, intrusionSet, malware, report, tool, ttp, vulnerability, tasks  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
TQ_malware_id | id | If available in JSON Result.  
TQ_malware_status_id | status_id | If available in JSON Result.  
TQ_malware_type_id | type_id | If available in JSON Result.  
TQ_malware_description | description | If available in JSON Result.  
TQ_malware_created_at | created_at | If available in JSON Result.  
TQ_malware_updated_at | updated_at | If available in JSON Result.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "total": 1,
        "data": [
            {
                "id": 1,
                "value": "Investigation1",
                "status_id": null,
                "type_id": null,
                "description": "<p>Investigation1</p>\n",
                "created_at": "2020-07-08 15:59:20",
                "updated_at": "2020-07-08 15:59:20",
                "touched_at": "2020-07-20 14:46:42",
                "object_id": 9,
                "object_code": "malware",
                "object_name": "Malware",
                "object_name_plural": "Malware",
                "adversaries": [],
                "attack_pattern": [],
                "campaign": [],
                "course_of_action": [],
                "attachments": [],
                "attributes": [],
                "comments": [],
                "events": [],
                "indicators": [],
                "signatures": [],
                "sources": [
                    {
                        "id": 5,
                        "type": "plugins",
                        "reference_id": 1,
                        "name": "Domain Tools",
                        "tlp_id": null,
                        "created_at": "2020-07-08 15:59:20",
                        "updated_at": "2020-07-08 15:59:20",
                        "published_at": null,
                        "pivot": {
                            "malware_id": 1,
                            "source_id": 5,
                            "id": 1,
                            "creator_source_id": 8
                        }
                    }
                ],
                "status": null,
                "tags": [],
                "type": null,
                "watchlist": [],
                "exploit_target": [],
                "identity": [],
                "incident": [],
                "intrusion_set": [],
                "malware": [],
                "report": [],
                "tool": [],
                "ttp": [],
                "vulnerability": [],
                "tasks": [
                    {
                        "id": 5,
                        "name": "Task2",
                        "description": "<p>Task2</p>\n",
                        "status_id": 1,
                        "priority": "Low",
                        "assignee_source_id": 8,
                        "creator_source_id": 8,
                        "due_at": null,
                        "completed_at": null,
                        "assigned_at": "2020-07-09 06:25:54",
                        "created_at": "2020-07-09 06:25:54",
                        "updated_at": "2020-07-09 06:25:54",
                        "pivot": {
                            "id": 9,
                            "created_at": "2020-07-09 06:25:55",
                            "updated_at": "2020-07-09 06:25:55"
                        }
                    }
                ]
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided entities successfully was enriched (is_success = true):_  
print "Successfully enriched the following entities: \n {1}".format(related object type, entity.identifier list)___If fail to list related objects for specific entities(is_success = true):_  
print "Action was not able to enrich the following entities: \n{0}".format(related object type, [entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ Print: "No entities were enriched."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "Get Malware Details". Reason: {0}''.format(error.Stacktrace) | General  
Link | **Name:** Details for {entity}**Link:** https://{server_ip}malware/{id}/details |   
  
### List Events

#### Description

List events from ThreatQ.‌

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Additional Fields | CSV | adversaries, attachments, attributes, comments, events, indicators, signatures, sources, spearphish, tags, type, watchlist. | No | Specify what additional fields should be included in the response. Possible values: adversaries, attachments, attributes, comments, events, indicators, signatures, sources, spearphish, tags, type, watchlist.  
Sort Field | DDL | IDPossible values:IDTitleCreated AtUpdated AtHappened At | No | Specify what field should be used for sorting events.  
Sort Direction | DDL | AscendingPossible Values: AscendingDescending | No | Specify the sorting direction.  
Max Events to Return | Integer | 50 | No | Specify how many events to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "total": 1,
        "data": [
            {
                "id": 1,
                "type_id": 4,
                "title": "Test",
                "description": null,
                "happened_at": "2020-07-19 09:19:00",
                "hash": "78f58dacd9c215003911a09d5b3e810d",
                "created_at": "2020-07-19 09:19:39",
                "updated_at": "2020-07-19 09:19:39",
                "touched_at": "2020-07-19 09:20:22",
                "adversaries": [],
                "attachments": [],
                "attributes": [],
                "comments": [],
                "events": [],
                "indicators": [
                    {
                        "id": 1,
                        "type_id": 18,
                        "status_id": 1,
                        "class": "host",
                        "hash": "6677d693422fbeb541397fb8554f4664",
                        "value": "7815696ecbf1c96e6894b779456d330e",
                        "description": null,
                        "last_detected_at": null,
                        "expires_at": null,
                        "expired_at": null,
                        "expires_needs_calc": "N",
                        "expires_calculated_at": "2020-07-19 11:10:02",
                        "created_at": "2020-07-19 09:17:20",
                        "updated_at": "2020-07-19 09:17:20",
                        "touched_at": "2020-07-19 11:08:48",
                        "pivot": {
                            "id": 11,
                            "created_at": "2020-07-19 09:19:39",
                            "updated_at": "2020-07-19 09:19:39"
                        }
                    },
                    {
                        "id": 2,
                        "type_id": 18,
                        "status_id": 1,
                        "class": "host",
                        "hash": "65b9aa337a73fa71b88bd613c1f4d06d",
                        "value": "7815696ecbf1c96e6894b779456d3301",
                        "description": null,
                        "last_detected_at": null,
                        "expires_at": null,
                        "expired_at": null,
                        "expires_needs_calc": "N",
                        "expires_calculated_at": "2020-07-19 09:25:02",
                        "created_at": "2020-07-19 09:17:43",
                        "updated_at": "2020-07-19 09:17:43",
                        "touched_at": "2020-07-19 09:20:22",
                        "pivot": {
                            "id": 12,
                            "created_at": "2020-07-19 09:20:22",
                            "updated_at": "2020-07-19 09:20:22"
                        }
                    }
                ],
                "signatures": [],
                "sources": [
                    {
                        "id": 6,
                        "type": "plugins",
                        "reference_id": 2,
                        "name": "Emerging Threats",
                        "tlp_id": null,
                        "created_at": "2020-07-19 09:19:39",
                        "updated_at": "2020-07-19 09:19:39",
                        "published_at": null,
                        "pivot": {
                            "event_id": 1,
                            "source_id": 6,
                            "id": 1,
                            "creator_source_id": 8
                        }
                    }
                ],
                "spearphish": null,
                "tags": [],
                "type": {
                    "id": 4,
                    "name": "DoS Attack",
                    "user_editable": "N",
                    "created_at": "2020-06-29 17:13:28",
                    "updated_at": "2020-06-29 17:13:28"
                },
                "watchlist": []
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and data is available (is_success=true):_ print "Successfully listed ThreatQ events."If fail no events (is_success=false):print "No events were found in ThreatQ."**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "List Events". Reason: {0}''.format(error.Stacktrace)_If invalid field is specified in the "Additional Fields" parameter:_ print "Error executing action "List Events". Reason: Invalid field was specified in the 'Additional Fields' parameter. '''.format(error.Stacktrace)" | General  
CSV Wall Table | **Table name:** ThreatQ Events**Table column:**

  * ID (mapped as id)
  * Title (mapped as title)
  * Created At (mapped as created_at)
  * Update At (mapped as updated_at)
  * Description (mapped as description)

| General  
  
### List Indicators

#### Description

List indicators from ThreatQ.‌‌

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Additional Fields | CSV | adversaries, attachments, attributes, comments, events, indicators, signatures, sources, spearphish, tags, type, watchlist. | No | Specify what additional fields should be included in the response. Possible values: adversaries, attachments, attributes, comments, events, indicators, score, signatures, sources, status, tags, type, watchlist.  
Sort Field | DDL | IDPossible values:IDTitleCreated AtUpdated AtHappened At | No | Specify what field should be used for sorting indicators.  
Sort Direction | DDL | AscendingPossible Values: AscendingDescending | No | Specify the sorting direction.  
Max Events to Return | Integer | 50 | No | Specify how many indicators to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "total": 8,
        "data": [
            {
                "id": 1,
                "name": "Abra Cadabra",
                "created_at": "2020-07-19 09:33:29",
                "updated_at": "2020-07-19 09:33:29",
                "touched_at": "2020-07-19 09:33:29",
                "adversaries": [],
                "attachments": [],
                "attributes": [],
                "comments": [],
                "description": null,
                "events": [],
                "indicators": [
                    {
                        "id": 1,
                        "type_id": 18,
                        "status_id": 1,
                        "class": "host",
                        "hash": "6677d693422fbeb541397fb8554f4664",
                        "value": "7815696ecbf1c96e6894b779456d330e",
                        "description": null,
                        "last_detected_at": null,
                        "expires_at": null,
                        "expired_at": null,
                        "expires_needs_calc": "N",
                        "expires_calculated_at": "2020-07-19 11:10:02",
                        "created_at": "2020-07-19 09:17:20",
                        "updated_at": "2020-07-19 09:17:20",
                        "touched_at": "2020-07-19 11:08:48",
                        "pivot": {
                            "id": 13,
                            "created_at": "2020-07-19 09:33:29",
                            "updated_at": "2020-07-19 09:33:29"
                        }
                    }
                ],
                "plugins": [],
                "plugin_actions": [],
                "signatures": [],
                "sources": [
                    {
                        "id": 8,
                        "type": "users",
                        "reference_id": 1,
                        "name": "tip.labops@siemplify.co",
                        "tlp_id": null,
                        "created_at": "2020-07-19 09:33:29",
                        "updated_at": "2020-07-19 09:33:29",
                        "published_at": null,
                        "pivot": {
                            "adversary_id": 1,
                            "source_id": 8,
                            "id": 1,
                            "creator_source_id": 8
                        }
                    }
                ],
                "tags": [],
                "value_weight": null,
                "watchlist": []
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and data is available (is_success=true):_ print "Successfully listed ThreatQ adversaries."If no data available (is_success=false):print "No adversaries were found in ThreatQ."**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "List Adversaries". Reason: {0}''.format(error.Stacktrace)_​_ _If invalid field is specified in the "Additional Fields" parameter:_ print "Error executing action "List Adversaries". Reason: Invalid field was specified in the 'Additional Fields' parameter. '''.format(error.Stacktrace)" | General  
CSV Wall Table | **Table name:** ThreatQ _Indicators_**Table column:**

  * ID (mapped as id)
  * Title (mapped as title)
  * Created At (mapped as created_at)
  * Update At (mapped as updated_at)
  * Description (mapped as description)

| General  
  
### List Adversaries

#### Description

List adversaries from ThreatQ.‌

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Additional Fields | CSV | adversaries, attachments, attributes, comments, events, indicators, signatures, sources, spearphish, tags, type, watchlist. | No | Specify what additional fields should be included in the response. Possible values: adversaries, attachments, attributes, comments, events, indicators, score, signatures, sources, status, tags, type, watchlist.  
Sort Field | DDL | IDPossible values:IDTitleCreated AtUpdated AtHappened At | No | Specify what field should be used for sorting adversaries.  
Sort Direction | DDL | AscendingPossible Values: AscendingDescending | No | Specify the sorting direction.  
Max Events to Return | Integer | 50 | No | Specify how many indicators to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "total": 3,
        "data": [
            {
                "id": 3,
                "type_id": 27,
                "status_id": 1,
                "class": "network",
                "hash": "6677d693422fbeb541397fb8554f4664",
                "value": "7815696ecbf1c96e6894b779456d330e",
                "description": null,
                "last_detected_at": null,
                "expires_at": null,
                "expired_at": null,
                "expires_needs_calc": "N",
                "expires_calculated_at": "2020-07-19 11:10:02",
                "created_at": "2020-07-19 11:08:48",
                "updated_at": "2020-07-19 11:08:48",
                "touched_at": "2020-07-19 11:08:48",
                "adversaries": [],
                "attachments": [],
                "attributes": [],
                "comments": [],
                "events": [],
                "indicators": [
                    {
                        "id": 1,
                        "type_id": 18,
                        "status_id": 1,
                        "class": "host",
                        "hash": "6677d693422fbeb541397fb8554f4664",
                        "value": "7815696ecbf1c96e6894b779456d330e",
                        "description": null,
                        "last_detected_at": null,
                        "expires_at": null,
                        "expired_at": null,
                        "expires_needs_calc": "N",
                        "expires_calculated_at": "2020-07-19 11:10:02",
                        "created_at": "2020-07-19 09:17:20",
                        "updated_at": "2020-07-19 09:17:20",
                        "touched_at": "2020-07-19 11:08:48",
                        "pivot": {
                            "id": 15,
                            "created_at": "2020-07-19 11:08:48",
                            "updated_at": "2020-07-19 11:08:48"
                        }
                    }
                ],
                "score": {
                    "indicator_id": 3,
                    "generated_score": "0.00",
                    "manual_score": null,
                    "score_config_hash": "7f8b888a2d2b462310d5227aa75e8c4a78973a96",
                    "created_at": "2020-07-19 11:08:48",
                    "updated_at": "2020-07-19 11:08:48"
                },
                "signatures": [],
                "sources": [
                    {
                        "id": 8,
                        "type": "users",
                        "reference_id": 1,
                        "name": "tip.labops@siemplify.co",
                        "tlp_id": null,
                        "created_at": "2020-07-19 11:08:48",
                        "updated_at": "2020-07-19 11:08:48",
                        "published_at": null,
                        "pivot": {
                            "indicator_id": 3,
                            "source_id": 8,
                            "id": 3,
                            "creator_source_id": 8
                        }
                    }
                ],
                "status": {
                    "id": 1,
                    "name": "Active",
                    "description": "Poses a threat and is being exported to detection tools.",
                    "user_editable": "N",
                    "visible": "Y",
                    "include_in_export": "Y",
                    "protected": "Y",
                    "created_at": "2020-06-29 17:14:34",
                    "updated_at": "2020-06-29 17:14:34"
                },
                "tags": [],
                "type": {
                    "id": 27,
                    "name": "String",
                    "class": "network",
                    "score": null,
                    "wildcard_matching": "Y",
                    "created_at": "2020-06-29 17:13:29",
                    "updated_at": "2020-06-29 17:13:29"
                },
                "watchlist": []
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and data is available (is_success=true):_ print "Successfully listed ThreatQ indicators."_​_ _If no data available (is_success=false):_ print "No indicators were found in ThreatQ."**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "List Indicators". Reason: {0}''.format(error.Stacktrace)_​_ _If invalid field is specified in the "Additional Fields" parameter:_ print "Error executing action "List Indicators". Reason: Invalid field was specified in the 'Additional Fields' parameter. '''.format(error.Stacktrace)" | General  
CSV Wall Table | **Table name:** ThreatQ _Indicators_**Table column:**

  * ID (mapped as id)
  * Title (mapped as title)
  * Created At (mapped as created_at)
  * Update At (mapped as updated_at)
  * Description (mapped as description)

| General  
  
### Update Indicator Status

#### Description

Action updates indicator status in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Status | DDL | ActivePossible values:ActiveExpiredIndirectReviewWhitelisted | True | Specify the new status of the indicator.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "id": 1,
            "type_id": 18,
            "status_id": 2,
            "class": "host",
            "hash": "6677d693422fbeb541397fb8554f4664",
            "value": "7815696ecbf1c96e6894b779456d330e",
            "description": null,
            "last_detected_at": null,
            "expires_at": null,
            "expired_at": "2020-07-21 09:05:56",
            "expires_needs_calc": "N",
            "expires_calculated_at": "2020-07-21 07:35:02",
            "created_at": "2020-07-19 09:17:20",
            "updated_at": "2020-07-21 09:05:56",
            "touched_at": "2020-07-21 09:05:56"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful (is_success = true):_  
print "Successfully updated status for the indicator with value '{0}' in ThreatQ.".format(indicator value)___If indicator was not found (is_success = false):_  
Print "Action was not able to update status for the indicator with value '{0}' in ThreatQ. Reason: Indicator with value '{0}' and type '{1}' was not found in ThreatQ.".format(indicator value, indicator type)  
_If fail general error(is_success = false):_ Print: "Action was not able to update status for the indicator with value '{0}' in ThreatQ.".format(indicator value)  
**The action should fail and stop a playbook execution:**_If fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Update Indicator Status". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Indicator Score

#### Description

Action updates indicator score in ThreatQ.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Score | DDL | "7 - Medium"Possible Values:"0 - Very Low""1 - Very Low""2 - Very Low""3 - Very Low""4 - Very Low""5 - Low""6 - Low""7 - Medium" "8 - Medium" "9 - High""10 - Very High" | Yes | Specify the new score of the indicator.  
Score Validation | DDL | Highest ScorePossible Values:Highest ScoreForce Update  
| Yes | Specify what kind of score validation should be used. If " Highest Score" is specified, action will compare current values and update the indicator's score only, if the specified score is higher than current generated and manual score. If "Force Update" is specified, action will update the indicator's score without comparing current values.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "indicator_id": 2,
            "generated_score": "5.00",
            "manual_score": 1,
            "score_config_hash": "7f8b888a2d2b462310d5227aa75e8c4a78973a96",
            "created_at": "2020-07-19 09:17:43",
            "updated_at": "2020-07-21 09:25:27"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful (is_success = true):_  
print "Successfully updated score for the indicator with value '{0}' in ThreatQ.".format(indicator value)_If Score Validation == "Highest Score" and specified score in the action parameter is smaller than current ones: (is_success = false):_ print "Action didn't update score for the indicator with value '{0}' in ThreatQ. Reason: Current score is higher.".format(indicator value)  
_If indicator was not found (is_success = false):_ print "Action was not able to update score for the indicator with value '{0}' in ThreatQ. Reason: Indicator with value '{0}' and type '{1}' was not found in ThreatQ.".format(indicator value, indicator type)  
_If fail general error(is_success = false):_ Print: "Action was not able to update score for the indicator with value '{0}' in ThreatQ.".format(indicator value)  
**The action should fail and stop a playbook execution:** if fatal error, like wrong credentials, no connection to server, other: print "Error executing action "Update Indicator Score". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
