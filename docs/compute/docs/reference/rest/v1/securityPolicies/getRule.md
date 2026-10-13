---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/getRule/
title: Method: securityPolicies.getRule \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:42.119145+00:00
---

# Method: securityPolicies.getRule  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/getRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: securityPolicies.getRule Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Gets a rule at the specified priority.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/securityPolicies/{securityPolicy}/getRule`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`securityPolicy` |  `string` Name of the security policy to which the queried rule belongs.  
  
### Query parameters

Parameters  
---  
`priority` |  `integer` The priority of the rule to get from the security policy.  
  
### Request body

The request body must be empty.

### Response body

Represents a rule that describes one or more match conditions along with the action to be taken when traffic matches this condition (allow or deny).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "description": string,
      "priority": integer,
      "match": {
        "expr": {
          "expression": string,
          "title": string,
          "description": string,
          "location": string
        },
        "exprOptions": {
          "recaptchaOptions": {
            "actionTokenSiteKeys": [
              string
            ],
            "sessionTokenSiteKeys": [
              string
            ]
          }
        },
        "versionedExpr": enum,
        "config": {
          "srcIpRanges": [
            string
          ]
        }
      },
      "networkMatch": {
        "userDefinedFields": [
          {
            "name": string,
            "values": [
              string
            ]
          }
        ],
        "srcIpRanges": [
          string
        ],
        "destIpRanges": [
          string
        ],
        "ipProtocols": [
          string
        ],
        "srcPorts": [
          string
        ],
        "destPorts": [
          string
        ],
        "srcRegionCodes": [
          string
        ],
        "srcAsns": [
          integer
        ]
      },
      "action": string,
      "preview": boolean,
      "rateLimitOptions": {
        "rateLimitThreshold": {
          "count": integer,
          "intervalSec": integer
        },
        "conformAction": string,
        "exceedAction": string,
        "exceedRedirectOptions": {
          "type": enum,
          "target": string
        },
        "enforceOnKey": enum,
        "enforceOnKeyName": string,
        "enforceOnKeyConfigs": [
          {
            "enforceOnKeyType": enum,
            "enforceOnKeyName": string
          }
        ],
        "banThreshold": {
          "count": integer,
          "intervalSec": integer
        },
        "banDurationSec": integer
      },
      "headerAction": {
        "requestHeadersToAdds": [
          {
            "headerName": string,
            "headerValue": string
          }
        ]
      },
      "redirectOptions": {
        "type": enum,
        "target": string
      },
      "preconfiguredWafConfig": {
        "exclusions": [
          {
            "targetRuleSet": string,
            "targetRuleIds": [
              string
            ],
            "requestHeadersToExclude": [
              {
                "val": string,
                "op": enum
              }
            ],
            "requestCookiesToExclude": [
              {
                "val": string,
                "op": enum
              }
            ],
            "requestQueryParamsToExclude": [
              {
                "val": string,
                "op": enum
              }
            ],
            "requestUrisToExclude": [
              {
                "val": string,
                "op": enum
              }
            ],
            "requestBodiesToExclude": [
              {
                "val": string,
                "op": enum
              }
            ]
          }
        ]
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#securityPolicyRule` for security policy rules  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`priority` |  `integer` An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.  
`match` |  `object` A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.  
`match.expr` |  `object` User defined CEVAL expression. A CEVAL expression is used to specify match criteria such as origin.ip, source.region_code and contents in the request header. Expressions containing `evaluateThreatIntelligence` require a Cloud Armor Enterprise subscription and are not supported in Edge Policies nor in Regional Policies. Expressions containing `evaluatePreconfiguredExpr('sourceiplist-*')` require a Cloud Armor Enterprise subscription and are only supported in Global Security Policies.  
`match.expr.expression` |  `string` Textual representation of an expression in Common Expression Language syntax.  
`match.expr.title` |  `string` Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`match.expr.description` |  `string` Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`match.expr.location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
`match.exprOptions` |  `object` The configuration options available when specifying a user defined CEVAL expression (i.e., 'expr').  
`match.exprOptions.recaptchaOptions` |  `object` reCAPTCHA configuration options to be applied for the rule. If the rule does not evaluate reCAPTCHA tokens, this field has no effect.  
`match.exprOptions.recaptchaOptions.actionTokenSiteKeys[]` |  `string` A list of site keys to be used during the validation of reCAPTCHA action-tokens. The provided site keys need to be created from reCAPTCHA API under the same project where the security policy is created.  
`match.exprOptions.recaptchaOptions.sessionTokenSiteKeys[]` |  `string` A list of site keys to be used during the validation of reCAPTCHA session-tokens. The provided site keys need to be created from reCAPTCHA API under the same project where the security policy is created.  
`match.versionedExpr` |  `enum` Preconfigured versioned expression. If this field is specified, config must also be specified. Available preconfigured expressions along with their requirements are: SRC_IPS_V1 - must specify the corresponding srcIpRange field in config.  
`match.config` |  `object` The configuration options available when specifying versionedExpr. This field must be specified if versionedExpr is specified and cannot be specified if versionedExpr is not specified.  
`match.config.srcIpRanges[]` |  `string` CIDR IP address range. Maximum number of srcIpRanges allowed is 10.  
`networkMatch` |  `object` A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.Example:networkMatch: srcIpRanges: - "192.0.2.0/24" - "198.51.100.0/24" userDefinedFields: - name: "ipv4_fragment_offset" values: - "1-0x1fff"The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.  
`networkMatch.userDefinedFields[]` |  `object` User-defined fields. Each element names a defined field and lists the matching values for that field.  
`networkMatch.userDefinedFields[].name` |  `string` Name of the user-defined field, as given in the definition.  
`networkMatch.userDefinedFields[].values[]` |  `string` Matching values of the field. Each element can be a 32-bit unsigned decimal or hexadecimal (starting with "0x") number (e.g. "64") or range (e.g. "0x400-0x7ff").  
`networkMatch.srcIpRanges[]` |  `string` Source IPv4/IPv6 addresses or CIDR prefixes, in standard text format.  
`networkMatch.destIpRanges[]` |  `string` Destination IPv4/IPv6 addresses or CIDR prefixes, in standard text format.  
`networkMatch.ipProtocols[]` |  `string` IPv4 protocol / IPv6 next header (after extension headers). Each element can be an 8-bit unsigned decimal number (e.g. "6"), range (e.g. "253-254"), or one of the following protocol names: "tcp", "udp", "icmp", "esp", "ah", "ipip", or "sctp".  
`networkMatch.srcPorts[]` |  `string` Source port numbers for TCP/UDP/SCTP. Each element can be a 16-bit unsigned decimal number (e.g. "80") or range (e.g. "0-1023").  
`networkMatch.destPorts[]` |  `string` Destination port numbers for TCP/UDP/SCTP. Each element can be a 16-bit unsigned decimal number (e.g. "80") or range (e.g. "0-1023").  
`networkMatch.srcRegionCodes[]` |  `string` Two-letter ISO 3166-1 alpha-2 country code associated with the source IP address.  
`networkMatch.srcAsns[]` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` BGP Autonomous System Number associated with the source IP address.  
`action` |  `string` The Action to perform when the rule is matched. The following are the valid actions: 

  * `allow`: allow access to target.
  * `deny(STATUS)`: deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502.
  * `rate_based_ban`: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rateLimitOptions to be set.
  * `redirect`: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR.
  * `throttle`: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rateLimitOptions to be set for this.
  * `fairshare (preview only)`: when traffic reaches the threshold limit, requests from the clients matching this rule begin to be rate-limited using the Fair Share algorithm. This action is only allowed in security policies of type `CLOUD_ARMOR_INTERNAL_SERVICE`.

  
`preview` |  `boolean` If set to true, the specified action is not enforced.  
`rateLimitOptions` |  `object` Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.  
`rateLimitOptions.rateLimitThreshold` |  `object` Threshold at which to begin ratelimiting.  
`rateLimitOptions.rateLimitThreshold.count` |  `integer` Number of HTTP(S) requests for calculating the threshold.  
`rateLimitOptions.rateLimitThreshold.intervalSec` |  `integer` Interval over which the threshold is computed.  
`rateLimitOptions.conformAction` |  `string` Action to take for requests that are under the configured rate limit threshold. Valid option is "allow" only.  
`rateLimitOptions.exceedAction` |  `string` Action to take for requests that are above the configured rate limit threshold, to either deny with a specified HTTP response code, or redirect to a different endpoint. Valid options are `deny(STATUS)`, where valid values for `STATUS` are 403, 404, 429, and 502, and `redirect`, where the redirect parameters come from `exceedRedirectOptions` below. The `redirect` action is only supported in Global Security Policies of type CLOUD_ARMOR.  
`rateLimitOptions.exceedRedirectOptions` |  `object` Parameters defining the redirect action that is used as the exceed action. Cannot be specified if the exceed action is not redirect. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`rateLimitOptions.exceedRedirectOptions.type` |  `enum` Type of the redirect action. Possible values are: 

  * `GOOGLE_RECAPTCHA`: redirect to reCAPTCHA for manual challenge assessment.
  * `EXTERNAL_302`: redirect to a different URL via a 302 response.

  
`rateLimitOptions.exceedRedirectOptions.target` |  `string` Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA.  
`rateLimitOptions.enforceOnKey` |  `enum` Determines the key to enforce the rateLimitThreshold on. Possible values are: 

  * `ALL`: A single rate limit threshold is applied to all the requests matching this rule. This is the default value if "enforceOnKey" is not configured.
  * `IP`: The source IP address of the request is the key. Each IP has this limit enforced separately.
  * `HTTP_HEADER`: The value of the HTTP header whose name is configured under "enforceOnKeyName". The key value is truncated to the first 128 bytes of the header value. If no such header is present in the request, the key type defaults to `ALL`.
  * `XFF_IP`: The first IP address (i.e. the originating client IP address) specified in the list of IPs under X-Forwarded-For HTTP header. If no such header is present or the value is not a valid IP, the key defaults to the source IP address of the request i.e. key type `IP`.
  * `HTTP_COOKIE`: The value of the HTTP cookie whose name is configured under "enforceOnKeyName". The key value is truncated to the first 128 bytes of the cookie value. If no such cookie is present in the request, the key type defaults to `ALL`.
  * `HTTP_PATH`: The URL path of the HTTP request. The key value is truncated to the first 128 bytes. 
  * `SNI`: Server name indication in the TLS session of the HTTPS request. The key value is truncated to the first 128 bytes. The key type defaults to `ALL` on a HTTP session. 
  * `REGION_CODE`: The country/region from which the request originates. 
  * `TLS_JA3_FINGERPRINT`: JA3 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2 or HTTP/3. If not available, the key type defaults to `ALL`. 
  * `USER_IP`: The IP address of the originating client, which is resolved based on "userIpRequestHeaders" configured with the security policy. If there is no "userIpRequestHeaders" configuration or an IP address cannot be resolved from it, the key type defaults to `IP`. 
  * `ASN`: The autonomous system number of the originating client. If not available, the key type defaults to `ALL`.
  * `TLS_JA4_FINGERPRINT`: JA4 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2 or HTTP/3. If not available, the key type defaults to `ALL`. 

For "fairshare" action, this value is limited to ALL i.e. a single rate limit threshold is enforced for all the requests matching the rule.   
`rateLimitOptions.enforceOnKeyName` |  `string` Rate limit key name applicable only for the following key types: HTTP_HEADER -- Name of the HTTP header whose value is taken as the key value. HTTP_COOKIE -- Name of the HTTP cookie whose value is taken as the key value.  
`rateLimitOptions.enforceOnKeyConfigs[]` |  `object` If specified, any combination of values of enforceOnKeyType/enforceOnKeyName is treated as the key on which ratelimit threshold/action is enforced. You can specify up to 3 enforceOnKeyConfigs. If enforceOnKeyConfigs is specified, enforceOnKey must not be specified.  
`rateLimitOptions.enforceOnKeyConfigs[].enforceOnKeyType` |  `enum` Determines the key to enforce the rateLimitThreshold on. Possible values are: 

  * `ALL`: A single rate limit threshold is applied to all the requests matching this rule. This is the default value if "enforceOnKeyConfigs" is not configured.
  * `IP`: The source IP address of the request is the key. Each IP has this limit enforced separately.
  * `HTTP_HEADER`: The value of the HTTP header whose name is configured under "enforceOnKeyName". The key value is truncated to the first 128 bytes of the header value. If no such header is present in the request, the key type defaults to `ALL`.
  * `XFF_IP`: The first IP address (i.e. the originating client IP address) specified in the list of IPs under X-Forwarded-For HTTP header. If no such header is present or the value is not a valid IP, the key defaults to the source IP address of the request i.e. key type `IP`.
  * `HTTP_COOKIE`: The value of the HTTP cookie whose name is configured under "enforceOnKeyName". The key value is truncated to the first 128 bytes of the cookie value. If no such cookie is present in the request, the key type defaults to `ALL`.
  * `HTTP_PATH`: The URL path of the HTTP request. The key value is truncated to the first 128 bytes. 
  * `SNI`: Server name indication in the TLS session of the HTTPS request. The key value is truncated to the first 128 bytes. The key type defaults to `ALL` on a HTTP session. 
  * `REGION_CODE`: The country/region from which the request originates. 
  * `TLS_JA3_FINGERPRINT`: JA3 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2 or HTTP/3. If not available, the key type defaults to `ALL`. 
  * `USER_IP`: The IP address of the originating client, which is resolved based on "userIpRequestHeaders" configured with the security policy. If there is no "userIpRequestHeaders" configuration or an IP address cannot be resolved from it, the key type defaults to `IP`. 
  * `ASN`: The autonomous system number of the originating client. If not available, the key type defaults to `ALL`.
  * `TLS_JA4_FINGERPRINT`: JA4 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2 or HTTP/3. If not available, the key type defaults to `ALL`. 

  
`rateLimitOptions.enforceOnKeyConfigs[].enforceOnKeyName` |  `string` Rate limit key name applicable only for the following key types: HTTP_HEADER -- Name of the HTTP header whose value is taken as the key value. HTTP_COOKIE -- Name of the HTTP cookie whose value is taken as the key value.  
`rateLimitOptions.banThreshold` |  `object` Can only be specified if the action for the rule is "rate_based_ban". If specified, the key will be banned for the configured 'banDurationSec' when the number of requests that exceed the 'rateLimitThreshold' also exceed this 'banThreshold'.  
`rateLimitOptions.banThreshold.count` |  `integer` Number of HTTP(S) requests for calculating the threshold.  
`rateLimitOptions.banThreshold.intervalSec` |  `integer` Interval over which the threshold is computed.  
`rateLimitOptions.banDurationSec` |  `integer` Can only be specified if the action for the rule is "rate_based_ban". If specified, determines the time (in seconds) the traffic will continue to be banned by the rate limit after the rate falls below the threshold.  
`headerAction` |  `object` Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`headerAction.requestHeadersToAdds[]` |  `object` The list of request headers to add or overwrite if they're already present.  
`headerAction.requestHeadersToAdds[].headerName` |  `string` The name of the header to set.  
`headerAction.requestHeadersToAdds[].headerValue` |  `string` The value to set the named header to.  
`redirectOptions` |  `object` Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`redirectOptions.type` |  `enum` Type of the redirect action. Possible values are: 

  * `GOOGLE_RECAPTCHA`: redirect to reCAPTCHA for manual challenge assessment.
  * `EXTERNAL_302`: redirect to a different URL via a 302 response.

  
`redirectOptions.target` |  `string` Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA.  
`preconfiguredWafConfig` |  `object` Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.  
`preconfiguredWafConfig.exclusions[]` |  `object` A list of exclusions to apply during preconfigured WAF evaluation.  
`preconfiguredWafConfig.exclusions[].targetRuleSet` |  `string` Target WAF rule set to apply the preconfigured WAF exclusion.  
`preconfiguredWafConfig.exclusions[].targetRuleIds[]` |  `string` A list of target rule IDs under the WAF rule set to apply the preconfigured WAF exclusion. If omitted, it refers to all the rule IDs under the WAF rule set.  
`preconfiguredWafConfig.exclusions[].requestHeadersToExclude[]` |  `object` A list of request header names whose value will be excluded from inspection during preconfigured WAF evaluation.  
`preconfiguredWafConfig.exclusions[].requestHeadersToExclude[].val` |  `string` The value of the field.  
`preconfiguredWafConfig.exclusions[].requestHeadersToExclude[].op` |  `enum` The match operator for the field.  
`preconfiguredWafConfig.exclusions[].requestCookiesToExclude[]` |  `object` A list of request cookie names whose value will be excluded from inspection during preconfigured WAF evaluation.  
`preconfiguredWafConfig.exclusions[].requestCookiesToExclude[].val` |  `string` The value of the field.  
`preconfiguredWafConfig.exclusions[].requestCookiesToExclude[].op` |  `enum` The match operator for the field.  
`preconfiguredWafConfig.exclusions[].requestQueryParamsToExclude[]` |  `object` A list of request query parameter names whose value will be excluded from inspection during preconfigured WAF evaluation. Note that the parameter can be in the query string or in the POST body.  
`preconfiguredWafConfig.exclusions[].requestQueryParamsToExclude[].val` |  `string` The value of the field.  
`preconfiguredWafConfig.exclusions[].requestQueryParamsToExclude[].op` |  `enum` The match operator for the field.  
`preconfiguredWafConfig.exclusions[].requestUrisToExclude[]` |  `object` A list of request URIs from the request line to be excluded from inspection during preconfigured WAF evaluation. When specifying this field, the query or fragment part should be excluded.  
`preconfiguredWafConfig.exclusions[].requestUrisToExclude[].val` |  `string` The value of the field.  
`preconfiguredWafConfig.exclusions[].requestUrisToExclude[].op` |  `enum` The match operator for the field.  
`preconfiguredWafConfig.exclusions[].requestBodiesToExclude[]` |  `object` A list of request body fields to be excluded from inspection during preconfigured WAF evaluation.  
`preconfiguredWafConfig.exclusions[].requestBodiesToExclude[].val` |  `string` The value of the field.  
`preconfiguredWafConfig.exclusions[].requestBodiesToExclude[].op` |  `enum` The match operator for the field.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.securityPolicies.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
