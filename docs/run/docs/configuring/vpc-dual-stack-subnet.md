---
url: https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet/
title: Set up dual-stack (IPv4 and IPv6) \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:47.759092+00:00
---

# Set up dual-stack (IPv4 and IPv6)  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set up dual-stack (IPv4 and IPv6) Stay organized with collections  Save and categorize content based on your preferences. 

Dual-stack subnets let your Cloud Run resources send IPv4 and IPv6 traffic to a VPC network with Direct VPC egress. You can change an existing IPv4 only (single-stack) subnet to a dual-stack subnet.

## Subnet types

VPC networks support the following [Compute Engine subnet types](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types):

  * IPv4 only (single-stack) subnets, with only [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges)

  * IPv4 and IPv6 (dual-stack) subnets, with both IPv4 and [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges)




## Dual-stack limitations

Before you change the stack type on an existing Cloud Run resource, consider the following limitations:

  * Dual-stack support is only available with subnets in a custom-mode VPC network. To have the internal access type available for dual-stack subnets, the VPC network internal IPv6 range must be enabled. Set up or [convert](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-network-mode) the VPC network to custom mode.

  * Compared to IPv4-only subnets, dual-stack subnets might experience elevated cold-start latencies, limiting how quickly your application can scale up.

  * [NAT64](https://tools.ietf.org/html/rfc6146) is not supported.




## Before you begin

Be sure that the [Cloud Run service agent](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-direct-vpc#iam) has the [Compute Public IP Admin role (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) to use the subnet with external IPv6.

## Add a dual-stack subnet on a resource

Dual-stack subnets have both IPv4 and IPv6 address ranges.

To add a dual-stack subnet on a Cloud Run resource, do the following:

###  Console 

  1. In the Google Cloud console:

     1. Enable the Compute Engine API:

[Enable the Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com)

     2. Go to the **VPC networks** page:

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network** if you are creating a new custom-mode network. If you are using an existing VPC network, click the name of the VPC network to show its _VPC network details_ page.

  3. If you are creating a new network or converting an existing one, enter the name and be sure that the **Subnet creation mode** is set to **Custom** , then select **Configure a ULA internal IPv6 range for this VPC Network**.

  4. From the **Subnets** tab, click **Add subnet**. In the panel that appears:

     1. Provide a **Name**.
     2. Select a **Region**.
     3. For **IP stack type** , select **IPv4 and IPv6 (dual-stack)**.
     4. Enter an **IPv4 range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.
     5. Select the **IPv6 access type**.

If the **Internal** option is not available and you need it, check that an internal IPv6 range is assigned on the network.

     6. Click **Add**.

  5. [Deploy a Cloud Run service](https://docs.cloud.google.com/run/docs/deploying), [execute a job](https://docs.cloud.google.com/run/docs/execute/jobs#execute_jobs), or [deploy a worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools) on the dual-stack subnet that you created. As you enter the needed resource details, select the new IPv6 address range by following these steps:

     1. Click **Container(s), Volumes, Networking, Security** and select the **Networking** tab.
     2. Click **Connect to a VPC for outbound traffic** and then **Send traffic directly to a VPC**.
     3. Select the **Network** that you created in the previous step.
     4. Click the **Subnet** field to select the newly created IPv6 address range.

The resource is automatically provisioned with the subnet's stack type.




###  gcloud 

  1. To create a custom-mode network that supports dual-stack subnets, run the `gcloud compute networks create` command.

To configure _internal_ IPv6 ranges on any subnets in this network, use the `--enable-ula-internal-ipv6` flag. This option assigns a `/48` ULA prefix from within the `fd20::/20` range used by Google Cloud for internal IPv6 subnet ranges.
         
         gcloud compute networks create NETWORK \
           --subnet-mode=custom \
           --enable-ula-internal-ipv6
         

Replace `NETWORK` with the name of the VPC network that will contain the new subnet.

  2. To convert to or update a custom-mode network so that it supports dual-stack subnets, run the following command:
         
         gcloud compute networks update NETWORK \
           --switch-to-custom-subnet-mode \
           --enable-ula-internal-ipv6
         

Replace `NETWORK` with the name of the VPC network that will contain the new subnet.

  3. To create a dual-stack subnet with an IPv6 range, run the [`subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) using the dual-stack settings:
         
         gcloud compute networks subnets create SUBNET \
           --network=NETWORK \
           --range=PRIMARY_IPv4_RANGE \
           --stack-type=IPV4_IPV6 \
           --ipv6-access-type=IPV6_ACCESS_TYPE \
           --region=REGION
         

Replace the following:

     * `SUBNET`: a name for the new subnet.
     * `NETWORK`: the name of the VPC network that will contain the new subnet.
     * `PRIMARY_IPv4_RANGE`: the primary IPv4 range for the new subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
     * `IPV6_ACCESS_TYPE`: the IPv6 access type for the new subnet, either `internal` or `external`.
     * `REGION`: the Google Cloud region that the new subnet will be created in.
  4. [Deploy a Cloud Run service](https://docs.cloud.google.com/run/docs/deploying), [execute a job](https://docs.cloud.google.com/run/docs/execute/jobs#execute_jobs), or [deploy a worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools) on the dual-stack subnet that you created. The resource is automatically provisioned with the subnet's stack type.




### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the following attributes:
         
         apiVersion: serving.knative.dev/v1
           kind: Service
           metadata:
             name: SERVICE_NAME
             labels:
               cloud.googleapis.com/location: REGION
           spec:
             template:
               metadata:
                 annotations:
                   run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET","tags":"NETWORK_TAG_NAMES"}]'
                   run.googleapis.com/vpc-access-egress: EGRESS_SETTING
               spec:
                 containers:
                 - image: IMAGE

Replace:

     * SERVICE_NAME with the name of your Cloud Run service. Service names must be 49 characters or less and must be unique per region and project.
     * REGION with the region for your Cloud Run service, which must match the region of your subnet.
     * NETWORK with the name of your VPC network.
     * SUBNET with the name of your subnet. You can deploy or execute multiple services, jobs, or worker pools on the same subnet. 
     * Optional: NETWORK_TAG_NAMES with the names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a service. For services, network tags are specified at the revision-level. Each service revision can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress): 
       * `all-traffic`: Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
     * IMAGE with the URL of your service container image.

You can also [specify more configuration](https://docs.cloud.google.com/run/docs/how-to#configure), such as environment variables or memory limits.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Add the following to your `main.tf` file:
         
         /**
          * Copyright 2024 Google LLC
          *
          * Licensed under the Apache License, Version 2.0 (the "License");
          * you may not use this file except in compliance with the License.
          * You may obtain a copy of the License at
          *
          *      http://www.apache.org/licenses/LICENSE-2.0
          *
          * Unless required by applicable law or agreed to in writing, software
          * distributed under the License is distributed on an "AS IS" BASIS,
          * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
          * See the License for the specific language governing permissions and
          * limitations under the License.
          */
         
         # Example configuration of a Cloud Run service with direct VPC
         
         resource "google_cloud_run_v2_service" "default" {
           name     = "cloudrun-service"
           location = "us-central1"
         
           deletion_protection = false # set to "true" in production
         
           template {
             containers {
               image = "us-docker.pkg.dev/cloudrun/container/hello"
             }
             vpc_access {
               network_interfaces {
                 network    = "default"
                 subnetwork = "default"
                 tags       = ["tag1", "tag2", "tag3"]
               }
             }
           }
         }
         




**Note:** Administrators can restrict the egress settings that developers can select by setting the [`run.allowedVPCEgress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

Optionally, [make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.

## Change a subnet from single-stack to dual-stack

To add an IPv6 subnet range to an existing IPv4-only subnet in a custom-mode VPC network, see [Change a subnet's stack type to dual-stack](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6). Then, [deploy the Cloud Run service](https://docs.cloud.google.com/run/docs/deploying), [execute the job](https://docs.cloud.google.com/run/docs/execute/jobs#execute_jobs), or [deploy the worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools) on the dual-stack subnet.

## Change a subnet from dual-stack to single-stack

To change a resource's dual-stack subnet to a single-stack subnet, see [Change a dual-stack subnet to IPv4 only](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-change-stacktype). Then, [deploy the Cloud Run service](https://docs.cloud.google.com/run/docs/deploying), [execute the job](https://docs.cloud.google.com/run/docs/execute/jobs#execute_jobs), or [deploy the worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools) on the dual-stack subnet.

## Verify the network and subnet

To check that your resource is on the VPC network, run the following command:
    
    
    gcloud run services describe SERVICE_NAME --region=REGION

Replace `REGION` with the Google Cloud region that the new subnet was created in.

The following example output shows your network and subnet:
    
    
      VPC Access:
        Network:        example-network
        Subnet:         example-subnet
        Egress:         private-ranges-only
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
