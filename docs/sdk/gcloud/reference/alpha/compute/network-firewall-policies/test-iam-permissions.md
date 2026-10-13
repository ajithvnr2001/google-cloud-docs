---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/test-iam-permissions/
title: gcloud alpha compute network-firewall-policies test-iam-permissions \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:11.350665+00:00
---

# gcloud alpha compute network-firewall-policies test-iam-permissions  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies/test-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute network-firewall-policies test-iam-permissions Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute network-firewall-policies test-iam-permissions - test IAM permissions for a Compute Engine network firewall policy 
SYNOPSIS
    

`gcloud alpha compute network-firewall-policies test-iam-permissions` `FIREWALL_POLICY` `--permissions`=[`PERMISSIONS`,…] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Returns permissions that a caller has on the specified network firewall policy. 
EXAMPLES
     To test if the caller has 'compute.firewallPolicies.get' permission on a network firewall policy `my-policy`, run: 
    
    
    [gcloud alpha compute network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies) test-iam-permissions my-policy --permissions=compute.firewallPolicies.get

POSITIONAL ARGUMENTS
    

Firewall policy resource - The network firewall policy for which to test permissions. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `firewall_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FIREWALL_POLICY`
     ID of the firewall_policy or fully qualified identifier for the firewall_policy. 

To set the `firewall_policy` attribute: 

  * provide the argument `firewall_policy` on the command line. 


REQUIRED FLAGS
    

`--permissions`=[`PERMISSIONS`,…]
     The permissions to test. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute network-firewall-policies test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/test-iam-permissions)
    
    
    [gcloud beta compute network-firewall-policies test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies/test-iam-permissions)
    
    
    [gcloud preview compute network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies) test-iam-permissions

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
