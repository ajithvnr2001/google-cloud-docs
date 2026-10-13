---
url: https://docs.cloud.google.com/security-command-center/docs/dspm-data-security/
title: Data Security Posture Management (DSPM) overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:54.960456+00:00
---

# Data Security Posture Management (DSPM) overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/dspm-data-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Data Security Posture Management (DSPM) overview Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions.  Data Security Posture Management will be shut down on February 1, 2027. Learn more about the controls and [ alternative detection capabilities](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework). 

Data Security Posture Management (DSPM) provides a data-centric view of Google Cloud security. DSPM lets you continuously identify and reduce data risk by helping you understand what sensitive data you have, where it is stored in Google Cloud, and if its use aligns with your security and compliance requirements.

DSPM capabilities depend on your [Security Command Center service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers). See [Data Security Posture Management in the Standard tier overview](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security-standard) for more information about which DSPM capabilities are available in the Standard tier.

DSPM in Premium and Enterprise tiers empowers your team to complete the following data security tasks:

  * **Data discovery and classification:** Automatically discover and classify sensitive data resources across your Google Cloud environment, including BigQuery and Cloud Storage.

  * **Data governance:** Evaluate your current data security posture against Google's best practices and compliance frameworks to identify and remediate potential security issues.

  * **Control enforcement:** Map your security requirements to specific data governance cloud controls, such as Data Access Governance and Data Flow Governance.

  * **Compliance monitoring:** Monitor workloads against applied data security frameworks to prove alignment, remediate violations, and generate evidence for audit.




## Core components of DSPM

The following sections describe the components of DSPM.

### Monitor your data security posture with the DSPM dashboard

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The data security dashboard in the Google Cloud console lets you see how your organization's data aligns with your data security and compliance requirements. It features a data map explorer to visualize data locations and filter by attributes like sensitivity and project. The dashboard provides security findings for policy violations, details security framework deployment and coverage, and more.

