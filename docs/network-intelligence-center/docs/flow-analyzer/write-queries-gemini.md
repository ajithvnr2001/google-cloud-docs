---
url: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/write-queries-gemini/
title: Write queries with Gemini assistance \u00a0|\u00a0 Network Intelligence Center - Flow Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:33.987644+00:00
---

# Write queries with Gemini assistance  |  Network Intelligence Center - Flow Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/write-queries-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Flow Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)



#  Write queries with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview —[Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use natural language prompts to generate SQL queries for VPC Flow Logs. To generate SQL queries for VPC Flow Logs, you interact with [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) in Flow Analyzer.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

  * [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini) in a Google Cloud project that contains a Cloud Logging bucket with flow logs.

  * Make sure that the log bucket is [upgraded to use Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket) and you have the [required roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows#required_roles_and_permissions) to query the flow logs.




## Generate a SQL query

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

To interact with Gemini Cloud Assist, use the pen_spark**Compose a Cloud Assist Query** prompt field. In the prompt field, you can enter a prompt or select a predefined prompt. The following table provides examples of prompts that you can use.

Prompt | Generated SQL query  
---|---  
Show me cross-zonal traffic | Selects flows where the source and destination are in different zones.  
Show me resources with SSH traffic | Selects flows with SSH traffic.  
Show me the top 10 VMs with the highest traffic | Selects 10 VMs with the highest number of bytes sent.  
Show me traffic from and to 10.10.0.10 | Selects flows where 10.10.0.10 is the source or destination IP address.  
Show me traffic from example-instance to the internet | Selects flows from the source VM instance named `example-instance` to the internet.  
Show me traffic from gateways within the last three days | Selects flows within the last three days where VLAN attachments for Cloud Interconnect and Cloud VPN tunnels are the source.  
  
To generate and run a SQL query, do the following:

  1. In the Google Cloud console, go to the **Flow Analyzer** page.

[Go to Flow Analyzer](https://console.cloud.google.com/net-intelligence/flow-analyzer)

  2. Click pen_spark**Compose a Cloud Assist Query**.

  3. Describe the log data that you want to view or select a predefined prompt.

  4. Click **Generate SQL**.

  5. Review the response and run the query:

     * To run the query in Flow Analyzer, click the **Explore in Flow Analyzer** tab and then click **Open in Flow Analyzer**.
     * To run the query in Observability Analytics, click the **Run SQL in Log Analytics** tab and then click **Run SQL in Log Analytics**.



After you run the query, you can optionally modify the populated values as needed.

## What's next

  * Read [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
