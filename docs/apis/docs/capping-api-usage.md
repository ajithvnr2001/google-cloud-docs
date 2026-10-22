---
url: https://docs.cloud.google.com/apis/docs/capping-api-usage/
title: Capping API usage \u00a0|\u00a0 Cloud APIs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:29.384899+00:00
---

# Capping API usage  |  Cloud APIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/capping-api-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)



Send feedback 

#  Capping API usage Stay organized with collections  Save and categorize content based on your preferences. 

API-specific usage quotas let you cap requests per day, requests per minute, or requests per minute per user to help you control service traffic and stay within free tier limits. Because these caps regulate individual API volumes rather than overall spending, use [budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) to prevent unexpected costs across an entire project or billing account. Quota enforcement has a latency period after a threshold is surpassed, so include a safety buffer when you configure caps to manage billing costs.

## View and modify the limits on the number of requests

You can set limits to all requests to any billable API. Most APIs set default limits, but you can change that limit up to a maximum specified by Google. Some APIs set a low limit until you [enable billing on your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

To view or change the limits for your API, do the following:

  1. In the Google Cloud console, go to the **APIs & Services Dashboard** page. 

[ Go to APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard?project=_)

  2. From the projects list, select a project or create a new one.
  3. Click the name of the API you're interested in.
  4. Click **Quotas**. If the **Quotas** tab is not present in the tab nav, it means the API you've selected doesn't have quotas defined.
  5. To find the quota you want to cap, enter the appropriate properties and values in the filter_list **Filter** field. For example, to find the **Subnetworks** quota, enter **Quota:Subnetworks**.
  6. Click the checkbox next to the quota you want to cap, and then click create **EDIT QUOTAS**.
  7. Complete the quota change form, including the new limit that you want to set.
  8. Click **SUBMIT REQUEST**.



Some APIs let you request a higher limit by submitting a form. Some APIs let you specify a higher quota only if [ billing is enabled on the project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

**Note:** You can set daily billable limits only on billable APIs, and in some cases, only if billing is enabled on your project. If your project doesn't use any billable APIs, then you can't set daily limits. [ Learn more about billing accounts](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account).

## Limiting requests per user

To prevent individual users from using up your API quota, some APIs include a default per user per minute limit.

To check if your API includes a default per user per minute limit, look for it in your API quotas as described in the instructions for View and modify the limits on the number of requests. If such a default limit exists for that API, you can modify that value to limit the quota available to each user by following the steps in these instructions. If your API does not include this default limit in its quotas, adding or modifying it is not supported.

By default, the system uses the authenticated principal to uniquely identify individual users. The authenticated principal includes user accounts using OAuth tokens, service accounts, or federated workload identities. If there is no authenticated principal, the system uses the client IP address. Because this fallback behavior is active by default, per-user quotas are enforced even if you don't specify a user identifier.

Using the client IP address fallback has two key limitations:

  * **Shared public IPs** : Multiple users behind a network address translation (NAT) gateway or proxy, such as a school office or VPN endpoint, will share a single public IP address. Their requests will pool into the same quota bucket, potentially leading to premature quota exhaustion.
  * **IP-based evasion** : Users with access to large blocks of IPv6 addresses or VPN proxies can rotate client IP addresses to bypass rate limiting, making the IP fallback unreliable for robust abuse protection.



If you are calling the API from a server-side application, where the calling code is hosted on a server that you own, on behalf of multiple users, and you use a single authenticated principal, all calls will be attributed to that single principal. In this case, calls from individual users cannot be capped separately. To prevent this, you can override the default user identification and partition quota usage by specifying the `quotaUser` parameter or `X-Goog-Quota-User` header in your requests. These are defined in the [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters) documentation.

To override the default user identification with the `quotaUser` parameter or `X-Goog-Quota-User` header, you must identify the quota project using a valid API key with service restrictions, such as IP address restrictions or HTTP referrer restrictions. Otherwise, the parameter or header is ignored and the system falls back to the default user identification.

To identify a user, use the `quotaUser=userID` URL query parameter. This value is for short-term quota enforcement only, so you don't need to use a real user ID. You can choose any arbitrary string under 40 characters long that uniquely identifies a user.

**Note:** Although per-user limits are specified in queries per minute, we permit short-term usage spikes. Therefore, you should set your limits based on sustained average traffic levels. If anyone tries to use an API in excess of these settings, the requests will trigger a _limit exceeded_ error.

To protect user privacy and limit metric volume, the Google Cloud console and Cloud Monitoring don't store or display telemetry parsed by an individual `quotaUser` or IP address. You can view the overall project quota limit and total usage, but you cannot monitor, override, or configure alerts for specific individual users.

If your API does not include a default per user per minute limit, then `quotaUser` values are ignored.

**Important:** When sending any user identifier, be sure that you comply with any local laws, including any laws relating to the disclosure of any personal information you send with each request. Best practice is to include as little personal information as possible.

## View and edit all quotas for APIs in a project

You can review, edit, and request higher quota limits for all billable APIs in a given project by viewing the **Quotas** page in the **IAM & Admin** section of Google Cloud console.

To view and edit quotas for all billable APIs in your project, do the following:

  1. In the Google Cloud console, go to the **Quotas** page. 

[ Go to Quotas](https://console.cloud.google.com/iam-admin/quotas?project=_)

  2. From the projects list, select a project or create a new one. The **Quotas** page for the selected project displays, listing one line item for each type of quota available in each service.
  3. Click filter_list **Filter table** to query your quota by a specific property.
  4. Check the box next to the quota(s) you want to edit. Billing must be enabled on the project in order to click some of the checkboxes. If you prefer to edit all the quotas for a single API, click the name of the service to access the Quotas page for that API.
  5. Click edit **EDIT QUOTAS**.
  6. In the **Quota changes** pane that displays, expand the service view, then edit the quotas in that service as needed, and then click **DONE**.
  7. Repeat to edit the quotas in each of the selected services. 
     * The current quota limits are pre-populated in the input boxes.
     * A service with an alert icon (error) on submission has input errors.
     * You can add more quotas to edit by selecting them as described before.
     * You can remove a service from the **Quota changes** pane by hovering over the unexpanded service view, and then clicking the delete icon (delete).
  8. When you are done editing quotas, click **NEXT**.
  9. If your quota edit request needs review, the **Contact details** form displays. Complete the form with your contact details.
  10. Click **SUBMIT REQUEST**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
