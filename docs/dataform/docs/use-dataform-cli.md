---
url: https://docs.cloud.google.com/dataform/docs/use-dataform-cli/
title: Use the open-source Dataform CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:41.139918+00:00
---

# Use the open-source Dataform CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/use-dataform-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Use the open-source Dataform CLI Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use the open-source Dataform command-line interface (CLI) to locally develop workflows by using the terminal. 

With the open-source Dataform CLI, you can initialize, compile, test, and run [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core) locally, outside of Google Cloud.

The Dataform CLI supports [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials). With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. To use ADC, you must first [provide your credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) to ADC.

**Note:** As of [Dataform core `3.0.0.`](https://github.com/dataform-co/dataform/releases/tag/3.0.0), Dataform doesn't distribute a Docker image. You can build your own Docker image of Dataform, which you can use to run the equivalent of Dataform CLI commands. To build your own Docker image, see [Containerize an application](https://docs.docker.com/guides/workshop/02_our_app/) in the Docker documentation.

## Before you begin

Before installing the Dataform CLI, install [NPM](https://www.npmjs.com/get-npm).

## Install Dataform CLI

  * To install Dataform CLI, run the following command:
        
        npm i -g @dataform/cli
        


**Note:** Version `3.0.0-beta` isn't supported. If `npm audit` reports a high-severity vulnerability related to the `vm2` package, note that while Dataform uses `vm2`, Dataform doesn't use `vm2` for sandboxing, which is the source of reported vulnerabilities. Newer versions of Dataform CLI don't depend on vulnerable `vm2` versions.

## Initialize a Dataform project

  * To initialize a new Dataform project, run the following command inside your project directory:
        
        dataform init . PROJECT_NAME DEFAULT_LOCATION
        

Replace the following:

    * `PROJECT_NAME`: the name of your project.
    * `DEFAULT_LOCATION` (optional): the location where you want Dataform to write BigQuery data. If unset, Dataform determines the location based on the datasets that your SQL query references. This works as follows:

      * If your query references datasets from the same location, Dataform uses that location.
      * If your query references datasets from two or more different locations, an error occurs. For details about this limitation, see [Cross-region dataset replication](https://docs.cloud.google.com/bigquery/docs/data-replication).
      * If your query doesn't reference any datasets, the default location for Dataform is the `US` multi-region. To choose a different location, set the default location. Alternatively, use the [`@@location` system variable](https://docs.cloud.google.com/bigquery/docs/reference/system-variables) in your query. For more information, see [Specify locations](https://docs.cloud.google.com/bigquery/docs/locations#specify_locations).



## Update Dataform core

  * To update the Dataform core framework, update the `dataformCoreVersion` in `workflow_settings.yaml` file, then re-run NPM install:
        
        npm i
        




## Update Dataform CLI

  * To update the Dataform CLI tool, run the following command:
        
        npm i -g @dataform/cli@^3.0.50
        




## Create a credentials file

Dataform requires a credentials file to connect to remote services and create the `.df-credentials.json` file on your disk.

**Warning:** If you use a source control system, don't commit the `.df-credentials.json` file to your repository to protect these access credentials. We recommend that you add the `.df-credentials.json` file to `.gitignore`.

To create the credentials file, follow these steps:

  1. Run the following command:
         
         dataform init-creds
         

  2. Follow the `init-creds` wizard that walks you through credentials file creation.




## Create a project

An empty Dataform project in Dataform core 3.0.0 or later has the following structure:
    
    
       project-dir
       ├── definitions
       ├── includes
       └── workflow_settings.yaml
    

  * To create a Dataform project to deploy assets to BigQuery, run the following command:
        
        dataform init PROJECT_NAME --default-database YOUR_GOOGLE_CLOUD_PROJECT_ID --default-location DEFAULT_LOCATION
        

Replace the following:

    * `PROJECT_NAME`: the name of your project.
    * `YOUR_GOOGLE_CLOUD_PROJECT_ID`: your Google Cloud project ID.
    * `DEFAULT_LOCATION` (optional): the location where you want Dataform to write BigQuery data. If unset, Dataform determines the location based on the datasets that your SQL query references. This works as follows:

      * If your query references datasets from the same location, Dataform uses that location.
      * If your query references datasets from two or more different locations, an error occurs. For details about this limitation, see [Cross-region dataset replication](https://docs.cloud.google.com/bigquery/docs/data-replication).
      * If your query doesn't reference any datasets, the default location for Dataform is the `US` multi-region. To choose a different location, set the default location. Alternatively, use the [`@@location` system variable](https://docs.cloud.google.com/bigquery/docs/reference/system-variables) in your query. For more information, see [Specify locations](https://docs.cloud.google.com/bigquery/docs/locations#specify_locations).



## Clone a project

To clone an existing Dataform project from a third-party Git repository, follow the instructions from your Git provider.

  * Once the repository is cloned, run the following command inside the cloned repository directory:
        
        dataform install
        




## Define a table

Store definitions in the `definitions/` folder.

  * To define a table, run the following command:
        
        echo "config { type: 'TABLE_TYPE' } SELECT_STATEMENT" > definitions/FILE.sqlx
        

Replace the following:

    * `TABLE_TYPE`: the type of the table: `table`, `incremental`, or `view`.
    * `SELECT_STATEMENT`: a `SELECT` statement that defines the table.
    * `FILE`: the name for the table definition file.



The following code sample defines a view in the `example` SQLX file.
    
    
    echo "config { type: 'view' } SELECT 1 AS test" > definitions/example.sqlx
    

## Define a manual assertion

Store definitions in the `definitions/` folder.

  * To define a manual assertion, run the following command:
        
        echo "config { type: 'assertion' } SELECT_STATEMENT" > definitions/FILE.sqlx
        

Replace the following:

    * `SELECT_STATEMENT`: a `SELECT` statement that defines the assertion.
    * `FILE`: the name for the custom SQL operation definition file.



## Define a custom SQL operation

Store definitions in the `definitions/` folder.

  * To define a custom SQL operation, run the following command:
        
        echo "config { type: 'operations' } SQL_QUERY" > definitions/FILE.sqlx
        

Replace the following:

    * `SQL_QUERY`: your custom SQL operation.
    * `FILE`: the name for the custom SQL operation definition file.



## View compilation output

Dataform compiles your code in real time.

  * To view the output of the compilation process in the terminal, run the following command:
        
        dataform compile
        

  * To view the output of the compilation process as a JSON object, run the following command:
        
        dataform compile --json
        

  * To view the output of the compilation with [custom compilation variables](https://docs.cloud.google.com/dataform/docs/configure-compilation#compilation-variables), run the following command:
        
        dataform compile --vars=SAMPLE_VAR=SAMPLE_VALUE,foo=bar
        

Replace the following:

    * `SAMPLE_VAR`: your custom compilation variable.
    * `SAMPLE_VALUE`: the value of your custom compilation variable.



## Run code

To run your code, Dataform accesses BigQuery to determine its current state and tailor the resulting SQL accordingly.

  * To run the code of your Dataform project, run the following command:
        
        dataform run
        

  * To run the code of your Dataform project in BigQuery with [custom compilation variables](https://docs.cloud.google.com/dataform/docs/configure-compilation#compilation-variables), run the following command:
        
        dataform run --vars=SAMPLE_VAR=SAMPLE_VALUE,sampleVar2=sampleValue2
        

Replace the following:

    * `SAMPLE_VAR`: your custom compilation variable.
    * `SAMPLE_VALUE`: the value of your custom compilation variable.
  * To run the code of your Dataform project in BigQuery and rebuild all tables from scratch, run the following command:
        
        dataform run --full-refresh
        




Without `--full-refresh`, Dataform updates incremental tables without rebuilding them from scratch.

  * To perform a dry run of your code against BigQuery, run the following command:
        
        dataform run --dry-run
        


**Note:** In Dataform core `3.0.2` or later, Dataform performs a dry run of each action in your compilation output against BigQuery, and requires corresponding IAM permissions. To verify compilation without a dry run, view compilation output.

## Get help

  * To list all of the available commands and options, run the following command:
        
        dataform help
        

  * To view a description of a specific command, run the following command:
        
        dataform help COMMAND
        

Replace `COMMAND` with the command you want to learn about.




## What's next

  * To learn more about Dataform CLI, see [Dataform CLI reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-cli-reference)
  * To learn more about Dataform, see [Dataform overview](https://docs.cloud.google.com/dataform/docs/overview). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
