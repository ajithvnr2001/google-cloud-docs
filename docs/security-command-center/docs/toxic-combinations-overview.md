---
url: https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview/
title: Toxic combinations and chokepoints overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:42.927681+00:00
---

# Toxic combinations and chokepoints overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Toxic combinations and chokepoints overview Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

_Toxic combinations_ are a group of security issues that, when they occur together in a particular pattern, creates a path to one or more of your high-value resources that a determined attacker could potentially use to compromise those resources.

The Risk Engine detects toxic combinations during the [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_path_simulations) that it runs. For each toxic combination that Risk Engine detects, it generates a finding. Each toxic combination includes a unique attack exposure score, called a _toxic combination score_ , that measures the risk of the toxic combination to the high-value resource set in your cloud environment. Risk Engine also generates a visualization of the attack path that the toxic combination creates to the resources in your high-value resource set.

_Chokepoints_ are similar to toxic combinations, but focus on common resources or resource groups where multiple attack paths converge. As a consequence, remediating a chokepoint can remediate multiple toxic combinations.

Toxic combinations and chokepoints are detected for the following cloud service provider platforms:

  * Google Cloud. Available for Premium and Enterprise (Deprecated) service tiers.
  * Amazon Web Services (AWS) ([Preview](https://cloud.google.com/products/#product-launch-stages)). Available for Enterprise (Deprecated) service tier.
  * Microsoft Azure ([Preview](https://cloud.google.com/products/#product-launch-stages)). Available for Enterprise (Deprecated) service tier.



For the list of supported resources, see [Risk Engine feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#cloud-support).

## View toxic combinations and chokepoints

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The highest risk toxic combinations and chokepoints are displayed as [issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview) on the Security Command Center **Risk Overview** and **Issues** pages in the console.

In the Enterprise (Deprecated) service tier, you also view toxic combinations on the **Cases** page in the Security Operations console.

Toxic combinations can also be viewed on the **Cases** page in the Enterprise (Deprecated) service tier.

To view findings that are related to toxic combinations and chokepoints in the Google Cloud console, go to the [**Findings**](https://console.cloud.google.com/security/command-center/findingsv2) page and filter by the **Toxic combination** or **Chokepoint** finding class.

Findings that are related to toxic combinations and chokepoints are captured in risk reports. For more information, see [Risk reports overview](https://docs.cloud.google.com/security-command-center/docs/risk-reports-overview).

## Attack exposure scores on toxic combinations and chokepoints

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Risk Engine calculates an attack exposure score for each toxic combination and chokepoint. This score is a measure of how much a toxic combination or chokepoint exposes one or more of the resources in your high-value resource set to potential attacks. The higher the score, the higher the risk.

**Note:** For toxic combinations, attack exposure scores are also called _toxic combination scores_ in some contexts, such as the **Findings** page of the Google Cloud console.

### Attack exposure score calculation

Attack exposure scores for toxic combinations and chokepoints are derived from the following:

  * The number of resources in your high-value resource set that are exposed and the priority values and attack exposure scores of those resources.
  * The likelihood that a determined attacker could succeed in reaching a high-value resource by leveraging the toxic combination or chokepoint.



Based on the attack exposure score, toxic combinations can have one of the following severities assigned to them:

  * **Critical** : Toxic combinations with an attack exposure score ≥ 10.
  * **High** : Toxic combinations with an attack exposure score < 10.



Chokepoints always have an attack exposure score ≥ 10, and so always have a critical severity rating.

For more information, see [Attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores).

## Attack path visualizations for toxic combinations and chokepoints

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Risk Engine provides a visual depiction of the toxic combination and chokepoint attack paths that lead to your high-value resource set. An attack path represents a series of attack steps that include related security issues and resources that a potential attacker could use to reach your resources.

Attack paths help you to understand the relationships between individual security issues in a toxic combination or chokepoint, and how they form paths to resources in your high-value resource set. The path visualization also shows you how many valued resources are exposed and their relative importance to your cloud environment.

Resources on an attack path are color-coded in the following way:

  * Resources with security issues that contribute to a toxic combination are highlighted with a yellow border.
  * Resources that are identified as a chokepoint are highlighted with a red border.



There are multiple places where you can view attack paths.

In the Premium service tier, view the full attack path on the **Attack paths** page. For more information, see [Attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_paths). Also, view a simplified version of the attack path in the following places:

  * The **Risk Overview** page, for items in the **Riskiest issues** widget.
  * The **Issues** page, when an issue is selected. You can access the simplified attack path in the **Overview** tab of the issue.



In the Enterprise (Deprecated) service tier, view a simplified version of the attack path in the following places:

  * The **Risk > Overview** page, for items in the **Riskiest issues** widget.
  * The **Risk > Issues** page, when an issue is selected. You can access the simplified attack path in the **Overview** tab of the issue.
  * The **Risk > Cases** page, when a case is selected. You can access the simplified attack path in the ![Case](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/case.svg)**Case overview** tab.



To view the full version of an attack path, view the simplified version, and then click **Explore full attack paths**.

The following screenshot is an example of a simplified attack path for a toxic combination:

![A simplified toxic combination attack
path](https://docs.cloud.google.com/static/security-command-center/images/attack-path-simplified.png)

The following screenshot is an example of a simplified attack path for a chokepoint:

![A simplified chokepoint attack
path](https://docs.cloud.google.com/static/security-command-center/images/chokepoint-simplified.png)

## Related findings

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Many of the individual risks that make up toxic combinations and chokepoints are also detected by other Security Command Center detection services. These other detection services generate separate findings for these risks, which are listed in issues and cases as related findings. Related findings are also identified in attack paths.

For toxic combinations, separate cases are opened for the related findings, different playbooks are run, and other members of your team might be working on their remediation independently from the remediation of the toxic combination finding. Check the status of the cases for these related findings and, if necessary, ask the owners of the cases to prioritize their remediation to help resolve the toxic combination.

## Cases

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

In the Enterprise (Deprecated) service tier, Security Command Center opens a case for each toxic combination finding that's generated. Chokepoints don't generate cases.

In the case detail view, you can find the following information related to toxic combinations:

  * A description of the toxic combination
  * The attack exposure score of the toxic combination
  * A visualization of the attack path that the toxic combination creates
  * Information about the affected resources
  * Information about the steps you can take to remediate the toxic combination
  * Information about any related findings from other Security Command Center detection services, including links to their associated cases
  * Applicable playbooks
  * Associated tickets



On the **Risk > Cases** Security Operations console page, you can query or filter toxic combination cases by using the **Toxic Combination** tag. You can also visually identify toxic combination cases in the case list by the following icon: ![Toxic combination
icon](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/toxic-combination.svg).

For more information about viewing toxic combination cases, see [View toxic combination cases](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-manage#view-cases).

### Case priority

By default, toxic combination cases have their priority set to the same value as the severity of the toxic combination finding and its associated alert in the related case. This means that all toxic combination cases initially have a priority of `Critical` or `High`.

After a case is opened, you can change the priority of the case or of the alert. Changing the priority of a case or an alert does not change the severity of the finding.

### Closing cases

When a finding is first generated for a toxic combination, its state is `Active`.

If you remediate the toxic combination, Risk Engine automatically detects the remediation during the next attack path simulation and closes the case. Simulations run approximately [every 48 hours](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#simulation_schedule).

Alternatively, if you determine that the risk posed by a toxic combination is acceptable or unavoidable, you can close a case by muting the finding.

When you mute a finding, the finding remains active, but Security Command Center closes the case and omits the finding from default queries and views.

For more information, see the following information:

  * [How to close toxic combination cases](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-manage#close_toxic_combination_cases)
  * [Cases overview](https://docs.cloud.google.com/security-command-center/docs/cases-overview)
  * [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings)



## What's next

  * Learn more about [attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

  * Learn more about how to [manage toxic combinations and chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-manage).

  * Learn more about [Risk Engine feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features).

  * Learn how to [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
