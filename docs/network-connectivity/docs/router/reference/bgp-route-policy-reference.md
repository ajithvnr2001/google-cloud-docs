---
url: https://docs.cloud.google.com/network-connectivity/docs/router/reference/bgp-route-policy-reference/
title: BGP route policy attribute reference \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:10.015679+00:00
---

# BGP route policy attribute reference  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/reference/bgp-route-policy-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BGP route policy attribute reference

This page shows example BGP route policies, using the Common Expression Language (CEL) for Cloud Router.

BGP route policies are defined as an ordered list of terms. Each term is evaluated in the order that you specify, and include both a condition and a corresponding action for when a route matches that term. A particular BGP route policy can be applied only in one direction, either inbound for learned routes, or outbound for advertised routes, but not both simultaneously. However, BGP route policies can be applied to multiple BGP peers on Cloud Router.

## Match attributes

The following table describes match attributes available for BGP route policies:

Attributes | Description  
---|---  
`communities` | List of communities attributed to the BGP route  
`destination` | The IP range for the BGP route  
  
## Match operations

The following table describes match operations available for BGP route policies:

Operation | Description  
---|---  
`communities.matchesEvery('65001:1234')` |  Returns true if communities are a superset of the list `'65001:1234'`.  A _community_value_ is a 32-bit field divided into two 16-bit sections. Conventionally, the first 16-bits of the value encode the autonomous system (AS) number of the network that the community originates from, but Cloud Router doesn't enforce this convention. The second 16-bits of the value encode a unique number assigned by the originating AS.  Restricted to import only.  
`destination == '192.168.0.0/24'` |  Returns `true` if a BGP route matches with `192.168.0.0/24` (exact match).  
`destination != '192.168.0.0/24'` |  Returns `true` if a BGP route doesn't match `192.168.0.0/24` (exact match).  
`destination.inAnyRange(r)` |  Returns `true` if a BGP route is in the range _r_ , where _r_ is one of the following:

  * A string with a CIDER-encoded prefix, such as `192.168.0.0/24`.
  * The abstract type returned by `prefix()`, or one of the fluent methods that you can call on `prefix()`, such as `longer()`.
  * A heterogeneous list where each element must be either of the values previously described.

Negatable with `!`.  
`prefix('192.168.0.0/24')` |  Returns a prefix match object representing the CIDR range `192.168.0.0/24`, used with `destination.inAnyRange()`.  
`prefix('192.168.0.0/24').longer()` |  Returns a prefix range object that's a copy of `prefix()` with the end of the range set to the input prefix's per-address family max (`/32` or `/128`), and the start of the range set to the input prefix's length plus one.  
`prefix().orLonger()` |  Returns a prefix range object that's a copy of `prefix()` with the end of the range set to the input prefix's per-address family max (`/32` or `/128`).  
`prefix().lengthRange(20, 30)` |  Returns a prefix range object that's a copy of `prefix()` with the start of the range set to /20, and the end set to /30.  
`prefix().upTo(30)` |  Returns a prefix range object that's a copy of `prefix()` with the end of the range set to the input prefix's /30.  
`communitySets('regional')` |  Returns the list of communities named in the community set `regional` on the router.  
`prefixSets('local')` |  Returns the list of prefixes named in the prefix set `local` on the router.  
`x || y` |  Return `true` if either _x_ or _y_ is `true`. _x_ and _y_ must be boolean expressions that use either the `communities` or the `destination` attribute.  
  
Due to the rules for `||` (OR) operations, all conditions are effectively zero or more `destination` match operations connected by OR. 

`(D0 || D1 || ... || Dm)`

The following table is an example of using `prefix` to build complex regular expressions compared to some router vendors:

