---
url: https://docs.cloud.google.com/iap/docs/securing-tcp-with-vpc-sc/
title: Securing IAP for TCP forwarding with VPC Service Controls \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:19.384121+00:00
---

# Securing IAP for TCP forwarding with VPC Service Controls  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/securing-tcp-with-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Securing IAP for TCP forwarding with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use VPC Service Controls to protect IAP for TCP forwarding, and how to use IAP for TCP forwarding within a VPC Service Controls perimeter.

## Before you begin

  1. Read the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

  2. [Set up](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) usage of IAP TCP forwarding without a service perimeter.

  3. [Create a service perimeter using VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters). This service perimeter protects the Google-managed resources of services that you specify. When you create your service perimeter, do the following:

     1. Add the project that contains the Compute Engine instance you want to connect to with IAP to the projects within your service perimeter. If you are running an IAP for TCP client on a Compute Engine instance, also put the project containing this instance into the perimeter.

     2. Add **Identity-Aware Proxy TCP API** to the list of services protected by your service perimeter.

If you created your service perimeter without adding the projects and services you need, see [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters) to learn how to update your service perimeter.




## Configure your DNS records using Cloud DNS

If your IAP for TCP client, which is likely the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), is not running inside any perimeter, then you can skip this step. On the other hand, if you run the client inside a perimeter, you must configure DNS records for IAP for TCP.

IAP for TCP uses domains that are not subdomains of `googleapis.com`. Using Cloud DNS, add DNS records to ensure that your VPC network correctly handles requests sent to those domains. To learn more about VPC routes, read the [Routes overview](https://docs.cloud.google.com/vpc/docs/routes).

Use the following steps to create a [managed zone](https://docs.cloud.google.com/dns/docs/zones) for a domain, add DNS records to route requests, and execute the transaction. You can use the gcloud CLI with your preferred terminal or use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell), which has the gcloud CLI preinstalled.

  1. [Configure](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring-dns-with) the `*.googleapis.com` DNS as is typical for VPC Service Controls integrations.

  2. Collect this information to use when configuring your DNS records:

     * PROJECT_ID is the ID of the project that hosts your VPC network.

     * NETWORK_NAME is the name of the VPC network in which you are running your IAP for TCP client.

     * ZONE_NAME is a name for the zone that you are creating. For example, `iap-tcp-zone`.

  3. Create a private managed zone for the domain `tunnel.cloudproxy.app` so the VPC network can handle it.
         
         gcloud dns managed-zones create ZONE_NAME \
          --visibility=private \
          --networks=https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME \
          --dns-name=tunnel.cloudproxy.app \
          --description="Description of your managed zone"

  4. Start a transaction.
         
         gcloud dns record-sets transaction start --zone=ZONE_NAME

  5. Add the following DNS A record. This reroutes traffic to Google's [restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity) (virtual IP address).
         
         gcloud dns record-sets transaction add \
          --name=tunnel.cloudproxy.app. \
          --type=A 199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7 \
          --zone=ZONE_NAME \
          --ttl=300

  6. Add the following DNS CNAME record to point to the A record that you just added. This redirects all traffic matching the domain to the IP addresses listed in the previous step.
         
         gcloud dns record-sets transaction add \
          --name="*.tunnel.cloudproxy.app." \
          --type=CNAME tunnel.cloudproxy.app. \
          --zone=ZONE_NAME \
          --ttl=300

  7. Execute the transaction.
         
         gcloud dns record-sets transaction execute --zone=ZONE_NAME




### Configuring DNS with BIND

Instead of using Cloud DNS, you can use [BIND](https://www.wikipedia.org/wiki/BIND). In that case, follow the directions for [configuring DNS with BIND](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring_dns_with_bind), but use the IAP for TCP domains instead of the general `googleapis.com` domains.

### Using the private VIP

Instead of using the restricted VIP, it might be possible to use the [private VIP](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid#config-choose-domain), depending on how you've configured your perimeter and network. If you prefer to do that, then use

`199.36.153.8 199.36.153.9 199.36.153.10 199.36.153.11`

in place of

`199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7`

in the instructions for configuring your DNS records.

## Using a shared VPC

If you're using a [shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you must add the host and the service projects to the service perimeter. See [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).

## What's next

  * See [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters) to add more resources to your service perimeter.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
