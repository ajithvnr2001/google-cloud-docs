---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/iboss/
title: iboss \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:03.864071+00:00
---

# iboss  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/iboss/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# iboss

This document provides guidance on how to integrate iboss with Google SecOps.

## Use Cases

  1. Perform enrichment actions - get data from iboss to enrich data in Google Security Operations alerts.
  2. Perform active actions - block an IP or URL in iboss from Google SecOps.



## Product Permission

In order to authenticate, actions perform two requests. The first request is to get a token and the second request is to get a special XSRF token.

## Configure iboss integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Note:** iboss may change your API root from time to time. Make sure that it is updated to the latest version.Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Cloud API Root | String | https://cloud.iboss.com/ | Yes | Specify the iboss cloud API Root.  
Account API Root | String | https://accounts.iboss.com/ | Yes | Specify the iboss Account API Root.  
Username | String | N/A | Yes | Specify the username of the iboss account.  
Password | Password | N/A | Yes | Specify the password of the iboss account.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verify the SSL certificate for the connection to the iboss public cloud server is valid.  
Run Remotely | Checkbox | Checked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the iboss with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
_if successful:_  
print "Successfully connected to the iboss server with the provided connection parameters!"  
**The action should fail and stop a playbook execution:**  
_if not successful:_ print "Failed to connect to the iboss server! Error is {0}".format(exception.stacktrace) | General  
  
### Add URL to Policy Block List

#### Description

Add URL to iboss Block List.

#### How to find Category ID

  1. Navigate to **Web Security** -> **Policy Layers**.
  2. Open **Developer Tools Console** (Ctrl + Shift + I in Google Chrome).
  3. Navigate there to **Network tab**.
  4. Try to edit the needed block list.



In the console, you will see requests that are being made. Search among those requests for customCategoryId=xxxx parameter.

##### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Category ID | Integer | 1001 | Yes | Specify to which policy category you want to add the URL.  
Priority | Integer | 50 | Yes | Specify priority of the URL that needs to be blocked.  
Direction | DDL | DestinationPossible values:DestinationSourceDestination and Source | Yes | Specify what is the direction of the URL.  
Start Port | Integer | N/A | No | Specify the start port related to the URL that needs to be blocked. Note: if only "Start Port" or "End Port" is specified, the value will be added to both action parameters.  
End Port | Integer | N/A | No | Specify the end port related to the URL that needs to be blocked. Note: if only "Start Port" or "End Port" is specified, the value will be added to both action parameters.  
Note | String | N/A | No | Add a note related to the URL that needs to be blocked.  
Is Regular Expression | Checkbox | Unchecked | No | If enabled, the URL will be considered as a regular expression.  
Strip Scheme | Checkbox | Unchecked | No | If enabled, action will strip the scheme related to the URL.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided URLs were blocked(is_success = true):_  
print "Successfully blocked the following URLs in the iboss category with ID {0}: \n {1}".format(category_id, entity.identifier list)  
_If fail to block specific URLs(is_success = true):_  
print "Action was not able to block the following URLs in the iboss category with ID {0}\n: {1}".format(category_id, [entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ print: "No URLs were blocked in the iboss category with ID {0}.".format(category_id)  
_If Policy is not a Block list: (is_success = false):_ print "Category with ID {category_id} is not associated with a Block list."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Add URL to Policy Block List". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add IP to Policy Block List

#### Description

Add IP to iboss Block List.

#### How to find Category ID

  1. Navigate to **Web Security** -> **Policy Layers**.
  2. Open **Developer Tools Console** (Ctrl + Shift + I in Google Chrome).
  3. Navigate there to **Network tab**.
  4. Try to edit the needed block list.



In the console, you will see requests that are being made. Search among those requests for customCategoryId=xxxx parameter.

##### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Category ID | Integer | 1001 | Yes | Specify to which policy category you want to add the URL.  
Priority | Integer | 50 | Yes | Specify priority of the URL that needs to be blocked.  
Direction | DDL | DestinationPossible values:DestinationSourceDestination and Source | Yes | Specify what is the direction of the URL.  
Start Port | Integer | N/A | No | Specify the start port related to the URL that needs to be blocked. Note: if only "Start Port" or "End Port" is specified, the value will be added to both action parameters.  
End Port | Integer | N/A | No | Specify the end port related to the URL that needs to be blocked. Note: if only "Start Port" or "End Port" is specified, the value will be added to both action parameters.  
Note | String | N/A | No | Add a note related to the URL that needs to be blocked.  
Is Regular Expression | Checkbox | False | No | If enabled, URL will be considered as a regular expression.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided URLs were blocked(is_success = true):_  
print "Successfully blocked the following URLs in the iboss category with ID {0}: \n {1}".format(category_id, entity.identifier list)  
_If fail to block specific URLs(is_success = true):_  
print "Action was not able to block the following URLs in the iboss category with ID {0}\n: {1}".format(category_id, [entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ print: "No URLs were blocked in the iboss category with ID {0}.".format(category_id)  
_If Policy is not a Block list: (is_success = false)_ :print "Category with ID {category_id} is not associated with a Block list."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Add URL to Policy Block List". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add IP to Policy Block List

#### Description

Add IP to iboss Block List.

#### How to find Category ID

  1. Navigate to **Web Security** -> **Policy Layers**.
  2. Open **Developer Tools Console** (Ctrl + Shift + I in Google Chrome).
  3. Navigate there to **Network tab**.
  4. Try to edit the needed block list.



In the console, you will see requests that are being made. Search among those requests for customCategoryId=xxxx parameter.

##### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Category ID | Integer | 1001 | Yes | Specify to which policy category you want to add the IP.  
Priority | Integer | 50 | Yes | Specify priority of the IP that needs to be blocked.  
Direction | DDL | DestinationPossible values:DestinationSourceDestination and Source | Yes | Specify what is the direction of the IP.  
Start Port | Integer | N/A | No | Specify the start port related to the IP that needs to be blocked. Note: if only "Start Port" or "End Port" is specified, the value will be added to both action parameters.  
End Port | Integer | N/A | No | Specify the end port related to the IP that needs to be blocked. Note: if only "Start Port" or "End Port" is specified, the value will be added to both action parameters.  
Note | String | N/A | No | Add a note related to the IP that needs to be blocked.  
Is Regular Expression | Checkbox | Unchecked | No | If enabled, IP will be considered as a regular expression.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided IPs were blocked(is_success = true):_  
print "Successfully blocked the following IPs in the iboss category with ID {0}: \n {1}".format(category_id, entity.identifier list)  
_If fail to block specific IPs(is_success = true):_  
print "Action was not able to block the following IPs in the iboss category with ID {0}\n: {1}".format(category_id, [entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ print: "No IPs were blocked in the iboss category with ID {0}.".format(category_id)  
_If Policy is not a Block list: (is_success = false):_ print "Category with ID {category_id} is not associated with a Block list."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Add IP to Policy Block List". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Policy Block List Entries

#### Description

Return iboss Block List entries in a specific group.

#### How to find Category ID

  1. Navigate to **Web Security** -> **Policy Layers**.
  2. Open **Developer Tools Console** (Ctrl + Shift + I in Google Chrome).
  3. Navigate there to **Network tab**.
  4. Try to edit the needed block list.



In the console, you will see requests that are being made. Search among those requests for customCategoryId=xxxx parameter.

##### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Category ID | Integer | 1001 | Yes | Specify in which policy category do you want to list Block List entries.  
Max Entries to Return | Integer | 50 | Yes | Specify how many entries to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "entries": [
           {
              "direction": 0,
              "endPort": 0,
              "isRegex": 0,
              "note": "",
              "priority": 0,
              "startPort": 0,
              "type": 0,
              "url": "asaa.com",
              "weight": 501
           }
        ],
        "message": ""
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful returned and is available data(is_success = true):_  
print "Successfully listed entries from the iboss Block List in a category with ID '{0}'".format(category_id)  
_If returned and no data (is_success = false):_ print: "No Block List entries were found in the iboss category with ID {0}.".format(category_id)If Policy is not a Block list: (is_success = false)Print "Category with ID {category_id} is not associated with a Block list."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "List Policy Block List Entries". Reason: {0}''.format(error.Stacktrace) | General  
CSV Case Wall | **Name:** "Block List Entries. Category {0}".format(Category)**Columns:**

  * Name (mapped as url)
  * Priority (mapped as priority)
  * Weight (mapped as weight)
  * Direction (mapped as direction. Check action behaviour)
  * Start Port (mapped as startPort)
  * End Port (mapped as endPort)
  * Note (mapped as note)
  * Regex (mapped as isRegex. 1 = True, 0 = False)

|   
  
### Remove URL from Policy Block List

#### Description

Remove URL from iboss Block List.

#### How to find Category ID

  1. Navigate to **Web Security** -> **Policy Layers**.
  2. Open **Developer Tools Console** (Ctrl + Shift + I in Google Chrome).
  3. Navigate there to **Network tab**.
  4. Try to edit the needed block list.



In the console, you will see requests that are being made. Search among those requests for customCategoryId=xxxx parameter.

##### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Category ID | Integer | 1001 | Yes | Specify from which policy category do you want to remove the URL.  
Start Port | Integer | N/A | No | Specify the start port related to the URL that needs to be deleted. This parameter is mandatory if the desired URL has a defined start port. This is an iboss limitation.  
End Port | Integer | N/A | No | Specify end port related to the URL that needs to be deleted. This parameter is mandatory if the desired URL has a defined end port. This is an iboss limitation.  
Strip Scheme | Checkbox | Un-checked | No | If enabled, action will strip the scheme related to the URL.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided URLs were removed (is_success = true):_  
print "Successfully removed the following URLs from the iboss category with ID {0}: \n {1}".format(category_id, entity.identifier list)  
_If fail to remove specific URLs(is_success = true):_ print "Action was not able to remove the following URLs from the category with ID {0}\n: {1}".format(category_id, [entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ Print: "No URLs were removed from the iboss category with ID {0}.".format(category_id)_If Policy is not a Block list: (is_success = false):_ Print "Category with ID {category_id} is not associated with a Block list."  
**The action should fail and stop a playbook execution:** if fatal error, like wrong credentials, no connection to server, other: print "Error executing action "Remove URL from Policy Block List". Reason: {0}''.format(error.Stacktrace) | General  
  
### Remove IP from Policy Block List

#### Description

Remove IP from iboss Block List.

#### How to find Category ID

  1. Navigate to **Web Security** -> **Policy Layers**.
  2. Open **Developer Tools Console** (Ctrl + Shift + I in Google Chrome).
  3. Navigate there to **Network tab**.
  4. Try to edit the needed block list.



In the console, you will see requests that are being made. Search among those requests for customCategoryId=xxxx parameter.

##### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Category ID | Integer | 1001 | Yes | Specify from which policy category do you want to remove IP.  
Start Port | Integer | N/A | No | Specify start port related to the IP that needs to be deleted. This parameter is mandatory if the desired URL has a defined start port. This is an iboss limitation.  
End Port | Integer | N/A | No | Specify end port related to the IP that needs to be deleted. This parameter is mandatory if the desired IP has a defined end port. This is an iboss limitation.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided URLs was removed (is_success = true):_  
print "Successfully removed the following IPs from the iboss category with ID {0}: \n {1}".format(category_id, entity.identifier list)  
_If fail to remove specific URLs(is_success = true):_ print "Action was not able to remove the following IPs from the iboss category with ID {0}\n: {1}".format(category_id, [entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ print: "No IPs were removed from the iboss category with ID {0}.".format(category_id)If Policy is not a Block list: (is_success = false)Print "Category with ID {category_id} is not associated with a Block list."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "Remove IP from Policy Block List". Reason: {0}''.format(error.Stacktrace) | General  
  
### URL Lookup

#### Description

Perform URL Lookup.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Group ID | Integer | N/A | No | Specify for which group to perform a URL Lookup. If nothing is specified, the "Default" group will be used.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
IBOSS_group_{group_id}_categories | categories | When available in JSON  
IBOSS_group_{group_id}_action | action | When available in JSON  
IBOSS_group_{group_id}_message | message | When available in JSON  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "action": "Not Blocked",
        "categories": "Pornography/Nudity",
        "message": "Url Known."
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful and at least one of the provided URLs was looked up (is_success = true):_  
print "Successfully retrieved information about the following URLs: \n {0}".format( entity.identifier list)  
_If fail to lookup specific URLs(is_success = true):_ Print: "Action was not able to retrieve information about the following URLs\n: {0}".format([entity.identifier])_If fail to lookup for all entities (is_success = false):_ Print "No information was retrieved about URLs."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to the server, other:_ print "Error executing action "URL Lookup". Reason: {0}''.format(error.Stacktrace) | General  
  
### URL Recategorization

#### Description

Submit URL for recategorization.

#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_if successful and at least one of the provided URLs was submitted(is_success = true):_  
print "Successfully submitted the following URLs for recategorization: \n {0}".format( entity.identifier list)  
_If fail to remove specific URLs(is_success = true):_ print "Action was not able to submit the following URLs for recategorization\n: {0}".format([entity.identifier])  
_If fail to enrich for all entities (is_success = false):_ print: "No URLs were submitted for recategorization."  
**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "URL Recategorization". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
