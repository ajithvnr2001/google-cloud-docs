---
url: https://docs.cloud.google.com/mainframe-connector/docs/agentic-tools-to-transcode-and-migrate-data/
title: Use Google Antigravity to transcode and migrate data \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:55.096557+00:00
---

# Use Google Antigravity to transcode and migrate data  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/agentic-tools-to-transcode-and-migrate-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Use Google Antigravity to transcode and migrate data Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can use agentic capabilities in Mainframe Connector to automatically transcode and migrate your mainframe data.

## Key benefits of agentic integration

Mainframe Connector supports an agentic surface you can use for data modernization. You can use agents in combination with Mainframe Connector to modernize your existing mainframe data on Cloud Storage and locally. You can also use agentic environments such as Google Antigravity to create the Mainframe Connector configurations required to transcode and migrate your mainframe data.

### Automate transcoding and data migration

Writing transcode configurations by hand can be error-prone and complex due to the mismatch between legacy COBOL structures (such as `REDEFINES`, `COMP-3`, and `PIC X`), and modern cloud databases (such as BigQuery). This complexity often leads to errors in data type mapping, byte alignment, and packed decimal translation.

To simplify this process, Mainframe Connector supports **agentic capabilities** —a suite of focused tools (API and CLI endpoints) and a dedicated _skills file_ —designed for use by LLM-powered agents such as Google Antigravity. This integration allows an agent to autonomously draft, strictly validate, self-correct, and test transcode configuration files. The agent can then migrate your existing data from Cloud Storage or a local storage to BigQuery or other databases, using the generated configurations.

Using agentic capabilities in Mainframe Connector provides the following benefits:

  * **Automated drafting:** Google Antigravity can generate the initial configuration based on a COBOL copybook and user-defined business rules.
  * **Rapid feedback loops:** Built-in validation tools allow the agent to quickly test configurations and self-correct errors before processing data.
  * **Byte-level inspection:** The agent can inspect raw binary data to diagnose alignment and encoding issues.
  * **Deterministic testing:** Lightweight, single-threaded commands provide a reliable test environment for the agent's reasoning process.



## Before you begin

  * To use the agentic capabilities, you must install the latest version of Mainframe Connector. Agentic capabilities are available starting from version 5.20.
  * To run the agent skills, you must install an agentic CLI or environment such as Google Antigravity in the same machine where you installed Mainframe Connector.
  * Extract the agent skills file to your environment's skills folder with the following command:
        
        java -jar mainframe-connector.jar agent skill-file --output-dir SKILLS_FOLDER_PATH
        




## How agentic integration works

The Mainframe Connector skills file contains all the necessary information to allow an agent to create, validate, and test transcode configuration mainframe copybook and data files. It abstracts the underlying Mainframe Connector CLI commands and provides a simplified interface for the agent to interact with the product.

When you prompt the agent using the skills file, you let the agent run AI-optimized versions of the Mainframe Connector commands. If you provide the copybook and sample data, the agent can create the transcode configuration file and validate it against real data. In your prompt, make sure you provide the agent with the context and the special rules to apply in the transcoding.

### Agentic workflow

The agentic workflow consists of five phases, allowing the agent to progress from the initial user request to a working, validated configuration. After the user's prompt, the agent can complete the following steps autonomously.

Phase | Description  
---|---  
**Initiation** |  The user prompts the agent to create a transcode configuration file. The user can optionally provide a COBOL copybook, custom business rules (such as "drop all FILLER fields"), and optional sample EBCDIC data.   
**Drafting** |  The agent reads the `configuration-doc` reference to understand formatting rules, then generates the draft configuration file.   
**Validation** |  The agent validates the draft's syntax and structure by running `validate-configuration`, correcting errors, and verifying the structural blueprint.   
**Testing** |  If sample data is provided, the agent tests the configuration by running `simple-encode` or `simple-decode`, and uses `inspect-data` to verify that the output matches expectations.   
**Finalize** |  The agent generates the target DDL using `generate-target-ddl`, and presents the working configuration and DDL to the user.   
  
### Use cases

The following examples illustrate how you can use the agentic capabilities to transcode and migrate your data.

#### Example 1: Generate data schemas for BigQuery using a copybook

The following sample prompt shows how to use the agentic capabilities to transcode the data from a mainframe copybook and generate a BigQuery table.

**Sample prompt**
    
    
    Your task is to produce a transcode configuration file and target DDL for a
    mainframe dataset using the Mainframe Connector skill.
    
    You are migrating a master file from a European subsidiary's mainframe into
    BigQuery. Each record holds a customer name, a city, and a price.
    The source is an EBCDIC extract from a German z/OS system; the system metadata
    gives its CCSID as 1140.
    
    The data is staged here in this directory:
    
    - `copybook.cpy`: the COBOL layout.
    - `input.dat`: the binary extract itself (CCSID 1140 - the German Euro-enabled
      EBCDIC code page).
    
    Produce two artifacts here:
    
    1. `config.json`: the transcode configuration that correctly decodes this file.
    2. `schema.sql`: the BigQuery `CREATE TABLE` DDL for the destination.
    

#### Example 2: Upload the data to BigQuery after transcoding

