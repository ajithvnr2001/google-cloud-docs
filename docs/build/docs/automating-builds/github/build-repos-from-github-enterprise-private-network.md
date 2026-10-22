---
url: https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network/
title: Build repositories from GitHub Enterprise in a private network \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:56.937203+00:00
---

# Build repositories from GitHub Enterprise in a private network  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build repositories from GitHub Enterprise in a private network Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

Cloud Build enables you to create triggers on a GitHub Enterprise instance. This page explains how you can use GitHub Enterprise triggers to invoke builds in response to commits or pull requests from a GitHub Enterprise instance and explains how you can build repositories from GitHub Enterprise if your instance is hosted in a private network.

## Before you begin

  * Enable the Cloud Build and Service Directory APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,servicedirectory.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network)



  * If you have not created a private pool, follow the instructions in [Create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools) to create a private pool. You will need a private pool to build in a private network.



## Build repositories from GitHub Enterprise in a private network

Complete the following steps to connect your GitHub Enterprise instance to Cloud Build from a private network:

  1. Grant Service Directory access to the Cloud Build service agent:
         
         export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         export CLOUD_BUILD_SERVICE_AGENT="service-$PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud projects add-iam-policy-binding  PROJECT_ID_CONTAINING_SERVICE_DIRECTORY \
            --member="serviceAccount:$CLOUD_BUILD_SERVICE_AGENT" \
            --role="roles/servicedirectory.viewer"
         

Replace the following:

     * PROJECT_ID is your Cloud Build project ID.
     * PROJECT_ID_CONTAINING_SERVICE_DIRECTORY is the ID of your Google Cloud project that contains your Service Directory.
  2. Grant VPC network resource access to the Cloud Build service agent:
         
         export PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         export CLOUD_BUILD_SERVICE_AGENT="service-$PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud projects add-iam-policy-binding PROJECT_ID_CONTAINING_NETWORK_RESOURCE \
            --member="serviceAccount:$CLOUD_BUILD_SERVICE_AGENT" \
            --role="roles/servicedirectory.pscAuthorizedService"
         

Replace the following:

     * PROJECT_ID is your Cloud Build project ID.
     * PROJECT_ID_CONTAINING_NETWORK_RESOURCE is the ID of your Google Cloud project that contains your network resource.
  3. Set up a Service Directory service by completing the following steps:

     1. Configure a [namespace](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configure_a_namespace) for your service:
            
            gcloud service-directory namespaces create NAMESPACE --location=REGION --project=PROJECT_ID_CONTAINING_SERVICE_DIRECTORY
            

Replace the following:

        * NAMESPACE is the name of your Service Directory namespace.
        * LOCATION is the [region](https://docs.cloud.google.com/build/docs/locations) where you create connections and link repositories.
        * PROJECT_ID_CONTAINING_SERVICE_DIRECTORY is the ID of your Google Cloud project that contain your Service Directory. 
**Note:** The region you specify in your namespace **must** match the region you specify in your Cloud Build host connection.
     2. Configure a [service](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configure_a_service) for your namespace:
            
            gcloud service-directory services create SERVICE --namespace=NAMESPACE --location=LOCATION
            

Replace the following:

        * SERVICE is the name of your Service Directory resource.
        * NAMESPACE is the name of your Service Directory namespace.
        * LOCATION is the [region](https://docs.cloud.google.com/build/docs/locations) where you create connections and link repositories.
     3. Configure an [endpoint](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configure_an_endpoint) for your service:
            
            gcloud service-directory endpoints create ENDPOINT_NAME \
               --namespace=NAMESPACE \
               --service=SERVICE \
               --location=LOCATION \
               --address=INSTANCE_IP_ADDRESS \
               --port=PORT \
               --network=projects/PROJECT_ID_CONTAINING_NETWORK/locations/global/networks/NETWORK
            

Replace the following:

        * ENDPOINT_NAME is the name of your endpoint.
        * NAMESPACE is the name of your Service Directory namespace.
        * SERVICE is the name of your Service Directory resource.
        * LOCATION is the [region](https://docs.cloud.google.com/build/docs/locations) where you create connections and link repositories.
        * INSTANCE_IP_ADDRESS is the IP address of your GitHub Enterprise instance in your network. For example, `123.45.67.89`. To learn more, see [Use Service Directory to reach hosts outside Google Cloud](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network?generation=2nd-gen#service_dir_gc).
        * PORT is the name of your port for HTTPS.
        * PROJECT_ID_CONTAINING_NETWORK is your Google Cloud project ID that contains your VPC network.
        * NETWORK is the name of your VPC network.

You can now use the service resource (`projects/{PROJECT_ID}/locations/{LOCATION}/namespaces/{NAMESPACE}/services/{SERVICE}`) to create your connection in the following steps.

  4. [Connect a GitHub Enterprise host](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise).

  5. [Connect a GitHub Enterprise repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise).

  6. [Create a GitHub Enterprise trigger](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise) to build repositories hosted on your GitHub Enterprise instance.




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

## Next steps

  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
