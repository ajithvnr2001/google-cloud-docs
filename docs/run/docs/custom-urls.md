---
url: https://docs.cloud.google.com/run/docs/custom-urls/
title: Create custom URLs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:21.456626+00:00
---

# Create custom URLs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/custom-urls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Create custom URLs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Custom URLs**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure and manage custom URLs, letting you obtain a simple-to-type, memorable, and globally available URL for your Cloud Run services instead of the default deterministic URL:

  * **Custom URL format** : `https://CUSTOM_SUBDOMAIN.cloud.run`
  * **Default URL format** : `https://SERVICE_NAME-PROJECT_NUMBER.REGION.run.app`



By using custom URLs, you can share your services without setting up custom domains, DNS records, or external load balancers.

When you use custom URLs for your Cloud Run services, you get the following benefits:

  * Simple URLs: Map your service to a clean `https://CUSTOM_SUBDOMAIN.cloud.run` format.
  * Global availability: Custom URLs are accessible from anywhere, matching standard `.run.app` URLs.
  * Flexible lifecycle: Flexibly attach, detach, or move a custom URL between services without deploying a new revision.
  * Multiple mappings: You can map multiple custom URLs to a single service.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Set up your Cloud Run development environment](https://docs.cloud.google.com/run/docs/setup) in your Google Cloud project.
  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).



### Required roles

