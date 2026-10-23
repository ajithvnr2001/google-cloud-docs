---
url: https://docs.cloud.google.com/looker/docs/looker-hosted-custom-domain/
title: Configure custom domains for Looker-hosted instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:36.368851+00:00
---

# Configure custom domains for Looker-hosted instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-hosted-custom-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Configure custom domains for Looker-hosted instances Stay organized with collections  Save and categorize content based on your preferences. 

Admins of Looker-hosted (original) instances can configure a custom domain (also known as a _vanity URL_), such as `analytics.example.com`, as the primary, canonical URL for their instance. Configuring a custom domain ensures that your custom domain remains visible in the browser address bar instead of redirecting to a default `cloud.looker.com` domain.

Configuring a custom domain for a Looker-hosted instance requires that you submit a request to Google Cloud Support and complete the DNS configuration with your domain provider.

**Note:** If you are using Looker (Google Cloud core), see [Set up a custom domain for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain).

## Workflow overview

To set up a custom domain for a Looker-hosted instance, complete the following steps:

  1. Contact Google Cloud Support to request custom domain configuration.
  2. Add the required CNAME records to your DNS provider's configuration.
  3. Wait for SSL/TLS certificate deployment during the next scheduled maintenance window.
  4. Update host URL and authentication settings.



## Contact Google Cloud Support

To request a custom domain for your Looker-hosted instance, open a ticket with [Google Cloud Support](https://cloud.google.com/support). Include the following information in your request:

  * Your **Looker license key**. You can find your license key in the Looker **Admin** panel under **General Settings**.
  * The chosen **custom domain name(s)** (for example, `looker.example.com`).



Google Cloud Support will initiate the backend configuration and provide you with two CNAME records:

  * **Traffic CNAME record** : Routes traffic from your custom domain to your Looker-hosted instance.
  * **`_acme-challenge` CNAME record**: Used by Google Trust Services (GTS) for Domain Control Validation (DCV) to issue and automatically renew your SSL/TLS certificate.



## Configure DNS records

After receiving the CNAME records from Google Cloud Support, add them to your DNS provider's configuration:

  1. Add the **Traffic CNAME record** mapping your custom domain (for example, `looker.example.com`) to the Looker target host provided by Support.
  2. Add the **`_acme-challenge` CNAME record** provided by Support for SSL certificate validation.
  3. Verify that there are no existing TXT records on the `_acme-challenge` subdomain that might conflict with the CNAME record.

**Caution:** You must maintain the `_acme-challenge` CNAME record in your DNS configuration permanently. Deleting or modifying this record after initial setup will prevent GTS from performing automated 90-day SSL/TLS certificate renewals, which will result in certificate expiration and service disruption.

## Wait for SSL/TLS certificate deployment

Once your DNS records have propagated, the follow actions occur:

  * GTS validates domain control by using the `_acme-challenge` CNAME record and issues an SSL/TLS certificate.
  * The certificate is deployed to your Looker-hosted instance during its next scheduled maintenance window.



If you require immediate deployment outside of the standard maintenance window, inform Google Cloud Support during your request.

## Update host URL and authentication settings

After the custom domain is active and accessible, complete the following steps:

  1. **Update Host URL** : In the Looker **Admin** panel, navigate to **Settings** under the **General** section, and update the **Host URL** field to your new custom domain URL (for example, `https://looker.example.com`).
  2. **Update SAML / SSO Identity Provider** : If your instance uses SAML, OpenID Connect, or LDAP authentication, update your Identity Provider (IdP) configuration. Ensure that the Entity ID, Assertion Consumer Service (ACS) URL, and Authorized Redirect URIs use the new custom domain URL to prevent authentication failures or user lockouts.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
