---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy/
title: AccessControl policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:51.444971+00:00
---

# AccessControl policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  AccessControl policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The AccessControl policy lets you allow or deny access to your APIs by specific IP addresses.

While you can attach this policy anywhere in the API proxy flow, you'll most likely want to check IP addresses at the beginning of the flow ( Request / ProxyEndpoint / PreFlow), even before authentication or quota checking.

Also consider using [Google Cloud Armor](https://cloud.google.com/armor) with Apigee as an alternative way to secure your APIs.

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

### Samples

The mask values in the following IPv4 samples identify which of the four octets (8, 16, 24, 32 bits) the match rule considers when allowing or denying access. The default value is 32. See the `mask` attribute in the Element reference for more information.

### Deny 198.51.100.1
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "ALLOW">
        <MatchRule action = "DENY">
          <SourceAddress mask="32">198.51.100.1</SourceAddress>
        </MatchRule>
      </IPRules>
    </AccessControl>

Deny all requests from client address: 198.51.100.1

Allow requests from any other client address.

### Deny using variables
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "ALLOW">
        <MatchRule action = "DENY">
          <SourceAddress mask="{kvm.mask.value}">{kvm.ip.value}</SourceAddress>
        </MatchRule>
        </IPRules>
    </AccessControl>

Suppose you're using a key value map (KVM) to store values for masking and IPs. This is a handy approach to changing IPs and masking during runtime without having to update and redeploy your API proxy. You can use the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) to retrieve the variables containing the values for `kvm.mask.value` and `kvm.ip.value` (assuming that's what you named the variables in your KVM policy that contain the values of the mask and IP values from your KVM). If the values you retrieved were `24` for the mask and `198.51.100.1` for the IP address, the AccessControl policy would deny all requests from: 198.51.100.*

All other client addresses would be allowed.

### Deny 198.51.100.*
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "ALLOW">
        <MatchRule action = "DENY">
          <SourceAddress mask="24">198.51.100.1</SourceAddress>
        </MatchRule>
        </IPRules>
    </AccessControl>

Deny all requests from client address: 198.51.100.*

Allow requests from any other client address.

### 198.51.*.*
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "ALLOW">
        <MatchRule action = "DENY">
           <SourceAddress mask="16">198.51.100.1</SourceAddress>
        </MatchRule>
      </IPRules>
    </AccessControl>

Deny all requests from client address: 198.51.*.*

Allow requests from any other client address.

### Deny 198.51.100.*, allow 192.0.2.1
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "ALLOW">
        <MatchRule action = "ALLOW">
          <SourceAddress mask="32">192.0.2.1</SourceAddress>
        </MatchRule>
        <MatchRule action = "DENY">
          <SourceAddress mask="24">198.51.100.1</SourceAddress>
        </MatchRule>
      </IPRules>
    </AccessControl>

Deny all requests from client address: 198.51.100.*, but allow 192.0.2.1.

Allow requests from any other client address.

### Allow 198.51.*.*
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "DENY">
        <MatchRule action = "ALLOW">
          <SourceAddress mask="16">198.51.100.1</SourceAddress>
        </MatchRule>
      </IPRules>
    </AccessControl>

Allow all requests from address: 198.51.*.*

Deny requests from any other client address.

### Allow multiple IPs
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "DENY">
        <MatchRule action = "ALLOW">
          <SourceAddress mask="24">198.51.100.1</SourceAddress>
          <SourceAddress mask="24">192.0.2.1</SourceAddress>
          <SourceAddress mask="24">203.0.113.1</SourceAddress>
         </MatchRule>
      </IPRules>
    </AccessControl>

Allow requests from client addresses: 198.51.100.* 192.0.2.* 203.0.113.*

Deny all other addresses.

### Deny multiple IPs
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "ALLOW">
        <MatchRule action = "DENY">
          <SourceAddress mask="24">198.51.100.1</SourceAddress>
          <SourceAddress mask="24">192.0.2.1</SourceAddress>
          <SourceAddress mask="24">203.0.113.1</SourceAddress>
        </MatchRule>
      </IPRules>
    </AccessControl>

Deny requests from client addresses: 198.51.100.* 192.0.2.* 203.0.113.*

