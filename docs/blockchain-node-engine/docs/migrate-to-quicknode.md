---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/migrate-to-quicknode/
title: Migrate to Quicknode before Dec 15, 2026 \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:12.249727+00:00
---

# Migrate to Quicknode before Dec 15, 2026  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/migrate-to-quicknode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/blockchain-node-engine/docs/resources)



Send feedback 

#  Migrate to Quicknode before Dec 15, 2026 Stay organized with collections  Save and categorize content based on your preferences. 

Blockchain Node Engine and Blockchain RPC will be shut down on December 15, 2026.

Google Cloud has partnered with **Quicknode** to serve as the recommended RPC infrastructure provider for our customers moving forward. Quicknode is designed to meet your specific node and RPC requirements without any service disruption.

To migrate, complete the following steps:

  1. **Provision nodes or endpoints** : Provision your required nodes or endpoints directly through [Quicknode's Marketplace](https://console.cloud.google.com/marketplace/product/quicknode-public/core-node-api) offering. This option includes incentives available in Google Cloud. Contact your sales representative for details. Alternatively, you can provision the nodes and endpoints directly through the [Quicknode platform](https://www.quicknode.com/gcp-node-migration).
  2. **Update configurations** : Update your applications and services to point to the new Quicknode endpoints before the shutdown date.
  3. **Validate workloads** : Test and verify that your workloads function correctly on the new infrastructure.
  4. **Decommission legacy resources** : [Delete your legacy Blockchain Node Engine nodes](https://docs.cloud.google.com/blockchain-node-engine/docs/delete-node) within the Google Cloud console. Blockchain RPC endpoints will be deleted by Google for you on December 15, 2026.



For more information on the deprecation timeline, see the [release notes](https://docs.cloud.google.com/blockchain-node-engine/docs/release-notes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
