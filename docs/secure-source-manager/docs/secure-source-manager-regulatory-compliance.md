---
url: https://docs.cloud.google.com/secure-source-manager/docs/secure-source-manager-regulatory-compliance/
title: Regulatory support in Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:35.273398+00:00
---

# Regulatory support in Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/secure-source-manager-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/secure-source-manager/docs/resources)



Send feedback 

#  Regulatory support in Secure Source Manager Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Secure Source Manager that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for FedRAMP High  
  
---  
  
## Data Boundary for FedRAMP High

### Supported services

The following table lists the Secure Source Manager APIs and versions that meet the requirements of Data Boundary for FedRAMP High. | Service | Version | Status  
---|---|---  
securesourcemanager.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Secure Source Manager is available for Data Boundary for FedRAMP High in the following Google Cloud regions:

  * us-central1
  * us-east1



### API fields for sensitive data

#### Resource: securesourcemanager.googleapis.com/Instance

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `securesourcemanager.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/instances` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.ListInstances`

| 

  * `filter`
  * `orderBy`

  
  
#### Resource: securesourcemanager.googleapis.com/Issue

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `securesourcemanager.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/repositories/*}/issues` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.ListIssues`

| 

  * `filter`

  
Service: `securesourcemanager.googleapis.com` REST API: `PATCH` `/v1/{issue.name=projects/*/locations/*/repositories/*/issues/*}` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateIssue`

| 

  * `issue.body`
  * `issue.title`

  
Service: `securesourcemanager.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/repositories/*}/issues` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateIssue`

| 

  * `issue.body`
  * `issue.title`

  
  
#### Resource: securesourcemanager.googleapis.com/IssueComment

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `securesourcemanager.googleapis.com` REST API: `PATCH` `/v1/{issue_comment.name=projects/*/locations/*/repositories/*/issues/*/issueComments/*}` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateIssueComment`

| 

  * `issueComment.body`

  
Service: `securesourcemanager.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/repositories/*/issues/*}/issueComments` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateIssueComment`

| 

  * `issueComment.body`

  
  
#### Resource: securesourcemanager.googleapis.com/PullRequest

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `securesourcemanager.googleapis.com` REST API: `PATCH` `/v1/{pull_request.name=projects/*/locations/*/repositories/*/pullRequests/*}` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdatePullRequest`

| 

  * `pullRequest.base.ref`
  * `pullRequest.body`
  * `pullRequest.head.ref`
  * `pullRequest.title`

  
Service: `securesourcemanager.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/repositories/*}/pullRequests` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.CreatePullRequest`

| 

  * `pullRequest.base.ref`
  * `pullRequest.body`
  * `pullRequest.head.ref`
  * `pullRequest.title`

  
  
#### Resource: securesourcemanager.googleapis.com/PullRequestComment

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `securesourcemanager.googleapis.com` REST API: `PATCH` `/v1/{pull_request_comment.name=projects/*/locations/*/repositories/*/pullRequests/*/pullRequestComments/*}` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdatePullRequestComment`

| 

  * `pullRequestComment.code.body`
  * `pullRequestComment.code.position.path`
  * `pullRequestComment.comment.body`
  * `pullRequestComment.review.body`

  
Service: `securesourcemanager.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/repositories/*/pullRequests/*}/pullRequestComments` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.CreatePullRequestComment`

| 

  * `pullRequestComment.code.body`
  * `pullRequestComment.code.position.path`
  * `pullRequestComment.comment.body`
  * `pullRequestComment.review.body`

  
Service: `securesourcemanager.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/repositories/*/pullRequests/*}/pullRequestComments:batchCreate` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.BatchCreatePullRequestComments`

| 

  * `requests.pullRequestComment.code.body`
  * `requests.pullRequestComment.code.position.path`
  * `requests.pullRequestComment.comment.body`
  * `requests.pullRequestComment.review.body`

  
  
#### Resource: securesourcemanager.googleapis.com/Repository

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `securesourcemanager.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/repositories` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.ListRepositories`

| 

  * `filter`

  
Service: `securesourcemanager.googleapis.com` REST API: `PATCH` `/v1/{repository.name=projects/*/locations/*/repositories/*}` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateRepository`

| 

  * `repository.description`

  
Service: `securesourcemanager.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/repositories` RPC methods:

  * `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateRepository`

| 

  * `repository.description`

  
  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
