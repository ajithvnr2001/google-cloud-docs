---
url: https://docs.cloud.google.com/integration-connectors/docs/connector-glossary/
title: Glossary \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:59:34.147977+00:00
---

# Glossary  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connector-glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Reference ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Glossary

This page provides brief definitions and links to more information for terms frequently used in the connectors documentation. 

**Action**

A first class function that is made available to an integration through the Connector interface. "Action" functions are defined in the connected application or service and define a change or series of changes that can be made to an entity or entities.

**Authentication**

Each connector type defines a set of available authentication methods that may be used to connect to the target application. Authentications are stored separately from the connector so that users can select from available authentication objects when creating a connection instance.

**Connection**

A configuration or instance of a Connector. A connection contains user-specified details, such as the URL of the target application, and may include specific service-account credentials or authentication parameters to use when connecting to that specific instance of an application or technology. Connections are designed to be reusable, so that any customizations applied may be shared and consumed by multiple users.

**Connector**

A specific type of _connection_ , defined by a number of attributes, including: 

  * A set of possible authentication methods
  * A unique (or templatized) data schema
  * A set of configuration parameters
  * A list of available methods, data types, operations, events, and objects
  * An author (person + company)
  * A "type" (for example, _table_ , _file store_ , _messaging service_ , etc.)

**Entity**

An object, or a collection of properties, in the connected application or service, that can be exposed to an integration through the Connector interface.

**Version**

A resource that represents a single version of a Connector and its associated attributes, such as its available methods, data schema, and authentication options. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
