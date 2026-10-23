---
url: https://docs.cloud.google.com/agent-registry/skills-architecture/
title: Skills architecture \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:21.167526+00:00
---

# Skills architecture  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/skills-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Skills architecture Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In Agent Registry, skills let you package instructions, optional scripts, and domain knowledge into modular capabilities that extend an agent's reasoning and workflow. By registering standalone skills in Agent Registry, you can centrally version, govern, and share reusable task logic across your agents. Agent Registry also indexes inline A2A skills declared on your agents' Agent Cards so other agents can discover and invoke them.

## Skill types

Agent Registry supports two types of skills:

  * **Standalone skills** : version-controlled packages registered as top-level `Skill` resources in Agent Registry. Standalone skills contain `SKILL.md` instruction files, optional scripts, and metadata assets managed independently of any single agent deployment.
  * **A2A skills** : capability descriptions listed inline in the `skills` field of an agent's `agent-card.json` [Agent Card](https://agent2agent.info/docs/concepts/agentcard/) that tell other agents when and how to delegate work to it.



For a comparison of these two models, see Differences between standalone and A2A skills.

## Standalone skills

Standalone skills are top-level resources in Agent Registry, governed alongside agents, MCP servers, and endpoints. Unlike those components, standalone skills don't use separate [`Service` resources](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#agentic-components-representation). Instead, you register, version, and query standalone skills directly across three resource levels:

  * **Publishers** : `Publisher` resources that establish the ownership, verification tier, and [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) syntax for a collection of skills.
  * **Skill containers** : top-level `Skill` resources in Agent Registry that consumers discover and resolve at runtime, each maintaining a pointer to a default serving revision of the skill.
  * **Skill revisions** : immutable, read-only `SkillRevision` resources containing a skill package's instructions, optional scripts, and metadata assets at a specific version.



### Publishers

Every standalone skill in Agent Registry belongs to a publisher. Publishers establish the provenance, verification tier, and naming prefix for skills:

  * **Google-managed publishers (`FIRST_PARTY`)**: verified publishers that Google manages, such as `cloud.google.com` and `discoveryengine.googleapis.com`. Google-managed skills from these publishers are discoverable across all projects when you set up Agent Registry and use the following [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) format: `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`. For example: `urn:skill:discoveryengine.googleapis.com:discoveryengine:report-writing`.
  * **Private publishers (`PRIVATE`)**: the default `private` publisher automatically assigned to custom skills that you manually register within a Google Cloud [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project). To prevent naming collisions with verified Google-managed skills, Agent Registry automatically prepends the `private-` prefix to the [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers). You can't register custom `Publisher` resources. Private skills use the following Uniform Resource Name (URN) format for the skill identifier: `urn:skill:projects-PROJECT_NUMBER:locations:LOCATION:private-SKILL_ID`. For example: `urn:skill:projects-PROJECT_NUMBER:locations:global:private-incident-triage`.



