---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-extraction-module/
title: Extraction module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:03.458450+00:00
---

# Extraction module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-extraction-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Extraction module

### TIPCommon.extraction.extract_action_param

`TIPCommon.extraction.extract_action_param(siemplify, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts an action parameter from the Siemplify object.

Parameters  
---  
`siemplify` | `Siemplify`A Siemplify object.  
`param_name` | `str`The name of the parameter to extract.  
`default_value` | Optional. `Any` The default value to return if the parameter is not found.  
`input_type` | Optional.`type`The type of the parameter.  
`is_mandatory` | Optional.`bool`Define whether the parameter is mandatory.  
`print_value` | Optional.`bool`Define whether to print the value of the parameter.  
`remove_whitespaces` | Optional.`bool`Define whether to remove whitespaces from the value of the parameter.  
  
#### Returns

The value of the parameter.

#### Return type

Any.

### TIPCommon.extraction.extract_configuration_param

`TIPCommon.extraction.extract_configuration_param(siemplify, provider_name, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts a configuration parameter value from the integration configuration.

Parameters  
---  
`siemplify` | The Siemplify object.  
`provider_name` | The integration identifier.  
`param_name` | The name of the parameter.  
`default_value` | The default value to set when there is no value in the configuration.   
`input_type` | The input type.  
`is_mandatory` | Define whether the parameter is mandatory.  
`print_value` | Define whether to print the value.  
`remove_whitespaces` | Define whether to remove whitespaces from the value.  
  
#### Returns

The extracted value.

### TIPCommon.extraction.extract_connector_param

`TIPCommon.extraction.extract_connector_param(siemplify, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts a connector parameter from the Siemplify object.

Parameters  
---  
`siemplify` | `Siemplify`The Siemplify object.  
`param_name` | `str`The name of the parameter to extract.  
`default_value` | Optional.`Any`The default value to return if the parameter is not found.  
`input_type` | Optional.`type`The type of the parameter.   
`is_mandatory` | Optional.`bool`Define whether the parameter is mandatory.  
`print_value` | Optional.`bool`Define whether to print the value of the parameter.  
`remove_whitespaces` | Optional.`bool`Define whether to remove whitespaces from the value of the parameter.  
  
#### Returns

The value of the parameter.

#### Return type

Any.

### TIPCommon.extraction.extract_job_param

`TIPCommon.extraction.extract_job_param(siemplify, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts a connector parameter from the Siemplify object.

Parameters  
---  
`siemplify` | `SiemplifyJob`The SiemplifyJob object.  
`param_name` | `str`The name of the parameter to extract.  
`default_value` | Optional.`Any`The default value to return if the parameter is not found.  
`input_type` | Optional.`type`The type of the parameter.   
`is_mandatory` | Optional.`bool`Define whether the parameter is mandatory.  
`print_value` | Optional.`bool`Define whether to print the parameter value.  
`remove_whitespaces` | Optional.`bool`Define whether to remove whitespaces from the parameter value.   
  
#### Returns

The value of the parameter.

#### Return type

Any.

### TIPCommon.extraction.extract_script_param

`TIPCommon.extraction.extract_script_param(siemplify, input_dictionary, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False, remove_whitespaces=True)`

Extracts a script parameter from an input dictionary.

Parameters  
---  
`siemplify` | The Siemplify object.  
`input_dictionary` | The input dictionary.  
`param_name` | The name of the parameter to extract.  
`default_value` | The default value to return if the parameter is not found.  
`input_type` | The type of the parameter.  
`is_mandatory` | Define whether the parameter is mandatory.  
`print_value` | Define whether to print the value of the parameter.  
`remove_whitespaces` | Define whether to remove whitespaces from the parameter value.  
  
#### Returns

The extracted value.

### TIPCommon.extraction.get_connector_detailed_params

`TIPCommon.extraction.get_connector_detailed_params(siemplify)`

Gets the detailed parameters for a connector.

Parameters  
---  
`siemplify` | `Siemplify`The Siemplify object.  
  
#### Returns

A list of `ConnectorParameter` objects.

#### Return type

`list`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
