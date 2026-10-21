---
url: https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies/
title: Use SSL policies \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:35.879427+00:00
---

# Use SSL policies  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Use SSL policies Stay organized with collections  Save and categorize content based on your preferences. 

Secure Sockets Layer (SSL) policies specify a minimum TLS version and a set of TLS capabilities that Cloud Load Balancing uses when negotiating SSL with clients. In this document, the term _SSL_ refers to both the SSL and TLS protocols.

SSL policies are supported with the following load balancers:

  * Global SSL policies 
    * Global external Application Load Balancer
    * Classic Application Load Balancer
    * Global external proxy Network Load Balancer (with a target SSL proxy)
    * Cross-region internal Application Load Balancer


  * Regional SSL policies 
    * Regional external Application Load Balancer
    * Regional internal Application Load Balancer



For more information about how SSL policies work, see [SSL policies for SSL and TLS protocols](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts).

You can create and manage SSL policies by using the Google Cloud console or the Google Cloud CLI when you create an HTTPS or SSL load balancer or at any time after you create the load balancer.

## Create SSL policies

You can create SSL policies with predefined profiles or with a custom profile.

### Create an SSL policy with a predefined profile

###  Console 

### Global SSL policy

To create a global SSL policy with a predefined profile, do the following:

  1. In the Google Cloud console, go to the **SSL policies** page.

