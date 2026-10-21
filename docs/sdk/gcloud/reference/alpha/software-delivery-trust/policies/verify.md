---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/policies/verify/
title: gcloud alpha software-delivery-trust policies verify \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:25:29.089303+00:00
---

# gcloud alpha software-delivery-trust policies verify  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/policies/verify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha software-delivery-trust policies verify Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha software-delivery-trust policies verify - verify policies against a target resource and software artifact 
SYNOPSIS
    

`gcloud alpha software-delivery-trust policies verify` `--location`=`LOCATION` `--subject-digest`=`SUBJECT_DIGEST` `--subject-url`=`SUBJECT_URL` `--target-resource`=`TARGET_RESOURCE` [`--custom-gate`=`CUSTOM_GATE`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Verify Software Delivery Trust policies in a given project and location against a target resource and artifact digest. 
EXAMPLES
     To verify policies in location 'us-central1' for a container image: 
    
    
    # gcloud-disable-gdu-domain
    gcloud alpha software-delivery-trust policies verify --location=us-central1 --target-resource="//container.googleapis.com/projects/my-project/locations/us-central1/clusters/prod-cluster" --subject-url="us-central1-docker.pkg.dev/my-project/my-repo/my-app" --subject-digest="sha256:82a15998df9a8fa9b" --custom-gate="prod-release"

REQUIRED FLAGS
    

Location resource - Parent location to evaluate policies in. Example: "projects/123456789/locations/global". This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


`--subject-digest`=`SUBJECT_DIGEST`
     Immutable cryptographic digest of the software artifact. Example: "sha256:82a15998df9a8fa9b" 
`--subject-url`=`SUBJECT_URL`
     The artifact URL. Example: "us-central1-docker.pkg.dev/my-project/my-repo/app" 
`--target-resource`=`TARGET_RESOURCE`
    
gcloud-disable-gdu-domain
     Full resource URI of the target resource being gated. Example: "//artifactregistry.googleapis.com/projects/my-project/locations/us-central1/repositories/my-repo" 
OPTIONAL FLAGS
    

`--custom-gate`=`CUSTOM_GATE`
     Optional lifecycle gate identifier for filtering policy bindings (e.g. 'prod-release' or 'staging-deploy'). 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `softwaredeliverytrust/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/>
REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
