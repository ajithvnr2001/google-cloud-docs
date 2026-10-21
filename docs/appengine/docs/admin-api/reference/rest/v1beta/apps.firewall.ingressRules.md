---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules
title: REST Resource: apps.firewall.ingressRules \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:12:49.514142+00:00
---

# REST Resource: apps.firewall.ingressRules  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  REST Resource: apps.firewall.ingressRules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: FirewallRule
    * JSON representation
  * Action
  * Methods



## Resource: FirewallRule

A single firewall rule that is evaluated against incoming traffic and provides an action to take on matched requests.

JSON representation  
---  
      
    
    {
      "priority": integer,
      "action": enum ([Action](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules#Action)),
      "sourceRange": string,
      "description": string
    }  
  
Fields  
---  
`priority` |  `integer` A positive integer between [1, Int32.MaxValue-1] that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user.  
`action` |  `enum (`[Action](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules#Action)`)` The action to take on matched requests.  
`sourceRange` |  `string` IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.Truncation will be silently performed on addresses which are not properly truncated. For example, `1.2.3.4/24` is accepted as the same address as `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` is accepted as the same address as `2001:db8::/32`.  
`description` |  `string` An optional string description of this rule. This field has a maximum length of 400 characters.  
  
## Action

Available actions to take on matching requests.

Enums  
---  
`UNSPECIFIED_ACTION` |   
`ALLOW` | Matching requests are allowed.  
`DENY` | Matching requests are denied.  
  
## Methods  
  
---  
  
### `[batchUpdate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/batchUpdate)`

|  Replaces the entire firewall ruleset in one bulk operation.  
  
### `[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/create)`

|  Creates a firewall rule for the application.  
  
### `[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/delete)`

|  Deletes the specified firewall rule.  
  
### `[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/get)`

|  Gets the specified firewall rule.  
  
### `[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/list)`

|  Lists the firewall rules of an application.  
  
### `[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/patch)`

|  Updates the specified firewall rule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
