---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting/
title: Step 3: Configure hosting and encryption \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:08.256251+00:00
---

# Step 3: Configure hosting and encryption  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 3: Configure hosting and encryption Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-1-setup.png)

## What you're doing in this step

In this step, depending on your specific  user journey, you specify hosting locations for your Apigee analytics or control plane, runtime and dataplane instances, and API consumer data region. You also specify encryption key selections. 

**Tip:** If you want to get up and running quickly with the simplest configuration, follow the instructions in User journey A: Google-managed encryption, no data residency. 

The difference between each of the user journeys is the selection or creation of encryption keys, whether they are [managed by Google](https://docs.cloud.google.com/storage/docs/encryption/default-keys) or the [customer](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys), and whether [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) is enabled or not.

Some features are not supported when data residency is enabled. See [ Data residency compatibility](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-compatibility) for details. 

If your Google Cloud project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies), data residency is enabled by default and CMEK is required. 

The following keys are used during organization creation:

**Encryption key** | **Description**  
---|---  
Control plane key |  Encrypts Analytics data that is stored within BigQuery in Apigee tenant project. Encrypts API proxies, Target Servers, Truststores and Keystores and anything else shared across runtimes.  
API consumer data key | Encrypts service infrastructure data. This is required to be a region within the control plane location.  
Runtime database key | Encrypts application data such as KVMs, cache, and client secrets, which is then stored in the database.  
  


The following key is used during each instance creation:

**Encryption key** | **Description**  
---|---  
Runtime disk key | Encrypts KVMs; environment cache; quota buckets and counters. Encrypts KMS data API products, developers, developer apps, OAuth tokens (including access tokens, refresh tokens, and authorization codes), and API keys.  
  
## Perform the step

#### Permissions required for this task

* * *

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ Runtime instance permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#runtime-instance-permissions). 

* * *

To view the steps for your specific user journey, select one of the following user journeys. They are listed in order of complexity, with the easiest being user journey A. 

#### View user journey flow diagram

* * *

The following diagram shows the possible user journeys to configure hosting and encryption for a Pay-as-you-go organization using the Cloud console. 

The user journeys are noted A through F and are ordered easy to complex, where A is the easiest, and F is the most complex.

![Paid provisioning flow](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/wizard-paid-config-host.svg)

* * *

| User journey | Description  
---|---|---  
![icon A](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/icon-a-circled.svg) | User journey A: Google-managed encryption, no data residency |  Select this option if you:

  * Want Google to manage encryption keys
  * Are not required to store [core content and processing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regions) in the same geographic region
  * Your Google Cloud project does not have a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies)

  
![icon B](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/icon-b-circled.svg) | User journey B: Google-managed encryption, with data residency |  Select this option if you:

  * Want Google to manage encryption keys
  * Want to store [core content and processing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regions) in the same geographic region
  * Your Google Cloud project does not have a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies)

  
![icon C](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/icon-c-circled.svg) | User journey C: Customer-managed encryption, no data residency |  Select this option if you:

  * Want to manage your own encryption keys
  * Are not required to store core content and processing in the same geographic region
  * Your Google Cloud project does not have a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies)

  
![icon D](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/icon-d-circled.svg) | User journey D: Customer-managed encryption, with data residency |  Select this option if you:

  * Want to manage your own encryption keys
  * Want to store your core content and processing in the same geographic region
  * Your Google Cloud project does have a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies)

  
  
### User journey A: Google-managed encryption, no data residency

**Note:** If your Google Cloud project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies), data residency and CMEK are required. User journey D is the only applicable path. 

