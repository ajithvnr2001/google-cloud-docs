---
url: https://docs.cloud.google.com/secure-web-proxy/docs/quickstart/
title: Quickstart: Deploy a Secure Web Proxy instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:53.232889+00:00
---

# Quickstart: Deploy a Secure Web Proxy instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and deploy a Secure Web Proxy instance

This quickstart explains how to deploy and test a Secure Web Proxy instance. The steps describe deploying Secure Web Proxy in explicit routing mode, functioning as an _explicit proxy_.

Secure Web Proxy instances in explicit routing mode can be [deployed as a Private Service Connect service](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment). Alternatively, you can [deploy Secure Web Proxy in next hop routing mode](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop).

Deploying Secure Web Proxy in explicit routing mode includes the following steps:

  1. Create a Secure Web Proxy policy.
  2. Create Secure Web Proxy rules and add them to the policy.
  3. Set up the Secure Web Proxy instance in explicit routing mode.
  4. Test connectivity from a Linux virtual machine (VM) instance to confirm that the proxy and its policies are functioning correctly.

[ ![Deploy Secure Web Proxy in explicit proxy routing mode.](https://docs.cloud.google.com/static/secure-web-proxy/images/swp-explicit-proxy-mode.svg)](https://docs.cloud.google.com/static/secure-web-proxy/images/swp-explicit-proxy-mode.svg) Deploy Secure Web Proxy in the explicit proxy routing mode (click to enlarge).

## Before you begin

  1. Complete the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  2. Optional: To run the `gcloud` command-line examples specified in this document, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) in any of the following development environments:

###  Cloud Shell 

To use an online terminal with the gcloud CLI already set up, activate Cloud Shell.

At the end of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

If you previously installed the gcloud CLI, then make sure that you have the latest available version by running the the [`gcloud components update` command](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).

### Local shell

To use a local development environment, follow these steps:

     1. [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install)
     2. [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize)

  3. Create or select an existing Google Cloud project.

If you don't plan to keep the resources that you create in this procedure, then we recommend that you create a project instead of selecting an existing project. After completing the steps of this quickstart, you can then delete the project to remove all resources associated with the project.

### Console

In the Google Cloud console, on the project selector page, either [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) or select an existing project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

###  Cloud Shell 

     1. Create a Google Cloud project.
            
            gcloud projects create PROJECT_ID
            

Replace `PROJECT_ID` with the project ID of your choice.

     2. Select the Google Cloud project that you created.
            
            gcloud config set project PROJECT_ID
            

  4. Create a Linux VM instance.
         
         gcloud compute instances create swp-test-vm \
             --subnet=default \
             --zone=ZONE \
             --image-project=debian-cloud \
             --image-family=debian-11
         

Replace `ZONE` with the zone of your test VM instance.

Compute Engine grants the [Compute Instance Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`) to the user who creates the VM instance. Compute Engine also adds that user to the sudo group.

  5. Create a firewall rule.
         
         gcloud compute firewall-rules create default-allow-ssh \
             --direction=INGRESS \
             --priority=1000 \
             --network=default \
             --action=ALLOW \
             --rules=tcp:22 \
             --source-ranges=0.0.0.0/0
         




### Required roles

Make sure that you have the following roles to complete the tasks in this tutorial:

  * [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)

  * [Certificate Manager Editor role](https://docs.cloud.google.com/certificate-manager/docs/permissions#certificatemanager.editor) (`roles/certificatemanager.editor`)




For more information, see the following:

  * [Secure Web Proxy roles and permissions](https://docs.cloud.google.com/secure-web-proxy/docs/roles-permissions)
  * [Compute Engine IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam)



## Create a Secure Web Proxy policy

This section explains the steps to create a Secure Web Proxy policy. The policy can then serve as the container for all security rules that govern traffic flow through the Secure Web Proxy. After creating the policy, you can create rules and add them to the policy.

### Console

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click add_box**Create a policy**.

  3. In the **Name** field, enter a name for the policy, such as `myswppolicy`.

  4. In the **Description** field, enter a description for the policy, such as `My new swp policy`.

  5. For **Regions** , select the region where you want to create the policy, such as `us-central1`.

  6. If you want to create rules for your policy, then click **Add rule**. For more information, see the Create Secure Web Proxy rules section.

  7. Click **Create**.


**Important:** To create a policy with TLS inspection, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).

###  Cloud Shell 

  1. Use a text editor to create a `policy.yaml` file.

  2. Add the following code to the `policy.yaml` file:
         
         description: basic Secure Web Proxy policy
           name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/myswppolicy
         

Replace the following:

     * `PROJECT_ID`: ID of your project
     * `REGION`: region where your policy is created, such as `us-central1`
**Important:** To create a policy with TLS inspection, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).
  3. Create the Secure Web Proxy policy.
         
         gcloud network-security gateway-security-policies import myswppolicy \
             --source=policy.yaml \
             --location=REGION
         




## Create Secure Web Proxy rules

This section details the steps to create Secure Web Proxy rules. Rules help define the actual access controls for web traffic.

Within the policy that you previously created, you can define rules such as `allow-wikipedia-org`. These rules specify the criteria for matching web sessions—for example, matching a specific host like `www.wikipedia.org`—and then either allowing or denying the web traffic.

###  Console 

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click the name of your policy, such as `myswppolicy`.

  3. Click add_box**Add rule**.

  4. For each rule, do the following:

     1. For **Priority** , enter a numeric evaluation order for the rule. Rules are evaluated from highest to lowest priority, where `0` is the highest priority.

     2. In the **Name** field, enter a name for the rule, such as `allow-wikipedia-org`.

     3. In the **Description** field, enter a description for the rule, such as `Allow wikipedia.org`.

     4. For **Action** , select one of the following options:

        * **Allow** : to allow connection requests that match the rule.
        * **Deny** : to deny connection requests that match the rule.
     5. For the **Status** field, select one of the following options for the rule enforcement:

        * **Enabled** : to enforce the rule on your Secure Web Proxy instance.
        * **Disabled** : to not enforce the rule on your Secure Web Proxy instance.
     6. In the **Session Match** section, specify the criteria for matching the session, such as `host() == 'www.wikipedia.org'`.

For more information about the syntax for `SessionMatcher`, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).

     7. In the **Application Match** section, specify the criteria for matching the request. Because we haven't enabled the rule for TLS inspection, the request can match only HTTP traffic.

For more information about matching TCP traffic, see [Configure TCP proxy rules](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules#configure-tcp-proxy-rules).

     8. Click **Create**.

  5. To add another rule, click **Add rule**.


**Important:** To create a rule with TLS inspection, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).

###  Cloud Shell 

  1. Use a text editor to create the `rule.yaml` file.

  2. Add the following code to the `rule.yaml` file. For more information about the syntax for `SessionMatcher`, see [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).
         
         name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1/rules/RULE_NAME
         description: Allow wikipedia.org
         enabled: true
         priority: 1
         basicProfile: ALLOW
         sessionMatcher: host() == 'www.wikipedia.org'
         

Replace the following:

     * `PROJECT_ID`: ID of your project
     * `REGION`: region of your policy
     * `RULE_NAME`: name of the rule, such as `allow-wikipedia-org`.
**Important:** To create a rule with TLS inspection, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).
  3. Create the security policy rule.
         
         gcloud network-security gateway-security-policies rules import allow-wikipedia-org \
             --source=rule.yaml \
             --location=REGION \
             --gateway-security-policy=policy1
         




## Set up a web proxy

This section describes how to deploy Secure Web Proxy in explicit routing mode, functioning as an _explicit proxy_. It also explains how to associate the previously created policy and rules with your Secure Web Proxy instance, ensuring that all traffic flowing through it is subject to the defined access controls.

###  Console 

  1. In the Google Cloud console, go to the **Web Proxies** page.

[Go to Web Proxies](https://console.cloud.google.com/net-security/swp/web-proxies/list)

  2. Click add_box**Create a secure web proxy**.

  3. In the **Name** field, enter a name for the web proxy, such as `myswp`.

  4. In the **Description** field, enter a description for the web proxy, such as `My new swp`.

  5. For **Routing mode** , select the **Explicit** option.

  6. For **Regions** , select the region where you want to create the web proxy, such as `us-central1`.

  7. For **Network** , select the network where you want to create the web proxy.

  8. For **Subnetwork** , select the [VPC subnet](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create-vpc-subnet) that you previously created as part of the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  9. Optional: In the **Web proxy IP address** field, enter the Secure Web Proxy IP address.

You can enter an IP address from the range of Secure Web Proxy IP addresses that reside in the subnetwork you created in the previous step. If you don't enter the IP address, then your Secure Web Proxy instance automatically chooses an IP address from the selected subnetwork.

  10. For **Ports** , enter the port numbers, such as `80` or `443`, on which you want the web proxy to listen.


**Important:** Secure Web Proxy supports a maximum of five frontend ports. You can't change the selected ports after creating the Secure Web Proxy gateway.

  1. For **Certificate** , select the certificate that you want to use to create the web proxy.

  2. For **Associated policy** , select the policy that you created to associate the web proxy with.

  3. Click **Create**.




###  Cloud Shell 

  1. Use a text editor to create a `gateway.yaml` file.

  2. Add the following code to the `gateway.yaml` file:
         
         name: projects/PROJECT_ID/locations/REGION/gateways/myswp
         type: SECURE_WEB_GATEWAY
         addresses: ["IP_ADDRESS"]
         ports: [443]
         gatewaySecurityPolicy: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
         network: projects/PROJECT_ID/global/networks/NETWORK
         subnetwork: projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK
         routingMode: EXPLICIT_ROUTING_MODE
         

**Optional** : To allow client applications from other Google Cloud regions to connect to your proxy, enable [global access](https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access) when creating your Secure Web Proxy instance.

In the `gateway.yaml` file, add the `allowGlobalAccess` field and set it to `true`.

**Important** : You can enable `allowGlobalAccess` only when you create a Secure Web Proxy instance. You can't configure this setting later.
         
         name: projects/PROJECT_ID/locations/REGION/gateways/swp1
         type: SECURE_WEB_GATEWAY
         addresses: ["IP_ADDRESS"]
         ports: [443]
         gatewaySecurityPolicy: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
         network: projects/PROJECT_ID/global/networks/NETWORK
         subnetwork: projects/PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK
         routingMode: EXPLICIT_ROUTING_MODE
         allowGlobalAccess: true
         

Replace the following:

     * `PROJECT_ID`: ID of your project
     * `REGION`: region where your Secure Web Proxy instance is created
     * `IP_ADDRESS`: IP address of your Secure Web Proxy instance
     * `NETWORK`: network of your Secure Web Proxy instance
     * `SUBNETWORK`: subnetwork of your Secure Web Proxy instance. You must use the [VPC subnet](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create-vpc-subnet) that you previously created as part of the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).
**Important:** Secure Web Proxy supports a maximum of five frontend ports. You can't change the selected ports after creating the Secure Web Proxy gateway.
  3. Create a Secure Web Proxy instance based on the `gateway.yaml` file.
         
         gcloud network-services gateways import myswp \
             --source=gateway.yaml \
             --location=REGION
         

A Secure Web Proxy instance can take several minutes to deploy.




**Note:** To improve the security of your Secure Web Proxy instance, [configure VPC Service Controls](https://docs.cloud.google.com/secure-web-proxy/docs/vpc-sc-support).

## Test connectivity

This section focuses on testing the connectivity from a Linux VM to confirm that the newly deployed Secure Web Proxy, its policies, and its associated rules are functioning correctly.

  1. Connect to the VM that you previously provisioned.
         
         gcloud compute ssh swp-test-vm \
             --zone=ZONE
         

Replace `ZONE` with the zone of your test VM instance.

  2. Test the Secure Web Proxy instance.
         
         curl -s -o /dev/null -w "%{http_code}\\n" -x IP_ADDRESS:443 https://www.wikipedia.org
         

Replace `IP_ADDRESS` with the IP address of your Secure Web Proxy instance.

This command prints the HTTP status code that's returned from `www.wikipedia.org`. If the command is successful, then the status code is `200`. However, if there's an issue with the proxy, then the command returns a `000` status code to indicate a connection error. To view the detailed error messages, add the `-v` option to the command.




We haven't configured TLS inspection in the example mentioned on this page. For more information about how to configure Secure Web Proxy for TLS inspection and then test your Secure Web Proxy instance, see [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).

**Important:** When you provision a Secure Web Proxy instance, a Cloud NAT gateway is created to enable internet access. Only Secure Web Proxy endpoints in that region and network have access to the Cloud NAT gateway. No other endpoint, such as a VM instance or a Google Kubernetes Engine (GKE) node, is allowed to route traffic through the gateway. For more information, see [Assign static IP addresses for egress traffic](https://docs.cloud.google.com/secure-web-proxy/docs/assign-static-ip-addresses-for-egress-traffic).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the `swp1` Secure Web Proxy instance

**Important:** When deleting your Secure Web Proxy instance, you must also delete its associated [Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/overview) and [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) as described in the Delete the Cloud NAT gateway and Delete the Cloud Router sections.

###  Console 

  1. In the Google Cloud console, go to the **Web Proxies** page. You can view the list of all web proxies or just the web proxies that are available in a particular network.

[Go to Web Proxies](https://console.cloud.google.com/net-security/swp/web-proxies/list)

  2. Select the web proxy that you want to delete. Here, the name of the web proxy is `swp1`.

  3. Click **Delete** , and then click **Delete** again to confirm.




###  Cloud Shell 
    
    
    gcloud network-services gateways delete swp1 \
        --location=REGION
    

Replace `REGION` with the region of your Secure Web Proxy instance.

### Delete the Cloud NAT gateway

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Select the Cloud NAT gateway that was auto-generated for your Secure Web Proxy instance. The Cloud NAT gateway is typically named `swg-autogen-nat`.

  3. Click **Delete** , and then click **Delete** again to confirm.




###  Cloud Shell 

  1. Optional: To identify the name of the auto-generated Cloud Router, list the routers in your region.
         
         gcloud compute routers list \
             --region=REGION \
             --filter="name:(swg-autogen-router-*)" \
             --format="value(name)"
         

Replace `REGION` with the region of your Secure Web Proxy instance.

  2. Delete the Cloud NAT gateway.
         
         gcloud compute routers nats delete NAT_NAME \
             --router=ROUTER_NAME \
             --region=REGION
         

Replace the following:

     * `NAT_NAME`: name of the Cloud NAT gateway, typically `swg-autogen-nat`
     * `ROUTER_NAME`: name of the Cloud Router that's associated with the Cloud NAT gateway. The name of the router typically starts with `swg-autogen-router-`.
     * `REGION`: region of the Cloud NAT gateway



### Delete the Cloud Router

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router that was auto-generated for your Secure Web Proxy instance. The name of the router typically starts with `swg-autogen-router-`.

  3. Click **Delete** , and then click **Delete** again to confirm.




###  Cloud Shell 
    
    
    gcloud compute routers delete ROUTER_NAME \
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: name of the Cloud Router
  * `REGION`: region of the Cloud Router



### Delete the `allow-wikipedia-org` rule

###  Console 

  1. In the Google Cloud console, go to the **Web Proxies** page. You can view the list of all web proxies or just the web proxies that are available in a particular network.

[Go to Web Proxies](https://console.cloud.google.com/net-security/swp/web-proxies/list)

  2. Click your policy. Here, the name of the policy is `policy1`.

  3. Select the rule that you want to delete. Here, the name of the rule is `allow-wikipedia-org`.

  4. Click **Delete** , and then click **Delete** again to confirm.




###  Cloud Shell 
    
    
    gcloud network-security gateway-security-policies rules delete allow-wikipedia-org \
        --location=REGION \
        --gateway-security-policy=policy1
    

Replace `REGION` with the region of your policy.

### Delete the `policy1` Secure Web Proxy policy

###  Console 

  1. In the Google Cloud console, go to the **Web Proxies** page. You can view the list of all web proxies or just the web proxies that are available in a particular network.

[Go to Web Proxies](https://console.cloud.google.com/net-security/swp/web-proxies/list)

  2. Select the policy that you want to delete. Here, the name of the policy is `policy1`.

  3. Click **Delete** , and then click **Delete** again to confirm.




###  Cloud Shell 
    
    
    gcloud network-security gateway-security-policies delete policy1 \
        --location=REGION
    

Replace `REGION` with the region of your policy.

### Delete the `swp-test-vm` Linux VM instance

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instances that you want to delete. Here, `swp-test-vm` is the name of the Linux VM instance.

  3. Click **Delete**.




###  Cloud Shell 
    
    
    gcloud compute instances delete swp-test-vm
    

## What's next

  * [Deploy Secure Web Proxy as next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop)

  * [Deploy Secure Web Proxy as a Private Service Connect service](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment)

  * [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview)

  * [Configure VPC Service Controls for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/vpc-sc-support)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