Allow all other addresses.

### Allow multiple IPs, deny multiple IPs
    
    
    <AccessControl name="ACL">
      <IPRules noRuleMatchAction = "DENY">
        <MatchRule action = "DENY">
          <SourceAddress mask="24">198.51.100.1</SourceAddress>
          <SourceAddress mask="24">192.0.2.1</SourceAddress>
          <SourceAddress mask="24">203.0.113.1</SourceAddress>
        </MatchRule>
        <MatchRule action = "ALLOW">
          <SourceAddress mask="16">198.51.100.1</SourceAddress>
          <SourceAddress mask="16">192.0.2.1</SourceAddress>
          <SourceAddress mask="16">203.0.113.1</SourceAddress>
        </MatchRule>
      </IPRules>
    </AccessControl>

Allow: 198.51.*.* 192.0.*.* 203.0.*.*

Deny a subset of the allow list: 198.51.100.* 192.0.2.* 203.0.113.*

## Usage notes

In addition to protecting your APIs against malicious IPs, the AccessControl policy also gives you control over legitimate IP access. For example, if you only want computers under the control of your enterprise to access the APIs exposed in your test environment, you can allow the IP address range for your internal network. Developers working from home can access these APIs using VPN.

**Note:** If you are using both [security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) and the AccessControl policy to manage traffic based on IP address, the security action always executes before the AccessControl policy. After that, neither impacts the other; the security action has no influence on the AccessControl policy and vice versa.

The configuration and execution of an AccessControl policy involves the following:

  * Define a set of _match rules_ with one of two actions (ALLOW or DENY) associated with each.
  * For each match rule, specify the IP address (SourceAddress element). 
    * See How the policy chooses which IP address to evaluate to determine which IP address(es) in the message you're configuring rules to handle.
    * Configure a mask for each IP address. You allow or deny access based on a mask value on the IP address. See About IP masking with CIDR notation.
  * Specify the order in which the rules are tested.
  * All the match rules are executed in the given order. When a rules matches, the corresponding action is executed and following match rules are skipped. 
    * If the same rule is configured with both ALLOW and DENY actions, the rule that is defined first in the order is triggered and the subsequent rule (with the other action) is skipped.



### Handling of invalid IP addresses

The AccessControl policy handles invalid IP address strings passed as variables differently from invalid strings parsed through headers.

  * Header-Based (no `<ClientIPVariable>`): When the policy directly parses the `X-Forwarded-For` (XFF) header, any non-IP string (for example, `pwned`) in the header being evaluated is silently ignored. The policy proceeds as if the IP address string did not match any rule, and the action specified by `<noRuleMatchAction>` is taken. This can be a security concern if `<noRuleMatchAction>` is set to **ALLOW** , as it could be used to bypass `blocklist` rules.
  * Variable-Based (`<ClientIPVariable>` is used): If a variable specified in `<ClientIPVariable>` contains an invalid IP address format, the policy will throw an error (for example, `accesscontrol.InvalidIPAddressInVariable`). This provides a more explicit failure and is the recommended approach for stricter IP validation.



### How the policy chooses which IP address to evaluate

IP addresses can come from various sources in a request. For example, the `X-Forwarded-For` header may contain one or more IP addresses. This section describes how to configure the AccessControl policy to evaluate the exact IP address(es) you want it to evaluate.

