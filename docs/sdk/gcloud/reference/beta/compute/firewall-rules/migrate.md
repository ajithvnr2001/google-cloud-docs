---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-rules/migrate/
title: gcloud beta compute firewall-rules migrate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:00.283177+00:00
---

# gcloud beta compute firewall-rules migrate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-rules/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute firewall-rules migrate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute firewall-rules migrate - create a new Network Firewall Policy and move all customer defined firewall rules there 
SYNOPSIS
    

`gcloud beta compute firewall-rules migrate` `--source-network`=`SOURCE_NETWORK` (`--bind-tags-to-instances` | `--export-exclusion-patterns` | `--export-tag-mapping` | `--target-firewall-policy`=`TARGET_FIREWALL_POLICY`) [`--exclusion-patterns-file`=`EXCLUSION_PATTERNS_FILE`] [`--export-terraform-script`] [`--force`] [`--skip-migrate-target-service-accounts-to-tags`] [`--tag-mapping-file`=`TAG_MAPPING_FILE`] [`--terraform-script-output-file`=`TERRAFORM_SCRIPT_OUTPUT_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute firewall-rules migrate` is used to create a new Network Firewall Policy that contain all rules defined in already existing Network Firewall Policy associated with the given VPC Network and all customer defined VPC Firewall Rules attached to that VPC Network. 
EXAMPLES
     To execute the migration for VPC Network 'my-network' which stores the result in 'my-policy' Network Firewall Policy, run: 
    
    
    gcloud beta compute firewall-rules migrate --source-network=my-network --target-firewall-policy=my-policy

REQUIRED FLAGS
    

`--source-network`=`SOURCE_NETWORK`
     The VPC Network for which the migration should be performed. 
Exactly one of these must be specified: 

`--bind-tags-to-instances`
     If set, migration tool will bind secure tags to the instances with the network tags which match secure tags from the tag mapping file. 
`--export-exclusion-patterns`
     If set, migration tool will dump list of regexes used to filter VPC Firewall out of migration. 
`--export-tag-mapping`
     If set, migration tool will inspect all VPC Firewalls attached to SOURCE_NETWORK, collect all source and target tags, and store them in TAG_MAPPING_FILE. 
`--target-firewall-policy`=`TARGET_FIREWALL_POLICY`
     Name of the new Network Firewall Policy used to store the migration result. 
OPTIONAL FLAGS
    

`--exclusion-patterns-file`=`EXCLUSION_PATTERNS_FILE`
     Path to a file with exclusion patterns used for VPC Firewall filtering. Each regular expression describing a single firewall naming pattern must be placed in a single line. No leading or tailing whitespaces. 
`--export-terraform-script`
     If set, migration tool will output a terraform script to create a Firewall Policy with migrated rules. 
`--force`
     If set, migration will succeed even if the tool detects that original rule evaluation order cannot be preserved. 
`--skip-migrate-target-service-accounts-to-tags`
     If set, migration will keep target service accounts as they are and will not try to replace them with secure tags. 
`--tag-mapping-file`=`TAG_MAPPING_FILE`
     Path to a JSON file with legacy tags and service accounts to secure tags mapping. 
`--terraform-script-output-file`=`TERRAFORM_SCRIPT_OUTPUT_FILE`
     Path to a file where to store generated Terraform script. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha compute firewall-rules migrate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
