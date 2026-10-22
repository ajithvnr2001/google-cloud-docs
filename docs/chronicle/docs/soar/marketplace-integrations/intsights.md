---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/intsights/
title: IntSights \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:19.188976+00:00
---

# IntSights  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/intsights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IntSights

This document provides guidance on how to integrate IntSights with Google SecOps.

## Configure IntSights integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Add Note

#### Description

Add a note to the alert in IntSights.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert to which you want to add a note.  
Note | String | N/A | Yes | Specify the note for the alert.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful (is_success=true):_ "Successfully add a note to the alert with ID '{0}' in Intsights ".format(alert id)  
**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Add Note". Reason: {0}''.format(error.Stacktrace)_If the 404 status code is reported:_ "Error executing action "Add Note". Reason: alert with ID {alert id} was not found in IntSights.' | General  
  
### Ask An Analyst

#### Description

Ask an analyst regarding the alert in IntSights.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert where you want to ask the analyst.  
Comment | String | N/A | Yes | Specify the comment for the analyst.  
  
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
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully asked analyst in the alert with ID '{0}' in Intsights ".format(alert id)  
_If the 400 or 500 status code is reported:_ ****"Action was not able to ask the analyst in the alert with ID {0} in Intsights. Reason: {1}.".format(alert_id, response string)  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Ask an Analyst". Reason: {0}''.format(error.Stacktrace) | General  
  
### Assign Alert

#### Description

Assign alert to an analyst in IntSights.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert on which you want to change the assignment.  
Assignee ID | String | N/A | No | Specify the ID of the analyst that should be assigned to the alert.   
Note: If both "Assignee ID" and "Assignee Email Address" are specified, action will prioritize "Assignee ID".  
Assignee Email Address | String | N/A | No | Specify the email address of the analyst that should be assigned to the alert.   
Note: If both "Assignee ID" and "Assignee Email Address" are specified, action will prioritize "Assignee ID".  
  
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
Output message* | **The action should not fail nor stop a playbook execution:******_If successful with assignee ID:_ ****"Successfully assigned analyst with ID '{0}' to the alert with ID {1} in Intsights ".format(assignee id, alert id)  
_If successful with assignee email address:_ "Successfully assigned analyst with email address '{0}' to the alert with ID {1} in Intsights ".format(assignee email address, alert id)  
_If assignee is not found, the status code is 400, and worked with assignee ID:_ "Action was not able to change the assignment on the alert with ID {0}. Reason: Assignee with ID {1} was not found.".format(alert_id, assignee id)"****  
****_If assignee is not found, the status code is 400, and worked with assignee email address:_ ****"Action was not able to change the assignment on the alert with ID {0}. Reason: Assignee with email address {1} was not found.format(alert_id, email address)"  
****_If the 400 or 500 status code is reported:_ ****"Action was not able to change the assignment on the alert with ID {0}. Reason: {1}.".format(alert_id, response)  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Assign Alert". Reason: {0}''.format(error.Stacktrace)  
_If the "Assignee ID" and "Assignee Email address" parameters are not specified:_ ****"Assignee ID or Email Address should be specified." | General  
  
### Close Alert

#### Description

Close alert in IntSights.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert which you want to close.  
Reason | DDL | Problem SolvedPossible Values:

  * Problem Solved
  * Informational Only
  * Problem We Are Aware Of
  * Company Owned Domain
  * Legitimate Application/Profile
  * Not Related To My Company
  * False Positive
  * Other

| Yes | Specify the reason why the alert needs to be closed.  
Additional Info | String | N/A | No | Specify additional information explaining why the alert should be closed.  
Rate | Integer | 5 | No | Specify the rating of the alert. Maximum is 5.  
  
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
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully closed the alert with ID '{0}' in Intsights ".format(alert id)  
_If the 400 status code is reported:_ "Action was not able to close the alert with ID {0} in Intsights. Reason: {1}.".format(alert_id, response string)  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Close Alert". Reason: {0}''.format(error.Stacktrace)  
_If the "Rate" parameter is not in the 1-5 range:_ ****"Rate value should be in range from 1 to 5." | General  
  
### Download Alert CSV

#### Description

Download CSV file containing information related to alert in IntSights.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert for which you want to download CSV.  
Download Folder Path | String | N/A | Yes | Specify the path to the folder, where you want to store the CSV file.  
Overwrite | Checkbox | N/A | No | If enabled, action will overwrite the file with the same name.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "absolute_paths": ["/opt/file_1"]
    }
    

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful for at least one CSV (is_success=true):_ ****"Successfully downloaded CSV for the alert with ID {0} in Intsights:".format(alert_id)  
****_If the 400 status code is reported (is_success=true):_ ****"No CSV information was found for the alert with ID {alert_id} in Intsights."  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ **** "Error executing action "Download Alert CSV". Reason: {0}''.format(error.Stacktrace)****_If a file with the same name already exists, but "Overwrite" is set to false:_ ****"Error executing action "Download Alert CSV". Reason: file with path {0} already exists. Please delete the file or set "Overwrite" to true."****_If the 404 status code is reported:_ ****"Error executing action "Download Alert CSV". Reason: Unable to find alert with ID {ID}' | General  
  
### Get Alert Image

#### Description

