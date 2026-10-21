---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-next-gen-firewall/
title: Integrate Palo Alto Next Gen Firewall with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:04:38.809867+00:00
---

# Integrate Palo Alto Next Gen Firewall with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-next-gen-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Palo Alto Next Gen Firewall with Google SecOps

**Important:** This integration refers to Palo Alto Networks Next-Generation Firewall (NGFW).

This document provides guidance on how to integrate Palo Alto Next Gen Firewall with Google Security Operations.

## Before you begin

The integration requires a custom administrator role in PAN-OS. Ensure that the API account has a role profile with **API Access** enabled.

**Note:** These requirements are based on codebase analysis. Validate these permissions against your PAN-OS version before you implement the integration.

### Integration-level permissions

The administrator role requires `Read/Write` access for the following nodes in the **REST API** or **XML API** tabs:

  * **Configuration > Device**: `Address Groups`, `Address Objects`, `Security Policies`, and `URL Categories`.
  * **Operational Requests** : `Commit` (to apply changes) and `Operational Requests` (`Read`).



### Minimum permissions by action

Review the following table for the specific API paths and permissions required to execute each integration action.

Action | Required permissions  
---|---  
Add IPs to Group | Configuration > Device > `Address Groups` and `Address Objects` (`Read/Write`)  
Block IPs in Policy | Configuration > Device > `Security Policies` and `Address Objects` (`Read/Write`)  
Block URLs / Unblock URLs | Configuration > Device > `URL Categories` (`Read/Write`)  
Commit Changes | Operational Requests > `Commit` (`Read/Write`)  
Edit/Get Blocked Applications | Configuration > Device > `Security Policies` (`Read/Write`) and Operational Requests (`Read`)  
Ping | Baseline API Access (keygen)  
  
## Integration parameters

The **Palo Alto Next Gen Firewall** integration requires the following parameters:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | https://x.x.x.x/api | Yes | API root of the Palo Alto Networks Next-Generation Firewall instance.  
Username | String | N/A | Yes | Username of the Palo Alto Networks Next-Generation Firewall account.  
Password | Password | N/A | Yes | Password of the Palo Alto Networks Next-Generation Firewall account.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verifies that the SSL certificate for the connection to the Palo Alto Networks Next-Generation Firewall server is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add IPs to Group

Add IP addresses to an address group.

