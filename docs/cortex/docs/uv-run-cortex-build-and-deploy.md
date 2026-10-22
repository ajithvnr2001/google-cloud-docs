---
url: https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build-and-deploy/
title: CLI Cortex Framework build and deploy \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:45.609676+00:00
---

# CLI Cortex Framework build and deploy  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build-and-deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CLI Cortex Framework build and deploy

**NAME**

`uv run cortex-build-and-deploy` \- Deploy Cortex Framework to Google Cloud project.

**SYNOPSIS**
    
    
    uv run cortex-build-and-deploy [-h] [--config config/config.yaml] 
                                   [--output-dir dist]
                                   [--enable-apis] [--create-datasets] 
                                   [--disable-telemetry] 
                                   [--assertions ASSERTIONS]
    

## Global flags

Flag | Description | Default  
---|---|---  
`-h, --help` | Show help message and exit. |   
`--config config/config.yaml` | Path to global config.yaml. | `config/config.yaml`  
`--output-dir dist` | Path to the build output directory. | `dist`  
`--enable-apis` | Enable required APIs without prompting. |   
`--create-datasets` | Create missing datasets without prompting. |   
`--disable-telemetry` | Temporarily disable telemetry event logging during execution. For more information, see [Cortex Framework Telemetry](https://docs.cloud.google.com/cortex/docs/telemetry). |   
`--assertions ASSERTIONS` | Path to a Dataform assertions file (assertions.sqlx). For more information, see [Cortex Framework Observability](https://docs.cloud.google.com/cortex/docs/observability). |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
