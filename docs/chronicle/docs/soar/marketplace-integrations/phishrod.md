---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/phishrod/
title: PhishRod \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:04.402960+00:00
---

# PhishRod  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/phishrod/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# PhishRod

This document provides guidance on how to integrate PhishRod with Google SecOps.

## Configure PhishRod integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://api.bitsighttech.com | Yes | API root of the PhishRod instance.  
API Key | Password | N/A | Yes | API Key of the PhishRod account.  
Client ID | Password | N/A | Yes | Client ID of the PhishRod account.  
Username | String | N/A | Yes | Username of the PhishRod account.  
Password | Password | N/A | Yes | Password of the PhishRod account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the BitSight server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to PhishRod with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run on

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

#### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
#### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful (is_success=true):_ ****"Successfully connected to the PhishRod server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful (is_success= false):****_"Failed to connect to the PhishRod server! Error is {0}".format(exception.stacktrace) | General  
  
### Update Incident

#### Description

Update an incident in PhishRod.

**Note:** you can only update incidents that went through the secondary analysis.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident ID | String | N/A | Yes | Specify the ID of the incident that needs to be updated.  
Status | DDL | Delete Possible Values:

  * Safe
  * Delete

| No | Specify the status for the incident.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

#### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
#### JSON Result
    
    
    {
        "statusMarked": false,
        "message": "Incident status is already marked."
    }
    

#### Case Wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If statusmarked == "true" (is_success=true):_ "Successfully updated incident {incident id} in PhishRod. _If statusmarked == "false" (is_success=false):_ "Incident {incident id} status was already modified previously in PhishRod." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported: "Error executing action "Update Incident". Reason: {0}''.format(error.Stacktrace)_ _If message != "Incident status is already marked." and ""statusMarked"": false"_ "Error executing action "Update Incident". Reason: {0}".format(message)" | General  
  
### Mark Incident

#### Description

Mark an incident in PhishRod. 

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident ID | String | N/A | Yes | Specify the ID of the incident that needs to be marked.  
Status | DDL | Mark For Secondary Analysis Possible Values:

  * SMark For Secondary Analysis
  * Mark As Spam
  * Mask As Safe

| No | Specify how the incidents need to be marked.  
Comment | String | N/A | Yes | Specify the comment describing the reasons for the incident to be marked.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

#### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
#### JSON Result
    
    
    {
        "code": "200",
        "status": "Incident status has already been updated before."
    }
    

#### Case Wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code is reported (is_success=true):_ "Successfully marked the incident {incident id} in PhishRod." _If the 200 status code is reported and status is "Incident status has already been updated before" (is_success = false):_ "Incident {incident id} was already marked previously in PhishRod. **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Mark Incident". Reason: {0}''.format(error.Stacktrace) _If the 400 or 404 status code is reported:_ "Error executing action "Mark Incident". Reason: {0}".format(message)" | General  
  
## Connectors

### PhishRod - Incidents Connector

#### Description

Pull information about incidents from PhishRod.

**Note:** The dynamic list filter works with the "emailSubject" parameter.

#### Configure PhishRod - Incidents Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | Event Field | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | N/A | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | PythonProcessTimeout | 300 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{instance}.phishrod.co | Yes | API root of the PhishRod instance.  
API Key | Password | N/A | Yes | API key of the PhishRod account.  
Client ID | Password | N/A | Yes | Client ID of the PhishRod account.  
Username | String | N/A | Yes | Username of the PhishRod account.  
Password | Password | N/A | Yes | Password of the PhishRod account.  
Alert Severity Score | String | Medium | Yes | Set the severity for the alert based on the incident. Possible values: Informational, Low, Medium, High, Critical.  
Use dynamic list as a blacklist | Checkbox | Unchecked | Yes | If enabled, the dynamic list is used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Crowdstrike server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
