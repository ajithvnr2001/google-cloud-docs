---
url: https://docs.cloud.google.com/security-command-center/docs/mute-findings-in-cases/
title: Mute findings in cases \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:18.653000+00:00
---

# Mute findings in cases  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/mute-findings-in-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Mute findings in cases Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The **SCC Enterprise - Urgent Posture Findings Connector** ingests all findings into cases, but you might notice specific findings that appear irrelevant to your project or indicate an expected behavior. In this case, the flow of negligible findings might overcomplicate the security analyst workload and prevent analysts from effectively responding to important vulnerabilities. Instead of being constantly notified about the existing irrelevant findings in Security Command Center Enterprise, you can mute them.

When you mute findings for cases, you prevent them from appearing in cases. You can mute findings in bulk by running a manual action on a case or mute an individual finding by running a manual action on the specific alert.

## Mute multiple findings

If you mute all findings in a case, Security Command Center automatically closes the case.

To mute multiple findings in a case, complete the following steps:

  1. In the Google Cloud console, open **Risk > Cases**.
  2. Select a case containing the findings to mute.
  3. In the **Case Overview** tab, click **Manual Action**.
  4. In the manual action **Search** field, input `Update Finding`.
  5. In the search results under the **GoogleSecurityCommandCenter** integration, select the **Update Finding** action. The action dialog window opens.

By default, the **Run on Alerts** parameter is set to the **All Alerts** value.

**Note:** The **All Alerts** value means that the action retrieves the **Finding Name** value from each alert in a case and extracts all finding IDs in one action run.
  6. Optional: To change the **Run on Alerts** parameter default settings, select the relevant finding types from the drop-down list.

  7. To configure the **Finding Name** parameter, input the following placeholder: `[Alert.TicketID]`

The placeholder dynamically retrieves finding names that correspond to selected alerts.

  8. To mute findings, set the **Mute Status** parameter to **Mute**.

  9. Click **Execute**.




## Mute an individual finding

Muting an individual finding requires you to run the _Update Finding_ action on a specific alert in the case. The action doesn't affect other alerts in the case.

To mute an individual finding, complete the following steps:

  1. In the Google Cloud console, go to **Risk > Cases** to open the Security Operations console **Cases list** page.
  2. Select a case containing the findings to mute.
  3. In a case, select the alert containing a finding to mute.
  4. In an alert, go to the **Events** tab.
  5. To retrieve a **Finding Name** from an event, click **View More**. The detailed view of the event opens.
  6. Under the **Highlighted Fields** section, find a **Name** field name. Click its value to see the full finding name.
  7. Copy the full finding name value in the following format:
         
         organizations/ORGANIZATION_ID/sources/SOURCE_ID/finding/FINDING_ID
         

  8. In the **Alert Overview** tab of the selected alert, click **Manual Action**.

  9. In the manual action **Search** field, enter `Update Finding`.

  10. In the search results under the **GoogleSecurityCommandCenter** integration, select the **Update Finding** action. The action dialog window opens.

By default, the **Run on Alerts** parameter is set to the selected alert value.

  11. To configure the **Finding Name** parameter, paste the **Name** value that you've copied from the event detailed view.

  12. To mute a finding, set the **Mute Status** parameter to **Mute**.

  13. Click **Execute**.




## What's next?

  * Learn how you can [mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

  * Learn more about the [cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview) in the Google SecOps documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
