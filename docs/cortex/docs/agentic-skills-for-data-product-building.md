---
url: https://docs.cloud.google.com/cortex/docs/agentic-skills-for-data-product-building/
title: Build data products with agent skills \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:17.235517+00:00
---

# Build data products with agent skills  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/agentic-skills-for-data-product-building/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build data products with agent skills

## Overview

This guide describes how to use specialized Cortex Framework agentic skills-provided directly by Cortex Framework in the GitHub repository-with an AI coding assistant (such as [Gemini](https://cloud.google.com/gemini) paired with the [Antigravity](https://antigravity.google/) agentic development framework) to build custom data products that follow Cortex Framework best practises.

Cortex Framework provides specialized agent skills to extend its capabilities, enabling your AI assistant to guide you through the process of building data products that follow Cortex Framework best practices. With these capabilities, you can use natural language to request a new data product based on specific business requirements. For example, you can ask for an Accounts Payable consumption data product to gain insights into total due, past due amounts, and turnover. The result is a fully integrated Cortex Framework data product—built based on your customer-specific requirements and data—that is ready for execution.

### Agent skills

[Agent skills](https://agentskills.io/home) are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. At its core, a skill is a folder containing a `SKILL.md` file (which includes metadata and instructions) along with optional scripts, references, and assets that instruct an agent how to perform a specific task. Skills package procedural knowledge and context into portable folders that agents load on demand, providing domain expertise and repeatable workflows. Cortex Framework skills are stored in [`.agent`](https://github.com/GoogleCloudPlatform/cortex-framework/tree/main/.agents/skills) directory.

### Cortex Framework agent skills

The agentic data product builder automates the end-to-end development lifecycle of data products within Cortex Framework. By instructing your AI assistant to execute structured development workflows, you eliminate the need to manually scaffold file structures, navigate complex SAP schemas, configure foundation layers, manage custom namespaces, and write boilerplate Dataform SQLX code.

The AI assistant manages the following core tasks:

  * **Planning and requirements mapping** : Translates concrete business requirements into an actionable data modeling and development plan.
  * **Live schema lookup** : Executes scripts that query replicated SAP Data Dictionary (DDIC) tables to provide customer-specific context information, such as custom Z-fields.
  * **Boilerplate scaffolding** : Generates all required configuration files, metadata, and SQLX or JavaScript code artifacts automatically.
  * **Data quality gates** : Validates data products by running local builds, compiling SQL code, executing unit and integration tests, and verifying compliance with naming standards.
  * **Documentation creation** : Creates documentation assets automatically, including visualizing the entity relationship (ER) diagrams and primary keys of your data product module.



Developing data products with these agentic skills is an iterative process. You can start with your initial goals, review the agent's proposed implementation plan including ER diagrams and schemas, and ask the AI assistant to refine the logic conversationally as you go. While the agent accelerates development, you remain in full control to review and approve all generated code before committing to your repository. Furthermore, because these agentic scripts execute locally using your authenticated credentials, they inherently respect your existing Google Cloud and BigQuery access limits.

## Prerequisites

Before using the agentic skills, verify that your development environment meets the following requirements to enable live schema queries, data compilation, and automated validation:

  1. **Google Cloud SDK (`gcloud`)**: Install and authenticate the (`gcloud`) CLI with your user account. For more information, see [deployment documentation](https://docs.cloud.google.com/cortex/docs/prerequisites#configure-Google%20Cloud%20SDK)

  2. **Application Default Credentials (ADC)** : Configure your local ADC and project targets so that local compilation tools and pytest suites can communicate with BigQuery. For more information, see [prepare your default Google Cloud project](https://docs.cloud.google.com/cortex/docs/prerequisites#prepare-your-Google%20Cloud-target-project)

  3. **Replicated SAP Data Dictionary (DDIC) Tables** : To allow the agent to perform case-insensitive schema checks and accurately verify field lengths, replicate the following SAP metadata tables in your raw target BigQuery dataset:

     * `DD03L` (Table Fields)
     * `DD04T` (Data Element Texts)
     * `DD08L` (Table Relationships)
     * `DD01L` (Domains)
     * `DD07L` (Domain Values - optional)
     * `DD07T` (Domain Value Texts - optional)
  4. **Local Python Environment** : Install local dependencies and run the sync tool using `uv` to ensure validation libraries and unit tests function properly. For more information, see [documentation](https://docs.cloud.google.com/cortex/docs/prerequisites#install_uv).




## Setup and IDE Configuration

Before you begin, refer to the documentation of your preferred AI coding assistant for installation and setup instructions (for example, [Antigravity](https://antigravity.google/)). 

  1. Gather the required installation artifacts and clone the repository. For more information, see [Installation Artifacts](https://docs.cloud.google.com/cortex/docs/prerequisites#installation_artifacts).

  2. Open the cloned Google Cloud Cortex Framework source code footprint within your designated AI coding assistant.




Google Cloud Cortex Framework exposes its agentic capabilities through a set of specialized skills located in the `.agents/skills/` directory of the repository. You can use these skills across multiple development environments:

  * **Antigravity framework** : Antigravity automatically discovers, indexes, and activates all workspace skills upon startup. No additional configuration is required. To verify, ask the assistant:

> _What skills do you have available?_

  * **VSCode with Gemini Code Assist** :

    1. Install the Gemini Code Assist extension from the VS Code Marketplace.
    2. Open the `cortex-framework-core` folder as a workspace. The assistant automatically scans and loads the skills from `.agents/skills/` directory.
  * **Other AI CLI Tools** : Reference the skills directory natively in your instruction prompts. For example:

> _Read the create-data-product skill inside the .agents/skills/ directory and scaffold..._




* * *

## Create a custom data product

The following steps outline the structured developer workflow for using agentic skills to create a custom data product.

### Step 1: Step 1: Provide requirements and context

Using your AI coding assistant's chat interface, provide a prompt that describes your specific data requirements. For example:

> Create a Cortex Framework data product for Accounts Payable Insights targeted at SAP S/4HANA and ECC. Use the namespace: custom_finance. The primary business requirement is to track total due and past due amounts across our vendors, and to calculate our accounts payable turnover rate by company code.

Note that you can also reference existing requirements or specification documents directly in your prompt. These documents (which can be in Markdown or other structured formats) provide the agent with vital context, such as:

  * **Business context and domain** : Detailed objectives, user stories, and target consumers.
  * **Input data specifications** : List of source tables (e.g., `LFA1`, `BSIK`, `BSEG` ,`Z...`), versioning details (ECC versus S/4HANA), exclusion rules, custom fields, and more.
  * **Transformation logic and business rules** : Core mapping constraints, client filtering (`mandt`), soft deletes (`loekz`), handling payment block indicator (`zlspr`) mappings, and reconciliation rules (for example, excluding intercompany vendor transactions to avoid skewed turnover rates).
  * **Data integrity and test assertions** : Verification scenarios (for example, verifying grain uniqueness and ensuring that the sum of open invoice amounts in the final output exactly matches the raw source tables).



### Step 2: Review the implementation plan

After you outline the requirements, the agent uses multiple skills-such as `query-sap-ddic` skill to query your raw BigQuery DDIC metadata tables. This allows the agent to identify and validate your required source tables, ensuring that field types and relationships are accurate. The agent may also invoke other skills to ensure your requirements align perfectly with Cortex Framework best practices.

Before starting the implementation, the agent provides a brief implementation plan for your review. This plan includes the identified source tables, mappings, and the proposed architectural structure of the data product. Review this plan and request any adjustments before confirming.

### Step 3: Generate the data product

After you confirm the implementation plan, the agent utilizes the `create-data-product` skill to scaffold the directory structure. This isolates your new custom developments from core platform updates under your designated custom namespace:
    
    
    src/data_modules/<custom_namespace>/products/<dataproductname>/
    ├── manifest.yaml
    ├── table_settings.default.yaml
    ├── README.md
    ├── definitions/
    │   └── [ecc|s4]/
    │       └── <product_name>.js
    └── annotations/
        └── [ecc|s4]/
            └── <product_name>.yaml
    

For more information about the folder structure and the individual files, see the [Extensibility Guide](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product) documentation.

During this phase, you can also ask the agent to automatically visualize the relationships using the generate-er-diagram skill, or to scaffold assertions using the create-python-tests skill.

### Step 4: Run quality gates and verify data

Depending on its granted permissions, the agent will either automatically execute the following mandatory validation gates or prompt you to run them. Throughout this process, the agent generates granular status reports so you can review the outcomes:

  1. **Build validation** : Executes `uv run cortex-build --config config/config.yaml` to ensure all generated SQL models compile successfully, producing a build summary.
  2. **Pytest execution** : Runs the full suite of Python unit tests, outputting a test execution report that verifies your core business logic and assertions.
  3. **Linter and audits** : Leverages the `validate-data-product` skill to perform strict field parity checks and verify naming convention compliance, concluding with a detailed readiness report.



### Step 5: Deploy and execute

After you review the validation reports and approve the generated code, you are ready to deploy your data product assets.

  * **Deploy assets** : Push the compiled data product definitions to your configured Dataform workspace by executing the deployment script locally (for example, uv run cortex-deploy --config config/config.yaml).
  * **Materialize data** : Complete the final post-deployment workflow to execute the generated Dataform pipelines, materializing your new tables and views directly within BigQuery.
  * **Deliver insights** : Once materialized, your custom data product is fully ready to be connected to downstream analytical apps—such as Gemini Enterprise—to deliver intelligent, actionable answers to your original business questions.



## Update an existing data product

Once your custom data product is built, you don't need to start from scratch to make modifications. You can leverage the `update-data-product` skill to iteratively add new fields, adjust business logic, or integrate entirely new source tables. For example: 

> Update my custom_finance AP data product. Add the payment terms field (ZTERM) from the LFA1 source table, and ensure it is properly mapped to the final output view. Run the build validation when you are finished.

The agent will locate the configuration, query the BigQuery DDIC for the exact field requirements, update your Dataform code, and execute the necessary build checks to verify the change.

## Best practices and limitations

  * **Schema query failures** : If the agent fails to fetch SAP metadata schemas, verify that your local Application Default Credentials (ADC) are active and hold the BigQuery Data Viewer IAM role for the target raw dataset.
  * **Context limits** : If you are building an exceptionally large data product involving dozens of tables, the agent might lose context. Broaden your success rate by providing smaller, atomic instructions (for example, instruct the agent to build the header-level dimensions first, and then add item-level facts in a separate, follow-up prompt).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
