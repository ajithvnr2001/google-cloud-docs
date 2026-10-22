---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/f5-big-ip-icontrol-api/
title: F5 BIG-IP iControl API \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:40.326393+00:00
---

# F5 BIG-IP iControl API  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/f5-big-ip-icontrol-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# F5 BIG-IP iControl API

This document describes how to integrate F5 BIG-IP iControl API with Google Security Operations.

## Use Cases

Perform enrichment of entities.

## Configure F5 BIG-IP iControl API integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https:/{{ip address}} | Yes | API root of the F5 BIG-IP instance.  
Username | String | N/A |  | Username of the F5 BIG-IP account.  
Password | Password | N/A | Yes | Password of the F5 BIG-IP account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the F5 BIG-IP server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the F5 BIG-IP with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If successful:_ ****"Successfully connected to the F5 BIG-IP server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:******  
****_If not successful:_ ****"Failed to connect to the F5 BIG-IP server! Error is {0}".format(exception.stacktrace) | General  
  
### List Data Groups

#### Description

List available data groups in F5 BIG-IP. Note: action only supports internal data groups.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDL:

  * Equal
  * Contains

| No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Data Groups To Return | Integer | 50 | No | Specify how many data groups to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     0: {
       "sessionID" : "fee20d24",
              "nestedStats": {
                    "entries": {
                        "clientIp": {
                            "description": "10.0.150.45"
                        },
                        "logonUser": {
                            "description": "n/a"
                        }
                    }
                }
            }
        }
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If data is available (is_success=true):_ ****"Successfully found data groups for the provided criteria in F5 BIG-IP".  
****_If data is not available (is_success=false):_ ****"No data groups were found for the provided criteria in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "List Data Groups". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
****| **Table Name:** Available Data Groups**Table Columns:**

  * Name
  * Type
  * Number of records 

| General  
  
### Add IP To Data Group

#### Description

Add IP to the data group in F5 BIG-IP. Supported entities: IP address.

