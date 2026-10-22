---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/permissions/
title: Permissions and roles \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:34.428351+00:00
---

# Permissions and roles  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Permissions and roles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the permissions and roles that are required to use and configure Blockchain Node Engine.

The blockchain nodes themselves expose an API endpoint. Google does not define this API, but is part of the third party software we run. You can see an example of this at [Ethereum's JSON-RPC Server](https://geth.ethereum.org/docs/rpc/server). This endpoint requires an API key to access. API keys are managed in Google Cloud, and as such use the permissions defined on [Access control with IAM](https://docs.cloud.google.com/api-keys/docs/access-control). These permissions have been added to the admin role.

## Roles

This section lists all curated roles provided by Blockchain Node Engine service.

### Viewer

Grants read access to all Blockchain Node Engine resources. Intended for engineers who use but do not manage nodes. API keys are expected to be provided from an admin. The viewer does not have direct access to look up API keys.

[Blockchain Node Engine actions](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest):

  * `blockchainnodeengine.googleapis.com/blockchainNodes.get`
  * `blockchainnodeengine.googleapis.com/blockchainNodes.list`
  * `blockchainnodeengine.googleapis.com/locations.get`
  * `blockchainnodeengine.googleapis.com/locations.list`
  * `blockchainnodeengine.googleapis.com/operations.get`
  * `blockchainnodeengine.googleapis.com/operations.list`



[Retrieve project information](https://docs.cloud.google.com/resource-manager/reference/rest):

  * `cloudresourcemanager.googleapis.com/projects.get`
  * `cloudresourcemanager.googleapis.com/projects.list`



[Return APIs information](https://docs.cloud.google.com/service-usage/docs/reference/rest):

  * `serviceusage.googleapis.com/services.get`



### Admin

Grants full access to all Blockchain Node Engine resources. Intended for blockchain node administrators.

Administrators have all permissions available to `blockchainnodeengine.googleapis.com/viewer` plus:

[API keys management](https://docs.cloud.google.com/api-keys/docs/reference/rest):

  * `apikeys.googleapis.com/keys.update`
  * `apikeys.googleapis.com/keys.create`
  * `apikeys.googleapis.com/keys.delete`
  * `apikeys.googleapis.com/keys.get`
  * `apikeys.googleapis.com/keys.getKeyString`
  * `apikeys.googleapis.com/keys.list`
  * `apikeys.googleapis.com/keys.undelete`



[Blockchain Node Engine actions](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest):

  * `blockchainnodeengine.googleapis.com/blockchainNodes.create`
  * `blockchainnodeengine.googleapis.com/blockchainNodes.delete`
  * `blockchainnodeengine.googleapis.com/operations.cancel`
  * `blockchainnodeengine.googleapis.com/operations.delete`



[Enable APIs](https://docs.cloud.google.com/service-usage/docs/reference/rest):

  * `serviceusage.googleapis.com/services.enable`



## See also

  * [Access control with IAM - API keys](https://docs.cloud.google.com/api-keys/docs/access-control)
  * [Access Control with IAM - Service usage](https://docs.cloud.google.com/service-usage/docs/access-control)
  * [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles)
  * [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference)
  * [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)
  * [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
