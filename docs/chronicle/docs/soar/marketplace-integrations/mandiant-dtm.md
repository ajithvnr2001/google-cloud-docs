---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-dtm/
title: Integrate Mandiant Digital Threat Monitoring with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:26.362501+00:00
---

# Integrate Mandiant Digital Threat Monitoring with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-dtm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Mandiant Digital Threat Monitoring with Google SecOps

This document provides guidance on how to integrate Mandiant Digital Threat Monitoring with Google Security Operations (Google SecOps).

**Note:** We recommended using the **Google Threat Intelligence** integration as it provides more capabilities and features.

## Use cases

The **Mandiant Digital Threat Monitoring** integration uses Google SecOps capabilities to support the following use cases:

  * **Ingest alerts** : Pull and manage external threat alerts directly in Google SecOps.

  * **Monitor compromised credentials** : Track leaked account information and domain discoveries identified by Mandiant.

  * **Update alert status** : Synchronize alert remediation by updating DTM alert statuses from the platform.

  * **Verify connectivity** : Test the integration connection to the Mandiant DTM server.




## Before you begin

This integration provides native platform capabilities and doesn't require external third-party API keys or credentials for authentication. Before you begin, ensure the integration is installed from the Content Hub within your Google SecOps instance.

## Integration parameters

The Mandiant Digital Threat Monitoring integration requires the following parameters:

Parameters | Description  
---|---  
`API Root` | _Required_ The API root of the Mandiant instance. The default value is `https://api.intelligence.mandiant.com`. To authenticate with Google Threat Intelligence credentials, enter the following value: `https://www.virustotal.com`.  
`Client ID` | _Optional_ The client ID of the Mandiant Digital Threat Monitoring account.  
`Client Secret` | _Optional_ The client secret of the Mandiant Digital Threat Monitoring account.  
`GTI API Key` | _Optional_ The API key of Google Threat Intelligence.To authenticate using Google Threat Intelligence, set the `API Root` parameter value to `https://www.virustotal.com`. Authenticating using the Google Threat Intelligence API key has a priority over other authentication methods.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for the connection to the Mandiant server is valid. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test connectivity to the Mandiant Digital Threat Monitoring server.

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
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Mandiant DTM server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Mandiant DTM server! Error is: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Alert

Use the **Update Alert** action to update an alert in Mandiant Digital Threat Monitoring.

#### Action inputs

The **Update Alert** action requires the following parameters:

Parameters | Description  
---|---  
`Alert ID` | _Required_ The ID of the alert to update.  
`Status` | _Optional_ The alert status.Possible values are as follows:

  * `New`
  * `Read`
  * `Resolved`
  * `Escalated`
  * `In Progress`
  * `No Action Required`
  * `Duplicate`
  * `Not Relevant`
  * `Tracked Externally`

  
  
#### Action outputs

The **Update Alert** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Update Alert** action:
    
    
    {
       "id": "ID",
       "monitor_id": "MONITOR_ID",
       "topic_matches": [
           {
               "topic_id": "4a6ffb0f-e90d-46ce-b10a-3a1e24fbe70d",
               "value": "ap-southeast-1.example.com",
               "term": "lwd",
               "offsets": [
                   26,
                   29
               ]
           },
           {
               "topic_id": "doc_type:domain_discovery",
               "value": "domain_discovery"
           }
       ],
       "label_matches": [],
       "doc_matches": [],
       "tags": [],
       "created_at": "2024-05-31T12:27:43.475Z",
       "updated_at": "2024-05-31T12:43:20.399Z",
       "labels_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/ID/labels",
       "topics_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/ID/topics",
       "doc_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/ID",
       "status": "closed",
       "alert_type": "Domain Discovery",
       "alert_summary": "See alert content for details",
       "title": "Suspicious domain \"ap-southeast-1.example.com\" similar to \"lwd\"",
       "email_sent_at": "",
       "severity": "medium",
       "confidence": 0.5,
       "has_analysis": false,
       "monitor_version": 2
    }
    

##### Output messages

The **Update Alert** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated alert with ID  INCIDENT_ID in Mandiant DTM.` | Action succeeded.  
`Error executing action "Update Alert". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Alert** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Mandiant DTM – Alerts Connector

Use the **Mandiant DTM – Alerts Connector** to pull alerts from Mandiant Digital Threat Monitoring. To work with a dynamic list, use the `alert_type` parameter.

