---
url: https://docs.cloud.google.com/appengine/docs/standard/ingress-settings/
title: Ingress settings \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:42.159353+00:00
---

# Ingress settings  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/ingress-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Ingress settings Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

This section describes how to use ingress settings to restrict network access to your App Engine app. At a network level, by default, any resource on the internet is able to reach your App Engine app on its [appspot URL](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-routed) or at a [custom domain](https://docs.cloud.google.com/appengine/docs/standard/mapping-custom-domains) set up in App Engine. For example, the `appspot.com` URL can have the following format: `SERVICE_ID.PROJECT_ID.REGION_ID.r.appspot.com`.

You can change this default setting by specifying a different setting for ingress. All ingress paths, including the default `appspot.com` URL, are subject to your ingress setting. Ingress is set at the service level.

## Available ingress settings

The following settings are available:

Setting | Description  
---|---  
Internal |  Most restrictive. Allows requests from resources attached to the project's VPC networks, such as:   


  * VMs in the same project, including Compute Engine VMs.
  * [Serverless VPC access connectors](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc).
  * [Shared VPC](https://docs.cloud.google.com/appengine/docs/standard/connecting-shared-vpc) when the App Engine app is deployed in the Shared VPC host project. See Accessing internal services.

Requests from these sources stay within the Google network, even if they access your service at the `appspot.com` URL. Requests from other sources, including the internet, cannot reach your service at the `appspot.com` URL or custom domains. There is no support for multi-tenancy, that is, multiple trust domains within the same project.   
Internal and Cloud Load Balancing | Allows requests from the following resources:   


  * Resources allowed by the more restrictive Internal setting
  * External Application Load Balancer

Use the Internal and Cloud Load Balancing setting to accept requests from an external Application Load Balancer but not directly from the internet. Requests to the `appspot.com` URL bypass the external Application Load Balancer, so this setting prevents external requests from reaching the `appspot.com` URL.   
All |  Least restrictive. Allows all requests, including requests directly from the internet to the `appspot.com` URL.   
  
### Accessing internal services

The following considerations apply:

  * For requests from a Shared VPC, traffic is only considered internal if the App Engine app is deployed in the Shared VPC host project. If the App Engine app is deployed in a Shared VPC service project, only traffic from networks owned by the app's own project is internal. All other traffic, including traffic from other Shared VPCs, is external.

  * When accessing internal services, call them as you would normally do by using their public URLs, either the default `appspot.com` URL or a [custom domain](https://docs.cloud.google.com/run/docs/mapping-custom-domains) set up in App Engine.

  * For requests from Compute Engine VM instances or other resources running inside a [VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc) in the same project, no further setup is required.

  * Requests from resources within VPC networks in the same project are classified as internal even if the resource they originate from has a public IP address.

  * Requests from on-premises resources connected to the VPC network via Cloud VPN are considered `internal`.



  * For requests from other App Engine services or from Cloud Run or Cloud Run functions in the same project, connect the service or function to a VPC network and route all egress through the connector, as described in [Connecting to a Shared VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-shared-vpc). 



### View ingress settings

### Console

  1. Go to the App Engine Services page.

[Go to the Services page](https://console.cloud.google.com/appengine/services)

  2. Locate the **Ingress** column. For each service, the value in this column shows the ingress setting as one of **All** (default), **Internal + Load Balancing** , or **Internal**.




### gcloud

To view the ingress setting for a service using the gcloud CLI:
    
    
    gcloud app services describe SERVICE

Replace SERVICE with the name of your service.

For example, to view the ingress settings and other information for the default service run: 
    
    
    gcloud app services describe default

### Edit ingress settings

### Console

  1. Go to the App Engine Services page.

[Go to the Services page](https://console.cloud.google.com/appengine/services)

  2. Select the service you wish to edit.

  3. Click **Edit ingress setting**.

  4. Select the ingress setting that you want from the menu and click **Save**.




### gcloud

To update the ingress setting for a service using the gcloud CLI:
    
    
    gcloud app services update SERVICE --ingress=INGRESS

Replace:

  * SERVICE: The name of your service.
  * INGRESS: The ingress control you want to apply. One of `all`, `internal-only`, or `internal-and-cloud-load-balancing`.



For example:

  * To update the default service of an App Engine app to accept traffic only from Cloud Load Balancing and VPC networks that are in the same project:
        
        gcloud app services update default --ingress=internal-and-cloud-load-balancing

  * To update a service named "internal-requests" to accept traffic only from VPC networks that are in the same project:
        
        gcloud app services update internal-requests --ingress=internal-only




## Egress settings

**Note:** Egress settings are not available for the PHP runtimes.

If you use [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access), you can specify the egress setting for your App Engine service.

By default, only requests to internal IP addresses and internal DNS names are routed through a Serverless VPC Access connector. You can specify the egress setting for your service in your `app.yaml` file.

Egress settings are not compatible with the URL Fetch service. Using the `urlfetch` library ignores egress settings, and requests will not route through a Serverless VPC Access connector. 

To configure the egress behavior of your App Engine service: 

  1. Add the `egress_setting` attribute to the `vpc_access_connector` field of your service's `app.yaml` file:
         
         vpc_access_connector:
           name: projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME
           egress_setting: EGRESS_SETTING

Replace:

     * `PROJECT_ID` with your Google Cloud project ID
     * `REGION` with the region your connector is in
     * `CONNECTOR_NAME` with the name of your connector
     * `EGRESS_SETTING` with one of the following: 
       * `private-ranges-only` Default. Only requests to [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3) and [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7) IP address ranges or internal DNS names are routed to your VPC network. All other requests are routed directly to the internet.
       * `all-traffic` All outbound requests from your service are routed to your VPC network. Requests are then subject to the firewall, DNS, and routing rules of your VPC network. Note that routing all outbound requests to your VPC network increases the amount of egress handled by the Serverless VPC Access connector and can [incur charges](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing). 
  2. Deploy the service:
         
         gcloud app deploy
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
