---
url: https://docs.cloud.google.com/armor/docs/rate-limiting-overview/
title: Rate limiting overview \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:12.490207+00:00
---

# Rate limiting overview  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/rate-limiting-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Rate limiting overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor provides capabilities to help protect your Google Cloud applications against a variety of Layer 3 and Layer 7 attacks. Rate-based rules help you protect your applications from a large volume of requests that flood your instances and block access for legitimate users.

Rate limiting can do the following:

  * Prevent any particular client from exhausting application resources.
  * Protect your application instances from erratic and unpredictable spikes in the rate of client requests.



In addition, when a resource is presented with a high volume of traffic from a small number of clients, you can prevent your other clients from being affected by large spikes of traffic from that small number of clients, enabling your resources to handle as many requests as possible.

Cloud Armor has two types of rate-based rules:

  * **Throttle**. You can enforce a maximum request limit per client or across all clients by throttling individual clients to a user-configured threshold.
  * **Rate-based ban**. You can rate limit requests that match a rule on a per-client basis and then temporarily ban those clients for a configured period of time if they exceed a user-configured threshold.



When you configure a rule with a rate-based ban action, you can't change it to a throttle action later. However, when you configure a rule with a throttle action, you can change it to a rate-based ban action later. For more information, see [Change a throttle rule to a rate-based ban rule](https://docs.cloud.google.com/armor/docs/configure-rate-limiting#change-rule-action).

Cloud Armor applies the rate limiting threshold to each associated backend. For example, if you have two backend services and you configure a rate limiting rule with a threshold of 1,000 requests per minute, then each backend service can receive 1,000 requests per minute before Cloud Armor applies the rule action.

You can preview the effects of rate limiting rules in a security policy by using preview mode and examining your request logs.

## Identifying clients for rate limiting

Cloud Armor identifies individual clients for rate limiting by using the following key types for aggregating requests and enforcing rate limits:

  * **ALL** : a single key for all requests that satisfy the rule match condition.
  * **IP** : a unique key for each client IP address whose requests satisfy the rule match condition.
  * **HTTP_HEADER** : a unique key for each unique HTTP header value whose name is configured. The key value is truncated to the first 128 bytes of the header value. The key type defaults to ALL if no such header is present, or if you attempt to use this key type with an external proxy Network Load Balancer.
  * **XFF_IP** : a unique key for each original client IP address, that is, the first IP address in the list of IPs specified in the `X-Forwarded-For` HTTP header. The key type defaults to IP address if no such header is present, if the value is not a valid IP address, or if you attempt to use this key type with an external proxy Network Load Balancer.
  * **HTTP_COOKIE** : a unique key for each HTTP cookie value whose name is configured. The key value is truncated to the first 128 bytes of the cookie value. The key type defaults to ALL if no such cookie is present, or if you attempt to use this key type with an external proxy Network Load Balancer.
  * **HTTP_PATH** : the URL path of the HTTP request. The key value is truncated to the first 128 bytes.
  * **SNI** : the server name indication in the TLS session of the HTTPS request. The key value is truncated to the first 128 bytes. The key type defaults to ALL on an HTTP session.
  * **REGION_CODE** : the country or region from which the request originates.
  * **TLS_JA4_FINGERPRINT** : JA4 TLS/SSL fingerprint if the client connects using `HTTPS`, `HTTP/2` or `HTTP/3`. If not available, the key type defaults to ALL. For more information about JA4, see the [rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes).
  * **TLS_JA3_FINGERPRINT** : JA3 TLS/SSL fingerprint if the client connects using `HTTPS`, `HTTP/2` or `HTTP/3`. If not available, the key type defaults to ALL.
  * **USER_IP** : The IP address of the originating client, included in the headers configured under `userIpRequestHeaders` and whose value is filled by an upstream proxy. If there is no `userIpRequestHeaders` configuration, or an IP address cannot be resolved from it, the key type defaults to IP. For more information, see the [rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes).
  * **ASN** : The Autonomous System Number of the originating client. If the ASN is not available, the key type defaults to ALL.



