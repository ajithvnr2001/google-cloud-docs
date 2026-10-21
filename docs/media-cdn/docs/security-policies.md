---
url: https://docs.cloud.google.com/media-cdn/docs/security-policies/
title: Configure security policies \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:25:36.075744+00:00
---

# Configure security policies  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/security-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Configure security policies Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN uses Google Cloud Armor security policies to prevent unwelcome traffic from hitting its services. You can allow or deny requests based on the following:

  * IPv4 and IPv6 addresses and ranges (CIDRs)
  * Country code (geography)
  * Layer 7 filtering
  * [Google Threat Intelligence](https://docs.cloud.google.com/armor/docs/threat-intelligence) (requires the Google Cloud Armor Enterprise tier)
  * Autonomous System Numbers (ASNs)



These capabilities let you restrict content downloads to users in specific locations where you have content licensing restrictions, only allow corporate IP addresses to access testing or staging endpoints, and deny a list of known _bad_ client IP addresses.

Cloud Armor integrates with ASN to let you permit or block network traffic originating from specific ASNs. Cloud Armor edge security policies can use the ASN associated with the origin IP address, as determined by the network operator responsible for those IP prefixes, to control the flow of traffic.

You can decorate requests that Cloud Armor allows by inserting custom headers with configurable names and values.

Cloud Armor's integration with Google Threat Intelligence lets you control traffic from known malicious IP addresses and domains, providing advanced protection against threats.

**Note:** Cloud Armor security policies require additional allowlists during the current release of Media CDN. Contact your account team to enable this feature.**Warning:** Do not include confidential, sensitive, or personally identifiable information in your URL paths or query parameters. URLs, including host, path and query parameters, are treated as non-identifiable service data in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). As a privacy and security best practice, URL components should be opaque system-generated identifiers, not derived from end user input.

Cloud Armor security policies apply to all content served from Media CDN, including both cached content and cache misses.

Cloud Armor security policies are configured per Media CDN service—all requests destined for that service's IP address (or hostnames) have the security policy enforced consistently. Different services can have different security policies applied to them, and you can create multiple services for different geographies as needed.

