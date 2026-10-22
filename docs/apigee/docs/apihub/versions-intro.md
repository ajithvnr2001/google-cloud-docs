---
url: https://docs.cloud.google.com/apigee/docs/apihub/versions-intro/
title: Versions overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:06.285642+00:00
---

# Versions overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/versions-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Versions overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

Every API resource in API hub has at least one version associated with it. You can think of a version as the state of an API at a point in time. Fundamentally, versions help you group and organize your APIs based on underlying sets of operations or tools, deployments, specifications, and other attributes. 

In API hub, a version represents a logical grouping. For a REST API, this grouping usually revolves around the operations it can perform. For example, the first version of a Pet Store API might let you perform basic tasks like adding a pet, finding a pet, and deleting a pet from the store. For an agentic API using the Model Context Protocol (MCP), a version would be grouped around a set of tools that an AI agent can use. 

It's a good practice for a version to include a set of API operations or tools that are deployed together. For example, a pet store API might have a version that includes add, find, and delete functions, all deployed to the same environments. 

## Creating versions

If the details of an API you want to add to API hub are captured in a specification file, you can [add the spec to an API version](https://docs.cloud.google.com/apigee/docs/apihub/manage-specifications#addspec). When you do, API hub parses the spec and pulls information out of it. 

  * For a REST API, API hub parses an OpenAPI spec and uses it to populate the version with the operations the API includes. 
  * For an MCP API, API hub parses an MCP Schema file to extract its tools



If you don't have a supported specification file, you can still [create a version](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions#addversion), but you'll have to populate it manually with relevant descriptive information. Another case where API hub supports automatic parsing of API details is through the [auto-registration of Apigee API proxies](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies). 

### When to create a new version?

If new operations or tools are added to an API, it may warrant creating a new version, but not always. 

Let's say the API producer adds a new function to an API and intends for it to be deployed to all of the deployments currently associated with the version. In that case, the producer may choose not to create a new version of the API. On the other hand, if the producer makes a backwardly incompatible change (a breaking change) and chooses to associate it with a new deployment, you may wish to create a new version. 

You can see that API hub provides flexibility for you to define and organize your API versions to best suit your organization's needs and the needs of specific API producers. 

## What's next

  * Learn how to [manage versions](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions).
  * Learn how to [manage API resources](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
