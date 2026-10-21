---
url: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/update/
title: gcloud design-center spaces application-templates update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:53.048530+00:00
---

# gcloud design-center spaces application-templates update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud design-center spaces application-templates update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud design-center spaces application-templates update - update an application template 
SYNOPSIS
    

`gcloud design-center spaces application-templates update` (`APPLICATION_TEMPLATE` : `--location`=`LOCATION` `--space`=`SPACE`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--application-parameters`=[`key`=`KEY`],[`value`=`VALUE`] | `--add-application-parameters`=[`key`=`KEY`],[`value`=`VALUE`] `--clear-application-parameters` | `--remove-application-parameters`=[`key`=`KEY`],[`value`=`VALUE`]] [`--clear-saas-runtime-context` `--saas-runtime-context-names`=[`SAAS_RUNTIME_CONTEXT_NAMES`,…] | `--add-saas-runtime-context-names`=[`ADD_SAAS_RUNTIME_CONTEXT_NAMES`,…] `--clear-saas-runtime-context-names` | `--remove-saas-runtime-context-names`=[`REMOVE_SAAS_RUNTIME_CONTEXT_NAMES`,…]] [`--root-input-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`] | `--add-root-input-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`] `--clear-root-input-variables` | `--remove-root-input-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`]] [`--root-output-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`] | `--add-root-output-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`] `--clear-root-output-variables` | `--remove-root-output-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an application template. 
EXAMPLES
     To update the display name to `My New App Template Name` for the application template `my-app-template` in space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud design-center spaces application-templates update my-app-template --space=my-space --project=my-project --location=us-central1 --display-name="My New App Template Name"

Or run: 
    
    
    gcloud design-center spaces application-templates update projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template --display-name="My New App Template Name"

To clear the application parameters for the application template `my-app-template` in space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud design-center spaces application-templates update my-app-template --space=my-space --project=my-project --location=us-central1 --clear-application-parameters

To add an application parameter key-value pair of `project_id:new-project` to the application template `my-app-template` in space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud design-center spaces application-templates update my-app-template --space=my-space --project=my-project --location=us-central1 --add-application-parameters=key=project_id,value=new-project

To remove an application parameter key-value pair of `project_id:new-project` from the application template `my-app-template` in space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud design-center spaces application-templates update my-app-template --space=my-space --project=my-project --location=us-central1 --remove-application-parameters=key=project_id,value=my-project

POSITIONAL ARGUMENTS
    

ApplicationTemplate resource - Identifier. Application template name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `application_template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`APPLICATION_TEMPLATE`
     ID of the applicationTemplate or fully qualified identifier for the applicationTemplate. 

To set the `application_template` attribute: 

  * provide the argument `application_template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the applicationTemplate resource. 

To set the `location` attribute: 

  * provide the argument `application_template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The space id of the applicationTemplate resource. 

To set the `space` attribute: 

  * provide the argument `application_template` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     Application template description. 
`--display-name`=`DISPLAY_NAME`
     Application template display name. 
Update application_parameters. 

At most one of these can be specified: 

`--application-parameters`=[`key`=`KEY`],[`value`=`VALUE`]
     Set application_parameters to new value. Parameters to apply to all components in an application. You can specify projectID and region. 

`key`
     The key of the parameter. 
`value`
     The value of the parameter. 
`Shorthand Example:`
    
    
    --application-parameters=key=string,value={…} --application-parameters=key=string,value={…}

`JSON Example:`
    
    
    --application-parameters='[{"key": "string", "value": {…}}]'

`File Example:`
    
    
    --application-parameters=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-application-parameters`=[`key`=`KEY`],[`value`=`VALUE`]
     Add new value to application_parameters list. Parameters to apply to all components in an application. You can specify projectID and region. 

`key`
     The key of the parameter. 
`value`
     The value of the parameter. 
`Shorthand Example:`
    
    
    --add-application-parameters=key=string,value={…} --add-application-parameters=key=string,value={…}

`JSON Example:`
    
    
    --add-application-parameters='[{"key": "string", "value": {…}}]'

`File Example:`
    
    
    --add-application-parameters=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-application-parameters`
     Clear application_parameters value and set to empty list. 
`--remove-application-parameters`=[`key`=`KEY`],[`value`=`VALUE`]
     Remove existing value from application_parameters list. Parameters to apply to all components in an application. You can specify projectID and region. 

`key`
     The key of the parameter. 
`value`
     The value of the parameter. 
`Shorthand Example:`
    
    
    --remove-application-parameters=key=string,value={…} --remove-application-parameters=key=string,value={…}

`JSON Example:`
    
    
    --remove-application-parameters='[{"key": "string", "value": {…}}]'

`File Example:`
    
    
    --remove-application-parameters=path_to_file.(yaml|json)

SaaS runtime context. 
`--clear-saas-runtime-context`
     Set applicationTemplate.saasRuntimeContext back to default value. 
Update saas_runtime_context_names. 

At most one of these can be specified: 

`--saas-runtime-context-names`=[`SAAS_RUNTIME_CONTEXT_NAMES`,…]
     Set saas_runtime_context_names to new value. 
Or at least one of these can be specified: 

`--add-saas-runtime-context-names`=[`ADD_SAAS_RUNTIME_CONTEXT_NAMES`,…]
     Add new value to saas_runtime_context_names list. 
At most one of these can be specified: 

`--clear-saas-runtime-context-names`
     Clear saas_runtime_context_names value and set to empty list. 
`--remove-saas-runtime-context-names`=[`REMOVE_SAAS_RUNTIME_CONTEXT_NAMES`,…]
     Remove existing value from saas_runtime_context_names list. 
Update root_input_variables. 

At most one of these can be specified: 

`--root-input-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`]
     Set root_input_variables to new value. Root level input variables of the application template. 

`componentUri`
     Component to which this variable belongs. 
`variable`
     Name of the variable. 
`Shorthand Example:`
    
    
    --root-input-variables=componentUri=string,variable=string --root-input-variables=componentUri=string,variable=string

`JSON Example:`
    
    
    --root-input-variables='[{"componentUri": "string", "variable": "string"}]'

`File Example:`
    
    
    --root-input-variables=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-root-input-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`]
     Add new value to root_input_variables list. Root level input variables of the application template. 

