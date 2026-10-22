---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-access/
title: Step 4: Customize access routing \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:52.366939+00:00
---

# Step 4: Customize access routing  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 4: Customize access routing Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-1-setup.png)

## What you're doing in this step

In this step, you can choose to expose your new Apigee instance to external requests or keep it private (and only allow requests from within the firewall).

**Tip:** There are fewer steps required to deploy and test a proxy if you choose **external**. If you are following these steps for testing purposes, choose that path. 

How you access the API proxy depends on whether you allow external requests or restrict access to internal requests only.

Access Type | Description of the configuration and deployment process  
---|---  
No internet access |  Allow only internal access to your API proxy. You can download the `Hello World` proxy from GitHub and then deploy it to your Apigee instance. You must then create a new VM inside the network and connect to it. From the new VM, you can send a request to the API proxy.  
Internet access |  Allow external access to your API proxy. **Note:** Apigee recommends using this approach.Apigee deploys a `Hello World` proxy to your Apigee instance. You can then send a request to the API proxy from your administration machine or any network-enabled machine, whether it is within or outside the firewall.  
  
Each of these approaches is presented on a tab in the instructions below.

## Perform the step

  1. Select **External Access** or **Internal Access** :

### External Access

This section describes how to configure routing from the Google Cloud console when you want to allow **external access** to your API proxy.

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

**To configure routing for external access in the Google Cloud console** : 

     1. Click create**Edit** to open the **Configure access** panel. 
     2. Select **Enable internet access**. 
     3. Under **Access Routing Location** , select one of the following options: 
        * **Global** : Choose this option to allow global load balancing for high availability and automatic failover across all regions. API requests automatically reroute if one region fails. If [advanced data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#advanced-data-residency) isn't enabled, this option is selected by default.
        * **Regional** : Choose this option to restrict load balancing to the same region as the Apigee instance. Recommended for organizations with data residency. **Note:** If [advanced data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#advanced-data-residency) is enabled, this option is selected by default and can't be changed.
     4. Under **Domain Type** , choose one of the following options: 
        * **Automatically managed domain, subnetwork and SSL certificates** : Choose this option to use the `nip.io` wildcard DNS service, and a Google-managed certificate to secure your domain. Apigee automatically creates an L7 global external load balancer to forward traffic to your runtime. 
        * **Customize** : Choose this option if you want to customize your domain name, subnetwork, or SSL certificate. Apigee automatically creates an L7 global external load balancer to forward traffic to your runtime. You can select or clear any of the following options to enter custom details: 
          * **Customize domain name** : Optional. Enter the custom domain name.
          * **Customize subnetwork** : Optional. Select an available subnetwork name from the dropdown menu. The subnetwork selected should be in the same region as the runtime instance.
          * **Customize SSL certificate** : Customize the SSL certificate. **Note:** If you selected **Regional** access routing, this option is selected by default and can't be changed.

Under **SSL Certificate** , select one of the following: 

            * **Automatically managed**. A [Google-managed certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) is automatically created for your domain. This can take up to 60 minutes.
            * **Self-managed certificate**. **Note:** If you selected **Regional** access routing, which requires a self-managed certificate, this option is selected by default and can't be changed.

To select an existing certificate:

              1. Select an existing certificate from the drop-down list. If there is no certificate in the list, click **Add new**. 
              2. Browse the file system and select the certificate you wish to use.
              3. Click **Save SSL**.

To provide a new certificate:

              1. Click in the **Select certificate** drop-down list. 
              2. Click **Add new**.
              3. In the respective fields, browse your file system and attach the files containing the certificate and private key. Both should be PEM-formatted.
              4. Click **Save SSL**.
     5. Click **Set access**. 

Apigee prepares your instance for external access. This includes creating firewall rules, uploading certificates, and creating a load balancer.

This process can take several minutes.

### Internal Access

This section describes how to configure routing when you're using the Cloud Console and you _do not_ want to allow external access to your API proxy. Instead, you want to limit access to _internal_ requests only that originate from within the VPC.

**To configure routing for internal access in the Cloud Console:**

     1. Click create**Edit** to open the **Configure access** panel. 
     2. Select **No internet access**.

     3. Click **Set access**.

  2. Click **Next**.
  3. Click **Submit** to begin the provisioning process.

The provisioning process may take up to 40 minutes to complete. If you want to leave the page while provisioning is in progress, a notification will appear in notifications **Notifications** in the Cloud console when the operation completes.

Once provisioning is complete, the **Apigee Overview** page will appear and you can begin exploring Apigee!




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
