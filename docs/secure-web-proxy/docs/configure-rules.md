---
url: https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules/
title: Security rules \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:50.887811+00:00
---

# Security rules  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Security rules Stay organized with collections  Save and categorize content based on your preferences. 

This page explains gateway security rules and how to create them.

Secure Web Proxy lets you define various types of security rules within your gateway security policies to secure outbound web traffic. You can use these rules to precisely control the security of your traffic by using specific request details—like headers and URL patterns—to make sure only approved HTTP/S traffic leaves your network.

**Note:** If you create an [authorization policy](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) in your Secure Web Proxy instance, then the proxy ignores all existing [gateway security policies](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy) and associated gateway security rules.

Gateway security rules have the following features:

  * Each rule is an `if-then` statement that checks a web request against the following parameters:

    * Source identity: _who_ is making the request, such as a specific virtual machine (VM) or [service account](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts).

    * Destination: _where_ the request is going, such as a destination URL or domain like `trusted-partner.com`.

    * Action: the decision to either allow or deny the traffic.

  * Gateway security rules provide granular control. These rules let you enforce different security standards across your organization by using clear, structured definitions.




## Host-matching rules

Secure Web Proxy uses hostname matching to verify the destination domain. The verification process varies depending on how your proxy is deployed as shown in the following table.

