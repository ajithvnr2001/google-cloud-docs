---
url: https://docs.cloud.google.com/artifact-analysis/docs/severity-levels/
title: Severity levels in Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:26.165716+00:00
---

# Severity levels in Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/severity-levels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Severity levels in Artifact Analysis Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how Artifact Analysis evaluates vulnerabilities and assigns severity levels.

Artifact Analysis rates vulnerability severity using the following levels:

  * Critical
  * High
  * Medium
  * Low



These severity levels are qualitative labels that reflect factors such as exploitability, scope, impact, and maturity of the vulnerability. For example, if a vulnerability enables a remote user to access a system and run arbitrary code without authentication or user interaction, that vulnerability would be classified as `Critical`.

Two additional types of severity are associated with each vulnerability:

  * Effective severity - Depending on the vulnerability type:

    * OS packages - The severity level assigned by the Linux distribution maintainer. If these severity levels are unavailable, Artifact Analysis uses the severity value from the note provider, [(NVD)](https://nvd.nist.gov/vuln-metrics). If NVD's CVSS v2 rating is unavailable, Artifact Analysis uses the CVSS v3 rating from NVD.
    * Language packages - The [severity level](https://docs.github.com/en/graphql/reference/enums#securityadvisoryseverity) assigned by the GitHub Advisory Database, with a slight difference: _Moderate_ is reported as _Medium_.
  * [CVSS score](https://www.first.org/cvss/v3.1/user-guide#Scoring-Guide) \- The Common Vulnerability Scoring System score and associated severity level, with two scoring versions:

    * [CVSS 2.0](https://www.first.org/cvss/v2/guide) \- Available when using the API, the Google Cloud CLI, and the GUI.
    * [CVSS 3.1](https://first.org/cvss/v3.1/user-guide) \- Available when using the API and the gcloud CLI.



## What's next

  * [Investigate vulnerabilities](https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities).
  * [Gate builds in your Cloud Build pipeline](https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild) based on vulnerability severity.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
