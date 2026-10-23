---
url: https://docs.cloud.google.com/secure-web-proxy/docs/tls-rule-evaluation/
title: Rule evaluation order \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:25.758978+00:00
---

# Rule evaluation order  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/tls-rule-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Rule evaluation order Stay organized with collections  Save and categorize content based on your preferences. 

Rule evaluation determines whether a web request should be allowed or denied by using the rules that you set in your policy. It considers the following attributes to make its decisions:

  * **Priority of a rule:** Lower integers indicate higher priorities.
  * **SessionMatcher:** Matches against the following session level attributes: 
    * IP address of the source machine
    * Service account of the source machine
    * Secure Tag of the source machine
    * Hostname of the target machine
  * **ApplicationMatcher:** Matches against the following HTTP request attributes: 
    * URL
    * Path
    * Request headers



For a list of all the `SessionMatcher` and `ApplicationMatcher` attributes, see [Available attributes in `SessionMatcher` and `ApplicationMatcher`](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference?cloudshell=false#available-attributes-in-sessionmatcher-and-applicationmatcher).

## How rule evaluation works

The rules are evaluated in the following order:

  1. High-priority rules are evaluated first.
  2. The highest priority rule that matches the `SessionMatcher` and `ApplicationMatcher` attributes determines the action to be taken on the traffic.
  3. If the request does not match the `SessionMatcher` and `ApplicationMatcher` attributes of that rule, the next rule with the highest priority is evaluated.
  4. This process continues until a rule is found that matches the request, or all the rules have been evaluated. If no match is found, the request is denied.



## Before you configure TLS inspection

You must understand the following rule-evaluation scenarios _before_ you configure TLS inspection:

  * A client can send an HTTP request to the proxy server. The request is then evaluated by using all the available data, including the hostname, source identity, HTTP headers, and path.

If the request is allowed, the HTTP traffic is sent to the destination. However, if the request is denied, the HTTP traffic is not allowed to pass.

  * A client can send the proxy an HTTP CONNECT request to establish a TCP tunnel to the destination. This is done when the client wants to send arbitrary TCP traffic or establish an end-to-end TLS connection with the destination through the proxy, as with HTTPS.

  * If a rule has a matching `SessionMatcher` attribute and does not contain an `ApplicationMatcher` attribute, and the rule evaluation results in allowing the traffic, then a tunnel to the destination is established and the traffic is TCP-proxied. This applies to HTTPS and TCP traffic.

  * If higher priority rules are unable to determine the action to be taken on a request, then the rule evaluation continues. If the evaluation proceeds to a rule with an `ApplicationMatcher` attribute, then the tunneled traffic is interpreted as HTTP or HTTPS.

If the underlying data is not HTTP or HTTPS, then the connection fails.

If the underlying data is HTTP, then the requests are evaluated, including the hostname, source identity, HTTP headers, and path. Based on the evaluation result, the traffic is either allowed or denied.

  * For HTTPS traffic, a rule is evaluated only if it has the TLS inspection flag enabled; otherwise, that rule is skipped.

  * For HTTPS traffic, a rule is inspected only if the following conditions are true:

    * The TLS inspection flag is enabled.
    * Traffic matches the `SessionMatcher` attributes.



## Recommendations for configuring TLS inspection rules

  * If you want to allow TCP traffic, then the rule that allows TCP traffic must have a higher priority than the rules that allow HTTP traffic.
  * Rules with the `ApplicationMatcher` attribute should be tightly scoped by using the `SessionMatcher` attribute to minimize the interpretation of unrelated flows as HTTP.
  * Rules that allow TLS (including HTTPS) traffic but do not perform TLS inspection can be interpreted as TCP proxy rules.
  * To avoid unnecessary TLS inspection of traffic, TLS inspection rules should be lower in priority than non-TLS inspection rules. Alternatively, to _fail fast_ for non-matching traffic, TLS inspection rules should be tightly scoped by using the `SessionMatcher` attribute.



## Examples of TLS inspection rule configurations

Consider the two rules in the following examples.

### Example 1

In this example, we assume the presence of other lower priority rules. Consider the following two rules:

  * Rule 1
        
        description: do not allow POST requests
        priority: 10
        basicProfile: DENY
        sessionMatcher: true
        tlsInspectionEnabled: true
        applicationMatcher: request.method == 'POST'
        

  * Rule 2
        
        description: allow TCP proxying from tag 12345 to example.com
        priority: 20
        basicProfile: ALLOW
        sessionMatcher: source.matchTag('tagValues/12345') && host() == 'example.com'
        




In this example, Secure Web Proxy interprets the two rules as follows:

  * Allowing TCP traffic but disallowing a specific type of HTTP request is mutually exclusive because the TCP traffic can contain a POST request.
  * Traffic in rule 2 is never allowed. It is denied because the traffic from tag 12345 to example.com is intercepted and interpreted as HTTP to evaluate the HTTP method.
  * For rule 2 to take effect, you can use either of the following solutions:

    * Recommended: Increase the priority of rule 2 to a higher level (priority: 5).
    * Scope rule 1 to avoid overlapping the allowed traffic with its `SessionMatcher` attribute:

`sessionMatcher: !(source.matchTag('tagValues/12345') && host() == 'example.com')`

We do not recommend this solution because it becomes difficult to maintain many overlapping rules.




### Example 2

Consider the following two rules:

  * Rule 1
        
        description: allow to specific GitHub repository (TLS inspect to match specific path)
        priority: 10
        basicProfile: ALLOW
        sessionMatcher: true
        tlsInspectionEnabled: true
        applicationMatcher: request.url().startsWith('github.com/grpc/grpc')
        

  * Rule 2
        
        description: allow TCP proxying from tag 12345 to example.com
        priority: 20
        basicProfile: ALLOW
        sessionMatcher: host() == 'bankofamerica.com'
        




In this example, Secure Web Proxy interprets the two rules as follows:

  * All traffic, including that destined for `bankofamerica.com`, is inspected for TLS to match the `request.url()` of the high priority rule 1.
  * To avoid TLS inspection in rule 2, you can use either of the following solutions:

    * Increase the priority of rule 2 to a higher level (priority: 5). As a result, rule 2 is applied before evaluating rule 1, and traffic from `bankofamerica.com` is allowed without being TLS inspected.
    * Recommended: Narrow the scope of rule 1 to allow TLS inspection specifically for the `github.com` domain. To narrow the scope, add a targeted `sessionMatcher` attribute:

`sessionMatcher: host() == 'github.com'`




## Limitations

You must consider these limitations _before_ configuring TLS inspection:

  * Servers are only verified by using public root certificates. The root certificate authority (CA) set is based on the [Mozilla Root Program](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/policy/). The behavior of certificate verification is subject to change and corresponds to how web browsers verify certificates.

Because backend verification is not possible at this time, traffic to servers with private or self-signed certificates cannot be intercepted.

  * Secure Web Proxy does not run certificate revocation list (CRL) checks.

  * For TLS inspection to work, clients must currently send Server Name Indication (SNI). SNI is a TLS specification extension that is optional, but most clients enable it by default.

  * TLS inspection does not work if the client requires [Encrypted Client Hello (ECH)](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/) (formerly known as Encrypted SNI).

ECH is a draft IETF standard that allows clients to encrypt the beginning of the TLS handshake by using a pre-established server key. Because TLS inspection is acting as an intercepting proxy, it does not have access to that pre-established server key. As a result, ECH does not function.

  * Clients must be configured to trust your private root certificate.

  * If you remove CAs from your private CA pool, you are served cached certificates signed by that CA for up to 28 hours. To prevent using the cached certificates, you can update your TLS inspection policy to point to a new CA pool. As a result, Secure Web Proxy is forced to generate new certificates.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
