---
url: https://docs.cloud.google.com/identity/docs/how-to/verify-domain/
title: Verifying your domain \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:28.277997+00:00
---

# Verifying your domain  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/verify-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Verifying your domain

To make sure no one else uses your domain with Cloud Identity, you need to add a unique text (TXT) record in your domain settings, which proves you own your domain.

**Note:** If you purchased your domain through a Google partner when you signed up for Cloud Identity, your domain might be verified already.

To verify your domain, you need to complete the following steps:

  1. Copy a unique TXT record value from the Google Admin console
  2. Paste the unique TXT record value in your domain registrar settings
  3. Verify ownership in the Google Admin console



## Step 1: Copy a unique TXT record value from the Google Admin console

  1. [Sign in](https://admin.google.com/) with an administrator account to the Google Admin console.

If you aren't using an administrator account, you can't access the Admin console.

  2. Go to **Account > Domains** > **Manage domains**.

Requires having the [Domain settings](https://support.google.com/a/answer/1219251#domains) administrator privilege.

**Tip:** If you recently signed up for Cloud Identity, you can use the [Setup tool](https://workspace.google.com/verify/expectations).
  3. Click **Verify domain** for the domain or subdomain you want to verify.

  4. In the domain setup tool, click **Get started** , then choose your domain registrar and click **Continue**. If your domain registrar isn't in the list, select **My domain uses a different host**.

  5. In the "TXT record" section, copy the **Value** , including "google-site-verification=".




## Step 2: Paste the unique TXT record value in your domain registrar settings

### Detailed instructions for popular domain registrars

  * [Amazon (AWS) Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html)
  * [BlueHost](https://www.bluehost.com/help/article/dns-management-add-edit-or-delete-dns-entries#access)
  * [Cloudflare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)
  * [GoDaddy](https://www.godaddy.com/help/add-a-txt-record-19232)
  * [Hostinger](https://support.hostinger.com/en/articles/4469063-how-to-add-and-remove-txt-records-in-cpanel)
  * [IONOS](https://www.ionos.com/help/domains/configuring-txt-and-srv-records/managing-txt-records/)

| 

  * [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/1244/2234/google-workspace-domain-registered-with-namecheap-ownership-validation/#g)
  * [Shopify](https://help.shopify.com/en/manual/domains/managing-domains/edit-dns-settings)
  * [Squarespace](https://support.squarespace.com/hc/en-us/articles/217402917-Troubleshooting-Google-Workspace-domain-verification#toc-step-4---add-a-txt-record-if-retrying-fails)
  * [Wix](https://support.wix.com/en/article/manually-verifying-your-domain-with-google-workspace-formerly-g-suite)
  * [Wordpress](https://wordpress.com/support/add-email/add-email-through-google-workspace/)

  
---|---  
  
### General instructions

  1. Sign in to the website where you manage your domain. This is where you can change your domain's DNS records.
  2. Go to your domain's DNS settings. Look for something like **DNS Records** , **Domain Management** , or **Name Server Management**.
  3. Find the TXT records.
  4. Add a new TXT record, using the following values: Type | `TXT`  
---|---  
Name / Host / Alias | Leave this blank, or enter `@` If you're adding a subdomain, enter the subdomain value in this field. (Example: For the subdomain _support.your-company.com_ , you enter `support`)   
Value / Answer / Destination |  Enter your unique ID, copied from the Google Admin console. Example: `google-site-verification=abcdef123_456wx789yz`  
  5. Save your new TXT record.
  6. Wait for the changes to take effect. It can take up to 72 hours for the new TXT records to be recognized. After your domain registrar publishes the code, the system recognizes you as the domain owner.



## Step 3: Verify ownership in the Google Admin console

  1. Go back to the Admin console, where you copied the unique TXT record value. If you've already closed that window, follow the instructions in Step 1 again.
  2. Select **Come back here and confirm** , then click **Confirm**. The Admin console then searches for your unique TXT record and checks if it's associated with the domain you're verifying.
  3. If the Admin console finds your unique TXT record associated with the expected domain, you're all set. If it can't find your TXT record, a message appears telling you that your domain couldn't be verified. Review the tips on screen and try the troubleshooting steps in this page for help.



## Troubleshooting steps

  * **Double-check your entries** : Make sure you entered everything correctly, following your domain registrar's preferred format.
  * **Wait 72 hours** : It can take some time for TXT record changes to be recognized across the internet.
  * **Contact your domain registrar's support** : They can help you troubleshoot any issues with your DNS settings. If you're not sure which registrar to contact, read our tips about how to [identify your domain registrar](https://docs.cloud.google.com/identity/docs/how-to/identify-host).
  * **Domain already in use** : If the domain is already associated with another Google Account, try to regain access by recovering the administrator account. For more information, see [Recover access](https://knowledge.workspace.google.com/admin/users/recovering-administrator-access-to-your-account).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
