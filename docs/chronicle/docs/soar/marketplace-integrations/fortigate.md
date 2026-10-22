---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate/
title: Integrate FortiGate with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:57.967145+00:00
---

# Integrate FortiGate with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate FortiGate with Google SecOps

This document describes how to integrate FortiGate with Google Security Operations.

## Before you begin

**Note:** These requirements are based on codebase analysis. Validate these permissions against your specific FortiOS version before you implement them.

To follow the principle of least privilege, create a dedicated **REST API Admin** in FortiOS with a custom **Admin Profile**. The profile requires the following permissions:

  * `Policy & Objects`: Set to `Read/Write`. This lets the integration manage address groups, address objects, and firewall policies.
  * `Log & Report`: Set to `Read`. This is required only if you use the **FortiGate - Threat Logs Connector**.



If you scope the integration to a specific Virtual Domain (VDOM), `Per-VDOM` permissions are sufficient.

### Minimum permissions by action

Review the following table for the specific permissions required to execute each integration action.

Action | Required permissions  
---|---  
Add Entities To Address Group | `Firewall Address Groups` (`Read/Write`), `Firewall Address Objects` (`Read/Write`)  
Add Entities To Policy | `Firewall Policies` (`Read/Write`), `Firewall Address Objects` (`Read/Write`)  
List Policies / List Address Groups | `Firewall Policies` / `Address Groups` (`Read`)  
Remove Entities (Policy/Group) | `Firewall Policies` / `Address Groups` (`Read/Write`), `Firewall Address Objects` (`Read`)  
Ping | `Firewall Address Groups` (`Read`)  
  
## Integration parameters

The **FortiGate** integration requires the following parameters:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https:/{{ip address}} | Yes | API root of the FortiGate instance.  
API Key | Password | N/A | Yes | API key of the FortiGate instance.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, the integration verifies that the SSL certificate for the connection to the FortiGate server is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### List Policies(`Read`)

List available policies in FortiGate.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Key | DDL | Select OnePossible Values:

  * Name

| No | Specify the key that needs to be used to filter policies.  
Filter Logic | DDL | Not SpecifiedPossible Values:

  * Not Specified
  * Equal
  * Contains

