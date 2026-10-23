---
url: https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts/
title: Use service accounts to create policies \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:02.676936+00:00
---

# Use service accounts to create policies  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Use service accounts to create policies Stay organized with collections  Save and categorize content based on your preferences. 

A service account is a special non-human Google Account that applications, automated processes, or compute workloads, such as a Compute Engine instance, use to make [authorized API calls](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#authorizingrequests). Unlike user accounts, a service account is identified solely by its unique email address.

Applications use service accounts to authenticate and gain access to Google Cloud resources. When an application authenticates by using a service account, it gains access to the resources that the service account has been assigned explicit Identity and Access Management permissions for. This provides a secure, auditable, and centralized method for machine-to-machine authorization.

For Secure Web Proxy, service accounts play a crucial role in authorization and policy enforcement. By using a service account to identify the traffic source of a workload, you can create granular Secure Web Proxy policies that specifically allow or deny web traffic based on the application's identity, rather than just its IP address.

This page shows you how to do the following:

  * Create a Secure Web Proxy instance with an empty policy
  * Create a service account and grant IAM roles
  * Create Secure Web Proxy rules
  * Test connectivity of your entire Secure Web Proxy configuration



## Before you begin

  * Complete the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  * Request an organization administrator to [grant you access to a service account](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

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




## Create a service account and grant IAM roles

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create): use the [`gcloud iam service-accounts create` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) to create a service account named `my-swp-sa` in your Google Cloud project.
         
         gcloud iam service-accounts create my-swp-sa \
             --display-name="Secure Web Proxy service account" \
             --description="Service account for Secure Web Proxy instances"

  2. [Grant IAM roles to the service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts): use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) to grant the necessary [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to the service account so that it can manage or use resources in your Google Cloud project.

For example, to allow the service account to use network resources, grant it the [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`).
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:my-swp-sa@PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/compute.networkUser"

Replace `PROJECT_ID` with the ID of your Google Cloud project.




## Create a Secure Web Proxy rule

###  Console 

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click the name of your policy that you previously created, such as `myswppolicy`.

  3. Click add_box**Add rule**.

  4. For each rule, do the following:

     1. In the **Priority** field, enter a numeric evaluation order for the rule. Rules are evaluated from highest to lowest priority, where `0` is the highest priority.

     2. In the **Name** field, enter a name for the rule.

     3. In the **Description** field, enter a description for the rule.

     4. For **Action** , select one of the following options: 

        * **Allow** : to allow connection requests that match the rule.
        * **Deny** : to deny connection requests that match the rule.
     5. For the **Status** field, select one of the following options for the rule enforcement:

        * **Enabled** : to enforce the rule on your Secure Web Proxy instance.
        * **Disabled** : to not enforce the rule on your Secure Web Proxy instance.
     6. In the **Session Match** section, specify the email address of the service account that you previously created. For example:
            
            sessionMatcher: "source.matchServiceAccount(SERVICE_ACCOUNT) && host() == 'example.com'"
              

For more information about the syntax for `SessionMatcher`, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).

     7. In the **Application Match** section, specify the criteria for matching the request.

     8. Click **Add rule**.

  5. To add another rule, click **Add rule**.




###  Cloud Shell 

  1. Use a text editor to create the `rule.yaml` file.

  2. To allow access to a URL from the appropriate service account, add the following to the `rule.yaml` file that you created:
         
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

For example, to allow access to `example.com` from the resource with the required service account, add the following code to the YAML file that you created for the `sessionMatcher`:
    
    ```yaml
    sessionMatcher: "source.matchServiceAccount('SERVICE_ACCOUNT') && host() == 'example.com'"
    ```
    

Replace `SERVICE_ACCOUNT` with the service account that you want to allow. This must be the service account's email address.

  3. Import the rules that you created by using the [`gcloud network-security gateway-security-policies rules import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/gateway-security-policies/rules/import):
         
         gcloud network-security gateway-security-policies rules import RULE_NAME \
             --source=RULE_FILE.yaml \
             --location=REGION \
             --gateway-security-policy=POLICY_NAME
         




## Test connectivity

You can test connectivity again to validate that your entire Secure Web Proxy configuration—including the service account, security policy rules, and the gateway—is working as intended.

To test connectivity, use the `curl` command from the resource—like a VM instance—with the attached `SERVICE_ACCOUNT`:
    
    
    curl -x https://IPv4_ADDRESS:443 http://example.com 
    --proxy-insecure
    

Replace `IPv4_ADDRESS` with the IPv4 address of your Secure Web Proxy instance.

If everything works correctly, then you receive a `200 OK` status code. This status code confirms the following key outcomes:

  * **Successful authorization** : it proves that the traffic originating from the resource is correctly identified by the assigned service account, and that this identity successfully matches the `allow` rule you added to the security policy.

  * **End-to-end functionality** : it validates that the traffic is flowing correctly through the configured path—from the resource > to the Secure Web Proxy instance > passing the security policy > and reaching the external destination.




## What's next

  * [Use a URL list to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list)
  * [Use tags to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
