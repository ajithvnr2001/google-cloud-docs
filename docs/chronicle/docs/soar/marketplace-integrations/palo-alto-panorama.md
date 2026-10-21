---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-panorama/
title: Palo Alto Panorama \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:37:08.703970+00:00
---

# Palo Alto Panorama  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-panorama/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Palo Alto Panorama

**Important:** This integration refers to Palo Alto Networks Panorama.

This document provides guidance on how to integrate Palo Alto Panorama with Google SecOps.

## Integrate Palo Alto Panorama with Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | https://`IP_ADDRESS`/api | Yes | Address of the Palo Alto Networks Panorama instance.  
Username | String | N/A | Yes | A username that should be used to connect to Palo Alto Networks Panorama.   
Password | Password | N/A | Yes | The password of the according user.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

Some actions can require additional configuration like permissions, device name, or device group name.

### Action permissions

For actions to execute properly, the following permissions are required: 

**Tab** | **Required permissions**  
---|---  
Configuration | _Read & Write_Permissions to retrieve or modify Panorama and firewall configurations.  
Operational Requests | _Read & Write_Permissions to run operational commands on Panorama and firewalls.  
Commit | _Read & Write_Permissions to commit Panorama and firewall configurations.  
  
### Obtain device name or device group name

  * To obtain the device name, use the following link:
        
        https://PANORAMA_WEB_CONSOLE_IP/php/rest/browse.php/config::devices
        

  * To obtain the device group name, use the following link:
        
        https://PANORAMA_WEB_CONSOLE_IP/php/rest/browse.php/config::devices::entry[@name='DEVICE_NAME']::device-group
        




### Add IPs to Group

Add IP addresses to an address group.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Device Name | String | N/A | Yes | Specify the name of the device. The default device name for Palo Alto Networks Panorama is localhost.localdomain.  
Device Group Name | String | N/A | Yes | Specify the name of the device group.  
Address Group Name | String | N/A | Yes | Specify the name of the address group.  
  
#### Run on

This action runs on the IP Address entity.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        "192.0.2.1",
        "203.0.113.1"
    ]
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if successful and at least one of the provided IPs was added (is_success = true):_  
print "Successfully added the following IPs to the Palo Alto Networks Panorama address group ''{0}'': \n {1}".format (address_group, entity.identifier list)_If fail to add specific IPs (is_success = true):_ print "Action was not able to add the following IPs to the Palo Alto Networks Panorama address group ''{0}':\n {1}".format(address_group, [entity.identifier])_If fail to add for all IPs (is_success = false):_ Print: "No IPs were added to the Palo Alto Networks Panorama address group '{0}'.format(address_group) | General  
  
### Block IPs in Policy

Block IP addresses in a given policy.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Device Name | String | N/A | Yes | Specify the name of the device. The default device name for Palo Alto Networks Panorama is localhost.localdomain.  
Device Group Name | String | N/A | Yes | Specify the name of the device group.  
Policy Name | String | N/A | Yes | Specify the name of the policy.  
Target | String | N/A | Yes | Specify what should be the target. Possible values: source, destination.   
  
#### Run on

This action runs on the IP Address entity.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        "192.0.2.1",
        "203.0.113.1"
    ]
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if successful and at least one of the provided IPs was blocked (is_success = true):_  
print "Successfully blocked the following IPs in the Palo Alto Networks Panorama policy ''{0}'': \n {1}".format(policy_name, entity.identifier list)_If fail to block specific IPs (is_success = true):_ print "Action was not able to block the following IPs in the Palo Alto Networks Panorama policy ''{0}':\n {1}".format(policy_name, [entity.identifier])_If fail to add for all IPs (is_success = false):_ Print: "No IPs were blocked in the Palo Alto Networks Panorama policy '{0}'.format(policy_name)  | General  
  
### Block URLs

Add URLs to a given URL category.