| No | Specify what filter logic should be applied.Filtering logic is working based on the value provided in the "Filter Key" parameter.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results.If "Contains" is selected, action will try to find results that contain the specified substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.  
Max Records To Return | Integer | 50 | No | Specify the number of records to return. If nothing is provided, the action returns 50 records.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    ​{
        "policyid": 1,
        "q_origin_key": 1,
        "status": "enable",
        "name": "Test",
        "uuid": "x-x-x-x-x",
        "uuid-idx": 27,
        "srcintf": [
            {
                "name": "l2t.root",
                "q_origin_key": "l2t.root"
            }
        ],
        "dstintf": [
            {
                "name": "port1",
                "q_origin_key": "port1"
            }
        ],
        "action": "deny",
        "nat64": "disable",
        "nat46": "disable",
        "srcaddr": [
            {
                "name": "all",
                "q_origin_key": "all"
            }
        ],
        "dstaddr": [
            {
                "name": "G Suite",
                "q_origin_key": "G Suite"
            },
            {
                "name": "10.0.0.1",
                "q_origin_key": "10.0.0.1"
            }
        ],
        "srcaddr6": [],
        "dstaddr6": [],
        "ztna-status": "disable",
        "ztna-ems-tag": [],
        "ztna-geo-tag": [],
        "internet-service": "disable",
        "internet-service-name": [],
        "internet-service-group": [],
        "internet-service-custom": [],
        "internet-service-custom-group": [],
        "internet-service-src": "disable",
        "internet-service-src-name": [],
        "internet-service-src-group": [],
        "internet-service-src-custom": [],
        "internet-service-src-custom-group": [],
        "reputation-minimum": 0,
        "reputation-direction": "destination",
        "src-vendor-mac": [],
        "rtp-nat": "disable",
        "rtp-addr": [],
        "send-deny-packet": "disable",
        "firewall-session-dirty": "check-all",
        "schedule": "always",
        "schedule-timeout": "disable",
        "service": [
            {
                "name": "ALL",
                "q_origin_key": "ALL"
            }
        ],
        "tos": "0x00",
        "tos-mask": "0x00",
        "tos-negate": "disable",
        "anti-replay": "enable",
        "tcp-session-without-syn": "disable",
        "geoip-anycast": "disable",
        "geoip-match": "physical-location",
        "dynamic-shaping": "disable",
        "passive-wan-health-measurement": "disable",
        "utm-status": "disable",
        "inspection-mode": "flow",
        "http-policy-redirect": "disable",
        "ssh-policy-redirect": "disable",
        "webproxy-profile": "",
        "profile-type": "single",
        "profile-group": "",
        "profile-protocol-options": "default",
        "ssl-ssh-profile": "no-inspection",
        "av-profile": "",
        "webfilter-profile": "",
        "dnsfilter-profile": "",
        "emailfilter-profile": "",
        "dlp-sensor": "",
        "file-filter-profile": "",
        "ips-sensor": "",
        "application-list": "",
        "voip-profile": "",
        "sctp-filter-profile": "",
        "icap-profile": "",
        "cifs-profile": "",
        "videofilter-profile": "",
        "waf-profile": "",
        "ssh-filter-profile": "",
        "logtraffic": "disable",
        "logtraffic-start": "disable",
        "capture-packet": "disable",
        "auto-asic-offload": "enable",
        "wanopt": "disable",
        "wanopt-detection": "active",
        "wanopt-passive-opt": "default",
        "wanopt-profile": "",
        "wanopt-peer": "",
        "webcache": "disable",
        "webcache-https": "disable",
        "webproxy-forward-server": "",
        "traffic-shaper": "",
        "traffic-shaper-reverse": "",
        "per-ip-shaper": "",
        "nat": "disable",
        "permit-any-host": "disable",
        "permit-stun-host": "disable",
        "fixedport": "disable",
        "ippool": "disable",
        "poolname": [],
        "poolname6": [],
        "session-ttl": "0",
        "vlan-cos-fwd": 255,
        "vlan-cos-rev": 255,
        "inbound": "disable",
        "outbound": "enable",
        "natinbound": "disable",
        "natoutbound": "disable",
        "wccp": "disable",
        "ntlm": "disable",
        "ntlm-guest": "disable",
        "ntlm-enabled-browsers": [],
        "fsso-agent-for-ntlm": "",
        "groups": [],
        "users": [],
        "fsso-groups": [],
        "auth-path": "disable",
        "disclaimer": "disable",
        "email-collect": "disable",
        "vpntunnel": "",
        "natip": "0.0.0.0 0.0.0.0",
        "match-vip": "disable",
        "match-vip-only": "disable",
        "diffserv-forward": "disable",
        "diffserv-reverse": "disable",
        "diffservcode-forward": "000000",
        "diffservcode-rev": "000000",
        "tcp-mss-sender": 0,
        "tcp-mss-receiver": 0,
        "comments": "",
        "label": "",
        "global-label": "",
        "auth-cert": "",
        "auth-redirect-addr": "",
        "redirect-url": "",
        "identity-based-route": "",
        "block-notification": "disable",
        "custom-log-fields": [],
        "replacemsg-override-group": "",
        "srcaddr-negate": "disable",
        "dstaddr-negate": "disable",
        "service-negate": "disable",
        "internet-service-negate": "disable",
        "internet-service-src-negate": "disable",
        "timeout-send-rst": "disable",
        "captive-portal-exempt": "disable",
        "decrypted-traffic-mirror": "",
        "dsri": "disable",
        "radius-mac-auth-bypass": "disable",
        "delay-tcp-npu-session": "disable",
        "vlan-filter": "",
        "sgt-check": "disable",
        "sgt": []
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success = true):_ "Successfully found policies for the provided criteria in FortiGate." _If data is not available (is_success=false):_ "No policies were found for the provided criteria in FortiGate." _If the "Filter Value" parameter is empty (is_success=true):_ "The filter was not applied, because parameter "Filter Value" has an empty value." **The action should fail and stop a playbook execution:** _If the "Filter Key" parameter is set to "Select One" and the "Filter Logic" parameter is set to "Equal" or "Contains":_ "Error executing action "{action name}"." Reason: you need to select a field from the "Filter Key" parameter. _If invalid value is provided for the "Max Records to Return" parameter: "_ Error executing action "{action name}"." Reason: "Invalid value was provided for "Max Records to Return": {provided value}. Positive number should be provided." _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "{action name}"." Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Available Policies **Table Columns:**

  * Name - name
  * Action - action
  * Status - status
  * Source Interface - CSV of srcintf/name
  * Destination Interface - CSV of dstintf/name
  * Source Address Count - len(srcaddr)
  * Destination Address Count - len(dstaddr)

