---
url: https://docs.cloud.google.com/looker/docs/looker-core-psc-access-public/
title: Public inbound access to a Looker (Google Cloud core) instance using Private Service Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:52.781134+00:00
---

# Public inbound access to a Looker (Google Cloud core) instance using Private Service Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-psc-access-public/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Public inbound access to a Looker (Google Cloud core) instance using Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

To provide public inbound access to your Looker (Google Cloud core) instance, you can configure Private Service Connect with custom domain authentication. Private Service Connect provides two ways for clients to connect: privately from your VPC network, or publicly through an external load balancer.

A common deployment for Looker (Google Cloud core) uses a custom domain and a Private Service Connect backend with an application load balancer. This configuration uses custom domain certificate authentication, which helps add a layer of security and control for user access. You must [enable Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-create-psc) for your Looker (Google Cloud core) instance during its creation to use this functionality.

When you use Private Service Connect to access Looker (Google Cloud core), you are the service consumer, and Looker (Google Cloud core) is the service producer. Inbound access to Looker (Google Cloud core) requires that the consumer VPC be added as an [allowed VPC](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#update_allowed_vpcs) for the Looker (Google Cloud core) Private Service Connect instance.

## Create a custom domain

The first step after the Looker (Google Cloud core) instance is created is to set up a custom domain and update the OAuth credentials for the instance. The next sections walk you through the process.

When you create a custom domain for private connections (Private Service Connect) instances, the custom domain must meet the following requirements:

  * The custom domain must consist of at least three parts, including at least one subdomain. For example, `subdomain.domain.com`.
  * The custom domain must not contain any of the following: 
    * looker.com
    * google.com
    * googleapis.com
    * gcr.io
    * pkg.dev



## Set up a custom domain

After your Looker (Google Cloud core) instance has been created, you can set up a custom domain.

### Before you begin

**Note:** Custom domains cannot be created using a looker.com domain.

Before you can customize the domain of your Looker (Google Cloud core) instance, identify where your domain's DNS records are stored, so that you can update them.

#### Required roles

To get the permissions that you need to create a custom domain for a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project the instance resides in. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create a custom domain

**Note:** You cannot modify a custom domain once it is created. If you want to make changes to the custom domain, you must delete the existing custom domain and create a new one.

In the Google Cloud console, follow these steps to customize the domain of your Looker (Google Cloud core) instance:

  1. On the **Instances** page, click the name of the instance for which you would like to set up a custom domain.
  2. Click the **Custom domain** tab.
  3. Click **Add a custom domain**.

![](https://docs.cloud.google.com/static/looker/docs/images/core-custom-domain-1-120125.png)

This opens the **Add a new custom domain** panel.

  4. Using only letters, numbers, and dashes, enter the hostname of up to 64 characters for the web domain that you would like to use — for example: `looker.examplepetstore.com`.

![](https://docs.cloud.google.com/static/looker/docs/images/core-custom-domain-2.png)

**Tip:** When entering the hostname, don't include `https://` or `http://`. Once the custom domain is created, Looker (Google Cloud core) automatically adds `https://` to the beginning of the hostname.
  5. Click the **Continue** button.

  6. The **Update your DNS records** section opens. The ingress public IP is listed in the **Data** field.

  7. Click **DONE** on the **Add a new custom domain** panel to return to the **CUSTOM DOMAIN** tab.




Updating the custom domain takes 10 to 15 minutes to complete.

**Note:** For instances that use only private networking, the status on the **CUSTOM DOMAIN** tab may remain **Unverified** because Google cannot verify private DNS records or reach internal IP addresses for your instance. Even if the status is **Unverified** , you can still use the custom domain.

Once your custom domain is set up, it is displayed in the **Domain** column on the **CUSTOM DOMAIN** tab of the Looker (Google Cloud core) [instance details page](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-settings) in the Google Cloud console.

After your custom domain has been created, you can [view information](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-settings) about it, or [delete](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-delete) it.

### Update the OAuth credentials

**Note:** You can use any OAuth client to create authorization credentials for your Looker (Google Cloud core) instance. As an example, these steps walk you through updating the credentials by using the Google Cloud console. If you are using a different client, adjust the steps accordingly.

  1. Access your OAuth client by navigating in the Google Cloud console to **APIs & Services > Credentials** and selecting the OAuth client ID for the OAuth client that is used by your Looker (Google Cloud core) instance.
  2. Click the **Add URI** button to update the **Authorized JavaScript origins** field in your OAuth client to include the same DNS name that your organization will use to access Looker (Google Cloud core). For example, if your custom domain is `looker.examplepetstore.com`, you enter `looker.examplepetstore.com` as the URI.

![](https://docs.cloud.google.com/static/looker/docs/images/core-custom-domain-ajso.png)

  3. [Update or add](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client) the custom domain to the list of **Authorized redirect URIs** for the [OAuth credentials that you used](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth) when you created the Looker (Google Cloud core) instance. Add `/oauth2callback` to the end of the URI. For example, if your custom domain is `looker.examplepetstore.com`, you enter `looker.examplepetstore.com/oauth2callback`.

![](https://docs.cloud.google.com/static/looker/docs/images/core-custom-domain-aruris.png)




## Public access to Looker (Google Cloud core)

After you have set up the custom domain, the next step is to create a self-signed certificate or Google-managed certificate with DNS authorization. Once your certificate is created, you can deploy an external regional application load balancer with a [Private Service Connect backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) as the backend service. Once the load balancer is deployed, you can update your public DNS with the customer domain and load balancer IP address as the A record.

### Required roles

**Role** | **Description**  
---|---  
[Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) `(roles/compute.networkAdmin)` | Grants full control over the VPC network that initiates a connection to a Looker (Google Cloud core) instance, including creating and managing an HTTPS target proxy.  
[Compute Load Balancer Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) `(roles/compute.loadBalancerAdmin)` | Create Private Service Connect backends.  
[Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) `(roles/looker.admin)` | Grants full control over Looker (Google Cloud core) resources, including creating an instance that is enabled for Private Service Connect and creating a custom domain.  
[DNS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) `(roles/dns.admin)` (optional) | Grants full control over Cloud DNS resources, including DNS zones and records.  
[Certificate Manager Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.owner) `(roles/certificatemanager.owner)` (optional) | Required to create and manage Certificate Manager resources.  
  
### Network setup

The following network components are required:

  * [Proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)
  * [Regional external application load balancer](https://docs.cloud.google.com/load-balancing/docs/https)
  * [SSL certificate resource](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)



Looker (Google Cloud core) deployed with Private Service Connect supports Private Service Connect network endpoint groups (NEGs), called _backends_ , that are integrated with Google Cloud load balancers. See the [Looker PSC Northbound Regional External L7 ALB](https://codelabs.developers.google.com/looker-psc-ext-northbound-l7) codelab for instructions on how to publicly access a Looker (Google Cloud core) instance that is enabled for Private Service Connect by using a backend.

An example of a Private Service Connect backend network setup for public access is displayed in the following diagram:

![The network architecture for accessing a Looker \(Google Cloud core\) instance from on-premises using a backend.](https://docs.cloud.google.com/static/looker/docs/images/psc-backend-setup-public.png)

As shown in the diagram, public clients access Looker (Google Cloud core) by performing a DNS lookup by specifying the Looker (Google Cloud core) customer domain that returns the external regional application load balancer's IP address as the A record. Once traffic is received by the load balancer, the backend service (which consists of the Private Service Connect backend) connects to a service attachment in a Google-managed producer VPC hosting Looker (Google Cloud core). Make sure that the consumer VPC network is [allowed ingress](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#update_allowed_vpcs) to your Looker (Google Cloud core) instance.

## Troubleshooting

When configuring inbound access to a Looker (Google Cloud core) instance by using a Private Service Connect backend, you might encounter issues where the instance fails to provision successfully or the load balancer cannot reach the backend service.

If your load balancer logs display `failed_to_pick_backend` and `no healthy upstream` (HTTP 503) errors, and the network endpoint group (NEG) remains stuck in a `pending` status, mandatory networking configuration steps for the consumer project are missing. Specifically, the consumer project isn't authorized to connect to the Looker (Google Cloud core) producer service, or a Network Attachment resource was not created in the consumer VPC.

To resolve these issues, ensure that you complete the following mandatory networking configuration steps:

  1. **VPC allowlisting** : Add the consumer network to the list of allowed VPCs for inbound connections in the [Looker (Google Cloud core) settings](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#configure-inbound). Adding this network authorizes the consumer VPC to establish a connection to the Looker (Google Cloud core) producer service.
  2. **Network attachment configuration** : Create a [network attachment resource](https://docs.cloud.google.com/vpc/docs/about-network-attachments) in the consumer VPC and associate it with the Looker (Google Cloud core) instance.



## What's next

  * [Connect Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects)
  * [Prepare a Looker (Google Cloud core) instance for users](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
