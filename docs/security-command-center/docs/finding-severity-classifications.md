---
url: https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications/
title: Finding severities \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:49.225408+00:00
---

# Finding severities  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Finding severities Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the `severity` property of Security Command Center findings and its possible values.

The `severity` property provides a general indicator of how important it is to remediate the findings of a particular finding category or, in some cases, subcategory.

Generally, you should remediate `HIGH` severity findings before `LOW` severity findings, but depending on the affected resource or other considerations, it's possible that remediating a particular `LOW` severity finding might be more important than a `HIGH` severity finding.

## Severity compared to attack exposure score

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

For the Premium and Enterprise (Deprecated) service tiers, you can use both finding severities and finding [attack exposure scores](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores) to prioritize the remediation of findings, but it's important to understand the differences between the two.

A severity is a general indicator that is predetermined based on the category of the finding. The same default severity is assigned to all findings within a given category or subcategory.

An attack exposure score is a dynamic indicator that is calculated for a finding after the finding is generated. The score is specific to the finding instance and is based on a number of factors, including which resource instances the finding affects and the difficulty that a hypothetical attacker would face traversing the path from a potential point of access to the affected high-value resource.

All findings can have a severity. Only vulnerability and misconfiguration findings that are [supported by attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#aes-finding-support) can have an [attack exposure score](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores).

When prioritizing vulnerability and misconfiguration findings, prioritize by attack exposure scores before prioritizing by severity.

## Severity classifications

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Command Center uses the following severity classifications, which are displayed in the **Severity** column when findings are displayed in the Google Cloud console:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Unspecified`



### `Critical` severity

A critical vulnerability is easily discoverable and it can be exploited to result in the direct ability to execute arbitrary code, exfiltrate data, and otherwise gain additional access and privileges in cloud resources and workflows. Examples include publicly accessible user data and public SSH access with weak or no passwords.

A critical threat is able to access, modify, or delete data, or execute unauthorized code within your existing resources.

A critical [`SCC error` class finding](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors) means any of the following:

  * A configuration error prevents Security Command Center from generating new findings of any severity.
  * A configuration error prevents you from seeing all of a service's findings.
  * A configuration error prevents attack path simulations from generating attack exposure scores and attack paths.



### `High` severity

A high-risk vulnerability is easily discoverable and could be exploited with other vulnerabilities to gain direct access to execute arbitrary code or exfiltrate data, and gain additional access and privileges to resources and workloads. For example, a database that has weak or no passwords and is only accessible internally could be compromised by an actor who has access to the internal network.

A high-risk threat is able to create computational resources in an environment, but is not able to access data or execute code in existing resources.

A high-risk `SCC error` class finding indicates that a configuration error is causing any of the following issues:

  * You cannot see or export some of a service's findings.
  * For attack path simulations, the attack exposure scores and attack paths might be incomplete or inaccurate.



### `Medium` severity

A medium-risk vulnerability could allow an actor to gain access to resources or privileges that enable them to eventually gain access and the ability to exfiltrate data or execute arbitrary code. For example, if a service account has unnecessary access to projects and an actor gains access to the service account, the actor could use that service account to manipulate a project.

A medium-risk threat could lead to a more severe issue, but might not indicate current data access or unauthorized code execution.

### `Low` severity

A low-risk vulnerability hampers a security team's ability to detect vulnerabilities or active threats in their deployment, or prevents the root cause investigation of security issues. For example, a scenario in which monitoring and logs are disabled for resource configurations and access.

A low-risk threat has obtained minimal access to an environment, but isn't able to access data, execute code, or create resources.

### `Unspecified` severity

A severity classification of `Unspecified` indicates that the service that generated the finding did not set a severity value for the finding.

If you get a finding with a severity of `Unspecified`, you need to assess the severity yourself by investigating the finding and reviewing any documentation that the product or service that generated the finding provides.

## Variable severity

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The severity of the findings in a finding category can vary under certain circumstances.

### Severities that vary based on attack exposure score

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

For the Enterprise (Deprecated) service tier, the severity levels of vulnerability and misconfiguration findings reflect more accurately the risk of each individual finding, because the severity of a finding can change to reflect the finding's attack exposure score.

Vulnerability and misconfiguration findings are generated with a default or baseline severity level that is common to all of the findings within a given finding category. After a finding is generated, if the attack path simulations of Security Command Center determine that the finding exposes one or more resources that you have designated as a [_high-value resource_](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#high-value_resources), the simulations assign an attack exposure score to the finding and increase the severity level accordingly. If the finding remains active, but the simulations later reduce the attack exposure score, the severity level of the finding can also decrease, but no lower than the original default level.

For other service tiers, the severity levels of all findings remain static.

### Severities that vary based on the detected issue

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

For a few finding categories, Security Command Center can assign a different default severity level to a finding depending on the particulars of the security issue that was detected.

For example, the severity classification of the [`IAM anomalous grant` finding](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-grant) that is generated by Event Threat Detection is usually `HIGH`. But if the finding is generated for the granting of sensitive permissions to a [custom IAM role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), the severity is `MEDIUM`.

## View finding severities in the Google Cloud console

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You can view Security Command Center findings by severity in several ways in the Google Cloud console:

### Standard and Standard-legacy

  * On the [**Overview** page](https://docs.cloud.google.com/security-command-center/docs/assess-risk), you can see how many findings at each severity level are active in your resources in the **All Risk > Top misconfigurations** section.

  * On the [**Findings** page](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings), you can add filters for specific severity levels to your findings queries from the **Quick filters** panel.

  * On the [**Vulnerabilities** page](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#vulnerabilities-page), you can filter the displayed vulnerability detection modules by severity level to show only the modules that have active findings at that severity level.




### Premium

  * On the **Risk Overview >** [**Threats** dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats), you can see how many threat findings exist at each severity level.

  * On the [**Findings** page](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings), you can add filters for specific severity levels to your findings queries from the **Quick filters** panel.

  * On the [**Issues** page](https://docs.cloud.google.com/security-command-center/docs/issues-overview), you can select an issue, and then view the findings, including the severity, in the **Findings** panel.

  * On the [**Vulnerabilities** page](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#vulnerabilities-page), you can filter the displayed vulnerability detection modules by severity level to show only the modules that have active findings at that severity level.




###  Enterprise 

  * On the **Risk Overview >** [**Threats** dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats), you can see how many threat findings exist at each severity level.

  * On the [**Findings** page](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings), you can add filters for specific severity levels to your findings queries from the **Quick filters** panel.

  * On the [**Vulnerabilities** page](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#vulnerabilities-page), you can filter the displayed vulnerability detection modules by severity level to show only the modules that have active findings at that severity level.

  * On the [**Issues** page](https://docs.cloud.google.com/security-command-center/docs/issues-overview), you can select an issue, and then view the findings, including the severity, in the **Findings** panel.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