In Step 3, the console displays a list of hosting and encryption configuration options and their default values. You can accept the default configuration, or click create **Edit** to open the **Hosting and encryption keys** panel.

  1. In the **Encryption type** section, select **Google-managed encryption key**. This is a Google-managed, server-side encryption key used to encrypt your Apigee instances and data before it is written to disk.
  2. Click **Next**.
  3. In the **Control Plane** section: 
     1. Clear the **Enable data residency** box. **Note** : If you are provisioning a new Apigee organization within a Google Cloud project with a [resource location constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) applied in an organization policy, confirm that the location constraint is set to `global`. Because the Apigee control plane is a global entity by default, provisioning will fail if a constraint other than `global` is applied. For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).
     2. From the **Analytics region** drop-down list, select the physical location where you want your analytics data stored. For a list of available Apigee API Analytics regions, including regions that support API hub, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions). If you select a region that does not support API hub, an API hub instance is not created. To learn more about API hub, see [ What is API hub?](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub)

     3. Click **Confirm**.
  4. In the **Runtime** section: 
     1. From the **Runtime hosting region** drop-down list, select the region in which you want your instance hosted. 
     2. Under **Runtime database encryption key** , **Google-managed** is listed as the encryption type.
     3. Under **Runtime disk encryption key** , **Google-managed** is listed as the encryption type.
     4. Click **Confirm**.
     5. Click **Done**. 
  5. Click **Next**.

**Warning:** When you submit the completed configuration for provisioning Apigee (at the end of [ Step 4](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing)), you cannot go back and change the hosting region and encryption key selections. Apigee does not support updating the hosting region or encryption key selections after provisioning is complete. For example, if you select Google-managed encryption, you cannot change it to Customer-managed encryption later and vice versa. 

Go to the next step, [ Step 4: Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing).

### User journey B: Google-managed encryption, with data residency

**Note:** If your Google Cloud project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies), data residency and CMEK are required. User journey D is the only applicable path. 

In Step 3, the console displays a list of hosting and encryption configuration options and their default values. You can accept the default configuration, or click create **Edit** to open the **Hosting and encryption keys** panel.

  1. In the **Encryption type** section, select **Google-managed encryption key**. This is a Google-managed, server-side encryption key used to encrypt your Apigee instances and data before it is written to disk.
  2. Click **Next**.
  3. In the **Control Plane** section: 
     1. Select the **Enable data residency** box.
     2. From the **Control plane hosting jurisdiction** drop-down list, select the physical location where you want your data stored. 

**Note** : A jurisdiction refers to a location within a geopolitical boundary that may span more than one region. For a list of available control plane hosting jurisdictions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).

     3. Under **Control plane encryption key** , **Google-managed** is listed as the encryption type. 
  4. In the **API consumer data region section:**
     1. From the **API consumer data region** drop-down list, select the physical location where you want your data stored. For a list of available consumer data regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). 
     2. Under **API consumer data encryption key** , **Google-managed** is listed as the encryption type.
     3. Click **Confirm**.
  5. In the **Runtime** section: 
     1. From the **Runtime hosting region** drop-down list, select the region in which you want your instance hosted. For a list of available runtime regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-runtime-regions). When using data residency, the runtime location must be within the control plane region. 
     2. Under **Runtime database encryption key** , **Google-managed** is listed as the encryption type. 
     3. Under **Runtime disk encryption key** , **Google-managed** is listed as the encryption type. 
     4. Click **Confirm**.
     5. Click **Done**. 
  6. Click **Next**.

**Warning:** When you submit the completed configuration for provisioning Apigee (at the end of [ Step 4](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing)), you cannot go back and change the hosting region and encryption key selections. Apigee does not support updating the hosting region or encryption key selections after provisioning is complete. For example, if you select Google-managed encryption, you cannot change it to Customer-managed encryption later and vice versa. 

Go to the next step, [ Step 4: Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing).

### User Journey C: Customer-managed encryption, no data residency

**Note:** If your Google Cloud project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies), data residency and CMEK are required. User journey D is the only applicable path. 

In Step 3, the console displays a list of hosting and encryption configuration options and their default values. You can accept the default configuration, or click create **Edit** to open the **Hosting and encryption keys** panel.

  1. In the **Encryption type** section, select **Customer-managed encryption key (CMEK)**. This is a user-managed, server-side encryption key used to encrypt your Apigee instances and data before it is written to disk.
  2. Click **Next**.
  3. In the **Control Plane** section: 
     1. Clear the **Enable data residency** box. **Note** : If you are provisioning a new Apigee organization within a Google Cloud project with a [resource location constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) applied in an organization policy, confirm that the location constraint is set to `global`. Because the Apigee control plane is a global entity by default, provisioning will fail if a constraint other than `global` is applied. For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).
     2. From the **Analytics region** drop-down list, select the physical location where you want your analytics data stored. For a list of available Apigee API Analytics regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#select-an-apigee-api-analytics-region). 

     3. Click **Confirm**. 
  4. In the **Runtime** section: 
     1. From the **Runtime hosting region** drop-down list, select the region in which you want your instance hosted. 
     2. From the **Runtime database encryption key** drop-down list, select or create a key for data stored and replicated across runtime locations. 
     3. Click **Grant** if prompted.
     4. From the **Runtime disk encryption key** , drop-down list, select or create a key for runtime instance data before it is written to disk. Each instance has its own disk encryption key. 
     5. Click **Grant** if prompted.
     6. Click **Confirm**.
     7. Click **Done**.
  5. Click **Next**.

