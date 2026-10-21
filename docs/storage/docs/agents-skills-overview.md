---
url: https://docs.cloud.google.com/storage/docs/agents-skills-overview/
title: Cloud Storage agent skills \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:23.379496+00:00
---

# Cloud Storage agent skills  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/agents-skills-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Cloud Storage agent skills Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage provides agent skills that can help your agent accomplish common tasks. Agents that use these skills can then accomplish tasks with higher fidelity than an agent without the skills.

Agent skills are a standardized way to give AI agents specific knowledge and instructions they can reuse. They contain resources like scripts, reference materials, and templates that help the agent complete tasks accurately and reliably. For more information about skills, see [Agent Skills Overview](https://agentskills.io/home).

## The Cloud Storage basics skill

The Cloud Storage basics skill, [`google-cloud-storage-basics`](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-storage-basics), contains instructions for completing basic tasks in Cloud Storage, such as storing, retrieving, and managing data as objects in buckets, with support for the Google Cloud CLI, APIs, client libraries, Terraform, and Model Context Protocol (MCP).

### Install the Cloud Storage basics skill

To install the `google-cloud-storage-basics` skill, run the following command in your agentic client or terminal:
    
    
    npx skills add google/skills --skill google-cloud-storage-basics
    

### Cloud Storage basics reference files

The Cloud Storage basics agent skill includes several reference files that provide technical depth. These references let the skill execute functions or commands accurately by providing specific context to the underlying model. By default, the Cloud Storage basics skill includes the following reference files:

  * [CLI and API usage](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/cli-api-usage.md)
  * [Cloud Client Libraries usage](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/client-library-usage.md)
  * [Core concepts](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/core-concepts.md)
  * [Data management](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/data-management.md)
  * [Data transfer](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/data-transfer.md)
  * [Cloud Storage FUSE](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/gcsfuse.md)
  * [High-performance storage](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/high-performance-storage.md)
  * [Infrastructure as code (IaC) usage](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/iac-usage.md)
  * [Model Context Protocol (MCP) usage](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/mcp-usage.md)
  * [Storage Intelligence](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/references/storage-intelligence.md)



## The Cloud Storage bucket architect skill

The Cloud Storage bucket architect skill, [`google-cloud-storage-bucket-architect`](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-storage-bucket-architect), contains instructions for designing and creating Cloud Storage buckets tailored to your workload (such as AI/ML, media hosting, archiving, backup, logging, or sensitive data). The skill validates project-level security settings and generates configurations using the Google Cloud CLI, REST APIs, Terraform, or client libraries.

### Install the Cloud Storage bucket architect skill

To install the `google-cloud-storage-bucket-architect` skill, run the following command in your agentic client or terminal:
    
    
    npx skills add google/skills --skill google-cloud-storage-bucket-architect
    

### Cloud Storage bucket architect reference files

The Cloud Storage bucket architect agent skill includes reference files that provide technical depth. By default, the Cloud Storage bucket architect skill includes the following reference files:

  * [AI and machine learning](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/storage_for_ai.md)
  * [Backup and disaster recovery](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/backup_dr.md)
  * [C++ SDK guide](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/sdk_cpp.md)
  * [Cloud Client Libraries overview](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/sdk.md)
  * [Direct user-generated content (UGC) ingestion](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/ugc_ingestion.md)
  * [Draft bucket create plan](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/phase_draft_plan.md)
  * [Google Cloud CLI reference](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/gcloud.md)
  * [Go SDK guide](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/sdk_go.md)
  * [Java SDK guide](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/sdk_java.md)
  * [Log storage](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/log_storage.md)
  * [Long-term archive and compliance](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/archiving_compliance.md)
  * [Media hosting and CDN](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/media_hosting.md)
  * [Output based on user intent](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/phase_output.md)
  * [Preflight and project checks](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/phase_project_checks.md)
  * [Python SDK guide](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/sdk_python.md)
  * [REST API reference](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/rest.md)
  * [Sensitive data and compliance](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/sensitive_data.md)
  * [Static website hosting](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/static_website.md)
  * [Terraform reference](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/references/terraform.md)



## The Cloud Storage FUSE skill

The Cloud Storage FUSE skill, [`google-cloud-storage-fuse`](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-storage-fuse), contains instructions for mounting Cloud Storage buckets as a POSIX file system with Cloud Storage FUSE, covering mount flag and cache tuning, performance diagnosis, and AI/ML and Google Kubernetes Engine (GKE) workload configurations.

### Install the Cloud Storage FUSE skill

To install the `google-cloud-storage-fuse` skill, run the following command in your agentic client or terminal:
    
    
    npx skills add google/skills --skill google-cloud-storage-fuse
    

### Cloud Storage FUSE reference files

The Cloud Storage FUSE agent skill includes reference files that provide technical depth. By default, the Cloud Storage FUSE skill includes the following reference files:

  * [Checkpoint and write safety](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-fuse/references/checkpoint-safety.md)
  * [GKE training deployment](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-fuse/references/gke-training-deployment.md)
  * [Performance and cost diagnosis](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-fuse/references/performance-diagnosis.md)



## What's next

  * To view the Cloud Storage basics `SKILL.md` file, see [`SKILL.md` (basics)](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-basics/SKILL.md).
  * To view the Cloud Storage bucket architect `SKILL.md` file, see [`SKILL.md` (bucket architect)](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-bucket-architect/SKILL.md).
  * To view the Cloud Storage FUSE `SKILL.md` file, see [`SKILL.md` (FUSE)](https://github.com/google/skills/blob/main/skills/cloud/google-cloud-storage-fuse/SKILL.md).
  * To learn more about agent skills, see [Agent Skills Overview](https://agentskills.io/home).
  * To view `SKILL.md` files for other Google Cloud products, see [`google/skills`](https://github.com/google/skills#agent-skills).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
