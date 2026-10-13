---
url: https://docs.cloud.google.com/cpp/docs/reference/securesourcemanager/latest/classgoogle_1_1cloud_1_1securesourcemanager__v1_1_1SecureSourceManagerConnectionIdempotencyPolicy/
title: Class SecureSourceManagerConnectionIdempotencyPolicy (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:02.653088+00:00
---

# Class SecureSourceManagerConnectionIdempotencyPolicy (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/securesourcemanager/latest/classgoogle_1_1cloud_1_1securesourcemanager__v1_1_1SecureSourceManagerConnectionIdempotencyPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class SecureSourceManagerConnectionIdempotencyPolicy (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0 

## Functions 

### virtual clone() const

Create a new copy of this object. 

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< SecureSourceManagerConnectionIdempotencyPolicy >` |   
  
### virtual ListInstances(google::cloud::securesourcemanager::v1::ListInstancesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListInstancesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetInstance(google::cloud::securesourcemanager::v1::GetInstanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::GetInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateInstance(google::cloud::securesourcemanager::v1::CreateInstanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CreateInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteInstance(google::cloud::securesourcemanager::v1::DeleteInstanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::DeleteInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListRepositories(google::cloud::securesourcemanager::v1::ListRepositoriesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListRepositoriesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetRepository(google::cloud::securesourcemanager::v1::GetRepositoryRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::GetRepositoryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateRepository(google::cloud::securesourcemanager::v1::CreateRepositoryRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CreateRepositoryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateRepository(google::cloud::securesourcemanager::v1::UpdateRepositoryRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::UpdateRepositoryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteRepository(google::cloud::securesourcemanager::v1::DeleteRepositoryRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::DeleteRepositoryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListHooks(google::cloud::securesourcemanager::v1::ListHooksRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListHooksRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetHook(google::cloud::securesourcemanager::v1::GetHookRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::GetHookRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateHook(google::cloud::securesourcemanager::v1::CreateHookRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CreateHookRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateHook(google::cloud::securesourcemanager::v1::UpdateHookRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::UpdateHookRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteHook(google::cloud::securesourcemanager::v1::DeleteHookRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::DeleteHookRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetIamPolicyRepo(google::iam::v1::GetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual SetIamPolicyRepo(google::iam::v1::SetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual TestIamPermissionsRepo(google::iam::v1::TestIamPermissionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateBranchRule(google::cloud::securesourcemanager::v1::CreateBranchRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CreateBranchRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListBranchRules(google::cloud::securesourcemanager::v1::ListBranchRulesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListBranchRulesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetBranchRule(google::cloud::securesourcemanager::v1::GetBranchRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::GetBranchRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateBranchRule(google::cloud::securesourcemanager::v1::UpdateBranchRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::UpdateBranchRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteBranchRule(google::cloud::securesourcemanager::v1::DeleteBranchRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::DeleteBranchRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreatePullRequest(google::cloud::securesourcemanager::v1::CreatePullRequestRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CreatePullRequestRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetPullRequest(google::cloud::securesourcemanager::v1::GetPullRequestRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::GetPullRequestRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListPullRequests(google::cloud::securesourcemanager::v1::ListPullRequestsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListPullRequestsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdatePullRequest(google::cloud::securesourcemanager::v1::UpdatePullRequestRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::UpdatePullRequestRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual MergePullRequest(google::cloud::securesourcemanager::v1::MergePullRequestRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::MergePullRequestRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual OpenPullRequest(google::cloud::securesourcemanager::v1::OpenPullRequestRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::OpenPullRequestRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ClosePullRequest(google::cloud::securesourcemanager::v1::ClosePullRequestRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ClosePullRequestRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListPullRequestFileDiffs(google::cloud::securesourcemanager::v1::ListPullRequestFileDiffsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListPullRequestFileDiffsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual FetchTree(google::cloud::securesourcemanager::v1::FetchTreeRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::FetchTreeRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual FetchBlob(google::cloud::securesourcemanager::v1::FetchBlobRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::FetchBlobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual FetchRefs(google::cloud::securesourcemanager::v1::FetchRefsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::FetchRefsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateIssue(google::cloud::securesourcemanager::v1::CreateIssueRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CreateIssueRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetIssue(google::cloud::securesourcemanager::v1::GetIssueRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::GetIssueRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListIssues(google::cloud::securesourcemanager::v1::ListIssuesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListIssuesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateIssue(google::cloud::securesourcemanager::v1::UpdateIssueRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::UpdateIssueRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteIssue(google::cloud::securesourcemanager::v1::DeleteIssueRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::DeleteIssueRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual OpenIssue(google::cloud::securesourcemanager::v1::OpenIssueRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::OpenIssueRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CloseIssue(google::cloud::securesourcemanager::v1::CloseIssueRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CloseIssueRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetPullRequestComment(google::cloud::securesourcemanager::v1::GetPullRequestCommentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::GetPullRequestCommentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListPullRequestComments(google::cloud::securesourcemanager::v1::ListPullRequestCommentsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListPullRequestCommentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreatePullRequestComment(google::cloud::securesourcemanager::v1::CreatePullRequestCommentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CreatePullRequestCommentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdatePullRequestComment(google::cloud::securesourcemanager::v1::UpdatePullRequestCommentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::UpdatePullRequestCommentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeletePullRequestComment(google::cloud::securesourcemanager::v1::DeletePullRequestCommentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::DeletePullRequestCommentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual BatchCreatePullRequestComments(google::cloud::securesourcemanager::v1::BatchCreatePullRequestCommentsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::BatchCreatePullRequestCommentsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ResolvePullRequestComments(google::cloud::securesourcemanager::v1::ResolvePullRequestCommentsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ResolvePullRequestCommentsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UnresolvePullRequestComments(google::cloud::securesourcemanager::v1::UnresolvePullRequestCommentsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::UnresolvePullRequestCommentsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateIssueComment(google::cloud::securesourcemanager::v1::CreateIssueCommentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::CreateIssueCommentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetIssueComment(google::cloud::securesourcemanager::v1::GetIssueCommentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::GetIssueCommentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListIssueComments(google::cloud::securesourcemanager::v1::ListIssueCommentsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::ListIssueCommentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateIssueComment(google::cloud::securesourcemanager::v1::UpdateIssueCommentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::UpdateIssueCommentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteIssueComment(google::cloud::securesourcemanager::v1::DeleteIssueCommentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::securesourcemanager::v1::DeleteIssueCommentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
