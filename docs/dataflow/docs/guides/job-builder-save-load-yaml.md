---
url: https://docs.cloud.google.com/dataflow/docs/guides/job-builder-save-load-yaml/
title: Save and load YAML job definitions with the job builder \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:17.532371+00:00
---

# Save and load YAML job definitions with the job builder  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/job-builder-save-load-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Save and load YAML job definitions with the job builder Stay organized with collections  Save and categorize content based on your preferences. 

You can save job builder jobs as [Apache Beam YAML](https://beam.apache.org/documentation/sdks/yaml/) files that encapsulate the job's configuration. These YAML files can be loaded back into the job builder for reuse and further editing.

## Save a pipeline

To save a pipeline to Beam YAML:

  1. Use the job builder to [create a pipeline](https://docs.cloud.google.com/dataflow/docs/guides/job-builder-custom-job).

  2. Click **Save YAML** to open the **Save YAML** window.

  3. Perform one of the following actions:

     * To copy the YAML to the clipboard, click content_copy**Copy**.
     * To save to Cloud Storage, enter a Cloud Storage path and click **Save**.
     * To download a local file, click **Download**.



## Load a pipeline

After you save a pipeline to Beam YAML, you can load it back into job builder. You can then use the job builder to modify or run the pipeline.

You can load Beam YAML from Cloud Storage or from text.

### Load a pipeline from Cloud Storage

To load a pipeline from Cloud Storage:

  1. Go to the **Jobs** page in the Google Cloud console.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. Click add_box**Create job from builder**.

  3. Click **Load YAML**.

  4. Click **Load from Cloud Storage**.

  5. In the **YAML file location** box, enter the Cloud Storage location of the YAML file, or click **Browse** to select the file.

  6. Click **Load**.




### Load a pipeline from text

To load a pipeline from text:

  1. Go to the **Jobs** page in the Google Cloud console.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. Click add_box**Create job from builder**.

  3. Click **Load YAML**.

  4. Click **Load from text**.

  5. Paste the YAML into the window.

  6. Click **Load**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
