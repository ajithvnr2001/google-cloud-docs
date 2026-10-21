---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/
title: gcloud compute \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:01.725228+00:00
---

# gcloud compute  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute - create and manipulate Compute Engine resources 
SYNOPSIS
    

`gcloud compute` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The gcloud compute command group lets you create, configure, and manipulate Compute Engine virtual machine (VM) instances. 

With Compute Engine, you can create and run VMs on Google's infrastructure. Compute Engine offers scale, performance, and value that lets you launch large compute clusters on Google's infrastructure. 

For more information about Compute Engine, see the [Compute Engine overview](https://cloud.google.com/compute/) and the [Compute Engine user documentation](https://cloud.google.com/compute/docs/). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[accelerator-types](https://docs.cloud.google.com/sdk/gcloud/reference/compute/accelerator-types)`
     Read Compute Engine accelerator types. 
`[addresses](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses)`
     Read and manipulate Compute Engine addresses. 
`[advice](https://docs.cloud.google.com/sdk/gcloud/reference/compute/advice)`
     Provides recommendation on optimal allocation of resources according to a flexible specifications. 
`[backend-buckets](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets)`
     Read and manipulate backend buckets. 
`[backend-services](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services)`
     List, create, and delete backend services. 
`[commitments](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments)`
     Manage Compute Engine commitments. 
`[composite-health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/compute/composite-health-checks)`
     Manage composite health checks. 
`[diagnose](https://docs.cloud.google.com/sdk/gcloud/reference/compute/diagnose)`
     Debugging tools for Compute Engine virtual machine instances. 
`[disk-types](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disk-types)`
     Read Compute Engine virtual disk types. 
`[disks](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks)`
     Read and manipulate Compute Engine disks. 
`[external-vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways)`
     List, create, delete and update External VPN Gateways. 
`[firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies)`
     Manage Compute Engine organization firewall policies. 
`[firewall-rules](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules)`
     List, create, update, and delete Compute Engine firewall rules. 
`[forwarding-rules](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules)`
     Read and manipulate traffic forwarding rules to network load balancers. 
`[future-reservations](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations)`
     Manage Compute Engine future reservations. 
`[global-vm-extension-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/global-vm-extension-policies)`
     Compute Engine global VM extension policies. 
`[health-aggregation-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-aggregation-policies)`
     Manage health aggregation policies. 
`[health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks)`
     Read and manipulate health checks for load balanced instances. 
`[health-sources](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-sources)`
     Manage health sources. 
`[hosts](https://docs.cloud.google.com/sdk/gcloud/reference/compute/hosts)`
     Read Compute Engine hosts. 
`[http-health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/compute/http-health-checks)`
     Read and manipulate HTTP health checks for load balanced instances. 
`[https-health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/compute/https-health-checks)`
     Read and manipulate HTTPS health checks for load balanced instances. 
`[image-views](https://docs.cloud.google.com/sdk/gcloud/reference/compute/image-views)`
     Read image-view resources with regional context. 
`[images](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images)`
     List, create, and delete Compute Engine images. 
`[instance-groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups)`
     Read and manipulate Compute Engine instance groups. 
`[instance-templates](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates)`
     Read and manipulate Compute Engine instances templates. 
`[instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances)`
     Read and manipulate Compute Engine virtual machine instances. 
`[instant-snapshot-groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instant-snapshot-groups)`
     Create, list and delete Compute Engine instant snapshot groups. 
`[instant-snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots)`
     Create, list and delete Compute Engine instant snapshots. 
`[interconnects](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects)`
     Read and manipulate Compute Engine interconnects. 
`[machine-images](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images)`
     Read and manage Compute Engine machine image resources. 
`[machine-types](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-types)`
     Read Compute Engine virtual machine types. 
`[managed-rulesets](https://docs.cloud.google.com/sdk/gcloud/reference/compute/managed-rulesets)`
     Read Cloud Armor managed rulesets. 
`[migration](https://docs.cloud.google.com/sdk/gcloud/reference/compute/migration)`
     Provides Migrate to Virtual Machines (VM migration) service functionality. 
`[network-attachments](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments)`
     Manage Compute Engine network attachment resources. 
`[network-edge-security-services](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services)`
     Read and manipulate network edge security services. 
`[network-endpoint-groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups)`
     Read and manipulate Compute Engine network endpoint groups. 
`[network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies)`
     Manage Compute Engine network firewall policies. 
`[network-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-profiles)`
     Read Compute Engine network profiles. 
`[networks](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks)`
     List, create, and delete Compute Engine networks. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations)`
     Read and manipulate Compute Engine operations. 
`[org-security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies)`
     Manage Compute Engine organization security policies. 
`[os-config](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config)`
     Manage OS Config tasks for Compute Engine VM instances. 
`[os-login](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-login)`
     Create and manipulate Compute Engine OS Login resources. 
`[packet-mirrorings](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings)`
     Manage Compute Engine packet mirroring resources. 
`[preview-features](https://docs.cloud.google.com/sdk/gcloud/reference/compute/preview-features)`
     Read and manipulate Compute Engine Preview Features. 
`[project-info](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info)`
     Read and manipulate project-level data like quotas and metadata. 
`[project-views](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-views)`
     Read project views with regional context. 
`[project-zonal-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata)`
     Describe and update project zonal metadata. 
`[public-advertised-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes)`
     Manage public advertised prefix resources. 
`[public-delegated-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes)`
     Manage public delegated prefix resources. 
`[regions](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions)`
     List Compute Engine regions. 
`[reservations](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations)`
     Manage Compute Engine reservations. 
`[resource-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies)`
     Manage Compute Engine Resource Policies. 
`[rollout-plans](https://docs.cloud.google.com/sdk/gcloud/reference/compute/rollout-plans)`
     Read and manipulate Compute Engine Rollout Plans. 
`[rollouts](https://docs.cloud.google.com/sdk/gcloud/reference/compute/rollouts)`
     Read and manipulate Compute Engine Rollouts. 
`[routers](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers)`
     List, create, and delete Compute Engine routers. 
`[routes](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes)`
     Read and manipulate routes. 
`[security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies)`
     Read and manipulate Cloud Armor security policies. 
`[service-attachments](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments)`
     Manage Compute Engine service attachment resources. 
`[shared-vpc](https://docs.cloud.google.com/sdk/gcloud/reference/compute/shared-vpc)`
     Configure shared VPC. 
`[snapshot-settings](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings)`
     Describe and update Compute Engine snapshot settings. 
`[snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots)`
     List, describe, and delete Compute Engine snapshots. 
`[sole-tenancy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy)`
     Read and manage Compute Engine sole-tenancy resources. 
`[ssl-certificates](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates)`
     List, create, and delete Compute Engine SSL certificate resources. 
`[ssl-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-policies)`
     List, create, delete and update Compute Engine SSL policies. 
`[storage-pool-types](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pool-types)`
     Read storage pool types. 
`[storage-pools](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pools)`
     Read and manipulate storage pools. 
`[target-grpc-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies)`
     Manage Compute Engine target gRPC proxy resources. 
`[target-http-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies)`
     List, create, and delete target HTTP proxies. 
`[target-https-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies)`
     List, create, and delete target HTTPS proxies. 
`[target-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-instances)`
     Read and manipulate Compute Engine virtual target instances. 
`[target-pools](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools)`
     Control Compute Engine target pools for network load balancing. 
`[target-ssl-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies)`
     List, create, and delete target SSL proxies. 
`[target-tcp-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies)`
     List, create, and delete target TCP proxies. 
`[target-vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways)`
     Read and manipulate classic VPN gateways. 
`[tpus](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus)`
     List, create, and delete Cloud TPUs. 
`[url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps)`
     List, create, and delete URL maps. 
`[vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways)`
     read and manipulate Highly Available VPN Gateways. 
`[vpn-tunnels](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels)`
     Read and manipulate Compute Engine VPN tunnels. 
`[zone-vm-extension-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zone-vm-extension-policies)`
     Compute Engine zone VM extension policies. 
`[zones](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones)`
     List Compute Engine zones. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[config-ssh](https://docs.cloud.google.com/sdk/gcloud/reference/compute/config-ssh)`
     Populate SSH config files with Host entries from each instance. 
`[connect-to-serial-port](https://docs.cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port)`
     Connect to the serial port of an instance. 
`[copy-files](https://docs.cloud.google.com/sdk/gcloud/reference/compute/copy-files)`
     Copy files to and from Google Compute Engine virtual machines via scp. 
`[reset-windows-password](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password)`
     Reset and return a password for a Windows machine instance. 
`[scp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp)`
     Copy files to and from Google Compute Engine virtual machines via scp. 
`[sign-url](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sign-url)`
     Sign specified URL for use with Cloud CDN Signed URLs. 
`[ssh](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh)`
     SSH into a virtual machine instance. 
`[start-iap-tunnel](https://docs.cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel)`
     Starts an IAP TCP forwarding tunnel. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute)
    
    
    [gcloud beta compute](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute)
    
    
    [gcloud preview compute](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
