---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-management/network-monitoring-providers/monitoring-points/download-install-script/
title: gcloud network-management network-monitoring-providers monitoring-points download-install-script \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:54:18.186411+00:00
---

# gcloud network-management network-monitoring-providers monitoring-points download-install-script  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-management/network-monitoring-providers/monitoring-points/download-install-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-management network-monitoring-providers monitoring-points download-install-script Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-management network-monitoring-providers monitoring-points download-install-script - download an installation script for a Monitoring Point 
SYNOPSIS
    

`gcloud network-management network-monitoring-providers monitoring-points download-install-script` `--hostname`=`HOSTNAME` `--location`=`LOCATION` `--monitoring-point-type`=`MONITORING_POINT_TYPE` `--network-monitoring-provider`=`NETWORK_MONITORING_PROVIDER` `--output-file`=`OUTPUT_FILE` [`--ntp-server-address`=`NTP_SERVER_ADDRESS`] [`--ntp-server-secondary-address`=`NTP_SERVER_SECONDARY_ADDRESS`] [`--password`=`PASSWORD`] [`--time-zone`=`TIME_ZONE`] [`--use-dhcp`] [`--dns-server-address`=`DNS_SERVER_ADDRESS` `--dns-server-secondary-address`=`DNS_SERVER_SECONDARY_ADDRESS` `--domain`=`DOMAIN` `--gateway-address`=`GATEWAY_ADDRESS` `--netmask`=`NETMASK` `--static-ip-address`=`STATIC_IP_ADDRESS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Downloads an installation script for a Monitoring Point for a given Network Monitoring Provider. 

The command downloads a tarball for `--monitoring-point-type=container` or `--monitoring-point-type=helm`, or a zip file for `--monitoring-point-type=aws-ec2`, `--monitoring-point-type=azure-vm`, `--monitoring-point-type=gce-vm`, `--monitoring-point-type=kvm` or `--monitoring-point-type=vmware`. 

The `--network-monitoring-provider`, `--location`, `--monitoring-point-type`, and `--hostname` arguments are required for all Monitoring Points. Additional arguments depend on the value of `--monitoring-point-type`. 

If `--monitoring-point-type=aws-ec2`, `--monitoring-point-type=azure-vm`, `--monitoring-point-type=container`, `--monitoring-point-type=gce-vm`, or `--monitoring-point-type=helm` is specified, no other flags are required, and flags like `--password`, `--time-zone`, `--use-dhcp`, and `--static-ip-address` are not allowed. 

If `--monitoring-point-type=kvm` or `--monitoring-point-type=vmware` is specified, `--password` and `--time-zone` are also required. You must also specify either `--use-dhcp` for DHCP configurations or `--static-ip-address` for static IP configurations. If using `--static-ip-address`, `--gateway-address` and `--dns-server-address` are also required. 

EXAMPLES
     To download the install script for a Monitoring Point of type `container`, run: 
    
    
    [gcloud network-management network-monitoring-providers](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/network-monitoring-providers) monitoring-points download-install-script --network-monitoring-provider=my-provider --location=global --monitoring-point-type=container --hostname=container-hostname --output-file=compose.container-hostname.tar.gz

To download the install script for a Monitoring Point of type `kvm` using DHCP, run: 
    
    
    [gcloud network-management network-monitoring-providers](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/network-monitoring-providers) monitoring-points download-install-script --network-monitoring-provider=my-provider --location=global --monitoring-point-type=kvm --hostname=kvm-hostname --password=my-password --time-zone=America/Los_Angeles --use-dhcp --output-file=kvm.kvm-hostname.zip

To download the install script for a Monitoring Point of type `vmware` using a static IP, run: 
    
    
    [gcloud network-management network-monitoring-providers](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/network-monitoring-providers) monitoring-points download-install-script --network-monitoring-provider=my-provider --location=global --monitoring-point-type=vmware --hostname=vmware-hostname --password=my-password --time-zone=America/Los_Angeles --static-ip-address=192.168.1.100 --netmask=255.255.255.0 --gateway-address=192.168.1.1 --dns-server-address=8.8.8.8 --output-file=vmwareApplianceConfig.zip

REQUIRED FLAGS
    

`--hostname`=`HOSTNAME`
     The hostname of the Monitoring Point (example: `test-vm`). 
`--location`=`LOCATION`
     The location of the Network Monitoring Provider (example:, `global`). 
`--monitoring-point-type`=`MONITORING_POINT_TYPE`
     The type of the Monitoring Point. `MONITORING_POINT_TYPE` must be one of: `aws-ec2`, `azure-vm`, `container`, `gce-vm`, `helm`, `kvm`, `vmware`. 
`--network-monitoring-provider`=`NETWORK_MONITORING_PROVIDER`
     The ID of the Network Monitoring Provider. 
`--output-file`=`OUTPUT_FILE`
     The path to save the downloaded install script. 
OPTIONAL FLAGS
    

`--ntp-server-address`=`NTP_SERVER_ADDRESS`
     Primary NTP server address (IP address or FQDN). Allowed for types KVM and VMWARE only. 
`--ntp-server-secondary-address`=`NTP_SERVER_SECONDARY_ADDRESS`
     Secondary NTP server address (IP address or FQDN). Allowed for types KVM and VMWARE only. 
`--password`=`PASSWORD`
     Password for logging into the Monitoring Point. Required for types KVM and VMWARE, not allowed for CONTAINER. 
`--time-zone`=`TIME_ZONE`
     Time zone ID for the Monitoring Point (example: `America/Los_Angeles`). Required for types KVM and VMWARE, not allowed for CONTAINER. 
`--use-dhcp`
     Whether to use DHCP for IP address configuration. Allowed for types KVM and VMWARE only. 
Static IP address configuration. Allowed for types KVM and VMWARE only. 
`--dns-server-address`=`DNS_SERVER_ADDRESS`
     Primary DNS server address. Required if `--static-ip-address` is specified. 
`--dns-server-secondary-address`=`DNS_SERVER_SECONDARY_ADDRESS`
     Secondary DNS server address. Used with `--static-ip-address`. 
`--domain`=`DOMAIN`
     Domain name of the Monitoring Point. Used with `--static-ip-address`. 
`--gateway-address`=`GATEWAY_ADDRESS`
     Gateway IP address. Required if `--static-ip-address` is specified. 
`--netmask`=`NETMASK`
     Network mask (example: "255.255.255.0"). Used with `--static-ip-address`. 
`--static-ip-address`=`STATIC_IP_ADDRESS`
     Static IP address of the Monitoring Point. If specified, `--gateway-address` and `--dns-server-address` are required. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Download an installation script for a Monitoring Point. 
NOTES
     This variant is also available: 
    
    
    [gcloud alpha network-management network-monitoring-providers](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers) monitoring-points download-install-script

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
