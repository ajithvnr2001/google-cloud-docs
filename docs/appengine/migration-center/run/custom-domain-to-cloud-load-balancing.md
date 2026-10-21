---
url: https://docs.cloud.google.com/appengine/migration-center/run/custom-domain-to-cloud-load-balancing/
title: Migrate an App Engine custom domain to Cloud Load Balancing \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:40.448997+00:00
---

# Migrate an App Engine custom domain to Cloud Load Balancing  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/run/custom-domain-to-cloud-load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate an App Engine custom domain to Cloud Load Balancing Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

This guide covers how to set up a new public endpoint for your App Engine app using Cloud Load Balancing.

With Cloud Load Balancing, you configure your custom domain endpoint as a frontend service, and configure your App Engine app as a backend service using a [serverless network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/backend-service#serverless_network_endpoint_groups). Traffic to the Cloud Load Balancing frontend service's endpoint is routed the same way as before, including all routing rules that you define in your app's [`dispatch.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) file.

The following diagram describes the changes to your app:

![Take an App Engine custom domain and shift incoming requests to a Cloud Load Balancing frontend service that distributes requests to the backend App Engine service.](https://docs.cloud.google.com/static/appengine/images/gae-to-gclb-and-gae.svg)

By migrating to Cloud Load Balancing, you gain significantly more flexibility in how traffic is handled when reaching your domain, such as serving static content from Cloud Storage, or adding services running on other compute platforms like Cloud Run and Google Kubernetes Engine.

You also gain access to key Google Cloud capabilities that are not available on App Engine, including:

  * [Google Cloud Armor](https://docs.cloud.google.com/armor), for improved security with advanced DDoS protection, IP-based and geo-based access controls, web application firewall rules, and more
  * [Cloud CDN](https://docs.cloud.google.com/cdn), for cached content delivery
  * [SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts), for managing which SSL features and TLS versions your app will accept



This guide covers the setup instructions for shifting incoming requests from your App Engine service with a custom domain to a Cloud Load Balancing frontend service:

  1. Ensure that you have the required permissions
  2. Create a Google-managed certificate
  3. Configure Cloud Load Balancing
  4. Test the load balancer
  5. Connect your domain to your load balancer
  6. Delete the App Engine custom domain mapping
  7. Set up ingress control to only allow access through Cloud Load Balancing



## Before you begin

Have an App Engine app with a custom domain [configured in App Engine settings](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains).

### Configure permissions

To follow this guide, you need to create a Google-managed certificate, serverless NEG, and an external HTTP(S) load balancer in a project. You should be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or have the following [IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required Role  
---|---  
Create a Google-managed SSL certificate using Certificate Manager | [Certificate Manager Owner](https://docs.cloud.google.com/certificate-manager/docs/permissions) or [Certificate Manager Editor](https://docs.cloud.google.com/certificate-manager/docs/permissions), and [Compute Load Balancer Admin](https://docs.cloud.google.com/compute/docs/access/iam)  
Update DNS records for the custom domain | [Cloud DNS Administrator](https://docs.cloud.google.com/dns/docs/access-control) if using Cloud DNS as your DNS solution.  
  
If using another DNS provider, you will need permissions to add and update the DNS records for the custom domain.   
Create load balancer and networking components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Create and modify NEGs | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
Create and modify SSL certificates | [Compute Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
Delete custom domains in App Engine settings | [App Engine Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appAdmin) or a role that contains the `appengine.applications.update` permission.   
  
## Create a Google-managed SSL certificate

A Google-managed SSL certificate (also known as TLS certificate in documentation) lets Google Cloud obtain, manage, and renew certificates automatically. To migrate to Cloud Load Balancing frontend without causing downtime for your existing App Engine service, you must use Certificate Manager to create DNS authorization and your Google-managed certificate.

Note that the Cloud Load Balancing documentation has similar instructions for [creating a Google-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs), but the instructions there use load balancer authorization, which requires downtime for your App Engine service that could last up to several hours. For more information, see [Domain authorization for Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization).

To avoid downtime for your app, follow the steps on this page.

### Create DNS authorization

  1. Create the DNS authorization in Certificate Manager by running the following commands:
         
         gcloud certificate-manager dns-authorizations create AUTHORIZATION_NAME \
             --domain="DOMAIN_NAME"
         gcloud certificate-manager dns-authorizations describe AUTHORIZATION_NAME
         

Replace the following:

     * `AUTHORIZATION_NAME` is a unique name that describes this DNS authorization.
     * `DOMAIN_NAME` is the App Engine custom domain name for which you are creating this DNS authorization.
  2. Note the CNAME returned by the `gcloud` command. You must use it to update your DNS record in the following steps.




### Add the CNAME record to your DNS configuration

Depending on whether you are using [Cloud DNS](https://docs.cloud.google.com/dns) or another third-party DNS solution, follow the instructions that is appropriate for your use case:

###  Cloud DNS 

When you create a DNS authorization, the `gcloud` command returns the corresponding CNAME record. You must add this CNAME record to your DNS configuration in the DNS zone of the target domain as follows:

  1. Initiate the DNS record transaction:
         
         gcloud dns record-sets transaction start --zone="DNS_ZONE_NAME"
         

Replace `DNS_ZONE_NAME` with the name of the public DNS zone. If you are using Google Cloud to manage your domain and receive traffic to that domain, you will have already created a public DNS zone. To view your public DNS zone, see [List and describe managed zones](https://docs.cloud.google.com/dns/docs/zones#list_and_describe_managed_zones).

  2. Add the CNAME record to the target DNS zone:
         
         gcloud dns record-sets transaction add CNAME_RECORD \
           --name="_acme-challenge.DOMAIN_NAME." \
           --ttl="30" \
           --type="CNAME" \
           --zone="DNS_ZONE_NAME"
         

Replace the following:

     * `CNAME_RECORD` is the full value of the CNAME record returned by the `gcloud` command that created the corresponding DNS authorization.
     * `DOMAIN_NAME` is the App Engine custom domain name. You must include the trailing period after the target domain name.
     * `DNS_ZONE_NAME` is the name of the target DNS zone from earlier.
  3. Execute the DNS record transaction to save your changes:
         
         gcloud dns record-sets transaction execute --zone="DNS_ZONE_NAME"
         

Replace `DNS_ZONE_NAME` with the name of the target DNS zone from earlier.




###  Other DNS solution 

Add a CNAME record to the DNS configuration for your domain, using the (host)name (`_acme-challenge.DOMAIN_NAME`) and data fields from the previous section. Consult the documentation for your third-party DNS solution.

### Create a Google-managed certificate referencing the DNS authorization

To create a Google-managed certificate that references the DNS authorization you created in the previous steps, run the following commands:

  1. Create a [Google-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/core-components#certificates):
         
         gcloud certificate-manager certificates create CERTIFICATE_NAME \
         --domains=DOMAIN_NAME --dns-authorizations=AUTHORIZATION_NAME
         

Replace the following:

     * `CERTIFICATE_NAME` is a unique name that describes the certificate.
     * `DOMAIN_NAME` is the App Engine custom domain name.
     * `AUTHORIZATION_NAME` is the name of the DNS authorization that was created earlier.
  2. Verify the certificate is active.

Use the following command to verify that the certificate itself is active before deploying it to your load balancer. Note that it can take up to several hours for the certificate state to change to `ACTIVE`.
         
         gcloud certificate-manager certificates describe CERTIFICATE_NAME
         

Replace `CERTIFICATE_NAME` with the name of the Google-managed certificate that was created earlier.

The `gcloud` tool returns output similar to the following:
         
         certificatePem: myPEM
         createTime: '2021-10-20T12:19:53.370778666Z'
         expireTime: '2022-05-07T05:03:49Z'
         managed:
           authorizationAttemptInfo:
           - domain: example.com
             state: AUTHORIZED
           dnsAuthorizations:
           - projects/my-project/locations/global/dnsAuthorizations/myAuth
           domains:
           - example.com
           state: ACTIVE
         name: projects/myProject/locations/global/certificates/myCert
         scope: myScope
         sanDnsnames:
         - example.com
         updateTime: '2021-10-20T12:19:55.083385630Z'
         

If the `gcloud` tool returns a different output, see [Troubleshooting Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/troubleshooting).




### Create a certificate map

  1. Create a [certificate map](https://docs.cloud.google.com/certificate-manager/docs/core-components#cert-maps):
         
         gcloud certificate-manager maps create CERTIFICATE_MAP_NAME
         

Replace `CERTIFICATE_MAP_NAME` with the a unique name that describes the certificate map.

  2. Create a [certificate map entry](https://docs.cloud.google.com/certificate-manager/docs/core-components#maps-entries) and associate it with your certificate and certificate map from earlier: 
         
         gcloud certificate-manager maps entries create CERTIFICATE_MAP_ENTRY_NAME \
             --map=CERTIFICATE_MAP_NAME \
             --certificates=CERTIFICATE_NAME \
             --set-primary
         

Replace the following:

     * `CERTIFICATE_MAP_ENTRY_NAME` is a unique name that describes this certificate map entry.
     * `CERTIFICATE_MAP_NAME` is the name of the certificate map to which this certificate map entry attaches.
     * `CERTIFICATE_NAME` is the name of the certificate you want to associate with this certificate map entry.

You can append the [`--set-primary` flag](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/create#--set-primary) to ensure that the certificate is used as the default certificate if a domain name is not specified.

  3. Verify certificate map is active.

Use the following command to verify that the certificate map entry is active before attaching its corresponding certificate map to the target proxy:
         
         gcloud certificate-manager maps entries describe CERTIFICATE_MAP_ENTRY_NAME \
             --map=CERTIFICATE_MAP_NAME
         

Replace the following:

     * `CERTIFICATE_MAP_ENTRY_NAME` is the certificate map entry name from earlier.
     * `CERTIFICATE_MAP_NAME` is the certificate map name to which this certificate map entry attaches.

The `gcloud` tool returns output similar to the following:
    
    createTime: '2021-09-06T10:01:56.229472109Z'
    name: projects/my-project/locations/global/certificateMaps/myCertMap/certificateMapEntries/myCertMapEntry
    state: ACTIVE
    updateTime: '2021-09-06T10:01:58.277031787Z'
    




For more information on using Certificate Manager, see [How Certificate Manager works](https://docs.cloud.google.com/certificate-manager/docs/certificate-selection-logic).

**Note:** While certificate creation can take up to a few hours, you can continue with the setup without needing to wait for the certificate to be `ACTIVE`. However, both the Certificate and the Certificate Map should be `ACTIVE` before you connect your domain to the load balancer.

## Configure Cloud Load Balancing

After you have a Google-managed certificate, you can replace your App Engine custom domain with a Cloud Load Balancing frontend service.

The following diagram shows an HTTPS load balancer with a single backend service and serverless NEG.

![Distributing traffic to an App Engine app](https://docs.cloud.google.com/static/appengine/images/gclb-with-gae-frontend.svg)

Forwarding rules route incoming requests from external IP addresses and direct requests to the target HTTPS proxy. The HTTPS load balancers use URL maps to direct requests to the backend service, which contains a serverless NEG for the App Engine service.

**Important:** This guide will configure Cloud Load Balancing to direct traffic to App Engine using default routing. This is the same routing behavior as [custom domains configured in App Engine](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains), or traffic hitting the app URL (_`https:// PROJECT_ID.REGION_ID.r.appspot.com`_). Using this method ensures that any routing configured with the [`dispatch.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) file will continue to function in the same way.

### Reserve an external IP address

Before configuring Cloud Load Balancing, you need to set up a global static external IP address for users to reach your load balancer.

### Console

  1. Go to the **External IP addresses** page in the Google Cloud console.

[Go to External IP addresses](https://console.cloud.google.com/addresses/list)

  2. Click **Reserve static address** to reserve an IPv4 address.

  3. Assign a **Name** for the static address, for example, `appengine-external-ip`.

  4. Set the Network tier to **Premium**.

  5. Set the **IP version** to **IPv4**.

  6. Set the **Type** to **Global**.

  7. Click **Reserve**.




### gcloud

  1. Create external IP address reservation:
         
         gcloud compute addresses create EXTERNAL_IP \
             --network-tier=PREMIUM \
             --ip-version=IPV4 \
             --global
         

`EXTERNAL_IP` is the name of the addresses to create.

  2. Note the IPv4 address that was reserved:
         
         gcloud compute addresses describe EXTERNAL_IP \
             --format="get(address)" \
             --global
         




### Configure backend service for App Engine

A [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) is used to specify a group of backend endpoints for a load balancer. To specify a backend that points to an App Engine service, configure the serverless NEG, then configure the backend service, routing rules, and frontend service in Cloud Load Balancing.

  1. Create a serverless NEG for your App Engine app:
         
         gcloud compute network-endpoint-groups create APP_ENGINE_NEG \
         --network-endpoint-type=serverless \
         --app-engine-app \
         --region=APP_ENGINE_REGION
         

Replace the following:

     * `APP_ENGINE_NEG` is the name of the network endpoint group.
     * `APP_ENGINE_REGION` is the [region](https://docs.cloud.google.com/appengine/docs/standard/locations) that was set in App Engine.

You can append the [`--app-engine-app` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create#--%5Bno-%5Dapp-engine-app) above to use default routing, instead of directing to a specific App Engine service. Using _default routing_ means that requests will be sent to the default service (_`https:// PROJECT_ID.REGION_ID.r.appspot.com`_), and otherwise follows all routing rules that you define in the [`dispatch.yaml` file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml). This is the same behavior as custom domains configured using App Engine.

  2. Create the backend service:
         
         gcloud compute backend-services create APP_ENGINE_BACKEND \
           --global \
           --load-balancing-scheme=EXTERNAL_MANAGED
         

Replace `APP_ENGINE_BACKEND` with the name of the backend service to create.

  3. Add the serverless NEG to the App Engine backend service:
         
         gcloud compute backend-services add-backend APP_ENGINE_BACKEND \
         --global --network-endpoint-group=APP_ENGINE_NEG \
         --network-endpoint-group-region=APP_ENGINE_REGION
         

Replace the following:

     * `APP_ENGINE_BACKEND` is the name of the backend service from earlier.
     * `APP_ENGINE_NEG` is the name of the network endpoint group.
     * `APP_ENGINE_REGION` is the [region](https://docs.cloud.google.com/appengine/docs/standard/locations) that was set in App Engine.
  4. Create a URL map to route incoming requests to the backend service:
         
         gcloud compute url-maps create URL_MAP_NAME \
               --default-service APP_ENGINE_BACKEND
         

Replace the following:

     * `URL_MAP_NAME` is a unique name for the URL map resource that defines the mapping of URLs to backend services.
     * `APP_ENGINE_BACKEND` is the name of the backend service from earlier.
  5. Create a target HTTPS proxy to route requests to your URL map:
         
         gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
               --certificate-map=CERTIFICATE_MAP_NAME \
               --url-map=URL_MAP_NAME
         

Replace the following:

     * `TARGET_HTTPS_PROXY_NAME` is a unique name that you choose to describe your HTTPS proxy.
     * `CERTIFICATE_MAP_NAME` is the name of the certificate map referencing your certificate map entry and its associated certificate.
     * `URL_MAP_NAME` is the name of the URL map from earlier.
  6. Create a forwarding rule to route incoming requests to the proxy:
         
         gcloud compute forwarding-rules create HTTPS_FORWARDING_RULE_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --network-tier=PREMIUM \
               --address=EXTERNAL_IP \
               --target-https-proxy=TARGET_HTTPS_PROXY_NAME \
               --global \
               --ports=443
         

Replace the following:

     * `HTTPS_FORWARDING_RULE_NAME` is a unique name that describes the forwarding rule for directing network traffic to the HTTPS proxy.
     * `TARGET_HTTPS_PROXY_NAME` is a name of the HTTPS proxy from earlier.
     * `EXTERNAL_IP` is the name of the IPv4 address that was created previously.



## Test the load balancer

Now that you have configured your load balancer, you can start sending traffic to the load balancer's IP address for testing before migrating the domain.

  1. Go to the **Load balancing** page in the Google Cloud console.  
[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)
  2. Click on the load balancer you just created.
  3. Note the **IP Address** of the load balancer.
  4. For an HTTPS load balancer, you can test your load balancer using a web browser by going to `https://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address, for example, `30.90.80.100`.

     * If that does not work and you are using a Google-managed certificate, confirm that your certificate is `ACTIVE`, and that the certificate map is `ACTIVE`.
     * If you use a self-signed certificate for testing, your browser displays a warning. You must explicitly instruct your browser to accept a self-signed certificate. Click through the warning to see the actual page.

For more configuration options, see [Set up a global external HTTP(S) load balancer with Serverless platforms](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless#additional_configuration_options).




## Connect your domain to your load balancer

After the load balancer is created, note the IP address that is associated with the load balancer—for example, `30.90.80.100`. To point your domain to your load balancer, create an `A` record by using your domain registration service. If you added multiple domains to your SSL certificate, you must add an `A` record for each one, all pointing to the load balancer's IP address. For example, to create `A` records for `www.example.com` and `example.com`, use the following:
    
    
    NAME                  TYPE     DATA
    www                   A        30.90.80.100
    @                     A        30.90.80.100
    

If you use Cloud DNS as your DNS provider, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).

## Delete the App Engine custom domain mapping

In the Google Cloud console:

  1. Go to the **Custom Domains** tab of the App Engine **Settings** page.

[Go to Custom Domains](https://console.cloud.google.com/appengine/settings/domains)

  2. Select the custom domain name and click **Delete**.




Alternatively, you can use [gcloud commands](https://docs.cloud.google.com/sdk/gcloud/reference/app/domain-mappings) or the [Admin API](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings) to delete the custom domain.

## Set up ingress control to only allow access through Cloud Load Balancing

After testing your load balancer, we recommend updating your App Engine app to accept traffic only from Cloud Load Balancing. To learn how to configure `internal-and-cloud-load-balancing` ingress controls, see [Ingress settings](https://docs.cloud.google.com/appengine/docs/standard/ingress-settings).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
