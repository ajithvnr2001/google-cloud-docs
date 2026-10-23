---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/preview-data/
title: Preview data \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:17.899910+00:00
---

# Preview data  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/preview-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Preview data Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to preview data in the Cloud Data Fusion Studio so that you can debug errors before you deploy and run a pipeline.

If you encounter errors, you can fix them while your pipeline is still in Draft mode.

Cloud Data Fusion uses the first 100 rows of your source dataset to generate the preview.

In _Preview_ mode, the **Studio** page displays the status and duration of the preview job. You can stop the preview job at any time. You can also monitor the log events as the preview job runs.

**Note:** Actions and post-run actions are ignored when running a preview. To preview data, follow these steps:

### Console

  1. Check that each source, transformation, and sink has no errors. To validate them, on the Cloud Data Fusion **Studio** page, go to the node for each plugin and click **Properties** > **Validate**.
  2. View your pipeline on the **Studio** page and click the **Preview** toggle to the on position. **Run** , **Duration** , and **Logs** options appear at the top of the **Studio** page canvas.
  3. Optional: before you run the preview job, update the following settings by clicking **Configure**.

     1. **Runtime arguments** : for more information see [Set up runtime arguments](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-macros-prefs-and-runtime-args#set-up-runtime-arguments).
     2. **Preview config** : update the number of rows to preview.
     3. **Advanced options** : update the pipeline and engine configurations. For more information, see [Manage pipeline configurations](https://docs.cloud.google.com/data-fusion/docs/concepts/manage-pipeline-configurations).
  4. To start the preview job, click **Run**. When the preview job runs, no data is written to the sink, but you can check that data is read and written as expected when you deploy the pipeline.

  5. Optional: after you run the preview job, to see what your data looks like at each stage in the pipeline, click **Preview data** on nodes in the pipeline that handle data, such as sources, sinks, and transformations.

  6. When you're finished previewing the data, exit Preview mode by clicking the **Preview** toggle to the off position.




## What's next

  * Learn how to [create pipeline alerts](https://docs.cloud.google.com/data-fusion/docs/how-to/create-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
