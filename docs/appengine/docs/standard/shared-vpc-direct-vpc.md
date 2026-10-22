---
url: https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-direct-vpc/
title: Direct VPC egress with a Shared VPC network \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:13.254163+00:00
---

# Direct VPC egress with a Shared VPC network  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-direct-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Direct VPC egress with a Shared VPC network Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Direct VPC egress for App Engine**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enable your App Engine service to send traffic to a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks) by using Direct VPC egress with no Serverless VPC Access connector required.

This page describes how to configure App Engine's IAM permissions to use the subnet of the Shared VPC network, and then place your service on the shared subnet.

## Before you begin

Review the IP address allocation section for guidance with allocating IP addresses from your subnet.

## Limitations

  * **IP address consumption** : Your service's IP address usage scales directly with the number of running instances, and your scaling ability is limited by the number of available IP addresses in your chosen subnet.

  * **Maintenance events** : Your service might experience brief connection breaks during networking infrastructure maintenance events. We recommend that you use client libraries for handling occasional connection resets.

  * **Cold starts** : Initial cold start times are dependent on the region and the specific use case. In rare cases, cold starts might last up to a minute.

  * **Direct VPC ingress** : App Engine doesn't support Direct VPC ingress.

  * **Number of instances** : You can only configure up to 100 instances per App Engine version to use Direct VPC egress.

  * **VPC Flow Logs** : Doesn't display your App Engine service version in the log records. The service name is displayed in the [`AppEngineServiceDetails`](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#app-engine-service-details) field.




## Set up IAM permissions

