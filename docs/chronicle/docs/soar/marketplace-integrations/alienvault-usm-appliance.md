---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alienvault-usm-appliance/
title: Integrate LevelBlue USM Appliance with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:32.970166+00:00
---

# Integrate LevelBlue USM Appliance with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alienvault-usm-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate LevelBlue USM Appliance with Google SecOps

This document describes how to integrate LevelBlue Unified Security Management (USM) Appliance with Google Security Operations (Google SecOps).

**Important:** AlienVault USM Appliance became LevelBlue USM Appliance. In the Google SecOps platform, the integration for LevelBlue USM Appliance is called _AlienVault USM Appliance_.

## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | https://<instance>.alienvault.com | Yes | Address of the LevelBlue USM Appliance instance.  
Username | String | N/A | Yes | The user's email address for connecting to the LevelBlue USM Appliance.  
Password | Password | N/A | Yes | The password of the user account.  
Run Remotely | Checkbox | Unchecked | No | Select the field to run the configured integration remotely.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Enrich Assets

Retrieve LevelBlue USM Appliance asset details. Within USM Appliance, an asset operates on the network of the organization as an integrated piece of equipment, which includes an exclusive IP address. An asset can be a PC, printer, firewall, router, server, or multiple devices that are allowed by the network. An asset is supervised by at least one USM Appliance Sensor.

#### Parameters

N/A

#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action results

##### Entity enrichment

Enrichment field name | Logic - When to apply  
---|---  
model | Returns if it exists in JSON result  
descr | Returns if it exists in JSON result  
hostname | Returns if it exists in JSON result  
asset_type | Returns if it exists in JSON result  
fqdn | Returns if it exists in JSON result  
devices | Returns if it exists in JSON result  
asset_value | Returns if it exists in JSON result  
ips | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
sensors | Returns if it exists in JSON result  
os | Returns if it exists in JSON result  
networks | Returns if it exists in JSON result  
icon | Returns if it exists in JSON result  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": {
                "model": null,
                "descr": " ",
                "hostname": "Hostname",
                "asset_type": "Internal",
                "fqdn": " ",
                "devices": [],
                "asset_value": "2",
                "ips": {
                    "3.3.3.3": {
                        "ip": "192.0.2.1",
                        "mac": "01:23:45:AB:CD:EF"
                    }},
                "id": "123D37D595B800734550B9D9D6A958C6",
                "sensors": {
                    "C221234962EA11E697DE0AF71A09DF3B": {
                        "ip": "192.0.2.1",
                        "ctxs": {
                            "C228355962EA11E697DE0AF71A09DF3B": "AlienVault"
                        },
                        "name": "DA"
                    }},
                "os": "Linux",
                "networks": {
                    "7E4B12EEFD06A21F898345C2AB46EB10": {
                        "ips": "192.0.2.1/24",
                        "ctx": "C228355962EA11E697DE0AF71A09DF3B",
                        "name": "Pvt_000"
                    }},
                "icon": " "
            },
            "Entity": "example.com"
        }
    ]
    

### Enrich Vulnerabilities

Retrieve vulnerability information from the LevelBlue USM Appliance. The integrated vulnerability scanner on the USM Appliance Sensor can detect vulnerabilities in critical assets. These uncovered vulnerabilities can then be used in cross-correlation rules, enforcement, and audit reporting.

#### Parameters

N/A

#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action results

##### Entity enrichment

Enrichment field name | Logic - When to apply  
---|---  
AlientVault_Severity | Returns if it exists in JSON result  
AlientVault_Service | Returns if it exists in JSON result  
AlientVault_Vulnerability | Returns if it exists in JSON result  
AlientVault_Scan Time | Returns if it exists in JSON result  
AlientVault_Asset | Returns if it exists in JSON result  
AlientVault_Id | Returns if it exists in JSON result  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
success | True or False | success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": [{
                "Severity": "High",
                "Service": "general (0/tcp))",
                "Vulnerability": "TCP Sequence Number Approximation Reset Denial of Service Vulnerability",
                "Scan Time": "2014-02-26 02:08:59",
                "Asset": "Hostname (192.0.2.1)",
                "Id": "123456"
            }, {
                "Severity": "High",
                "Service": "https (443/tcp)",
                "Vulnerability": "robot(s).txt exists on the Web Server",
                "Scan Time": "2014-02-26 02:08:59",
                "Asset": "Hostname (192.0.2.1)",
                "Id": "123457"
            }, {
                "Severity": "Medium",
                "Service": "general (0/tcp))",
                "Vulnerability": "TCP timestamps",
                "Scan Time": "2014-02-26 02:08:59",
                "Asset": "Hostname (192.0.2.1)",
                "Id": "123458"
            }],
            "Entity": "test"
        }
    ]
    

