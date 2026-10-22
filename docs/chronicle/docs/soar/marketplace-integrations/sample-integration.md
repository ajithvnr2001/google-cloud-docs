---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sample-integration/
title: Integrate a sample integration with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:51.687493+00:00
---

# Integrate a sample integration with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sample-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate a sample integration with Google SecOps

This document is a comprehensive guide to a sample integration that demonstrates common design patterns for building actions, connectors, and jobs for Google Security Operations (Google SecOps).

## Integration parameters

The Sample Integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The API root for the integration instance. In this example case, the [VAT Comply](https://www.vatcomply.com) service is being used to integrate, with the API root `api.vatcomply.com`. The default value is `http://api.vatcomply.com`.  
`Password Field` | Optional. An example API password field. This parameter is included for demonstration purposes only and is not required by the API for authentication. The default value is `Google SecOps`.  
`Verify SSL` | Required. If selected, the action validates the SSL certificate of the API server. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test the connectivity to the integration.

This action doesn't run on Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result. | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the API Service server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the API Service server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Simple action example

This is an example of a basic action in Google SecOps.

This action fetches data from the `api.vatcomply.com` service based on the provided parameters. 

**Note:** This action is not asynchronous.

This action doesn't run on Google SecOps entities. 

#### Action inputs

Parameter | Description  
---|---  
`Currencies String` |  _This is an example of a parameter that accepts a comma-separated list of values._ Optional. A comma-separated list of currencies to process. The default value is `USD, EUR`.  
`Currencies DDL` |  _This is an example of a parameter that accepts a drop-down list of values._ Optional. A drop-down list of currencies to process. The default value is `Select One`. The possible values are: `

  * Select One
  * USD
  * EUR
  * CAD

`  
`Time Frame` |  Optional. The timeframe for the results. The default value is `Today`. The possible values are: `

  * Today
  * Last 7 Days
  * Custom

` If you select `Custom`, you must also provide a value for the `Start Time` parameter.  
`Start Time` |  Optional. The start time for the results in ISO 8601 format. This parameter is required if you select `Custom` for the `Time Frame` parameter. The time span between `Start Time` and `End Time` can't be more than seven days. The action only uses the date portion of the timestamp.  
`End Time` |  Optional. The end time for the results in ISO 8601 format. If you select `Custom` for the `Time Frame` and don't provide a value, the action uses the current time. The time span between `Start Time` and `End Time` can't be more than seven days. The action only uses the date portion of the timestamp.  
`Return JSON Result` |  _This is an example of a boolean input._ Optional. If enabled, the action returns a JSON result. Selected by default.  
  
#### Action outputs

The **Search Graphs** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Available  
Case wall link | Available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The action returns the following link:

  * Currency: `https://www.vatcomply.com/currencies/BASE_CURRENCY/date/DATE`



##### Case wall table

The action provides the following table for every API response:

Table name: **Currency: {base} - {date}**

Table columns:

  * **Currency** (rate.keyname)
  * **Value** (rate.keyname.value)



##### JSON result

The following example shows the JSON result output received when using the action:
    
    
    [
       {
           "date": "2000-03-03",
           "exchange_rates": [
               {
                   "base": "USD",
                   "rates": {
                       "EUR": 1.035303861683404,
                       "USD": 1.0,
                       "JPY": 107.8476032715602,
                       "CYP": 0.5955481933947614,
                       "CZK": 36.87752355316285,
                       "DKK": 7.711357283362667,
                       "EEK": 16.19898540221555,
                       "GBP": 0.6332953721917383,
                       "HUF": 265.60720571487735,
                       "LTL": 4.001035303861683,
                       "LVL": 0.5954032508541256,
                       "MTL": 0.4235428098146806,
                       "PLN": 4.125168236877524,
                       "ROL": 18961.590226731547,
                       "SEK": 8.769023708458434,
                       "SIT": 209.5625841184388,
                       "SKK": 43.26845429133451,
                       "CHF": 1.6630085930220522,
                       "ISK": 73.39269075473652,
                       "NOK": 8.369396417848638,
                       "TRL": 574745.8329019567,
                       "AUD": 1.647479035096801,
                       "CAD": 1.454705456051351,
                       "HKD": 7.782379128274149,
                       "KRW": 1119.9503054146392,
                       "NZD": 2.0485557511129517,
                       "SGD": 1.7232632777720263,
                       "ZAR": 6.4730303344031475
                   }
               },
               {
                   "base": "EUR",
                   "rates": {
                       "EUR": 1.0,
                       "USD": 0.9659,
                       "JPY": 104.17,
                       "CYP": 0.57524,
                       "CZK": 35.62,
                       "DKK": 7.4484,
                       "EEK": 15.6466,
                       "GBP": 0.6117,
                       "HUF": 256.55,
                       "LTL": 3.8646,
                       "LVL": 0.5751,
                       "MTL": 0.4091,
                       "PLN": 3.9845,
                       "ROL": 18315.0,
                       "SEK": 8.47,
                       "SIT": 202.4165,
                       "SKK": 41.793,
                       "CHF": 1.6063,
                       "ISK": 70.89,
                       "NOK": 8.084,
                       "TRL": 555147.0,
                       "AUD": 1.5913,
                       "CAD": 1.4051,
                       "HKD": 7.517,
                       "KRW": 1081.76,
                       "NZD": 1.9787,
                       "SGD": 1.6645,
                       "ZAR": 6.2523
                   }
               }
           ]
       }
    ]
    

##### Output messages

The action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about the following currencies from START_TIME to END_TIME: "CURRENCIES"` | The action succeeded.  
`Error executing action "ACTION_NAME". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enrich Entity action example

This is an example of an action that works with and enriches entities in Google SecOps.

This action runs on all Google SecOps entities provided in the parameter `Entity Type`.

**Note:** This is not an asynchronous action.

#### Action inputs

The **Enrich Entity** action requires the following parameters:

Parameter | Description  
---|---  
`Entity Type` | Required. The entities from the alert's scope to process. The default value is `All Entities`. The possible values are: `

  * IP
  * Hash
  * User

`  
  
#### Action outputs

The **Enrich Entity** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment table

The **Enrich Entity** action supports the following enrichment for entities:

Enrichment field | Source (JSON key) | Applicability  
---|---|---  
`SampleIntegration_enriched` | `true` | When available in the JSON result.  
`SampleIntegration_timestamp` | `timestamp` | When available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich Entity** action:
    
    
    {
       "Entity": "Entity",
       "EntityResult": [
           {
               "enriched": "true",
               "timestamp": "12123213123"
           }
       ]
    }
    

##### Output messages

The **Enrich Entity** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following entities: ENTITIES` | The action succeeded.  
`No eligible entities were found in the scope of the alert.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Entity** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Async action example

This is an example of an asynchronous action in Google SecOps.

The action won't finish execution until the timeout is reached or the cases have a tag specified in the `Case Tag To Wait For` parameter.

This action doesn't run on Google SecOps entities. 

**Note:** This is an asynchronous action.

#### Action inputs

The **Async** action requires the following parameters:

Parameter | Description  
---|---  
`Case IDs` | Optional. A comma-separated list of cases to handle. If nothing is provided, the action uses the case ID from which the action was executed.  
`Case Tag To Wait For` | Required. The action waits for cases to be tagged with this value before it finishes execution.  
  
#### Action outputs

The **Async** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Async** action:
    
    
    [{
       "case_id": "123",
       "tags": ["Async"]
    }, {
       "case_id": "123",
       "tags": ["Async"]
    },]
    

##### Output messages

The **Async** action can return the following output messages:

Output message | Message description  
---|---  
`The following cases have tag TAG: CASE_ID` | The action succeeded.  
`Error executing action "Async Action Example". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Async** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Sample Integration - Simple Connector Example

Use the **Sample Integration - Simple Connector Example** to retrieve currency rates and other data from the `api.vatcomply.com` service.

To work with a dynamic list, use the `alert_type` parameter.

#### Connector inputs

The **Google Threat Intelligence - DTM Alerts Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required. The name of the field that determines the event name (subtype). The default value is `event_type`.  
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`API Root` | Required. The API root for the integration instance. In this example case, [VAT Comply](https://www.vatcomply.com/) service is being used to integrate, with the API root `api.vatcomply.com`. The default value is `http://api.vatcomply.com`.  
`Password Field` | Optional. An example API password field. This parameter is included for demonstration purposes only and is not required by the API for authentication. The default value is `Google SecOps`.  
`Currencies To Fetch` | Optional. The currency exchange rates to retrieve. The default value is `USD, EUR`.  
`Create Alert Per Exchange Rate` | Optional. If enabled, the connector creates a separate alert for each exchange rate.  
`Alert Severity` | Optional. The severity level of the alert. The possible values are:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Informational`

The default value is `Informational`.  
`Add Attachment` | Optional. If enabled, the connector adds a JSON object to the alert. The default value is `True`.  
`Max Days Backwards` | Required. The number of days back from which to retrieve alerts. The maximum value is `30`. The default value is `1`.  
`Max Alerts To Fetch` | Required. The number of alerts to process in every connector iteration. The default value is `3`.  
`Use dynamic list as a blocklist` | Required. If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Disable Overflow` | Optional. If selected, the connector ignores the Google SecOps overflow mechanism. Selected by default.  
`Verify SSL` | Required. If selected, the action validates the SSL certificate of the API server. Selected by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
  
## Jobs

The sample integration allows the use of the following job:

  * Simple Job Example



### Simple Job Example

Use the **Simple Job Example** job to automatically manage cases.

This job has two primary functions: 

  * Close a case if it has a `Closed` tag.

  * Add a comment to a case if it has a `Currency` tag.




#### Job inputs

To configure this job, use the following parameters:

Parameters  
---  
`API Root` | Required. The API root for the integration instance. In this example case, [VAT Comply](https://www.vatcomply.com/) service is being used to integrate, with the API root `api.vatcomply.com`. The default value is `http://api.vatcomply.com`.  
`Password Field` | Optional. An example API password field. This parameter is included for demonstration purposes only and is not required by the API for authentication. The default value is `Google SecOps`.  
`Verify SSL` | Required. If selected, the action validates the SSL certificate of the API server. Selected by default.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
