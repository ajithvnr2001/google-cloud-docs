---
url: https://docs.cloud.google.com/secure-web-proxy/docs/use-tags/
title: Use tags to create policies \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:36.573800+00:00
---

# Use tags to create policies  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/use-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Use tags to create policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to attach [Resource Manager tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) to Secure Web Proxy policies. Resource Manager tags are labels that you can attach to various Google Cloud resources, such as your virtual machine (VM) instances. You can use tags to enforce conditional access controls across your network with existing organizational labels.

By using these tags, you can perform the following actions:

  * **Segment workloads** : you can uniquely identify different environments like `production` or `development` and service types like `frontend` or `database`.

  * **Centralize access control** : you can base your Secure Web Proxy policies on these tags. For example, you can create a policy rule that says: "Only the traffic that originates from resources that have the `tag segment=production` tag can access a specific set of URLs."




This page shows you how to do the following:

  * Create a Secure Web Proxy instance with an empty policy
  * Create and attach a Resource Manager tag to a VM instance
  * Create a Secure Web Proxy rule
  * Test the connectivity of your entire Secure Web Proxy configuration



## Before you begin

  * Configure the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  * Have an organization administrator [grant you the necessary role to create and update tags](https://docs.cloud.google.com/vpc/docs/use-tags-for-firewalls#grant-tag-roles).

  * Verify that you have the Google Cloud CLI version 406.0.0 or later installed:
        
        gcloud version | head -n1
        

If you have an earlier gcloud CLI version installed, update the version:
        
        gcloud components update --version=406.0.0
        




## Create a Secure Web Proxy instance with an empty policy

To create a Secure Web Proxy instance, you must first create an empty security policy and then create a web proxy that uses the policy.

### Create an empty security policy

###  Console 

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click add_box**Create a policy**.

  3. In the **Name** field, enter a name for the policy, such as `myswppolicy`.

  4. In the **Description** field, enter a description for the policy, such as `My new swp policy`.

  5. For **Regions** , select the region where you want to create the policy, such as `us-central1`.

  6. Click **Create**.




###  Cloud Shell 

  1. Use a text editor to create a `policy.yaml` file.

  2. Add the following code to the `policy.yaml` file:
         
         name: projects/PROJECT_NAME/locations/REGION/gatewaySecurityPolicies/POLICY_NAME
         description: POLICY_DESCRIPTION
         

Replace the following:

     * `PROJECT_NAME`: name of your project

     * `REGION`: region where your policy is created, such as `us-central1`

     * `POLICY_NAME`: name of your policy

     * `POLICY_DESCRIPTION`: description for your policy

  3. Import the security policy by using the [`gcloud network-security gateway-security-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/gateways/import):
         
         gcloud network-security gateway-security-policies import POLICY_NAME \
             --source=POLICY_FILE.yaml \
             --location=REGION
         




### Create a web proxy

###  Console 

  1. In the Google Cloud console, go to the **Web Proxies** page.

[Go to Web Proxies](https://console.cloud.google.com/net-security/swp/web-proxies/list)

  2. Click add_box**Create a secure web proxy**.

  3. In the **Name** field, enter a name for the web proxy, such as `myswp`.

  4. In the **Description** field, enter a description for the web proxy, such as `My new swp`.

  5. For **Routing mode** , select one of the following options:

     * **Explicit** : deploys your Secure Web Proxy instance in explicit proxy mode.
     * **Next hop** : deploys your Secure Web Proxy instance in next hop mode.
  6. For **Regions** , select the region where you want to create the web proxy, such as `us-central1`.

  7. For **Network** , select the network where you want to create the web proxy.

  8. For **Subnetwork** , select the [VPC subnet](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create-vpc-subnet) that you created during the [initial setup](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  9. Optional: In the **Web proxy IP address** field, enter the Secure Web Proxy IP address.

You can enter an IP address from the range of Secure Web Proxy IP addresses that reside in the subnetwork you created in the previous step. If you don't enter the IP address, then your Secure Web Proxy instance automatically chooses an IP address from the selected subnetwork.

  10. For **Certificate** , select the certificate that you want to use to create the web proxy.

  11. For **Policy** , select the policy that you created to associate the web proxy with.

  12. Click **Create**.




###  Cloud Shell 

  1. Use a text editor to create a `gateway.yaml` file.

  2. Add the following code to the `gateway.yaml` file:
         
         name: projects/PROJECT_NAME/locations/REGION/gateways/GATEWAY_NAME
         type: SECURE_WEB_GATEWAY
         ports: [GATEWAY_PORT_NUMBERS]
         certificateUrls: [CERTIFICATE_URLS]
         gatewaySecurityPolicy: projects/PROJECT_NAME/locations/REGION/gatewaySecurityPolicies/POLICY_NAME
         network: projects/PROJECT_NAME/global/networks/NETWORK_NAME
         subnetwork: projects/PROJECT_NAME/regions/REGION/subnetworks/SUBNETWORK
         routingMode: ROUTING_MODE
         addresses: [GATEWAY_IP_ADDRESS]
         scope: samplescope
         

**Optional** : To allow client applications from other Google Cloud regions to connect to your proxy, enable [global access](https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access) when creating your Secure Web Proxy instance.

In the `gateway.yaml` file, add the `allowGlobalAccess` field and set it to `true`.

**Important** : You can enable `allowGlobalAccess` only when you create a Secure Web Proxy instance. You can't configure this setting later.
         
         name: projects/PROJECT_NAME/locations/REGION/gateways/GATEWAY_NAME
         type: SECURE_WEB_GATEWAY
         ports: [GATEWAY_PORT_NUMBERS]
         certificateUrls: [CERTIFICATE_URLS]
         gatewaySecurityPolicy: projects/PROJECT_NAME/locations/REGION/gatewaySecurityPolicies/POLICY_NAME
         network: projects/PROJECT_NAME/global/networks/NETWORK_NAME
         subnetwork: projects/PROJECT_NAME/regions/REGION/subnetworks/SUBNETWORK
         addresses: [GATEWAY_IP_ADDRESS]
         scope: samplescope
         allowGlobalAccess: true
         

Replace the following:

     * `GATEWAY_NAME`: name of this Secure Web Proxy instance

     * `GATEWAY_PORT_NUMBERS`: list of port numbers for this gateway, such as `[80,443]`

     * `CERTIFICATE_URLS`: list of SSL certificate URLs

     * `SUBNETWORK`: [VPC subnet](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create-vpc-subnet) that you created during the [initial setup](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps)

     * `ROUTING_MODE`: specify the required web proxy routing mode:

       * `EXPLICIT_ROUTING_MODE`: deploys your Secure Web Proxy instance in explicit proxy mode
       * `NEXT_HOP_ROUTING_MODE`: deploys your Secure Web Proxy instance in next hop mode
     * `GATEWAY_IP_ADDRESS`: optional list of IP addresses for your Secure Web Proxy instances within the proxy subnets that you previously created in the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps)

If you choose not to list IP addresses, omit the field to let the web proxy choose an IP address for you.

  3. Create the Secure Web Proxy instance by using the [`gcloud network-services gateways import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/import):
         
         gcloud network-services gateways import GATEWAY_NAME \
             --source=gateway.yaml \
             --location=REGION
         




### Test connectivity

To test connectivity, use the `curl` command from any virtual machine (VM) instance within your Virtual Private Cloud (VPC) network:
    
    
      curl -x https://GATEWAY_IP_ADDRESS:PORT_NUMBER https://www.example.com --proxy-insecure
      

If everything is working correctly, then your Secure Web Proxy instance returns a `403 Forbidden` status code. This error confirms the following:

  * The Secure Web Proxy instance has been successfully deployed and is actively receiving traffic.

  * The Secure Web Proxy policy is correctly enforcing the default security posture of rejecting all traffic until you define specific `allow` rules in the next sections.




## Create and attach Resource Manager tags

  1. [Create secure tag keys and values](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#create-tags)

**Important:** When you create your tag, designate it with the `GCE_FIREWALL` purpose. Google Cloud networking products, including Secure Web Proxy, require the `GCE_FIREWALL` purpose to successfully apply tags and enforce security policies based on workload identity.

**Example** : To create a tag for restricted environments, follow these steps:

     1. Create the tag key (`access-level`) by using the [`gcloud resource-manager tags keys create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create) with the purpose set to `GCE_FIREWALL`. 

     2. Retrieve the tag key ID either from the output of the creation command or by using the [`gcloud resource-manager tags keys list` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/list). You need this ID to link tag values to this specific tag key.

     3. Create the tag value (`restricted`) by using the [`gcloud resource-manager tags values create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create), specifying the tag key ID as the parent.
    
    # Create the tag key
    # The output provides a unique ID, such as "tagKeys/1234567890"
    
    gcloud resource-manager tags keys create "access-level" \
        --parent="organizations/1234567890" \
        --purpose="GCE_FIREWALL" \
        --purpose-values="execution_env=ANS"
    
    # Create the tag value and connect it to the key
    # The "--parent" flag identifies to which key this value belongs
    
    gcloud resource-manager tags values create "restricted" \
        --parent="tagKeys/1234567890"
    

  2. [Attach tags to VM instances](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#bind-tags)

Attaching these tags associates the outbound traffic from your VM instances with a specific tag identity, which allows the proxy to recognize the workload and enforce your security policy rules.

**Example** : Consider that you have a VM instance named `internal-tool`. You can attach the `restricted` tag value to `internal-tool` by using the [`gcloud resource-manager tags bindings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create). This tag assignment allows your proxy to identify the traffic that originates from the `internal-tool` VM instance.
         
         # Attach the "restricted" tag to a specific VM instance
         
         
         gcloud resource-manager tags bindings create \
             --parent="//[compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/internal-tool](https://compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/internal-tool)" \
             --tag-value="tagValues/987654321"
         




## Create a Secure Web Proxy rule

###  Console 

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click the name of your policy, such as `myswppolicy`.

  3. Click add_box**Add rule**.

  4. For each rule, do the following:

     1. For **Priority** , enter a numeric evaluation order for the rule. Rules are evaluated from highest to lowest priority, where `0` is the highest priority.

     2. In the **Name** field, enter a name for the rule.

     3. In the **Description** field, enter a description for the rule.

     4. For **Action** , select one of the following options: 

        * **Allow** : to allow connection requests that match the rule.
        * **Deny** : to deny connection requests that match the rule.
     5. For the **Status** field, select one of the following options for the rule enforcement:

        * **Enabled** : to enforce the rule on your Secure Web Proxy instance.
        * **Disabled** : to not enforce the rule on your Secure Web Proxy instance.
     6. In the **Session match** section, specify the unique ID of the tag that you created in the previous section. For example:
            
            sessionMatcher: "source.matchTag('TAG_VALUE') && host() == 'example.com'"
            

For more information about the syntax for `SessionMatcher`, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).

     7. In the **Application match** section, specify the criteria for matching the request.

     8. Click **Add rule**.




###  Cloud Shell 

  1. Use a text editor to create the `rule.yaml` file.

  2. To allow access to a URL from the required tag, add the following code to the `rule.yaml` file:
         
         name: projects/PROJECT_NAME/locations/REGION/gatewaySecurityPolicies/POLICY_NAME/rules/RULE_NAME
         description: RULE_DESCRIPTION
         enabled: true
         priority: RULE_PRIORITY
         sessionMatcher: CEL_EXPRESSION
         basicProfile: ALLOW
         

Replace the following:

     * `RULE_NAME`: name of this rule 
     * `RULE_DESCRIPTION`: description for the rule
     * `RULE_PRIORITY`: priority of this rule; a lower number corresponds to a higher priority
     * `CEL_EXPRESSION`: a Common Expression Language (CEL) expression. For more information, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).

For example, to allow access to `example.com` from the required tag, add the following `sessionMatcher` line to the YAML file:
    
    sessionMatcher: "source.matchTag('TAG_VALUE') && host() == 'example.com'"
    

Replace `TAG_VALUE` with the tag that you want to allow. Make sure that the tag follows the numeric resource identifier format; for example, `tagValues/567890123456`.

  3. Import the rules that you created by using the [`gcloud network-security gateway-security-policies rules import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/import):
         
         gcloud network-security gateway-security-policies rules import RULE_NAME \
             --source=RULE_FILE.yaml \
             --location=REGION \
             --gateway-security-policy=POLICY_NAME
         




## Test the policy configuration

You can test connectivity again to validate that your Secure Web Proxy policy, which relies on Resource Manager tags for identity, is working as intended.

To test connectivity, use the `curl` command from any VM that's associated with the appropriate `TAG_VALUE` tag.
    
    
    curl -x https://IPv4_ADDRESS:443 http://example.com
    --proxy-insecure
    

Replace `IPv4_ADDRESS` with the IPv4 address of your Secure Web Proxy instance.

If everything works correctly, then you receive either a `200 OK` or a `403 Forbidden` status code. These responses confirm the following key outcomes:

  * **Tag-based success** : a `200 OK` status code validates that the traffic from a VM with the correct Resource Manager tag attached to it matches the policy rule and is allowed through the proxy. This verified match results in a successful connection.

  * **Tag-based denial** : a `403 Forbidden` status code verifies that the traffic from a VM either without the specified tag or with an incorrect tag is correctly denied access by the policy. This enforcement proves that your tag-based segmentation and enforcement is working as intended.




## What's next

  * [Use a URL list to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list)
  * [Use service accounts to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
