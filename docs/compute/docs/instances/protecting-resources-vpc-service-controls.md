---
url: https://docs.cloud.google.com/compute/docs/instances/protecting-resources-vpc-service-controls/
title: Protecting resources with VPC Service Controls \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:35.407083+00:00
---

# Protecting resources with VPC Service Controls  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/protecting-resources-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Protecting resources with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

To further protect your Compute Engine resources, you can protect them using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

VPC Service Controls let you define a service perimeter for your Compute Engine resources. The service perimeter limits exporting and importing of resources and their associated data to within the defined perimeter.

When you create a service perimeter, you select one or more projects to be protected by the perimeter. Requests between projects within the same perimeter remain unaffected. All existing APIs continue to function as long as the resources involved are within the same service perimeter. Note the IAM roles and policies still apply within a service perimeter.

When a service is protected by a perimeter, requests cannot be made by the service _inside_ the perimeter to any resource _outside_ the perimeter. This includes exporting resources from inside to outside the perimeter. Requests for protected resources from _outside_ a perimeter is possible if they meet certain criteria. For more information, see [Overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview) in the [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) documentation.

When a request is made that violates the service perimeter, the request fails with the following error:

`"code": 403, "message": "Request is prohibited by organization's policy."`

## Security benefits

VPC Service Controls provide the following security benefits:

  * Access to sensitive Compute Engine API operations, such as changing firewall rules, can be restricted to private access from authorized networks or to IP addresses that are part of an allowlist.
  * Compute Engine persistent disk snapshots and custom images can be restricted to a perimeter.
  * Compute Engine instance metadata acts as a limited storage system. Access to instance metadata through the Compute Engine API is limited by service perimeter policy, mitigating exfiltration risks using this channel.



Additionally, the Compute Engine API is now accessible on the [restricted virtual IP (VIP)](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services). This simplifies the Cloud DNS and routing configuration for clients within the perimeter that need access to this API.

## Limitations

  * Configuring a load balancer to use backend services across different projects poses a potential data exfiltration risk. If you add one of these projects to a perimeter, the cross-project backend attachment can still allow data to move between projects even if you restrict the other project within a different perimeter. To mitigate this risk, we recommend that you enable the `constraints/compute.restrictCrossProjectServices` organization policy when you restrict the Compute Engine API within a perimeter. For more information, see [Restrict cross-project backend buckets and backend services](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints#cross-project-bb-bs).
  * Hierarchical firewalls are not affected by service perimeters.
  * VPC peering operations don't enforce VPC service perimeter restrictions.
  * The [`projects.ListXpnHosts`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/listXpnHosts) API method for Shared VPC does not enforce service perimeter restrictions on returned projects.



## Permissions

Make sure that you have the [proper roles](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) to administer VPC Service Controls Perimeter configurations for your organization.

## Set up a service perimeter

Follow the instructions at [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) in the VPC Service Controls documentation to set up a service perimeter.

If setting up a service perimeter by using the Google Cloud CLI, specify `compute.googleapis.com` with the `--restricted-services` flag to restrict the Compute Engine API.

## Adding Compute Engine as a restricted service to an existing perimeter

If you have an existing service perimeter and would like to add Compute Engine to the service perimeter, follow the instructions at [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) in the VPC Service Controls documentation.

## Creating a VM with VPC Service Controls

After setting up a service perimeter, you don't need to make any changes to existing API calls or tooling, as long as the affected resources in your requests are included in the same service perimeter. For example, the following command creates a VM instance with an example image. In this case, the command fails if the `IMAGE_PROJECT` is outside of the service perimeter (and there is no [service perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters) between the projects).
    
    
    gcloud compute instances create new-instance \
        --image-family IMAGE_FAMILY --image-project IMAGE_PROJECT \
        --zone us-central1-a --machine-type n1-standard-72
    

If you are creating a VM from an instance template, any resources referenced in the instance template must belong within the same service perimeter where you are running the command or be connected using a service perimeter bridge. The request fails if the instance template refers to a resource outside of the service perimeter, even if the instance template itself is within the perimeter.

For an example scenario of a Compute Engine client outside the perimeter creating a Compute Engine disk outside the perimeter using a Cloud KMS key inside the perimeter, see [Examples of API requests allowed by combination of ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#examples-allowed-ingress-egress-rules).

## Public image projects

All image projects listed on the [OS details](https://docs.cloud.google.com/compute/docs/images/os-details) page are automatically included in all service perimeters. In addition, the image projects for the [Fedora Cloud](https://docs.cloud.google.com/compute/docs/images#fedora_cloud), [openSUSE](https://docs.cloud.google.com/compute/docs/images#opensuse), and [HPC-ready VM images](https://docs.cloud.google.com/compute/docs/images/workload/hpc-vm-images) are also automatically included.

If you're using image projects that are not included in your service perimeter and don't want to add them directly, we recommend that you copy these image projects to a separate project. Then, you can add that project into your service perimeter.

## Copying images with VPC Service Controls

You can copy images from one project to another if both projects belong to the same service perimeter. In this example, both `DST_PROJECT` and `SRC_PROJECT` must belong to the same service perimeter for the request to work.
    
    
    gcloud compute images create --project DST_PROJECT IMAGE_NAME \
       --source-image SOURCE_IMAGE --source-image-project SRC_PROJECT \
        --family IMAGE_FAMILY --storage-location LOCATION
    

If you choose not to include the image project directly into your security perimeter, we recommend you make a copy of all of the images to be used into a separate project first, then include the separate project into your security perimeter.

## Shared VPC with VPC Service Controls

When using Shared VPC, service perimeter restrictions to apply to all projects involved in a given operation. In other words, we recommend that you make sure that the host project and service projects are within the same service perimeter when an operation involves resources distributed between the host and service projects.

## VPC Network Peering

[VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) allows peering VPC networks between two separate organizations. Because a service perimeter is limited to projects within an organization, service perimeters don't affect peering VPC networks.

## Hierarchical firewalls

Hierarchical firewalls are firewalls that are configured outside a project (either at the folder or at the organization level). Service perimeter restrictions don't apply to hierarchical firewalls.

## Managed instance groups

[Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) help you manage a group of VM instances as a single entity. Managed instance groups (MIGs) use instance templates to create VMs, and all restrictions around images or cross-project networks and subnetworks apply. That is, when using images from other projects, make sure the projects belong to the same perimeter, or copy the images you need into another project and include that project in the service perimeter. Google-maintained public image projects are automatically included in all service perimeters.

If you want to use instance groups with Shared VPC, make sure that your projects are in the same service perimeter.

## What's next

  * Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Learn about services supported by [restricted virtual IPs](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services).
  * Read more about [service perimeter configuration steps](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#stages). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
