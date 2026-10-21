---
url: https://docs.cloud.google.com/dns/docs/zones/manage-response-policies/
title: Manage response policies and rules \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:57.872335+00:00
---

# Manage response policies and rules  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/manage-response-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Manage response policies and rules Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about how to manage [response policies](https://docs.cloud.google.com/dns/docs/key-terms#response-policy) and response policy rules.

Cloud DNS private zones let you create response policies that can modify resolver behavior based on response policy rules. However, you can only attach one response policy per network.

You can create multiple rules within a single response policy that can each do one of the following:

  * Alter results for the selected query names (including wildcards) by providing specific resource records.
  * Trigger [passthru](https://datatracker.ietf.org/doc/html/draft-ietf-dnsop-dns-rpz-00#section-3.3) behavior that bypasses the response policy and exempts names that would otherwise match. For example, for wildcard responses, this lets private DNS query matching continue as if it never encountered a wildcard.



For information about how VPC Service Controls lets customers enforce controls on API access from their private VPC networks, see [Set up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring_dns_with).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.responsePolicies.create` to create response policies
  * `dns.networks.bindDNSResponsePolicy` to create response policies
  * `dns.responsePolicies.delete` to delete response policies
  * `dns.responsePolicies.get` to get response policies
  * `dns.responsePolicies.update` to update response policies
  * `dns.responsePolicies.list` to create, modify, list, or delete response policies
  * `dns.responsePolicyRules.create` to create response policy rules
  * `dns.responsePolicyRules.delete` to delete response policy rules
  * `dns.responsePolicyRules.get` to get response policy rules
  * `dns.responsePolicyRules.update` to update response policy rules
  * `dns.responsePolicyRules.list` to create, modify, list, or delete response policy rules



**Roles**

  * `roles/dns.admin`



## Manage response policies

### Create a response policy

To create a response policy, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones)

  2. Click the **Response policy zones** tab.

  3. Click **Create response policy**.

  4. Enter the name of the response policy that you want to create, such as `myresponsepolicy`.

  5. Enter a description of the response policy, such as `My new response policy`.

  6. From the **Networks** drop-down, select one or more networks to associate with the response policy.

  7. Click **Create**.

You can create a response policy rule in each response policy zone that you create. For instructions, see Creating a response policy rule.




###  gcloud 

Run the [`gcloud dns response-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/create) command:
    
    
    gcloud dns response-policies create RESPONSE_POLICY_NAME \
        --networks=NETWORK \
       [--description=DESCRIPTION]
    

Replace the following:

  * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to create, such as `myresponsepolicy`
  * `NETWORK`: a comma-separated list of network names to associate with the response policy, such as `network1, network2`
  * `DESCRIPTION`: a description of the response policy, such as `My new response policy`



###  API 

Send a `POST` request by using the [`responsePolicies.create`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicies/create) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies
    

Replace `PROJECT_ID` with the name or ID of the project that you want to create the response policy in.

### View response policies

To view the list of all response policies in a given project, or to view the description of a specific response policy, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones)

  2. Click the **Response policy zones** tab.

  3. The **Response policies list** page lists the response policies that you have created.




###  gcloud 

  * To see the list of all response policies in a project, run the [`gcloud dns response-policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/list) command:
        
        gcloud dns response-policies list
        

  * You can limit the number of response policies by using the `--limit` flag. For example, to see a list of the first ten response policies, run the following command:
        
        gcloud dns response-policies list \
          --limit=10
        

  * To see a detailed description of a response policy, run the [`gcloud dns response-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/describe) command:
        
        gcloud dns response-policies describe RESPONSE_POLICY_NAME
        

Replace `RESPONSE_POLICY_NAME` with the name or ID of the response policy that you want to view the description for.




###  API 

To see the detailed description of a response policy, send a `GET` request by using the [`responsePolicies.get`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicies/get) method:
    
    
    GET https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you have created the response policy
  * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to see the description for, such as `myresponsepolicy`



### Update a response policy

To update a response policy, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones)

  2. Click the response policy that you want to edit. You can also click _more_vert_**More** in the row of the response policy name.

  3. Click **Edit response policy**.

  4. Make the required updates.

  5. Click **Save**.




###  gcloud 

