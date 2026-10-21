---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/policies/update/
title: gcloud beta services policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:43.086240+00:00
---

# gcloud beta services policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta services policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta services policies update - update the consumer policy for a project, folder or organization 
SYNOPSIS
    

`gcloud beta services policies update` `--consumer-policy-file`=`CONSUMER_POLICY_FILE` [`--bypass-api-usage-check`] [`--bypass-dependency-check`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update the consumer policy for a project, folder or organization. 
EXAMPLES
     Update the consumer policy 
    
    
    gcloud beta services policies update --consumer-policy-file=/path/to/the/file.yaml

Validate the update action on the policy: 
    
    
    gcloud beta services policies update --consumer-policy-file=/path/to/the/file.yaml --validate-only

Update consumer policy and bypass dependency check: 
    
    
    gcloud beta services policies update --consumer-policy-file=/path/to/the/file.yaml --bypass-dependency-check

Update consumer policy and bypass api usage check: 
    
    
    gcloud beta services policies update --consumer-policy-file=/path/to/the/file.yaml --bypass-api-usage-check

REQUIRED FLAGS
    

`--consumer-policy-file`=`CONSUMER_POLICY_FILE`
     Path to the file that contains the consumer policy in the YAML format. 
OPTIONAL FLAGS
    

`--bypass-api-usage-check`
     If true, the system will bypass usage checks for services that are being removed. If false, the system will check if the service to be removed was used in the last 30 days or enabled in the last 3 days. If so, an error will be returned. 
`--bypass-dependency-check`
     This flag controls dependency management within the consumer policy. If false, dependencies are enforced. When adding a new service, it verifies that all the services dependencies are already present in the policy. When removing a service, the system will ensure that no other services in the policy depend on it. If the policy lacks any required dependencies, the update will not succeed, and an error will be returned. 
`--validate-only`
     Validate the to update action, but don't actually perform it 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha services policies update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/policies/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