For instructions on inspecting publishers, see [Review skill publisher details](https://docs.cloud.google.com/agent-registry/review-publishers).

### Skill containers

A skill container is a `Skill` resource that represents a standalone skill within a governance project and location. For a manually created skill, Agent Registry generates a [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) in the format `projects/PROJECT_NUMBER/locations/LOCATION/skills/private-SKILL_ID`.

The `Skill` resource serves as the stable reference point for discovery in Agent Registry and maintains the following fields:

  * **Descriptive metadata** : the human-readable display name (`displayName`), summary description (`description`), [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) (`skillId`), and publisher attribution.
  * **Default revision pointer** : the `defaultRevision` field, which references the specific `SkillRevision` resource served when consumers resolve or download the skill without requesting an explicit revision ID.
  * **Target lifecycle state** : the `targetState` field, which controls whether the skill is in an active, disabled, deprecated, or decommissioned state.



For instructions on viewing and updating skills, see [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).

### Skill revisions

A skill revision (`SkillRevision`) resource represents an immutable, versioned snapshot of a skill package. The [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) is in the following format: `projects/PROJECT_NUMBER/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID`.

When you update a skill's instructions, optional scripts, or metadata assets, you don't modify the existing package in place. Instead, you upload a new ZIP archive to create a new revision. When Agent Registry validates that the archive meets the [Agent Skills Specification](https://agentskills.io/specification#validation) and [ingestion payload constraints](https://docs.cloud.google.com/agent-registry/register-skills#payload-constraints), the revision enters the **Active** (`ACTIVE`) state. You can then [update the default revision pointer](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill) on the parent skill to serve the new revision. If you delete the revision that is set as the skill's default revision, Agent Registry clears the `defaultRevision` pointer and transitions the active skill to the **Disabled** (`DISABLED`) state.

Separating the skill container from its skill revision snapshots provides the following benefits:

  * **Deterministic execution** : agents pinned to a specific revision are protected from unexpected prompt changes or script updates.
  * **Controlled rollbacks** : you can upload and verify new skill revisions, or revert the `defaultRevision` pointer to an earlier revision if an issue occurs.
  * **Auditability** : historical revisions of the skill package remain preserved and inspectable until explicitly deleted.



For instructions on uploading, downloading, and deleting revisions, see [Manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).

## Package specification

Standalone skills are packaged as ZIP archives that comply with the open standard [Agent Skills Specification](https://agentskills.io/specification).

The archive must contain a `SKILL.md` file at its root, as well as any scripts or metadata assets that are required by the skill. The `SKILL.md` file defines the instructions for the skill. This file combines YAML front matter metadata, such as `name` and `description`, with natural language instructions interpreted by agent runtimes, and references to any optional scripts or supporting assets in the archive.

When you register a skill or create a revision, Agent Registry validates the archive against [ingestion payload constraints](https://docs.cloud.google.com/agent-registry/register-skills#payload-constraints), parses the `SKILL.md` file, and indexes its metadata for search and discovery.

## Skill lifecycle states

To control how a standalone skill is resolved and downloaded at runtime, you can transition the `targetState` of the skill container across four states:

  * **Active (`ACTIVE`)**: the skill is served, indexed for discovery, and available for runtime resolution and payload downloads. Setting a skill to **Active** requires its `defaultRevision` pointer to reference an active `SkillRevision` resource.
  * **Disabled (`DISABLED`)**: the default initial state when a skill is created. The skill isn't served at runtime, and resolution and payload downloads fail immediately. A skill also transitions to the **Disabled** state if its `defaultRevision` pointer is cleared or if its default revision is deleted. Unlike the **Decommissioned** state, you can enable a disabled skill by setting a valid `defaultRevision` and updating its target state to **Active**.
  * **Deprecated (`DEPRECATED`)**: the skill remains resolvable and downloadable, but indicates to consumers that it will be decommissioned.
  * **Decommissioned (`DECOMMISSIONED`)**: a final state where the skill is permanently deactivated, no longer served, and can't be reverted to **Active** or any other state. A skill can be decommissioned only after it has been deprecated.



You can update a skill's lifecycle state using the Google Cloud console, the Google Cloud CLI, or the Agent Registry API without deleting historical revisions. To download a revision's ZIP payload, the parent skill must be in the **Active** or **Deprecated** state, and the revision itself must be in the **Active** state. For step-by-step instructions, see [Manage skill lifecycle states](https://docs.cloud.google.com/agent-registry/manage-skills#lifecycle).

## Differences between standalone and A2A skills

Agent Registry supports both standalone skills and inline A2A skills. The following table compares their characteristics:

Characteristic | Standalone skill | Inline A2A skill  
---|---|---  
**Resource type** | Top-level `Skill` resource in Agent Registry with child `SkillRevision` resources. | Nested array within the `Agent` resource.  
**Package content** | ZIP archive containing `SKILL.md`, optional scripts, and supporting assets. | JSON object in the Agent Card containing `id`, `name`, and `description`.  
**Versioning model** | Immutable skill revision snapshots with a configurable `defaultRevision` pointer. | Tied directly to updates of the agent's `agent-card.json`.  
**Execution model** | Downloaded and loaded into an agent's context or runtime environment. | Advertises task capabilities for inter-agent delegation.  
**Specification** | [Agent Skills Specification](https://agentskills.io/specification). | [Agent2Agent (A2A) specification](https://a2a-protocol.org/).  
**Governance scope** | Governed across projects independently of individual agent deployments. | Coupled to the lifecycle of the host agent deployment.  
  
## What's next

  * [Register skills](https://docs.cloud.google.com/agent-registry/register-skills).
  * [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).
  * [Manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).
  * [Review skill publisher details](https://docs.cloud.google.com/agent-registry/review-publishers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
