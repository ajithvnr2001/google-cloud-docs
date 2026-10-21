---
url: https://docs.cloud.google.com/dns/docs/update-name-servers/
title: Update your domain's name servers \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:58.371825+00:00
---

# Update your domain's name servers  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/update-name-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Update your domain's name servers Stay organized with collections  Save and categorize content based on your preferences. 

After you [create a managed zone](https://docs.cloud.google.com/dns/docs/zones#create_managed_zones), you must change the name servers that are associated with your domain registration to point to the Cloud DNS name servers. The process differs by domain registrar provider. Consult the documentation for your provider to determine how to make the name server change.

If you don't already have a domain name, you can use Cloud Domains to register a domain. If you already have a domain registered by using Cloud Domains, see [Configure DNS for the domain](https://docs.cloud.google.com/domains/docs/buy-register-domain#configure-dns) in the [Cloud Domains documentation](https://docs.cloud.google.com/domains/docs).

**Note:** Instructions to update your domain's name servers differ based on your registrar.

## Look up your Cloud DNS name servers

For Cloud DNS to work, you must determine the name servers that have been associated with your managed zone and verify that they match the name servers for your domain. Different managed zones have different name servers.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/)

  2. Under **Zone name** , select the name of your managed zone.

  3. On the **Zone details** page, click **Registrar setup** at the top right of the page.




###  gcloud 

To return the list of name servers that are configured to serve DNS queries for your zone, run the [`dns managed-zones describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe) command:
    
    
    gcloud dns managed-zones describe ZONE_NAME
    

Replace `ZONE_NAME` with the name of the managed zone for which you want to return a list of name servers.

## Find the IP addresses of your name servers

The IP addresses of your Cloud DNS name servers change, and may be different for users in different geographic locations.

To find the IP addresses for the name servers in the `a` name server shard, run the following command:
    
    
      dig ns-cloud-a1.googledomains.com +short
      dig ns-cloud-a2.googledomains.com +short
      dig ns-cloud-a3.googledomains.com +short
      dig ns-cloud-a4.googledomains.com +short
    

For private zones, you can't query name servers on the public internet. Therefore, it's not necessary to find their IP addresses.

To find all the IP address ranges used by Google Cloud, see [Where can I find Compute Engine IP ranges?](https://docs.cloud.google.com/compute/docs/faq#find_ip_range)

## Change your domain registrar's name servers for your domain

Now that you have the list of Cloud DNS name servers hosting your managed zone, use your domain registrar to update the name servers for your domain. Your domain registrar might be Cloud Domains or a third-party registrar.

**Note:** Instructions to update your domain's name servers differ based on your registrar.

Typically, you must provide at least two Cloud DNS name servers to the domain registrar. To benefit from Cloud DNS's high availability, you must use all the name servers.

After changing your domain registrar's name servers, it can take a while for resolver traffic to be directed to your new Cloud DNS name servers. Resolvers could continue to use your old name servers until the TTL on the old NS records expire.

## Verify your name servers

Verify that the name servers for the domain match the name servers listed in the Cloud DNS zone.

To look up name servers that are in use, run the `dig` command:
    
    
    dig -t NS myzone.example.com.
    

**Note:** If you're using Microsoft Windows and `dig` is not installed on your system, you can [run a `dig -t NS` query](https://toolbox.googleapps.com/apps/dig/#NS/) from the web interface.

## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
