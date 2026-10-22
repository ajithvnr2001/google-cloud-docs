---
url: https://docs.cloud.google.com/knowledge-catalog/docs/build-policy-as-code-data-quality-workflow/
title: Build a policy-as-code data quality workflow \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:53.571102+00:00
---

# Build a policy-as-code data quality workflow  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/build-policy-as-code-data-quality-workflow/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Build a policy-as-code data quality workflow Stay organized with collections  Save and categorize content based on your preferences. 

Build a policy-as-code data quality and metadata enrichment workflow. This tutorial covers how to move beyond manual processes by defining data quality expectations in declarative, version-controlled files. 

By establishing automated profiling and data quality rules, you enrich your metadata with trust signals and business context.

Using a **Human-in-the-Loop** approach, where AI drafts the initial rules and you review, refine, and validate them, you can quickly translate profile statistics into a data quality framework.

### Objectives

  * Flatten nested BigQuery data with materialized views to enable Knowledge Catalog profiling.
  * Run Knowledge Catalog profile scans using the Python client library.
  * Use the Antigravity CLI to generate data quality rules based on profile statistics.
  * Validate and deploy AI-generated rules as Knowledge Catalog quality scans using a Human-in-the-Loop review process.



## Before you begin

Before you begin, make sure you have a Google Cloud project with billing enabled.

## Prepare your environment