**Note:** You need to create a policy and add the URL category to that policy in order to block the URL.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Device Name | String | N/A | Yes | Specify the name of the device. The default device name for Palo Alto Networks Panorama is localhost.localdomain.  
Device Group Name | String | N/A | Yes | Specify the name of the device group.  
URL Category Name | String | N/A | Yes | Specify the name of the URL Category.  
  
#### Run on

This action runs on the URL entity.

#### Action results

##### Script result

**Script Result Name** | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
****  
  
##### JSON result
    
    
    [
        "www.example.com"
    ]
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if successful and at least one of the provided URLs was added (is_success = true):_  
print "Successfully added the following URLs to the Palo Alto Networks Panorama URL Category ''{0}'': \n {1}".format(category, entity.identifier list)___If fail to add specific URLs (is_success = true):_ print "Action was not able to add the following URLs to the Palo Alto Networks Panorama URL Category''{0}':\n {1}". format(category, [entity.identifier])___If fail to add for all URLs (is_success = false):_ Print: "No URLs were added to the Palo Alto Networks Panorama URL Category '{0}'.format(category) | General  
  
### Edit Blocked Applications

Block and unblock applications. Each application is added to or removed from a given policy.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Applications To Block | String | N/A | No | Specify what kind of application should be blocked. Example: apple-siri,windows-azure  
Applications To UnBlock | String | N/A | No | Specify what kind of application should be unblocked. Example: apple-siri,windows-azure  
Device Name | String | N/A | Yes | Specify the name of the device. The default device name for Palo Alto Networks Panorama is localhost.localdomain.  
Device Group Name | String | N/A | Yes | Specify the name of the device group.  
Policy Name | String | N/A | Yes | Specify the name of the policy.  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        "1und1-mail",
        "Filter",
        "Group1",
        "SiemplifyAppBlacklist",
        "apple-siri",
        "google-analytics"
    ]
    

### Get Blocked Applications

List all blocked applications in a given policy.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Device Name | String | N/A | Yes | Specify the name of the device. The default device name for Palo Alto Networks Panorama is localhost.localdomain.  
Device Group Name | String | N/A | Yes | Specify the name of the device group.  
Policy Name | String | N/A | Yes | Specify the name of the policy.  
  
#### Run On

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value options** | **Example**  
---|---|---  
blocked_applications | N/A | N/A  
  
##### JSON result
    
    
    [
        "1und1-mail",
        "Filter",
        "Group1",
        "SiemplifyAppBlacklist",
        "apple-siri",
        "google-analytics"
    ]
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | "Successfully listed blocked applications in a policy ''{0}: {1}".format(Policy name, \n separated list of applications) | General  
  
### Ping

Test connectivity to Panorama.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Commit Changes

**Warning:** To apply the changes, you need to first _commit_ those changes, and then _push_ them to firewalls.

Action commits changes in Palo Alto Networks Panorama.

To use the `Only My Changes` parameter, the user must be an administrator.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Only My Changes | Checkbox | Unchecked | No | If enabled, action will only commit changes that were done by the current user.  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Push Changes

**Warning:** To apply the changes, you need to first _commit_ those changes, and then _push_ them to firewalls.

Push commits of a device group in Palo Alto Networks Panorama.

It can take several minutes before changes are pushed.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Device Group Name | String | N/A | Yes | Specify the name of the device group. Visit action documentation to get more insights on where you can find this value.  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Remove IPs From Group

Remove IP addresses from an address group.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Device Name | String | N/A | Yes | Specify the name of the device. The default device name for Palo Alto Networks Panorama is localhost.localdomain.  
Device Group Name | String | N/A | Yes | Specify the name of the device group.  
Address Group Name | String | N/A | Yes | Specify the name of the address group.  
  
#### Run on