The **Mandiant DTM – Alerts Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `Product Name`.  
`Event Field Name` | _Required_ The name of the field used to determine the event name (subtype).The default value is `event_type`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to the default value.The default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`Script Timeout` | _Required_ The timeout limit in seconds for the Python process running the current script.The default value is 180.  
`API Root` | _Required_ The API root of the Mandiant instance. The default value is `https://api.intelligence.mandiant.com`. To authenticate with Google Threat Intelligence credentials, enter the following value: `https://www.virustotal.com`.  
`Client ID` | _Optional_ The client ID of the Mandiant Digital Threat Monitoring account.  
`Client Secret` | _Optional_ The client secret of the Mandiant Digital Threat Monitoring account.  
`GTI API Key` | _Optional_ The API key of Google Threat Intelligence.To authenticate using Google Threat Intelligence, set the `API Root` parameter value to `https://www.virustotal.com`. When you authenticate using the Google Threat Intelligence API key, it takes priority over other authentication methods.  
`Lowest Severity To Fetch` | _Optional_ The lowest severity score of the alerts to retrieve. If you don't configure this parameter, the connector ingests alerts with all severities. The parameter accepts the following severity values:

  * `Low`
  * `Medium`
  * `High`

  
`Monitor ID Filter` | _Optional_ A comma-separated list of monitor IDs to retrieve the alerts from.  
`Max Hours Backwards` | _Required_ The number of hours previously from when to fetch alerts. The default value is 1 hour.  
`Max Alerts To Fetch` | _Required_ The number of alerts to process for every connector iteration. The default value is 25.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the overflow mechanism.Not selected by default.  
`Use dynamic list as a blocklist` | _Required_ If selected, the integration uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | _Required_ If selected, verifies that the SSL certificate for the connection to the Mandiant server is valid. Selected by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

#### Connector events

There are two types of events for the **Mandiant DTM – Alerts Connector** : an event that is based on the main alert and an event that is based on a topic.

An example of the connector event based on the main alert is as follows:
    
    
    {
       "id": "ID",
       "event_type": "Main Alert",
       "monitor_id": "MONITOR_ID",
       "doc": {
           "__id": "6ed37932-b74e-4253-aa69-3eb4b00d0ea2",
           "__type": "account_discovery",
           "ingested": "2024-05-20T16:15:53Z",
           "service_account": {
               "login": "user@example.com",
               "password": {
                   "plain_text": "********"
               },
               "profile": {
                   "contact": {
                       "email": "user@example.com",
                       "email_domain": "example.com"
                   }
               },
               "service": {
                   "inet_location": {
                       "domain": "www.example-service.com",
                       "path": "/signin/app",
                       "protocol": "https",
                       "url": "https://www.example-service.com/signin/app"
                   },
                   "name": "www.example-service.com"
               }
           },
           "source": "ccmp",
           "source_file": {
               "filename": "[1.145.094.680] urlloginpass ap.txt",
               "hashes": {
                   "md5": "c401baa01fbe311753b26334b559d945",
                   "sha1": "bf700f18b6ab562afb6128b42a34ae088f9c7434",
                   "sha256": "5e6302d95a7e7edb28d68926cede0c44babded720ad1cc9a72c12d8c6d66153f"
               },
               "size": 84161521407
           },
           "source_url": "https://cymbalgroup.com",
           "timestamp": "2023-11-14T20:09:04Z"
       },
       "labels": "Label",
       "topic_matches": [
           {
               "topic_id": "doc_type:account_discovery",
               "value": "account_discovery"
           }
       ],
       "label_matches": [],
       "doc_matches": [
           {
               "match_path": "service_account.profile.contact.email_domain",
               "locations": [
                   {
                       "offsets": [
                           0,
                           9
                       ],
                       "value": "example.com"
                   }
               ]
           }
       ],
       "tags": [],
       "created_at": "2024-05-20T16:16:52.439Z",
       "updated_at": "2024-05-30T12:10:56.691Z",
       "labels_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/account_discovery/ID/labels",
       "topics_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/account_discovery/ID/topics",
       "doc_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/account_discovery/ID",
       "status": "read",
       "alert_type": "Compromised Credentials",
       "alert_summary": "ccmp",
       "title": "Leaked Credentials found for domain \"example.com\"",
       "email_sent_at": "",
       "indicator_mscore": 60,
       "severity": "high",
       "confidence": 0.9999995147741939,
       "aggregated_under_id": "ID",
       "monitor_name": "Compromised Credentials - Example",
       "has_analysis": false,
       "meets_password_policy": "policy_unset",
       "monitor_version": 1
    }
    

An example of the connector event based on a topic is as follows:
    
    
    {
       "id": "ID",
       "event_type": "location_name",
       "location_name": "LOCATION_NAME",
       "timestamp": "2024-05-25T10:56:17.201Z",
       "type": "location_name",
       "value": "LOCATION_NAME",
       "extractor": "analysis-pipeline.nerprocessor-nerenglish-gpu",
       "extractor_version": "4-0-2",
       "confidence": 100,
       "entity_locations": [
           {
               "element_path": "body",
               "offsets": [
                   227,
                   229
               ]
           }
       ]
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
