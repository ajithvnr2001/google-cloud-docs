---
url: https://docs.cloud.google.com/chronicle/docs/detection/threat-hunt-agent/
title: Threat Hunt agent overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:02.891183+00:00
---

# Threat Hunt agent overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/threat-hunt-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Threat Hunt agent overview

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

The Threat Hunt Agent is an autonomous AI capability embedded in Google Security Operations that automates proactive threat hunting across your enterprise security telemetry.

This guide is for Google SecOps analysts and threat hunters who want to automate proactive threat hunting across their enterprise security telemetry. It explains how to use the Threat Hunt Agent to autonomously plan threat hunts, query telemetry, and analyze forensic evidence. The Threat Hunt Agent lets you detect hidden adversaries and validate security hypotheses without manual research. Successful completion reduces investigation time and accelerates response to emerging threats.

## Use case: Automate threat hypothesis validation

  * **Objective** : Automate the research, query construction, and noise filtering required to validate a threat hypothesis.
  * **Value** : Frees up senior analysts to focus on complex tasks by reducing the time spent on manual log analysis and query building.



## Key terminology

  * **Threat Hunt Agent** : An autonomous AI capability powered by Gemini and grounded in Google Threat Intelligence, Mandiant frontline expertise, and the MITRE ATT&CK® framework that automates proactive threat hunting.
  * **YARA-L 2.0 (YL2)** : The search query language used by Google SecOps to query historical telemetry.
  * **Determination** : The final verdict issued by the agent. For example, `Substantial Evidence`, `Evidence Found`, or `Threat Not Found`.



## Before you begin

