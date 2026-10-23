---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/authentication/
title: Authenticate to Access Approval \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:16.098735+00:00
---

# Authenticate to Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/authentication/

  * [ Reference ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/authentication)



#  Authenticate to Access Approval Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to authenticate to Access Approval programmatically. How you authenticate to Access Approval depends on the interface you use to access the API and the environment where your code is running. 

For more information about Google Cloud authentication, see the [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

## API access

Access Approval supports programmatic access. You can access the API in the following ways: 

  * Google Cloud CLI
  * REST



### Google Cloud CLI

When you use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/access-approval) to access Access Approval, you authenticate to Google Cloud as a principal, which provides the credentials used by the gcloud CLI commands. 

If your organization's security policies prevent user accounts from having the required permissions, you can use service account impersonation. 

For more information, see [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate). For more information about using the gcloud CLI with Access Approval, see [the gcloud CLI reference pages](https://docs.cloud.google.com/sdk/gcloud/reference/access-approval). 

### REST

You can authenticate to [the Access Approval API](https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest) by using your [gcloud CLI credentials](https://docs.cloud.google.com/sdk/docs/authenticate) or by using [ Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials). For more information about authentication for REST requests, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest). 

## Access control for Access Approval

After you authenticate to Access Approval, you must be authorized to access Google Cloud resources. Access Approval uses Identity and Access Management (IAM) for authorization. 

For more information about the roles for Access Approval, see [Access control with IAM](https://docs.cloud.google.com/assured-workloads/access-approval/docs/access-control). For more information about IAM and authorization, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview). 

## What's next

  * Learn about [Google Cloud authentication methods](https://docs.cloud.google.com/docs/authentication#auth-decision-tree). 
  * See a list of [authentication use cases](https://docs.cloud.google.com/docs/authentication/use-cases). 



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
