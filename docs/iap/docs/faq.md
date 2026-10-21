---
url: https://docs.cloud.google.com/iap/docs/faq/
title: Troubleshooting and frequently asked questions \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:48.188319+00:00
---

# Troubleshooting and frequently asked questions  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Support ](https://docs.cloud.google.com/iap/docs/support)



Send feedback 

#  Troubleshooting and frequently asked questions Stay organized with collections  Save and categorize content based on your preferences. 

This document provides troubleshooting guidance and answers to frequently asked questions about Identity-Aware Proxy (IAP).

## Troubleshooting web sign-in

If you encounter errors during sign-in or when accessing your application, inspecting your browser's network traffic can help you diagnose the issue.

### Inspecting network traffic

  1. Open a new **Incognito** (Chrome) or **Private** window in your browser.
  2. Open your browser's developer tools and go to the **Network** tab.
  3. Select the **Preserve log** option to capture all requests during redirects.
  4. Reproduce the issue by navigating to the URL where you're experiencing problems.
  5. Examine the network requests in the log to identify where the error occurred.



### Analyzing network traffic

When you access an IAP-secured application, you're redirected to the sign-in page. After successful authentication with the identity provider, a request is made to the `https://iap.googleapis.com` domain to complete authentication before an IAP cookie is issued and you're redirected to the application.

You can troubleshoot errors based on the domain where the error occurs:

  * **Errors on`iap.googleapis.com`**: If an error occurs on the `iap.googleapis.com` domain, a detailed error message is displayed on the page. If the error is related to your IAP settings, such as OAuth client issues, adjust your settings. If you encounter client errors that you don't know how to address, or if you see server errors, open a [Google Cloud Support ticket](https://docs.cloud.google.com/support).
  * **Errors on your application domain** : If an error occurs after you're redirected to your IAP-secured application domain, an error code is displayed. Reference the Error codes section for details on common errors. If you cannot resolve the issue, open a [Google Cloud Support ticket](https://docs.cloud.google.com/support).



## What apps can I secure with IAP?

IAP can be used with the following:

  * App Engine standard environment and App Engine flexible environment apps

  * Compute Engine instances with HTTP(S) load balancing backend services

  * Google Kubernetes Engine containers

  * Cloud Run apps with HTTP(S) load balancing backend services

  * [Cloud Run with one click](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run) and no load balancing backend services 

