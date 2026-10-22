---
url: https://docs.cloud.google.com/appengine/docs/flexible/mapping-custom-domains/
title: Mapping custom domains \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:35.670141+00:00
---

# Mapping custom domains  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/mapping-custom-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Mapping custom domains Stay organized with collections  Save and categorize content based on your preferences. 

You can use a custom domain rather than the default address that App Engine provides for your app.

To use a custom domain, map the domain to your app, then update your DNS records. You can map a naked domain, such as `example.com` or a subdomain, such as `subdomain.example.com`. You can also use wildcards to map subdomains.

By default, when you map a domain to your app, App Engine issues a managed certificate for SSL for HTTPS connections. For more information on using SSL with your custom domain, including how to use your own SSL certificates, see [Securing your custom domains with SSL](https://docs.cloud.google.com/appengine/docs/flexible/securing-custom-domains-with-ssl).

Using custom domains might add noticeable latency to responses that App Engine sends to your app's users in some regions. The regions are as follows:

  * us-west2
  * us-east4
  * northamerica-northeast1
  * southamerica-east1
  * europe-west2
  * europe-west3
  * asia-south1
  * asia-northeast1
  * australia-southeast1



App Engine custom domains use a pool of shared IP addresses for all applications. If you want to use an IP address that only maps to your domain then you should instead [set up a load balancer with App Engine](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless). This may mitigate a domain fronting issue in which a request to application A in the SNI certificate may be routed to application B in the HTTP Host header.

## Before you begin

  * If you do not have a domain, purchase one. You can use any domain name registrar.

  * In order to add or edit a custom domain mapping, your account must have the [App Engine Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`) or a custom role that contains the `appengine.applications.get` permission.

  * If you use Cloud Load Balancing and [serverless network endpoint group (NEGS)](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) to route traffic to your App Engine app, we recommend that you map your custom domain to the load balancer instead of directly to your app, and use Google-managed SSL certificates that are created for the load balancer. This eliminates the need to manage separate SSL certificates for each serverless app. With Cloud Load Balancing, you can set SSL policies that control the features of SSL that your load balancer negotiates with clients.

For more information, see the following pages:

    * [Using Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)
    * [Using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)
    * [SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)

Note the following limitation:

    * We recommend that you [use ingress controls](https://docs.cloud.google.com/appengine/docs/flexible/application-security#ingress_controls) so that your app only receives requests sent from the load balancer (and the VPC if you use it). Otherwise, users can use your app's App Engine URL to bypass the load balancer, Cloud Armor security policies, SSL certificates, and private keys that are passed through the load balancer.



## Mapping a custom domain to your app

**Note:** These instructions describe using the Google Cloud console to map custom domains. If you prefer, you can use [gcloud commands](https://docs.cloud.google.com/sdk/gcloud/reference/app/domain-mappings) or the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings).

  1. In the Google Cloud console, go to the **Application settings** tab of the App Engine **Settings** page.

[Go to Application settings](https://console.cloud.google.com/appengine/settings)

If you do not need to modify the default **Google Accounts API** Referrer, move to the next step.

If you need to enable Google Workspace authentication for your custom domain, click **Edit** to modify the **Google Accounts API** Referrer. In the **Google Authentication** drop-down menu, select **Google Workspace domain** , then add your domain such as `example.com` in the empty field.

  2. In the Google Cloud console, go to the **Custom Domains** tab of the App Engine **Settings** page.

[Go to Custom Domains](https://console.cloud.google.com/appengine/settings/domains)

  3. Click **Add a custom domain**.

  4. If your domain is already verified, the domain appears in the _Select the domain you want to use_ section. Select the domain from the drop-down menu and click **Continue**.

If you haven't verified your domain yet, do the following:

     1. Select **Verify a new domain** from the drop-down menu.
     2. Enter your naked domain name (such as "example.com") and click **Verify**.

Even if you only want to map a subdomain, such as "www.subdomain.example.com", enter the naked domain name to verify ownership.

Note that domain names must be shorter than 64 bytes.

     3. Enter information in the Search Console window that appears. For help using Search Console, see [Search Console help](https://support.google.com/webmasters/answer/9008080)

     4. After you complete the steps in Search Console, return to the **Add a new custom domain** page in the Google Cloud console.

  5. In the _Point your domain to [project-ID]_ section, specify the domain and subdomains that you want to map.

We recommend mapping the naked domain and the `www` subdomain. You can add more subdomains if you need them.

When you've added all the mappings you want, click **Save mappings**.

  6. Click **Continue** to see your domain's DNS records.

You can retrieve these records any time on the **Custom Domains** tab of the App Engine **Settings** page.

  7. Sign in to your domain registrar web site and update your DNS records with the records displayed in the previous step.




## Updating DNS records at your domain registrar

**Note:** If you have a custom domain set up for your App Engine app and want to move it to a different Google Cloud project, you do not need to update your custom domain DNS records as these will remain fixed for the domain when you switch projects.

After you've mapped your service to a custom domain in App Engine, you need to update your DNS records at your domain registrar. As a convenience, App Engine generates and displays the DNS records you need to enter.

**Note:** Some third party CDN providers might inadvertently intercept validation requests, preventing them from reaching the App Engine app and causing the domain mapping to fail or its certificate to fail to renew. For example, if you are using Cloudflare CDN, you should turn off the "_Always use https_ " option in the "_Edge Certificates_ " tab of the _SSL/TLS_ tab.

  1. Retrieve the DNS record information for your domain mappings:

In the Google Cloud console, go to the **Custom Domains** tab of the App Engine **Settings** page. The page lists DNS records for all of the domains you have mapped to your app.

  2. Log in to your account at your domain registrar and open the DNS configuration page.

  3. Locate the host records section of your domain's configuration page and add each of the DNS records that you retrieved when you mapped your domain to your app.

Enter the following information in the record fields:

     * Record type: Enter the record type that is shown in the DNS record Google created for you (`A`, or `AAAA`, or `CNAME`).
     * Record name:

       * In `A` or `AAAA` records, enter `@`
       * In `CNAME` records, enter a third-level domain name. For example, enter `www` to map the `www.example.com` subdomain.
     * Note that if you are using Cloud DNS, there is no need to add an @ symbol when creating an `A` record for your parent custom domain (example.com). However, you might need to specify an @ symbol for other DNS providers like GoDaddy.

     * TTL: Specify a TTL depending on your needs.

     * Data: Enter the record data (rrdata) that is shown in the DNS record Google created for you.

       * In `A` or `AAAA` records, the record data is an IP address
       * In `CNAME` records, the record data is a domain name
  4. Save your changes in the DNS configuration page of your domain's account. In most cases, it takes only a few minutes for these changes to take effect, but in some cases it can take up to several hours, depending on the registrar and the [Time-To-Live (TTL)](https://support.google.com/a/answer/48090) of any previous DNS records for your domain. You can use a [`dig`](https://wikipedia.org/wiki/Dig_\(command\)) tool, such as [this online `dig` version](https://toolbox.googleapps.com/apps/dig/#A/), to confirm the DNS records have been successfully updated.

  5. Test for success by browsing to your service at its new URL, for example `https://www.example.com`. Note that it can take several minutes for the automatic SSL certificate to be issued.


**Note:** According to [RFC 1912, section 2.4](https://www.rfc-editor.org/rfc/rfc1912), a `CNAME` record cannot coexist with any other data. In other words, if the subdomain `www.example.com` is an alias for `example.com`, you cannot also have an `MX` record, an `A` record, or even a `TXT` record for `www.example.com`.

### Delegating ownership to other Google Cloud users or service accounts

If you need to delegate the ownership of your domain to other users or service accounts, you can add permission through the _Search Console_ page. To view a list of service accounts, open the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page in the Google Cloud console

To add permissions through the _Search Console_ : 

  1. Open the [Search Console verification](https://search.google.com/search-console/welcome). 

  2. Under **Properties** , click the domain for which you want to add a user or service account.

  3. Go to **Settings** from the side panel.

  4. Under **General Settings** , click **Users and Permissions** to find the owners of your domain.

  5. Click **Add User** and enter the email ID of the user. Select the required permission to grant the user. For details on permissions, see [Managing owners, users and permissions](https://support.google.com/webmasters/answer/7687615).

  6. Click **Add** to delegate ownership to the user.




## Using subdomains

If you set up a wildcard subdomain mapping for your custom domain, your application serves requests for any matching subdomain.

  * If the user browses a domain that matches an application version name or service name, the application serves that version.
  * If the user browses a domain that matches a service name, the application serves that service.
  * There is a limit of 20 managed SSL certificates per week for each base domain. If you encounter the limit, App Engine keeps trying to issue managed certificates until all requests have been fulfilled.



### Wildcard mappings

You can use wildcards to map subdomains at any level, starting at third-level subdomains. For example, if your domain is `example.com` and you enter text in the web address field:

  * Entering `*.example.com` maps all subdomains of `example.com` to your app.
  * Entering `*.private.example.com` maps all subdomains of `private.example.com` to your app.
  * Entering `*.nichol.sharks.nhl.example.com` maps all subdomains of `nichol.sharks.nhl.example.com` to your app.
  * Entering `*.excogitate.system.example.com` maps all subdomains of `excogitate.system.example.com` to your app.



You can use wildcard mappings with services in App Engine by using the [`dispatch.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/dispatch-yaml) file to define request routing to specific services.

**Note:** Wildcard mappings are not supported for managed SSL certificates.

If you use [Google Workspace](https://workspace.google.com/) with other subdomains on your domain, such as `sites` and `mail`, those mappings have higher priority and are matched first, before any wildcard mapping takes place. In addition, if you have other App Engine apps mapped to other subdomains, those mappings also have higher priority than any wildcard mapping.

Some DNS providers might not work with wildcard subdomain mapping. In particular, a DNS provider must permit wildcards in `CNAME` host entries.

Wildcard routing rules apply to URLs that contain components for services, versions, and instances, following the [service routing rules for App Engine](https://docs.cloud.google.com/appengine/docs/flexible/how-requests-are-routed#urls).

## Deleting custom domains from your app

In order to delete a custom domain mapping from your app, your account must have the [App Engine Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) (`roles/appengine.appAdmin`) or a custom role that contains the `appengine.applications.update` permission.

In the Google Cloud console, do the following:

  1. Go to the **Custom Domains** tab of the App Engine **Settings** page.

[Go to Custom Domains](https://console.cloud.google.com/appengine/settings/domains)

  2. Select the custom domain name and click **Delete**.




Alternatively, you can use [gcloud commands](https://docs.cloud.google.com/sdk/gcloud/reference/app/domain-mappings) or the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings) to delete custom domains.

## Troubleshooting

If your app shows authentication errors after configuring your custom domain with Google Workspace domain authentication, remove your custom domain mapping and redo the steps for mapping a custom domain to your app. Make sure to configure your Google Workspace domain authentication _before_ configuring your custom domain mapping in App Engine.

## What's next

  * Learn how to [secure your custom domains with SSL](https://docs.cloud.google.com/appengine/docs/flexible/securing-custom-domains-with-ssl).
  * If you want Cloud Load Balancing to manage incoming requests to your custom domain, see [Migrate App Engine custom domain to Cloud Load Balancing](https://docs.cloud.google.com/appengine/docs/flexible/custom-domain-to-cloud-load-balancing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
