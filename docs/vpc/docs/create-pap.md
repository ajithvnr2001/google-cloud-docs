---
url: https://docs.cloud.google.com/vpc/docs/create-pap/
title: Create a public advertised prefix \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:53.095435+00:00
---

# Create a public advertised prefix  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-pap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a public advertised prefix

You can bring your own IP addresses (BYOIP) to Google Cloud. After we validate that you own the IP range, and the IP addresses are imported to Google Cloud, you can assign them to [supported resources](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#support).

The first step in using bring your own IP is to create a public advertised prefix. The following options are available:

**Note:** Public advertised prefixes created before July 2023 can contain both regional _and_ global public delegated prefixes. Any public advertised prefixes created after this date can be used to create either global _or_ regional public delegated prefixes. 

Configuration | Regional (v2) | Regional internal (v2) | Regional (v1) | Global (v1)  
---|---|---|---|---  
Availability | Recommended regional configuration | Used for internal IPv6 addresses | Not recommended for new regional configurations | Must [request adding your project to an allowlist](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#global-pdp)  
Public advertised prefix provisioning time | Approximately 2 weeks | Immediate | Approximately 4 weeks | Approximately 4 weeks  
Public delegated prefix provisioning time | A few minutes | Immediate | 4 weeks  Can overlap with public advertised prefix provisioning time  | 4 weeks  Can overlap with public advertised prefix provisioning time   
Sub-prefix provisioning time | A few minutes | Immediate | A few minutes | A few minutes  
BGP announcement | The public advertised prefix is not automatically announced when it is provisioned. You decide when to [announce or withdraw](https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement) advertisement. | Not announced | The public advertised prefix is automatically announced after provisioning completes. | The public advertised prefix is automatically announced after provisioning completes.  
Access type | External | Internal | External | External  
[Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview) | 

  * Premium Tier
  * Standard Tier ([Preview](https://cloud.google.com/products#product-launch-stages))

| Premium Tier | Premium Tier | Premium Tier  
IP stack | 

  * Premium Tier: IPv4, IPv6 (only for external passthrough Network Load Balancers and subnets that exclusively host VMs)
  * Standard Tier: IPv4

| IPv6 | IPv4 | IPv4  
  
## Before you begin

  * Bringing your own IP addresses to Google Cloud requires careful planning. For more information, see [Planning for bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/byoip-planning#planning).
  * Consider using an organization, and creating a dedicated project for managing BYOIP addresses. For more information, see [Project architecture](https://docs.cloud.google.com/vpc/docs/byoip-planning#architecture).
  * If you are creating an external access public advertised prefix, check if any part of the prefix that you want to import is already publicly advertised. If it is, you must make sure that Google Cloud does not advertise it while it is being advertised from another source: 
    * If you are creating a v2 public advertised prefix for regional addresses, you have [control over the announcement of the prefix](https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement). You can create the public advertised prefix and public delegated prefixes, but you must ensure the prefix is not advertised anywhere else before you announce it from Google Cloud.
    * If you are creating a v1 public advertised prefix for global addresses, the prefix is automatically announced as soon as public delegated prefix provisioning is complete. Don't create public delegated prefixes until the prefix is no longer being announced from another source.



### Roles

To get the permissions that you need to complete the tasks in this guide, ask your administrator to grant you the [Compute Public IP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) (`roles/compute.publicIpAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create and validate a public advertised prefix

When you create a public advertised prefix, you must validate ownership of the prefix. The details of these validation tasks are outlined in the following sections. The validation process depends on the [access type](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#access-type) of the prefix:

  * For _external access_ prefixes, you complete two tasks which together let Google Cloud validate that you own this prefix:

    * Creating a Route Origin Authorization (ROA) for your prefix.
    * Creating a PTR record for an IP address in your prefix.

After validation is complete, it takes approximately two weeks to complete configuration for v2 prefixes or four weeks for v1 prefixes.

  * For _internal access_ prefixes, you only need to create a ROA for your prefix. The configuration is complete immediately, and the prefix is ready to use.




### Create a ROA request

To prove that you have ownership of a prefix, create a Route Origin Authorization (ROA) request.

Submit the ROA request with your regional registry for the prefix that you want Google Cloud to advertise. When you create a public advertised prefix, the ROA for that prefix must exist and point to the ASN for Google Cloud, remaining in effect for some time after you delete the public advertised prefix. For more information, see [Remove a ROA](https://docs.cloud.google.com/vpc/docs/deprovision-byoip#remove-roa).

The values that you include in the ROA request depend on the network tier of the prefix.

#### Premium Tier ROA requirements

For Premium Tier, create a ROA request that includes the public advertised prefix, its prefix length, and the Premium Tier ASN for Google Cloud: `396982`.

#### Standard Tier ROA requirements

For Standard Tier ([Preview](https://cloud.google.com/products#product-launch-stages)), do one of the following:

  * Create separate ROA requests for the public advertised prefix and each top-level public delegated prefix that you plan to provision. For each request, include the prefix, its prefix length, and the Standard Tier ASN for Google Cloud: `19527`. Google recommends this approach.

  * Create a single ROA request that includes the public advertised prefix, its prefix length, a [maximum prefix length (`maxLength`)](https://datatracker.ietf.org/doc/html/rfc9582#section-4.3.2.2) of `/24`, and the Standard Tier ASN for Google Cloud: `19527`.




#### Create a ROA for your own ASN

We recommend that you submit another ROA request for your public advertised prefix. Use the same details as the ROA you submitted with Google's ASN, but substitute your own ASN as the origin. If you ever need to advertise the prefix, the ROA with your ASN prevents networks that use Resource Public Key Infrastructure (RPKI) from considering the prefix to be invalid because it is also advertised with the origin ASN for Google Cloud.

#### Regional internet registries

Your local regional internet registry processes ROA requests. For more information, see the link for your location:

  * [AFRINIC](https://www.afrinic.net/resource-certification?highlight=WyJycGtpIl0=) (Africa)
  * [APNIC](https://www.apnic.net/get-ip/faqs/rpki/) (Portions of Asia and Oceania)
  * [ARIN](https://www.arin.net/resources/rpki/index.html) (North America and some Caribbean Islands)
  * [LACNIC](https://www.lacnic.net/1018/2/lacnic/resource-certification-system-rpki) (Latin America)
  * [RIPE NCC](https://www.ripe.net/manage-ips-and-asns/resource-management/certification) (Europe, Central Asia, Middle East)



### Renew a ROA

To let Google Cloud advertise your public advertised prefixes, you must actively maintain a valid ROA with your regional internet registry. ROAs expire periodically and must be renewed before expiration.

If your ROA expires and you fail to renew it within four weeks of receiving a renewal notification, Google Cloud stops advertising the public advertised prefix to the internet, which might result in connectivity disruptions for resources that use IP addresses from the prefix.

To renew your ROA, consult your local regional internet registry for specific instructions. For more information, see Create a ROA request.

### Create a public advertised prefix

**Warning:** Google Cloud does not support overlapping BYOIP route announcements. For example, importing `203.0.112.0/23` is not supported if `203.0.112.0/23` or a subset of this prefix, such as `203.0.112.0/24`, is advertised outside Google Cloud. If Google Cloud and another network advertise the same route with matching or mismatched prefix lengths, you might experience unexpected routing and packet loss.

You can create a [public advertised prefix](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#pap) for the prefix that you want to bring to Google Cloud.

A public advertised prefix name can't be changed without deleting and recreating the resource. For this reason, we recommend that you create generic names that won't need to change—for example, `pap-203-0-113-0-24`, where `pap` denotes the resource type and `203-0-113-0-24` denotes the specific prefix and prefix length.

If you want to use the public advertised prefix to create global public delegated prefixes, your project must be added to an allowlist. For more information, see [Global public delegated prefixes](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#global-pdp).

For external access prefixes, choose an unused IP address for DNS validation. Verification requires that you configure a new PTR record for this IP address, and you don't know the hostname until after you create the public advertised prefix.

To create a Standard Tier public advertised prefix ([Preview](https://cloud.google.com/products#product-launch-stages)), use the Google Cloud CLI. 

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Click **Add PAP**.

  3. For **Name** , enter a name for the public advertised prefix.

  4. For **Description** , enter an optional description for the public advertised prefix.

  5. For **IP version** , select **IPv4** or **IPv6**.

  6. Enter the prefix that you want to import.

  7. If you're importing an **IPv4** prefix, select a **Scope** for the public advertised prefix: **Regional** or **Global**.

**Note:** if the **Global** option is not available, you are not part of the allowlist for [global public advertised prefixes](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#global-pap).
  8. If you're importing an **IPv6** prefix, select an access type.

  9. Click **Next**.

  10. Review the information that you entered. To confirm that you own this prefix, click **Confirm**.

  11. If you're adding a PAP with external access, for **IP address** , enter an unused IP address from the prefix that you are adding. This address is used for DNS validation, and in a later step, you must create a PTR record for it that uses a hostname provided by Google Cloud.

  12. Click **Create**. The **Validation** screen shows you the validation status of this request.




###  gcloud 

Use the [`public-advertised-prefixes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create).

Except where noted, the commands in this section create Premium Tier prefixes.

  * To create a public advertised prefix (v1) for global addresses, run the following command:
        
        gcloud compute public-advertised-prefixes create PAP_NAME \
            --range=PAP_IP_RANGE \
            --dns-verification-ip=VERIFICATION_IP_ADDRESS
        

**Important:** You must [request that your project be added to an allowlist](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#global-pdp) before you can create global [public delegated prefixes](https://docs.cloud.google.com/vpc/docs/create-pdp) from this public advertised prefix.
  * To create a public advertised prefix (v2) for regional addresses, run the following command:
        
        gcloud compute public-advertised-prefixes create PAP_NAME \
            --range=PAP_IP_RANGE \
            --pdp-scope=REGIONAL \
            --dns-verification-ip=VERIFICATION_IP_ADDRESS
        

  * To create a Standard Tier public advertised prefix (v2) for regional IPv4 addresses ([Preview](https://cloud.google.com/products#product-launch-stages)), run the following command:
        
        gcloud beta compute public-advertised-prefixes create PAP_NAME \
            --range=PAP_IP_RANGE \
            --pdp-scope=REGIONAL \
            --dns-verification-ip=VERIFICATION_IP_ADDRESS \
            --network-tier=STANDARD
        

  * To create an internal access public advertised prefix for regional IPv6 addresses, run the following command:
        
        gcloud compute public-advertised-prefixes create PAP_NAME \
            --range=PAP_IP_RANGE \
            --pdp-scope=REGIONAL \
            --ipv6-access-type=INTERNAL
        

If you're creating an internal access public advertised prefix, your prefix is ready to use after this step. You don't need to complete the remaining steps on this page.

  * Creating a public advertised prefix (v1) for regional addresses is not recommended. Create a v2 public advertised prefix instead. If you must create a v1 public advertised prefix for regional addresses, run the following command:
        
        gcloud compute public-advertised-prefixes create PAP_NAME \
            --range=PAP_IP_RANGE \
            --dns-verification-ip=VERIFICATION_IP_ADDRESS
        




Replace the following:

  * `PAP_NAME`: a name for the public advertised prefix that you're creating.

  * `PAP_IP_RANGE`: the IP address range for the public advertised prefix. The range can be an IPv4 or IPv6 address range.

  * `VERIFICATION_IP_ADDRESS`: an unused IP address chosen from the PAP_IP_RANGE. This address is used for DNS validation, and in a later step, you must create a PTR record for it that uses a hostname provided by Google Cloud.




### Validate ownership with DNS

If you created an external access public advertised prefix, complete the steps in the following sections to verify that you own the prefix. If you created an internal access public advertised prefix, you don't need to validate ownership with DNS.

#### Find the name to use for the PTR record

When you create an external access public advertised prefix, Google Cloud generates a name for you to use as a hostname for the PTR validation step.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Click **Check status** for the prefix that you want to check.

  3. The name and IP address to use for PTR validation are displayed in the **DNS validation** section.




###  gcloud 

  1. To get the name from the `sharedSecret` field, use the [`public-advertised-prefixes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/describe).
         
         gcloud compute public-advertised-prefixes describe \
             PAP_NAME --format='value(sharedSecret)'
         

  2. If needed, you can retrieve the IP address you provided for DNS validation.
         
         gcloud compute public-advertised-prefixes describe \
             PAP_NAME --format='value(dnsVerificationIp)'
         




In both commands, replace `PAP_NAME` with the name of the public advertised prefix.

#### Create the PTR record

To verify that you own the IP address range that you are importing to Google Cloud, you must create a public PTR record in the DNS zone that is used for the IP address range that you are importing.

Use the following values in the PTR record:

  * IP address: the verification IP address that you used when you created the public advertised prefix.
  * Hostname: the name (`sharedSecret`) that Google Cloud provided.
  * Domain name: the domain name associated with the DNS zone that is used for the IP address range that you are importing.



Examples:

  * **IPv4** : If your verification IP address is `203.0.113.144`, and the DNS domain for `203.0.113.0/24` is `example.net`, and the name provided by Google Cloud is `55kk88tt00`, the required PTR record would look like this:
        
        $ dig +noall +answer -x 203.0.113.144
        
        144.113.0.203.in-addr.arpa. 21599 IN PTR 55kk88tt00.example.net
        

  * **IPv6** : If your verification IP address is `2001:db8::10`, and the DNS domain for `2001:db8::/32` is `example.net`, and the name provided by Google Cloud is `55kk88tt00`, the required PTR record would look like this:
        
        $ dig +noall +answer -x 2001:db8::10
        
        0.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa
        21599 IN PTR 55kk88tt00.example.net.
        




#### Validate the PTR record

After you have created the PTR record, update the public advertised prefix to trigger validation of the PTR record.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Click **Check status** for the prefix that you want to update.

  3. In the **DNS validation** section, select the **I have created this PTR record** checkbox and click **Validate**.




###  gcloud 

To change the status of the public advertised prefix to `PTR-CONFIGURED`, use the [`public-advertised-prefixes update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update).

The status change triggers validation of the PTR record. If it is successful, the status changes to `VALIDATED`. If it fails, the status changes to `REVERSE_DNS_LOOKUP_FAILED`.
    
    
    gcloud compute public-advertised-prefixes update PAP_NAME --status=PTR-CONFIGURED
    

Replace `PAP_NAME` with the public advertised prefix that you have created a PTR record for.

## Check the status of a public advertised prefix

It takes approximately four weeks for Google Cloud to provision the public advertised prefix. You can check the status to see if provisioning is complete.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Click **Check status** for the prefix that you want to check.

  3. View the **Validation** section.




###  gcloud 

To describe the public advertised prefix and get its status, use the [`public-advertised-prefixes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/describe).
    
    
    gcloud compute public-advertised-prefixes describe PAP_NAME --format='value(status)'
    

Replace `PAP_NAME` with the public advertised prefix that you want to get status information for.

After the prefix is validated, the status field changes from `VALIDATED` to `PREFIX_CONFIGURATION_COMPLETE`.

## What's next

  * [Create public delegated prefixes](https://docs.cloud.google.com/vpc/docs/create-pdp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
