---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/extrahop/
title: ExtraHop \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:45.505770+00:00
---

# ExtraHop  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/extrahop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ExtraHop

This document describes how to integrate ExtraHop with Google Security Operations.

## Configure ExtraHop integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration: 

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String |  | Yes | API root of the ExtraHop instance.  
Client ID | String | N/A | Yes | Client ID of the ExtraHop instance.  
Client Secret | Password | N/A | Yes | Client Secret of the ExtraHop instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the ExtraHop server is valid.  
  
## Product Use Cases

Ingestion of alerts

## Actions

### Ping

#### Description

Test connectivity to ExtraHop with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
#### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _if successful:_ "Successfully connected to the ExtraHop server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the ExtraHop server! Error is {0}".format(exception.stacktrace) | General  
  
### Update Detection

Update a detection in ExtraHop.

#### Run On

This action doesn't run on entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Detection ID | String | N/A | Yes | Specify the ID of the detection that needs to be updated.  
Status | DDL | Possible Values: 

  * Closed
  * In Progress
  * Acknowledged

| No | Specify the status for the detection.  
Resolution | DDL | Possible Values: 

  * Action Taken
  * No Action Taken

| No | Specify the resolution for the detection. If Status parameter is set to "Closed", Resolution parameter is needed.  
Assign To | String | N/A | No | Specify the name of the analyst to whom the alert needs to be assigned. If "Unassign" is provided, the action will remove assignment from the alert.  
  
#### Action Outputs

Type | Available  
---|---  
Script Result | True  
JSON Result | True  
Enrichment Table | False  
Case Wall Table | False  
Case Wall Link | False  
Case Wall Attachment | False  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
     0: {
       "id": 4294967299,
       "start_time": 1693795020000,
       "update_time": 1693805700000,
       "end_time": 1694198520000,
       "title": "LLMNR Activity",
       "description": "[EVAL\\-W2019\\-PRD](https://wwt-mand.cloud.extrahop.com#/
       // metrics/devices/d0ded7fd86f0459890394969c49d2bf6.005056bd27330000/
       // overview?from=1693795020&interval_type=DT&until=1694198520) sent
       // Link-Local Multicast Name Resolution (LLMNR) requests that are part of an
       // internal broadcast query to resolve a hostname. The LLMNR protocol is 
       // known to be vulnerable to attacks.",
       "risk_score": 30,
       "type": "llmnr_activity_individual",
       "recommended_factors": [],
       "recommended": false,
       "categories": [
           "sec",
           "sec.hardening"
       ],
       "properties": {},
       "participants": [
           {
               "role": "offender",
               "scanner_service": null,
               "endpoint": null,
               "external": false,
               "object_id": 4294967305,
               "object_type": "device",
               "username": null,
               "id": 2
           }
       ],
       "ticket_id": null,
       "assignee": "ankita.shakya@wwtatc.com",
       "status": "in_progress",
       "resolution": null,
       "mitre_tactics": [],
       "mitre_techniques": [],
       "appliance_id": 1,
       "is_user_created": false,
       "mod_time": 1694790591224,
       "create_time": 1693795051521,
       "url": "https://wwt-mand.cloud.extrahop.com/extrahop/#/detections/detail/4294
       // 967299/?from=1693794120&until=1694199420&interval_type=DT"
    }
    

#### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* |  **The action should not fail or stop a playbook execution:** _if returned info (is_success = true):_ print "Successfully updated detection with ID {detection id} in Extrahop." **The action should fail and stop a playbook execution:** _if fatal error, like wrong credentials, no connection to server, other:_ print "Error executing action "Update Detection". Reason: {0}''.format(error.Stacktrace) _If detection not found (404 status code):_ Error executing action "Update Detection". Reason: detection with ID {alert id} wasn't found in Extrahop. Please check the spelling." _If "type": "request_error":_ Error executing action "Update Detection". Reason: {detail}" _If "Status" is "Select One", and nothing is provided in "Assign To":_ Error executing action "Update Detection". Reason: at least one of the "Status" or "Assign To" parameters should have a value."  | General  
  
## Connectors

### ExtraHop - Detections Connector

#### Description

Pull information about detections from ExtraHop. Note: The whitelist filter works with the "type" parameter.

#### Configure ExtraHop - Detections Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector: 

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .__|  No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is . to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{instance}.api.cloud.extrahop.com | Yes | API root of the ExtraHop instance.  
Client ID | String | N/A | Yes | Client ID of the ExtraHop instance.  
Client Secret | Password | N/A | Yes | Client Secret of the ExtraHop instance.  
Lowest Risk Score To Fetch | Integer | N/A | No | Lowest risk score that needs to be used to fetch detections. Maximum: 100. If nothing is provided, the connector will ingest detections with all risk scores.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch detections.  
Max Detections To Fetch | Integer | 100 | No | How many detections to process per one connector iteration. Default: 100.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the ExtraHop server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy. **Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