| General  
  
### Ping(`Read`)

Test connectivity to FortiGate with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the FortiGate server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the FortiGate server! Error is {0}".format(exception.stacktrace) | General  
  
### List Address Groups(`Read`)

List available address groups in FortiGate.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Key | DDL | Select OnePossible Values:

  * Name

| No | Specify the key that needs to be used to filter address groups.  
Filter Logic | DDL | Not SpecifiedPossible Values:

  * Not Specified
  * Equal
  * Contains

| No | Specify what filter logic should be applied.Filtering logic is working based on the value provided in the "Filter Key" parameter.  
Filter Value | String | N/A | No | Specify what value should be used in the filter.If "Equal" is selected, action will try to find the exact match among results.If "Contains" is selected, action will try to find results that contain the specified substring.If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.  
Max Records To Return | Integer | 50 | No | Specify the number of records to return. If nothing is provided, the action returns 50 records.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    [
        {
            "name": "G Suite",
            "q_origin_key": "G Suite",
            "type": "default",
            "category": "default",
            "uuid": "8bf3fcac-1547-51ec-9fcf-fe85a3222eff",
            "member": [
                {
                    "name": "gmail.com",
                    "q_origin_key": "gmail.com"
                }
            ],
            "comment": "",
            "exclude": "disable",
            "exclude-member": [],
            "color": 0,
            "tagging": [],
            "allow-routing": "disable",
            "fabric-object": "disable"
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success=true):_ "Successfully found address groups for the provided criteria in FortiGate". _If data is not available (is_success=false):_ "No address groups were found for the provided criteria in FortiGate"  
****_If the "Filter Value" parameter is empty (is_success=true):_ "The filter was not applied, because parameter "Filter Value" has an empty value." **The action should fail and stop a playbook execution:** _If the "Filter Key" parameter is set to "Select One" and the "Filter Logic" parameter is set to "Equal" or "Contains":_ "Error executing action "{action name}"." Reason: you need to select a field from the "Filter Key" parameter. _If an invalid value is provided for the "Max Records to Return" parameter:_ "Error executing action "{action name}"." Reason: "Invalid value was provided for "Max Records to Return": {provided value}. Positive number should be provided". _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "{action name}"." Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
| **Table Name:** Available Policies **Table Columns:**

  * Name - name
  * Type - type
  * Category - category
  * Member Count - len(member)
  * Comment - comment

| General  
  
### Remove Entities From Address Group(`Read`)

Remove entities from the address group in FortiGate. Supported entities: URL, IP Address.

**Note:** This action extracts the domain part of URL entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Location | DDL | DestinationPossible Values:

  * Destination
  * Source

| No | Specify the location for the entities.  
Address Group Name | String | N/A | Yes | Specify the name of the address group from which action should remove entities.  
  
#### Run On

This action runs on the following entities:

  * URL
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully removed the following entities from the address group "{name}" in FortiGate: {entity.identifier}". _If the entity is not found in the address group or it doesn't exist in FortiGate (is_success=true):_ "The following entities were not a part of the address group {address group name} in FortiGate: {entity.identifier}". **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Remove Entities From Policy"." Reason: {0}''.format(error.Stacktrace) _If the address doesn't exist:_ "Error executing action "Remove Entities From Policy". Reason: address group {address group} was not found in FortiGate. Please check the spelling.'' | General  
  
### Remove Entities From Policy(`Read`)

Remove entities from the policy in FortiGate. Supported entities: URL, IP Address, Mac Address.

**Note:** This action extracts the domain part of URL entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Policy Name | String | N/A | Yes | Specify the name of the policy from which action should remove entities.  
  
#### Run On

This action runs on the following entities:

  * URL
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully removed the following entities from the policy "{name}" in FortiGate: {entity.identifier}". _If the entity is not found in the address group or it doesn't exist in FortiGate (is_success=true):_ "The following entities were not a part of the policy {name} in FortiGate: {entity.identifier}". **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Remove Entities From Policy". Reason: {0}''.format(error.Stacktrace) _If the address doesn't exist:_ "Error executing action "Remove Entities From Policy". Reason: policy {name} was not found in FortiGate. Please check the spelling.'' | General  
  
### Add Entities To Policy(`Read`)

Add entities to policy in FortiGate. Supported entities: URL, IP Address.

**Note:** This action extracts the domain part of URL entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Location | DDL | DestinationPossible Values:

  * Destination
  * Source

| No | Specify the location for the entities.  
Policy Name | String | N/A | Yes | Specify the name of the policy to which action should add entities.  
  
#### Run On

This action runs on the following entities:

  * URL
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully added the following entities to policy "{policy name}" in FortiGate: {entity.identifier}". _If data is not available for one entity (is_success=true):_ "The following entities are already a part of policy {policy name} in FortiGate: {entity.identifier}". _If can't add one entity to the policy:_ "Action wasn't able to add the following entities to policy {policy name} in FortiGate: {entity.identifier}". _If data is not available for all entities (is_success=false):_ "None of the provided entities were added to the policy {policyname} in FortiGate." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Entities To Policy". Reason: {0}''.format(error.Stacktrace) _If the policy doesn't exist:_ "Error executing action "Add Entities To Policy". Reason: policy {policy name} was not found in FortiGate. Please check the spelling.'' | General  
  
### Add Entities To Address Group(`Read`)

Add entities to the address group in FortiGate. Supported entities: URL, IP Address.

**Note:** This action extracts the domain part of URL entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Address Group Name | String | N/A | Yes | Specify the name of the address group to which action should add entities.  
  
#### Run On

This action runs on the following entities:

  * URL
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully added the following entities to the address group "{name}" in FortiGate: {entity.identifier}". _If data is not available for one entity (is_success=true):_ "The following entities are already a part of the address group {address group name} in FortiGate: {entity.identifier}". _If can't add one entity to address group (is_success=true):_ "Action wasn't able to add the following entities to address group {address group name} in FortiGate: {entity.identifier}". _If data is not available for all entities (is_success=false):_ None of the provided entities were added to the address group {name} in FortiGate. **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Entities To Policy". Reason: {0}''.format(error.Stacktrace) _If the address doesn't exist:_ "Error executing action "Add Entities To Policy". Reason: address group {address group} was not found in FortiGate. Please check the spelling.'' | General  
  
## Connectors

### FortiGate - Threat Logs Connector(`Read`)

Pull information about different threat logs from FortiGate.

**Note:** The whitelist filter works with the "eventtype" parameter.

#### Configure FortiGate - Threat Logs Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventtype | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{{ip}} | Yes | API root of the FortiGate instance.  
API Key | String | N/A | Yes | API key of the FortiGate account.  
Threat Subtypes To Fetch | CSV | N/A | Yes | A comma-separated list of threat subtypes to ingest. Possible values: virus, webfilter, waf, ips, anomaly, app-ctrl, emailfilter, dlp, voip, gtp, dns, ssh, ssl, cifs, file-filter. The default value is `virus, webfilter, waf, ips, anomaly, file-filter`.  
Threat Log Location | String | N/A | No | Location of the threat log.  
VDOM | String | N/A | No | The Virtual Domain (VDOM) name to target within the FortiGate device.  
Serial Number | String | N/A | No | The serial number of the FortiGate device.  
Lowest Security Level To Fetch | String | warning | No | The lowest security level that needs to be used to fetch threat logs. Possible values: debug, information, notice, warning, error, critical, alert, emergency. If nothing is specified, the connector ingests threat logs with all security levels.  
Max Hours Backwards | Integer | 1 | No | The number of hours for which threat logs should be fetched.  
Max Alerts To Fetch | Integer | 100 | No | The number of alerts to process per one connector iteration per subtype.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist is used as a blacklist.  
Disable Overflow | Checkbox | Unchecked | No | If enabled, the connector ignores the overflow mechanism.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the FortiGate server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
