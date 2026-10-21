---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/policies/update/
title: gcloud alpha design-center spaces application-templates policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:02:29.737201+00:00
---

# gcloud alpha design-center spaces application-templates policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha design-center spaces application-templates policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha design-center spaces application-templates policies update - update a policy 
SYNOPSIS
    

`gcloud alpha design-center spaces application-templates policies update` (`POLICY` : `--application-template`=`APPLICATION_TEMPLATE` `--location`=`LOCATION` `--space`=`SPACE`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--policy-type`=`POLICY_TYPE`] [`--apply-conditions`=[`conditionKey`=`CONDITIONKEY`],[`conditionValue`=`CONDITIONVALUE`] | `--add-apply-conditions`=[`conditionKey`=`CONDITIONKEY`],[`conditionValue`=`CONDITIONVALUE`] `--clear-apply-conditions` | `--remove-apply-conditions`=[`conditionKey`=`CONDITIONKEY`],[`conditionValue`=`CONDITIONVALUE`]] [`--policy-revision-uri`=`POLICY_REVISION_URI` | `--policy-uri`=`POLICY_URI`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a policy for an application template. 
EXAMPLES
     To update the display name to `My New Policy Name` for the policy `my-policy` in application template `my-template` and space `my-space`, run: 
    
    
    [gcloud alpha design-center spaces application-templates policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates/policies) update my-policy --application-template=my-template --space=my-space --project=my-project --location=us-central1 --display-name="My New Policy Name"

POSITIONAL ARGUMENTS
    

Policy resource - Identifier. The policy name in the following format: `projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate/policies/$policy` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`POLICY`
     ID of the policy or fully qualified identifier for the policy. 

To set the `policy` attribute: 

  * provide the argument `policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--application-template`=`APPLICATION_TEMPLATE`
     The applicationTemplate id of the policy resource. 

To set the `application-template` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--application-template` on the command line. 


`--location`=`LOCATION`
     The location id of the policy resource. 

To set the `location` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The space id of the policy resource. 

To set the `space` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     The policy description. 
`--display-name`=`DISPLAY_NAME`
     The policy display name. 
`--policy-type`=`POLICY_TYPE`
     The policy type. Policy type is used to determine the domain of the policy. `POLICY_TYPE` must be (only one value is supported): 

`compliance-framework`
     Compliance framework policy. 
Update apply_conditions. 

At most one of these can be specified: 

`--apply-conditions`=[`conditionKey`=`CONDITIONKEY`],[`conditionValue`=`CONDITIONVALUE`]
     Set apply_conditions to new value. Conditions for applying the policy. Condition accepts the `criticality` and `environment` parameters from the application template. 

`conditionKey`
     The key of the parameter for the condition. 
`conditionValue`
     The value of the parameter for the condition. 
`Shorthand Example:`
    
    
    --apply-conditions=conditionKey=string,conditionValue=string --apply-conditions=conditionKey=string,conditionValue=string

`JSON Example:`
    
    
    --apply-conditions='[{"conditionKey": "string", "conditionValue": "string"}]'

`File Example:`
    
    
    --apply-conditions=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-apply-conditions`=[`conditionKey`=`CONDITIONKEY`],[`conditionValue`=`CONDITIONVALUE`]
     Add new value to apply_conditions list. Conditions for applying the policy. Condition accepts the `criticality` and `environment` parameters from the application template. 

`conditionKey`
     The key of the parameter for the condition. 
`conditionValue`
     The value of the parameter for the condition. 
`Shorthand Example:`
    
    
    --add-apply-conditions=conditionKey=string,conditionValue=string --add-apply-conditions=conditionKey=string,conditionValue=string

`JSON Example:`
    
    
    --add-apply-conditions='[{"conditionKey": "string", "conditionValue": "string"}]'

`File Example:`
    
    
    --add-apply-conditions=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-apply-conditions`
     Clear apply_conditions value and set to empty list. 
`--remove-apply-conditions`=[`conditionKey`=`CONDITIONKEY`],[`conditionValue`=`CONDITIONVALUE`]
     Remove existing value from apply_conditions list. Conditions for applying the policy. Condition accepts the `criticality` and `environment` parameters from the application template. 

`conditionKey`
     The key of the parameter for the condition. 
`conditionValue`
     The value of the parameter for the condition. 
`Shorthand Example:`
    
    
    --remove-apply-conditions=conditionKey=string,conditionValue=string --remove-apply-conditions=conditionKey=string,conditionValue=string

`JSON Example:`
    
    
    --remove-apply-conditions='[{"conditionKey": "string", "conditionValue": "string"}]'

`File Example:`
    
    
    --remove-apply-conditions=path_to_file.(yaml|json)

Arguments for the uri. 

At most one of these can be specified: 

`--policy-revision-uri`=`POLICY_REVISION_URI`
     URI of the policy revision. 
`--policy-uri`=`POLICY_URI`
     URI of the policy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1alpha` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