This action runs on the IP Address entity.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        "192.0.2.1",
        "203.0.113.1"
    ]
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if successful and at least one of the provided IPs was removed (is_success = true):_  
print "Successfully removed the following IPs from the Palo Alto Networks Panorama address group ''{0}'': \n {1}".format(address_group, entity.identifier list)___If fail to remove specific IPs (is_success = true):_ print "Action was not able to remove the following IPs from the Palo Alto Networks Panorama address group ''{0}':\n {1}".format(address_group, [entity.identifier])___If fail to remove for all IPs (is_success = false):_ Print: "No IPs were removed from the Palo Alto Networks Panorama address group '{0}'.format(address_group) | General  
  
### Unblock IPs in Policy

Block IP addresses in a given policy.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Device Name | String | N/A | Yes | Specify the name of the device. The default device name for Palo Alto Networks Panorama is localhost.localdomain.  
Device Group Name | String | N/A | Yes | Specify the name of the device group.  
Policy Name | String | N/A | Yes | Specify the name of the policy.  
Target | String | N/A | Yes | Specify what should be the target. Possible values: source, destination.   
  
#### Run on

This action runs on the IP Address entity.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        "192.0.2.1",
        "203.0.113.1"
    ]
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if successful and at least one of the provided IPs was unblocked (is_success = true):_  
print "Successfully unblocked the following IPs in the Palo Alto Networks Panorama policy ''{0}'': \n {1}".format(policy_name, entity.identifier list)___If fail to block specific IPs (is_success = true):_ print "Action was not able to unblock the following IPs in the Palo Alto Networks Panorama policy ''{0}':\n {1}".format(policy_name, [entity.identifier])___If fail to add for all IPs (is_success = false):_ Print: "No IPs were unblocked in the Palo Alto Networks Panorama policy '{0}'.format(policy_name)  | General  
  
### Unblock URLs

Remove URLs from a given URL category.

#### Parameters

**Parameter** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Device Name | String | N/A | Yes | Specify the name of the device. The default device name for Palo Alto Networks Panorama is localhost.localdomain.  
Device Group Name | String | N/A | Yes | Specify the name of the device group.  
URL Category Name | String | N/A | Yes | Specify the name of the URL Category.  
  
#### Run on

This action runs on the URL entity.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
****  
  
##### JSON result
    
    
    [
        "www.example.com"
    ]
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | _if successful and at least one of the provided URLs was removed (is_success = true):_  
print "Successfully removed the following URLs from the Palo Alto Networks Panorama URL Category ''{0}'': \n {1}".format(category, entity.identifier list)___If fail to add specific URLs (is_success = true):_ print "Action was not able to remove the following URLs from the Palo Alto Networks Panorama URL Category''{0}':\n {1}".format(category, [entity.identifier])___If fail to add for all URLs (is_success = false):_ Print: "No URLs were removed from the Palo Alto Networks Panorama URL Category '{0}'.format(category) | General  
  
### Search Logs

