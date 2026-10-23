---
url: https://docs.cloud.google.com/knowledge-catalog/docs/use-antigravity-cli-agent-to-test-data-context/
title: Use the Antigravity CLI to test data context \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:52.718945+00:00
---

# Use the Antigravity CLI to test data context  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/use-antigravity-cli-agent-to-test-data-context/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use the Antigravity CLI to test data context Stay organized with collections  Save and categorize content based on your preferences. 

AI agents can reason, but they start with zero knowledge about your specific company. Imagine asking an agent, "What is our Q1 revenue?" Without guidance, the agent might pick from dozens of tables named "revenue" in your databases, ranging from official reports to messy test data. If the agent picks the table with the closest-sounding name, it could return convincingly wrong answers based on unverified sources.

Metadata enrichment is the solution to this context problem. In this tutorial, you set up [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspects) that provide this context, and use the [Antigravity CLI](https://antigravity.google/docs/cli/overview) to test data context and verify that an agent can accurately ground its answers in trusted, certified data.

## Objectives

  * Deploy a realistic, multi-tiered data lake in BigQuery for testing.
  * Design and register custom metadata templates ([aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspect-types)) in Knowledge Catalog to distinguish official data products from raw sandbox tables.
  * Verify data governance rules and AI agent grounding using the [Antigravity CLI](https://antigravity.google/docs/cli/overview) (`agy`).



## Before you begin

Before you begin, make sure you do the following:

  * Pick a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for this tutorial.
  * Confirm that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project) for your project.



To complete this tutorial, you should also have a basic understanding of [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) and [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).

## Prepare your environment

This tutorial uses [Google Cloud Shell](https://docs.cloud.google.com/shell/docs), a command-line environment that runs in the cloud. The [Antigravity CLI (`agy`)](https://antigravity.google/docs/cli/overview) is pre-installed in Google Cloud Shell.

  1. From the Google Cloud console, click **Activate Cloud Shell** in the top right toolbar. It takes a few moments to provision and connect to the environment.

  2. In Cloud Shell, set your `PROJECT_ID` and `REGION` variables so that all future commands target your specific Google Cloud project.
         
         export PROJECT_ID=$(gcloud config get-value project)
         gcloud config set project $PROJECT_ID
         export REGION="us-central1"
         

  3. Enable the necessary Google Cloud services.
         
         gcloud services enable \
           artifactregistry.googleapis.com \
           bigquery.googleapis.com \
           dataplex.googleapis.com \
           aiplatform.googleapis.com \
           run.googleapis.com \
           cloudbuild.googleapis.com \
           iam.googleapis.com
         

  4. Clone the [Google Cloud DevRel Demos repository](https://github.com/GoogleCloudPlatform/devrel-demos).

Download the infrastructure code and scripts from GitHub. Use a sparse checkout to pull only the specific folder you need for this tutorial.
         
         # Perform a shallow clone to get only the latest repository structure without the full history
         git clone --depth 1 --filter=blob:none --sparse https://github.com/GoogleCloudPlatform/devrel-demos.git
         cd devrel-demos
         
         # Specify and download only the folder you need for this tutorial
         git sparse-checkout set data-analytics/governance-context
         cd data-analytics/governance-context
         




## Deploy a sample data lake in BigQuery

Real-world data environments are rarely clean. To simulate reality, you need a mix of "official" data marts and untrusted "sandbox" tables.

You use a setup script to deploy the BigQuery datasets and tables.

Make the setup script executable and run it. This creates three BigQuery datasets (`finance_mart`, `marketing_prod`, `analyst_sandbox`) and populates their tables with sample data:
    
    
    chmod +x ./setup_bq_tables.sh
    ./setup_bq_tables.sh
    

You now have a fully populated, but un-governed, data lake. To an AI agent, every table looks exactly the same.

## Define a custom aspect type in Knowledge Catalog

Now, you define the rules of your data governance. To do this in Knowledge Catalog, you create an [aspect type](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspect-types), which is a reusable, strongly-typed metadata template.

In this section, you register this template using the `gcloud` CLI so you can see how it is defined.

### Inspect the aspect template schema

Output the contents of `aspect_template.json` to see the schema definition:
    
    
    cat aspect_template.json
    

It shows the following JSON structure:
    
    
    {
      "name": "OfficialDataProductSpec",
      "type": "record",
      "recordFields": [
        {
          "name": "product_tier",
          "type": "enum",
          "enumValues": [
            { "name": "GOLD_CRITICAL", "index": 1 },
            { "name": "SILVER_STANDARD", "index": 2 },
            { "name": "BRONZE_ADHOC", "index": 3 }
          ],
          ...
        },
        {
          "name": "is_certified",
          "type": "bool",
          "...": "..."
        }
      ]
    }
    

Notice how this schema enforces strict data types, such as `enum` for the criticality tier (`GOLD_CRITICAL`, `SILVER_STANDARD`, `BRONZE_ADHOC`) and a `bool` for `is_certified`. This ensures the metadata remains structured and machine-readable.

### Register the aspect type in Knowledge Catalog

Run the following `gcloud` command to register this template in your Knowledge Catalog registry:
    
    
    gcloud dataplex aspect-types create official-data-product-spec \
        --location="${REGION}" \
        --project="${PROJECT_ID}" \
        --description="Defines the comprehensive profile of a data product for data governance agents." \
        --display-name="Official Data Product Spec" \
        --metadata-template-file-name="aspect_template.json"
    

## Attach governance aspects to data lake tables

This is the critical engineering step. Right now, the table `finance_mart.fin_monthly_closing_internal` and `analyst_sandbox.tmp_data_dump_v2_final_real` look identical to an AI agent. They are just objects with columns.

To tell them apart, you apply [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspects), which attach certified metadata labels to these tables to differentiate them. In a real enterprise, you would automate this with CI/CD pipelines. In this tutorial, you simulate that automation with scripts.

### Generate the aspect metadata payloads

Knowledge Catalog aspect keys must be globally unique (prefixed with your project ID). The `./generate_payloads.sh` script dynamically generates the YAML metadata files:
    
    
    chmod +x ./generate_payloads.sh
    ./generate_payloads.sh
    

This creates an `aspect_payloads/` directory that contains 4 YAML files defining different data governance scenarios (`fin_internal.yaml`, `fin_public.yaml`, `mkt_realtime.yaml`, `sandbox.yaml`).

### Attach aspects to BigQuery tables

  1. Before you run the script, look at the data that you're attaching to the tables. Run the following command to see the metadata for your internal finance data:
         
         cat aspect_payloads/fin_internal.yaml
         

The YAML file defines the business context for the table:
         
         your-project-id.us-central1.official-data-product-spec:
           data:
             product_tier: GOLD_CRITICAL
             data_domain: FINANCE
             usage_scope: INTERNAL_ONLY
             update_frequency: DAILY_BATCH
             is_certified: true
         

Notice how this explicitly defines the business context, such as setting `is_certified: true` and assigning the `GOLD_CRITICAL` tier. This gives the AI agent clear, structured rules to evaluate instead of guessing based on table names.

  2. Run the application script. This script iterates through your BigQuery tables and uses the `gcloud dataplex entries update` command to attach your metadata payloads onto each table:
         
         chmod +x ./apply_governance.sh
         ./apply_governance.sh
         




### Verify the applied aspects in the Google Cloud console

Before you move on, check that the script applied the aspects correctly in the Google Cloud console:

  1. Open the **Knowledge Catalog** page in the Google Cloud console. You can use the top search bar to find it.
  2. Search for `fin_monthly_closing_internal`. Select the BigQuery table name in the results to open its details page.
  3. In the **Optional tags and aspects** section at the bottom, find the `official-data-product-spec` aspect. Confirm that the values match the "Gold Internal" scenario you applied.



You have now confirmed that technically identical BigQuery tables (`fin_monthly_closing_internal` and `tmp_data_dump_v2_final_real`) are logically differentiated by machine-readable metadata.

## Test your data context with the Antigravity CLI

Before building an application, you can verify your data governance logic locally with the [Antigravity CLI](https://antigravity.google/docs/cli/overview). To do this, you install the Knowledge Catalog plugin and configure the agent skill.

### Install the Knowledge Catalog plugin

In Cloud Shell, install the service plugin:
    
    
    export DATAPLEX_PROJECT="${PROJECT_ID}"
    
    agy plugin install https://github.com/gemini-cli-extensions/dataplex
    

### Inspect the agent skill definition

The agent skill is a static, reusable definition file located in `.agents/skills/knowledge-catalog-governance/SKILL.md`. It contains the logic that translates abstract human rules like "I need safe data" into structured technical lookups.

To check the skill setup and understand how the data context works, inspect the `SKILL.md` file:
    
    
    cat .agents/skills/knowledge-catalog-governance/SKILL.md
    

Notice that it instructs the model to follow strict Phase 1 (Metadata Verification) and Phase 2 (Query Execution) loops. The model must discover and verify metadata before constructing any SQL statements. This search-first logic prevents the agent from guessing table names or hallucinating answers from unverified sources.

### Start the Antigravity CLI session

Start the Antigravity CLI session. Since you're in the project folder, the CLI automatically discovers and loads the skill from the `.agents/skills` directory:
    
    
    agy
    

**Note:** You might see multiple context files load. This is normal. The CLI loads the local skill for this project's specific rules, plus the default instructions for the service plugin.

### Verify plugin installation in the CLI

In the Antigravity CLI prompt, confirm that the plugin is active. Type `/mcp` to list configured tools and plugins:
    
    
    /mcp
    

The output should show `knowledge-catalog` listed as an active plugin with its available tools:
    
    
    MCP Servers ... >  ✓ knowledge-catalog  Tools: search_entries, lookup_context, lookup_entry
    

### Run data context verification scenarios

Now it's time to see your data context in action. Paste these prompts into the Antigravity CLI session one by one.

**Tip:** If prompted to authorize tool use, select **"2. Yes, and always allow 'knowledge-catalog/search_entries' in this conversation"** for testing without having to approve every step.

#### Scenario 1: Retrieve certified gold-tier data

See whether the Antigravity CLI can find the most trustworthy data for a high-stakes board meeting:
    
    
    We are preparing the deck for an internal Board of Directors meeting next week. I need the numbers to be absolutely finalized, trustworthy, and kept strictly confidential. Which table is safe to use?
    

The CLI should skip over the raw data and find `fin_monthly_closing_internal`. It does this by matching your request for "finalized" and "confidential" data against the `GOLD_CRITICAL` and `INTERNAL_ONLY` tags you applied earlier.

#### Scenario 2: Restrict retrieval to externally approved data

Pretend you want to share data externally. You want to make sure the CLI doesn't let any internal secrets slip out:
    
    
    I need to share our quarterly financial summary with an external consulting firm. It is critical that we do not leak any raw or internal metrics. Which dataset is officially scrubbed and explicitly approved for external sharing?
    

Even though the internal table has the most detail, the CLI must bypass it. It should point you to `fin_quarterly_public_report` because it's the only table tagged as `EXTERNAL_READY`.

#### Scenario 3: Retrieve real-time streaming data

Data scientists often need the absolute latest info. See if the Antigravity CLI understands the difference between a daily batch and a livestream:
    
    
    My dashboard needs to show what's happening right now with our ad spend. I can't wait for the overnight load. What do you recommend?
    

The CLI should find `mkt_realtime_campaign_performance`. It identifies the `REALTIME_STREAMING` update frequency in the metadata.

#### Scenario 4: Explore uncertified sandbox data

Sometimes "good enough" is better than "perfect." See if the Antigravity CLI can find the raw sandbox data for some experimental ML work:
    
    
    I'm just playing around with some new ML models and need a lot of raw data. It doesn't need to be perfect, just a sandbox environment.
    

The CLI should find `tmp_data_dump_v2_final_real`. It knows this is the right choice because it matches the `BRONZE_ADHOC` tier and is explicitly marked with `is_certified: false`.

When you finish testing, you can exit the CLI session:
    
    
    /quit
    

## Clean up

Follow these steps to avoid recurring charges:

  1. If you are in the Antigravity CLI session, exit the session by pressing `Ctrl+C` twice or typing `/quit`.

  2. Execute the cleanup script to destroy the BigQuery tables, datasets, and Knowledge Catalog aspect types created in this tutorial:
         
         chmod +x ./cleanup_data_lake.sh
         ./cleanup_data_lake.sh
         

  3. Uninstall the service plugin and remove your local demo files:
         
         agy plugin uninstall dataplex
         cd ~
         rm -rf ~/devrel-demos
         




## What's next

  * Try other [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
