---
url: https://docs.cloud.google.com/developer-connect/docs/authentication/
title: Authenticate to Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:33.903382+00:00
---

# Authenticate to Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Authenticate to Developer Connect Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to authenticate to Developer Connect programmatically. How you authenticate to Developer Connect depends on the interface you use to access the API and the environment where your code is running. 

For more information about Google Cloud authentication, see the [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

## API access

Developer Connect supports programmatic access. You can access the API in the following ways: 

  * Google Cloud CLI
  * REST



### Google Cloud CLI

When you use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference) to access Developer Connect, you authenticate to Google Cloud as a principal, which provides the credentials used by the gcloud CLI commands. 

If your organization's security policies prevent user accounts from having the required permissions, you can use service account impersonation. 

For more information, see [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate). For more information about using the gcloud CLI with Developer Connect, see [the gcloud CLI reference pages](https://docs.cloud.google.com/sdk/gcloud/reference). 

### REST

You can authenticate to [the Developer Connect API](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest) by using your [gcloud CLI credentials](https://docs.cloud.google.com/sdk/docs/authenticate) or by using [ Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials). For more information about authentication for REST requests, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest). 

## Access control for Developer Connect

After you authenticate to Developer Connect, you must be authorized to access Google Cloud resources. Developer Connect uses Identity and Access Management (IAM) for authorization. 

For more information about the roles for Developer Connect, see [Access control with IAM](https://docs.cloud.google.com/developer-connect/docs/access-control). For more information about IAM and authorization, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview). 

## What's next

  * Learn about [Google Cloud authentication methods](https://docs.cloud.google.com/docs/authentication#auth-decision-tree). 
  * See a list of [authentication use cases](https://docs.cloud.google.com/docs/authentication/use-cases). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
