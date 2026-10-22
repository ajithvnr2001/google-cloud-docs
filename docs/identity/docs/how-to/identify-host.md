---
url: https://docs.cloud.google.com/identity/docs/how-to/identify-host/
title: Finding your domain host \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:36.076542+00:00
---

# Finding your domain host  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/identify-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Finding your domain host

A domain registrar is an internet company that manages your domain name, such as, _example.com_. Domain registrars use Domain Name System (DNS) records to connect your domain name with email, websites, and other web services. Popular domain registrars include GoDaddy, Squarespace, and IONOS, to name a few.

Google Workspace uses DNS records to:

  * Verify you are the owner of your domain
  * Route your company's email messages to Google mail servers



## Find your domain registrar

### Check your billing records

Your domain registrar is typically who you bought your domain name from. If you don't remember who your domain registrar is, search your email archives for billing records about registration or transfer of your domain name.

Your domain registrar is listed on your invoice.

### Use ICANN Lookup

If you can't find your billing records, you can search for your domain registrar online. The Internet Corporation for Assigned Names and Numbers (ICANN) is a non-profit organization that collects domain information. Use the ICANN Lookup tool to find your domain registrar.

  1. Go to [lookup.icann.org](https://lookup.icann.org).
  2. In the search field, enter your domain name and click **Lookup**.
  3. In the results page, scroll to **Registrar Information**.

The registrar is usually your domain registrar.




#### Domain resellers

Some domains are registered by resellers through a separate registrar. If you can't sign in with your listed registrar or the registrar field is blank, your domain registrar might be a reseller.

  1. In the ICANN Lookup results page, go to the **Raw Registry RDAP Response**.
  2. Look for the **Reseller** entry.
  3. Go to the reseller's website.
  4. Sign in with the credentials you used when you purchased (or transferred) your domain.

If you forgot your password, contact the reseller's support team.




If no reseller is listed, contact the listed registrar's support team for help.

### Third-party DNS registrars

Several third-party DNS registrar services, such as ClouDNS.net and FreeDNS, offer custom DNS registration. If you use a third-party DNS registrar for your domain, the registrar listed in the ICANN Lookup is not where your domain records are managed.

Sign in to your third-party DNS registrar to access your domain records.

_Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product names are trademarks of the companies with which they are associated._

## What's next

  * [Verify your domain ownership](https://docs.cloud.google.com/identity/docs/verify-domain)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