For Apigee hybrid, we recommend that you set up a load balancer in front of your Kubernetes cluster. The load balancer may be L7 (HTTP aware) or L4 (TCP aware). L7 load balancers can add the client source IP address to the `X-Forwarded-For` (XFF) header. L4 load balancers should be configured to use the [PROXY protocol](https://cloud.google.com/load-balancing/docs/tcp/setting-up-tcp#proxy-protocol). Consult your load balancer's manual on how to enable PROXY protocol support. For enabling the PROXY protocol on the Ingress, see [ Source IP address of the original client](https://istio.io/latest/docs/tasks/security/authorization/authz-ingress/#source-ip-address-of-the-original-client) in the Istio documentation. 

Following is the logic the AccessControl policy uses to decide which IP address to evaluate:

#### X-Forwarded-For header

Apigee automatically populates the `X-Forwarded-For` header with the IP address it received from the last external TCP handshake (such as the client IP or router). If there are multiple IP addresses in the header, those addresses are likely the chain of servers that processed a request. However, the list of addresses could also contain a spoofed IP address. So how does the policy know which addresses to evaluate?

##### Apigee specification for XFF header behavior

In Apigee, the presence of Google Cloud Load Balancers (GCLBs) affects the structure of the `X-Forwarded-For` (XFF) header. The typical format of the header is as follows:

`X-Forwarded-For: <client_ip>, <GCLB1_ip>, <internal_ingress_ip>` **Note:** The `X-Forwarded-For` header format depends on the network topology (path taken by the request across the network). 

It is crucial to understand the implications of this structure when using the `ValidateBasedOn` element:

  * `X_FORWARDED_FOR_LAST_IP`: In Apigee, using this setting will evaluate the internal IP address of the second GCLB, not the original client IP. This can lead to unexpected policy behavior.
  * `X_FORWARDED_FOR_FIRST_IP`: While this setting correctly evaluates the original `<client_ip>`, you should be aware that `<client_ip>` can be easily spoofed by the client, making it less reliable for security-sensitive use cases.



#### X-Forwarded-For dimensions in Apigee analytics

Apigee Analytics writes the value of the `X-Forwarded-For` header to the `x_forwarded_for_ip` dimension. To determine the client IP that made the request to Apigee, use the values in the `ax_resolved_client_ip` dimension but _exclude_ `ax_true_client_ip`, which is not supported with the AccessControl policy. See [Analytics metrics, dimensions, and filters reference](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference).

### About IP masking with CIDR notation

CIDR notation (Classless Inter-Domain Routing) is a way of indicating a range of IP addresses through masking. It applies to both IPv4 and IPv6. Here's how it works. We'll use IPv4 in our examples for simplicity.

IP addresses are groups of numbers separated by periods. In binary terms, each group is a specific number of bits (8 for IPv4 and 16 for IPv6). The IPv4 address 198.51.100.1 looks like this in binary:

`11000110.00110011.01100100.00000001`

That's 4 groups of 8 bits, or 32 total bits. With CIDR, you can indicate a range by adding a /number (1-32) to the IP address, like this:

`198.51.100.1/24`

In this case, the 24 is the number you would use for the `mask` attribute value in this policy.

This notation means, "Keep the first 24 bits exactly as is, the remaining bits can be any value 0 through 255." For example:

Keep these exactly as is | Possible values for the last group  
---|---  
198.51.100. | 0 - 255  
  
Notice that the mask happens at the end of group three. This makes things nice and tidy, in essence creating a mask like this: 198.51.100.*. In most cases, using multiples of 8 (IPv4) and 16 (IPv6) will give you the masking level you want:

IPv4: 8, 16, 24, 32

IPv6: 16, 32, 48, 64, 80, 96, 112, 128

However, you can use other numbers for finer-grained control, which involves a little binary calculation. Here's an example using a mask of 30, as in **198.51.100.1/30** , where the last 1 is 00000001 in binary:

Keep these exactly as is | Possible values  
---|---  
**11000110.00110011.01100100.000000** (first 30 bits) | 000000**00** , 000000**01** , 000000**10** , or 000000**11**  
**198.51.100.** | 0, 1, 2, or 3  
  
In this example, with the configuration set to `<SourceAddress mask="30">198.51.100.1</SourceAddress>`, the following IPs would be allowed (or denied, depending on your rules):

  * 198.51.100.0
  * 198.51.100.1
  * 198.51.100.2
  * 198.51.100.3



## Element reference

The element reference describes the elements and attributes of the AccessControl policy.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <AccessControl async="false" continueOnError="false" enabled="true" name="Access-Control-1">
        <DisplayName>Access Control 1</DisplayName>
        <IPRules noRuleMatchAction = "ALLOW">
            <MatchRule action = "ALLOW">
                <SourceAddress mask="32">198.51.100.1</SourceAddress>
            </MatchRule>
            <MatchRule action = "DENY">
                <SourceAddress mask="24">198.51.100.1</SourceAddress>
            </MatchRule>
        </IPRules>
        <ValidateBasedOn>X_FORWARDED_FOR_ALL_IP</ValidateBasedOn>
    </AccessControl>

## <AccessControl> attributes
    
    
    <AccessControl async="false" continueOnError="false" enabled="true" name="Access-Control-1">

## <ClientIPVariable> element

Specifies a flow variable containing an IP address that the policy checks against the IPRules. If the flow variable does not contain a valid IP address (ipv4 or ipv6), then the policy throws an error. 

**Note:** You can use the `client.resolved.ip` flow variable for the client IP address. See [Client IP resolution](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution) for information on how the client IP address is determined for that variable.

Suppose the flow variable is set to the `12.31.34.52`. In the following example, access is denied. If the variable is set to `10.11.12.13`, access is granted. 
    
    
    <AccessControl name='ACL'>
       <ClientIPVariable>FLOW_VARIABLE</ClientIPVariable>
       <IPRules noRuleMatchAction = 'DENY'>
         <MatchRule action = 'ALLOW'>
           <SourceAddress mask='32'>10.11.12.13</SourceAddress>
         </MatchRule>
       </IPRules>
    </AccessControl>

Default | N/A  
---|---  
Presence | Optional  
Type | Flow variable  
  
## <IgnoreTrueClientIPHeader> element

**Note:** Leaving out this element or setting this element to false does currently not lead to Apigee correctly evaluating the `True-Client-IP` header.

## <IPRules> element

The parent element containing the rules that allow or deny IP addresses. The `noRuleMatchAction` attribute lets you define how to handle any IP addresses that aren't covered by your matching rules.
    
    
    <IPRules noRuleMatchAction = "ALLOW">

Default | N/A  
---|---  
Presence | Optional  
Type | N/A  
  
### Attributes

Attribute | Description | Type | Default | Presence  
---|---|---|---|---  
noRuleMatchAction |  The action to take (allow or deny access) if the match rule specified is not resolved (unmatched).  Valid value: ALLOW or DENY  | String | ALLOW | Required  
  
## <IPRules>/<MatchRule> element

The action to take (allow or deny access) if the IP address matches the SourceAddress(es) you define.
    
    
    <IPRules noRuleMatchAction = "ALLOW">
        **< MatchRule action = "ALLOW">**
            <SourceAddress mask="32">198.51.100.1</SourceAddress>
        </MatchRule>
        **< MatchRule action = "DENY">**
            <SourceAddress mask="24">198.51.100.1</SourceAddress>
        </MatchRule>
    </IPRules>

Default | N/A  
---|---  
Presence | Optional  
Type | N/A  
  
### Attributes

Attribute | Description | Type | Default | Presence  
---|---|---|---|---  
action |  The action to take (allow or deny access) if the match rule specified is not resolved (unmatched). Valid value: ALLOW or DENY | String | ALLOW | Required  
  
## <IPRules>/<MatchRule>/<SourceAddress> element

The IP address range of a client.

Valid value: Valid IP address (dotted decimal notation). For wildcard behavior, use the `mask` attribute.
    
    
    <IPRules noRuleMatchAction = "ALLOW">
        <MatchRule action = "ALLOW">
            **< SourceAddress mask="{variable}">198.51.100.1</SourceAddress>**
        </MatchRule>
        <MatchRule action = "DENY">
            **< SourceAddress mask="24">{variable}</SourceAddress>**
        </MatchRule>
    </IPRules>

As shown in the previous example, the `SourceAddress` element also supports [Message templates](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro) for the `mask` attribute or IP address, which means you can set the values using variables that are currently available in the API proxy flow.

For example, you can store an IP address in a key value map (KVM) and use the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) to retrieve the IP address and assign it to a variable (such as `kvm.ip.value`). You can then use that variable for the IP address:

