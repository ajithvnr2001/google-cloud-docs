---
url: https://docs.cloud.google.com/cortex/docs/telemetry/
title: Telemetry in Cortex Framework \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:21.365585+00:00
---

# Telemetry in Cortex Framework  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/telemetry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Telemetry in Cortex Framework

Cortex Framework collects anonymous usage statistics during deployment and synchronization processes. 

## Purpose of data collection

  * **Feature adoption evaluation** : Monitoring the frequency of framework module and data product deployments informs development priorities.
  * **Integration pattern identification** : Tracking connected source system variants (e.g., SAP ECC, SAP S/4HANA) enables the verification of compatibility and the prioritization of maintenance for these integrations.



Telemetry is **enabled by default**. To disable it, see "Disable telemetry" section.

## Data collected

The framework collects configuration identifiers, such as dataset IDs, data product instance IDs, and repository IDs. User identity attributes, such as names, emails, or IP addresses, are not collected.

  * **Google Cloud project number** : Identifies the project running the deployment, transmitted in the `X-Goog-User-Project` header to aggregate usage.
  * **Deployment region or location** : The region where target resources are being deployed, used to track geographic distribution..
  * **Framework version** : The version of the Cortex Framework codebase in use (for example, `7.0.0`).
  * **Component name** : The high-level architecture component being acted upon (for example, `platform`, `data-product`, or `foundation`).
  * **Tool type** : The specific CLI command or utility executed (for example, `deployer`, or `knowledge-catalog`)
  * **Target variant** : The source system or domain category of the deployed modules (e.g., `sap`, or `marketing`).
  * **Enabled module types** : The directory names or paths of individual modules enabled in the configuration.
  * **Dataform repository ID** : The user-configured name of the target Dataform repository.
  * **BigQuery dataset ID** : The user-configured target BigQuery dataset name.
  * **Data product instance ID** : The user-provided ID used during the Knowledge Catalog registration step to identify registered data products.
  * **Execution status** : The success or failure state of the deployment step (for example, `deployed`, `post-deploy-success`, `error`, `registered`, or `updated`).



## User-Agent header structure

Telemetry parameters are injected into Google Cloud API requests using a specialized HTTP User-Agent header that is dynamically formatted using the following pattern:

`gcp-cortex-eng/framework/<version>/<component>/<tool_type>/<variant>[/<optional_extension>]/<status>`

For example, when successfully deploying SAP ERP foundations:

`gcp-cortex-eng/framework/7.0.0/platform/deployer/sap/cortex/sap/foundations/sap/deployed`

## Data transmission

Cortex Framework utilizes a passive, zero-payload metadata logging mechanism. Rather than transmitting explicit log payloads to external endpoints, telemetry events are recorded using standard interactions with Google Cloud services.

During the execution of deploy, sync, or demo commands, the framework communicates with standard Google Cloud APIs, including [BigQuery](https://docs.cloud.google.com/bigquery/docs) and [Dataform](https://docs.cloud.google.com/dataform/docs).

No telemetry data is sent in the body of these API requests. Instead, telemetry data is captured natively by Google Cloud's API traffic logging, which parses the custom User-Agent and project number headers to measure the adoption and success rates of the solution.

## Disable telemetry

Cortex Framework respects your privacy settings and implements a persistent opt-out policy. You can manage telemetry globally using the cortex-config tool or by passing a CLI flag during execution.

### Disable globally

You can manage telemetry by updating a persistent user preference file located on your machine at ~/.cortex/cortex-framework-consent.properties. If this file contains enable_telemetry=false, telemetry API calls are completely skipped at runtime.

  * **Permanently opt out (globally disable)** :


    
    
    uv run cortex-config telemetry disable
    

  * **Permanently opt in (globally enable)** :


    
    
    uv run cortex-config telemetry enable
    

  * **Check the current status** :


    
    
    uv run cortex-config telemetry status
    

### Disable for a single execution

You can pass the --disable-telemetry flag to execution commands. When --disable-telemetry is executed once, the framework automatically creates the persistent configuration file at ~/.cortex/cortex-framework-consent.properties containing enable_telemetry=false.
    
    
    ## Cortex Framework-deploy
    uv run cortex-deploy --config config/config.yaml --disable-telemetry
    
    ## Cortex Framework-build-and-deploy
    uv run cortex-build-and-deploy --config config/config.yaml --disable-telemetry
    
    ## Cortex Framework-demo
    uv run cortex-demo --config config/config.yaml --disable-telemetry
    
    ## Cortex Framework-kc-sync
    uv run cortex-kc-sync --config config/config.yaml --disable-telemetry
    

For more information about these commands and their parameters, see the following CLI references:

  * [CLI Cortex Framework config](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-config)
  * [CLI Cortex Framework deploy](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-deploy)
  * [CLI Cortex Framework build and deploy](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build-and-deploy)
  * [CLI Cortex Framework demo deploy](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-demo)
  * [CLI Cortex Framework Knowledge Catalog sync](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-kc-sync)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
