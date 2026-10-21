---
url: https://docs.cloud.google.com/application-integration/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:18.171566+00:00
---

# Security bulletins  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Resources ](https://docs.cloud.google.com/application-integration/docs/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security bulletins

The following describes all security bulletins related to Application Integration.

## GCP-2026-068

**Published:** 2026-10-15

Description | Severity | Notes  
---|---|---  
Starting October 15, 2026, Application Integration requires `iam.serviceAccounts.actAs` on the run-as service account.

#### What should I do?

After October 15, 2026, the test feature and any new integrations require the correct permissions. Existing integrations and their new versions are unaffected. For more information, see [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes).

#### What vulnerabilities are being addressed?

An Incorrect Authorization vulnerability in the `AuthConfig` validation and integration execution runtime could allow an authenticated user to escalate privileges and impersonate a service account. | High |  [CVE-2026-85298](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-85298)  
  
## GCP-2026-067

**Published:** 2026-10-14

### Description

Description | Severity | Notes  
---|---|---  
An Incorrect Authorization vulnerability in the `AuthConfig` validation and integration execution runtime in Application Integration versions prior to August 27, 2026.

#### What should I do?

No customer action is required. This vulnerability was patched on August 27, 2026.

#### What vulnerabilities are being addressed?

An authenticated user could escalate privileges and impersonate a service account in the Google Cloud project. | High |  [CVE-2026-85298](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-85298)  
  
## GCP-2026-066

**Published:** 2026-09-28

Description | Severity | Notes  
---|---|---  
A Confused Deputy vulnerability was discovered in the Email Task component in Application Integration versions prior to June 30, 2026.

#### What should I do?

No customer action is required. This vulnerability was patched on June 30, 2026.

#### What vulnerabilities are being addressed?

An authenticated attacker could read and exfiltrate arbitrary Google-internal files using a crafted attachment path. | High |  [CVE-2026-81375](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-81375)  
  
## GCP-2026-065

**Published:** 2026-09-28

Description | Severity | Notes  
---|---|---  
A Deserialization of Untrusted Data vulnerability was discovered in the JavaScript Task in Application Integration versions prior to June 28, 2026.

#### What should I do?

No customer action is required. This vulnerability was patched on June 28, 2026.

#### What vulnerabilities are being addressed?

An authenticated user with standard permissions could use a specially crafted script to run arbitrary code on the shared production servers. | Critical |  [CVE-2026-81867](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-81867)  
  
## GCP-2026-064

**Published:** 2026-09-28

Description | Severity | Notes  
---|---|---  
An Incorrect Authorization vulnerability was discovered in the task configuration in Application Integration versions prior to June 17, 2026.

#### What should I do?

No customer action is required. This vulnerability was patched on June 17, 2026.

#### What vulnerabilities are being addressed?

An authenticated user could use an internal-only task type to execute arbitrary internal RPCs from the Google-internal production network under a privileged identity. | Critical |  [CVE-2026-19759](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-19759)  
  
## GCP-2026-044

**Published:** 2026-06-25

Description | Severity | Notes  
---|---|---  
A vulnerability was detected in Application Integration's JavaScript task, which was using the Rhino JavaScript engine. This only impacted tasks published before January 2025.

#### What should I do?

Google has transitioned to the more secure V8 JavaScript engine for JavaScript tasks in Application Integration. Since January 2025, all newly published integrations use the V8 engine, and as of March 30, 2026, the Rhino engine has been fully deprecated. Executions using the Rhino engine are also now blocked.  If you have integrations published before January 2025, review your JavaScript tasks to confirm none still rely on the Rhino engine. Any task still configured to use Rhino will no longer execute and must be migrated to the V8 engine. For migration steps, see [Migrate JavaScript tasks](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task#javascript-execution-engine).

#### What vulnerabilities are being addressed?

The vulnerability, CVE-2025-0982, allowed a user with authorization to author and run JavaScript tasks to execute arbitrary code within the Application Integration execution environment. The JavaScript task previously used the Rhino JavaScript engine to run user-supplied JavaScript. Rhino permitted the use of Java reflection and the modification of in-memory permission objects, which could be combined to bypass the Java security manager and escape the intended execution sandbox. Google remediated this by moving to the V8 JavaScript engine in January 2025 and fully deprecating and blocking the Rhino engine on March 30, 2026. | High |  [CVE-2025-0982](https://www.cve.org/CVERecord?id=CVE-2025-0982)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