`<SourceAddress mask="24">**{kvm.ip.value}** </SourceAddress>`

Setting mask and/or IP address with a variable gives you the flexibility to change values at runtime without having to modify and re-deploy your API proxy.

Default | N/A  
---|---  
Presence | Optional  
Type | String (single IP address only)  
  
### Attributes

Attribute | Description | Type | Default | Presence  
---|---|---|---|---  
mask |  The `mask` attribute is a way to indicate the range of IP addresses to allow or deny. Mask is the equivalent of using CIDR notation (Classless Inter-Domain Routing). For example: `<SourceAddress mask="24">198.51.100.1</SourceAddress>` is equivalent to the following CIDR notation: 198.51.100.1/24 Valid values: IPv4: 1-32 IPv6: 1-128 A value of zero (0) is valid only for IP 0.0.0.0, hence impractical. **Set the mask with a variable** The `mask` attribute also supports [Message templates](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro), which means you can set the value with a variable that's currently available in the API proxy flow. For example, you can store a mask value in a KVM and use the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) to retrieve the mask and assign it to a variable. To set the IP mask with the variable, use the following format, assuming the variable is named `kvm.mask.value`: `mask="{kvm.mask.value}"` | Integer | N/A | Required  
  
## <ValidateBasedOn> element

When the `X-Forwarded-For` HTTP header contains multiple IP addresses, use this `ValidateBasedOn` element to control which IP addresses are evaluated.

