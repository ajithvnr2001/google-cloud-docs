---
url: https://docs.cloud.google.com/cortex/docs/uv-run-cortex-config/
title: CLI config \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:38.272171+00:00
---

# CLI config  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/uv-run-cortex-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CLI config

**NAME**

`uv run cortex-config` \- Configure Cortex Framework settings and user preferences.

**SYNOPSIS**
    
    
    uv run cortex-config [-h] {telemetry} ...
    

## Description

The `cortex-config` tool lets you globally manage user preferences, such as telemetry consent, for Cortex Framework on your machine.

## Subcommands

Use the following subcommands to manage specific configurations and preferences:

### `telemetry`

Globally manage telemetry data collection consent.
    
    
    uv run cortex-config telemetry {enable|disable|status}
    

  * `enable`: Opt in and globally enable telemetry collection. This updates the local consent properties file to `enable_telemetry=true`.
  * `disable`: Opt out and globally disable telemetry collection. This updates the local consent properties file to `enable_telemetry=false`.
  * `status`: Display the current telemetry consent state.



## Global flags

Flag | Description  
---|---  
`-h, --help` | Show help message and exit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
