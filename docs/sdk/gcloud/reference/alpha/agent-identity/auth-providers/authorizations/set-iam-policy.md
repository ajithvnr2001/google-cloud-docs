---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity/auth-providers/authorizations/set-iam-policy/
title: gcloud alpha agent-identity auth-providers authorizations set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:26:58.475320+00:00
---

# gcloud alpha agent-identity auth-providers authorizations set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity/auth-providers/authorizations/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha agent-identity auth-providers authorizations set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha agent-identity auth-providers authorizations set-iam-policy - set the IAM policy for an Agent Identity authorization 
SYNOPSIS
    

`gcloud alpha agent-identity auth-providers authorizations set-iam-policy` (`AUTHORIZATION` : `--auth-provider`=`AUTH_PROVIDER` `--location`=`LOCATION`) `POLICY_FILE` [`--endpoint-mode`=`ENDPOINT_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command replaces the existing IAM policy for an authorization, given an authorization and a file encoded in JSON or YAML that contains the IAM policy. 
EXAMPLES
     The following command will read an IAM policy defined in a JSON file 'policy.json' and set it for an authorization with identifier 'my-auth' in auth provider 'my-auth-provider' and location 'us-central1': 
    
    
    [gcloud alpha agent-identity auth-providers authorizations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity/auth-providers/authorizations) set-iam-policy my-auth policy.json --auth-provider=my-auth-provider --location=us-central1

POSITIONAL ARGUMENTS
    

Authorization resource - The authorization for which to set the IAM policy. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `authorization` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`AUTHORIZATION`
     ID of the authorization or fully qualified identifier for the authorization. 

To set the `authorization` attribute: 

  * provide the argument `authorization` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--auth-provider`=`AUTH_PROVIDER`
     The authProvider id of the authorization resource. 

To set the `auth-provider` attribute: 

  * provide the argument `authorization` on the command line with a fully specified name; 
  * provide the argument `--auth-provider` on the command line. 


`--location`=`LOCATION`
     The location id of the authorization resource. 

To set the `location` attribute: 

  * provide the argument `authorization` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

FLAGS
    

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
     This command uses the `agentidentity/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/docs/>
REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta agent-identity auth-providers authorizations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/agent-identity/auth-providers/authorizations) set-iam-policy

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
