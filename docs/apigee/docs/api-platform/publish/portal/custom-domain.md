---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-domain/
title: Customizing your domain \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:30.264914+00:00
---

# Customizing your domain  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Customizing your domain Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

When you create a developer portal, by default you are provided with an Apigee sample domain name for accessing your live portal in the following format:

`https://_orgname-portalname_.apigee.io`

Where `_orgname_` is the organization name and `_portalname_` is defined using the portal name converted to all lowercase and with spaces and dashes removed.

Before launching a developer portal, it is recommended that you provide your own custom domain name. For example, a popular alternative is:

`https://developers.example.com`

**Note:** Domain names can be customized for paid accounts only.

For considerations for using a custom domain with a SAML identity provider, see [ Using a custom domain with the SAML identity provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#custom-domain-saml).

## Steps to customize your domain

To customize your domain name perform the following steps:

  1. Register your domain name.
  2. Create a TLS certificate for your custom domain. You will need the cert when creating the load balancer.
  3. Determine the default hostname for your portal.
  4. Create an Internet network endpoint group (NEG) to define the backend endpoint to your integrated portal for the load balancer.
  5. Create a load balancer that points to the Internet NEG and reserves the IP for your incoming client requests.
  6. Configure the custom domain on your portal.
  7. Update your DNS to create a new record for the custom domain host.



## Step 1: Register your domain name

If you need to register a new domain, there are many popular domain registration sites available, such as [ Google Domains](https://domains.google/). Which domain registration site you choose is up to you.

When deciding on your domain name, consider that user-friendly, human-readable URLs are a key component in improving search engine optimization, as described in [Implement search engine optimization (SEO)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-best-practices#seo).

**Notes:**

  * Don't use the string "apigee" in your custom domain name.
  * Consider redirecting to other similar domain name alternatives.



## Step 2: Create a TLS certificate for your custom domain

Create a TLS certificate for your custom domain using your preferred tool, such as [Let's Encrypt](https://letsencrypt.org/). For more information, see:

  * [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates)
  * [Using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)



## Step 3: Determine the default hostname for your portal

To determine the default hostname for your portal:

  1. Display the list of portals.

In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Copy the contents in the **Location** field for the portal for which you want to create a custom domain. For example, `apigee-gcp-prod1-helloworld.apigee.io`.

You will need this value in the next step.




## Step 4: Create an Internet NEG

In this step you create an Internet network endpoint group (NEG) to define the backend endpoint to your integrated portal for the load balancer. For more information, see [Internet network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts).

  1. In the Google Cloud console, go to the **Dashboard** page and select or create a Google Cloud project. 

[Go to the Dashboard page](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select **Compute Engine > Network endpoint groups** in the navigator.

  3. Click **Create network endpoint group**.

  4. Configure the following fields:

Field | Value  
---|---  
**Name** | Enter a name for the Internet NEG.   
**Network endpoint group type** | Select **Network endpoint group (Internet)**.   
**New network endpoint** | 
     * **Add through** : Select **Fully qualified domain name and port**.
     * **Fully qualifed domain name** : Enter the default domain name that you copied in Step 3: Determine the default hostname for your portal.  
  5. You can leave the remaining fields set to their defaults.

  6. Click **Create**.




The Internet NEG is created.

## Step 5: Create a load balancer

Create a load balancer that points to the Internet NEG and reserves the IP for your incoming client requests.

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  5. For **Global or single region deployment** , select **Best for global workloads** and click **Next**.
  6. For **Load balancer generation** , select **Global external Application Load Balancer** and click **Next**.
  7. Click **Configure**.



#### Configure the load balancer

  1. Click each category and configure the load balancer as described in the following table.

Category | Steps  
---|---  
Frontend configuration  |  Reserve the IP address for your incoming client requests and upload the TLS certificate created in Step 2: Create a TLS certificate:
     1. In the **Create global external Application Load Balancer** section, position your cursor over **Frontend configuration** and click the arrow.
     2. Enter a name for the frontend in the **Name** field.
     3. Select **HTTPS** from the **Protocol** drop-down menu.
     4. In the **IP address** drop-down menu, select **Create IP address**  
The Reserve a new static IP address dialog displays.
     5. Enter a name for the static IP address in the **Name** field.
     6. Optionally enter a description.
     7. Click **Reserve**.
     8. Store the IP address that has been reserved for use when setting up the DNS record.
     9. Select **Create a new certificate** in the **Certificate** drop-down.  
The Create a new certificate window slides open.
     10. Enter a name for the new certificate in the **Name** field.
     11. Select **Upload my certificate** under **Create mode**.
     12. Upload your TLS certificate details, including the public key, certificate chain, and private key.
     13. Click **Create**.
     14. Click **Done** to create the new frontend IP and port.  
Backend configuration  |  Configure the backend configuration to direct incoming traffic to the Internet NEG created in Step 4: Create an Internet network endpoint group (NEG):
     1. In the **Create global external Application Load Balancer** section, position your cursor over **Backend configuration** and click the arrow.
     2. In the **Backend services & backend buckets** section, select **Backend services > Create a backend service** from the drop-down.  
The Create backend service window slides open.
     3. Enter a name in the **Name** field.
     4. Select **Internet network endpoint group** in the **Backend type** drop-down.
     5. Select **HTTPS** as the protocol.
     6. In the **New backend** section, select the Internet NEG that you created in Step 4: Create an Internet network endpoint group (NEG) in the **Internet network endpoint group** drop-down menu, and click **Done**.
     7. Clear the checkbox for **Enable Cloud CDN**.
     8. You can leave all other values set to their defaults.
     9. Click **Create**.
**Note:** Cloud CDN is not supported for use with the Apigee Portal.  
Host and path rules  |  Configure the host and path rules to determine how your traffic will be directed:
     1. In the **Create global external Application Load Balancer** section, position your cursor over **Host and path rules** and click the arrow.
     2. Click **Advanced host and path rule (URL redirect, URL rewrite)** under **Mode**.
     3. In the **New host and path rule** section: 
        1. Select **Route traffic to a single backend** in the **Action** drop-down.
        2. Expand **Add-on action (URL rewrite)**.
        3. Enter the default domain name that you copied in Step 3: Determine the default hostname for your portal in the **Host rewrite** field.
        4. Select the backend service that you configured in the **Backend** drop-down.
        5. Click **Done**.  
  2. Click **Create** on the **Create global external Application Load Balancer** page.




## Step 6: Configure the custom domain on your portal

To configure the custom domain on your portal:

  1. Display the list of portals.

In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Select your portal in the list.

  3. Select **Settings**.

  4. Click the **Domains** tab.

  5. Enter your custom domain name in the **Domain** field.

  6. Click **Enable**.




Test that when you access the custom domain in a browser you are directed to your integrated portal.

See also Editing a custom domain and Disabling a custom domain.

## Step 7: Update your DNS

In your DNS system, create a new record for the custom domain host.

To create a Cloud DNS zone, follow the steps described in [Managing Zones](https://cloud.google.com/dns/zones). Ensure that you configure the following fields:

Field  | Description  
---|---  
Zone type  | Select **Public**.   
Zone name  | Enter a meaningful name for the zone. For example: `mycompany-zone`  
DNS name  | Enter the suffix for the zone using a domain name that you own. For example: `mycompany.com`  
  
After you create a zone, on the Zone details page, click **Add record set** and follow the steps described in [Managing Records](https://cloud.google.com/dns/records). Ensure that you configure the following fields:

Field  | Description   
---|---  
DNS Name  | Specify the prefix for your DNS name. The suffix that you defined for the Cloud DNS zone is also displayed, but is not editable. For example: `**developers**.mycompany.com`  
Resource Record Type  | Select **A** (the default).   
TTL  | Set to desired value or leave set to **5** (default).   
TTL Unit  | Set to desired value or leave set to **minutes** (default).   
IPv4 Address  | Enter the external IP address that you reserved when creating the load balancer.   
  
## Editing a custom domain on your portal

To edit a custom domain on your portal:

  1. Display the list of portals.

In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Select your portal in the list.

  3. Select **Settings**.

  4. Click the **Domains** tab.

  5. Edit the custom domain information.

  6. Click **Save**.




## Disabling a custom domain on your portal

To disable a custom domain name on your portal:

  1. Display the list of portals.

In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Select your portal in the list.

  3. Select **Settings**.

  4. Click the **Domains** tab.

  5. Click **Disable**.

  6. Click **Disable** at the prompt to confirm the operation.




The custom domain is disabled and the fields are cleared.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
