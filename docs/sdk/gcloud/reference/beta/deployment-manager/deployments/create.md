---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/create/
title: gcloud beta deployment-manager deployments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:42.953334+00:00
---

# gcloud beta deployment-manager deployments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/deployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta deployment-manager deployments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta deployment-manager deployments create - create a deployment 
SYNOPSIS
    

`gcloud beta deployment-manager deployments create` `DEPLOYMENT_NAME` (`--composite-type`=`COMPOSITE_TYPE` | `--config`=`CONFIG` | `--template`=`TEMPLATE`) [`--create-policy`=`CREATE_POLICY`; default="create-or-acquire"] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--preview`] [`--properties`=[`PROPERTIES`,…]] [`--async` | `--automatic-rollback-on-error`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command inserts (creates) a new deployment based on a provided config file. 
EXAMPLES
     To create a new deployment from a top-level YAML file, run: 
    
    
    gcloud beta deployment-manager deployments create my-deployment --config=config.yaml --description="My deployment"

To create a new deployment from a top-level template file, run: 
    
    
    [gcloud deployment-manager deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create) my-deployment --template=template.{jinja|py} --properties="string-key:'string-value',integer-key:12345"

To create a new deployment directly from a composite type, run: 
    
    
    [gcloud deployment-manager deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create) my-deployment --composite-type=<project-id>/composite:<type-name> --properties="string-key:'string-value',integer-key:12345"

To preview a deployment without actually creating resources, run: 
    
    
    gcloud beta deployment-manager deployments create my-new-deployment --config=config.yaml --preview

To instantiate a deployment that has been previewed, issue an update command for that deployment without specifying a config file. 

More information is available at <https://cloud.google.com/deployment-manager/docs/configuration/>. 

POSITIONAL ARGUMENTS
    

`DEPLOYMENT_NAME`
     Deployment name. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--composite-type`=`COMPOSITE_TYPE`
     Name of a composite type to deploy. For an example of creating and deploying a composite type, see: <https://cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types#examplecompositetype>
`--config`=`CONFIG`
     Filename of a top-level yaml config that specifies resources to deploy. For a guide to creating a configuration, refer to <https://cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration>
`--template`=`TEMPLATE`
     Filename of a top-level jinja or python config template. 
OPTIONAL FLAGS
    

`--create-policy`=`CREATE_POLICY`; default="create-or-acquire"
     Create policy for resources that have changed in the update. `CREATE_POLICY` must be one of: `acquire`, `create`, `create-or-acquire`. 
`--description`=`DESCRIPTION`
     Optional description of the deployment to insert. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--preview`
     Preview the requested create without actually instantiating the underlying resources. (default=False) 
`--properties`=[`PROPERTIES`,…]
     A comma separated, key:value, map to be used when deploying a template file or composite type directly. 
At most one of these can be specified: 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--automatic-rollback-on-error`
     If the create request results in a deployment with resource errors, delete that deployment immediately after creation. (default=False) 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud deployment-manager deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create)
    
    
    [gcloud alpha deployment-manager deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/deployments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
