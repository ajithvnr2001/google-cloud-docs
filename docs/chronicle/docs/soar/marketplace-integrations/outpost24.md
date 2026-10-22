---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/outpost24/
title: Outpost24 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:40.967258+00:00
---

# Outpost24  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/outpost24/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Outpost24

This document provides guidance on how to integrate Outpost24 with Google SecOps.

## Configure Outpost24 integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://your-appliance.outpost24.com | Yes | API root of the Outpost24 instance.  
Username | String | N/A | Yes | Username of the Outpost24 account.  
Password | Password | N/A | Yes | Password of the Outpost24 account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Outpost24 server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Use Cases

  1. Perform enrichment of entities
  2. Ingestion of alerts



## Actions

### Enrich Entities

#### Description

Enrich entities using information from Outpost24. Supported entities: IP Address, Hostname.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
Return Finding Information | Checkbox | Checked | No | If enabled, the action also retrieves information about findings that were found on the endpoint.  
Finding Type | DDL | AllPossible values:

  * All
  * Vulnerability
  * Information
  * Port

| No | Specify the type of findings to return.  
Finding Risk Level Filter | CSV | Initial, Recommendation, Low, Medium, High, Critical | No | Specify a comma-separated list of risk level findings that are used during filtering. Possible values: Initial, Recommendation, Low, Medium, High, Critical. If nothing is provided, the action fetches findings with all risk levels.  
Max Findings To Return | Integer | 100 | No | Specify the number of findings to process per entity. If nothing is provided, the action returns 100 findings.  
  
#### Run On

The action is runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "id": 24358,
        "ip": "10.205.0.35",
        "hostname": "lix18.mirmine.net",
        "businessCriticality": "MEDIUM",
        "exposed": false,
        "created": "2021-09-09T12:58:47.085514Z",
        "firstSeen": "2021-09-09T12:58:47.085514Z",
        "source": [
            "NETSEC"
        ]
    "Findings": [list of findings]
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
hostname | When available in JSON  
ip | When available in JSON  
exposed | When available in JSON  
businessCriticality | When available in JSON  
created | When available in JSON  
firstSeen | When available in JSON  
source | When available in JSON  
count_initial_findings | When available in JSON  
count_recommendation_findings | When available in JSON  
count_low_findings | When available in JSON  
count_medium_findings | When available in JSON  
count_high_findings | When available in JSON  
count_critical_findings | When available in JSON  
  
##### Case Wall

Result type | Value / Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**___If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from Outpost24 Mobile: {entity.identifier}"._If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Outpost24: {entity.identifier}"_If data is not available for any entity (is_success=false): "_ None of the provided entities were enriched."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace): "Error executing action "Enrich Entities". Reason: invalid risk level filter values provided: {csv of invalid values}. Possible values: Initial, Recommendation, Low, Medium, High, Critical.' | General  
Case Wall Table | **Table Title:** {entity.identifier}**Table Columns:**

  * Key
  * Value

| Entity  
Case Wall Table | **Table Title:** {entity.identifier}**Table Columns:**

  * CVE
  * Product Name
  * Service Name
  * Type
  * Solution
  * Reason
  * Description
  * Risk Level

| Table  
  
### Ping

#### Description

Test connectivity to the Outpost24 with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Outpost24 server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the Outpost24 server! Error is {0}".format(exception.stacktrace) | General  
  
## Connectors

### Outpost24 - Outscan Findings Connector

#### Description

Pull information about outscan findings from Outpost24.

**Note:** The whitelist filter works with the "productName" parameter.

#### Configure Outpost24 - Outscan Findings Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | **""** | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 300 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://your-appliance.outpost24.com | Yes | API root of the Outpost24 instance.  
Username | String | N/A | Yes | Username of the Outpost24 account.  
Password | Password | N/A | Yes | Password of the Outpost24 account.  
Type Filter | CSV | Vulnerability, Information, Port | Yes | Comma-separated list of type filters for the finding. Possible values: Vulnerability, Information, Port.  
Lowest Risk To Fetch | String | N/A | No | The lowest risk that needs to be used to fetch alerts. Possible values: Initial, Recommendation, Low, Medium, High, Critical. If nothing is specified, the connector ingests alerts with all risk levels.  
Max Days Backwards | Integer | 1 | No | The number of hours for which findings should be fetched.  
Max Findings To Fetch | Integer | 100 | No | The number of findings to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist is used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Outpost24 server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
