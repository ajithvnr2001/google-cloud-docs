---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-reusable-enrichment-block/
title: Create an enrichment playbook block \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:13.714226+00:00
---

# Create an enrichment playbook block  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-reusable-enrichment-block/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an enrichment playbook block

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how to create a reusable block you can use in Google Security Operations playbooks to enrich entities, such as IPs, domains, file hashes, and users, with data from various third-party threat intelligence and information services. Using a block promotes modularity, consistency, and easier maintenance across multiple playbooks.

## Core concepts

  * **Entity:** An object of interest within an alert or case, such as an IP address, domain name, file hash, URL, or username.
  * **Enrichment:** The process of adding context or information to an entity from external data sources. This can include reputation scores, geolocation, WHOIS data, malware analysis results, or user-directory details.
  * **Block:** A reusable set of actions and logic within Google SecOps, similar to a function or subroutine. You can call blocks from multiple playbooks to reduce duplication.
  * **Third-party intelligence services:** External services that provide data for enrichment. Examples include VirusTotal, Mandiant, AbuseIPDB, WHOIS services, and internal custom threat feeds.



## Design the enrichment block

Review the following principles and requirements before you build a block that processes various entity types and queries multiple third-party services.

  * **Inputs:** The block typically operates on the entities present in the alert's context. Actions automatically target entities, so you don't usually need special block inputs.
  * **Outputs:** The block modifies the entities in the alert context by adding new fields or properties that contain the enrichment data. It doesn't usually need to return a specific output value.
  * **Abstraction principles:**
    * **Service-agnostic:** Add or remove intelligence sources.
    * **Entity type handling:** Conditionally execute actions based on the entity type.
    * **Configurable:** Lets you toggle sources and set parameters. For example, set thresholds for suspicious flags through integration settings or environment variables.



## Create the enrichment block

This section describes how to create the enrichment block.

### Define the block

This example creates a block called `TPI_Enrich_Entities` (Third-Party Intelligence Enrich Entities).

To define the block, follow these steps:

  1. Go to **Response** > **Playbooks**.
  2. Click  add  **Add** and select **Block**.
  3. Enter the name for the block: `TPI_Enrich_Entities`.
  4. Provide a clear description: `Enriches entities (IPs, domains, hashes, URLs) using various third-party intelligence services`.
  5. Make the block available for all environments unless service keys are environment-specific.



### Add enrichment actions

To add enrichment actions to the block, drag the following actions (and other services) from the **Actions** set for each third-party service, as required:

  * **VirusTotal v3:**
    * `Enrich Hash`
    * `Enrich IP`
    * `Enrich Domain`
    * `Enrich URL`
  * **Mandiant Threat Intelligence:**
    * `Mandiant Enrich Entities` This action often handles multiple entity types internally.
  * **AbuseIPDB:**
    * `Enrich IP`



### Configure actions

To configure actions, follow these steps:

  1. Double-click each step to configure its parameters.
  2. Select the appropriate integration instance for the environments that need the block. Use **Dynamic** if your integrations aren't in the shared environment.
  3. **Thresholds:** For services, such as VirusTotal, set appropriate detection thresholds (for example: `engine_threshold`).
  4. **Scope:** Most enrichment actions automatically run on all relevant entities in the alert.



### Error handling

To configure the block to deal with errors:

  * Within each action's settings, turn on the **Retry on failure** slider. It's generally best to allow at least one retry on enrichment actions in case of any self-correcting issues with the network or load on the third-party side. Further retries will depend on your API allotments and subject-matter expertise in the third-party integration.
  * Configure the **If action fails** option. It's generally best to set this to **Skip** to prevent the failure of one service from stopping the entire enrichment process. You can view any failed steps manually.



### Save the block

When you finish setting up the block, save it to add to your playbook blocks.

### Extend the block

To extend the block by adding new enrichment sources, follow these steps:

  1. Verify that the integration for the new service is installed and configured in the Content Hub.
  2. Open the `TPI_Enrich_Entities` block to edit it.
  3. **Add Actions** by dragging the relevant enrichment actions from the integration into the block.
  4. Define the new action's parameters and specific settings.
  5. **Test** the block with entities relevant to the new source.



## Use the enrichment block in playbooks

To use the block in playbooks, follow these steps:

  1. Open the playbook where you want to add enrichment. This typically applies to most playbooks.
  2. In the **Playbook** editor, go to the **Blocks** tab.
  3. Drag the `TPI_Enrich_Entities` block into your playbook flow, typically after the trigger and initial triage steps. The block instance doesn't usually need special parameters because it acts on the alert's entities.



#### Example: Default playbook flow

  1. **Trigger** : All alerts

  2. **Action** : Set case stage to `Triage`

  3. **Run block** : `TPI_Enrich_Entities`

  4. **Action** : Continue with manual review or additional analysis.




## Troubleshooting

Issue | Suggestions  
---|---  
Enrichment data not appearing | 

  * Check the case playbook execution log or case wall for errors in the block's actions.
  * Confirm the alert entities match the types supported by the block.
  * Verify you've not exceeded API rate limits.

  
Action failures | 

  * Review error messages in the execution log. Common issues can include network problems, invalid API keys, or service outages.
  * Because actions are set to `Skip` on failure, other services should still run.

  
Unexpected data | 

  * Look at the raw JSON output from the enrichment action to understand the structure.
  * Adjust any custom field mappings or display widgets as needed.

  
  
## Best practices

The following are recommended practices for working with blocks.

### Security

Manage your API keys securely within the settings. Don't hardcode any credentials in playbooks or blocks.

### Efficiency

  * Monitor API rate limits for each third-party service.
  * Avoid excessive calls.
  * Integrations often handle entity-type filtering internally.



### Data handling

  * **Prefix field names:** When enrichment data is added to an entity, use the source name as a key prefix. This is to avoid conflicts and provide clarity. Many integrations do this automatically. If you parse data manually, add prefixes, such as `VT_DetectionRatio`, `MDT_Score`, `AIPDB_Confidence`.
  * **Normalization:** While full normalization within the block can be complex, be aware of different data formats. Aim for consistency in data formats where possible.
  * **JSON Results:** Many actions return JSON. Use built-in JSON-path expressions to extract key information from actions that return JSON.



### Maintenance

  * Update integrations to their latest versions.
  * Periodically review the effectiveness and reliability of each third-party service.
  * Document the included services in the block description.



### Testing

  * Test the block with various alert scenarios containing different entity types.
  * Verify the block adds enrichment data correctly and handles failures gracefully.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
