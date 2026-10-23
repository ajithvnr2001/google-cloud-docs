---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/getting-support-diag-info/
title: Diagnostic information for BigQuery Connector for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:46.980383+00:00
---

# Diagnostic information for BigQuery Connector for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/getting-support-diag-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  Diagnostic information for BigQuery Connector for SAP Stay organized with collections  Save and categorize content based on your preferences. 

For problems that are related to BigQuery Connector for SAP, provide the following diagnostic information to Cloud Customer Care when you open a case: 

  * A complete and detailed description of the problem
  * Error messages encountered
  * LTRC settings
  * BigQuery Connector for SAP configuration
  * SAP system environment details
  * Logs



## Detailed description of the problem

Provide a complete and detailed description of the problem, including the version of BigQuery Connector for SAP and the date and time when the problem occurred.

To see the version of BigQuery Connector for SAP that you are using, complete the following steps:

###  Version 2.8 and later 

  * In SAP GUI, execute the transaction `/GOOG/BQC_VERSION`. A dialog appears with the version of the BigQuery Connector for SAP installed on your system.



###  Previous versions 

  1. In the SAP GUI, enter the transaction `SE24`.
  2. Enter the class name `/GOOG/CL_GCP_CLIENT_BQ`.
  3. Click **Display** , and then navigate to the **Attributes** tab.
  4. For attribute `C_USER_AGENT`, note the value set in the **Initial value column**. If the column doesn't show the entire string, then expand it.



## Error messages encountered

Provide the error messages that you encountered in BigQuery Connector for SAP. Include details such as the screen or transaction where you encountered the issue, or a screenshot.

## LTRC settings

For the required mass transfer ID in the transaction `LTRC`, provide the details of the settings specified in the **Administration data** tab.

## BigQuery Connector for SAP configuration

Provide the following configuration details:

  * Client key configurations specified in the table `/GOOG/CLIENT_KEY`. For more information, see the appropriate guide: 
    * For SAP workloads running on Google Cloud, see [Specify access settings in `/GOOG/CLIENT_KEY`](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token#specify-clientkey-table).
    * For SAP workloads running outside Google Cloud, see [Specify access settings in `/GOOG/CLIENT_KEY`](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt#jwt-specify-access-settings).
  * Service mapping configurations specified in the table `/GOOG/SERVIC_MAP`.
  * Parameter settings specified in the table `/GOOG/BQ_PARAM`. For more information, see [Advanced settings](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#advanced-settings).
  * Mass transfer configuration for BigQuery Connector for SAP that is specified in the transaction `/GOOG/SLT_SETTINGS`.
  * Table settings specified for tables included in the mass transfer ID.
  * Field settings for the tables specified in the transaction `/GOOG/SLT_SETTINGS`.



## SAP system environment details

Provide the following environment details of your SAP system:

  * Specify if your SAP system runs on Google Cloud or outside Google Cloud.
  * Specify if your SAP LT Replication Server is installed standalone or if it's embedded with the SAP source system server.
  * Provide the SAP system version: 
    * The `SAP_BASIS` component version.
    * The version of the installed SAP product.
  * Provide the environment language: 
    * The SAP logon language.
    * The language of the background mode.
  * If your SAP LT Replication Server is hosted outside Google Cloud, then specify if you are authenticating to Google Cloud using the gcloud CLI or JSON Web Tokens (JWT).



## Logs

Provide the following logs:

  * LTRC application logs. To get these logs, complete the following steps:

    1. In the SAP GUI, enter the transaction `LTRC`.
    2. Select your mass transfer ID, and then navigate to the **Application Logs**.
    3. Use filters such as date and timestamps to extract the logs that are relevant to your issue.
  * The `ST22` dumps, if available.

  * The `SMICM` logs, if available. This requires switching on the HTTP trace in the transaction `SMICM`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
