---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/setup-log-based-alerts/
title: Configure log-based alerts \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:05.970613+00:00
---

# Configure log-based alerts  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/setup-log-based-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Configure log-based alerts Stay organized with collections  Save and categorize content based on your preferences. 

You can use log-based alerts to notify you when Network Analyzer detects specific insights. Examples for Network Analyzer insights include the following:

  * View all the insights on GKE cluster-related issues
  * View all high priority insights
  * View all load balancer firewall health check issues
  * View all insights in the region `us-central1`



Network Analyzer logs are part of the Google Cloud platform logs. The log names are in the following format:
    
    
    projects/{project-id}/logs/networkanalyzer.googleapis.com%2Fanalyzer_reports
    

You can find the log ID, monitored resource, and the payload proto details in the [Network Analyzer logs API](https://docs.cloud.google.com/logging/docs/api/platform-logs#network_analyzer). By default, the logs are routed to the [default log bucket](https://docs.cloud.google.com/logging/docs/routing/overview#default-bucket).

To get details about supported Cloud Logging insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

## Create log queries

You can use the Logging query language to query and filter Cloud Logging data. For more information, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language). Following are some examples of log queries for specific Network Analyzer insights:

  * **Example:** The following query returns the insights on all GKE cluster-related issues:
        
        LOG_ID("networkanalyzer.googleapis.com%2Fanalyzer_reports")
        jsonPayload.resourceName=~"^//container.googleapis.com/projects/.+/clusters/"
        

  * **Example:** The following query returns all **high priority** insights:
        
        LOG_ID("networkanalyzer.googleapis.com%2Fanalyzer_reports")
        jsonPayload.priority="HIGH"
        

  * **Example:** The following query returns all insights that belong to either of the two specific **Load Balancer Health Check** insight types:
        
        (jsonPayload.causeCode="LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_RANGE_BLOCKED" OR
        jsonPayload.causeCode="LOAD_BALANCER_HEALTH_CHECK_FIREWALL_HEALTH_CHECK_FIREWALL_NOT_CONFIGURED"
        )
        

  * **Example:** The following query returns all insights with location `us-central1`:
        
        LOG_ID("networkanalyzer.googleapis.com%2Fanalyzer_reports")
        jsonPayload.location="us-central1"
        

  * **Example:** The following query returns all insights that belong to the hybrid connectivity category:
        
        LOG_ID("networkanalyzer.googleapis.com%2Fanalyzer_reports")
        jsonPayload.reportGroups="HYBRID_CONNECTIVITY"
        




## Set up log-based alerts

You can use the log queries to set up log-based alerts to notify you when the matching insights are discovered by Network Analyzer. You can create log-based alerts from the [Logs Explorer](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition) in the Google Cloud console or by using the [Cloud Monitoring API](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api).

## Configure log-based alerts for organizations, folders, and metrics scopes

To route logs from multiple projects to a single destination project, see [Create a sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#creating-sink). You can then configure alerts in the destination project.

## Export logs to a third-party platform

You can configure a customized log sink to export logs to Cloud Storage, BigQuery, Pub/Sub, and third-party platforms. For more information, see [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## Enable or disable logging

To enable the Cloud Logging API, see [Enable the Logging API](https://docs.cloud.google.com/logging/docs/api/enable-api). To access the logs data in the [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest), the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), and the [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging), you must grant the required Identity and Access Management (IAM) roles and permissions. For more information, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

To disable Network Analyzer logs for a project, you can configure an [exclusion filter](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) to filter out Network Analyzer logs for the project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