Make sure you meet the following prerequisites:

  * **Enterprise plus license** : During the public preview phase, Threat Hunt Agent is only available for Enterprise Plus customers. This is due to the Emerging Threats integration point, which heavily invokes Google Threat Intelligence.
  * **Case Management experience** : Enable the enhanced Case Management experience to use the Threat Hunt Agent. This feature is in Public Preview. For information on how to enable preview features, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) and [Investigation management overview prerequisites](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview#prerequisites).
  * **Permissions** : You must have appropriate access to the Google SecOps platform, particularly Case Management.
  * **Environment check** : If your organization uses multi-tenant or segmented environments, make sure you have access to the target environment.



## Start a threat hunt

The following steps describe how to start the Threat Hunt Agent from the **Emerging Threats** window:

  1. From the navigation menu, go to **Detection** > **Emerging Threats**. Click **New Threat Hunt**.
  2. In the **Agentic Threat Hunt** dialog, configure the following: 
     * In the **What would you like to hunt for?** section, select the threat category you want to investigate: 
       * **Actor** : Hunt for known adversary groups, for example: `APT28` or `UNC2452`.
       * **Campaign** : Hunt for organized adversary campaigns.
       * **Malware** : Hunt for specific malware families or loaders, for example, `FAKEUPDATES` or `CHERRYRED`.
       * **Software Toolkit** : Hunt for abused administrative tools or Living-off-the-Land Binaries (LOLbins), for example, `PowerShell`, `Certutil`, or `vssadmin`.
       * **TTP** : Hunt for specific MITRE ATT&CK techniques, for example, `T1003.001 - OS Credential Dumping: LSASS Memory`.
     * Once you select the threat category, select the specific threat name, alias, or MITRE ID in the field next to it.
     * In the **Select your hunt window** , define the historical telemetry timeframe to analyze. The default is the last seven days. The maximum is up to a 30-day period.
     * From the **Case environment** menu, if applicable, select the target environment to hunt within.
  3. Click **Begin Hunt** to launch the investigation.



Once you start the Threat Hunt Agent, it runs autonomously in the background and Google SecOps creates a new case in **Case Management**. The new case uses the `Threat Hunt for [Subject Name]` prefix to simplify identifying cases produced by the Threat Hunt Agent. A Threat Hunt tag also shows in the **Tags** column.

You can also open the **Agentic Threat Hunt** dialog to start threat hunts from additional entry points as follows:

  * **Google Threat Intelligence pop-outs** : On the **Threats Feed** page or **Campaign Detail** page, click **Run Threat Hunt** next to any threat report or adversary profile.
  * **Threat association details** : Inside threat intelligence drawers, click **Run Threat Hunt**.
  * **MITRE ATT &CK matrix**: In the **MITRE ATT &CK**, click a technique drawer. Then click **Run Hunt**.



## View threat hunt cases

You can locate and track threat hunts at any time from the **Case Management** queue:

  * On the navigation menu, go to **Cases**. 
    * **Filter by tag** : Use the tag filter to select the **Threat Hunt** tag.
    * **Search by name** : Use the search bar to query specific hunt titles., such as `Mimikatz`.



### Statuses and alerts

Inside the case list and case wall, threat hunts display their live status. When you open a case, you'll see tags next to the **Manage Tags** option as follows:

**Status** | **Explanation**  
---|---  
**Threat Hunt Running** | Displayed while the agent is actively planning, translating queries, and scanning UDM events. The case status remains open and updates automatically.   
**Completed** | Displayed when the agent finishes its analysis and posts the final determination and evidence summary.   
**Queued** | Displayed when the agent is waiting for prior threat hunts to complete execution before beginning.   
**Failed** | Displayed if a fatal error occurs (for example, search service timeout).   
  
### Review a threat hunt case

To review and manage a threat hunt case, do the following:

  1. From the **Cases** queue, select the case you want to review.
  2. Go to the **Agentic Threat Hunt** widget to view the case's summary.
  3. See the **Determination** button to view the threat hunt result: 
     * **Substantial Evidence** : Strong, highly convincing evidence the threat behavior was detected.
     * **Evidence Found** : Potential indicators or threat behaviors supporting the hypothesis were detected.
     * **Threat Not Found** : No evidence of the threat behavior was detected _._
  4. Read the **Results Summary**. This is a hunt summary that details what the Threat Hunt Agent discovered. This can include information such as observed hostnames, user accounts, process command lines, timestamps, and behavioral context.



### View more detailed information

To see more detailed information about a case, do the following:

  1. In a case's **Agentic Threat Hunt** widget, under **Subject** click the link.
  2. Click one of the following options that may be displayed: 
     * **Actor/Malware** : Opens the **Entity Summary** side drawer for detailed threat intelligence profiles.
     * **MITRE Technique** : Opens the **MITRE Details** overlay for technique descriptions and mitigation guidance.
     * **Campaign** : Navigates directly to the **Campaign** or **Emerging Threats** detail window.



### Inspect the hunt steps timeline

Review the forensic trail of the agent's investigation in the **Hunt Steps** timeline.

  1. On the right side of the **Agentic Threat Hunt** widget, click **View Hunt Detail**.
  2. Expand each step to view details of that step.
  3. You can: 
     * View **Atomic questions** : Inspect each individual question the agent asked to validate the hunt plan.
     * Inspect **generated YL2 queries** : Review the exact YL2 search queries used by the agent.
     * Check **event counts & telemetry**: See the number of relevant events extracted by the agent.
     * Review **step evidence** : Read forensic observations, such as specific parent-child process relationships or command-line flags, for each individual step.



### Provide feedback on hunt results

Help improve the AI agent's accuracy by submitting feedback.

  1. In the **Agentic Threat Hunt** widget, click either  thumb_down or thumb_up.

**Note:** The feedback options are available in the **Results Summary** window and from expanded individual investigation steps within the **Hunt Steps Timeline**.
  2. In the **Send Feedback** dialog that opens, you can send feedback, including comments explaining why the determination or query was accurate or where it could be improved.

  3. Click **Send Feedback**.




## Troubleshooting

  * **Execution time** : Threat hunts typically take **60-90 minutes** to complete, depending on the selected time window and the volume of telemetry in your environment.
  * **Queued status** : Threat hunts may be queued if the agent is waiting for prior threat hunts to finish running. For AI capacity reasons, avoid triggering multiple redundant hunts.
  * **Hunt quota** : During preview, customers are limited to two concurrent threat hunts and up to five threat hunts per day. This is subject to adjustment for managing global capacity. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
