---
url: https://docs.cloud.google.com/build/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:26:58.754710+00:00
---

# Security bulletins  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Support ](https://docs.cloud.google.com/build/docs/support)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes all security bulletins related to Cloud Build.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the [feed URL](https://docs.cloud.google.com/static/feeds/cloud-build-security-bulletins.xml) directly to your feed reader.



## GCP-2026-042

**Published:** 2026-06-24

### Description

Description | Severity | Notes  
---|---|---  
When you create or update repository connections, Cloud Build uses Secret Manager secrets to authenticate to third-party Git providers. For GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC) connections, these referenced secrets were previously retrieved by the Cloud Build service agent (P4SA) on your behalf. This meant that permission checks were performed against the P4SA's credentials rather than those of the calling principal. This could allow a principal with limited permissions to read referenced Secret Manager secrets by pointing the repository connection host URI to an attacker-controlled endpoint. To mitigate this vulnerability and adhere to the security principle of least privilege, Cloud Build now checks permissions against both the calling principal's credentials (using end-user credentials) and the P4SA when calling repository connection APIs for GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC) connections. Specifically, the server now verifies that both the caller and the P4SA possess the `secretmanager.versions.access` IAM permission on the referenced Secret Manager secrets. **What should I do?** No action is required for existing repository connections. If you encounter permission errors when creating or updating GitLab Enterprise (GLE) or Bitbucket Data Center (BBDC) repository connections, grant the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role on the referenced secrets to the user or service account creating or updating the connections. **What vulnerabilities are addressed by this patch?** This vulnerability allowed users with repository connection administrator access to read referenced Secret Manager secrets because the permission checks were only performed against the P4SA's credentials. By requiring permission checks against both the calling principal (using end-user credentials) and the P4SA for GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC) connections, only users authorized with the `secretmanager.versions.access` IAM permission on the secrets (in addition to the P4SA itself) can use them in repository connections. | Low |   
  
## GCP-2023-013

**Published:** 2023-06-08

### Description

Description | Severity | Notes  
---|---|---  
When you enable the Cloud Build API in a project, Cloud Build automatically creates a [default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) to execute builds on your behalf. This Cloud Build legacy service account previously had the `logging.privateLogEntries.list` IAM permission, which allowed the build to have access to list private logs by default. This permission has now been revoked from the Cloud Build service account to adhere to the [security principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege). **What should I do?** No further user action is required. The `logging.privateLogEntries.list` IAM permission has been revoked from the Cloud Build legacy service account and the fix has been rolled out. **What vulnerabilities are addressed by this patch?** This vulnerability granted builds the permission to list private logs. Since the `logging.privateLogEntries.list` IAM permission has now been revoked from the Cloud Build legacy service account, builds no longer have access to list private logs by default. | Low |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
