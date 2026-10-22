---
url: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs/
title: Understanding and using Access Transparency logs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:51.591268+00:00
---

# Understanding and using Access Transparency logs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Transparency ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understanding and using Access Transparency logs

This page describes the contents of Access Transparency log entries and how to view and use them.

## Access Transparency logs in detail

Access Transparency logs can be integrated with your existing security information and event management (SIEM) tools to automate your audits of Google personnel when they access your content. Access Transparency logs are available in the Google Cloud console alongside your Cloud Audit Logs.

Access Transparency log entries include the following types of details:

  * The affected resource and action.
  * The time of the action.
  * The reasons for the action (for example, the case number associated with a customer support request).
  * Data about who is acting on the content (for example, the Google personnel's location).



## Enabling Access Transparency

For information about enabling Access Transparency for your Google Cloud organization, see [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable).

## Viewing Access Transparency logs

After you've configured Access Transparency for your Google Cloud organization, you can set controls for who can access the Access Transparency logs by assigning a user or group the **Private Logs Viewer** role. See the [Cloud Logging access control guide](https://docs.cloud.google.com/logging/docs/access-control) for details.

To view Access Transparency logs, use the following Google Cloud Observability logging filter.
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Faccess_transparency"
    

To learn how to see your Access Transparency logs in the Logs Explorer, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

You can also monitor the logs by using the Cloud Monitoring API or using Cloud Run functions. To get started, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

Optional: Create a [logs-based metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics) and then set up an [alerting policy](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts#alert-on-lbm) to give you timely awareness of issues surfaced by these logs. 

## Sample Access Transparency log entry

The following is an example of an Access Transparency log entry:
    
    
    {
     insertId:  "abcdefg12345"
     jsonPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.TransparencyLog"
      location: {
       principalOfficeCountry:  "US"
       principalEmployingEntity:  "Google LLC"
       principalPhysicalLocationCountry:  "CA"
      }
      principalJobTitle: "Engineering"
      product: [
       0:  "Cloud Storage"
      ]
      reason: [
        detail:  "Case number: bar123"
        type:  "CUSTOMER_INITIATED_SUPPORT"
      ]
      permissionDetails:[
        0: {
         permissionType: "DATA_READ"
         logAccessed: true
       }
       1: {
         permissionType: "ADMIN_READ"
        }
      ]
      eventId: "asdfg12345asdfg12345asdfg12345"
      accesses: [
       0: {
        methodName: "GoogleInternal.Read"
        resourceName: "//googleapis.com/storage/buckets/BUCKET_NAME/objects/foo123"
        }
      ]
      accessApprovals: [
       0: "projects/123/approvalRequests/abcdef12345"
      ]
     }
     logName:  "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Faccess_transparency"
     operation: {
      id:  "12345xyz"
     }
     receiveTimestamp:  "2017-12-18T16:06:37.400577736Z"
     resource: {
      labels: {
       project_id:  "1234567890"
      }
      type:  "project"
     }
     severity:  "NOTICE"
     timestamp:  "2017-12-18T16:06:24.660001Z"
    }

## Log field descriptions

Field | Description  
---|---  
`insertId` | Unique identifier for the log.  
`@type` | Access Transparency log identifier.  
`principalOfficeCountry` | ISO 3166-1 alpha-2 country code of country in which the accessor has a permanent desk, `??` if location not available, or 3-character continent identifier where Google personnel are in a low-population country.  
`principalEmployingEntity` | The entity that employs the Google personnel making the access (for example, `Google LLC`).   
`principalPhysicalLocationCountry` | ISO 3166-1 alpha-2 country code of country from which access was made, `??` if location not available, or 3-character continent identifier where Google personnel are in a low-population country.  
`principalJobTitle` | The job family of the Google identity making the access.   
  
When the job title is `Support Agent`, the actor is an AI support agent, and `principalPhysicalLocationCountry` and `principalOfficeCountry` are not provided (`??`).   
`product` | Customer's Google Cloud product that was accessed.  
`reason:detail` | Details of the reason, for example, a support ticket ID.  
`reason:type` | Access reason type (for example, `CUSTOMER_INITIATED_SUPPORT)`.  
`permissionDetails` | Details about permissions linked to an access. Up to two permissionType details may be present. For more information, see  Values for permission details.  
`accesses:methodName` | What type of access was made. For example, `GoogleInternal.Read`. For more information about the methods that can appear in the `methodName` field, see Values for `accesses: methodName` field.   
`accesses:resourceName` | [Name](https://cloud.google.com/apis/design/resource_names) of resource that was accessed.  
`accessApprovals` | Includes the [resource names](https://docs.cloud.google.com/apis/design/resource_names) of Access Approval requests that approved the access. These requests are subject to [exclusions](https://docs.cloud.google.com/access-approval/docs/overview#exclusions) and [supported services](https://docs.cloud.google.com/access-approval/docs/supported-services).  
  
This field is populated only if Access Approval is enabled for the accessed resources. Access Transparency logs published before the date March 24, 2021 won't have this field populated.   
`logName` | Name of the log location.  
`operation:id` | Log cluster ID.  
`receiveTimestamp` | Time the access was received by the logging pipeline.  
`project_id` | Project associated with the resource that was accessed.  
`type` | Type of resource that was accessed (for example, `project`).  
`eventId` | Unique event ID associated with a single access event justification (for example, a single support case). All accesses logged to the same justification have the same `event_id` value.  
`severity` | Log severity.  
`timestamp` | Time the log was written.  
  
### Values for permissionDetails fields

The following permission details are available in Access Transparency logs:

  * **permissionType** : Indicates the [Identity and Access Management (IAM) Permission type](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#permission-types) associated with the data access by the Google administrator. For example, permission types for each public API method for Cloud SQL can be found [in the SQL documentation](https://docs.cloud.google.com/sql/docs/mysql/audit-logging). Permission types indicate the maximum permission present, even if an access would have been possible with a lesser permission type.

  * **logAccessed** : This field indicates if an administrator or data read access permission is limited to log accesses. For example a data_read access to Observability Analytics logs is accompanied by "logAccessed = true", indicating that the data_read permission is limited to log data. This field is omitted if the access is not a log.


IAM Permission Type | Description | Examples  
---|---|---  
`ADMIN_READ` | Signifies a read access limited to a configuration, log, or similar data. | See [IAM Permission type](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#permission-types) for more details.  
`ADMIN_WRITE` | Signifies a read or write access limited to a configuration, log, or similar data. | See [IAM Permission type](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#permission-types) for more details.  
`DATA_READ` | Signifies a read access that _may_ contain [Customer Data](https://cloud.google.com/terms). An access with data_read permission type indicates the administrator had the permission to access Customer Data; however, it is not confirmation that Customer Data was accessed. | See [IAM Permission type](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#permission-types) for more details.  
`DATA_WRITE` | Signifies a read or write access that _may_ contain [Customer Data](https://cloud.google.com/terms). An access with data_write permission type indicates the administrator _may_ have included a permission to access at least resource of Customer Data. See [IAM Permission type](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#permission-types) for more details. |   
logAccessed | Description  
---|---  
`true` | Signifies an access limited to **read access** of logging data. This property extends the permissionType field. Accesses labeled true indicate the access is to logging data only, without access to the data directly.  
  
### Values for `accesses:methodNames` field

The following methods can appear in the `accesses:methodNames` field in Access Transparency logs:

  * **Standard methods** : These methods are `List`, `Get`, `Create`, `Update`, and `Delete`. For more information, see [Standard methods](https://docs.cloud.google.com/apis/design/standard_methods).
  * **Custom methods** : Custom methods refer to API methods besides the 5 standard methods. Common custom methods include `Cancel`, `BatchGet`, `Move`, `Search`, and `Undelete`. For more information, see [Custom methods](https://docs.cloud.google.com/apis/design/custom_methods).
  * **GoogleInternal methods** : The following are examples of `GoogleInternal` methods that appear in the `accesses:methodNames` field:

Method name | Description | Examples  
---|---|---  
`GoogleInternal.Read` | Signifies a read action performed on customer content with a valid business justification. The read action occurs using an internal API that is specifically designed for administering Google Cloud services. This method doesn't mutate customer content. | Reading IAM permissions.  
`GoogleInternal.Write` | Signifies a write action performed on customer content with a valid business justification. The write action occurs using an internal API that is specifically designed for administering Google Cloud services. This method can update customer content and/or configurations. | 

  * Setting IAM permissions for a resource.
  * Suspending a Compute Engine instance.

  
`GoogleInternal.Create` | Signifies a create action performed on customer content with a valid business justification. The create action occurs using an internal API that is specifically designed for administering Google Cloud services. This method creates new customer content. | 

  * Creating a Cloud Storage bucket.
  * Creating a Pub/Sub topic.

  
`GoogleInternal.Delete` | Signifies a delete action performed on customer content using an internal API specifically designed for administering Google Cloud services. This method mutates customer content and/or configurations. | 

  * Deleting a Cloud Storage object.
  * Deleting a BigQuery table.

  
`GoogleInternal.List` | Signifies a list action performed on customer content with a valid business justification. The list action occurs using an internal API that is specifically designed for administering Google Cloud services. This method doesn't mutate customer content or configurations. | 

  * Listing a customer's Compute Engine instances.
  * Listing a customer's Dataflow jobs.

  
`GoogleInternal.Update` | Signifies a modification performed on customer content with a valid business justification. The update action occurs using an internal API that is specifically designed for administering Google Cloud services. This method mutates customer content and/or configurations. | Updating HMAC keys in Cloud Storage.  
`GoogleInternal.Get` | Signifies a get action performed on customer content with a valid business justification. The get action occurs using an internal API that is specifically designed for administering Google Cloud services. This method doesn't mutate customer content or configurations. | 

  * Retrieving IAM policy for a resource.
  * Retrieving a customer's Dataflow job.

  
`GoogleInternal.Query` | Signifies a query action performed on customer content with a valid business justification. The query action occurs using an internal API that is specifically designed for administering Google Cloud services. This method doesn't mutate customer content or configurations. | 

  * Running a BigQuery query.
  * AI Platform debugging console lookup on customer content.

  
  
The `GoogleInternal` accesses are strictly restricted to authorized personnel for justified and auditable access. The presence of a method doesn't indicate availability to all roles. Organizations seeking enhanced controls over administrative access on a project or organization can activate Access Approval to enable approval or denial of accesses based on access details. For example, Access Approval users can choose to permit only requests with the `CUSTOMER_INITIATED_SUPPORT` justification for requests made by a Google employee. For more information, see [Overview of Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview).

If an event meets strict emergency access criteria, Access Approval can log that emergency access with the `auto approved` status. Access Transparency and Access Approval are specifically designed to include uninterrupted logging for emergency access scenarios.

If you are looking for more data security control over your workloads, we recommend using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview). Assured Workloads projects offer enhanced capabilities such as data residency, sovereign controls, and access to features such as confidential computing in Compute Engine. Assured Workloads uses [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) for externally-managed encryption keys. 

## Justification reason codes

**Reason** | **Description**  
---|---  
`CUSTOMER_INITIATED_SUPPORT` | Customer-initiated support, for example, "Case Number: ####".   
`GOOGLE_INITIATED_SERVICE` |  Refers to Google-initiated access for system management and troubleshooting. Google personnel can make this type of access for the following reasons: 

  * To perform technical debugging needed for a complex support request or investigation. 
  * To remediate technical issues, such as storage failure or data corruption. 
  * Proactive support by Technical Account Management teams. **Tagged with a reason detail of "TAM Support"** 

  
`THIRD_PARTY_DATA_REQUEST` | Google-initiated access in response to a legal request or legal process, including when responding to legal process from the customer that requires Google to access the customer's own data.   
`GOOGLE_INITIATED_REVIEW` | Google-initiated access for security, fraud, abuse, or compliance purposes, including: 

  * Ensuring the safety and security of customer accounts and data.
  * Confirming whether data is affected by an event that might impact account security (for example, malware infections).
  * Confirming whether customer is using Google services in compliance with Google Terms of Service.
  * Investigating complaints by other users and customers, or other signals of abusive activity.
  * Checking that Google services are being used consistently with relevant compliance regimes (for example, anti-money laundering regulations).

  
`GOOGLE_RESPONSE_TO_PRODUCTION_ALERT` |  Refers to Google-initiated access to maintain system reliability. Google personnel can make this type of access for the following reasons: 

  * To investigate and confirm that a suspected service outage doesn't affect the customer. 
  * To ensure backup and recovery from outages and system failures. 

  
  
## Monitoring Access Transparency logs

You can monitor Access Transparency logs by using the Cloud Monitoring API. To get started, see the [Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

You can set up a [logs-based metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics) and then set up an [alerting policy](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts#alert-on-lbm) to give you timely awareness of issues surfaced by these logs. For example, you can create a logs-based metric that captures Google personnel accesses of your content and then create an alerting policy in Monitoring that lets you know if the number of accesses in a given period exceeds a specified threshold.

## What's next

  * Learn how to [view and understand Access Transparency logs for Google Workspace services](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/understanding-workspace-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
