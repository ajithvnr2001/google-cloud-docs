---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/case-playbooks/
title: Case playbooks overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:32:34.041402+00:00
---

# Case playbooks overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/case-playbooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Case playbooks overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

While alert playbooks focus on individual alerts, case playbooks let you run automation workflows across the broader scope of an entire case.

Running workflows at the case level provides three primary advantages:

  * **Case-specific context** : You can build automation for operational tasks that apply directly to the case container rather than a specific alert.
  * **Consolidated execution** : You can perform a single action on the case or its combined entities instead of running separate executions for each individual alert, which cuts out redundant work and saves third-party API credits.
  * **Case-level reaction triggers** : You can automatically trigger workflows based on lifecycle changes that happen to the case itself during an investigation.



## Understand case playbooks

Because a single case often groups multiple similar alerts together, running playbooks on an alert-by-alert basis can cause inefficiencies. For example, you might see a playbook reset a user's password multiple times, or spend third-party API credits enriching the exact same IP address across ten different alerts.

Case playbooks solve this by looking at the whole case container. You can access all the alerts and entities associated with that case. This lets you run a single operational action for the entire case—such as sending one unified Slack notification to your team or opening a single tracking ticket in an external system—instead of triggering repetitive actions for every individual alert.

Case playbooks also introduce reaction triggers. Instead of only running when an alert first arrives, you can automatically trigger these playbooks based on events that happen during the investigation—like when a case priority changes, or when a case is reassigned.

**Note:** When a case playbook is executed, it will only process and extract data from alerts that are in an "Open" status within the case.**Important:** If your playbook actions are configured to execute on a Remote Agent, the agent must run **Remote Agent version 2.6.6 or higher**. Actions dispatched to remote agents running versions earlier than 2.6.6 fail with an unsupported version error. For instructions on upgrading your agents, see [Upgrade Remote Agents](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-remote-agents).

## Common use cases

Case playbooks work best when you need to focus on the overall incident rather than isolated events. Typical scenarios include:

  * **Upon case creation** : Run an automated workflow the moment a new case opens. For example, you can automatically create a tracking ticket in an external IT service management (ITSM) system.
  * **Manual attachment during an investigation** : Run a single, centralized workflow directly on the case container. For example, if you need to rerun an enrichment block on all entities collected from the various alerts, a case playbook runs this action once at the case level instead of looping through each alert separately.
  * **When using reaction triggers** : Automate tasks based on lifecycle updates. For example, you can trigger a Slack notification or assign a new task automatically when the case assignee changes.



## Supported triggers

Case playbooks use specific triggers to determine when to run. These are split into two categories:

### Ingestion triggers

These triggers control how a playbook attaches when a new case is created:

  * **All** : Attaches the playbook to every newly created case.
  * **Custom Trigger** : Attaches the playbook based on specific fields you choose to evaluate.
  * **Tag Name** : Attaches the playbook only when a case is being ingested with specific tags (configured in your SOAR settings).



For more information, see [Use triggers in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-triggers-in-playbooks).

### Reaction triggers

These triggers automate responses based on changes made during an active investigation:

  * **Case Assignee Changed** : Fires when ownership shifts between analysts or SOC roles.
  * **Case Custom Field Changed** : Fires when a case-level custom field or case context value updates.
  * **Case Priority Changed** : Fires when the global severity or priority level of the case updates.
  * **Case Stage Changed** : Fires when a case transitions between phases of the investigation lifecycle (such as moving from `Triage` to `Containment`).
  * **Case Tag Added** : Fires when a tag is added to the case. You can configure this trigger to listen for any tag or filter for specific tag values.
  * **Case Comment was Added** : Fires when a new comment is posted to the case. You can configure conditions to trigger only when the comment text or the filename of an attachment matches specific criteria.



For more information, see [Use reaction triggers in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks).

## Create and configure case playbooks

To set up a case playbook, use the following steps:

### Choose the playbook scope

When you create a new playbook, select **Case** from the scope options (the default option is **Alert**).

When you choose **Case** , the playbook builder updates to show the ingestion and reaction triggers designed for case-level operations.

### Manual case creation

When creating a case manually, you can attach case-scoped playbooks directly within the wizard to execute across the entire case container upon creation. For detailed instructions, see [Create a manual case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case).

### Manual action on case scope

