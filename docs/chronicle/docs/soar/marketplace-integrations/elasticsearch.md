---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/elasticsearch/
title: Elasticsearch \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:28.288951+00:00
---

# Elasticsearch  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/elasticsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Elasticsearch

This document describes how to integrate Elasticsearch with Google Security Operations.

## Accessing Elasticsearch

Google Security Operations accesses Elasticsearch via RESTful API on TCP port 9200 by default. The Google SecOps server will need access to the relevant Elasticsearch nodes on TCP 9200 (default) or an alternate port if the default port was not used during Elasticsearch deployment.

## Configure Elasticsearch integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Configure Elasticsearch integration with a CA certificate

You can verify your connection with a CA certificate file if needed.

Before you start, ensure you have the following:

  * The CA certificate file
  * The latest Elasticsearch integration version



To configure the integration with a CA certificate, complete the following steps:

  1. Parse your CA certificate file into a Base64 String.
  2. Open the integration configuration parameters page.
  3. Insert the string in the **CA Certificate File** field.
  4. To test that the integration is successfully configured, select the **Verify SSL** checkbox and click **Test**.



### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Server Address | Sring | x.x.x.x | Yes | IP address of the Elasticsearch server.  
Username | String | N/A | Yes | The email address of the user which should be used to connect to Elasticsearch.  
Password | Password | N/A | Yes | The password of the according user.  
Authenticate | Checkbox | Unchecked | No | N/A  
Verify SSL | Checkbox | Unchecked | No | Use this checkbox, if your Elasticsearch connection requires an SSL verification.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Advanced ES Search

#### Description

An Elasticsearch test that is pre-made, and returns a word dictionary.

#### Parameters

