---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/setting-the-sla/
title: Set the SLA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:08.940650+00:00
---

# Set the SLA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/setting-the-sla/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Support ](https://docs.cloud.google.com/chronicle/docs/secops/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set the SLA 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

A Service Level Agreement (SLA) represents a commitment by the SOC to perform specific tasks, such as investigating or remediating a case within a set timeframe. You can configure SLAs for alerts, cases, or both.

## Understand the SLA types

  * **Alert SLA** : The maximum time to close an alert. An alert SLA is mainly based on alert attributes (for example, **Alert Type** or **Alert Priority**), but can also be based on case attributes. The start time begins when the alert is created.
  * **Case SLA** : The maximum time to close a case. A Case SLA is mainly based on case attributes (for example, `Case Stage` or `Case Priority`), but can also be based on alert attributes. The start time begins when the case is created, unless the SLA is configured by **Case Stage** —in which case it begins when the stage starts. 
    * When a Case SLA is based on a specific Case Stage, the SLA timer starts the first time the case enters that stage and is active only while the case is in that stage. When the case transitions to a different stage, the active Case SLA switches to the new stage's SLA. If the case returns to the previous stage later, that stage's SLA timer continues from where it left off and doesn't reset.
    * Similarly, if a Case SLA is based on Case Priority, the SLA resets if the case's priority is changed.
    * Historical SLA data for previous stages or priorities is not lost. You can review all historical SLA status information within the **Dashboards & Reports** section.



You can configure an SLA in **Settings** or automatically using a playbook action.

## Manage SLAs

This section explains how to manage SLAs in your environment, including how to create new rules and how to pause and resume them during an investigation.

### Set SLA priorities

If multiple SLA rules are set, the system follows a clear priority order:

  * **Case SLAs** : Playbook action > Case Stage > Case Priority
  * **Alert SLAs** : Playbook action > Alert Type > Alert Priority



### Add an SLA

To add an SLA, follow these steps:

  1. Go to **Settings > Environments > SLA**.
  2. Click add **Add**.
  3. Select whether the SLA is based on alert attributes (type or priority) or case attributes (stage or priority).
  4. Define the timeframes for the **SLA Period** (the time before an SLA is breached) and the **SLA Time to Critical Period** (the time before the SLA enters a critical phase). For example, an **SLA Period** of 10 minutes and an **SLA Time to Critical Period** of 6 minutes results in a 4-minute critical period.
  5. Click **Add**.

**Note:** When you create a new case priority SLA rule, the system applies the rule to existing cases only if their priority changes. The system doesn't apply the new rule when other case attributes change, such as the stage.

### Interpret an SLA status

An SLA status is indicated by an hourglass hourglass icon. A **'C'** next to the hourglass hourglass icon indicates a **Case** SLA, while an **A** indicates an **Alert SLA**. The icon's color shows its status as follows:

  * Green: The SLA is active.
  * Gray: The SLA is paused.



In the **Cases** tab, a green countdown timer indicates an active case SLA at the top. For cases with multiple alerts, the **Alerts** icon in the header displays all alert SLAs. Each Alert SLA can be clicked to view the individual alert.

## Pause and resume an SLA

You can pause SLAs to provide flexibility during investigations. Pausing a case SLA doesn't affect an alert SLA, and the other way around. All pause and resume events are recorded on the **Case Wall**.

### Pause an alert SLA

To pause an alert SLA, do the following:

  1. On the **Cases** page, select the case with the relevant alert.
  2. In the alert tab, click more_vert **More > Alert Options**.
  3. Select **Pause alert SLA**.
  4. Optional: In the **Pause alert SLA** dialog, enter a reason for pausing the SLA.
  5. Click **Pause**.



A gray hourglass hourglass in the **Alert** tab indicates that the SLA is paused and a tooltip also indicates the paused status.

### Resume an alert SLA

To resume the Alert SLA, do the following:

  1. Click more_vert **More > Alert Options**.
  2. Select **Resume alert SLA**.



The green hourglass in the **Alert** tab indicates that the SLA is running again. The alerts icon in the case top bar also shows a countdown timer that has resumed ticking for the resumed Alert SLA.

### Pause a case SLA

To pause a case SLA, do the following:

  1. On the **Cases** page, select the relevant case.
  2. Click format_list_bulleted **Menu > Case Actions**.
  3. Select **Pause Case SLA**.
  4. Optional: In the **Pause Case SLA** dialog, enter a reason for pausing the SLA.
  5. Click **Pause**.



The case SLA timer in the header turns gray and stops. A tooltip also indicates the paused status.

### Resume a case SLA

To resume a paused case SLA, do the following:

  1. In the case top bar, click format_list_bulleted **Case Actions**.
  2. Select **Resume Case SLA**.



The timer turns green and resumes the countdown.

**Note:** The case SLA is automatically paused when a case is closed and automatically resumes when the case is reopened.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
