---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/opensearch/
title: Integrate OpenSearch with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:37.473941+00:00
---

# Integrate OpenSearch with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/opensearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate OpenSearch with Google SecOps 

This document explains how to integrate OpenSearch with Google Security Operations. 

## Use cases

The **OpenSearch** integration addresses the following security orchestration and investigation use cases:

  * **Automated threat hunting** : Periodically search across all OpenSearch indexes for specific Indicators of Compromise (IoCs) or suspicious patterns using Lucene and DSL queries.

  * **Centralized alert ingestion** : Ingest documents from OpenSearch as actionable alerts into Google SecOps, ensuring that security events from your data lake are prioritized and investigated.

  * **Contextual data retrieval** : Enrich existing security cases by automatically pulling related logs or historical data from OpenSearch to provide analysts with deeper context during an investigation.

  * **Flexible data mapping** : Dynamically map severity levels and environment tags from OpenSearch documents to Google SecOps standards to maintain consistency across different log sources.




## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following:

  * **CA Certificate file** : A valid Certificate Authority file to secure the connection.

  * **Latest integration version** : Ensure you are using the most recent version of the OpenSearch integration.

  * **Base64-encoded certificate** : The content of your CA certificate file must be converted into a Base64 string before configuration.




To configure the integration with a CA certificate, complete the following steps:

  1. Open the integration configuration parameters page.
  2. Paste the Base64-encoded string into the **CA Certificate File** field.
  3. Select the **Verify SSL** checkbox.
  4. Click **Test** to verify that the integration is successfully configured.



## Integration parameters

The **OpenSearch** integration requires the following parameters:

Parameter | Description  
---|---  
`Server Address` | Required. The endpoint URL of the OpenSearch instance, including the protocol and port (for example, `https://10.0.0.1:9200`).  
`Username` | Optional. The username used to authenticate with the OpenSearch instance.  
`Password` | Optional. The password associated with the specified username.  
`API Token` | Optional. The API token used for authentication as an alternative to a username and password.  
`Authenticate` | Optional. If selected, the integration authenticates the connection to the OpenSearch server using the provided credentials.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the OpenSearch server.  
`CA Certificate File` | Optional. The content of the Certificate Authority (CA) certificate file in PEM format, used to verify the server's SSL certificate.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Advanced ES Search

Use the **Advanced ES Search** action to execute a pre-configured search query on the OpenSearch server and retrieve the results in a dictionary format.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Advanced ES Search** action requires the following parameters:

Parameter | Description  
---|---  
`Index` | Optional. The search pattern for the OpenSearch index (for example, `smp_playbooks-2019.06.13`). You can use wildcards to search multiple indexes (for example, `smp_playbooks-*`). The default value is `*`.  
`Query` | Optional. The search query to perform using Lucene syntax (for example, `level:error OR level:warning`). The default value is `*`.  
`Limit` | Optional. The maximum number of documents to return. Set this value to `0` for no limit. The default value is `100`.  
`Display Field` | Optional. A comma-separated list of specific fields to return. The default value is `*` and returns all fields.  
`Search Field` | Optional. The specific field to search when `Query` doesn't include a target field name. This acts as the default search target for free-text queries. The default value is `_all`, which searches across all indexed fields.  
`Timestamp Field` | Optional. The name of the field used for time-based filtering. If both `Earliest Date` and `Oldest Date` are empty, the action doesn't perform time-based filtering. The default value is `@timestamp`.  
`Oldest Date` | Optional. The start date for the search. The action returns records that occurred on or after this timestamp. You can provide an exact UTC timestamp (`YYYY-MM-DDTHH:MM:SSZ`) or relative date-math (for example, `now-1d`). The default value is `now-1d`.  
`Earliest Date` | Optional. The end date for the search. The action returns records that occurred on or before this timestamp. You can provide an exact UTC timestamp (`YYYY-MM-DDTHH:MM:SSZ`) or relative date-math (for example, `now`). The default value is `now`.  
  
#### Action outputs

