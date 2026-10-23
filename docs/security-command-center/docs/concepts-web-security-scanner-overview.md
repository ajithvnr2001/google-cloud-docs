---
url: https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview/
title: Overview of Web Security Scanner \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:51.525681+00:00
---

# Overview of Web Security Scanner  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of Web Security Scanner Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Web Security Scanner identifies security vulnerabilities and misconfigurations in your App Engine, Google Kubernetes Engine (GKE), and Compute Engine web applications. It crawls your application, following all links within the scope of your starting URLs, and attempts to exercise as many user inputs and event handlers as possible. Web Security Scanner only supports public URLs and IPs that aren't behind a firewall.

Web Security Scanner supports the App Engine standard environment and App Engine flexible environments, Compute Engine instances, and GKE resources.

Web Security Scanner is designed to complement your existing secure design and development processes. To avoid distracting you with false positives, Web Security Scanner errs on the side of under reporting and doesn't display low confidence alerts. It does not replace a manual security review, and it does not guarantee that your application is free from security flaws.

**Note:** Google may use aggregated and anonymized data to improve the performance of Web Security Scanner and to analyze web vulnerability trends. Google won't share information on specific issues or the security state of a scanned website with any third party.

Findings categorized as _misconfigurations_ represent issues that can be resolved through customer action by updating configurations. Although these findings are important for improving security posture, they are distinct from vulnerabilities, which represent actively exploitable weaknesses. You can view these misconfigurations on the **Findings** page of Security Command Center. For more information, see [Web Security Scanner misconfiguration findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#remediate-misconfiguration-findings).

**Caution** : Web Security Scanner can adversely affect the reliability of some applications and might not be suitable for use in a production environment. Also, Web Security Scanner cannot detect all possible vulnerabilities in an application. For more information, see the following:

  * [Usage caveats](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#usage_caveats)
  * [Best practices](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#best_practices)



## Scan types

[Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) provides managed and custom web vulnerability scanning for public App Engine, GKE, and Compute Engine serviced web applications.

### Managed scans

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Web Security Scanner managed scans are configured and managed by Security Command Center. Managed scans automatically run once each week to detect and scan public web endpoints. These scans don't use authentication and they send GET-only requests so they don't submit any forms on live websites.

Managed scans run separately from custom scans.

If Security Command Center is activated at the [organization level](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation), you can use managed scans to centrally manage basic web application vulnerability detection for projects in your organization, without having to involve individual project teams. When findings are discovered, you can work with those teams to set up more comprehensive custom scans.

When you enable Web Security Scanner as a service, managed scan findings are automatically available in the Security Command Center **Vulnerabilities** page and related reports. For information about how to enable Web Security Scanner managed scans, see [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).

Managed scans support only applications that use the default port, which is 80 for HTTP connections and 443 for HTTPS connections. If your application uses a non-default port, do a custom scan instead.

### Custom scans

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Web Security Scanner custom scans provide granular information about application vulnerability findings, like outdated libraries, cross-site scripting, or use of mixed content.

You define custom scans at the project level.

Custom scan findings are available in Security Command Center after you complete the guide to [set up Web Security Scanner custom scans](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans).

## Scan findings

This section describes Web Security Scanner finding types and relevant compliance standards.

**Note:** Attack path simulations don't support Web Security Scanner findings, so the findings don't get [attack exposure scores or attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).

### Detectors and compliance

Web Security Scanner supports categories in the [OWASP Top Ten](https://owasp.org/www-project-top-ten/), a document that ranks and provides remediation guidance for the top 10 most critical web application security risks, as determined by the Open Web Application Security Project (OWASP).

**Note:** The category [A09:2021 Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/) (previously **A10:2017 Insufficient Logging & Monitoring**) is not supported. This category describes insufficiencies that allow attackers to remain undetected. Unlike the other nine OWASP categories, it doesn't pertain to specific vulnerabilities that attackers can exploit. Similarly, Web Security Scanner can't attack web applications to provoke a detectable response. The issues included in this category require human judgment.

The compliance mapping is included for reference and is not provided or reviewed by the OWASP Foundation. It's only intended for you to monitor for compliance controls violations. The mappings are not provided for use as the basis of, or as a substitute for, the audit, certification, or report of compliance of your products or services with any regulatory or industry benchmarks or standards.

For more information about compliance, see [Assess and report security benchmark compliance](https://docs.cloud.google.com/security-command-center/docs/compliance-management).

### Finding types

Web Security Scanner [custom and managed scans](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#scan_types) identify the following finding types. 

Web Security Scanner custom and managed scans identify the following finding types. In the Standard-legacy tier, Web Security Scanner supports custom scans of deployed applications with public URLs and IPs that aren't behind a firewall.

Category | Finding description | Finding Category | OWASP 2017 Top 10 | OWASP 2021 Top 10  
---|---|---|---|---  
  
#### `Accessible Git repository`

Category name in the API: `ACCESSIBLE_GIT_REPOSITORY` |  A Git repository is exposed publicly. To resolve this finding, remove unintentional public access to the Git repository. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#accessible_repository) | Vulnerability | A5 | A01  
  
#### `Accessible SVN repository`

Category name in the API: `ACCESSIBLE_SVN_REPOSITORY` |  An SVN repository is exposed publicly. To resolve this finding, remove public unintentional access to the SVN repository. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#accessible_repository) | Vulnerability | A5 | A01  
  
#### `Accessible ENV File`

Category name in the API: `ACCESSIBLE_ENV_FILE` |  An ENV file is exposed publicly. To resolve this finding, remove public unintentional access to the ENV file. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#accessible_repository) | Vulnerability | A5 | A01  
  
#### `Cacheable password input`

Category name in the API: `CACHEABLE_PASSWORD_INPUT` |  Passwords entered on the web application can be cached in a regular browser cache instead of a secure password storage. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#cacheable_password_input) | Vulnerability | A3 | A04  
  
#### `Clear text password`

Category name in the API: `CLEAR_TEXT_PASSWORD` |  Passwords are being transmitted in clear text and can be intercepted. To resolve this finding, encrypt the password transmitted over the network. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#clear_text_password) | Vulnerability | A3 | A02  
  
#### `Insecure allow origin ends with validation`

Category name in the API: `INSECURE_ALLOW_ORIGIN_ENDS_WITH_VALIDATION` |  A cross-site HTTP or HTTPS endpoint validates only a suffix of the `Origin` request header before reflecting it inside the `Access-Control-Allow-Origin` response header. To resolve this finding, validate that the expected root domain is part of the `Origin` header value before reflecting it in the `Access-Control-Allow-Origin` response header. For subdomain wildcards, prepend the dot to the root domain—for example, `.endsWith(".google.com")`. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#insecure_allow_origin_ends_with_validation) | Vulnerability | A5 | A01  
  
#### `Insecure allow origin starts with validation`

Category name in the API: `INSECURE_ALLOW_ORIGIN_STARTS_WITH_VALIDATION` |  A cross-site HTTP or HTTPS endpoint validates only a prefix of the `Origin` request header before reflecting it inside the `Access-Control-Allow-Origin` response header. To resolve this finding, validate that the expected domain fully matches the `Origin` header value before reflecting it in the `Access-Control-Allow-Origin` response header—for example, `.equals(".google.com")`. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#insecure_allow_origin_starts_with_validation) | Vulnerability | A5 | A01  
  
#### `Invalid content type`

Category name in the API: `INVALID_CONTENT_TYPE` |  A resource was loaded that doesn't match the response's Content-Type HTTP header. To resolve this finding, set `X-Content-Type-Options` HTTP header with the correct value. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#invalid_content_type) | Vulnerability | A6 | A05  
  
#### `Invalid header`

Category name in the API: `INVALID_HEADER` |  A security header has a syntax error and is ignored by browsers. To resolve this finding, set HTTP security headers correctly. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#invalid_header) | Vulnerability | A6 | A05  
  
#### `Mismatching security header values`

Category name in the API: `MISMATCHING_SECURITY_HEADER_VALUES` |  A security header has duplicated, mismatching values, which result in undefined behavior. To resolve this finding, set HTTP security headers correctly. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#mismatching_security_header_values) | Vulnerability | A6 | A05  
  
#### `Misspelled security header name`

Category name in the API: `MISSPELLED_SECURITY_HEADER_NAME` |  A security header is misspelled and is ignored. To resolve this finding, set HTTP security headers correctly. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#misspelled_security_header_name) | Vulnerability | A6 | A05  
  
#### `Mixed content`

Category name in the API: `MIXED_CONTENT` |  Resources are being served over HTTP on an HTTPS page. To resolve this finding, make sure that all resources are served over HTTPS. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#mixed_content) | Vulnerability | A6 | A05  
  
#### `Outdated library`

Category name in the API: `OUTDATED_LIBRARY` |  A library was detected that has known vulnerabilities. To resolve this finding, upgrade libraries to a newer version. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#outdated_library) | Vulnerability | A9 | A06  
  
#### `Server side request forgery`

Category name in the API: `SERVER_SIDE_REQUEST_FORGERY` |  A server-side request forgery (SSRF) vulnerability was detected. To resolve this finding, use an allowlist to limit the domains and IP addresses that the web application can make requests to. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#server_side_request_forgery) | Vulnerability | Not applicable | A10  
  
#### `Session ID leak`

Category name in the API: `SESSION_ID_LEAK` |  When making a cross-domain request, the web application includes the user's session identifier in its `Referer` request header. This vulnerability gives the receiving domain access to the session identifier, which can be used to impersonate or uniquely identify the user. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#session_id_leak) | Vulnerability | A2 | A07  
  
#### `SQL injection`

Category name in the API: `SQL_INJECTION` |  A potential SQL injection vulnerability was detected. To resolve this finding, use parameterized queries to prevent user inputs from influencing the structure of the SQL query. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#sql_injection) | Vulnerability | A1 | A03  
  
#### `Struts insecure deserialization`

Category name in the API: `STRUTS_INSECURE_DESERIALIZATION` |  The use of a vulnerable version of [Apache Struts](https://struts.apache.org/) was detected. To resolve this finding, upgrade Apache Struts to the latest version. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#struts_insecure_deserialization) | Vulnerability | A8 | A08  
  
#### `XSS`

Category name in the API: `XSS` |  A field in this web application is vulnerable to a cross-site scripting (XSS) attack. To resolve this finding, validate and escape untrusted user-supplied data. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#xss) | Vulnerability | A7 | A03  
  
#### `XSS angular callback`

Category name in the API: `XSS_ANGULAR_CALLBACK` |  A user-provided string isn't escaped and AngularJS can interpolate it. To resolve this finding, validate and escape untrusted user-supplied data handled by Angular framework. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#xss_angular_callback) | Vulnerability | A7 | A03  
  
#### `XSS error`

Category name in the API: `XSS_ERROR` |  A field in this web application is vulnerable to a cross-site scripting attack. To resolve this finding, validate and escape untrusted user-supplied data. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#xss_error) | Vulnerability | A7 | A03  
  
#### `XXE reflected file leakage`

Category name in the API: `XXE_REFLECTED_FILE_LEAKAGE` |  An XML External Entity (XXE) vulnerability was detected. This vulnerability can cause the web application to leak a file on the host. To resolve this finding, configure your XML parsers to disallow external entities. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#xxe_reflected_file_leakage) | Vulnerability | A4 | A05  
  
#### `Prototype pollution`

Category name in the API: `PROTOTYPE_POLLUTION` |  The application is vulnerable to prototype pollution. This vulnerability arises when properties of the `Object.prototype` object can be assigned attacker-controllable values. Values planted on these prototypes are universally assumed to translate into cross-site scripting, or similar client-side vulnerabilities, as well as logic bugs. **Pricing tier** : [Premium or Standard](https://cloud.google.com/security-command-center/pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#prototype_pollution) | Vulnerability | A1 | A03  
  
#### `Hsts Misconfiguration`

Category name in the API: `HSTS_MISCONFIGURATION` |  A misconfigured HTTP Strict Transport Security (HSTS) header was detected. To significantly reduce the risk of downgrading and eavesdropping attacks on HTTP connections, resolve the misconfigured HSTS header. HSTS headers force connections through encrypted channels (TLS) so that plaintext HTTP connections fail. Find out [ more about HSTS headers build](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#hsts_misconfiguration) | Misconfiguration | Not applicable | Not applicable  
  
#### `Content Security Policy Header Missing`

Category name in the API: `CSP_MISSING` |  A missing Content Security Policy (CSP) HTTP response header was detected. CSP headers mitigate the exploitation of common web vulnerabilities, particularly cross-site scripting XSS, by preventing untrusted scripts or plugins from being loaded. A strict CSP header is recommended. Find out [ more about CSP headers build](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#csp_missing) | Misconfiguration | Not applicable | Not applicable  
  
#### `Content Security Policy Header Misconfigured`

Category name in the API: `CSP_MISCONFIGURATION` |  A misconfigured Content Security Policy (CSP) HTTP response header was detected. CSP headers mitigate the exploitation of common web vulnerabilities, particularly cross-site scripting XSS, by preventing untrusted scripts or plugins from being loaded. A strict CSP header is recommended. Learn [ more about CSP headers build](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#csp_misconfiguration) | Misconfiguration | Not applicable | Not applicable  
  
#### `Cross-Origin-Opener-Policy Header Missing`

Category name in the API: `COOP_MISSING` |  A missing Cross-Origin-Opener-Policy (COOP) HTTP header was detected. COOP is a web security mechanism that restricts a page opened in a new window from accessing the properties from its originating page. COOP offers a strong layer of protection against common web attacks. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#coop_missing) | Misconfiguration | Not applicable | Not applicable  
  
#### `Clickjacking Protection Missing`

Category name in the API: `CLICKJACKING_PROTECTION_MISSING` |  A missing response header was detected. To prevent clickjacking, implement an HTTP response header like an `X-Frame-Option` (XFO) or `Content-Security-Policy` (CSP). Clickjacking (also called UI Redress) is a web attack where attackers modify the interface of a target website so victims don’t realize they are taking an important action. Implementing an HTTP response header is recommended: XFO headers are easy to use; CSP headers provide more flexibility.  
[ \- Learn more about XFO headers build](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)   
[ \- Learn more about CSP headers build](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#clickjacking_protection_missing) | Misconfiguration | Not applicable | Not applicable  
  
## Usage caveats

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

Other important things to be aware of when using Web Security Scanner:

  * Because Web Security Scanner is undergoing continual improvements, a future scan might report issues that are not reported by the current scan.
  * Some features or sections of your application might not be tested.
  * Web Security Scanner attempts to activate every control and input it finds.
  * Web Security Scanner only supports websites using IPv4. Websites using IPv6 are not scanned.
  * If you expose state-changing actions for which your test account has permission, Web Security Scanner is likely to activate them. This might lead to undesirable results.
  * Web Security Scanner has a limit of 15 scans per project. Because scans are run concurrently, users who reach this limit are advised to add multiple starting URLs per scan, or to add scans to different projects that have not yet reached the limit.



## Who can run a security scan?

For information about the Identity and Access Management (IAM) roles that are available for Web Security Scanner, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

## How much time is required for a security scan?

The security scan does not execute immediately. It is queued and then executes later, possibly hours later depending on system load. After the scan starts to execute, the time it takes will depend on the size of your application. A scan of a large application with many URLs can take several hours, or even days. If a scan has not completed within 20 days, the scan is automatically stopped, and all crawl results and findings found during the scan will be visible as the scan result.

## Target restrictions

Web Security Scanner has filters in place that restrict scan targets to the specific App Engine instance for which the scan is created. Entering URLs for a different App Engine project or an outside domain will result in an error message.

**Important:** Attempting to subvert or in any way direct traffic to out-of-scope URLs is a violation of the [acceptable use policy](https://cloud.google.com/terms/aup).

Scans for Compute Engine and GKE are restricted to domains that map to static external IP addresses _reserved_ for the same project and static external IP addresses that belong to the same project. For instructions on reserving IP addresses for projects, see the following links:

  * Compute Engine: [Reserving a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address)

  * GKE: [Configuring domain names with static IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip)




App Engine does not provide a way to map static IP addresses to an application. However, you can use Cloud Load Balancing and serverless network endpoint groups to [reserve a static IP address for your load balancer](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-serverless-negs#ip-address), which then directs traffic to your application. For information about pricing, see [All networking pricing](https://cloud.google.com/vpc/network-pricing).

Within your project, the Web Security Scanner automatically _attempts_ to avoid logout URLs and other generic locations that may adversely affect a scan. However, to be sure, you can use the scan settings to manually [exclude URLs](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans#excluding_urls).

### Validation

Scan configurations are validated when they are created and before each scan. Web Security Scanner checks Security Command Center settings and your application's authentication credentials to ensure scans are configured correctly and can log into your application successfully. Configuration parameters, including maximum scan speed, are also checked to ensure they are within supported ranges.

You must resolve errors before a scan is created or updated. Applications that are changed after initial configuration may produce errors during scans. For example, if a domain no longer points to an IP address owned by the project, the resource is not scanned and an error is reported on the scan configuration page.

## Best practices

Because Web Security Scanner populates fields, pushes buttons, clicks links, and performs other user actions, you should use it with caution, particularly if you are scanning production resources. Web Security Scanner could potentially activate features that change the state of your data or system, with undesirable results.

For example:

  * In a blog application that allows public comments, Web Security Scanner might post test strings as comments on all your blog articles.
  * In an email sign-up page, Web Security Scanner might generate large numbers of test emails.



Following are some techniques that you can use, separately or in combination, to avoid unwanted outcomes:

  1. **Run scans in a test environment.** Set up a test environment by creating a separate App Engine project and loading your application and data there. If you use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), you can specify the target project as a command-line option when you upload your app.
  2. **Use a test account.** Create a user account that doesn't have access to sensitive data or harmful operations, and use it when scanning your app. Many applications present a special workflow during a user's first-time login, like accepting terms and creating a profile. Because of the different workflow, a test account for an initial user can have different scan results than an established user account. It's best to scan with an account that is in the normal user state, after the first-time flow is complete.
  3. **Block individual user interface elements** that you do not want activated by applying the CSS class `inq-no-click`. Event handlers that are attached to this element aren't activated during crawling and testing, regardless of whether they are inline JavaScript, or attached using `addEventListener`, or attached by setting the appropriate event handler property.
  4. **Use backup data.** Consider making a backup of your data before scanning.
  5. **Excluded URLs.** You can specify URL patterns that won't be crawled or tested. For information on syntax, see [Excluding URLs](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans#excluding_urls).



Before you scan, carefully audit your application for any feature that might affect data, users, or systems beyond the scope of your scan.

## What's next

  * Get started with the [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/how-to-use-web-security-scanner).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
