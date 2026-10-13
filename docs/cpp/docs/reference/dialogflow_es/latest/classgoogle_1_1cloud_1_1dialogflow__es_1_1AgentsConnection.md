---
url: https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es_1_1AgentsConnection/
title: Class AgentsConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:08.842025+00:00
---

# Class AgentsConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es_1_1AgentsConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class AgentsConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`AgentsConnection`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es_1_1AgentsConnection) object for [`AgentsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es_1_1AgentsClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`AgentsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es_1_1AgentsClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`AgentsClient`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es_1_1AgentsClient).

To create a concrete instance, see [`MakeAgentsConnection()`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/namespacegoogle_1_1cloud_1_1dialogflow__es).

For mocking, see [`dialogflow_es_mocks::MockAgentsConnection`](https://docs.cloud.google.com/cpp/docs/reference/dialogflow_es/latest/classgoogle_1_1cloud_1_1dialogflow__es__mocks_1_1MockAgentsConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual GetAgent(google::cloud::dialogflow::v2::GetAgentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::GetAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::dialogflow::v2::Agent >` |   
  
### virtual SetAgent(google::cloud::dialogflow::v2::SetAgentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::SetAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::dialogflow::v2::Agent >` |   
  
### virtual DeleteAgent(google::cloud::dialogflow::v2::DeleteAgentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::DeleteAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual SearchAgents(google::cloud::dialogflow::v2::SearchAgentsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::SearchAgentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::dialogflow::v2::Agent >` |   
  
### virtual TrainAgent(google::cloud::dialogflow::v2::TrainAgentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::TrainAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::protobuf::Struct > >` |   
  
### virtual TrainAgent(NoAwaitTag, google::cloud::dialogflow::v2::TrainAgentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::TrainAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual TrainAgent(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::protobuf::Struct > >` |   
  
### virtual ExportAgent(google::cloud::dialogflow::v2::ExportAgentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::ExportAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::ExportAgentResponse > >` |   
  
### virtual ExportAgent(NoAwaitTag, google::cloud::dialogflow::v2::ExportAgentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::ExportAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ExportAgent(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::dialogflow::v2::ExportAgentResponse > >` |   
  
### virtual ImportAgent(google::cloud::dialogflow::v2::ImportAgentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::ImportAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::protobuf::Struct > >` |   
  
### virtual ImportAgent(NoAwaitTag, google::cloud::dialogflow::v2::ImportAgentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::ImportAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ImportAgent(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::protobuf::Struct > >` |   
  
### virtual RestoreAgent(google::cloud::dialogflow::v2::RestoreAgentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::RestoreAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::protobuf::Struct > >` |   
  
### virtual RestoreAgent(NoAwaitTag, google::cloud::dialogflow::v2::RestoreAgentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::dialogflow::v2::RestoreAgentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RestoreAgent(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::protobuf::Struct > >` |   
  
### virtual GetValidationResult(google::cloud::dialogflow::v2::GetValidationResultRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dialogflow::v2::GetValidationResultRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::dialogflow::v2::ValidationResult >` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::location::Location >` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::location::Location >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
