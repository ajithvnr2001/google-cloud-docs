---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/intercept-deployments/create/
title: gcloud alpha network-security intercept-deployments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:56:55.510991+00:00
---

# gcloud alpha network-security intercept-deployments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/intercept-deployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-security intercept-deployments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-security intercept-deployments create - create an Intercept Deployment 
SYNOPSIS
    

`gcloud alpha network-security intercept-deployments create` (`INTERCEPT_DEPLOYMENT` : `--location`=`LOCATION`) (`--forwarding-rule`=`FORWARDING_RULE` : `--forwarding-rule-location`=`FORWARDING_RULE_LOCATION`) (`--intercept-deployment-group`=`INTERCEPT_DEPLOYMENT_GROUP` : `--intercept-deployment-group-location`=`INTERCEPT_DEPLOYMENT_GROUP_LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--max-wait`=`MAX_WAIT`; default="20m"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an intercept deployment. Successful creation of a deployment results in a deployment in ACTIVE state. Check the progress of deployment creation by using `[gcloud network-security intercept-deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/list)`. 

For more examples, refer to the EXAMPLES section below. 

EXAMPLES
     To create an intercept deployment called `my-deployment`, in project ID `my-project` and zone `us-central1-a`, run:
    
    
    gcloud alpha network-security intercept-deployments create my-deployment --project=my-project --location=us-central1-a --deployment-group-location=global --forwarding-rule=my-forwarding-rule --forwarding-rule-location=us-central1 --intercept-deployment-group=my-deployment-group

OR 
    
    
    gcloud alpha network-security intercept-deployments create my-deployment --project=my-project --location=us-central1-a --forwarding-rule=projects/my-project/regions/us-central1/forwardingRules/my-forwarding-rule --intercept-deployment-group=projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group

OR 
    
    
    gcloud alpha network-security intercept-deployments create projects/my-project/locations/us-central1/interceptDeployments/my-deployment --forwarding-rule=projects/my-project/regions/us-central1/forwardingRules/my-forwarding-rule --intercept-deployment-group=projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group

OR 
    
    
    gcloud alpha network-security intercept-deployments create projects/my-project/locations/us-central1/interceptDeployments/my-deployment --forwarding-rule=projects/my-project/regions/us-central1/forwardingRules/my-forwarding-rule --intercept-deployment-group=projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group --description="my-description"

POSITIONAL ARGUMENTS
    

Intercept deployment resource - Intercept Deployment. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `INTERCEPT_DEPLOYMENT` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INTERCEPT_DEPLOYMENT`
     ID of the intercept deployment or fully qualified identifier for the intercept deployment. 

To set the `deployment-id` attribute: 

  * provide the argument `INTERCEPT_DEPLOYMENT` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the intercept deployment. 

To set the `location` attribute: 

  * provide the argument `INTERCEPT_DEPLOYMENT` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

ForwardingRule resource - Intercept Deployment Forwarding Rule. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--forwarding-rule` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--forwarding-rule`=`FORWARDING_RULE`
     ID of the forwardingRule or fully qualified identifier for the forwardingRule. 

To set the `forwarding-rule-id` attribute: 

  * provide the argument `--forwarding-rule` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--forwarding-rule-location`=`FORWARDING_RULE_LOCATION`
     The Cloud region for the forwardingRule. 

To set the `forwarding-rule-location` attribute: 

  * provide the argument `--forwarding-rule` on the command line with a fully specified name; 
  * provide the argument `--forwarding-rule-location` on the command line. 


Intercept deployment group resource - Intercept Deployment Group. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--intercept-deployment-group` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--intercept-deployment-group`=`INTERCEPT_DEPLOYMENT_GROUP`
     ID of the intercept deployment group or fully qualified identifier for the intercept deployment group. 

To set the `id` attribute: 

  * provide the argument `--intercept-deployment-group` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--intercept-deployment-group-location`=`INTERCEPT_DEPLOYMENT_GROUP_LOCATION`
     Location of the intercept deployment group. 

To set the `location` attribute: 

  * provide the argument `--intercept-deployment-group` on the command line with a fully specified name; 
  * provide the argument `--intercept-deployment-group-location` on the command line; 
  * provide the argument `networksecurity.projects.locations.interceptDeployments` on the command line with a fully specified name. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Description of the deployment. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--max-wait`=`MAX_WAIT`; default="20m"
     Time to synchronously wait for the operation to complete, after which the operation continues asynchronously. Ignored if --no-async isn't specified. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud network-security intercept-deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/create)
    
    
    [gcloud beta network-security intercept-deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/intercept-deployments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
