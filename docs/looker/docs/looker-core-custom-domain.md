---
url: https://docs.cloud.google.com/looker/docs/looker-core-custom-domain/
title: Set up a custom domain for a Looker (Google Cloud core) instance that uses public connections \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:15.467732+00:00
---

# Set up a custom domain for a Looker (Google Cloud core) instance that uses public connections  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-custom-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Set up a custom domain for a Looker (Google Cloud core) instance that uses public connections Stay organized with collections  Save and categorize content based on your preferences. 

You can serve your Looker (Google Cloud core) instance with a custom web domain, such as `yourcompany.com`, rather than the default domain that Looker provides. A custom domain helps to enhance branding and creates a professional, recognizable URL for your users.

You can configure a custom domain for Looker (Google Cloud core) instances that use any networking connectivity option. To set up a custom domain for instances that use [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections) or [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip), follow the process on this page. To set up a custom domain for instances that use private connections, see the custom domain documentation for instances that use [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access) or [private services access](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-private-ip).

Google provides a managed, auto-renewing SSL certificate for instances that use a public network connection.

If your instance uses hybrid connections, be aware that changing to a private connections configuration later invalidates your custom domain, requiring you to recreate it for the new setup.

To implement a custom domain for a public connections or hybrid connections instance, you must perform the following steps:

  1. Set up the custom domain.
  2. Create the DNS A record.
  3. Update the OAuth credentials.



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

  1. On the **Instances** page, click the name of the instance for which you want to set up a custom domain.
  2. Click the **CUSTOM DOMAIN** tab.
  3. Click **ADD A CUSTOM DOMAIN**.

