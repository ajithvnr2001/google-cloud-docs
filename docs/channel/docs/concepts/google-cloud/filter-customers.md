---
url: https://docs.cloud.google.com/channel/docs/concepts/google-cloud/filter-customers/
title: Set up a customer filter using the ListCustomers API \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:50.746992+00:00
---

# Set up a customer filter using the ListCustomers API  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/concepts/google-cloud/filter-customers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Set up a customer filter using the ListCustomers API Stay organized with collections  Save and categorize content based on your preferences. 

If you need to find information about a specific customer, you can use the Cloud Channel API `filter` parameter through the [`customers.list` method](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/list).

If you use a filter, there is a short delay (usually a few seconds) during the creation of a customer. If you need access to a customer immediately after creation, we recommend using `customers.list` without a filter or [`customers.get`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/get).

## Available filters

Strings for the filter parameter support exact match, or exact match plus prefix filtering. Filters are not case sensitive.

The following table describes the available fields you can search for, and the methods they support.

External Search Key | Exact match support | Prefix support  
---|---|---  
domain | Yes | Yes  
org_display_name | Yes | Yes  
cloud_identity_id | Yes | No  
channel_partner_id | Yes | No  
  
You can find the complete filter syntax in the [API filtering guide](https://google.aip.dev/160).

### Exact match syntax

Exact match filters will only find customers that contain the same fields as those in the submitted string.

Syntax: `<domain | org_display_name | cloud_identity_id | channel_partner_id> = <value>`

Example: `domain = "domain.com" AND channel_partner_id = "12345"`

### Prefix syntax

Prefix filters allow the use of an asterisk as a wild-card symbol. This filter will find customers that have fields with the prefix, regardless of the content that comes after it.

Syntax: `<domain | org_display_name> : <value>*`

Example: `domain : "uw.com*" AND org_display_name : "prefix*"`

## Examples of filters with logical operators

Cloud Channel API filters support the use of AND and OR logical operators. You can use both operators in one filter by using a parenthetical statement.

### AND example

`domain = "domain.com" AND channel_partner_id = "12345" AND org_display_name : "display*"`

### OR example

`domain = "domain.com" OR channel_partner_id = "12345" OR org_display_name : "display*"`

### AND + OR example

`domain = "domain.com" OR (channel_partner_id = "12345" AND org_display_name : "display*" )`

You need to use parentheses if the filter contains an AND and an OR statement. The following example is not a valid filter string.

`domain = "domain.com" OR channel_partner_id = "12345" AND org_display_name : "display*`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
