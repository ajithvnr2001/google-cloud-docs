---
url: https://docs.cloud.google.com/vmware-engine/docs/whats-new/
title: What's new with VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:25.057599+00:00
---

# What's new with VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/whats-new/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# What's new with VMware Engine

This document highlights the latest updates to VMware Engine. The refreshed VMware Engine is integrated with the Google Cloud console, provides automation through new VMware Engine API and Google Cloud CLI workflows, and has simplified networking.

## Google Cloud console experience for VMware Engine

You can use the Google Cloud console to manage your VMware Engine environments directly inside the console without opening another tab.

## Simplified VMware networking architecture

Advancements in networking are further simplifying the VMware networking architecture and experience in VMware Engine. With zero-config VPC peering during private cloud creation, as well as increasing the limits on the number of peerings allowed, it radically simplifies the task of building a connected VMware Private Cloud while enabling a variety of networking topologies.

## Integrated Cloud DNS

Integrated Cloud DNS offers built-in support for bi-directional DNS resolution for both management and workload resolution. Additionally, support for more than 1 consumer DNS binding delivers enterprise needs in a less complex and more streamlined fashion.

## Additional Google Cloud CLI and VMware Engine API endpoints

More capabilities delivered using VMware Engine API and Google Cloud CLI enables users to programmatically manage VMware Engine environments, including VMware Engine API and Google Cloud CLI functions for managing the new networking model, network peering, external access rules and external IP service, consumer DNS and more.

## What's changed

The following sections describe changes you can expect when interacting with VMware Engine after cutover to the Google Cloud console.

## Changes to VPC Service Controls

If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), you no longer need to take additional steps or opt in to additional VMware Engine controls to interoperate with a project in a VPC Service Controls perimeter. For details, see [VPC Service Controls with VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls).

## Changes to point-to-site VPNs

Point to Site (P2S) VPNs were [deprecated starting March 2023](https://docs.cloud.google.com/vmware-engine/docs/release-notes#August_10_2022). For customers that are still using P2S, further configuration or listing of P2S VPNs is not possible. Any established P2S VPNs will remain operational. Contact [Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/getting-support) to remove legacy P2S VPNs. You can continue to use an alternative VPN solution. For details, see [Point-to-site VPN gateways](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways#point-to-site_vpn_gateways).

## Changes to firewall tables

Firewall rule tables will be migrated to External Access Rules. All rules will remain the same, but will be viewed and configured within External Access Rules.

## Changes to DNS profiles

Existing DNS Profiles will be migrated to each private cloud which the DNS Profile was assigned. DNS Conditional forwarding can be configured in the Google Cloud console within each private cloud.

## Changes to elevate privileges

Customers who use the privilege elevation option don't need to elevate privileges of the `CloudOwner@gve.local` user. You can log in using one of the solution users to perform elevated privileges actions. For details, see [Elevating VMware Engine privileges](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege).

## Transitioning to the Google Cloud console

You can take advantage of the Google Cloud console experience for performing VMware Engine tasks after a migration process.

### Data migration experience

The VMware Engine team will migrate projects over a period of time to the Google Cloud console. During this time, you will see two navigation options for VMware Engine. If you navigate to the incorrect console, you will be redirected to the right place to manage your private clouds.

The data migration will take place over a short duration that is expected to be less than 30 minutes and won't impact any of your private clouds or workloads operating within them. During the data migration, you can expect:

  * Access to the VMware Engine API and Google Cloud CLI
  * Access to vCenter, NSX-T, and HCX interfaces
  * No access to the Google Cloud console
  * No changes to the underlying network communication
  * No risk of network communication disruption



Once the data migration is complete, you can perform VMware Engine tasks from the Google Cloud console.

## FAQs

### What impact does this have on my private cloud and VMware workloads?

There will be no impact to your Private Cloud or VMware workloads because:

  * No changes are being made to the underlying infrastructure
  * No VMware stack components are being upgraded or modified
  * No networking infrastructure changes are being made
  * No data path traffic is being manipulated



### How long does it take?

Migration from the VMware Engine portal to the Google Cloud console is expected to be less than 30 minutes. During this time, only the Google Cloud console will be inaccessible. You will receive a message indicating that the migration is taking place in the UI if you navigate to the Google Cloud console during this time.

**Note:** the Google Cloud CLI and VMware Engine API remain available during this time.

### When will my project be migrated?

You will receive a notification when your project is planned to be migrated.

### How can I get sign-in credentials during data migration using the Google Cloud CLI?

If you are unable to wait for the completion of the data migration and need to get sign-in credentials urgently, use the following Google Cloud CLI commands:

VMware vCenter: Use the [`gcloud vmware private-clouds vcenter credentials describe`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/vcenter/credentials/describe) command, for example:
    
    
    gcloud vmware private-clouds vcenter credentials describe \
        --private-cloud=my-private-cloud \
        --location=us-west2-a \
        --project=my-project
    

VMware NSX-T: Use the [`gcloud vmware private-clouds nsx credentials describe`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/nsx/credentials/describe) command, for example:
    
    
    gcloud vmware private-clouds nsx credentials describe \
        --private-cloud=my-private-cloud \
        --location=us-west2-a \
        --project=my-project
    

### How can I get sign-in credentials during data migration using the VMware Engine API?

If you are unable to wait for the completion of the data migration and need to get sign-in credentials urgently, use the VMware Engine API:

  * For VMware vCenter: Use [Method: projects.locations.privateClouds.showVcenterCredentials](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds/showVcenterCredentials)
  * For VMware NSX-T: Use [Method:projects.locations.privateClouds.showNsxCredentials](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds/showNsxCredentials)



## What's next

  * [Access the Google Cloud console](https://docs.cloud.google.com/vmware-engine/docs/howto-access-portal)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