Run the [`gcloud dns response-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/update) command:
    
    
    gcloud dns response-policies update RESPONSE_POLICY_NAME
    

Replace `RESPONSE_POLICY_NAME` with the name or ID of the response policy that you want to update, such as `myresponsepolicy`.

Use the same syntax as the `create` command for any updated fields.

###  API 

  * To apply a partial update to a response policy, send a `PATCH` request by using the [`responsePolicies.patch`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicies/patch) method:
        
        PATCH https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you have created the response policy
    * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to update, such as `myresponsepolicy`
  * To update a response policy, send an `UPDATE` request by using the [`responsePolicies.update`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicies/update) method:
        
        UPDATE https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you have created the response policy
    * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to update, such as `myresponsepolicy`



### Delete a response policy

To delete a response policy, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones)

  2. Click _more_vert_**More** in the row of the response policy name.

  3. Click **Delete**.


**Note:** You cannot delete a response policy that is associated with a network or response policy rule. You must first remove the network from the policy or delete the rule before deleting the policy.

###  gcloud 

Run the [`gcloud dns response-policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/delete) command:
    
    
    gcloud dns response-policies delete RESPONSE_POLICY_NAME
    

Replace `RESPONSE_POLICY_NAME` with the name or ID of the response policy that you want to delete.

###  API 

Send a `DELETE` request by using the [`responsePolicies.delete`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicies/delete) method:
    
    
    DELETE https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you have created the response policy
  * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to delete, such as `myresponsepolicy`



## Manage response policy rules

A site's DNS response policy consists of rules that a DNS resolver consults during lookups. If a rule in the response policy affects the incoming query, it is processed; otherwise, the lookup proceeds normally.

### Create a response policy rule

To create a response policy rule, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones)

  2. Click the **Response policy zones** tab.

  3. From the list of response policy zones, click the response policy zone for which you want to create a rule.

  4. Click **Create response policy rule**.

  5. Enter the name of the response policy rule that you want to create, such as `myresponsepolicyrule`.

  6. From the **Selector** drop-down, choose the selector type to apply this rule to.

**Note:** Google Cloud only supports **DNS Name** selector.
  7. Enter the DNS name (wildcard or exact) to apply the rule to, such as `www.googleapis.com`.

  8. Choose the action for the response policy rule. For example, to alter the behavior of the response policy, choose **Behavior** ; otherwise, choose **Local data**.

     * If you chose **Behavior** , from the drop-down, select the behavior for the rule.

**Note:** Google Cloud only supports **Bypass response policy** behavior at this time.
     * If you chose **Local data** , you must add a new resource record set. For instructions about how to add a new resource record set, see [Creating a resource record set](https://docs.cloud.google.com/dns/docs/records#creating_a_resource_record_set).

  9. Click **Create**.




###  gcloud 

  * To alter behavior for selected query names, run the [`gcloud dns response-policies rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/create) command, and specify the `--type` flag:
        
        gcloud dns response-policies rules create RESPONSE_POLICY_RULE_NAME \
          --response-policy=RESPONSE_POLICY_NAME \
          --dns-name=DNS_NAME \
          --local-data=name="DNS_NAME.",type="RRTYPE",ttl=TTL,rrdatas="RRDATA"
        

Replace the following:

    * `RESPONSE_POLICY_RULE_NAME`: a name for the response policy rule that you want to create, such as `myresponsepolicyrule`
    * `RESPONSE_POLICY_NAME`: the name of the response policy, such as `myresponsepolicy`
    * `DNS_NAME`: the DNS or domain name, such as `www.googleapis.com`
    * `TTL`: time to live for the response policy, such as `21600`
    * `RRTYPE`: the resource record type, such as `A`
    * `RRDATA`: the resource record data, such as `1.2.3.4`. Separate multiple entries with `|`, such as `1.2.3.4|5.6.7.8`.
  * To create a bypass rule, run the [`gcloud dns response-policies rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/create) command, and set the `--behavior` flag to `bypassResponsePolicy`:
        
        gcloud dns response-policies rules create RESPONSE_POLICY_RULE_NAME \
          --response-policy=RESPONSE_POLICY_NAME \
          --dns-name=DNS_NAME \
          --behavior=bypassResponsePolicy
        

Replace the following:

    * `RESPONSE_POLICY_RULE_NAME`: a name for the response policy rule that you want to create, such as `myresponsepolicyrule`
    * `RESPONSE_POLICY_NAME`: the name of the response policy, such as `myresponsepolicy`
    * `DNS_NAME`: the DNS or domain name, such as `www.googleapis.com`



###  API 

  * To create a new response policy rule, send a `POST` request by using the [`responsePolicyRules.create`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicyRules/create) method:
        
        POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME/rules
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you have created the response policy
    * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to create a rule for, such as `myresponsepolicy`



### View a response policy rule

To view the list of all response policy rules in a given response policy, or to view the description of a specific response policy rule, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones)

  2. On the **Response policy zones** tab, click the response policy name that you want to see the associated rules for. The **Response policy details** page lists the rules associated with the response policy.

  3. To view the details of a specific response policy rule, click the name of the rule. You can also click _more_vert_**More** in the row of the response policy rule name.