**Warning:** When you submit the completed configuration for provisioning Apigee (at the end of [ Step 4](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing)), you cannot go back and change the hosting region and encryption key selections. Apigee does not support updating the hosting region or encryption key selections after provisioning is complete. For example, if you select Google-managed encryption, you cannot change it to Customer-managed encryption later and vice versa. 

Go to the next step, [ Step 4: Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing).

### User journey D: Customer-managed encryption, with data residency

In Step 3, the console displays a list of hosting and encryption configuration options and their default values. You can accept the default configuration, or click create **Edit** to open the **Hosting and encryption keys** panel. 

  1. In the **Encryption type** section, select **Customer-managed encryption key (CMEK)**. This is a user-managed, server-side encryption key used to encrypt your Apigee instances and data before it is written to disk. **Note:** If your Google Cloud project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies), **Google-managed encryption key** is disabled and **Customer-managed encryption key** cannot be cleared. 
  2. Click **Next**.
  3. In the **Control Plane** section: 
     1. Select the **Enable data residency** box. **Note:** If your Google Cloud project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies), data residency is selected and cannot be cleared. 
     2. From the **Control plane hosting jurisdiction** drop-down list, select the physical location where you want your data stored. 

**Note** : A jurisdiction refers to a location within a geopolitical boundary that may span more than one region. For a list of available control plane hosting jurisdictions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).

     3. From the **Control plane encryption key** drop-down list, select or create a key for data stored and replicated across runtime locations. **Note** : This step is only required if you select `us (multiple regions in us)` or `eu (multiple regions in European Union)` as your control plane hosting jurisdiction. If you select another region, this key is not required.
     4. Click **Grant** if prompted.
  4. In the **API consumer data region section:**
     1. From the **API consumer data region** drop-down list, select the physical location where you want your data stored. For a list of available consumer data regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). 
     2. From the **API consumer data encryption key** drop-down list, select or create a key for data stored for the control plane.
     3. Click **Grant** if prompted.
     4. Click **Confirm**.
  5. In the **Runtime** section: 
     1. From the **Runtime hosting region** drop-down list, select the region in which you want your instance hosted. When using data residency, the runtime location must be within the control plane region. 
     2. From the **Runtime database encryption key** drop-down list, select or create a key for data stored and replicated across runtime locations. 
     3. Click **Grant** if prompted.
     4. From the **Runtime disk encryption key** , drop-down list, select or create a key for runtime instance data before it is written to disk. Each instance has its own disk encryption key. 
     5. Click **Grant** if prompted.
     6. Click **Confirm**.
     7. Click **Done**. 
  6. Click **Next**.

**Warning:** When you submit the completed configuration for provisioning Apigee (at the end of [ Step 4](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing)), you cannot go back and change the hosting region and encryption key selections. Apigee does not support updating the hosting region or encryption key selections after provisioning is complete. For example, if you select Google-managed encryption, you cannot change it to Customer-managed encryption later and vice versa. 

Go to the next step, [ Step 4: Customize access routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing).

## How to create a key

To create a key:

  1. Click **Create key**.
  2. Select a key ring, or if one doesn't exist, enable **Create key ring** and enter a key ring name and pick your key ring location. Key ring names can contain letters, numbers, underscores (_), and hyphens (-). Key rings can't be renamed or deleted.
  3. Click **Continue**.
  4. Create a key. Enter a name and protection level. Note that key names can contain letters, numbers, underscores (_), and hyphens (-). Keys can't be renamed or deleted. For protection level, **Software** is a good choice. This is the same default used by Cloud KMS; however, you can change it if you wish.
  5. Click **Continue** and review your selections.
  6. Click **Create**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
