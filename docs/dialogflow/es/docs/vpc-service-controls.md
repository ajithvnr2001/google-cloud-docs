---
url: https://docs.cloud.google.com/dialogflow/es/docs/vpc-service-controls/
title: Using VPC Service Controls \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:48.273241+00:00
---

# Using VPC Service Controls  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Using VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) can help you mitigate the risk of data exfiltration from Dialogflow. Use VPC Service Controls to create a _service perimeter_ that protects the resources and data that you specify. For example, when you use VPC Service Controls to protect Dialogflow, the following artifacts cannot leave your service perimeter:

  * Agent data
  * Detect intent requests and responses



## Limitations

The following limitations apply:

  * [Integrations](https://docs.cloud.google.com/dialogflow/es/docs/integrations) let third-party applications directly connect to Agents regardless of if the Agent is within a service perimeter.
  * [Service Directory](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview) is not supported.
  * When VPC Service Controls is enabled, [webhook](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook) calls are blocked.



## Service perimeter creation

A service perimeter acts as a virtual security boundary that isolates your Google Cloud resources. This ensures that sensitive data cannot be moved to unauthorized locations outside the perimeter. Services within the boundary can communicate freely, while access to or from resources external to that boundary is blocked.

When you create a service perimeter, include Dialogflow (`dialogflow.googleapis.com`) as a protected service. Include any services that you want to restrict (for example, `storage.googleapis.com`, `bigquery.googleapis.com`) under the **Restricted services** pane.

For more information about creating a service perimeter, see [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) in the VPC Service Controls documentation.

[ Previous arrow_back  Using multiple projects  ](https://docs.cloud.google.com/dialogflow/es/docs/multi-project)

[ Next Data application levels  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/data-level)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
