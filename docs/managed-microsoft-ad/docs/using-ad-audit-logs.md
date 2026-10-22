---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/using-ad-audit-logs/
title: Set up audit logging for a domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:28.833356+00:00
---

# Set up audit logging for a domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/using-ad-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Set up audit logging for a domain Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to enable and view Managed Microsoft AD audit logs for a domain. For information about Cloud Audit Logs for Managed Microsoft AD, see [Managed Microsoft AD audit logging](https://docs.cloud.google.com/managed-microsoft-ad/docs/audit-logging).

## Enable Managed Microsoft AD audit logs

You can enable Managed Microsoft AD audit logs during domain creation or by updating an existing domain.

### At domain creation

To enable Managed Microsoft AD audit logs during domain creation, run the following gcloud CLI command.
    
    
    gcloud active-directory domains create DOMAIN_NAME --enable-audit-logs
    

### Update existing domain

To update a domain to enable Managed Microsoft AD audit logs, complete the following steps.

###  Console 

  1. Go to the [Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad) page in the Google Cloud console.  
[Go to the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)
  2. On the Managed Microsoft AD page, in the list of instances, select the domain where you want to enable audit logs.
  3. On the domain details page, select **View audit logs** , and then select **Configure logs** from the dropdown.
  4. In the **Configure audit logs** pane, under **Turn off/on logs** , toggle logs to **On**.



###  gcloud 

Run the following gcloud CLI command.
    
    
    gcloud active-directory domains update DOMAIN_NAME --enable-audit-logs
    

To limit what is logged, you can use [logs exclusions](https://docs.cloud.google.com/logging/docs/exclusions).

Note that logs stored in your project are chargeable. Learn more about [pricing for Cloud Logging](https://cloud.google.com/stackdriver/pricing#logging-costs).

## Disable Managed Microsoft AD audit logs

To disable Managed Microsoft AD audit logs, complete the following steps.

###  Console 

  1. Go to the [Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad) page in the Google Cloud console.  
[Go to the Managed Microsoft AD page](https://console.cloud.google.com/security/cloud-ad)
  2. On the Managed Microsoft AD page, in the list of instances, select the domain where you want to disable audit logs.
  3. On the domain details page, select **View audit logs** , and then select **Configure logs** from the dropdown.
  4. In the **Configure audit logs** pane, under **Turn off/on logs** , toggle logs to **Off**.



###  gcloud 

Run the following gcloud CLI command.
    
    
    gcloud active-directory domains update DOMAIN_NAME --no-enable-audit-logs
    

## Verify logging status

To verify that logging is enabled or disabled, complete the following steps, run the following gcloud CLI command.
    
    
    gcloud active-directory domains describe DOMAIN_NAME
    

In the response, verify the value of the `auditLogsEnabled` field.

## View logs

Managed Microsoft AD audit logs are only available for domains that are enabled to collect logs.

To view Managed Microsoft AD audit logs, you must have the `roles/logging.viewer` Identity and Access Management (IAM) permission. Learn about [granting permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To view the Managed Microsoft AD audit logs for your domain, complete the following steps.

### Logs Explorer

  1. Go to the [Logs Explorer](https://console.cloud.google.com/logs/query) page in the Google Cloud console.   
[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)
  2. In the **Query Builder** , enter the following values.
         
         resource.type="microsoft_ad_domain"
         resource.labels.fqdn="DOMAIN_NAME"
         

To filter by event IDs, add the following line to your advanced filter.
         
         jsonPayload.ID=EVENT_ID
         

  3. Select **Run Filter**.




Learn about the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary).

### Logs Explorer

  1. Go to the [Logs Explorer](https://console.cloud.google.com/logs/query) page in the Google Cloud console.   
[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)
  2. In the filter textbox, click keyboard_arrow_down, and then select **Convert to advanced filter**.
  3. In the advanced filter textbox, enter the following values.
         
         resource.type="microsoft_ad_domain"
         resource.labels.fqdn="DOMAIN_NAME"
         

To filter by event IDs, add the following line to your advanced filter.
         
         jsonPayload.ID=EVENT_ID
         

  4. Select **Submit Filter**.




Learn about the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### gcloud

Run the following gcloud CLI command.
    
    
    gcloud logging read FILTER
    

Where FILTER is an expression to identify a set of log entries. To read log entries in folders, billing accounts, or organizations, add the `--folder`, `--billing-account`, or `--organization` flags.

To read all the logs for your domain, you can run the following command.
    
    
    gcloud logging read "resource.type=microsoft_ad_domain AND resource.labels.fqdn=DOMAIN_NAME"
    

Learn about [reading log entries with the gcloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#reading_log_entries) and the [`gcloud logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).

## Interpret logs

Each `log_entry` contains the following fields.

  * The `log_name` is the event log where this event is logged.
  * The `provider_name` is the event provider that published this event.
  * The `version` is the version number for the event.
  * The `event_id` is identifier for this event.
  * The `machine_name` is the computer on which this event was logged.
  * The `xml` is the XML representation of the event. It conforms to the [event schema](https://docs.microsoft.com/en-us/windows/win32/wes/eventschema-schema).
  * The `message` is a human-readable representation of the event.



### Exported event IDs

The following table shows the event IDs that are exported.

**Table 1.** Exported event IDs Audit category | Event IDs  
---|---  
Account logon security | 4767, 4768, 4769, 4770, 4771, 4772, 4773, 4774, 4775, 4776, 4777  
Account management security | 4720, 4722, 4723, 4724, 4725, 4726, 4727, 4728, 4729, 4730, 4731, 4732, 4733, 4734, 4735, 4737, 4738, 4740, 4741, 4742, 4743, 4754, 4755, 4756, 4757, 4758, 4764, 4765, 4766, 4780, 4781, 4782, 4793, 4798, 4799, 5376, 5377  
DS access security | 4662, 5136, 5137, 5138, 5139, 5141  
Logon-logoff security | 4624, 4625, 4634, 4647, 4648, 4649, 4672, 4675, 4778, 4779, 4964  
Object access security | 4661, 5145  
Policy change security | 4670, 4703, 4704, 4705, 4706, 4707, 4713, 4715, 4716, 4717, 4718, 4719, 4739, 4864, 4865, 4866, 4867, 4904, 4906, 4911, 4912  
Privilege use security | 4985  
System security | 4612, 4621  
NTLM authentication | 8004  
  
If you find any event IDs are missing and you do not see them listed in the Exported Event IDs table, you can use the [Issue Tracker](https://issuetracker.google.com/issues/new?component=809523) to file a bug. Use the component **Public Trackers > Cloud Platform > Identity & Security > Managed Service for Microsoft AD**.

## Export logs

You can export Managed Microsoft AD audit logs to Pub/Sub, BigQuery, or Cloud Storage. Learn [how to export logs to other Google Cloud services](https://docs.cloud.google.com/logging/docs/export).

You can also export logs for compliance requirements, [security and access analytics](https://docs.cloud.google.com/solutions/exporting-stackdriver-logging-for-security-and-access-analytics), and to external 

SIEMs such as [Splunk](https://docs.cloud.google.com/solutions/exporting-stackdriver-logging-for-splunk) and Datadog.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
