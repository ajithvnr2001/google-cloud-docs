---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-legacy-conditional-dns-forwarding/
title: (Legacy networks) Create DNS forwarding rules \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:11.469647+00:00
---

# (Legacy networks) Create DNS forwarding rules  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-legacy-conditional-dns-forwarding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# (Legacy networks) Create DNS forwarding rules

**Caution:** You can only use conditional DNS forwarding rules for private clouds attached to Legacy VMware Engine networks. To configure DNS resolution for management appliances in private clouds attached to Standard VMware Engine networks, see [Configure DNS Bindings](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings).

Your private cloud's DNS forwarding rules determines how Google Cloud VMware Engine forwards DNS requests from management appliances to the DNS servers of your on-premises services.

You can configure multiple conditional DNS forwarding rules each with one or more DNS servers associated with the domains.

Here are some example processes that require conditional DNS forwarding rules:

  * Forwarding syslog messages from your private cloud vCenter to your syslog collection server by server name.
  * Using an [on-premises Active Directory deployment as an identity source](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-identity-sources) for your private cloud.
  * Using [VMware Site Recovery Manager (SRM) for disaster recovery](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-srm).
  * Using [Zerto Virtual Replication for disaster recovery](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-zerto).



## Before you begin

The steps in this document assume that you have done the following:

  * [Establish a connection between your private cloud and on-premises networks](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises)
  * [Make your on-premises DNS server accessible to your private cloud network](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises)



## Create DNS forwarding rules

To create DNS forwarding rules in your project, use one of the following methods.

###  Console 

To create a DNS forwarding rule for a private cloud by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the DNS forwarding rule.

  3. Select the private cloud to create a rule for.

  4. On the private clouds summary page, click **DNS**.

  5. Click **Add rule**.

  6. Specify the domain you want to forward for and specify one or more IPv4 addresses that can resolve the domain, provided as a comma-separated list.




###  gcloud 

To create a DNS forwarding rule for a private cloud, use the [`gcloud vmware private-clouds dns-forwarding update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/update). You can specify multiple rules by using multiple `--rule` flags for each request.
    
    
    gcloud vmware private-clouds dns-forwarding update \
        --project=PROJECT_ID \
        --location=ZONE \
        --private-cloud=PRIVATE_CLOUD_NAME \
        --rule=domain=DOMAIN,name-servers=DNS_SERVER_IP1,DNS_SERVER_IP2,.... \
        --rule=domain=DOMAIN,name-servers=DNS_SERVER_IP1,DNS_SERVER_IP2,....
    

Replace the following:

  * `PROJECT_ID`: the ID for your project where the private cloud is located
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_NAME`: the name of the private cloud
  * `DOMAIN`: the domain to be forwarded
  * `DNS_SERVER_IP1,DNS_SERVER_IP2,....`: a comma-separated list of IPv4 addresses for the authoritative DNS server



###  API 

Create a `POST` request. You can add one or more rules to each request.
    
    
    curl -X POST -H "Authorization: Bearer
    TOKEN
    "  -H "Content-Type: application/json; charset=utf-8"
    https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_NAME/dnsForwarding -d '{"forwardingRules": [
        {
          "domain": "DOMAIN",
          "nameServers": [
            "DNS_SERVER_IP1",
            "DNS_SERVER_IP2"
          ]
        },
        {
          "domain": "DOMAIN",
          "nameServers": [
            "DNS_SERVER_IP1",
            "DNS_SERVER_IP2"
          ]
        }
      ]}
    

Replace the following:

  * `PROJECT_ID`: the ID for your project where the private cloud is located
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_NAME`: the name of the private cloud
  * `DOMAIN`: the domain to be forwarded
  * `DNS_SERVER_IP1,DNS_SERVER_IP2,....`: a comma-separated list of IPv4 addresses for the authoritative DNS server



## Describe DNS forwarding rules

To describe DNS forwarding rules in your project, use one of the following methods.

###  Console 

To describe a DNS forwarding rule for a private cloud by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud you want to DNS forwarding rules for.

  3. Select the private cloud to create a rule for.

  4. On the private clouds summary page, click **DNS**.




###  gcloud 

To create a DNS forwarding rule for a private cloud, use the [`gcloud vmware private-clouds dns-forwarding describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/dns-forwarding/describe):
    
    
    gcloud vmware private-clouds dns-forwarding describe \
        --project=PROJECT_ID \
        --location=ZONE \
        --private-cloud=PRIVATE_CLOUD_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID for your project where the private cloud is located
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_NAME`: the name of the private cloud



###  API 

Create a `POST` request.
    
    
    POST https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/dnsForwarding

Replace the following:

  * `PROJECT_ID`: the ID for your project where the private cloud is located
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_NAME`: the name of the private cloud



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
