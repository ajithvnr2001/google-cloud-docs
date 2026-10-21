---
url: https://docs.cloud.google.com/security-command-center/docs/vulnerabilities-prioritize-remediation/
title: Prioritize the remediation of vulnerabilities \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:58.994345+00:00
---

# Prioritize the remediation of vulnerabilities  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/vulnerabilities-prioritize-remediation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Prioritize the remediation of vulnerabilities Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains some of the information and methods that you can use to prioritize Security Command Center findings of software vulnerabilities, misconfigurations, and, with the Premium and Enterprise (Deprecated) service tiers, toxic combinations and chokepoints (_issues_ , collectively). You can use this information to help reduce risk and help improve your security posture relative to your compliance needs.

## The purpose of prioritization

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Because your time is limited and the volume of Security Command Center issues can be overwhelming, especially in larger organizations, you need to quickly identify and respond to the vulnerabilities that pose the greatest risk to your organization.

You need to fix vulnerabilities to reduce the risk of a cyberattack on your organization and to maintain your organization's compliance with applicable security standards.

To effectively reduce the risk of a cyberattack, you need to find and fix the vulnerabilities that expose your resources the most, that are most exploitable, or that would result in the most severe damage if they were to be exploited.

To effectively improve your security posture with respect to a particular security standard, you need to find and fix the vulnerabilities that violate the controls of the security standards that apply to your organization.