Deployment mode | Host verification process  
---|---  
Explicit proxy mode | For unencrypted traffic, the proxy checks the hostname against the HTTP connection header. If you use [Application Matcher attributes](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference#attributes-available-only-to-applicationmatcher) for TLS inspection, then the proxy checks the hostname first at the connection level and then at the application level.  
Next hop mode | For encrypted traffic, the proxy checks the destination hostname against the Server Name Indication (SNI) field in the outbound request. This field is visible even on secure connections.  
  
### Configure host-matching rules for explicit proxy mode

When deploying Secure Web Proxy as an explicit proxy, configure host-matching rules to verify that the host information sent by the client is correctly extracted and checked against your defined security rules. In the explicit proxy mode, clients are actively configured to send their traffic directly to the Secure Web Proxy instance.

Host matching in the explicit proxy mode works for different types of web traffic in the following manner:

Traffic type | Matching mechanism | Rule configuration  
---|---|---  
Unencrypted HTTP | Secure Web Proxy checks the destination hostname against the `host` field in the standard `CONNECT` header of the HTTP request. | In the `sessionMatcher` field, use `host() == "example.com"`.  
Encrypted HTTPS (without Transport Layer Security (TLS) inspection) | Host matching isn't possible either at the application level or at the session level. This is because the request details are encrypted and the `destination.ip` attribute isn't supported. You must either use broader policy controls like source identity matching or enable TLS inspection for host-based filtering. | To use the Application Matcher, use either source identity matching like service accounts or enable TLS inspection.  
Encrypted HTTPS (with TLS inspection) | To inspect the full request, you must use both the Session Matcher and the Application Matcher. | 1\. Set a general Session Matcher rule that either returns `true` or matches the destination host such as `host() == "example.com"`. 2\. In the `applicationMatcher` field, add a specific host rule such as `request.host() == "example.com"`.   
  
### Configure host-matching rules for next hop mode

When deploying Secure Web Proxy as next hop, you must configure host-matching rules. Traffic is redirected to the proxy through a Virtual Private Cloud (VPC) route based on IP address ranges that you define. Host-matching rules ensure that the proxy correctly identifies the destination host by checking various fields of the traffic, such as the Server Name Indication (SNI) header.

Host matching in the next hop mode works for different types of web traffic in the following manner:

Traffic type | Matching mechanism | Rule configuration  
---|---|---  
Unencrypted HTTP | Secure Web Proxy checks the destination hostname against the `host` field in the standard HTTP request header. | In the `sessionMatcher` field, use `host() == "example.com"`.  
Encrypted HTTPS (without TLS inspection) | Secure Web Proxy checks the hostname against the SNI header in the outbound request, which is visible even if the rest of the traffic is encrypted. | In the `sessionMatcher` field, use `host() == "example.com"`.  
Encrypted HTTPS (with TLS inspection) | To inspect the full request, you must use both the Session Matcher and the Application Matcher. | 1\. Set a general Session Matcher rule that either returns `true` or matches the destination host such as `host() == "example.com"`. 2\. In the `applicationMatcher` field, add a specific host rule such as `request.host() == "example.com"`.   
  
## TCP proxy rules

Transmission Control Protocol (TCP) proxy rules let you control traffic that isn't standard web traffic, such as HTTP (port `80`) or HTTPS (port `443`). By configuring TCP proxy rules, you can either allow or block traffic on any other TCP port. These rules help you block malicious traffic and manage non-web applications that use TCP.

If your workload (such as your applications and services) uses [Secure Web Proxy as next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop), then applying TCP proxy rules is beneficial. Route-based redirection directs non-HTTP(S) and non-web traffic to your Secure Web Proxy instance. By doing so, you can block outbound traffic from reaching malicious external sites and manage the external services to which your network workloads can connect.

### Configure TCP proxy rules

You can configure TCP proxy rules for your application to secure non-web traffic and enforce security policies for applications that don't use standard HTTP/S, such as for ports `80` and `443`.

By applying these rules, you can prevent unauthorized use of other TCP ports for data transfer or malicious activity. This is particularly useful when your workloads use [Secure Web Proxy as next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop) for non-web protocols.

To implement TCP proxy rules and create an allow or block traffic rule for your application, you must specify the destination port. Optionally, you can include any of the following Session Matcher attributes to refine the criteria of the allow or block rule.

The following table provides more information about the various attributes that you can use in a TCP proxy rule:

Attribute | Attribute type | Description  
---|---|---  
`source.ip` | string | IP address of the client that sent the request.  
`source.port` | string | Client port that sent the request.  
`destination.port` | string | Upstream port to which your Secure Web Proxy instance sends the traffic.  
`source.matchTag(SECURE_TAG)` | boolean | `True`, if the source is associated with `SECURE_TAG`. The argument is the permanent ID of the secure tag, such as `source.matchTag('tagValues/123456')`.  
`source.matchServiceAccount(SERVICE_ACCOUNT)` | boolean | `True`, if the source is associated with `SERVICE_ACCOUNT` such as `source.matchServiceAccount('x@my-project.iam.gserviceaccount.com')`.   
`inIpRange(IP_ADDRESS,  
IP_RANGE)` | boolean | `True`, if `IP_ADDRESS` is contained within the `IP_RANGE` such as `inIpRange(source.ip, '1.2.3.0/24')`. Subnet masks for IPv6 addresses can't be larger than `/64`.   
  
### TCP proxy rule example

This example shows how to define a Secure Web Proxy `gatewaySecurityPolicyRule` by using a [CEL expression](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference) to allow all TCP traffic to port `22`. You can use this configuration when applying Secure Web Proxy's TCP proxy capabilities.

The following code sample shows how to define a TCP proxy rule:
    
    
    name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/POLICY_NAME/rules/RULE_NAME
    enabled: true
    priority: 100 # Lower numbers have higher priority
    description: "Allow TCP proxy traffic to port 22 - such as, for SSH"
    basicProfile: ALLOW
    sessionMatcher: "destination.port == 22"
    

Replace the following:

  * `PROJECT_ID`: ID of your project
  * `REGION`: region of your policy
  * `POLICY_NAME`: name of your policy
  * `RULE_NAME`: name of the TCP proxy rule. In this example, we can consider its value as `allow-ssh-tcp-proxy`.



### Important considerations

  * Any TCP proxy rules that you configure must have a higher priority (lower number) than HTTP/S rules to ensure they are evaluated and acted upon first. For more information, see [Rule evaluation order](https://docs.cloud.google.com/secure-web-proxy/docs/tls-rule-evaluation).

  * When configuring TCP proxy rules, the `host` Session Matcher attribute isn't supported because host information isn't available at the TCP layer.

  * TCP proxy rules filter web traffic based only on the destination port. To enhance your network's security, we recommend that you add other conditions by using logical operators the logical AND operator (&&) and the logical OR operator (||) and supported attributes like `source.ip`. Here's an example of how to define a more specific TCP proxy rule:
        
        // Allow port 22 from only a specific source IP range
          sessionMatcher: "destination.port == 22 && inIpRange(source.ip, '10.0.0.0/24')"
        

  * Secure Web Proxy doesn't support the ability to configure proxy rules for [User Datagram Protocol (UDP)](https://en.wikipedia.org/wiki/User_Datagram_Protocol) applications. As a result, Secure Web Proxy blocks the traffic of UDP-based applications.




## Create a security rule

Before creating a gateway security rule, make sure that you perform the following actions:

  1. Complete all the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  2. [Create a policy](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy#create-policy)


**Important:** To analyze request attributes for HTTPS traffic, [enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).

After creating a rule and associating it with a policy, you can use the rule when deploying Secure Web Proxy.

###  Console 

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click the name of your policy, such as `policy1`.

  3. Click add_box**Add rule**.

  4. For each rule, do the following:

     1. For **Priority** , enter a numeric evaluation order for the rule. Rules are evaluated from highest to lowest priority, where `0` is the highest priority.

     2. In the **Name** field, enter a name for the rule.

     3. In the **Description** field, enter a description for the rule.

     4. For **Action** , select one of the following options:

        * **Allow** : to allow connection requests that match the rule.
        * **Deny** : to deny connection requests that match the rule.
     5. For the **Status** field, select one of the following options for the rule enforcement:

        * **Enabled** : to enforce the rule on your Secure Web Proxy instance.
        * **Disabled** : to not enforce the rule on your Secure Web Proxy instance.
     6. In the **Session Match** section, specify the criteria for matching the session, such as `host() == "www.wikipedia.org"`.

For more information about the syntax for `SessionMatcher`, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).

     7. In the **Application Match** section, specify the criteria for matching the request.

For more information about matching TCP traffic, see Configure TCP proxy rules.

     8. Click **Add rule**.


**Important:** To create a rule with TLS inspection, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).

###  Cloud Shell 

  1. Use your preferred text editor to create a `rule.yaml` file. For more information about the syntax for `sessionMatcher`, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).
         
         name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1/rules/RULE_NAME
         description: Allow wikipedia.org
         enabled: true
         priority: 1
         basicProfile: ALLOW
         sessionMatcher: host() == 'www.wikipedia.org'
         

