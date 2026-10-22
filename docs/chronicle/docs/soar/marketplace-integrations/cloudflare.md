---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cloudflare/
title: Cloudflare \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:14.992607+00:00
---

# Cloudflare  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cloudflare/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloudflare

This document describes how to integrate Cloudflare with Google Security Operations.

## Product Use Cases

Perform enrichment of entities

## Configure Cloudflare integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | `https://api.cloudflare.com` | Yes | API root of the Cloudflare instance.  
API Token | Password | N/A | Yes | API Token of the Cloudflare instance.  
Account Name | String | N/A | Yes | Name of the account that needs to be used in the integration.  
Verify SSL | Checkbox | Checked | No | If enabled, verifies that the SSL certificate for the connection to the Cloudflare server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## How to configure token

  1. Go to **Profile Settings** and click **API Tokens**.
  2. Navigate to **Create Token > Create Custom Token** and select the following permissions:

Account | Account WAF | Read  
---|---|---  
Account | Rule Policies | Read  
Account | Account Filter Lists | Edit  
Account | Account Firewall Access | Edit  
Account | DNS Firewall | Read  
Account | Account Settings | Read  
Zone | Zone WAF | Edit  
Zone | Zone Settings | Read  
Zone | Zone | Read  
Zone | Logs | Read  
Zone | Firewall Services | Edit  
Zone | Firewall Services | Read  
Zone | Analytics | Read  
  
