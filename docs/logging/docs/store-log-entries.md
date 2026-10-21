---
url: https://docs.cloud.google.com/logging/docs/store-log-entries/
title: Store log entries \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:39.952268+00:00
---

# Store log entries  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/store-log-entries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Store log entries Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Logging uses containers called _log buckets_ to store and organize your log data. Understanding how system-created and user-defined log buckets work helps you configure data retention, regional storage locations, encryption keys, and Identity and Access Management (IAM) access controls. For organizations and folders, you can also use organization policies and default resource settings for Cloud Logging to enforce location and encryption requirements for new log buckets.

## About log buckets

Cloud Logging [encrypts customer content stored at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption). Data stored in log buckets by Logging is encrypted using key-encryption keys, a process known as [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption). Access to your logging data requires access to those key-encryption keys.

Log buckets are regional resources with a fixed location and are encrypted with either a customer-managed encryption key (CMEK) or a Google-owned and Google-managed encryption key. After a log bucket is created, you can't change its location or how its encryption key is managed. Google Cloud manages the infrastructure so that your log data is available redundantly across the zones within that region.

Your organization might have compliance, regulatory, or security requirements that govern where log buckets are located and whether they use CMEK. To enforce these requirements across an organization or folder, see Support for organizations and folders.

The retention period for the data stored in a log bucket depends on the type of log bucket. The retention period for the `_Required` log bucket is fixed, whereas you can configure custom retention for the `_Default` log bucket and for user-defined log buckets.