To get the permissions that you need to manage custom URLs, ask your administrator to grant you the following IAM roles: 

  * To create, update, or delete custom URL mappings: [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * By default, you can map up to 50 domains per project.
  * The custom URL subdomain must be between 6 and 63 characters, adhere to standard DNS naming conventions that allow alphanumeric characters and hyphens, and cannot start or end with a hyphen.
  * Certain subdomains are restricted.
  * You cannot temporarily disable a custom URL like you can with a default `.run.app` URL. To stop serving traffic from it, you must delete the mapping.
  * Cloud Run services that [restrict ingress](https://docs.cloud.google.com/run/docs/securing/ingress#settings) to **Internal** or **Internal and Cloud Load Balancing** traffic aren't supported.
  * Terraform isn't supported for custom URLs. To avoid potential breaking changes, don't use the Preview [`domain_mapping` resource](https://docs.cloud.google.com/run/docs/mapping-custom-domains#map).
  * Custom URLs are fully independent. If you choose to [disable the default `.run.app` URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url) for a service, your custom URL mapping remains fully active and accessible.

**Important:** Google reserves the right to manage its domains, which includes the ability to revoke or reassign subdomains to prevent abuse, protect trademarks, address security issues, or meet other operational or legal requirements.

## Attach or map a custom URL to a service

You can attach a custom URL to a new service when you deploy it, or map a custom URL to an existing service using the Google Cloud console or the gcloud.

### Attach custom URLs to a new service

When you deploy a new Cloud Run service, you can attach a custom URL as part of the deployment configuration.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Run** **Services** page.

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click **Deploy container**.

  3. Fill in the basic configuration details for your service.

  4. In the **Custom URLs** section, click **Add a custom URL**.

  5. Enter a valid custom URL subdomain.

  6. Optional. To add multiple custom URLs, click **Add a custom URL** again.

  7. Click **Create**.




###  gcloud 

  * **Deploy from container image**

To create a custom URL subdomain mapping for a Cloud Run service during its initial container deployment, run the following command:
        
        gcloud beta run deploy SERVICE \
            --image=IMAGE_URL \
            --domain=CUSTOM_SUBDOMAIN.cloud.run

Replace the following:

    * SERVICE: the name of the Cloud Run service that you're deploying. You can omit this parameter, but you might be prompted for the service name if you omit it.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
    * CUSTOM_SUBDOMAIN: the subdomain that you want to attach.
  * **Deploy from source**

To create a custom URL subdomain mapping for a Cloud Run service during its initial source deployment, run the following command:
        
        gcloud beta run deploy SERVICE \
            --source=SOURCE \
            --domain=CUSTOM_SUBDOMAIN.cloud.run

Replace the following:

    * SERVICE: the name of the Cloud Run service that you're deploying. You can omit this parameter, but you might be prompted for the service name if you omit it.
    * SOURCE: the location of the source to build (for example, `.` for the current directory).
    * CUSTOM_SUBDOMAIN: the subdomain that you want to attach.



If the requested subdomain is already in use by another user or service across Google Cloud, you receive an error and must choose a target that's unique.

### Map custom URLs to an existing service

You can map a custom URL to an existing Cloud Run service using the Google Cloud console or the gcloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Domain mappings** page.

[Go to Domain mappings](https://console.cloud.google.com/run/domains)

  2. Click **Add custom URL**.

  3. In the **Service** list, select the service that you want to map to.

  4. Enter your custom URL subdomain.

  5. Click **Continue**.




If you want to add multiple custom URLs, click **Add a custom URL** again and follow the previous steps.

###  gcloud 

To create a custom URL subdomain mapping for an existing service, run the following command:
    
    
    gcloud beta run domain-mappings create \
        --service=SERVICE_NAME \
        --domain=CUSTOM_SUBDOMAIN.cloud.run

Replace the following:

  * SERVICE_NAME: the name of the service that you are mapping the custom URL to.
  * CUSTOM_SUBDOMAIN: the subdomain that you want to attach.



Optional. To map multiple custom URLs using the gcloud CLI, execute the mapping creation command repeatedly for each custom URL:
    
    
    gcloud beta run domain-mappings create \
        --service=SERVICE_NAME \
        --domain=CUSTOM_SUBDOMAIN_1.cloud.run
    
    gcloud beta run domain-mappings create \
        --service=SERVICE_NAME \
        --domain=CUSTOM_SUBDOMAIN_2.cloud.run

Replace the following:

  * SERVICE_NAME: the name of the service that you are deploying.
  * CUSTOM_SUBDOMAIN_1: the first subdomain to attach.
  * CUSTOM_SUBDOMAIN_2: the second subdomain to attach.



If the requested subdomain is already in use by another user or service across Google Cloud, you receive an error and must choose a target that is unique.

## List and view custom URLs

You can list all custom URLs and view mapping details for your environment.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Run** page.

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the name of the service.

  3. Go to the **Networking** tab.

  4. Locate your attached URLs in the **Custom domains** section under the **Endpoints** label.




###  gcloud 

To list all custom URLs and domain mappings in a project, run the following command:
    
    
    gcloud beta run domain-mappings list

To view details for a specific custom URL subdomain mapping, run:
    
    
    gcloud beta run domain-mappings describe \
        --domain=CUSTOM_SUBDOMAIN.cloud.run

Replace CUSTOM_SUBDOMAIN with the subdomain that you want to describe.

## Secure with custom audiences

You can attach a [custom audience](https://docs.cloud.google.com/run/docs/configuring/custom-audiences) to your custom URL to restrict access.
    
    
    gcloud beta run services update SERVICE_NAME \
        --add-custom-audiences=CUSTOM_SUBDOMAIN.cloud.run

Replace the following:

  * SERVICE_NAME: the name of your service.
  * CUSTOM_SUBDOMAIN: the subdomain that acts as your custom audience.



## Delete a custom URL

**Warning:** If you delete a domain mapping, the subdomain is immediately available for other users to claim. It's heavily recommended to NOT delete these domain mappings frequently due to the risk of domain sniping. You are responsible for managing the lifecycle of these domains.

You can delete a custom URL mapping when it's no longer needed.

###  Console 

  1. In the Google Cloud console, go to the **Domain mappings** page.

[Go to Domain mappings](https://console.cloud.google.com/run/domains)

  2. Select the checkbox next to the custom URL that you want to delete.

  3. Click **Delete**.




###  gcloud 

To remove a custom URL subdomain mapping from a Cloud Run service, run the following command:
    
    
    gcloud beta run domain-mappings delete \
        --domain=CUSTOM_SUBDOMAIN.cloud.run

Replace CUSTOM_SUBDOMAIN with the subdomain that you want to delete.

**Important:** If you delete the underlying Cloud Run service, the custom URL mapping is **not** automatically released. You must explicitly delete the custom URL mapping to release your claim.

## Known issues

  * Propagation latency: It might take a few seconds after creating a custom URL before it's fully operational. Accessing the URL immediately after creation might result in a temporary routing error.

  * Update or move a custom URL: There is no direct update command for custom URLs. To move an attached custom URL from one service to another, you must follow a delete-and-recreate flow.

###  Console 

    1. In the Google Cloud console, go to the **Domain mappings** page.

[Go to Domain mappings](https://console.cloud.google.com/run/domains)

    2. Select the checkbox next to the custom URL that you want to move.

    3. Click **Delete**.

    4. Click **Add custom URL**.

    5. In the **Service** list, select the new target service.

    6. Enter your exact previously claimed custom URL subdomain.

    7. Click **Create** to redirect traffic to the new service.

###  gcloud 

    1. Delete the existing mapping from the old service:
           
           gcloud beta run domain-mappings delete \
               --domain=CUSTOM_SUBDOMAIN.cloud.run

Replace CUSTOM_SUBDOMAIN with the subdomain that you previously claimed.

    2. Reclaim and map the URL to the new service:
           
           gcloud beta run domain-mappings create \
               --service=NEW_SERVICE_NAME \
               --domain=CUSTOM_SUBDOMAIN.cloud.run

Replace the following:

       * NEW_SERVICE_NAME: the name of the service that you are moving the custom URL to.
       * CUSTOM_URL_DOMAIN: the subdomain that you want to attach.




## What's next

  * Learn more about [Mapping custom domains](https://docs.cloud.google.com/run/docs/mapping-custom-domains).
  * Learn about [Serving static assets with CDN](https://docs.cloud.google.com/run/docs/set-up-cdn).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