`componentUri`
     Component to which this variable belongs. 
`variable`
     Name of the variable. 
`Shorthand Example:`
    
    
    --add-root-input-variables=componentUri=string,variable=string --add-root-input-variables=componentUri=string,variable=string

`JSON Example:`
    
    
    --add-root-input-variables='[{"componentUri": "string", "variable": "string"}]'

`File Example:`
    
    
    --add-root-input-variables=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-root-input-variables`
     Clear root_input_variables value and set to empty list. 
`--remove-root-input-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`]
     Remove existing value from root_input_variables list. Root level input variables of the application template. 

`componentUri`
     Component to which this variable belongs. 
`variable`
     Name of the variable. 
`Shorthand Example:`
    
    
    --remove-root-input-variables=componentUri=string,variable=string --remove-root-input-variables=componentUri=string,variable=string

`JSON Example:`
    
    
    --remove-root-input-variables='[{"componentUri": "string", "variable": "string"}]'

`File Example:`
    
    
    --remove-root-input-variables=path_to_file.(yaml|json)

Update root_output_variables. 

At most one of these can be specified: 

`--root-output-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`]
     Set root_output_variables to new value. Root level output variables of the application template. 

`componentUri`
     Component to which this variable belongs. 
`variable`
     Name of the variable. 
`Shorthand Example:`
    
    
    --root-output-variables=componentUri=string,variable=string --root-output-variables=componentUri=string,variable=string

`JSON Example:`
    
    
    --root-output-variables='[{"componentUri": "string", "variable": "string"}]'

`File Example:`
    
    
    --root-output-variables=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-root-output-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`]
     Add new value to root_output_variables list. Root level output variables of the application template. 

`componentUri`
     Component to which this variable belongs. 
`variable`
     Name of the variable. 
`Shorthand Example:`
    
    
    --add-root-output-variables=componentUri=string,variable=string --add-root-output-variables=componentUri=string,variable=string

`JSON Example:`
    
    
    --add-root-output-variables='[{"componentUri": "string", "variable": "string"}]'

`File Example:`
    
    
    --add-root-output-variables=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-root-output-variables`
     Clear root_output_variables value and set to empty list. 
`--remove-root-output-variables`=[`componentUri`=`COMPONENTURI`],[`variable`=`VARIABLE`]
     Remove existing value from root_output_variables list. Root level output variables of the application template. 

`componentUri`
     Component to which this variable belongs. 
`variable`
     Name of the variable. 
`Shorthand Example:`
    
    
    --remove-root-output-variables=componentUri=string,variable=string --remove-root-output-variables=componentUri=string,variable=string

`JSON Example:`
    
    
    --remove-root-output-variables='[{"componentUri": "string", "variable": "string"}]'

`File Example:`
    
    
    --remove-root-output-variables=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha design-center spaces application-templates update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
