---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/apache-kafka/
title: Integrate Apache Kafka with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:27:22.230703+00:00
---

# Integrate Apache Kafka with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/apache-kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Apache Kafka with Google SecOps 

This document explains how to integrate Apache Kafka with Google Security Operations (Google SecOps).

**Note:** All testing for version one of this integration was performed and validated using Apache Kafka version 4.0.0.

## Use cases

The Apache Kafka integration can address the following use cases:

  * **Real-time security log ingestion** : Automatically ingest and process security events from Kafka topics into Google SecOps. This allows for centralized log management and real-time analysis to generate alerts based on streaming data.

  * **Event-driven automation** : Trigger automated playbooks in Google SecOps based on specific security events or messages streamed from a Kafka topic. This accelerates the response to critical events like a user login from an unusual location.

  * **Threat intelligence enrichment** : Pull custom threat intelligence feeds from Kafka topics to enrich existing alerts and cases. This provides analysts with up-to-date context on Indicators of Compromise (IOCs) and improves the accuracy of threat analysis.




## Before you begin

Before you configure the Apache Kafka integration in Google SecOps, complete the following prerequisites:

  * **Apache Kafka server** : Ensure you have access to a running Apache Kafka server with the necessary Kafka brokers and topics configured.
  * **Remote agent Docker image** : When creating remote agents, you must use a Debian-based image. Use the following image to ensure compatibility:
        
        us-docker.pkg.dev/siem-ar-public/images/agent-debian:latest
        




## Integration parameters

The **Apache Kafka** integration requires the following parameters:

