---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/vpc-service-controls/
title: Using VPC Service Controls \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:51.642649+00:00
---

# Using VPC Service Controls  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/vpc-service-controls/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Using VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) can help you mitigate the risk of data exfiltration from Dialogflow. Use VPC Service Controls to create a _service perimeter_ that protects the resources and data that you specify. For example, when you use VPC Service Controls to protect Dialogflow, the following artifacts cannot leave your service perimeter:

  * Agent data
  * Detect intent requests and responses



## Limitations

The following limitations apply:

  * [Integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) let third-party applications directly connect to Agents regardless of if the Agent is within a service perimeter.
  * Webhooks can be used to directly connect to a Cloud Function or Cloud Run endpoint within the same service perimeter as the Agent
  * Webhooks can be used to connect to services integrated with [Service Directory private network access](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#sd)



Any other type of webhook service is not supported and will be blocked.

## Service perimeter creation

A service perimeter acts as a virtual security boundary that isolates your Google Cloud resources. This ensures that sensitive data cannot be moved to unauthorized locations outside the perimeter. Services within the boundary can communicate freely, while access to or from resources external to that boundary is blocked.

When you create a service perimeter, include Dialogflow (`dialogflow.googleapis.com`) as a protected service. Include any services that you want to restrict (for example, `storage.googleapis.com`, `bigquery.googleapis.com`) under the **Restricted services** pane.

For more information about creating a service perimeter, see [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) in the VPC Service Controls documentation.

[ Previous arrow_back  Security settings  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings)

[ Next Mutual TLS authentication  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/mtls)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