Search logs in Palo Alto Networks Panorama based on the query.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Log Type | DDL | Traffic | Yes | Specify which log type should be returned.Possible values: Traffic, Threat, URL Filtering, WildFire Submissions, Data Filtering, HIP Match, IP Tag, User ID, Tunnel Inspection, Configuration, System, Authentication.  
Query | String | N/A | No | Specify what query filter should be used to return logs.  
Max Hours Backwards | Integer | N/A | No | Specify the amount of hours from where to fetch logs.  
Max Logs to Return | Integer | 50 | No | Specify how many logs to return. The maximum is 1000.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
      <logs count="1" progress="100">
                    <entry logid="28889">
                        <domain>0</domain>
                        <receive_time>2020/07/06 13:51:19</receive_time>
                        <serial>007051000096801</serial>
                        <seqno>21467</seqno>
                        <actionflags>0x0</actionflags>
                        <is-logging-service>no</is-logging-service>
                        <type>THREAT</type>
                        <subtype>spyware</subtype>
                        <config_ver>0</config_ver>
                        <time_generated>2020/07/06 13:51:10</time_generated>
                        <src>192.0.2.1</src>
                        <dst>203.0.113.254</dst>
                        <natsrc>198.51.100.4</natsrc>
                        <natdst>203.0.113.254</natdst>
                        <rule>inside to outside</rule>
                        <srcloc code="192.0.2.0-192.0.2.255" cc="192.0.2.0-192.0.2.255">192.0.2.0-192.0.2.255</srcloc>
                        <dstloc code="United States" cc="US">United States</dstloc>
                        <app>ms-update</app>
                        <vsys>vsys1</vsys>
                        <from>inside</from>
                        <to>Outside</to>
                        <inbound_if>ethernet1/2</inbound_if>
                        <outbound_if>ethernet1/1</outbound_if>
                        <logset>log forward1</logset>
                        <time_received>2020/07/06 13:51:10</time_received>
                        <sessionid>2348</sessionid>
                        <repeatcnt>1</repeatcnt>
                        <sport>56761</sport>
                        <dport>80</dport>
                        <natsport>45818</natsport>
                        <natdport>80</natdport>
                        <flags>0x80403000</flags>
                        <flag-pcap>yes</flag-pcap>
                        <flag-flagged>no</flag-flagged>
                        <flag-proxy>no</flag-proxy>
                        <flag-url-denied>no</flag-url-denied>
                        <flag-nat>yes</flag-nat>
                        <captive-portal>no</captive-portal>
                        <non-std-dport>no</non-std-dport>
                        <transaction>no</transaction>
                        <pbf-c2s>no</pbf-c2s>
                        <pbf-s2c>no</pbf-s2c>
                        <temporary-match>yes</temporary-match>
                        <sym-return>no</sym-return>
                        <decrypt-mirror>no</decrypt-mirror>
                        <credential-detected>no</credential-detected>
                        <flag-mptcp-set>no</flag-mptcp-set>
                        <flag-tunnel-inspected>no</flag-tunnel-inspected>
                        <flag-recon-excluded>no</flag-recon-excluded>
                        <flag-wf-channel>no</flag-wf-channel>
                        <pktlog>1594032670-2348.pcap</pktlog>
                        <proto>tcp</proto>
                        <action>alert</action>
                        <tunnel>N/A</tunnel>
                        <tpadding>0</tpadding>
                        <cpadding>0</cpadding>
                        <rule_uuid>9f1bcd9d-0ebc-4815-87cd-b377e0b4817f</rule_uuid>
                        <dg_hier_level_1>11</dg_hier_level_1>
                        <dg_hier_level_2>0</dg_hier_level_2>
                        <dg_hier_level_3>0</dg_hier_level_3>
                        <dg_hier_level_4>0</dg_hier_level_4>
                        <device_name>PA-VM</device_name>
                        <vsys_id>1</vsys_id>
                        <tunnelid_imsi>0</tunnelid_imsi>
                        <parent_session_id>0</parent_session_id>
                        <threatid>Suspicious HTTP Evasion Found</threatid>
                        <tid>14984</tid>
                        <reportid>0</reportid>
                        <category>computer-and-internet-info</category>
                        <severity>informational</severity>
                        <direction>client-to-server</direction>
                        <url_idx>1</url_idx>
                        <padding>0</padding>
                        <pcap_id>1206408081198547007</pcap_id>
                        <contentver>AppThreat-0-0</contentver>
                        <sig_flags>0x0</sig_flags>
                        <thr_category>spyware</thr_category>
                        <assoc_id>0</assoc_id>
                        <ppid>4294967295</ppid>
                        <http2_connection>0</http2_connection>
                        <misc>3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/0</misc>
                        <tunnelid>0</tunnelid>
                        <imsi/>
                        <monitortag/>
                        <imei/>
                    </entry>
                </logs>
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and returned at least one log (is_success = true):_  
print "Successfully listed {0} logs. Used query: '{1}' ".format(log_type)___if successful, but no logs(is_success = false):_  
print "No {0} logs were found. Used query: '{1}' ".format(log_type, query)___If incorrect query (response status = error) (is_success=false):_ print "Action wasn't able to list logs. Reason: {0}".format(response/msg) **The action should fail and stop a playbook execution:** _if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "Search Logs". Reason: {0}''.format(error.Stacktrace) | General  
CSV Case Wall (Traffic) | **Name:** Traffic Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Src IP (mapped as src)
  * Dst IP (mapped as dst)
  * Action (mapped as action)
  * Type (mapped as subtype)
  * Application (mapped as app)

