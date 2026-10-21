---
url: https://docs.cloud.google.com/docs/security/gcmvsp/monitoring-logging-alerting/
title: Monitoring, logging, and alerting guidelines \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:39.657170+00:00
---

# Monitoring, logging, and alerting guidelines  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/gcmvsp/monitoring-logging-alerting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Monitoring, logging, and alerting guidelines Stay organized with collections  Save and categorize content based on your preferences. 

The following guidelines for the minimum viable security platform align with the monitoring, logging, and alerting pillar.

## Basic level guidelines

Implement the following monitoring, logging, and alerting guidelines first.

Item | 

### Subscribe to security bulletins  
  
---|---  
Description | Subscribe to the security bulletin notifications for Google Cloud services to receive alerts about vulnerabilities and mitigation measures.When security bulletins are available that are relevant to your Google Cloud service (such as GKE), the service can publish notifications about those events as messages to Pub/Sub topics that you configure. You can receive these notifications on a Pub/Sub subscription, integrate with third-party services, and filter for the notification types you want to receive.  
Related information | 

  * [Security Bulletins](https://docs.cloud.google.com/support/bulletins)

  
Item ID | MVSP-CO-1.54  
Mapping |  Related NIST-800-53 controls:

  * SI-5

Related CRI profile controls:

  * PR.IP-1.4

  
Item | 

### Configure Essential Contacts groups  
  
---|---  
Description | Configure Essential Contacts to ensure that a monitored group alias or mailing list receive important notifications.Google sends critical security alerts (like a potential account compromise) to the email addresses listed as Essential Contacts. If an individual's email is used for this purpose, the alert is missed if that person is unavailable or has left the company.Using a monitored group email address helps ensure these time-sensitive alerts are delivered to an active team that can respond quickly.  
Related information | 

  * [Essential Contacts overview](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts)

  
Item ID | MSVP-CO-1-55  
Mapping |  Related NIST-800-53 controls:

  * IR-4

Related CRI profile controls:

  * PR.IP-1.4

Compliance Manager control:

  * [Define Essential Contacts](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#define-essential-contacts)

  
Item | 

### Monitor billing anomalies  
  
---|---  
Description | Use the billing anomaly feature in Cloud Billing to track any spikes or deviations in expected spend. A sudden, unexpected spike in a cloud bill is a primary indicator of a security compromise. Unexpected billing spikes are sometimes caused by attackers who have gained access and are using resources for unauthorized activities.Enabling billing anomaly detection provides an essential early warning system so that you can automatically flag this suspicious activity.  
Related information | 

  * [View and manage cost anomalies](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies)
  * [Set up programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications)

  
Item ID | MSVP-CO-1-56  
Mapping |  Related NIST-800-53 controls:

  * AU-6

Related CRI profile controls:

  * DE.AE-1.1

  
  
## Intermediate level guidelines

After you implemented the basic guidelines, implement the following monitoring, logging, and alerting guidelines.

Item | 

### Enable Firewall Rules Logging  
  
---|---  
Description | By default, firewall rules don't automatically write logs.Firewall Rules Logging lets you audit, verify, and analyze the effects of your firewall rules. For example, you can determine if a firewall rule designed to deny traffic is functioning as intended. Logging is also useful if you want to determine how many connections are affected by a given firewall rule.  Enable logging for each firewall rule. You can configure logging using a pipeline that you use to create a firewall.  
Related information | 

  * [Use Firewall Rules Logging](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging)

  
Item ID | MSVP-CO-1-58  
Mapping |  Related NIST-800-53 controls:

  * AU-2
  * AU-3
  * AU-8
  * AU-9

Related CRI profile controls:

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

Compliance Manager control:

  * [Enable Firewall Rule Logging](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-firewall-rule-logging)

  
Item | 

### Share audit logs from Cloud Identity  
  
---|---  
Description | If using Cloud Identity, share audit logs from Cloud Identity to Google Cloud.Admin Activity audit logs from Google Workspace or Cloud Identity are ordinarily managed and viewed in the Google Admin console, separately from your logs in your Google Cloud environment. These logs contain information that is relevant for your Google Cloud environment, such as user login events.We recommend that you share Cloud Identity audit logs to your Google Cloud environment to centrally manage logs from all sources.  
Related information | 

  * [Audit logs for Google Workspace](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging)
  * [Share data with Google Cloud services](https://support.google.com/a/answer/9320190)

  
Item ID | MSVP-CO-1-59  
Mapping |  Related NIST-800-53 controls:

  * AC-2
  * AC-3
  * AC-8
  * AC-9

Related CRI profile controls:

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4

Compliance Manager control:

  * [Import Google Workspace Audit Logs](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#import-google-workspace-audit-logs)

  
  
## Advanced level guidelines

After you implemented the intermediate guidelines, implement the following monitoring, logging, and alerting guidelines.

Item | 

### Enable Access Transparency logs  
  
---|---  
Description | Standard logs show you what your organization's own users are doing, but Access Transparency logs show what Google support staff do when they access the account. This access typically only happens in response to a support request. Access Transparency logs provide a complete and verifiable audit trail of all access, which is essential for meeting strict compliance and data governance requirements. You can enable Access Transparency at the organization level.  
Related information | 

  * [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable)

  
Item ID | MSVP-CO-1-57  
Mapping |  Related NIST-800-53 controls:

  * AU-2
  * AU-3
  * AU-8
  * AU-9

Related CRI profile controls:

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

Compliance Manager control:

  * [Enable Access Transparency](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-access-transparency)

  
Item | 

### Export logs to a log sink for long-term storage  
  
---|---  
Description | Create a log sink to export logs for your security monitoring solution and set the retention period to meet your requirements.The default log retention periods are often not long enough to meet the 1-7 year requirements mandated by compliance regulations like PCI or HIPAA.Creating a log sink to export logs to a long-term storage location is essential for meeting certain legal and regulatory obligations. Log sinks also let you send logs to a centralized security monitoring system for advanced threat detection.  
Related information | 

  * [Route log entries](https://docs.cloud.google.com/logging/docs/routing/overview)

  
Item ID | MSVP-CO-1-60  
Mapping |  Related NIST-800-53 controls:

  * AU-9

Related CRI profile controls:

  * PR.DS-4.1

Compliance Manager control:

  * [Configure Log Sinks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#configure-log-sinks)

  
  
## What's next

  * [Overview of minimum viable secure platform](https://docs.cloud.google.com/docs/security/gcmvsp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