###  gcloud 

  * To view the list of Cloud DNS response policy rules within a response policy, run the [`gcloud dns response-policies rules list`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/list) command:
        
        gcloud dns response-policies rules list RESPONSE_POLICY_NAME
        

Replace `RESPONSE_POLICY_NAME` with the name of the response policy, such as `myresponsepolicy`.

  * To view details about a specific response policy rule, run the [`gcloud dns response-policies rules describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/describe) command:
        
        gcloud dns response-policies rules describe RESPONSE_POLICY_RULE_NAME \
          --response-policy=RESPONSE_POLICY_NAME
        

Replace the following:

    * `RESPONSE_POLICY_RULE_NAME`: a name for the response policy rule that you want to create, such as `myresponsepolicyrule`
    * `RESPONSE_POLICY_NAME`: the name of the response policy, such as `myresponsepolicy`



###  API 

To see the detailed description of a rule in a response policy, send a `GET` request by using the [`responsePolicyRules.get`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicyRules/get) method:
    
    
    GET https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME/rules/RESPONSE_POLICY_RULE
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you have created the response policy
  * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to create a rule for, such as `myresponsepolicy`
  * `RESPONSE_POLICY_RULE`: the response policy rule that you want to see the details of



### Update a response policy rule

To edit or update a response policy rule, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones)

  2. Click the response policy name that you want to edit the rules for.

  3. Click the name of the response policy rule that you want to edit.

  4. On the **Response policy rule details** page, click the rule name that you want to edit.

  5. Make the required updates.

  6. Click **Save**.




###  gcloud 

Run the [`gcloud dns response-policies rules update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update) command:
    
    
    gcloud dns response-policies rules update RESPONSE_POLICY_RULE_NAME \
        --response-policy=RESPONSE_POLICY_NAME
      

Replace the following:

  * `RESPONSE_POLICY_RULE_NAME`: a name for the response policy rule that you want to create, such as `myresponsepolicyrule`
  * `RESPONSE_POLICY_NAME`: the name of the response policy, such as `myresponsepolicy`

Use the same syntax as the `create` command for any updated fields.




###  API 

  * To apply a partial update to a response policy rule, send a `PATCH` request by using the [`responsePolicyRules.patch`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicyRules/patch) method:
        
        PATCH https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME/rules/RESPONSE_POLICY_RULE
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you have created the response policy
    * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to update the rule for, such as `myresponsepolicy`
    * `RESPONSE_POLICY_RULE`: the response policy rule that you want to update
  * To update a response policy rule, send an `UPDATE` request by using the [`responsePolicyRules.update`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicyRules/update) method:
        
        UPDATE https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME/rules/RESPONSE_POLICY_RULE
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you have created the response policy
    * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to update the rule for, such as `myresponsepolicy`
    * `RESPONSE_POLICY_RULE`: the response policy rule that you want to update



### Delete a response policy rule

To delete a response policy rule, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones)

  2. Click the response policy name that you want to edit the rules for.

  3. Click the name of the response policy rule that you want to delete.

  4. On the **Response policy rule details** page, click _more_vert_**More** in the row of the response policy rule name.

  5. Click **Delete**. You can also click the rule that you want to delete: on the **Response policy rule details** page, click **Delete response policy rules**.




###  gcloud 

  * To delete a Cloud DNS response policy rule, run the [`gcloud dns response-policies rules delete`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete) command:
        
        gcloud dns response-policies rules delete RESPONSE_POLICY_RULE_NAME \
          --response-policy=RESPONSE_POLICY_NAME
        

Replace the following:

    * `RESPONSE_POLICY_RULE_NAME`: a name for the response policy rule that you want to create, such as `myresponsepolicyrule`
    * `RESPONSE_POLICY_NAME`: the name of the response policy, such as `myresponsepolicy`



