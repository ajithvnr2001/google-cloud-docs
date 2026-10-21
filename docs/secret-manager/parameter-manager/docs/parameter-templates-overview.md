---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/parameter-templates-overview/
title: Parameter templates overview \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:08:27.997676+00:00
---

# Parameter templates overview  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/parameter-templates-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Parameter templates overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use parameter templates to define standardized configuration blueprints (templates) and insert instance-specific values through variables from [parameter versions](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version). With parameter templates, you can separate configuration structure from data, and achieve safer and faster deployments.

Instead of manually maintaining similar configuration files for each environment, you can define a single parameter template and reuse it across your entire infrastructure.

### Key benefits

Parameter templates offer the following key benefits:

  * Eliminate unintended changes and ensure consistency across all environments.
  * Enforce baseline security policies to ensure compliance.
  * Save time and effort when creating new instances by reusing common configurations.
  * Reduce the risk of downtime and compliance failures by eliminating manual, error-prone edits.



## How parameter templates work

Parameter templates help separate your configuration structure from the actual data. This process involves two primary resources and a rendering step.

  * **Parameter template** : resource that holds template metadata.
  * **Parameter template version** : resource that contains the structural data in YAML or JSON format. To include variables as placeholders in a template version, specify them in the `{{.variableName}}` format, for example, `{{.cpuCount}}`.
  * **Rendering a template version** : the process of generating the final configuration. Parameter Manager securely substitutes the variables in your template version with the values from the parameter version.



## Parameter template example

To understand how parameter templates let you separate your configuration structure from the data, consider a `forex-trading-engine` application. The application connects to market data providers for real-time rates and interacts with execution engines to place orders. It also maintains business constants, such as default transaction limits for specific currency pairs.

Instead of maintaining separate configuration files for each environment, you define a single configuration blueprint (the parameter template) and inject environment-specific values from a parameter version.

### Parameter template

The parameter template defines the configuration structure. It uses variables formatted as `{{.variableName}}` to act as placeholders for environment-specific data.
    
    
    appName: forex-trading-engine
    environment: {{.env}}
    logLevel: {{.log_level}}
    currencyPairDefaultsInUSD:
        EURUSD: 10000000
        XAUUSD: 5000000
        BTCUSD: 2000000
    marketData:
        provider: {{.market.dataProviderName}}
        apiEndpoint: {{.market.dataProviderEndpoint}}
    execution:
        provider: {{.execution.providerName}}
        apiEndpoint: {{.execution.providerEndpoint}}
    

### Parameter version

The parameter version contains the data that will replace the placeholders in your template. In this example, the following are the production-specific values:
    
    
    env: prod
    log_level: INFO
    
    market:
        dataProviderName: ProdAltostratProvider
        dataProviderEndpoint: wss://prod-market-data.altostrat.com:443
    
    execution:
        providerName: ProdCymbalgroupExecutor
        providerEndpoint: https://prod-execution.cymbalgroup.com/v1/orders
    

### Rendered output

When you render a parameter template, Parameter Manager generates the final configuration by securely substituting the variables in your template with the values from the parameter version.

The following is the final configuration:
    
    
    appName: forex-trading-engine
    environment: prod
    logLevel: INFO
    currencyPairDefaultsInUSD:
        EURUSD: 10000000
        XAUUSD: 5000000
        BTCUSD: 2000000
    marketData:
        provider: ProdAltostratProvider
        apiEndpoint: wss://prod-market-data.altostrat.com:443
    execution:
        provider: ProdCymbalgroupExecutor
        apiEndpoint: https://prod-execution.cymbalgroup.com/v1/orders
    

## Limitations

To ensure a secure and stable experience, consider the following operational constraints:

  * Templates only support direct variable substitution, for example, `{{.cpuCount}}` is replaced with the value of the variable from the corresponding parameter version.
  * Each template version must be a valid JSON or YAML object. The API doesn't support unformatted text.
  * You can't reference Secret Manager secrets directly in a template. To use secrets, you must use the `__REF__()` syntax within a parameter version, which is then hydrated into the template during rendering. For more information, see [Reference secrets in parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter).
  * The size of the final rendered output must not exceed 1 MB.
  * Each template version supports a maximum of 64 variables.



## What's next

  * [Create a parameter template](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter-template)
  * [Add a parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-template-version)
  * [Reference secrets in parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
