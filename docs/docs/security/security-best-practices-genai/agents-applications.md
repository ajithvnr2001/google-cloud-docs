---
url: https://docs.cloud.google.com/docs/security/security-best-practices-genai/agents-applications/
title: Agents and application controls \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:11:57.215074+00:00
---

# Agents and application controls  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/security-best-practices-genai/agents-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Agents and application controls Stay organized with collections  Save and categorize content based on your preferences. 

This document includes the best practices and guidelines for agents and applications when running workloads on Google Cloud.

### Configure vulnerability scanning for artifacts

Google control ID | AR-CO-6.2  
---|---  
Implementation | Required  
Description | Use Artifact Analysis or another tool to scan for vulnerabilities in images and packages within Artifact Registry.If you use a third-party scanning tool, you must deploy these tools correctly to scan Artifact Registry for vulnerabilities in images and packages.  
Applicable products | 

  * Artifact Registry
  * Artifact Analysis

  
Path | `serviceusage.getservice`  
Operator | =  
Value |  `containerscanning.googleapis.com`  
Related NIST-800-53 controls | 

  * RA-5
  * SI-5
  * SA-5
  * SR-8
  * CA-7

  
Related CRI profile controls | 

  * ID-RA-1.1
  * ID-RA-1.2
  * ID-RA-3.1
  * ID-RA-3.2
  * ID-RA-3.3
  * PR.IP-7.1
  * PR.IP-8.1
  * PR.IP-12.1
  * PR.IP-12.2
  * PR.IP-12.3
  * PR.IP-12.4
  * DE.CM-8.1
  * DE.CM-8.2
  * DE.DP-4.1
  * DE-DP-4.2
  * DE-DP-5.1
  * RS.CO-3.1
  * RS.CO-3.2
  * RS.CO-5.2
  * RS.CO-5.3
  * RS.AN-5.1
  * RS.AN-5.2
  * RS-AN-5.3
  * RS.MI-3.1
  * RS-MI-3.2

  
Related information | 

  * [Artifact analysis and vulnerability scanning](https://docs.cloud.google.com/artifact-registry/docs/analysis)

  
  
### Define permitted private pools

Google control ID | CBD-CO-6.1  
---|---  
Implementation | Required  
Description | The `cloudbuild.allowedWorkerPools` list constraint lets you define the permitted private pools that you can use within your organization, folder, or project.Use one of the following formats to define an allowed or denied list of Worker Pools:

  * `under:organizations/ORGANIZATION_ID`
  * `under:folders/FOLDER_ID`
  * `under:projects/PROJECT_ID`
  * `projects/PROJECT_ID/locations/REGION/workerPools/WORKER_POOL_ID`

  
Applicable products | 

  * Organization Policy Service
  * Cloud Build

  
Path | `constraints/cloudbuild.allowedWorkerPools`  
Operator | =  
Type | String  
Related NIST-800-53 controls | 

  * AC-3
  * AC-5
  * AC-6
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Enforcing the usage of private pools](https://docs.cloud.google.com/build/docs/private-pools/use-in-private-network#enforcing_the_usage_of_private_pools)

  
  
### Define which external services can invoke build triggers

Google control ID | CBD-CO-6.2  
---|---  
Implementation | Required  
Description | The `cloudbuild.allowedIntegrations` constraint defines which external services (for example, GitHub) can invoke build triggers. For example, if your build trigger listens for changes to a GitHub repository and GitHub is denied in this constraint, your trigger won't run. You can specify any number of allowed or denied values for your organization or project.  
Applicable products | 

  * Organization Policy Service
  * Cloud Build

  
Path | `constraints/cloudbuild.allowedIntegrations`  
Operator | =  
Type | List  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Gate builds on organization policy](https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-organization-policy)

  
  
### Enable Model Armor

Implementation | Required  
---|---  
Description | Enable Model Armor to screen for malicious or harmful content in natural language communications, including LLM prompts and responses, MCP server-client connections, or agentic communications.  
Applicable products |  Model Armor  
Path | `serviceusage.getservice`  
Operator | =  
Value |  `modelarmor.googleapis.com`  
Related NIST-800-53 controls | 

  * AC-4
  * AU-2
  * AU-8
  * AU-14
  * CM-6
  * IR-7
  * MP-4
  * MP-6
  * PM-30
  * RA-3
  * RA-5
  * RA-10
  * SA-9
  * SA-11
  * SC-7
  * SC-18
  * SI-3
  * SI-4
  * SI-8
  * SI-10
  * SI-15
  * SI-19

  
Related information | 

  * [Model Armor overview](https://docs.cloud.google.com/model-armor/overview)

  
  
### Configure runtime vulnerability scanning

Google control ID | AR-CO-6.3  
---|---  
Implementation | Required  
Description | Automatically scan the container operating systems and language packages in your running workloads for known vulnerabilities to get actionable mitigation strategies.  
Applicable products |  GKE  
Path | `workload-vulnerability-scanning`  
Operator | ==  
Value |  `Enterprise`  
Related NIST-800-53 controls | 

  * RA-5
  * SI-4
  * SA-5

  
Related information | 

  * [Automatically audit workloads for configuration issues](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration)

  
  
### Create cleanup policies for artifacts

Google control ID | AR-CO-6.1  
---|---  
Implementation | Recommended based on use case  
Description | Cleanup policies are useful if you store many versions of your artifacts but only need to keep specific versions that you release to production. Create separate cleanup policies for deleting artifacts and retaining artifacts.  
Applicable products |  Artifact Registry  
Related NIST-800-53 controls | 

  * SI-12

  
Related CRI profile controls | 

  * PR.IP-2.1
  * PR.IP-2.2
  * PR.IP-2.3

  
Related information | 

  * [Configure cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy)

  
  
## What's next

  * See more [Google Cloud security best practices and guidelines](https://docs.cloud.google.com/docs/security/security-best-practices-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
