---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats/
title: Investigate and respond to threats \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:37.978844+00:00
---

# Investigate and respond to threats  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Investigate and respond to threats Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how to investigate and respond to threat findings in Security Command Center. To handle a threat, you typically do the following:

  1. Review the finding details.
  2. Consult available guidance.
  3. Identify related risks in your environment.
  4. Take action to remediate the threat and help secure your resources.



## Before you begin

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You need the required Identity and Access Management (IAM) roles to view or edit findings and logs, and modify Google Cloud resources. If you encounter access errors in Security Command Center, ask your administrator for assistance and see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control) to learn about roles. To resolve resource errors, read the documentation for the affected products.

## Review the finding

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To start investigating a threat, review the details that Security Command Center provides in the [finding](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

To review a threat finding, follow these steps:

  1. In the Google Cloud console, go to the Security Command Center **Findings** page. 

[ Go to Findings](https://console.cloud.google.com/security/command-center/findings)

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

  2. If necessary, select your Google Cloud project, folder, or organization.

  3. In the **Quick filters** section, click an appropriate filter to display the finding that you need in the **Findings query results** table. For example, if you select **Event Threat Detection** or **Container Threat Detection** in the **Source display name** subsection, only findings from the selected service appear in the results.

The table is populated with findings for the source you selected.

  4. To view details of a specific finding, click the finding name under **`Category`**. The finding details pane expands to display a summary of the finding's details.

  5. To view the finding's JSON definition, click the **JSON** tab.




Findings provide the names and numeric identifiers of resources that are involved in an incident, along with environment variables and asset properties. You can use that information to isolate affected resources and determine the potential scope of an event.

To aid in your investigation, threat findings also contain links to the following external resources:

  * [MITRE ATT&CK](https://attack.mitre.org/) framework entries. The framework explains techniques for attacks against cloud resources and provides remediation guidance.
  * [VirusTotal](https://www.virustotal.com/gui/home/search), an Alphabet-owned service that provides context on potentially malicious files, URLs, domains, and IP addresses. If available, the **VirusTotal Indicator** field provides a link to VirusTotal to help you further investigate potential security issues.

VirusTotal is a separately-priced offering with its own usage limits and features. You are responsible for understanding and adhering to VirusTotal's API usage policies and any associated costs. For more information, see the [VirusTotal documentation](https://docs.virustotal.com/).

**Note:** VirusTotal might not contain hashes for all malware variants.



## Consult investigation guidance

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

After reviewing the finding details, consult the investigation and response recommendations that Security Command Center provides.

Security Command Center offers informal guidance to help you investigate findings. These findings identify suspicious activities in your Google Cloud environment from potentially malicious actors. Following the guidance can help you understand what happened during a potential attack and develop possible responses for affected resources.

**Note:** The techniques that Security Command Center provides aren't guaranteed to be effective against any previous, current, or future threats that you face. For information about why Security Command Center does not provide official remediation guidance for threats, see [Approach to threat finding remediation](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#remediating_threats).

To view the investigation and response recommendations for a finding, locate the finding in the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).

You can also view high-level response recommendations for the following types of threat findings:

  * [AI threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-ai-threats)
  * [Cloud Run threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-cloud-run-threats)
  * [Compute Engine threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-compute-engine-threats)
  * [Google Kubernetes Engine threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-gke-threats)
  * [Google Workspace threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-google-workspace-threats)
  * [Network threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-network-threats)

**Note:** Security Command Center doesn't provide recommendations for findings generated by [ custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview), because your organization defines the recommended actions for those detectors.

## Review threats using the Threats dashboard

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The **Threats** dashboard on the **Risk Overview** page helps you monitor, prioritize, and investigate potentially harmful events in your Google Cloud environment.

To access the **Threats** dashboard, follow these steps:

  1. In the Google Cloud console, go to the Security Command Center **Threats** page.

[ Go to Threats](https://console.cloud.google.com/security/command-center/threats)

  2. If necessary, select your Google Cloud project, folder, or organization.




You can use the following sections to identify and prioritize your threat investigations:

  * **New threats over time** : Shows potentially harmful events in your resources over a time period that you specify. The default time period is seven days. To change the specified time period, use the **Time range** field. This panel helps you identify sudden spikes in threat activity.
  * **Top Threats** : Shows the following information to help you identify critical issues: 
    * **Threats by severity** : Shows the number of threat findings in each severity level (for example, `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`). Selecting a severity level filters findings so that you can focus on the highest-priority risks first.
    * **Threats by category** : Shows the number of findings classified by specific threat types across all projects.
    * **Threats by project** : Shows the number of findings for each project in your organization. This is useful for identifying the projects that are experiencing the most threat activity.



Clicking on data elements within these panels applies the relevant filters and redirects you to the **Findings** page where you can continue a deeper investigation of specific threat findings.

## Identify related risks

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To help you understand the context of a threat and keep threats from reoccurring, review and respond to related vulnerability and misconfiguration findings. These findings might indicate security weaknesses that allowed the threat to occur or that could be exploited in the future.

To locate related vulnerability and misconfiguration findings, follow these steps:

### Locate the finding attribute

  1. In the Google Cloud console, go to the Security Command Center **Findings** page.

[ Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Review the threat finding and copy the value of an attribute that is likely to appear in any related vulnerability or misconfiguration finding, such as the principal email address or the name of the affected resource.




### Build the finding filter

  1. On the **Findings** page, open the **Query editor** by clicking **Edit query**.
  2. Click **Add filter**. The **Select filter** menu opens.
  3. From the list of filter categories on the left side of the menu, select the category that contains the attribute that you noted in the threat finding.

For example, if you noted the full name of the affected resource, select **Resource**. The attribute types of the **Resource** category are displayed in the column to the right, including the **Full name** attribute.

  4. From the displayed attributes, select the type of attribute that you noted in the threat finding. A search panel for attribute values opens to the right and displays all found values of the selected attribute type.

  5. In the **Filter** field, paste the attribute value that you copied from the threat finding. The displayed list of values is updated to show only the values that match the pasted value.

  6. From the list of displayed values, select one or more values and click **Apply**. The **Findings query results** panel updates to show only the matching findings.




### Refine the results by finding class

If a large number of findings appear in the results, filter the findings by selecting additional filters from the **Quick filters** panel.

For example, to show only the `Vulnerability` and `Misconfiguration` class findings that contain the selected attribute values, go to the **Finding class** section of the **Quick filters** panel and select **Vulnerability** and **Misconfiguration**.

## Respond to the threat

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

After you review the finding, consult investigation guidance, and identify related risks, you need to respond to the threat and manage the lifecycle of the finding in Security Command Center.

### Approach to threat finding remediation

Unlike vulnerability and misconfiguration findings, Security Command Center doesn't provide official remediation guidance for threat findings. The informal guidance that Security Command Center provides isn't guaranteed to be effective against any previous, current, or future threats.

Misconfigurations and compliance violations identify weaknesses in resources that could be exploited. Typically, misconfigurations have known fixes, like enabling a firewall or rotating an encryption key.

Threats differ from vulnerabilities in that they're dynamic and indicate a possible active exploit against one or more resources. A remediation recommendation might not be effective in securing your resources because the exact methods used to achieve the exploit might not be known.

For example, an `Added Binary Executed` finding indicates that an unauthorized binary was launched in a container. A basic remediation recommendation might advise you to quarantine the container and delete the binary, but that might not resolve the underlying root cause that allowed the attacker access to execute the binary. You need to find out how the container image was corrupted to fix the exploit. Determining whether the file was added through a misconfigured port or by some other means requires a thorough investigation. An analyst with expert-level knowledge of your system might need to review it for weaknesses.

Bad actors attack resources using different techniques, so applying a fix for a specific exploit might not be effective against variations of that attack. For example, in response to a `Brute Force: SSH` finding, you might lower permission levels for some user accounts to limit access to resources. However, weak passwords might still provide an attack path.

The breadth of attack vectors makes it difficult to provide remediation steps that work in all situations. Security Command Center's role in your cloud security plan is to identify impacted resources in near-real time, tell you what threats you face, and provide evidence and context to aid your investigations. However, your security personnel must use the extensive information in Security Command Center findings to determine the best ways to remediate issues and secure resources against future attacks.

**Note:** In the Enterprise (Deprecated) service tier, threat findings that match specific criteria appear as [Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)), which provide remediation recommendations that map to MITRE ATT&CK tactics.

### Deactivate or mute a finding

After you resolve an issue that triggered a threat finding, Security Command Center does not automatically set the state of the finding to `INACTIVE`. The state of a threat finding remains `ACTIVE` unless you manually [change the finding's state](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#change-state) to `INACTIVE`.

For a false positive, consider leaving the state of the finding as `ACTIVE` and instead [mute the finding](https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings#mute-findings).

For persistent or recurring false positives, [create a mute rule](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#create_a_mute_rule). Setting a mute rule can reduce the number of findings that you need to manage, which makes it easier to identify a true threat when one occurs.

For a true threat, before you set the state of the finding to `INACTIVE`, eliminate the threat and complete a thorough investigation of the detected threat, the extent of the intrusion, and any other related findings and issues.

## What's next

  * [Threat detection in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/overview-threats)
  * [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index)
  * [Correlated threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
