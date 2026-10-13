---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/
title: REST Resource: responsePolicyRules \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:22.432176+00:00
---

# REST Resource: responsePolicyRules  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  REST Resource: responsePolicyRules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ResponsePolicyRule
    * JSON representation
  * LocalData
    * JSON representation
  * Behavior
  * Methods



## Resource: ResponsePolicyRule

A Response Policy Rule is a selector that applies its behavior to queries that match the selector. Selectors are DNS names, which may be wildcards or exact matches. Each DNS query subject to a Response Policy matches at most one ResponsePolicyRule, as identified by the dnsName field with the longest matching suffix.

JSON representation  
---  
      
    
    {
      "ruleName": string,
      "kind": string,
    
      // Union field selector can be only one of the following:
      "dnsName": string
      // End of list of possible types for union field selector.
    
      // Union field action can be only one of the following:
      "localData": {
        object ([LocalData](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules#LocalData))
      },
      "behavior": enum ([Behavior](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules#Behavior))
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
`ruleName` |  `string` An identifier for this rule. Must be unique with the ResponsePolicy.  
`kind` |  `string`  
Union field `selector`.`selector` can be only one of the following:  
`dnsName` |  `string` The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule.  
Union field `action`.`action` can be only one of the following:  
`localData` |  `object (`[LocalData](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules#LocalData)`)` Answer this query directly with DNS data. These ResourceRecordSets override any other DNS behavior for the matched name; in particular they override private zones, the public internet, and GCP internal DNS. No SOA nor NS types are allowed.  
`behavior` |  `enum (`[Behavior](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules#Behavior)`)` Answer this query with a behavior rather than DNS data.  
  
## LocalData

JSON representation  
---  
      
    
    {
      "localDatas": [
        {
          object ([ResourceRecordSet](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet))
        }
      ]
    }  
  
Fields  
---  
`localDatas[]` |  `object (`[ResourceRecordSet](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet)`)` All resource record sets for this selector, one per resource record type. The name must match the dnsName.  
  
## Behavior

Enums  
---  
`behaviorUnspecified` |   
`bypassResponsePolicy` | Skip a less-specific Response Policy Rule and let the query logic continue. This mechanism, when used with wildcard selectors, lets you exempt specific subdomains from a broader Response Policy Rule and direct the queries to the public internet instead. For example, if the following rules exist:
    
    
    *.example.com -> LocalData 1.2.3.4
    foo.example.com -> Behavior 'passthrough'
    

A query for foo.example.com skips the wildcard rule.This functionality also facilitates allowlisting. Response Policy Zones (RPZs) can be applied at multiple levels within the hierarchy: for example, an organization, a folder, a project, or a VPC network. If an RPZ rule is applied at a higher level, adding a `passthrough` rule at a lower level will override it. Queries from affected virtual machines (VMs) to that domain bypass the RPZ and proceed with normal resolution.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/create)`

|  Creates a new Response Policy Rule.  
  
### `[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/delete)`

|  Deletes a previously created Response Policy Rule.  
  
### `[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/get)`

|  Fetches the representation of an existing Response Policy Rule.  
  
### `[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/list)`

|  Enumerates all Response Policy Rules associated with a project.  
  
### `[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/patch)`

|  Applies a partial update to an existing Response Policy Rule.  
  
### `[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/update)`

|  Updates an existing Response Policy Rule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
