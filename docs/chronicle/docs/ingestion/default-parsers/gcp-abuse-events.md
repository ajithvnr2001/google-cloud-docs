---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-abuse-events/
title: Collect Google Cloud Abuse Events logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:30.283543+00:00
---

# Collect Google Cloud Abuse Events logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-abuse-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Google Cloud Abuse Events logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect Google Cloud Abuse Events logs by enabling Google Cloud telemetry ingestion to Google SecOps and how log fields of Google Cloud Abuse Events logs map to Google SecOps Unified Data Model (UDM) fields.

For more information, see [Data ingestion to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

The deployment contains the following components:

  * **Google Cloud** : The Google Cloud services and products from which you collect logs.

  * **Google Cloud Abuse Events logs** : The Google Cloud Abuse Events logs that are enabled for ingestion to Google SecOps.

  * **Google SecOps** : Google SecOps retains and analyzes the logs from Google Cloud Abuse Events.




An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `GCP_ABUSE_EVENTS` ingestion label.

## Before you begin

Make sure all systems in the deployment architecture are configured in the UTC time zone.

### Configure Google Cloud to ingest Google Cloud Abuse Events logs

To ingest Google Cloud Abuse Events logs to Google SecOps, follow the steps in [Ingest Google Cloud logs to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#option_1_native_ingestion).

A typical deployment consists of Google Cloud Abuse Events logs enabled for ingestion to Google SecOps. Each customer deployment might differ from this representation and might be more complex.

If you encounter issues when you ingest Google Cloud Abuse Events logs, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support).

### Supported Google Cloud Abuse Events log format and sample

The Google Cloud Abuse Events parser supports logs in JSON format. The following is an example:
    
    
        {
            "insertId": "dummy-insert-id",
            "jsonPayload": {
                "action": "NOTIFY",
                "@type": "type.googleapis.com/google.cloud.abuseevent.logging.v1.AbuseEvent",
                "cryptoMiningEvent": {
                    "detectedMiningEndTime": "2048-03-18T07: 10: 00Z",
                    "detectedMiningStartTime": "2016-07-10T05: 24: 00Z",
                    "vmIp": [
                        "dummy.ip.address.1",
                        "dummy.ip.address.2",
                        "dummy.ip.address.3"
                    ],
                    "vmResource": [
                        "projects/dummy-project-id/zones/dummy-zone/instances/dummy-instance-id"
                    ]
                },
                "detectionType": "CRYPTO_MINING",
                "reason": "The monitored resource is mining cryptocurrencies",
                "remediationLink": "https://dummy-remediation-link"
            },
            "resource": {
                "type": "abuseevent.googleapis.com/Location",
                "labels": {
                    "location": "global",
                    "resource_container": "projects/dummy-resource-container-id"
                }
            },
            "timestamp": "2025-07-10T17:31:53.966189618Z",
            "severity": "NOTICE",
            "labels": {
                "abuseevent.googleapis.com/vm_resource": "projects/dummy-project-id/zones/dummy-zone/instances/dummy-instance-id"
            },
            "logName": "projects/dummy-project-id/logs/abuseevent.googleapis.com%2Fabuse_events",
            "receiveTimestamp": "2025-07-10T17:31:54.754890208Z"
        }
    
    

### Field mapping reference

### Field mapping reference: GCP_ABUSE_EVENTS

The following table lists the log fields and their corresponding UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `SCAN_UNCATEGORIZED`.  
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `Google Cloud Platform`.  
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `GCP Abuse Events`.  
`insertId` | `metadata.product_log_id` |   
`resource.type` | `target.resource.resource_subtype` |   
`resource.labels.location` | `target.location.name` |   
`timestamp` | `metadata.event_timestamp` |   
`` | `security_result.severity` | If the `severity` log field value is equal to `CRITICAL` then, the `security_result.severity` UDM field is set to `CRITICAL`.   
Else, if `severity` log field value is equal to `ERROR` then, the `security_result.severity` UDM field is set to `ERROR`.   
Else, if `severity` log field value contain one of the following values

  * `ALERT`
  * `EMERGENCY`

then, the `security_result.severity` UDM field is set to `HIGH`.   
Else, if `severity` log field value contain one of the following values

  * `INFO`
  * `NOTICE`

then, the `security_result.severity` UDM field is set to `INFORMATIONAL`.   
Else, if `severity` log field value is equal to `DEBUG` then, the `security_result.severity` UDM field is set to `LOW`.   
Else, if `severity` log field value is equal to `WARNING` then, the `security_result.severity` UDM field is set to `MEDIUM`.   
Else, the `security_result.severity` UDM field is set to `UNKNOWN_SEVERITY`.  
  
`severity` | `security_result.severity_details` |   
`logName` | `metadata.url_back_to_product` |   
`receiveTimestamp` | `metadata.collected_timestamp` |   
`jsonPayload.detectionType` | `security_result.category_details` |   
`` | `security_result.category` | If the `security_result.category_mapping` log field value is equal to `DETECTION_TYPE_UNSPECIFIED` then, the `security_result.category` UDM field is set to `UNKNOWN_CATEGORY`.   
Else, if `security_result.category_mapping `log field value is equal to `CRYPTO_MINING` then, the `security_result.category` UDM field is set to `EXPLOIT`.   
Else, if `security_result.category_mapping `log field value is equal to `LEAKED_CREDENTIALS` then, the `security_result.category` UDM field is set to `PHISHING`.   
Else, if `security_result.category_mapping `log field value is equal to `PHISHING` then, the `security_result.category` UDM field is set to `PHISHING`.   
Else, if `security_result.category_mapping `log field value is equal to `MALWARE` then, the `security_result.category` UDM field is set to `SOFTWARE_MALICIOUS`.   
Else, if `security_result.category_mapping `log field value is equal to `NO_ABUSE` then, the `security_result.category` UDM field is set to `POLICY_VIOLATION`.  
  
`jsonPayload.reason` | `security_result.description` |   
`` | `security_result.action` | If the `jsonPayload.action` log field value is equal to `ACTION_TYPE_UNSPECIFIED` then, the `security_result.action` UDM field is set to `UNKNOWN_ACTION`.   
Else, if the `jsonPayload.action` log field value is equal to `NOTIFY` then, the `security_result.action` UDM field is set to `ALLOW`.   
Else, if the `jsonPayload.action` log field value is equal to `PROJECT_SUSPENSION` then, the `security_result.action` UDM field is set to `BLOCK`.   
Else, if the `jsonPayload.action` log field value is equal to `REINSTATE` then, the `security_result.action` UDM field is set to `ALLOW`.   
Else, if the `jsonPayload.action` log field value is equal to `WARN` then, the `security_result.action` UDM field is set to `ALLOW`.   
Else, if the `jsonPayload.action` log field value is equal to `RESOURCE_SUSPENSION` then, the `security_result.action` UDM field is set to `BLOCK`.  
  
`labels.abuseevent.googleapis.com/vm_resource` | `principal.resource.name` |   
`` | `principal.resource.resource_type` | If the `event_type.crypto_mining_event.vm_resource` log field value is _not_ empty then, the `target.resource.resource_type` UDM field is set to `VIRTUAL_MACHINE`.  
`jsonPayload.cryptoMiningEvent.detectedMiningStartTime` | `security_result.detection_fields[detected_mining_start_time]` |   
`jsonPayload.cryptoMiningEvent.detectedMiningEndTime` | `security_result.detection_fields[detected_mining_end_time]` |   
`jsonPayload.cryptoMiningEvent.vmIp` | `principal.ip` |   
`jsonPayload.leaked_credential_event.credential_type.service_account_credential.service_account.service_account` | `principal.user.userid` |   
`jsonPayload.leaked_credential_event.credential_type.service_account_credential.service_account.key_id` | `principal.user.attribute.labels[service_account_key_id]` |   
`jsonPayload.leakedCredentialEvent.apiKeyCredential.apiKey` | `principal.user.attribute.labels[api_key_credential_api_key]` |   
`jsonPayload.leakedCredentialEvent.detectedUri` | `security_result.about.url` |   
`jsonPayload.harmfulContentEvent.uri` | `security_result.detection_fields[harmful_content_event_uri]` |   
`jsonPayload.remediationLink` | `security_result.detection_fields[remediation_link]` |   
`jsonPayload.@type` | `security_result.detection_fields[jsonPayload_type]` |   
`resource.labels.resource_container` | `principal.resource.attribute.labels[resource_container]` |   
  
## What's next

  * [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow)



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-abuse-events-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
