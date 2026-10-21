---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/mesh/debug/proxy-config/
title: gcloud alpha container hub mesh debug proxy-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:24:58.644424+00:00
---

# gcloud alpha container hub mesh debug proxy-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/mesh/debug/proxy-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container hub mesh debug proxy-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container hub mesh debug proxy-config - retrieve a configuration summary for a given Envoy instance 
SYNOPSIS
    

`gcloud alpha container hub mesh debug proxy-config` `POD_NAME_NAMESPACE` `--type`=`TYPE` (`--membership`=`MEMBERSHIP` : `--location`=`LOCATION`) [`--fqdn`=`FQDN`] [`--output`=`OUTPUT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Retrieve a configuration summary for a given Envoy instance. 
EXAMPLES
     To retrieve the type cluster config dump for Pod instance pn.default. 

$gcloud alpha container hub mesh debug proxy-config pn.default
    
    
    --type=cluster
    --project=projectId
    --membership=membershipId
    --location=us-central1
    --ouput=yaml

POSITIONAL ARGUMENTS
    

`POD_NAME_NAMESPACE`
     Pod to check against. Use in format of <pod-name[.Namespace]>
REQUIRED FLAGS
    

`--type`=`TYPE`
     Proxy configuration type to retrieve. 
    
    
    bootstrap            Retrieves bootstrap configuration for the Envoy in the specified pod
    clusters/cluster     Retrieves cluster configuration for the Envoy in the specified pod
    endpoints/endpoint   Retrieves endpoint configuration for the Envoy in the specified pod
    listeners/listener   Retrieves listener configuration for the Envoy in the specified pod
    log                  Retrieves logging levels of the Envoy in the specified pod
    routes/route         Retrieves route configuration for the Envoy in the specified pod
    secrets/secret       Retrieves secret configuration for the Envoy in the specified pod

`TYPE` must be one of: `bootstrap`, `cluster`, `clusters`, `endpoint`, `endpoints`, `listener`, `listeners`, `log`, `route`, `routes`, `secret`, `secrets`. 

Membership resource - The group of arguments defining a membership. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--membership` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--membership`=`MEMBERSHIP`
     ID of the membership or fully qualified identifier for the membership. 

To set the `membership` attribute: 

  * provide the argument `--membership` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location for the membership. 

To set the `location` attribute: 

  * provide the argument `--membership` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


OPTIONAL FLAGS
    

`--fqdn`=`FQDN`
     Filter clusters by substring of Service FQDN field. If unspecified, all clusters will be included in the output" 
`--output`=`OUTPUT`
     Return the detailed proxy config. The output format is either json or yaml. `OUTPUT` must be one of: `json`, `yaml`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta container hub mesh debug proxy-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/mesh/debug/proxy-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