Cloud Router | Cisco | Juniper | Explanation  
---|---|---|---  
`'192.168.0.1'` | `192.168.0.1` | `192.168.0.1` | Exactly match the prefix `192.168.0.1/32`  
`'192.168.0.0/24'` `prefix('192.168.0.0/24')` | `192.168.0.0/24` | `192.168.0.0/24 exact` | Exactly match the prefix `192.168.0.0/24`  
`prefix('192.168.0.0/24').longer()` | `192.168.0.0/24 ge 25 le 32` | `192.168.0.0/24 longer` | Match the range within `192.168.0.0/25` to `192.168.0.0/32`  
`prefix('192.168.0.0/24').orLonger()` | `192.168.0.0/24 le 32` | `192.168.0.0/24 orlonger` | Match the range within `192.168.0.0/24` to `192.168.0.0/32`  
`prefix('192.168.0.0/24').lengthRange(25, 30)` | `192.168.0.0/24 ge 25 le 30` | `192.168.0.0/24 prefix-length-range /25-/30` | Match the range within `192.168.0.0/25` to `192.168.0.0/30`  
`prefix('192.168.0.0/24').upTo(30)` | `192.168.0.0/24 le 30` | `192.168.0.0/24 up to /30` | Match the range within `192.168.0.0/24` to `192.168.0.0/30`  
  
### Match all routes

The following table describes examples that match all routes in a BGP route policy's match expression:

Operation | Description  
---|---  
`communities.matchesEvery([])` | Matches all routes for import policies.  
`destination.inAnyRange(prefix('0.0.0.0/0').orLonger())` | Matches all IPv4 addresses for either import or export policies.  
`destination.inAnyRange(prefix('::/0').orLonger())` | Matches all IPv6 addresses for either import or export policies.  
`destination.inAnyRange([prefix('0.0.0.0/0').orLonger(), prefix('::/0').orLonger()])` | Matches all routes for either import or export policies.  
  
## Action attributes

The following table describes action attributes available for BGP route policies:

Attribute | Description | Restrictions  
---|---|---  
`asPath` | The list of AS numbers the BGP route update traversed | Export and import policies  
`communities` | The route's list of communities | Export policies only  
`med` | The route's multi-exit discriminator (MED) | Export and import policies  
  
## Action operations

The following table describes action operations available for BGP route policies:

Operation | Description | Restrictions  
---|---|---  
`accept()` |  Accepts the BGP route, and stop further evaluation of BGP route policies or terms, including any actions that come after this one. | None  
`drop()` |  Filters out the BGP route, and stops further evaluation of BGP policies or terms, including any actions that come after this one. | None  
`nextPolicy()` |  Stops the execution of remaining terms in this BGP route policy (including any actions after this term), and moves on to the next applied BGP route policy (if any). | None  
`asPath.prependSequence([1, 2, 3])` |  Prepends a list of AS numbers to the AS-PATH attribute, as a sequence.   
  
The arguments must be integers within the range of 32-bits. | None  
`communities.add('65001:1234')` |  Adds the community value to the list of communities. The community value can be a single community or a list. Any community values that are private communities mapped to the following Google-owned ASNs are ignored by Cloud Router: 6432, 15169, 16550, 16591, 19448, 19527, 22859, 26910, 32381, 36039, 36384, 36385, 36492, 55023  | Export policies only  
`communities.remove('65001:1234')` |  Removes the community value from the list of communities. The community value can be a single community or a list. Any community values that are private communities mapped to the following Google-owned ASNs are ignored by Cloud Router: 6432, 15169, 16550, 16591, 19448, 19527, 22859, 26910, 32381, 36039, 36384, 36385, 36492, 55023  | Export policies only  
`communities.replaceAll(['65001:1234'])` |  Replaces the list of communities with the community value, which can be empty. Any community values that are private communities mapped to the following Google-owned ASNs are ignored by Cloud Router: 6432, 15169, 16550, 16591, 19448, 19527, 22859, 26910, 32381, 36039, 36384, 36385, 36492, 55023  | Export policies only  
`med.set(12345)` | Sets MED to `12345`. The value of MED must be an unsigned integer from `0` to `232`. | None  
`med.add(12345)` | Adds `12345` to the set value of MED. The value of MED must be an unsigned integer from `0` to `232`. If the result of the addition is greater than 232 \- 1, this operation sets MED to `232 - 1`. | None  
`med.subtract(12345)` | Subtracts `12345` from the set value of MED. The value of MED must be an unsigned integer from `0` to `232`. If the result of the subtraction is less than 0, this operation sets MED to `0`. | None  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
