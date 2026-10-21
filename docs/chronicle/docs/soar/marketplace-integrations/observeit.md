---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/observeit/
title: ObserveIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:08.262304+00:00
---

# ObserveIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/observeit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ObserveIT

This document provides guidance on how to integrate ObserveIT with Google SecOps.

## Use Cases

Ingest ObserveIT alerts and use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.

## Generate Client ID and Client Secret

**Note:** ObserveIT has a bug, where it would authenticate integration, even if invalid Client ID is specified. It happens because the backend in ObserveIT only validates the first 36 characters and everything else is ignored. For example, if AAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAAA is known valid Client ID, if you use AAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAABBBBB it will still let you to authenticate.

  1. Go to https://:/v2/apps/portal/home.html?#creds.
  2. Press on the "+ Create App" button
  3. Fill out the "Application Name" parameter.

![Create application
dialog](https://docs.cloud.google.com/static/chronicle/images/integrations/observeit-create-application.png)

  4. Press on the "Save".

  5. You will find a new ObserveIT application. Press on it and you will see this window.

![Created application details with Client ID and Client Secret
values](https://docs.cloud.google.com/static/chronicle/images/integrations/oberveit-application-details.png)

  6. Copy "Client Id" and "Client Secret".

  7. Use these values in the integration configuration.




## Configure ObserveIT integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
API Root | String | https://<address>:<port> | Yes | ObserveIT API Root.  
Client ID | String | N/A | Yes | Client ID of the ObserveIT app.  
Client Secret | Password | N/A | Yes | Client Secret of the ObserveIT app.  
Use SSL | Checkbox | Checked | Yes | Option to enable SSL/TLS connection  
  
## Actions

### Ping

#### Description

Test connectivity to ObserveIT with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Playbook Use Cases Examples

The action is used to test connectivity at the integration configuration page on the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

## Connectors

### ObserveIT - Alerts Connector

#### Description

Pull alerts from ObserveIT.

#### Configure ObserveIT - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://x.x.x.x:x | Yes | API root of ObserveIT server.  
Client ID | String | N/A | Yes | Client ID of the ObserveIT app.  
Client Secret | Password |  | Yes | Client Secret of the ObserveIT app.  
Lowest Severity To Fetch | String | Medium | Yes | Lowest severity that will be used to fetch Alerts. Possible values:  
Low Medium High Critical  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch alerts.  
Max Alerts To Fetch | Integer | 25 | No | How many alerts to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Use SSL | Checkbox | Checked | Yes | Option to enable SSL/TLS connection  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