Parameters | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Index | String | * | No | Search pattern for a Elasticsearch index.In Elasticsearch, index is like a DatabaseName, and data is stored across various indexes.This parameter defines in what index(es) to search. It can be an exact name ie: "smp_playbooks-2019.06.13" or you can use a wildcard to search by a pattern. e: "smp_playbooks-2019.06 _"or "smp_ ".To learn more about Elasticsearch indexes visit <https://www.elastic.co/blog/what-is-an-elasticsearch-index>  
Query | String | * | No | The search query to perform. It is in Lucene syntax.IE1: "*" (this is a wildcard that will return all record)IE2: "level:error"IE3: "level:information"IE4: "level:error OR level:warning"To learn more about Lucene syntax, visit <https://www.elastic.co/guide/en/kibana/current/lucene-query.html#lucene-query\r\nhttps://www.elastic.co/guide/en/elasticsearch/reference/7.1/query-dsl-query-string-query.html#query-string-syntax>  
Limit | String | 100 | No | Limits the document return count, ie: 10.0 = No limit.  
Display Field | String | * | No | Limits the returned fields. Default "*" = Return all fields.You can state a single field. ie: "level"  
Search Field | String | _all | No | Search field for free text queries (When query doesn't specify a field name).Default is "_all", which means all fields are searched. It is best to use proper Lucene syntax on "_all" fields, or textual search on a specific field.Ie1: Search Field = "_all". Query = "level:error" Query will return all records where "level" field, equals "error".Ie2: Search Field = "Message", query = "_Login Alarm_ ". Query will return all records, which their "Message" field, contains the text "Login Alarm"  
Timestamp Field | String | @timestamp | No | The name of the field to run time-based filtering against. Default is @timestamp. If both Earliest Date and Oldest Date are empty, no time-based filtering will occur.  
Oldest Date | String | now-1d | No | Start date of the search. Search will return only records equal or after this point in time.Input may be in exact UTC:Format: YYYY-MM-DDTHH:MM:SSZie: 2019-06-04T10:00:00ZInput may also be in relative form (using date-math): tie: "now", "now-1d", "now-1d/d", "now-2h/h"To learn more about date-math visit <https://www.elastic.co/guide/en/elasticsearch/reference/7.1/common-options.html#date-math>  
Earliest Date | String | now | No | End date of the search. Search will return only records equal or before this point in time.Input may be in exact UTC:Format: YYYY-MM-DDTHH:MM:SSZie: 2019-06-04T10:00:00ZInput may also be in relative form (using date-math):ie: "now", "now-1d", "now-1d/d", "now-2h/h"To learn more about date-math visit <https://www.elastic.co/guide/en/elasticsearch/reference/7.1/common-options.html#date-math>  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
results | N/A | N/A  
  
### DSL Search

#### Description

Searches through everything in Elasticsearch and returns back results in a dictionary format. This action supports only queries without time range, if you want to use time range in your query use Advanced ES Search action.

#### Parameters

Parameters | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Index | String | * | No | Search pattern for a Elasticsearch index.In Elasticsearch, index is like a DatabaseName, and data is stored across various indexes.This param defines in what index(es) to search. It can be an exact name ie: \"smp_playbooks-2019.06.13\"\r\nor you can use a (_) wildcard to search by a pattern. e: \"smp_playbooks-2019.06_ \" or \"smp*\".To learn more about Elasticsearch indexes visit <https://www.elastic.co/blog/what-is-an-elasticsearch-index>  
Query | String | * | No | The search query to perform. It is in Lucene syntax.IE1: \"*\" (this is a wildcard that will return all record)IE2: \"level:error\"IE3: \"level:information\"IE4: \"level:error OR level:warning\"To learn more about Lucene syntax, visit <https://www.elastic.co/guide/en/kibana/current/lucene-query.html#lucene-query\r\nhttps://www.elastic.co/guide/en/elasticsearch/reference/7.1/query-dsl-query-string-query.html#query-string-syntax>  
Limit | String | 100 | No | NoLimits the document return count, ie: 10.0 = No limit  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
results | N/A | N/A  
  
##### JSON Result
    
    
    [
        {
            "_score": 0.2876821,
            "_type": "person",
            "_id": "2",
            "_source": {
                "lastname": "Smith",
                "name": "John",
                "job_description": "Systems administrator"
            },
            "_index": "accounts"
        }, {
            "_score": 0.28582606,
            "_type": "person",
            "_id": "1",
            "_source":
            {
                "lastname": "Doe",
                "name": "John",
                "job_description": "Systems administrator and Linux specialist"
            },
            "_index": "accounts"
        }
    ]
    

### Ping

#### Description.

Test Verifies connectivity to the Elasticsearch server.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
### Simple ES Search

#### Description

Action searches through everything in Elasticsearch and returns back results in a dictionary format.

#### Parameters

Parameters | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Index | String | * | No | Search pattern for a Elasticsearch index.In Elasticsearch, index is like a DatabaseName, and data is stored across various indexes.This param defines in what index(es) to search. It can be an exact name ie: \"smp_playbooks-2019.06.13\" or you can use a (_) wildcard to search by a pattern. e: \"smp_playbooks-2019.06_ \" or \"smp*\".To learn more about Elasticsearch indexes visit <https://www.elastic.co/blog/what-is-an-elasticsearch-index>  
Query | String | * | No | The search query to perform. It is in Lucene syntax.IE1: \"*\" (this is a wildcard that will return all record)IE2: \"level:error\"IE3: \"level:information\"IE4: \"level:error OR level:warning\"To learn more about Lucene syntax, visit <https://www.elastic.co/guide/en/kibana/current/lucene-query.html#lucene-query\r\nhttps://www.elastic.co/guide/en/elasticsearch/reference/7.1/query-dsl-query-string-query.html#query-string-syntax>  
Limit | String | 100 | No | Limits the document return count, ie: 10.0 = No limit.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
results | N/A | N/A  
  
##### JSON Result
    
    
    [{
        "_score": 0.2876821,
        "_type": "person",
        "_id": "2",
        "_source":
            {
              "lastname": "Smith",
              "name": "John",
              "job_description": "Systems administrator"
             },
         "_index": "accounts"
     },
     {
         "_score": 0.28582606,
         "_type": "person",
         "_id": "1",
         "_source":
           {
             "lastname": "Doe",
             "name": "John",
             "job_description": "Systems administrator and Linux specialist"
           },
        "_index": "accounts"
      }
     ]
    

## Connectors

### Configure Elasticsearch connectors in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

To configure the selected connector use the connector-specific parameters listed in the following tables:

  * [Elasticsearch Connector configuration parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/elasticsearch#elasticsearch-connector-parameters)
  * [Elasticsearch DSL Connector configuration parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/elasticsearch#elasticsearch-dsl-connector-parameters)



### Elasticsearch Connector

#### Description

This topic shows how Google SecOps integrates Elasticsearch with the mechanism and configuration for ingesting and processing.

#### Elasticsearch alert forwarding to Google SecOps

Google SecOps will search specified Elasticsearch indexes with a provided query (using Lucene query syntax) and return Elasticsearch documents that will be translated and contextualized as "alerts" for cases.

#### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Default Environment | String | N/A | No | Select the required environment. For example, "Customer One".  
Run Every | Integer | 0:0:0:10 | No | Select the amount of time to run the connection. For example, "every day".  
Product Field Name | String | device_product | Yes | The field name used to determine the device product. Example: _type.  
Event Field Name | String | name | Yes | The field name used to determine the event name (sub-type). Example: _source_match_event_id.  
Script Timeout (Seconds) | String | 60 | Yes | The timeout limit (in seconds) for the python process running current script.  
Server Address | String | N/A | Yes | The Elasticsearch server address, for example: http://{ip_address}:{port}  
Username | String | N/A | Yes | Elasticsearch username.  
Password | Password | N/A | Yes | Elasticsearch password.  
Authenticate | Checkbox | Unchecked | Yes | Whether to authenticate on connection or not.  
Verify SSL | Checkbox | Unchecked | No | Whether to use ssl on connection or not.  
Alert Name Field | String | N/A | Yes | The name of the field where the alert name is located (flat field path). Example: _source_alert_info_alert  
Timestamp Field | String | N/A | Yes | The name of the field where the timestamp is located (flat field path). Example: _source_ @timestamp  
Environment Field | String | N/A | No | The name of the field where the environment is located (flat field path). Example: _source_environment  
Indexes | String | N/A | No | Index pattern to search by. Example: '*'  
Query | String | N/A | No | Search pattern query (Lucene query syntax). Example: '*'  
Alerts Count Limit | Integer | 20 | Yes | Max count of alerts to pull in one cycle. Example: 20  
Max Days Backwards | Integer | 1 | Yes | Max number of days to fetch alerts since. Example: 3.  
Severity Field Name | String | N/A | No | If you want to map severity based on the string value then you would need to create a mapping file. Please refer to documentation portal for more details.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic If the regex pattern is null or empty, or the environment value is null, the final environment result is "".  
CA Certificate File | String | N/A | No | CA Certificate File  
  
#### How to map severity in the connector

**Note:** If you introduce a new key in the Severity Field Name, it will overwrite the mapping file. You would need to configure it again.

In order to map severity you need to specify what field should be used to get value for severity in the "Severity Field Name" parameter. In the response you can get 3 types of values: integers, floats and strings. For integers and floats, you don't need to do any additional configuration. The connector will read those values and map them according to the Google SecOps standards. A quick reminder of how integer values are mapped:

  * 100 - Critical
  * 100 > x >= 80 High
  * 80 > x >=60 Medium
  * 60 > x >=40 Low
  * 40 > x Informational



If in the response, we are working with strings then additional configuration is required. In the folder, where connector scripts are located you will have a config file name `severity_map_config.json`. This file defines mapping rules for the severity.

Initially, the file will look like this:
    
    
    {
        "Default": 50
    }
    

Imagine a situation, where the needed values are located in the `event.severity`. `event.severity` can contain the following values: "Malicious", "Benign", "Unknown".

First, we have to specify in the "Severity Field Name" parameter that we will use `event.severity`.

Secondly, we have to update the config file.

After changes, this is how `severity_map_config.json` file should look like:
    
    
    {
        "event.severity": {
            "Malicious": 100,
            "Unknown": 60,
            "Benign": -1
        },
        "Default": 50
    }
    

Now, when the connector will get an event with `event.severity` = "Malicious" it will give it Critical severity.

#### Connector rules

##### Whitelist/Blacklist

The connector doesn't support Whitelist/Blacklist.

##### Proxy support

The connector supports proxy.

### Elasticsearch DSL Connector

#### Description

The connector works by making a REST API call with a DSL query.

#### Use cases and examples

Ability to use DSL queries as a search parameter in Elasticsearch.

#### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | device_product | Yes | Describes the name of the field where the product name is stored.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is "".  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic If the regex pattern is null or empty, or the environment value is null, the final environment result is "".  
Script Timeout (Seconds) | Integer | 60 | Yes | Timeout limit for the python process running the current script.  
Server Address | String | N/A | Yes | IP address of the Elasticsearch API server.  
Port | String | N/A | Yes | Port of Elasticsearch API server.  
Query | String | N/A | Yes | DSL Query that is used for the search. Valid JSON format needed. To make the connector more stable it is recommended to add a sorting timestamp key in the ascending order.  
Index | String | N/A | Yes | Index that is used for a search. For example: _all  
Timestamp Field | String | N/A | Yes | The name of the field where the timestamp is located. Example: _source_ @timestamp  
Alert Field Name | String | N/A | Yes | The name of the field where the alert name is located. Example: _source_info_alertname  
Description Field | String | N/A | No | The name of the field where the description is located. Example: _source_alert_info_description  
Severity | String | Medium | Yes | Severity of the alerts.  
Possible value: Info Low Medium High Critical  
Alerts Count Limit | Integer | 100 | No | Limit the number of alerts returned by the connector per 1 iteration.  
Authenticate | Checkbox | Unchecked | No | Whether to authenticate on a connection or not.  
Username | String | N/A | No | Elasticsearch account username.  
Password | Password | N/A | No | Elasticsearch account password.  
Use SSL | Checkbox | Unchecked | No | Option to enable SSL/TLS connection.  
Severity Field Name | String | N/A | No | If you want to map severity based on the string value then you would need to create a mapping file. Please refer to documentation portal for more details.  
Alert Severity | String | N/A | No | The severity of the alerts. Possible value: Info, Low, Medium, High, Critical. **Note:** this parameter has priority over "Severity Field Name". If you want to work with "Severity Field Name", this field should be left empty.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
**Supported Notations**

The connector supports three notations. For example, if you want use event.type in the "Event Field Name" parameter. In that case, you can either provide _source_event_type, event_type or event.type. All of these values will behave the same way.

For parameters:

  * Product Field Name
  * Event Field Name
  * Severity Field Name
  * Environment Field
  * Timestamp Field
  * Alert Name Field
  * Alert Description Field - this one is only for DSL connectors



#### How to map severity in the connector

**Note:** Note: if you introduce a new key in the Severity Field Name, it will overwrite the mapping file. You would need to configure it again.

In order to map severity you need to specify what field should be used to get value for severity in the "Severity Field Name" parameter. In the response you can get 3 types of values: integers, floats and strings. For integers and floats, you don't need to do any additional configuration. The connector will read those values and map them according to the Google SecOps standards. A quick reminder of how integer values are mapped:

  * 100 - Critical
  * 100 > x >= 80 High
  * 80 > x >=60 Medium
  * 60 > x >=40 Low
  * 40 > x Informational



If in the response, we are working with strings then additional configuration is required. In the folder, where connector scripts are located you will have a config file name `severity_map_config.json`. This file defines mapping rules for the severity.

Initially, the file will look like this:
    
    
    {
        "Default": 50
    }
    

Imagine a situation, where the needed values are located in the `event.severity`. `event.severity` can contain the following values: "Malicious", "Benign", "Unknown".

First, we have to specify in the "Severity Field Name" parameter that we will use `event.severity`.

Secondly, we have to update the config file.

After changes, this is how `severity_map_config.json` file should look like:
    
    
    {
        "event.severity": {
            "Malicious": 100,
            "Unknown": 60,
            "Benign": -1
        },
        "Default": 50
    }
    

Now, when the connector will get an event with `event.severity` = "Malicious" it will give it Critical severity.

#### Connector rules

##### Whitelist/Blacklist

The connector doesn't support Whitelist/Blacklist.

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