###  API 

  * To delete a response policy rule, send a `DELETE` request by using the [`responsePolicyRules.delete`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicyRules/delete) method:
        
        DELETE https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies/RESPONSE_POLICY_NAME/rules/RESPONSE_POLICY_RULE
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you have created the response policy
    * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to delete the rule from, such as `myresponsepolicy`
    * `RESPONSE_POLICY_RULE`: the response policy rule that you want to delete



## Use cases

This section provides example use cases to configure rules for response policies.

### Direct specific names to restricted VIP addresses

You can configure a response policy that has local CNAME data for each zone to translate Google API requests to restricted Google APIs. Names that aren't specified continue to be resolved by using regular DNS.

For example, you can create a response policy for `pubsub.googleapis.com`, which has local CNAME data for a zone, to translate Google API requests to `restricted.googleapis.com`. In the meantime, `www.googleapis.com`, which is unspecified, continues to be resolved by using regular DNS.

In the following example configuration, you create a policy and apply it to a specific VPC network.

### gcloud 

  1. To create a response policy, run the [`gcloud dns response-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/create) command:
         
         gcloud dns response-policies create RESPONSE_POLICY_NAME \
             --networks=NETWORK \
             --description=DESCRIPTION
         

Replace the following:

     * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to create, such as `myresponsepolicy`
     * `NETWORK`: a comma-separated list of network names to associate with the response policy, such as `network1,network2`
     * `DESCRIPTION`: a description of the response policy, such as `My new response policy`
  2. If you're using only the IPv4 address range for `restricted.googleapis.com`, add a rule to the policy that contains a record set for the IPv4 address range.

[`gcloud dns response-policies rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/create) command:
         
         gcloud dns response-policies rules create RESPONSE_POLICY_RULE_NAME \
             --response-policy=RESPONSE_POLICY_NAME \
             --dns-name=DNS_NAME. \
             --local-data=name="DNS_NAME.",type="A",ttl=300,rrdatas="199.36.153.4|199.36.153.5|199.36.153.6|199.36.153.7"
         

Replace the following:

     * `RESPONSE_POLICY_RULE_NAME`: a name for the response policy rule that you want to create, such as `myresponsepolicyrule`
     * `RESPONSE_POLICY_NAME`: the name of the response policy, such as `myresponsepolicy`
     * `DNS_NAME`: the DNS name for which you are creating the rule, such as `pubsub.googleapis.com.`; note the trailing dot
  3. If you're using both the IPv4 and IPv6 address ranges for `restricted.googleapis.com`, add a rule to the policy that contains record sets for both the IPv4 and IPv6 address ranges.
         
         gcloud dns response-policies rules create RESPONSE_POLICY_RULE_NAME \
             --response-policy=RESPONSE_POLICY_NAME \
             --dns-name=DNS_NAME. \
             --local-data=name="DNS_NAME.",type="A",ttl=300,rrdatas="199.36.153.4|199.36.153.5|199.36.153.6|199.36.153.7" \
             --local-data=name="DNS_NAME.",type="AAAA",ttl=300,rrdatas="2600:2d00:0002:1000::"
         




###  API 

  1. Create a response policy by URL:
         
         {
           kind: "dns#responsePolicy",
           response_policy_name: RESPONSE_POLICY_NAME,
           description: RESPONSE_POLICY_DESCRIPTION,
           networks: [
             {
               network_url: URL_TO_NETWORK;
             }
           ]
         }
         

Replace the following:

     * `RESPONSE_POLICY_NAME`: a name for the response policy
     * `RESPONSE_POLICY_DESCRIPTION`: a description of the response policy
     * `URL_TO_NETWORK`: the URL for which you're creating the response policy

**Note:** It is not necessary to refer to the parent response policy in the JSON. The parent response policy is inferred from the URL that you use.
  2. If you're using only the IPv4 address range for `restricted.googleapis.com`, add a rule to the policy that contains a record set for the IPv4 address range.
         
         {
           kind: "dns#responsePolicyRules",
           rule_name: RULE_NAME,
           dns_name: DNS_NAME,
           local_data: [
             {
               name: "DNS_NAME.",
               type: "A",
               ttl: 300,
               rrdata: ["199.36.153.4", "199.36.153.5", "199.36.153.6", "199.36.153.7"]
             }
           ]
         }
         

