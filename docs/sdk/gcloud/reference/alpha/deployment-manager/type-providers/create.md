---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/type-providers/create/
title: gcloud alpha deployment-manager type-providers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:51:13.975997+00:00
---

# gcloud alpha deployment-manager type-providers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager/type-providers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha deployment-manager type-providers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha deployment-manager type-providers create - create a type provider 
SYNOPSIS
    

`gcloud alpha deployment-manager type-providers create` `PROVIDER_NAME` `--descriptor-url`=`DESCRIPTOR_URL` [`--api-options-file`=`API_OPTIONS_FILE`] [`--async`] [`--custom-certificate-authority-roots`=`CA_ROOT`,[`CA_ROOT`,…]] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command inserts (creates) a new type provider based on a provided configuration file. 
EXAMPLES
     To create a new type provider, run: 
    
    
    gcloud alpha deployment-manager type-providers create my-type-provider --api-options-file=my-options.yaml --descriptor-url=<descriptor URL> --description="My type."

POSITIONAL ARGUMENTS
    

`PROVIDER_NAME`
     Type provider name or URI. 
REQUIRED FLAGS
    

`--descriptor-url`=`DESCRIPTOR_URL`
     URL of API of your type. 
OPTIONAL FLAGS
    

`--api-options-file`=`API_OPTIONS_FILE`
     YAML file with options for the API: e.g. options and collection overrides. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--custom-certificate-authority-roots`=`CA_ROOT`,[`CA_ROOT`,…]
     Comma-separated list of CA root certificates to use when connecting to the type's API by HTTPS. 
`--description`=`DESCRIPTION`
     Optional description of the type provider. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta deployment-manager type-providers create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager/type-providers/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
