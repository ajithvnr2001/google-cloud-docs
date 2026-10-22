---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/auditing/
title: Best practices for auditing SSH access \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:45.834767+00:00
---

# Best practices for auditing SSH access  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/auditing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for auditing SSH access Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for auditing SSH access to Linux virtual machine (VM) instances.

Cloud Audit Logs let you analyze past activity and can be an important source of information when investigating suspicious activity affecting your Google Cloud resources.

The following sections contains best practices that can help you maintain a non-repudiable audit trail:

  * Enable data access logs for IAP
  * Monitor audit log entries related to SSH usage



The document focuses on practices that are either specific to Google Cloud or of particular relevance when using SSH on Google Cloud. The document doesn't cover best practices for specific SSH client or server implementations.

## Enable data access logs for IAP

To make sure that IAP adds an entry to the Cloud Audit Logs whenever a user attempts to establish an SSH connection, [enable data access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for the **Cloud Identity-Aware Proxy API**. Data access logs are disabled by default. Unless you have concerns about log volume, enable data access logs for all projects that contain VM instances.

## Monitor audit log entries related to SSH usage

SSH usage can impact the security of VMs and their workloads, so it's important to keep an audit trail for both successful connection attempts and failed access attempts. This is especially important in production environments, where SSH usage should be considered a sensitive action.

To track SSH access and possibly to find suspicious behavior, make sure that you monitor log entries related to SSH, including the following:

Service | Method | Description  
---|---|---  
IAP | `AuthorizeUser` |  Indicates a connection attempt through IAP TCP-forwarding. Log entries contain details about the user's device, satisfied access levels, and unsatisfied access levels.   
OS Login | `google.cloud.oslogin.dataplane.OsLoginDataPlaneService.CheckPolicy` | [Indicates a login attempt](https://docs.cloud.google.com/compute/docs/oslogin/view-audit-logs).  
OS Login | `google.cloud.oslogin.dataplane.OsLoginDataPlaneService.StartSession` | [Indicates the start of a OS Login 2FA challenge](https://docs.cloud.google.com/compute/docs/oslogin/view-audit-logs)  
OS Login | `google.cloud.oslogin.dataplane.OsLoginDataPlaneService.ContinueSession` | [Indicates the completion of a OS Login 2FA challenge](https://docs.cloud.google.com/compute/docs/oslogin/view-audit-logs)  
Compute Engine | `v1.compute.projects.setCommonInstanceMetadata` |  If the field `projectMetadataDelta` contains an entry for `ssh-keys`, then this log entry indicates that an SSH key was added, removed or modified in project metadata.   
Compute Engine | `v1.compute.instances.setMetadata` |  If the field `projectMetadataDelta` contains an entry for `ssh-keys` or `sshKeys`, then this log entry indicates that an SSH key was added, removed or modified in instance metadata.   
Compute Engine | `google.ssh-serialport.v1.connect` | Indicates a connection attempt to the serial console  
IAM |  `beta.compute.instances.setIamPolicy`, `v1.compute.instances.setIamPolicy` |  Indicates a change to the IAM policy of a VM instance. An IAM policy change might affect users' ability to modify instance metadata.   
IAM |  `SetIamPolicy` |  Indicates a change to the IAM policy of a project. An IAM policy change might affect users' ability to modify project metadata and the project's [Data Access audit logs configuration](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-api).   
  
All audit log records contain a `principalEmail` field that identifies the principal that initiated the activity.

To get a complete picture of activity on your VMs, configure your VMs to export `/var/log/messages` and SSH server logs to Cloud Logging, for example by using [Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent).

Notice that depending on the Linux distribution you use, SSH server logs might be written to different log files (typically, `/var/log/auth.log` or `/var/log/secure`), and that these log files aren't covered by the [default configuration used by Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#default).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
