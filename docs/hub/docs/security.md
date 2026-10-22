---
url: https://docs.cloud.google.com/hub/docs/security/
title: Assess security and compliance status \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:21.838090+00:00
---

# Assess security and compliance status  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  Assess security and compliance status Stay organized with collections  Save and categorize content based on your preferences. 

The **Security & compliance** page in Cloud Hub provides a centralized view of your project's security and compliance posture. This page aggregates key insights from Security Command Center, which helps you quickly identify critical risks. Additionally, you can navigate directly to Security Command Center to address security issues.

For more information about the concepts on this page, see the [Security Command Center overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).

## Before you begin

To view data for Security Command Center in Cloud Hub, ensure that the following steps are complete:

  * Confirm that you have a [project](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project#project_requirements) and verify your Security Command Center service tier for that project.
  * Obtain specific Identity and Access Management (IAM) roles and permissions.



### Security Command Center service tiers

There are multiple [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers): Standard-legacy, Standard, Premium, or Enterprise.

Security Command Center Standard is activated by default, but your activation type might have been upgraded. To confirm your activation type, see [View your current activation type](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#check-scc-activation-level). To change tiers, see [Modify your Security Command Center tier configuration](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#modify-tier). Upgrading to Security Command Center Premium or Enterprise lets you see additional security and compliance insights.

### Required roles

To get the permissions that you need to view security and compliance data from Security Command Center in Cloud Hub, ask your administrator to grant you the [Cloud Hub Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view security and compliance data from Security Command Center in Cloud Hub. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view security and compliance data from Security Command Center in Cloud Hub:

  * `securitycenter.findingsViewer`
  * `securitycenter.assetsViewer`
  * `securitycenter.attackPathsViewer`
  * `cloudsecuritycompliance.viewer`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## About Security Command Center findings in Cloud Hub

A finding is a record of a potential security issue that a Security Command Center service detects. The Security & compliance page in Cloud Hub surfaces the most critical findings relevant to your project, which lets you focus on the highest-priority risks. For detailed investigation and remediation workflows, you can navigate from a finding in Cloud Hub to the Security Command Center interface.

## Use the Security & compliance page

To assess your security status, use the cards on the Security & compliance page to review risks, monitor compliance, and prioritize remediation efforts.

### View findings by severity

The **Findings by severity** card helps you focus on the newest and most serious security risks. The card lists findings, giving higher priority to those detected most recently and those with `Critical` or `High` [severity ratings](https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications).

  1. In the Google Cloud console, go to the **Security & compliance** page.
  2. Review the list of findings on the **Findings by severity** card. Each entry includes the finding severity, category, class, creation time, affected resource, and resource type.
  3. To focus your investigation on a specific area, select a filter: **All** , **Vulnerabilities** , **Identity & access**, **External exposure** , **Misconfigurations** , or **Threats**.



Your Security Command Center service tier determines which filters are available, as listed in the following table:

Security Command Center service tier | Filter  
---|---  
Standard-legacy | All, Vulnerabilities, Identity & access, Misconfigurations  
Standard | All, Vulnerabilities, Identity & access, Misconfigurations  
Premium | All, Vulnerabilities, Identity & access, External exposure, Misconfigurations, Threats  
Enterprise | All, Vulnerabilities, Identity & access, Misconfigurations  
  
You can click any **Finding category** to view comprehensive details and remediation steps in Security Command Center. For information about working with findings, see [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

### Monitor compliance frameworks

The **Frameworks** card helps you monitor your compliance against industry standards and benchmarks. This helps you to identify compliance frameworks that might require attention.

  1. In the Google Cloud console, go to the **Security & compliance** page.
  2. On the **Frameworks** card, review the compliance score and trend for the last 30 days for each listed framework. This information helps you track your compliance posture over time.
  3. To investigate a specific framework, click its name to navigate to the Compliance page in Security Command Center.



### Prioritize top failing cloud controls

The **Top failing cloud controls** card helps you prioritize which security controls to address first.

  1. In the Google Cloud console, go to the **Security & compliance** page.
  2. On the **Top failing cloud controls** card, review the controls with the most open findings. Use this list to determine which failing controls to address to improve your compliance score.
  3. To explore your controls in depth in Security Command Center, click **View cloud controls in Security Command Center**.



## What's next

  * Learn more about [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).
  * Learn about the [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) that Security Command Center uses to detect security issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
