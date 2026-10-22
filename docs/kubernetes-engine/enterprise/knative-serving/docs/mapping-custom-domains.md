---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains/
title: Mapping custom domains \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:45.971231+00:00
---

# Mapping custom domains  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Mapping custom domains Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Configure custom domains to use for accessing your Knative serving services. You can map one or more custom domain to an individual service, or you can map a single domain to your cluster that all services use. Your custom domain mapping can be the base domain like `your-domain.com`, or a subdomain, such as `your-subdomain.your-domain.com`.

By default, the services that you deploy to your Knative serving clusters are set to the `nip.io` base domain. This allows you to immediately test your services at a URL like:

`http://{SERVICE_NAME}.{NAMESPACE}.kuberun.{EXTERNAL_IP}.nip.io`

[Learn more about test domains](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/default-domain#testdomain).

## Before you begin

  * You must have or purchase the domain that you want to map to your services. You can use any domain name registrar, but if you use [Cloud Domains](https://docs.cloud.google.com/domains/docs), the domain is automatically verified for Knative serving, so you won't have to go through the domain verification process.

If you want to register a domain with Cloud Domains, see Registering a domain with Cloud Domains within the Knative serving console.

  * You must have at least the [_Kubernetes Engine Developer_](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#roles) Identity and Access Management role or equivalent permissions.

  * To enable HTTPS with your custom domain mappings, you must either set up [managed TLS certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls) or [configure your own certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/bring-your-own-cert).

  * To map a custom domain to your cluster or services in a [private, internal network](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/setup#setting_up_a_private_internal_network), you must [disable managed TLS certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls#disable-for-cluster).




## Mapping a custom domain

You can use the Google Cloud console or the command-line tools to map your custom domain.

Generally, to configure a custom domain:

  1. Optional: Reserve the IP address of your load balancer.
  2. Map your services or the cluster to the custom domain in Knative serving.
  3. Update your DNS records in your domain registrar.



### Reserve the load balancer IP address

When Knative serving is installed, the Istio ingress controller creates a load balancer with an available IP address.

Depending on your GKE cluster, you might need to reserve the IP address of the load balancer for the Istio ingress controller:

Outside Google Cloud
    Refer to the documentation for the environment where you run your GKE cluster to determine how IP addresses are managed and if your load balancer's IP address is static. Also see the configuration pages for your [GKE cluster](https://docs.cloud.google.com/anthos/clusters/docs). For example, depending on how you configured load balancing for Google Distributed Cloud, you might have already reserved those IP addresses.
On Google Cloud
    

You must reserve the external IP address of the load balancer to [ensure it remains the same if your ingress service is ever deleted](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#static_ip_addresses_for_https_load_balancers). Depending on your cluster configuration, the IP address is either externally available or internal only, for example, [private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept).

Internal load balancers on Google Cloud
    See the following page for details about how to reserve the IP address of your internal load balancer: [Reserving a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip)
External load balancers on Google Cloud
    To reserve the IP address of your external load balancer:

  1. Obtain the IP address of the load balancer:

### Console

To get the load balancer's external IP address from the Google Cloud console: 
     1. Go to the GKE page in the Google Cloud console:   
[Go to GKE](https://console.cloud.google.com/kubernetes)
     2. Click **Services and ingress**. 
     3. Identify the service that is your cluster's Istio ingress. The service's **Type** will be **External load balancer** , and the **Name** will be `istio-ingressgateway`. 
     4. Once you've found your cluster's Istio ingress service, copy its **Endpoint**. This will be the IP address without the port number. For example, you might see `00.000.000.000:11` listed as an endpoint, but you only need to copy `00.000.000.000`. 

### kubectl

To obtain the external IP for the Load Balancer, run the following command:
    
    kubectl get svc istio-ingressgateway -n ASM-INGRESS-NAMESPACE

Replace ASM-INGRESS-NAMESPACE with the namespace where your Cloud Service Mesh ingress is located. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

The resulting output looks similar to the following:
    
    NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP  PORT(S)
    istio-ingressgateway   LoadBalancer   XX.XX.XXX.XX   pending      80:32380/TCP,443:32390/TCP,32400:32400/TCP

where the **EXTERNAL-IP** value is your external IP address of the Load Balancer.

  2. Reserve the IP address as a static IP:
         
         gcloud compute addresses create ADDRESS-NAME --addresses EXTERNAL-IP --region REGION

Replace:

     * ADDRESS-NAME with the name you want to give your static IP.
     * EXTERNAL-IP with the external IP address of the load balancer that you obtained in the previous step.
     * REGION with the [region](https://docs.cloud.google.com/compute/docs/regions-zones#identifying_a_region_or_zone) where your cluster is located.



After you obtain the IP address of your load balancer, you can use it to map your custom domain:

  * Mapping to services
  * Mapping to clusters



### Mapping services

Choose one of the following methods to map your custom domain to a Knative serving service. Each individual service can be mapped to multiple domains.

### Console

  1. Open the domain mappings page in the Google Cloud console:

[Go to Domain mappings](https://console.cloud.google.com/kubernetes/run/domains)

Note that if your display window is too small, the _Mapping Custom Domains button_ isn't displayed and you must click the 3-dot vertical ellipse icon at the right corner of the page.

  2. Click _Add Mapping_ , and select **Add service domain mapping** to map a domain to an individual service. You can map multiple domains to each service.

  3. From the dropdown list in the _Add Mapping_ form, select the service to which you want to mapping your custom domain:

  4. Enter the domain name. For example, `your-domain.com` or `subdomain.your-domain.com`. Domain requirements: 

     * Base path mapping is not supported. The term _base path_ refers to the URL path name that is after the domain name. For example, `users` is the base path of `your-domain.com/users`. Knative serving only allows you to map a domain to `/`, not to a specific base path. So any path routing has to be handled by using a router inside the service's container or by using [Firebase Hosting](https://firebase.google.com/docs/hosting). 
     * You cannot map your domain to a subdomain that matches the URL of your services. URLs to a service are defined as `http://{service}.{namespace}.{your-domain.com}`, therefore if you have a service at `test.default.your-domain.com`, you must not create a domain mapping to the same subdomain **`test.default.`**`your-domain.com`. 
  5. Click **Continue**.

  6. Update your DNS records at your domain registrar web site using the DNS records displayed in the last step. You can display the records at any time by clicking **DNS Records** in the "..." action menu for a domain mapping.

  7. Click **Done**.




### gcloud

  1. Map your service to the custom domain:
         
         gcloud run domain-mappings create --service SERVICE --domain DOMAIN

Replace:

     * SERVICE with your service name.
     * DOMAIN with your custom domain. For example, `your-domain.com` or `subdomain.your-domain.com`. Domain requirements: 
       * Base path mapping is not supported. The term _base path_ refers to the URL path name that is after the domain name. For example, `users` is the base path of `your-domain.com/users`. Knative serving only allows you to map a domain to `/`, not to a specific base path. So any path routing has to be handled by using a router inside the service's container or by using [Firebase Hosting](https://firebase.google.com/docs/hosting). 
       * You cannot map your domain to a subdomain that matches the URL of your services. URLs to a service are defined as `http://{service}.{namespace}.{your-domain.com}`, therefore if you have a service at `test.default.your-domain.com`, you must not create a domain mapping to the same subdomain **`test.default.`**`your-domain.com`. 



Now that your custom domain is mapped to Knative serving, you must add DNS records at your domain registrar.

### Mapping clusters

Choose one of the following methods to map your custom domain to your cluster:

### Console

  1. Open the domain mappings page in the Google Cloud console:

[Go to Domain mappings](https://console.cloud.google.com/kubernetes/run/domains)

Note that if your display window is too small, the _Mapping Custom Domains button_ isn't displayed and you must click the 3-dot vertical ellipse icon at the right corner of the page.

  2. Click _Add Mapping_ , and select **Add default domain** to map a domain to all services in your cluster. By default, new services that you deploy use the mapped domain.

  3. Click the checkbox to apply your new domain mapping to all the existing services in your cluster.

  4. From the dropdown list in the _Add Mapping_ form, select the cluster to which you want to mapping your custom domain:

  5. Enter the domain name. For example, `your-domain.com` or `subdomain.your-domain.com`. Domain requirements: 

     * Base path mapping is not supported. The term _base path_ refers to the URL path name that is after the domain name. For example, `users` is the base path of `your-domain.com/users`. Knative serving only allows you to map a domain to `/`, not to a specific base path. So any path routing has to be handled by using a router inside the service's container or by using [Firebase Hosting](https://firebase.google.com/docs/hosting). 
     * You cannot map your domain to a subdomain that matches the URL of your services. URLs to a service are defined as `http://{service}.{namespace}.{your-domain.com}`, therefore if you have a service at `test.default.your-domain.com`, you must not create a domain mapping to the same subdomain **`test.default.`**`your-domain.com`. 
  6. Click **Continue**.

  7. Update your DNS records at your domain registrar web site using the DNS records displayed in the last step. You can display the records at any time by clicking **DNS Records** in the "..." action menu for a domain mapping.

  8. Click **Done**.




### kubectl

  1. Run the following command to remove the existing base domain from the `config-domain` ConfigMap and replace it with your custom domain:
         
         kubectl patch configmap config-domain --namespace knative-serving --patch \
         '{"data": {"nip.io": null, "DOMAIN": ""}}'

Replace DOMAIN with your custom domain. For example, `your-domain.com` or `subdomain.your-domain.com`. Domain requirements: 

     * Base path mapping is not supported. The term _base path_ refers to the URL path name that is after the domain name. For example, `users` is the base path of `your-domain.com/users`. Knative serving only allows you to map a domain to `/`, not to a specific base path. So any path routing has to be handled by using a router inside the service's container or by using [Firebase Hosting](https://firebase.google.com/docs/hosting). 
     * You cannot map your domain to a subdomain that matches the URL of your services. URLs to a service are defined as `http://{service}.{namespace}.{your-domain.com}`, therefore if you have a service at `test.default.your-domain.com`, you must not create a domain mapping to the same subdomain **`test.default.`**`your-domain.com`. 



Now that your custom domain is mapped to Knative serving, you must add DNS records at your domain registrar.

## Add your DNS records at your domain registrar

After you've mapped your service to a custom domain in Knative serving, you need to update your DNS records at your domain registrar. As a convenience, Knative serving generates and displays the DNS records you need to enter. You must add these records that point to the Knative serving service at your domain registrar for the mapping to go into effect.

If you're using Cloud DNS as your DNS provider, see [Adding a record](https://docs.cloud.google.com/dns/docs/records#adding_a_record).

**Note:** Some third party CDN providers might inadvertently intercept validation requests, preventing them from reaching the Knative serving service and causing the domain mapping to fail or its certificate to fail to renew. For example, if you are using Cloudflare CDN, you should turn off the "_Always use https_ " option in the "_Edge Certificates_ " tab of the _SSL/TLS_ tab.

  1. Retrieve the DNS record information for your domain mappings using:

### Console

     1. Go to the Knative serving domain mappings page:

[Go to Domain mappings](https://console.cloud.google.com/kubernetes/run/domains)

     2. Click the 3-dot vertical ellipse icon to the right of your service, then click **DNS RECORDS** to display all the DNS records:

### gcloud
    
    gcloud run domain-mappings describe --domain DOMAIN

Replace DOMAIN with your custom domain. For example, `your-domain.com` or `subdomain.your-domain.com`.

You need all of the records returned under the heading `resourceRecords`.

  2. Log in to your account at your domain registrar and then open the DNS configuration page.

  3. Locate the host records section of your domain's configuration page and then add each of the resource records that you received when you mapped your domain to your Knative serving service.

  4. When you add each of the above DNS records to the account at the DNS provider:

     * Select the type returned in the DNS record in the previous step: `A`, or `AAAA`, or `CNAME`.
     * Use the name `www` to map to `www.your-domain.com`.
     * Use the name `@` to map `your-domain.com`.
     * Use the [wildcard](https://en.wikipedia.org/wiki/Wildcard_DNS_record) `*` to map to `*.your-domain.com`.
  5. Save your changes in the DNS configuration page of your domain's account. In most cases, it takes only a few minutes for these changes to take effect, but in some cases it can take up to several hours, depending on the registrar and the [Time-To-Live (TTL)](https://support.google.com/a/answer/48090) of any previous DNS records for your domain. You can use a [`dig`](https://en.wikipedia.org/wiki/Dig_\(command\)) tool, such as [this online `dig` version](https://toolbox.googleapps.com/apps/dig/#A/), to confirm the DNS records have been successfully updated.

  6. Test for success by browsing to your service at its new URL, for example `https://www.your-domain.com`. Note that it can take several minutes for the managed SSL/TLS certificate to be issued.




## Adding verified domain owners to other users or service accounts

When a user verifies a domain, that domain is only verified to that user's account. This means that only that user can add more domain mappings that use that domain. So, to enable other users to add mappings that use that domain, you must add them as verified owners.

**Note:** A verified domain owner is able to override existing domain mappings from other projects after confirmation.

If you need to add verified owners of your domain to other users or service accounts, you can add permission through the _Search Console_ page:

  1. Navigate to this address in your web browser:

[`https://search.google.com/search-console/welcome`](https://search.google.com/search-console/welcome)

  2. Under **Properties** , click the domain for which you want to add a user or service account.

  3. Scroll down to the **Verified owners** list, click **Add an owner** , and then enter a Google Account email address or service account ID.

To view a list of your service accounts, open the Service Accounts page in the Google Cloud console:

[Go to Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)




## Registering a domain with Cloud Domains within the Knative serving console

**Preview — Registering a domain with Cloud Domains within the Knative serving console**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To register a domain with Cloud Domains from within the Knative serving console:

  1. Go to the Knative serving domain mappings page:

[Go to Domain mappings](https://console.cloud.google.com/kubernetes/run/domains?enableapi=true)

  2. Click **Register domain**.

  3. Complete the registration process following the instructions for [Registering a domain](https://docs.cloud.google.com/domains/docs/register-domain).

  4. Complete the steps earlier in this page to Map your domain to Knative serving and then add DNS records at your domain registrar.




## Troubleshooting

View the common issues in [Troubleshooting custom domains and managed TLS](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting#managed-tls).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
