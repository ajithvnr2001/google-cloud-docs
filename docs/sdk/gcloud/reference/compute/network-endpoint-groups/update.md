---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update/
title: gcloud compute network-endpoint-groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:28:57.001502+00:00
---

# gcloud compute network-endpoint-groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute network-endpoint-groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute network-endpoint-groups update - update a Compute Engine network endpoint group 
SYNOPSIS
    

`gcloud compute network-endpoint-groups update` `NAME` (`--add-endpoint`=[`client-destination-port`=`CLIENT-DESTINATION-PORT`],[`fqdn`=`FQDN`],[`instance`=`INSTANCE`],[`ip`=`IP`],[`ipv6`=`IPV6`],[`port`=`PORT`] | `--remove-endpoint`=[`client-destination-port`=`CLIENT-DESTINATION-PORT`],[`fqdn`=`FQDN`],[`instance`=`INSTANCE`],[`ip`=`IP`],[`ipv6`=`IPV6`],[`port`=`PORT`]) [`--global` | `--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Compute Engine network endpoint group. 
EXAMPLES
     To add two endpoints to a network endpoint group: 
    
    
    gcloud compute network-endpoint-groups update my-neg --zone=us-central1-a --add-endpoint=instance=my-instance1,ip=127.0.0.1,port=1234 --add-endpoint=instance=my-instance2

To remove two endpoints from a network endpoint group: 
    
    
    gcloud compute network-endpoint-groups update my-neg --zone=us-central1-a --remove-endpoint=instance=my-instance1,ip=127.0.0.1,port=1234 --remove-endpoint=instance=my-instance2

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the network endpoint group to operate on. 
REQUIRED FLAGS
    

These flags can be specified multiple times to add/remove multiple endpoints. 

Exactly one of these must be specified: 

`--add-endpoint`=[`client-destination-port`=`CLIENT-DESTINATION-PORT`],[`fqdn`=`FQDN`],[`instance`=`INSTANCE`],[`ip`=`IP`],[`ipv6`=`IPV6`],[`port`=`PORT`]
     The network endpoint to add to the network endpoint group. Keys used depend on the endpoint type of the NEG. 

`gce-vm-ip-port`
    
    
    *instance* - Name of instance in same zone as the network endpoint
    group.
    
    
    The VM instance must belong to the network / subnetwork
    associated with the network endpoint group. If the VM instance
    is deleted, then any network endpoint group that has a reference
    to it is updated.
    
    
    *ip* - Optional IP address of the network endpoint. The IP address
    must belong to a VM in compute engine (either the primary IP or
    as part of an aliased IP range). If the IP address is not
    specified, then the primary IP address for the VM instance in
    the network that the network endpoint group belongs to is
    used.
    
    
    *ipv6* - Optional IPv6 address of the network endpoint. The IPv6
    address must belong to a VM in compute engine (either the internal
    or external IPv6 address).
    
    
    *port* - Required endpoint port unless NEG default port is set.
    
    
    *client-destination-port* - Required endpoint client destination port only for the port
    mapping NEG.

`internet-ip-port`
    
    
    *ip* - Required IPv4 address of the endpoint to attach. Must be
    publicly routable.
    
    
    *port* - Optional port of the endpoint to attach. If unspecified,
    the NEG default port is set. If no default port is set, the
    well-known port for the backend protocol is used instead
    (80 for HTTP, 443 for HTTPS).

`internet-fqdn-port`
    
    
    *fqdn* - Required fully qualified domain name to use to look up an
    external endpoint. Must be resolvable to a public IP address via
    public DNS.
    
    
    *port* - Optional port of the endpoint to attach. If unspecified,
    the NEG default port is set. If no default port is set, the
    well-known port for the backend protocol is used instead
    (80 for HTTP, 443 for HTTPS or HTTP2).
    
    
    Example: `--add-endpoint="fqdn=backend.example.com,port=443"`

`non-gcp-private-ip-port`
    
    
    *ip* - Required IPv4 address of the network endpoint to attach.
    The IP address must belong to a VM not in Compute Engine and must
    be routable using a Cloud Router over VPN or an Interconnect
    connection.
    
    
    *port* - Required port of the network endpoint to attach unless
    the NEG default port is set.

`gce-vm-ip`
    
    
    *instance* - Required instance name in same zone as the network
    endpoint group.
    
    
    The VM instance must belong to the network / subnetwork
    associated with the network endpoint group. If the VM instance
    is deleted, then any network endpoint group that has a reference
    to it is updated.
    
    
    *ip* - Optional IP address of the network endpoint to attach. The
    IP address must be the VM's network interface address. If not
    specified, the primary NIC address is used.

`--remove-endpoint`=[`client-destination-port`=`CLIENT-DESTINATION-PORT`],[`fqdn`=`FQDN`],[`instance`=`INSTANCE`],[`ip`=`IP`],[`ipv6`=`IPV6`],[`port`=`PORT`]
     The network endpoint to detach from the network endpoint group. Keys used depend on the endpoint type of the NEG. 

`gce-vm-ip-port`
    
    
    *instance* - Required name of instance whose endpoint(s) to
    detach. If the IP address is unset, all endpoints for the
    instance in the NEG are detached.
    
    
    *ip* - Optional IPv4 address of the network endpoint to detach.
    If specified port must be provided as well.
    
    
    *ipv6* - Optional IPv6 address of the network endpoint to detach.
    If specified port must be provided as well.
    
    
    *port* - Optional port of the network endpoint to detach.
    
    
    *client-destination-port* - Optional client destination port, only for port mapping NEGs.

`internet-ip-port`
    
    
    *ip* - Required IPv4 address of the network endpoint to detach.
    
    
    *port* - Optional port of the network endpoint to detach if the
    endpoint has a port specified.

`internet-fqdn-port`
    
    
    *fqdn* - Required fully qualified domain name of the endpoint to
    detach.
    
    
    *port* - Optional port of the network endpoint to detach if the
    endpoint has a port specified.

`non-gcp-private-ip-port`
    
    
    *ip* - Required IPv4 address of the network endpoint to detach.
    
    
    *port* - Required port of the network endpoint to detach unless
    NEG default port is set.

`gce-vm-ip`
    
    
    *instance* - Required name of instance with endpoints to
    detach. If the IP address is unset, all endpoints for the
    instance in the NEG are detached.
    
    
    *ip* - Optional IP address of the network endpoint to attach. The
    IP address must be the VM's network interface's primary IP
    address. If not specified, the primary NIC address is used.

OPTIONAL FLAGS
    

At most one of these can be specified: 

`--global`
     If set, the network endpoint group is global. 
`--region`=`REGION`
     Region of the network endpoint group to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     Zone of the network endpoint group to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute network-endpoint-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-endpoint-groups/update)
    
    
    [gcloud beta compute network-endpoint-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-endpoint-groups/update)
    
    
    [gcloud preview compute network-endpoint-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-endpoint-groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
