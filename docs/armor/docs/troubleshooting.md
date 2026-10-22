---
url: https://docs.cloud.google.com/armor/docs/troubleshooting/
title: Troubleshoot Cloud Armor issues \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:28.804330+00:00
---

# Troubleshoot Cloud Armor issues  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Troubleshoot Cloud Armor issues Stay organized with collections  Save and categorize content based on your preferences. 

Use these instructions to troubleshoot issues with Google Cloud Armor security policies.

## General issues

This section covers common issues encountered when using Cloud Armor.

### Debugging security policies

If you need additional information about what particular event triggers preconfigured rules, read [Using request logging](https://docs.cloud.google.com/armor/docs/request-logging), and then enable verbose logging. Cloud Logging records a higher level of detail in your logs that you can use to analyze and debug your policies and rules.

### Traffic is allowed despite a deny rule configured in the Cloud Armor security policy

To fix this, follow these steps:

  1. Make sure that the Cloud Armor security policy is attached to a target backend service. For example, the following command describes all data associated with the backend service `BACKEND`. The results returned must include the name of the Cloud Armor security policy associated with this backend service.
         
         gcloud compute backend-services describe BACKEND
         

Replace `BACKEND` with the name of the backend service.

  2. Review the HTTP(S) logs to determine which policy and rule were matched for your traffic along with the associated action. To view the logs, use [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

The following is a sample log of an allowed request with the interesting fields highlighted. Check for the following fields and make sure that they match the rule that you configured to deny the traffic:

     * `configuredAction` must match the action configured in the rule.
     * `name` must match the name of the Cloud Armor security policy attached to this backend service.
     * `outcome` must match `configuredAction`.
     * `priority` must match the priority number of the rule.
    
    httpRequest:
      remoteIp: 104.133.0.95
      requestMethod: GET
      requestSize: '801'
      requestUrl: http://74.125.67.38/
      responseSize: '246'
      serverIp: 10.132.0.4
      status: 200
      userAgent: curl/7.35.0
        insertId: ajvis5ev4i60
        internalId:
          projectNumber: '895280006100'
        jsonPayload:
          '@type': type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry
          enforcedSecurityPolicy:
            configuredAction: ACCEPT
            name: mydev-policy-log-test1
            outcome: ACCEPT
            priority: 2147483647
          statusDetails: response_sent_by_backend
        logName: projects/mydev-staging/logs/requests
        resource:
          labels:
            backend_service_name: BACKEND_SERVICE_NAME
            forwarding_rule_name: FORWARDING_RULE_NAME
            project_id: PROJECT_ID
            target_proxy_name: TARGET_HTTP_PROXY_NAME
            url_map_name: URL_MAP_NAME
            zone: global
          type: http_load_balancer
        severity: INFO
        timestamp: '2017-04-18T18:57:05.845960288Z'
    

This output includes the following values:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `FORWARDING_RULE_NAME`: the name of the forwarding rule
     * `PROJECT_ID`: the ID of your project
     * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy
     * `URL_MAP_NAME`: the name of the URL map
  3. Review the hierarchy of rules to ensure that the correct rule is matched. It is possible that a higher priority rule with an allow action is matching your traffic. Use the `describe` command on the `security-policies` in the Google Cloud CLI to see the contents of the Cloud Armor security policy.

For example, the following example shows how a higher priority allow rule (at priority 100) matches traffic coming from the 1.2.3.4 IP address, preventing the lower priority deny rule (at priority 200) from triggering and blocking the traffic.
         
         gcloud compute security-policies describe POLICY_NAME
         

Replace `POLICY_NAME` with the name of the security policy.

The output is similar to the following:
         
         creationTimestamp: '2017-04-18T14:47:58.045-07:00
         description: ''
         fingerprint: Yu5spBjdoC0=
         id: '2560355463394441057'
         kind: compute#securityPolicy
         name: POLICY_NAME
         rules:
         -action: allow
          description: allow high priority rule
          kind: compute#securityPolicyRule
          match:
            srcIpRanges:
            -'1.2.3.4/32'
          preview: false
          priority: 100
         -action: deny
          description: deny lower priority rule
          kind: compute#securityPolicyRule
          match:
            srcIpRanges:
            -'1.2.3.0/24
          preview: false
          priority: 200
         -action: deny
          description: default rule
          kind: compute#securityPolicyRule
          match:
            srcIpRanges:
            -'*'
          preview: false
          priority: 2147483647
          selfLink: http://www.googleapis.com/compute/v1/projects/bigclustertestdev0-devconsole/global/securityPolicies/sp
         




### Preconfigured rule returns false positives

XSS and SQLi detection are based on static signature matching on HTTP request headers and other Layer 7 parameters. These regular expression patterns are prone to false positives. You can use the preconfigured rule for XSS and SQLi detection in preview mode and then check the log for any false positives.

If you find a false positive, you can compare the traffic content with the [OWASP CRS rules](https://coreruleset.org/). If you are migrating from an older CRS version, see the [WAF rules version comparison](https://docs.cloud.google.com/armor/docs/waf-rules#version-diffs) for a list of rule changes and renames. If the rule is invalid or not relevant, disable it by using the `evaluatePreconfiguredWaf` expression, and specify the rule's ID in the `exclude ID list` argument.

After reviewing the logs and removing all false positives, disable the preview mode.

To add a preconfigured rule in preview mode:

  1. Create a security policy with the preconfigured expression set in preview mode:
         
         gcloud compute security-policies rules create 1000
              --security-policy POLICY_NAME
              --expression "evaluatePreconfiguredWaf('xss-stable')"
              --action deny-403
              --preview
         

Replace `POLICY_NAME` with the name of the security policy.

  2. Review the HTTP(S) [logs](https://docs.cloud.google.com/logging/docs/view/logs_viewer) for HTTP request fields such as `url` and `cookie`. For example, the `requestUrl` compares positively to the OWASP CRS rule ID 941180:
         
         httpRequest:
          remoteIp: 104.133.0.95
          requestMethod: GET
          requestSize: '801'
          requestUrl: http://74.125.67.38/foo?document.cookie=1010"
          responseSize: '246'
          serverIp: 10.132.0.4
          status: 200
          userAgent: curl/7.35.0
         insertId: ajvis5ev4i60
         internalId:
          projectNumber: '895280006100'
         jsonPayload:
          '@type': type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry
          enforcedSecurityPolicy:
            configuredAction: ACCEPT
            name: POLICY_NAME
            outcome: ACCEPT
            priority: 2147483647
            preconfiguredExprIds: [ 'owasp-crs-v042200-id941180-xss' ]
          statusDetails: response_sent_by_backend
         logName: projects/mydev-staging/logs/requests
         resource:
          labels:
            backend_service_name: BACKEND_SERVICE
            forwarding_rule_name: mydev-forwarding-rule
            project_id: mydev-staging
            target_proxy_name: mydev-target-http-proxy
            url_map_name: mydev-url-map
            zone: global
          type: http_load_balancer
         severity: INFO
         timestamp: '2017-04-18T18:57:05.845960288Z'
         

This log includes the following values:

     * `POLICY_NAME`: the name of the security policy
     * `BACKEND_SERVICE`: the name of the backend service
  3. Exclude the OWASP CRS rule ID 941180 by updating the rule in the Cloud Armor security policy:
         
         gcloud compute security-policies rules update 1000 \
              --security-policy POLICY_NAME \
              --expression "evaluatePreconfiguredWaf('xss-v422-stable', ['owasp-crs-v042200-id941180-xss'])" \
              --action deny-403 \
              --preview
         

Replace `POLICY_NAME` with the name of the security policy.

  4. Review the logs again and then disable preview mode to implement the rule.




### Clients with denied signatures aren't blocked or denied

If you are using Cloud Armor with Cloud CDN, security policies are enforced only for requests for dynamic content, cache misses, or other requests that are destined for the CDN origin server. Cache hits are served even if the downstream Cloud Armor security policy can prevent that request from reaching the CDN origin server.

## Issues with request body inspection

Because Cloud Armor evaluates data progressively as it is received, up to the configured inspection limit, rules might be evaluated against incomplete body data. To prevent potential false positives or incomplete results, write rules that match on the existence of data rather than its absence. For more information, see [Request body inspection limitation](https://docs.cloud.google.com/armor/docs/security-policy-overview#request-body).

### View matched subexpressions in logs

When troubleshooting rules, you can enable [verbose logging](https://docs.cloud.google.com/armor/docs/verbose-logging) by setting the `--log-level` flag to `VERBOSE`, and use Cloud Logging to see which subexpressions in a rule matched. If a rule contains multiple subexpressions, Cloud Armor only logs details about the most recently matched subexpression.

The following example expression contains two subexpressions:

`request.url.contains('__') && request.body.contains('abc')`

If you send a `POST` request with the body `abc` to the URL `example.com/etc/pass__word`, the expression matches. Because the subexpressions are evaluated from left to right, the `request.body.contains('abc')` subexpression is evaluated last. The following log excerpt shows the details for the `request.body` subexpression that is matched:
    
    
    jsonPayload: {
      [...]
      enforcedSecurityPolicy: {
        [...]
        matchedFieldType: "request.body",
        matchedFieldName: "request.body",
        matchedFieldValue: "abc",
        matchedFieldLength: 3,
        matchedOffset: 0,
        matchedLength: 3,
      }
      [..*]
    }
    

## Issues with named IP address lists

This section provides information for resolving problems with named IP address lists.

### IP addresses within a named IP address list

The IP addresses in the lists always match the IP addresses in the [provider websites listed](https://docs.cloud.google.com/armor/docs/threat-intelligence#ip-list-providers) in the Cloud Armor named IP address lists guide. If you have questions about the lists, [contact the Cloud Support team](https://docs.cloud.google.com/armor/docs/getting-support).

### IP addresses within a named IP address list are stale in Cloud Armor

Cloud Armor synchronizes its lists with IP address list providers daily. It is possible to have stale data that lags a few hours or a day behind the data at a provider. However, if you believe that the stale data lags more than expected, for example, more than a week, [contact the Cloud Support team](https://docs.cloud.google.com/armor/docs/getting-support).

### Difficulty creating a security policy that references a named IP address list

You might try to create a security policy that references a named IP address list, using a command such as this:
    
    
    gcloud compute security-policies rules create 750 \
        --security-policy my \
        --expression "evaluatePreconfiguredWaf('sourceiplist-example')" \
        --action "allow"
    

If the command fails, the error that you see looks something like this:
    
    
    ERROR: (gcloud.compute.security-policies.rules.create) Could not fetch resource:
     - Invalid value for field 'resource.match.expr': '{  "expression": "evaluatePreconfiguredWaf(\u0027sourceiplist-example\u0027)"}'.
    Error parsing Cloud Armor rule matcher expression: sourceiplist-example
    isn't a valid preconfigured expression set.
    

Make sure that the particular provider is supported, and that the name of the IP address list is given correctly. You can check this by using the following `gcloud` command to list the current preconfigured expression sets:
    
    
    gcloud compute security-policies list-preconfigured-expression-sets
    

### Traffic is blocked despite a preconfigured rule for a named IP address allowlist

You might find that traffic is blocked from an IP address that is on a named IP address list:

  1. Make sure that traffic is coming from an IP address that is on a [named IP address allowlist](https://docs.cloud.google.com/armor/docs/threat-intelligence#ip-list-providers).

  2. Check whether there are other security rules with a higher priority that can block the traffic. If you still see the issue, [contact the Cloud Support team](https://docs.cloud.google.com/armor/docs/getting-support).

  3. Make sure that the security policy is attached to the correct backend service:
         
         gcloud compute backend-services describe BACKEND_SERVICE
         

  4. Check the rules that are in the security policy. For example:
         
         gcloud compute security-policies describe POLICY_NAME
         

The command returns information similar to the following:
         
         ---
         …
         name: POLICY_NAME
         rules:
         -action: allow
         description: allow fastly ip addresses
         kind: compute#securityPolicyRule
         match:
            expr:
              expression: evaluatePreconfiguredWaf('sourceiplist-fastly')
         preview: false
         priority: 100
         -action: deny(403)
         description: Default rule, higher priority overrides it
         kind: compute#securityPolicyRule
         match:
            config:
              srcIpRanges:
              -'*'
            versionedExpr: SRC_IPS_V1
         preview: false
         priority: 2147483647
         -action: deny(404)
         description: deny altostrat referer
         kind: compute#securityPolicyRule
         match:
            expr:
              expression: request.headers['Referer'].contains('altostrat')
         preview: false
         priority: 50
         …
         

The preceding security policy contains three rules: a default deny rule, an allow rule for [Fastly's IP addresses](https://api.fastly.com/public-ip-list), and a deny rule for a referrer that contains `altostrat`. Their respective priorities are also listed.

  5. Review the logs to determine which rule is matched to your traffic and the associated action. For information about logging, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

The following is an example of a log:
         
         httpRequest: {
            referer: "http://www.altostrat.com/"
            remoteIp: "23.230.32.10"
            requestMethod: "HEAD"
            requestSize: "79"
            requestUrl: "http://www.example.com/"
            responseSize: "258"
            status: 404
            userAgent: "Mozilla/5.0"
          }
          …
          jsonPayload: {
            @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
            enforcedSecurityPolicy: {
              configuredAction: "DENY"
              name: "POLICY_NAME"
              outcome: "DENY"
              priority: 50
            }
            statusDetails: "denied_by_security_policy"
          }
          …
         

From the preceding log, the request is coming from `23.230.32.10`, which is covered by [Fastly's public IP address list](https://api.fastly.com/public-ip-list). However, the request is matched with a deny rule of a higher priority of 50. Comparing this with what's in the security policy, the rule corresponds to the deny rule for a referer that contains `altostrat`. Because the request has a referer of `http://www.altostrat.com/`, the security rule enforcement is working correctly. 




## Issues with Security Command Center findings

This section contains information about issues with Security Command Center findings.

### The Cloud Armor card does not appear in the Security Command Center

Enable Cloud Armor findings in the Security Command Center interface.

### Findings from Cloud Armor don't appear in the Security Command Center

If findings from Cloud Armor don't appear in the Security Command Center, traffic to the backend services might not meet the criteria for raising a finding.

For questions about traffic volume to your backends, check request statistics in the Cloud Monitoring dashboards under the [Network Security Policies](https://docs.cloud.google.com/armor/docs/monitoring).

### Findings are too noisy

For assistance with this issue, [contact the Cloud Support team](https://docs.cloud.google.com/armor/docs/getting-support). 

## Issues with Google Cloud Armor Adaptive Protection

Use these instructions to help you resolve issues with Adaptive Protection.

### Adaptive Protection is enabled for a security policy but there are no logs in Cloud Logging

Adaptive Protection logs are generated separately from Cloud Armor request logs and appear under a different resource in Cloud Logging. Adaptive Protection logs and events are under the **Network Security Policy** resource in Cloud Logging. There is a training period of at least an hour after Adaptive Protection is enabled in a security policy before Adaptive Protection starts generating alerts for suspected attacks. During the training period, Adaptive Protection learns from incoming request traffic and develops distinct baselines for each backend service that is protected by that security policy. Adaptive Protection is subsequently able to identify suspicious activity.

If you enable Adaptive Protection for a security policy and you don't observe any alerts after a one-hour training period, this suggests that there is no activity that can be identified as potentially malicious targeting of any of the backend services associated with that security policy.

If the potential attack or anomalous traffic persists for longer periods of time, exceeding several hours, then Adaptive Protection starts to deem that behavior as baseline behavior and does not continue to alert on similar traffic patterns. After the potential attack subsides and traffic patterns go back to the original baseline, either because the attack concluded or you blocked it with the appropriate Cloud Armor rules, Adaptive Protection alerts on future traffic behaviors that are considered departures from the baseline.

Adaptive Protection analyzes traffic that can otherwise be allowed through a Cloud Armor security policy. If you set the default rule to deny access with a restricted allowlist of traffic, then Adaptive Protection only detects malicious activity on the traffic that passes evaluation with respect to the allowlist.

### There are too many alerts or too many logs in Cloud Logging from Adaptive Protection

An Adaptive Protection alert provides a confidence score, indicating how strongly Adaptive Protection models identify the detected activity as anomalous and potentially an attack. You can filter on the log's specific entry through Cloud Logging to only surface (or forward to downstream) the alerts that have a confidence score above a particular threshold.

Adaptive Protection provides a mechanism for reporting alerts as false positives, which is described in the section [Monitoring, feedback and reporting event errors](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview#monitor-feedback-report-errors). Note that false positive reporting might not result in immediate changes to what Adaptive Protection alerts on. Over time, Adaptive Protection models learn that such traffic patterns are normal and acceptable, and Adaptive Protection stops alerting on these patterns.

If Adaptive Protection alerts are too frequent on a subset of backend services in a security policy, it might suggest that these backend services' normal traffic has significant fluctuations that are constantly identified by Adaptive Protection as anomalous behaviors. You can create a separate security policy without Adaptive Protection enabled and associate these backend services with the new security policy.

### A particular incident reported by Adaptive Protection is considered a false positive or isn't relevant

Adaptive Protection provides a mechanism for reporting false positive alerts. Follow the procedure described in the section [Monitoring, feedback and reporting event errors](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview#monitor-feedback-report-errors). Note that false positive reporting might not result in immediate changes to what Adaptive Protection alerts on. Over time, Adaptive Protection models learn that such traffic patterns are normal and acceptable, and Adaptive Protection stops alerting on these patterns.

### How do I know that my edge security policies are being enforced?

You can check the actions taken on your edge security policies by checking the monitoring dashboards, monitoring metrics, or per-request logging.

#### Monitoring dashboards

Cloud Monitoring is available on the **Network Security Policies** page under **Monitoring**. You can use the breakdown by security policy on the page to measure the number of requests allowed and denied by the configured edge security policy. You can also examine the breakdown by backend service to debug a particular backend service. For details about the Cloud Monitoring dashboard, see [Monitoring Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/monitoring).

#### Monitoring metrics

Raw metrics that measure the requests allowed and denied are available for edge security policies. For more information, see [Monitoring metrics for security policies](https://docs.cloud.google.com/armor/docs/monitoring#monitoring_metrics_for_security_policies).

#### Per-request logging

The edge security policy decision is logged to the load balancing request logs under `enforcedEdgeSecurityPolicy`. This is separate from the `enforcedSecurityPolicy`, which captures the backend security policy decision. 

## Bot management

This section contains information about troubleshooting issues with bot management.

### Users aren't exempted as expected

You might have configured security policy rules with the redirect action for reCAPTCHA assessment, and find that some users that you think are legitimate were not exempted as expected. Use the following steps to troubleshoot.

First, check in the per-request logs to see whether there is a security policy rule with a higher priority that matches the traffic, in which the action is different. In particular, look for the `configured_action` and `outcome` fields. Note that for a user to be exempted, at least two requests are involved. The initial request comes without an exemption cookie, and the follow-on requests come with an exemption cookie if the user passes the reCAPTCHA assessment. Therefore, at least two log entries are expected.

  * If you see `GOOGLE_RECAPTCHA` as the configured action, and `REDIRECT` as the outcome, the request was redirected for reCAPTCHA assessment;
  * If you see `GOOGLE_RECAPTCHA` as the configured action, and `ACCEPT` as the outcome, the request was exempted from being redirected for reCAPTCHA assessment.
  * If you see different values in the preceding fields, a rule with a different action was matched. In that case, it is expected that the user isn't redirected or exempted.



Second, there are several requirements on the user's side for them to be exempted from being redirected for reCAPTCHA assessment.

  1. The user must be using a browser.
  2. The browser must enable JavaScript to allow proper loading of the redirect page with reCAPTCHA JavaScript embedded.
  3. The browser must enable cookies to allow the setting and auto-attaching of the exemption cookie.
  4. The user must pass reCAPTCHA assessment—for example, they must resolve dialog challenges if there are any.



Expect that users who cannot meet any of the preceding requirements don't receive exemption, even if a rule with the redirect action for reCAPTCHA assessment is matched.

Third, reCAPTCHA assessment is only executed when the redirect page that embeds the reCAPTCHA JavaScript is rendered. For that reason, redirecting for reCAPTCHA assessment is only applicable for requests that expect a response leading to a full page render. Other requests, such as assets loading within a page, or requests stemming from an embedded script that don't expect the response to be rendered, aren't expected to get reCAPTCHA assessment. As such, we recommend that you apply this action with a match condition for URL paths that satisfy this condition.

For example, suppose that you have a webpage that contains embedded elements like images, links to other web pages, and scripts. You don't want to apply the redirect action for reCAPTCHA assessment for URL paths that host images, or that are supposed to be accessed by scripts where a full page render isn't expected. Instead, you can apply the redirect action for reCAPTCHA assessment for URL paths that host web pages, like the main webpage or other linked web pages.

Finally, if the redirect page is rendered successfully, check in the Developer Tool provided by the browser to see whether an exemption cookie is set and whether it is attached in the follow-on requests for the same site. For further assistance, you can contact the [Cloud Support](https://docs.cloud.google.com/armor/docs/getting-support) team. 

## Issues with rate limiting

This section helps you troubleshoot common issues with rate limiting.

### Traffic isn't throttled as expected

You might find that a client IP address is sending high levels of traffic to an application at a rate that exceeds the threshold you set, but the traffic is not throttled as you expect. Follow these steps to investigate the issue.

First, confirm whether a higher-priority rule is allowing traffic from that IP address. Examine the logs to see whether an `ALLOW` rule was triggered for the IP address. This could be an `ALLOW` rule on its own, or in another `THROTTLE` or `RATE_BASED_BAN` rule.

If you find a higher-priority rule, do one of the following:

  1. Change the priorities to ensure that the rate-limiting rule has a higher priority, by assigning it a _lower_ numerical value.
  2. Exclude the IP address from the matched expression in the rule that has a higher priority.



The issue might also be that the threshold is set incorrectly. If this is the case, the requests are matched accurately, but the conform action is triggered. Examine the logs to confirm that this is the case, then reduce the threshold in your rule.

Lastly, the IP address might not match the throttle or rate-based ban rule. To fix this, check for a mistake in the match condition, then change the rule's match condition to the correct value.

## What's next

  * [Get support](https://docs.cloud.google.com/armor/docs/getting-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
