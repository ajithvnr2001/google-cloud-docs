---
url: https://docs.cloud.google.com/secure-web-proxy/docs/roles-permissions/
title: Roles and permissions \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:00.543332+00:00
---

# Roles and permissions  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the Identity and Access Management (IAM) permissions that are necessary to perform specific Secure Web Proxy operations. It also explains how to create a custom IAM role and assign the required permissions to the role for managing various Secure Web Proxy resources.

## Permissions

The following table lists the permissions that you require to perform specific operations in Secure Web Proxy. For more information, see the [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference).

Operation | Resource | Permission (method)  
---|---|---  
Create a policy | Gateway security policies | `networksecurity.gatewaySecurityPolicies.create`  
Delete a policy | Gateway security policies | `networksecurity.gatewaySecurityPolicies.delete`  
Retrieve a policy | Gateway security policies | `networksecurity.gatewaySecurityPolicies.get`  
List policies | Gateway security policies | `networksecurity.gatewaySecurityPolicies.list`  
Update a policy | Gateway security policies | `networksecurity.gatewaySecurityPolicies.update`  
Create a rule | Gateway security policy rules | `networksecurity.gatewaySecurityPolicyRules.create`  
Delete a rule | Gateway security policy rules | `networksecurity.gatewaySecurityPolicyRules.delete`  
Retrieve a rule | Gateway security policy rules | `networksecurity.gatewaySecurityPolicyRules.get`  
List rules | Gateway security policy rules | `networksecurity.gatewaySecurityPolicyRules.list`  
Update a rule | Gateway security policy rules | `networksecurity.gatewaySecurityPolicyRules.update`  
Retrieve an operation | Operations | `networksecurity.operations.get`  
Create a TLS inspection policy | TLS inspection policies | `networksecurity.tlsInspectionPolicies.create`  
Delete a TLS inspection policy | TLS inspection policies | `networksecurity.tlsInspectionPolicies.delete`  
Retrieve a TLS inspection policy | TLS inspection policies | `networksecurity.tlsInspectionPolicies.get`  
List TLS inspection policies | TLS inspection policies | `networksecurity.tlsInspectionPolicies.list`  
Update a TLS inspection policy | TLS inspection policies | `networksecurity.tlsInspectionPolicies.update`  
Attach a TLS inspection policy to a Secure Web Proxy policy | TLS inspection policies | `networksecurity.tlsInspectionPolicies.use`  
Create a URL list | URL lists | `networksecurity.urlLists.create`  
Delete a URL list | URL lists | `networksecurity.urlLists.delete`  
Retrieve a URL list | URL lists | `networksecurity.urlLists.get`  
List all URL lists | URL lists | `networksecurity.urlLists.list`  
Update a URL list | URL lists | `networksecurity.urlLists.update`  
Attach a URL list to a Secure Web Proxy rule | URL lists | `networksecurity.urlLists.use`  
Provision and manage a Secure Web Proxy instance | Various Certificate Manager, Compute Engine, Secure Web Proxy, Resource Manager, and Cloud Monitoring resources | 

  * `certificatemanager.certs.get`
  * `certificatemanager.certs.list`
  * `certificatemanager.certs.use`
  * `compute.addresses.create`
  * `compute.addresses.createInternal`
  * `compute.addresses.list`
  * `compute.instances.update`
  * `compute.networks.get`
  * `compute.networks.list`
  * `compute.projects.get`
  * `compute.regionOperations.get`
  * `compute.routers.create`
  * `compute.routers.delete`
  * `compute.routers.get`
  * `compute.routers.list`
  * `compute.routers.update`
  * `compute.subnetworks.get`
  * `compute.subnetworks.list`
  * `networksecurity.gatewaySecurityPolicies.get`
  * `networksecurity.gatewaySecurityPolicies.list`
  * `networksecurity.gatewaySecurityPolicies.use`
  * `networksecurity.gatewaySecurityPolicyRules.get`
  * `networksecurity.gatewaySecurityPolicyRules.list`
  * `networksecurity.locations.list`
  * `networksecurity.urlLists.get`
  * `networksecurity.urlLists.list`
  * `networksecurity.urlLists.use`
  * `networkservices.gateways.create`
  * `networkservices.gateways.delete`
  * `networkservices.gateways.get`
  * `networkservices.gateways.list`
  * `networkservices.gateways.update`
  * `networkservices.gateways.use`
  * `networkservices.locations.list`
  * `networkservices.operations.get`
  * `networkservices.operations.list`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `serviceusage.quotas.get`
  * `serviceusage.services.get`
  * `serviceusage.services.list`

  
Create, update, or delete a telemetry policy | Telemetry policies | 

  * `networkservices.telemetryPolicies.create`
  * `networkservices.telemetryPolicies.update`
  * `networkservices.telemetryPolicies.delete`
  * `compute.backendServices.update`
  * `networkservices.gateways.get`
  * `networkservices.gateways.use`

  
Retrieve or list telemetry policies | Telemetry policies | 

  * `networkservices.telemetryPolicies.get`
  * `networkservices.telemetryPolicies.list`

  
View distributed traces in Cloud Trace | Traces | 

  * `cloudtrace.traces.get`
  * `cloudtrace.traces.list`

  
Write or export distributed trace spans | Traces | 

  * `cloudtrace.traces.patch`

  
  
## Roles

To get the permissions that you need to provision a Secure Web Proxy instance, request your administrator to grant you the following IAM roles on your project:

  * To configure policies and provision a Secure Web Proxy instance: [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * To upload explicit Secure Web Proxy TLS certificates: [Certificate Manager Editor role](https://docs.cloud.google.com/certificate-manager/docs/permissions#certificatemanager.editor) (`roles/certificatemanager.editor`)
  * To configure distributed tracing and telemetry policies: [Network Services Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networkservices#networkservices.admin) (`roles/networkservices.admin`) or [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * To view trace spans in Cloud Trace: [Cloud Trace User role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)
  * To export trace spans to Trace: grant the [Cloud Trace Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`) to the following service accounts: 
    * Compute Engine service agent: `service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`
    * Network Security service agent: `service-PROJECT_NUMBER@gcp-sa-networksecurity.iam.gserviceaccount.com`
    * Client virtual machine (VM) service accounts, if client applications generate or propagate spans



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through custom roles or other predefined roles.

Optional: If you have a set of users who are responsible for managing your Compute Engine organization security policies, then grant them the [Compute Organization Security Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityPolicyAdmin) (`roles/compute.orgSecurityPolicyAdmin`).

For more information about project roles and permissions, see the following:

  * [Identity and Access Management documentation](https://docs.cloud.google.com/iam/docs)
  * [Compute Engine API documentation](https://docs.cloud.google.com/compute/docs/apis)
  * [Cloud Monitoring API documentation](https://docs.cloud.google.com/monitoring/docs/apis)



## What's next

  * To complete the initial tasks to set up Secure Web Proxy, see [Initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
