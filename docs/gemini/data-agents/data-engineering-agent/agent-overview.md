---
url: https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/agent-overview/
title: Data Engineering Agent overview \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:59.162766+00:00
---

# Data Engineering Agent overview  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/agent-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Data Engineering Agent overview Stay organized with collections  Save and categorize content based on your preferences. 

The Data Engineering Agent lets you to build, modify, and troubleshoot data pipelines in BigQuery using natural language prompts. The Data Engineering Agent offers the following capabilities to streamline your data engineering workflows to ingest data into BigQuery:

  * **Dataform integration** : The agent generates and organizes data pipeline code directly within Dataform repositories and workspaces.
  * **Plan generation** : The agent can summarize its thinking and generate a plan that lets you review and verify the agent's plan before proceeding.
  * **Code validation** : The agent automatically validates and fixes compilation errors of any generated code to ensure that the data pipeline is functional.
  * **Automatic data wrangling** : The agent performs data wrangling and transforms raw data into structured tables without manual intervention.
  * **Custom instructions** : The agent supports custom agent instructions that let you define specific rules and reusable guidelines in natural language.
  * **External context** : The agent is integrated with Knowledge Catalog for additional context.
  * **Pipeline control** : You can review and customize generated agent plans before any actions are executed.
  * **Optimization** : The agent can optimize performance in your data pipeline.
  * **Troubleshoot and repair** : The agent can troubleshoot pipeline failures and fix its code.
  * **Interactive recommendations** : The agent provides interactive, context-aware recommendations at the beginning and throughout the session.
  * **Knowledge Catalog metadata enrichment** : The agent can automatically generate Knowledge Catalog metadata from your table configurations, and can send the metadata to Knowledge Catalog during pipeline execution.



## Where you can use the Data Engineering Agent

You can use the Data Engineering Agent with the following methods:

  * [Build data pipelines from the BigQuery pipelines interface or in Dataform](https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines).
  * [Install the Google Cloud Data Agent Kit extension in Visual Studio Code](https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/use-in-ide) to build data pipelines from your integrated development environment (IDE).
  * Use the [Data Engineering Agent API](https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/api-overview).



## How the Data Engineering Agent uses your data

To produce higher-quality agent responses, the Data Engineering Agent can retrieve additional data and metadata from BigQuery and Knowledge Catalog, including sample rows from BigQuery tables and data scan profiles generated in Knowledge Catalog. The agent doesn't use this data for training; it uses the data only as additional context during agent conversations to inform its responses.

## Where the Data Engineering Agent processes your data

