---
url: https://docs.cloud.google.com/application-design-center/docs/agent-skills-overview/
title: App Design Center agent skills \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:02.480251+00:00
---

# App Design Center agent skills  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/agent-skills-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  App Design Center agent skills Stay organized with collections  Save and categorize content based on your preferences. 

Application Design Center provides an agent skill, [`application-design-center-design-deploy`](https://github.com/google/skills/tree/main/skills/cloud/application-design-center-design-deploy), that can help your agent accomplish common tasks. The skill contains instructions for completing basic tasks in App Design Center, such as designing, validating, deploying, and troubleshooting infrastructure. Agents that use this skill can then accomplish these tasks with higher fidelity than an agent without the skill.

Agent skills are a standardized way to give AI agents specific knowledge and instructions they can reuse. They contain resources like scripts, reference materials, and templates that help the agent complete tasks accurately and reliably. For more information about skills, see [Agent Skills Overview](https://agentskills.io/home).

## Install skills

To install the `application-design-center-design-deploy` skill, use the following command:
    
    
    npx skills add google/skills --skill application-design-center-design-deploy
    

## `application-design-center-design-deploy` reference

The `application-design-center-design-deploy` agent skill includes several reference files that provide technical depth. These references let the skill execute functions or commands accurately by providing specific context to the underlying model. The application-design-center-design-deploy skill includes the following references:

  * [Application troubleshooting](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/adc_application_troubleshooting.md): analyzes and resolves deployment failures for App Design Center applications.
  * [Design guide](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/design_guide.md): designs modular Terraform architectures and performs local CLI validation.
  * [Error analysis guide](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/error_analysis_guide.md): analyzes deployment errors and identifies failing components in App Design Center.
  * [Generator instructions](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/generator_instructions.md): generates raw Terraform configurations.
  * [Planner instructions](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/planner_instructions.md): translates design queries into Google Cloud architectures.
  * [Raw Terraform troubleshooting](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/raw_terraform_troubleshooting.md): analyzes and resolves direct Terraform deployment and configuration errors.
  * [Remediation guide](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/remediation_guide.md): constructs remediation plans and configures component parameters for deployment failures.
  * [Terraform validator instructions](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/terraform_validator_instructions.md): reviews and verifies Terraform module configurations.
  * [Troubleshooting guide](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/references/troubleshooting_guide.md): guides the troubleshooting process for application deployments and Terraform configurations.



## What's next

  * To view the `application-design-center-design-deploy` `SKILL.md` file, see [`SKILL.md`](https://github.com/google/skills/blob/main/skills/cloud/application-design-center-design-deploy/SKILL.md).
  * To learn more about agent skills, see [Agent Skills Overview](https://agentskills.io/home).
  * To view `SKILL.md` files for other Google Cloud products, see [`google/skills`](https://github.com/google/skills#agent-skills).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