The following prompt shows how to use the agentic capabilities to upload the transcoded data from the previous example to BigQuery.

**Sample prompt**
    
    
    Using the Mainframe Connector skill and the config.json and schema.sql files
    you created before, migrate the data to BigQuery at
    `project_id.dataset_name.table_name`.
    

#### Example 3: Deploy into a PostgreSQL database with privacy controls

The following prompt shows how to use the agentic capabilities to deploy the transcoded data from the previous example to PostgreSQL, while removing PII data.

**Sample prompt**
    
    
    Using the Mainframe Connector skill, migrate the data to Cloud SQL for
    PostgreSQL at `table_name.schema_name.host_name`.
    
    Compliance constraint: `CUST-NAME` and `CITY` are classified as
    personally identifying or residency restricted information. They must NOT
    appear in the PostgreSQL CSV staging file, must NOT decode into a JSM
    string at any point, and must NOT appear in the Postgres table DDL.
    Only `PRICE-TEXT` should appear.
    
    Deliverables in the current working directory:
    
    1. `config-postgres.json`: a NEW transcode configuration (do not overwrite
    the BigQuery config.json).
    2. `schema-postgres.sql`: the PostgreSQL `CREATE TABLE` DDL for the
       destination.
    3. `copy-postgres.sql`: the PostgreSQL `COPY FROM` command to load the
       data into the table.
    

## Agentic command suite

The following commands are designed for LLM agents.

### `agent configuration-doc`

Outputs the configuration doc for LLM agents to stdout.

#### Synopsis
    
    
    agent configuration-doc [-h]
    

#### Flags and arguments

The `agent configuration-doc` command uses the following flags and arguments:

**`--help` or `-h`**
    (Optional) Display this help message.

### `agent inspect-data`

Reads a single logical record starting at a specific byte offset, then prints its hex dump and text representation.

#### Synopsis
    
    
    agent inspect-data [-h] [--byte-offset=BYTEOFFSET]
                              --input=INPUTPATH
    

#### Flags and arguments

The `agent inspect-data` command uses the following flags and arguments:

**`--byte-offset`=BYTEOFFSET**
    (Optional) Specify the absolute byte offset within the file to begin reading from. The default value is 0.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--input`=INPUTPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the input data path.

### `agent simple-decode`

Decodes a few rows of a mainframe file to stdout for agent debugging.

#### Synopsis
    
    
    agent simple-decode [-h] [--byte-offset=BYTEOFFSET]
                               --copybook=COPYBOOKPATH
                               --input=INPUTPATH
                               [--limit=LIMIT]
                               [--output=OUTPUTPATH]
                               --transcode-configuration=CONFIGPATH
    

#### Flags and arguments

The `agent simple-decode` command uses the following flags and arguments:

**`--byte-offset`=BYTEOFFSET**
    (Optional) Specify the absolute byte offset in the input file to start reading from. The default value is 0.
**`--copybook`=COPYBOOKPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the data path of the copybook.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--input`=INPUTPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the input data path.
**`--limit`=LIMIT**
    (Optional) Specify the maximum number of records to attempt to decode. Records dropped by `record_filter_condition` still count against this limit. The default value is 5.
**`--output`=OUTPUTPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    (Optional) Specify the destination for the decoded JSON output. If not provided, defaults to `stdout`.
**`--transcode-configuration`=CONFIGPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the data path of the transcoding configuration. For more information on the transcoder configuration format, see [transcoder configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration).

### `agent simple-encode`

Encodes a JSON file back into mainframe EBCDIC binary data.

#### Synopsis
    
    
    agent simple-encode [-h] --copybook=COPYBOOKPATH
                               --input=INPUTPATH
                               --output=OUTPUTPATH
                               --transcode-configuration=CONFIGPATH
    

#### Flags and arguments

The `agent simple-encode` command uses the following flags and arguments:

**`--copybook`=COPYBOOKPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the data path of the copybook.
**`--help` or `-h`**
    (Optional) Display this help message.
**`--input`=INPUTPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the input JSON data path.
**`--output`=OUTPUTPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the output binary data path.
**`--transcode-configuration`=CONFIGPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the data path of the transcoding configuration. For more information on the transcoder configuration format, see [transcoder configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration).

### `agent validate-configuration`

Validates a [transcoder configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration) against a copybook and database rules.

#### Synopsis
    
    
    agent validate-configuration [-h] --copybook=COPYBOOKPATH
                                        --database=DATABASE
                                        --transcode-configuration=CONFIGPATH
    

#### Flags and arguments

The `agent validate-configuration` command uses the following flags and arguments:

**`--copybook`=COPYBOOKPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the data path of the copybook.
**`--database`=DATABASE**
    Specify the target database (e.g. `BIGQUERY`, `POSTGRES`, `MYSQL`).
**`--help` or `-h`**
    (Optional) Display this help message.
**`--transcode-configuration`=CONFIGPATH : [DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#DataPath)**
    Specify the data path containing the draft transcoding configuration. For more information on the transcoder configuration format, see [Transcoder configuration](https://docs.cloud.google.com/mainframe-connector/docs/transcoder-configuration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