Replace the following:

     * `RULE_NAME`: a name for the rule that you are creating, such as `pubsub`
     * `DNS_NAME`: the DNS name for which you are creating the rule, such as `pubsub.googleapis.com.`; note the trailing dot
  3. If you're using both the IPv4 and IPv6 address ranges for `restricted.googleapis.com`, add a rule to the policy that contains record sets for both the IPv4 and IPv6 address ranges.
         
         {
           kind: "dns#responsePolicyRules",
           rule_name: RULE_NAME,
           dns_name: DNS_NAME,
           local_data: [
             {
               name: "DNS_NAME.",
               type: "A",
               ttl: 300,
               rrdata: [""199.36.153.4", "199.36.153.5", "199.36.153.6", "199.36.153.7""]
             }
           ],
           local_data: [
             {
               name: "DNS_NAME.",
               type: "AAAA",
               ttl: 300,
               rrdata: ["2600:2d00:0002:1000::"]
             }
           ]
         }
         

Replace the following:

     * `RULE_NAME`: a name for the rule that you are creating, such as `pubsub`
     * `DNS_NAME`: the DNS name for which you are creating the rule, such as `pubsub.googleapis.com.`; note the trailing dot



### Direct all names except some to restricted VIP addresses

You can set rules to exempt some DNS responses from a policy rule that covers an entire domain or a large IP address block. This concept is called _passthru behavior_. By using passthru behavior, you can let names that lack support for service controls be allowed past the wildcard name.

For example, you can let `www.googleapis.com` be allowed past the wildcard name in the example `*.googleapis.com`. The exact match for `www` takes precedence over the wildcard `*`.

In the following example configuration, you create a policy with a specified name and apply it to a specific VPC network. The rule allows `www.googleapis.com` to bypass the wildcard `*.googleapis.com`.

### gcloud 

  1. To create a response policy, run the [`gcloud dns response-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/create) command:
         
         gcloud dns response-policies create RESPONSE_POLICY_NAME \
             --networks=NETWORK \
             --description=DESCRIPTION
         

Replace the following:

     * `RESPONSE_POLICY_NAME`: the name or ID of the response policy that you want to create, such as `myresponsepolicy`
     * `NETWORK`: a comma-separated list of network names to associate with the response policy, such as `network1,network2`
     * `DESCRIPTION`: a description of the response policy, such as `My new response policy`
  2. To add a bypass rule to the policy, run the [`gcloud dns response-policies rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/create) command, and set the `--behavior` flag to `bypassResponsePolicy`:
         
         gcloud dns response-policies rules create RESPONSE_POLICY_RULE_NAME \
             --response-policy=RESPONSE_POLICY_NAME \
             --dns-name=DNS_NAME \
             --behavior=bypassResponsePolicy
         

Replace the following:

     * `RESPONSE_POLICY_RULE_NAME`: a name for the response policy rule that you want to create, such as `myresponsepolicyrule`
     * `RESPONSE_POLICY_NAME`: the name of the response policy, such as `myresponsepolicy`
     * `DNS_NAME`: the DNS or domain name, such as `www.googleapis.com`



###  API 

  1. Create a response policy:
         
         {
           kind: "dns#responsePolicy",
           response_policy_name: RESPONSE_POLICY_NAME,
           description: RESPONSE_POLICY_DESCRIPTION,
           networks: [
             {
               network_url: URL_TO_NETWORK;
             }
           ]
         }
         

Replace the following:

     * `RESPONSE_POLICY_NAME`: a name for the response policy, such as `my-response-policy`
     * `RESPONSE_POLICY_DESCRIPTION`: a description of the response policy, such as `my response policy`
     * `URL_TO_NETWORK`: the URL for which you're creating the response policy
  2. Add a rule to the policy:
         
         {
           kind: "dns#responsePolicyRules",
           rule_name: RULE_NAME,
           dns_name: DNS_NAME,
           local_data: [
             {
               name: "*.googleapis.com.",
               type: "A",
               ttl: 300,
               rrdata: ["restricted.googleapis.com."]
             }
           ]
         }
         {
           kind: "dns#responsePolicyRules",
           rule_name: "www-passthru",
           dns_name: "www.googleapis.com.",
           behavior: BYPASS_RESPONSE_POLICY
         }
         

Replace the following:

     * `RULE_NAME`: a name for the rule that you are creating, such as `googleapis`
     * `DNS_NAME`: the wildcard DNS name for which you are creating the rule, such as `*.googleapis.com.`; note the trailing dot



## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