**Note:** This action only supports internal data groups.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Data Group Name | String | N/A | Yes | Specify the name of the data group to which you want to add IP addresses.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:ltm:data-group:internal:internalstate",
        "name": "aol",
        "partition": "Common",
        "fullPath": "/Common/aol",
        "generation": 1,
        "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~aol?ver=16.0.1.1",
        "type": "ip",
        "records": [
            {
                "name": "64.12.96.0/19",
                "data": ""
            },
            {
                "name": "195.93.16.0/20",
                "data": ""
            },
            {
                "name": "195.93.48.0/22",
                "data": ""
            },
            {
                "name": "195.93.64.0/19",
                "data": ""
            },
            {
                "name": "195.93.96.0/19",
                "data": ""
            },
            {
                "name": "198.81.0.0/22",
                "data": ""
            },
            {
                "name": "198.81.8.0/23",
                "data": ""
            },
            {
                "name": "198.81.16.0/20",
                "data": ""
            },
            {
                "name": "202.67.65.128/25",
                "data": ""
            },
            {
                "name": "205.188.112.0/20",
                "data": ""
            },
            {
                "name": "205.188.146.144/30",
                "data": ""
            },
            {
                "name": "205.188.192.0/20",
                "data": ""
            },
            {
                "name": "205.188.208.0/23",
                "data": ""
            },
            {
                "name": "207.200.112.0/21",
                "data": ""
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If added at least one IP (is_success=true):_ "Successfully added the following IPs to the {name} data group in F5 BIG-IP: {entity.id}".  
****_If not added at least one (is_success=true):_ ****"Action wasn't able to add the following IPs to the {name} data group in F5 BIG-IP: {entity.id}".  
****_If not added any IPs (is_success=false):_ "No IPs were added to the {name} data group in F5 BIG-IP".  
******The action should fail and stop a playbook execution:**  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Add IP To Data Group". Reason: {0}''.format(error.Stacktrace)****_If the data group is not found or doesn't have the correct type:_ ****"Error executing action "Add IP To Data Group". Reason: data group {name} was not found or doesn't have the IP type in F5 BIG-IP. Please check the spelling. '.format(error.Stacktrace) | General  
  
### Remove IP From Data Group

#### Description

Remove IP from the data group in F5 BIG-IP. Supported entities: IP address.

**Note:** This action only supports internal data groups.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Data Group Name | String | N/A | Yes | Specify the name of the data group from which you want to remove IP addresses.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:ltm:data-group:internal:internalstate",
        "name": "aol",
        "partition": "Common",
        "fullPath": "/Common/aol",
        "generation": 1,
        "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~aol?ver=16.0.1.1",
        "type": "ip",
        "records": [
            {
                "name": "64.12.96.0/19",
                "data": ""
            },
            {
                "name": "195.93.16.0/20",
                "data": ""
            },
            {
                "name": "195.93.48.0/22",
                "data": ""
            },
            {
                "name": "195.93.64.0/19",
                "data": ""
            },
            {
                "name": "195.93.96.0/19",
                "data": ""
            },
            {
                "name": "198.81.0.0/22",
                "data": ""
            },
            {
                "name": "198.81.8.0/23",
                "data": ""
            },
            {
                "name": "198.81.16.0/20",
                "data": ""
            },
            {
                "name": "202.67.65.128/25",
                "data": ""
            },
            {
                "name": "205.188.112.0/20",
                "data": ""
            },
            {
                "name": "205.188.146.144/30",
                "data": ""
            },
            {
                "name": "205.188.192.0/20",
                "data": ""
            },
            {
                "name": "205.188.208.0/23",
                "data": ""
            },
            {
                "name": "207.200.112.0/21",
                "data": ""
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If removed at least one IP (is_success=true):_ ****"Successfully removed the following IPs from the {name} data group in F5 BIG-IP: {entity.id}".  
****_If IP doesn't exist initially:_ "The following IPs didn't exist in {name} data group in F5 BIG-IP: {entity.id}"  
******The action should fail and stop a playbook execution:******  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Remove IP From Data Group". Reason: {0}''.format(error.Stacktrace)****_If the data group is not found or doesn't have the correct type:_ ****"Error executing action "Remove IP To Data Group". Reason: data group {name} was not found or doesn't have the IP type in F5 BIG-IP. Please check the spelling. '.format(error.Stacktrace)****_If the action tries to remove all items (fail):_ ****Error executing action "Remove IP From Date Group". Reason: you can't remove all of the IPs from the data group. | General  
  
### Create Data Group

#### Description

Create a data group in F5 BIG-IP.

**Note:** This action only supports internal data groups.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the data group that needs to be created.  
Type | DDL | DDL:

  * IP Address
  * String
  * Integer

| Yes | Specify the type for the data group.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:ltm:data-group:internal:internalstate",
        "name": "aol",
        "partition": "Common",
        "fullPath": "/Common/aol",
        "generation": 1,
        "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~aol?ver=16.0.1.1",
        "type": "ip",
        "records": [
    
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If successful (is_success=true):_ ****"Successfully created data group {name} in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Create Data Group". Reason: {0}''.format(error.Stacktrace)****_If status code is not 200:_ "Error executing action "Create Data Group". Reason: {0}''.format(message) | General  
  
### Delete Data Group

#### Description

Delete a data group in F5 BIG-IP.

**Note:** This action only supports internal data groups.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the data group that needs to be deleted.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **The action should not fail nor stop a playbook execution:**  
****_If the 200 status code is reported (is_success=true):_ "Successfully deleted data group {name} in F5 BIG-IP".  
****_If the 404 status code is reported (is_success=true):_ ****"Data group {name} doesn't exist in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Delete Data Group". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Address Lists

#### Description

List available address lists in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDL:

  * Equal
  * Contains

| No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Address Lists To Return | Integer | 50 | No | Specify how many address lists to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:security:firewall:address-list:address-liststate",
        "name": "internal_ips",
        "partition": "Common",
        "fullPath": "/Common/internal_ips",
        "generation": 713,
        "selfLink": "https://localhost/mgmt/tm/security/firewall/address-list/~Common~internal_ips?ver=16.0.1.1",
        "addresses": [
            {
                "name": "192.168.26.2"
            },
            {
                "name": "192.168.26.3"
            },
            {
                "name": "192.168.26.4"
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If data is available (is_success=true):_ "Successfully found address lists for the provided criteria in F5 BIG-IP".  
****_If data is not available (is_success=false):_ "No address lists were found for the provided criteria in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "List Address Lists". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
| **Table Name:** Available Address Lists**Table Columns:**

  * Name
  * Number of Addresses

| General  
  
### Add IP To Address List

#### Description

Add IP to the address list in F5 BIG-IP. Supported entities: IP address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Address List Name | String | N/A | Yes | Specify the name of the address list to which you want to add IP addresses.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:security:firewall:address-list:address-liststate",
        "name": "internal_ips",
        "partition": "Common",
        "fullPath": "/Common/internal_ips",
        "generation": 713,
        "selfLink": "https://localhost/mgmt/tm/security/firewall/address-list/~Common~internal_ips?ver=16.0.1.1",
        "addresses": [
            {
                "name": "192.168.26.2"
            },
            {
                "name": "192.168.26.3"
            },
            {
                "name": "192.168.26.4"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **The action should not fail nor stop a playbook execution:******  
****_If added at least one IP (is_success=true):_ ****"Successfully added the following IPs to the {name} address list in F5 BIG-IP: {entity.id}".  
****_If not added at least one IP (is_success=true):_ ****"Action wasn't able to add the following IPs to the {name} address list in F5 BIG-IP: {entity.id}".  
****_If not added any IPs (is_success=false):_ ****"No IPs were added to the {name} address list in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Add IP To Address List". Reason: {0}''.format(error.Stacktrace)****_If the data group is not found or doesn't have the correct type:_ ****"Error executing action "Add IP To Address List". Reason: address list {name} was not found in F5 BIG-IP. Please check the spelling. '.format(error.Stacktrace) | General  
  
### Remove IP From Address List

#### Description

Remove IP from the address list in F5 BIG-IP. Supported entities: IP address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Address List Name | String | N/A | Yes | Specify the name of the address list from which you want to remove IP addresses.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:security:firewall:address-list:address-liststate",
        "name": "internal_ips",
        "partition": "Common",
        "fullPath": "/Common/internal_ips",
        "generation": 713,
        "selfLink": "https://localhost/mgmt/tm/security/firewall/address-list/~Common~internal_ips?ver=16.0.1.1",
        "addresses": [
            {
                "name": "192.168.26.2"
            },
            {
                "name": "192.168.26.3"
            },
            {
                "name": "192.168.26.4"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If added at least one IP (is_success=true):_ "Successfully removed the following IPs from the {name} address list in F5 BIG-IP: {entity.id}".  
****_If IP doesn't exist initially:_ "The following IPs didn't exist in {name} address list in F5 BIG-IP: {entity.id}".  
******The action should fail and stop a playbook execution:**  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Add IP To Address List". Reason: {0}''.format(error.Stacktrace)****_If the data group is not found or doesn't have the correct type:_ "Error executing action "Remove IP From Address List". Reason: address list {name} was not found in F5 BIG-IP. Please check the spelling. '.format(error.Stacktrace)  
****_If the action tries to remove all items (fail):_ ****Error executing action "Remove IP From Address List". Reason: you can't remove all of the IPs from the address list. | General  
  
### Create Address List

#### Description

Create an address list in F5 BIG-IP. Supported entities: IP address.

**Note:** The address list requires at least one IP address to be available during creation.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the address list that needs to be created.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:security:firewall:address-list:address-liststate",
        "name": "koko",
        "partition": "Common",
        "fullPath": "/Common/koko",
        "generation": 803,
        "selfLink": "https://localhost/mgmt/tm/security/firewall/address-list/~Common~koko?ver=16.0.1.1",
        "addresses": [
            {
                "name": "192.168.26.2"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful (is_success=true):_ "Successfully created address list {name} in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Create Address List". Reason: {0}''.format(error.Stacktrace)****_If status code is not 200:_ ****"Error executing action "Create Address List". Reason: {0}''.format(message) | General  
  
### Delete Address List

#### Description

Delete an address list in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the address list that needs to be deleted.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If successful (is_success=true):_ "Successfully created address list {name} in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Create Address List". Reason: {0}''.format(error.Stacktrace)****_If status code is not 200:_ ****"Error executing action "Create Address List". Reason: {0}''.format(message) | General  
  
### List Port Lists

#### Description

List available port lists in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDL:

  * Equal
  * Contains

| No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max Port Lists To Return | Integer | 50 | No | Specify how many port lists to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:security:firewall:address-list:address-liststate",
        "name": "internal_ips",
        "partition": "Common",
        "fullPath": "/Common/internal_ips",
        "generation": 713,
        "selfLink": "https://localhost/mgmt/tm/security/firewall/address-list/~Common~internal_ips?ver=16.0.1.1",
        "addresses": [
            {
                "name": "192.168.26.2"
            },
            {
                "name": "192.168.26.3"
            },
            {
                "name": "192.168.26.4"
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If data is available (is_success=true):_ "Successfully found port lists for the provided criteria in F5 BIG-IP".  
****_If data is not available (is_success=false):_ "No port lists were found for the provided criteria in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "List Port Lists". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
****| **Table Name:** Available Port Lists**Table Columns:**

  * Name
  * Number of Ports 

| General  
  
### Add Port To Port List

#### Description

Add port to the port list in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Port List Name | String | N/A | Yes | Specify the name of the port list to which you want to add ports.  
Ports | CSV | N/A | Yes | Specify a comma-separated list of ports that need to be added.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:security:firewall:port-list:port-liststate",
        "name": "_sys_self_allow_tcp_defaults",
        "fullPath": "_sys_self_allow_tcp_defaults",
        "generation": 809,
        "selfLink": "https://localhost/mgmt/tm/security/firewall/port-list/_sys_self_allow_tcp_defaults?ver=16.0.1.1",
        "ports": [
            {
                "name": "1"
            },
            {
                "name": "22"
            },
            {
                "name": "53"
            },
            {
                "name": "161"
            },
            {
                "name": "443"
            },
            {
                "name": "1029-1043"
            },
            {
                "name": "4353"
            }
        ]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If added at least one port (is_success=true):_ ****"Successfully added the following ports to the {name} port list in F5 BIG-IP: {port}".  
****_If not added at least one port, meaning that port is invalid (is_success=true):_ ****"Action wasn't able to add the following ports to the {name} port list in F5 BIG-IP: {port}".  
****_If not added any ports (is_success=false):_ ****"No ports were added to the {name} port list in F5 BIG-IP".  
******The action should fail and stop a playbook execution:**  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Add Port To Port List". Reason: {0}''.format(error.Stacktrace)****_If the data group is not found or doesn't have the correct type:_ ****"Error executing action "Add Port To Port List". Reason: port list {name} was not found in F5 BIG-IP. Please check the spelling. '.format(error.Stacktrace) | General  
  
### Remove Port From Port List

#### Description

Remove port from the port list in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Port List Name | String | N/A | Yes | Specify the name of the port list from which you want to remove ports.  
Ports | CSV | N/A | Yes | Specify a comma-separated list of ports that need to be removed.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:security:firewall:address-list:address-liststate",
        "name": "internal_ips",
        "partition": "Common",
        "fullPath": "/Common/internal_ips",
        "generation": 713,
        "selfLink": "https://localhost/mgmt/tm/security/firewall/address-list/~Common~internal_ips?ver=16.0.1.1",
        "addresses": [
            {
                "name": "192.168.26.2"
            },
            {
                "name": "192.168.26.3"
            },
            {
                "name": "192.168.26.4"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If removed at least one port (is_success=true):_ "Successfully removed the following ports from the {name} port list in F5 BIG-IP: {port}"  
****_If the port doesn't exist initially:_ "The following ports didn't exist in {name} port list in F5 BIG-IP: {port}".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Remove Port From Port List". Reason: {0}''.format(error.Stacktrace)****_If the data group is not found or doesn't have the correct type:_ ****"Error executing action "Remove Port From Port List". Reason: port list {name} was not found in F5 BIG-IP. Please check the spelling. '.format(error.Stacktrace)  
****_If the action tries to remove all items (fail):_ ****Error executing action "Remove Port From Port List". Reason: you can't remove all of the ports from the port list. | General  
  
### Create Port List

#### Description

Create a port list in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the port list that needs to be created. Note: name shouldn't contain whitespace. This is the F5 BIG-IP limitation.  
Ports | CSV | N/A | Yes | Specify a comma-separated list of ports that will be a part of the new port list.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "kind": "tm:security:firewall:port-list:port-liststate",
        "name": "koko",
        "partition": "Common",
        "fullPath": "/Common/koko",
        "generation": 811,
        "selfLink": "https://localhost/mgmt/tm/security/firewall/port-list/~Common~koko?ver=16.0.1.1",
        "ports": [
            {
                "name": "123"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful (is_success=true):_ "Successfully created port list {name} in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Create Port List". Reason: {0}''.format(error.Stacktrace)****_If status code is not 200:_ ****"Error executing action "Create Port List". Reason: {0}''.format(message) | General  
  
### Delete Port List

#### Description

Delete a port list in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the port list that needs to be deleted.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******  
****_If successful (is_success=true):_ ****"Successfully created address list {name} in F5 BIG-IP".  
******The action should fail and stop a playbook execution:**  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Create Address List". Reason: {0}''.format(error.Stacktrace)****_If status code is not 200:_ "Error executing action "Create Address List". Reason: {0}''.format(message) | General  
  
### List iRules

#### Description

List available iRules in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualDDL:

  * Equal
  * Contains

| No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  
Max iRules To Return | Integer | 50 | No | Specify how many iRules to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_https_redirect",
                "partition": "Common",
                "fullPath": "/Common/_sys_https_redirect",
                "generation": 1,
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_https_redirect?ver=16.0.1.1",
                "apiAnonymous": "nodelete nowrite \n# copy 2003-2006, 2012-2013, 2016, 2019.  F5 Networks, Inc.  See End User License Agreement (\"EULA\")\n# for",
                "apiRawValues": {
                    "verificationStatus": "signature-verified"
                }
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If data is available (is_success=true):_ ****"Successfully found port lists for the provided criteria in F5 BIG-IP".  
****_If data is not available (is_success=false):_ "No port lists were found for the provided criteria in F5 BIG-IP".  
******The action should fail and stop a playbook execution:**  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "List iRules". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
| **Table Name:** Available iRules**Table Columns:**

  * Name
  * Rule 

| General  
  
### Create iRule

#### Description

Create an iRule in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the iRule that needs to be created.  
Rule | String | N/A | Yes | Specify the rule that needs to be executed.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     {
        "kind": "tm:ltm:rule:rulestate",
        "name": "koko",
        "partition": "Common",
        "fullPath": "/Common/koko",
        "generation": 813,
        "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~koko?ver=16.0.1.1",
        "apiAnonymous": "when CLIENT_ACCEPTED {\n        set tmm_auth_ssl_ocsp_sid 0\n        set tmm_auth_ssl_ocsp_done 0\n    }\n    when CLIENTSSL_CLIENTCERT {\n        if {[SSL::cert count] == 1} {\n            return\n        }\n        set tmm_auth_ssl_ocsp_done 0\n        if {$tmm_auth_ssl_ocsp_sid == 0} {\n            set tmm_auth_ssl_ocsp_sid [AUTH::start pam default_ssl_ocsp]\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_ssl_ocsp_sid\n            }\n        }\n        AUTH::cert_credential $tmm_auth_ssl_ocsp_sid [SSL::cert 0]\n        AUTH::cert_issuer_credential $tmm_auth_ssl_ocsp_sid [SSL::cert issuer 0]\n        AUTH::authenticate $tmm_auth_ssl_ocsp_sid\n        SSL::handshake hold\n    }\n    when CLIENTSSL_HANDSHAKE {\n        set tmm_auth_ssl_ocsp_done 1\n    }\n    when AUTH_RESULT {\n        if {[info exists tmm_auth_ssl_ocsp_sid] and \\\n            ($tmm_auth_ssl_ocsp_sid == [AUTH::last_event_session_id])} {\n            set tmm_auth_status [AUTH::status]\n            if {$tmm_auth_status == 0} {\n                set tmm_auth_ssl_ocsp_done 1\n                SSL::handshake resume\n            } elseif {$tmm_auth_status != -1 || $tmm_auth_ssl_ocsp_done == 0} {\n                reject\n            }\n        }\n    }"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful (is_success=true):_ "Successfully created iRule {name} in F5 BIG-IP".  
**The action should fail and stop a playbook execution:**  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Create iRule". Reason: {0}''.format(error.Stacktrace)****If status code is not 200: "Error executing action "Create iRule". Reason: {0}''.format(message) | General  
  
### Delete iRule

#### Description

Delete an iRule in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the iRule that needs to be deleted.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     {
        "kind": "tm:ltm:rule:rulestate",
        "name": "koko",
        "partition": "Common",
        "fullPath": "/Common/koko",
        "generation": 813,
        "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~koko?ver=16.0.1.1",
        "apiAnonymous": "when CLIENT_ACCEPTED {\n        set tmm_auth_ssl_ocsp_sid 0\n        set tmm_auth_ssl_ocsp_done 0\n    }\n    when CLIENTSSL_CLIENTCERT {\n        if {[SSL::cert count] == 1} {\n            return\n        }\n        set tmm_auth_ssl_ocsp_done 0\n        if {$tmm_auth_ssl_ocsp_sid == 0} {\n            set tmm_auth_ssl_ocsp_sid [AUTH::start pam default_ssl_ocsp]\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_ssl_ocsp_sid\n            }\n        }\n        AUTH::cert_credential $tmm_auth_ssl_ocsp_sid [SSL::cert 0]\n        AUTH::cert_issuer_credential $tmm_auth_ssl_ocsp_sid [SSL::cert issuer 0]\n        AUTH::authenticate $tmm_auth_ssl_ocsp_sid\n        SSL::handshake hold\n    }\n    when CLIENTSSL_HANDSHAKE {\n        set tmm_auth_ssl_ocsp_done 1\n    }\n    when AUTH_RESULT {\n        if {[info exists tmm_auth_ssl_ocsp_sid] and \\\n            ($tmm_auth_ssl_ocsp_sid == [AUTH::last_event_session_id])} {\n            set tmm_auth_status [AUTH::status]\n            if {$tmm_auth_status == 0} {\n                set tmm_auth_ssl_ocsp_done 1\n                SSL::handshake resume\n            } elseif {$tmm_auth_status != -1 || $tmm_auth_ssl_ocsp_done == 0} {\n                reject\n            }\n        }\n    }"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful (is_success=true):_ ****"Successfully deleted iRule {name} in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Delete iRule". Reason: {0}''.format(error.Stacktrace)****_If status code is not 200:_ "Error executing action "Delete iRule". Reason: {0}''.format(message) | General  
  
### Update iRule

#### Description

Update an iRule in F5 BIG-IP.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the iRule that needs to be updated.  
Rule | String | N/A | Yes | Specify the new rule that needs to be executed.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     {
        "kind": "tm:ltm:rule:rulestate",
        "name": "koko",
        "partition": "Common",
        "fullPath": "/Common/koko",
        "generation": 813,
        "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~koko?ver=16.0.1.1",
        "apiAnonymous": "when CLIENT_ACCEPTED {\n        set tmm_auth_ssl_ocsp_sid 0\n        set tmm_auth_ssl_ocsp_done 0\n    }\n    when CLIENTSSL_CLIENTCERT {\n        if {[SSL::cert count] == 1} {\n            return\n        }\n        set tmm_auth_ssl_ocsp_done 0\n        if {$tmm_auth_ssl_ocsp_sid == 0} {\n            set tmm_auth_ssl_ocsp_sid [AUTH::start pam default_ssl_ocsp]\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_ssl_ocsp_sid\n            }\n        }\n        AUTH::cert_credential $tmm_auth_ssl_ocsp_sid [SSL::cert 0]\n        AUTH::cert_issuer_credential $tmm_auth_ssl_ocsp_sid [SSL::cert issuer 0]\n        AUTH::authenticate $tmm_auth_ssl_ocsp_sid\n        SSL::handshake hold\n    }\n    when CLIENTSSL_HANDSHAKE {\n        set tmm_auth_ssl_ocsp_done 1\n    }\n    when AUTH_RESULT {\n        if {[info exists tmm_auth_ssl_ocsp_sid] and \\\n            ($tmm_auth_ssl_ocsp_sid == [AUTH::last_event_session_id])} {\n            set tmm_auth_status [AUTH::status]\n            if {$tmm_auth_status == 0} {\n                set tmm_auth_ssl_ocsp_done 1\n                SSL::handshake resume\n            } elseif {$tmm_auth_status != -1 || $tmm_auth_ssl_ocsp_done == 0} {\n                reject\n            }\n        }\n    }"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful (is_success= true):_ ****"Successfully updated iRule {name} in F5 BIG-IP".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Update iRule". Reason: {0}''.format(error.Stacktrace)****_If status code is not 200:_ ****"Error executing action "Update iRule". Reason: {0}''.format(message) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
