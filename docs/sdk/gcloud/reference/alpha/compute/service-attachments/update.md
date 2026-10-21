---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/service-attachments/update/
title: gcloud alpha compute service-attachments update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:23:46.583934+00:00
---

# gcloud alpha compute service-attachments update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/service-attachments/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute service-attachments update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute service-attachments update - update a Google Compute Engine service attachment 
SYNOPSIS
    

`gcloud alpha compute service-attachments update` `NAME` [`--connection-preference`=`CONNECTION_PREFERENCE`] [`--consumer-accept-list`=[`PROJECT_OR_NETWORK_OR_ENDPOINT`=`LIMIT`,…]] [`--consumer-reject-list`=[`REJECT_LIST`,…]] [`--description`=`DESCRIPTION`] [`--[no-]enable-proxy-protocol`] [`--nat-ips-per-endpoint`=`NAT_IPS_PER_ENDPOINT`] [`--nat-subnets`=`NAT_SUBNETS`,[`NAT_SUBNETS`,…]] [`--nat-subnets-region`=`NAT_SUBNETS_REGION`] [`--propagated-connection-limit`=`PROPAGATED_CONNECTION_LIMIT`] [`--[no-]reconcile-connections`] [`--region`=`REGION`] [`--remove-obsolete-endpoint-accept-reject-entries`] [`--routing-mode`=`ROUTING_MODE`] [`--target-service`=`TARGET_SERVICE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute service-attachments update` is used to update service attachments. A service producer creates service attachments to make a service available to consumers. Service consumers use Private Service Connect endpoints to privately forward traffic to the service attachment. 
EXAMPLES
     To update the connection policy of a service attachment to be ACCEPT_MANUAL, run: 
    
    
    gcloud alpha compute service-attachments update SERVICE_ATTACHMENT_NAME --region=us-central1 --connection-preference=ACCEPT_MANUAL

To update all supported fields of a service attachment, run: 
    
    
    gcloud alpha compute service-attachments update SERVICE_ATTACHMENT_NAME --region=us-central1 --connection-preference=ACCEPT_AUTOMATIC --nat-subnets=MY_SUBNET1,MY_SUBNET2 --enable-proxy-protocol --consumer-reject-list=PROJECT_ID1,PROJECT_ID2 --consumer-accept-list=PROJECT_ID3=10,PROJECT_ID4=20

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the service attachment to update. 
FLAGS
    

`--connection-preference`=`CONNECTION_PREFERENCE`
     This defines the service attachment's connection preference. `CONNECTION_PREFERENCE` must be one of: 

`ACCEPT_AUTOMATIC`
     Always accept connection requests from consumers automatically. 
`ACCEPT_MANUAL`
     Only accept connection requests from consumers with the approval of the service provider. 
`--consumer-accept-list`=[`PROJECT_OR_NETWORK_OR_ENDPOINT`=`LIMIT`,…]
     Specifies which consumer projects/networks/endpoints are allowed to connect to the service attachment. A connection limit is required for each accepted project/network (optional for endpoints). For a given service attachment, consumer accept and reject lists must contain entries of the same type: all projects, all networks or all endpoints. 

For example: 

  * `--consumer-accept-list myProjectId1=20` \- Accepts a consumer project myProjectId1 with connection limit 20. 
  * `--consumer-accept-list projects/myProjectId1/global/networks/myNet1=20` \- Accepts a consumer network myNet1 with connection limit 20. 
  * `--consumer-accept-list projects/myProjectId1/regions/myRegion1/forwardingRules/8167352512` \- Accepts a consumer endpoint with ID 8167352512. 


  * `PROJECT_OR_NETWORK_OR_ENDPOINT` \- Consumer project ID/number or network URL or endpoint URL. 
  * `CONNECTION_LIMIT` \- The maximum number of allowed connections. This field is optional for endpoints. 


`--consumer-reject-list`=[`REJECT_LIST`,…]
     Specifies a comma-separated list of projects/networks/endpoints that are not allowed to connect to this service attachment. The project can be specified using its project ID or project number and the network or endpoint can be specified using its URL. For a given service attachment, consumer accept and reject lists must contain entries of the same type: all projects, all networks, or all endpoints. 
`--description`=`DESCRIPTION`
     An optional, textual description for the service attachment. 
`--[no-]enable-proxy-protocol`
     If True, then enable the proxy protocol which is for supplying client TCP/IP address data in TCP connections that traverse proxies on their way to destination servers. Use `--enable-proxy-protocol` to enable and `--no-enable-proxy-protocol` to disable. 
`--nat-ips-per-endpoint`=`NAT_IPS_PER_ENDPOINT`
     The number of NAT IP addresses to be allocated per connected endpoint. 
`--nat-subnets`=`NAT_SUBNETS`,[`NAT_SUBNETS`,…]
     The subnetworks provided by service producer to use for NAT 
`--nat-subnets-region`=`NAT_SUBNETS_REGION`
     Region of the subnetworks to operate on. If not specified, it will be set to the region of the service attachment. Overrides the default `compute/region` property value for this command invocation. 
`--propagated-connection-limit`=`PROPAGATED_CONNECTION_LIMIT`
     The number of consumer spokes that connected Private Service Connect endpoints can be propagated to through Network Connectivity Center. This limit lets the service producer limit how many propagated Private Service Connect connections can be established to this service attachment from a single consumer. 

If the connection preference of the service attachment is ACCEPT_MANUAL, the limit applies to each project or network that is listed in the consumer accept list. If the connection preference of the service attachment is ACCEPT_AUTOMATIC, the limit applies to each project that contains a connected endpoint. 

If unspecified, the default propagated connection limit is 250. 

`--[no-]reconcile-connections`
     Determines whether to apply changes to consumer accept or reject lists to existing connections or only to new connections. 

If false, existing endpoints with a connection status of ACCEPTED or REJECTED are not updated. 

If true, existing endpoints with a connection status of ACCEPTED or REJECTED are updated based on the connection policy update. For example, if a project or network is removed from the --consumer-accept-list and added to \--consumer-reject-list, all the endpoints in that project or network with the ACCEPTED state are set to REJECTED. 

Use `--reconcile-connections` to enable and `--no-reconcile-connections` to disable. 

`--region`=`REGION`
     Region of the service attachment to update. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--remove-obsolete-endpoint-accept-reject-entries`
     If set to true, this flag cleans up the service attachment's consumer accept and reject lists by removing entries for Private Service Connect endpoints that are no longer connected. 

The cleanup process compares the resource ID of each endpoint in the lists against the currently connected endpoints. In rare cases, an obsolete entry will be left untouched if its resource ID collides with another connected endpoint from a different project. 

This flag only affects endpoint-based accept/reject entries, project-based and network-based entries are left unchanged. 

`--routing-mode`=`ROUTING_MODE`
     Specifies the routing mode for tunneling configuration on this service attachment. `ROUTING_MODE` must be one of: 

`PACKET_INJECTION`
     Traffic sent to this service attachment will be reinjected into the consumer network. 
`STANDARD_ROUTING`
     Response traffic, after de-encapsulation, will be returned to the client. 
`--target-service`=`TARGET_SERVICE`
     URL of the target service that receives forwarded traffic. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute service-attachments update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/update)
    
    
    [gcloud beta compute service-attachments update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/service-attachments/update)
    
    
    [gcloud preview compute service-attachments update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/service-attachments/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
