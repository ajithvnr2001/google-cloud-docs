---
url: https://docs.cloud.google.com/cortex/docs/uv-run-cortex-kc-sync/
title: CLI Cortex Framework Knowledge Catalog sync \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:11.727501+00:00
---

# CLI Cortex Framework Knowledge Catalog sync  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/uv-run-cortex-kc-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CLI Cortex Framework Knowledge Catalog sync

**NAME**

`uv run cortex-kc-sync` \- Synchronize Cortex Framework Data Products with Knowledge Catalog.

**SYNOPSIS**
    
    
    uv run cortex-kc-sync [-h] [--config config/config.yaml] [--kc-project-id KC_PROJECT_ID ] 
                          [--data-modules-root-directory src/data_modules] 
                          [--owner-email OWNER_EMAIL] [--disable-telemetry]
    

## Global flags

Flag | Description | Default  
---|---|---  
`-h, --help` | Show help message and exit. |   
`--config config/config.yaml` | Path to the global `config.yaml` file used during deployment. | `config/config.yaml`  
`--kc-project-id KC_PROJECT_ID` | The Google Cloud project ID where Knowledge Catalog resources will be created. If omitted, the tool automatically infers the project ID from the target BigQuery dataset defined in `config.yaml`. |   
`--data-modules-root-directory src/data_modules` | Path to the root directory containing Cortex Framework data modules. | `src/data_modules`  
`--owner-email OWNER_EMAIL` | **Required.** The email address of the owner of the data products. |   
`--disable-telemetry` | Temporarily disable telemetry event logging during execution. For more information, see [Cortex Framework Telemetry](https://docs.cloud.google.com/cortex/docs/telemetry). |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
