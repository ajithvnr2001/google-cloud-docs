---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/
title: gcloud alpha compute \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:52.501604+00:00
---

# gcloud alpha compute  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute - create and manipulate Compute Engine resources 
SYNOPSIS
    

`gcloud alpha compute` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The gcloud compute command group lets you create, configure, and manipulate Compute Engine virtual machine (VM) instances. 

With Compute Engine, you can create and run VMs on Google's infrastructure. Compute Engine offers scale, performance, and value that lets you launch large compute clusters on Google's infrastructure. 

For more information about Compute Engine, see the [Compute Engine overview](https://cloud.google.com/compute/) and the [Compute Engine user documentation](https://cloud.google.com/compute/docs/). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[accelerator-types](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/accelerator-types)`
     `(ALPHA)` Read Compute Engine accelerator types. 
`[addresses](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses)`
     `(ALPHA)` Read and manipulate Compute Engine addresses. 
`[advice](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/advice)`
     `(ALPHA)` Provides recommendation on optimal allocation of resources according to a flexible specifications. 
`[backend-buckets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets)`
     `(ALPHA)` Read and manipulate backend buckets. 
`[backend-services](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services)`
     `(ALPHA)` List, create, and delete backend services. 
`[commitments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments)`
     `(ALPHA)` Manage Compute Engine commitments. 
`[composite-health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/composite-health-checks)`
     `(ALPHA)` Manage composite health checks. 
`[diagnose](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/diagnose)`
     `(ALPHA)` Debugging tools for Compute Engine virtual machine instances. 
`[disk-settings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-settings)`
     `(ALPHA)` Read Compute Engine disk settings. 
`[disk-types](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disk-types)`
     `(ALPHA)` Read Compute Engine virtual disk types. 
`[disks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks)`
     `(ALPHA)` Read and manipulate Compute Engine disks. 
`[external-vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/external-vpn-gateways)`
     `(ALPHA)` List, create, delete and update External VPN Gateways. 
`[firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies)`
     `(ALPHA)` Manage Compute Engine organization firewall policies. 
`[firewall-rules](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules)`
     `(ALPHA)` List, create, update, and delete Compute Engine firewall rules. 
`[forwarding-rules](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules)`
     `(ALPHA)` Read and manipulate traffic forwarding rules to network load balancers. 
`[future-reservations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/future-reservations)`
     `(ALPHA)` Manage Compute Engine future reservations. 
`[global-vm-extension-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/global-vm-extension-policies)`
     `(ALPHA)` Compute Engine global VM extension policies. 
`[health-aggregation-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-aggregation-policies)`
     `(ALPHA)` Manage health aggregation policies. 
`[health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks)`
     `(ALPHA)` Read and manipulate health checks for load balanced instances. 
`[health-sources](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-sources)`
     `(ALPHA)` Manage health sources. 
`[hosts](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/hosts)`
     `(ALPHA)` Read Compute Engine hosts. 
`[http-health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/http-health-checks)`
     `(ALPHA)` Read and manipulate HTTP health checks for load balanced instances. 
`[https-health-checks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/https-health-checks)`
     `(ALPHA)` Read and manipulate HTTPS health checks for load balanced instances. 
`[image-views](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/image-views)`
     `(ALPHA)` Read image-view resources with regional context. 
`[images](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/images)`
     `(ALPHA)` List, create, and delete Compute Engine images. 
`[instance-groups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups)`
     `(ALPHA)` Read and manipulate Compute Engine instance groups. 
`[instance-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-templates)`
     `(ALPHA)` Read and manipulate Compute Engine instances templates. 
`[instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances)`
     `(ALPHA)` Read and manipulate Compute Engine virtual machine instances. 
`[instant-snapshot-groups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshot-groups)`
     `(ALPHA)` Create, list and delete Compute Engine instant snapshot groups. 
`[instant-snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instant-snapshots)`
     `(ALPHA)` Create, list and delete Compute Engine instant snapshots. 
`[interconnects](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects)`
     `(ALPHA)` Read and manipulate Compute Engine interconnects. 
`[machine-images](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/machine-images)`
     `(ALPHA)` Read and manage Compute Engine machine image resources. 
`[machine-types](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/machine-types)`
     `(ALPHA)` Read Compute Engine virtual machine types. 
`[managed-rulesets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/managed-rulesets)`
     `(ALPHA)` Read Cloud Armor managed rulesets. 
`[migration](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration)`
     `(ALPHA)` Provides Migrate to Virtual Machines (VM migration) service functionality. 
`[network-attachments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-attachments)`
     `(ALPHA)` Manage Compute Engine network attachment resources. 
`[network-edge-security-services](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-edge-security-services)`
     `(ALPHA)` Read and manipulate network edge security services. 
`[network-endpoint-groups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-endpoint-groups)`
     `(ALPHA)` Read and manipulate Compute Engine network endpoint groups. 
`[network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies)`
     `(ALPHA)` Manage Compute Engine network firewall policies. 
`[network-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-policies)`
     `(ALPHA)` Manage Compute Engine network policies. 
`[network-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-profiles)`
     `(ALPHA)` Read Compute Engine network profiles. 
`[networks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/networks)`
     `(ALPHA)` List, create, and delete Compute Engine networks. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/operations)`
     `(ALPHA)` Read and manipulate Compute Engine operations. 
`[org-rollout-plans](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-rollout-plans)`
     `(ALPHA)` Read and manipulate Compute Engine organization rollout plans. 
`[org-rollouts](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-rollouts)`
     `(ALPHA)` Read and manipulate Compute Engine organization rollouts. 
`[org-security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-security-policies)`
     `(ALPHA)` Manage Compute Engine organization security policies. 
`[os-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-config)`
     `(ALPHA)` Manage OS Config tasks for Compute Engine VM instances. 
`[os-login](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-login)`
     `(ALPHA)` Create and manipulate Compute Engine OS Login resources. 
`[packet-mirrorings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/packet-mirrorings)`
     `(ALPHA)` Manage Compute Engine packet mirroring resources. 
`[preview-features](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/preview-features)`
     `(ALPHA)` Read and manipulate Compute Engine Preview Features. 
`[project-info](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/project-info)`
     `(ALPHA)` Read and manipulate project-level data like quotas and metadata. 
`[project-views](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/project-views)`
     `(ALPHA)` Read project views with regional context. 
`[project-zonal-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/project-zonal-metadata)`
     `(ALPHA)` Describe and update project zonal metadata. 
`[public-advertised-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/public-advertised-prefixes)`
     `(ALPHA)` Manage public advertised prefix resources. 
`[public-delegated-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/public-delegated-prefixes)`
     `(ALPHA)` Manage public delegated prefix resources. 
`[queued-resources](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/queued-resources)`
     `(ALPHA)` Manage queued resources. 
`[recoverable-snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/recoverable-snapshots)`
     `(ALPHA)` Recover, list, describe and delete Compute Engine recoverable snapshots. 
`[regions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/regions)`
     `(ALPHA)` List Compute Engine regions. 
`[reservations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations)`
     `(ALPHA)` Manage Compute Engine reservations. 
`[resource-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/resource-policies)`
     `(ALPHA)` Manage Compute Engine Resource Policies. 
`[rollout-plans](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/rollout-plans)`
     `(ALPHA)` Read and manipulate Compute Engine Rollout Plans. 
`[rollouts](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/rollouts)`
     `(ALPHA)` Read and manipulate Compute Engine Rollouts. 
`[routers](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routers)`
     `(ALPHA)` List, create, and delete Compute Engine routers. 
`[routes](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routes)`
     `(ALPHA)` Read and manipulate routes. 
`[security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/security-policies)`
     `(ALPHA)` Read and manipulate Cloud Armor security policies. 
`[service-attachments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/service-attachments)`
     `(ALPHA)` Manage Compute Engine service attachment resources. 
`[shared-vpc](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/shared-vpc)`
     `(ALPHA)` Configure shared VPC. 
`[snapshot-groups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshot-groups)`
     `(ALPHA)` Create, list, describe and delete Compute Engine snapshot groups. 
`[snapshot-recycle-bin-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshot-recycle-bin-policy)`
     `(ALPHA)` Update and describe Compute Engine snapshot recycle bin policy. 
`[snapshot-settings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshot-settings)`
     `(ALPHA)` Describe and update Compute Engine snapshot settings. 
`[snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots)`
     `(ALPHA)` List, describe, and delete Compute Engine snapshots. 
`[sole-tenancy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/sole-tenancy)`
     `(ALPHA)` Read and manage Compute Engine sole-tenancy resources. 
`[ssl-certificates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/ssl-certificates)`
     `(ALPHA)` List, create, and delete Compute Engine SSL certificate resources. 
`[ssl-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/ssl-policies)`
     `(ALPHA)` List, create, delete and update Compute Engine SSL policies. 
`[storage-pool-types](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/storage-pool-types)`
     `(ALPHA)` Read storage pool types. 
`[storage-pools](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/storage-pools)`
     `(ALPHA)` Read and manipulate storage pools. 
`[target-grpc-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-grpc-proxies)`
     `(ALPHA)` Manage Compute Engine target gRPC proxy resources. 
`[target-http-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-http-proxies)`
     `(ALPHA)` List, create, and delete target HTTP proxies. 
`[target-https-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-https-proxies)`
     `(ALPHA)` List, create, and delete target HTTPS proxies. 
`[target-instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-instances)`
     `(ALPHA)` Read and manipulate Compute Engine virtual target instances. 
`[target-pools](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-pools)`
     `(ALPHA)` Control Compute Engine target pools for network load balancing. 
`[target-ssl-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-ssl-proxies)`
     `(ALPHA)` List, create, and delete target SSL proxies. 
`[target-tcp-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-tcp-proxies)`
     `(ALPHA)` List, create, and delete target TCP proxies. 
`[target-vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-vpn-gateways)`
     `(ALPHA)` Read and manipulate classic VPN gateways. 
`[tpus](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus)`
     `(ALPHA)` List, create, and delete Cloud TPUs. 
`[url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps)`
     `(ALPHA)` List, create, and delete URL maps. 
`[vpn-gateways](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/vpn-gateways)`
     `(ALPHA)` read and manipulate Highly Available VPN Gateways. 
`[vpn-tunnels](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/vpn-tunnels)`
     `(ALPHA)` Read and manipulate Compute Engine VPN tunnels. 
`[zone-vm-extension-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/zone-vm-extension-policies)`
     `(ALPHA)` Compute Engine zone VM extension policies. 
`[zones](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/zones)`
     `(ALPHA)` List Compute Engine zones. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[config-ssh](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh)`
     `(ALPHA)` Populate SSH config files with Host entries from each instance. 
`[connect-to-serial-port](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/connect-to-serial-port)`
     `(ALPHA)` Connect to the serial port of an instance. 
`[copy-files](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/copy-files)`
     `(ALPHA)` Copy files to and from Google Compute Engine virtual machines via scp. 
`[reset-windows-password](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reset-windows-password)`
     `(ALPHA)` Reset and return a password for a Windows machine instance. 
`[scp](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/scp)`
     `(ALPHA)` Copy files to and from Google Compute Engine virtual machines via scp. 
`[sign-url](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/sign-url)`
     `(ALPHA)` Sign specified URL for use with Cloud CDN Signed URLs. 
`[ssh](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/ssh)`
     `(ALPHA)` SSH into a virtual machine instance. 
`[start-iap-tunnel](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/start-iap-tunnel)`
     `(ALPHA)` Starts an IAP TCP forwarding tunnel. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute](https://docs.cloud.google.com/sdk/gcloud/reference/compute)
    
    
    [gcloud beta compute](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute)
    
    
    [gcloud preview compute](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