For more information about the locations where the Data Engineering Agent processes your data, see [Where Gemini in BigQuery processes your data](https://docs.cloud.google.com/bigquery/docs/gemini-locations).

## Limitations

The Data Engineering Agent has the following limitations:

  * The Data Engineering Agent doesn't support natural-language commands for the following file types: 
    * Notebooks
    * Data preparation
  * The Data Engineering Agent cannot execute pipelines. You must review and run or schedule pipelines.
  * The Data Engineering Agent cannot search any web links or URLs provided through instructions or direct prompts.
  * When importing files in an [agent instruction file](https://docs.cloud.google.com/gemini/data-agents/data-engineering-agent/agent-overview#agent_instructions), the `@` import syntax supports only paths that begin with `./`, `/`, or a letter.
  * The [data preview](https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines#review_a_data_pipeline) feature is supported only for tables, declarations, or queries with the `hasOutput` flag set to `true`.
  * The Data Engineering Agent is subject to the [general limitations of AI technology](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).
  * When creating pipelines over Apache Iceberg external tables managed by the Lakehouse runtime catalog (formerly BigLake metastore), all [Lakehouse runtime catalog limitations](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs#limitations) apply. Most notably, the agent cannot generate write mutations (such as `INSERT`, `UPDATE`, `DELETE`, or `MERGE`) or DDL statements (such as `CREATE TABLE` or `DROP TABLE`) on Iceberg tables. For more information, see [Apache Iceberg REST catalog endpoint concepts](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types).



## Agent features and customizations

The following sections describe additional agent capabilities and other methods to customize the Data Engineering Agent.

### Agent instructions

Agent instructions are natural-language instructions for the Data Engineering Agent that let you store persistent instructions so the agent follows a set of custom, predefined rules. Use agent instructions if you want the agent's results to be consistent across your organization—for example, with naming conventions or to enforce a style guide.

To create agent instructions for the Data Engineering Agent, create a [`GEMINI.MD` context file](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer#create-context-file) as an agent instruction file.

#### Best practices with agent instruction files

When you use agent instructions, we recommend the following:

  * All file paths in Dataform are relative to the root of the repository. Use relative paths for any `@file.md` syntax to properly import instructions to `GEMINI.md`.
  * Files imported in `GEMINI.md` can themselves contain imports, which can create a nested structure. To prevent infinite recursion, `GEMINI.md` has a maximum import depth of five levels.
  * To share instructions across data pipelines, store instructions in a central Dataform repository and link them to the working Dataform repository. You can use local instructions to override central rules for pipeline-specific behavior.
  * To ensure consistency in your project, you can link to naming convention files or style guides and instruct the agent to follow these guidelines when working with your data pipelines.
  * You can suggest data layers in the instruction file to group different types of data together.
  * Using headings and lists in the agent instruction file can help organize and clarify instructions for the Data Engineering Agent.
  * Provide meaningful filenames and group similar instructions together in a file. Organize rules logically by category, feature, or functionality with Markdown headings.
  * To avoid conflicting instructions, clearly define the specific conditions under which each instruction applies.
  * Iterate and refine your prompts and workflow. Agent behavior changes over time with agent rollouts and model upgrades, so we recommend iterating on your rules with different prompts to identify areas that might need improvement. Keep your rules file in sync with any changes to your data pipeline.



The following example shows an agent instruction file named `GEMINI.md` that utilizes our best practices for effective use of the Data Engineering Agent:
    
    
      ### Naming Conventions
    
      * Datasets: [business_domain]_[use_case] (e.g., ecommerce_sales)
    
      * Tables:
          - Raw/External: raw_[source_name]
          - Staging: stg_[business_entity]
          - Dimension: dim_[dimension_name]
          - Fact: fct_[fact_name]
    
      * Dataform folders:
          - sources
          - staging
          - marts
          - dataProducts
    
      * Views: vw_[view_name]
    
      * Columns: snake_case (e.g., order_id, customer_name)
    
      ## Cloud Storage data load
      * When ingesting data from Cloud Storage, create external tables.
    
      ## Null handling
      * Filter out null id values
    
      ## String normalization
      * Standardize string columns by converting to lower case
    
      ## Data cleaning guidelines
      @./generic_cleaning.md
    

#### Import additional local files as agent instructions

You can also import other instruction files for the Data Engineering Agent into the `GEMINI.md` file with `@file.md` syntax. For more information, see [Memory Import Processor](https://geminicli.com/docs/reference/memport/).

### Automatic data wrangling

You can use the Data Engineering Agent to transform raw, unprocessed data into structured tables suitable for data analysis. When requested, the agent first samples up to 1,000,000 records from each standard or external table. The agent then performs deep data analysis by running profiling queries on this sample. After generating data transformations, the agent repeats this sampling and profiling process to assess the quality of the transformations. These data wrangling transformations might include fixing data inconsistencies, outliers, or type mismatches. The Data Engineering Agent then creates a plan that outlines the proposed wrangling steps for you to review and refine before any action occurs.

The Data Engineering Agent also initiates the data wrangling analysis whenever you add a raw table, such as a CSV-based external table. You can review the data wrangling plan and adjust it with conversational commands.

Data sampling and profiling uses BigQuery resources and are subject to [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

The Data Engineering Agent supports the following data wrangling transformations:

  * Data cleaning. The agent can analyze raw data and suggest cleanup opportunities, such as removing outliers, filling missing or inconsistent values (data imputation), fixing duplicate data, or standardizing data formats—for example, phone numbers or addresses.
  * Structural transformations. When a target schema is provided, the agent can unnest or extract values from `JSON`, `ARRAY`, or `STRUCT` types; merge multiple columns into one; or split one column into multiple columns.
  * Data type detection and conversion. The agent can analyze the data to determine the appropriate field types. The agent can then perform secure type casting to resolve any formatting inconsistencies within the date, time, datetime, or timestamp fields.
  * Unit conversions. The agent can automatically convert various units within a field into one consistent unit to standardize your data.



To ensure accuracy, the agent uses representative samples of your data to detect issues and validate its transformation logic.

### Generate and review agent plans

The Data Engineering Agent can generate agent plans that provide a summary and overview of the objectives and steps that it takes to complete a request. When you prompt the agent with complex requests that require many changes, we recommend asking the agent to provide you an agent plan so you can review the agent's intentions before it takes any actions. A Data Engineering Agent plan generally consists of the following:

  * The agent's objective for a particular request
  * A high-level overview of the steps the agent plans to take
  * Any assumptions the agent makes
  * Files the agent plans to modify
  * Any optimization or cleaning steps it plans to perform
  * A phased execution plan



In your prompt, you can include the need to review and approve the plan so that the agent doesn't take any action without your explicit approval. For example:
    
    
    Create a plan for a pipeline that finds the
    top N pick up and drop off locations in NYC. I want to review the plan and
    approve it before you create the pipeline.

The agent might also generate an agent plan automatically and request your approval. This result can occur when a prompt is too ambiguous, or if the agent needs more clarity to fulfill your request.

For best practices about using agent plans, see Best practices.

### Add context from Knowledge Catalog

The Data Engineering Agent uses Knowledge Catalog by attaching glossary terms to BigQuery tables and columns and generating data profile scans. Glossary terms can tag columns that require additional context, such as columns containing personally identifiable information (PII) that require special-handling instructions, or to identify matching columns with different naming across tables.

Knowledge Catalog also utilizes [data profiling](https://docs.cloud.google.com/dataplex/docs/data-profiling-overview), which provides the agent with a better understanding of data distribution within table columns and helps the agent create more specified data quality assertions.

The agent can also use Knowledge Catalog to discover and query Apache Iceberg tables. For more information, see Create pipelines over Apache Iceberg tables.

### Add data quality checks to an existing table

When you prompt the agent to add quality checks, the agent infers reasonable checks for the table based on the schema and samples. You can also add opinionated assertions as part of the prompt. For example:
    
    
      Add data quality checks for bigquery-public-data.thelook_ecommerce.users.
    

During pipeline execution, the results of any Dataform assertions are automatically published to Knowledge Catalog. These results populate the [Knowledge Catalog data quality scorecard](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#data-quality-scorecard) with a pass or fail status. Each execution overwrites existing data quality scorecards published by prior Dataform runs, but doesn't affect scorecards created by Knowledge Catalog data scans.

### Generate schema mapping

You can prompt the Data Engineering Agent to generate a schema mapping between a source and target schema:
    
    
      Create a Dataform pipeline to map the tables from schema
      SOURCE_SCHEMA to schema TARGET_SCHEMA. Give me the plan.

Replace the following:

  * `SOURCE_SCHEMA`: the name of the schema for your source tables.
  * `TARGET_SCHEMA`: the name of the schema for your target tables.



The agent then generates a plan by doing the following:

  * **Anchor table selection** : Determine the primary source table for each target table.
  * **Join graph optimization** : Map join-paths directly aligned with property graph edge definitions, avoiding cartesian explosions and type mismatches.
  * **Field-level gap analysis** : Classify every mapping into a mapping type, either `Direct`, `Derived`, `Joined`, or `Aggregated`, then verifies `NOT NULL` and `REQUIRED` constraint integrity.



After you have reviewed the plan and confirmed the mapping logic, you can prompt the agent to create the pipeline based on that schema mapping.

#### Schema mapping with BigQuery Graph

If you have a BigQuery Graph in your project, the agent automatically detects and reads it to provide additional context and improve schema mapping accuracy. The agent can read a BigQuery Graph to understand the semantic relationships between your source and target tables, which lets it generate more accurate mappings and reduces manual user intervention when migrating or transforming complex datasets. When you prompt the agent to generate a schema mapping, the agent automatically scans your dataset and uses a BigQuery Graph if a relevant graph exists.

For more information about BigQuery Graph capabilities, editions, and pricing, see [BigQuery Graph overview](https://docs.cloud.google.com/bigquery/docs/graph-overview). For more information about access control and creating a BigQuery Graph, see [Create and query BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-create).

## Automatic data enrichment

Standard metadata from BigQuery—for example, datasets, tables, and views—is automatically available in Knowledge Catalog.

You can also define custom metadata for your tables and views directly in the config block of your `.sqlx` files. Upon successful completion of an action, Dataform automatically initiates a metadata sync to Knowledge Catalog. This enrichment process updates Knowledge Catalog with the semantic metadata defined in your SQLX configuration.

Use the metadata key to specify information for the Knowledge Catalog. The enrichment process supports the following metadata constructs:

  * Overview: documentation and summary text for the entry. Requires Dataform core version 3.0.37 or later.
  * Generic aspects: semantic details such as table system and type information. Requires Dataform core version 3.0.52 or later.



The following example configuration shows you how to add an overview and generic metadata aspects to a table configuration for Knowledge Catalog:
    
    
    config {
      type: "table",
      metadata: {
        overview: "This table provides standardized trip data.",
        extraProperties: {
            generic: {
                  system: "BigQuery",
                  type: "table"
            }
          }
      }
    }
    

To check the status of a metadata update, see [Inspect workspace execution logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#inspect-workspace-execution-logs) for Dataform workflows or [View past manual runs](https://docs.cloud.google.com/bigquery/docs/manage-pipelines#view-manual-runs) for BigQuery pipelines.

To verify the synchronized metadata, you can search for the asset in Knowledge Catalog. For more information, see [Search for resources](https://docs.cloud.google.com/dataplex/docs/search-assets#search-data-assets).

### Optimize data pipelines

You can prompt the agent to optimize your data pipelines. When generating DDL for new tables, the Data Engineering Agent recommends partitioning and clustering based on the analyzed data usage patterns. Additionally, the agent can automatically apply other pipeline optimizations. Examples of possible optimizations include the following:

  * Column pruning to reduce data read from storage to act as a primary cost and performance driver.
  * Predicate pushdowns to filter data early in the execution plan to significantly reduce the volume processed by subsequent operations.
  * Elimination of common subexpressions to improve efficiency by identifying and computing shared transformation logic only once, preventing inefficient practices like scanning and joining large tables multiple times.
  * Incremental models to process only new or changed data since the last run instead of rebuilding entire tables with each run.



### Create pipelines over Apache Iceberg tables

The Data Engineering Agent supports generating and compiling Dataform pipelines over Apache Iceberg tables managed by the Lakehouse runtime catalog (formerly BigLake metastore). This feature lets you query and join regional open-source format tables (stored in Cloud Storage) directly alongside your BigQuery tables. For more information, see [Apache Iceberg REST catalog endpoint concepts](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types).

For example, you can prompt the agent to query an Apache Iceberg table in the Lakehouse runtime catalog:
    
    
    Include the stackoverflow_post_history_iceberg table in this pipeline.
    

In your prompts, you don't need to specify fully qualified four-part paths—for example, `project.catalog.dataset.table`. You can refer to Apache Iceberg tables by using standard natural language names or logical identifiers—for example, `the StackOverflow post history table` or `post_history`. The agent automatically invokes semantic catalog searches using Knowledge Catalog to resolve and bind the correct Apache Iceberg tables to your pipeline workspace.

To use this feature, your Dataform repository must use Dataform Core version 3.0.33 or later.

### Interactive recommendations

The Data Engineering Agent analyzes your workspace compilation status, execution history, and active conversation state to provide actionable recommendations directly in the chat interface. These suggestions automatically appear when you open a workspace and throughout the session to provide recommendations for setup, troubleshooting, and optimizations to guide your workflow.

To use a recommendation, click one of the suggestions under **AI recommendations** , which loads the prompt into your chat input bar, which you can edit or customize before sending it to the agent. You can also hover over a suggestion to view the exact prompt.

## Best practices

To improve results when working with the Data Engineering Agent and Dataform, we recommend that you do the following:

**Use agent instructions for common requests.** If you commonly apply certain techniques, or if you frequently make the same corrections to the agent, use agent instructions as a centralized location to store common instructions and requests.

**Utilize agent plans.** Agent plans can be helpful to break down complex pipeline tasks. Agent plans can also show you agent assumptions and intentions, so we recommend reviewing those plans to make sure the agent is provided the correct context.

After reviewing a plan, you can edit the plan by prompting the Data Engineering Agent with feedback and changes. For example:
    
    
    In the plan, ensure that all of the intermediate tables are views.
    

In some cases, it can be helpful to ask the agent to generate a plan that doesn't need your explicit approval. The act of making the agent plan forces the Data Engineering Agent to break down its actions, which often leads to better outcomes. You can force the agent to generate a plan and execute it automatically. For example:
    
    
    Create a plan for a pipeline that finds the
    top N pick up and drop off locations in NYC. You have my explicit pre-approval
    to go ahead and execute this plan.
    

**Write clearly.** State your request clearly and avoid being vague. Where possible, provide source and destination data sources when prompting, as shown in the following example:
    
    
      Extract data from the sales.customers table in the us_west_1 region, and load
      it into the reporting.dim_customers table in BigQuery. Match the schema of the
      destination table.
    

**Provide direct and scoped requests.** Ask one question at a time, and keep prompts concise. For prompts with more than one question, itemize each distinct part of the question to improve clarity, as shown in the following example:
    
    
      1. Create a new table named staging.events_cleaned. Use raw.events as the
         source. This new table should filter out any records where the user_agent
         matches the pattern '%bot%'. All original columns should be included.
    
      2. Next, create a table named analytics.user_sessions. Use
         staging.events_cleaned as the source. This table should calculate the
         duration for each session by grouping by session_id and finding the
         difference between the MAX(event_timestamp) and MIN(event_timestamp).
    

**Provide explicit instructions and emphasize key terms.** You can add emphasis to key terms or concepts in your prompts and label certain requirements as important, as shown in the following example:
    
    
      When creating the staging.customers table, it is *VERY IMPORTANT* that you
      transform the email column from the source table bronze.raw_customers.
      Coalesce any NULL values in the email column to an empty string ''.
    

**Specify the order of operations.** For ordered tasks, structure your prompt in lists, where listed items are divided into small, focused steps, as shown in the following example:
    
    
      Create a pipeline with the following steps:
      1. Extract data from the ecomm.orders table.
      2. Join the extracted data with the marts.customers table on customer_id.
      3. Load the final result into the reporting.customer_orders table.
    

**Refine and iterate.** Keep trying different phrases and approaches to see what yields the best results. If the agent generates invalid SQL or other mistakes, guide the agent with examples or public documentation.
    
    
      The previous query was incorrect because it removed the timestamp. Please
      correct the SQL. Use the TIMESTAMP_TRUNC function to truncate the
      event_timestamp to the nearest hour, instead of casting it as a DATE. For
      example: TIMESTAMP_TRUNC(event_timestamp, HOUR).
    

## Evaluate data pipelines

To evaluate the effectiveness of a data pipeline generated by the Data Engineering Agent, use the [EvalBench tool](https://github.com/GoogleCloudPlatform/evalbench). EvalBench is an open-source framework that supports multi-turn agentic evaluations. EvalBench acts as an automated unit-testing suite, letting you set up multi-turn scenarios, add LLM-backed and deterministic scorers, and manage the lifecycle of your Dataform pipelines.

By simulating natural language prompts in an isolated sandbox, EvalBench measures how effectively the agent understands instructions, calls the right tools, and generates correct pipeline code. EvalBench can check your data pipelines by doing the following:

  * **Validating custom rules** : Verify that the agent strictly follows your organization's specific coding guidelines, naming conventions, and best practices.
  * **Preventing code regressions** : Test pipeline changes before deployment to ensure that agent updates or schema modifications don't break existing functionality.
  * **Generating quality benchmarks** : Get objective, automated scores for SQL correctness, tool execution accuracy, and pipeline reliability.



### Run a data pipeline evaluation

You can run EvalBench in the following two modes:

  * **Dynamic sandbox** : EvalBench provisions a fresh, temporary Dataform repository and workspace at the start of an evaluation run, executes the test scenarios, and automatically tears down all created resources upon completion. This mode doesn't modify any production code, production repositories, or BigQuery datasets, and doesn't leave any leftover artifacts in your Google Cloud project. The dynamic sandbox mode is suitable for automated CI/CD pipelines, nightly regression testing, and objective benchmark scoring where strict environment isolation is required.

  * **Static workspace** : EvalBench connects to a pre-existing, user-managed Dataform repository and workspace, and skips automated creation and deletion scripts. This mode lets the agent under evaluation modify and create new SQLX files within the existing workspace as it processes evaluation cases. The static workspace mode is suitable for active prompt engineering, rubric iteration, and local debugging where you need to inspect generated SQLX files directly in your Dataform workspace after execution.




#### Before you begin

To get the permissions that you need to run EvalBench, ask your administrator to grant you the following IAM roles on the service account or user identity running EvalBench: 

  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`)
  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
  * Export evaluation results as ZIP packages: [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.objectAdmin) (`roles/bigquery.objectAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Run evaluation in a dynamic sandbox

To evaluate your data pipeline in dynamic sandbox mode, do the following:

  1. Follow the steps to clone the repository, set up the virtual environment, and install any EvalBench dependencies. For more information, see [Getting Started](https://github.com/GoogleCloudPlatform/evalbench#getting-started-).
  2. In the `datasets/dea-tools/` directory, verify that the example run configuration (`example_run_config.yaml`) file includes the following lines:
         
         set_up_script: datasets/dea-tools/scripts/setup_dataform.sh
         tear_down_script: datasets/dea-tools/scripts/teardown_dataform.sh

  3. Run EvalBench with the following command:
         
         EVAL_GCP_PROJECT_ID=PROJECT_ID \
         EVAL_GCP_PROJECT_REGION=REGION \
         .venv/bin/python3 evalbench/evalbench.py --experiment_config=datasets/dea-tools/example_run_config.yaml

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project.
     * `REGION`: the region of the Google Cloud project.



#### Run evaluation in a static evaluation workspace

To evaluate your data pipeline in static workspace mode, do the following:

  1. Follow the steps to clone the repository, set up the virtual environment, and install any dependencies. For more information, see [Getting Started](https://github.com/GoogleCloudPlatform/evalbench#getting-started-).
  2. In the `datasets/dea-tools/` directory, edit the example run configuration (`example_run_config.yaml`) file to comment out the `set_up_script` and `tear_down_script` lines and add the `dataform_repository` and `dataform_workspace` configurations:
         
         ...
         # set_up_script: datasets/dea-tools/scripts/setup_dataform.sh
         # tear_down_script: datasets/dea-tools/scripts/teardown_dataform.sh
         dataform_repository: !ENV ${EVAL_DEA_REPOSITORY_ID}
         dataform_workspace: !ENV ${EVAL_DEA_WORKSPACE_ID}
         ...

  3. Run EvalBench with the following command:
         
         EVAL_GCP_PROJECT_ID=PROJECT_ID \
         EVAL_GCP_PROJECT_REGION=REGION \
           EVAL_DEA_REPOSITORY_ID=REPOSITORY_ID \
           EVAL_DEA_WORKSPACE_ID=WORKSPACE_ID \
           .venv/bin/python3 evalbench/evalbench.py --experiment_config=datasets/dea-tools/example_run_config.yaml

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project.
     * `REGION`: the region of the Google Cloud project.
     * `REPOSITORY_ID`: the ID of the repository that contains the data pipeline.
     * `WORKSPACE_ID`: the ID of the workspace that contains the data pipeline.
  4. Optional: You can also run EvalBench with `core_10_cases_suite.yaml` to test the data pipeline against 10 core evaluation cases sequentially with environment isolation by creating a new repository for each test case. To do so, run the following command:
         
         EVAL_GCP_PROJECT_ID=PROJECT_ID \
         EVAL_GCP_PROJECT_REGION=REGION \
         .venv/bin/python3 evalbench/evalbench.py --suite_config=datasets/dea-tools/core_10_cases_suite.yaml




### Data pipeline evaluation best practices

To improve the performance and accuracy of your data pipeline evaluations using EvalBench, we recommend that you do the following:

  * Look for Dataform workflow invocation and BigQuery job IDs in the evaluation logs. Use these IDs to cross-reference and inspect generated execution artifacts, compilation results, and query logs in the Google Cloud console.
  * Always run the core evaluation suite (`--suite_config`) before releasing model or prompt changes to ensure full regression coverage across diverse data engineering scenarios.
  * Use `EVAL_DATAFORM_SETUP_ENV_FILES_DIR` to preload environment setup files, such as `workflow_settings.yaml` and base schema definitions, into the test workspace. These setup files ensure that the agent builds upon realistic existing environments instead of empty workspaces.
  * When troubleshooting failed evaluation cases in dynamic sandbox mode, comment out `tear_down_script` in your run config to keep the target workspace for post-mortem analysis.
  * Always pair cloud compilation and execution verifiers (`dataform_cloud_compile`, `dataform_cloud_run`) with LLM-based binary rubrics to identify both syntactical or runtime errors and high-level logic flaws.
  * Enable BigQuery reporting (`<PROJECT_ID>.evalbench.results`) and use the generated Data Studio links to track pass rates, tool usage accuracy, and prompt efficiency over time.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
