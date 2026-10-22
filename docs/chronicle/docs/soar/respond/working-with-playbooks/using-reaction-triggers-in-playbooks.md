---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks/
title: Use reaction triggers in playbooks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:43.696515+00:00
---

# Use reaction triggers in playbooks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use reaction triggers in playbooks

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

A reaction trigger acts as a post-ingestion trigger configured during the initial playbook setup. While standard triggers execute immediately upon ingestion, reaction triggers automate playbooks based on real-time modifications or specific events that occur during an active investigation.

The availability of specific reaction triggers depends on the playbook scope. When configuring a playbook, selecting the **Alert** scope displays alert-level event triggers, while selecting the **Case** scope displays case-level triggers.

By introducing event-based logic, reaction triggers eliminate the need to manually attach playbooks when an alert state changes.

## Use cases

The following examples demonstrate how to use reaction triggers to automate common investigative workflows at both the alert and case level:

### Automate enrichment for newly discovered entities (Alert scope)

  * **Goal** : Ensure all entities associated with an investigation are automatically enriched, even if they are added after initial alert ingestion.
  * **Scenario** : A new entity is attached to an active investigation.
  * **Outcome** : The **Entity Added** reaction trigger detects the new entity and automatically executes an enrichment playbook to provide immediate reputation data.



### Dynamic incident escalation and notification (Alert scope)

  * **Goal** : Automatically notify senior stakeholders when the severity of an investigation increases.
  * **Scenario** : An alert priority changes from `Medium` to `Critical`.
  * **Outcome** : The **Alert Priority Changed** trigger executes a workflow that sends an automated email to the case assignee and a notification to the Incident Response Slack channel.



### Cross-platform ticket synchronization (Case scope)

  * **Goal** : Maintain strict alignment between the platform and external IT service management (ITSM) platforms during ownership shifts.
  * **Scenario** : A security case is reassigned from a general queue to a specialized SOC role or user.
  * **Outcome** : The **Case Assignee Changed** reaction trigger fires, automatically updating the owner field in the corresponding external ticketing system and sending an operational summary to the new owner.



## Available reaction triggers

The options available under the **Reaction** tab dynamically filter based on the operational scope selected during playbook setup:

### Case scope reaction triggers

When a playbook is configured with a **Case** scope, the menu displays triggers that monitor the overarching case container:

  * **Case Assignee Changed** : Fires when ownership shifts between analysts or SOC roles.
  * **Case Custom Field Changed** : Fires when a case-level custom field or case context value updates.
  * **Case Priority Changed** : Fires when the global severity or priority level of the case updates.
  * **Case Stage Changed** : Fires when a case transitions between phases of the investigation lifecycle (such as moving from `Triage` to `Containment`).
  * **Case Tag Added** : Fires when a tag is added to the case. You can configure this trigger to listen for any tag or filter for specific tag values.
  * **Case Comment was Added** : Fires when a new comment is posted to the case. You can configure conditions to trigger only when the comment text or the filename of an attachment matches specific criteria.



### Alert scope reaction triggers

When a playbook is configured with an **Alert** scope, you can select from the following event-based triggers:

  * **Entity Added** : Fires when a new entity is attached to an active alert after its initial ingestion.
  * **Alert Priority Changed** : Fires when an analyst or system workflow modifies the priority level of the alert.
  * **Alert Custom Field Changed** : Fires when a designated alert-level custom field or contextual value updates.



## Configure a reaction trigger

To configure a playbook to react to specific platform events or data modifications, follow these steps:

  1. Click **Add New Playbook or Block** to create a new playbook.
  2. In the **Create New** dialog, select the playbook **Scope** : 
     * Select **Alert** to configure alert-level event triggers.
     * Select **Case** to configure case-level triggers.
  3. Click **Create**.
  4. In the **Step Selection** panel, select **Triggers**.
  5. Select the **Reaction** tab to view available event-based triggers for the selected scope.
  6. Select the appropriate trigger and drag it to the trigger target area in the playbook designer.
  7. Double-click the trigger to open the side drawer. The parameters available in the **Conditions** tab automatically update to match the trigger you selected.
  8. Depending on your selected trigger and playbook scope, configure the following logic:

     * If using **Entity Added** (Alert scope): Define criteria for triggering based on new entities that were added to the alert post-ingestion.

       * Select **Any entity is added** to trigger on every new entity.
       * Select **A specific entity is added** to define filtering logic. You can select from a list of entity properties and use logical operators (`AND` and `OR`) to configure multiple conditions. For example, `Entity.Identifier` contains `@google.com` **AND** `Entity.Type` is `USERUNIQNAME`.
**Note:** Trigger conditions evaluate exact, case-sensitive technical syntax for entity types (for example, `USERUNIQNAME` or `DestinationURL`). Triggers don't attach for entities created during initial alert ingestion.
     * If using **Alert Priority Changed** (Alert scope) or **Case Priority Changed** (Case scope): Configure the `Priority changed from` and `Priority changed to` states.

       * You can select a specific priority from the list or use `ANY` to match any state value.
       * You can create multiple state combinations using the `OR` logical operator (for example, triggering when priority moves from `Medium` to `High` **OR** `Medium` to `Critical`).
     * If using **Alert Custom Field Changed** (Alert scope) or **Custom Case Field Changed** (Case scope): Select the appropriate field from the menu and configure the `From` and `To` states. Use the toggle next to each value to determine if that specific part of the state change is validated.

       * Toggle Off (Disabled): The system does not check the value for this state. Disabling the toggle effectively matches any value, allowing the trigger to fire regardless of what the field contained before or after the change.
       * Toggle On (Enabled): The system checks for a specific value. If the field is left empty while the toggle is on, it signifies a search for an empty string (for example, triggering when a previously blank field is updated).
     * If using **Case Assignee Changed** (Case scope): Configure the `Assignee changed from` and `Assignee changed to` parameters to track ownership shifts. You can isolate shifts between specific analysts or SOC roles.

     * If using **Case Stage Changed** (Case scope): Configure the `Stage changed from` and `Stage changed to` parameters to detect when a case transitions between different phases of the investigation lifecycle (such as moving from `Triage` to `Containment`).