The **Advanced ES Search** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Advanced ES Search** action:

Script result name | Value  
---|---  
`results` | `RESULTS`  
  
### DSL Search

Use the **DSL Search** action to perform a comprehensive search across all OpenSearch indexes and retrieve results in a dictionary format.

This action doesn't run on Google SecOps entities. 

**Note:** This action does not support time-range filtering. To perform a search with a specific time range, use the Advanced ES Search action.

#### Action inputs

The **DSL Search** action requires the following parameters:

Parameter | Description  
---|---  
`Index` | Optional. The search pattern for the OpenSearch index (for example, `smp_playbooks-2019.06.13`). You can use wildcards to search multiple indexes (for example, `smp_playbooks-*`). The default value is `*`.  
`Query` | Optional. The search query to perform using Lucene syntax (for example, `level:error OR level:warning`). The default value is `*`.  
`Limit` | Optional. The maximum number of documents to return. Set this value to `0` for no limit. The default value is `100`.  
  
#### Action outputs

The **DSL Search** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **DSL Search** action:
    
    
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
    

##### Script result

The following table lists the value for the script result output when using the **DSL Search** action:

Script result name | Value  
---|---  
`results` | `RESULTS`  
  
### Ping

Use the **Ping** action to test the connectivity to OpenSearch.

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
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
is_success | `true` or `false`  
  
### Simple ES Search

Use the **Simple ES Search** action to perform a basic search across all indexed fields in OpenSearch and retrieve the results in a dictionary format.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Simple ES Search** action requires the following parameters:

Parameter | Description  
---|---  
`Index` | Optional. The search pattern for the OpenSearch index (for example, `smp_playbooks-2019.06.13`). You can use wildcards to search multiple indexes (for example, `smp_playbooks-*`). The default value is `*`.  
`Query` | Optional. The search query to perform using Lucene syntax (for example, `level:error OR level:warning`). The default value is `*`.  
`Limit` | Optional. The maximum number of documents to return. Set this value to `0` for no limit. The default value is `100`.  
  
#### Action outputs

The **Simple ES Search** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Simple ES Search** action:
    
    
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
    

##### Script result

The following table lists the value for the script result output when using the **Simple ES Search** action:

Script result name | Value  
---|---  
`results` | `RESULTS`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### OpenSearch Connector

Use the **OpenSearch Connector** to search specified OpenSearch indexes with a provided Lucene query and ingest documents as alerts into Google SecOps.

**Note:** This connector supports proxy servers. It does not support whitelist or blocklist filtering.

#### Connector inputs