Replace the following:

     * `PROJECT_ID`: ID of your project
     * `REGION`: region of your policy
     * `RULE_NAME`: name of the rule. In this example, we can consider its value as `allow-wikipedia-org`.

**Optional** : Alternatively, if you want to create a rule with TLS inspection enabled, then create the `rule.yaml` file as shown here. For more information, see [TLS inspection overview](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview) and [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).
    
    name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1/rules/RULE_NAME
      description: Allow wikipedia.org
      enabled: true
      priority: 1
      basicProfile: ALLOW
      sessionMatcher: host() == 'www.wikipedia.org'
      applicationMatcher: request.path.contains('index.html')
      tlsInspectionEnabled: true
    

For more information about matching TCP traffic, see Configure TCP proxy rules.

**Important:** To enable TLS inspection for every rule that you create, set the `tlsInspectionEnabled` attribute to `true` for each rule that uses `applicationMatcher` to match the HTTPS traffic. The TLS inspection for the rule is limited to the traffic that matches the `sessionMatcher` attribute of the rule. For more information, see [TLS inspection rule evaluation](https://docs.cloud.google.com/secure-web-proxy/docs/tls-rule-evaluation).
  2. Create the security policy rule. 
         
         gcloud network-security gateway-security-policies rules import allow-wikipedia-org \
             --source=rule.yaml \
             --location=REGION \
             --gateway-security-policy=policy1
         




## Limitations

  * If you create an [authorization policy](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) in your Secure Web Proxy instance, then the proxy ignores all existing [gateway security policies](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy) and associated gateway security rules.

  * Secure Web Proxy doesn't support the ability to configure rules for [User Datagram Protocol (UDP)](https://en.wikipedia.org/wiki/User_Datagram_Protocol) applications. Secure Web Proxy blocks the traffic of UDP-based applications.




## What's next

  * [Create a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)
  * [Deploy Secure Web Proxy as a Private Service Connect service](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment)
  * [Deploy Secure Web Proxy as next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