**Note:** This change remains in the candidate configuration until you run the **Commit Changes** action.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device Name | String | N/A | The device name in which the group is located. The default device name of NGFW is localhost.localdomain. In case configured differently, please refer to https://php/rest/browse.php/config::devices for the list of all the device names and select the relevant device.  
Vsys Name | String | N/A | Specify a comma-separated list of vsys on which you want to run the action. The default vsys name for NGFW is `vsys1`. If it is configured differently, see `https://{ip}/php/rest/browse.php/config::devices::entry[@name='{device name{']::vsys` for the list of all available vsys on the device.  
Address Group Name | String | N/A | Group name value.  
Use Shared Objects | Checkbox | N/A | If enabled, action will use shared objects instead of vsys. Note: action will not create a shared address group, if it doesn't exist.  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    ["1.1.1.1", "2.2.2.2"]
    
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success for one vsys and one IP (is_success=true):** Successfully added the following IPs to the group "{group_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for one vsys and one IP (is_success=true):** Action wasn't able to add the following IPs to the group "{group_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for all IPs in vsys (is_success=false, if the same behavior for all vsys and is_success=true if partial):** No IPs were added to the group "{group_name}" for vsys "{vsys name}" in Palo Alto NGFW.**If at least one of the vsys were not found (fail):** Error executing action "Add Ips to group". Reason: The following vsys were not found in Palo Alto NGFW: {vsys that were not found}**If "Use Shared Objects" is disabled and none of the "Device name" and "Vsys name" are provided (fail):** Error executing action "{action_name}": Either "Use Shared Objects" parameter should be enabled or "Device name" and "Vsys name" to be provided.**If device name is invalid (fail):** Error executing action "Add Ips to group". Reason: Device {device name} was not found. Please check the spelling.**If "Use Shared Objects" is enabled and at least one IP address was added (is_success=true):** Successfully added the following IP addresses to the shared address group '{Group Name}' in Palo Alto NGFW:\n {entity.identifier}**If "Use Shared Objects" is enabled and one IP addresses was already a part of address group (is_success=true) :** The following IP addresses were already a part of the the shared address group '{Group Name}' in Palo Alto NGFW:\n {entity.identifier}**If "Use Shared Objects" is enabled and at least one IP address was not added (is_success=true):** Action wasn't able to add the following IP addresses to the shared address group '{Group Name}' in Palo Alto NGFW:\n {entity.identifier}**If "Use Shared Objects" is enabled and no IP address was added (is_success=false):** No IP addresses were added to the shared address group '{Group Name}' in Palo Alto NGFW.**If Address Group wasn't found (fail):** Error executing action "Add Ips to group". Shared address group "{Group Name}" was not found in Palo Alto NGFW.**Critical Error** Error executing action "Add Ips to group". Reason: {error traceback} | General  
  
### Block IPs in Policy

Block IP addresses in a policy (each IP is added individually to the policy).

**Note:** This change remains in the candidate configuration until you run the **Commit Changes** action.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device Name | String | N/A | The device name in which the group is located. The default device name of NGFW is localhost.localdomain. In case configured differently, please refer to https://php/rest/browse.php/config::devices for the list of all the device names and select the relevant device.  
Vsys Name | String | N/A | "Specify a comma-separated list of vsys on which you want to execute the action. The default vsys name of NGFW is vsys1. In case configured differently, please refer to https://{ip}/php/rest/browse.php/config::devices::entry[@name='{device name{']::vsys for the list of all available vsys on the device."  
Policy Name | String | N/A | Policy name value.  
Target | String | N/A | Has to be source or destination.  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        "1.1.1.1",
        "2.2.2.2"
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success for one vsys and one IP (is_success=true):** Successfully blocked the following IPs in policy "{policy name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for one vsys and one IP (is_success=true):** Action wasn't able to block the following IPs in policy "{policy_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for all IPs in vsys (is_success=false, if the same behavior for all vsys and is_success=true if partial):** No IPs were blocked in policy "{policy_name}" for vsys "{vsys name}" in Palo Alto NGFW.**If Policy name wasn't found in some vsys (is_success=true):** Policy "{policy name}" wasn't found in the following vsys in the Palo Alto NGFW: {vsys that don't have the policy}**If at least one of the vsys were not found (fail):** Error executing action "Block Ips in policy". Reason: The following vsys were not found in Palo Alto NGFW: {vsys that were not found}**If Policy name wasn't found in all vsys (fail):** Error executing action "Block Ips in policy". Reason: Policy "{policy name}" wasn't found in the provided vsys. Please check the spelling.**If device name is invalid (fail):** Error executing action "Block Ips in policy". Reason: Device "{device name}" was not found. Please check the spelling.**if Target != source or destination:** Error executing action "Block Ips in policy". Reason: Target should be either "source" or "destination"**Critical Error:** Error executing action "Block Ips in policy". Reason: {error traceback} | General  
  
### Block URLs

Add URLs to a given URL category.

**Note:** To correctly block the URL, create a policy, and add the desired URL category to it. 

This change remains in the candidate configuration until a **Commit Changes** action is executed.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device Name | String | N/A | The device name in which the group is located. The default device name of NGFW is localhost.localdomain. In case configured differently, please refer to https://php/rest/browse.php/config::devices for the list of all the device names and select the relevant device.  
Vsys Name | String | N/A | "Specify a comma-separated list of vsys on which you want to execute the action. The default vsys name of NGFW is vsys1. In case configured differently, please refer to https://{ip}/php/rest/browse.php/config::devices::entry[@name='{device name{']::vsys for the list of all available vsys on the device."  
URL Category Name | String | N/A | Policy name value.  
Use Shared Objects | Checkbox | N/A | If enabled, action will use shared objects instead of vsys.  
  
#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        "www.example.com"
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success for one vsys and one URL (is_success=true):** Successfully added the following URLs to the category "{category_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for one vsys and one URL (is_success=true):** Action wasn't able to add the following URLs to the category "{category_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for all URLs in vsys:** No URLs were added to the category "{category_name}" for vsys "{vsys name}" in Palo Alto NGFW.**If Group name wasn't found in some vsys (is_success=true):** Category "{category name}" wasn't found in the following vsys in the Palo Alto NGFW: {vsys that don't have the category}**If "Use Shared Objects" is disabled and none of the "Device name" and "Vsys name" are provided (fail):** Error executing action "{action_name}": Either "Use Shared Objects" parameter should be enabled or "Device name" and "Vsys name" to be provided.**If at least one of the vsys were not found (fail):** Error executing action "Block Urls". Reason: The following vsys were not found in Palo Alto NGFW: {vsys that were not found}**If Category name wasn't found in all vsys (fail):** Error executing action "Block Urls". Reason: Category "{category name}" wasn't found in the provided vsys. Please check the spelling.**If device name is invalid (fail):** Error executing action "Block Urls". Reason: Device "{device name}" was not found. Please check the spelling.**If "Use Shared Objects" is enabled and at least one URL was added (is_success=true):** Successfully added the following URLs to the shared category '{Category Name}' in Palo Alto NGFW:\n {entity.identifier}**If "Use Shared Objects" is enabled and one URL was already a part of URL Category (is_success=true) :** The following URLs were already a part of the the shared category '{Category Name}' in Palo Alto NGFW:\n {entity.identifier}**If "Use Shared Objects" is enabled and at least one URL was not added (is_success=true):** Action wasn't able to add the following URLs to the shared category '{Category Name}' in Palo Alto NGFW:\n {entity.identifier}**If "Use Shared Objects" is enabled and no URL was added (is_success=false):** No URLs were added to the shared category '{Category Name}' in Palo Alto NGFW.**If Category wasn't found (fail):** Error executing action "Block Urls". Shared category "{Category Name}" was not found in Palo Alto NGFW.**Critical Error:** Error executing action "Block Urls". Reason: {error traceback} | General  
  
### Commit Changes

Commit changes in Palo Alto NGFW.

**Note:** For using the Only My Changes option, the user must be an admin.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Only My Changes | String | N/A | Commit only the configured use changes.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Edit Blocked Applications

Block and unblock applications. Each application is added to or removed from a given policy.

**Note:** This change remains in the candidate configuration until you run the **Commit Changes** action.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Applications To Block | String | N/A | List of applications to block, comma separated. Example: apple-siri,app2  
Applications To UnBlock | String | N/A | List of applications to unblock, comma separated. Example: apple-siri,app2  
Device Name | String | N/A | The device name in which the group is located. The default device name of NGFW is localhost.localdomain. In case configured differently, please refer to https://php/rest/browse.php/config::devices for the list of all the device names and select the relevant device.  
Vsys Name | String | N/A | "Specify a comma-separated list of vsys on which you want to execute the action. The default vsys name of NGFW is vsys1. In case configured differently, please refer to https://{ip}/php/rest/browse.php/config::devices::entry[@name='{device name{']::vsys for the list of all available vsys on the device."  
Policy Name | String | N/A | Policy name value.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        "1und1-mail",
        "Filter",
        "Group1",
        "SiemplifyAppBlacklist",
        "apple-siri",
        "google-analytics"
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success for one vsys for blocking of applications (is_success=true):** Successfully added the following applications to the policy "{policy name}" in vsys "{vsys name}" in Palo Alto NGFW: {applications to block}**Not success for one vsys for blocking of one application (is_success-=true):** Action wasn't able to add the following applications to the policy "{policy name}" in vsys "{vsys name}" in Palo Alto NGFW: {applications to block}**Not success for one vsys for blocking of all applications (is_success-=true):** No applications were added to the policy "{policy name}" in vsys "{vsys name}" in Palo Alto NGFW: {applications to block}**Success for one vsys for unblocking of applications (is_success=true):** Successfully removed the following applications from the policy "{policy name}" in vsys "{vsys name}" in Palo Alto NGFW: {applications to block}**Not success for one vsys for blocking of one application (is_success-=true):** Action wasn't able to remove the following applications from the policy "{policy name}" in vsys "{vsys name}" in Palo Alto NGFW: {applications to block}**Not success for one vsys for blocking of all applications (is_success-=true):** No applications were removed from the policy "{policy name}" in vsys "{vsys name}" in Palo Alto NGFW: {applications to block}**If Policy name wasn't found in some vsys (is_success=true):** Policy "{policy name}" wasn't found in the following vsys in the Palo Alto NGFW: {vsys that don't have the policy}**If at least one of the vsys were not found (fail):** Error executing action "Edit Blocked Applications". Reason: The following vsys were not found in Palo Alto NGFW: {vsys that were not found}**If Policy name wasn't found in all vsys (fail):** Error executing action "Edit Blocked Applications". Reason: Policy "{policy name}" wasn't found in the provided vsys. Please check the spelling.**If device name is invalid (fail):** Error executing action "Edit Blocked Applications". Reason: Device "{device name}" was not found. Please check the spelling.**Critical Error:** Error executing action "Edit Blocked Applications". Reason: {error traceback} | General  
  
### Get Blocked Applications

List all blocked applications in a given policy.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device Name | String | N/A | The device name in which the group is located. The default device name of NGFW is localhost.localdomain. In case configured differently, please refer to https://php/rest/browse.php/config::devices for the list of all the device names and select the relevant device.  
Vsys Name | String | N/A | "Specify a comma-separated list of vsys on which you want to execute the action. The default vsys name of NGFW is vsys1. In case configured differently, please refer to https://{ip}/php/rest/browse.php/config::devices::entry[@name='{device name{']::vsys for the list of all available vsys on the device."  
Policy Name | String | N/A | Policy name value.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
blocked_applications | N/A | N/A  
  
##### JSON Result
    
    
    [
        "1und1-mail",
        "Filter",
        "Group1",
        "SiemplifyAppBlacklist",
        "apple-siri",
        "google-analytics"
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success for one vsys (is_success=true):** Successfully listed available blocked applications in the following vsys in Palo Alto NGFW: {vsys with success}**Not success for one vsys (is_success=true):** Action wasn't able to list available blocked application in the following vsys in Palo Alto NGFW: {vsys with success}**Not success for all IPs in all vsys:** No blocked applications were found in the provided vsys in Palo Alto NGFW.**If Policy name wasn't found in some vsys (is_success=true):** Policy "{policy name}" wasn't found in the following vsys in the Palo Alto NGFW: {vsys that don't have the policy}**If at least one of the vsys were not found (fail):** Error executing action "Get Blocked Applications". Reason: The following vsys were not found in Palo Alto NGFW: {vsys that were not found}**If Policy name wasn't found in all vsys (fail):** Error executing action "Get Blocked Applications". Reason: Policy "{policy name}" wasn't found in the provided vsys. Please check the spelling.**If device name is invalid (fail):** Error executing action "Get Blocked Applications". Reason: Device "{device name}" was not found. Please check the spelling.**Critical Error:** Error executing action "Get Blocked Applications". Reason: {error traceback} | General  
  
### Ping

Test connectivity to Panorama.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Remove IPs From Group

Remove IP addresses from an address group.

**Note:** This change remains in the candidate configuration until you run the **Commit Changes** action.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device Name | String | N/A | The device name in which the group is located. The default device name of NGFW is localhost.localdomain. In case configured differently, please refer to https://php/rest/browse.php/config::devices for the list of all the device names and select the relevant device.  
Vsys Name | String | N/A | "Specify a comma-separated list of vsys on which you want to execute the action. The default vsys name of NGFW is vsys1. In case configured differently, please refer to https://{ip}/php/rest/browse.php/config::devices::entry[@name='{device name{']::vsys for the list of all available vsys on the device."  
Address Group Name | String | N/A | The name of the required address group.  
Use Shared Objects | Checkbox | N/A | If enabled, action will use shared objects instead of vsys. Note: action will not create a shared address group, if it doesn't exist.  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        "1.1.1.1",
        "2.2.2.2"
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success for one vsys and one IP (is_success=true):** Successfully removed the following IPs from the group "{group_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for one vsys and one IP (is_success=true):** Action wasn't able to remove the following IPs from the group "{group_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for all IPs in vsys (is_success=false, if the same behavior for all vsys and is_success=true if partial):** No IPs were removed from the group "{group_name}" for vsys "{vsys name}" in Palo Alto NGFW.**If Group name wasn't found in some vsys (is_success=true):** Group "{group name}" wasn't found in the following vsys in the Palo Alto NGFW: {vsys that don't have the group}**If at least one of the vsys were not found (fail):** Error executing action "Remove Ips from group". Reason: The following vsys were not found in Palo Alto NGFW: {vsys that were not found}**If "Use Shared Objects" is disabled and none of the "Device name" and "Vsys name" are provided (fail):** Error executing action "{action_name}": Either "Use Shared Objects" parameter should be enabled or "Device name" and "Vsys name" to be provided.**If Group name wasn't found in all vsys (fail):** Error executing action "Remove Ips from group". Reason: Group "{group name}" wasn't found in the provided vsys. Please check the spelling.**If device name is invalid (fail):** Error executing action "Remove Ips from group". Reason: Device "{device name}" was not found. Please check the spelling.**If "Use Shared Objects" is enabled and at least one IP address was removed (is_success=true):** Successfully removed the following IP addresses from the shared address group '{Group Name}' in Palo Alto NGFW:\n {entity.identifier}**If "Use Shared Objects" is enabled and one IP addresses was already not a part of address group (is_success=true) :** The following IP addresses were not a part of the the shared address group '{Group Name}' in Palo Alto NGFW:\n {entity.identifier}**If Address Group wasn't found (fail):** Error executing action "Remove Ips to group". Shared address group "{Group Name}" was not found in Palo Alto NGFW.**Critical Error:** Error executing action "Remove Ips from group". Reason: {error traceback} | General  
  
### Unblock IPs in Policy

Unblock IP addresses in a policy (each IP address is removed individually from the policy).

**Note:** This change remains in the candidate configuration until you run the **Commit Changes** action.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device Name | String | N/A | The device name in which the group is located. The default device name of NGFW is localhost.localdomain. In case configured differently, please refer to https://php/rest/browse.php/config::devices for the list of all the device names and select the relevant device.  
Vsys Name | String | N/A | "Specify a comma-separated list of vsys on which you want to execute the action. The default vsys name of NGFW is vsys1. In case configured differently, please refer to https://{ip}/php/rest/browse.php/config::devices::entry[@name='{device name{']::vsys for the list of all available vsys on the device."  
Policy Name | String | N/A | Policy name value.  
Target | String | N/A | Has to be source or destination.  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        "1.1.1.1",
        "2.2.2.2"
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success for one vsys and one IP (is_success=true):** Successfully unblocked the following IPs in policy "{policy name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for one vsys and one IP (is_success=true):** Action wasn't able to unblock the following IPs in policy "{policy_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for all IPs in vsys:** No IPs were unblocked in policy "{policy_name}" for vsys "{vsys name}" in Palo Alto NGFW.**If Policy name wasn't found in some vsys (is_success=true):** Policy "{policy name}" wasn't found in the following vsys in the Palo Alto NGFW: {vsys that don't have the policy}**If at least one of the vsys were not found (fail):** Error executing action "Unblock Ips in policy". Reason: The following vsys were not found in Palo Alto NGFW: {vsys that were not found}**If Policy name wasn't found in all vsys (fail):** Error executing action "Unblock Ips in policy". Reason: Policy "{policy name}" wasn't found in the provided vsys. Please check the spelling.**If device name is invalid (fail):** Error executing action "Unblock Ips in policy". Reason: Device "{device name}" was not found. Please check the spelling.**if Target != source or destination.:** Error executing action "Unblock Ips in policy". Reason: Target should be either "source" or "destination".**Critical Error:** Error executing action "Unblock Ips in policy". Reason: {error traceback} | General  
  
### Unblock URLs

Remove URLs from a given URL category.

**Note:** This change remains in the candidate configuration until you run the **Commit Changes** action.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
Device Name | String | N/A | The device name in which the group is located. The default device name of NGFW is localhost.localdomain. In case configured differently, please refer to https://php/rest/browse.php/config::devices for the list of all the device names and select the relevant device.  
Vsys Name | String | N/A | "Specify a comma-separated list of vsys on which you want to execute the action. The default vsys name of NGFW is vsys1. In case configured differently, please refer to https://{ip}/php/rest/browse.php/config::devices::entry[@name='{device name{']::vsys for the list of all available vsys on the device."  
URL Category Name | String | N/A | N/A  
Use Shared Objects | Checkbox | N/A | If enabled, action will use shared objects instead of vsys.  
  
#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [
        "www.example.com"
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success for one vsys and one URL(is_success=true):** Successfully removed the following URLs from the category "{category_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for one vsys and one URL (is_success=true):** Action wasn't able to remove the following URLs to the category "{category_name}" for vsys "{vsys name}" in Palo Alto NGFW: {entity.identifiers}**Not success for all URLs in vsys:** No URLs were removed from the category "{category_name}" for vsys "{vsys name}" in Palo Alto NGFW.**If Group name wasn't found in some vsys (is_success=true):** Category "{category name}" wasn't found in the following vsys in the Palo Alto NGFW: {vsys that don't have the category}**If at least one of the vsys were not found (fail):** Error executing action "Unblock Urls". Reason: The following vsys were not found in Palo Alto NGFW: {vsys that were not found}**If "Use Shared Objects" is disabled and none of the "Device name" and "Vsys name" are provided (fail):** Error executing action "{action_name}": Either "Use Shared Objects" parameter should be enabled or "Device name" and "Vsys name" to be provided.**If Category name wasn't found in all vsys (fail):** Error executing action "Unblock Urls". Reason: Category "{category name}" wasn't found in the provided vsys. Please check the spelling.**If device name is invalid (fail):** Error executing action "Unblock Urls". Reason: Device "{device name}" was not found. Please check the spelling.**If "Use Shared Objects" is enabled and at least one URL was added (is_success=true):** Successfully removed the following URLs from the shared category '{Category Name}' in Palo Alto NGFW:\n {entity.identifier}**If "Use Shared Objects" is enabled and one URL was already a part of URL Category (is_success=true) :** __The following URLs were not a part of the the shared category '{Category Name}' in Palo Alto NGFW:\n {entity.identifier}**If Category wasn't found (fail):** Error executing action "Block Urls". Shared category "{Category Name}" was not found in Palo Alto NGFW.**Critical Error:** Error executing action "Unblock Urls". Reason: {error traceback} | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