The **OpenSearch Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype). The default value is `name`.  
`Script Timeout (Seconds)` | Required.The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`Server Address` | Required. The endpoint URL of the OpenSearch instance, including the protocol and port (for example, `https://10.0.0.1:9200`).  
`Username` | Optional. The username used to authenticate with the OpenSearch instance.  
`Password` | Optional. The password associated with the specified username.  
`Authenticate` | Optional. If selected, the integration authenticates the connection to the OpenSearch server using the provided credentials.  
`API Token` | Optional. The API token used for authentication as an alternative to a username and password.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the OpenSearch server.  
`Alert Name Field` | Required. The name of the field that contains the alert name (for example, `_source_alert_info_alert`).  
`Timestamp Field` | Required. The name of the field that contains the timestamp (for example, `_source_@timestamp`).  
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Indexes` | Optional. The index pattern to search. Use `*` to search across all indexes.  
`Query` | Optional. The search query to perform using Lucene syntax.  
`Alerts Count Limit` | Required. The maximum number of alerts to pull in a single cycle. The default value is `20`.  
`Max Days Backwards` | Required. The number of days prior to now to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The default value is `1`.  
`Severity Field Name` | Optional. The field name used to extract the severity value for the alert. If the field contains numeric values (integers or floats), the connector automatically maps them to Google SecOps severity levels (for example, `100` is `Critical`). If the field contains string values, you must define the mapping rules in the `severity_map_config.json` file.  
`Proxy Server Address` | Optional. The address of the proxy server to use.  
`Proxy Username` | Optional. The username used to authenticate with the proxy server.  
`Proxy Password` | Optional. The password used to authenticate with the proxy server.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
  
### OpenSearch DSL Connector

Use the **OpenSearch DSL Connector** to ingest documents as alerts into Google SecOps by making REST API calls using Domain Specific Language (DSL) queries.

**Note:** This connector supports proxy servers. It does not support whitelist or blocklist filtering.

#### Connector inputs

The **OpenSearch DSL Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`. The default value is `device_product`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype). The default value is `name`.  
`Script Timeout (Seconds)` | Required.The timeout limit, in seconds, for the Python process that runs the current script. The default value is `60`.  
`Server Address` | Required. The endpoint URL of the OpenSearch instance, including the protocol (for example, `https://10.0.0.1`).  
`Port` | Required. The port used to connect to the OpenSearch API server.  
`Query` | Required. The DSL query used for the search in JSON format. To improve connector stability, it is recommended to include a sorting timestamp key in ascending order within your query.  
`Index` | Required. The index used for the search. Use `_all` to search across all indexes.  
`Timestamp Field` | Required. The name of the field that contains the timestamp (for example, `_source_@timestamp`).  
`Alert Field Name` | Required. The name of the field that contains the alert name (for example, `_source_info_alertname`).  
`Description Field` | Optional. The name of the field that contains the alert description (for example, `_source_alert_info_description`).  
`Severity` | Required. The static severity level to assign to all ingested alerts. This parameter is used if `Alert Severity` and `Severity Field Name` are empty. The default value is `Medium`.  
`Alert Severity` | Optional. The severity to assign to alerts. This parameter has priority over `Severity Field Name`. If you want to use dynamic mapping using the `Severity Field Name`, leave this field empty.  
`Severity Field Name` | Optional. The field name used to extract the severity value for the alert. If the field contains numeric values (integers or floats), the connector automatically maps them to Google SecOps severity levels (for example, `100` is `Critical`). If the field contains string values, you must define the mapping rules in the `severity_map_config.json` file.  
`Alerts Count Limit` | Optional. The maximum number of alerts to pull in a single cycle. The default value is `100`.  
`Authenticate` | Optional. If selected, the connector authenticates the connection using the provided credentials.  
`Username` | Optional. The username used to authenticate with the OpenSearch instance.  
`Password` | Optional. The password used to authenticate with the OpenSearch instance.  
`Use SSL` | Optional. If selected, the connector enables an SSL/TLS connection to the server.  
`Proxy Server Address` | Optional. The address of the proxy server to use for the connection.  
`Proxy Username` | Optional. The username used to authenticate with the proxy server.  
`Proxy Password` | Optional. The password used to authenticate with the proxy server.  
`Environment Field Name` | Optional.The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment. The default value is `.*`.  
  
#### Notation support

The connector supports three different notations for field mapping. For example, to map `event.type`, you can provide `_source_event_type`, `event_type`, or `event.type`.

This applies to the following parameters:

  * `Product Field Name`
  * `Event Field Name`
  * `Severity Field Name`
  * `Environment Field Name`
  * `Timestamp Field`
  * `Alert Field Name`
  * `Description Field` (DSL connector only)



#### How to map severity in the connector

If the `Severity Field Name` contains numeric values (integers or floats), the connector maps them as follows:

  * **Critical** : 100
  * **High** : 80 ≤ x < 100
  * **Medium** : 60 ≤ x < 80
  * **Low** : 40 ≤ x < 60
  * **Informational** : x < 40



For string values, you must update the `severity_map_config.json` file in the connector scripts folder.

##### Example configuration

To map an `event.severity` field containing "Malicious", "Unknown", or "Benign":

  1. Enter `event.severity` in the **Severity Field Name** parameter.
  2. Update `severity_map_config.json`:


    
    
    {
        "event.severity": {
            "Malicious": 100,
            "Unknown": 60,
            "Benign": -1
        },
        "Default": 50
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
