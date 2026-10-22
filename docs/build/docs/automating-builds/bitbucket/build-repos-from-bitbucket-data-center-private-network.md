---
url: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center-private-network/
title: Build repositories from Bitbucket Data Center in a private network \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:34.955671+00:00
---

# Build repositories from Bitbucket Data Center in a private network  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center-private-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build repositories from Bitbucket Data Center in a private network Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

Cloud Build lets you create triggers to build from repositories hosted on [Bitbucket Data Center](https://confluence.atlassian.com/bitbucketserver/bitbucket-data-center-and-server-documentation-776639749.html), allowing you to execute builds in response to events such as commit pushes or pull requests associated with your Bitbucket Data Center repository.

This page explains how you can enable trigger functionality on a Bitbucket Data Center instance if your instance is hosted in a private network.

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center)



  * Follow the instructions to [connect a Bitbucket Data Center host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center).
  * Follow the instructions to [connect a Bitbucket Data Center repository](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-data-center).



## Build repositories from Bitbucket Data Center in a private network

If your Bitbucket Data Center instance is only accessible within a VPC network, you need to set up a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) Service Directory service and build using private pools. The project containing your VPC network can exist in a different project than the one containing your Service Directory service. Use the following steps to set up Service Directory and create a Bitbucket Data Center trigger:

  1. Enable the [Service Directory API](https://console.cloud.google.com/apis/library/servicedirectory.googleapis.com).

  2. Grant the **Project IAM Admin** role to the Google Cloud project you intend to create your Service Directory service in. To learn how to grant IAM roles, see [Configuring access to Cloud Build resources](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources).

  3. Set up a Service Directory service by completing the following steps:

     1. [Configure a namespace](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configure_a_namespace) for your Google Cloud project.

The region you specify in your namespace **must** match the region you specify in your Cloud Build host connection.

     2. [Configure a service](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configure_a_service) in your namespace.

     3. [Configure an endpoint](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configure_an_endpoint) for your registered service.

When configuring an endpoint, you **must** use an internal IP address and specify an HTTPS port number in order for Cloud Build to reach your service.

To learn more about private network access configuration, see [Configure private network access](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access). Service Directory also provides integration with services such as load balancers and Google Kubernetes Engine (GKE). To learn more, see [Service Directory and load balancing overview](https://docs.cloud.google.com/service-directory/docs/sd-lb-overview) or [Service Directory for GKE overview](https://docs.cloud.google.com/service-directory/docs/sd-gke-overview).

  4. Grant Service Directory access to the Cloud Build service agent:
         
         export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         export CLOUD_BUILD_SERVICE_AGENT="service-$PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud projects add-iam-policy-binding  PROJECT_ID_CONTAINING_SERVICE_DIRECTORY \
            --member="serviceAccount:$CLOUD_BUILD_SERVICE_AGENT" \
            --role="roles/servicedirectory.viewer"
         

Replace the following:

     * PROJECT_ID is your Cloud Build project ID.
     * PROJECT_ID_CONTAINING_SERVICE_DIRECTORY is the ID of your Google Cloud project that contains your Service Directory.
  5. Grant VPC network resource access to the Cloud Build service agent:
         
         export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         export CLOUD_BUILD_SERVICE_AGENT="service-$PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud projects add-iam-policy-binding PROJECT_ID_CONTAINING_NETWORK_RESOURCE \
            --member="serviceAccount:$CLOUD_BUILD_SERVICE_AGENT" \
            --role="roles/servicedirectory.pscAuthorizedService"
         

Replace the following:

     * PROJECT_ID is your Cloud Build project ID.
     * PROJECT_ID_CONTAINING_NETWORK_RESOURCE is the ID of your Google Cloud project that contains your network resource.
  6. Use [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) to run your builds. If you have not created a private pool, see [create a new private pool](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).

  7. Follow the instructions to [create a Bitbucket Data Center trigger](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center) to build repositories hosted on a Bitbucket Data Center instance.

If you include a self-signed or private certificate when connecting your Bitbucket Data Center host to Cloud Build, you _must_ set the host URI as the Subject Alternative Name (SAN) of your certificate.




Your Bitbucket Data Center trigger will now automatically invoke builds on your Bitbucket Data Center instance based on your configuration.

## Use Service Directory to reach hosts outside Google Cloud

Service Directory uses the IP address range `35.199.192.0/19` to connect your host outside of Google Cloud. You must add this range to an allowlist in your firewall. Additionally, your private network needs to be configured to route this range through the Cloud VPN or Cloud Interconnect connection.

If your connection uses a Cloud Router, you can configure your connection to [communicate](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) the range to your private network.

To learn more, see [Configure private network access](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access).

### Use Cloud Load Balancing to reach hosts outside Google Cloud

If your network configuration does not allow you to route the Service Directory IP address range `35.199.192.0/19` to the Cloud VPN or Cloud Interconnect, you can [create a load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) using Cloud Load Balancing that directs traffic to your host.

When you create the Service Directory endpoint, make sure to use the IP address of the forwarding rule of the load balancer instead of the IP address of your host. You can use an [internal HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-int-https-hybrid) or an [internal transmission control protocol (TCP) load balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid) when creating your endpoint.

When creating your TCP load balancer, consider the following:

  * Only a hybrid connectivity network endpoint group (NEG) is required to reach your host.
  * The TCP load balancer does not require the unencrypted private key for your SSL certificate.
  * Your Cloud VPN setup needs to use Cloud Router with global dynamic routing. If your Cloud VPN uses static routing, you can use a proxy that uses Cloud Service Mesh instead. To learn more, see [Set up network edge services for hybrid deployments](https://docs.cloud.google.com/traffic-director/tutorials/network-edge-services-multi-environment).



To learn more about creating an HTTPS load balancer, see [Set up an internal Application Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-int-https-hybrid). To learn more about creating a TCP load balancer, see [Set up a regional internal proxy Network Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid).

## Data sharing

The data sent to Bitbucket Data Center from Cloud Build helps you identify triggers by name and see build results on your Bitbucket Data Center repositories.

The following data is shared between Cloud Build and Bitbucket Data Center:

  * Google Cloud project ID
  * Trigger name



## What's next

  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [perform blue/green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
