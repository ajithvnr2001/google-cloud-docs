---
url: https://docs.cloud.google.com/security-command-center/docs/risk-reports-overview/
title: Risk reports overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:51.883635+00:00
---

# Risk reports overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/risk-reports-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Risk reports overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides an overview of risk reports and the data that is included in them.

Risk reports help you understand the results of the attack path simulations that Security Command Center runs. A risk report starts with a high-level overview, and then the report provides details of sample toxic combinations and associated attack paths.

## When to use risk reports

You can access risk reports in the Google Cloud console. However, you must have [a role with specific permissions](https://docs.cloud.google.com/security-command-center/docs/download-risk-reports#before-you-begin) to download a PDF copy of a risk report. A risk report is useful if you want to share a high-level view of the security landscape of your environment.

**Note:** Risk reports only display data for resources in Google Cloud.

## Sections included in risk reports

Risk reports provide a snapshot of data about your environment in the following sections, ordered to match the layout of the generated report:

### Risk Engine introduction

This section provides an overview of the results of the attack path simulations, including explanations of high-level concepts and how the [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) works.

  * **High-value resource set** : Indicates whether you created resource value configurations.
  * **Sensitive Data Protection** : Generates profiles for your cloud assets so you can determine where sensitive and high-priority security risks exist across your cloud environments.
  * **Valued resources assigned** : Summarizes the valued resources assigned in the latest simulation and the number of resources per resource type.
  * **VPC Service Controls (VPC-SC)** : Creates perimeters to protect resources and data of services that you explicitly specify.
  * **Your risk exposure** : Refers to the following: 
    * The number of successful attack paths.
    * The number of exposed resources with a score that is greater than zero.
    * **Percentage of exposed resource value** : A graph that shows the attack exposure score divided by the resource value over time.
  * **Attack paths graph** : Represents successful attack paths that the Risk Engine identifies on all of your exposed resources in your cloud environment.



### System attack exposure

This section summarizes your organization's exposure score and the percentage of your exposed resources over time. You can see how risk is distributed over projects and which projects and resources have the highest exposure scores.

  * **Attack exposure across your organization over time** : A graph that shows the trend of your organization's exposure score and the percentage of exposed resources.
  * **Project exposure histogram** : A histogram that shows how risk is distributed across your projects.
  * **Most exposed projects** : A table that lists the projects with the most exposed resources and their exposure scores.
  * **Most exposed resources** : A table that lists the resources with the highest exposure scores.



### Entry points and chokepoints

This section summarizes entry points and chokepoints, including suggested mitigations and accompanying descriptions.

  * **Attacker entry points** : This diagram represents common entry points across attack paths. An entry point is the starting point of an attack. The width of the nodes in the diagram indicates their frequency. For more information, see [Types of nodes](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#types_of_nodes).
  * **Entry Point** table: Lists all entry points from the attack path simulations, grouped by type. Provides a description of the entry point and the frequency.
  * **Attack path chokepoints** : This diagram shows the top chokepoints with the highest score. A chokepoint is a resource or resource group where high-risk attack paths converge. If you address these chokepoints, you can mitigate many attack exposures. Displays chokepoints and the affected resource types.
  * **Top chokepoints and suggested mitigations** : This table provides information about the top four chokepoints with the highest scores and suggested mitigations.



### Toxic combination details

This section provides a detailed look into the toxic combination with the highest score.

  * **Toxic combination example** : A toxic combination is a group of security issues that, when they occur together in a particular pattern, create a path to one or more of your high-value resources. A determined attacker could potentially use this path to compromise those resources.

The diagram in the report shows an example attack path from one toxic combination to visualize how an attacker could reach a high-value resource through a combination of attack paths.

  * **Remediate the above toxic combination** : Suggested short-term remediation steps to secure the exposed resources.

  * **Long-term remediations for the above toxic combination** : Suggested strategic remediation steps and security best practices to limit future exposure risk.




### Toxic combination across your environment

This section provides an overview of the top toxic combinations. It also provides an overview of the types of attack steps that appear most in the attack paths.

  * **Toxic combination categories with highest scored issues** : Displays the number of toxic combinations per category and the highest score within each category. This list helps you focus remediation efforts across categories.
  * **Toxic combinations with the highest exposure scores** : Displays the toxic combinations with the highest exposure scores and their primary resource name, type, and exposure score.
  * **Attack step method breakdown** : Displays attack steps that are common across all attack paths and how these steps map to the [MITRE ATT&CK framework](https://attack.mitre.org/). The **Frequency** column indicates what percentage of attack paths they appear in.



## What's next

For more information about what is presented in the risk reports, see the following documentation:

  * [Download risk reports](https://docs.cloud.google.com/security-command-center/docs/download-risk-reports)
  * [Risk Engine feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features)
  * [Toxic combinations and chokepoints overview](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview)
  * [Attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
