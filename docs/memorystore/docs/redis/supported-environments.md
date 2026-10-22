---
url: https://docs.cloud.google.com/memorystore/docs/redis/supported-environments/
title: Supported environments \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:02.791211+00:00
---

# Supported environments  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/supported-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Supported environments Stay organized with collections  Save and categorize content based on your preferences. 

This page describes which Google Cloud environments are supported for Memorystore for Redis. It also shows which requirements are necessary for connectivity, given different environments and networking setups.

## All supported environments for Memorystore for Redis

#### Environments that do not need a Serverless VPC Access connector

  * [Compute Engine](https://docs.cloud.google.com/compute/docs)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible)



#### Serverless environments that need a Serverless VPC Access connector

  * [Cloud Run functions](https://docs.cloud.google.com/functions/docs)
  * [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard)
  * [Cloud Run](https://docs.cloud.google.com/run/docs)



## Capabilities and requirements

Environment  |  Requires a Serverless VPC Access connector.1 |  Supports Shared VPC when Redis instance is provisioned in the _host project_ and a private service access connection is established. 2 |  Supports Shared VPC when Redis instance is provisioned in the _service project_ and a private service access connection is established. 2  
---|---|---|---  
Compute Engine  |  X  |  ✓  |  ✓   
Google Kubernetes Engine  |  X  |  ✓  |  ✓   
App Engine flexible environment  |  X  |  ✓  |  X   
App Engine standard environment  |  ✓  |  ✓  |  X   
Cloud Run functions  |  ✓  |  ✓  |  X   
Cloud Run  |  ✓  |  ✓  |  ✓   
  
1 Some of the serverless environments listed above require a Serverless VPC Access connector. See [Serverless VPC Access connector requirement](https://docs.cloud.google.com/memorystore/docs/redis/supported-environments#serverless-vpc-access-connector-requirement) for more details.

2 See [Networking](https://docs.cloud.google.com/memorystore/docs/redis/networking) for more details.

## Serverless VPC Access connector requirement

Some serverless environments require a Serverless VPC Access connector as a prerequisite for connectivity with Memorystore for Redis. The serverless environments that need the connector are Cloud Run functions, the App Engine standard environment, and Cloud Run.

More details and connector setup instructions for these environments are found below:

  * Cloud Run functions: [Compare Direct VPC egress and VPC connectors](https://docs.cloud.google.com/functions/docs/connecting-vpc).
  * App Engine standard environment: [Connect to a VPC network](https://docs.cloud.google.com/appengine/docs/standard/python/connecting-vpc#creating_a_connector).
  * Cloud Run: [Compare Direct VPC egress and VPC connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
