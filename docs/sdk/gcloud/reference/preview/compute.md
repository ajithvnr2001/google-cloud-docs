---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/
title: gcloud preview compute \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:34.019637+00:00
---

# gcloud preview compute  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute - create and manipulate Compute Engine resources 
SYNOPSIS
    

`gcloud preview compute` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` The gcloud compute command group lets you create, configure, and manipulate Compute Engine virtual machine (VM) instances. 

With Compute Engine, you can create and run VMs on Google's infrastructure. Compute Engine offers scale, performance, and value that lets you launch large compute clusters on Google's infrastructure. 

For more information about Compute Engine, see the [Compute Engine overview](https://cloud.google.com/compute/) and the [Compute Engine user documentation](https://cloud.google.com/compute/docs/). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[accelerator-interconnects](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/accelerator-interconnects)`
     `(PREVIEW)` Read and manipulate Compute Engine accelerator interconnects. 
`[accelerator-types](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/accelerator-types)`
     `(PREVIEW)` Read Compute Engine accelerator types. 
`[addresses](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/addresses)`
     `(PREVIEW)` Read and manipulate Compute Engine addresses. 
`[advice](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/advice)`
     `(PREVIEW)` Provides recommendation on optimal allocation of resources according to a flexible specifications. 
`[backend-buckets](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/backend-buckets)`
     `(PREVIEW)` Read and manipulate backend buckets. 
`[backend-services](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/backend-services)`
     `(PREVIEW)` List, create, and delete backend services. 
`[commitments](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/commitments)`
     `(PREVIEW)` Manage Compute Engine commitments. 
`[diagnose](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/diagnose)`
     `(PREVIEW)` Debugging tools for Compute Engine virtual machine instances. 
`[disk-types](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disk-types)`
     `(PREVIEW)` Read Compute Engine virtual disk types. 
`[disks](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks)`
     `(PREVIEW)` Read and manipulate Compute Engine disks. 
`[external-vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/external-vpn-gateways)`
     `(PREVIEW)` List, create, delete and update External VPN Gateways. 
`[firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-policies)`
     `(PREVIEW)` Manage Compute Engine organization firewall policies. 
`[firewall-rules](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/firewall-rules)`
     `(PREVIEW)` List, create, update, and delete Compute Engine firewall rules. 
`[forwarding-rules](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/forwarding-rules)`
     `(PREVIEW)` Read and manipulate traffic forwarding rules to network load balancers. 
`[future-reservations](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/future-reservations)`
     `(PREVIEW)` Manage Compute Engine future reservations. 
`[health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/health-checks)`
     `(PREVIEW)` Read and manipulate health checks for load balanced instances. 
`[http-health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/http-health-checks)`
     `(PREVIEW)` Read and manipulate HTTP health checks for load balanced instances. 
`[https-health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/https-health-checks)`
     `(PREVIEW)` Read and manipulate HTTPS health checks for load balanced instances. 
`[images](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/images)`
     `(PREVIEW)` List, create, and delete Compute Engine images. 
`[instance-groups](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups)`
     `(PREVIEW)` Read and manipulate Compute Engine instance groups. 
`[instance-templates](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-templates)`
     `(PREVIEW)` Read and manipulate Compute Engine instances templates. 
`[instances](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances)`
     `(PREVIEW)` Read and manipulate Compute Engine virtual machine instances. 
`[instant-snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instant-snapshots)`
     `(PREVIEW)` Create, list and delete Compute Engine instant snapshots. 
`[interconnects](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects)`
     `(PREVIEW)` Read and manipulate Compute Engine interconnects. 
`[machine-images](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/machine-images)`
     `(PREVIEW)` Read and manage Compute Engine machine image resources. 
`[machine-types](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/machine-types)`
     `(PREVIEW)` Read Compute Engine virtual machine types. 
`[network-attachments](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-attachments)`
     `(PREVIEW)` Manage Compute Engine network attachment resources. 
`[network-edge-security-services](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-edge-security-services)`
     `(PREVIEW)` Read and manipulate network edge security services. 
`[network-endpoint-groups](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-endpoint-groups)`
     `(PREVIEW)` Read and manipulate Compute Engine network endpoint groups. 
`[network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies)`
     `(PREVIEW)` Manage Compute Engine network firewall policies. 
`[network-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-profiles)`
     `(PREVIEW)` Read Compute Engine network profiles. 