For more fine-grained protection of content at a per-user level, we recommend using [signed URLs and signed cookies](https://docs.cloud.google.com/media-cdn/docs/signed-requests) in conjunction with a Cloud Armor policy.

Media CDN doesn't consider the `referer` header during rule evaluation of Layer 7 header filtering edge security policies when it's set to any of the following values:

  * Multiple URLs
  * A relative URL
  * A valid absolute URLs containing user information or a fragment component



## Configure security policies

Use the following instructions to configure a security policy.

### Before you begin

To attach a Cloud Armor security policy to a Media CDN service, ensure the following:

  * Be familiar with [Cloud Armor](https://docs.cloud.google.com/armor/docs/security-policy-overview).
  * Have [an existing Media CDN service](https://docs.cloud.google.com/media-cdn/docs/configuration) that you want to apply the policy to.
  * Optional, but recommended: enable logging on your Media CDN service so that you can identify blocked requests.



You also need the following Identity and Access Management permissions to authorize, create, and attach security policies to a Media CDN service:

  * `compute.securityPolicies.addAssociation`
  * `compute.securityPolicies.create`
  * `compute.securityPolicies.delete`
  * `compute.securityPolicies.get`
  * `compute.securityPolicies.list`
  * `compute.securityPolicies.update`
  * `compute.securityPolicies.use`



Users that need to attach an existing certificate to a Media CDN service only require these IAM permissions:

  * `compute.securityPolicies.get`
  * `compute.securityPolicies.list`
  * `compute.securityPolicies.use`



The `roles/networkservices.edgeCacheUser` role includes all of these permissions.

### Create a security policy

Cloud Armor security policies are composed of several _rules_ , with each rule defining a set of matching criteria (an _expression_) for a request, and an action. For example, an expression can contain matching logic for clients that are located in India, with the associated action being `allow`. If a request doesn't match the rule, Cloud Armor continues to evaluate the next rule, until all rules have been attempted.

Security policies have a _default rule_ with an `allow` action. The default rule allows requests that don't match preceding rules. This can be changed to a `deny` rule when you want to `allow` only requests that match preceding rules and reject all others.

The following example shows how to create a rule that blocks all clients geolocated to Australia with an HTTP 403, and allows all other requests.

###  gcloud 

To create a new policy of type `CLOUD_ARMOR_EDGE`, use the [`gcloud compute security-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/create):
    
    
    gcloud compute security-policies create block-australia \
        --type="CLOUD_ARMOR_EDGE" --project="PROJECT_ID"
    

This creates a policy with a default allow rule at the lowest priority (`priority: 2147483647`):
    
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/securityPolicies/block-australia].
    

Then you can add a rule with a higher priority:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy=block-australia --description "block AU" \
        --expression="origin.region_code == 'AU'" --action="deny-403"
    

The output is the following:
    
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/securityPolicies/block-australia].
    

###  Terraform 
    
    
    resource "google_compute_security_policy" "default" {
      name        = "block-australia"
      type        = "CLOUD_ARMOR_EDGE"
      description = "block AU"
    
      rule {
        action      = "deny(403)"
        description = "block AU"
        priority    = "1000"
        match {
          expr {
            expression = "origin.region_code == 'AU'"
          }
        }
      }
      rule {
        action   = "allow"
        priority = "2147483647"
        match {
          versioned_expr = "SRC_IPS_V1"
          config {
            src_ip_ranges = ["*"]
          }
        }
        description = "default rule"
      }
    }

If you inspect the policy, you see the two rules: the first rule blocks requests originating from Australia (`origin.region_code == 'AU'`) and the second, lowest priority rule, allows all traffic not matching the higher priority rule (or rules).
    
    
    kind: compute#securityPolicy
    name: block-australia
    rules:
    - action: deny(403)
      description: block AU
      kind: compute#securityPolicyRule
      match:
        expr:
          expression: origin.region_code == 'AU'
      preview: false
      priority: 1000
    - action: allow
      description: default rule
      kind: compute#securityPolicyRule
      match:
        config:
          srcIpRanges:
          - '*'
        versionedExpr: SRC_IPS_V1
      preview: false
      priority: 2147483647
      ruleNumber: '1'
    type: CLOUD_ARMOR_EDGE
    

### Add rules to a security policy

Cloud Armor security policies are sets of rules that match on Layer 7 attributes to help protect externally facing applications or services. Each rule is evaluated with respect to incoming traffic.

These attributes can be used for HTTP requests in security policies: `request.headers`, `request.method`, `request.path`, `request.scheme`, and `request.query`. For more information about writing expressions for security policy rules, see the [Cloud Armor custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference).

A Cloud Armor security policy _rule_ consists of a match condition and an action to take when that condition is met.

###  gcloud 

To create a rule for a security policy, use the [`gcloud compute security-policies rules create PRIORITY` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create). Replace `PRIORITY` with the priority of the rule in the policy:
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME \
        --description DESCRIPTION \
        --src-ip-ranges IP_RANGES | --expression EXPRESSION \
        --action=[ allow | deny-403 | deny-404 | deny-502 ] \
        --preview
    

### Attach a policy to a service

**Important:** Only security policies with a type of `CLOUD_ARMOR_EDGE` can be associated with a Media CDN service.

###  gcloud 

To attach an existing Cloud Armor policy to a Media CDN service, use the [`gcloud edge-cache services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/update):
    
    
    gcloud edge-cache services update SERVICE_NAME \
        --edge-security-policy=SECURITY_POLICY
    

### Update a rule in a security policy

Use these instructions to update a single rule in a Cloud Armor security policy. Alternatively, you can [atomically update multiple rules in a security policy](https://docs.cloud.google.com/armor/docs/manage-security-policies#atomic-update).

###  gcloud 

Use the [`gcloud compute security-policies rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/update):
    
    
    gcloud compute security-policies rules update PRIORITY [ \
        --security-policy POLICY_NAME  \
        --description DESCRIPTION  \
        --src-ip-ranges IP_RANGES  | --expression EXPRESSION \
        --action=[ allow | deny-403 | deny-404 | deny-502 ]  \
        --preview
      ]
      

For example, the following command updates a rule with priority 1111 to allow traffic from the IP address range 192.0.2.0/24:
    
    
    gcloud compute security-policies rules update 1111 \
        --security-policy my-policy \
        --description "allow traffic from 192.0.2.0/24" \
        --src-ip-ranges "192.0.2.0/24" \
        --action "allow"
    

To update the priority of a rule, you must use the REST API. For more information, see the [`securityPolicies.patchRule` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/patchRule).

### View a policy attachment

To review what policy is attached to an existing service, inspect (describe) that service.

###  gcloud 

To view the Cloud Armor policy that's attached to a Media CDN service, use the [`gcloud edge-cache services describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/describe):
    
    
    gcloud edge-cache services describe SERVICE_NAME
    

The `edgeSecurityPolicy` field of the service describes the attached policy:
    
    
    name: "SERVICE_NAME"
    edgeSecurityPolicy: "SECURITY_POLICY
    

### Remove a policy

To remove an existing policy, update the associated service and pass an empty string as the policy.

###  gcloud 

Use the [`gcloud edge-cache services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/update):
    
    
      gcloud edge-cache services update SERVICE_NAME \
          --edge-security-policy=""
    

The `edgeSecurityPolicy` field is now omitted from the output of the `gcloud edge-cache services describe SERVICE_NAME` command.

## Examples

Consider the following detailed example use cases.

### Example: Identify blocked requests

You must have [logging enabled](https://docs.cloud.google.com/media-cdn/docs/logging) for a given Edge Cache service for blocked requests to be logged.

Requests allowed or denied by a filtering policy are logged to Logging. To filter for rejected requests, the following [Logging query](https://docs.cloud.google.com/logging/docs/view/advanced-queries) for the `prod-video-service` configuration would look like:
    
    
    resource.type="edge_cache_service"
    jsonPayload.statusDetails="denied_by_security_policy"
    

### Example: Customize response codes

You can configure a Cloud Armor rule to return a specific status code as the action associated with a given rule. In most cases, it's best to return an HTTP `403 DENY` status code to clearly signal that the client was blocked by the rule.

The supported status codes are:

  * HTTP `403 Forbidden`
  * HTTP `404 Not Found`
  * HTTP `502 Bad Gateway`



The following example shows how to configure the returned status code:

To specify one of `[allow | deny-403 | deny-404 | deny-502]` as the action associated with the rule, run the following command. This example configures the rule to return an HTTP `502` status code.
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy=block-australia --description "block AU" \
        --expression="origin.region_code == 'AU'" --action="deny-502"
    

Each rule in a security policy can define a different status code response.

### Example: Deny clients outside of a country, except for allowed IP addresses

A common case in media serving is denying connections from clients that are outside of the region that you have content licenses or payment mechanisms for.

For example, you might want to only allow clients located in India, as well as any IP addresses that are in the allowlist, including those of content partners and your own employees, within the range `192.0.2.0/24`, and reject all others.

Using the [Cloud Armor custom rules language](https://docs.cloud.google.com/armor/docs/rules-language-reference#deny_traffic_from_a_specific_region), the following expression achieves this:
    
    
    origin.region_code == "IN" || inIpRange(origin.ip, '192.0.2.0/24')
    

This expression is configured as an `allow` rule, with a default `deny` rule configured to match all other clients. Security policies [always have a default rule](https://docs.cloud.google.com/armor/docs/security-policy-overview#default-rule). You typically configure this to `default deny` traffic that you don't explicitly allow. In other cases, you might choose to block some traffic and `default allow` all other traffic.

In the security policy output, note the following:

  * The highest priority (`priority: 0`) rule allows traffic from India _OR_ from the defined list of IP addresses.
  * The lowest priority rule represents a `default deny`. The rules engine denies all clients that higher priority rules don't evaluate to true.
  * You can combine multiple rules by using [boolean operators](https://docs.cloud.google.com/armor/docs/rules-language-reference#operations).



The policy allows traffic from clients in India, allows clients from a defined IP range, and _denies all other traffic_.

When you [view the details of the policy](https://docs.cloud.google.com/media-cdn/docs/security-policies#view-policy-attachment), the output resembles the following:
    
    
    kind: compute#securityPolicy
    name: allow-india-only
    type: "CLOUD_ARMOR_EDGE"
    rules:
    - action: allow
      description: ''
      kind: compute#securityPolicyRule
      match:
        expr:
          expression: origin.region_code == "IN" || inIpRange(origin.ip, '192.0.2.0/24')
      preview: false
      priority: 0
    - action: deny(403)
      description: Default rule, higher priority overrides it
      kind: compute#securityPolicyRule
      match:
        config:
          srcIpRanges:
          - '*'
        versionedExpr: SRC_IPS_V1
      preview: false
      priority: 2147483647
    

You can also set a [custom response header](https://docs.cloud.google.com/media-cdn/docs/custom-headers) with the `{region_code}` header variable. This header can be inspected by using JavaScript and reflected to the client.

### Example: Block traffic from known malicious IPs

The following [Cloud Armor custom rules language](https://docs.cloud.google.com/armor/docs/rules-language-reference#deny_traffic_from_a_specific_region) expression blocks traffic from IP addresses that are identified as malicious:
    
    
    evaluateThreatIntelligence('iplist-known-malicious-ips')
    

The expression directs Cloud Armor to check incoming requests against Google's constantly updated list of known malicious IP addresses and provides robust, automated protection.

To automatically block malicious IP addresses, you can configure your edge security policies with Google Threat Intelligence rules.

The following Google Cloud CLI commands show how to add a new Google Threat Intelligence rule to an existing policy, such as `my-edge-policy`:
    
    
      gcloud compute security-policies create my-edge-policy \
          --type=CLOUD_ARMOR_EDGE
    
      gcloud edge-cache services update my-edge-cache-service \
          --edge-security-policy "my-edge-policy"
    
      gcloud compute security-policies rules create 1000 \
          --security-policy "my-edge-policy" \
          --expression "evaluateThreatIntelligence('iplist-known-malicious-ips')" \
          --action "deny-403"
    

### Example: Block malicious clients by IP address and IP ranges

Using the [Cloud Armor custom rules language](https://docs.cloud.google.com/armor/docs/rules-language-reference#deny_traffic_from_a_specific_region), the following expression achieves this:
    
    
    inIpRange(origin.ip, '192.0.2.2/32') || inIpRange(origin.ip, '192.0.2.170/32')
    

You can block IP ranges up to a `/8` mask in IPv4 and a `/32` in IPv6. A common case for streaming platforms is blocking the egress IP ranges of proxies or VPN providers to minimize content licensing circumvention:
    
    
    inIpRange(origin.ip, '192.0.2.0/24') || inIpRange(origin.ip, '198.51.100.0/24') || inIpRange(origin.ip, '203.0.113.0/24') || inIpRange(origin.ip, '2001:DB8::B33F:2002/64')
    

Both IPv4 and IPv6 address ranges are supported.

### Example: Only allow a fixed list of geographies

If you have a list of country codes, you can use the boolean OR operator `||` to combine match conditions.

**Warning:** Don't use the logical AND operator `&&` to combine `origin.region_code` conditions. A client cannot be geo-located to two regions at once, and thus no client matches the condition. This results in _all_ clients being blocked.

Using the [Cloud Armor custom rules language](https://docs.cloud.google.com/armor/docs/rules-language-reference#deny_traffic_from_a_specific_region), the following expression allows users identified as coming from Australia or New Zealand:
    
    
    origin.region_code == "AU" || origin.region_code == "NZ"
    

This can additionally be combined with `origin.ip` or `inIpRange(origin.ip, '...')` expressions to allow testers, partners, and your corporate IP ranges, even if they aren't from one of the specified geographies.

There is a [documented number of subexpressions for each rule with a custom expression](https://docs.cloud.google.com/armor/quotas). If you need to combine more subexpressions, define multiple rules within a single policy.

### Example: Block clients from a specific set of countries

A less common example might be to block clients from a certain set of countries, but otherwise allow requests from all other countries.

To do this, you create a policy that _blocks_ both the country and any clients where their region cannot be determined, and then fall through to a default allow rule for all other requests.

**Note:** Clients who have a location that cannot be determined have a `region_code` of `ZZ`.

The following example describes a policy that blocks clients from Canada, as well as any clients where the location is unknown, but allows all other traffic:
    
    
      kind: compute#securityPolicy
      name: block-canada
      type: "CLOUD_ARMOR_EDGE"
      rules:
      - action: deny(403)
        description: ''
        kind: compute#securityPolicyRule
        match:
          expr:
            expression: origin.region_code == "CA" || origin.region_code == "ZZ"
        preview: false
        priority: 0
      - action: allow
        description: Default rule, higher priority overrides it
        kind: compute#securityPolicyRule
        match:
          config:
            srcIpRanges:
            - '*'
          versionedExpr: SRC_IPS_V1
        preview: false
        priority: 2147483647
    

### Example: Deny requests for cached content with specific headers

An [edge security policy](https://docs.cloud.google.com/armor/docs/security-policy-overview#edge-policies) applies to all requests targeting any Media CDN service that the policy is attached to. This policy enforcement takes place before any cache lookup. Requests that are not allowed by the edge security policy are denied with the configured status code.

The following expression matches against requests from the IP address `1.2.3.4` that contain the string `user1` in the `user-agent` header:
    
    
    inIpRange(origin.ip, '1.2.3.4/32') && request.headers['user-agent'].contains('user1')
    

The following command adds the filtering rule `105` to the edge security policy `my-edge-policy`, which is attached to a Media CDN service:
    
    
    gcloud compute security-policies rules create 105 \
        --security-policy "my-edge-policy" \
        --expression = "inIpRange(origin.ip, '1.2.3.4/32') && request.headers['user-agent'].contains('charlie')" \
        --action= deny-403 \
        --description="block requests from IP addresses in which the user-agent header contains the string charlie"
        

## Logging enforcement actions

Each [request log](https://docs.cloud.google.com/media-cdn/docs/logging) provides details about which security policy was applied and whether the request was allowed (`ALLOW`) or rejected (`DENY`).

To enable logging, ensure that `logConfig.enable` is set to `true` on your service. Services without logs enabled don't log security policy events.

When a client is located outside the United States and a security policy called `deny-non-us-clients` is in force that denies requests that originate outside the US, this is the log entry for a denied request:
    
    
    enforcedSecurityPolicy:
      name: deny-non-us-clients
      outcome: DENY
    

Services with no Cloud Armor policy attached contain `no_policy` as the value of `enforcedSecurityPolicy.name` and an `outcome` of `ALLOW`. For example, a [request log](https://docs.cloud.google.com/media-cdn/docs/logging) entry for a service without a policy attached has the following values:
    
    
    enforcedSecurityPolicy:
      name: no_policy
      outcome: ALLOW
    

## Understand GeoIP classifications

Media CDN relies on Google's internal IP classification data-sources to derive a location (region, state, province, or city) from an IP address. If you are migrating from, or splitting traffic between, multiple providers, a small number of IP addresses might sometimes be associated with different locations.

  * Cloud Armor uses [ISO 3166-1 alpha 2](https://www.wikipedia.org/wiki/ISO_3166-1_alpha-2) region codes to associate a client to a geographic location.
  * For example, `US` for the United States, or `AU` for Australia.
  * In some cases, a region corresponds to a country, but this is not always the case. For example, the `US` code includes all states of the United States, one district, and six outlying areas.
  * For more information, see [unicode_region_subtag](http://www.unicode.org/reports/tr35/#unicode_region_subtag) in the Unicode Technical Standard.
  * For clients where the location cannot be derived, the `origin.region_code` is set to `ZZ`.



You can add [geographic data to response headers](https://docs.cloud.google.com/media-cdn/docs/custom-headers) to an Media CDN endpoint (with `routing.routeRules[].headerActions[].responseHeadersToAdd[]`) or reflect the geographic data provided to a [Cloud Function](https://docs.cloud.google.com/functions) to validate any differences between geoIP data sources during initial integration and testing.

Additionally, Media CDN request logs include the `clientRegion` and other client-specific data that you can validate against your existing data sources.

## What's next

  * Learn how to use [signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests) to authorize content on a per-user basis.
  * Review the [Cloud Armor rules reference](https://docs.cloud.google.com/armor/docs/rules-language-reference) to understand how IP and geographic matching rules can be expressed and combined together.
  * Visit the [logging documentation](https://docs.cloud.google.com/media-cdn/docs/logging) to understand how to query request logs and check which requests have been blocked.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
