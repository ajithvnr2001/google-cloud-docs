---
url: https://docs.cloud.google.com/web-risk/docs/lists/
title: Web Risk Lists \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:34.568476+00:00
---

# Web Risk Lists  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/lists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Guides ](https://docs.cloud.google.com/web-risk/docs/detect-malicious-urls)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Web Risk Lists

This document applies to the following methods:

  * [Lookup API](https://docs.cloud.google.com/web-risk/docs/lookup-api): [`uris.search`](https://docs.cloud.google.com/web-risk/docs/lookup-api#example-urissearch)
  * [Update API](https://docs.cloud.google.com/web-risk/docs/update-api): [`hashes.search`](https://docs.cloud.google.com/web-risk/docs/update-api#example-hashessearch)
  * [Update API](https://docs.cloud.google.com/web-risk/docs/update-api): [`threatLists:computeDiff`](https://docs.cloud.google.com/web-risk/docs/update-api#example-threatlistscomputeDiff)



## About the lists

The Web Risk lists also referred to as **threat lists** or simply **lists** are Google's constantly updated lists of unsafe web resources. Examples of unsafe web resources are social engineering sites like phishing and deceptive sites, and sites that host malware or unwanted software.

## Threat types

Each Web Risk list is named (identified) using a [`threatType`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/ThreatType).

## List contents

Currently, all Web Risk lists consist of variable length SHA 256 hashes between 4 and 32 bytes. These hashes are based on the suffix/prefix expressions of the URLs associated with unsafe web resources. Note that the URLs themselves are not stored in the Web Risk lists. For more information, see [URLs and Hashing](https://docs.cloud.google.com/web-risk/docs/urls-hashing).

When using the Lookup API to check URLs, the client sends the actual URL in the request and the Web Risk server converts the URL to a hash before performing the check. For additional details, see [Checking URLs](https://docs.cloud.google.com/web-risk/docs/lookup-api#checking-urls) for the Lookup API.

When using the Update API to check URLs, the client must convert the URL to a hash and then send the hash prefix in the request to perform the URL check. See [Checking URLs](https://docs.cloud.google.com/web-risk/docs/update-api#checking-urls) for more information about checking URLs with the Update API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
