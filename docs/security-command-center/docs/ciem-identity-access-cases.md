---
url: https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-cases/
title: Review cases for identity and access issues \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:59.750479+00:00
---

# Review cases for identity and access issues  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Review cases for identity and access issues Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to review cases corresponding to identity and access findings in Security Command Center Enterprise.

Security Command Center automatically creates cases for threat findings, toxic combinations, and findings related to toxic combinations.

## Before you begin

Make sure you have completed the following tasks before continuing:

  * Learn about [Security Command Center's CIEM capabilities](https://docs.cloud.google.com/security-command-center/docs/ciem-overview).
  * [Set up permissions for CIEM](https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service#ciem-permissions).
  * [Enable the CIEM detection service](https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service).
  * [Integrate the Enterprise tier with ticketing systems](https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems).



## View case details

To view the case details of an identity and access misconfiguration case from the **Findings** page, take the following steps:

  1. In the Google Cloud console, select **Findings** in the navigation.
  2. Click **Identity** to display a pre-filtered query for identity and access findings.
  3. Identify a finding with a value in the **Case ID** column.
  4. Do one of the following to open the case details:

     * Click the value in the **Case ID** column.
     * Click the finding name in the **Category** column. In the **Finding details** pane, go to the **Case information** section. Click the case ID number in the **Case ID** row.

The **Cases** window opens and displays details about the case, including the following information:

     * List of alert events associated with the case
     * Playbooks attached to the alert
     * A finding description
     * Next steps for remediation
     * Information about the impacted asset
     * Ticket information (if you connected your ticketing system to Security Command Center)
  5. If you have connected Security Command Center to Jira or ServiceNow, you can use the ticket ID link to navigate to your ticketing system.

  6. Check the **Case Wall** tab for details about the activity performed on the case and included alerts.

  7. Check the **Case Overview** tab for a full overview of the case.




On the **Cases** page, you can see all cases created for your environment, not just identity and access cases. You can navigate all existing cases in the cases list on the left side of the page. You can also search and filter the list to make it easier to identify cases to focus on.

For more information on working with cases, see [Cases overview](https://docs.cloud.google.com/security-command-center/docs/cases-overview).

## What's next

  * Learn how to [investigate identity and access findings](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-findings).
  * Learn more about cases from the Google SecOps documentation: 
    * [Cases overview tab](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-case-overview-tab)
    * [What's on the Cases page?](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-cases-screen)
    * [How to perform a manual action on a case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action)
    * [How to simulate cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/simulate-cases)
    * [Work with playbook blocks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-blocks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
