---
url: https://docs.cloud.google.com/bare-metal/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:11.254767+00:00
---

# Security bulletins  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/security-bulletins/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Resources ](https://docs.cloud.google.com/bare-metal/docs/resource)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security bulletins

From time to time, we might release security bulletins related to Bare Metal Solution. All security bulletins for Bare Metal Solution are described here.

[ Use this XML feed to subscribe to security bulletins for this page. ![Subscribe](https://docs.cloud.google.com/static/docs/images/feed-icon.png)](https://cloud.google.com/feeds/bare-metal-solution-security-bulletins.xml)

## GCP-2024-040

**Published:** 2024-07-02

Description | Severity | Notes  
---|---|---  
A vulnerability CVE-2024-6387 was discovered in OpenSSH server (sshd). This vulnerability is exploitable remotely on glibc-based linux systems: an unauthenticated remote code execution as root, because it affects sshd's privileged code, which is not sandboxed and runs with full privileges.   
  
At the time of publication, exploitation is believed to be difficult–requiring winning a race condition, which is hard to successfully exploit and may take several hours per machine being attacked. 

#### Bare Metal Solution impact

Based on our investigations, we are not aware of any exploitation attempts on existing Google managed Bare Metal Solution infrastructure. 

#### What should I do?

  1. We recommend updating to the safe OpenSSH version 9.8p1 once it is released, or applying sshd patches once provided by OS vendors. 
  2. We also recommend disabling/removing vulnerable OpenSSH server wherever it is not required. 
  3. Setup firewall rules to restrict access to SSH servers from trusted network endpoints. 
  4. Monitor for any unusual network activity involving SSH servers. 

| Critical | 

  * [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
