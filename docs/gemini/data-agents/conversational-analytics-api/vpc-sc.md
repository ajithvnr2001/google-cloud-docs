---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/vpc-sc/
title: Configure perimeter security with VPC Service Controls \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:50.198947+00:00
---

# Configure perimeter security with VPC Service Controls  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Configure perimeter security with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

The Conversational Analytics API, which is part of the Gemini Data Analytics service, is integrated with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). You can [add the Conversational Analytics API to your service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#create-perimeter) to enhance the security of your data and services and help mitigate the risk of data exfiltration. When you include `geminidataanalytics.googleapis.com` as a protected service in a perimeter, VPC Service Controls protects the Conversational Analytics API.

### Protect data sources

Even though the service perimeter restricts access to the Conversational Analytics API, you must also include its data source services within the same service perimeter to help protect the data those sources contain. Common data sources for Conversational Analytics API include BigQuery and Looker. Ensure that the services corresponding to these data sources (for example, `bigquery.googleapis.com`) are also protected in the service perimeter.

### IAM roles and permissions

VPC Service Controls perimeters and Identity and Access Management (IAM) roles work together. VPC Service Controls enforces security boundaries around the service, while IAM governs who can access resources within the perimeter.

Even when access is within a protected perimeter, users or service accounts still require the [necessary IAM permissions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api#grant-required-roles) on both the Conversational Analytics API service and the underlying data sources (such as BigQuery datasets or Looker instances) to perform actions. Combining VPC Service Controls with proper IAM management is essential for robust security of your Conversational Analytics API workflows.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
