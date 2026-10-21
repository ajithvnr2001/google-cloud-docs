---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/humio/
title: Humio \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:03.789768+00:00
---

# Humio  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/humio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Humio

**Important:** Humio was acquired by CrowdStrike and became part of CrowdStrike Falcon Insight XDR.

This document provides guidance on how to integrate Humio with Google SecOps.

## Configure Humio integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://cloud.us.humio.com | Yes | API root of the Humio instance.  
API Token | Password | N/A | Yes | API token of the Humio instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Humio server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Use Cases

  1. Perform ingestion of the events from repositories
  2. Perform searching



## Actions

### Ping

#### Description

Test connectivity to the Humio with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Humio server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the Humio server! Error is {0}".format(exception.stacktrace) | General  
  
### Execute Simple Search

#### Description

Search events based on parameters in Humio.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Repository Name | String | N/A | Yes | Specify the name of the repository that should be searched.  
Query Filter | String | N/A | No | Specify the query that should be executed during the search. **Note:** The "head()" and "select()" functions shouldn't be provided.  
Time Frame | DDL | Last HourPossible Values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Custom

| No | Specify a time frame for the results. If "Custom" is selected, you also need to provide the ****"Start Time" parameter.  
Start Time | String | N/A | No | Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.  
Fields To Return | CSV | N/A | No | Specify the fields to return. If nothing is provided, the action returns all fields.  
Sort Field | String | N/A | No | Specify what parameter should be used for sorting. By default the query sorts data by timestamp in the ascending order.  
Sort Field Type | DDL | StringPossible Values:

  * String
  * Number
  * Hex

| No | Specify the type of the field that is used for sorting. This parameter is needed to ensure that the correct results are returned.  
Sort Order | DDL | ASCPossible Values:

  * ASC
  * DESC

| No | Specify the order of sorting.  
Max Results To Return | Integer | 50 | No | Specify the number of results to return.  
  
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
        "@timestamp": 1636028056292,
        "@rawstring": {
          "actor": {
            "ip": "31.43.227.151",
            "orgRoot": false,
            "organizationId": "z4ApqmrB7XbvsQB5E1muelI4WAKz4buZ",
            "proxyRequest": false,
            "type": "orgUser",
            "user": {
              "id": "MgPXnBAKQ4gCg25hW5jKhYTo",
              "isRoot": false,
              "username": "dana@example.com"
            }
          },
          "method": "google",
          "sensitive": false,
          "timestamp": "2021-11-04T12:14:16.292Z",
          "type": "user.signin"
        },
        "@id": "gZPMhXMMcScGXHwxZ7bRH6Ns_88_264_1636028056"
      },
      {
        "@timestamp": 1636028057934,
        "@rawstring": {
          "actor": {
            "ip": "31.43.227.151",
            "orgRoot": false,
            "organizationId": "z4ApqmrB7XbvsQB5E1muelI4WAKz4buZ",
            "proxyRequest": false,
            "type": "orgUser",
            "user": {
              "id": "MgPXnBAKQ4gCg25hW5jKhYTo",
              "isRoot": false,
              "username": "dana@example.com"
            }
          },
          "sensitive": false,
          "timestamp": "2021-11-04T12:14:17.934Z",
          "type": "notifications.user.create"
        },
        "@id": "lSLLg2gMDW8GwHtpZTGD8GU1_65_108_1636028057"
      }
    ]
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
**Result type** | **Value/Description** | **Type**  
Output message* | **The action should not fail nor stop a playbook execution:******_If found at least one result (is_success=true):_ "Successfully returned results for the query "{query}" in Humio.**"**_If no results are found (is_succees=true):_ "No results were found for the query "{query}" in Humio."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other:_ "Error executing action "Execute Simple Search". Reason: {0}''.format(error.Stacktrace)If the 400 status code is reported: "Error executing action "Execute Simple Search". Reason: {0}''.format(response)If the 404 status code is reported: "Error executing action "Execute Custom Search". Reason: {0}''.format(response) | General  
Case Wall | **Name:** Results | General  
  
### Execute Custom Search

#### Description

Search events using custom query in Humio.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Repository Name | String | N/A | Yes | Specify the name of the repository that should be searched.  
Query | String | N/A | Yes | Specify the query that needs to be executed in Humio. **Note:** The "head()" function shouldn't be a part of this string.  
Max Results To Return | Integer | 50 | No | Specify the number of results to return.  
  
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
        "@timestamp": 1636028056292,
        "@rawstring": {
          "actor": {
            "ip": "31.43.227.151",
            "orgRoot": false,
            "organizationId": "z4ApqmrB7XbvsQB5E1muelI4WAKz4buZ",
            "proxyRequest": false,
            "type": "orgUser",
            "user": {
              "id": "MgPXnBAKQ4gCg25hW5jKhYTo",
              "isRoot": false,
              "username": "dana@example.com"
            }
          },
          "method": "google",
          "sensitive": false,
          "timestamp": "2021-11-04T12:14:16.292Z",
          "type": "user.signin"
        },
        "@id": "gZPMhXMMcScGXHwxZ7bRH6Ns_88_264_1636028056"
      },
      {
        "@timestamp": 1636028057934,
        "@rawstring": {
          "actor": {
            "ip": "31.43.227.151",
            "orgRoot": false,
            "organizationId": "z4ApqmrB7XbvsQB5E1muelI4WAKz4buZ",
    
                  "proxyRequest": false,
            "type": "orgUser",
            "user": {
              "id": "MgPXnBAKQ4gCg25hW5jKhYTo",
              "isRoot": false,
              "username": "dana@example.com"
            }
          },
          "sensitive": false,
          "timestamp": "2021-11-04T12:14:17.934Z",
          "type": "notifications.user.create"
        },
        "@id": "lSLLg2gMDW8GwHtpZTGD8GU1_65_108_1636028057"
      }
    ]
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**___If found at least one result (is_success=true):_ "Successfully returned results for the query "{query}" in Humio."_If no results are found (is_succees=true):_ "No results were found for the query "{query}" in Humio"**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Execute Custom Search". Reason: {0}''.format(error.Stacktrace)If the 400 status code is reported: "Error executing action "Execute Custom Search". Reason: {0}''.format(response)If the 404 status code is reported: "Error executing action "Execute Custom Search". Reason: {0}''.format(response) | General  
Case Wall | **Name:** Results | General  
  
## Connectors

### Humio - Events Connector

#### Description

Pull information about events in the repository from Humio.

#### Configure Humio - Events Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | event_field | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | **""** | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 360 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://cloud.us.humio.com | Yes | API root of the Humio instance.  
API Token | Password | N/A | No | API token of the Humio instance.  
Repository Name | String | N/A | Yes | Name of the repository from the results will be fetched.  
Query | String | N/A | No | Query for the events. Note: select() and head() functions should not be added here.  
Alert Field Name | String | N/A | No | Name of the key that should be used for Alert Name. If nothing or invalid value is provided, the connector will use "Humio Alert" as fallback.  
Severity Field Name | CSV | N/A | Yes | A comma-separated list of keys that should be used for mapping of the severity. Note: if the key contains "string" values, they should be mapped with "Severity Mapping JSON". If invalid key is provided, "Default" from the "Severity Mapping JSON" parameter will be used.  
Severity Mapping JSON | JSON | { "fieldName": { "value_1": 100, "value_2": 75, "value_3": -1 }, "Default": 50} | Yes | JSON object that contains all of the keys with mapped string values. Note: "Default" key is mandatory.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch events.  
Max Events To Fetch | Integer | 20 | No | How many events to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Checked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Humio is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
