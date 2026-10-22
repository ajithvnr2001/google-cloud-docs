---
url: https://docs.cloud.google.com/application-integration/docs/enable-new-region/
title: Manage regions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:59.822763+00:00
---

# Manage regions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/enable-new-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage regions

Application Integration is _regional_ , which means the infrastructure that runs your integrations is located in a specific region, and Google manages it so that it is available redundantly across [all of the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions). Apart from selecting the initial provisioning region for Application Integration during the [setup](https://docs.cloud.google.com/application-integration/docs/setup-application-integration) process, you can also enable or provision new regions to create and manage your integrations within the same Google Cloud project.

This page describes the steps needed to successfully provision a new Application Integration region and edit an existing region in your Google Cloud project.

## Before you begin

Enable the following APIs:

  * [Application Integration API](https://console.cloud.google.com/apis/library/integrations.googleapis.com) (`integrations.googleapis.com`)
  * [Connectors API](https://console.cloud.google.com/apis/library/connectors.googleapis.com) (`connectors.googleapis.com`)



## Provision new region

To provision a new region for Application Integration in your Google Cloud project, select one of the following options: 

### Console

  1. Go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Regions**

The **Regions** page appears listing all the regions provisioned in your project. 

  3. Click **Provision new region**.
  4. Configure the following fields in the **Provision new region** page: 
     1. **Region:** Select the new regional location that you want to provision. 

For information about the supported Application Integration regions, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations). 

     2. **Advanced settings:** Optionally, expand this section to enable or disable the HTTP access for integrations and configure the [encryption method](https://docs.cloud.google.com/application-integration/docs/encryption) for the selected region. 
        * **HTTP:** Click the **Enable HTTP** toggle to enable HTTP access for integrations within the selected region. When enabled, integrations in this region can be accessed over HTTP. **Note:** The HTTP toggle is disabled by default to ensure all integrations are invoked securely over HTTPS. 
        * **AI features:** Click the **Enable AI features** toggle to enable AI features in the selected region. For more information about troubleshooting using Gemini AI, see [Troubleshoot failed execution logs using AI](https://docs.cloud.google.com/application-integration/docs/troubleshoot-ai).
        * **Encryption:** Select the encryption method for the selected region. There are two options: 
          * **Google-owned and Google-managed encryption key:** This is the default encryption method. Use this method if you want Google to manage the encryption keys that protect your data in the selected region.
          * **Customer-managed encryption key (CMEK):** Use this method if you want to manage the encryption keys that protect your data in the selected region. **Caution:** Enabling CMEK encryption for an Application Integration region cannot be undone. This also means that you can't change/switch the encryption method for a region once CMEK is enabled.

When configuring your encryption settings, you have two options for managing CMEK: Application Integration and Connectors (CMEK), and Use a different CMEK for Integration Connectors, as follows:

            * **Application Integration and Connectors - CMEK:** This is the default option and is suitable if you want to use the same encryption key for both Application Integration and Integration Connectors. To use this option, perform the following steps: 
              1. Click **Select a Cloud KMS key** and choose an existing CMEK key available in the selected region. You can also create a new key or use the KMS resource ID of your existing key.
              2. Click **Verify** to check if your default service account has CryptoKey access to the selected CMEK key.
              3. If the verification fails, click **Grant** to assign the CryptoKey Encrypter/Decrypter IAM role to the default service account.
**Tip:** Granting CryptoKey access is an optional step, which means that you can directly click Done to complete the Application Integration setup process. However, if you don't grant CryptoKey access, authentication profiles for Application Integration are not configured, and you have to manually grant this access when creating a new authentication profile.
            * **Use different CMEK for Integration Connectors:** Select this checkbox if you prefer to use separate encryption keys for Application Integration and Integration Connectors. If selected, the following options appear: 
              * **Application Integration - CMEK**
                1. Click **Select a Cloud KMS key** and choose an existing CMEK key for Application Integration in the selected region. Alternatively, you can create a new key or use the Key resource ID of an existing one.
                2. Click **Verify** to finish setting up CMEK for Application Integration.
              * **Integration Connectors - CMEK**
                1. Click **Select a Cloud KMS key** and choose an existing CMEK key for Integration Connectors in the selected region. Alternatively, you can create a new key or use the Key resource ID of an existing key.
                2. Click **Verify** to check if your default service account has CryptoKey access to the selected CMEK.
                3. If the verification for the selected CMEK key fails, click **Grant** to assign the CryptoKey Encrypter/Decrypter IAM role to the default service account.
**Note:** Application Integration automatically checks if your default service account has CryptoKey access to the selected CMEK, if Integration Connectors CMEK is enabled. If the verification fails, you have to manually grant this access.

For more information about CMEK, see [Customer-managed encryption keys](https://docs.cloud.google.com/application-integration/docs/cmek).

  5. Click **Done**.



### Terraform

Use the `[google_integrations_client](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integrations_client)` resource. The following example provisions the `us-east1` region: 
    
    
    resource "random_id" "default" {
      byte_length = 8
    }
    
    resource "google_kms_key_ring" "default" {
      name     = "${random_id.default.hex}-example-keyring"
      location = "us-east1"
    }
    
    resource "google_kms_crypto_key" "default" {
      name            = "crypto-key-example"
      key_ring        = google_kms_key_ring.default.id
      rotation_period = "7776000s"
    }
    
    resource "google_kms_crypto_key_version" "default" {
      crypto_key = google_kms_crypto_key.default.id
    }
    
    resource "google_service_account" "default" {
      account_id   = "service-account-id"
      display_name = "Service Account"
    }
    
    resource "google_integrations_client" "example" {
      location                   = "us-east1"
      create_sample_integrations = true
      run_as_service_account     = google_service_account.default.email
      cloud_kms_config {
        kms_location   = "us-east1"
        kms_ring       = basename(google_kms_key_ring.default.id)
        key            = basename(google_kms_crypto_key.default.id)
        key_version    = basename(google_kms_crypto_key_version.default.id)
        kms_project_id = data.google_project.default.project_id
      }
    }

## Edit region

You can edit an existing region to enable or disable integration governance, and to update the [data encryption method](https://docs.cloud.google.com/application-integration/docs/encryption) for the region. 

**Caution:** Enabling CMEK encryption for an Application Integration region cannot be undone. This also means that you can't change the encryption method for a region if CMEK is already enabled. 

To edit an existing region in Application Integration, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Regions**.

The **Regions** page appears, listing the provisioned regions in Application Integration. 

  3. For the existing region that you want to edit, in the **Actions** column, click  more_vert **Region actions** and select **Edit**. 

The **Edit region** pane appears.

  4. Expand **Advanced settings**.
  5. To enable or disable integration governance for the selected region, click the **Enable governance** toggle. **Note:**
     * Enable governance to make service account authentication mandatory for the region. Once governance is enabled, you must manually add a service account to all the new integrations and integration versions created in this region. You can change or update the service account details of an integration any time from the settings **Integration settings** pane in the integration toolbar. 

If governance is enabled, you can publish or test an integration only when a service account is attached to it.

     * If you disable governance for the selected region, then all the existing published integrations continue to use their respective attached service accounts until a new version of the integrations is created.
  6. To enable or disable HTTP access for integrations in the selected region, click the **Enable HTTP** toggle. When enabled, integrations in this region can be accessed over HTTP.
  7. To enable or disable AI features for integrations in the selected region, click the **Enable AI features** toggle. When enabled, you can use AI features like troubleshooting using Gemini AI in the selected region.
  8. To enable masking for variables, in the **Variable Masking** section, click the **Enable Variable Masking in logs** toggle. This feature is in [preview](https://docs.cloud.google.com/products#product-launch-stages). 

For information about masking, see [Mask sensitive data in logs](https://docs.cloud.google.com/application-integration/docs/mask-sensitive-data-logs).

  9. To enable CMEK encryption for selected region, select **Customer-managed encryption key (CMEK)** , and do the following: 
     1. Select a CMEK from the available drop-down list. The CMEKs listed in the drop-down are based on the provisioned region. To create a new key, see [Create new CMEK](https://docs.cloud.google.com/application-integration/docs/cmek#new-key). 
     2. Click **Verify** to check if your default service account has CryptoKey access to the selected CMEK.
     3. If the verification for the selected CMEK fails, click **Grant** to assign the [CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) IAM role to the default service account. 
  10. To enable CMEK encryption for Integration Connectors, select **Use different CMEK for Integration connectors** , and do the following: 
     1. Select a CMEK from the available drop-down list. The CMEKs listed in the drop-down are based on the provisioned region. To create a new key, see [Create new CMEK](https://docs.cloud.google.com/application-integration/docs/cmek#new-key). 
     2. Click **Verify** to finish setting up Integration Connectors CMEK.
  11. Click **Done** to complete editing the region.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
