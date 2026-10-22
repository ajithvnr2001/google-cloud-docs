---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rapid7-insightsvm/
title: Rapid7 InsightVM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:12.888236+00:00
---

# Rapid7 InsightVM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rapid7-insightsvm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Rapid7 InsightVM

This document provides guidance on how to integrate Rapid7 InsightVM with Google SecOps.

**Note:** This integration is supported only for on-premises deployments of the product.

## Configure Rapid7 InsightVM integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | N/A | Yes | API root of the Rapid7 InsightVM instance.  
Username | String | N/A | Yes | Rapid7 InsightVM API Username.  
Password | Password | N/A | Yes | Rapid7 InsightVM API Password.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the Rapid7 InsightVM server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Enrich Asset

#### Description

Enrich an asset.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "10.0.0.100": {
            "users": [{
                "id": 500,
                "name": "Administrator"
            },{
                "id": 503,
                "name": "DefaultAccount"
            },{
                "id": 501,
                "name": "Guest"
            }],
            "userGroups": [{
                "id": 7,
                "name": "ANONYMOUS LOGON"
            },{
                "id": 579,
                "name": "Access Control Assistance Operators"
            },{
                "id": 544,
                "name": "Administrators"
            }],
            "hostNames": [{
                "source": "netbios",
                "name": "WS-HUNULULU"
            },{
                "source": "dns",
                "name": "ws-chaimsky.siemplify.local"
            }],
            "addresses": [{
                "ip": "1.1.1.1",
                "mac": "48:4D:7E:B8:3B:A4"
            }],
            "links": [{
                "href": "https://1.1.1.1:3780/api/3/assets/1",
                "rel": "self"
            },{
                "href": "https://1.1.1.1:3780/api/3/assets/1/software",
                "rel": "Software"
            },{
                "href": "https://1.1.1.1:3780/api/3/assets/1/files",
                "rel": "Files"
            }],
            "assessedForPolicies": false,
            "ip": "1.1.1.1",
            "hostName": "ws-chaimsky.siemplify.local",
            "osFingerprint": {
                "product": "Windows Server 2016",
                "vendor": "Microsoft",
                "description": "Microsoft Windows Server 2016",
                "family": "Windows",
                "systemName": "Microsoft Windows",
                "type": "General",
                "id": 8
            },
            "riskScore": 8270.22559,
            "mac": "48:4D:7E:B8:3B:A4",
            "rawRiskScore": 8270.22559,
            "vulnerabilities": {
                "moderate": 6,
                "exploits": 1,
                "malwareKits": 0,
                "severe": 12,
                "critical": 0,
                "total": 18
            },
            "services": [{
                "protocol": "tcp",
                "name": "DCE Endpoint Resolution",
                "links": [{
                    "href": "https://1.1.1.1:3780/api/3/assets/1/services/tcp/135",
                    "rel": "self"
                },{
                    "href": "https://1.1.1.1:3780/api/3/assets/1/services/tcp/135/configurations",
                    "rel": "Configurations"
                },{
                    "href": "https://1.1.1.1:3780/api/3/assets/1/services/tcp/135/databases",
                    "rel": "Databases"
                }],
                "port": 135
            },{
                "name": "CIFS Name Service",
                "protocol": "udp",
                "port": 137,
                "links": [{
                    "href": "https://1.1.1.1:3780/api/3/assets/1/services/udp/137",
                    "rel": "self"
                },{
                    "href": "https://1.1.1.1:3780/api/3/assets/1/services/udp/137/configurations",
                    "rel": "Configurations"
                },{
                    "href": "https://1.1.1.1:3780/api/3/assets/1/services/udp/137/databases",
                    "rel": "Databases"
                }],
                "configurations": [{
                    "name": "advertised-name-1",
                    "value": "SIEMPLIFY (Domain Name)"
                },{
                    "name": "advertised-name-2",
                    "value": "WS-CHAIMSKY (File Server Service)"
                },{
                    "name": "advertised-name-3",
                    "value": "WS-CHAIMSKY (Computer Name)"
                }]}, {
                    "product": "Windows 10 Enterprise N 2016 LTSB 6.3",
                    "protocol": "tcp",
                    "name": "CIFS",
                    "links": [{
                        "href": "https://1.1.1.1:3780/api/3/assets/1/services/tcp/139",
                        "rel": "self"
                    },{
                        "href": "https://1.1.1.1:3780/api/3/assets/1/services/tcp/139/configurations",
                        "rel": "Configurations"
                    },{
                        "href": "https://1.1.1.1:3780/api/3/assets/1/services/tcp/139/databases",
                        "rel": "Databases"
                    }],
                    "port": 139,
                    "configurations": [{
                        "name": "domain",
                        "value": "SIEMPLIFY"
                    },{
                        "name": "password-mode",
                        "value": "encrypt"
                    },{
                        "name": "security-mode",
                        "value": "user"
                    }]}],
            "assessedForVulnerabilities": true,
            "os": "Microsoft Windows Server 2016",
            "id": 1,
            "history": [{
                "date": "2019-03-25T04:25:46.333Z",
                "scanId": 1,
                "version": 1,
                "type": "SCAN"
            },{
                "date": "2019-03-25T06:58:49.450Z",
                "scanId": 2,
                "version": 2,
                "type": "SCAN"
            },{
                "date": "2019-03-26T03:58:44.859Z",
                "scanId": 5,
                "version": 3,
                "type": "SCAN"
            }]
        }
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
users | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
userGroups | Returns if it exists in JSON result  
hostName | Returns if it exists in JSON result  
source | Returns if it exists in JSON result  
addresses | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
mac | Returns if it exists in JSON result  
links | Returns if it exists in JSON result  
href | Returns if it exists in JSON result  
rel | Returns if it exists in JSON result  
assessedForPolicies | Returns if it exists in JSON result  
product | Returns if it exists in JSON result  
vendor | Returns if it exists in JSON result  
description | Returns if it exists in JSON result  
Family | Returns if it exists in JSON result  
systemName | Returns if it exists in JSON result  
type | Returns if it exists in JSON result  
riskScore | Returns if it exists in JSON result  
rawRiskScore | Returns if it exists in JSON result  
moderate | Returns if it exists in JSON result  
vulnerabilities | Returns if it exists in JSON result  
exploits | Returns if it exists in JSON result  
malwareKits | Returns if it exists in JSON result  
severe | Returns if it exists in JSON result  
critical | Returns if it exists in JSON result  
total | Returns if it exists in JSON result  
configurations | Returns if it exists in JSON result  
date | Returns if it exists in JSON result  
ScanId | Returns if it exists in JSON result  
Version | Returns if it exists in JSON result  
  
