---
url: https://docs.cloud.google.com/solutions/authenticating-web-users/
title: Controlling access to websites and apps \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:31.940547+00:00
---

# Controlling access to websites and apps  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/authenticating-web-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Controlling access to websites and apps Stay organized with collections  Save and categorize content based on your preferences. 

To secure your web resources in a simple-to-manage, scalable, and granular way, Google Cloud offers [context-aware access](https://docs.cloud.google.com/context-aware-access/docs/overview) using [Identity-Aware Proxy](https://docs.cloud.google.com/iap) (IAP). IAP is designed to enforce the [BeyondCorp](https://docs.cloud.google.com/beyondcorp) security model, which establishes a zero-trust perimeter on the public internet for secure, remote work without the need for a traditional VPN.

You can allow secure access to your websites or web apps for users located anywhere or on any device by using IAP to control granular restrictions. Access control can be configured based on the user's identity and context of their request without making additional site changes. You can also centrally define and enforce access policies across multiple apps and sites, including [IAM policies with conditional binding](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto). IAP works with other Google Cloud offerings, including [Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run), [App Engine standard environment](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts), [Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto), and [Google Kubernetes Engine](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto).

## Configuring your access levels

When accessing web resources that IAP knows about, users need to sign in with their Google identity service credentials (for example, their Gmail or Google Workspace email address) or an LDAP registered with an LDAP directory service that's synchronized with the Google identity service. If the user is authorized, IAP forwards their request to the web server along with header data that includes the user's identity.

![Image shows IAP routing requests from authenticated users to a web server.](https://docs.cloud.google.com/static/solutions/images/iap-web-access.png)

**Figure 1.** Controlling user access to web resources behind IAP.

In the Google Cloud console, you can configure IAP to block unauthorized users from accessing a given resource.

To do so for a resource on App Engine:

  1. Open the [Identity-Aware Proxy page](https://console.cloud.google.com/security/iap) in your active project.
  2. Select the resource you want to modify.
  3. Click **Add Principal** and add the email addresses of groups or individuals to whom you want to grant the **IAP-secured Web App User** role for the project.

The following table lists some common access scenarios and the principal to grant access to for each scenario.

**Access Level** | **Example Web Resource** | **Example Principal**  
---|---|---  
Open, public access  | Company public website.  | `allUsers`  
User-authenticated access  | Site to submit support tickets.  | `allAuthenticatedUsers`  
Employee-restricted access  | App running on the company intranet.  | `bigcorpltd.com`, `contractors@bigcorpltd.com`  
Highly-sensitive, device and employee-restricted access  | App with access to customer private information.  | `customer.support@bigcorpltd.com` **Note** : This access level requires adding restriction information through the [Access Context Manager](https://console.cloud.google.com/security/access-level), such as device policy attributes or allowed IP subnetworks. Users also need to have work profiles on their mobile device or a Chrome extension set up on their browser.  
  4. Click **Add** to save your changes.



## Next steps

  * Get started by familiarizing yourself with [IAP concepts](https://docs.cloud.google.com/iap/docs/concepts-overview) and following the [quickstarts](https://docs.cloud.google.com/iap/docs/quickstarts).
  * Learn more by viewing these introductory videos: 
    * [BeyondCorp in a bottle](https://www.youtube.com/watch?v=TtmsV-xq0r0)
    * [Centralize access to your organization’s websites with Identity-Aware Proxy](https://youtu.be/xM9-FSU5MoY)
  * Check out these tutorials for using IAP with [App Engine standard environment](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts), [Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto), [Google Kubernetes Engine](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto), and [on-premises apps](https://docs.cloud.google.com/iap/docs/enabling-on-prem-howto).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
