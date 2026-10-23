---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/install/
title: Install the BigQuery Connector for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:46.947270+00:00
---

# Install the BigQuery Connector for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install the BigQuery Connector for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to install **version 2.15(latest)** of the BigQuery Connector for SAP in your SAP LT Replication Server.

This guide covers how to prepare BigQuery, SAP Landscape Transformation Replication Server (SAP LT Replication Server), and BigQuery Connector for SAP to replicate SAP data from SAP applications directly and securely to Google Cloud in real time.

This guide is intended for SAP administrators, Google Cloud administrators, and other SAP and Google Cloud security and data professionals.

## Before you begin

Before you install BigQuery Connector for SAP, make sure that the following prerequisites have been satisfied:

  * You have read the [BigQuery Connector for SAP planning guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning). The planning guide explains BigQuery Connector for SAP options, performance considerations, field mapping, and other information that you need for the optimal configuration of BigQuery Connector for SAP.
  * If you don't have a Google Cloud project already, then create one:

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * Billing is enabled for your project. [Learn how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project). A billing account is required to download BigQuery Connector for SAP.

  * Maintenance for the installed SAP software is current and the versions of all of the SAP software are compatible with each other, as documented in the [SAP Product Availability Matrix](https://support.sap.com/en/release-upgrade-maintenance.html#section_1969201630).

  * The versions of the SAP software you are using are supported by the BigQuery Connector for SAP, as documented in [Software requirements](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#reqs-software).

  * You have the correct SAP licenses that are required to replicate data to any target through the SAP LT Replication Server SDK. For more information about SAP licensing, see [SAP Note 2707835](https://launchpad.support.sap.com/#/notes/2707835).

  * SAP LT Replication Server is installed. For information about installing SAP LT Replication Server, see the [SAP documentation](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

  * The RFC or database connection between SAP LT Replication Server and the source system is configured. If necessary, test the RFC connections by using SAP transaction `SM59`. Test database connections by using SAP transaction `DBACOCKPIT`.




## Overview of the installation and configuration process

The following table shows procedures covered in this guide and the roles that typically perform them.

**Note:** Depending on your version of SAP LT Replication Server, some of the details in the procedures that are documented in this guide might differ from the details that you see when you perform the steps.Procedure | Role  
---|---  
If necessary, after validating all appropriate licenses from SAP, follow the SAP instructions to [install an SAP Landscape Transformation Replication Server](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US). | SAP administrator.   
If necessary, install the user interface (UI) add-on for SAP NetWeaver. For more information, see [SAP software version requirements](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#reqs-software-sap). | SAP administrator.   
If your SAP workload is not running on Google Cloud, then  establish a network connection between your SAP system and Google Cloud. | Network administrator.  
If your SAP workload is not running on Google Cloud, then  enable private access to the Google Cloud APIs.  | Google Cloud network administrator.  
Download the BigQuery Connector for SAP installation package. | Google Cloud billing account holder.  
Install BigQuery Connector for SAP. | SAP administrator.  
[Set up authentication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication). | Google Cloud security administrator.  
According to your replication path, choose one of the following configuration options:

  * [Configure the connector for CDC replication through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api).
  * [Configure the connector for streaming data replication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api).
  * [Configure the connector for file-based replication to Cloud Storage](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication).

| Data engineers or administrators.  
  
## Establish a network connection to Google Cloud

If your SAP workload is running on Google Cloud, then you can skip this step.

If your SAP workload is not running on Google Cloud, then you or a network administrator needs to establish a secure, high-bandwidth, low-latency connection to Google Cloud.

You have the following two connection options:

  * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) (recommended)
  * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



To set up a connection, follow the instructions provided by the Google Cloud connection service that you select.

Each connection service has different instructions for different scenarios, so review the service documentation and follow the instructions for your scenario.

## Enable private access to the Google Cloud APIs

If your SAP workload is running on Google Cloud, then you can skip this step.

If your SAP workload is not running on Google Cloud, then after you establish a network connection to Google Cloud, you need to enable private access to the Google Cloud APIs.

To enable private API access, see [Configuring Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

## Download the installation package

Download the latest BigQuery Connector for SAP installation package from [BigQuery Connector for SAP download portal](https://bq-slt-connector.appspot.com/bqconnectorforsap/).

You need your Cloud Billing number to complete the download. For information about billing accounts, see [Cloud Billing & payments profile](https://docs.cloud.google.com/billing/docs/concepts#billing_account).

The installation package includes transport files that you copy into the appropriate transport directory for SAP LT Replication Server.

## Install BigQuery Connector for SAP

After you download the installation package that contains the BigQuery Connector for SAP transport files, your SAP administrator can install BigQuery Connector for SAP by importing the transport files into SAP LT Replication Server.

The SAP transport for BigQuery Connector for SAP contains all of the objects that are required for BigQuery Connector for SAP, including the `/GOOG/` namespace, DDIC objects, the SLT SDK BADI implementation and classes, report programs, and more.

Before importing the transport files into SAP LT Replication Server, verify that your SAP LT Replication Server is supported by BigQuery Connector for SAP, as documented in [Software requirements](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#reqs-software).

In spite of using a supported version of SAP LT Replication Server, in some cases, while importing the transport files, you might see the error message, `Requests do not match the component version of the target system`. In such cases, you need to re-import the transport files into SAP LT Replication Server and while re-importing, on the **Import Transport Request** screen, go to the **Options** tab, and then select the **Ignore Invalid Component Version** checkbox.

**Warning** : 

If you need to install BigQuery Connector for SAP on a host machine where the [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/whats-new) is already installed, then you must contact Cloud Customer Care to get appropriate installation instructions for your setup. Installing BigQuery Connector for SAP without following the instructions from Customer Care can render your ABAP SDK for Google Cloud inoperable.

To find the contact information for Customer Care, go to the [Support overview](https://console.cloud.google.com/support) page in the Google Cloud console. For more information, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

The following procedure is a general procedure. Each SAP system is different, so work with your SAP administrator to determine any changes to the procedure that might be required for your SAP system:

  1. Copy BigQuery Connector for SAP transport files into the following SAP LT Replication Server transport import directories:

     * `/usr/sap/trans/cofiles/KXXXXXX.GM1`
     * `/usr/sap/trans/data/RXXXXXX.GM1`

In the preceding examples, `XXXXXX` represents the numbered filename.

  2. In the SAP GUI, use transaction code `STMS_IMPORT` or `STMS` to import the files into the SAP system.

  3. Make sure all objects in `/GOOG/SLT_SDK` package are active and consistent:

     1. In the SAP interface, enter transaction code `SE80`.
     2. In the package selector, select `/GOOG/SLT_SDK`.
     3. In the **Object name** field, right-click on the package `/GOOG/SLT_SDK`, and then choose **Check > Package Check > Objects of Package**.

A green check in the **Result** column indicates that all objects passed the package check.




## Verify the installation

To verify that the BigQuery Connector for SAP is installed correctly, check the following:

  * BigQuery Connector for SAP Business Add-In (BAdI) implementation is active.
  * BigQuery Connector for SAP replication applications have entries in the `IUUC_REPL_APPL` table.



To verify the BigQuery Connector for SAP installation, do the following:

  1. Check the BAdI implementation: 
     1. Use the transaction **SE80** to navigate to and select the `/GOOG/EI_IUUC_REPL_RUNTIME_BQ` enhancement object folder.
     2. Select **Enh. Implementation Elements** on the right side of the page.
     3. Under **Runtime Behavior** , confirm that **Implementation is active** is checked.
  2. Check the replication applications: 
     1. Using the SAP **Data Browser** or transaction `SE16`, display the `IUUC_REPL_APPL` table.
     2. Confirm that the following applications appear in the `IUUC_REPL_APPL` table: 
        * `/GOOG/SLT_BQ`
        * `ZGOOG_SLT_BQ`, for use when the `/GOOG/` namespace isn't registered



## Troubleshoot

For information about diagnosing and resolving issues that you might encounter when you install the BigQuery Connector for SAP, see [BigQuery Connector for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting).

## Get support

If you need help resolving problems with installing the BigQuery Connector for SAP, then collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

## What's next

For information about how to set up authentication, see [Authentication overview for the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