### Fetch Last PCAP Files

Fetch last PCAP files from AlienVault.

#### Parameters

Parameter name | Type | Default value | Description  
---|---|---|---  
Number Of Files To Fetch | String | N/A | Example: 10  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "scan_name": "pcap_file_1545041396_10_192.0.2.1.pcap",
            "creation_time": "2018-12-17 10:09:56",
            "user": null,
            "download_link": "https://www.alienvault.com/ossim/pcap/download.php?scan_name=0000000_10_192.0.2.1.pcap&sensor_ip=192.0.2.1",
            "sensor_ip": "192.0.2.1",
            "duration": "10"
        }, {
            "scan_name": "pcap_file_1545041397_10_192.0.2.1.pcap",
            "creation_time": "2018-12-17 10:09:56",
            "user": null,
            "download_link": "https://www.alienvault.com/ossim/pcap/download.php?scan_name=0000000_10_192.0.2.1.pcap&sensor_ip=192.0.2.1",
            "sensor_ip": "192.0.2.1",
            "duration": "10"
        }, {
            "scan_name": "pcap_file_1545041398_10_192.0.2.1.pcap",
            "creation_time": "2018-12-17 10:09:56",
            "user": null,
            "download_link": "https://www.alienvault.com/ossim/pcap/download.php?scan_name=0000000_10_192.0.2.1.pcap&sensor_ip=192.0.2.1",
            "sensor_ip": "192.0.2.1",
            "duration": "10"
        }
    ]
    

### Get PCAP Files for Events

Get PCAP files for events in an alert.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result
    
    
    {
        "#0-1B09DN3B0D2011E985730AS799BFE5BC": "obLD1AACAAQAAAAAAAAAAAAABdwAAAABV+kUZQAHyFMAAAXqAAAF6gr3GgnfOwobLz7Y6wgARQAF3Dd3QABnBvvXVduqw6wfLg8MmgG7xmc2dMr3EdxQEAD+OgAAABcDAwdVAAAAAAAAAASEw70Ys0kQbz8wdaj1lsHAAA=="
    }
    

### Get Vulnerability Reports

Get environment vulnerability report files.

#### Parameters

Parameter name | Type | Default value | Description  
---|---|---|---  
Number of Files to Fetch | string | N/A | Example: 10  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "creation_time": "2014-02-26 02:08:59",
            "download_link": "https://www.alienvault.com/ossim/vulnmeter/lr_rescsv.php?treport=latest&ipl=192.0.2.1&ctx=C22835597DE0AF71A09DF3B&scantype=M",
            "Address": "Hostname (192.0.2.1)"
        }, {
            "creation_time": "2014-02-26 02:08:59",
            "download_link":
            "https://www.alienvault.com/ossim/vulnmeter/lr_rescsv.php?treport=latest&ipl=192.0.2.1&ctx=C228351E697DE071A09DF3B&scantype=M",
            "Address": "Hostname (192.0.2.1)"
        }, {
            "creation_time": "2014-02-26 02:08:59",
            "download_link": "https://www.alienvault.com/ossim/vulnmeter/lr_rescsv.php?treport=latest&ipl=192.0.2.1&ctx=C22835597DE0AF71A09DF3B&scantype=M",
            "Address": "Hostname (192.0.2.1)"
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
success | True or False | success:False  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### AlienVault USM Appliance Connector

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Environment | DDL | N/A | Yes | Select the required environment. For example, "Customer One". If the alert's **Environment** field is empty, it will be injected into this environment.  
Run Every | Integer | 0:0:0:10 | No | Select the time to run the connection.  
Product Field Name | String | device_product | Yes | The field name used to determine the device product.  
Event Field Name | String | event_name | Yes | The name of the field that determines the event name (subtype).  
Script Timeout (Seconds) | String | 60 | Yes | The timeout limit, in seconds, for the Python process that runs the current script.  
Api Root | String | N/A | Yes | Address of the LevelBlue USM Appliance instance, such as https://<instance>.alienvault.com  
Username | String | N/A | Yes | Email of the user.  
Password | Password | N/A | Yes | The password of the according user.  
Max Events Per Alert | Integer | 10 | Yes | Limits the number of events per alert.  
Max Days Backwards | Integer | 1 | Yes | The number of days prior to today to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp.  
Max Alerts Per Cycle | Integer | 10 | Yes | The maximum number of alerts to fetch in every connector cycle. Limits the number of alerts in every cycle.  
Server Timezone | String | UTC | Yes | The timezone configured in the AlienVault instance, such as `UTC Asia/Jerusalem`.  
Environment Field Name | String | N/A | No | The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
  
#### Connector rules

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
