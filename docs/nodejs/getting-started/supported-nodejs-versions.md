---
url: https://docs.cloud.google.com/nodejs/getting-started/supported-nodejs-versions/
title: Supported Node.js versions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:05:04.075134+00:00
---

# Supported Node.js versions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/getting-started/supported-nodejs-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Guides ](https://docs.cloud.google.com/nodejs/docs/setup)



Send feedback 

#  Supported Node.js versions Stay organized with collections  Save and categorize content based on your preferences. 

This section provides an overview of how to keep your version of the Cloud Client Libraries for Node.js up-to-date with ongoing releases of Node.js. The Cloud Client Libraries for Node.js release schedule trails the Node.js release schedule.

## For new development

New feature development uses the Active LTS described in the Node.js release schedule. Node.js Client libraries are also tested against all Maintenance LTS versions.

When starting a new project, choose the current Active LTS. If this version is not yet available on your chosen runtime, a Maintenance LTS version should be your second choice.

**Note:** Be sure to use even-numbered Node.js releases. Avoid Node.js odd-numbered releases because they do not represent LTS candidates and become end-of-life after 6 months. 

## Keeping production systems current

Keeping your production systems on supported Node.js runtimes is the best way to ensure that you receive critical security and bug fixes. After a Node version goes end-of-life, the runtime will no longer receive critical updates.

Client libraries increment a major version when ending support for a Node.js runtime. An attempt is made to keep other breaking changes minimal. When a new major version of a library becomes available and ends support for your Node.js runtime, be sure to upgrade your runtime to a supported LTS version of Node.js, and upgrade your dependency. For more information, see [Semantic Versioning](https://semver.org/).

### Legacy support

Google's client libraries support legacy versions of Node.js runtimes on a best effort basis because it may not be possible to backport all patches. When possible, critical patches and bug fixes are released to prior major Node.js library versions.

### Where to find version information

The latest versions and supported Node.js versions for Google Cloud libraries appear in the individual GitHub repositories for client libraries. You can also find a table of libraries that interact with individual Google Cloud services on the [GitHub Google Cloud Client Library for Node.js](https://github.com/googleapis/google-cloud-node) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