[Go to SSL policies](https://console.cloud.google.com/net-services/ssl-policies/list)

  2. Click **Create policy**.

  3. For **Global SSL policy** , click the **Create** button next to it. The **Create policy** page appears.

  4. Enter a name.

  5. For **Minimum TLS Version** , select a value.

  6. For **Profile** , select **Compatible** , **Modern** , **Restricted** , or **FIPS_202205**.

     * SSL policies that use the `FIPS_202205` profile must use a minimum TLS version of 1.2.
     * If you set the minimum TLS version of an SSL policy to 1.3, the policy must use the `RESTRICTED` profile.

The **Enabled features** and **Disabled features** for the profile are displayed.

  7. For **Post-quantum key exchange** , select **Default** , **Enabled** , or **Deferred**. To learn more about the different modes, see [Post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).

  8. If there is a load balancer to which you want to attach the policy, click **Apply to targets** and select a forwarding rule as the target of the SSL policy. If necessary, add more targets.

  9. Click **Create**.




### Regional SSL policy

To create a regional SSL policy with a predefined profile, do the following:

  1. In the Google Cloud console, go to the **SSL policies** page.

[Go to SSL policies](https://console.cloud.google.com/net-services/ssl-policies/list)

  2. Click **Create policy**.

  3. For **Regional SSL policy** , click the **Create** button next to it. The **Create policy** page appears.

  4. Enter a name.

  5. For **Region** , select a region.

  6. For **Minimum TLS Version** , select a value.

  7. For **Profile** , select **Compatible** , **Modern** , **Restricted** , or **FIPS_202205**.

     * SSL policies that use the `FIPS_202205` profile must use a minimum TLS version of 1.2.
     * If you set the minimum TLS version of an SSL policy to 1.3, the policy must use the `RESTRICTED` profile.

The **Enabled features** and **Disabled features** for the profile are displayed.

  8. For **Post-quantum key exchange** , select **Default** , **Enabled** , or **Deferred**. To learn more about the different modes, see [Post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).

  9. If there is a load balancer to which you want to attach the policy, click **Apply to targets** and select a forwarding rule as the target of the SSL policy. If necessary, add more targets.

  10. Click **Create**.




###  gcloud 

### Global SSL policy

The following is the general syntax for creating a global SSL policy with a predefined profile.

  * SSL policies that use the `FIPS_202205` profile must use a minimum TLS version of 1.2.
  * If you set the minimum TLS version of an SSL policy to 1.3, the policy must use the `RESTRICTED` profile.


    
    
    gcloud compute ssl-policies create SSL_POLICY_NAME \
        --profile {COMPATIBLE | MODERN | RESTRICTED | FIPS_202205} \
        --min-tls-version {1.0 | 1.1 | 1.2 | 1.3} \
        --post-quantum-key-exchange MODE
    

Replace the following:

  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients.
  * `MODE`: you can set the post-quantum key exchange mode to `ENABLED`, `DEFAULT`, or `DEFERRED`. To learn more about the different modes, see [post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).



### Regional SSL policy

The following is the general syntax for creating a regional SSL policy with a predefined profile.

  * SSL policies that use the `FIPS_202205` profile must use a minimum TLS version of 1.2.
  * If you set the minimum TLS version of an SSL policy to 1.3, the policy must use the `RESTRICTED` profile.


    
    
    gcloud compute ssl-policies create SSL_POLICY_NAME \
        --profile {COMPATIBLE | MODERN | RESTRICTED | FIPS_202205} \
        --min-tls-version {1.0 | 1.1 | 1.2 | 1.3} \
        --region REGION \
        --post-quantum-key-exchange MODE
    

Replace the following:

  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients.
  * `REGION`: the region for the SSL policy.
  * `MODE`: you can set the post-quantum key exchange mode to `ENABLED`, `DEFAULT`, or `DEFERRED`. To learn more about the different modes, see [post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).



### Create an SSL policy with a custom profile

###  Console 

### Global SSL policy

To create a global SSL policy with a custom profile, do the following:

  1. In the Google Cloud console, go to the **SSL policies** page.

[Go to SSL policies](https://console.cloud.google.com/net-services/ssl-policies/list)

  2. Click **Create policy**.

  3. For **Global SSL policy** , click the **Create** button next to it. The **Create policy** page appears.

  4. Enter a name.

  5. For **Minimum TLS Version** , select a value.

  6. For **Profile** , select **Custom**. All features are shown as **Disabled features**.

  7. For **Post-quantum key exchange** , select **Default** , **Enabled** , or **Deferred**. To learn more about the different modes, see [Post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).

  8. In the list of **Features** , select each cipher suite that you want to enable. The cipher suites you enable are listed as **Enabled features**. To learn more about the different cipher suites that you can select when you use the `CUSTOM` profile, see [Cipher suites for TLS 1.2 and earlier](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#cipher-suites-tls-1.2-and-earlier).

  9. If there is a load balancer to which you want to attach the policy, click **Apply to targets** and select a forwarding rule as the target of the SSL policy. If necessary, add more targets.

  10. Click **Create**.




### Regional SSL policy

To create a regional SSL policy with a custom profile, do the following:

  1. In the Google Cloud console, go to the **SSL policies** page.

[Go to SSL policies](https://console.cloud.google.com/net-services/ssl-policies/list)

  2. Click **Create policy**.

  3. For **Regional SSL policy** , click the **Create** button next to it. The **Create policy** page appears.

  4. Enter a name.

  5. For **Region** , select a region.

  6. For **Minimum TLS Version** , select a value.

  7. For **Profile** , select **Custom**. All features are shown as **Disabled features**.

  8. For **Post-quantum key exchange** , select **Default** , **Enabled** , or **Deferred**. To learn more about the different modes, see [Post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).

  9. In the list of **Features** , select each cipher suite that you want to enable. The cipher suites you enable are listed as **Enabled features**. To learn more about the different cipher suites that you can select when you use the `CUSTOM` profile, see [Cipher suites for TLS 1.2 and earlier](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#cipher-suites-tls-1.2-and-earlier).

  10. If there is a load balancer to which you want to attach the policy, click **Apply to targets** and select a forwarding rule as the target of the SSL policy. If necessary, add more targets.

  11. Click **Create**.




###  gcloud 

When you create an SSL policy with the `CUSTOM` profile, only the features that you specify in the `create` command are supported. Other features aren't supported.

### Global SSL policy

The following is the general syntax for creating a global SSL policy with a custom profile:
    
    
    gcloud compute ssl-policies create SSL_POLICY_NAME \
        --profile CUSTOM \
        --min-tls-version {1.0 | 1.1 | 1.2} \
        --custom-features SSL_FEATURE_1[,SSL_FEATURE_2,SSL_FEATURE_3] \
        --post-quantum-key-exchange MODE
    

Replace the following:

  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients
  * `SSL_FEATURE_1 | 2 | 3`: the different cipher suites that you can select when you use the `CUSTOM` profile. To learn more, see [Cipher suites for TLS 1.2 and earlier](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#cipher-suites-tls-1.2-and-earlier).
  * `MODE`: you can set the post-quantum key exchange mode to `ENABLED`, `DEFAULT`, or `DEFERRED`. To learn more about the different modes, see [post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).



### Regional SSL policy

The following is the general syntax for creating a regional SSL policy with a custom profile:
    
    
    gcloud compute ssl-policies create SSL_POLICY_NAME \
        --profile CUSTOM \
        --min-tls-version {1.0 | 1.1 | 1.2} \
        --custom-features SSL_FEATURE_1[,SSL_FEATURE_2,SSL_FEATURE_3] \
        --region REGION \
        --post-quantum-key-exchange MODE
    

Replace the following:

  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients
  * `SSL_FEATURE_1 | 2 | 3`: the different cipher suites that you can select when you use the `CUSTOM` profile. To learn more, see [Cipher suites for TLS 1.2 and earlier](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#cipher-suites-tls-1.2-and-earlier).
  * `REGION`: the region in which to apply the SSL policy
  * `MODE`: you can set the post-quantum key exchange mode to `ENABLED`, `DEFAULT`, or `DEFERRED`. To learn more about the different modes, see [post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).



## List SSL policies

###  Console 

In the Google Cloud console, go to the **SSL policies** page.

[Go to SSL policies](https://console.cloud.google.com/net-services/ssl-policies/list)

You can view a list of all the available SSL policies. The **Scope** field indicates whether the SSL policy is global or regional.

###  gcloud 

List both global and regional SSL policies:
    
    
    gcloud compute ssl-policies list
    

List only global SSL policies:
    
    
    gcloud compute ssl-policies list --global
    

List only regional SSL policies:
    
    
    gcloud compute ssl-policies list --regions REGION
    

Replace `REGION` with the region in which to apply the SSL policy.

## List features available in an SSL policy

###  Console 

  1. In the Google Cloud console, go to the **SSL policies** page.

[Go to SSL policies](https://console.cloud.google.com/net-services/ssl-policies/list)

  2. Click the name of the policy whose features you want to see. The enabled and disabled cipher suites are listed.




###  gcloud 

List the features available in global SSL policies:
    
    
    gcloud compute ssl-policies list-available-features
    

List the features available in regional SSL policies:
    
    
    gcloud compute ssl-policies list-available-features \
        --region REGION
    

Replace `REGION` with the region of the SSL policy whose features you want to list.

## Modify SSL policies

###  Console 

To modify a global or a regional SSL policy, do the following:

  1. In the Google Cloud console, go to the **SSL policies** page.

[Go to SSL policies](https://console.cloud.google.com/net-services/ssl-policies/list)

  2. Click the name of the policy that you want to modify.

  3. Click **Edit**.

  4. Make any changes you want.

  5. Click **Save**.




###  gcloud 

To modify an existing SSL policy, pass any or all of the flags corresponding to the fields you want to update. Unspecified fields aren't updated.

If you update the features, previously enabled features are deleted and replaced with the new features you specify.

### Global SSL policies

  * SSL policies that use the `FIPS_202205` profile must use a minimum TLS version of 1.2.
  * If you set the minimum TLS version of an SSL policy to 1.3, the policy must use the `RESTRICTED` profile.


    
    
    gcloud compute ssl-policies update SSL_POLICY_NAME \
        --profile {COMPATIBLE | MODERN | RESTRICTED | CUSTOM | FIPS_202205} \
        --min-tls-version {1.0 | 1.1 | 1.2 | 1.3} \
        --custom-features FEATURES \
        --post-quantum-key-exchange MODE
    

Replace the following:

  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients
  * `FEATURES`: the different cipher suites that you can select when you use the `CUSTOM` profile. To learn more, see [Cipher suites for TLS 1.2 and earlier](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#cipher-suites-tls-1.2-and-earlier).
  * `MODE`: you can set the post-quantum key exchange mode to `ENABLED`, `DEFAULT`, or `DEFERRED`. To learn more about the different modes, see [post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).



### Regional SSL policies

  * SSL policies that use the `FIPS_202205` profile must use a minimum TLS version of 1.2.
  * If you set the minimum TLS version of an SSL policy to 1.3, the policy must use the `RESTRICTED` profile.


    
    
    gcloud compute ssl-policies update SSL_POLICY_NAME \
        --profile {COMPATIBLE | MODERN | RESTRICTED | CUSTOM | FIPS_202205} \
        --min-tls-version {1.0 | 1.1 | 1.2 | 1.3} \
        --custom-features FEATURES \
        --region REGION \
        --post-quantum-key-exchange MODE
    

Replace the following:

  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients
  * `FEATURES`: the different cipher suites that you can select when you use the `CUSTOM` profile. To learn more, see [Cipher suites for TLS 1.2 and earlier](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#cipher-suites-tls-1.2-and-earlier).
  * `REGION`: the region of the SSL policy whose features you want to update
  * `MODE`: you can set the post-quantum key exchange mode to `ENABLED`, `DEFAULT`, or `DEFERRED`. To learn more about the different modes, see [post-quantum key exchange modes](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#post-quantum-key-exchange-modes).



## Create a target proxy with an SSL policy

###  Console 

You can create a target proxy by using the Google Cloud console when you're creating or updating the load balancer as shown in the following documents:

  * [Set up an external proxy Network Load Balancer with a target SSL proxy](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl)
  * [Set up a global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute)
  * [Set up a classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple)
  * [Set up a cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)


  * [Set up a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)
  * [Set up a regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal)



###  gcloud 

To create a target SSL proxy with a global SSL policy:
    
    
    gcloud compute target-ssl-proxies create TARGET_SSL_PROXY_NAME \
        --backend-service BACKEND_SERVICE_NAME \
        --ssl-certificate SSL_CERTIFICATE_NAME \
        --ssl-policy SSL_POLICY_NAME
    

Replace the following:

  * `TARGET_SSL_PROXY_NAME`: the name of the target proxy
  * `BACKEND_SERVICE_NAME`: the name of the backend service
  * `SSL_CERTIFICATE_NAME`: the name of the TLS certificate
  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients



To create a global target HTTPS proxy with a global SSL policy:
    
    
    gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
        --ssl-certificate SSL_CERTIFICATE_NAME \
        --url-map URL_MAP_NAME \
        --ssl-policy SSL_POLICY_NAME
    

Replace the following:

  * `TARGET_HTTPS_PROXY_NAME`: the name of the target proxy
  * `SSL_CERTIFICATE_NAME`: the name of the TLS certificate
  * `URL_MAP_NAME`: the name of the URL map
  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients



To create a regional target HTTPS proxy with a regional SSL policy:
    
    
    gcloud compute target-https-proxies create REGIONAL_TARGET_HTTPS_PROXY_NAME \
        --ssl-certificates SSL_CERTIFICATE_NAME \
        --url-map URL_MAP_NAME \
        --url-map-region MAP_REGION \
        --ssl-policy SSL_POLICY_NAME \
        --region REGION
    

Replace the following:

  * `REGIONAL_TARGET_HTTPS_PROXY_NAME`: the name of the target proxy
  * `SSL_CERTIFICATE_NAME`: the name of the TLS certificate
  * `URL_MAP_NAME`: the name of the URL map
  * `MAP_REGION`: the name of the Google Cloud region where the URL map is located
  * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients
  * `REGION`: the region of the SSL policy that you want to create the target HTTPS proxy with



## Attach an existing SSL policy to an existing target proxy

###  Console 

Target proxies can't be modified in the Google Cloud console. Use the gcloud CLI or the API instead.

###  gcloud 

Use these commands to attach an existing SSL policy to an SSL proxy or HTTPS proxy.

  * To find all projects in your organization that have target SSL proxies:
        
        gcloud asset search-all-resources \
            --scope=organizations/ORGANIZATION_ID \
            --asset-types=compute.googleapis.com/TargetSslProxy
        

Replace `ORGANIZATION_ID` with the ID of the organization in which to find target SSL proxies.



  * To find all projects in your organization that have target HTTPS proxies:
        
        gcloud asset search-all-resources \
            --scope=organizations/ORGANIZATION_ID \
            --asset-types=compute.googleapis.com/TargetHttpsProxy
        

Replace `ORGANIZATION_ID` with the ID of the organization in which to find target HTTPS proxies.



  * To list all global target SSL proxies in a project, use the `targetSslProxies.aggregatedList` method. Then, use the `filter` query parameter to search for target SSL proxies that don't reference an SSL policy.
        
        curl \
            'https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/targetSslProxies?filter=sslPolicy%3D%22%22&key=YOUR_API_KEY' \
            --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
            --header 'Accept: application/json' \
            --compressed
        

Replace the following:

    * `PROJECT_ID`: the name of the project ID
    * `YOUR_API_KEY`: your API key
    * `YOUR_ACCESS_TOKEN`: your access token


  * To list all global and regional target HTTPS proxies in a project, use the `targetHttpsProxies.aggregatedList` method with the `includeAllScopes` query parameter set to `true`. Then, use the `filter` query parameter to search for target HTTPS proxies that don't reference an SSL policy.
        
        curl \
            'https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/targetHttpsProxies?filter=sslPolicy%3D%22%22&includeAllScopes=true&key=YOUR_API_KEY' \
            --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
            --header 'Accept: application/json' \
            --compressed
        

Replace the following:

    * `PROJECT_ID`: the name of the project ID
    * `YOUR_API_KEY`: your API key
    * `YOUR_ACCESS_TOKEN`: your access token


  * To attach an existing global SSL policy to a target SSL proxy:
        
        gcloud compute target-ssl-proxies update TARGET_SSL_PROXY_NAME \
            --ssl-policy SSL_POLICY_NAME
        

Replace the following:

    * `TARGET_SSL_PROXY_NAME`: the name of the target proxy
    * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients
  * To attach an existing global SSL policy to a global target HTTPS proxy:
        
        gcloud compute target-https-proxies update TARGET_HTTPS_PROXY_NAME \
            --ssl-policy SSL_POLICY_NAME
        

Replace the following:

    * `TARGET_HTTPS_PROXY_NAME`: the name of the target proxy
    * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients


  * To attach an existing regional SSL policy to a regional target HTTPS proxy:
        
        gcloud compute target-https-proxies update REGIONAL_TARGET_HTTPS_PROXY_NAME \
            --ssl-policy SSL_POLICY_NAME \
            --region REGION
        

Replace the following:

    * `REGIONAL_TARGET_HTTPS_PROXY_NAME`: the name of the target proxy
    * `SSL_POLICY_NAME`: the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients
    * `REGION`: the region of the SSL policy that you want to attach to the regional target HTTPS proxy



If you don't provide the `--ssl-policy` flag or the `--clear-ssl-policy` flag in a target proxy update (for example, when updating an SSL certificate), the SSL policy is unchanged. The `--clear-ssl-policy` flag is described in Delete an SSL policy from a target proxy.

###  API 

To set a global SSL policy for a global target proxy, use the [`targetHttpsProxies.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies/patch).

To set a regional SSL policy for a regional target proxy, use the [`regionTargetHttpsProxies.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies/patch).

## Delete an SSL policy from a target proxy

###  Console 

Target proxies can't be modified in the Google Cloud console. Use the gcloud CLI or the API instead.

###  gcloud 

Use these commands to remove an SSL policy from an SSL proxy or HTTPS proxy. If you don't attach a different SSL policy to the target proxy, the load balancer uses the default SSL policy. Using the `--clear-ssl-policy` flag is equivalent to replacing an SSL policy with the default SSL policy.

To remove a global SSL policy from a target SSL proxy:
    
    
    gcloud compute target-ssl-proxies update TARGET_SSL_PROXY_NAME \
        --clear-ssl-policy
    

Replace `TARGET_SSL_PROXY_NAME` with the name of the target proxy.

To remove a global SSL policy from a global target HTTPS proxy:
    
    
    gcloud compute target-https-proxies update TARGET_HTTPS_PROXY_NAME \
        --clear-ssl-policy
    

Replace `TARGET_HTTPS_PROXY_NAME` with the name of the target proxy.

To remove a regional SSL policy from a regional target HTTPS proxy:
    
    
    gcloud compute target-https-proxies update REGIONAL_TARGET_HTTPS_PROXY_NAME \
        --clear-ssl-policy \
        --region REGION
    

Replace the following:

  * `REGIONAL_TARGET_HTTPS_PROXY_NAME`: the name of the target proxy
  * `REGION`: the region of the SSL policy that you want to attach to the regional target HTTPS proxy



When you provide the `--clear-ssl-policy` flag in the update command, the SSL policy is removed from the proxy.

If you don't provide the `--clear-ssl-policy` flag or the`--ssl-policy` flag in the target proxy update (for example, when updating an SSL certificate), the SSL policy is unchanged. The `--ssl-policy` flag is described in Attach an existing SSL policy to an existing target proxy.

## Configure cross-project SSL policy referencing

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When you configure cross-project SSL policy referencing, you create an SSL policy in an administrative project (the central policy project) and then reference it when you create or update a target HTTPS proxy or target SSL proxy in a different project (a service project).

Cross-project referencing is supported for global and regional SSL policies.

To reference an SSL policy across projects, you must use the full resource URI of the policy.

### Roles and permissions

The following table lists the Identity and Access Management roles and permissions required to configure cross-project SSL policy referencing.

Scope | Required role | Required permissions  
---|---|---  
**Central policy project** (contains the central SSL policy) | 

  * To create and manage policies: `roles/compute.securityAdmin`, `roles/compute.networkAdmin`, or `roles/compute.loadBalancerAdmin`
  * To attach a policy: `roles/compute.securityAdmin`, `roles/compute.networkAdmin`, or a custom role with the `compute.sslPolicies.use` permission

| `compute.sslPolicies.use` (can be granted on the specific SSL policy resource)  
**Service project** (contains the load balancer's target proxy) | `roles/compute.networkAdmin` or `roles/compute.loadBalancerAdmin` | 

  * `compute.targetHttpsProxies.create` or `compute.targetHttpsProxies.update`
  * `compute.targetSslProxies.create` or `compute.targetSslProxies.update`

  
  
### Create a target proxy that references a cross-project SSL policy

To create a new target proxy that references an SSL policy in a different project, reference the central policy's full resource URI.

###  gcloud 

Depending on your load balancer type, use one of the following commands:

  * **To create a global target HTTPS proxy** :
        
        gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
            --url-map=URL_MAP_NAME \
            --ssl-certificates=SSL_CERTIFICATE_NAME \
            --ssl-policy=projects/POLICY_PROJECT_ID/global/sslPolicies/CENTRAL_SSL_POLICY_NAME \
            --project=SERVICE_PROJECT_ID
        

  * **To create a global target SSL proxy** :
        
        gcloud compute target-ssl-proxies create TARGET_SSL_PROXY_NAME \
            --backend-service=BACKEND_SERVICE_NAME \
            --ssl-certificates=SSL_CERTIFICATE_NAME \
            --ssl-policy=projects/POLICY_PROJECT_ID/global/sslPolicies/CENTRAL_SSL_POLICY_NAME \
            --project=SERVICE_PROJECT_ID
        



  * **To create a regional target HTTPS proxy** :
        
        gcloud compute target-https-proxies create REGIONAL_TARGET_HTTPS_PROXY_NAME \
            --url-map=URL_MAP_NAME \
            --url-map-region=REGION \
            --ssl-certificates=SSL_CERTIFICATE_NAME \
            --ssl-policy=projects/POLICY_PROJECT_ID/regions/REGION/sslPolicies/CENTRAL_SSL_POLICY_NAME \
            --region=REGION \
            --project=SERVICE_PROJECT_ID
        




Replace the following:

  * `TARGET_HTTPS_PROXY_NAME`, `TARGET_SSL_PROXY_NAME`, and `REGIONAL_TARGET_HTTPS_PROXY_NAME`: the name of the target proxy.
  * `URL_MAP_NAME`: the name of the URL map.
  * `SSL_CERTIFICATE_NAME`: the name of the TLS certificate.
  * `BACKEND_SERVICE_NAME`: the name of the backend service.
  * `POLICY_PROJECT_ID`: the ID of the project where the SSL policy resides.
  * `CENTRAL_SSL_POLICY_NAME`: the name of the SSL policy.
  * `SERVICE_PROJECT_ID`: the ID of the project where you are deploying the load balancer.
  * `REGION`: the region where the target proxy and SSL policy reside.



###  Terraform 

To configure cross-project SSL policy referencing within the same Terraform configuration, use the [google_compute_ssl_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_ssl_policy) resource in the central policy project and pass its resource ID to the [google_compute_target_https_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_https_proxy) resource in the service project.
    
    
    # SSL Policy in the central policy project
    resource "google_compute_ssl_policy" "central_policy" {
      name             = "CENTRAL_SSL_POLICY_NAME"
      project          = "POLICY_PROJECT_ID"
      profile          = "MODERN"
      min_tls_version  = "TLS_1_2"
    }
    
    # Target HTTPS proxy in the service project
    resource "google_compute_target_https_proxy" "default" {
      name             = "TARGET_HTTPS_PROXY_NAME"
      project          = "SERVICE_PROJECT_ID"
      url_map          = google_compute_url_map.default.id
      ssl_certificates = [google_compute_managed_ssl_certificate.default.id]
      ssl_policy       = google_compute_ssl_policy.central_policy.id
    }
    

### Attach a cross-project SSL policy to a target proxy

To attach an existing central SSL policy to a target proxy in another project, use one of the following methods.

###  gcloud 

To reference the central policy, run the update command for the target proxy, providing the full resource URI of the policy.

Depending on your load balancer type, use one of the following commands:

  * **For global HTTPS load balancers** :
        
        gcloud compute target-https-proxies update TARGET_PROXY_NAME \
            --ssl-policy=projects/POLICY_PROJECT_ID/global/sslPolicies/CENTRAL_SSL_POLICY_NAME \
            --project=SERVICE_PROJECT_ID
        

  * **For global SSL proxy load balancers** :
        
        gcloud compute target-ssl-proxies update TARGET_PROXY_NAME \
            --ssl-policy=projects/POLICY_PROJECT_ID/global/sslPolicies/CENTRAL_SSL_POLICY_NAME \
            --project=SERVICE_PROJECT_ID
        



  * **For regional HTTPS load balancers** :
        
        gcloud compute target-https-proxies update REGIONAL_TARGET_HTTPS_PROXY_NAME \
            --ssl-policy=projects/POLICY_PROJECT_ID/regions/REGION/sslPolicies/CENTRAL_SSL_POLICY_NAME \
            --region=REGION \
            --project=SERVICE_PROJECT_ID
        




Replace the following:

  * `TARGET_PROXY_NAME` and `REGIONAL_TARGET_HTTPS_PROXY_NAME`: the name of the target SSL or HTTPS proxy.
  * `POLICY_PROJECT_ID`: the ID of the project where the SSL policy resides.
  * `CENTRAL_SSL_POLICY_NAME`: the name of the SSL policy.
  * `SERVICE_PROJECT_ID`: the ID of the project where the load balancer resides.
  * `REGION`: the region where the target proxy and SSL policy reside.



###  Terraform 

  * **For global load balancers** :

If the central global SSL policy is managed in a separate Terraform configuration or by a different team, set the `ssl_policy` field in your target HTTPS proxy to the policy's full resource URI. For more information, see [google_compute_target_https_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_https_proxy).
        
        resource "google_compute_target_https_proxy" "default" {
          name             = "TARGET_HTTPS_PROXY_NAME"
          project          = "SERVICE_PROJECT_ID"
          url_map          = google_compute_url_map.default.id
          ssl_certificates = [google_compute_managed_ssl_certificate.default.id]
          ssl_policy       = "projects/POLICY_PROJECT_ID/global/sslPolicies/CENTRAL_SSL_POLICY_NAME"
        }
        



  * **For regional load balancers** :

To reference an existing central regional SSL policy managed by a different team or in a separate Terraform configuration, set the `ssl_policy` field in your target proxy configuration to the resource ID of the SSL policy created in the central policy project by providing the full resource URI string. For more information, see [google_compute_target_https_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_https_proxy).
        
        resource "google_compute_target_https_proxy" "default" {
          name             = "TARGET_HTTPS_PROXY_NAME"
          project          = "SERVICE_PROJECT_ID"
          url_map          = google_compute_url_map.default.id
          ssl_certificates = [google_compute_managed_ssl_certificate.default.id]
          ssl_policy       = "projects/POLICY_PROJECT_ID/regions/REGION/sslPolicies/CENTRAL_SSL_POLICY_NAME"
        }
        




### Troubleshooting

Use this section to resolve issues you might encounter when configuring cross-project SSL policy referencing.

  * **Error: Required`compute.sslPolicies.use` permission**.

This error occurs when the user or service account performing the update doesn't have the `compute.sslPolicies.use` permission on the central policy project containing the central SSL policy. To resolve this issue, ensure the correct role (such as `roles/compute.securityAdmin` or `roles/compute.networkAdmin`) has been granted on the central policy project. For more information, see Roles and permissions.

  * **Error: Policy not found**.

This error occurs if there's a mistake in the resource URI for the SSL policy. Check the project ID and policy name in the URI to ensure there are no typos.

  * **Can't delete the central SSL policy**.

Google Cloud automatically prevents the deletion of any SSL policy that's referenced by a target proxy, even if the referencing target proxy resides in a different project. You must first detach the policy from all target proxies before you can delete it.




## Manage SSL policies

If you [use custom constraints to restrict TLS capabilities](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints#restrict-tls-capabilities-custom-constraint), manually check for TLS compliance in pre-existing SSL policies that are attached to target SSL proxies and target HTTPS proxies.

Use the following sample steps to find and update SSL policies that don't meet your security goals.

  * To find all projects in your organization that have SSL policy resources:
        
        gcloud asset search-all-resources \
            --scope=organizations/ORGANIZATION_ID \
            --asset-types=compute.googleapis.com/SslPolicy
        

Replace `ORGANIZATION_ID` with the ID of the organization in which to find all projects that have SSL policy resources.

  * To list all global and regional SSL policies in a project, use the `sslPolicies.aggregatedList` method with the `includeAllScopes` query parameter set to `true`. Then, use the `filter` query parameter to search for SSL policies that don't align with your security goals.

For example, to find SSL policies with TLS version lower than `1.2`, use the filter `minTlsVersion="TLS_1_0"` _or_ `minTlsVersion="TLS_1_1"`:
        
        curl \
        
          'https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/sslPolicies?filter=minTlsVersion%3D%22TLS_1_0%22%20OR%20minTlsVersion%3D%22TLS_1_1%22&includeAllScopes=true&key=YOUR_API_KEY' \
          --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
          --header 'Accept: application/json' \
          --compressed
        

Replace the following:

    * `PROJECT_ID`: the name of the project ID
    * `YOUR_API_KEY`: your API key
    * `YOUR_ACCESS_TOKEN`: your access token

To get your API key, see [Manage API keys](https://docs.cloud.google.com/docs/authentication/api-keys). To get your access token, use the `projects.serviceAccounts.generateAccessToken` method.

Then update the SSL policies that don't meet your minimum TLS requirement.

To update a global SSL policy, you can use the following command:
    
    gcloud compute ssl-policies update SSL_POLICY_NAME \
        --min-tls-version=TLS_1_2 \
        --global
    

Replace `SSL_POLICY_NAME` with the name that you assigned to the SSL policy that defines the TLS capabilities that your load balancer uses when negotiating connections with clients.

To update a regional SSL policy, you can use the following command:
    
    gcloud compute ssl-policies update SSL_POLICY_NAME \
        --min-tls-version=TLS_1_2 \
        --region REGION
    

Replace the following:

    * `SSL_POLICY_NAME`: the name of the SSL policy
    * `REGION`: the region for the SSL policy


  * To list all the target SSL proxies in a project that aren't associated with an SSL policy, run the following command:
        
        curl \
        
          'https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/targetSslProxies?filter=sslPolicy%3D%22%22&key=YOUR_API_KEY' \
            --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
            --header 'Accept: application/json' \
            --compressed
        

Replace the following:

    * `PROJECT_ID`: the name of the project ID
    * `YOUR_API_KEY`: your API key
    * `YOUR_ACCESS_TOKEN`: your access token

To attach an SSL policy to these target proxies, see Attach an existing SSL policy to an existing target proxy.

  * You can also use either [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/query-assets-with-sql) or the Google APIs Explorer to find and update resources that don't meet your security requirements.

For example, to look up a list of target SSL proxies that aren't associated with an SSL policy, you can use the following steps in Cloud Asset Inventory:

    1. In the Google Cloud console, go to the **Asset inventory** page.

[Go to Asset inventory](https://console.cloud.google.com/iam-admin/asset-inventory/)

    2. Click **Asset query**.

    3. In the **Edit query** field, enter the following query and click **Run**.
           
           select * from `compute_googleapis_com_TargetSslProxy` where resource.data.sslPolicy IS NULL
           

    4. To attach an SSL policy to these target proxies, see Attach an existing SSL policy to an existing target proxy.

    5. Run the query in Cloud Asset Inventory until you see an empty response.




## Limits

See [Target proxies](https://docs.cloud.google.com/load-balancing/docs/quotas#target_proxies).

## API reference

For descriptions of the properties and methods available to you when working with SSL policies through the REST API, see the following:

Product | API documentation  
---|---  
  
  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Global external proxy Network Load Balancer
  * Classic proxy Network Load Balancer

| [sslPolicies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslPolicies)  
  
  * Regional external Application Load Balancer
  * Regional internal Application Load Balancer

| [regionSslPolicies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionSslPolicies)  
  
## gcloud CLI reference

For the Google Cloud CLI reference, see the following:

  * [gcloud compute ssl-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-policies)

    * Global: `--global`
    * Regional: `--region=REGION`



## What's next

  * For conceptual information about SSL policies, see [SSL policies for SSL and TLS protocols](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts).


  * For information about external proxy Network Load Balancers, see [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp).


  * For information about external Application Load Balancers, see [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
