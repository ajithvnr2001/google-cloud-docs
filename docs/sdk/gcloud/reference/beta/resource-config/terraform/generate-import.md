---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-config/terraform/generate-import/
title: gcloud beta resource-config terraform generate-import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:49.197558+00:00
---

# gcloud beta resource-config terraform generate-import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-config/terraform/generate-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta resource-config terraform generate-import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta resource-config terraform generate-import - generate Terraform import script for exported resources 
SYNOPSIS
    

`gcloud beta resource-config terraform generate-import` `INPUT_PATH` [`--output-dir`=`OUTPUT_DIR` | `--output-module-file`=`OUTPUT_MODULE_FILE` `--output-script-file`=`OUTPUT_SCRIPT_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Generate Terraform import script for exported resources. 
EXAMPLES
     To generate an import script named `import.sh` and a module file named `modules.tf` based on exported files in `my-dir/`, run: 
    
    
    gcloud beta resource-config terraform generate-import my-dir/ --output-script-file=import.sh --output-module-file=modules.tf

To generate an import script with the default `terraform_import_YYYYMMDD-HH-MM-SS.cmd` and `gcloud-export-modules.tf` names on Windows, based on exported files in `my-dir/`, run: 
    
    
    gcloud beta resource-config terraform generate-import my-dir

POSITIONAL ARGUMENTS
    

`INPUT_PATH`
     Path to a Terrafrom formatted (.tf) resource file or directory of files exported via. `[gcloud alpha resource-config bulk-export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-config/bulk-export)` or resource surface specific `config export` command. 
OUTPUT DESTINATION FLAGS
    

Specify the destination of the generated script. 

At most one of these can be specified: 

`--output-dir`=`OUTPUT_DIR`
     Specify the output directory only for the generated import script. If specified directory does not exists it will be created. Generated script will have a default name of the form `terraform_import_YYYYMMDD-HH-MM-SS.sh|cmd`
Or at least one of these can be specified: 

Specify the exact filenames for the output import script and module files. 
`--output-module-file`=`OUTPUT_MODULE_FILE`
     Specify the full path path for generated terraform module file. If not set, a default filename of `gcloud-export-modules.tf` will be generated. 
`--output-script-file`=`OUTPUT_SCRIPT_FILE`
     Specify the full path path for generated import script. If not set, a default filename of the form `terraform_import_YYYYMMDD-HH-MM-SS.sh|cmd` will be generated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha resource-config terraform generate-import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-config/terraform/generate-import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
