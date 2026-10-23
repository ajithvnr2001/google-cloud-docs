---
url: https://docs.cloud.google.com/oracle/database/docs/generate-wallet/
title: Generate a wallet \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:02.762896+00:00
---

# Generate a wallet  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/generate-wallet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Generate a wallet Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate a wallet for an Autonomous AI Database in Google Cloud.

You can download your client credentials by generating a wallet. The wallet contains information for mTLS connections only. For TLS connections, you don't need to generate a wallet.

Generating a wallet for an APEX workload type database is not supported.

## Generate a wallet for an Autonomous AI Database

To generate a wallet, do the following:

### Console

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the Autonomous AI Database for which you want to generate the wallet.

  3. On the **Autonomous AI Database details** page, select the **Connections** tab.

  4. In the **Download client credentials (Wallet)** section, click **Download wallet**.

  5. In the **Download your wallet** dialog, set a password for the wallet.

  6. Click **Download**.




### gcloud

Use the `gcloud oracle-database autonomous-databases generate-wallet` command to generate the wallet.
    
    
    gcloud oracle-database autonomous-databases generate-wallet DATABASE_NAME \
        --location=REGION_ID \
        --project=PROJECT_NAME \
        --password=PASSWORD
    

Replace the following:

  * DATABASE_NAME: name of the database.
  * REGION_ID: the region of your database.
  * PROJECT_NAME: the name of your Google Cloud project.
  * PASSWORD: a password for the wallet.



## What's next

  * Learn how to [manage](https://docs.cloud.google.com/oracle/database/docs/manage-databases) or [delete](https://docs.cloud.google.com/oracle/database/docs/delete-databases) an Autonomous AI Database.
  * Configure [Identity and Access Management roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles) for an instance.
  * [Use monitoring metrics](https://docs.cloud.google.com/oracle/database/docs/monitoring-metrics) to monitor your instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