The following steps use [Cloud Shell](https://cloud.google.com/cloud-shell/), a command-line environment running in the cloud.

  1. In the Google Cloud console, click **Activate Cloud Shell** in the top right toolbar. The environment takes a few moments to provision and connect.

  2. In Cloud Shell, set up your project ID and environment variables:
         
         export PROJECT_ID=$(gcloud config get-value project)
         gcloud config set project $PROJECT_ID
         export LOCATION="us-central1"
         export BQ_LOCATION="us"
         export DATASET_ID="kc_dq_codelab"
         export TABLE_ID="ga4_transactions"
         

Use `us` (multi-region) as the location since the public sample data is also located in the `us` (multi-region). For BigQuery queries, the source data and destination table must be in the same location.

**Note:** Cloud Shell sessions occasionally time out. Before you run shell scripts, you can check your environment variables by running `echo $PROJECT_ID`. If the command returns an empty line, re-run the export commands from this environment setup step. 
  3. Enable the required services:
         
         gcloud services enable dataplex.googleapis.com \
                                bigquery.googleapis.com \
                                serviceusage.googleapis.com \
                                aiplatform.googleapis.com
         

  4. Create a BigQuery dataset to store sample data and results:
         
         bq --location=us mk --dataset $PROJECT_ID:$DATASET_ID
         

  5. Prepare the sample data, which comes from a public ecommerce dataset from the Google Merchandise Store. 

The following `bq` command creates a new table, `ga4_transactions`, in your `kc_dq_codelab` dataset. To ensure scans run quickly, it only copies data from one day (2021-01-31).
         
         bq query \
         --use_legacy_sql=false \
         --destination_table=$PROJECT_ID:$DATASET_ID.$TABLE_ID \
         --replace=true \
         'SELECT * FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_20210131`'
         

  6. Clone the GitHub repository that contains the folder structure and supporting files for this tutorial:
         
         # Perform a shallow clone to get only the latest repository structure without the full history
         git clone --depth 1 --filter=blob:none --sparse https://github.com/GoogleCloudPlatform/devrel-demos.git
         cd devrel-demos
         
         # Specify and download only the folder we need for this lab
         git sparse-checkout set data-analytics/programmatic-dq
         cd data-analytics/programmatic-dq
         

This directory is your active working area.




## Profile nested data

With [data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview), Knowledge Catalog finds statistics for top-level columns, like null percentages, uniqueness, and value distributions in your data to help you understand it.

To get statistics for nested fields, you can flatten the data using a set of materialized views. This turns each nested field into a top-level column that Knowledge Catalog can profile.

### Get the nested schema

Get the full schema of your source table, including all nested structures, and save the output as a JSON file:
    
    
    bq show --schema --format=json $PROJECT_ID:$DATASET_ID.$TABLE_ID > bq_schema.json
    

View the schema:
    
    
    jq < bq_schema.json
    

The `bq_schema.json` file reveals complex structures.

**Tip:** To see this nested schema visually, go to BigQuery in the Google Cloud console. Find your `kc_dq_codelab` dataset, select the `ga4_transactions` table, and browse the **Schema** tab.

### Flatten data with a materialized view

When you flatten nested data, it's important not to unnest multiple independent arrays in the same view. Doing so performs an implicit cross join (Cartesian product) between the arrays, which multiplies rows incorrectly and corrupts your data.

It's best to create multiple views instead, each built for a specific purpose. Each view should keep a single, clear level of detail. In this step, you create the following materialized views:

  * **Session flat view** (`mv_ga4_user_session_flat.sql`): one row per event.
  * **Transactions view** (`mv_ga4_ecommerce_transactions.sql`): one row per transaction.
  * **Items view** (`mv_ga4_ecommerce_items.sql`): one row per item.



The project repository provides three SQL files in the `devrel-demos/data-analytics/programmatic-dq` directory that define these views. 

**Tip:** To inspect the files that define the materialized views, click **Open Editor** in the Cloud Shell toolbar.

Run these files from the Cloud Shell using the following BigQuery commands.
    
    
    envsubst < mv_ga4_user_session_flat.sql | bq query --use_legacy_sql=false
    envsubst < mv_ga4_ecommerce_transactions.sql | bq query --use_legacy_sql=false
    envsubst < mv_ga4_ecommerce_items.sql | bq query --use_legacy_sql=false
    

### Run profile scans with the Python client

You can now create and run Knowledge Catalog data profile scans for each materialized view. The following Python script uses the `google-cloud-dataplex` client library to automate this process.

Before you run the script, create an isolated Python virtual environment in your project directory.
    
    
    # Create the virtual environment
    python3 -m venv dq_venv
    
    # Activate the environment
    source dq_venv/bin/activate
    

Install the Knowledge Catalog client library inside the virtual environment.
    
    
    # Install the Knowledge Catalog client library
    pip install google-cloud-dataplex
    

Now that you've set up the environment and installed the library, you're ready to use the `1_run_scan.py` script. This script profiles your three materialized views by creating and running a scan for each one. When it finishes, it outputs a rich statistical summary that you use in the next step to generate AI-powered data quality rules.

**Tip:** To inspect the script file, click **Open Editor** in the Cloud Shell toolbar and open the `devrel-demos/data-analytics/programmatic-dq/` directory.

Run the script from your Cloud Shell terminal.
    
    
    python3 1_run_scan.py
    

### Check your profile scans

You can check out the new profile scans in the Google Cloud console.

  1. In the navigation menu, go to **Knowledge Catalog** and **Data profiling & quality** in the **Govern** section. 
  2. Find your three profile scans listed, along with their latest job status. Click a scan to explore its detailed results.



### Export profile results to JSON

In order for the Antigravity CLI to read your profile scans, you need to extract their contents into a local file.

Use the `2_dq_profile_save.py` script to find the latest successful scan for the `mv_ga4_user_session_flat` view, download the profile data, and save it to a file named `dq_profile_results.json`.
    
    
    python3 2_dq_profile_save.py
    

When the script finishes, it creates a `dq_profile_results.json` file in the directory. This file holds the detailed statistical metadata you need to generate data quality rules. Take a look at its contents by running the following command:
    
    
    cat dq_profile_results.json
    

**Note:** For simplicity, this tutorial focuses only on the `mv_ga4_user_session_flat` view. In a real production setup, repeat this process for your other views to build comprehensive data quality specifications and enrich metadata across your data catalog.

## Generate data quality rules with the Antigravity CLI

Now you can use the Antigravity CLI to read the local profile scan results. 

Manually writing data quality specifications for complex datasets is time-consuming and error-prone. Using a generative AI agent accelerates this workflow by drafting an initial declarative configuration in seconds. This allows data teams to shift from manual syntax drafting to high-level, business-aligned Human-in-the-Loop (HITL) oversight.

To start the Antigravity CLI, use the following command:
    
    
    agy
    

Now you're ready to generate quality rules. Because the CLI can read files in your current directory, it can use your new profile scan data directly.

### Prompt the agent to create a plan

First, ask the agent to analyze the statistical profile and propose a plan of action. Instruct it not to write the YAML file yet so it focuses on analysis and justification.

**Tip:** The prompt specifies the `./dq_profile_results.json` path, which tells the CLI exactly where to find the file in your current working directory.

In your interactive Antigravity CLI session, enter the following structured prompt:
    
    
    # Context
    You are preparing a data quality rule configuration plan for Google Cloud Knowledge Catalog based on data profile statistics.
    
    # Input
    - File Path: `./dq_profile_results.json` (contains metrics like null percentage, distinct counts, and distributions)
    
    # Task
    Analyze the input statistics and propose a step-by-step plan for establishing automated data quality rules. 
    *Do not write any YAML code in this step.* Focus only on analytical planning.
    
    # Rule Mapping Strategy
    For candidate columns, match the statistical metrics to the most appropriate expectations:
    - `nonNullExpectation`: Propose for columns with 0% null values in the profile.
    - `setExpectation`: Propose for columns with a highly limited, stable set of categorical values.
    - `rangeExpectation`: Propose for numeric columns with consistent and predictable value boundaries.
    
    # Guidelines
    - Provide a metric-based justification for each proposed rule (for example, "Recommend nonNullExpectation for column 'user_pseudo_id' because its null percentage is 0%").
    - Flag volatile metrics such as hardcoded row counts that could cause false-positive alerts in production.
    
    # Output Format
    Provide your analysis and proposed rules as a structured, step-by-step markdown plan with clear headings.
    

The agent will analyze the JSON file and return a structured plan like the following:
    
    
    Automated Data Quality Rule Configuration Plan                                                                                                          
                                                                                                                                                               
      Google Cloud Knowledge Catalog (Dataplex Data Quality)                                                                                                   
      ──────                                                                                                                                                   
      ## Executive Summary                                                                                                                                     
      This analytical planning document outlines a step-by-step strategy for configuring automated data quality (DQ) rules in Google Cloud Knowledge Catalog (formerly Dataplex Data Quality) based on profiling statistics.
      The dataset contains 26,489 rows representing GA4 event logs. Based on statistical metrics (null ratios, distinct value distributions, and data types), candidate columns are mapped to appropriate expectation rules.
      ──────                                                                                                                                                   
      ## 1. Data Profile Overview & Statistical Highlights                                                                                                     
                                                                                                                                                               
       Column Name     │ Data Type │ Null Ratio     │ Distinct Count │ Key Value Range / Categories
      ─────────────────┼───────────┼────────────────┼────────────────┼──────────────────────────────────────────────────
       event_date      │ STRING    │ 0.0% (0)       │ 1 (3.78e-05)   │ "20210131" (100%)
       event_timestamp │ INTEGER   │ 0.0% (0)       │ ~16,539 (0.62) │ Min: 1612051200657906, Max: 1612137595412363
       event_name      │ STRING    │ 0.0% (0)       │ 16 (0.0006)    │ page_view (35.8%), user_engagement (18.9%), etc.
       user_pseudo_id  │ STRING    │ 0.0% (0)       │ ~2,545 (0.09)  │ 18–21 characters string identifiers
       user_id         │ STRING    │ 100.0% (1.0)   │ 0 (0.0)        │ Entirely NULL
       device_category │ STRING    │ 0.0% (0)       │ 3 (0.0001)     │ desktop (57.5%), mobile (40.1%), tablet (2.4%)
       ...             │ ...       │ ...            │ ...            │ ...
      ──────                                                                                                                                                   
      ## 2. Rule Mapping Strategy & Analytical Justifications                                                                                                  
                                                                                                                                                               
      ### Step 1: Nullability Rules (nonNullExpectation)                                                                                                       
      Propose nonNullExpectation for mandatory columns where the data profile demonstrates 0% null values.                                                     
      • user_pseudo_id, event_timestamp, event_name, event_date, stream_id, platform, device_category (Metric Justification: nullRatio is 0.0%)
                                                                                                                                                               
      │ [!NOTE] Exclusions:                                                                                                                    
      │ • user_id: Has a nullRatio of 100.0% (unauthenticated traffic).
      │ • device_language: Has a nullRatio of 37.53%.                                                                                                          
      ──────                                                                                                                                                   
      ### Step 2: Categorical Value Set Validation (setExpectation)                                                                                            
      Propose setExpectation for columns with a highly limited, stable set of categorical domain values.                                                       
      • device_category: Distinct count is exactly 3. Allowed set: ['desktop', 'mobile', 'tablet']
      • platform: Distinct count is 1. Allowed set expanded to: ['WEB', 'ANDROID', 'IOS'] to avoid over-fitting.
      • geo_continent: Distinct count is 6. Allowed set: ['Americas', 'Asia', 'Europe', 'Africa', 'Oceania', 'Antarctica', '(not set)']
                                                                                                                                                               
      ──────                                                                                                                                                   
      ### Step 3: Numeric & Timestamp Boundary Validation (rangeExpectation)                                                                                   
      Propose rangeExpectation for numeric columns with consistent and predictable value boundaries.                                                           
      • event_timestamp: rangeExpectation requiring event_timestamp > 0 (avoid dynamic microsecond range hardcoding)
      • stream_id: rangeExpectation requiring positive integer stream IDs (stream_id > 0)
                                                                                                                                                               
      ──────                                                                                                                                                   
      ## 3. Risk Warning: Volatile Metrics & Production False Positives                                                                                        
      │ [!WARNING] Volatile Metrics Flagged for Risk Mitigation:                                                                                                      
      1. Hardcoded Total Row Count (rowCount = 26,489) -> Daily event volume fluctuates. Use dynamic volume thresholds.
      2. Hardcoded Partition Date (event_date = '20210131') -> Breaks on future runs. Validate against YYYYMMDD regex patterns.
      3. Exact Timestamp Range Bounds -> Enforcing these microsecond limits on incoming live pipelines will reject all future data.
      4. Single-Value Domain Restrictions -> Single profile sample might lack active streams. Set sets according to enterprise schema.
      
      ──────
      ## Summary Table of Proposed Rules
      
       Target Column   │ Rule Type          │ Metric-Based Justification │ Operational Considerations
      ─────────────────┼────────────────────┼────────────────────────────┼──────────────────────────────────────────────────
       user_pseudo_id  │ nonNullExpectation │ Null Ratio: 0.0%           │ Core identifier, strictly required
       event_timestamp │ nonNullExpectation │ Null Ratio: 0.0%           │ Temporal key, strictly required
       event_timestamp │ rangeExpectation   │ Min: > 0 (Microseconds)    │ Avoid hardcoding epoch min/max
       event_name      │ nonNullExpectation │ Null Ratio: 0.0%           │ Required event taxonomy key
       event_name      │ setExpectation     │ Categorical distribution   │ Map to standard GA4 event taxonomy
       device_category │ nonNullExpectation │ Null Ratio: 0.0%           │ Required form-factor dimension
       device_category │ setExpectation     │ Distinct Count: 3 values   │ ['desktop', 'mobile', 'tablet']
       ...             │ ...                │ ...                        │ ...
    

### Generate data quality rules

This is the most critical step in the entire workflow: the Human-in-the-Loop (HITL) review. The plan that the agent generated is based purely on statistical patterns in the data. The agent doesn't understand your business context, future data changes, or the specific intent behind your data. Your role as the human expert is to validate, correct, and approve this plan before turning it into code.

#### What to validate during HITL review

Check the agent's proposed plan against these core business criteria:

  * **Statistical anomalies vs. business reality** : 
    * _Why_ : An AI agent might assume a column with 0% nulls in a one-day sample should never contain nulls, or set a strict numerical range based on limited historical distributions.
    * _Action_ : Verify whether suggested boundaries (such as `rangeExpectation` or `nonNullExpectation`) reflect true business constraints or merely sample-set artifacts.
  * **Volatile metrics (such as row counts)** : 
    * _Why_ : Metrics like `rowCount` or table growth vary daily in active enterprise environments. A static rule will cause false-positive alerts.
    * _Action_ : Reject or modify rules that enforce static thresholds on dynamic transactional tables.
  * **Categorical completeness (`setExpectation`)**: 
    * _Why_ : Profile data only reveals values present in the scanned sample window. It cannot predict valid categories that did not occur during that timeframe.
    * _Action_ : Check categorical lists against your official business glossary or reference data, adding any valid values that were omitted from the sample (for example, adding missing region codes or product categories).



#### Refine the plan with prompt feedback

Provide feedback to the agent and give it the final command to generate the code. Adapt the following prompt based on the plan you actually received and the corrections you want to make.

The prompt is just a template. The first line is where you add your specific corrections.

This prompt requires conformance to the `DataQualityRule` specification because Knowledge Catalog requires a precise YAML structure, preventing syntax errors or outdated schema versions.
    
    
    # Feedback & Approvals
    [YOUR CORRECTIONS AND APPROVAL GO HERE. Examples:
    - "The plan looks good. Please proceed."
    - "The rowCount rule is not necessary, as the table size changes daily. The rest of the plan is approved. Please proceed."
    - "For the setExpectation on the geo_continent column, please also include 'Antarctica'."]
    
    # Objective
    Based on the approved analysis plan and the provided feedback, generate the final `dq_rules.yaml` file conforming to the standard `DataQualityRule` schema.
    
    # Instructions
    1. **Rule Justifications**: For every generated rule, add a YAML comment (`#`) on the line directly above it, briefly explaining the justification established in the plan.
    2. **Schema Alignment**: Ensure the structure strictly adheres to the required Knowledge Catalog data quality scan specification. Refer to the `sample_rule.yaml` file in the current directory and the `DataQualityRule` class definition as the schema authority. Search for the `data_quality.py` file inside the `./dq_venv/lib/` directory to read this class definition.
    3. **Data-Driven Values**: Derive all rule parameters, such as thresholds or expected values, directly from the statistical metrics in `dq_profile_results.json`.
    
    # Constraints
    - **Output Purity**: Return ONLY the raw, valid, and properly formatted YAML code block.
    - Do not include conversational preambles, introductory sentences, explanations, or markdown blocks around the YAML.
    

The agent now generates a YAML file called `dq_rules.yaml` in your working directory, based on your validated instructions.

**Caution:** It might take the agent several minutes to create the rules.

## Create and run a data quality scan

You now have an agent-generated, human-validated set of data quality rules that you can register and deploy as a scan. 

  1. Exit the Antigravity CLI by entering `/quit` or pressing `Ctrl+C` twice.

  2. Then, create a data scan in Knowledge Catalog:
         
         export DQ_SCAN="dq-scan"
         gcloud dataplex datascans create data-quality $DQ_SCAN \
             --project=$PROJECT_ID \
             --location=$LOCATION \
             --data-quality-spec-file=dq_rules.yaml \
             --data-source-resource="//bigquery.googleapis.com/projects/$PROJECT_ID/datasets/$DATASET_ID/tables/mv_ga4_user_session_flat"
         

  3. Run the scan:
         
         gcloud dataplex datascans run $DQ_SCAN --location=$LOCATION --project=$PROJECT_ID
         

This command creates a data quality scan named `dq-scan`. 

  4. Check your scan's progress in the Knowledge Catalog section of the Google Cloud console.

     1. In the navigation menu, go to **Knowledge Catalog** and **Data profiling & quality** in the **Govern** section. 
     2. Find the `dq-scan`. When the scan completes, click the scan to see the results.
**Note:** Because large language models (LLMs) are non-deterministic, the initial rules that the agent creates might require adjustment. Iterate with the agent to refine the rules and eliminate false alerts. Seeing failed results at this stage is normal, and demonstrates why Human-in-the-Loop (HITL) review is an integral part of continuous metadata enrichment and quality validation.



## Clean up

To avoid recurring billing charges for the resources you created in this tutorial, delete them.

### Delete the Knowledge Catalog scans

Delete your profile and quality scans using the specific scan names from this codelab:
    
    
    # Delete the Data Quality Scan
    gcloud dataplex datascans delete dq-scan \
        --location=us-central1 \
        --project=$PROJECT_ID --quiet
    
    # Delete the Data Profile Scans
    gcloud dataplex datascans delete profile-scan-mv-ga4-user-session-flat \
        --location=us-central1 \
        --project=$PROJECT_ID --quiet
    
    gcloud dataplex datascans delete profile-scan-mv-ga4-ecommerce-transactions \
        --location=us-central1 \
        --project=$PROJECT_ID --quiet
    
    gcloud dataplex datascans delete profile-scan-mv-ga4-ecommerce-items \
        --location=us-central1 \
        --project=$PROJECT_ID --quiet
    

### Delete the sample dataset

Delete your temporary BigQuery dataset and its tables.

**Caution:** Since this action is permanent, manually type the following command (ensuring the dataset name is correct) to prevent accidental data loss:
    
    
    bq rm -r -f --dataset $PROJECT_ID:kc_dq_codelab
    

### Delete local files

Deactivate the Python virtual environment and remove the cloned repository and its contents:
    
    
    deactivate
    cd ../../..
    rm -rf devrel-demos
    

## Conclusion

Congratulations, you built an end-to-end, programmatic data quality and metadata enrichment workflow.

By pairing an Antigravity CLI agent with Knowledge Catalog, you establish a verifiable foundation for AI-assisted metadata enrichment. This approach accelerates declarative rule creation so Data Stewards can focus on Human-in-the-Loop (HITL) validation and refining rules against business logic—ensuring your data catalog acts as a trusted context engine for enterprise AI consumption.

## What's next

  * Read more about the philosophy behind this architecture in [AI-Assisted Governance: Accelerating Data Quality with Human Oversight](https://medium.com/google-cloud/ai-assisted-governance-accelerating-data-quality-with-human-oversight-dcc8281b8bd0).
  * Manage data quality as code by creating a [CI/CD pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-quality-rules-as-code).
  * Explore using [custom SQL rules](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#supported-custom-sql-rule-types) to enforce business-specific logic.
  * Optimize your scans with filters and sampling to [reduce costs](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).
  * Automate your infrastructure by [provisioning Knowledge Catalog resources with Terraform](https://docs.cloud.google.com/knowledge-catalog/docs/terraform) to manage your data quality specifications and metadata enrichment at scale.
  * Learn more using the [Antigravity CLI quickstart](https://antigravity.google/product/antigravity-cli).
  * Try other Knowledge Catalog [use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
