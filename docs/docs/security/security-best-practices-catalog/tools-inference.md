---
url: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/tools-inference/
title: Tools and inference controls \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:35:33.637405+00:00
---

# Tools and inference controls  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/tools-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Tools and inference controls Stay organized with collections  Save and categorize content based on your preferences. 

This document includes the best practices and guidelines for Gemini Enterprise Agent Platform when running workloads on Google Cloud.

### Define the access mode for Agent Platform Workbench notebooks and instances

Google control ID | VAI-CO-4.1  
---|---  
Implementation | Required  
Description | This list constraint defines the permitted access modes for Agent Platform Workbench notebooks and instances. The allow or deny list can specify multiple users using `service-account` mode or single-user access using `single-user` mode.  
Applicable products | 

  * Gemini Enterprise Agent Platform Workbench
  * Organization Policy Service

  
Path | `constraints/ainotebooks.accessMode`  
Operator | Is  
Value | 

  * `service-account`
  * `single-user`

  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
  
### Disable file downloads on Agent Platform Workbench instances

Google control ID | VAI-CO-4.2  
---|---  
Implementation | Required  
Description | The `ainotebooks.disableFileDownloads` boolean constraint prevents you from creating Gemini Enterprise Agent Platform Workbench instances with the file download option enabled. By default, you can enable the file download option on any Agent Platform Workbench instance.  
Applicable products | 

  * Organization Policy Service
  * Agent Platform Workbench

  
Path | `constraints/ainotebooks.disableFileDownloads`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
  
### Disable root access on Agent Platform Workbench user-managed notebooks and instances

Google control ID | VAI-CO-4.3  
---|---  
Implementation | Required  
Description | The `ainotebooks.disableRootAccess` boolean constraint prevents you from creating Gemini Enterprise Agent Platform Workbench user-managed notebooks and instances with root access enabled. By default, Agent Platform Workbench user-managed notebooks and instances can have root access enabled.  
Applicable products | 

  * Organization Policy Service
  * Agent Platform Workbench

  
Path | `constraints/ainotebooks.disableRootAccess`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
  
### Disable terminal on Agent Platform Workbench instances

Google control ID | VAI-CO-4.4  
---|---  
Implementation | Required  
Description | The `ainotebooks.disableTerminal` boolean constraint prevents you from creating Gemini Enterprise Agent Platform Workbench instances with the terminal enabled. By default, you can enable the terminal on Agent Platform Workbench instances.  
Applicable products | 

  * Organization Policy Service
  * Agent Platform Workbench

  
Path | `constraints/ainotebooks.disableTerminal`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
  
### Restrict environment options on Agent Platform Workbench notebooks and instances

Google control ID | VAI-CO-4.5  
---|---  
Implementation | Required  
Description | The `ainotebooks.environmentOptions` list constraint defines the VM and container image options that you can select when creating Gemini Enterprise Agent Platform Workbench notebooks and instances. You must explicitly specify the options that you want to allow or deny.The expected format for VM instances is: `ainotebooks-vm/PROJECT_ID/IMAGE_TYPE/CONSTRAINED_VALUE`. Replace `IMAGE_TYPE` with `image-family` or `image-name`For example:`ainotebooks-vm/deeplearning-platform-release/image-family/pytorch-1-4-cpu ainotebooks-vm/deeplearning-platform-release/image-name/pytorch-latest-cpu-20200615`The expected format for container images is: `ainotebooks-container/CONTAINER_REPOSITORY:TAG`For example:`ainotebooks-container/gcr.io/deeplearning-platform-release/tf-gpu.1-15:latest ainotebooks-container/gcr.io/deeplearning-platform-release/tf-gpu.1-15:m48`  
Applicable products | 

  * Organization Policy Service
  * Agent Platform Workbench

  
Path | `constraints/ainotebooks.environmentOptions`  
Operator | Is  
Type | List  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
  
### Enforce automatic scheduled upgrades on Agent Platform Workbench user-managed notebooks and instances

Google control ID | VAI-CO-4.6  
---|---  
Implementation | Required  
Description | The `ainotebooks.requireAutoUpgradeSchedule` boolean constraint prevents you from creating Gemini Enterprise Agent Platform Workbench user-managed notebooks and instances without an automatic upgrade schedule.To define a cron schedule for the automatic upgrades, use the `notebook-upgrade-schedule` metadata flag. For example:\--`metadata=notebook-upgrade-schedule="00 19 * * MON"`  
Applicable products | 

  * Organization Policy Service
  * Agent Platform Workbench

  
Path | `constraints/ainotebooks.requireAutoUpgradeSchedule`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * MA-2
  * MA-3

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
  
### Restrict public access on new Agent Platform Workbench notebooks and instances

Google control ID | VAI-CO-4.7  
---|---  
Implementation | Required  
Description | This boolean constraint restricts access from public IP addresses to Gemini Enterprise Agent Platform Workbench notebooks and instances. By default, public IP addresses can access Agent Platform Workbench notebooks and instances.  
Applicable products | 

  * Organization Policy Service
  * Agent Platform Workbench

  
Path | `constraints/ainotebooks.restrictPublicIp`  
Operator | is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20
  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-3.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
  
### Restrict VPC networks on Agent Platform Workbench instances

Google control ID | VAI-CO-4.8  
---|---  
Implementation | Required  
Description | The `ainotebooks.restrictVpcNetworks` list constraint defines the VPC networks that a user can select when creating Gemini Enterprise Agent Platform Workbench instances. By default, a Agent Platform Workbench instance can be created in any VPC network.Use one of the following formats to define an allowed or denied list of networks:

  * `under:organizations/ORGANIZATION_ID`
  * `under:folders/FOLDER_ID`
  * `under:projects/PROJECT_ID`
  * `projects/PROJECT_ID/global/networks/NETWORK_NAME`

  
Applicable products | 

  * Organization Policy Service
  * Agent Platform Workbench

  
Path | `constraints/ainotebooks.restrictVpcNetworks`  
Operator | is  
Type | List  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20
  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-5.1
  * PR.AC-5.2
  * PR.AC-6.1
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-3.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
  
## What's next

  * Review [agent and application controls](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/agents-applications).

  * See more [Google Cloud security best practices and guidelines](https://docs.cloud.google.com/docs/security/security-best-practices-catalog).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
