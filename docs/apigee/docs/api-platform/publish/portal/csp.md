---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/csp/
title: Configure a content security policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:12.767715+00:00
---

# Configure a content security policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/csp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure a content security policy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Configure a content security policy (CSP) for all pages in your portal to protect against cross-site scripting (XSS) and other code-injection attacks. The CSP defines trusted sources for content such as scripts, styles, and images. After configuring a policy, content loaded from untrusted sources will be blocked by your browser.

The CSP is added as a `Content-Security-Policy` HTTP response header to all pages in your portal, as follows:

`Content-Security-Policy: _policy_`

You define the policy using directives, as defined in [ Content Security Policy Directives](https://www.w3.org/TR/CSP3/#csp-directives) in the W3C site.

If you enable the CSP header, by default the following CSP directive is defined:

`default-src 'unsafe-eval' 'unsafe-inline' * data:`

The `default-src` directive configures the default policy for resource types that do not have a configured directive.

Apigee recommends that you define a default directive as part of the CSP to configure the minimum restrictions.

The following table describes the policies defined as part of the default directive.

Policy | Access  
---|---  
`'unsafe-inline'` | Inline resources, such as inline `<script>` elements, `javascript:` URLs, inline event handlers, and inline `<style>` elements. **Note** : You must enclose the policy in single quotes.  
`'unsafe-eval'` | Unsafe dynamic code evaluation such as JavaScript `eval()` and similar methods used to create code from strings. **Note** : You must enclose the policy in single quotes.  
`* (wildcard)` | Any URL except `data:`, `blob:`, and `filesystem:` schemes.  
`data:` | Resources loaded via the data scheme (for example, Base64-encoded images).  
  
The following provides examples of configuring the CSP to restrict specific resource types.

Policy | Access  
---|---  
`default-src 'none'` | No access for resource types that do not have a configured directive.  
`img-src *` | Image URL from any source.  
`media-src https://example.com/` | Video or audio URL over HTTPS from the `example.com` domain.  
`script-src *.example.com` | Execution of any script from a subdomain of `example.com`.  
`style-src 'self' css.example.com` | Application of any style from the site's origin or the `css.example.com` domain.  
  
To configure a content security policy:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click your portal.

  3. Click **Settings** in the navigation menu.

  4. Click the **Security** tab.

  5. Click **Enable content security policy**.

  6. Configure the CSP or leave the default.

  7. Click **Save**.




You can restore the default CSP policy at any time by clicking **Restore default**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
