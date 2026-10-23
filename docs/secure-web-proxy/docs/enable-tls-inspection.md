---
url: https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection/
title: Enable TLS inspection \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:54.605279+00:00
---

# Enable TLS inspection  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Enable TLS inspection Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable Transport Layer Security (TLS) inspection for your Secure Web Proxy instance. Secure Web Proxy offers a TLS inspection service that lets you intercept the TLS traffic, inspect the encrypted request, and enforce security policies. For more information about TLS inspection, see [TLS inspection overview](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview).

## Before you begin

Before you configure your Secure Web Proxy instance for TLS inspection, complete the tasks in the following sections.

### Enable Certificate Authority Service

Secure Web Proxy uses [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) to generate the certificates used for TLS inspection.

To enable CA Service, use the following command:
    
    
      gcloud services enable privateca.googleapis.com
      

### Create a CA pool

A [certificate authority (CA) pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool) is a collection of multiple CAs with a common certificate issuance policy and [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) policy. CA pools provide the ability to rotate [trust chains](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/format-certificates#intermediatecertificates) without any outage or downtime for their payloads.

You must create a CA pool before you can use [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) to create a CA. This section walks you through the permissions that you need to complete this task and then describes how to create a CA pool.

To generate certificates, TLS inspection uses a separate [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) for each project called `service-[PROJECT_NUMBER]@gcp-sa-networksecurity.iam.gserviceaccount.com`. Make sure that you have granted permissions to this service account to use your CA pool. If this access is revoked, then TLS inspection stops working.

To retrieve the `PROJECT_NUMBER` by using the `PROJECT_ID` of the CA pool project, use the following command:
    
    
    gcloud projects describe PROJECT_ID
        --format="value(projectNumber)"
    

**Important:** To check the current permissions granted to a service account, open [IAM](https://console.cloud.google.com/iam-admin/). In the **View by principals** tab, locate the service account in the table. Then, under the **Security insights** column, click the link specified for the service account. The current permissions of the service account are displayed in a pane.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions or IAM roles.

**Permissions**

  * `networksecurity.tlsInspectionPolicies.create`
  * `networksecurity.tlsInspectionPolicies.get`
  * `networksecurity.tlsInspectionPolicies.list`
  * `networksecurity.tlsInspectionPolicies.delete`
  * `networksecurity.tlsInspectionPolicies.update`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Certificate Manager Editor (`roles/certificatemanager.editor`)
  * Optional: Security Policy Admin (`roles/compute.orgSecurityPolicyAdmin`)



To create the pool, use the `gcloud privateca pools create` command and specify the subordinate pool ID, tier, project ID, and location.
    
    
    gcloud privateca pools create SUBORDINATE_POOL_ID \
        --tier=TIER \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `SUBORDINATE_POOL_ID`: name of the CA pool
  * `TIER`: tier of the CA pool, either `devops` or `enterprise`. We recommend that you create the CA pool in the `devops` tier because tracking individually-issued certificates is unnecessary.
  * `PROJECT_ID`: ID of the CA pool project
  * `REGION`: region in which the CA pool is to be created

**Important:** The certificates that are generated for TLS inspection have a short lifespan. After the certificates are issued, they can't be changed or revoked by using CA Service.

#### Configure a local intermediate CA signing

To enable the `LOCAL_INTERMEDIATE_CA_SIGNING` [certificate issuance mode](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview#certificate_issuance_modes), you must set the value of `isCa` to `true`.

**Note:** You can't configure `certificateIssuanceMode` in the Google Cloud console.

  1. Create the `ca-issuance-policy.yaml` file with the following configuration:
         
         issuancePolicy:
           baselineValues:
             caOptions:
               isCa: true
             keyUsage:
               baseKeyUsage:
                 certSign: true
                 crlSign: true
               extendedKeyUsage:
                 serverAuth: true
         

  2. When creating the CA pool, specify the issuance policy file.
         
         gcloud privateca pools create SUBORDINATE_POOL_ID \
             --tier=TIER \
             --project=PROJECT_ID \
             --location=REGION \
             --issuance-policy-file=ca-issuance-policy.yaml
         

Replace the following:

     * `SUBORDINATE_POOL_ID`: name of the CA pool
     * `TIER`: tier of the CA pool, either `devops` or `enterprise`. We recommend that you create the CA pool in the `devops` tier because tracking individually-issued certificates is unnecessary.
     * `PROJECT_ID`: ID of the CA pool project
     * `REGION`: region in which the CA pool is to be created



### Create a subordinate CA pool

If you have multiple certificate issuance scenarios, then you can [create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca) for each of those scenarios. You can create a subordinate CA in a [CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool), and the [root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities) signs all the CAs in that CA pool. These certificates are used to sign server certificates that are generated for TLS inspection.

To create a subordinate CA pool, use _one_ of the following methods.

#### Create a subordinate CA pool by using an existing root CA stored within Certificate Authority Service

To generate a subordinate CA, do the following:

  1. Create a CA pool
  2. [Create subordinate CAs within a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca#subordinate-internal)



#### Create a subordinate CA pool by using an existing root CA held externally

To generate a subordinate CA, do the following:

  1. Create a CA pool
  2. [Create subordinate CAs signed by an external root CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-sub-ca-from-external-ca#subordinate-external)



#### Create a root CA

If a root CA doesn't exist, then you can create one within CA Service.

To create a root CA, do the following:

  1. [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#create-root-ca)
  2. Create a subordinate CA pool by using an existing root CA stored within CA Service



### Create a service account

A [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) helps provide the necessary permissions for TLS inspection without compromising either the security of your user accounts or your Secure Web Proxy instance itself.

If you don't have a service account, you must create one and then grant the required permissions to that service account.

  1. Create a service account.
         
         gcloud beta services identity create \
             --service=networksecurity.googleapis.com \
             --project=PROJECT_ID
         

In response, the Google Cloud CLI creates a service account called `service-[PROJECT_NUMBER]@gcp-sa-networksecurity.iam.gserviceaccount.com`.

To retrieve the `PROJECT_NUMBER` by using the `PROJECT_ID` of the CA pool project, use the following command:
         
         gcloud projects describe PROJECT_ID
             --format="value(projectNumber)"
         

  2. For the service account that you created, grant permissions to generate certificates with your CA pool.
         
         gcloud privateca pools add-iam-policy-binding CA_POOL \
             --member='serviceAccount:SERVICE_ACCOUNT' \
             --role='roles/privateca.certificateManager' \
             --location='REGION'
         




## Configure Secure Web Proxy for TLS inspection

You can proceed with the tasks in this section only after you have completed the prerequisite tasks listed in the Before you begin section.

To configure TLS inspection, complete the tasks in the following sections.

### Create a TLS inspection policy

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `certificatemanager.trustconfigs.list`
  * `certificatemanager.trustconfigs.use`
  * `privateca.caPools.list`
  * `privateca.caPools.use`
  * `privateca.certificateAuthorities.list`
  * `networksecurity.operations.get`
  * `networksecurity.tlsInspectionPolicies.list`
  * `networksecurity.tlsInspectionPolicies.create`



**Roles**

  * Compute Security Admin role (`compute.securityAdmin`)
  * Compute Network Admin role (`compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **TLS inspection policies** page.

[Go to TLS inspection policies](https://console.cloud.google.com/net-security/tls/policies/list)

  2. In the project selector menu, select your project.

  3. Click **Create TLS inspection policy**.

  4. In the **Name** field, enter a name for the policy.

**Caution:** Don't include sensitive information such as personally identifiable information or security data in the TLS inspection policy name.
  5. Optional: In the **Description** field, enter a description for the policy.

  6. In the **Region** list, select the region where you want to create the policy.

  7. In the **CA pool** list, select the CA pool from which you want to create the certificates.

If you haven't configured a CA pool, then click **New Pool** and follow the instructions in the Create a CA pool section.

  8. Click **Create**.


**Note:** Don't configure the **Minimum TLS version** , **Trust configuration** , and **Cipher suite profile** fields. These fields aren't supported on Secure Web Proxy.

###  gcloud 

  1. Create the `TLS_INSPECTION_FILE.yaml` file. Replace `TLS_INSPECTION_FILE` with the required filename.

  2. Add the following code to the YAML file to configure the required TlsInspectionPolicy:
         
         name: projects/PROJECT_ID/locations/REGION/tlsInspectionPolicies/TLS_INSPECTION_NAME
         caPool: projects/PROJECT_ID/locations/REGION/caPools/CA_POOL
         certificateIssuanceMode: CERTIFICATE_ISSUANCE_MODE
         

Replace the following:

     * `PROJECT_ID`: ID of the project
     * `REGION`: region in which the policy is to be created
     * `TLS_INSPECTION_NAME`: name of the Secure Web Proxy TLS inspection policy
     * `CA_POOL`: name of the CA pool from which the certificates are created. The CA pool _must_ exist within the same region.
     * `CERTIFICATE_ISSUANCE_MODE`: optional mode for [certificate issuance](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview#certificate_issuance_modes). You can specify one of the following values: 
       * `CERTIFICATE_ISSUANCE_MODE_UNSPECIFIED`: use this to set `certificateIssuanceMode` to its default value of `DIRECT_LEAF_PROVISIONING` for Secure Web Proxy
       * `LOCAL_INTERMEDIATE_CA_SIGNING`: set this value to configure Secure Web Proxy to use intermediate CA signing certificate issuance mode
       * `DIRECT_LEAF_PROVISIONING`: set this value to configure Secure Web Proxy to use direct leaf CA provisioning for each domain



### Import the TLS inspection policy

Import the TLS inspection policy that you created in the previous step:
    
    
    gcloud network-security tls-inspection-policies import TLS_INSPECTION_NAME \
        --source=TLS_INSPECTION_FILE.yaml \
        --location=REGION
    

### Add the TLS inspection policy to the security policy

### Console

#### Create the web proxy policy

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. Click add_box**Create a policy**.

  3. Enter a name for the policy that you want to create, such as `myswppolicy`.

  4. Enter a description of the policy, such as `My new swp policy`.

  5. In the **Regions** list, select the region where you want to create the Secure Web Proxy policy.

  6. To configure TLS inspection, select **Configure TLS inspection**.

  7. In the **TLS inspection policy** list, select the TLS inspection policy that you created.

  8. If you want to create rules for your policy, click **Continue** , and then click **Add rule**. For details, see Create Secure Web Proxy rules.

  9. Click **Create**.




#### Create Secure Web Proxy rules

  1. In the Google Cloud console, go to the **SWP Policies** page.

[Go to SWP Policies](https://console.cloud.google.com/net-security/swp/policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains your policy.

  3. Click the name of your policy.

  4. Click add_box**Add rule**.

  5. Populate the rule fields:

     1. **Name**
     2. **Description**
     3. **Status**
     4. **Priority** : the numeric evaluation order of the rule. The rules are evaluated from highest to lowest priority where `0` is the highest priority.
     5. In the **Action** section, specify whether connections that match the rule are allowed (**Allow**) or denied (**Deny**).
     6. In the **Session Match** section, specify the criteria for matching the session. For more information about the syntax for `SessionMatcher`, see the [CEL matcher language reference](https://docs.cloud.google.com/secure-web-proxy/docs/cel-matcher-language-reference).
     7. To enable TLS inspection, select **Enable TLS inspection**.
     8. In the **Application Match** section, specify the criteria for matching the request. If you don't enable the rule for TLS inspection, then the request can only match HTTP traffic.
     9. Click **Create**.
  6. Click **Add rule** to add another rule.

  7. Click **Create** to create the policy.




#### Set up a web proxy

  1. In the Google Cloud console, go to the **Web Proxies** page.

[Go to Web Proxies](https://console.cloud.google.com/net-security/swp/web-proxies/list)

  2. Click add_box**Create a secure web proxy**.

  3. Enter a name for the web proxy that you want to create, such as `myswp`.

  4. Enter a description of the web proxy, such as `My new swp`.

  5. In the **Regions** list, select the region where you want to create the web proxy.

  6. In the **Network** list, select the network where you want to create the web proxy.

  7. In the **Subnetwork** list, select the subnetwork where you want to create the web proxy.

  8. Optional: Enter the Secure Web Proxy IP address. You can enter an IP address from the range of Secure Web Proxy IP addresses that reside in the subnetwork you created in the previous step. If you don't enter the IP address, then your Secure Web Proxy instance automatically chooses an IP address from the selected subnetwork.

  9. In the **Certificate** list, select the certificate that you want to use to create the web proxy.

  10. In the **Policy** list, select the policy that you created to associate the web proxy with.

  11. Click **Create**.




###  Cloud Shell 

  1. Create the file `policy.yaml`:
         
         description: basic Secure Web Proxy policy
           name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
           tlsInspectionPolicy: projects/PROJECT_ID/locations/REGION/tlsInspectionPolicies/TLS_INSPECTION_NAME
         

  2. Create the Secure Web Proxy policy:
         
         gcloud network-security gateway-security-policies import policy1 \
               --source=policy.yaml --location=REGION
         

  3. Create the file `rule.yaml`:
         
         name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1/rules/allow-example-com
           description: Allow example.com
           enabled: true
           priority: 1
           basicProfile: ALLOW
           sessionMatcher: host() == 'example.com'
           applicationMatcher: request.path.contains('index.html')
           tlsInspectionEnabled: true
         

**Note:** You must enable TLS inspection for each rule. To enable TLS inspection, set the `tlsInspectionEnabled` attribute to `true` for each rule that uses `applicationMatcher` to match the HTTPS traffic. The TLS inspection for the rule is limited to the traffic that matches the `sessionMatcher` attribute of the rule. For more information, see [TLS inspection rule evaluation](https://docs.cloud.google.com/secure-web-proxy/docs/tls-rule-evaluation).
  4. Create the security policy rule.
         
         gcloud network-security gateway-security-policies rules import allow-example-com \
               --source=rule.yaml \
               --location=REGION \
               --gateway-security-policy=policy1
         

  5. To attach a TLS inspection policy to an existing security policy, create the file `POLICY_FILE`.yaml. Replace `POLICY_FILE` with your filename.
         
         description: My Secure Web Proxy policy
           name: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/POLICY_NAME
           tlsInspectionPolicy: projects/PROJECT_ID/locations/REGION/tlsInspectionPolicies/TLS_INSPECTION_NAME
         




## What's next?

  * [Use a URL list to create policies](https://docs.cloud.google.com/secure-web-proxy/docs/use-url-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
