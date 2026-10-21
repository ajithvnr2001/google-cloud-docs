---
url: https://docs.cloud.google.com/sql/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Cloud SQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:32.662451+00:00
---

# Security bulletins  |  Cloud SQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/resources)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

This page describes all security bulletins related to Cloud SQL.

To get the latest security bulletins, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the following feed URL directly to your feed reader:
        
        https://cloud.google.com/feeds/cloud-sql-security-bulletins.xml




## GCP-2023-007

**Published:** 2023-06-02

### Description

Description | Severity | Notes  
---|---|---  
A third-party researcher identified a Cloud SQL for SQL Server vulnerability, and the instance they triggered this vulnerability on was automatically detected by Google Cloud through a security alert. After the detection, Google Cloud contacted the researcher and the researcher reported the issue through the [Google Cloud VRP program](https://bughunters.google.com/). Google Cloud resolved the issue by patching the security vulnerability by March 1, 2023. Google Cloud didn't find any compromised customer instances.

#### What should I do?

**No further action is required for any customer.** Cloud SQL for SQL Server has been updated to fix this vulnerability and the fix was rolled out to all instances in March 2023. No action is required.

#### What vulnerabilities are being addressed?

The vulnerability allowed customer administrator accounts to create triggers in the `tempdb` database and use those to gain `sysadmin` privileges in the instance. The `sysadmin` privileges would give the attacker access to system databases and partial access to the machine running that SQL Server instance. Because the attack requires access to a customer administrator account, this vulnerability didn't expose any customer data that the attacker didn't already have access to. Moreover, this vulnerability didn't give the attacker any access to other Cloud SQL for SQL Server instances. This issue was not a security incident and no data was compromised. | High |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
