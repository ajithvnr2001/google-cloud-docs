---
url: https://docs.cloud.google.com/filestore/docs/delete-data/
title: Delete data from a file share \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:24.894172+00:00
---

# Delete data from a file share  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/delete-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Delete data from a file share Stay organized with collections  Save and categorize content based on your preferences. 

After you mount a Filestore file share on a client VM, you can interact with it like any other local file system, using standard file system commands.

When you delete files or directories from a Filestore file share, the operation completes immediately, but space reclamation happens in the background and takes some time, especially when you delete large amounts of data.

Before you add new data, make sure enough disk space is reclaimed. Monitor the **Free raw capacity percent** and **Free disk space percent** metrics for your instance:

  1. Go to the Filestore instances page: [Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID to open the instance details page.

  3. Go to the **Observability** tab and explore metrics.




Alternatively, use the metrics explorer to view metrics and create dashboards. For more information, see [Monitoring instances and quota](https://docs.cloud.google.com/filestore/docs/monitoring-instances#add-metric-chart).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
