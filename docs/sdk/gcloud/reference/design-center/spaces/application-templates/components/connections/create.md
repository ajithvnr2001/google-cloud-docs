---
url: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/connections/create/
title: gcloud design-center spaces application-templates components connections create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:50.227845+00:00
---

# gcloud design-center spaces application-templates components connections create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components/connections/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud design-center spaces application-templates components connections create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud design-center spaces application-templates components connections create - create a connection 
SYNOPSIS
    

`gcloud design-center spaces application-templates components connections create` (`CONNECTION` : `--component`=`COMPONENT`) `--destination-component-uri`=`DESTINATION_COMPONENT_URI` [`--application-template`=`APPLICATION_TEMPLATE`] [`--destination-component-parameters`=[`key`=`KEY`],[`value`=`VALUE`]] [`--location`=`LOCATION`] [`--source-component-parameters`=[`key`=`KEY`],[`value`=`VALUE`]] [`--space`=`SPACE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a connection between components in an application template. 
EXAMPLES
     To create the connection `my-connection` in component `my-component` of application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` with a destination component `other-component`, run: 
    
    
    [gcloud design-center spaces application-templates components](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components) connections create my-connection --component=my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --destination-component-uri=other-component

Or run: 
    
    
    [gcloud design-center spaces application-templates components](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components) connections create my-connection --component=my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --destination-component-uri=projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template/components/other-component

Or run: 
    
    
    [gcloud design-center spaces application-templates components](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components) connections create projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template/components/my-component/connections/my-connection --destination-component-uri=projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template/components/other-component

To create the connection `my-connection` with a parameter key-value pair of `type:connection-type` in component `my-component` of application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1` with a destination component `other-component`, run the following shorthand example: 
    
    
    [gcloud design-center spaces application-templates components](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components) connections create my-connection --component=my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --destination-component-uri=other-component --parameters=key=type,value=connection-type

Or run the following JSON example: 
    
    
    [gcloud design-center spaces application-templates components](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components) connections create my-connection --component=my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --destination-component-uri=other-component --parameters='[{"key": "type", "value": "connection-type"}]'

Or create a YAML or JSON file with the parameters and run the following file example: 
    
    
    [gcloud design-center spaces application-templates components](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/components) connections create my-connection --component=my-component --application-template=my-app-template --space=my-space --project=my-project --location=us-central1 --destination-component-uri=other-component --parameters=my-parameters.yaml

POSITIONAL ARGUMENTS
    

Connection resource - Identifier. The connection name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `connection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `connection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



To set the `space` attribute: 

  * provide the argument `connection` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 



To set the `application-template` attribute: 

  * provide the argument `connection` on the command line with a fully specified name; 
  * provide the argument `--application-template` on the command line. 



This must be specified. 

`CONNECTION`
     ID of the connection or fully qualified identifier for the connection. 

To set the `connection` attribute: 

  * provide the argument `connection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--component`=`COMPONENT`
     The component id of the connection resource. 

To set the `component` attribute: 

  * provide the argument `connection` on the command line with a fully specified name; 
  * provide the argument `--component` on the command line. 


REQUIRED FLAGS
    

Component resource - The destination component URI used to generate the connection. Format is `projects/$project/locations/$location/spaces/$space/applicationTemplates/$application_template/components/$component` This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--destination-component-uri` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--destination-component-uri` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



To set the `space` attribute: 

  * provide the argument `--destination-component-uri` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 



To set the `application-template` attribute: 

  * provide the argument `--destination-component-uri` on the command line with a fully specified name; 
  * provide the argument `--application-template` on the command line. 



This must be specified. 

`--destination-component-uri`=`DESTINATION_COMPONENT_URI`
     ID of the component or fully qualified identifier for the component. 

To set the `component` attribute: 

  * provide the argument `--destination-component-uri` on the command line. 


OPTIONAL FLAGS
    

`--application-template`=`APPLICATION_TEMPLATE`
     For resources [connection, destination-component-uri], provides fallback value for resource application-template attribute. When the resource's full URI path is not provided, application-template will fallback to this flag value. 
`--destination-component-parameters`=[`key`=`KEY`],[`value`=`VALUE`]
     The parameters of the connection associated with the destination component. 

`key`
     The key of the parameter. 
`value`
     The value of the parameter. 
`Shorthand Example:`
    
    
    --destination-component-parameters=key=string,value={…} --destination-component-parameters=key=string,value={…}

`JSON Example:`
    
    
    --destination-component-parameters='[{"key": "string", "value": {…}}]'

`File Example:`
    
    
    --destination-component-parameters=path_to_file.(yaml|json)

`--location`=`LOCATION`
     For resources [connection, destination-component-uri], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--source-component-parameters`=[`key`=`KEY`],[`value`=`VALUE`]
     The parameters of the connection associated with the source component. 

`key`
     The key of the parameter. 
`value`
     The value of the parameter. 
`Shorthand Example:`
    
    
    --source-component-parameters=key=string,value={…} --source-component-parameters=key=string,value={…}

`JSON Example:`
    
    
    --source-component-parameters='[{"key": "string", "value": {…}}]'

`File Example:`
    
    
    --source-component-parameters=path_to_file.(yaml|json)

`--space`=`SPACE`
     For resources [connection, destination-component-uri], provides fallback value for resource space attribute. When the resource's full URI path is not provided, space will fallback to this flag value. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) components connections create

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