|   
CSV Case Wall (Threat) | **Name:** Threat Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Description (mapped as threatID)
  * Src IP (mapped as src)
  * Dst IP (mapped as dst) 
  * Name (mapped as misc)
  * Type (mapped as subtype)
  * Severity (mapped as severity)

|   
CSV Case Wall(URL Filtering)  | **Name:** URL Filtering Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Src IP (mapped as src)
  * Dst IP (mapped as dst)
  * URL (mapped as misc) 
  * Category (mapped as category)
  * Severity (mapped as severity) 
  * Action (mapped as action)

|   
CSV Case Wall(Wildfire Submissions)  | **Name:** Wildfire Submission Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Description (mapped as threatID)
  * Src IP (mapped as src)
  * Dst IP (mapped as dst)
  * Name (mapped as misc)
  * Type (mapped as subtype)
  * Severity (mapped as severity)
  * Action (mapped as action)
  * Hash (mapped as filedigest)
  * File Type (mapped as filetype)

|   
CSV Case Wall(Data Filtering)  | **Name:** Data Filtering Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Description (mapped as threatID)
  * Src IP (mapped as src)
  * Dst IP (mapped as dst)
  * Name (mapped as misc)
  * Type (mapped as subtype)
  * Severity (mapped as severity)
  * Action (mapped as action)

|   
CSV Case Wall(HIP Match)  | **Name:** HIP Match Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * IP (mapped as src) 
  * HIP (mapped as matchname)
  * Repeat Count(mapped as repeatcnt) 
  * Device Name (mapped as device_name)

|   
CSV Case Wall(IP Tag)  | **Name:** IP Tag Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * IP (mapped as ip)
  * Tag Name (mapped as tag_name)
  * Device Name (mapped as device_name) 
  * Event ID (mapped as event_id)

|   
CSV Case Wall(User ID)  | **Name:** User ID Match Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * IP (mapped as ip)
  * User (mapped as user)
  * Device Name (mapped as device_name)
  * Type (mapped as subtype)

|   
CSV Case Wall(Tunnel Inspection)  | **Name:** Tunnel Inspection Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Src IP (mapped as src)
  * Dst IP (mapped as dst)
  * Application (mapped as app)
  * Type (mapped as subtype)
  * Severity (mapped as severity) 
  * Action (mapped as action)

|   
CSV Case Wall(Configuration)  | **Name:** Configuration Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Command (mapped as cmd)
  * Admin (mapped as admin)
  * Device Name (mapped as device_name)

|   
CSV Case Wall(System)  | **Name:** System Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Device Name (mapped as device_name)
  * Type (mapped as subtype)
  * Severity (mapped as severity)
  * Description (mapped as opaque)

|   
CSV Case Wall(Authentication)  | **Name:** Authentication Logs**Columns:**

  * Receive Time (mapped as receive_time)
  * Device Name (mapped as device_name)
  * IP (mapped as ip)
  * User (mapped as user)
  * Type (mapped as subtype)
  * Severity (mapped as severity)
  * Description (mapped as desc)

|   
  
### Get Correlated Traffic Between IPs

Action returns correlated network traffic logs from Palo Alto Networks Panorama between the source IP address and the destination IP address.

#### Playbook recommendations

