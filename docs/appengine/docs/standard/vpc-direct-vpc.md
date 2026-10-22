---
url: https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc/
title: Direct VPC egress \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:41.268022+00:00
---

# Direct VPC egress  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Direct VPC egress Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Direct VPC egress for App Engine**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Direct VPC egress provides a high-performing networking solution for your App Engine service to send traffic to a Virtual Private Cloud (VPC) network. Direct VPC egress lets workloads seamlessly access VPC network resources and removes the need to configure Serverless VPC Access connectors.

## Key benefits

  * **Simplified management** : Eliminates the operational overhead of managing connector instances, machine types, and scaling settings. App Engine handles configurations directly within your service's `app.yaml` file.
  * **Cost efficiency** : Using Direct VPC egress has no additional charge, and you don't have to pay fixed monthly charges for connector VMs.
  * **Improved performance and reliability** : By eliminating the need to use a connector, Direct VPC egress offers a faster, more reliable connection to your VPC network resources. It scales as quickly as your App Engine service and avoids connection drops that might occur with connectors during maintenance.
  * **Granular security** : You can apply network tags directly to your App Engine service versions, enabling precise, service-specific firewall rules and network policies.

  * **Supports VPC Flow Logs** : You can enable [VPC Flow Logs on your subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs) to log egress traffic from your App Engine service.




## Limitations

  * **IP address consumption** : Your service's IP address usage scales directly with the number of running instances, and your scaling ability is limited by the number of available IP addresses in your chosen subnet.

  * **Maintenance events** : Your service might experience brief connection breaks during networking infrastructure maintenance events. We recommend that you use client libraries for handling occasional connection resets.

  * **Cold starts** : Initial cold start times are dependent on the region and the specific use case. In rare cases, cold starts might last up to a minute.

  * **Direct VPC ingress** : App Engine doesn't support Direct VPC ingress.

  * **Number of instances** : You can only configure up to 100 instances per App Engine version to use Direct VPC egress.

  * **VPC Flow Logs** : Doesn't display your App Engine service version in the log records. The service name is displayed in the [`AppEngineServiceDetails`](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#app-engine-service-details) field.




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

## Before you begin

  1. Make sure you have an existing VPC network and a subnet in your project. If you don't already have an existing VPC, follow the instructions to create one in [Create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  2. Enable the Compute Engine API and the Cloud Build API:

[Enable APIs](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com,cloudbuild.googleapis.com)

  3. To use Direct VPC egress, make sure you are running the most recent version of the Google Cloud CLI:
         
         gcloud components update




## Required roles