Before App Engine in a Shared VPC service project can access a Shared VPC network, make sure the App Engine service agent has sufficient permissions to use the subnet.

  * **App Engine Service Agent role** : To access the Shared VPC network, grant sufficient permissions to the [App Engine service agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) by adding one of the following roles:

    * [Compute Network User (`roles/compute.networkUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) on the Shared VPC host project. Subnets with external IPv6 also require the [Compute Public IP Admin (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) role.

For example, to grant the Compute Network User role, run the following command:
          
          gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
          --member "serviceAccount:service-SERVICE_PROJECT_NUMBER@gcp-gae-service.iam.gserviceaccount.com" \
          --role "roles/compute.networkUser"

Replace the following:

      * HOST_PROJECT_ID: the ID of your Shared VPC host project.
      * SERVICE_PROJECT_NUMBER: the Shared VPC service project number where you deploy your App Engine service.
    * [Compute Network Viewer (`compute.networkViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) on the Shared VPC host project and the [Compute Network User (`compute.networkUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) role on the Shared VPC subnet. Subnets with external IPv6 also require the [Compute Public IP Admin (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) role.

For example, to grant the Compute Network User role on the subnet, run the following command:
          
          gcloud compute networks subnets add-iam-policy-binding SUBNET_NAME \
            --region REGION \
            --member "serviceAccount:service-SERVICE_PROJECT_NUMBER@gcp-gae-service.iam.gserviceaccount.com" \
            --role "roles/compute.networkUser" \
            --project HOST_PROJECT_ID

Replace the following:

      * SUBNET_NAME: the fully qualified resource name of the subnet that you want to run your App Engine services.
      * REGION: the region for your App Engine service, which must match the region of your subnet.
      * SERVICE_PROJECT_NUMBER: the Shared VPC service project number where you deploy your App Engine service.
      * HOST_PROJECT_ID: the ID of your Shared VPC host project.
  * **Custom permissions** : For more granular control, grant the App Engine service agent the following additional permissions on the project:

    * `compute.networks.get` on the Shared VPC host project
    * `compute.subnetworks.get` on the host project or the specific subnet
    * `compute.subnetworks.use` on the host project or the specific subnet
    * `compute.addresses.get` on the Shared VPC service project
    * `compute.addresses.list` on the Shared VPC service project
    * `compute.addresses.create` on the Shared VPC service project
    * `compute.addresses.delete` on the Shared VPC service project
    * `compute.addresses.createInternal` on the Shared VPC service project
    * `compute.addresses.deleteInternal` on the Shared VPC service project
    * `compute.regionOperations.get` on the Shared VPC service project



## IP address allocation

To place your App Engine service on a VPC network, specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. App Engine allocates IP addresses from your subnet.

IP addresses are ephemeral, so don't create policies based on individual IPs. If you need to create a policy based on IPs, such as in firewall rules, you must use the IP address range of the entire subnet.

To change the network or subnet that your service uses, deploy a new version that uses the new network and subnet values.

### Scale up and scale down

For faster scale up during a traffic surge, App Engine reserves IP addresses in blocks of 16 (`28` subnet mask) at a time. To ensure that you have enough IPv4 addresses available for use across App Engine, your subnet's IPv4 address range must be `/26` or larger.

For IP allocation efficiency and ease of management, place multiple resources on the same subnet. If your IPv4 address space is limited, see Supported IPv4 ranges for more options.

To delete the subnet, you must first delete or redeploy your App Engine service to stop using the subnet, and then wait 1-2 hours.

### IP address consumption for services

At steady state, App Engine uses 2 times (2X) as many IP addresses as the number of instances. When a version scales down, App Engine retains its IP addresses for up to 20 minutes. In total, reserve at least 2X the number of IP addresses, plus a buffer to account for version updates.

For example, if you upgrade versions so that `version 1` scales from 100 instances down to zero while `version 2` scales from zero up to 100, App Engine retains the `version 1` IP addresses for up to 20 minutes after scaling down. During the 20-minute retention window, you must reserve at least 400 IP addresses (`(100 + 100) * 2`).

### Supported IPv4 ranges

App Engine supports the following IPv4 ranges for your subnet:

  * [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)
    * `10.0.0.0/8`
    * `172.16.0.0/12`
    * `192.168.0.0/16`
  * [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7)
    * `100.64.0.0/10`
  * Class E 
    * `240.0.0.0/4`

**Note:** Test non-RFC 1918 setups to identify possible compatibility issues with non-Google Cloud resources or hardware. Learn more about [creating subnets with non-RFC 1918 IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).

## Deploy an App Engine service

Direct VPC egress allows your App Engine service to send traffic to a Shared VPC network without a Serverless VPC Access connector. You can assign network tags to a specific version of your App Engine service for more granular network security, such as applying [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

To place your service on the shared subnet, specify the fully qualified resource names for the Shared VPC network and subnet in your `app.yaml` file.

  1. Update your `app.yaml` file to include the `vpc_access` section:
         
         vpc_access:
           network_interface:
             network: projects/HOST_PROJECT_ID/global/networks/VPC_NETWORK
             subnet: projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
             tags:
                 - NETWORK_TAGS
           vpc_egress: EGRESS_SETTING

Replace the following:

     * HOST_PROJECT_ID: the ID of your Shared VPC project.
     * VPC_NETWORK: the name of your Shared VPC network.
     * REGION: the region for your App Engine service, which must match the region of your subnet.
     * SUBNET_NAME: the fully qualified resource name of your subnet.
     * Optional: NETWORK_TAGS: a list of network tags to associate with your App Engine service's instances for use in firewall rules and routing policies.
     * Optional: EGRESS_SETTING: controls how outbound traffic is routed. This field supports the following configuration settings:

       * `all-traffic`: Sends all outbound traffic through the Shared VPC network.
       * `private-ranges-only` (default): Sends only traffic to internal addresses through the Shared VPC network.
  2. Deploy your service by running the following command:
         
         gcloud beta app deploy




## Disconnect a service

To remove your service from the Shared VPC network:

  1. Remove the `vpc_access` section from your `app.yaml` file.
  2. Redeploy your service:
         
         gcloud beta app deploy




## Troubleshoot

This section describes common errors you might encounter when using Direct VPC egress with a Shared VPC network and provides guidance on how to resolve them.

### Cannot delete subnet

To delete a subnet, you must first delete all resources that use it. If App Engine is using a subnet, you must disconnect it or move it to a different subnet before deleting the subnet.

After you delete or move your App Engine resources, wait 1-2 hours for App Engine to release the IPs before you delete the subnet.

### Deployment failures

If your deployment fails, the Google Cloud CLI displays error messages indicating the root cause. Some common issues include the following:

  * Incorrect VPC network metadata, such as a misspelled network or subnet name in your `app.yaml` file. To fix potential errors, review the VPC network configuration in your `app.yaml` file.

  * Insufficient IAM permissions. Make sure you grant the required permissions on your deploying service account. If you encounter permission errors during deployment, ensure that you grant the following additional roles to the service account:

    * [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)
    * [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`)



### Cannot detach Shared VPC network

To detach the Shared VPC network in the host project, follow the steps to [Deprovision Shared VPC](https://docs.cloud.google.com/vpc/docs/deprovisioning-shared-vpc) and be sure to disconnect any App Engine services from the Shared VPC network.

To see which App Engine resources are using the Shared VPC network, run the following command:
    
    
    gcloud compute shared-vpc list-associated-resources HOST_PROJECT_ID

Replace HOST_PROJECT_ID with the ID of your Shared VPC host project.

### Direct VPC egress subnet runs out of IPv4 addresses

If the subnet of the VPC network runs out of IPv4 addresses, App Engine cannot start any more service instances.

To resolve this issue, consider moving to a subnetwork with more available IP addresses or expanding the subnet range.

### View allocated IP addresses

To see which IP addresses App Engine has allocated, go to the [IP addresses page](https://console.cloud.google.com/networking/addresses) in the Google Cloud console or run the following command from the Google Cloud CLI:
    
    
    gcloud compute addresses list

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
