---
url: https://docs.cloud.google.com/iam/docs/audit-logging/examples-oauth-clients/
title: Example logs for Workforce Identity Federation OAuth application integration \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:16.184271+00:00
---

# Example logs for Workforce Identity Federation OAuth application integration  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/audit-logging/examples-oauth-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Example logs for Workforce Identity Federation OAuth application integration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides examples of the audit logs that are generated when you use [Workforce Identity Federation OAuth application integration](https://docs.cloud.google.com/iam/docs/workforce-oauth-app). With Workforce Identity Federation OAuth application integration, you can allow third-party applications to integrate with Google Cloud through OAuth and use external identities to access Google Cloud resources.

Each of the following examples shows only the most relevant fields in the log entries.

For more information about enabling and viewing audit logs, see [Identity and Access Management audit logging](https://docs.cloud.google.com/iam/docs/audit-logging).

## Required roles

IAM can generate audit logs when you create and manage OAuth clients. To enable audit logs when managing OAuth clients, you must [enable audit logs for Data Access activity](https://docs.cloud.google.com/iam/docs/audit-logging#enabling_audit_logging) for the following API:

  * Identity and Access Management API (enable log type "ADMIN_READ")



## Logs for creating an OAuth client

The log entry is similar to the following:
    
    
    {
      "logName": "projects/PROJECT_NUMBER/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : PRINCIPAL_EMAIL,**
        },
        "methodName": "google.iam.admin.v1.OauthClients.CreateOauthClient",
        **"resourceName" : "projects/PROJECT_NUMBER/locations/global",**
        "serviceName": "iam.googleapis.com",
        "request": {
          "@type": "type.googleapis.com/google.iam.admin.v1.CreateOauthClientRequest",
          **"oauthClient" : {},
          "oauthClientId": OAUTH_CLIENT_ID,
          "parent": "projects/PROJECT_NUMBER/locations/global"**
        }
      },
      "resource": {
        "type": "audited_resource"
      }
    }

This log entry includes the following values, which you can use to filter logs:

  * PROJECT_NUMBER: the project number of the project that contains the OAuth application integration.

  * PRINCIPAL_EMAIL: the email address of the principal that owns the OAuth client.

  * OAUTH_CLIENT_ID: the identity of the OAuth client




## Logs for creating an OAuth client credential

The log entry is similar to the following:
    
    
    {
      "logName": "projects/PROJECT_NUMBER/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : PRINCIPAL_EMAIL,**
        },
        "methodName": "google.iam.admin.v1.OauthClients.CreateOauthClientCredential",
        **"resourceName" : "projects/PROJECT_NUMBER/locations/global/oauthClients/OAUTH_CLIENT_ID",**
        "serviceName": "iam.googleapis.com",
        "request": {
          "@type": "type.googleapis.com/google.iam.admin.v1.CreateOauthClientCredentialRequest",
          **"oauthClientCredential" : {},
          "oauthClientCredentialId": OAUTH_CLIENT_CREDENTIAL_ID,
          "parent": "projects/PROJECT_NUMBER/locations/global/oauthClients/OAUTH_CLIENT_ID"**
        }
      },
      "resource": {
        "type": "audited_resource"
      }
    }

This log entry includes the following values, which you can use to filter logs:

  * PROJECT_NUMBER: the project number of the project that contains the OAuth application integration.

  * PRINCIPAL_EMAIL: the email address of the principal that (owns|accessed) the OAuth client.

  * OAUTH_CLIENT_ID: the identity of the OAuth client

  * OAUTH_CLIENT_CREDENTIAL_ID: the identity of the OAuth client credential




## What's next

  * [Configure and view the audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) for IAM.
  * Get more information about [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).
  * Set up [Workforce OAuth application integration](https://docs.cloud.google.com/iam/docs/workforce-oauth-app) using OAuth clients.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
