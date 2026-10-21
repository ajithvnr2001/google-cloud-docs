---
url: https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-manage/
title: Manage toxic combinations and chokepoints \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:20.497043+00:00
---

# Manage toxic combinations and chokepoints  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Manage toxic combinations and chokepoints Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides instructions for identifying and responding to toxic combinations and chokepoints by using the following pages:

  * Issues, available on the Premium and Enterprise (Deprecated) service tiers.
  * Cases, available on the Enterprise (Deprecated) service tier.
  * Findings, available on the Premium and Enterprise (Deprecated) service tiers.



## Before you begin

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To ensure that the detection of toxic combinations and chokepoints is accurate, check that the security operations component software is up to date, your high-value resource set is designated accurately, and that you have the proper IAM permissions.

### Optional: Collect data from other clouds

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Risk Engine supports running simulations on data from Amazon Web Services (AWS) ([Preview](https://cloud.google.com/products/#product-launch-stages)) and Microsoft Azure ([Preview](https://cloud.google.com/products/#product-launch-stages)) to identify toxic combinations and chokepoints.

Configure the connection from Security Command Center to these cloud providers to collect resource and configuration data. For information about setting up the connections, see the following:

  * [Connect to AWS for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws)
  * [Connect to Microsoft Azure for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure)



For the list of supported resources, see [Risk Engine feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#cloud-support).

### Obtain the required permissions

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To work with toxic combinations and chokepoints, you need permissions that grant access to Security Command Center and Google SecOps features.

#### Security Command Center IAM roles

To get the permissions that you need to work with toxic combinations and chokepoints, ask your administrator to grant you the following IAM roles on your organization: 

  * View attack paths: 
    * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
    * [Security Center Attack Paths Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.attackPathsViewer) (`roles/securitycenter.attackPathsViewer`)
    * [Security Center Findings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)
  * View attack path findings: 
    * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
    * [Security Center Attack Paths Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.attackPathsViewer) (`roles/securitycenter.attackPathsViewer`)
    * [Security Center Findings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)
  * View findings: 
    * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
    * [Security Center Findings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)
  * Mute findings: 
    * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
    * [Security Center Findings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)
    * [Security Center Findings Mute Setter ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsMuteSetter) (`roles/securitycenter.findingsMuteSetter`)
  * View resources: 
    * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
    * [Security Center Findings Mute Setter ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsMuteSetter) (`roles/securitycenter.findingsMuteSetter`)
  * Edit findings: 
    * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
    * [Security Center Findings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)
    * [Security Center Findings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Security Command Center roles and permissions, see [IAM for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org).

#### Google SecOps IAM roles

For the Enterprise (Deprecated) service tier, to work with toxic combinations and cases, you need any one of the following roles:

  * **Chronicle SOAR Vulnerability Manager** (`roles/chronicle.soarVulnerabilityManager`)
  * **Chronicle SOAR Threat Manager** (`roles/chronicle.soarThreatManager`)
  * **Chronicle SOAR Admin** (`roles/chronicle.soarAdmin`)



For information about granting the role to a user, see [Map and authorize users using IAM](https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops).

### Install the latest security operations use case

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The toxic combination feature requires the June 25, 2024, or later release of the **SCC Enterprise – Cloud Orchestration and Remediation** use case.

For information about installing the use case, see [Update Enterprise use case, June 2024](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update#install_the_latest_use_case_version).

### Specify your high-value resource set

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You don't need to enable the detection of toxic combinations and chokepoints—it's always on. Risk Engine automatically detects toxic combinations and chokepoints that expose a default high-value resource set.

Toxic combination and chokepoint findings generated based on the default high-value resource set are unlikely to accurately reflect your security priorities. To specify which resources are part of your high-value resource set, you create _resource value configurations_ in the Google Cloud console. For instructions, see [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).

## Remediate toxic combinations and chokepoints

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Toxic combinations and chokepoints can expose many high-value resources to potential attackers. You should remediate them before other risks in your cloud environments.

You can prioritize the order in which you remediate toxic combinations and chokepoints based on their attack exposure score. How you do this changes depending on where you view toxic combinations and chokepoints.

To remediate a toxic combination or chokepoint finding, remediate the underlying vulnerabilities, misconfigurations, or external exposure findings along the simulated attack path. When the Risk Engine runs a subsequent attack path simulation and identifies that the path to the high-value resources no longer exists, it automatically changes the state of the toxic combination or chokepoint finding from `ACTIVE` to `INACTIVE`.

###  Issues 

For the Premium and Enterprise (Deprecated) service tiers, you can access the highest risk toxic combinations and chokepoints (displayed as [issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview)) on the following pages:

  * Enterprise (Deprecated) service tier: **Risk > Overview** page
  * Premium service tier: **Security Command Center > Risk Overview**



All toxic combinations and chokepoints can be viewed on the **Risk > Issues** page.

To remediate an issue, complete the following instructions:

###  Premium 

**View all issues**

  1. To view all issues, go to the Security Command Center **Issues** page. 

[Go to Issues](https://console.cloud.google.com/security/command-center/issues)

  2. Select your Google Cloud organization.



**Sort by attack exposure score**

  1. By default, grouped issues are ranked by severity. Within the group, the issues are ranked by attack exposure score. To sort all issues by attack exposure score instead, disable **Group by detections**.
  2. Select an issue.
  3. Review the issue's description and evidence.



**Access further information**

  1. If there are related findings, view their details.
  2. If multiple critical issues are found on a primary resource in a toxic combination or chokepoint, a message appears after the **Evidence** diagram. To optimize your remediation efforts, click **Filter issues for this primary resource** in this message to focus on resolving issues for that specific resource. Click the back arrow near ![Open filter
      panel](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg)**Add filter** when you want to remove the filter.
  3. Click **Explore full attack paths** in the **Evidence** diagram for an in-depth understanding of the issue, and how the attack paths expose high-value resources.
  4. Click **How to fix** , and follow the guidance to help mitigate the risk.



###  Enterprise 

**View all issues**

  1. To view all issues, go to the Security Command Center **Risk > Issues** page. 

[Go to Issues](https://console.cloud.google.com/security/command-center/issues)

  2. Select your Google Cloud organization.



**Sort by attack exposure score**

  1. By default, grouped issues are ranked by severity. Within the group, the issues are ranked by attack exposure score. To sort all issues by attack exposure score instead, disable **Group by detections**.
  2. Select an issue.
  3. Review the issue's description and evidence.



**Access further information**

  1. If there are related findings, view their details.
  2. If multiple critical issues are found on a primary resource in a toxic combination or chokepoint, a message is displayed after the **Evidence** diagram. To optimize your remediation efforts, click **Filter issues for this primary resource** in this message to focus on resolving issues for that specific resource. Click the back arrow near ![Open filter
      panel](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg)**Add filter** when you want to remove the filter.
  3. Click **Explore full attack paths** in the **Evidence** diagram for an in-depth understanding of the issue, and how the attack paths expose high-value resources.
  4. Click **How to fix** , and follow the guidance to help mitigate the risk.



###  Cases 

For the Enterprise (Deprecated) service tier, you can view all toxic combination cases by going to the **Cases** page. Chokepoints don't automatically generate a case, and should be viewed on the **Issues** page.

To find toxic combinations in cases, complete the following instructions:

  1. In the Google Cloud console, go to **Risk > Cases**. The **Cases** Security Operations console page opens.
  2. In the list of cases, click ![Open filter panel](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg)**Cases filter** to open the filter panel. The **Case queue filter** panel opens.
  3. In the **Case queue filter** , specify the following: 1\. In the **Time frame** field, specify the time period during which the case is active. 1\. Set **Logical operator** to **AND**. 1\. In the filter key list box, select **Tags**. 1\. Set the equality operator to **is**. 1\. In the filter value list box, select **Toxic combination**. 1\. Click **Apply**. The cases in the case queue are updated to show only the cases that match the filter you specified.
  4. Click **Sort** next to ![Open filter panel](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg)**Cases filter** , and select **Sort by attack exposure (high to low)**.
  5. From the case queue, click the case you want to see. If you are viewing cases in **List view** , click the case ID instead. The case information is displayed.
  6. Click ![Case](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/case.svg)**Case overview**.
  7. In the **Case summary** section, follow the **Next steps** guidance.



### Review related findings in toxic combination cases

Usually, a toxic combination includes one or more findings of a software vulnerability or a misconfiguration. For each of these findings, Security Command Center automatically opens a separate case and runs the associated playbooks. You can review the cases for these findings, and ask the ticket owners to prioritize their remediation to help resolve the toxic combination.

To review the related findings in a toxic combination, follow these steps:

  1. From the ![Case](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/case.svg)**Case overview** tab of a case, go to the **Findings** section.
  2. In the **Findings** section, review the listed findings.

     * Click the case ID of the finding to open the case and view its status, assigned owner, and other case information.
     * Click the attack exposure score to review the attack path for the finding.
     * If the finding has a ticket ID, click it to open the ticket.



Alternatively, you can view related findings in their own alert tabs in the case.

###  Findings 

A toxic combination or chokepoint finding is the initial record that Risk Engine generates when it detects a toxic combination or chokepoint in your cloud environment.

  1. Go to the **Findings** page.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud organization.

  3. In the **Finding class** section of the **Quick filters** panel, select **Toxic combination** or **Chokepoint**. The **Findings query results** panel updates to show only toxic combination or chokepoint findings.

  4. To sort the findings by severity, click the **Attack Exposure Score** column heading until the scores are in descending order.

  5. Click a finding category to open the finding details panel. Go to the **Next steps** section, and follow its guidance to help remediate the security issue.




## Close toxic combination cases

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You can close a case for a toxic combination by either remediating the underlying toxic combination, or by muting the related finding in the Google Cloud console.

### Close a case by remediating a toxic combination

After you remediate the security issues that make up a toxic combination, and they no longer expose any resources in your high-value resource set, Risk Engine closes the case automatically during the next attack path simulation, which runs up to every 48 hours.

### Close a case by muting the finding

If the risk that is posed by the toxic combination is acceptable to your business or you can't remediate the toxic combination, you can close the case by muting the related finding.

To mute a toxic combination finding, follow these steps:

  1. In the Google Cloud console, go to **Risk > Cases**.
  2. Locate and open the toxic combination case.
  3. Click the related alert tab.
  4. In the **Finding summary** widget, click **Explore findings in SCC**. The related finding opens.
  5. Use the **Mute options** on the finding details page to mute the finding.



You can also mute findings in the Google Cloud console. For more information, see [Mute an individual finding](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings#mute_an_individual_finding).

### View closed toxic combination cases

When a case is closed, Security Command Center removes it from the **Cases** page.

To view a closed toxic combination case, follow these steps:

  1. In the Google Cloud console, go to the **Cases** page. The Security Operations console opens.
  2. Expand the **Status** section, and then select **Closed**.
  3. Expand the **Tags** section, and then select **Toxic combination**.
  4. Click **Apply**. Closed toxic combination cases are displayed in the search results.



## What's next

  * Learn more about [attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

  * Learn more about [Risk Engine feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features).

  * Learn how to [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
