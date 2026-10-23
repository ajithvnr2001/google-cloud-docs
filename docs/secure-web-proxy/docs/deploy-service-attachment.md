---
url: https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment/
title: Publish Secure Web Proxy as a Private Service Connect service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:16.038522+00:00
---

# Publish Secure Web Proxy as a Private Service Connect service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Publish Secure Web Proxy as a Private Service Connect service Stay organized with collections  Save and categorize content based on your preferences. 

To centralize your Secure Web Proxy deployment across multiple VPC networks, you can make Secure Web Proxy available through a Private Service Connect service attachment.

Deploying Secure Web Proxy with Private Service Connect involves the following steps:

  1. Create a Secure Web Proxy [policy](https://docs.cloud.google.com/secure-web-proxy/docs/overview#swp-policies) and [rules](https://docs.cloud.google.com/secure-web-proxy/docs/overview#swp-rules).
  2. Create a Secure Web Proxy instance that uses your policy.
  3. Create a service attachment to publish the Secure Web Proxy instance as a Private Service Connect service.
  4. Create a Private Service Connect consumer endpoint in each VPC network that needs to connect to Secure Web Proxy.
  5. Point your workload's outbound traffic to the centralized Secure Web Proxy instance within the region.

[ ![Deploy Secure Web Proxy as a
         Private Service Connect service attachment.](https://docs.cloud.google.com/static/secure-web-proxy/images/swp-service-attachment.svg)](https://docs.cloud.google.com/static/secure-web-proxy/images/swp-service-attachment.svg) Deploy Secure Web Proxy as a Private Service Connect service attachment (click to enlarge).

## Before you begin

Before completing the steps on this page, complete the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

## Create and configure a Secure Web Proxy instance

This guide describes how to create a Secure Web Proxy policy and rules that match traffic by session.

For information about optionally configuring TLS inspection, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).

For information about optionally configuring application-level matching, see [Create and deploy a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart).

### Create a Secure Web Proxy policy

### Console

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click add_box**Create a policy**.

  3. Enter a name for the policy that you want to create, such as `myswppolicy`.

  4. Enter a description of the policy.

  5. In the **Regions** list, select the region where you want to create the web proxy policy.

  6. Click **Create**.




###  Cloud Shell 

  1. Create a `policy.yaml` file.
         
         description: basic Secure Web Proxy policy
         name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
         

Replace the following:

     * `PROJECT_ID`: the project ID of your project
     * `REGION`: the region of the policy
  2. Create a Secure Web Proxy policy based on `policy.yaml`.
         
         gcloud network-security gateway-security-policies import policy1 \
             --source=policy.yaml \
             --location=REGION
         




### Add Secure Web Proxy rules to your policy

Configure Secure Web Proxy rules to allow egress traffic from each workload.

This section shows how to create a rule to allow traffic from workloads that are identified by Resource Manager tag or service account. For information about matching traffic in other ways, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).

**Note:** Private Service Connect traffic doesn't support matching traffic based on source IP address. Packets that flow through a service attachment are [translated using source NAT (SNAT)](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#psc-subnets) so that their original source IP addresses are converted to source IP addresses from the service attachment's Private Service Connect subnet.

###  Console 

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click the name of your policy.

  3. To add rules to allow workloads to access the internet, do the following:

     1. Click add_box**Add rule**.
     2. Enter a priority. Rules are evaluated from highest to lowest priority, where `0` is the highest priority.
     3. Enter a name.
     4. Enter a description.
     5. Enter a status.
     6. For **Action** , select **Allow**.
     7. Click **Status** , and then select **Enabled**.
     8. In the **Session Match** section, specify the [criteria for matching the session](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference#available-attributes-in-sessionmatcher-and-applicationmatcher).

        * For example, to allow traffic to google.com from workloads with the Resource Manager tag value ID `tagValues/123456`, enter the following:

`source.matchTag('tagValues/123456') && host() == 'google.com'`

        * To allow traffic to google.com from workloads that use the service account `my-service-account@my-project.iam.gserviceaccount.com`, enter the following: 

`source.matchServiceAccount('my-service-account@my-project.iam.gserviceaccount.com') && host() == 'google.com'`

     9. Click **Create**.




###  Cloud Shell 

For each rule that you want to add, do the following:

  1. Create a `rule.yaml` file and specify the [criteria for matching the session](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference#available-attributes-in-sessionmatcher-and-applicationmatcher).

     * To allow traffic to a specific domain from workloads identified by Resource Manager tag value ID, create the following file:
           
           name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1/rules/RULE_NAME
           description: Allow traffic based on tag
           enabled: true
           priority: PRIORITY
           basicProfile: ALLOW
           sessionMatcher: source.matchTag('TAG_VALUE_ID') && host() == 'DOMAIN_NAME'
           

Replace the following:

       * `PROJECT_ID`: the project ID of your project
       * `REGION`: the region of your policy
       * `RULE_NAME`: the name of the rule
       * `PRIORITY`: the priority of the rule—rules are evaluated from highest to lowest priority, where `0` is the highest priority
       * `TAG_VALUE_ID`: the tag value ID of the workloads to allow traffic for
       * `DOMAIN_NAME`: the domain name to allow traffic to
     * To allow traffic to a specific domain from workloads that use a service account, create the following file:
           
           name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1/rules/RULE_NAME
           description: Allow traffic based on service account
           enabled: true
           priority: PRIORITY
           basicProfile: ALLOW
           sessionMatcher: source.matchServiceAccount('SERVICE_ACCOUNT') && host() == 'DOMAIN_NAME'
           

Replace `SERVICE_ACCOUNT` with the name of the service account.

  2. To update your policy with the rule that you defined in `rule.yaml`, use the following command:
         
         gcloud network-security gateway-security-policies rules import RULE_NAME \
            --source=rule.yaml \
            --location=REGION \
            --gateway-security-policy=policy1
         




### Deploy a Secure Web Proxy instance

Deploy a Secure Web Proxy instance in explicit routing mode in the Virtual Private Cloud (VPC) network that you want to use for egress traffic. When you create the instance, associate it with the policy and rules that you created in previous steps.

Publishing Secure Web Proxy with a Private Service Connect service attachment doesn't support next hop routing mode.

For information about configuring the instance, see [Set up a web proxy](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart#create-a-gateway). You don't need to complete the other steps on that page at this time.

## Deploy Secure Web Proxy as a Private Service Connect service in a hub and spoke model

This section describes how to deploy Secure Web Proxy as a Private Service Connect service, using a hub and spoke model to centralize egress traffic management.

### Publish Secure Web Proxy as a Private Service Connect service

To publish Secure Web Proxy as a service, create a Private Service Connect subnet and service attachment. The subnet and service attachment must share the same region as the Private Service Connect endpoints that access the service attachment.

#### Create a subnet for Private Service Connect

To create a subnet for Private Service Connect, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click **Subnets**.

  4. Click **Add subnet**. In the panel that appears, do the following:

     1. Provide a **Name**.
     2. Select a **Region**.
     3. In the **Purpose** section, select **Private Service Connect**.
     4. For **IP stack type** , select **IPv4 (single-stack)** or **IPv4 and IPv6 (dual-stack)**.
     5. Enter an **IPv4 range**. For example, `10.10.10.0/24`.
     6. If you are creating a dual-stack subnet, set the **IPv6 access type** to **Internal**.
     7. Click **Add**.



###  Cloud Shell 

Do one of the following:

  * To create an IPv4-only Private Service Connect subnet, do the following:
        
        gcloud compute networks subnets create SUBNET_NAME \
            --network=NETWORK_NAME \
            --region=REGION \
            --range=SUBNET_RANGE \
            --purpose=PRIVATE_SERVICE_CONNECT
        

  * To create a dual-stack Private Service Connect subnet, do the following:
        
        gcloud compute networks subnets create SUBNET_NAME \
            --network=NETWORK_NAME \
            --region=REGION \
            --stack-type=IPV4_IPV6 \
            --ipv6-access-type=INTERNAL \
            --range=SUBNET_RANGE \
            --purpose=PRIVATE_SERVICE_CONNECT
        




Replace the following:

  * `SUBNET_NAME`: the name to assign to the subnet.

  * `NETWORK_NAME`: the name of the VPC for the new subnet.

  * `REGION`: the region for the new subnet. This must be the same region as the service you are publishing.

  * `SUBNET_RANGE`: the IPv4 address range to use for the subnet—for example, `10.10.10.0/24`.




#### Create a service attachment

To publish Secure Web Proxy as a service attachment in the central (hub) VPC network, do the following.

This section describes how to create a service attachment that automatically accepts all connections. For information about explicit approval or other configuration options, see [Publish a service with explicit approval](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service-explicit).

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click **Publish service**.

  4. In the **Target details** section, select **Secure Web Proxy**.

  5. Select the Secure Web Proxy instance that you want to publish. The network and region fields are populated with the details for the selected Secure Web Proxy instance.

  6. For **Service name** , enter a name for the service attachment.

  7. Select one or more Private Service Connect subnets for the service. The list is populated with subnets from the selected Secure Web Proxy instance's VPC network.

  8. In the **Connection preference** section, select **Automatically accept all connections**.

  9. Click **Add service**.




###  Cloud Shell 

Use the [`gcloud compute service-attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/create).
    
    
    gcloud compute service-attachments create SERVICE_ATTACHMENT_NAME \
        --target-service=SWP_INSTANCE_URI \
        --connection-preference=ACCEPT_AUTOMATIC \
        --nat-subnets=NAT_SUBNET_NAME \
        --region=REGION \
        --project=PROJECT
    

Replace the following:

  * `SERVICE_ATTACHMENT_NAME`: the name of the service attachment
  * `SWP_INSTANCE_URI`: the URI of the Secure Web Proxy instance, in the following form: `//networkservices.googleapis.com/projects/PROJECT_ID/locations/REGION/gateways/INSTANCE_NAME`
  * `NAT_SUBNET_NAME`: the name of the Private Service Connect subnet
  * `REGION`: the region of the Secure Web Proxy deployment
  * `PROJECT`: the project of the Secure Web Proxy deployment



### Create endpoints

Create an endpoint in each VPC network that needs to send outbound traffic through the centralized Secure Web Proxy instance. By default, an endpoint is accessible only to workloads in its own region.

To allow workloads from any Google Cloud region to access an endpoint, enable the global access option.

**Note:** This section describes the basic steps to create an endpoint. For more information about all configuration options, see the [Create an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) section in the VPC documentation.

Repeat the following steps for each endpoint that you need to create.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Click **Connect endpoint**.

  4. For **Target** , select **Published service**.

  5. For **Target service** , enter the service attachment URI that you want to connect to.

The service attachment URI is in this format: `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`

  6. For **Endpoint name** , enter a name to use for the endpoint.

  7. Select a **Network** for the endpoint.

  8. Select a **Subnetwork** for the endpoint.

  9. Select an **IP address** for the endpoint. If you need a new IP address, you can create one:

     1. Click the **IP address** drop-down menu and select **Create IP address**.
     2. Enter a **Name** and optional **Description** for the IP address.
     3. Select an **IP version**.
     4. If you're creating an IPv4 address, select **Assign automatically** or **Let me choose**.

If you selected **Let me choose** , enter the **Custom IP address** you want to use.

     5. Click **Reserve**.

  10. Optional: To allow clients from any Google Cloud region to access the endpoint, select **Enable global access**.

For more information, see the [Global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) and [Create an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) sections in the VPC documentation.

  11. Click **Add endpoint**.




###  Cloud Shell 

  1. Reserve an internal IP address to assign to the endpoint.
         
         gcloud compute addresses create ADDRESS_NAME \
             --region=REGION \
             --subnet=SUBNET \
             --ip-version=IP_VERSION
         

Replace the following:

     * `ADDRESS_NAME`: the name to assign to the reserved IP address.

     * `REGION`: the region for the endpoint IP address. This must be the same region that contains the service producer's service attachment.

     * `SUBNET`: the name of the subnet for the endpoint IP address.

     * `IP_VERSION`: the IP version of the IP address, which can be either `IPV4` or `IPV6`. `IPV4` is the default. To specify `IPV6`, the IP address must be connected to a [subnet with an internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

  2. Create a forwarding rule to connect the endpoint to the service producer's service attachment.
         
         gcloud compute forwarding-rules create ENDPOINT_NAME \
            --region=REGION \
            --network=NETWORK_NAME \
            --address=ADDRESS_NAME \
            --target-service-attachment=SERVICE_ATTACHMENT
         

**Optional** : To allow clients from any Google Cloud region to access the endpoint, add the `--allow-psc-global-access` flag.

For more information, see the [Global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) and [Create an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) sections in the VPC documentation.

Replace the following:

     * `ENDPOINT_NAME`: the name to assign to the endpoint.

     * `REGION`: the region for the endpoint. This must be the same region that contains the service producer's service attachment.

     * `NETWORK_NAME`: the name of the VPC network for the endpoint.

     * `ADDRESS_NAME`: the name of the reserved address.

     * `SERVICE_ATTACHMENT`: the URI of the service producer's service attachment. For example: `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`




### Point workloads to Private Service Connect endpoints

Configure proxy environmental variables so that each workload uses the IP address of a Private Service Connect endpoint for egress traffic.

For example, for a workload in a Linux or macOS environment, you can use the command line to temporarily configure the `HTTP_PROXY` and `HTTPS_PROXY` environmental variables:
    
    
    export HTTP_PROXY="http://ENDPOINT_IP_ADDRESS:HTTP_PORT"
    export HTTPS_PROXY="https://ENDPOINT_IP_ADDRESS:HTTPS_PORT"
    

Replace the following:

  * `ENDPOINT_IP_ADDRESS`: the internal IP address of your endpoint
  * `HTTP_PORT`: the port for receiving HTTP traffic
  * `HTTPS_PORT`: the port for receiving HTTPS traffic



For information about permanently setting proxy variables in your workloads' environment, see your operating system's documentation.

## What's next?

  * [Configure TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview)
  * [Use tags to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags)
  * [Assign static IP addresses for egress traffic](https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
