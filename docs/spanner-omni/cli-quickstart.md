---
url: https://docs.cloud.google.com/spanner-omni/cli-quickstart/
title: Quickstart using the Spanner Omni CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:01.062789+00:00
---

# Quickstart using the Spanner Omni CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/cli-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Quickstart using the Spanner Omni CLI Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use the Spanner Omni command-line interface (CLI) to interact with and manage a Spanner Omni deployment. The Spanner Omni CLI provides commands for common administrative tasks and includes an interactive SQL shell for querying your database.

## Before you begin

Before you can use the Spanner Omni CLI, ensure you meet the following requirements:

  1. A Spanner Omni deployment is set up and running.
  2. The machine running the Spanner Omni CLI has network access to the load balancer of the Spanner Omni deployment or to at least one of the servers in the deployment.



## Step 1: Download and install the Spanner Omni CLI

  1. Download the Spanner Omni CLI from the `spanner-omni` Cloud Storage bucket.

[Go to the Spanner Omni bucket](https://console.cloud.google.com/storage/browser/spanner-omni)

  2. Extract the tar file.
         
         tar -xvf CLI_TAR_FILE
         

This installs the Spanner Omni CLI binary, called `spanner`, in the `google/spanner/bin` directory.

To run the `spanner` command, add the `google/spanner/bin` directory to your `PATH` environment variable, or use the full path to the binary in the following steps.




## Step 2: Connect to your deployment

By default, the Spanner Omni CLI attempts to connect to `localhost:15000`. To connect to your specific deployment, use the `--deployment-endpoint` flag.

For example, the following command lists the zones in your deployment:
    
    
    spanner deployment zones list \
        --deployment-endpoint=LOAD_BALANCER_IP_OR_SERVER_IP:PORT
    

## Step 3: Run common commands

The following are common administrative commands you can run with the Spanner Omni CLI.

### Get help

To see a list of available commands and global flags, run:
    
    
    spanner --help
    

### Create a database

To create a new database in your deployment, run:
    
    
    spanner databases create DATABASE_NAME \
        --deployment-endpoint=LOAD_BALANCER_IP_OR_SERVER_IP:PORT
    

### List all databases

To list all databases in your deployment, run:
    
    
    spanner databases list \
        --deployment-endpoint=LOAD_BALANCER_IP_OR_SERVER_IP:PORT
    

## Step 4: Start an interactive SQL shell session

The Spanner Omni CLI includes an interactive SQL shell for running queries. By starting the shell for a specific database with the `--database` flag, you can run SQL commands without needing to specify the database or endpoint for every query.

To start the SQL shell, run:
    
    
    spanner sql --database=DATABASE_NAME \
        --deployment-endpoint=LOAD_BALANCER_IP_OR_SERVER_IP:PORT
    

After the shell starts, you see the `sql>` prompt:
    
    
    spanner-cli>
    

To exit the shell, type `exit`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
