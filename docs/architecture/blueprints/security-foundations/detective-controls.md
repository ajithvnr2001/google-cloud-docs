---
url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls/
title: Detective controls \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:38.329253+00:00
---

# Detective controls  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Detective controls Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-15 UTC

Threat detection and monitoring capabilities are provided using a combination of built-in security controls from Security Command Center and custom solutions that let you detect and respond to security events.

## Centralized logging for security and audit

The blueprint configures logging capabilities to track and analyze changes to your Google Cloud resources with logs that are aggregated to a single project.

The following diagram shows how the blueprint aggregates logs from multiple sources in multiple projects into a centralized log sink.

![Logging structure for example.com.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-logging-structure.svg)

The diagram describes the following:

  * Log sinks are configured at the organization node to aggregate logs from all projects in the resource hierarchy.
  * Multiple log sinks are configured to send logs that match a filter to different destinations for storage and analytics.
  * The `prj-c-logging` project contains all the resources for log storage and analytics.
  * Optionally, you can configure additional tooling to export logs to a SIEM.



The blueprint uses different log sources and includes these logs in the log sink filter so that the logs can be exported to a centralized destination. The following table describes the log sources.

Log source | Description  
---|---  
[Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) | You cannot configure, disable, or exclude Admin Activity audit logs.  
[System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event) | You cannot configure, disable, or exclude System Event audit logs.  
[Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied) | You cannot configure or disable Policy Denied audit logs, but you can optionally exclude them with [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).  
[Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) | By default, the blueprint doesn't enable data access logs because the volume and cost of these logs can be high.To determine whether you should enable data access logs, evaluate where your workloads handle sensitive data and consider whether you have a requirement to enable data access logs for each service and environment working with sensitive data.  
[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) | The blueprint enables VPC Flow Logs for every subnet. The blueprint configures [log sampling](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling) to sample 50% of logs to reduce cost.If you create additional subnets, you must ensure that VPC Flow Logs are enabled for each subnet.  
[Firewall policy rules logging format](https://docs.cloud.google.com/firewall/docs/firewall-policy-log-format). | The blueprint enables Firewall Rules Logging for every firewall policy rule.If you create additional firewall policy rules for workloads, you must ensure that Firewall Rules Logging is enabled for each new rule.  
[Cloud DNS logging](https://docs.cloud.google.com/dns/docs/monitoring) | The blueprint enables Cloud DNS logs for managed zones.If you create additional managed zones, you must enable those DNS logs.  
[Google Workspace audit logging](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging) | Requires a one-time enablement step that is not automated by the blueprint. For more information, see [Share data with Google Cloud services](https://support.google.com/a/answer/9320190).  
[Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) | Requires a one-time enablement step that is not automated by the blueprint. For more information, see [Enable Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable).  
  
The following table describes the log sinks and how they are used with [supported destinations](https://docs.cloud.google.com/logging/docs/routing/overview#destinations) in the blueprint.

Sink | Destination | Purpose  
---|---|---  
`sk-c-logging-la` | [Logs routed to Cloud Logging buckets](https://docs.cloud.google.com/logging/docs/export/using_exported_logs) with [Log Analytics](https://docs.cloud.google.com/logging/docs/log-analytics#analytics) and a linked BigQuery dataset enabled | Actively analyze logs. Run ad hoc investigations by using [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) in the console, or write SQL queries, reports, and views using the [linked BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets).  
`sk-c-logging-bkt` | [Logs routed to Cloud Storage](https://docs.cloud.google.com/logging/docs/export/storage) | Store logs long-term for compliance, audit, and incident-tracking purposes.Optionally, if you have compliance requirements for mandatory data retention, we recommend that you additionally configure [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock).  
`sk-c-logging-pub` | [Logs routed to Pub/Sub](https://docs.cloud.google.com/logging/docs/export/pubsub) | Export logs to an external platform such as your existing SIEM.This requires additional work to integrate with your SIEM, such as the following mechanisms:

  * For many tools, [third-party integration with Pub/Sub](https://docs.cloud.google.com/logging/docs/export/pubsub#integrate-thru-pubsub) is the preferred method to ingest logs.
  * For Google Google Security Operations, you can [ingest Google Cloud data to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#export-logs) without provisioning additional infrastructure.
  * For Splunk, you can [stream logs from Google Cloud to Splunk](https://docs.cloud.google.com/architecture/stream-logs-from-google-cloud-to-splunk) using Dataflow.

  
  
For guidance on enabling additional log types and writing log sink filters, see the [log scoping tool](https://docs.cloud.google.com/architecture/security-log-analytics#log_scoping_tool).

## Threat monitoring with Security Command Center

We recommend that you activate Security Command Center to automatically detect threats, vulnerabilities, and misconfigurations in your Google Cloud resources. Security Command Center creates security findings from multiple sources including the following:

  * **[Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics):** detects common vulnerabilities and misconfigurations across Google Cloud resources.
  * **[Attack path exposure](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn):** shows a simulated path of how an attacker could exploit your high-value resources, based on the vulnerabilities and misconfigurations that are detected by other Security Command Center sources.
  * **[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection):** applies detection logic and proprietary threat intelligence against your logs to identify threats in near-real time.
  * **[Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection):** detects common container runtime attacks.
  * **[Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection):** detects potentially malicious applications that are running on virtual machines.
  * **[Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/how-to-use-web-security-scanner):** scans for OWASP Top Ten vulnerabilities in your web-facing applications on Compute Engine, App Engine, or Google Kubernetes Engine.



For more information on the vulnerabilities and threats addressed by Security Command Center, see [Security Command Center sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).

You must activate Security Command Center after you deploy the blueprint. For instructions, see [Overview of activating Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview).

After you activate Security Command Center, we recommend that you export the findings that are produced by Security Command Center to your existing tools or processes for triaging and responding to threats. The blueprint creates the `prj-c-scc` project with a Pub/Sub topic to be used for this integration. Depending on your existing tools, use one of the following methods to export findings:

  * If you use the console to manage security findings directly in Security Command Center, configure [folder-level and project-level roles](https://docs.cloud.google.com/security-command-center/docs/access-control-org#folder-level_and_project-level_roles) for Security Command Center to let teams view and manage security findings just for the projects for which they are responsible.
  * If you use Google SecOps as your SIEM, [ingest Google Cloud data to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs).

  * If you use a SIEM or SOAR tool with integrations to Security Command Center, share data with [Cortex XSOAR](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-cortex-xsoar), [Elastic Stack](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker), [ServiceNow](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-servicenow), [Splunk](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-splunk), or [QRadar](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-qradar).

  * If you use an external tool that can ingest findings from Pub/Sub, configure [continuous exports](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports) to Pub/Sub and configure your existing tools to ingest findings from the Pub/Sub topic.




## Custom solution for automated log analysis

You might have requirements to create alerts for security events that are based on custom queries against logs. Custom queries can help supplement the capabilities of your SIEM by analyzing logs on Google Cloud and exporting only the events that merit investigation, especially if you don't have the capacity to export all cloud logs to your SIEM.

The blueprint helps enable this log analysis by setting up a centralized source of logs that you can query using a linked BigQuery dataset. To automate this capability, you must implement the code sample at [`bq-log-alerting`](https://github.com/terraform-google-modules/terraform-google-log-export/tree/master/modules/bq-log-alerting) and extend the foundation capabilities. The sample code lets you regularly query a log source and send a custom finding to Security Command Center.

The following diagram introduces the high-level flow of the automated log analysis.

![Automated logging analysis.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/efb-logging-analysis.svg)

The diagram shows the following concepts of automated log analysis:

  * Logs from various sources are aggregated into a centralized logs bucket with log analytics and a linked BigQuery dataset.
  * BigQuery views are configured to query logs for the security event that you want to monitor.
  * Cloud Scheduler pushes an event to a Pub/Sub topic every 15 minutes and triggers Cloud Run functions.
  * Cloud Run functions queries the views for new events. If it finds events, it pushes them to Security Command Center as custom findings.
  * Security Command Center publishes notifications about new findings to another Pub/Sub topic.
  * An external tool such as a SIEM subscribes to the Pub/Sub topic to ingest new findings.



The sample has several [use cases](https://github.com/terraform-google-modules/terraform-google-log-export/blob/master/modules/bq-log-alerting/use-cases/README.md) to query for potentially suspicious behavior. Examples include a login from a list of super admins or other highly privileged accounts that you specify, changes to logging settings, or changes to network routes. You can extend the use cases by writing new query views for your requirements. Write your own queries or reference [security log analytics](https://docs.cloud.google.com/architecture/security-log-analytics#analyze_logs) for a library of SQL queries to help you analyze Google Cloud logs.

## Custom solution to respond to asset changes

To respond to events in real time, we recommend that you use Cloud Asset Inventory to [monitor asset changes](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes). In this custom solution, an asset feed is configured to trigger notifications to Pub/Sub about changes to resources in real time, and then Cloud Run functions runs custom code to enforce your own business logic based on whether the change should be allowed.

The blueprint has an example of this custom governance solution that monitors for IAM changes that add highly sensitive roles including Organization Admin, Owner, and Editor. The following diagram describes this solution.

![Automatically reverting an IAM policy change and sending a notification.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/reverting-iam-policy-change.svg)

The previous diagram shows these concepts:

  * Changes are made to an allow policy.
  * The Cloud Asset Inventory feed sends a real-time notification about the allow policy change to Pub/Sub.
  * Pub/Sub triggers a function.
  * Cloud Run functions runs custom code to enforce your policy. The example function has logic to assess if the change has added the Organization Admin, Owner, or Editor roles to an allow policy. If so, the function [creates a custom security finding](https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-findings) and sends it to Security Command Center.
  * Optionally, you can use this model to automate remediation efforts. Write additional business logic in Cloud Run functions to automatically take action on the finding, such as reverting the allow policy to its previous state.



In addition, you can extend the infrastructure and logic used by this sample solution to add custom responses to other events that are important to your business.

## What's next

  * Read about [preventative controls](https://docs.cloud.google.com/architecture/blueprints/security-foundations/preventative-controls) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
