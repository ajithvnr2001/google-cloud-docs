---
url: https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list/
title: Use URL lists to create policies \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:59:33.489918+00:00
---

# Use URL lists to create policies  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Use URL lists to create policies Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use URL lists to create and manage granular access policies for your outbound web traffic within your Secure Web Proxy instance. Instead of creating individual rules for every website, URL lists let you define a reusable, centralized collection of domains, hostnames, and specific URL patterns.

Here are a few key benefits of using URL lists:

  * **Simplify policy management** : you can apply a large set of `allow` or `deny` rules with a single reference in your security policy.

  * **Enforce precise control** : you can use specific syntax to match entire domains, subdomains, or exact URL paths. This helps ensure that your workloads can access only authorized destinations.

  * **Secure web access** : you can efficiently secure and audit web access across your Google Cloud environment.




## Before you begin

  * Complete the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

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




## Create and configure a URL list

### Console

  1. In the Google Cloud console, go to the **URL Lists** page.

[Go to URL Lists](https://console.cloud.google.com/net-security/swp/url-lists/list)

  2. Click add_box**Create a URL list**. The **Create URL list** page opens.

  3. In the **Name** field, enter a name for the URL list, such as `example-org-allowed-list`.

  4. In the **Description** field, enter a description for the URL list, such as `My new URL list`.

  5. For **Regions** , select the region where you want to create the URL list, such as `us-central1`.

  6. To add the list of hosts, URLs, or patterns to match, in the **URL list** field, either enter the details or click **Upload list** to upload a custom list of URLs. For more information, see [UrlList syntax reference](https://docs.cloud.google.com/secure-web-proxy/docs/url-list-syntax-reference).

  7. Click **Create**.




###  Cloud Shell 

  1. Use a text editor to create the `url_list.yaml` file.

  2. Add the following code to the `url_list.yaml` file:
         
         name: projects/PROJECT_ID/locations/REGION/urlLists/URL_LIST_NAME
           values: URL_LIST
         

Replace the following:

     * `PROJECT_ID`: unique ID of your Google Cloud project

     * `REGION`: region where your URL list is created, such as `us-central1`

     * `URL_LIST_NAME`: name of the URL list

     * `URL_LIST`: list of hosts, URLs, or patterns to match

For more information, see [UrlList syntax reference](https://docs.cloud.google.com/secure-web-proxy/docs/url-list-syntax-reference).

The following is an example of a URL list rule file:
    
    name: projects/PROJECT_ID/locations/REGION/urlLists/example-org-allowed-list
    values:
      - www.example.com
      - about.example.com
      - "*.google.com"
      - "github.com/example-org/*"
    

The asterisk (`*`) character has a special meaning in YAML. You must add quotation marks around URLs that include an `*` character.

  3. Import the URL list that you created by using the [`gcloud network-security url-lists import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/url-lists/import) so that your Secure Web Proxy rule can reference it.
         
         gcloud network-security url-lists import URL_LIST_NAME \
             --location=REGION \
             --project=PROJECT_ID \
             --source=url_list.yaml
         




## Add a Secure Web Proxy rule

### Console

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click the name of your policy, such as `myswppolicy`.

  3. Click add_box**Add rule**.

  4. For each rule, do the following:

     1. For **Priority** , enter a numeric evaluation order for the rule. Rules are evaluated from highest to lowest priority, where `0` is the highest priority.

     2. In the **Name** field, enter a name for the rule, such as `allow-org-url-list`.

     3. In the **Description** field, enter a description for the rule.

     4. For **Action** , select one of the following options:

        * **Allow** : to allow connection requests that match the rule.
        * **Deny** : to deny connection requests that match the rule.
     5. For the **Status** field, select one of the following options for the rule enforcement:

        * **Enabled** : to enforce the rule on your Secure Web Proxy instance.
        * **Disabled** : to not enforce the rule on your Secure Web Proxy instance.
     6. In the **Session Match** section, specify the unique name of the URL list that you created in the previous section. For example:
            
            sessionMatcher: "inUrlList(host(), 'projects/PROJECT_ID/locations/REGION/urlLists/URL_LIST_NAME)"
              

For more information about the syntax for `SessionMatcher`, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).

     7. In the **Application Match** section, specify the criteria for matching the request.

     8. Click **Add rule**.




###  Cloud Shell 

  1. Use a text editor to create a `rule.yaml` file.

  2. Add the following code to the `rule.yaml` file:
         
         name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/POLICY_NAME/rules/RULE_NAME
         basicProfile: ALLOW
         enabled: true
         priority: RULE_PRIORITY
         description: RULE_DESCRIPTION
         sessionMatcher: SESSION_CEL_EXPRESSION
         applicationMatcher: APPLICATION_CEL_EXPRESSION
         

Replace the following:

     * `PROJECT_ID`: unique ID of your Google Cloud project

     * `REGION`: region that this rule applies to

     * `POLICY_NAME`: name of an existing security policy that your Secure Web Proxy instance uses

     * `RULE_NAME`: name of the rule

     * `PRIORITY_VALUE`: priority of the rule; a lower number corresponds to a higher priority 

     * `RULE_DESCRIPTION`: description for the rule

     * `SESSION_CEL_EXPRESSION`: a Common Expression Language (CEL) expression. For more information, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).

     * `APPLICATION_CEL_EXPRESSION`: a CEL expression for your application

The following is an example of a rule file:
    
    name: projects/PROJECT_ID/locations/REGION/urlLists/allow-repos
    basicProfile: ALLOW
    enabled: true
    priority: 100
    description: Allow access to our list of known code repos.
    sessionMatcher: "inUrlList(host(), 'projects/PROJECT_ID/locations/REGION/urlLists/URL_LIST_NAME')"
    

  3. Import the rule that you created by using the [`gcloud network-security gateway-security-policies rules import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/import).
         
         gcloud network-security gateway-security-policies rules import RULE_NAME \
           --location=REGION \
           --project=PROJECT_ID \
           --source=rule.yaml \
           --gateway-security-policy=POLICY_NAME
         




## Test the policy configuration

You can test connectivity again to validate that the URL list-based access rules are correctly configured and actively enforced by your Secure Web Proxy instance.

To test connectivity, use the following `curl` command:
    
    
    curl -x https://SWP_IP_ADDRESS:SWP_PORT_NUMBER HTTP_TEST_ADDRESS
    --proxy-insecure
    

Replace the following:

  * `SWP_IP_ADDRESS`: IP address of your Secure Web Proxy instance

  * `SWP_PORT_NUMBER`: port number of your web proxy, such as `443`

  * `HTTP_TEST_ADDRESS`: an address to test, such as `https://www.example.com`. It matches a host or URL entry in your `url_list`.




If everything works correctly, then you receive a `200 OK` response. This response confirms that the outbound traffic to a URL that's listed in your URL list and referenced by the security policy rule is successfully allowed through your Secure Web Proxy instance.

## What's next

  * [Use tags to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags)
  * [Use service accounts to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
