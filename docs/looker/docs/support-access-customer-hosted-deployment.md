---
url: https://docs.cloud.google.com/looker/docs/support-access-customer-hosted-deployment/
title: Allowing Looker support to access a customer-hosted deployment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:07:54.543872+00:00
---

# Allowing Looker support to access a customer-hosted deployment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/support-access-customer-hosted-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Allowing Looker support to access a customer-hosted deployment Stay organized with collections  Save and categorize content based on your preferences. 

If you are hosting your own Looker deployment, we **strongly** recommend that you provide a means for the Looker Support team to access your Looker application. This helps us answer questions and resolve issues as quickly as possible.

## Contacting Looker Support to access your Looker instance

You can enable support by adding to the allowlist the traffic from our secure gateway IP address, `54.209.194.236`, to your Looker application. Looker access to the secure gateway is strictly controlled and secured with multifactor authentication. The secure gateway IP to add to the allowlist is different than the IP addresses that Looker hosts customers on.

The destination will be your Looker application's host and HTTPS port, generally 9999. This hostname/IP needs to be publicly routable from the internet. See this [American Registry for Internet Numbers](https://www.arin.net/knowledge/address_filters.html) page for more information on private addresses.

## Contacting Looker Support to finish deploying your Looker instance

After you have added Looker's secure gateway to the allowlist, the Looker Support team will need to do some further configuration. [Open a support request](http://console.cloud.google.com/support/cases) and provide the following:

  * Your company's name.
  * The destination URL of your Looker instance.
  * The hostname of your Looker instance as seen from the public Internet, for example `looker.mycompany.com`.
  * The port on which Looker's web interface is listening. By default this is 9999, but many customers change it to 443 (the standard for HTTPS).



This support request lets the Looker Support team finish enabling access for Looker support or answer any additional questions you may have.

## Next steps

Once you have added Looker's secure gateway IP address to the allowlist, you can ensure the [Support Access](https://docs.cloud.google.com/looker/docs/admin-panel-general-support-access) feature is enabled.

After that, you're ready to [set up Looker monitoring](https://docs.cloud.google.com/looker/docs/monitoring-looker).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-22 UTC."],[],[]] 