IAP _cannot_ be used with [Cloud CDN](https://docs.cloud.google.com/cdn/docs).

## Why is there a # at the end of my URL after signing in to my app?

In some browsers and under certain conditions, a `#` may be appended to the URL after authentication. This is normal and won't cause issues when logging in.

## Why are my requests failing and returning `405 Method Not Allowed`?

This typically happens when cookies aren't attached to your requests. JavaScript methods don't attach cookies by default.

Different request methods require different approaches:

    * For [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials), set `withCredentials` to `true`.

    * For the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#Sending_a_request_with_credentials_included), set `credentials` to `include` or `same-origin`.

For handling session-related errors, see [Managing IAP sessions](https://docs.cloud.google.com/iap/docs/sessions-howto). 

## Why am I receiving an `HTTP 401 Unauthorized` instead of a `302 Redirect`?

IAP sends a `302 Redirect` only when your client is configured to handle redirects.

Add `HTTP Accept="text/html,*/*"` to your request headers to indicate support for redirects.

## Why aren't POST requests triggering redirects?

Browsers don't redirect in response to POST requests. Instead, IAP returns a `401 Unauthorized` status code.

For POST requests to IAP-secured resources, include either of the following:

    * An ID token in an `Authorization: Bearer` header

    * Valid cookies (see [refreshing sessions](https://docs.cloud.google.com/iap/docs/sessions-howto#expired_session_responses))

## Can I use IAP if I have disabled the API?

Yes, resources secured by IAP remain accessible when the API is disabled, but you won't be able to modify IAM permissions.

## How can I prevent users with the Owner role from using IAP for TCP?

Ideally, limit use of the Owner (`roles/owner`) role in favor of more granular permissions. See [IAM best practices](https://docs.cloud.google.com/iam/docs/using-iam-securely) for guidance.

If that's not possible, you can block IAP for TCP using [Firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).

## What domain does IAP for TCP use?

IAP uses the following Google-owned domains: 
    * `tunnel.cloudproxy.app`

    * `mtls.tunnel.cloudproxy.app` (when [certificate-based access](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-resources-with-certificate-based-access) is enabled)

**Caution:** Ensure that your proxy servers and firewalls allow traffic to these domains and don't block WebSocket connections.

## Why am I receiving `Server Error`?

If you see:
    
    The server encountered a temporary error and could not complete your request. Please try again in 30 seconds.
    

It's possible that your firewall may be blocking the load balancer IPs.

Check that your firewall allows traffic from `130.211.0.0/22` and `35.191.0.0/16`. If these IPs can't reach your backend, your applications will be inaccessible.

For IAP TCP connections to specific VMs, also ensure the VM accepts connections from the `35.235.240.0/20` range.

## Why am I receiving intermittent internal server errors?

Messages like `An internal server error occurred while authorizing your request. Error code X` indicate backend failures.

Error codes `1`, `30`, `62`, `63`, `64`, or `703` typically reflect transient issues. Implement exponential backoff for retries.

## How to correct Identity Platform errors (Error code 38)

Error code `38` indicates that the Identity Platform authentication URL for your external identity isn't configured correctly in IAP.

To find the URL, do the following:

    1. Go to the IAP page.

[Go to IAP](https://console.cloud.google.com/security/iap)

    2. Click the **Applications** tab.

    3. In the **Resource** column, find your application and select the checkbox.

    4. In **Authentication URL** or **Login URL** , make sure the URL is correct.

To learn how to use external identities with IAP, see [Authenticate users with external identities](https://docs.cloud.google.com/iap/docs/authenticate-users-external-identities). 

## How can I address quota exceeded errors (Error code 429)?

Error code 429 occurs when your application exceeds IAP's request limits. The service enforces separate quotas:

    * **Browser-based requests:** 360,000 per minute per project

    * **Programmatic requests:** 360,000 per minute per project

A programmatic request is one that includes an `AUTHORIZATION` or `PROXY-AUTHORIZATION` header and no IAP cookie. All other requests (including those with no credentials) are considered browser requests.

These limits apply collectively to all IAP-protected resources in your project.

If you're experiencing quota-related errors, consider these solutions:

    * Avoid load testing in production. Instead, use alternative network paths that bypass IAP.

    * For service-to-service traffic, implement exponential backoff to handle 429 errors gracefully.

    * Distribute high-traffic applications across multiple projects.

    * Use Apigee or similar API gateway solutions for API-based applications.

    * Contact [Google Cloud Support](https://docs.cloud.google.com/support) for quota increases if organic growth is causing the issue.

## Sign-in issues or unexpected behavior with IAP using Identity Platform

When using a third-party Identity Provider (IdP) with Identity Platform, large claims data in the ID token can cause the IAP session cookie to exceed browser size limits (typically around 4 KB). IAP stores session information, including these claims, in browser cookies.

Exceeding the session cookie size limit can lead to sign-in failures or infinite sign-in loops. To prevent these issues, consider the following actions:

    * **Reduce claims** : Configure your third-party IdP to send only essential claims to Identity Platform. Minimize the size and number of claims included in the token.

    * **Inspect cookie size** : Use browser developer tools to check the size of the cookies set on your application's domain. Look for warnings related to cookie size, particularly for IAP-related cookies.

    * **Test minimal claims** : Temporarily configure the IdP to send the smallest possible set of claims. If this resolves the issue, it confirms that cookie size limitation is the root cause.

## Why am I receiving an HTTP 502 error with "Empty Google Account OAuth client ID(s)/secret(s)"?

If you access your IAP-secured application and receive an `HTTP 502 Bad Gateway` error with the message `Empty Google Account OAuth client ID(s)/secret(s).`, IAP cannot find OAuth credentials for your application.

This error typically occurs in the following scenarios:

    * **The project does not belong to an organization:** The default Google-managed OAuth client is only available for projects that belong to a Google Cloud organization. If your project does not belong to an organization, you must [configure custom OAuth credentials for App Engine](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#app-engine) or for your respective platform.
    * **The OAuth credentials were deleted or not configured:** If you previously configured custom OAuth credentials and the OAuth client was deleted, re-create the credentials on the [Credentials page](https://console.cloud.google.com/apis/credentials) and update your IAP settings as described in [Use custom OAuth clients with IAP](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration). 

## Error codes

The following table lists common error codes and messages that return when configuring and using IAP.

Error code | Description | Troubleshooting  
---|---|---  
7, HTTP 502 | Empty OAuth client ID or secret (`Empty Google Account OAuth client ID(s)/secret(s).`) | If your project does not belong to an organization, [configure custom OAuth credentials](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration). Otherwise, visit the [Credentials page](https://console.cloud.google.com/apis/credentials) to verify your client ID and secret, or check settings using API methods ([`GET`](https://docs.cloud.google.com/iap/docs/reference/compute-engine-apis#get_iap_properties) for Compute Engine, [`GET`](https://docs.cloud.google.com/iap/docs/reference/app-engine-apis#get_iap_properties) for App Engine) and reset them with [`PATCH`](https://docs.cloud.google.com/iap/docs/reference/compute-engine-apis#set_iap_properties_by_updating). For more information, see HTTP 502 error.  
9 | Failed OAuth redirect | This is an internal error that has been logged automatically. No action is required on your part.  
9 (with path rewrite rules) | Failed OAuth redirect | Your load balancer's path rewrite rules are preventing OAuth completion. Make sure all backends behind your load balancer use identical OAuth client IDs. You can update this using the [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command.  
9 (with path routing rules) | Failed OAuth redirect | Create path rule variants for both versions of each path (with and without trailing slashes) and direct them to the same backend. For example, include rules for both `/path/` and `/path`.  
11 | Incorrectly configured OAuth client ID | Check your client ID and secret in the [Credentials page](https://console.cloud.google.com/apis/credentials). If they appear correct but aren't working, use API methods to check settings ([`GET`](https://docs.cloud.google.com/iap/docs/reference/compute-engine-apis#get_iap_properties) for Compute Engine, [`GET`](https://docs.cloud.google.com/iap/docs/reference/app-engine-apis#get_iap_properties) for App Engine) and reset them with [`PATCH`](https://docs.cloud.google.com/iap/docs/reference/compute-engine-apis#set_iap_properties_by_updating).  
13 | Invalid OIDC token | Go to the [Credentials page](https://console.cloud.google.com/apis/credentials) to confirm your client ID hasn't been deleted or modified incorrectly.  
51 | Browser lacks connection pooling support | Ask end users to update their browsers to current versions. For more details about connection requirements, see [Restrict resource access](https://docs.cloud.google.com/iap/docs/allowed-domains).  
52 | Hostname/SSL certificate mismatch | Your system administrator needs to update the SSL certificate to match the hostname. Refer to [Restrict resource access](https://docs.cloud.google.com/iap/docs/allowed-domains) for guidance.  
52 (with primary certificate map entry) | Hostname/SSL certificate mismatch | IAP does not support primary certificate map entries. Use separate entries to map each certificate to the correct hostname. See [Create a certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/map-entries#entry-create) for guidance.  
53 | Hostname not in allowed domains | An administrator must add your hostname to the allowed domains list. See [Restrict resource access](https://docs.cloud.google.com/iap/docs/allowed-domains) for instructions.  
253, HTTP 429 | Request quota exceeded | You've reached the request limits (360,000/min for each request type). Consider distributing workloads across multiple projects, implementing client-side request throttling, or contacting [Support](https://docs.cloud.google.com/support) for quota increases if needed for legitimate growth.  
551 | IAP enabled in multiple places | You can't enable IAP on both forwarding rule and backend service. Disable it on one location following the guidance in [Enable for Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto).  
700, 701 | Workforce pool provider issues | Configure exactly one provider for your workforce pool. Review [Workforce pools limitations](https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation#limitations-when-working-with-workforce-pools) for detailed requirements.  
705 | Missing OAuth client ID for workforce identity | Follow the complete setup process: first [create an OAuth client ID](https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation#create-oauth-client), then [update your IAP settings](https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation#update-iap-settings-wif).  
708 | Invalid workforce pool name | Verify your workforce pool exists and uses the correct format: `locations/global/workforcePools/WORKFORCE_POOL_ID`.  
4003 | Connection or firewall issue | Check that your VM process is running and listening on the expected port. Also verify that your [firewall rules](https://console.cloud.google.com/networking/firewalls/list) allow connections on that port.  
4010 | Connection closed by destination | [Reset](https://docs.cloud.google.com/compute/docs/samples/compute-reset-instance) the VM. If problems persist, examine `auth.log` (usually in `/var/log/`) or use the [serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console) for more detailed diagnostics.  
4033 | Permission, existence, or VM state issue | Confirm you have the Tunnel User role assigned for the resource through the [IAP page](https://console.cloud.google.com/security/iap), and verify the VM exists and is running.  
4047 | Instance doesn't exist or is stopped | Make sure your VM is powered on and has fully completed its startup sequence.  
  
If you're unable to resolve your issue, or you don't see your error listed on this page, then contact Cloud Customer Care with a description of the error and the response you get from a `GET` call to the API. Ensure that you remove your client secret from the response.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
