---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationSecurityPolicies/insert/
title: Method: organizationSecurityPolicies.insert \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:58.122355+00:00
---

# Method: organizationSecurityPolicies.insert  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/organizationSecurityPolicies/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: organizationSecurityPolicies.insert Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
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
        * JSON representation
        * JSON representation
      * JSON representation
        * JSON representation
      * JSON representation
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
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-10-01-preview

Creates a new policy in the specified organization using the data included in the request.

Use this API to add Cloud Armor policies. Previously, alpha and beta versions of this API were used to add firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.insert instead.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/locations/global/securityPolicies?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`requestId` |  `string` An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`).  
`parentId` |  `string` Parent ID for this request. The ID can be either be "folders/[FOLDER_ID]" if the parent is a folder or "organizations/[ORGANIZATION_ID]" if the parent is an organization.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userDefinedFields": [
        {
          "name": string,
          "base": enum,
          "offset": integer,
          "size": integer,
          "mask": string
        }
      ],
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "rules": [
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
      ],
      "adaptiveProtectionConfig": {
        "layer7DdosDefenseConfig": {
          "enable": boolean,
          "ruleVisibility": enum,
          "thresholdConfigs": [
            {
              "name": string,
              "autoDeployLoadThreshold": number,
              "autoDeployConfidenceThreshold": number,
              "autoDeployImpactedBaselineThreshold": number,
              "autoDeployExpirationSec": integer,
              "detectionLoadThreshold": number,
              "detectionAbsoluteQps": number,
              "detectionRelativeToBaselineQps": number,
              "trafficGranularityConfigs": [
                {
                  "type": enum,
                  "value": string,
                  "enableEachUniqueValue": boolean
                }
              ]
            }
          ]
        }
      },
      "ddosProtectionConfig": {
        "ddosProtection": enum,
        "ddosAdaptiveProtection": enum,
        "ddosImpactedBaselineThreshold": number
      },
      "advancedOptionsConfig": {
        "jsonParsing": enum,
        "jsonCustomConfig": {
          "contentTypes": [
            string
          ]
        },
        "logLevel": enum,
        "userIpRequestHeaders": [
          string
        ],
        "requestBodyInspectionSize": string
      },
      "recaptchaOptionsConfig": {
        "redirectSiteKey": string
      },
      "fingerprint": string,
      "selfLink": string,
      "type": enum,
      "associations": [
        {
          "name": string,
          "attachmentId": string,
          "excludedProjects": [
            string
          ],
          "excludedFolders": [
            string
          ],
          "securityPolicyId": string,
          "shortName": string,
          "displayName": string
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "labelFingerprint": string,
      "shortName": string,
      "parent": string,
      "region": string
    }  
  
Fields  
---  
`userDefinedFields[]` |  `object` Definitions of user-defined fields for CLOUD_ARMOR_NETWORK policies. A user-defined field consists of up to 4 bytes extracted from a fixed offset in the packet, relative to the IPv4, IPv6, TCP, or UDP header, with an optional mask to select certain bits. Rules may then specify matching values for these fields.Example:userDefinedFields: - name: "ipv4_fragment_offset" base: IPV4 offset: 6 size: 2 mask: "0x1fff"  
`userDefinedFields[].name` |  `string` The name of this field. Must be unique within the policy.  
`userDefinedFields[].base` |  `enum` The base relative to which 'offset' is measured. Possible values are: 

  * `IPV4`: Points to the beginning of the IPv4 header.
  * `IPV6`: Points to the beginning of the IPv6 header.
  * `TCP`: Points to the beginning of the TCP header, skipping over any IPv4 options or IPv6 extension headers. Not present for non-first fragments.
  * `UDP`: Points to the beginning of the UDP header, skipping over any IPv4 options or IPv6 extension headers. Not present for non-first fragments.

required   
`userDefinedFields[].offset` |  `integer` Offset of the first byte of the field (in network byte order) relative to 'base'.  
`userDefinedFields[].size` |  `integer` Size of the field in bytes. Valid values: 1-4.  
`userDefinedFields[].mask` |  `string` If specified, apply this mask (bitwise AND) to the field to ignore bits before matching. Encoded as a hexadecimal number (starting with "0x"). The last byte of the field (in network byte order) corresponds to the least significant byte of the mask.  
`kind` |  `string` Output only. Type of the resource. Always `compute#securityPolicy`for security policies  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`rules[]` |  `object` A list of rules that belong to this policy. There must always be a default rule which is a rule with priority 2147483647 and match all condition (for the match condition this means match "*" for srcIpRanges and for the networkMatch condition every field must be either match "*" or not set). If no rules are provided when creating a security policy, a default rule with action "allow" will be added.  
`rules[].kind` |  `string` Output only. Type of the resource. Always `compute#securityPolicyRule` for security policy rules  
`rules[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`rules[].priority` |  `integer` An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.  
`rules[].match` |  `object` A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.  
`rules[].match.expr` |  `object` User defined CEVAL expression. A CEVAL expression is used to specify match criteria such as origin.ip, source.region_code and contents in the request header. Expressions containing `evaluateThreatIntelligence` require a Cloud Armor Enterprise subscription and are not supported in Edge Policies nor in Regional Policies. Expressions containing `evaluatePreconfiguredExpr('sourceiplist-*')` require a Cloud Armor Enterprise subscription and are only supported in Global Security Policies.  
`rules[].match.expr.expression` |  `string` Textual representation of an expression in Common Expression Language syntax.  
`rules[].match.expr.title` |  `string` Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`rules[].match.expr.description` |  `string` Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`rules[].match.expr.location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
`rules[].match.exprOptions` |  `object` The configuration options available when specifying a user defined CEVAL expression (i.e., 'expr').  
`rules[].match.exprOptions.recaptchaOptions` |  `object` reCAPTCHA configuration options to be applied for the rule. If the rule does not evaluate reCAPTCHA tokens, this field has no effect.  
`rules[].match.exprOptions.recaptchaOptions.actionTokenSiteKeys[]` |  `string` A list of site keys to be used during the validation of reCAPTCHA action-tokens. The provided site keys need to be created from reCAPTCHA API under the same project where the security policy is created.  
`rules[].match.exprOptions.recaptchaOptions.sessionTokenSiteKeys[]` |  `string` A list of site keys to be used during the validation of reCAPTCHA session-tokens. The provided site keys need to be created from reCAPTCHA API under the same project where the security policy is created.  
`rules[].match.versionedExpr` |  `enum` Preconfigured versioned expression. If this field is specified, config must also be specified. Available preconfigured expressions along with their requirements are: SRC_IPS_V1 - must specify the corresponding srcIpRange field in config.  
`rules[].match.config` |  `object` The configuration options available when specifying versionedExpr. This field must be specified if versionedExpr is specified and cannot be specified if versionedExpr is not specified.  
`rules[].match.config.srcIpRanges[]` |  `string` CIDR IP address range. Maximum number of srcIpRanges allowed is 10.  
`rules[].networkMatch` |  `object` A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.Example:networkMatch: srcIpRanges: - "192.0.2.0/24" - "198.51.100.0/24" userDefinedFields: - name: "ipv4_fragment_offset" values: - "1-0x1fff"The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.  
`rules[].networkMatch.userDefinedFields[]` |  `object` User-defined fields. Each element names a defined field and lists the matching values for that field.  
`rules[].networkMatch.userDefinedFields[].name` |  `string` Name of the user-defined field, as given in the definition.  
`rules[].networkMatch.userDefinedFields[].values[]` |  `string` Matching values of the field. Each element can be a 32-bit unsigned decimal or hexadecimal (starting with "0x") number (e.g. "64") or range (e.g. "0x400-0x7ff").  
`rules[].networkMatch.srcIpRanges[]` |  `string` Source IPv4/IPv6 addresses or CIDR prefixes, in standard text format.  
`rules[].networkMatch.destIpRanges[]` |  `string` Destination IPv4/IPv6 addresses or CIDR prefixes, in standard text format.  
`rules[].networkMatch.ipProtocols[]` |  `string` IPv4 protocol / IPv6 next header (after extension headers). Each element can be an 8-bit unsigned decimal number (e.g. "6"), range (e.g. "253-254"), or one of the following protocol names: "tcp", "udp", "icmp", "esp", "ah", "ipip", or "sctp".  
`rules[].networkMatch.srcPorts[]` |  `string` Source port numbers for TCP/UDP/SCTP. Each element can be a 16-bit unsigned decimal number (e.g. "80") or range (e.g. "0-1023").  
`rules[].networkMatch.destPorts[]` |  `string` Destination port numbers for TCP/UDP/SCTP. Each element can be a 16-bit unsigned decimal number (e.g. "80") or range (e.g. "0-1023").  
`rules[].networkMatch.srcRegionCodes[]` |  `string` Two-letter ISO 3166-1 alpha-2 country code associated with the source IP address.  
`rules[].networkMatch.srcAsns[]` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` BGP Autonomous System Number associated with the source IP address.  
`rules[].action` |  `string` The Action to perform when the rule is matched. The following are the valid actions: 

  * `allow`: allow access to target.
  * `deny(STATUS)`: deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502.
  * `rate_based_ban`: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rateLimitOptions to be set.
  * `redirect`: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR.
  * `throttle`: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rateLimitOptions to be set for this.
  * `fairshare (preview only)`: when traffic reaches the threshold limit, requests from the clients matching this rule begin to be rate-limited using the Fair Share algorithm. This action is only allowed in security policies of type `CLOUD_ARMOR_INTERNAL_SERVICE`.

  
`rules[].preview` |  `boolean` If set to true, the specified action is not enforced.  
`rules[].rateLimitOptions` |  `object` Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.  
`rules[].rateLimitOptions.rateLimitThreshold` |  `object` Threshold at which to begin ratelimiting.  
`rules[].rateLimitOptions.rateLimitThreshold.count` |  `integer` Number of HTTP(S) requests for calculating the threshold.  
`rules[].rateLimitOptions.rateLimitThreshold.intervalSec` |  `integer` Interval over which the threshold is computed.  
`rules[].rateLimitOptions.conformAction` |  `string` Action to take for requests that are under the configured rate limit threshold. Valid option is "allow" only.  
`rules[].rateLimitOptions.exceedAction` |  `string` Action to take for requests that are above the configured rate limit threshold, to either deny with a specified HTTP response code, or redirect to a different endpoint. Valid options are `deny(STATUS)`, where valid values for `STATUS` are 403, 404, 429, and 502, and `redirect`, where the redirect parameters come from `exceedRedirectOptions` below. The `redirect` action is only supported in Global Security Policies of type CLOUD_ARMOR.  
`rules[].rateLimitOptions.exceedRedirectOptions` |  `object` Parameters defining the redirect action that is used as the exceed action. Cannot be specified if the exceed action is not redirect. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`rules[].rateLimitOptions.exceedRedirectOptions.type` |  `enum` Type of the redirect action. Possible values are: 

  * `GOOGLE_RECAPTCHA`: redirect to reCAPTCHA for manual challenge assessment.
  * `EXTERNAL_302`: redirect to a different URL via a 302 response.

  
`rules[].rateLimitOptions.exceedRedirectOptions.target` |  `string` Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA.  
`rules[].rateLimitOptions.enforceOnKey` |  `enum` Determines the key to enforce the rateLimitThreshold on. Possible values are: 

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
`rules[].rateLimitOptions.enforceOnKeyName` |  `string` Rate limit key name applicable only for the following key types: HTTP_HEADER -- Name of the HTTP header whose value is taken as the key value. HTTP_COOKIE -- Name of the HTTP cookie whose value is taken as the key value.  
`rules[].rateLimitOptions.enforceOnKeyConfigs[]` |  `object` If specified, any combination of values of enforceOnKeyType/enforceOnKeyName is treated as the key on which ratelimit threshold/action is enforced. You can specify up to 3 enforceOnKeyConfigs. If enforceOnKeyConfigs is specified, enforceOnKey must not be specified.  
`rules[].rateLimitOptions.enforceOnKeyConfigs[].enforceOnKeyType` |  `enum` Determines the key to enforce the rateLimitThreshold on. Possible values are: 

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

  
`rules[].rateLimitOptions.enforceOnKeyConfigs[].enforceOnKeyName` |  `string` Rate limit key name applicable only for the following key types: HTTP_HEADER -- Name of the HTTP header whose value is taken as the key value. HTTP_COOKIE -- Name of the HTTP cookie whose value is taken as the key value.  
`rules[].rateLimitOptions.banThreshold` |  `object` Can only be specified if the action for the rule is "rate_based_ban". If specified, the key will be banned for the configured 'banDurationSec' when the number of requests that exceed the 'rateLimitThreshold' also exceed this 'banThreshold'.  
`rules[].rateLimitOptions.banThreshold.count` |  `integer` Number of HTTP(S) requests for calculating the threshold.  
`rules[].rateLimitOptions.banThreshold.intervalSec` |  `integer` Interval over which the threshold is computed.  
`rules[].rateLimitOptions.banDurationSec` |  `integer` Can only be specified if the action for the rule is "rate_based_ban". If specified, determines the time (in seconds) the traffic will continue to be banned by the rate limit after the rate falls below the threshold.  
`rules[].headerAction` |  `object` Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`rules[].headerAction.requestHeadersToAdds[]` |  `object` The list of request headers to add or overwrite if they're already present.  
`rules[].headerAction.requestHeadersToAdds[].headerName` |  `string` The name of the header to set.  
`rules[].headerAction.requestHeadersToAdds[].headerValue` |  `string` The value to set the named header to.  
`rules[].redirectOptions` |  `object` Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`rules[].redirectOptions.type` |  `enum` Type of the redirect action. Possible values are: 

  * `GOOGLE_RECAPTCHA`: redirect to reCAPTCHA for manual challenge assessment.
  * `EXTERNAL_302`: redirect to a different URL via a 302 response.

  
`rules[].redirectOptions.target` |  `string` Target for the redirect action. This is required if the type is EXTERNAL_302 and cannot be specified for GOOGLE_RECAPTCHA.  
`rules[].preconfiguredWafConfig` |  `object` Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.  
`rules[].preconfiguredWafConfig.exclusions[]` |  `object` A list of exclusions to apply during preconfigured WAF evaluation.  
`rules[].preconfiguredWafConfig.exclusions[].targetRuleSet` |  `string` Target WAF rule set to apply the preconfigured WAF exclusion.  
`rules[].preconfiguredWafConfig.exclusions[].targetRuleIds[]` |  `string` A list of target rule IDs under the WAF rule set to apply the preconfigured WAF exclusion. If omitted, it refers to all the rule IDs under the WAF rule set.  
`rules[].preconfiguredWafConfig.exclusions[].requestHeadersToExclude[]` |  `object` A list of request header names whose value will be excluded from inspection during preconfigured WAF evaluation.  
`rules[].preconfiguredWafConfig.exclusions[].requestHeadersToExclude[].val` |  `string` The value of the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestHeadersToExclude[].op` |  `enum` The match operator for the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestCookiesToExclude[]` |  `object` A list of request cookie names whose value will be excluded from inspection during preconfigured WAF evaluation.  
`rules[].preconfiguredWafConfig.exclusions[].requestCookiesToExclude[].val` |  `string` The value of the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestCookiesToExclude[].op` |  `enum` The match operator for the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestQueryParamsToExclude[]` |  `object` A list of request query parameter names whose value will be excluded from inspection during preconfigured WAF evaluation. Note that the parameter can be in the query string or in the POST body.  
`rules[].preconfiguredWafConfig.exclusions[].requestQueryParamsToExclude[].val` |  `string` The value of the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestQueryParamsToExclude[].op` |  `enum` The match operator for the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestUrisToExclude[]` |  `object` A list of request URIs from the request line to be excluded from inspection during preconfigured WAF evaluation. When specifying this field, the query or fragment part should be excluded.  
`rules[].preconfiguredWafConfig.exclusions[].requestUrisToExclude[].val` |  `string` The value of the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestUrisToExclude[].op` |  `enum` The match operator for the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestBodiesToExclude[]` |  `object` A list of request body fields to be excluded from inspection during preconfigured WAF evaluation.  
`rules[].preconfiguredWafConfig.exclusions[].requestBodiesToExclude[].val` |  `string` The value of the field.  
`rules[].preconfiguredWafConfig.exclusions[].requestBodiesToExclude[].op` |  `enum` The match operator for the field.  
`adaptiveProtectionConfig` |  `object`  
`adaptiveProtectionConfig.layer7DdosDefenseConfig` |  `object` If set to true, enables Cloud Armor Machine Learning.  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.enable` |  `boolean` If set to true, enables CAAP for L7 DDoS detection. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.ruleVisibility` |  `enum` Rule visibility can be one of the following: STANDARD - opaque rules. (default) PREMIUM - transparent rules. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[]` |  `object` Configuration options for layer7 adaptive protection for various customizable thresholds.  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].name` |  `string` The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). The name must be unique within the security policy.  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].autoDeployLoadThreshold` |  `number`  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].autoDeployConfidenceThreshold` |  `number`  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].autoDeployImpactedBaselineThreshold` |  `number`  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].autoDeployExpirationSec` |  `integer`  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].detectionLoadThreshold` |  `number`  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].detectionAbsoluteQps` |  `number`  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].detectionRelativeToBaselineQps` |  `number`  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].trafficGranularityConfigs[]` |  `object` Configuration options for enabling Adaptive Protection to operate on specified granular traffic units.  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].trafficGranularityConfigs[].type` |  `enum` Type of this configuration.  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].trafficGranularityConfigs[].value` |  `string` Requests that match this value constitute a granular traffic unit.  
`adaptiveProtectionConfig.layer7DdosDefenseConfig.thresholdConfigs[].trafficGranularityConfigs[].enableEachUniqueValue` |  `boolean` If enabled, traffic matching each unique value for the specified type constitutes a separate traffic unit. It can only be set to true if `value` is empty.  
`ddosProtectionConfig` |  `object`  
`ddosProtectionConfig.ddosProtection` |  `enum`  
`ddosProtectionConfig.ddosAdaptiveProtection` |  `enum`  
`ddosProtectionConfig.ddosImpactedBaselineThreshold` |  `number` DDoS Protection for Network Load Balancers (and VMs with public IPs) builds DDoS mitigations that minimize collateral damage. It quantifies this as the fraction of a non-abuse baseline that's inadvertently blocked.Rules whose collateral damage exceeds ddosImpactedBaselineThreshold will not be deployed. Using a lower value will prioritize keeping collateral damage low, possibly at the cost of its effectiveness in rate limiting some or all of the attack. It should typically be unset, so Advanced DDoS (and Adaptive Protection) uses the best mitigation it can find. Setting the threshold is advised if there are logs for false positive detections with high collateral damage, and will cause Advanced DDoS to attempt to find a less aggressive rule that satisfies the constraint. If a suitable rule cannot be found, the system falls back to either no mitigation for smaller attacks or broader network throttles for larger ones.  
`advancedOptionsConfig` |  `object`  
`advancedOptionsConfig.jsonParsing` |  `enum`  
`advancedOptionsConfig.jsonCustomConfig` |  `object` Custom configuration to apply the JSON parsing. Only applicable when jsonParsing is set to STANDARD.  
`advancedOptionsConfig.jsonCustomConfig.contentTypes[]` |  `string` A list of custom Content-Type header values to apply the JSON parsing.As per RFC 1341, a Content-Type header value has the following format:Content-Type := type "/" subtype *[";" parameter]When configuring a custom Content-Type header value, only the type/subtype needs to be specified, and the parameters should be excluded.  
`advancedOptionsConfig.logLevel` |  `enum`  
`advancedOptionsConfig.userIpRequestHeaders[]` |  `string` An optional list of case-insensitive request header names to use for resolving the callers client IP address.  
`advancedOptionsConfig.requestBodyInspectionSize` |  `string` The maximum request size chosen by the customer with Waf enabled. Values supported are "8KB", "16KB, "32KB", "48KB" and "64KB". Values are case insensitive.  
`recaptchaOptionsConfig` |  `object`  
`recaptchaOptionsConfig.redirectSiteKey` |  `string` An optional field to supply a reCAPTCHA site key to be used for all the rules using the redirect action with the type of GOOGLE_RECAPTCHA under the security policy. The specified site key needs to be created from the reCAPTCHA API. The user is responsible for the validity of the specified site key. If not specified, a Google-managed site key is used. This field is only supported in Global Security Policies of type CLOUD_ARMOR.  
`fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Specifies a fingerprint for this resource, which is essentially a hash of the metadata's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update metadata. You must always provide an up-to-date fingerprint hash in order to update or change metadata, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make `get()` request to the security policy.A base64-encoded string.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`type` |  `enum` The type indicates the intended use of the security policy. 

  * `CLOUD_ARMOR`: Cloud Armor backend security policies can be configured to filter incoming HTTP requests targeting backend services. They filter requests before they hit the origin servers.
  * `CLOUD_ARMOR_EDGE`: Cloud Armor edge security policies can be configured to filter incoming HTTP requests targeting backend services (including Cloud CDN-enabled) as well as backend buckets (Cloud Storage). They filter requests before the request is served from Google's cache.
  * `CLOUD_ARMOR_INTERNAL_SERVICE (preview only)`: Cloud Armor internal service policies can be configured to filter HTTP requests targeting services managed by Traffic Director in a service mesh. They filter requests before the request is served from the application.


