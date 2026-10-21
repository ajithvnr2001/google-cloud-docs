---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/dns-quickstart/
title: DNS setup quickstart \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:55:26.724506+00:00
---

# DNS setup quickstart  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/dns-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  DNS setup quickstart Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/dns-quickstart.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/dns-quickstart.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/dns-quickstart.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/dns-quickstart.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/dns-quickstart.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/dns-quickstart.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/dns-quickstart.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/dns-quickstart.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/dns-quickstart.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/dns-quickstart.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/dns-quickstart.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/dns-quickstart.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/dns-quickstart.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/dns-quickstart.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/dns-quickstart.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/dns-quickstart.html)



This topic offers an example showing how to use [Google Cloud DNS](https://cloud.google.com/dns) to configure a DNS zone with a record set that points to your Apigee hybrid ingress IP address. 

**Note:** If you already have your own domain and DNS zone to use, you do not need to do these steps. You can simply configure your own zone with a new record set pointing to your ingress load balancer.

##  Create a managed zone and record set 

This section explains how to create a DNS zone and record set in Google Cloud DNS. 

  1. Create a managed zone and record set for your domain. This is the address you will use to make API proxy calls to hybrid. 
     1. Create a managed public zone. For instructions, see [ Create a managed public zone](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name#create_a_managed_public_zone).
     2. Create a new record set with the following selections. For instructions, see [Create a new record](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name#create_a_new_record). 
        * **DNS Name** : The name of the endpoint external API calls communicate with, like ` api-services` or `example-endpoint`
        * **Resource Record Type** : **A**
        * **TTL** and **TTL Unit** : Accept defaults
        * **IP Address** : The static IP you created
  2. In the **Zone details** view, copy the DNS name of the **A** record you just created and save it to a **`DOMAIN`** environment variable. Be careful to not include the period at the end. 

![DNS name environment variable highlighted](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.15/images/copy-dns-name.png)
         
         export DOMAIN=dns_name_of_record

##  Add your DNS servers to Cloud DNS 

In this step, you copy the DNS servers from your domain to [Google Cloud DNS](https://cloud.google.com/dns/). Doing so allows Google Cloud to manage the DNS for your Google Cloud Project. 

  3. The **Zone details** view lists four DNS servers as the NS data for your new zone. Copy the DNS record data as shown in the following example: 

![Zone details, DNS servers highlighted](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.15/images/copy-dns-records.png)




##  Configure your domain to use the Google Cloud name servers 

Go to your domain registrar and edit your domain's DNS settings to use the Google Cloud Name servers. 

The following screenshot shows an example of entering the Google Cloud name servers in [Google Domains](https://domains.google.com): 

![Google domain, Use custom name servers highlighted](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.15/images/hybrid-dns-fields.png)

Google Cloud DNS now manages the DNS records for your domain. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