To automate the process of retrieving correlated traffic between two IPs, use the `Event.sourceAddress` attribute for the source IP address and `Event.destinationAddress` for the destination IP address. This approach is recommended for alerts that only have one Google SecOps event. In other cases, unexpected results can happen.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Source IP | CSV | N/A | Yes | Specify source IP that will be used to get traffic.  
Destination IP | CSV | N/A | Yes | Specify destination IP that will be used to get traffic.  
Max Hours Backwards | Integer | N/A | No | Specify the amount of hours from where to fetch logs.  
Max Logs to Return | Integer | 50 | No | Specify how many logs to return. The maximum is 1000.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
         <logs count="1" progress="100">
                        <entry logid="28889">
                            <domain>0</domain>
                            <receive_time>2020/07/06 13:51:19</receive_time>
                            <serial>007051000096801</serial>
                            <seqno>21467</seqno>
                            <actionflags>0x0</actionflags>
                            <is-logging-service>no</is-logging-service>
                            <type>THREAT</type>
                            <subtype>spyware</subtype>
                            <config_ver>0</config_ver>
                            <time_generated>2020/07/06 13:51:10</time_generated>
                            <src>192.0.2.3</src>
                            <dst>198.51.100.254</dst>
                            <natsrc>203.0.113.4</natsrc>
                            <natdst>198.51.100.254</natdst>
                            <rule>inside to outside</rule>
                            <srcloc code="192.0.2.0-192.0.2.255" cc="192.0.2.0-192.0.2.255">192.0.2.0-192.0.2.255</srcloc>
                            <dstloc code="United States" cc="US">United States</dstloc>
                            <app>ms-update</app>
                            <vsys>vsys1</vsys>
                            <from>inside</from>
                            <to>Outside</to>
                            <inbound_if>ethernet1/2</inbound_if>
                            <outbound_if>ethernet1/1</outbound_if>
                            <logset>log forward1</logset>
                            <time_received>2020/07/06 13:51:10</time_received>
                            <sessionid>2348</sessionid>
                            <repeatcnt>1</repeatcnt>
                            <sport>56761</sport>
                            <dport>80</dport>
                            <natsport>45818</natsport>
                            <natdport>80</natdport>
                            <flags>0x80403000</flags>
                            <flag-pcap>yes</flag-pcap>
                            <flag-flagged>no</flag-flagged>
                            <flag-proxy>no</flag-proxy>
                            <flag-url-denied>no</flag-url-denied>
                            <flag-nat>yes</flag-nat>
                            <captive-portal>no</captive-portal>
                            <non-std-dport>no</non-std-dport>
                            <transaction>no</transaction>
                            <pbf-c2s>no</pbf-c2s>
                            <pbf-s2c>no</pbf-s2c>
                            <temporary-match>yes</temporary-match>
                            <sym-return>no</sym-return>
                            <decrypt-mirror>no</decrypt-mirror>
                            <credential-detected>no</credential-detected>
                            <flag-mptcp-set>no</flag-mptcp-set>
                            <flag-tunnel-inspected>no</flag-tunnel-inspected>
                            <flag-recon-excluded>no</flag-recon-excluded>
                            <flag-wf-channel>no</flag-wf-channel>
                            <pktlog>1594032670-2348.pcap</pktlog>
                            <proto>tcp</proto>
                            <action>alert</action>
                            <tunnel>N/A</tunnel>
                            <tpadding>0</tpadding>
                            <cpadding>0</cpadding>
                            <rule_uuid>9f1bcd9d-0ebc-4815-87cd-b377e0b4817f</rule_uuid>
                            <dg_hier_level_1>11</dg_hier_level_1>
                            <dg_hier_level_2>0</dg_hier_level_2>
                            <dg_hier_level_3>0</dg_hier_level_3>
                            <dg_hier_level_4>0</dg_hier_level_4>
                            <device_name>PA-VM</device_name>
                            <vsys_id>1</vsys_id>
                            <tunnelid_imsi>0</tunnelid_imsi>
                            <parent_session_id>0</parent_session_id>
                            <threatid>Suspicious HTTP Evasion Found</threatid>
                            <tid>14984</tid>
                            <reportid>0</reportid>
                            <category>computer-and-internet-info</category>
                            <severity>informational</severity>
                            <direction>client-to-server</direction>
                            <url_idx>1</url_idx>
                            <padding>0</padding>
                            <pcap_id>1206408081198547007</pcap_id>
                            <contentver>AppThreat-0-0</contentver>
                            <sig_flags>0x0</sig_flags>
                            <thr_category>spyware</thr_category>
                            <assoc_id>0</assoc_id>
                            <ppid>4294967295</ppid>
                            <http2_connection>0</http2_connection>
                            <misc>3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/0</misc>
                            <tunnelid>0</tunnelid>
                            <imsi/>
                            <monitortag/>
                            <imei/>
                        </entry>
                    </logs>
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful for at least one pair(is_success = true):_  
print "Successfully listed correlated logs for the following pairs of Source and Destination IPs:\n.{0} - {1}".format(source IP, destination IP.) ___if unsuccessful for certain pairs or incomplete pairs (is_success = true):_  
print "Unable to list correlated logs for the following pairs of Source and Destination IPs:\n.{0} - {1}".format(source IP, destination IP. In the incomplete pair, missing part should be replaced to "N/A") ___if no logs for every pair(is_success = false):_  
print "No correlated network traffic logs were found."  
**The action should fail and stop a playbook execution:** _if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "Get Correlated Traffic Between IPs". Reason: {0}''.format(error.Stacktrace) | General  
CSV Case Wall (For each pair) | **Name:** Traffic Logs between {Source IP} and {Destination IP}**Columns:**

  * Receive Time (mapped as receive_time)
  * Src IP (mapped as src)
  * Dst IP (mapped as dst)
  * Action (mapped as action)
  * Type (mapped as subtype)
  * Application (mapped as app)

