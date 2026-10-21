---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/list/
title: gcloud alpha access-context-manager cloud-bindings list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:04.677608+00:00
---

# gcloud alpha access-context-manager cloud-bindings list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha access-context-manager cloud-bindings list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha access-context-manager cloud-bindings list - list cloud access bindings under an organization 
SYNOPSIS
    

`gcloud alpha access-context-manager cloud-bindings list` [`--organization`=`ORGANIZATION`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List cloud access bindings. 

By default, this command returns only user bindings (Google Groups). 

To return service account bindings, set `--filter` to `principal:serviceAccount OR principal:serviceAccountProjectNumber`. 

To return federated principal bindings (workforce or workload identities), set `--filter` to `principal:federatedPrincipal`. 

EXAMPLES
     To list cloud access bindings, run the following command: 
    
    
    gcloud alpha access-context-manager cloud-bindings list

This command prints a list of Google Cloud user access bindings, `gcpUserAccessBindings`, in YAML format. By default, the binding is printed in the following format: 
    
    
    ---
    accessLevels:
    - accessPolicies/9522/accessLevels/device_trusted
    dryRunAccessLevels:
    - accessPolicies/9522/accessLevels/specific_location
    groupKey: a3dad
    name: organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N
    sessionSettings:
      sessionLength: 57600s
      sessionLengthEnabled: true
      sessionReauthMethod: LOGIN

Or 
    
    
    ---
    accessLevels:
    - accessPolicies/9522/accessLevels/device_trusted
    dryRunAccessLevels:
    - accessPolicies/9522/accessLevels/specific_location
    groupKey: a3dad
    name: organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N
    scopedAccessSettings:
    - activeSettings:
        accessLevels:
        - accessPolicies/9522/accessLevels/device_trusted
      dryRunSettings:
        accessLevels:
        - accessPolicies/9522/accessLevels/specific_location
      scope:
        clientScope:
          restrictedClientApplication:
            clientId: 123.apps.googleusercontent.com
    - activeSettings:
        accessLevels:
        - accessPolicies/9522/accessLevels/device_trusted
      dryRunSettings:
        accessLevels:
        - accessPolicies/9522/accessLevels/specific_location
      scope:
        clientScope:
          restrictedClientApplication:
            name: Cloud Console
    - activeSettings:
        sessionSettings:
          sessionLength: 57600s
          sessionLengthEnabled: true
          sessionReauthMethod: LOGIN
      scope:
        clientScope:
          restrictedClientApplication:
            clientId: 123.apps.googleusercontent.com
    sessionSettings:
      sessionLength: 57600s
      sessionLengthEnabled: true
      sessionReauthMethod: LOGIN

If filter is specified as `principal:serviceAccount OR principal:serviceAccountProjectNumber`, the output is printed in the following format: 
    
    
    ---
    accessLevels:
    - accessPolicies/9522/accessLevels/device_trusted
    dryRunAccessLevels:
    - accessPolicies/9522/accessLevels/specific_location
    principal:
    serviceAccount: service_account@project.iam.gserviceaccount.com
    name: organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N

Or 
    
    
    ---
    accessLevels:
    - accessPolicies/9522/accessLevels/device_trusted
    dryRunAccessLevels:
    - accessPolicies/9522/accessLevels/specific_location
    principal:
    serviceAccountProjectNumber: 123456789
    name: organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N

If filter is specified as `principal:federatedPrincipal`, the output is printed in the following format for a workload identity: 
    
    
    ---
    accessLevels:
    - accessPolicies/9522/accessLevels/device_trusted
    dryRunAccessLevels:
    - accessPolicies/9522/accessLevels/specific_location
    principal:
      federatedPrincipal: principal://iam.googleapis.com/projects/123/locations/global/workloadIdentityPools/pool-id/subject/subject-id
    name: organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N

Or for all workforce pools in an organization with project-scoped session settings: 
    
    
    ---
    name: organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N
    principal:
      federatedPrincipal: principalSet://cloudresourcemanager.googleapis.com/organizations/256/type/WorkforcePool
    scopedAccessSettings:
    - activeSettings:
        sessionSettings:
          sessionLength: 7776000s
          sessionLengthEnabled: true
          sessionReauthMethod: LOGIN
      scope:
        clientScope:
          restrictedProject:
            name: projects/1234567890

FLAGS
    

Organization resource - The parent organization of the bindings you want to list. This represents a Cloud resource. 
`--organization`=`ORGANIZATION`
     ID of the organization or fully qualified identifier for the organization. 

To set the `organization` attribute: 

  * provide the argument `--organization` on the command line; 
  * set the property `access_context_manager/organization`. 


LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud access-context-manager cloud-bindings list](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