* `CLOUD_ARMOR_NETWORK`: Cloud Armor network policies can be configured to filter packets targeting network load balancing resources such as backend services, target pools, target instances, and instances with external IPs. They filter requests before the request is served from the application.
This field can be set only at resource creation time.   
`associations[]` |  `object` A list of associations that belong to this policy.  
`associations[].name` |  `string` The name for an association.  
`associations[].attachmentId` |  `string` The resource that the security policy is attached to.  
`associations[].excludedProjects[]` |  `string` A list of projects to exclude from the security policy.  
`associations[].excludedFolders[]` |  `string` A list of folders to exclude from the security policy.  
`associations[].securityPolicyId` |  `string` Output only. The security policy ID of the association.  
`associations[].shortName` |  `string` Output only. The short name of the security policy of the association.  
`associations[].displayName  
**(deprecated)**` |  `string` Output only. The display name of the security policy of the association.  
`labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty.  
`labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this security policy, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels.To see the latest fingerprint, make `get()` request to the security policy.A base64-encoded string.  
`shortName` |  `string` User-provided name of the organization security policy. The name should be unique in the organization in which the security policy is created. This should only be used when SecurityPolicyType is CLOUD_ARMOR. The name must be 1-63 characters long, and comply with <https://www.ietf.org/rfc/rfc1035.txt>. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`parent` |  `string` Output only. The parent of the security policy.  
`region` |  `string` Output only. URL of the region where the regional security policy resides. This field is not applicable to global security policies.  
  
