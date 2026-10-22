---
url: https://docs.cloud.google.com/memorystore/docs/valkey/supported-environments/
title: Supported environments \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:27.700581+00:00
---

# Supported environments  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/supported-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Supported environments Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Google Cloud environments that Memorystore for Valkey supports. It also shows which requirements are necessary for connectivity, given that there are different environments and networking setups.

## All supported environments

The following serverless environments don't need a Serverless VPC Access connector:

  * [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible)
  * [Compute Engine](https://docs.cloud.google.com/compute/docs)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)



The following serverless environments need this connector:

  * [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard)
  * [Cloud Run](https://docs.cloud.google.com/run/docs)
  * [Cloud Run functions](https://docs.cloud.google.com/functions/docs)



## Capabilities and requirements

The table in this section lists the following information:

  * The environments that need a Serverless VPC Access connector
  * The environments that support Shared VPC when an instance is provisioned in the _host_ project
  * The environments that support Shared VPC when the instance is provisioned in the _service_ project

Environment  |  Requires a Serverless VPC Access connector1 |  Supports Shared VPC when the instance is provisioned in the host project and a connection is established that uses Private Service Connect 2 |  Supports Shared VPC when the instance is provisioned in the service project and a connection is established that uses Private Service Connect 2  
---|---|---|---  
App Engine flexible environment  |  X  |  ✓  |  X   
Compute Engine  |  X  |  ✓  |  ✓   
Google Kubernetes Engine  |  X  |  ✓  |  ✓   
App Engine standard environment  |  ✓  |  ✓  |  X   
Cloud Run  |  ✓  |  ✓  |  ✓   
Cloud Run functions  |  ✓  |  ✓  |  X   
  
1 Some of the serverless environments listed in this section require a Serverless VPC Access connector. For more information, see Serverless VPC Access connector requirements.

2 For more information, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

## Serverless VPC Access connector requirements

To connect to Memorystore for Valkey, some serverless environments require a Serverless VPC Access connector. These environments are App Engine standard environment, Cloud Run, and Cloud Run functions.

For more information and connector setup instructions for these environments, use the following links:

  * App Engine standard environment: [Connecting to a VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc)
  * Cloud Run: [Compare Direct VPC egress and VPC connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc)
  * Cloud Run functions: [Connecting to a VPC network](https://docs.cloud.google.com/functions/docs/connecting-vpc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