For more information about how to use the dashboard, see [Monitor your data security posture](https://docs.cloud.google.com/security-command-center/docs/use-dspm-dashboard).

### DSPM data security frameworks and compliance

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You use [frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#security-compliance-service-components) to define your data security and compliance requirements and apply those requirements to your Google Cloud environment. DSPM includes the Data security and privacy essentials framework, which defines recommended baseline controls for data security and compliance. When you enable DSPM, this framework is automatically applied to the Google Cloud organization in detective mode. You can use the generated findings to harden your data posture.

If required, you can make copies of the framework to create custom data security frameworks. You can add the advanced data security cloud controls to your custom frameworks and apply the custom frameworks to the organization, folders, projects, and App Hub applications in [folders configured for application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications). For example, you can create custom frameworks that apply jurisdictional controls to specific folders to ensure that data within those folders stays within a particular geographical region.

## Data security and privacy essentials framework (baseline controls)

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The following cloud controls are part of the Data security and privacy essentials framework. These controls provide comparable detection capability as specific findings from Compliance Manager and Sensitive Data Protection.

This table lists the cloud controls, their descriptions, and the [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls) and [Sensitive Data Protection](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#sdp) detectors that provide comparable detection capability when combined. For information about how to correlate these findings during an investigation, see Correlate findings from Compliance Manager and Sensitive Data Protection.

Cloud control | Description  
---|---  
[Require CMEK for BigQuery Tables with Sensitive Data](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#sensitive-data-bigquery-table-cmek-disabled) (`SENSITIVE_DATA_BIGQUERY_TABLE_CMEK_DISABLED`) | Detect when CMEK isn't used for BigQuery tables that include sensitive data. This control provides comparable detection capability as the following combined detection services and detectors:

  * Compliance Manager: [BIGQUERY_TABLE_CMEK_DISABLED](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#cmek-key-in-use-for-bigquery-table)
  * Sensitive Data Protection: [DATA_SENSITIVITY](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#data-sensitivity)

  
[Require CMEK for BigQuery Datasets with Sensitive Data](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#sensitive-data-dataset-cmek-disabled) (`SENSITIVE_DATA_DATASET_CMEK_DISABLED`) |  Detect when CMEK isn't used for BigQuery datasets that include sensitive data. This control provides comparable detection capability as the following combined detection services and detectors:

  * Compliance Manager: [DATASET_CMEK_DISABLED](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-cmek-on-bigquery-datasets)
  * Sensitive Data Protection: [DATA_SENSITIVITY](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#data-sensitivity)

  
[Block Public Access to BigQuery Datasets with Sensitive Data](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#sensitive-data-public-dataset) (`SENSITIVE_DATA_PUBLIC_DATASET`) |  Detect sensitive data within publicly accessible BigQuery datasets. This control provides comparable detection capability as the following combined detection services and detectors:

  * Compliance Manager: [PUBLIC_DATASET](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-public-access-bigquery-datasets)
  * Sensitive Data Protection: [DATA_SENSITIVITY](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#data-sensitivity)

  
[Block Public Access to Cloud SQL Instances with Sensitive Data](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#sensitive-data-public-sql-instance) (`SENSITIVE_DATA_PUBLIC_SQL_INSTANCE`) |  Detect sensitive data within publicly accessible SQL databases. This control provides comparable detection capability as the following combined detection services and detectors:

  * Compliance Manager: [PUBLIC_SQL_INSTANCE](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-public-access-cloud-sql-instance) and [SQL_PUBLIC_IP](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-cloud-sql-public-ip-addresses)
  * Sensitive Data Protection: [DATA_SENSITIVITY](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#data-sensitivity)

  
[Require CMEK for Cloud SQL Instances with Sensitive Data](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#sensitive-data-sql-cmek-disabled) (`SENSITIVE_DATA_SQL_CMEK_DISABLED`) |  Detect when CMEK isn't used for Cloud SQL databases that include sensitive data. This control provides comparable detection capability as the following combined detection services and detectors:

  * Compliance Manager: [SQL_CMEK_DISABLED](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#configure-cmek-cloud-sql-database)
  * Sensitive Data Protection: [DATA_SENSITIVITY](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#data-sensitivity)

  
  
### Correlate findings from Compliance Manager and Sensitive Data Protection

During an investigation you can correlate specific Compliance Manager and Sensitive Data Protection `ACTIVE` findings identified on the same resource to help identify a condition that's comparable to a DSPM cloud control finding.

Use one of the following methods to perform this investigation:

  * **Real-time alerting with Pub/Sub** : Set up a [continuous export](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports) to Pub/Sub that filters for `ACTIVE` findings. Use downstream services, such as Cloud Run functions or Cloud Run, to trigger automated alerts or workflows when both the related Compliance Manager and and Sensitive Data Protection finding exists for the same resource and both findings are in `ACTIVE` state.

  * **Scheduled analysis with BigQuery** : Use either [continuous streaming export](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query) or [bulk one-time export](https://docs.cloud.google.com/security-command-center/docs/bulk-exports-to-big-query) to BigQuery. You can run scheduled SQL queries in BigQuery that self-join the `findings` table on `resource_name` and filter for findings where both the Compliance Manager and Sensitive Data Protection finding exists and are in the `ACTIVE` state.




## Advanced data governance and security cloud controls

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

DSPM includes advanced data security to help you meet additional data security requirements. These advanced data security cloud controls are grouped as follows:

  * **Monitor user permissions:** Detects whether principals other than the ones that you specify are accessing sensitive data. The control name is _Restrict Access to Sensitive Data to Permitted Users_.
  * **Prevent data exfiltration:** Detects whether clients that are outside of specified geographic (country) locations are accessing sensitive data. The control name is _Restrict Flow of Sensitive Data Across Geographic Jurisdictions_.
  * **Enforce CMEK encryption:** Detects whether sensitive data is being created without [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek) encryption. Multiple controls help enforce CMEK for different Google Cloud services.
  * **Manage data deletion:** Detects violations to maximum retention period policies for sensitive data. The control name is _Govern the Maximum Retention Period for Sensitive Data_.
  * **Manage data retention:** ([Preview](https://cloud.google.com/products/#product-launch-stages)) Enforces a minimum retention period (in seconds) for Cloud Storage objects to ensure that they are retained for a minimum period of time. The control name is _Govern the minimum retention period for Cloud Storage objects_. You must [sign up](https://forms.gle/8At5HfN36SgFewoeA) to use this control.
  * **Manage data encryption:** ([Preview](https://cloud.google.com/products/#product-launch-stages)) Requires encryption for objects in Cloud Storage buckets. The control name is _Require Customer-Managed Encryption for Cloud Storage Objects_. You must [sign up](https://forms.gle/8At5HfN36SgFewoeA) to use this control.
  * **Manage public access to data:** ([Preview](https://cloud.google.com/products/#product-launch-stages)) Restricts public access to objects in Cloud Storage buckets to avoid data exposure risk. The control name is _Restrict Public Access to Cloud Storage Objects_. You must [sign up](https://forms.gle/8At5HfN36SgFewoeA) to use this control.



These controls support detective mode only. For more information about deploying these controls, see [Use DSPM](https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security#deploy-advanced-data-security-cloud-controls).

### Monitor user permissions

The [Restrict Access to Sensitive Data to Permitted Users](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#data-access-governance) control restricts access to sensitive data to specified principal sets. When there is a non-conformant access attempt (access by principals other than the allowed principals) to data resources, a finding is created. Supported principal types are user accounts or groups. For information about what format to use, see [the supported principal format table](https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security#principals-table).

User accounts include the following:

  * Consumer Google Accounts that users sign up for on google.com, such as Gmail.com accounts
  * Managed Google Accounts for businesses
  * Google Workspace for Education accounts



User accounts don't include robot accounts, service accounts, delegation-only brand accounts, resource accounts, and device accounts.

Supported asset types include the following:

  * BigQuery datasets and tables
  * Cloud Storage buckets
  * Gemini Enterprise Agent Platform models, datasets, feature stores, and metadata stores



DSPM evaluates for conformance with this control whenever a user account reads a supported resource type.

This cloud control requires that you enable Data Access audit logs for Cloud Storage and Agent Platform.

Limitations include the following:

  * Only read operations are supported.
  * Access by service accounts, including service account impersonation, is exempt from this control. As a mitigation, ensure that only trusted service accounts have access to sensitive Cloud Storage, BigQuery, and Agent Platform resources. Additionally, don't grant the [Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) to users who shouldn't have access.
  * This control doesn't prevent access by users to copies that are made through service account operations such as those made by Storage Transfer Service and BigQuery Data Transfer Service. Users could access copies of data which don't have this control enabled.
  * [Linked datasets](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) aren't supported. Linked datasets create a read-only BigQuery dataset that acts as a symbolic link to a source dataset. Linked datasets don't produce data access audit logs and might let an unauthorized user read data without it being flagged. For example, a user could bypass the access control by linking a dataset to a dataset outside of your compliance boundary and they could then query the new dataset without generating logs against the source dataset. As a mitigation, don't grant the [BigQuery Admin (`roles/bigquery.admin`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.admin), [BigQuery Data Owner (`roles/bigquery.dataOwner`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataOwner) or [BigQuery Studio Admin (`roles/bigquery.studioAdmin`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.studioAdmin) roles to users who shouldn't have access to sensitive BigQuery resources.
  * [Wildcard table queries](https://docs.cloud.google.com/bigquery/docs/querying-wildcard-tables) are supported at the dataset level, but not the tableset level. This feature lets you query multiple BigQuery tables at the same time using wildcard expressions. DSPM processes wildcard queries as though you're accessing the parent BigQuery dataset, not individual tables within the dataset.
  * Public access to Cloud Storage objects isn't supported. Public access grants access to all users without any policy checks.
  * Access or downloads of Cloud Storage objects using [authenticated browser sessions](https://docs.cloud.google.com/storage/docs/request-endpoints#cookieauth) isn't supported.
  * When deployed to an App Hub application, BigQuery tables and datasets aren't supported.



### Prevent data exfiltration

The [Restrict Flow of Sensitive Data Across Geographic Jurisdictions](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#data-flow-governance) control lets you specify the allowed countries from where data can be accessed. The cloud control works as follows:

  * If a read request comes from the internet, the country is determined based on the IP address of the read request. If a proxy is used to send the read request, alerts are sent based on the location of the proxy.

  * If the read request comes from a Compute Engine VM, the country is determined by the cloud zone where the request originates.




Supported asset types include the following:

  * BigQuery datasets and tables
  * Cloud Storage buckets
  * Agent Platform models, datasets, feature stores and metadata stores



Limitations include the following:

  * Only read operations are supported.
  * For Agent Platform, only requests from the internet are supported.
  * Public access to Cloud Storage objects isn't supported.
  * Access or downloads of Cloud Storage objects using [authenticated browser sessions](https://docs.cloud.google.com/storage/docs/request-endpoints#cookieauth) isn't supported.
  * When deployed to an [App Hub application](https://docs.cloud.google.com/app-hub/docs/key-concepts#application) in a folder configured for application management, BigQuery tables and datasets aren't supported.
  * When a principal accesses a resource more than once from a non-compliant location within 24 hours, violations are only supported for the first access.



### Enforce CMEK encryption

These controls require that you encrypt specific resources using CMEKs. They include the following:

  * [Enable CMEK for Gemini Enterprise Agent Platform Datasets](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#cmek-key-is-use-for-vertex-ai-dataset)
  * [Enable CMEK for Gemini Enterprise Agent Platform Metadata Stores](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#detective-policy-for-vertex-ai-metadata-store-that-checks-whether-cmek-is-enabled)
  * [Enable CMEK for Gemini Enterprise Agent Platform Models](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#cmek-key-is-use-for-vertex-ai-model)
  * [Enable CMEK for Gemini Enterprise Agent Platform Featurestore](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#detective-policy-for-vertex-ai-feature-store-that-checks-whether-cmek-is-enabled)
  * [Enable CMEK for BigQuery Tables](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#cmek-key-in-use-for-bigquery-table)



When you deploy these controls to an [App Hub application](https://docs.cloud.google.com/app-hub/docs/key-concepts#application), BigQuery tables aren't supported.

### Manage maximum data retention policies

The [Govern the Maximum Retention Period for Sensitive Data](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#data-deletion) control governs the retention period for sensitive data. You can select resources (for example, BigQuery tables) and apply a data deletion cloud control that detects if any of the resources violate maximum age retention limits.

Supported asset types include the following:

  * BigQuery datasets and tables
  * Agent Platform models, datasets, feature stores, and metadata stores
  * Cloud Storage objects ([Preview](https://cloud.google.com/products/#product-launch-stages)). You must [sign up](https://forms.gle/8At5HfN36SgFewoeA) to use this control.



When you deploy this control to an App Hub application, BigQuery tables and datasets aren't supported.

### Manage data retention

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The _Govern the minimum retention period for Cloud Storage objects_ control enforces a minimum retention period for Cloud Storage objects. This control prevents the deletion or modification of Cloud Storage objects until the minimum retention period (specified in seconds) has passed.

This control detects Cloud Storage objects that don't meet the configured minimum retention policy. Findings are generated in Security Command Center at the bucket level. You can query the findings at the object level within Storage Intelligence Datasets (in `object_security_findings_view`). Object-level findings have `findingType`: `SCC_DSPM_DATA_RETENTION` and `findingReason`: `MINIMUM_RETENTION_VIOLATION`.

Supported asset types: Cloud Storage objects

You must [sign up](https://forms.gle/8At5HfN36SgFewoeA) to use this control.

### Manage data encryption

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The _Require Customer-Managed Encryption for Cloud Storage Objects_ control helps you enforce encryption for objects in Cloud Storage buckets using CMEKs. The control detects Cloud Storage objects that are not encrypted with CMEK, in violation of your encryption policy.

Findings are generated in Security Command Center at the bucket level. You can query the findings at the object level within Storage Intelligence Datasets (in `object_security_findings_view`). Object-level findings have `findingType`: `SCC_DSPM_ENCRYPTION_NO_CMEK` and `findingReason`: `ENCRYPTION_CMEK_VIOLATION`.

Supported asset types: Cloud Storage objects

You must [sign up](https://forms.gle/8At5HfN36SgFewoeA) to use this control.

### Manage public access to data

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The _Restrict Public Access to Cloud Storage Objects_ control helps you restrict public access to objects in Cloud Storage buckets to avoid data exposure risk. This control detects Cloud Storage objects that are publicly accessible, in violation of your public access policy.

Findings are generated in Security Command Center at the bucket level. You can query the detailed object-level findings within Storage Intelligence Datasets (in `object_security_findings_view`). Object-level findings have `findingType`: `SCC_DSPM_PUBLIC_ACCESS_GOVERNANCE` and `findingReason`: `PUBLIC_ACCESS_VIOLATION`.

The `sccDspmFinding.securityInsights` field in the object-level finding provides more details on the public accessibility status, including read and write access.

Supported asset types: Cloud Storage objects

You must [sign up](https://forms.gle/8At5HfN36SgFewoeA) to use this control.

## Using DSPM with Sensitive Data Protection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

DSPM works with [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). Sensitive Data Protection finds the sensitive data in your organization, and DSPM lets you deploy data security cloud controls on the sensitive data to meet your security and compliance requirements.

The following table describes how you can use Sensitive Data Protection for data discovery and DSPM for policy enforcement and security posture management.

Service | **Sensitive Data Protection** | **DSPM**  
---|---|---  
Data scope | Finds and classifies sensitive data (such as PII or secrets) in storage on Google Cloud. | Assesses the security posture _around_ the classified sensitive data.  
Core actions | Scans, profiles, and de-identifies sensitive data. | Enforces, monitors, and validates policies.  
Findings focus | Reports on _where_ the sensitive data is located (for example, BigQuery, or Cloud Storage). | Reports on _why_ the data is exposed (for example, public access, missing CMEK, or excessive permissions).  
Integration | Feeds DSPM with sensitivity and classification metadata. | Uses Sensitive Data Protection data to apply and monitor security controls and risk assessments.  
  
## What's next

  * [Enable DSPM](https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security).
  * [Send Sensitive Data Protection inspection job results to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-scc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
