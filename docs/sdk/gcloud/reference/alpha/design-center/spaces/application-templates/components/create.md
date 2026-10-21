---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/components/create/
title: gcloud alpha design-center spaces application-templates components create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:43.514854+00:00
---

# gcloud alpha design-center spaces application-templates components create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/components/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces application-templates components create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces application-templates components create - create a component 
SYNOPSIS
    

`gcloud alpha design-center spaces application-templates components create` (`COMPONENT` : `--application-template`=`APPLICATION_TEMPLATE` `--location`=`LOCATION` `--space`=`SPACE`) `--shared-template-revision-uri`=`SHARED_TEMPLATE_REVISION_URI` [`--display-name`=`DISPLAY_NAME`] [`--input-variable-aliases`=[`alias`=`ALIAS`],[`variable`=`VARIABLE`]] [`--parameters`=[`key`=`KEY`],[`value`=`VALUE`]] [`--use-as-root-module`] [[`--application-info-apphub-id`=`APPLICATION_INFO_APPHUB_ID` : `--application-info-deployment-region`=`APPLICATION_INFO_DEPLOYMENT_REGION` `--application-info-display-name`=`APPLICATION_INFO_DISPLAY_NAME` `--scope-type`=`SCOPE_TYPE` `--attributes-business-owners`=[`channel`=`CHANNEL`],[`displayName`=`DISPLAYNAME`],[`email`=`EMAIL`] `--attributes-developer-owners`=[`channel`=`CHANNEL`],[`displayName`=`DISPLAYNAME`],[`email`=`EMAIL`] `--attributes-operator-owners`=[`channel`=`CHANNEL`],[`displayName`=`DISPLAYNAME`],[`email`=`EMAIL`] [`--criticality-type`=`CRITICALITY_TYPE` : `--criticality-level`=`CRITICALITY_LEVEL` `--criticality-mission-critical`] [`--environment-type`=`ENVIRONMENT_TYPE` : `--environment`=`ENVIRONMENT`]]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a component in an application template. 
EXAMPLES
     To create the component `my-component` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` using a shared template revision, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1

Or run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template/components/my-component --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1

To create the component `my-component` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` using a google shared template `google-shared-template` and revision `rev1`, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=google/google-shared-template/revisions/rev1

To create the component `my-component` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` using a google shared template `google-shared-template` with its latest revision, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=google/google-shared-template

To create the component `my-component` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` using a shared template `my-shared-template` and revision `rev1` present in the same space, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=my-shared-template/revisions/rev1

To create the component `my-component` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` using a shared template `my-shared-template` with its latest revision present in the same space, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=my-shared-template

To create the component `my-component` with a display name `My Component` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` using a shared template revision, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1 --display-name="My Component"

To create the component `my-component` with parameter key value pair of `region:us-central1` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1`, run the following shorthand example: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1 --parameters=key=region,value=us-central1

Or run the following JSON example: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1 --parameters='[{"key": "region", "value": "us-central1"}]'

Or create a YAML or JSON file with the parameters and run the following file example: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1 --parameters=my-parameters.yaml

To create the component `my-component` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` as a separate root module, run: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1 --use-as-root-module

To create the component `my-component` with input variable alias mapping of `variable=db_password,alias=database_password` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1`, run the following shorthand example: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1 --input-variable-aliases=variable=db_password,alias=database_password

Or run the following JSON example: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1 --input-variable-aliases='[{"variable": "db_password", "alias":
     "database_password"}]'

Or create a YAML or JSON file with the input variable aliases and run the following file example: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components create my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --shared-template-revision-uri=projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template/revisions/rev1 --input-variable-aliases=my-aliases.yaml

POSITIONAL ARGUMENTS
    

Component resource - Identifier. The component name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `component` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`COMPONENT`
     ID of the component or fully qualified identifier for the component. 

To set the `component` attribute: 

  * provide the argument `component` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--application-template`=`APPLICATION_TEMPLATE`
     The applicationTemplate id of the component resource. 

To set the `application-template` attribute: 

  * provide the argument `component` on the command line with a fully specified name; 
  * provide the argument `--application-template` on the command line. 


`--location`=`LOCATION`
     The location id of the component resource. 

To set the `location` attribute: 

  * provide the argument `component` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The space id of the component resource. 

To set the `space` attribute: 

  * provide the argument `component` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


REQUIRED FLAGS
    

`--shared-template-revision-uri`=`SHARED_TEMPLATE_REVISION_URI`
     The shared template used to generate the component. 
OPTIONAL FLAGS
    

`--display-name`=`DISPLAY_NAME`
     The component display name. 
`--input-variable-aliases`=[`alias`=`ALIAS`],[`variable`=`VARIABLE`]
     Input variable aliases defined on this live component. 

`alias`
     Alias for the variable name to be exposed at the root level of the composite template. 
`variable`
     Name of the input variable inside the component's underlying template or module. 
`Shorthand Example:`
    
    
    --input-variable-aliases=alias=string,variable=string --input-variable-aliases=alias=string,variable=string

`JSON Example:`
    
    
    --input-variable-aliases='[{"alias": "string", "variable": "string"}]'

`File Example:`
    
    
    --input-variable-aliases=path_to_file.(yaml|json)

`--parameters`=[`key`=`KEY`],[`value`=`VALUE`]
     The component parameters. 

`key`
     The key of the parameter. 
`value`
     The value of the parameter. 
`Shorthand Example:`
    
    
    --parameters=key=string,value={…} --parameters=key=string,value={…}

`JSON Example:`
    
    
    --parameters='[{"key": "string", "value": {…}}]'

`File Example:`
    
    
    --parameters=path_to_file.(yaml|json)

`--use-as-root-module`
     Whether the component is exported as a separate terraform root module in a composite application template. If this is false, then native components will be exported as a submodule of a separate terraform root module. 
This captures the apphub application details associated with the component. 
`--application-info-apphub-id`=`APPLICATION_INFO_APPHUB_ID`
     The application ID of the apphub application. The ID must be 1-63 characters long and should match the regular expression `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--application-info-deployment-region`=`APPLICATION_INFO_DEPLOYMENT_REGION`
     Deployment region for the component. If the scope is set to REGIONAL, then the apphub application is created in this region, e.g. `us-central1`. 
`--application-info-display-name`=`APPLICATION_INFO_DISPLAY_NAME`
     Display name for the application. The number of characters should be less than 64 characters. 
Scope of an application. 
`--scope-type`=`SCOPE_TYPE`
     Scope Type. `SCOPE_TYPE` must be one of: 

`global`
     Global type. 
`regional`
     Regional type. 
Consumer provided attributes. 
`--attributes-business-owners`=[`channel`=`CHANNEL`],[`displayName`=`DISPLAYNAME`],[`email`=`EMAIL`]
     Business team that ensures user needs are met and value is delivered. 

`channel`
     Communication channel of the contacts. 

`uri`
     URI of the channel. 
`displayName`
     Contact's name. Can have a maximum length of 63 characters. 
`email`
     Email address of the contacts. 
`Shorthand Example:`
    
    
    --attributes-business-owners=channel={uri=string},displayName=string,email=string --attributes-business-owners=channel={uri=string},displayName=string,email=string

`JSON Example:`
    
    
    --attributes-business-owners='[{"channel": {"uri": "string"}, "displayName": "string", "email": "string"}]'

`File Example:`
    
    
    --attributes-business-owners=path_to_file.(yaml|json)

`--attributes-developer-owners`=[`channel`=`CHANNEL`],[`displayName`=`DISPLAYNAME`],[`email`=`EMAIL`]
     Developer team that owns development and coding. 

`channel`
     Communication channel of the contacts. 

`uri`
     URI of the channel. 
`displayName`
     Contact's name. Can have a maximum length of 63 characters. 
`email`
     Email address of the contacts. 
`Shorthand Example:`
    
    
    --attributes-developer-owners=channel={uri=string},displayName=string,email=string --attributes-developer-owners=channel={uri=string},displayName=string,email=string

`JSON Example:`
    
    
    --attributes-developer-owners='[{"channel": {"uri": "string"}, "displayName": "string", "email": "string"}]'

`File Example:`
    
    
    --attributes-developer-owners=path_to_file.(yaml|json)

`--attributes-operator-owners`=[`channel`=`CHANNEL`],[`displayName`=`DISPLAYNAME`],[`email`=`EMAIL`]
     Operator team that ensures runtime and operations. 

`channel`
     Communication channel of the contacts. 

`uri`
     URI of the channel. 
`displayName`
     Contact's name. Can have a maximum length of 63 characters. 
`email`
     Email address of the contacts. 
`Shorthand Example:`
    
    
    --attributes-operator-owners=channel={uri=string},displayName=string,email=string --attributes-operator-owners=channel={uri=string},displayName=string,email=string

`JSON Example:`
    
    
    --attributes-operator-owners='[{"channel": {"uri": "string"}, "displayName": "string", "email": "string"}]'

`File Example:`
    
    
    --attributes-operator-owners=path_to_file.(yaml|json)

Criticality of the Application, Service, or Workload 
`--criticality-type`=`CRITICALITY_TYPE`
     Criticality Type. `CRITICALITY_TYPE` must be one of: 

`high`
     High impact. 
`low`
     Low impact. 
`medium`
     Medium impact. 
`mission-critical`
     Mission critical service, application or workload. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--criticality-level`=`CRITICALITY_LEVEL`
     Criticality level. Can contain only lowercase letters, numeric characters, underscores, and dashes. Can have a maximum length of 63 characters. Deprecated: Please refer to type instead. 
`--criticality-mission-critical`
     Indicates mission-critical Application, Service, or Workload. Deprecated: Please refer to type instead. 
Environment of the Application, Service, or Workload 
`--environment-type`=`ENVIRONMENT_TYPE`
     Environment Type. `ENVIRONMENT_TYPE` must be one of: 

`development`
     Development environment. 
`production`
     Production environment. 
`staging`
     Staging environment. 
`test`
     Test environment. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--environment`=`ENVIRONMENT`
     Environment name. Can contain only lowercase letters, numeric characters, underscores, and dashes. Can have a maximum length of 63 characters. Deprecated: Please refer to type instead. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1alpha` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud design-center spaces application-templates components create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
