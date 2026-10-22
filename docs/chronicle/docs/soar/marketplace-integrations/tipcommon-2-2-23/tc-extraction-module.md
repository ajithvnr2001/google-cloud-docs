---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-extraction-module/
title: extraction module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:05.356967+00:00
---

# extraction module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-extraction-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# `extraction` module

The **`extraction` module** contains standardized functions to retrieve parameter values from various platform objects. These utilities ensure that data is correctly typed and validated, supporting mandatory field checks and whitespace management for seamless integration development.

### TIPCommon.extraction.extract_action_param

`TIPCommon.extraction.extract_action_param(siemplify, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts an action parameter from the `siemplify` object.

#### Parameters

Parameters  
---  
`siemplify` | `SiemplifyAction.SiemplifyAction` The `siemplify` object used for action execution.  
`param_name` | `str` The name of the parameter to extract.  
`default_value` | `Any` The default value to return if the parameter isn't found.  
`input_type` | `type` The expected data type of the parameter.  
`is_mandatory` | `bool` Indicates if the parameter is required.  
`remove_whitespaces` | `bool` Indicates if leading and trailing whitespaces are removed from the value.  
  
#### Returns

The extracted parameter value.

#### Return type

`Any`

### TIPCommon.extraction.extract_configuration_param

`TIPCommon.extraction.extract_configuration_param(siemplify, provider_name, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts a configuration parameter value from the integration's global configuration.

#### Parameters

Parameters  
---  
`provider_name` | `str` The unique identifier for the integration.  
`param_name` | `str`The specific configuration key to retrieve.  
  
#### Returns

The extracted configuration value.

### TIPCommon.extraction.extract_connector_param

`TIPCommon.extraction.extract_connector_param(siemplify, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts a connector parameter from the `siemplify` object during connector execution.

#### Parameters

Parameters  
---  
`siemplify` | `SiemplifyConnectors.SiemplifyConnectorExecution` The `siemplify` object used for connector execution.  
  
#### Returns

The value of the connector parameter.

#### Return type

`Any`

### TIPCommon.extraction.extract_job_param

`TIPCommon.extraction.extract_job_param(siemplify, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts a job parameter from the `siemplify` job object.

#### Parameters

Parameters  
---  
`siemplify` | `SiemplifyJob.SiemplifyJob` The `siemplify` object for the current job instance.  
  
#### Returns

The extracted job parameter value.

### TIPCommon.extraction.extract_script_param

`TIPCommon.extraction.extract_script_param(siemplify, input_dictionary, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts a script parameter from a provided input dictionary.

#### Parameters

Parameters  
---  
`input_dictionary` | `dict` The dictionary source containing script parameters.  
  
#### Returns

The extracted parameter value from the dictionary.

### TIPCommon.extraction.get_connector_detailed_params

`TIPCommon.extraction.get_connector_detailed_params(siemplify)`

Retrieves a detailed list of parameters specifically defined for a connector.

#### Parameters

Parameters  
---  
`siemplify` | `SiemplifyConnectors.SiemplifyConnectorExecution` The `siemplify` object for the connector.  
  
#### Returns

A list of `ConnectorParameter` objects.

#### Return type

`list`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
