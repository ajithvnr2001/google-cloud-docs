---
url: https://docs.cloud.google.com/workflows/docs/security-overview/
title: Workflows security overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:37.116647+00:00
---

# Workflows security overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/security-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Workflows security overview Stay organized with collections  Save and categorize content based on your preferences. 

Because a workflow contains no code or library dependencies, it does not require security patches. Once you deploy a workflow, you can expect it to reliably execute without maintenance. In addition, Workflows offers several security features and takes specific compliance measures to satisfy enterprise security requirements.

## Data encryption

By default, Google Cloud uses several layers of encryption to protect user data that's stored in Google production data centers. This default encryption occurs at the application or storage infrastructure layer. Traffic between your devices and the Google Front End (GFE) is encrypted using strong encryption protocols such as Transport Layer Security (TLS). Your data in use is protected, and confidentiality for workloads in a multi-tenant cloud environment is maintained, by performing computation in cryptographic isolation. For more information about the main security controls that Google Cloud uses to help protect your data, see [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper).

## Identity and access management

Since every workflow execution requires an authenticated call, you can mitigate the risk of accidental or malicious calls by using Workflows. Workflows manages access and authentication using Identity and Access Management (IAM) roles and permissions. You can simplify interactions with other Google Cloud APIs by using [IAM-based service accounts](https://docs.cloud.google.com/docs/authentication/production). For details, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication) and [Make authenticated requests from a workflow](https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow).

You can use Workflows to invoke an endpoint for which Identity-Aware Proxy (IAP) has been enabled. IAP verifies identity and enforces authorization at the application level, so you can use an application-level access control model instead of relying on network-level firewalls. When an application or resource is protected by IAP, it can only be accessed through the proxy by principals who have the correct Identity and Access Management (IAM) role. For more information, see [Invoke an IAP-secured endpoint](https://docs.cloud.google.com/workflows/docs/invoke-iap-secured-endpoints).

## Restricted network ingress

Workflows can also invoke Cloud Run functions or Cloud Run services in the same Google Cloud project that have ingress restricted to internal traffic. With this configuration, your services are unreachable from the internet but can be reached from Workflows. To apply these restrictions, you must adjust the ingress settings of your service or function. Note that the Cloud Run service must be reached on its `run.app` URL and not at a custom domain. For more information, see [Restrict network ingress](https://docs.cloud.google.com/run/docs/securing/ingress) (for Cloud Run) and [Configuring network settings](https://docs.cloud.google.com/functions/docs/networking/network-settings) (for Cloud Run functions). No other changes are needed to your workflow.

## Customer-managed encryption keys (CMEK)

If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use customer-managed encryption keys. Your workflow and associated data at rest are protected using an encryption key that only you can access, and that you can control and manage using Cloud Key Management Service (Cloud KMS). For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/workflows/docs/use-cmek).

## VPC Service Controls (VPC SC) support

VPC Service Controls is a mechanism to mitigate data exfiltration risks. You can use VPC Service Controls with Workflows to help protect your services. For more information, see [Set up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/workflows/docs/use-vpc-service-controls).

## Secret Manager to store and secure sensitive data

Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. You can use a Workflows connector to access Secret Manager within a workflow. This simplifies the integration for you, because the connector handles the formatting of requests, and provides methods and arguments so that you don't need to know the details of the Secret Manager API. For more information, see [Secure and store sensitive data using the Secret Manager connector](https://docs.cloud.google.com/workflows/docs/use-secret-manager).

## Integration with Cloud Logging, Cloud Monitoring, and Cloud Audit Logs

Logs are a primary source of diagnostic information about the health of your workflows. [Logging](https://docs.cloud.google.com/logging/docs) lets you store, view, search, analyze, and alert on log data and events.

Workflows is integrated with Logging and automatically generates execution logs for workflow executions. Because of the streaming nature of Logging, you can view the logs that any workflow emits immediately, and you can use Logging to centralize logs from all your workflows. You can also control when logs are sent to Logging during a workflow execution through call logging or custom logs. For details, see [Send logs to Logging](https://docs.cloud.google.com/workflows/docs/log-workflow).

In addition to consuming logs, you typically need to monitor other aspects of your services to ensure reliable operation. Use [Monitoring](https://docs.cloud.google.com/monitoring/docs) to get visibility into the performance, uptime, and overall health of your workflows.

To track and maintain details of interactions with your Google Cloud resources, you can use [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) to help capture activity such as data access. Use IAM controls to limit who can view audit logs. For more information, see the audit logging information for [workflows](https://docs.cloud.google.com/workflows/docs/audit-logging) and [workflow executions](https://docs.cloud.google.com/workflows/docs/audit-logging-workflow-executions).

## Compliance with standards

To confirm Workflows' compliance with various standards, see [Compliance controls](https://docs.cloud.google.com/workflows/docs/compliance-controls).

## What's next

  * [Security best practices](https://docs.cloud.google.com/workflows/docs/security-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