![](https://docs.cloud.google.com/static/looker/docs/images/core-custom-domain-1.png)

This action opens the **Add a new custom domain** panel.

  4. Using only letters, numbers, and dashes, enter the hostname of up to 64 characters for the web domain that you want to use — for example: `looker.examplepetstore.com`.

![](https://docs.cloud.google.com/static/looker/docs/images/core-custom-domain-2.png)

**Tip:** When entering the hostname, don't include `https://` or `http://`. Once the custom domain is created, Looker (Google Cloud core) automatically adds `https://` to the beginning of the hostname.
  5. Click the **Continue** button.

  6. If you haven't [associated manual OAuth credentials](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#edit-oauth-credentials) with your Looker (Google Cloud core) instance (for example, if you have a [public secure connections instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) and didn't [manually add OAuth credentials](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings)), the **OAuth application credentials** section opens. Follow the instructions to complete the following two tasks:

     1. [Generate an OAuth client ID and client secret](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret).
     2. Add the authorized redirect URI in the **Authorized redirect URIs** section of the OAuth client. At this point in the process, enter the **Looker autogenerated URL** that appears on the [**Instances** page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) within the Google Cloud console. You will enter the custom domain when you [update the OAuth credentials](https://docs.cloud.google.com/looker/docs/looker/docs/looker-core-custom-domain#update_the_oauth_credentials).

Enter the credentials in the **OAuth Client ID** and **OAuth Client Secret** fields, and then click the **Continue** button.

  7. If your Looker (Google Cloud core) instance already has [manual OAuth credentials](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#view-oauth-credentials) associated with it (for example, if you have a [hybrid connections instance](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip)), or, if you just added OAuth credentials in the **OAuth application credentials** section of the panel, the **Update your DNS records** section opens. Use the ingress public IP that's listed in the **Data** field when you are creating or updating your A record's IP address.

  8. Click **DONE** on the **Add a new custom domain** panel to return to the **CUSTOM DOMAIN** tab.


**Note:** Updating the custom domain takes 10 to 15 minutes to complete.

Once your custom domain is set up, it is displayed in the **Domain** column on the **CUSTOM DOMAIN** tab of the Looker (Google Cloud core) [instance details page](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-settings) in the Google Cloud console.

After your custom domain has been created, you can [view information](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-settings) about it, or [delete](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-delete) it.

## Access the custom domain

To set up access to a custom domain for a Looker (Google Cloud core) instance that uses public secure connections, create a DNS record and update the OAuth credentials.

### Before you begin

To get the permissions that you need to set up access to a public secure connections custom domain, ask your administrator to grant you the following IAM roles on the project the instance resides in: 

  * [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)
  * [DNS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`)
  * Use Google OAuth: [OAuth Config Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create a DNS record

Wherever your DNS records are stored, create an A record in the DNS zone for your domain. For an instance that uses a public network connection, use the Looker (Google Cloud core) instance's ingress public IP for the A record's IP address. The ingress public IP can be found on the [**Details**](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_details_and_custom_domain_tabs) tab of the Looker (Google Cloud core) instance in the Google Cloud console. (It is also displayed in the **Data** field in the **Update your DNS records** section of the **Add a new custom domain** panel.)

If your domain uses Certification Authority Authorization (CAA) records, verify that they authorize Google's Certificate Authorities (`pki.goog` and `letsencrypt.org`) to issue certificates. Custom domains for public instances also don't support third-party CDNs or reverse proxies (such as Akamai or Cloudflare) in front of the public IP address because automated certificate provisioning requires direct A record resolution. To route traffic through a third-party CDN or WAF, see [Public inbound access to a Looker (Google Cloud core) instance using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access-public).

If a **VERIFY DOMAIN** button appears on the **CUSTOM DOMAIN** tab of the Looker (Google Cloud core) instance, your DNS record may require additional configuration. Click **VERIFY DOMAIN** to complete the setup of your custom domain. If domain verification fails with a `code: 9` error ("DNS record is not created or not the same as public IP address"), then see [Troubleshoot custom domain code 9 error](https://docs.cloud.google.com/looker/docs/looker-core-networking-troubleshooting#custom-domain-code-9).

**Note:** It may take up to 24 hours for any changes to your DNS record to take effect. The SSL certificate that is associated with your DNS record may require several minutes to activate.

Once your domain's DNS records are updated and your domain has been verified in the Google Cloud console, the [status](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-settings) of the custom domain that is mapped to the instance will be updated from **Unverified** to **Available** on the **Custom domain** tab.

### Update the OAuth credentials

**Note:** You can use any OAuth client to create authorization credentials for your Looker (Google Cloud core) instance. As an example, these steps walk you through updating the credentials using the Google Cloud console. If you are using a different client, adjust the steps accordingly.

  1. Access your OAuth client by navigating in the Google Cloud console to **APIs & Services > Credentials** and selecting the OAuth client ID for the OAuth client that is used by your Looker (Google Cloud core) instance.
  2. Click the **Add URI** button to update the **Authorized JavaScript origins** field in your OAuth client to include the same DNS name that your organization will use to access Looker (Google Cloud core). For example, if your custom domain is `looker.examplepetstore.com`, you would enter `looker.examplepetstore.com` as the URI.

![](https://docs.cloud.google.com/static/looker/docs/images/core-custom-domain-ajso.png)

  3. [Add](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client) the custom domain to the list of **Authorized redirect URIs** for the [OAuth credentials that you used](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth) when you created the Looker (Google Cloud core) instance. Add `/oauth2callback` to the end of the URI. For example, if your custom domain is `looker.examplepetstore.com`, you would enter `looker.examplepetstore.com/oauth2callback`.

![](https://docs.cloud.google.com/static/looker/docs/images/core-custom-domain-aruris.png)

You must have both the custom domain URL and the original Looker (Google Cloud core) autogenerated URL listed in the **Authorized redirect URIs** section of the OAuth client.




### Add users

Once the preceding steps are completed, the custom domain URL is accessible to users.

Ensure that the [user authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication) is completely set up for the Looker (Google Cloud core) instance before adding users to the instance.

## Configure your custom domain for cross-domain iframe embedding

After you set up the custom domain, ensure that you update the application's iframe URL to point to the new custom domain. Additionally, verify that corporate network policies, such as VPNs or MAM tunnels, allow access to the new custom domain.

## What's next

  * [Configure an IP allowlist for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist)
  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)
  * [Configure your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Connect Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