Retrieve information about alert images in IntSights.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert Image IDs | CSV | N/A | Yes | Specify the comma-separated list of alert image IDs.   
Example: id1,id2.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
      {
        "image_name": "5b59daf4bdafd90xxxxxx",
        "image_base64_content": "image content in base64"
      }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful for at least one image:_ "Successfully retrieved images from the following IDs in Intsights:".format(list of ids)  
_If not successful for at least one image:_ ****"Action wasn't able to successfully retrieve images from the following IDs in Intsights:\n".format(list of ids)  
_If not successful for all images:_ ****"No images were retrieved".  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Get Alert Image". Reason: {0}''.format(error.Stacktrace) | General   
  
### Ping

#### Description

Check connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the URL entity.

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

### Reopen Alert

#### Description

Reopen alert in IntSights.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | True | Specify the ID of the alert which you want to reopen.  
  
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
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ ****"Successfully reopened the alert with ID '{0}' in Intsights ".format(alert id)****_If the 400 status code is reported:_ "Action was not able to reopen the alert with ID {0} in Intsights. Reason: {1}.".format(alert_id, response string)  
******The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to server, other is reported:_ ****"Error executing action "Reopen Alert". Reason: {0}''.format(error.Stacktrace) | General  
  
### Search IOCs

#### Description

Organize and search all your IOCs within a single, easy-to-use dashboard. The centralized TIP dashboard summarizes IOCs by severity and confidence level, so you can easily understand which malicious IOCs pose the greatest risk to your organization.

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
    
    
    [{
       "EntityResult":
         {
            "Status": "Active",
            "Domain": "sephoratv.com",
            "Severity":
             {
               "Status": "done",
               "LastUpdate": "2019-01-20T04:32:58.833Z",
               "Features":
                 [{
                     "Score": 10, "Name": "base_intsights_multiple",
                      "Match": 1
                   },
                   {
                      "Score": 0,
                      "Name": "domain_associated_malware_names",
                      "Match": 0
                    },
                   {
                      "Score": 0,
                      "Name": "domain_associated_malware_ip_addresses",
                      "Match": 1
                  }],
               "LastUpdateMessage": "",
               "Value": "Low",
               "Score": 20
              },
            "SourceID": "59e376681bb0800644e1368f",
            "Value": "sephoratv.com",
            "Flags": {"IsInAlexa": false},
            "LastSeen": "2019-01-20T04:24:27.258Z",
            "_id": "5c43f80483df230007485c48",
            "Type": "Domains",
            "Enrichment":
             {
               "Status": "done",
               "LastUpdate": "2019-01-20T04:32:58.613Z",
               "Data":
                   {
                      "domain_status_blocked": false,
                      "latest_resolution_date": "2019-01-20T04:27:22.299Z",
                      "associated_malware_ip_addresses": ["185.16.44.132"],
                      "contact_emails": [],
                      "referencing_file_hashes": [],
                      "malware_category": [],
                      "mail_servers": ["a.mx.domainoo.fr."],
                      "associated_malware_names": [],
                      "threat_actor_category": [],
                      "campaigns": [],
                      "associated_malware_families": [],
                      "resolved_ips": ["185.16.44.132"],
                      "cve_ids": [],
                      "downloaded_file_hashes": [],
                      "domain_expired": false,
                      "communicating_file_hashes": ["210c2ddbf747220df645fc4d77e7decd1be7df27e43b2f79e4b45bd5fe0a2a6e"],
                      "name_servers": ["a.ns.domainoo.fr.",
                                       "b.ns.domainoo.fr.",
                                       "c.ns.domainoo.fr."],
                      "registrar": "N/A",
                      "threat_actors": []
                    }
               },
            "FirstSeen": "2019-01-20T04:24:27.258Z",
            "AccountID": null
        },
     "Entity": "sephoratv.com"
    }]
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Status | Returns if it exists in JSON result  
Domain | Returns if it exists in JSON result  
Severity | Returns if it exists in JSON result  
SourceID | Returns if it exists in JSON result  
Value | Returns if it exists in JSON result  
Flags | Returns if it exists in JSON result  
LastSeen | Returns if it exists in JSON result  
_id | Returns if it exists in JSON result  
Type | Returns if it exists in JSON result  
Enrichment | Returns if it exists in JSON result  
FirstSeen | Returns if it exists in JSON result  
AccountID | Returns if it exists in JSON result  
  
##### Insights

Yes

## Connectors

### Intsights Connector

#### Description

Fetches issues from Intsights to Google SecOps.

#### Configure Insights Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Name | Type | Default Value | Description  
---|---|---|---  
DeviceProductField | String | Details_Source_NetworkType | The field name used to determine the device product.  
EventClassId | String | Details_Title | The field name used to determine the event name (sub-type).  
PythonProcessTimeout | String | 60 | The timeout limit (in seconds) for the python process running current script.  
Api Root | String | https://api.intsights.com | The API root of the Intsights server.  
Account ID | String | N/A | The account ID to login with.  
Api Key | Password | N/A | The API key to login with.  
Verify SSL | Checkbox | Unchecked | Whether to verify the SSL certificate of the server.  
Max Days Backwards | Integer | 3 | Max number of days backwards to pull alerts from.  
Max Alerts Per Cycle | Integer | 10 | Max number of alerts to fetch per single connector cycle.  
Proxy Server Address | String | N/A | The address of the proxy server to use.  
Proxy Username | String | N/A | The proxy username to authenticate with.  
Proxy Password | Password | N/A | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

##### Whitelist/Blacklist

The connector supports Whitelist/Blacklist rules.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