You can create [log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views). A _log view_ provides access to only a subset of the log data stored in a log bucket. For every log bucket, Cloud Logging automatically creates the `_AllLogs` view that provides access to every log entry in the log bucket. You control access to a log view by using [IAM](https://docs.cloud.google.com/iam/docs/overview).

To query and view your log data, use the **Logs Explorer** or **Observability Analytics** pages of the Google Cloud console:

  * The **Logs Explorer** page helps you troubleshoot and analyze the performance of your services and applications. You can view individual log entries and filter your log data. This interface has a scope setting, which lets you search for log data by project, log bucket, or log view.

  * The **Observability Analytics** page offers a SQL interface that lets you perform aggregate analysis on your log data that is stored in a [log bucket upgraded to use analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket). For example, use this interface to compute and chart trends. You can query log views and [analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views).




To learn more, see [Query and view log entries](https://docs.cloud.google.com/logging/docs/log-analytics).

## System-created log buckets

When the system creates a Google Cloud project, billing account, folder, or organization, Logging creates two log buckets, one named `_Required` and the other named `_Default`:

  * **Location** : Cloud Logging selects the location of these buckets unless [default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/default-settings) are configured. You can't change the location after the buckets are created.

  * **Encryption** : These buckets use Google-owned and Google-managed encryption keys unless default resource settings for Cloud Logging specify a CMEK. You can't change this configuration after the buckets are created.




You can't delete the system-created log buckets.

You can [upgrade system-created log buckets to use analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket). This upgrade lets you query your log data by using the **Observability Analytics** page, which supports SQL.

### `_Required` log bucket

The `_Required` log bucket stores log entries that are required for compliance or auditing purposes. For this reason, you can't delete this log bucket, and you can't modify which log entries are stored in this log bucket. Log entries in this log bucket are retained for 400 days; you can't change this retention period.

The log entries that are stored in the `_Required` log bucket for a resource also originate in that resource. That is, the `_Required` log bucket in a Google Cloud project can only store log entries that originate in that project.

The `_Required` log bucket stores the following types of log entries:

  * [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
  * [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event)
  * Google Workspace Admin Audit logs
  * Enterprise Groups Audit logs
  * Login Audit logs


  * [Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



### `_Default` log bucket

The `_Default` log bucket stores log entries that aren't automatically stored in the `_Required` log bucket. Because the `_Default` log bucket is system created, you can't delete it. However, you can modify which log entries are stored in this log bucket.

Cloud Logging retains the log entries in the `_Default` bucket for 30 days, unless you [configure custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention) for the bucket.

For example, this log bucket stores the following types of log entries:

  * [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access)
  * [Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied)
  * Logs generated by applications and Google Cloud services



## User-defined log buckets

You can create [user-defined log buckets](https://docs.cloud.google.com/logging/docs/buckets) in any Google Cloud project. When you create a user-defined log bucket, you select the location and set the [data retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention) period. You have the option to provide a CMEK.

You can [upgrade user-defined log buckets to use analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket). This upgrade lets you query your log data by using the **Observability Analytics** page, which supports SQL.

You can modify and delete user-defined log buckets. To protect against deleting a log bucket that stores log entries that are within their retention period, you can [lock the log bucket against updates](https://docs.cloud.google.com/logging/docs/buckets#locking-logs-buckets).

## Support for organizations and folders

To help your organization meet compliance and regulatory needs, Logging supports both default resource settings and organization policies:

  * **[Default resource settings](https://docs.cloud.google.com/logging/docs/default-settings)** : For organizations and folders, default resource settings for Cloud Logging control the location of new system-created log buckets. They also let you specify a CMEK, which applies to both new system-created and user-defined log buckets.

  * **[Organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)** : An organization policy can [restrict the location of new user-defined log buckets](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). Logging supports organization policies that specify regions where log buckets can, or can't, be created.




## Control access to a log bucket

[IAM](https://docs.cloud.google.com/iam/docs/overview) permissions and roles control access to log data. For example, you can do all of the following:

  * Grant read and edit access to a log bucket.
  * Grant edit access to a log bucket based on group membership by [using tags](https://docs.cloud.google.com/logging/docs/manage-log-buckets-with-tags).
  * Control access to specific fields in a log entry by [configuring field-level access on a log bucket](https://docs.cloud.google.com/logging/docs/field-level-acl).
  * Grant access to a subset of log entries in a log bucket by [creating a log view on that log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

Every log bucket has a _default log view_ , which typically includes every log entry in the log bucket. For the `_Default` log bucket, the default log view excludes Data Access audit log entries.




To give a user the permissions they need to view and analyze log entries, you typically grant one of the following IAM roles:

  * [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) role: Grants access to all log entries in the `_Required` bucket and access to the default log view on the `_Default` bucket.

  * [Private Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) (`roles/logging.privateLogViewer`) role: Grants access to all logs in the `_Required` and `_Default` buckets, including Data Access audit logs.




If you create user-defined log buckets or log views on log buckets, then additional permissions are required. For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## List of supported regions

Log buckets are regional resources. The infrastructure that stores, indexes, and searches your log entries is located in a specific geographical location. With the exception of log buckets in the `global`, `eu`, or `us` regions, Google Cloud manages the infrastructure so that your log data is available redundantly across the zones within the region of the log bucket.

The following [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) are supported by Cloud Logging:

#### Global

**Note:** If you want to choose the storage location for your log data or choose where your log data is analyzed with Observability Analytics, then don't create log buckets in the `global` location. Instead, either use a regional log bucket or, if you have data in a BigQuery multi-region and want to colocate your log data, then set the location of your log buckets to the appropriate multi-region location.Region name | Region description  
---|---  
`global` | Logs stored in any data centers in the world. Logs might be moved to different data centers. Unlike [ other global resources in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#global-resources), global log buckets in Cloud Logging don't provide additional redundancy guarantees compared to a regional log bucket.  
  
#### Multi-regions: EU and US

**Note:** If you have data in a [BigQuery multi-region](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions) and want to colocate your log data with that other business data then set the location of your log buckets to the appropriate multi-region. Alternatively, to control the storage location for your log data or where your log data is analyzed with Observability Analytics, specify that location when you create the log bucket. Don't use the `global` location.Region name | Region description  
---|---  
`eu` | Logs stored in any data centers within the European Union. Logs might be moved to different data centers. No additional redundancy guarantees.  
`us` | Logs stored in any data centers within the United States. Logs might be moved to different data centers. No additional redundancy guarantees.  
  
#### Africa

Region name | Region description  
---|---  
`africa-south1` | Johannesburg  
  
#### Americas

Region name | Region description  
---|---  
`northamerica-northeast1` | Montréal  
`northamerica-northeast2` | Toronto  
`northamerica-south1` | Mexico  
`southamerica-east1` | São Paulo  
`southamerica-west1` | Santiago  
`us-central1` | Iowa  
`us-east1` | South Carolina  
`us-east4` | North Virginia  
`us-east5` | Columbus  
`us-south1` | Dallas  
`us-west1` | Oregon  
`us-west2` | Los Angeles  
`us-west3` | Salt Lake City  
`us-west4` | Las Vegas  
  
#### Asia Pacific

Region name | Region description  
---|---  
`asia-east1` | Taiwan  
`asia-east2` | Hong Kong  
`asia-northeast1` | Tokyo  
`asia-northeast2` | Osaka  
`asia-northeast3` | Seoul  
`asia-south1` | Mumbai  
`asia-south2` | Delhi  
`asia-southeast1` | Singapore  
`asia-southeast2` | Jakarta  
`asia-southeast3` | Bangkok  
`australia-southeast1` | Sydney  
`australia-southeast2` | Melbourne  
  
#### Europe

Region name | Region description  
---|---  
`europe-central2` | Warsaw  
`europe-north1` | Finland  
`europe-north2` | Stockholm  
`europe-southwest1` | Madrid  
`europe-west1` | Belgium  
`europe-west2` | London  
`europe-west3` | Frankfurt  
`europe-west4` | Netherlands  
`europe-west6` | Zurich  
`europe-west8` | Milan  
`europe-west9` | Paris  
`europe-west10` | Berlin  
`europe-west12` | Turin  
  
#### Middle East

Region name | Region description  
---|---  
`me-central1` | Doha  
`me-central2` | Dammam  
`me-west1` | Tel Aviv  
  
## What's next

  * [Route log data](https://docs.cloud.google.com/logging/docs/routing/overview)
  * [Query and view log entries](https://docs.cloud.google.com/logging/docs/log-analytics)
  * [Configure and manage log buckets](https://docs.cloud.google.com/logging/docs/buckets)
  * [Configure default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/default-settings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
