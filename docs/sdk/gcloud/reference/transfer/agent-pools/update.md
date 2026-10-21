---
url: https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update/
title: gcloud transfer agent-pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:10.027738+00:00
---

# gcloud transfer agent-pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud transfer agent-pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud transfer agent-pools update - update a Transfer Service agent pool 
SYNOPSIS
    

`gcloud transfer agent-pools update` `NAME` [`--bandwidth-limit`=`BANDWIDTH_LIMIT`] [`--clear-bandwidth-limit`] [`--clear-display-name`] [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an agent pool. 
EXAMPLES
     To remove the bandwidth limit for agent pool 'foo', run: 
    
    
    gcloud transfer agent-pools update foo --clear-bandwidth-limit

To remove the display name for agent pool 'foo', run: 
    
    
    gcloud transfer agent-pools update foo --clear-display-name

To update the bandwidth limit for agent pool 'foo' to 100 MB/s, run: 
    
    
    gcloud transfer agent-pools update foo --bandwidth-limit=100

To update the display name for agent pool 'foo' to 'example name', run: 
    
    
    gcloud transfer agent-pools update foo --display-name="example name"

POSITIONAL ARGUMENTS
    

`NAME`
     A unique, permanent identifier for this pool. 
FLAGS
    

`--bandwidth-limit`=`BANDWIDTH_LIMIT`
     Set how much of your bandwidth to make available to this pool's agents. A bandwidth limit applies to all agents in a pool and can help prevent the pool's transfer workload from disrupting other operations that share your bandwidth. For example, enter '50' to set a bandwidth limit of 50 MB/s. By leaving this flag unspecified, this flag unspecified, this pool's agents will use all bandwidth available to them. 
`--clear-bandwidth-limit`
     Remove the agent pool's bandwidth limit, which enables the pool's agents to use all bandwidth available to them. 
`--clear-display-name`
     Remove the display name from the agent pool. 
`--display-name`=`DISPLAY_NAME`
     A modifiable name to help you identify this pool. You can include details that might not fit in the pool's unique full resource name. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha transfer agent-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/agent-pools/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
