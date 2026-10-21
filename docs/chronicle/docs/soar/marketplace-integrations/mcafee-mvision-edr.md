---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-mvision-edr/
title: McAfee MVISION EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:59.494178+00:00
---

# McAfee MVISION EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-mvision-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee MVISION EDR

**Important:** McAfee MVISION EDR became part of the Trellix product portfolio and was renamed to Trellix EDR.

This document provides guidance on how to integrate McAfee MVISION EDR with Google SecOps.

## Configure McAfee MVISION EDR integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://<address>:<port> | Yes | Trellix EDR API Root. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Login API Root | String | https://iam.cloud.trellix.com/iam/v1.0/token | No |  The endpoint used to retrieve authentication tokens. This is utilized for both authentication methods. If you are in specific geographic regions or use custom IAM gateways rather than the Trellix public cloud IAM, you must update this URL to ensure tokens are successfully generated.  
Username | String | N/A | Yes | Username of Trellix EDR account. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Password | Password | N/A | Yes | Password of the Trellix EDR account. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Client ID | String | N/A | No | Client ID of the Trellix EDR account. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Client Secret | Password | N/A | No | Client Secret of the Trellix EDR account. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Trellix EDR public cloud server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## How to generate Client ID and Client Secret

For more information on how to generate Client ID and Client Secret, see the [McAfee MVISION EDR Integrations](https://github.com/mohlcyber/McAfee-MVISION-EDR-Integrations/blob/master/README.md) document.

## Use Cases

  1. Ingest Trellix EDR threats and detections to use them to create Google SecOps alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.
  2. Perform enrichment actions - get data from Trellix EDR to enrich data in Google SecOps Alerts.
  3. Perform active actions - quarantine a host using Trellix EDR agent from Google SecOps.



## Actions

### Ping

#### Description

Test connectivity to Trellix EDR with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Use Cases

The action is used to test connectivity at the integration configuration page in the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

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

### Enrich Endpoint

#### Description

Fetch endpoint's system information by its hostname or IP address.

#### Parameters

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
        "total": 9,
        "skipped": 0,
        "items": 1,
        "hosts": [
            {
                "maGuid": "3975892D-E16D-45C0-8795-164CFDF27946",
                "hostname": "AWS-LT-EDR1",
                "os": {
                    "major": 10,
                    "minor": 0,
                    "build": 18362,
                    "sp": "",
                    "desc": "Windows 10"
                },
                "lastBootTime": "2020-02-24T21:41:38Z",
                "netInterfaces": [
                    {
                        "name": "Ethernet 2",
                        "macAddress": "02:33:86:c2:6b:d4",
                        "ip": "10.0.3.212",
                        "type": 6
                    }
                ],
                "traceExtendedVisibility": 0
            }
        ]
    }
    

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
MMV_EDR_maGuid | hosts/maGuid | When available in JSON  
MMV_EDR_hostname | hosts/hostname | When available in JSON  
MMV_EDR_OS | hosts/os/desc | When available in JSON  
MMV_EDR_lastBootTime | hosts/lastBootTime | When available in JSON  
MMV_EDR_certainty | hosts/certainty | When available in JSON  
MMV_EDR_ips | Space separated results/net_interfaces/ip | When available in JSON  
  
##### Insights

N/A

### Quarantine Endpoint

#### Description

Create quarantine endpoint task on the Trellix EDR server based on the Google SecOps IP Address or Hostname entities.

#### Known Issue from Trellix

**Reference** : [Trellix EDR Known Issues](https://kcm.trellix.com/corporate/index?page=content&id=KB91275)

When you quarantine an endpoint connected to a VPN, the endpoint becomes unreachable. You can't send the reaction to End the Quarantine.

**Workaround:**

  1. Gain physical access to the endpoint.
  2. Uninstall the EDR Client from Add and Remove Programs.
  3. Install the EDR client again.



#### Parameters

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
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Unquarantine Endpoint

#### Description

Create unquarantine endpoint task on the McAfee MVISION EDR server based on the Google SecOps IP Address or Hostname entities.

#### Known Issue from Trellix

**Reference** : [Trellix EDR Known Issues](https://kcm.trellix.com/corporate/index?page=content&id=KB91275)

When you quarantine an endpoint connected to a VPN, the endpoint becomes unreachable. You can't send the reaction to End the Quarantine.

**Workaround:**

  1. Gain physical access to the endpoint.
  2. Uninstall the EDR Client from Add and Remove Programs.
  3. Install the EDR client again.



#### Parameters

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
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Remove File

#### Description

Remove a file from the endpoint.

#### Action execution known issue

McAfee may not remove files and still show in the WebUI that action was executed successfully. The following issue can be related to permissions on agent. Verify that the agent has the required permissions and try again.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Full File Path | String | N/A | Yes | Specify the full path to the file that you want to remove.  
Safe Removal | Checkbox | Unchecked | Yes | If enabled, ignores files that may be critical or trusted.  
  
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
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Stop And Remove Content

#### Description

Stop interpreter process by PID, for example Python or Bash, and remove the associated script by full path on the McAfee MVISION EDR.

#### Action execution known issue

McAfee may not remove or kill associated files and still show in the WebUI that action was executed successfully. The following issue can be related to permissions on agent. Verify that the agent has the required permissions and try again.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
PID | Integer | N/A | Yes | Specify the PID of the interpreter.  
Full File Path | String | N/A | Yes | Specify the full path to the file that you want to remove.  
  
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
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Kill Process

#### Description

Stop a running process and remove its file. If the process is not running, then its file is just removed from the managed endpoint.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Process Identifier Type | DDL | PID Possible Values:

  * PID
  * SHA256
  * Name
  * Full Path

| Yes | Specify which process identifier type to use.  
Process Identifier | String | N/A | Yes | Specify the value for the process identifier.  
  
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
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Dismiss Threat

#### Description

Dismiss threat in Trellix EDR.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Threat ID | String | N/A | Yes | Specify the ID of the threat that you want to dismiss.  
  
#### Run On

This action doesn't run on entities.

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

### McAfee MVISION EDR - Threats Connector

#### Description

Trellix EDR threats can be updated with new detections with time. Right now, in order to process new detections, you would need to dismiss the threat. This way Trellix EDR will create a new threat and it will be ingested into Google SecOps with those new detections. In other cases, new detections that were added after ingestion of threat will not be available within Google SecOps.

#### Configure McAfee MVISION EDR - Threats Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name  
| String | "" | No | Describes the name of the field where the environment name is stored.If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern  
| String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic.If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://x.x.x.x | Yes | API root of Trellix EDR server.  
Login API Root | String | https://iam.cloud.trellix.com/iam/v1.0/token | No |  The endpoint used to retrieve authentication tokens. This is utilized for both authentication methods. If you are in specific geographic regions or use custom IAM gateways rather than the Trellix public cloud IAM, you must update this URL to ensure tokens are successfully generated.  
Username | String | N/A | Yes | Trellix EDR account username. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Password | Password | N/A | Yes | Trellix EDR account password. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Client ID | String | N/A | No | Client ID of the Trellix EDR account. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Client Secret | Password | N/A | No | Client Secret of the Trellix EDR account. **Note:** Provide either the Client ID and Client Secret or Username and Password parameters. If both parameters are provided, the integration use the Client ID and Client Secret parameters for authentication.  
Lowest Severity To Fetch | String | Medium | Yes | Lowest severity that will be used to fetch threats. Possible values:  
Info Medium High Critical  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch threats.  
Max Threats To Fetch | Integer | 25 | No | How many threats to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Trellix EDR public cloud server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