Parameter | Description  
---|---  
`Kafka brokers` | Required. A comma-separated list of Kafka brokers to connect to, in the format `hostname:port`.  
`Use TLS for connection` | Optional. If selected, the integration uses TLS encryption for authentication.  This parameter requires a Certificate Authority (CA) certificate. Not enabled by default.  
`Use SASL PLAIN with TLS for connection` | Optional. If selected, the integration uses the SASL PLAIN username and password mechanism for authentication. This option is only supported with TLS encryption, and requires both a SASL username and password and a CA certificate. Not enabled by default.  
`CA certificate of Kafka server` | Optional. The CA certificate used to verify the identity of the Kafka server. This parameter is required if SASL is enabled.  
`Client certificate` | Optional. The client's certificate for mutual TLS authentication with the Kafka server. This parameter is required if mutual TLS (mTLS) is enabled.  
`Client certificate key` | Optional. The private key that corresponds to the client's certificate, used for mutual TLS authentication. This parameter is required if mutual TLS (mTLS) is enabled.  
`Client certificate key password` | Optional. The password used to decrypt the client certificate's private key. This parameter is required if mutual TLS (mTLS) is enabled.  
`SASL PLAIN Username` | Optional. The username for SASL PLAIN authentication with Kafka brokers. This parameter is required if SASL is enabled.  
`SASL PLAIN Password` | Optional. The password for SASL PLAIN authentication with Kafka brokers. This parameter is required if SASL is enabled.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to to test the connectivity to Apache Kafka.

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
`Successfully connected to the Apache Kafka server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Apache Kafka server! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Apache Kafka - Messages Connector

Use the **Apache Kafka - Messages Connector** to retrieve messages from Apache Kafka.

The connector retrieves messages from a specified Kafka topic and can process them in different ways based on the message format. If a message is a valid JSON object, the connector extracts specific fields for alert creation and mapping. If the message is a plain string, it's ingested as the raw event data.

The connector handles severity mapping, alert name templating, and unique ID generation based on the parameters you provide.

#### JSON severity mapping

To map the alert severity, you need to specify which field the **Apache Kafka - Messages Connector** uses to get the value for severity in the `Severity Mapping JSON` parameter. The connector response can contain value types, such as `integer`, `float`, and `string`.

The **Apache Kafka - Messages Connector** reads the `integer` and `float` values and maps them according to the Google SecOps settings. The following table shows the mapping of the `integer` values to severity in Google SecOps:

Integer value | Mapped severity  
---|---  
`100` | `Critical`  
From `80` to `100` | `High`  
From `60` to `80` | `Medium`  
From `40` to `60` | `Low`  
Less than `40` | `Informational`  
  
If the response contains the `string` value, the **Pub/Sub – Messages Connector** requires additional configuration.

Initially, the default value appears as follows:
    
    
    {
        "Default": 60
    }
    

If the values that are required for mapping are located in the `event_severity` JSON key, the values can be as follows:

  * `"Malicious"`
  * `"Benign"`
  * `"Unknown"`



To parse the `event_severity` JSON key values and ensure that the JSON object has a correct format, configure the `Severity Mapping JSON` parameter as follows:
    
    
    {
        "event_severity": {
            "Malicious": 100,
            "Unknown": 60,
            "Benign": -1
        },
        "Default": 50
    }
    

The `"Default"` value is required.

In a case when there are multiple matches for the same JSON object, the **Apache Kafka - Messages Connector** prioritizes the first JSON object key.

To work with fields that contain `integer` or `float` values, configure the key and an empty string in the `Severity Mapping JSON` parameter:
    
    
    {
      "Default":"60",
      "integer_field": "",
      "float_field": ""
    }
    

#### Connector inputs

The **Apache Kafka - Messages Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required. The name of the field that determines the event name (subtype). The default value is `event_type`.  
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`Kafka brokers` | Required. A comma-separated list of Kafka brokers to connect to, in the format `hostname:port`.  
`Use TLS for connection` | Optional. If selected, the integration uses TLS encryption for authentication.  This parameter requires a CA certificate. Not enabled by default.  
`Use SASL PLAIN with TLS for connection` | Optional. If selected, the integration uses the SASL PLAIN username and password mechanism for authentication. This option requires a SASL username and password to be provided. It's only supported with TLS encryption, which requires a CA certificate. Not enabled by default.  
`CA certificate of Kafka server` | Optional. The CA certificate used to verify the identity of the Kafka server.  
`Client certificate` | Optional. The client's certificate for mutual TLS authentication with the Kafka server.  
`Client certificate key` | Optional. The private key that corresponds to the client's certificate, used for mutual TLS authentication.  
`Client certificate key password` | Optional. The password used to decrypt the client certificate's private key.  
`SASL PLAIN Username` | Optional. The username for SASL PLAIN authentication with Kafka brokers.  
`SASL PLAIN Password` | Optional. The password for SASL PLAIN authentication with Kafka brokers.  
`Topic` | Required. The Kafka topic from which incidents are retrieved.  
`Consumer Group ID` | Optional. The identifier of the consumer group used when retrieving incidents. If no value is provided, a unique ID is generated.  
`Partitions` | Optional. A CSV list of partitions from which to fetch messages.  
`Initial Offset` | Optional. Where the connector starts fetching messages from a Kafka partition. You can specify a positive integer to start at a particular offset, or use the values `earliest` or `latest` to start fetching from the beginning or end of the partition.  
`Poll Timeout` | Optional. A poll timeout to consume a message from Kafka, in seconds.  
`Case Name Template` | Optional. A template to define a custom case name. The connector adds a `custom_case_name` key to the event. You can use placeholders in the format FIELD_NAME, which are populated from the first event's string values. Example: `Phishing - EVENT_MAILBOX`.  
`Alert Name Template` | Required. A template to define the alert name. You can use placeholders in the format FIELD_NAME, which are populated from the first event's string values. Example: `Phishing - EVENT_MAILBOX`. If a value isn't provided or the template is invalid, the connector uses a default alert name.  
`Rule Generator Template` | Required. A template to define the rule generator. You can use placeholders in the format FIELD_NAME, which are populated from the first event's string values. Example: `Phishing - EVENT_MAILBOX`. If a value isn't provided or the template is invalid, the connector uses a default rule generator name.  
`Timestamp Field` | Required. The field name in the Kafka message that contains the Google SecOps alert timestamp.  If the timestamp isn't in Unix epoch format, its format must be defined in the `Timestamp Format` parameter.  
`Timestamp Format` | Optional. The format of the message timestamp, required for non-Unix epoch timestamps. Use standard Python `strftime` format codes. If the timestamp isn't in Unix epoch format and this parameter isn't configured, the connector fails.  
`Severity Mapping JSON` | Required. The JSON object used by the connector to extract and map the severity level from the message to the Google SecOps priority scale. The default value is `{"Default": "60"}`.  
`Unique ID Field` | Optional. The name of the field to use as a unique message identifier. If no value is provided, the connector generates and uses a SHA-256 hash of the message content as the message identifier.  
`Max Messages To Fetch` | Required. The maximum number of messages the connector processes for every iteration. The default value is `100`.  
`Disable Overflow` | Optional. If selected, the connector ignores the Google SecOps overflow mechanism. Enabled by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Apache Kafka server. Enabled by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

#### Connector alerts

The following table describes the mapping of Apache Kafka message fields to Google SecOps alert fields:

Siemplify Alert Field | Apache Kafka Message Field  
---|---  
`SourceSystemName` | Filled by the framework.  
`TicketId` | The value of the unique ID field or a SHA-256 hash of the message.  
`DisplayId` | `ApacheKafka_{unique id or hash}_{connector identifier}`  
`Name` | The value generated by the `Alert Name Template`.  
`Reason` | N/A  
`Description` | N/A  
`DeviceVendor` | Hardcoded: `Apache Kafka`  
`DeviceProduct` | Fallback value: `Message`  
`Priority` | Mapped from the `Severity Mapping JSON` parameter.  
`RuleGenerator` | The value generated by the `Rule Generator Template`.  
`SourceGroupingIdentifier` | N/A  
`StartTime` | Converted from the `Timestamp Field`.  
`EndTime` | Converted from the `Timestamp Field`.  
`Siemplify Alert - Extensions` | N/A  
`Siemplify Alert - Attachments` | N/A  
  
#### Connector events

The example of a connector event is as follows:
    
    
    {
      "notificationConfigName": "organizations/ORGANIZATION_ID/notificationConfigs/soar_connector_CONNECTOR_ID_toxic_notifications_config",
      "finding": {
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/global/firewalls/FIREWALL_ID",
        "state": "ACTIVE",
        "category": "OPEN_NETBIOS_PORT",
        "externalUri": "https://console.cloud.google.com/networking/firewalls/details/default-allow-rdp?project=PROJECT_ID",
        "sourceProperties": {
          "Recommendation": "Restrict the firewall rules at: https://console.cloud.google.com/networking/firewalls/details/default-allow-rdp?project=PROJECT_ID",
          "ExceptionInstructions": "Add the security mark \"allow_open_netbios_port\" to the asset with a value of \"true\" to prevent this finding from being activated again.",
          "Explanation": "Firewall rules that allow connections from all IP addresses on TCP ports 137-139 or UDP ports 137-139 may expose NetBIOS services to attackers.",
          "ScannerName": "FIREWALL_SCANNER",
          "ResourcePath": [
            "projects/PROJECT_ID/",
            "folders/FOLDER_ID_1/",
            "folders/FOLDER_ID_2/",
            "organizations/ORGANIZATION_ID/"
          ],
          "ExposedService": "NetBIOS",
          "OpenPorts": {
            "TCP": [
              137.0,
              138.0,
              139.0
            ],
            "UDP": [
              137.0,
              138.0,
              139.0
            ]
          },
          "compliance_standards": {
            "iso": [
              {
                "ids": [
                  "A.13.1.1"
                ]
              }
            ],
            "pci": [
              {
                "ids": [
                  "1.2.1"
                ]
              }
            ],
            "nist": [
              {
                "ids": [
                  "SC-7"
                ]
              }
            ]
          },
          "ReactivationCount": 4.0
        },
        "securityMarks": {
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks",
          "marks": {
            "USER_ID": "SECURITY_MARK"
          }
        },
        "eventTime": "2024-08-30T14:44:37.973090Z",
        "createTime": "2024-06-24T07:08:54.777Z",
        "propertyDataTypes": {
          "ResourcePath": {
            "listValues": {
              "propertyDataTypes": [
                {
                  "primitiveDataType": "STRING"
                }
              ]
            }
          },
          "ReactivationCount": {
            "primitiveDataType": "NUMBER"
          },
          "Explanation": {
            "primitiveDataType": "STRING"
          },
          "ExposedService": {
            "primitiveDataType": "STRING"
          },
          "ScannerName": {
            "primitiveDataType": "STRING"
          }
        }
      }
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
