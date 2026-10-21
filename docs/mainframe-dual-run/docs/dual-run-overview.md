---
url: https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview/
title: Dual Run overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:14:11.391650+00:00
---

# Dual Run overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Dual Run ](https://docs.cloud.google.com/mainframe-dual-run/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview)



Send feedback 

#  Dual Run overview Stay organized with collections  Save and categorize content based on your preferences. 

Dual Run lets you simultaneously run workloads on your existing mainframes and on Google Cloud, and compare their behavior, allowing you to perform real-time testing and quickly gather data on performance and stability.

With Dual Run, you test, certify and de-risk mainframe applications that are being modernized with Google Cloud, ensuring correctness, completeness, and performance of the modernized application during the migration, and before going live.

## How Dual Run works

After you modernize your mainframe application on Google Cloud, you can use Dual Run to compare the output of your mainframe calculations, such as daily reports or database snapshots, with the output of your Google Cloud application. If the input of both systems is the same, so must be the output; if this is not the case, Dual Run lets you identify and analyze the differences, without disruption to your business.

With Dual Run, you can also use automation to replay actual, live events from the production mainframe system onto the modernized Google Cloud application. This lets you compare the outputs between the two systems, ensuring the correctness of the updated business logic within the modernized application.

When you're satisfied with the functional and nonfunctional performance equivalence of the two systems, you can switch to your new Google Cloud environment in production, and start decommissioning your mainframe.

Dual Run works for the following workload types:

  * **Batch workloads** , such as daily reports or database logs.
  * **Online transactions** (preview), such as bank transactions.



## Benefits of Dual Run

Dual Run offers the following benefits:

  * It lets you test your mainframe application without disrupting your business. You can thoroughly test and compare both applications before you build the necessary confidence in the functional equivalence of the two.
  * It lets you securely control your data. Only you and the users you authorize have access to the data stored in your Google Cloud project. Google has no access to your data.
  * It helps you accelerate your migration journey to Google Cloud by shortening the time required to test your application.
  * It lets you observe and compare the behavior of the two systems from a single pane of glass.



## What's next

Learn more about [Dual Run architecture for batch workloads](https://docs.cloud.google.com/mainframe-dual-run/docs/batch-architecture).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