All standard actions in the Content Hub work directly over cases. Analysts can execute manual actions on the case container from the case interface without attaching or running a full playbook. While manual alert actions run separately across individual or bulk-selected alerts, a manual case action executes once for the entire case context.

To run a manual action from the case interface:

  1. Open the case and click the **Manual action** icon in the toolbar.
  2. Select whether to run the action on the **Case level** or **Alert level**.
  3. Choose the specific action to run and configure any required parameters.
  4. Click **Execute**.

**Note:** Built-in integrations fully support case-level workflows by default. If you use custom actions or custom Python scripts, make sure your code loops through the entire array of alerts so you don't drop entity details at the case level.

## Entity scoping and deduplication

A case functions as a higher-level container that groups multiple individual alerts together. Because each alert within that case brings its own separate list of entities, the exact same entity (such as a specific IP address or hostname) often appears across multiple alerts. When you look at a case as a whole, it naturally contains these duplicate entities.

To manage this, a case playbook automatically aggregates all entities from the different alerts associated with the case into a single list. To keep your third-party API use efficient and prevent you from processing the same entity multiple times, every case playbook action includes a **Deduplicate entities** toggle:

  * **Enabled (Default)** : The action finds unique entities (by identifier and type) and sends only that unique set to your third-party tools. When the results come back, the playbook automatically copies those details to all matching duplicate entities across the case, which helps you save API credits.

**Note:** This toggle only affects the entities processed by actions. Placeholders like `[Entity.Identifier]` always resolve to the full list of distinct entities regardless of this setting.
  * **Disabled** : Turn this off if you need to run an action against every single instance of an entity (including duplicates), or if you want to keep duplicates in your initial scope so you can filter them later in the workflow.




### Deduplication inside loops

When you use an entities loop, a **Deduplicate loop entities** toggle is available inside the **Start Loop** step settings (enabled by default):

  * **Enabled (Default)** : The loop runs only on distinct case entities and skips duplicates. When this setting is active, the behavior of actions inside the loop depends on the **Lock scope to iteration** setting: 
    * **Lock scope to iteration is enabled** : Internal loop actions only see the current looped entity. When the action finishes, the results automatically apply to all matching duplicates across the case.
    * **Lock scope to iteration is disabled** : Internal loop actions remain aware of the entire case entity array, allowing you to manually configure how the step handles the broader context just like any standard action.
  * **Disabled** : The loop iterates over every duplicate entity across all alerts in the case. This is useful when a specific instance of a duplicate entity contains unique alert-level properties that you need to process.



## Work with playbook blocks

Playbook blocks are scope-agnostic, meaning they are not tied to a specific alert or case context. You can build a block once and use it in both alert and case playbooks.

When you place a block inside a case playbook, the block step includes a **Deduplicate entities** toggle that is turned on by default. When active, all internal block actions run against unique case entities, skip duplicates, and automatically apply the results to matching duplicates across the case.

## Limitations and considerations

  * **Playbook name uniqueness** : Playbook names must be unique across the platform. A case playbook and an alert playbook cannot share the exact same name. For details on attachment limits and playbook capacity, see [Attach playbooks to an alert or case](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/attach-playbooks-to-alerts-cases).
  * **Reporting and export exclusions** : Executions for case playbooks are excluded from Legacy Monitoring dashboards and SOAR Data Exports (Managed BigQuery and Bring Your Own BigQuery (BYOBQ)).



### Integration versioning for full case playbook support

To ensure stable functionality with case playbooks, update your integrations to minimum required versions. If you're using an older version of these integrations, some case playbook features may not work as expected.

Integration | Minimum Version  
---|---  
[**AlienVaultAppliance**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alienvault-usm-appliance) | 28  
[**ConnectWise**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/connectwise) | 23  
[**EmailUtilities**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/email-utilities) | 50  
[**Enrichment**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/enrichment) | 35  
[**FileUtilities**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/file-utilities) | 25  
[**GoogleChronicle**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chronicle) | 84  
[**Jira**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/jira) | 58  
[**MISP**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/misp) | 40  
[**ServiceDeskPlus**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/service-desk-plus) | 10  
[**ServiceDeskPlusV3**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/service-desk-plus-v3) | 10  
[**ServiceNow**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/servicenow) | 67  
[**Siemplify**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify) | 108  
[**TemplateEngine**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-and-integrations/power-ups/templateengine) | 23  
[**Tools**](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/tools) | 81  
  
Refer to the specific integration's documentation for detailed feature support and update instructions.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