`[networks](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/networks)`
     `(PREVIEW)` List, create, and delete Compute Engine networks. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/operations)`
     `(PREVIEW)` Read and manipulate Compute Engine operations. 
`[org-security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/org-security-policies)`
     `(PREVIEW)` Manage Compute Engine organization security policies. 
`[packet-mirrorings](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/packet-mirrorings)`
     `(PREVIEW)` Manage Compute Engine packet mirroring resources. 
`[preview-features](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/preview-features)`
     `(PREVIEW)` Read and manipulate Compute Engine Preview Features. 
`[project-info](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/project-info)`
     `(PREVIEW)` Read and manipulate project-level data like quotas and metadata. 
`[project-zonal-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/project-zonal-metadata)`
     `(PREVIEW)` Describe and update project zonal metadata. 
`[public-advertised-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/public-advertised-prefixes)`
     `(PREVIEW)` Manage public advertised prefix resources. 
`[public-delegated-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/public-delegated-prefixes)`
     `(PREVIEW)` Manage public delegated prefix resources. 
`[regions](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/regions)`
     `(PREVIEW)` List Compute Engine regions. 
`[reservations](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reservations)`
     `(PREVIEW)` Manage Compute Engine reservations. 
`[resource-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/resource-policies)`
     `(PREVIEW)` Manage Compute Engine Resource Policies. 
`[routers](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers)`
     `(PREVIEW)` List, create, and delete Compute Engine routers. 
`[routes](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routes)`
     `(PREVIEW)` Read and manipulate routes. 
`[security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies)`
     `(PREVIEW)` Read and manipulate Cloud Armor security policies. 
`[service-attachments](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/service-attachments)`
     `(PREVIEW)` Manage Compute Engine service attachment resources. 
`[shared-vpc](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/shared-vpc)`
     `(PREVIEW)` Configure shared VPC. 
`[snapshot-settings](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshot-settings)`
     `(PREVIEW)` Describe and update Compute Engine snapshot settings. 
`[snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots)`
     `(PREVIEW)` List, describe, and delete Compute Engine snapshots. 
`[sole-tenancy](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/sole-tenancy)`
     `(PREVIEW)` Read and manage Compute Engine sole-tenancy resources. 
`[ssl-certificates](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/ssl-certificates)`
     `(PREVIEW)` List, create, and delete Compute Engine SSL certificate resources. 
`[ssl-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/ssl-policies)`
     `(PREVIEW)` List, create, delete and update Compute Engine SSL policies. 
`[storage-pool-types](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/storage-pool-types)`
     `(PREVIEW)` Read storage pool types. 
`[storage-pools](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/storage-pools)`
     `(PREVIEW)` Read and manipulate storage pools. 
`[target-grpc-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-grpc-proxies)`
     `(PREVIEW)` Manage Compute Engine target gRPC proxy resources. 
`[target-http-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-http-proxies)`
     `(PREVIEW)` List, create, and delete target HTTP proxies. 
`[target-https-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-https-proxies)`
     `(PREVIEW)` List, create, and delete target HTTPS proxies. 
`[target-instances](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-instances)`
     `(PREVIEW)` Read and manipulate Compute Engine virtual target instances. 
`[target-pools](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-pools)`
     `(PREVIEW)` Control Compute Engine target pools for network load balancing. 
`[target-ssl-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-ssl-proxies)`
     `(PREVIEW)` List, create, and delete target SSL proxies. 
`[target-tcp-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-tcp-proxies)`
     `(PREVIEW)` List, create, and delete target TCP proxies. 
`[target-vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-vpn-gateways)`
     `(PREVIEW)` Read and manipulate classic VPN gateways. 
`[url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/url-maps)`
     `(PREVIEW)` List, create, and delete URL maps. 
`[vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/vpn-gateways)`
     `(PREVIEW)` read and manipulate Highly Available VPN Gateways. 
`[vpn-tunnels](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/vpn-tunnels)`
     `(PREVIEW)` Read and manipulate Compute Engine VPN tunnels. 
`[zones](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/zones)`
     `(PREVIEW)` List Compute Engine zones. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[config-ssh](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/config-ssh)`
     `(PREVIEW)` Populate SSH config files with Host entries from each instance. 
`[connect-to-serial-port](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/connect-to-serial-port)`
     `(PREVIEW)` Connect to the serial port of an instance. 
`[copy-files](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/copy-files)`
     `(PREVIEW)` Copy files to and from Google Compute Engine virtual machines via scp. 
`[reset-windows-password](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reset-windows-password)`
     `(PREVIEW)` Reset and return a password for a Windows machine instance. 
`[scp](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/scp)`
     `(PREVIEW)` Copy files to and from Google Compute Engine virtual machines via scp. 
`[sign-url](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/sign-url)`
     `(PREVIEW)` Sign specified URL for use with Cloud CDN Signed URLs. 
`[ssh](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/ssh)`
     `(PREVIEW)` SSH into a virtual machine instance. 
`[start-iap-tunnel](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/start-iap-tunnel)`
     `(PREVIEW)` Starts an IAP TCP forwarding tunnel. 
NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute](https://docs.cloud.google.com/sdk/gcloud/reference/compute)
    
    
    [gcloud alpha compute](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute)
    
    
    [gcloud beta compute](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