|   
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Palo Alto Panorama - Threat Log Connector

Connector ingests threat logs based on the specified query filter and its parameters.

**Note:** Service account is not supported.

#### Connector permissions

For the connector to function properly, the following permissions are needed: 

**Tab** | **Required permissions**  
---|---  
Web UI | 

  * Privacy (all)
  * Tasks
  * Global (all)

  
XML API | 

  * Log
  * Operational Requests

  
  
#### How to work with the `Query Filter` connector parameter

The `Query Filter` connector parameter lets you customize filters that are used to ingest logs. By default, the connector uses a time filter and severity filter, but it is possible to have more specific filters.

Example of a query used by the connector is as follows:

`{time_filter} and {severity_filter} and {custom_query_filter}`

The value you put in the `Query Filter` connector parameter is used in {custom_query_filter}. For example, if you specify the `Query Filter` with the `(subtype eq spyware)` attribute, the example of the query is as follows:

`(time_generated geq '2020/06/22 08:00:00') and (severity geq medium) and (subtype eq spyware)`

**Note:** The connector automatically prepends the `and` operator to every query. The `time_generated` and `severity` keywords are already a part of the query.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.   
Event Field Name | String | subtype | Yes | Enter the source field name in order to retrieve the Event Field name.   
Environment Field Name  
| String | "" | No | Describes the name of the field where the environment name is stored.  If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern  
| String | .* | No | A regular expression pattern to run on the value found in the `Environment Field Name` field. Default is .* to catch all and return the value unchanged. Used to let the user manipulate the environment field using the regular expression logic. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://`IP_ADDRESS`/api | Yes | API root of Palo Alto Networks Panorama instance.  
Username | String | N/A | Yes | Username of the Palo Alto Networks Panorama account.  
Password | Password | N/A | Yes | Password of the Palo Alto Networks Panorama account.  
Query Filter | String | N/A | No | Specify additional filters in the query.  
Lowest Severity To Fetch | String | N/A | Yes | Lowest severity that will be used to fetch threat logs. Possible values: Informational, Low, Medium, High, Critical.   
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch logs.  
Max Logs To Fetch | Integer | 25 | No | How many logs to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, the dynamic list will be used as a blocklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Palo Alto Networks Panorama server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
