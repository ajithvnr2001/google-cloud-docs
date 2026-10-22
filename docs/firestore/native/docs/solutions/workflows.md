---
url: https://docs.cloud.google.com/firestore/native/docs/solutions/workflows/
title: Firestore connector for Workflows \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:43.283053+00:00
---

# Firestore connector for Workflows  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/solutions/workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Firestore connector for Workflows

[Workflows](https://docs.cloud.google.com/workflows/docs/overview) is a Google Cloud product you can use to create serverless workflows that link series of serverless tasks together in an order you define. Combine functionality from Google Cloud's APIs, serverless products like Cloud Run functions and Cloud Run, and calls to external APIs to create flexible serverless applications. 

## Example use case

**Automating low-latency shipment processing**

For example, the architecture below implements a workflow that checks whether a shipment can be executed based on inventory levels. It requests the shipment if the stock levels are sufficient. Otherwise, it requests replenishment from a supplier using their public API. In either case, the workflow immediately responds to the caller about whether the shipment transaction will be accepted.

![low-latency shipment processing diagram](https://cloudx-bricks-prod-bucket.storage.googleapis.com/d73aad6ed6ea3211307c6c72fb5590983959ac52744e9daddd580d5ea386ecf1.svg)

## Firestore connector for Workflows

Workflows supports a connector for Firestore. Use the connector to integrate Firestore into your workflows:

  * [Learn more about connectors.](https://docs.cloud.google.com/workflows/docs/connectors)
  * [See a sample workflow that uses Firestore.](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/Overview)



## What's next

  * [See the Workflows quickstarts.](https://docs.cloud.google.com/workflows/docs/quickstarts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
