---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/policy-bindings/create/
title: gcloud alpha software-delivery-trust policy-bindings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:44.234571+00:00
---

# gcloud alpha software-delivery-trust policy-bindings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/policy-bindings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha software-delivery-trust policy-bindings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha software-delivery-trust policy-bindings create - create a Software Delivery Trust policy binding 
SYNOPSIS
    

`gcloud alpha software-delivery-trust policy-bindings create` `POLICY_BINDING` `--enforcement-mode`=`ENFORCEMENT_MODE` `--resource-selectors`=[`matchPattern`=`MATCHPATTERN`],[`path`=`PATH`] [`--async`] [`--custom-gate`=`CUSTOM_GATE`] [`--location`=`LOCATION`] [`--policy`=`POLICY`] [`--policy-revision`=`POLICY_REVISION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Bind a policy to target deployment resources with an enforcement mode (e.g. DRY_RUN or DENY). 
EXAMPLES
     To create policy binding 'prod-gke-binding' linking policy 'require-slsa-build' to a GKE cluster in location 'us-central1', run: 
    
    
    gcloud alpha software-delivery-trust policy-bindings create prod-gke-binding --location=us-central1 --policy=projects/my-project/locations/us-central1/policies/require-slsa-build --enforcement-mode=DENY --resource-selectors="path=//container.googleapis.com/projects/my-project/locations/us-central1/clusters/prod-cluster,matchPattern=EXACT"

POSITIONAL ARGUMENTS
    

PolicyBinding resource - Identifier. Unique resource name of the binding. Example: "projects/123456789/locations/global/policyBindings/prod-cluster-binding". This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy_binding` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `policy_binding` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`POLICY_BINDING`
     ID of the policyBinding or fully qualified identifier for the policyBinding. 

To set the `policy_binding` attribute: 

  * provide the argument `policy_binding` on the command line. 


REQUIRED FLAGS
    

`--enforcement-mode`=`ENFORCEMENT_MODE`
     How the policy is enforced. `ENFORCEMENT_MODE` must be one of: 

`enforcement-mode-deny`
     Actively block non-compliant operations. 
`enforcement-mode-log-only`
     Log violations but do not block operations. 
`--resource-selectors`=[`matchPattern`=`MATCHPATTERN`],[`path`=`PATH`]
     Required, Target resources this binding applies to. 

`matchPattern`
     Enforced match pattern type. 
`path`
     Full resource path string to match. Supported patterns must match one of the following API surfaces in MVP: 1. GKE Clusters: "//container.googleapis.com/projects/{project}/locations/{location}/clusters/{cluster}" 2\. Cloud Run Services: "//run.googleapis.com/projects/{project}/locations/{location}/services/{service}" 3\. Skill Registry: "//aiplatform.googleapis.com/projects/{project}/locations/{location}/skills/{skill}". 
`Shorthand Example:`
    
    
    --resource-selectors=matchPattern=string,path=string --resource-selectors=matchPattern=string,path=string

`JSON Example:`
    
    
    --resource-selectors='[{"matchPattern": "string", "path": "string"}]'

`File Example:`
    
    
    --resource-selectors=path_to_file.(yaml|json)

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--custom-gate`=`CUSTOM_GATE`
     Custom lifecycle gate for which this policy binding applies (e.g., "staging-deploy", "prod-release"). 
`--location`=`LOCATION`
     For resources [policy, policy-revision, policy_binding], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--policy`=`POLICY`
     For resources [policy, policy-revision], provides fallback value for resource policy attribute. When the resource's full URI path is not provided, policy will fallback to this flag value. 
Arguments for the policy reference. 
Revision resource - Reference to a specific pinned PolicyRevision. Example: "projects/my-project/locations/us-central1/policies/deny-critical-vulns/revisions/a1b2c3d4" This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--policy-revision` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--policy-revision` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



To set the `policy` attribute: 

  * provide the argument `--policy-revision` on the command line with a fully specified name; 
  * provide the argument `--policy` on the command line. 


`--policy-revision`=`POLICY_REVISION`
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `--policy-revision` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `softwaredeliverytrust/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