##### Insights

N/A

### Get Scan Results

#### Description

Get scan results by ID.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scan ID | String | N/A | Yes | The ID of the scan.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
        "STATUS": {
            "STATE": "Finished"
        },
        "EXPIRATION_DATETIME": "2019-02-04T13:11:15Z",
        "TITLE": "Scan scan/1533110666.07264 Report",
        "USER_LOGIN": "sempf3mh",
        "OUTPUT_FORMAT": "PDF",
        "LAUNCH_DATETIME": "2019-01-28T13:11:14Z",
        "TYPE": "Scan",
        "ID": "775111",
        "SIZE": "22.17 KB"
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Launch Scans

#### Description

Start a scan for a specific site.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scan Name | String | N/A | No | The scan name.  
Scan Engine | String | N/A | Yes | The name of the engine to use in the scan.  
Scan Template | String | N/A | Yes | The name of the template to use in the scan.  
Site Name | String | N/A | Yes | The name of the site to run the scan on.  
Fetch Results | Checkbox | Unchecked | No | Whether to wait for the scan to complete and get its results or not.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
scan_id | N/A | N/A  
  
##### JSON Result
    
    
    {
        "status": "finished",
        "scanType": "Manual",
        "assets": 1,
        "links": [{
            "href": "https://1.1.1.1:3780/api/3/scans/8",
            "rel": "self"
        }],
        "vulnerabilities": {
            "severe": 12,
            "total": 18,
            "critical": 0,
            "moderate": 6
        },
        "startTime": "2019-04-11T07:44:00.095Z",
        "duration": "PT7M58.298S",
        "engineName": "Local scan engine",
        "endTime": "2019-04-11T07:51:58.393Z",
        "id": 8,
        "scanName": "siemplify_20190411-104353"
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
status | Returns if it exists in JSON result  
scanType | Returns if it exists in JSON result  
assets | Returns if it exists in JSON result  
links | Returns if it exists in JSON result  
href | Returns if it exists in JSON result  
rel | Returns if it exists in JSON result  
vulnerabilities | Returns if it exists in JSON result  
severe | Returns if it exists in JSON result  
total | Returns if it exists in JSON result  
critical | Returns if it exists in JSON result  
moderate | Returns if it exists in JSON result  
startTime | Returns if it exists in JSON result  
duration | Returns if it exists in JSON result  
engineName | Returns if it exists in JSON result  
endTime | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
scanName | Returns if it exists in JSON result  
  
##### Insights

N/A

### List Scans

#### Description

List scans.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Days Backwards | String | N/A | Yes | Number of days backwards to fetch scans from.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "status": "finished",
            "scanType": "Manual",
            "assets": 1,
            "links": [{
                "href": "https://1.1.1.1:3780/api/3/scans/8",
                "rel": "self"
            }],
            "vulnerabilities": {
                "severe": 12,
                "total": 18,
                "critical": 0,
                "moderate": 6
            },
            "startTime": "2019-04-11T07:44:00.095Z",
            "duration": "PT7M58.298S",
            "engineName": "Local scan engine",
            "endTime": "2019-04-11T07:51:58.393Z",
            "id": 8,
            "scanName": "siemplify_20190411-104353"
        }
    ]
    
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

## Connectors

## Rapid7 InsightVM - Vulnerabilities Connector

#### Description

Pull information about asset vulnerabilities from Rapid7 InsightVM.

**Note:** The whitelist filter works with the "title" parameter.

#### Configure Rapid7 InsightVM - Vulnerabilities Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | riskEventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 500 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{ip}:3780 | Yes | API root of the Rapid7 InsightVM instance.  
Username | String | N/A | Yes | Username of the Rapid7 InsightVM account.  
Password | Password | N/A | Yes | Password of the Rapid7 InsightVM account.  
Lowest Severity To Fetch | String | Moderate | No | The lowest severity that needs to be used to fetch vulnerabilities. Possible values: Moderate, Severe, Critical.If nothing is provided, the connector fetches vulnerabilities with all severities.  
Max Assets To Process | Integer | 5 | No | Amount of assets that need to be processed per one connector iteration. **Note:** It's not recommended to increase the value of this parameter, because the connector will be more prone to timeouts.  
Grouping Mechanism | String | Host | No | Grouping mechanism that is used to create Google SecOps alerts. Possible values: Host, None. If "Host" is provided, the connector creates one Google SecOps alert containing all of the vulnerabilities related to the host. If "None" or invalid value is provided, the connector creates a new Google SecOps alert for each separate vulnerability per host.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist is used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Rapid7 InsightVM server is valid.r is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