Ensure that App Engine has access to the VPC network by granting the following roles to your deploying service account:

  * **App Engine Service Agent role** : By default, the App Engine service agent has the [App Engine Service Agent role (`roles/appengine.serviceAgent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) that contains the necessary permissions.

  * **Custom permissions** : For more granular control, grant the App Engine service agent the following additional permissions on the project:

    * `compute.networks.get`
    * `compute.subnetworks.get`
    * `compute.subnetworks.use` on the project or the specific subnet
    * `compute.addresses.get`
    * `compute.addresses.list`
    * `compute.addresses.create`
    * `compute.addresses.delete`
    * `compute.addresses.createInternal`
    * `compute.addresses.deleteInternal`
    * `compute.regionOperations.get`
  * **Compute Network User role** : If you don't use the default App Engine Service Agent role or the custom permissions, grant the [Compute Network User role (`roles/compute.networkUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) on the App Engine Service Agent service account. Subnets with external IPv6 also require the [Compute Public IP Admin role (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin).

For example, to grant the Compute Network User role, run the following command:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:service-PROJECT_NUMBER@gcp-gae-service.iam.gserviceaccount.com" \
        --role "roles/compute.networkUser"

Replace the following:

    * PROJECT_ID: the ID of your project.
    * PROJECT_NUMBER: the project number where you deploy your App Engine service.



## Configure an App Engine service with Direct VPC egress

To enable a new or existing App Engine service to connect directly to your VPC network, follow these steps:

  1. Add the following `vpc_access` setting to your `app.yaml` file:
         
         vpc_access:
           network_interface:
             network: NETWORK
             subnet: SUBNET
             tags:
                 - NETWORK_TAGS
           vpc_egress: EGRESS_SETTING

Replace the following:

     * NETWORK: the name of the existing network your application instances connect to, for example, `default`. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.

     * SUBNET: the name of the existing subnetwork your application instances connect to, for example, `default`. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.

     * Optional: NETWORK_TAGS: a list of [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) to associate with your App Engine service's instances for use in firewall rules and routing policies.

     * Optional: EGRESS_SETTING: controls how outbound traffic is routed. This field supports the following configuration settings:

       * `all-traffic`: All outbound requests are routed through the VPC network.
       * `private-ranges-only` (default): Only traffic to internal IP addresses is routed through the VPC network. Internet traffic uses the default App Engine path.
  2. Deploy to App Engine by running the following command:
         
         gcloud beta app deploy




### Disconnect a service

To disconnect your service from the VPC network:

  1. Remove the `vpc_access` section from your `app.yaml` file.

  2. Redeploy your service:
         
         gcloud beta app deploy




## Best practices for IP management

It is necessary to manage your IP addresses since each instance of your service consumes an IP address from your subnet. Use the following strategies for managing your IP addresses:

  * **Recommended IP range** : For best compatibility, we recommend starting with the RFC 6598 (`100.64.0.0/10`) range.

  * **Alternative IP ranges** : If you are already using the recommended IP range of `100.64.0.0/10`, you can use non-RFC 1918 ranges, such as Class E (`240.0.0.0/4`) in your subnet.

  * **Subnet sizing** : Ensure your subnet's IPv4 address range is `/26` or larger to provide enough addresses for scaling.

  * **Overprovision IPs** : We recommend overprovisioning the number of available IPs in your subnet to avoid exhaustion. Similar to Cloud Run services, you should typically use four times as many IPs (2X for steady state and an additional 2X during deployment) as the number of running instances to facilitate smooth scaling and updates.




## Troubleshoot

This section describes the common errors you might encounter while deploying your App Engine service with Direct VPC egress.

### Cannot delete subnet

To delete a subnet, you must first delete or redeploy all resources that use it. If App Engine is using a subnet, disconnect the App Engine service from the VPC network or move it to a different subnet before deleting the subnet.

After you delete or move your App Engine service, wait 1-2 hours for App Engine to release the IP addresses before you delete the subnet.

### Deployment failures

If your deployment fails, the Google Cloud CLI displays error messages indicating the root cause. Some common issues include the following:

  * Incorrect VPC metadata, such as a misspelled network or subnet name in your `app.yaml` file. To fix potential errors, review the VPC configuration in your `app.yaml` file.

  * Insufficient IAM permissions. Make sure you grant the required permissions on your deploying service account. If you encounter permission errors during deployment, ensure that you grant the following additional roles to the service account:

    * [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)
    * [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`)



### IP address exhaustion

If your subnet runs out of available IP addresses, App Engine fails to start new instances and [logs an error](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs?tab=python#view_logs). To resolve this issue, expand the IP range of your subnet or move your service to a larger subnet.

### IP address leaks

IP address leaks might lead to IP address exhaustion. IP address leaks are unlikely during standard operations, but might occur due to the following causes:

  * Your deploying service account only has permissions to reserve addresses (`create`, `createInternal`) and lacks permissions to release addresses (`delete`, `deleteInternal`).
  * Your service account was deleted while other Google Cloud address reservations were active.
  * The Cloud Billing account was removed and later re-enabled in the project while Serverless address reservations were active.
  * Your Google Cloud project was deleted and later restored while Serverless address reservations still existed.



To resolve this issue, follow these steps:

  1. Query for the following logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries#building-queries) to identify the leaked addresses:
         
         protoPayload.authorizationInfo.permission=~"compute.addresses.delete.*"
         protoPayload.authorizationInfo.resourceAttributes.type="compute.addresses"
         protoPayload.resourceName=~"projects/.*/regions/.*/addresses/serverless-.*"
         severity>=WARNING
         

If this query doesn't return results, there are no IP address leaks, and no further action is required.

  2. If your query returns results, make sure that your deploying service account contains the [App Engine Service Agent role (`roles/appengine.serviceAgent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent). If you can't use this role, ensure that you grant other required roles and permissions on your deploying service account.

  3. Manually delete leaked IP addresses by using the Google Cloud console or the Google Cloud CLI:

###  Console 

     1. Go to the **IP addresses** page in the Google Cloud console:

[Go to IP addresses](https://console.cloud.google.com/networking/addresses)

     2. Select the leaked IP addresses you identified in the previous step by running the query.

     3. Click **Release static address** to remove the leaked addresses.

###  gcloud 

Run the [`gcloud compute addresses delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/delete) command:
    
    gcloud compute addresses delete ADDRESS_NAME --region=REGION

Replace the following:

     * ADDRESS_NAME: the name of the leaked IP address.
     * REGION: the region of the leaked IP address.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
