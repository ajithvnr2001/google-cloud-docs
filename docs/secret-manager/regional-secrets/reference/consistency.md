---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/reference/consistency/
title: Resource consistency \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:07.898538+00:00
---

# Resource consistency  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/reference/consistency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)



Send feedback 

#  Resource consistency Stay organized with collections  Save and categorize content based on your preferences. 

In Secret Manager, adding a secret version and then immediately accessing that secret version by version number is a strongly consistent operation.

**Note:** This doesn't apply when you access a secret version using `aliases` or `latest`.

Other operations within Secret Manager are eventually consistent. Eventually consistent operations typically converge within minutes, but may take a few hours.

Propagating IAM permissions is eventually consistent. This means granting or revoking access to secrets may not take effect immediately. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
