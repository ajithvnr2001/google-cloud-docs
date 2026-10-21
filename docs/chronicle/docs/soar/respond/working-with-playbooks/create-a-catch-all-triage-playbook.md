---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-a-catch-all-triage-playbook/
title: Create a fallback playbook \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:05:06.901202+00:00
---

# Create a fallback playbook  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-a-catch-all-triage-playbook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a fallback playbook

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to create a "fallback" playbook in Google Security Operations. Use this example to process any alert that a more specific playbook trigger doesn't catch. This baseline approach provides every alert with automated triage, enrichment, and initial assessment. This playbook focuses on gathering information and preparing the case for an analyst, rather than performing deep, use-case-specific remediations.

## Purpose of a fallback playbook

  * **Maintain coverage:** Makes sure no alert is missed.
  * **Baseline analysis:** Provides consistent initial enrichment and analysis for all alerts.
  * **Efficiency:** Automates repetitive triage tasks, saving analyst time.
  * **Preparation:** Gathers essential context before manual review.
  * **Safety net:** Acts as a fallback for new or uncategorized alert types.
  * **AI template:** Enables AI to standardize playbooks to existing expectations.



## Design principles and best practices

  * **Low priority:** Assign this playbook the lowest priority (3) in the trigger order. This makes sure the system matches use-case-specific playbooks first.
  * **Modularity:** Use blocks extensively for common functions, such as enrichment, notification, and ticket creation. This makes the playbook cleaner and easier to maintain.
  * **Non-destructive:** Avoid automated containment or remediation actions. The goal is to triage and prepare, not to act on potentially incomplete information.
  * **Information gathering:** Focus on enriching entities and providing context.
  * **Clear analyst handover:** Use manual actions, questions, or clear case-wall updates to guide the analyst.
  * **Iterative refinement:** Regularly review alerts handled by the catch-all playbook to identify candidates for new, specific playbooks.



## Playbook structure and example steps

**Playbook name:** `Generic_Alert_Triage`

**Trigger:**

  * Type: All Trigger.
  * Because the playbook priority is set to 3, you can use `All trigger` make sure any alerts that haven't triggered an event-specific (P1) or product-specific (P2) playbook will then trigger the catch-all playbook.



### Playbook flow

  1. **Initialization:**

     * **Action:** `Siemplify - Change Case Stage`
       * Parameters: Stage Name = `Triage`
     * **Action:** `Siemplify - Add Case Tag`
       * Parameters: Tags = `CatchAll,NeedsReview`
  2. **Standard enrichment:**

     * **Run Block:** `TPI_Enrich_Entities`
       * This block enriches all IPs, domains, hashes, and entities using configured third-party intelligence.
     * **Optional blocks:**
       * `Internal_User_Enrichment`. For example, enrich usernames against Google Workspace or Active Directory.
       * `Internal_Asset_Enrichment`. For example, enrich hostnames or IPs against a CMDB.
  3. **Basic alert analysis:**

     * **Action:** `Siemplify - Get Similar Cases`
       * Configure based on entities or key alert fields to identify potential duplicates. Add a tag if related cases are found.
     * **Branch/Condition:** `Initial Risk Assessment`
       * Example Condition: If any entity has a high threat score from enrichment, such as `[Entity.VT_DetectionRatio] > 0.1` or `[Entity.MDT_Score] > 80`. 
         * **True Path:**
           * `Siemplify - Change Case Priority`: Priority = `High`
           * `Siemplify - Add Case Tag`: Tags = `HighRisk`
         * **False Path:** (Continue)
  4. **Analyst handover:**

     * **Action:** `Email - Send Email` or `Slack - Send Message`
       * Notify a triage team or channel about the new case, possibly including key details using placeholders.
     * **Action:** `Siemplify - Multiple Choice Question`
       * Example question: "Initial triage complete. Review enriched data. Is this a True Positive?"
       * Options: "Yes, True Positive", "No, False Positive", "Needs More Investigation".
     * **Action:** `Siemplify - Add Case Comment`
       * Summarize enrichment findings on the case wall.
  5. **Handle analyst response (example branch):**

     * Based on the `Multiple Choice Question` result: 
       * "**Yes, True Positive":**
         * `Siemplify - Change Case Stage`: Stage Name = `Investigation`
         * `Siemplify - Assign Case`: Assignee Type = `Role`, Assignee = `Tier 2 Analysts`
         * `Siemplify - Add Case Tag`: Tags = `TruePositive`
       * "**No, False Positive":**
         * `Siemplify - Change Case Stage`: Stage Name = `Closed`
         * `Siemplify - Close Case`: Reason = `False Positive - Benign Activity`
         * `Siemplify - Add Case Tag`: Tags = `FalsePositive`
       * **"Needs More Investigation":**
         * `Siemplify - Change Case Stage`: Stage Name = `Investigation`
         * `Siemplify - Add Case Comment`: Comment = `Analyst requested further investigation`



## AI playbook generation templates

The structure of this fallback playbook is composed of modular blocks and logical stages (Triage, Enrich, Analyze, Decide, Close). It's an excellent template for AI-driven playbook generation, such as with Gemini features in Google SecOps. For more information, see [Create and edit playbooks with Gemini](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-edit-playbook-with-gemini).

You can guide AI to build new, **use-case-specific** playbooks by prompting it to:

  * **Follow a standard framework:** "Generate a playbook for 'Phishing' alerts based on the Generic Alert Triage template."
  * **Include standard blocks:** "Ensure the playbook includes the `TPI_Enrich_Entities` block."
  * **Utilize Siemplify actions for core functions:** "Use Siemplify actions for changing case stages, adding tags, and assigning cases."
  * **Customize specific stages:** "In the Analysis stage, add steps to extract URLs from emails and check against a blocklist. If matched, raise priority to Critical using `Siemplify - Change Case Priority`."
  * **Add use-case-specific actions:** "If confirmed phishing, add a block to submit the URL to a sandbox and create a ticket in GUTS."



A well-structured, block-based default playbook that uses standard "Siemplify" actions, provides the AI with a clear pattern to follow. This approach promotes consistency and keeps generated playbooks aligned with best practices. A solid manual template lets the AI produce more useful, structured results.

For more information, see [Generate playbooks for alerts with Gemini](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-recommender).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
