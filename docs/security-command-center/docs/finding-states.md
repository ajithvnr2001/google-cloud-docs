---
url: https://docs.cloud.google.com/security-command-center/docs/finding-states/
title: Finding states \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:49.394591+00:00
---

# Finding states  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/finding-states/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Finding states Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

A finding can have one of two states: `Active` or `Inactive`.

When a finding is first created, the built-in detection services set the `state` property of the finding to `Active`. Generally, you can consider `Active` to mean that the underlying security issue still exists; however, as explained later in this section, that is not always the case.

The state of a finding can become `Inactive` if certain detection services detect that the security issue was remediated or that the affected resource was deleted. You can also manually change the state to `Inactive`. Generally, `Inactive` means that the underlying security issue no longer exists; however, as explained later in this section, that is not always the case.

At any point in time, the `state` of a finding might not reflect the current state of the detected security issue. The following list shows some of the reasons a mismatch might occur:

  * Some detection services do not update their findings automatically after the detected issue is remediated.

The state of threat findings are never changed automatically.

  * For the detection services that do update their findings automatically, there is usually a delay before the remediation is detected and the finding is updated.

  * For some detection services, the state of a finding might be changed manually to a state that does not match the state of the detected issue.




Only the following vulnerability and misconfiguration detection services automatically change the state of a finding from `Active` to `Inactive` upon detecting that the corresponding issue is remediated:

  * Security Health Analytics, including when a detector in Security Health Analytics is disabled. See [Automatic deactivation of findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings#finding-deactivation) for information about all the events that might cause Security Health Analytics to automatically change the state of their finding. + VM Manager



Downgrading to the Standard tier also changes the state of Premium or Enterprise findings to `Inactive`. Learn more about [Service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

For information about manually changing the state of a finding in the Google Cloud console, see [Changing the state of a finding](https://docs.cloud.google.com/security-command-center/docs/how-to-work-with-findings-in-the-dashboard#change_the_state_of_a_finding).

## What's next

  * Learn how to [change the state of a finding](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#change-state).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