You can use the preceding keys individually, or you can apply rate limiting based on a combination of up to three keys. You can use multiple `HTTP-HEADER` or `HTTP-COOKIE` keys, and only one of each other key type. For more information, see [Rate limiting based on multiple keys](https://docs.cloud.google.com/armor/docs/configure-rate-limiting#multiple-keys).

**Note:** The rate-limiting key data is classified as service data, which is processed as described in [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). Rate-limiting key data isn't treated as [customer data](https://cloud.google.com/terms/data-processing-addendum). If your workload is subject to regulatory regimes or other compliance requirements that necessitate [access transparency or access approval](https://cloud.google.com/security/products/access-transparency), review the key types whose values might contain sensitive information.

## Choose between rate based ban and throttle rate limiting rules

Cloud Armor `rate-based ban` and `throttle` rate limiting rules differ in how they handle traffic exceeding the configured threshold.

  * `rate_based_ban`: when the rate of requests exceeds the defined threshold, Cloud Armor blocks all further requests from the source or target of those requests for a specified period.
  * `throttle`: instead of blocking all traffic, throttling limits the rate of requests to a defined maximum. Throttling allows some traffic to pass through, but at a controlled rate that prevents overload.



The most appropriate rule depends on your specific needs and the type of traffic you're dealing with. For example, if you're facing a DDoS attack, a rate-based ban might be more appropriate to quickly block the malicious traffic. Alternatively, if you're experiencing a sudden surge in legitimate traffic, throttling might be a better option to maintain service availability while preventing overload.

### Throttling traffic

The `throttle` action in a rule lets you enforce a per-client request threshold to protect backend services. This rule enforces the threshold to limit traffic from each client that satisfies the match conditions in the rule. The threshold is configured as a specified number of requests in a specified time interval.

For example, you might set the request threshold to 2,000 requests within 1,200 seconds (20 minutes). If a client sends 2,500 requests within any 1,200 second period, approximately 20% of the client's traffic is throttled until the permitted request volume is at or below the configured threshold.

When a client's traffic rate is under or equal to the `rate_limit_threshold_count`, requests follow the `conform_action`, which is always an `allow` action. The request is allowed through the security policy and permitted to reach its destination. When a client's traffic rate exceeds the specified `rate_limit_threshold_count`, Cloud Armor applies the `exceed_action`, which can be either `deny` or `redirect`, for requests over the limit for the rest of the threshold interval.

You set these parameters to control the action:

  * `rate_limit_threshold_count`: the number of requests per client allowed within a specified time interval. The minimum value is 1 and the maximum value is 1,000,000. 
    * `interval_sec`: the number of seconds in the time interval. The value must be 10, 30, 60, 120, 180, 240, 300, 600, 900, 1200, 1800, 2700, or 3600 seconds.
  * `exceed_action`: when a request exceeds the `rate_limit_threshold_count`, Cloud Armor applies the configured `exceed_action`. Possible values for the `exceed_action` follow: 
    * `deny(status)`: the request is denied and the specified status code is returned. Valid values are `403 Forbidden`, `404 Page Not Found`, `429 Too Many Requests`, and `502 Bad Gateway`. We recommend using the `429 Too Many Requests` status code.
    * `redirect`: the request is either redirected for reCAPTCHA assessment or to a different URL, based on the `exceed_redirect_options` parameter.
  * `exceed_redirect_options`: when the `exceed_action` is `redirect`, use this parameter to specify the redirect action: 
    * `type`: type for the redirect action, either `GOOGLE_RECAPTCHA` or `EXTERNAL_302`.
    * `target`: URL target for the redirect action. Only applicable when the `type` is `EXTERNAL_302`.
  * `conform_action`: the action performed when the number of requests is under the `rate_limit_threshold_count`. This action is always an `allow` action.



### Banning clients based on request rates

The `rate_based_ban` action in a rule lets you enforce a per-client threshold to temporarily ban clients that exceed the limit by applying the configured `exceed_action` for all requests from the client for a configurable time period. The threshold is configured as a specified number of requests in a specified time interval. You can temporarily ban traffic for a user-configured time period (`'ban_duration_sec'`), provided that the traffic matches the specified match condition and exceeds the configured threshold.

For example, you might set the request threshold to 2,000 requests within 1,200 seconds (20 minutes). If a client sends 2,500 requests within any 1,200 seconds, Cloud Armor applies the `exceed_action` to traffic from that client exceeding the 2,000 request threshold until the full 1,200 seconds has elapsed and for an additional number of seconds that you set as the ban duration period. If the ban duration period is set to `3600`, for example, traffic from the client would be banned for 3,600 seconds (one hour) beyond the end of the threshold interval.

When a client's request rate is under the rate limit threshold, the request can immediately proceed to the backend service. When a client's traffic rate exceeds the specified `rate_limit_threshold_count`, Cloud Armor applies the `exceed_action` to all incoming requests from the client for the rest of the threshold interval and for the next `ban_duration_sec` seconds, whether or not the threshold is exceeded.

With this configuration, it is possible to accidentally ban welcome clients that only occasionally exceed the allowable request rate. To prevent this, and ban only clients that frequently exceed the request rate, you can optionally track the total client requests against an additional, preferably longer, threshold configuration called the `ban_threshold_count`. In this mode, the client is banned for the configured `ban_duration_sec` only if the request rate crosses the configured `ban_threshold_count`. If the request rate doesn't exceed the `ban_threshold_count`, the requests keep getting throttled to `rate_limit_threshold_count`. For the purpose of `ban_threshold_count`, the total requests from the client, consisting of all incoming requests before throttling, are counted.

These parameters control the action of a `rate_based_ban` rule:

  * `rate_limit_threshold_count`: the number of requests per client allowed within a specified time interval. The minimum value is 1 request and the maximum value is 10,000 requests. 
    * `interval_sec`: the number of seconds in the time interval. The value must be 10, 30, 60, 120, 180, 240, 300, 600, 900, 1200, 1800, 2700, or 3600 seconds.
  * `exceed_action`: when a request exceeds the `rate_limit_threshold_count`, Cloud Armor applies the configured `exceed_action`. Possible values for the `exceed_action` are as follows: 
    * `deny(status)`: the request is denied and the specified status code is returned. Valid values are `403 Forbidden`, `404 Page Not Found`, `429 Too Many Requests`, and `502 Bad Gateway`. We recommend using the status code `429 Too Many Requests`.
    * `redirect`: the request is either redirected for reCAPTCHA assessment or to a different URL, based on the `exceed_redirect_options` parameter.
  * `exceed_redirect_options`: when the `exceed_action` is `redirect`, use this parameter to specify the redirect action: 
    * `type`: the type for the redirect action, either `GOOGLE_RECAPTCHA` or `EXTERNAL_302`.
    * `target`: the URL target for the redirect action. This URL target is only applicable when the `type` is `EXTERNAL_302`.
  * `conform_action`: the action performed when the number of requests is under the `rate_limit_threshold_count`. This action is always an `allow` action.
  * `ban_threshold_count`: the number of requests per client allowed within a specified time interval, over which Cloud Armor bans requests. If specified, the key is banned for the configured `ban_duration_sec` when the number of requests that exceed the `rate_limit_threshold_count` also exceed this `ban_threshold_count`. 
    * `ban_threshold_interval_sec`: the number of seconds in the time interval for your `ban_threshold_count`. The `ban_threshold_interval_sec` value must be 10, 30, 60, 120, 180, 240, 300, 600, 900, 1200, 1800, 2700, or 3600 seconds.
  * `ban_duration_sec`: the additional number of seconds for which a client is banned after the `interval_sec` period elapses. The `ban_duration_sec` value must be 60, 120, 180, 240, 300, 600, 900, 1200, 1800, 2700, or 3600 seconds.



## Default rate limiting security policy

When you configure a [default security policy](https://docs.cloud.google.com/armor/docs/security-policy-overview#about) during load balancer creation, the default threshold is 500 requests during each one-minute interval (a `rate_limit_threshold_count` and `interval_sec` of `500` and `60`, respectively). If you want to select a different threshold, we recommend that you use the following steps to tune your parameters:

  1. Enable [Cloud Logging](https://docs.cloud.google.com/armor/docs/request-logging) and query the maximum number of requests that arrived per IP address and per minute over a day or longer at your Cloud Armor-protected backend service.

For example, suppose that you believe that 99% of the network traffic that you receive isn't impacted by the rate limit rule. In this scenario, we recommend that you set your rate limit threshold to the 99th percentile of the maximum number of requests per IP address and per minute of the distribution that is generated from the Cloud Logging data.

  2. If you still notice default rate limit rules blocking legitimate traffic, consider the following additional steps:

     1. Enable caching (Cloud CDN or Media CDN).
     2. Increase throttle time interval (requests received per several minutes, instead of per 60 seconds).
     3. You can ban clients to reduce attack impact further after the initial wave. The Cloud Armor `rate_based_ban` action lets you ban all clients that exceed the limits too many times within a user-specified window. For example, clients that exceed the limits 10 times within a minute can be banned for 15 minutes.



## Threshold enforcement

The configured thresholds for throttling and rate-based bans are enforced independently in each of the Google Cloud regions where your HTTP(S) backend services are deployed. For example, if your service is deployed in two regions, each of the two regions applies the configured rate limit threshold to each key, so your backend service might experience cross-region aggregated traffic volumes that are twice the configured threshold. If the configured threshold is set to 5,000 requests, the backend service might receive 5,000 requests from one region and 5,000 requests from the second region.

However, for the key type IP address, it is reasonable to assume that traffic from the same client IP address is directed to the region that is closest to the region where your backends are deployed. In this case, rate limiting can be considered to be enforced at a backend service level, regardless of the regions in which it is deployed.

It is important to note that the enforced rate limits are approximate and might not be strictly accurate compared to the configured thresholds. Also, in rare cases, because of internal routing behavior, it is possible that rate limiting might be enforced in more regions than the regions you are deployed in, thus impacting accuracy. For these reasons, we recommend that you use rate limiting only for abuse mitigation or maintaining application and service availability, not for enforcing strict quota or licensing requirements.

Rate limiting based on REGION_CODE considers the region where the request originates from and doesn't consider the region of the backends in the backend service, regardless of their type. Backends include instance groups, any type of network endpoint group (NEG) supported by the load balancers, and Cloud Storage buckets. Supported backends can be found in [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview).

## Logging

Cloud Logging records the security policy name, matched rate limit rule priority, rule ID, the associated action, and other information in your request logs. For more information about logging, see [Use request logging](https://docs.cloud.google.com/armor/docs/request-logging).

## Integration with reCAPTCHA

You can apply rate limiting to some reCAPTCHA resources in order to mitigate token abuse and limit token reuse. These resources include action tokens, session tokens, and exemption cookies. For more information about using rate limiting with reCAPTCHA, see the [bot management overview](https://docs.cloud.google.com/armor/docs/bot-management#rate-limiting).

## Custom error responses

You can apply custom error responses to Cloud Armor rate limiting, including `throttle` and `rate_based_ban` traffic. When these limits are enforced, custom error messages are sent to end users. In addition, when you use a global external Application Load Balancer, you can configure custom error responses for specific HTTP status codes generated by load balancers or backend instances.

For more information about custom error responses, see the [Custom error response overview](https://docs.cloud.google.com/load-balancing/docs/https/custom-error-response). To configure custom error responses, see [Configure custom error responses](https://docs.cloud.google.com/load-balancing/docs/https/configure-custom-error-responses). 

## Cloud Armor with Cloud Service Mesh

**Note:** The `fairshare` rate limiting action is only available for rules in internal service security policies.

You can configure internal service security policies for your service mesh to enforce global server-side rate limiting per client, helping you fairly share your service's available capacity and mitigating the risk of malicious or misbehaving clients overloading your services. You attach a security policy to a Cloud Service Mesh endpoint policy to enforce rate limiting on inbound traffic on the server-side. However, you can't configure a Cloud Armor security policy if you are using TCP traffic routing. For more information about using Cloud Armor with Cloud Service Mesh, see [Configure rate limiting with Cloud Armor](https://docs.cloud.google.com/service-mesh/docs/service-routing/rate-limiting-overview).

## What's next

  * [Configure rate limiting](https://docs.cloud.google.com/armor/docs/configure-rate-limiting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
