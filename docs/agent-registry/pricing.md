---
url: https://docs.cloud.google.com/agent-registry/pricing/
title: Agent Registry pricing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:20.047223+00:00
---

# Agent Registry pricing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/pricing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Resources ](https://docs.cloud.google.com/agent-registry/resources)



Send feedback 

#  Agent Registry pricing Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the pricing details for Agent Registry. You can register, catalog, and discover resources in Agent Registry at no charge, and you pay only for optional value-added security features that you use.

## Pricing overview

Agent Registry provides baseline catalog registration, storage, and discovery at no charge. There are no charges for registering, storing, updating, or searching [agents](https://docs.cloud.google.com/agent-registry/concepts#agent), [MCP servers](https://docs.cloud.google.com/agent-registry/concepts#server), [endpoints](https://docs.cloud.google.com/agent-registry/concepts#endpoint), [skills](https://docs.cloud.google.com/agent-registry/concepts#skill), or [skill revisions](https://docs.cloud.google.com/agent-registry/concepts#skill-revision) in Agent Registry.

Consumption charges apply only when you use skill vulnerability scanning to scan new skill revisions for security risks, such as prompt injection or data exfiltration patterns.

The following table summarizes the pricing for Agent Registry features in US dollars (USD):

Feature | Billing metric | Price (USD) | Effective date  
---|---|---|---  
Catalog storage for agents, MCP servers, endpoints, skills, and skill revisions | `agentregistry.googleapis.com/object_storage` | Included at no charge ($0.00) | Always  
Catalog discovery, search, and Agent Registry API operations | None | Included at no charge ($0.00) | Always  
Skill vulnerability scanning | `agentregistry.googleapis.com/token_usage` | Included at no charge ($0.00) | Through December 31, 2026  
$8.00 per 1 million input tokens | January 1, 2027  
  
## Skill vulnerability scanning pricing

Skill vulnerability scanning inspects uploaded skill packages for security vulnerabilities when you create a skill revision. Through December 31, 2026, skill vulnerability scanning is available at no charge. Starting January 1, 2027, skill vulnerability scanning costs $8.00 per 1 million input tokens.

### Pricing updates and billing schedule

Storing, managing, and discovering skills in Agent Registry is included at no charge ($0.00). You aren't charged for skill storage or catalog operations. You're billed only when Agent Registry scans a new skill revision for vulnerabilities.

The following schedule applies to billing for skills in Agent Registry:

  * **Through December 31, 2026** : Skill vulnerability scanning in Agent Registry continues to be available at no charge ($0.00).
  * **January 1, 2027** : Consumption billing ($8.00 per 1 million input tokens) takes effect for skill vulnerability scanning in Agent Registry.



### Scanning charges

Agent Registry triggers an asynchronous vulnerability scan only when all of the following conditions are met:

  * You [register a new skill](https://docs.cloud.google.com/agent-registry/register-skills) with an initial revision payload or [create a new skill revision](https://docs.cloud.google.com/agent-registry/manage-skill-revisions#create-revision) by uploading a ZIP archive.
  * The skill's `scanningConfig.policy` field is set to `ENABLED_BLOCKING`, which is the default setting for new skills, or `ENABLED_NONBLOCKING`.



There are no scanning charges for the following resources and operations:

  * **Existing skill revisions** : Agent Registry doesn't retroactively scan existing skill revisions. You are billed only when you upload a new skill revision.
  * **Skills with scanning disabled** : No scanning charges apply when a skill's `scanningConfig.policy` field is set to `DISABLED`.
  * **Google-created skills** : Pre-registered skills from [Google publishers](https://docs.cloud.google.com/agent-registry/concepts#publisher) don't incur scanning charges in your project.
  * **Metadata updates and payload downloads** : Updating skill metadata, changing a skill's lifecycle state or default revision pointer, searching skills, or downloading skill revision payloads doesn't trigger a scan and incurs no charges.



### Token usage for skill scanning

Agent Registry measures skill vulnerability scanning charges strictly on the input tokens in your uploaded skill package, including the `SKILL.md` instruction file, code scripts, and text assets inside the ZIP archive.

You aren't billed for internal security system prompts, multi-model evaluation passes, intermediate model reasoning tokens, or output tokens generated by the vulnerability scanner.

### Pricing example

Suppose you upload a new skill revision packaged as a 10 KB ZIP archive. A typical skill package between 8 KB and 12 KB contains approximately 2,000 to 3,000 input tokens:

  * **Uploaded skill content** : 2,500 input tokens (0.0025 million input tokens)
  * **Unit price (starting January 1, 2027)** : $8.00 per 1 million input tokens
  * **Total cost for the revision scan** : 0.0025 × $8.00 = $0.02



Subsequent searches, metadata updates, and runtime downloads of that skill revision incur $0.00 in Agent Registry charges.

### Manage and disable scanning costs

By default, new skills in Agent Registry set `scanningConfig.policy` to `ENABLED_BLOCKING`. If you want to register skills or upload skill revisions without incurring skill vulnerability scanning charges, you can set the scanning policy on a skill to `DISABLED`.

You can configure the scanning policy using the Google Cloud CLI or the Agent Registry API:

###  gcloud 

To create a skill with vulnerability scanning disabled, include the `--scanning-policy=disabled` flag:
    
    
    gcloud alpha agent-registry skills create SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION \
      --display-name="DISPLAY_NAME" \
      --description="DESCRIPTION" \
      --scanning-policy=disabled \
      --payload="LOCAL_ZIP_PATH"
    

To disable vulnerability scanning on an existing skill before uploading new revisions, run the `skills update` command with the `--scanning-policy=disabled` flag:
    
    
    gcloud alpha agent-registry skills update private-SKILL_ID \
      --project=PROJECT_ID \
      --location=LOCATION \
      --scanning-policy=disabled
    

Replace the following:

  * `SKILL_ID`: the ID of the skill.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the registry location, such as `global`.
  * `DISPLAY_NAME`: a display name for the skill.
  * `DESCRIPTION`: a description of the skill.
  * `LOCAL_ZIP_PATH`: the local path to your skill ZIP archive.



###  REST 

To disable vulnerability scanning on an existing skill using the REST API, set `scanningConfig.policy` to `DISABLED` in your `PATCH` request body:
    
    
    curl -X PATCH \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          -d '{
            "scanningConfig": {
              "policy": "DISABLED"
            }
          }' \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/skills/private-SKILL_ID?updateMask=scanningConfig"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the registry location, such as `global`.
  * `SKILL_ID`: the ID of the skill.



Allowed values for `scanningConfig.policy` are `ENABLED_BLOCKING`, `ENABLED_NONBLOCKING`, and `DISABLED`.

## Costs for other Google Cloud services

Catalog storage and discovery in Agent Registry are included at no charge, but you might incur separate charges when you use other Google Cloud services with Agent Registry:

  * **Cloud Storage** : If you import skill ZIP archives from a Cloud Storage bucket, standard [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing) applies to objects stored in your bucket.
  * **Agent and tool runtimes** : Hosting and executing agents or MCP servers on runtimes such as Agent Runtime on Gemini Enterprise Agent Platform, Cloud Run, or Google Kubernetes Engine (GKE) incurs standard compute and runtime charges for those services.



## What's next

  * Get help with [billing questions](https://docs.cloud.google.com/agent-registry/billing-questions) or read the [Cloud Billing documentation](https://docs.cloud.google.com/billing/docs).
  * Learn how to [register skills](https://docs.cloud.google.com/agent-registry/register-skills) and [manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).
  * View [quotas and limits](https://docs.cloud.google.com/agent-registry/quotas) for Agent Registry.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
