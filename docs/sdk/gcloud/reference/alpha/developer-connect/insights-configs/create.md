---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/insights-configs/create/
title: gcloud alpha developer-connect insights-configs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:27.623119+00:00
---

# gcloud alpha developer-connect insights-configs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/insights-configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha developer-connect insights-configs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha developer-connect insights-configs create - create an insight config 
SYNOPSIS
    

`gcloud alpha developer-connect insights-configs create` (`INSIGHTS_CONFIG` : `--location`=`LOCATION`) [`--artifact-config`=`ARTIFACT_CONFIG_ITEM`] [`--app-hub-application`=`APP_HUB_APPLICATION` | `--target-projects`=[`TARGET_PROJECTS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an insights config. 
EXAMPLES
     To create an insights config with an apphub application, run: 
    
    
    gcloud alpha developer-connect insights-configs create insights-config-name --app-hub-application=projects/my-project/locations/us-central1/applications/my-app-hub-application

To create an insights config with projects, run: 
    
    
    gcloud alpha developer-connect insights-configs create insights-config-name --target-projects=project1,project2

POSITIONAL ARGUMENTS
    

Insights config resource - The insights config to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `insights_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSIGHTS_CONFIG`
     ID of the insights_config or fully qualified identifier for the insights_config. 

To set the `insightsConfigs` attribute: 

  * provide the argument `insights_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The region of the insight config. 

To set the `location` attribute: 

  * provide the argument `insights_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--artifact-config`=`ARTIFACT_CONFIG_ITEM`
     Specifies a single artifact configuration. This flag can be repeated for multiple configurations. 

Each configuration can be provided in a key-value format. 

Format examples: `--artifact-config=uri={REGION}-docker.pkg.dev/my-project/my-repo/my-image,buildProject=my-project` `--artifact-config=[uri={REGION}-docker.pkg.dev/my-project/my-repo/my-image,buildProject=my-project]`

Supported keys within a configuration: 

  * `buildProject`: String, e.g., `my-project`
  * `uri`: String, e.g., `{REGION}-docker.pkg.dev/my-project/my-repo/my-image`


At most one of these can be specified: 

`--app-hub-application`=`APP_HUB_APPLICATION`
     The App Hub application to which the insight config is associated. 
`--target-projects`=[`TARGET_PROJECTS`,…]
     A comma-separated list of target project IDs/numbers to which the insight config is associated. 

Format examples: `--target-projects=123567890,my-project` `--target-projects=projects/1234567890,projects/my-project`

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud developer-connect insights-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/insights-configs/create)
    
    
    [gcloud beta developer-connect insights-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-connect/insights-configs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
