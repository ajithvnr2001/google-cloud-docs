---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel/
title: gcloud compute start-iap-tunnel \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:00:06.780983+00:00
---

# gcloud compute start-iap-tunnel  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute start-iap-tunnel Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute start-iap-tunnel - starts an IAP TCP forwarding tunnel 
SYNOPSIS
    

`gcloud compute start-iap-tunnel` `INSTANCE_NAME` `INSTANCE_PORT` [`--iap-tunnel-disable-connection-check`] [`--local-host-port`=`LOCAL_HOST_PORT`; default="localhost:0"] [`--zone`=`ZONE`] [`--network`=`NETWORK` `--region`=`REGION` : `--dest-group`=`DEST_GROUP`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Starts a tunnel to Cloud Identity-Aware Proxy for TCP forwarding through which another process can create a connection (eg. SSH, RDP) to a Google Compute Engine instance. 

To learn more, see the [IAP for TCP forwarding documentation](https://cloud.google.com/iap/docs/tcp-forwarding-overview). 

If the `--region` and `--network` flags are provided, then an IP address or FQDN must be supplied instead of an instance name. This is most useful for connecting to on-prem resources. 

EXAMPLES
     To open a tunnel to the instances's RDP port on an arbitrary local port, run: 
    
    
    gcloud compute start-iap-tunnel my-instance 3389

To open a tunnel to the instance's RDP port on a specific local port, run: 
    
    
    gcloud compute start-iap-tunnel my-instance 3389 --local-host-port=localhost:3333

To use the IP address or FQDN of your remote VM (eg, for on-prem), you must also specify the `--region` and `--network` flags: 
    
    
    gcloud compute start-iap-tunnel 10.1.2.3 3389 --region=us-central1 --network=default

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
`INSTANCE_PORT`
     The name or number of the instance's port to connect to. 
FLAGS
    

`--iap-tunnel-disable-connection-check`
     Disables the immediate check of the connection. 
`--local-host-port`=`LOCAL_HOST_PORT`; default="localhost:0"
     `LOCAL_HOST:LOCAL_PORT` on which gcloud should bind and listen for connections that should be tunneled. 

`LOCAL_PORT` may be omitted, in which case it is treated as 0 and an arbitrary unused local port is chosen. The colon also may be omitted in that case. 

If `LOCAL_PORT` is 0, an arbitrary unused local port is chosen. 

`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

`--network`=`NETWORK`
     Configures the VPC network to use when connecting via IP address or FQDN. 
`--region`=`REGION`
     Configures the region to use when connecting via IP address or FQDN. 
`--dest-group`=`DEST_GROUP`
     Configures the destination group to use when connecting via IP address or FQDN. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute start-iap-tunnel](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/start-iap-tunnel)
    
    
    [gcloud beta compute start-iap-tunnel](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/start-iap-tunnel)
    
    
    [gcloud preview compute start-iap-tunnel](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/start-iap-tunnel)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
