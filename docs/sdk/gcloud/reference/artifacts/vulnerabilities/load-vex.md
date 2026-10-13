---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex/
title: gcloud artifacts vulnerabilities load-vex \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:19.067932+00:00
---

# gcloud artifacts vulnerabilities load-vex  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts vulnerabilities load-vex Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts vulnerabilities load-vex - load VEX data from a CSAF file into Artifact Analysis 
SYNOPSIS
    

`gcloud artifacts vulnerabilities load-vex` `--source`=`SOURCE` `--uri`=`URI` [`--location`=`LOCATION`] [`--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Command loads VEX data from a Common Security Advisory Framework (CSAF) file into Artifact Analysis as VulnerabilityAssessment Notes. VEX data tells Artifact Analysis whether vulnerabilities are relevant and how. 
EXAMPLES
     To load a CSAF security advisory file given an artifact in Artifact Registry and the file on disk, run: 
    
    
    gcloud artifacts vulnerabilities load-vex --uri=us-east1-docker.pkg.dev/project123/repository123/someimage@sha256:49765698074d6d7baa82f --source=/path/to/vex/file

To load a CSAF security advisory file given an artifact with a tag and a file on disk, run: 
    
    
    gcloud artifacts vulnerabilities load-vex --uri=us-east1-docker.pkg.dev/project123/repository123/someimage:latest --source=/path/to/vex/file

REQUIRED FLAGS
    

`--source`=`SOURCE`
     The path of the VEX file. 
`--uri`=`URI`
     The path of the artifact in Artifact Registry. A 'gcr.io' image can also be used if redirection is enabled in Artifact Registry. Make sure 'artifactregistry.projectsettings.get' permission is granted to the current gcloud user to verify the redirection status. 
OPTIONAL FLAGS
    

`--location`=`LOCATION`
     If specified, all requests to Artifact Analysis for occurrences will go to location specified 
`--project`=`PROJECT`
     The parent project to load security advisory into. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
