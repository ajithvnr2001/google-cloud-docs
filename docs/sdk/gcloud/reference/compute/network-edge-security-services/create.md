---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/create/
title: gcloud compute network-edge-security-services create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:59:16.613771+00:00
---

# gcloud compute network-edge-security-services create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute network-edge-security-services create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute network-edge-security-services create - create a Compute Engine network edge security service 
SYNOPSIS
    

`gcloud compute network-edge-security-services create` `NAME` [`--description`=`DESCRIPTION`] [`--region`=`REGION`] [`--security-policy`=`SECURITY_POLICY`] [`--security-policy-region`=`SECURITY_POLICY_REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute network-edge-security-services create` is used to create network edge security services. 
EXAMPLES
     To create a network edge security service with the name 'my-service' in region 'us-central1', run: 
    
    
    gcloud compute network-edge-security-services create my-service --region=us-central1

To create a network edge security service with the name 'my-service' with security policy 'my-policy' attached in region 'us-central1', run: 
    
    
    gcloud compute network-edge-security-services create my-service --security-policy=my-policy --region=us-central1

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the network edge security service to create. 
FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the network edge security service. 
`--region`=`REGION`
     Region of the network edge security service to create. Overrides the default `compute/region` property value for this command invocation. 
`--security-policy`=`SECURITY_POLICY`
     The security policy that will be set for this network edge security service. To remove the policy from this network edge security service set the policy to an empty string. 
`--security-policy-region`=`SECURITY_POLICY_REGION`
     Region of the security policy to operate on. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute network-edge-security-services create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-edge-security-services/create)
    
    
    [gcloud beta compute network-edge-security-services create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-edge-security-services/create)
    
    
    [gcloud preview compute network-edge-security-services create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-edge-security-services/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