![List of required
permissions](https://docs.cloud.google.com/static/chronicle/images/integrations/cloudflare-configure-token.png)

## Actions

### Add IP To Rule List

#### Description

Add IP addresses to the rule list in Cloudflare. Supported Entities: IP Address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Rule Name | String | N/A | Yes | Specify the name of the rule list to which you want to add rule list items.  
Description | String | N/A | No | Specify a description for the newly added rule list items.  
  
#### Run on

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "result": {
            "operation_id": "f16b978552ca49f88b36fe628de31142"
        },
        "success": true,
        "errors": [],
        "messages": []
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If the 200 status code is reported for one entity (is_success=true):_ "Successfully added the following entities to the {name} rule list in Cloudflare: {entity.identifier}."_If not successful for one entity (is_success=true):_ "Action wasn't able to add the following entities to the {name} rule list in Cloudflare: {entity.identifier}."_If not successful for all (is_success=false):_ "None of the provided entities were added to the {name} rule list."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Add IP To Rule List". Reason: {0}''.format(error.Stacktrace)_If the list is not found:_ "Error executing action "Add IP To Rule List". Reason: rule list {name} wasn't found in Cloudflare.'' _If the list is not of the valid kind:_ "Error executing action "Add IP To Rule List". Reason: rule list {name} is not of type "IP"." | General  
  
### Add URL To Rule List

#### Description

Add URLs to the rule list in Cloudflare. Supported Entities: URL.

**Note:** The URL entities are treated as "Target URLs".

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Rule Name | String | N/A | Yes | Specify the name of the rule list to which you want to add rule list items.  
Source URL | String | N/A | Yes | Specify the source URL for the rule list item.  
Description | String | N/A | No | Specify a description for the newly added rule list items.  
Status Code | DDL | 301Possible Values:

  * 301
  * 302
  * 307
  * 308

| No | Specify the status for the rule list item.  
Preserve Query String | Checkbox | Unchecked | No | If enabled, the rule list item preserves the query string.  
Include Subdomains | Checkbox | Unchecked | No | If enabled, the rule list item includes subdomains.  
Subpath Matching | Checkbox | Unchecked | No | If enabled, the rule list item matches the subpath.  
Preserve Path Suffix | Checkbox | Unchecked | No | If enabled, the rule list item preserves the path suffix.  
  
#### Run on

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "result": {
            "operation_id": "f16b978552ca49f88b36fe628de31142"
        },
        "success": true,
        "errors": [],
        "messages": []
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code for one entity (is_success=true):_ "Successfully added the following entities to the {name} rule list in Cloudflare: {entity.identifier}."_If not successful for one entity (is_success=true):_ "Action wasn't able to add the following entities to the {name} rule list in Cloudflare: {entity.identifier}."_If not success for all entities (is_success=false):_ "None of the provided entities were added to the {name} rule list."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Add URL To Rule List". Reason: {0}''.format(error.Stacktrace)_If the list is not found:_ "Error executing action "Add URL To Rule List". Reason: rule list {name} wasn't found in Cloudflare.'' _If the list is not of the valid kind:_ "Error executing action "Add URL To Rule List". Reason: rule list {name} is not of type "Redirect".' | General  
  
### Create Firewall Rule

#### Description

Create a firewall rule in Cloudflare.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Zone Name | String | N/A | Yes | Specify the name of the zone, which contains the firewall rule.  
Name | String | N/A | No | Specify the name for the firewall rule.  
Action | DDL | BlockPossible Values:

  * Allow
  * Block
  * Bypass
  * Log
  * Legacy CAPTCHA
  * Managed Challenge
  * JS Challenge

| No | Specify the action for the firewall rule.If "Block" is selected, you need to provide values in the "Products" parameter.  
Expression | String | N/A | Yes | Specify the expression for the firewall rule.  
Products | CSV | N/A | No | Specify a comma-separated list of products for the firewall rule.**Note:** This parameter is only mandatory, if "Bypass" is selected for the "Action" parameter.Possible values: zoneLockdown, uaBlock, bic, hot, securityLevel, rateLimit, waf  
Priority | Integer | N/A | No | Specify the priority for the firewall rule.  
Reference Tag | String | N/A | No | Specify a reference tag for the firewall rule.**Note:** It can only be up to 50 characters long.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
            {
                "id": "b520c154bdeb4fe2a1f647b2c6b35829",
                "paused": false,
                "description": "Blocks traffic identified during investigation for MIR-31",
                "action": "block",
                "priority": 50,
                "filter": {
                    "id": "fc6dfad848c24a42ae5be0114db09fb9",
                    "expression": "(ip.geoip.continent eq \"ASIA\")",
                    "paused": false
                },
                "created_on": "2022-07-25T11:19:22Z",
                "modified_on": "2022-07-25T11:19:22Z",
                "index": 0
            }
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code is reported (is_success=true):_ "Successfully created a new firewall rule in "{zone_name}" zone in Cloudflare.".**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Create Firewall Rule". Reason: {0}''.format(error.Stacktrace)_If the errors list is not empty:_ "Error executing action "Create Firewall Rule". Reason: {0}''.format(errors/message)_If the zone is not found:_ "Error executing action "Create Firewall Rule". Reason: zone {zone_name} wasn't found in Cloudflare.'' | General  
  
### Create Rule List

#### Description

Create a rule list in Cloudflare.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name for the rule list.  
Type | DDL | IP AddressPossible Values:

  * IP Address
  * Redirect

| No | Specify the type for the rule list.  
Description | String | N/A | No | Specify the description for the rule list.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "id": "d19589d629f140c0b961c467feadf99d",
        "name": "123",
        "kind": "ip",
        "num_items": 0,
    "description": "description",
        "num_referencing_filters": 0,
        "created_on": "2022-07-25T12:13:46Z",
        "modified_on": "2022-07-25T12:13:46Z"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code is reported (is_success = true):_ "Successfully create a rule list in Cloudflare."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Create Rule List". Reason: {0}''.format(error.Stacktrace)_If the errors list is not empty:_ "Error executing action "Create Rule List". Reason: {0}''.format(errors/message) | General  
  
### List Firewall Rules

#### Description

List available firewall rules in Cloudflare.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Zone Name | String | N/A | Yes | Specify the name of the zone, which will contain the firewall rule.  
Filter Key | DDL | Select OnePossible Values:

  * Select One
  * Name
  * ID
  * Action

| No | Specify the key that needs to be used to filter {item type}.  
Filter Logic | DDL | Select OnePossible Values:

  * Select one
  * Equal
  * Contains

| No | Specify the filter logic that should be applied. The filtering logic is based on the value provided in the "Filter Key" parameter.  
Filter Value | String | N/A | No | Specify the value that should be used in the filter.If "Equal" is selected, the action tries to find the exact match among results.If "Contains" is selected, the action tries to find results that contain that substring.If nothing is provided in this parameter, the filter is not applied. The filtering logic is based on the value provided in the "Filter Key" parameter.  
Max Records To Return | Integer | 50 | No | Specify the number of records to return.If nothing is provided, the action returns 50 records.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "id": "55ec8db30f9e4640b5d0d13cff6b5429",
        "paused": false,
        "description": "rulle2",
        "action": "allow",
        "filter": {
            "id": "2bb05df8c4f547bd9792d8dc38a86b81",
            "expression": "(ip.geoip.country eq \"BG\")",
            "paused": false
        },
        "created_on": "2022-07-05T13:53:39Z",
        "modified_on": "2022-07-05T13:53:39Z"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available (is_success=true):_ "Successfully found {item name} for the provided criteria in {product name}"._If data is not available (is_success=false):_ "No {item name} were found for the provided criteria in {product name}"_If the "Filter Value" parameter is empty (is_success=true):_ "The filter was not applied, because parameter "Filter Value" has an empty value."**The action should fail and stop a playbook execution:**___If the "Filter Key" parameter is set to "Select One" and the "Filter Logic" parameter is set to "Equal" or "Contains":_ "Error executing action "{action name}". Reason: you need to select a field from the "Filter Key" parameter."_If an invalid value is provided for the "Max Records to Return" parameter:_ "Error executing action "{action name}". Reason: "Invalid value was provided for "Max Records to Return": . Positive number should be provided."_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "{action name}". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Available {item group}**Table Columns:** {fields} | General  
  
### Ping

#### Description

Test connectivity to Cloudflare with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run on

The action doesn't use any of the Google SecOps scope entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the SpyCloud server with the provided connection parameters!"**The action should fail and stop a playbook execution:**___If not successful:_ "Failed to connect to the SpyCloud server! Error is {0}".format(exception.stacktrace)If the account is not found: "Failed to connect to the Cloudflare server! Invalid account name was provided. Please check the spelling." | General  
  
### Update Firewall Rule

#### Description

Update a firewall rule in Cloudflare.

#### Run on

This action doesn't run on entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Rule Name | String | N/A | Yes | Specify the name of the rule that needs to be updated.  
Zone Name | String | N/A | Yes | Specify the name of the zone, which contains the firewall rule.  
Action | DDL | BlockPossible Values:

  * Allow
  * Block
  * Bypass
  * Log
  * Legacy CAPTCHA
  * Managed Challenge
  * JS Challenge

| No | Specify the action for the firewall rule.If "Block" is selected, you need to provide values in the "Products" parameter.  
Expression | String | N/A | Yes | Specify the expression for the firewall rule.  
Products | CSV | N/A | No | Specify a comma-separated list of products for the firewall rule.**Note:** This parameter is only mandatory, if "Bypass" is selected for the "Action" parameter.Possible values: zoneLockdown, uaBlock, bic, hot, securityLevel, rateLimit, waf  
Priority | Integer | N/A | No | Specify the priority for the firewall rule.  
Reference Tag | String | N/A | No | Specify a reference tag for the firewall rule.**Note:** It can only be up to 50 characters long.  
  
#### Run on

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
            {
                "id": "b520c154bdeb4fe2a1f647b2c6b35829",
                "paused": false,
                "description": "Blocks traffic identified during investigation for MIR-31",
                "action": "block",
                "priority": 50,
                "filter": {
                    "id": "fc6dfad848c24a42ae5be0114db09fb9",
                    "expression": "(ip.geoip.continent eq \"ASIA\")",
                    "paused": false
                },
                "created_on": "2022-07-25T11:19:22Z",
                "modified_on": "2022-07-25T11:19:22Z",
                "index": 0
            }
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******If the 200 status code is reported (is_success=true): "Successfully updated a firewall rule in "{zone_name}" zone in Cloudflare."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Firewall Rule". Reason: {0}''.format(error.Stacktrace)_If the errors list is not empty:_ "Error executing action "Update Firewall Rule". Reason: {0}''.format(errors/message)_If the zone is not found:_ "Error executing action "Update Firewall Rule". Reason: zone {zone_name} wasn't found in Cloudflare.'' | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
