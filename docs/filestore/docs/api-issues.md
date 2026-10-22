---
url: https://docs.cloud.google.com/filestore/docs/api-issues/
title: Troubleshoot Filestore API response errors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:44.691573+00:00
---

# Troubleshoot Filestore API response errors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/api-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Troubleshoot Filestore API response errors Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting information to help address issues you might encounter while using the Filestore API.

## Filestore API cannot be disabled

Make sure that all of your Filestore related resources, such as Filestore instances and backups, are deleted. You cannot disable the Filestore API while Filestore instances are deployed.

## Failed to create a subnetwork

For a given private connection, if you exhaust your allocated IP address space, Google Cloud returns this error: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges.`

For details on how to resolve this issue, see [IP address range exhaustion](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modify-ip-range).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