**Note:** Available investigation stages are configured in the SOAR settings by an administrator.
     * If using **Case Tag Added** (Case scope): Configure the parameters to detect when a tag is added to the case container. Select the appropriate tag from the menu and define whether the trigger logic validates the addition event.

  9. To reduce the number of unwanted executions, go to the **Define additional conditions (optional)** section to define criteria that are not directly tied to the reaction trigger itself.

     * Example: Configure a playbook to trigger on an alert priority change to `Critical` only when the case priority is also set to `High`.
  10. Click **Save**. The parameter details appear in the trigger description.




## Reaction trigger priority

When a supported event occurs (such as a case assignee change or an alert priority change), the platform evaluates all reaction playbooks to determine which ones match the event conditions.

If multiple playbooks match the same trigger event, the platform executes them according to their configured priority level:

  * **Priority execution** : Playbooks with higher priority run first. For example, Priority 1 takes precedence over Priority 2 and Priority 3.
  * **Same-priority tie breaking** : If multiple matching playbooks share the same priority level, the platform automatically selects and executes one of them.



To ensure that specific or critical playbooks execute when an event fires before more generic playbooks, adjust their individual priority settings accordingly.

## Reaction execution modes

Because investigative data can change rapidly, reaction triggers allow you to define how the system handles back-to-back events if a playbook is already running. To select an execution mode, click the **Settings** tab in the trigger side drawer:

  * **Restart (default)** : Terminates the active playbook execution and starts a fresh one immediately using the most current data. Use this mode when you don't want to complete the execution if the state changes.
  * **Queued** : Allows the active playbook to finish its current run before processing the next trigger event. Use this mode when you must complete the execution even if the trigger has already changed. Queued playbooks appear in the case overview playbooks viewer.



## Reaction chain limit

Reaction triggers include a built-in mechanism to enforce a maximum execution depth, preventing infinite loops or redundant runs (for example, a reaction playbook performing an action that re-triggers the same playbook).

To configure the reaction chain limit:

  1. Double-click the trigger card on the Playbook Designer canvas to open its configuration panel.
  2. Select the **Settings** tab.
  3. Under **Reaction Chain Limit** , configure the **Max number** parameter (default is `5`).



Set this value to `1` if you want to prevent the playbook from triggering any subsequent playbook chain.

**Note:** This limit applies exclusively to reaction playbooks and is not enforced for playbooks attached using the **Attach playbook** action.

## Test reaction triggers with the simulator

You can test and validate reaction trigger logic in the playbook designer using the playbook simulator:

  1. Open a playbook that contains a reaction trigger and click **Simulator**.
  2. In the simulator panel, select a test case and configure the simulated event parameters according to your selected trigger. The simulator panel automatically updates its layout and parameters based on the specific reaction trigger placed on the canvas (such as priority changes, custom field updates, or entity additions).

**Note:** Removing a reaction trigger automatically switches the panel back to the standard ingestion simulator.
  3. Click **Run**.

     * **Matching Event** : If the simulated event criteria match your reaction trigger, the trigger step displays a green checkmark, and dynamic trigger placeholders (such as `[trigger.from_state]` and `[trigger.to_state]`) become available for subsequent steps.
     * **Non-Matching Event** : If the simulated event does not match the trigger criteria, the trigger step displays a failure status and trigger placeholders are unavailable, but the rest of the playbook continues executing.



## Dynamic reaction placeholders

Reaction triggers use specific placeholders to capture the exact snapshot of the trigger at the moment of modification. This ensures your playbook logic remains accurate even if the alert data changes again while the playbook is mid-execution:

  * **State Changes** : Use `[trigger.from_state]` and `[trigger.to_state]` to capture property shifts (e.g., capture old and new priority values).
  * **Event-Specific Details** : Use `[trigger.EntityIdentifier]` and `[trigger.EntityType]` to dynamically target a newly attached entity.
  * **Trigger Metadata** : Use `[trigger.TriggeredBy]` to identify the initiator. For manual UI actions or manual playbook runs, this placeholder displays the full username. If the change is executed by a playbook, it displays **System Automation**. Use `[trigger.DateTime]` for the precise event timestamp, formatted as YYYY-MM-DD HH:MM:SS UTC+Offset.



## Limitations

  * **Unique playbook limits** : You can attach up to 30 unique playbooks per alert or case.
  * **Rerun limits** : A playbook can run a maximum of 30 times per alert or case. If a trigger fires for a playbook already attached, it registers as a rerun. Subsequent activations are registered as skipped.
  * **Reporting and export exclusions** : Executions for reaction trigger playbooks are excluded from Legacy Monitoring dashboards and SOAR Data Exports—both Managed BigQuery and Bring Your Own BigQuery (BYOBQ).



You can now continue building the playbook with actions. For more information, see [Manage actions in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
