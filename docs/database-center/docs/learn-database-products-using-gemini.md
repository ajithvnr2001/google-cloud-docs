---
url: https://docs.cloud.google.com/database-center/docs/learn-database-products-using-gemini/
title: Learn about databases using Gemini \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:15:14.674833+00:00
---

# Learn about databases using Gemini  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/learn-database-products-using-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  Learn about databases using Gemini Stay organized with collections  Save and categorize content based on your preferences. 

You can learn about Google Cloud database products by entering prompts into Gemini at the Google Cloud project or folder level. For example, you can learn about the following:

  * Database Center concepts. For example, you can prompt Gemini to provide guidance about how Database Center measures your database fleet health.
  * Database Center health issues. For example, you can prompt Gemini to explain why it's an issue that your database has public IP enabled.



The following are example prompts to help you learn general information about Database Center:

  * "Which of my Cloud SQL instances have performance issues?"
  * "Which of my databases are not backed-up properly?"
  * "Which of my AlloyDB for PostgreSQL instances have had their CPU spike to more than 80% and memory spike to more than 85% in the last 7 days?"



## Before you begin

  * [Ensure that Database Center is set up for your organization](https://docs.cloud.google.com/database-center/docs/set-up-database-center).

  * Set up Gemini chat at the Google Cloud project level, the folder level, or both.

###  Project level 

To use Gemini chat at the Google Cloud project level, [set up Gemini Cloud Assist for a project](https://docs.cloud.google.com/cloud-assist/set-up-gemini#project).

###  Folder level 

To use Gemini chat at the folder level, [set up Gemini Cloud Assist for a folder](https://docs.cloud.google.com/cloud-assist/set-up-gemini#folder).




## Use Gemini to learn about fleet health issues

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

You can use Gemini Cloud Assist to track health issues in Database Center, and [Gemini chat](https://docs.cloud.google.com/database-center/docs/learn-database-products-using-gemini#use-gemini-learn-database-fleet-health-issues) to learn more about your database fleet and inventory.

### Use Gemini chat

To use Gemini chat to learn more about database fleet health issues and Database Center, follow these steps:

  1. In the Google Cloud console, go to the **Database Center** page.

[Database Center](https://console.cloud.google.com/database-center)

  2. To open Gemini, click spark **Gemini**.

  3. Click **Start chatting**.

  4. In the Gemini chat enter a prompt, for example, `What is a database fleet?`

  5. To send the prompt, click send**Send**. Gemini returns a response similar to the following:
         
         A database fleet consists of all the provisioned database resources across all Google Cloud database products that your organization uses. Database resources are the clusters, instances, and virtual machines that power your workloads. Database Center supports Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and AlloyDB.
         




### Use Gemini Cloud Assist

Use Gemini Cloud Assist to detect and publish intelligent performance insights and recommendations at the fleet level for your organization. Gemini Cloud Assist lets you investigate select scenarios and performance issues with granular metrics using system insights and query insights integration. Gemini Cloud Assist also provides cost optimization recommendations.

The following is a list of Database Center recommendations provided by Gemini Cloud Assist.

#### Performance insights and recommendations

The following performance insights and recommendations for certain database products are detected for Database Center by Gemini Cloud Assist:

Insight or recommendation | Database products  
---|---  
Inefficient queries and index advisor to enhance query performance | Cloud SQL, AlloyDB for PostgreSQL  
  
#### Cost recommendations

The following are the cost recommendations detected for Database Center by Gemini Cloud Assist:

Cost recommendation | Recommendation details | Database products  
---|---|---  
Over provisioned resource | Checks if a database resource had low CPU and memory utilization during the past 30 days | Cloud SQL  
Idle resource | Checks if a database resource had a low level of activity during the past 30 days | Cloud SQL  
  
## What's next

  * [Analyze database fleet health using Gemini](https://docs.cloud.google.com/database-center/docs/analyze-database-using-gemini).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