In the Premium and Enterprise (Deprecated) service tiers, issues help you complete these tasks by providing detailed information about the toxic combinations and chokepoints that are detected in your organization. An issue can also include the severity; the attack exposure score; and [CVE records](https://www.cve.org/ResourcesSupport/Glossary) with CVE assessments by Mandiant ([Preview](https://cloud.google.com/products/#product-launch-stages)).

**Note:** In the Premium service tier, toxic combinations, chokepoints, and attack exposure scores are available in findings with a `Critical` severity level.

The following sections explain how you can prioritize Security Command Center issues to meet these purposes.

## Prioritize by attack exposure scores

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Generally, prioritize the remediation of an issue that has a high attack exposure score over an issue finding that has a lower score or no score.

For more information, see the following:

  * [Using scores to prioritize finding remediations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#using_scores_to_prioritize_finding_remediations)
  * [Attack exposure scores on toxic combinations and chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview#toxic-combination-attack-exposure-score)



### View scores in Security Command Center Google Cloud console

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The scores appear with the findings in multiple places, including the following:

  * On the **Risk overview** page.
  * In a column on the **Findings** page in Security Command Center, where you can query and sort findings by score.



To see the findings that have the highest attack exposure scores, follow these steps:

  1. Go to the **Risk overview** page in the Google Cloud console:

[Go to Risk overview](https://console.cloud.google.com/security/command-center/overview)

  2. Use the project selector in the Google Cloud console to select the project, folder, or organization for which you need to prioritize vulnerabilities.

The **Riskiest Issues** section displays issues that have the highest attack exposure scores.

  3. Select an issue, then click **View issue detail** to open the attack path details page and the **Attack exposure score**.

  4. Click **View All** to view a list of all issues with the attack exposure score for each.




For more information about the **Risk overview** page, see [Assess risk at a glance](https://docs.cloud.google.com/security-command-center/docs/assess-risk).

### View scores in cases

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

In the Security Operations console, you work primarily with _cases_ , in which findings are documented as _alerts_.

In the Enterprise (Deprecated) service tier, you can view the toxic combination cases with the top attack exposure scores on the **Risk > Cases** page. You can sort the cases by their attack exposure scores.

For information about how to query for toxic combination cases specifically, see [View the details of a toxic combination case](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-manage#view_the_details_of_a_toxic_combination_case).

## Prioritize by CVE exploitability and impact

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Generally, prioritize the remediation of findings that have a CVE assessment of high-exploitability and high-impact over findings with a CVE assessment of low-exploitability and low-impact.

CVE information, including exploitability and impact assessments of the CVE that are provided by Mandiant, are based on the software vulnerability itself.

On the **Overview** page, under the **Vulnerabilities** dashboard, the **Top Common Vulnerabilities and Exploits** _heatmap_ summarizes vulnerability findings into blocks by the exploitability and impact assessments that are provided by Mandiant.

When you view the details of a software vulnerability finding in the Google Cloud console, you can find the CVE information in the **Vulnerability** section of the **Summary** tab. In addition to impact and exploitability, the **Vulnerability** section includes the CVSS score, references links, and other information about the CVE vulnerability definition.

To quickly identify the findings that have the highest impact and exploitability, follow these steps:

  1. In the Google Cloud console, go to the **Risk overview** page.

[Go to Risk overview](https://console.cloud.google.com/security/command-center/overview)

  2. Use the project selector in the Google Cloud console to select the project, folder, or organization for which you need to prioritize vulnerabilities.

  3. On the **Risk Overview** page, click **Vulnerabilities**.

     * In the **Top Common Vulnerabilities and Exploits** panel, do the following:

       1. Click the block with a non-zero number that has the highest exploitability and impact. The panel displays only those findings that have the selected impact and exploitability.

       2. Click the count in the **Findings** column. The **Findings** page opens to display the list of findings that share that CVE ID.

     * In the **Latest Compute Vulnerabilities with Known Exploits** section, click a resource ID in the **Virtual Machine** column. The asset details pane opens to display information about that asset.




## Prioritize issues by severity

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Generally, prioritize an issue or finding with a `CRITICAL` severity over an issue or finding with a `HIGH` severity, prioritize `HIGH` severity over a `MEDIUM` severity, and so forth.

Severities are based on the type of security issue and are assigned to finding categories by Security Command Center. All findings in a particular category or subcategory are generated with the same severity level.

Unless you are using the Enterprise (Deprecated) service tier, finding severity levels are static values that don't change over the life of the finding.

In the Enterprise (Deprecated) service tier, the severity levels of issues more accurately represent the real-time risk of a finding. The findings are generated with the default severity level of the finding category, but, while the finding remains active, the severity level can increase or decrease as the attack exposure score of the finding increases or decreases.

Perhaps the easiest way to identify the highest severity vulnerabilities is to use **Quick filters** on the **Findings** page in the Google Cloud console.

To view the highest severity findings, follow these steps:

  1. Go to the **Findings** page in the Google Cloud console:

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Use the project selector in the Google Cloud console to select the project, folder, or organization for which you need to prioritize vulnerabilities.

  3. In the **Quick filters** panel on the **Findings** page, select the following properties:

     * Under **Finding class** , select **Vulnerability**.
     * Under **Severity** , select **Critical** , **High** , or both.

The **Findings query results** panel updates to show only findings that have the specified severity.




## Prioritize to improve compliance

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When prioritizing posture findings for compliance, your main concern is the findings that violate the controls of the applicable compliance standard.

You can see the findings that violate the controls of a particular benchmark by following these steps:

  1. Go to the **Compliance** page in the Google Cloud console:

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance)

  2. Use the project selector in the Google Cloud console to select the project, folder, or organization for which you need to prioritize vulnerabilities.

  3. Next to the name of the security standard that you need to comply with, click **View details**. The **Compliance details** page opens.

  4. If the security standard you need is not displayed, specify the standard in the **Compliance standard** field on the **Compliance detail** page.

  5. Sort the listed rules by **Findings** by clicking the column heading.

  6. For any rule that shows one or more findings, click the rule name in the **Rules** column. The **Findings** page opens to display the findings for that rule.

  7. Remediate the findings until there are no findings left. After the next scan, if no new vulnerabilities are found for the rule, the percentage of controls passed increases.




## What's next

  * [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings)
  * [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate)
  * [Assess risk using Risk overview dashboards](https://docs.cloud.google.com/security-command-center/docs/assess-risk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
