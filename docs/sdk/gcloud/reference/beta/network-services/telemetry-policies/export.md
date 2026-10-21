---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/export/
title: gcloud beta network-services telemetry-policies export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:50:43.786452+00:00
---

# gcloud beta network-services telemetry-policies export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-services telemetry-policies export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-services telemetry-policies export - export a TelemetryPolicy 
SYNOPSIS
    

`gcloud beta network-services telemetry-policies export` (`TELEMETRY_POLICY` : `--location`=`LOCATION`) [`--destination`=`DESTINATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Export a TelemetryPolicy. 
EXAMPLES
     To export a TelemetryPolicy named 'my-telemetry-policy' to a YAML file, run: 
    
    
    gcloud beta network-services telemetry-policies export my-telemetry-policy --destination=my-telemetry-policy.yaml --location=global

POSITIONAL ARGUMENTS
    

Telemetry policy resource - Name of the telemetry policy to export. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `telemetry_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TELEMETRY_POLICY`
     ID of the telemetry policy or fully qualified identifier for the telemetry policy. 

To set the `telemetry_policy` attribute: 

  * provide the argument `telemetry_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. 

To set the `location` attribute: 

  * provide the argument `telemetry_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--destination`=`DESTINATION`
     Path to a YAML file where the configuration will be exported. The exported data will not contain any output-only fields. Alternatively, you may omit this flag to write to standard output. For a schema describing the export/import format, see $CLOUDSDKROOT/lib/googlecloudsdk/schemas/… 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha network-services telemetry-policies export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/telemetry-policies/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