### Response body

Represents an Operation resource.

Google Compute Engine has three Operation resources:

  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations)
  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations)



You can use an operation resource to manage asynchronous API requests. For more information, read [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses).

Operations can be global, regional or zonal. 

  * For global operations, use the `globalOperations` resource.
  * For regional operations, use the `regionOperations` resource.
  * For zonal operations, use the `zoneOperations` resource.



For more information, read [ Global, Regional, and Zonal Resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

Note that completed Operation resources have a limited [ retention period.](https://cloud.google.com/compute/docs/instances/viewing-compute-operations#operation-retention-period)

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "zone": string,
      "clientOperationId": string,
      "operationType": string,
      "targetLink": string,
      "targetId": string,
      "status": enum,
      "statusMessage": string,
      "user": string,
      "progress": integer,
      "insertTime": string,
      "startTime": string,
      "endTime": string,
      "error": {
        "errors": [
          {
            "code": string,
            "location": string,
            "message": string,
            "errorDetails": [
              {
                "errorInfo": {
                  "reason": string,
                  "domain": string,
                  "metadatas": {
                    string: string,
                    ...
                  }
                },
                "quotaInfo": {
                  "metricName": string,
                  "limitName": string,
                  "dimensions": {
                    string: string,
                    ...
                  },
                  "limit": number,
                  "futureLimit": number,
                  "rolloutStatus": enum
                },
                "help": {
                  "links": [
                    {
                      "description": string,
                      "url": string
                    }
                  ]
                },
                "localizedMessage": {
                  "locale": string,
                  "message": string
                }
              }
            ]
          }
        ]
      },
      "warnings": [
        {
          "code": enum,
          "message": string,
          "data": [
            {
              "key": string,
              "value": string
            }
          ]
        }
      ],
      "httpErrorStatusCode": integer,
      "httpErrorMessage": string,
      "selfLink": string,
      "region": string,
      "description": string,
      "operationGroupId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "setCommonInstanceMetadataOperationMetadata": {
        "clientOperationId": string,
        "perLocationOperations": {
          string: {
            "state": enum,
            "error": {
              "code": integer,
              "message": string,
              "details": [
                {
                  "@type": string,
                  field1: ...,
                  ...
                }
              ]
            }
          },
          ...
        }
      },
      "instancesBulkInsertOperationMetadata": {
        "perLocationStatus": {
          string: {
            "status": enum,
            "targetVmCount": integer,
            "createdVmCount": integer,
            "failedToCreateVmCount": integer,
            "deletedVmCount": integer
          },
          ...
        }
      },
      "getVersionOperationMetadata": {
        "inlineSbomInfo": {
          "currentComponentVersions": {
            string: string,
            ...
          },
          "targetComponentVersions": {
            string: string,
            ...
          }
        }
      },
      "getHealthOperationMetadata": {
        "healthInfo": {
          "healthStatus": enum,
          "unhealthyReason": enum,
          "repairCategory": enum,
          "availabilitySloStatus": enum,
          "updateTime": string
        }
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#operation` for Operation resources.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the operation. This identifier is defined by the server.  
`creationTimestamp` |  `string` [Deprecated] This field is deprecated.  
`name` |  `string` Output only. Name of the operation.  
`zone` |  `string` Output only. The URL of the zone where the operation resides. Only applicable when performing per-zone operations.  
`clientOperationId` |  `string` Output only. The value of `requestId` if you provided it in the request. Not present otherwise.  
`operationType` |  `string` Output only. The type of operation, such as `insert`, `update`, or `delete`, and so on.  
`targetLink` |  `string` Output only. The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the disk that the snapshot was created from.  
`targetId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique target ID, which identifies a specific incarnation of the target resource.  
`status` |  `enum` Output only. The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`.  
`statusMessage` |  `string` Output only. An optional textual description of the current status of the operation.  
`user` |  `string` Output only. User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`.  
`progress` |  `integer` Output only. An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses.  
`insertTime` |  `string` Output only. The time that this operation was requested. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`startTime` |  `string` Output only. The time that this operation was started by the server. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`endTime` |  `string` Output only. The time that this operation was completed. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`error` |  `object` Output only. If errors are generated during processing of the operation, this field will be populated.  
`error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`warnings[]` |  `object` Output only. If warning messages are generated during processing of the operation, this field will be populated.  
`warnings[].code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warnings[].message` |  `string` Output only. A human-readable description of the warning code.  
`warnings[].data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warnings[].data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warnings[].data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`httpErrorStatusCode` |  `integer` Output only. If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found.  
`httpErrorMessage` |  `string` Output only. If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`region` |  `string` Output only. The URL of the region where the operation resides. Only applicable when performing regional operations.  
`description` |  `string` Output only. A textual description of the operation, which is set when the operation is created.  
`operationGroupId` |  `string` Output only. An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request.  
Output only. Service-specific metadata attached to this operation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`setCommonInstanceMetadataOperationMetadata` |  `object` Output only. If the operation is for projects.setCommonInstanceMetadata, this field will contain information on all underlying zonal actions and their state.  
`setCommonInstanceMetadataOperationMetadata.clientOperationId` |  `string` Output only. The client operation id.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[]` |  `map (key: string, value: object)` Output only. Status information per location (location name is key). Example key: zones/us-central1-a  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].state` |  `enum` Output only. Status of the action, which can be one of the following: `PROPAGATING`, `PROPAGATED`, `ABANDONED`, `FAILED`, or `DONE`.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error` |  `object` Output only. If state is `ABANDONED` or `FAILED`, this field is populated.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`instancesBulkInsertOperationMetadata` |  `object`  
`instancesBulkInsertOperationMetadata.perLocationStatus[]` |  `map (key: string, value: object)` Status information per location (location name is key). Example key: zones/us-central1-a  
`instancesBulkInsertOperationMetadata.perLocationStatus[].status` |  `enum` Output only. Creation status of BulkInsert operation - information if the flow is rolling forward or rolling back.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].targetVmCount` |  `integer` Output only. Count of VMs originally planned to be created.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].createdVmCount` |  `integer` Output only. Count of VMs successfully created so far.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].failedToCreateVmCount` |  `integer` Output only. Count of VMs that started creating but encountered an error.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].deletedVmCount` |  `integer` Output only. Count of VMs that got deleted during rollback.  
`getVersionOperationMetadata` |  `object`  
`getVersionOperationMetadata.inlineSbomInfo` |  `object`  
`getVersionOperationMetadata.inlineSbomInfo.currentComponentVersions` |  `map (key: string, value: string)` A mapping of components to their currently-applied versions or other appropriate identifiers.  
`getVersionOperationMetadata.inlineSbomInfo.targetComponentVersions` |  `map (key: string, value: string)` A mapping of components to their target versions or other appropriate identifiers.  
`getHealthOperationMetadata` |  `object` Output only. Metadata for GetHealth operations.  
`getHealthOperationMetadata.healthInfo` |  `object` Output only. The health information.  
`getHealthOperationMetadata.healthInfo.healthStatus` |  `enum` Output only. The health status.  
`getHealthOperationMetadata.healthInfo.unhealthyReason` |  `enum` Output only. The reason for unhealthy status.  
`getHealthOperationMetadata.healthInfo.repairCategory` |  `enum` Output only. The repair category.  
`getHealthOperationMetadata.healthInfo.availabilitySloStatus` |  `enum` Output only. The availability SLO status.  
`getHealthOperationMetadata.healthInfo.updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when health info was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.securityPolicies.create`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
