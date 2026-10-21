---
url: https://docs.cloud.google.com/security-command-center/docs/view-python-package-vulnerabilities/
title: View Python package vulnerabilities \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:10.376402+00:00
---

# View Python package vulnerabilities  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/view-python-package-vulnerabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  View Python package vulnerabilities Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how you can view the vulnerabilities in Python packages that were detected by Notebook Security Scanner.

## Filter package vulnerability findings

For Notebook Security Scanner, you can filter the package vulnerability findings by using the category, source display name, severity, and project ID.

  1. Go to the Security Command Center **Findings** page.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. In the project selector, select the project or organization for which you need to view the package vulnerability findings.

The **Findings** page displays findings only for the project or organization that you selected.

  3. In the **Quick filters** section, select one or more of the following:

     * In the **Category** section, select **Package vulnerability**.
     * In the **Project ID** section, select your project ID.
     * In the **Source display name** section, select **Notebook Security Scanner**.
     * In the **Severity** section, select the required severity value.

The **Findings** page displays a list of findings that match the type you selected.




## View older package vulnerability findings

By default, the Security Command Center **Findings** page displays only active package vulnerability findings that are less than seven days old.

If you want to view package vulnerability findings that are older than seven days and have not been addressed, do the following:

  1. Go to the Security Command Center **Findings** page.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. In the project selector, select the project or organization for which you need to view the package vulnerability findings.

The **Findings** page displays findings only for the project or organization that you selected.

  3. In the **Time range** list, select the required time range.

You can also add more filters such as **Source display name** and **Category**.

  4. If you want to view the package vulnerability findings that are published after a particular timestamp, do the following:

     1. Click **Edit Query**.
     2. In the **Query Editor** , add a condition on `create_time` and `parent_display_name`.

The following example query displays the active package vulnerability findings that are created after 2024-07-16.
            
            state="ACTIVE"
            AND NOT mute="MUTED"
            AND parent_display_name="Notebook Security Scanner"
            AND create_time > "2024-07-16"
            




## What's next

  * Learn more about [filtering vulnerability findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/filter-vulnerability-findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
