---
url: https://docs.cloud.google.com/looker/docs/looker-core-instance-create/
title: Create a public secure connections Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:53.391847+00:00
---

# Create a public secure connections Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-instance-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create a public secure connections Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses how to provision a Looker (Google Cloud core) production or [non-production](https://docs.cloud.google.com/looker/docs/looker-core-overview#staging_environments_and_testing) instance configured for public secure connections.

If you want to create a private connections instance, the configuration must be assigned at instance creation. For instructions on how to create a private connections instance, follow the procedure on the [Create a Looker (Google Cloud core) Private Service Connect instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc) or on the [Create a Create a private connections (private services access) Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip) documentation pages instead of the following procedure.

## Before you begin

  1. [Work with Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to ensure that your [annual contract](https://cloud.google.com/looker/pricing) is completed and that you have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) allocated in your project.
  2. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console).
  3. In the Google Cloud console, on the project selector page, [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) or navigate to an existing one. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Enable the Looker API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=looker.googleapis.com)

**Caution:** Disabling the Looker API after instance creation will affect Looker (Google Cloud core) features. For example, disabling the API will disable the ability to create [instance backups](https://docs.cloud.google.com/looker/docs/looker-core-backup-restore).
  5. If you want to use [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc), you must create a [private connections (private services access)](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip) instance instead of a public secure connection instance.



### Required roles

To get the permissions that you need to create a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project the instance will reside in. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to create a Looker (Google Cloud core) instance. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

You may also need additional IAM roles to set up Workforce Identity Federation or customer-managed encryption keys (CMEK). Learn more by visiting the [Use Workforce Identity Federation for Looker (Google Cloud core) user authentication](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity) or [Enable CMEK for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek) documentation pages for those features.

## Create a Looker (Google Cloud core) instance

> Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.

**Important:** If you want to use customer-managed encryption keys (CMEK) with the Looker (Google Cloud core) instance that you are creating, see the [Enable CMEK for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek) documentation page for information on the additional setup that's required prior to instance creation.

To create your Looker (Google Cloud core) instance, select one of the following options:

### console

  1. Navigate to the Looker (Google Cloud core) product page from your project in the Google Cloud console. If you have already created a Looker (Google Cloud core) instance within this project, this will open the **Instances** page. 

[Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker)

  2. Click **CREATE INSTANCE**.
  3. In the **Instance name** section, provide a name for your Looker (Google Cloud core) instance. The instance name isn't associated with the URL of the Looker (Google Cloud core) instance once it is created. The instance name cannot be changed after instance creation.
  4. In the **Region** section, select the appropriate option from the drop-down menu to host your Looker (Google Cloud core) instance. Select the region that matches the region in the subscription contract, which is where the [quota for your project](https://docs.cloud.google.com/docs/quotas/view-manage) is allocated. Available regions are listed on the [Looker (Google Cloud core) locations](https://docs.cloud.google.com/looker/docs/looker-core-locations) documentation page. You cannot change the region once the instance has been created.
  5. In the **Edition** section, set the instance edition according to your organization's needs. The edition type affects some of the [features that are available](https://docs.cloud.google.com/looker/docs/looker-core-edition-types) for the instance. Make sure that you choose the same edition type as listed in your [annual contract](https://cloud.google.com/looker/pricing) and that you have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) allocated for that edition type. These are the edition options:

     * **Standard** : Looker (Google Cloud core) platform for small organizations or teams with fewer than 50 users
     * **Enterprise** : Looker (Google Cloud core) platform with enhanced security features for addressing a wide variety of internal BI and analytics use cases
     * **Embed** : Looker (Google Cloud core) platform for deploying and maintaining reliable external analytics and custom applications at scale
     * Non-production editions: If you want a staging and testing environment, select one of the non-production editions. For more information, see the [Non-production instances](https://docs.cloud.google.com/looker/docs/looker-core-overview#staging_environments_and_testing) documentation.
     * Trial editions: A [trial edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#trials) has the same feature support as its corresponding production edition, with the exception that trial editions are valid for 90 days.

Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](https://docs.cloud.google.com/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.

**Tip:** If your project doesn't have quota, you won't be able to select an edition type. [Contact Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to allocate quota to your project. For more troubleshooting help, see the [Troubleshooting Looker (Google Cloud core) instance creation failures](https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-instance-creation-troubleshooting) documentation page.
  6. In the **Customize your instance** section, click **Show configuration options** to display a group of additional settings that you can customize for the instance.

  7. In the **Connections** section, select **Use public secure connections**. A public secure connection setting assigns an external, internet-accessible IP address and is available for all edition types.

**Note:** If you are creating an **Enterprise** and **Embed** edition, you can also use a private connection, which uses a [Private Service Connect (PSC)](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview) URI and PSC endpoints for outbound connections, or a hybrid connection, which will have a public URL and use PSC endpoints for outbound connections. If you want to use private or hybrid connection, follow the steps on the [Create a Looker (Google Cloud core) Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-create-psc) documentation page.
  8. In the **Authentication** section, select the [primary authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication#primary-authentication-methods) for the instance. Primary authentication methods are required for all Looker (Google Cloud core) instances. The following primary authentication options are available: 
     * **Google OAuth** : Use this method if your users authenticate with Google Accounts (Google Workspace or Cloud Identity). This option is the default.
     * **Workforce Identity Federation (SAML/OIDC)** : Use this method if your users authenticate with an external identity provider (such as Okta, Microsoft Entra ID, or PingIdentity) and you want single sign-on (SSO) with IAM access control without managing individual Google Accounts.
**Note:** The integration between Looker (Google Cloud core) and Workforce Identity Federation is in [preview](https://cloud.google.com/products#product-launch-stages).
  9. In the **Release Channel** section, select the [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) that best fits your needs:

     * **Rapid** : Earliest access to features. Recommended default for non-production instances.
     * **Regular** : Balanced stability. Recommended for production instances. 
     * **No channel** : No release channel. During the preview, No channel is the default.
**Note:** The release channels feature is in [preview](https://cloud.google.com/products#product-launch-stages).
  10. If you are creating an **Enterprise** or **Embed** edition instance, you will see the **Encryption** section. In the **Encryption** section, you can select the type of encryption to use on your instance. The following encryption options are available:

     * [**Google-managed encryption key**](https://docs.cloud.google.com/docs/security/encryption/default-encryption): This option is the default and doesn't require any additional configuration.
     * [**Customer-managed encryption key (CMEK)**](https://docs.cloud.google.com/kms/docs/cmek): See the [Using customer-managed encryption keys with Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek#create_a_instance_with_cmek) documentation page for more information on CMEK and how to configure it during instance creation. The type of encryption cannot be changed after instance creation.
     * **Enable[FIPS 140-3 level 1 Validated Encryption](https://csrc.nist.gov/pubs/fips/140-3/final)**: See the [Enable FIPS 140-3 level 1 compliance on a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode) documentation page for more information on FIPS 140-3 level 1 support on Looker (Google Cloud core).
  11. In the **Maintenance Window** section, you can optionally [specify the day of the week and the hour](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) in which Looker (Google Cloud core) schedules maintenance.

  12. In the **Deny Maintenance Period** section, you can optionally [specify a block of days](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#define_a_maintenance_deny_period_to_defer_maintenance) in which Looker (Google Cloud core) doesn't schedule maintenance. You cannot set a deny maintenance period if you are also enrolling the instance in the Rapid release channel or using the [Accelerated Security Patching (ASP) configuration flag](https://docs.cloud.google.com/looker/docs/looker-core-release-process#asp-flag) with the Regular release channel.

  13. In the **Gemini in Looker** section, you can optionally make [Gemini in Looker features](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini#gemini-feature-availability) available for the Looker (Google Cloud core) instance. To enable Gemini in Looker, select **Gemini** , and then select **Trusted Tester features**. When **Trusted Tester features** is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. You may request access to the non-public Trusted Tester capabilities through the [Gemini in Looker preview form](https://docs.google.com/forms/d/e/1FAIpQLSefBWbxchQFyZB9EOOcRxYTRi-16TezwRExW-x-XJRfeklCiA/viewform) on a per-user basis. You must enable this setting to use Gemini during the pre-GA preview. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview)To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.

  14. In the **Knowledge Catalog integration** section, you can optionally select the **Opt out of Knowledge Catalog integration** checkbox if you don't want Looker (Google Cloud core) to [integrate with Knowledge Catalog](https://docs.cloud.google.com/looker/docs/looker-core-dataplex). Looker (Google Cloud core) and Knowledge Catalog are integrated by default.

  15. Click **Create**.




###  gcloud 

  1. If you are using [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek), then [create the Looker service account](https://docs.cloud.google.com/looker/docs/looker-core-cmek#create_a_service_account) and follow the instructions for setting up CMEK first.
  2. Use the `gcloud looker instances create` command to create the instance:
         
         gcloud looker instances create INSTANCE_NAME \
         --project=PROJECT_ID \
         --region=REGION \
         --edition=EDITION \
         [--release-channel=RELEASE_CHANNEL]\
         --public-ip-enabled \
         --async
         

Replace the following:

     * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it isn't associated with the instance URL.
     * `PROJECT_ID`: the name of the Google Cloud project in which you are creating the Looker (Google Cloud core) instance.
     * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. Available regions are listed on the [Looker (Google Cloud core) locations](https://docs.cloud.google.com/looker/docs/looker-core-locations) documentation page. You cannot change the region once the instance has been created.
     * `EDITION`: the edition, environment type (production or [non-production](https://docs.cloud.google.com/looker/docs/looker-core-overview#staging_environments_and_testing)), and whether this is a [trial edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#trials) for the instance. Its available values are `core-standard-annual`, `core-enterprise-annual`, `core-embed-annual`, `nonprod-core-standard-annual`, `nonprod-core-enterprise-annual`, `nonprod-core-embed-annual`, `core-trial-standard`, `core-trial-enterprise`, and `core-trial-embed`. Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](https://docs.cloud.google.com/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
     * `RELEASE_CHANNEL`: the [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) for the instance. Available values are `rapid`, `regular`, and `no-channel`. The default during the preview is `no-channel`. If you don't include this flag in your `create` command, the instance will be created with the default channel. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

Also include these flags:

     * `--public-ip-enabled` is used to enable public secure connection.
     * `--async` is recommended when you're creating a Looker (Google Cloud core) instance.
  3. You can add more parameters to apply other instance settings: 
         
         [--maintenance-window-day=MAINTENANCE_WINDOW_DAY
               --maintenance-window-time=MAINTENANCE_WINDOW_TIME]
         [--deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
               --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
               --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME]
         [--kms-key=KMS_KEY_ID]
         [--accelerated-security-patch-enabled]
         [--no-accelerated-security-patch-enabled]
         [--fips-enabled]
         [--catalog-integration-enabled]
         [--no-catalog-integration-enabled]
         

Replace the following:

     * `MAINTENANCE_WINDOW_DAY`: must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the [Manage maintenance policies for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#maintenance_settings) documentation page for more information about maintenance window settings.
     * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC time in 24-hour format (for example, 13:00, 17:45).
     * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`. You cannot set a deny maintenance period if you are also enrolling the instance in the Rapid release channel or using the [Accelerated Security Patching (ASP) configuration flag](https://docs.cloud.google.com/looker/docs/looker-core-release-process#asp-flag) with the Regular release channel.
     * `KMS_KEY_ID`: must be the key that is created when setting up [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/looker/docs/looker-core-cmek#copy_or_write_down_the_kms_key_id_and_the_kms_keyring_id).

The following flags enable other settings:

     * `--accelerated-security-patch-enabled` and `--no-accelerated-security-patch-enabled`: Include one of these flags if your instance is on the `regular` channel and you want to receive or disable security patches bi-weekly. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).
     * `--fips-enabled`: [Enable FIPS 140-3 level 1 compliance](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode).
     * Replace the `--catalog-integration-enabled` flag with the `--no-catalog-integration-enabled` flag to disable the [ Looker (Google Cloud core) and Knowledge Catalog integration](https://docs.cloud.google.com/looker/docs/looker-core-dataplex).

**Tip:** You must have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) for the proper edition type to create an instance. If you don't have quota, [contact Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to allocate quota to your project. For more troubleshooting help, see the [Troubleshooting Looker (Google Cloud core) instance creation failures](https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-instance-creation-troubleshooting) documentation page.

### Terraform

Use the following [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/looker_instance#example-usage---looker-instance-basic) to provision a **Standard** Looker (Google Cloud core) instance with basic functionality:
    
    
    # Creates a Standard edition Looker (Google Cloud core) instance with basic functionality enabled.
    resource "google_looker_instance" "main" {
      name             = "my-instance"
      platform_edition = "LOOKER_CORE_STANDARD"
      region           = "us-central1"
      oauth_config {
        client_id     = "my-client-id"
        client_secret = "my-client-secret"
      }
    }

Use the following [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/looker_instance#example-usage---looker-instance-full) to provision a **Standard** Looker (Google Cloud core) instance with additional settings applied:
    
    
    # Creates a Standard edition Looker (Google Cloud core) instance with full functionality enabled.
    
    resource "google_looker_instance" "main" {
      name              = "my-instance"
      platform_edition  = "LOOKER_CORE_STANDARD"
      region            = "us-central1"
      public_ip_enabled = true
      admin_settings {
        allowed_email_domains = ["google.com"]
      }
      // User metadata config is only available when platform edition is LOOKER_CORE_STANDARD.
      user_metadata {
        additional_developer_user_count = 10
        additional_standard_user_count  = 10
        additional_viewer_user_count    = 10
      }
      maintenance_window {
        day_of_week = "THURSDAY"
        start_time {
          hours   = 22
          minutes = 0
          seconds = 0
          nanos   = 0
        }
      }
      deny_maintenance_period {
        start_date {
          year  = 2050
          month = 1
          day   = 1
        }
        end_date {
          year  = 2050
          month = 2
          day   = 1
        }
        time {
          hours   = 10
          minutes = 0
          seconds = 0
          nanos   = 0
        }
      }
      oauth_config {
        client_id     = "my-client-id"
        client_secret = "my-client-secret"
      }
    }
    

**Important:** To run the following Terraform resource, you must have the [Cloud KMS Admin (`roles/cloudkms.admin`) IAM role](https://docs.cloud.google.com/kms/docs/create-key-ring#required-roles) on the project in which you are creating the Looker (Google Cloud core) instance. See more about encryption keys on the [Enable CMEK for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek#create_a_key_ring_and_key) documentation page.

Use the following [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/looker_instance#example-usage---looker-instance-enterprise-full) to provision an **Enterprise** Looker (Google Cloud core) instance with a private network connection:
    
    
    # Creates an Enterprise edition Looker (Google Cloud core) instance with full, Private IP functionality.
    resource "google_looker_instance" "main" {
      name               = "my-instance"
      platform_edition   = "LOOKER_CORE_ENTERPRISE_ANNUAL"
      region             = "us-central1"
      private_ip_enabled = true
      public_ip_enabled  = false
      reserved_range     = google_compute_global_address.main.name
      consumer_network   = data.google_compute_network.main.id
      admin_settings {
        allowed_email_domains = ["google.com"]
      }
      encryption_config {
        kms_key_name = google_kms_crypto_key.main.id
      }
      maintenance_window {
        day_of_week = "THURSDAY"
        start_time {
          hours   = 22
          minutes = 0
          seconds = 0
          nanos   = 0
        }
      }
      deny_maintenance_period {
        start_date {
          year  = 2050
          month = 1
          day   = 1
        }
        end_date {
          year  = 2050
          month = 2
          day   = 1
        }
        time {
          hours   = 10
          minutes = 0
          seconds = 0
          nanos   = 0
        }
      }
      oauth_config {
        client_id     = "my-client-id"
        client_secret = "my-client-secret"
      }
      depends_on = [
        google_service_networking_connection.main,
        google_kms_crypto_key.main
      ]
    }
    
    resource "google_kms_key_ring" "main" {
      name     = "keyring-example"
      location = "us-central1"
    }
    
    resource "google_kms_crypto_key" "main" {
      name     = "crypto-key-example"
      key_ring = google_kms_key_ring.main.id
    }
    
    resource "google_service_networking_connection" "main" {
      network                 = data.google_compute_network.main.id
      service                 = "servicenetworking.googleapis.com"
      reserved_peering_ranges = [google_compute_global_address.main.name]
    }
    
    resource "google_compute_global_address" "main" {
      name          = "looker-range"
      purpose       = "VPC_PEERING"
      address_type  = "INTERNAL"
      prefix_length = 20
      network       = data.google_compute_network.main.id
    }
    
    data "google_project" "main" {}
    
    data "google_compute_network" "main" {
      name = "default"
    }
    
    resource "google_kms_crypto_key_iam_member" "main" {
      crypto_key_id = google_kms_crypto_key.main.id
      role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
      member        = "serviceAccount:service-${data.google_project.main.number}@gcp-sa-looker.iam.gserviceaccount.com"
    }

**Note:** If you create a private connections instance, a URL won't appear on the **Instances** page. To access the instance, you need to create a [custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain).

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Instance creation cannot be paused or terminated once it has been initiated. When your Terraform resource has been provisioned successfully, your terminal will print the following message:
    
    
    Creation complete after XmXs [id=projects/PROJECT-ID/locations/REGION/instances/my-instance-randomly-generated-name]
    
    
    
    Apply complete! Resources: X added, X changed, X destroyed.
    

As the instance is being created, you can view its status on the [**Instances**](https://docs.cloud.google.com/looker/docs/looker-core-view-console) page within the console. You can also see your instance creation activity by clicking on the notifications icon in the Google Cloud console menu.

**Note:** If your `gcp.restrictTLSCipherSuites` organization policy constraint doesn't include any cipher suites that are in the [MODERN SSL policy profile](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#defining_an_ssl_policy), Looker will return an error, and instance creation will fail. Update the policy to resolve the error and create the instance. See the [Restrict TLS cipher suites](https://docs.cloud.google.com/looker/docs/looker-core-tls-cipher-suites#policy_violations) documentation page for more information.

Once the public secure connection instance is created, the instance's public URL will appear in the **Instance URL** column of the **Instances** page.

After the instance is created, you can view the instance by navigating to the instance URL, which will be shown on the **Instances** page, and [sign in with Google](https://support.google.com/accounts/answer/12629094?&sjid=8591543582681818450-NC).

You can edit instance settings, including adding manual OAuth credentials if you want them, by visiting the [instance details page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#instance_tabs) and [clicking **Edit**](https://docs.cloud.google.com/looker/docs/looker-core-view-console#config_edit).

## Troubleshooting instance creation issues

For troubleshooting help, see the [Troubleshooting Looker (Google Cloud core) instance creation failures](https://docs.cloud.google.com/looker/docs/looker-core-instance-creation-troubleshooting) documentation page.

## What's next

  * [Set up and access a custom domain for a public secure connections Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain)
  * [Connect Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects)
  * [Prepare a Looker (Google Cloud core) instance for users](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
