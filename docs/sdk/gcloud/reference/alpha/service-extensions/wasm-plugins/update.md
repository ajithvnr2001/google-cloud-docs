---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-extensions/wasm-plugins/update/
title: gcloud alpha service-extensions wasm-plugins update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:52.453730+00:00
---

# gcloud alpha service-extensions wasm-plugins update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-extensions/wasm-plugins/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha service-extensions wasm-plugins update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha service-extensions wasm-plugins update - update a `WasmPlugin` resource 
SYNOPSIS
    

`gcloud alpha service-extensions wasm-plugins update` (`WASM_PLUGIN` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--log-config`=[`LOG_CONFIG`,…]] [`--image`=`IMAGE` `--main-version`=`MAIN_VERSION` `--plugin-config`=`PLUGIN_CONFIG` | `--plugin-config-file`=`PATH_TO_FILE` | `--plugin-config-uri`=`PLUGIN_CONFIG_URI`] [`--kms-key-name`=`KMS_KEY_NAME` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update an existing `WasmPlugin` resource and optionally create a `WasmPluginVersion` resource and set it as the main (serving) one. 

If `--image` is not specified: 

  * the method only updates the `WasmPlugin` resource without creating a `WasmPluginVersion`. 
  * the `--plugin-config***` flags are disallowed. 
  * if `--main-version` is set, then the referenced `WasmPluginVersion` must already exist and it is set as the main (serving) one. 



If `--image` is specified: 

  * the `--main-version` flag must also be specified. 
  * the method updates the `WasmPlugin` resource and creates a new `WasmPluginVersion` with `--main-version` name and sets it as the main (serving) one. 
  * the `--plugin-config***` flags are allowed. 
  * the `--async` flag is disallowed. 


EXAMPLES
     To update a `WasmPlugin` called `my-plugin`, run: 
    
    
    gcloud alpha service-extensions wasm-plugins update my-plugin --main-version=new-version --description="A new description." --labels=label1=value1

To update a `WasmPlugin` called `my-plugin` and also create a new version called `v1` and set it as main: 
    
    
    gcloud alpha service-extensions wasm-plugins update my-plugin --main-version=v1 --description="A new description." --labels=label1=value1 --image=…-docker.pkg.dev/my-project/repository/container:tag

POSITIONAL ARGUMENTS
    

WasmPlugin resource - The ID of the `WasmPlugin` to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `wasm_plugin` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`WASM_PLUGIN`
     ID of the WasmPlugin or fully qualified identifier for the WasmPlugin. 

To set the `wasm_plugin` attribute: 

  * provide the argument `wasm_plugin` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location ID. To set the `location` attribute: 

  * provide the argument `wasm_plugin` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * use global location. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A human-readable description of the resource. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--log-config`=[`LOG_CONFIG`,…]
     Logging options for the activity performed by this plugin. The following options can be set: 

  * `enable`: whether to enable logging. If `log-config` flag is set, `enable` option is required. 


  * `sample-rate`: configures the sampling rate of activity logs, where `1.0` means all logged activity is reported and `0.0` means no activity is reported. The default value is `1.0`, and the value of the field must be in range `0` to `1` (inclusive). 


  * `min-log-level`: specifies the lowest level of the logs that should be exported to Cloud Logging. The default value is `INFO`. 



Example usage: `--log-config=enable=True,sample-rate=0.5,min-log-level=INFO --log_config=enable=False`

`--image`=`IMAGE`
     URI of the container image containing the plugin's Wasm module, stored in the Artifact Registry. 
`--main-version`=`MAIN_VERSION`
     The ID of the `WasmPluginVersion` that should be the currently serving one. The version referred to must be a child of this `WasmPlugin`. 

If the `--image` flag was also provided, the `WasmPluginVersion` will be created for that `WasmPlugin` and will be set as the current main version. 

Configuration for the plugin, provided at runtime by the `on_configure` function (Rust Proxy-Wasm SDK) or the `onConfigure` method (C++ Proxy-Wasm SDK). 

At most one of these can be specified: 

`--plugin-config`=`PLUGIN_CONFIG`
     Plugin runtime configuration in the textual format. 
`--plugin-config-file`=`PATH_TO_FILE`
     Path to a local file containing the plugin runtime configuration. 

Use a full or relative path to a local file containing the value of plugin_config_file. 

`--plugin-config-uri`=`PLUGIN_CONFIG_URI`
     URI of the container image containing the plugin's runtime configuration, stored in the Artifact Registry. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the WasmPlugin. The 'Network Actions Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key-name`=`KMS_KEY_NAME`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key-name` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key-name` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Google Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key-name` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key-name` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud service-extensions wasm-plugins update](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/update)
    
    
    [gcloud beta service-extensions wasm-plugins update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-extensions/wasm-plugins/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
