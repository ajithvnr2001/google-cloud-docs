---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/forescout-counteract/
title: ForeScout CounterACT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:28.572971+00:00
---

# ForeScout CounterACT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/forescout-counteract/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ForeScout CounterACT

This document describes how to integrate FireEye NX with Google Security Operations.

## Use Cases

Perform enrichment actions.

## Configure ForeScout CounterACT integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | https://<ip address> | Yes | ForeScout CounterACT API root  
Username | String | N/A | Yes | ForeScout CounterACT API username.  
Password | Password | N/A | Yes | ForeScout CounterACT API password.  
CA Certificate File | String | N/A | No | Base64 encoded CA certificate file.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Armis server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to ForeScout CounterACT with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successful:** "Successfully connected to the ForeScout CounterACT server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
**if not successful:** "Failed to connect to the ForeScout CounterACT server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from ForeScout CounterACT. Supported entities: IP, Mac Address.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, action will create insights containing enrichment information.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Mac Address



#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
            "ip": "172.30.202.30",
            "mac": "005056a2196c",
            "fields": {
                "channel": {
                    "timestamp": 1623834301,
                    "value": "eth1.-1"
                },
                "nmap_banner7": [
                    {
                        "timestamp": 1623834430,
                        "value": "80/tcp Apache httpd 2.4.6 (CentOS)"
                    },
                    {
                        "timestamp": 1623834430,
                        "value": "22/tcp OpenSSH 7.4 protocol 2.0"
                    }
                ],
                "onsite": {
                    "timestamp": 1623834301,
                    "value": "true"
                },
                "classification_source_os": {
                    "timestamp": 1623838175,
                    "value": "engine"
                },
                "linux_manage": {
                    "timestamp": 1623838175,
                    "value": "false"
                },
                "access_ip": {
                    "timestamp": 1623838175,
                    "value": "172.30.202.30"
                },
                "classification_source_vendor": {
                    "timestamp": 1623838175,
                    "value": "engine"
                },
                "mac_vendor_string": {
                    "timestamp": 1623834302,
                    "value": "VMWARE, INC."
                },
                "openports": [
                    {
                        "timestamp": 1623834384,
                        "value": "22/TCP"
                    },
                    {
                        "timestamp": 1623834397,
                        "value": "161/UDP"
                    },
                    {
                        "timestamp": 1623834384,
                        "value": "80/TCP"
                    }
                ]
            },
            "id": 2887698974
    }
    

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
ip | When available in JSON  
mac | When available in JSON  
onsite | When available in JSON  
guest_corporate_state | When available in JSON  
fingerprint | When available in JSON  
vendor | When available in JSON  
classification | When available in JSON  
agent_version | When available in JSON  
online | When available in JSON  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if enriched some(is_success = true):** "Successfully enriched the following entities using ForeScout CounterACT:\n".format(entity.identifier)  
******If didn't enrich some (is_success = true):** "Action wasn't able to enrich the following entities using ForeScout CounterACT:\n".format(entity.identifier)  
******If didn't enrich all (is_success = false):** "No entities were enriched".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Entity Table | Same Columns as in the Enrichment table, but without prefix. | Entity  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
