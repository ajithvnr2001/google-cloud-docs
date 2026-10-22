---
url: https://docs.cloud.google.com/nat/docs/using-nat-rules/
title: Set up and manage Cloud NAT rules \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:41.837090+00:00
---

# Set up and manage Cloud NAT rules  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/using-nat-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up and manage Cloud NAT rules

This page describes how to configure Cloud NAT rules for Public NAT. Before configuring Cloud NAT rules, see the [Cloud NAT rules overview](https://docs.cloud.google.com/nat/docs/nat-rules-overview).

## Create NAT rules

To create NAT rules, Cloud NAT uses Common Expression Language (CEL), as described in [Rule expressions](https://docs.cloud.google.com/nat/docs/nat-rules-overview#rule-expression-language). For example expressions that you can use in your NAT rules, see [Example expressions](https://docs.cloud.google.com/nat/docs/nat-rules-overview#example-expressions).

If you want to create NAT rules, make sure that [endpoint-independent mapping (EIM) is disabled](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#set-mapping) for your NAT gateway.

### Create source-based rules

The steps in this section describe how to create source-based NAT rules for the following conditions:

  1. Packets from source IP range `10.10.1.0/24` must use `IP_ADDRESS_1`.
  2. Packets from source IP range `10.10.2.0/24` must use `IP_ADDRESS_2`.
  3. All other packets must use `IP_ADDRESS_3`.



For conditions 1 and 2, you create two NAT rules. Condition 3 is fulfilled by the default NAT rule for source address matching. `IP_ADDRESS_1`, `IP_ADDRESS_2`, and `IP_ADDRESS_3` are the external IP addresses that you want to use for NAT.

### Console

#### Add NAT rules to an existing NAT gateway

  1. Add a NAT rule that matches traffic from `10.10.1.0/24` and translates the source IP to `IP_ADDRESS_1`.

     1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

     2. Click your NAT gateway.

     3. Click **Edit**.

     4. For **Cloud NAT IP addresses** , select **Manual**.

     5. In the **Cloud NAT Rules** section, click **Add a rule**.

     6. In the **Rule priority** field, enter a number from `0` (highest priority) to `65000` (lowest priority). For example, `100`.

     7. For **Match IP ranges** , select **Source**.

     8. In the **Source IP ranges** field, enter `10.10.1.0/24`.

     9. In the **IP addresses** section, select the IP address that you want to use for `IP_ADDRESS_1`.

     10. Click **Done**.

  2. Add a NAT rule that matches traffic from `10.10.2.0/24` and translates it to `IP_ADDRESS_2`.

     1. In the **Cloud NAT Rules** section, click **Add a rule**.
     2. In the **Rule priority** field, enter a number from `0` (highest priority) to `65000` (lowest priority). For example, `200`.
     3. For **Match IP ranges** , select **Source**.
     4. In the **Source IP ranges** field, enter `10.10.2.0/24`.
     5. In the **IP addresses** section, select the IP address that you want to use for `IP_ADDRESS_2`.
     6. Click **Done**.
     7. Click **Save** to save both rules.



###  gcloud 

You can use the steps in the following sections to create a rule file, create a Cloud NAT gateway that uses the rules in the rule file, or add rules to an existing NAT gateway.

#### Add NAT rules to an existing NAT gateway

You can add a new NAT rule by using the [`gcloud compute routers nats rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/create).

  1. Add a NAT rule that uses `IP_ADDRESS_1` for traffic from `10.10.1.0/24`:
         
         gcloud compute routers nats rules create NAT_RULE_PRIORITY \
             --router=NAT_ROUTER \
             --region=REGION \
             --nat=NAT_CONFIG \
             --match='inIpRange(source.ip, "10.10.1.0/24")' \
             --source-nat-active-ips=IP_ADDRESS_1
         

Replace the following:

     * `NAT_RULE_PRIORITY`: a rule number that uniquely identifies the NAT rule, from `0` (highest priority) to `65000` (lowest priority)—for example, `100`
     * `NAT_ROUTER`: the name of the Cloud Router that you use for the NAT gateway
     * `REGION`: the region of the NAT gateway
     * `NAT_CONFIG`: the name of the NAT configuration
     * `IP_ADDRESS_1`: the manually allocated external IP address that you want to use for packets that match the rule
  2. Add a NAT rule that uses `IP_ADDRESS_2` for traffic from `10.10.2.0/24`:
         
         gcloud compute routers nats rules create NAT_RULE_PRIORITY \
             --router=NAT_ROUTER \
             --region=REGION \
             --nat=NAT_CONFIG \
             --match='inIpRange(source.ip, "10.10.2.0/24")' \
             --source-nat-active-ips=IP_ADDRESS_2
         

Replace the following:

     * `NAT_RULE_PRIORITY`: a rule number that uniquely identifies the NAT rule, from `0` (highest priority) to `65000` (lowest priority)—for example, `200`
     * `NAT_ROUTER`: the name of the Cloud Router that you use for the NAT gateway
     * `REGION`: the region of the NAT gateway
     * `NAT_CONFIG`: the name of the NAT configuration
     * `IP_ADDRESS_2`: the manually allocated external IP address that you want to use for packets that match the rule



#### Create a NAT gateway using a NAT rule file

The following code sample is an example rule file. You can modify this rule file to fit your use case or skip this step if you already have a rule file.

##### Create a rule file
    
    
    rules:
     - ruleNumber: 100
       match: inIpRange(source.ip, '10.10.1.0/24')
       action:
         sourceNatActiveIps:
         -  /projects/PROJECT_ID/regions/REGION/addresses/IP_ADDRESS_1
     - ruleNumber: 200
       match: inIpRange(source.ip, '10.10.2.0/24')
       action:
         sourceNatActiveIps:
         -  /projects/PROJECT_ID/regions/REGION/addresses/IP_ADDRESS_2
    

In the preceding example, `IP_ADDRESS_1` and `IP_ADDRESS_2` are the manually allocated external IP addresses that you want to use for packets that match the rules. For each IP address, replace the following:

  * `PROJECT_ID`: the project of the IP address
  * `REGION`: the region where the IP address is reserved



##### Create a NAT gateway using a NAT rule file

The following command creates a NAT gateway and configures it with rules from a NAT rule file. If you already have a NAT gateway configured, see Add NAT rules to an existing NAT gateway.
    
    
    gcloud compute routers nats create NAT_CONFIG \
        --router=NAT_ROUTER \
        --region=REGION \
        --nat-all-subnet-ip-ranges \
        --nat-external-ip-pool=IP_ADDRESS_3,[IP_ADDRESS_4] \
        --rules=PATH_TO_NAT_RULE_FILE
    

Replace the following:

  * `NAT_CONFIG`: a name for the NAT configuration
  * `NAT_ROUTER`: the name of the Cloud Router that you want to use for the NAT gateway
  * `REGION`: the region where you want to create the Cloud NAT gateway
  * `IP_ADDRESS_3` and `IP_ADDRESS_4`: the external IP addresses that you want to use for the default NAT rule
  * `PATH_TO_NAT_RULE_FILE`: the path to the NAT rule file



### Create destination-based rules

The following example configuration steps fulfill the following conditions:

  * Packets with destination address `198.51.100.10` must use NAT IP address `IP_ADDRESS_1`.
  * Packets with destination address `198.51.100.20/30` must use NAT IP address `IP_ADDRESS_2` or `IP_ADDRESS_3`.



You can create one NAT rule to fulfill each of these conditions.

### Console

#### Add NAT rules to an existing NAT gateway

  1. Add a NAT rule that uses `IP_ADDRESS_1` to send traffic to `198.51.100.10`.

     1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

     2. Click **Edit**.

     3. For **Cloud NAT IP addresses** , select **Manual**.

     4. In the **Cloud NAT Rules** section, click **Add a rule**.

     5. In the **Rule priority** field, enter a number from `0` (highest priority) to `65000` (lowest priority). For example, `100`.

     6. For **Match IP ranges** , select **Destination**.

     7. In the **Destination IP ranges** field, enter `198.51.100.10`.

     8. In the **IP addresses** section, select the IP address that you want to use for `IP_ADDRESS_1`.

     9. Click **Done**.

  2. Add a NAT rule that uses `IP_ADDRESS_2` or `IP_ADDRESS_3` to send traffic to `198.51.100.20/30`.

     1. In the **Cloud NAT Rules** section, click **Add a rule**.
     2. In the **Rule priority** field, enter a number from `0` (highest priority) to `65000` (lowest priority). For example, `200`.
     3. For **Match IP ranges** , select **Destination**.
     4. In the **Destination IP ranges** field, enter `198.51.100.20/30`.
     5. In the **IP addresses** section, select the IP address that you want to use for `IP_ADDRESS_2`.
     6. Click **Add IP address** and select the IP address that you want to use for `IP_ADDRESS_3`.
     7. Click **Done**.
     8. Click **Save** to save both rules.



### gcloud

You can use the steps in the following sections to create a rule file, create a NAT gateway that uses the rules in the rule file, or add rules to an existing NAT gateway.

#### Add NAT rules to an existing NAT gateway

You can add a new NAT rule using the NAT rule command. Replace the `NAT_RULE_PRIORITY` with the NAT rule priority that you want to assign to the rule—from `0` (highest) to `65000` (lowest)—and replace the other variables with information matching your configuration.

First, add a NAT rule that sends traffic from `IP_ADDRESS1` to `198.51.100.10`.
    
    
    gcloud compute routers nats rules create NAT_RULE_PRIORITY \
        --router=ROUTER_NAME \
        --nat=NAT_NAME \
        --match='destination.ip == "198.51.100.10"' \
        --source-nat-active-ips=IP_ADDRESS1 \
        [--region=REGION] [GLOBAL-FLAG ...]
    

Next, add a NAT rule that sends traffic from `IP_ADDRESS2` or `IP_ADDRESS3` to `198.51.100.20/30`.
    
    
    gcloud compute routers nats rules create NAT_RULE_PRIORITY \
        --router=ROUTER_NAME \
        --nat=NAT_NAME \
        --match='inIpRange(destination.ip, "198.51.100.20/30")' \
        --source-nat-active-ips=IP_ADDRESS2,IP_ADDRESS3 \
        [--region=REGION] [GLOBAL-FLAG ...]
    

#### Create a rule file

The following code sample is an example rule file. You can modify this rule file to fit your use case, or skip this step if you already have a rule file.
    
    
    rules:
     - ruleNumber: 100
       match: destination.ip == '198.51.100.10'
       action:
         sourceNatActiveIps:
         -  /projects/PROJECT ID/regions/REGION/addresses/IP_ADDRESS1
     - ruleNumber: 200
       match: inIpRange(destination.ip, '198.51.100.20/30')
       action:
         sourceNatActiveIps:
         -  /projects/PROJECT ID/regions/REGION/addresses/IP_ADDRESS2
         -  /projects/PROJECT ID/regions/REGION/addresses/IP_ADDRESS3
    

#### Create a NAT gateway using a NAT rule file

The following command creates a NAT gateway and configures it with rules from a NAT rule file. If you already have a NAT gateway configured, see Add NAT rules to an existing NAT gateway. Replace the variables with information matching your configuration.
    
    
    gcloud compute routers nats create NAT_NAME \
        --router=ROUTER_NAME \
        --nat-external-ip-pool=IP_ADDRESS4,[IP_ADDRESS5] \
        --nat-all-subnet-ip-ranges \
        --rules=PATH_TO_NAT_RULE_FILE \
        [--region=REGION] [GLOBAL-FLAG ...]
    

## Update NAT rules

To update your NAT rules, use the steps in the following sections. You can only use rule files with the `gcloud` command-line tool.

### Console

  1. In the Google Cloud console, go to the Cloud NAT page. 

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat)

  2. Click your NAT gateway.
  3. Click **Edit**.
  4. Under **Customized rules** , click the rule that you want to update.
  5. In the expanded fields, you can modify any information that you want to change.
  6. Click **Done**.
  7. Click **Save**.



### gcloud

### Update using a NAT rule file

To update a NAT gateway with your NAT rule file, use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

Replace the variables with information that matches your configuration.
    
    
    gcloud compute routers nats update NAT_NAME \
        --router=ROUTER_NAME \
        --rules=PATH_TO_NAT_RULE_FILE \
        [--region=REGION] [GLOBAL-FLAG ...]
    

The following code sample is an example rule file. Note the `sourceNatDrainIps` action, which prevents new connections to the destination using `IP_ADDRESS1` but keeps existing connections.
    
    
    rules:
     - ruleNumber: 100
       match: destination.ip == '198.51.100.10'
       action:
         sourceNatActiveIps:
         -  /projects/PROJECT ID/regions/REGION/addresses/IP_ADDRESS2
         sourceNatDrainIps:
         -  /projects/PROJECT ID/regions/REGION/addresses/IP_ADDRESS1
    

### Update using a NAT rule command

To update a single NAT rule, use the following command. Replace the `NAT_RULE_PRIORITY` with the NAT rule priority number and replace the other variables with information that matches your configuration. Note the `source-nat-drain-ips` option, which prevents new connections to the destination using `IP_ADDRESS3` and `IP_ADDRESS4`, but keeps existing connections.
    
    
    gcloud compute routers nats rules update NAT_RULE_PRIORITY \
        --router=ROUTER_NAME \
        --nat=NAT_NAME \
        --match=Match conditions (expressed in CEL) \
        --source-nat-active-ips=[IP_ADDRESS1],[IP_ADDRESS2] \
        --source-nat-drain-ips=[IP_ADDRESS3],[IP_ADDRESS4] \
        [--region=REGION] [GLOBAL-FLAG ...]
    

## Delete NAT rules

### Console

  1. In the Google Cloud console, go to the Cloud NAT page. 

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat)

  2. Click your NAT gateway.
  3. Click **Edit**.
  4. Under **Customized rules** , hold the pointer over on the rule that you want to delete. Click delete.
  5. Click **Save**.



### gcloud

To remove a NAT rule from a gateway, you can either remove it from the gateway directly, or remove it from the rule file and update the gateway.

### Delete using a NAT rule file

You can remove a NAT rule from your rule file directly and then update your NAT gateway. The command for updating your NAT gateway is repeated here for convenience.

Replace the variables with information that matches your configuration.
    
    
    gcloud compute routers nats update NAT_NAME \
        --router=ROUTER_NAME \
        --rules=PATH_TO_NAT_RULE_FILE \
        [--region=REGION] [GLOBAL-FLAG ...]
    

### Delete using a NAT rule command

Alternatively, you can use a NAT rule `delete` command to remove a NAT rule from your gateway. Replace the `NAT_RULE_PRIORITY` with the NAT rule priority number and replace the other variables with information that matches your configuration.
    
    
    gcloud compute routers nats rules delete NAT_RULE_PRIORITY \
        --router=ROUTER_NAME \
        --nat=NAT_NAME \
        [--region=REGION] [GLOBAL-FLAG ...]
    

## Describe a NAT rule

### Console

You can view information about your NAT rules on the Cloud NAT page.

  1. In the Google Cloud console, go to the Cloud NAT page. 

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat)

  2. Click your NAT gateway.
  3. View the NAT rules.



For additional information about an individual NAT rule, you can do the following:

  1. Click **Edit**.
  2. Under the **Customized rules** heading, select a NAT rule.
  3. View the additional information.
  4. Click **Cancel**.



### gcloud

To describe a NAT rule, use the following command. Replace the `NAT_RULE_PRIORITY` with your NAT rule priority number and replace the other variables with information that matches your configuration.
    
    
    gcloud compute routers nats rules describe NAT_RULE_PRIORITY \
        --router=ROUTER_NAME \
        --nat=NAT_NAME \
        [--region=REGION] [GLOBAL-FLAG ...]
    

## List all NAT rules in a NAT gateway

### Console

You can view your NAT rules on the Cloud NAT page.

  1. In the Google Cloud console, go to the Cloud NAT page. 

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat)

  2. Click your NAT gateway.
  3. View the NAT rules.



### gcloud

To list all NAT rules in a NAT gateway, use the following command. This also displays all the NAT IP addresses present in the NAT rules, including the default rule. Replace the variables with information that matches your configuration.
    
    
    gcloud compute routers nats rules list \
        --router=ROUTER_NAME \
        --nat=NAT_NAME \
        [--region=REGION] [GLOBAL-FLAG ...]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
