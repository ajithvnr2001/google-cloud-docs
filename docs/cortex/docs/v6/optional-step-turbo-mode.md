---
url: https://docs.cloud.google.com/cortex/docs/v6/optional-step-turbo-mode/
title: Turbo mode \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:38.428799+00:00
---

# Turbo mode  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/optional-step-turbo-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Turbo mode

This page describes an optional step to enable the Turbo Mode for the Cortex Framework Data Foundation deployment. Google Cloud Cortex Framework offers the following two deployment modes to consider when setting up your data pipelines in the [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file.

  1. **Standard Mode (`turboMode=false`)**:

This option is recommended if you are still making adjustments to your data source or suspect there might be mismatches between your views and the actual data tables. In this mode, the deployment process attempts to create all the defined views in your configuration, even if there are errors in some views. This might take longer, but it helps identify all potential issues (mismatches between views and tables) in a single run.

  2. **Turbo Mode (`turboMode=true`)**:

This mode is for faster deployments once your data source configuration is done correctly. The deployment process dynamically generates a `cloudbuild.views.yaml` file with each view in the right dependencies file (for example, `dependencies_ecc.txt` or `dependencies_s4.txt`) as a single step of the build. This can significantly speed up deployment times (up to 10 times faster). However, the downside is that if there's an error in any view during deployment, the entire process stops. This might not be ideal for debugging purposes as you might need to rerun the deployment to identify the specific error.




The suggestion is to choose "Standard" for initial setup or troubleshooting, and "Turbo" for faster deployments later.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
