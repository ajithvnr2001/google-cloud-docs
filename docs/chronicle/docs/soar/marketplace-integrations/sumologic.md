---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sumologic/
title: Sumo Logic \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:49.135104+00:00
---

# Sumo Logic  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sumologic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sumo Logic

This document provides guidance on how to integrate Sumo Logic with Google SecOps.

## Configure Sumo Logic integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Ping

#### Description

Test connectivity to Sumo Logic.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    N/A
    

### Search

#### Description

Run a query and get the search results from Sumo Logic.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Query | String | N/A | Sumo Logic query to run. Example: _collector=*  
Delete Search Job | Checkbox | Un-Checked | If checked, delete the jobs after a search is completed.  
Since | String | N/A | Start date of the search, ISO-8601 or unixtime. Example: 1970-01-01T00:00:00. Default: 1 (unixtime).  
To | String | N/A | End date of the search, ISO-8601 or unixtime. Example: 1970-01-01T00:00:00. Default: now (current utc unixtime).  
Limit | String | N/A | Number of results to return. Example: 10. Default: 25.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
results | N/A | N/A  
  
##### JSON Result
    
    
    [
    {
    "_messageid": "-9223372036854773772",
    "_messagetime": "1359407049529",
    "_blockid": "-9223372036854775674",
    "_sourcecategory": "service",
    "_format": "plain:atp:o:0:l:29:p:yyyy-MM-dd HH:mm:ss,SSS ZZZZ",
    "_sourcename": "/Users/christian/Development/sumo/ops/assemblies/latest/service-20.1-SNAPSHOT/logs/service.log",
    "_source": "service",
    "_receipttime": "1359407051885",
    "_collectorid": "1579",
    "_sourceid": "1640",
    "_raw": "2013-01-28 13:04:09,529 -0800 INFO
    [module=SERVICE]
    [logger=com.netflix.config.sources.DynamoDbConfigurationSource] [thread=pollingConfigurationSource] Successfully polled Dynamo for a new configuration based on table:raychaser-chiapetProperties",
    "_size": "246",
    "_collector": "local",
    "_messagecount": "2035",
    "_sourcehost": "Chiapet.local"
    }
    ]
    

## Connectors

### Sumo Logic Connector

#### Description

Sumo Logic Connector.

#### Configure Sumo Logic Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter | Type | Default Value | Description  
---|---|---|---  
DeviceProductField | String | device_product | The field name used to determine the device product. Example: _type  
EventClassId | String | name | The field name used to determine the event name (sub-type). Example: _source_match_event_id  
PythonProcessTimeout | String | 60 | The timeout limit (in seconds) for the python process running current script.  
API Root | String | null | The Sumo Logic Api root, for example: https://api.{region}.sumologic.com  
Access ID | String | null | Sumo Logic access ID.  
Access Key | Password | null | Sumo Logic access key.  
Verify SSL | Checkbox | FALSE | Whether to use ssl on connection or not.  
Alert Name Field | String | null | The name of the field where the alert name is located (flat field path). Example: _sourcecategory  
Timestamp Field | String | null | The name of the field where the timestamp is located (flat field path). Example: _receipttime  
Environment Field | String | null | The name of the field where the environment is located (flat field path). Example: _collector  
Indexes | String | null | Indexes to get alerts in".  
Alerts Count Limit | Integer | 10 | Max count of alerts to pull in one cycle. Example: 20  
Max Days Backwards | Integer | 1 | Max number of days to fetch alerts since. Example: 3  
Proxy Server Address | String | null | The address of the proxy server to use.  
Proxy Username | String | null | The proxy username to authenticate with.  
Proxy Password | Password | null | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

##### Dynamic/whitelist rule support

This will run a single search job for each query added as a rule. If both were supplied: indexes and queries, queries have priority over the connector's 'indexes' parameter.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
