---
url: https://docs.cloud.google.com/appengine/docs/flexible/creating-firewalls/
title: Creating App Engine firewall rules \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:13.047250+00:00
---

# Creating App Engine firewall rules  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/creating-firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Creating App Engine firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

In App Engine, you can create a firewall with up to 1000 prioritized individual rules that either allow or restrict a range of IP addresses and subnets. Your app will only respond to requests that are allowed by the firewall.

To learn how the App Engine firewall works, see [Understanding firewalls](https://docs.cloud.google.com/appengine/docs/flexible/understanding-firewalls).

## Before you begin

Before you can create App Engine firewall rules for your app, you must have one of the following [App Engine IAM roles](https://docs.cloud.google.com/appengine/docs/flexible/access-control), which include the necessary privileges for creating or modifying firewall rules:

  * App Engine Admin
  * Editor
  * Owner



## Creating firewall rules

Use one of the following methods to create a firewall rule. Repeat these steps for each additional rule:

Console

Use the Firewall rules page in Google Cloud console to create a firewall rule: 

  1. Go to the Create a firewall rule page in Google Cloud console: 

[ Go to the Create a firewall rule page](https://console.cloud.google.com/appengine/firewall/create)

  2. Specify the details of the firewall rule: 

     1. In **Priority** , enter an integer to specify the relative importance of the rule and define the order of when the rule is evaluated. 

Valid values are `1` to `2147483646`. Priority `1` is the first rule evaluated. Priority `2147483647` is the last rule evaluated and is reserved for the `default` rule. 

**Important** : After a rule is created, you cannot edit the priority value. You must delete and then recreate a rule to change the value of a rule's priority. 
     2. In **Action on match** , specify whether to allow or deny access for requests that match the rule. Rules set to `allow` forward the request to the app. Rules set to `deny` respond to requests with a `403 Forbidden` error. 
     3. In **IP range** , define the range of IP addresses that apply to the rule. The IP address range must be defined in [CIDR notation](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing), can include subnet masks, and support both IPv4 and IPv6. 
     4. Optional: In **Description** , include a description of the rule that is no longer than 100 characters. 
  3. Click **Save** to create the rule. 
  4. Test the rule to ensure that the priority and action provide the expected behavior: 
     1. Click **Test IP address**. 
     2. Enter the IP address that you want to validate and then click **Test** to ensure that the corresponding rule gets correctly evaluated. 

gcloud

Run the following [`gcloud app firewall-rules`](https://docs.cloud.google.com/sdk/gcloud/reference/app/firewall-rules) commands to create a firewall rule: 

  1. Run the following command to create a firewall rule: 
         
         gcloud app firewall-rules create PRIORITY --action ALLOW_OR_DENY --source-range IP_RANGE --description DESCRIPTION

where: 
     * PRIORITY is an integer between `1` and `2147483646` that defines the rule's importance and order for which the rule is evaluated. Priority `1` is the first rule evaluated. Priority `2147483647` is the last rule evaluated and is reserved for the `default` rule. **Important** : After a rule is created, you cannot edit the priority value. You must delete and then recreate a rule to change the value of a rule's priority. 
     * ALLOW_OR_DENY specifies whether to allow or deny access for requests that match the rule. Valid values are `allow` or `deny`. Rules set to `allow` forward the request to the app. Rules set to `deny` respond to requests with a `403 Forbidden` error. 
     * IP_RANGE defines the range of IP addresses that apply to the rule. The IP range must be defined in [CIDR notation](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing), can include subnet masks, and support both IPv4 and IPv6. 
     * DESCRIPTION is an optional description of the rule that is no longer than 100 characters. 
  2. Run the following command to test your rule and ensure that the priority and action provide the expected behavior: 
         
         gcloud app firewall-rules test-ip IP_ADDRESS

where IP_ADDRESS is the IP address that you want to test against your firewall. 
  3. Run the following command to view a list of the existing rules: 
         
         gcloud app firewall-rules list

  4. Run the following command to delete an existing rule: 
         
         gcloud app firewall-rules delete PRIORITY

where PRIORITY is the priority value of the rule that you want to delete. 



Examples:
     Use the following examples to help you create your firewall: 

  * Add a rule that allows an IPv6 address and subnet mask, and then test that rule to ensure it gets evaluated prior to your other rules: 
        
        gcloud app firewall-rules create 123 --source-range fe80::3636:3bff:fecc:8778/128 --action allow
        gcloud app firewall-rules test-ip fe80::3636:3bff:fecc:8778

  * Add a rule to deny an IPv4 address and subnet mask, and then test that rule to ensure that it gets appropriately evaluated: 
        
        gcloud app firewall-rules create 123456 --source-range "74.125.0.0/16" --action deny
        gcloud app firewall-rules test-ip 74.125.0.8

  * Update and then test the default rule to ensure that it restricts all IP addresses that don't match any other rules: 
        
        gcloud app firewall-rules update default --action deny
        gcloud app firewall-rules test-ip 123.456.7.89



API

To programmatically create firewall rules for your App Engine app, you can use the [ `apps.firewall.ingressRules`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules) methods in the Admin API. 

To test a firewall rule and ensure that the priority and action provide the expected behavior, you can use the [ `apps.firewall.ingressRules.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules/list) method and specify the IP address that you want to test within the `matchingAddress` parameter. 

## Understanding App Engine firewall rules

An App Engine firewall consists of an ordered list of rules that can allow or deny access from the specified IP address or range to your app. The rule applies to all resources of the App Engine application.

### Firewall rule priority

The firewall rules are ordered by importance, which you define as a numerical value in each rule's priority. You must specify a unique priority value for each rule as it defines the importance relative to the other rules in the firewall. The values for a rule's priority scale from the most important value of `1` up to the least important at value `2147483647`.

Each firewall includes a `default` rule that is automatically created with the `2147483647` priority and applies to the entire IP range of your app. The `default` rule is always evaluated after all the other rules in the firewall and applied to all requests across all IP addresses.

The firewall evaluates the highest priority rule first. All the remaining rules in the firewall are sequentially evaluated until a rule matches the IP range of that request. When a matching rule is found, the connection is either allowed or denied, and all the remaining rules in the firewall are then skipped. If none of the manually defined rules in the firewall match the request, the `default` rule is evaluated.

For example, if you create a rule with priority `1` it is always evaluated first. If an incoming request matches the rule with priority `1`, only that rule is evaluated and all the other rules in the firewall are skipped, including the `default` rule.

The example firewall below shows how a rule's priority can change the behavior of your firewall.

**Note:** If you set up [port forwarding](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#port_forwarding), remember that all requests through that forwarded port bypass the App Engine firewall.

## Example firewall

In this example, a company has set up a firewall to grant access to the engineering team and internal corporate network to their in-development app. The firewall rules have been created with large gaps between each priority to allow for growth.

Priority | Action | IP range | Description  
---|---|---|---  
1000 | Deny | 192.0.2.1 | Denies access to a DoS attacker.  
2000 | Allow | 198.51.100.2 | Allows access to an engineer in the satellite office.  
3000 | Deny | 198.51.100.0/24 | Denies access to all non-engineering buildings.  
5000 | Allow | 203.0.113.0/24 | Allows access to the main building's network.  
2147483647 | Deny | * | Default Action  
  
After the firewall is created, assume that the following requests are directed at the sample app and note the app's response:

  * Request from 198.51.100.2 matches rule with priority 2000 and is allowed.
  * Request from 198.51.100.100 matches rule with priority 3000 and gets denied.
  * Request from 203.0.113.54 matches rule with priority 5000 and is allowed.
  * Request from 45.123.35.242 matches the default rule and gets denied.



### Resolving conflicting rules

For example, assume that two of the priorities in the company's firewall are swapped. If the rules for priorities 2000 and 3000 are swapped, notice the unintended behavior.

Priority | Action | IP range | Description  
---|---|---|---  
1000 | Deny | 192.0.2.1 | Denies access to a DoS attacker.  
_2000_ | _Deny_ | _198.51.100.0/24_ | _Denies access to all non-engineering buildings._  
**3000** | **Allow** | **198.51.100.2** | **Allows access to an engineer in the satellite office.**  
5000 | Allow | 203.0.113.0/24 | Allows access to the main building's network.  
2147483647 | Deny | * | Default Action  
  
The engineer in the satellite office will not be able to access the company's app as the rule's new priority means it will never be evaluated. The engineer's IP address `198.51.100.2` matches the rule that denies all non-engineers in the range `198.51.100.0/24` before the rule that allows access to the engineer's IP address.

To fix this, you must set the priority of the rule that allows access to `198.51.100.2` to be higher than the rule that denies access for the IP range `198.51.100.0/24`.

## What's next

To ensure that you've securely configured your app and set the appropriate levels of access, review [Application Security](https://docs.cloud.google.com/appengine/docs/flexible/application-security) as well as [Access Control](https://docs.cloud.google.com/appengine/docs/flexible/access-control).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
