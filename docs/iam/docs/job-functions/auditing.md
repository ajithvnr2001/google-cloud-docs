---
url: https://docs.cloud.google.com/iam/docs/job-functions/auditing/
title: IAM roles for auditing-related job functions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:40.107171+00:00
---

# IAM roles for auditing-related job functions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/job-functions/auditing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  IAM roles for auditing-related job functions Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Identity and Access Management (IAM) offers predefined roles that are tailored to specific job functions. If you want to give a user the necessary permissions to perform a specific job function in your organization, consider granting one of these predefined roles. To determine if IAM offers a predefined role for your use case, see [Predefined roles for job functions](https://docs.cloud.google.com/iam/docs/job-functions/roles-for-job-functions). 

This topic describes how to configure Identity and Access Management permissions for a set of sample auditing scenarios. It provides guidance on which IAM roles to grant to the auditing-related functional roles in your company for each scenarios. The examples in this topic are mainly targeted at security administrators, auditors, and employees who manage auditing tasks for an organization.

To learn about audit logs for Google Cloud, see [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). To learn about the audit logs that IAM generates, see [IAM audit logging for service accounts](https://docs.cloud.google.com/iam/docs/audit-logging).

## Scenario: Operational monitoring

In this scenario, an organization has a central security team that has the ability to review logs that may contain sensitive information both in Cloud Logging and when stored in long-term storage.

Historical audit data is stored in Cloud Storage. The organization uses an application to provide access to the historical audit data. The application uses a service account to access the log data. Due to the sensitivity of some of the audit log data, it is redacted using Sensitive Data Protection before being made accessible for viewing.

The table below explains the IAM roles that need to be granted to the CTO, security team, and service account, as well as the resource level at which the roles are granted.

Role | Resource | Principal | Description  
---|---|---|---  
**resourcemanager.organizationAdmin** | Organization | CTO | The **resourcemanager.organizationAdmin** role gives the CTO the ability to assign permissions to the security team and service account.  
**logging.viewer** | Organization | Security team | The **logging.viewer** role gives the security admin team the ability to view the Admin Activity logs.  
**logging.privateLogViewer** | Organization | Security team | The **logging.privateLogViewer** role gives the ability to view the Data Access logs.  
  
Once log entries have been exported, access to the exported copies is controlled entirely by IAM permissions and roles on any of the destinations: Cloud Storage, BigQuery, or Pub/Sub. In this scenario, Cloud Storage is the destination for long term storage of audit logs.

Role | Resource | Principal | Description  
---|---|---|---  
**logging.viewer** | Organization | Service account | The **logging.viewer** role permits the service account to read the Admin Activity logs in Cloud Logging.  
  
Data in the Data Access logs is deemed as personally identifiable information (PII) for this organization. Integrating the application with [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs) gives the ability to redact sensitive PII data when viewing Data Access logs whether they are in the Data Access logs or from the historical archive in Cloud Storage.

Role | Resource | Principal | Description  
---|---|---|---  
**storage.objectViewer** | Bucket | Service account | The **storage.objectViewer** role permits the service account to read the exported Admin Activity logs.  
  
The allow policy bound to the organization resource for this scenario will look similar to the following:
    
    
    {
      "bindings": [{
        "role": "roles/resourcemanager.organizationAdmin",
          "members": [
            "user:cto@example.com"
          ]
        },
        {
          "role": "roles/logging.viewer",
          "members": [
            "group:security-team@example.com",
            "serviceAccount:prod-logviewer@admin-resources.iam.gserviceaccount.com"
          ]
        },
        {
          "role": "roles/logging.privateLogViewer",
          "members": [
            "group:security-team@example.com"
          ]
        }
      ]
    }
    

The allow policy bound at the bucket configured as the destination sink for this scenario will look similar to the following:
    
    
    {
      "bindings": [{
        "role": "roles/storage.objectViewer",
        "members": [
          "serviceAccount:prod-logviewer@admin-resources.iam.gserviceaccount.com"
        ]
      }]
    }
    

## Scenario: Development teams monitoring their audit logs

In this scenario, the organization's developers need to look at audit logs generated while developing their applications. They are not permitted to review production logs unless they have been redacted using Sensitive Data Protection. A dashboard application is available to the developers that provides view-only access to exported production data. The organization's security team has access to all logs both in production and in the development environment.

The table below explains the IAM roles that need to be granted to the security team, developers, and service account, as well as the resource level at which the roles are granted.

Role | Resource | Principal | Description  
---|---|---|---  
**logging.viewer** | Organization | Security team | The **logging.viewer** role gives the security admin team the ability to view the Admin Activity logs.  
**logging.privateLogViewer** | Organization | Security team | The **logging.privateLogViewer** role gives the ability to view the Data Access logs.  
**logging.viewer** | Folder | Developer team | The **logging.viewer** role gives the developer team the ability to view the Admin Activity logs generated by the developer projects contained in a folder where all developer projects are located.  
**logging.privateLogViewer** | Folder | Developer team | The **logging.privateLogViewer** role gives the ability to view the Data Access logs.  
  
Access to the exported copies is controlled entirely by IAM permissions and roles on any of the destinations: Cloud Storage, BigQuery, or Pub/Sub. In this scenario, BigQuery is the destination for storage of audit logs.

Role | Resource | Principal | Description  
---|---|---|---  
**bigquery.dataViewer** | BigQuery dataset | Dashboard service account | The **bigquery.dataViewer** role permits the service account used by the dashboard application to read the exported Admin Activity logs.  
  
The allow policy bound to the development team's folder resource for this scenario will look similar to the following:
    
    
    {
      "bindings": [{
        "role": "roles/logging.viewer",
        "members": [
          "group:developer-team@example.com"
        ]
      },
      {
        "role": "roles/logging.privateLogViewer",
        "members": [
          "group:developer-team@example.com"
        ]
      }]
    }
    

The allow policy bound to the organization resource for this scenario will look similar to the following:
    
    
    {
      "bindings": [{
        "role": "roles/logging.viewer",
        "members": [
          "group:security-team@example.com"
        ]
      },
      {
        "role": "roles/logging.privateLogViewer",
        "members": [
          "group:security-team@example.com"
        ]
      }]
    }
    

The allow policy bound at the BigQuery dataset that is configured as the destination sink for this scenario will look similar to the following:
    
    
    {
      "bindings": [{
        "role": "roles/bigquery.dataViewer",
        "members": [
          "serviceAccount:prod-project-dashboard@admin-resources.iam.gserviceaccount.com"
        ]
      }]
    }
    

## Scenario: External auditors

In this scenario, audit logs for an organization are aggregated and exported to a central sink location. A third-party auditor is granted access several times a year to review the organization's audit logs. The auditor is not authorized to view PII data in the Admin Activity logs. To comply with this requirement, a dashboard is available that provides access to the historic logs stored in BigQuery, and on request, to the Cloud Logging Admin Activity logs.

The organization creates a group for these external auditors and adds the current auditor to the group. This group is monitored and is typically granted access to the dashboard application.

During normal access, the auditors' group is only granted access to view the historic logs stored in BigQuery. If any anomalies are discovered, the group is granted permission to view the actual Cloud Logging Admin Activity logs via the dashboard's elevated access mode. At the end of each audit period, the group's access is then revoked.

Data is redacted using Sensitive Data Protection before being made accessible for viewing via the dashboard application.

The table below explains IAM logging roles that an Organization Administrator can grant to the service account used by the dashboard, as well as the resource level at which the role is granted.

Role | Resource | Principal | Description  
---|---|---|---  
**logging.viewer** | Organization | Dashboard service account | The **logging.viewer** role permits the service account to read the Admin Activity logs in Cloud Logging.  
**bigquery.dataViewer** | BigQuery dataset | Dashboard service account | The **bigquery.dataViewer** role permits the service account used by the dashboard application to read the exported Admin Activity logs.  
  
The allow policy bound to the Organization resource for this scenario will look similar to the following:
    
    
    {
      "bindings": [{
        "role": "roles/logging.viewer",
        "members": [
          "serviceAccount:prod-project-dashboard@admin-resources.iam.gserviceaccount.com"
        ]
      }]
    }
    

The allow policy bound at the BigQuery dataset that is configured as the destination sink for this scenario will look similar to the following:
    
    
    {
      "bindings": [{
        "role": "roles/bigquery.dataViewer",
        "members": [
          "serviceAccount:prod-project-dashboard@admin-resources.iam.gserviceaccount.com"
        ]
      }]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
