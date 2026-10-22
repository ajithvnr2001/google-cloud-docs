---
url: https://docs.cloud.google.com/cortex/docs/v6/optional-step-telemetry/
title: Telemetry opt out \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:29.881018+00:00
---

# Telemetry opt out  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/optional-step-telemetry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Telemetry opt out 

Starting with [Release 6.0](https://docs.cloud.google.com/cortex/docs/v6/release-notes#release_60), Cortex Framework now collects telemetry metrics during the deployment process, and operationally when the DAGs are executed. This helps the Cortex Framework team better support our customers, however you may opt out of this by setting `"allowTelemetry": false` in the [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file, as the following example shows:
    
    
    {
      ...
      "marketing": {
          ...
      },
      "OracleEBS": {
          ...
      },
      "allowTelemetry": false
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