**Note:** Currently it is necessary to set the element <IgnoreTrueClientIPHeader> to true in order for multiple IP addresses to be evaluated.

Use this approach to evaluating a IP addresses only if you're certain about the validity of the IP addresses you want to evaluate. For example, if you choose to evaluate all IP addresses in the `X-Forwarded-For` header, you have to be able to trust the validity of those addresses, and/or set up comprehensive DENY or ALLOW rules to let only trusted IPs call your API proxy.

**Note:** You can use the `client.resolved.ip` flow variable for the client IP address in `<clientIPVariable>` rather than using `<ValidateBasedOn>`. See <ClientIPVariable> element.

The leftmost IP address in the header belongs to the client, and the rightmost is the server which forwarded the request to the current service. The rightmost, or last IP address, is the address Apigee received from the last external TCP handshake.

The value you enter in this element lets you determine whether to check all IP addresses in the header (default), only the first IP address, or only the last IP address.
    
    
    <AccessControl async="false" continueOnError="false" enabled="true" name="Access-Control-1">
        <DisplayName>Access Control 1</DisplayName>
        <IPRules noRuleMatchAction = "ALLOW">
            <MatchRule action = "DENY">
                <SourceAddress mask="32">198.51.100.1</SourceAddress>
            </MatchRule>
        </IPRules>
        **< ValidateBasedOn>X_FORWARDED_FOR_ALL_IP</ValidateBasedOn>**
    </AccessControl>

Default | `X_FORWARDED_FOR_ALL_IP`  
---|---  
Presence | Optional  
Valid values |  `X_FORWARDED_FOR_ALL_IP` (default) `X_FORWARDED_FOR_FIRST_IP` `X_FORWARDED_FOR_LAST_IP`  
  
## Schemas

Each policy type is defined by an XML schema (.xsd). For reference, [ policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`accesscontrol.IPDeniedAccess` | `403` | The client IP address, or an IP address passed in the API request, matches an IP address specified in the `<SourceAddress>` element within the `<MatchRule>` element of the Access Control Policy, and the `action` attribute of the `<MatchRule>` element is set to `DENY`. | [ _build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/access-control-runtime-errors#ipdeniedaccess)  
`accesscontrol.InvalidIPAddressInVariable` | `500` | The flow variable in `<ClientIPVariable>` contains an invalid IP address.  
  
### Fault variables

These variables are set when a runtime error occurs. For more information, see [Variables specific to policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors#variablesspecifictopolicyerrors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "IPDeniedAccess"`  
`acl.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `acl.AC-AllowAccess.failed = true`  
  
### Example fault response

**Note:** For fault handling, the best practice is to trap the `errorcode` part of the fault response. Do not rely on the text in the `faultstring` because it could change.
    
    
    {
       "fault":{
         "faultstring":"Access Denied for client ip : 52.211.243.3"
          "detail":{
             "errorcode":"steps.accesscontrol.IPDeniedAccess"
          }
       }
    }

### Example fault rule
    
    
    <FaultRule name="IPDeniedAccess">
        <Step>
            <Name>AM-IPDeniedAccess</Name>
            <Condition>(fault.name Matches "IPDeniedAccess") </Condition>
        </Step>
        <Condition>(acl.failed = true) </Condition>
    </FaultRule>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
