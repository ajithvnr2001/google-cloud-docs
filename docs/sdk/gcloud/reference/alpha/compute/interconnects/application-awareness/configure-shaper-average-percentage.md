---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/application-awareness/configure-shaper-average-percentage/
title: gcloud alpha compute interconnects application-awareness configure-shaper-average-percentage \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:54:42.416586+00:00
---

# gcloud alpha compute interconnects application-awareness configure-shaper-average-percentage  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/application-awareness/configure-shaper-average-percentage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute interconnects application-awareness configure-shaper-average-percentage Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute interconnects application-awareness configure-shaper-average-percentage - configure shaper average percentage for application awareness configuration of a Compute Engine interconnect 
SYNOPSIS
    

`gcloud alpha compute interconnects application-awareness configure-shaper-average-percentage` `NAME` `--bandwidth-percentages`=[`TC1`=`TC1`],[`TC2`=`TC2`],[`TC3`=`TC3`],[`TC4`=`TC4`],[`TC5`=`TC5`],[`TC6`=`TC6`] [`--enabled`] [`--profile-description`=`PROFILE_DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute interconnects application-awareness configure-shaper-average-percentage` is used to configure shaper average percentage for using application awareness on interconnect. Note that an application awareness policy (strict priority or bandwidth percentage) should be configure before configuring traffic shaping. 

For an example, refer to the `EXAMPLES` section below. 

EXAMPLES
     To configure shaper average percentage for an interconnect example-interconnect, run: 
    
    
    [gcloud alpha compute interconnects application-awareness](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/application-awareness) configure-shaper-average-percentage example-interconnect --bandwidth-percentages="TC1=30,TC2=90
    --enabled --profile-description="some string"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect to patch. 
REQUIRED FLAGS
    

`--bandwidth-percentages`=[`TC1`=`TC1`],[`TC2`=`TC2`],[`TC3`=`TC3`],[`TC4`=`TC4`],[`TC5`=`TC5`],[`TC6`=`TC6`]
     A list of bandwidth percentages, for configuring the bandwidth percentage policy or traffic shaping. 

For configuring bandwidth percentages for the bandwidth percentage policy: 

1\. Each bandwidth percentage value must be an integer between 1-100. 2. It is required to provide a percentage value for each class. 3. The sum of all bandwidth percentages must be 100. 

For configuring bandwidth percentages for traffic shaping: 

1\. Each bandwidth percentage value must be an integer between 1-100. 2. It is not required to provide a percentage value for each class. 3. The sum of all bandwidth percentages does not need to be 100. 

OPTIONAL FLAGS
    

`--enabled`
     Enable or disable application awareness on the interconnect. Application awareness enablement will fail if the application awareness configuration is not specified. Use --no-enabled to disable it. 
`--profile-description`=`PROFILE_DESCRIPTION`
     Add profile description for application awareness. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute interconnects application-awareness](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/application-awareness) configure-shaper-average-percentage
    
    
    [gcloud beta compute interconnects application-awareness](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/application-awareness) configure-shaper-average-percentage
    
    
    [gcloud preview compute interconnects application-awareness](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/application-awareness) configure-shaper-average-percentage

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
