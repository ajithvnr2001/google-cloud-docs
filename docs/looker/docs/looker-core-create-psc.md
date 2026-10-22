---
url: https://docs.cloud.google.com/looker/docs/looker-core-create-psc/
title: Create a Looker (Google Cloud core) Private Service Connect instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:25.346066+00:00
---

# Create a Looker (Google Cloud core) Private Service Connect instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-create-psc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create a Looker (Google Cloud core) Private Service Connect instance Stay organized with collections  Save and categorize content based on your preferences. 

Create a Looker (Google Cloud core) instance with [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) enabled to ensure secure and private connections for your production or non-production environments. You can set up your instance by using the Google Cloud console, the gcloud CLI, or Terraform. For other connection options, refer to the documentation for [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) or [private services access](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip).

Private Service Connect can be enabled for a Looker (Google Cloud core) instance that meets the following criteria:

  * The Looker (Google Cloud core) instance must be new. Private Service Connect can be enabled only at the time of instance creation.
  * The [instance edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#looker_\(google_cloud_core\)_editions) must be Enterprise (`core-enterprise-annual`) or Embed (`core-embed-annual`).



## Before you begin

  1. [Work with Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to ensure that your [annual contract](https://cloud.google.com/looker/pricing) is completed and that you have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) allocated in your project.
  2. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console).
  3. In the Google Cloud console, on the project selector page, select the project where you want to create the Private Service Connect instance. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Enable the Looker API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=looker.googleapis.com)

**Caution:** Disabling the Looker API after instance creation will affect Looker (Google Cloud core) features. For example, disabling the API will disable the ability to create [instance backups](https://docs.cloud.google.com/looker/docs/looker-core-backup-restore).
  5. [Set up an OAuth client and create authorization credentials](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth). The OAuth client lets you authenticate and access the instance. You must set up OAuth to create a Looker (Google Cloud core) instance, even if you are using a different [authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication) to authenticate users into your instance.
  6. If you want to use [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) or [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/looker/docs/looker-core-cmek) with the Looker (Google Cloud core) instance that you are creating, additional setup is required prior to instance creation. Additional edition and network configuration may also be required during instance creation.

**Important:** Once Private Service Connect is enabled on a Looker (Google Cloud core) instance, you cannot switch that instance to use public secure connection or [private connections (private services access) connectivity](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip).

### Required roles

To get the permissions that you need to create a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project the instance will reside in. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to create a Looker (Google Cloud core) instance. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

You may also need additional IAM roles to set up [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) or [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/looker/docs/looker-core-cmek). Visit the documentation pages for those features to learn more.

## Create a Private Service Connect instance

### console

  1. Navigate to the Looker (Google Cloud core) product page from your project in the Google Cloud console. If you have already created a Looker (Google Cloud core) instance within this project, the **Instances** page will open. 

[Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker)

  2. Click **CREATE INSTANCE**.
  3. In the **Instance name** section, provide a name for your Looker (Google Cloud core) instance. The instance name isn't associated with the URL of the Looker (Google Cloud core) instance once it is created. The instance name cannot be changed after instance creation.
  4. In the **Region** section, select the appropriate option from the drop-down menu to host your Looker (Google Cloud core) instance. Select the region that matches the region in the subscription contract, which is where the [quota for your project](https://docs.cloud.google.com/docs/quotas/view-manage) is allocated. Available regions are listed on the [Looker (Google Cloud core) locations](https://docs.cloud.google.com/looker/docs/looker-core-locations) documentation page.

You cannot change the region once the instance has been created.

  5. In the **Edition** section, choose an **Enterprise** or **Embed** (production or non-production) edition option. The edition type affects some of the [features that are available](https://docs.cloud.google.com/looker/docs/looker-core-edition-types) for the instance. Make sure that you choose the same edition type as listed in your [annual contract](https://cloud.google.com/looker/pricing) and that you have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) allocated for that edition type.

     * **Enterprise** : Looker (Google Cloud core) platform with enhanced security features for addressing a wide variety of internal BI and analytics use cases
     * **Embed** : Looker (Google Cloud core) platform for deploying and maintaining reliable external analytics and custom applications at scale
     * Non-production editions: If you want a staging and testing environment, select one of the non-production editions. For more information, see the [Non-production instances](https://docs.cloud.google.com/looker/docs/looker-core-overview#staging_environments_and_testing) documentation.
     * Trial editions: A [trial edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#trials) has the same feature support as its corresponding production edition, with the exception that trial editions are valid for 90 days.

Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](https://docs.cloud.google.com/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.

**Tip:** If your project doesn't have quota, you won't be able to select an edition type. [Contact Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to allocate quota to your project. For more troubleshooting help, see the [Troubleshooting Looker (Google Cloud core) instance creation failures](https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-instance-creation-troubleshooting) documentation page.
  6. In the **Customize your instance** section, click **Show configuration options** to display a group of additional settings that you can customize for the instance.

  7. In the **Connections** section, under **Instance IP assignment** , choose either **Use hybrid connections** or **Use private connections**. The type of network connection that you select impacts the [Looker features that are available](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences#feature_compatibility_by_edition_type) to the instance. The following network connection options are available:

     * **Use public secure connections** : Looker will have a public URL and use a public network for outbound connections.
     * **Use hybrid connections** : Looker will have a public URL and use PSC endpoints for outbound connections.

**Note:** If hybrid connections are assigned at the time of instance creation, you can change to [using private connections later](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings).
     * **Use private connections** : Assigns an internal, customer-defined IP address that is accessible in a [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) for ingress. To communicate to VPC and on-premises or multi-cloud workloads, you must deploy service attachments for egress traffic. If you want to use VPC Service Controls, you must select **Use private connections**.

     * If you are creating an instance that uses only private connections, set at least one allowed VPC that will be granted [inbound connections](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#psc-access) into the instance. Under **Configure inbound connections** , in the **Project 1** field, select the project in which this network was created.

To add additional inbound connections, click **Add Item** to add each VPC. In the **Project X** field, select the project in which the network was created. In the **Network** drop-down menu, select the network.

If you select **Use hybrid connections** in the **Connections** section, the **Configure inbound connections** section doesn't appear. You can set up access to the instance through the instance's web URL.

     * In the **Local FQDN** section, specify one or more service attachments that expose an endpoint for outbound connections that Looker can connect to. In the **Local FQDN 1** field, enter the fully qualified domain name of the service, and in the **Target Service Attachment URI 1** field, enter the full service attachment URI for the external service.

To add additional service attachments, click **Add Item** to add each service attachment. In the **Local FQDN** field, enter the fully qualified domain name of the service. In the **Target Service Attachment URI** field, enter the full service attachment URI for the external service.

     * In the **Encryption** section, you can select the type of encryption to use on your instance. The following encryption options are available:

       * [**Google-managed encryption key**](https://cloud.google.com/docs/security/encryption-at-rest/default-encryption): This option is the default and doesn't require any additional configuration.
       * [**Customer-managed encryption key (CMEK)**](https://docs.cloud.google.com/kms/docs/cmek): See the [Using customer-managed encryption keys with Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek#create_a_instance_with_cmek) documentation page for more information on CMEK and how to configure it during instance creation. The type of encryption cannot be changed after instance creation.
       * **Enable[FIPS 140-3 level 1 Validated Encryption](https://csrc.nist.gov/pubs/fips/140-3/final)**: See the [Enable FIPS 140-3 level 1 compliance on a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode) documentation page for more information on FIPS 140-3 level 1 support on Looker (Google Cloud core).
     * In the **Release Channel** section, select the [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) that best fits your needs:

       * **Rapid** : Earliest access to features. Recommended for non-production instances.
       * **Regular** : Balanced stability. Recommended for production instances. 
       * **No channel** : No release channel. During the preview, No channel is the default.
**Note:** The release channels feature is in [preview](https://cloud.google.com/products#product-launch-stages).
     * In the **Maintenance Window** section, you can optionally [specify the day of the week and the hour](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour. By default, the **Preferred Window** option in the **Maintenance Window** is set to **Any window**.

     * In the **Deny Maintenance Period** section, you can optionally [specify a block of days](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#define_a_maintenance_deny_period_to_defer_maintenance) on which Looker (Google Cloud core) doesn't schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods. You cannot set a deny maintenance period if you are also enrolling the instance in the Rapid release channel or using the [Accelerated Security Patching (ASP) configuration flag](https://docs.cloud.google.com/looker/docs/looker-core-release-process#asp-flag) with the Regular release channel.

     * In the **Gemini in Looker** section, you can optionally make [Gemini in Looker features](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini#gemini-feature-availability) available for the Looker (Google Cloud core) instance. To enable Gemini in Looker, select **Gemini** , and then select **Trusted Tester features**. When **Trusted Tester features** is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. You may request access to the non-public Trusted Tester capabilities through the [Gemini in Looker preview form](https://docs.google.com/forms/d/e/1FAIpQLSefBWbxchQFyZB9EOOcRxYTRi-16TezwRExW-x-XJRfeklCiA/viewform) on a per-user basis. You must enable this setting to use Gemini during the pre-GA preview. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview)To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.

     * In the **Knowledge Catalog integration** section, you can optionally select the **Opt out of Knowledge Catalog integration** checkbox if you want Looker (Google Cloud core) to disable the [integration with Knowledge Catalog](https://docs.cloud.google.com/looker/docs/looker-core-dataplex). The integration between Looker (Google Cloud core) and Knowledge Catalog is enabled by default.

**Note:** The integration between Looker (Google Cloud core) and Knowledge Catalog is in preview. Pre-GA products and features are available "as is" and might have limited support.
     * Click **Create**.




### gcloud

To create a Private Service Connect instance, run the `gcloud looker instances create` command with all the following flags:
    
    
    
    gcloud looker instances create INSTANCE_NAME \
    --psc-enabled \
    --oauth-client-id=OAUTH_CLIENT_ID \
    --oauth-client-secret=OAUTH_CLIENT_SECRET \
    --region=REGION \
    --edition=EDITION \
    [--psc-allowed-vpcs=ALLOWED_VPC,ADDITIONAL_ALLOWED_VPCS]\
    [--no-public-ip-enabled]\
    [--public-ip-enabled]\
    [--release-channel=RELEASE_CHANNEL]\
    --async
    
    

Replace the following:

  * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it is not associated with the instance URL.
  * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret). After the instance has been created, [enter the instance's URL in the **Authorized redirect URIs** section of the OAuth client](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client).
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. Available regions are listed on the [Looker (Google Cloud core) locations](https://docs.cloud.google.com/looker/docs/looker-core-locations) documentation page.
  * `EDITION`: the edition, environment type (production or [non-production](https://docs.cloud.google.com/looker/docs/looker-core-overview#staging_environments_and_testing)), and whether this is a [trial edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#trials) for the instance. Its available values are `core-enterprise-annual`, `core-embed-annual`, `nonprod-core-enterprise-annual`, `nonprod-core-embed-annual`, `core-trial-enterprise`, and `core-trial-embed`. Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](https://docs.cloud.google.com/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
  * `ALLOWED_VPC`: If you are creating an instance that uses only private connections, list a VPC that will be allowed [inbound](https://docs.cloud.google.com/looker/docs/glossary#northbound-traffic) (ingress) access into Looker (Google Cloud core). To access the instance from outside the VPC that the instance is located in, you must list at least one VPC. Specify a VPC using one of the following formats:

    * `projects/{project}/global/networks/{network}`
    * `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`

If you are creating an instance that uses hybrid connections, you don't need to set an allowed VPC.

  * `ADDITIONAL_ALLOWED_VPCS`: any additional VPCs to be allowed inbound access into Looker (Google Cloud core) can be added to the `--psc-allowed-vpcs` flag in a comma-separated list.

  * `RELEASE_CHANNEL`: the [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) for the instance. Available values are `rapid`, `regular`, and `no-channel`. The default during the preview is `no-channel`. If you don't include this flag in your `create` command, the instance will be created with the default channel. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).




You must also include **one** of the following flags to enable or disable public connections:

  * `--public-ip-enabled` enables public connections. If you enable public connections for the instance, incoming traffic will be routed through public connections, and outgoing traffic will be routed through Private Service Connect.
  * `--no-public-ip-enabled` disables public connections.

**Important:** When creating an instance using Google Cloud CLI, don't specify outbound (egress) connections, such as service attachments, in the `create` command. Specifying outbound connections at this point will cause the `create` operation to fail. Outbound connections must be specified after the instance has been created.

If you want, you can add more parameters to apply other instance settings:
    
    
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

  * `MAINTENANCE_WINDOW_DAY`: Must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the [Manage maintenance policies for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#maintenance_settings) documentation page for more information about maintenance window settings.
  * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: Must be in UTC time in 24-hour format (for example, `13:00`, `17:45`). You cannot set a deny maintenance period if you are also enrolling the instance in the Rapid release channel or using the [Accelerated Security Patching (ASP) configuration flag](https://docs.cloud.google.com/looker/docs/looker-core-release-process#asp-flag) with the Regular release channel. 
  * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: Must be in the format `YYYY-MM-DD`.
  * `KMS_KEY_ID`: Must be the key that is created when setting up [customer-managed encryption keys (CMEK).](https://docs.cloud.google.com/looker/docs/looker-core-cmek#copy_or_write_down_the_kms_key_id_and_the_kms_keyring_id)



The following flags enable other settings:

  * `--accelerated-security-patch-enabled` and `--no-accelerated-security-patch-enabled`: Include one of these flags if your instance is on the `regular` channel and you want to receive or disable security patches bi-weekly. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).
  * `--fips-enabled`: [enable FIPS 140-3 level 1 compliance](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode).
  * replace the `--catalog-integration-enabled` flag with the `--no-catalog-integration-enabled` flag to disable the [ Looker (Google Cloud core) and Knowledge Catalog integration](https://docs.cloud.google.com/looker/docs/looker-core-dataplex). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).



The process for creating a Private Service Connect instance differs from the process for creating a Looker (Google Cloud core) (private services access) instance in the following ways:

  * With Private Service Connect setup, the `--consumer-network` and `--reserved-range` flags are not necessary.
  * Private Service Connect instances require an additional flag: `--psc-enabled`.
  * The `--psc-allowed-vpcs` flag is a comma-separated list of VPCs. You can specify as many VPCs as you like in the list.

**Tip:** You must have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) for the proper edition type to create an instance. If you don't have quota, [contact Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to allocate quota to your project. For more troubleshooting help, see the [Troubleshooting Looker (Google Cloud core) instance creation failures](https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-instance-creation-troubleshooting) documentation page.

### Terraform

Use the following [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/looker_instance#example-usage---looker-instance-psc) to provision a [**Enterprise**](https://docs.cloud.google.com/looker/docs/looker-core-overview#enterprise_edition) Looker (Google Cloud core) instance that uses PSC:
    
    
    # Create an ENTERPRISE edition Looker (Google Cloud core) instance that has PSC enabled.
    resource "google_looker_instance" "default" {
      name               = "my-instance"
      platform_edition   = "LOOKER_CORE_ENTERPRISE_ANNUAL"
      region             = "us-central1"
      private_ip_enabled = false
      public_ip_enabled  = false
      psc_enabled        = true
      oauth_config {
        client_id     = "my-client-id"
        client_secret = "my-client-secret"
      }
      psc_config {
        # allowed_vpcs = ["projects/{project}/global/networks/{network}"]
        # (Optional) List of VPCs that are allowed ingress into the Looker instance. Set an allowed VPC if you are creating an instance that uses only private IP.
      }
    }

Enter values for the following:

  * `name`: a name for your Looker (Google Cloud core) instance; it is not associated with the instance URL.
  * `platform_edition`: the edition, environment type (production or [non-production](https://docs.cloud.google.com/looker/docs/looker-core-overview#staging_environments_and_testing)), and whether this is a [trial edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#trials) for the instance. Its possible values are `LOOKER_CORE_ENTERPRISE_ANNUAL`, `LOOKER_CORE_EMBED_ANNUAL`, `LOOKER_NONPROD_CORE_ENTERPRISE_ANNUAL`, `LOOKER_NONPROD_CORE_EMBED_ANNUAL`, `LOOKER_CORE_TRIAL_ENTERPRISE`, or `LOOKER_CORE_TRIAL_EMBED`. This example uses `LOOKER_CORE_ENTERPRISE_ANNUAL`. Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](https://docs.cloud.google.com/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
  * `region`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. This example uses `us-central1`. Available regions are listed on the [Looker (Google Cloud core) locations](https://docs.cloud.google.com/looker/docs/looker-core-locations) documentation page.
  * `client_id` and `client_secret`: the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret). After the instance has been created, [enter the instance's URL in the **Authorized redirect URIs** section of the OAuth client](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client).
  * `allowed_vpcs`: If you are creating an instance that uses only private connections, list a VPC that will be allowed [inbound](https://docs.cloud.google.com/looker/docs/glossary#northbound-traffic) (ingress) access into the Looker (Google Cloud core) instance. To access the instance from outside the VPC that the instance is located in, you must list at least one VPC. Specify a VPC using one of the following formats:

    * `projects/{project}/global/networks/{network}`
    * `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`

If you are creating an instance that uses hybrid connections, you don't need to set an allowed VPC. You can update and add additional VPC IPs later.

You will also need to update the instance to make outbound connections.

**Important:** When creating an instance using Terraform, don't define outbound (egress) connections, such as service attachments, in the create resource block. Specifying outbound connections at this point will cause instance creation to fail. Outbound connections must be specified after the instance has been created.



### Check the status of the instance

It takes approximately 40-60 minutes for the instance to be created.

### console

As the instance is being created, you can view its status on the [**Instances**](https://docs.cloud.google.com/looker/docs/looker-core-view-console) page within the console. You can also see your instance creation activity by clicking on the notifications icon in the Google Cloud console menu. On the **Details** page for the instance, its status will show **Active** once it's created.

### gcloud

To check the status, use the `gcloud looker instances describe` command:
    
    
    gcloud looker instances describe INSTANCE_NAME --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.



The instance is ready once it reaches the `ACTIVE` state.

**Important:** When you create a Private Service Connect instance where public connections are disabled, you **will not receive a URL** for the instance. You must set up a [custom domain](https://docs.cloud.google.com/looker/docs/looker-core-psc-access#create-custom-domain) and configure access to that domain. See the [Northbound access to a Looker (Google Cloud core) instance using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access) documentation page for more information about how to set up access to your Looker (Google Cloud core) (Private Service Connect) instance.

In addition, you can make other changes after instance creation by [editing the instance settings](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings).

## Configure inbound connections

Once your Looker (Google Cloud core) Private Service Connect instance has been created, you can configure inbound connections.

If you use hybrid connections in the Looker (Google Cloud core) instance, the instance can be accessed over [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain). If you chose to use only private connections in the Looker (Google Cloud core) instance, you must allow at least one VPC access to the instance. Complete the following steps to update the VPCs that have access to the instance. More than one VPC can have access to the instance.

### console

  1. On the **Instances** page, click the name of the instance for which you want to update the VPCs that are allowed inbound access.
  2. Click **Edit**.
  3. Expand the **Connections** section.
  4. Navigate to the **Configure inbound connections** section.
  5. Click **Add Item**. Then, select the project in which the VPC is located in the **Project** field, and select the network from the **Network** drop-down menu.
  6. To delete a VPC, click the **Delete item** trash icon that appears when you hold the pointer over the network.
  7. Click **Save**.



### gcloud

Use the `--psc-allowed-vpcs` flag to update the list of VPCs that have authorized inbound access into the instance.

When you update the allowed VPCs, you must specify the entire list that you want to be in effect after your update. For example, suppose VPC `ALLOWED_VPC_1` is already allowed, and you want to add VPC `ALLOWED_VPC_2`. To add VPC `ALLOWED_VPC_1` while making sure that VPC `ALLOWED_VPC_2` continues to be allowed, add the `--psc-allowed-vpcs` flag as follows:
    
    
    gcloud looker instances update INSTANCE_NAME \
    --psc-allowed-vpcs=ALLOWED_VPC_1,ALLOWED_VPC_2 --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `ALLOWED_VPC_1` and `ALLOWED_VPC_2`: the VPCs that will be allowed ingress into Looker (Google Cloud core). Specify each allowed VPC using one of the following formats: 
    * `projects/{project}/global/networks/{network}`
    * `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.



Once a VPC has inbound access to the instance, you can set up northbound connections through that VPC.

### Delete all allowed VPCs

To delete all allowed VPCs, run the following command:
    
    
    gcloud looker instances update MY_INSTANCE --clear-psc-allowed-vpcs \
    --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.



## Configure outbound connections

Once your Looker (Google Cloud core) Private Service Connect instance has been created, you can configure outbound (egress) connections to external services.

If you want to connect to an external service that uses the standard web protocol, HTTPS, with available ports 443 or 8443, you can use Looker (Google Cloud core)'s [controlled native egress](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#controlled-native-egress) and the [**Global FQDN**](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#global-fqdn) setting to set up your connection. However, if the external service uses a different protocol, that external service must be [published using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#set_up_for_external_services) to enable it to connect to your Looker (Google Cloud core) instance using [**Local FQDN**](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#local-fqdn).

The following sections describe how to connect to the Looker Marketplace, an external domain using **Global FQDN** , or published services using **Local FQDN**.

### Connect to the Looker Marketplace

Looker (Google Cloud core) can use HTTPS and a [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) to connect directly to the [Looker Marketplace](https://marketplace.looker.com/). Connecting to the Marketplace also allows egress to github.com.

To connect to Marketplace, complete the following steps:

### console

  1. On the **Instances** page, click the name of the instance for which you want to enable [outbound](https://docs.cloud.google.com/looker/docs/glossary#southbound-traffic) (egress) connections.
  2. Click **Edit**.
  3. Expand the **Connections** section.
  4. Navigate to the **Configure outbound connections** section.
  5. Select the **Enable Looker to connect to external services** checkbox.
  6. Select the **Enable connection to Looker Marketplace** checkbox.
  7. Click **Confirm** on the dialog explaining that connecting to Marketplace allows egress to github.com.
  8. Click **Save**.



### Connect to an external domain using **Global FQDN**

Looker (Google Cloud core) can use HTTPS and a [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) to connect to an external, public domain with the **Global FQDN** setting. The connection is made using HTTPS. Port 443 must be open in the external service; a service attachment URI is not required.

This setting is also used to allow traffic to Google APIs that are not supported by the [restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services). For example, to allow your Looker (Google Cloud core) instance to connect to the Google Maps API, add `maps.googleapis.com` as a Global FQDN.

You can identify the public egress IP addresses that are used by your Looker (Google Cloud core) instance by navigating to the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) of the **Instances** page for your Looker (Google Cloud core) instance in the Google Cloud console. The IP addresses that are used for internet egress traffic appear in the **Egress IPs** field in the **Controlled Egress Configuration** section. The IP addresses are unique to your Looker (Google Cloud core) instance. These IP addresses are allocated using the Secure Web Proxy, and they are dynamic and may change without warning.

**Note:** We recommend using controlled native egress only with remote endpoints that allow all incoming network traffic without IP-based restrictions.

To connect to an external service using global FQDN, complete the following steps:

### console

  1. On the **Instances** page, click the name of the instance for which you want to enable [outbound](https://docs.cloud.google.com/looker/docs/glossary#southbound-traffic) (egress) connections.
  2. Click **Edit**.
  3. Expand the **Connections** section.
  4. Navigate to the **Configure outbound connections** section.
  5. Select the **Enable Looker to connect to external services** checkbox.
  6. In the **Global FQDN** section, enter the fully-qualified domain name you want to connect to.
  7. Click **Add Item** if you want to add another domain.
  8. Click **Save**.



### Connect to published services using **Local FQDN**

Looker (Google Cloud core) can use Private Service Connect to connect to a [published service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) with the **Local FQDN** setting.

First you need to publish the external service using Private Service Connect and obtain the service attachment URI for the service. Next you need to update the **Local FQDN** setting in the Google Cloud console.

#### Publish external services with Private Service Connect

Follow the [instructions for publishing services by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) for any service that you want to publish.

Services can be published with [automatic approval](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service-auto) or with [explicit approval](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service-explicit). If you choose to publish with explicit approval, you must configure the service attachment as follows:

  * Set your service attachment allowlist to use projects (not networks).
  * Add the Looker tenant project ID to the allowlist.



You can find your Looker tenant project ID after your instance has been created by running the following command:
    
    
    gcloud looker instances describe INSTANCE_NAME --region=REGION--format=json
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.



In the command output, the `looker_service_attachment_uri` field will contain your Looker tenant project ID. It will have the following format: `projects/{Looker tenant project ID}/regions/…`

##### Service attachment URI

When you update your Looker (Google Cloud core) instance in the Google Cloud console to connect to your service, you'll need the full service attachment URI for the external service. The URI will be specified as follows, using the project, region, and name that you used to create the service attachment:
    
    
    projects/{project}/regions/{region}/serviceAttachments/{name}
    

#### Update the **Local FQDN** setting in the Google Cloud console

### console

  1. On the **Instances** page, click the name of the instance for which you want to enable [outbound](https://docs.cloud.google.com/looker/docs/glossary#southbound-traffic) (egress) connections.
  2. Click **Edit**.
  3. Expand the **Connections** section.
  4. Navigate to the **Local FQDN** section.
  5. To edit an existing service attachment, update the fully qualified domain name of the service in the **Local FQDN** field and the [service attachment URI](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#service_attachment_uri) in the **Target Service Attachment URI** field.
  6. To add a new service attachment, click **Add Item**. Next, enter the fully qualified domain name of the service in the **Local FQDN** field and the service attachment URI in the **Target Service Attachment URI** field.
  7. Click **Save**.

**Note:** When connecting Looker (Google Cloud core) to a database, ensure that the name given in the **Local FQDN** field and the name given in the [**Host** field](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#hostname) of the **Connect your database to Looker** page within Looker (Google Cloud core) match exactly.

### gcloud

Use `--psc-service-attachment` flags to enable [outbound](https://docs.cloud.google.com/looker/docs/glossary#southbound-traffic) (egress) connections to external services for which you have already set up Private Service Connect:
    
    
    gcloud looker instances update INSTANCE_NAME \
    --psc-service-attachment  domain=DOMAIN_1,attachment=SERVICE_ATTACHMENT_URI_1 \
    --psc-service-attachment domain=DOMAIN_2,attachment=SERVICE_ATTACHMENT_URI_2 \
    --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `DOMAIN_1` and `DOMAIN_2`: If you are connecting to a public service, use the service's domain name. If you are connecting to a private service, use your choice of a fully qualified domain name. The following restrictions apply to the domain name:

  * Each outbound connection supports a single domain.

  * The domain name must consist of at least three parts. For example, `mydomain.github.com` is acceptable, but `github.com` is not acceptable.

  * The last part of the name cannot be any the following:

    * `googleapis.com`
    * `google.com`
    * `gcr.io`
    * `pkg.dev`

When you set up a connection to your service from within your Looker (Google Cloud core) instance, use this domain as the alias for your service.

  * `SERVICE_ATTACHMENT_1` and `SERVICE_ATTACHMENT_2`: the full service attachment URI for the published service you are connecting to. Each service attachment URI can be accessed by a single domain.

  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.




#### Include all connections that should be enabled

Each time you run an update command with `--psc-service-attachment` flags, you must include every connection that you want to be enabled, including connections that were already enabled previously. For example, suppose you have previously connected an instance called `my-instance` to the `www.cloud.com` domain as follows:
    
    
    gcloud looker instances update my-instance --psc-service-attachment \
    domain=www.cloud.com,attachment=projects/123/regions/us-central1/serviceAttachment/cloud
    

Running the following command to add a new `www.me.com` connection would delete the `www.cloud.com` connection:
    
    
    gcloud looker instances update my-instance --psc-service-attachment \
    domain=www.me.com,attachment=projects/123/regions/us-central1/serviceAttachment/my-sa
    

To prevent deletion of the `www.cloud.com`connection when you add the new `www.me.com` connection, include a separate `psc-service-attachment` flag for both the existing connection and the new connection within the update command as follows:
    
    
    gcloud looker instances update my-instance --psc-service-attachment \
    domain=www.cloud.com,attachment=projects/123/regions/us-central1/serviceAttachment/cloud \
    --psc-service-attachment domain=www.me.com,attachment=projects/123/regions/us-central1/serviceAttachment/my-sa
    

### Terraform

Use the following Terraform resource to update your Looker (Google Cloud core) instance to enable [outbound](https://docs.cloud.google.com/looker/docs/glossary#southbound-traffic) (egress) connections to external services that you have already published with Private Service Connect:
    
    
    service_attachments = [{local_fqdn: "www.local-fqdn.com" target_service_attachment_uri: "projects/{project}/regions/{region}/serviceAttachments/{name}}]
    

Enter values for the following:

  * `local_fqdn`: the fully qualified domain name of the published service.
  * `target_service_attachment_uri`: the full service attachment URI for the published service you are connecting to. Each service attachment URI can be accessed by a single domain.



If you are connecting to a non-Google managed service in a region other than the region where your Looker (Google Cloud core) instance is located, [enable global access](https://docs.cloud.google.com/vpc/docs/manage-endpoints-published-services#enable-global-access) on the producer load balancer.

### Check outbound connection status

You can check the status of your outbound (egress) connections through Google Cloud CLI or in the console.

### console

View the connection status on the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) of the instance configuration page in the console. The **PSC Configuration** fields show the statuses for each type of connection.

### gcloud

Run the `gcloud looker instances describe --format=json` command to check outbound connection status. Each service attachment should be populated with a `connection_status` field.

**Note:** The connection status is updated every five minutes. If you recently updated your service attachments, this field may be stale.**Caution:** You may receive an error or a connection status that doesn't progress past **Pending** if you have not [set allowed VPCs](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#create_instance) through the **Allowed VPCs** field in the console or the `--psc-allowed-vpcs` flag in the `gcloud` command.

#### Troubleshoot outbound connections

If you encounter a **Rejected** connection status when you're configuring a service attachment for outbound connections (for example, when you're connecting to your Git repository or database), check the producer organization policies on the project or organization that's hosting the service attachment. The `compute.restrictPrivateServiceConnectConsumer` list constraint might be preventing the connection. Ensure that the organization, folder, or project that's associated with your Looker (Google Cloud core) instance's network connection is included in the allowed values for this policy on the producer side. See the [producer organization policies](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-producers#producer-org-policies) documentation for more details.

#### Delete all outbound connections

To delete all outbound (egress) connections, run the following command:
    
    
    gcloud looker instances update MY_INSTANCE --clear-psc-service-attachments \
    --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.



## Northbound access to your instance

After the Looker (Google Cloud core) (Private Service Connect) instance is created, you can set up inbound access to allow your users to access the instance.

If you chose hybrid connections when setting up the instance, you can set up inbound access through the web URL for the instance. That URL can be found on the **Instances** page of the Google Cloud console, or the **Custom domain** tab of the instance details page, if you set up a custom domain. You can [set up an IP allowlist](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist) to restrict inbound connections to traffic from certain IP addresses.

If you selected private connections when setting up the instance, you can set up inbound access to the instance from another VPC network by following the [instructions for creating a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint). Follow these guidelines when creating the endpoint:

  * Make sure that the network is allowed inbound access to your Looker (Google Cloud core) instance by adding it to the allowed VPC's list.
  * Set the **Target service** field (if using the Google Cloud console) or the `SERVICE_ATTACHMENT` variable (if using Google Cloud CLI or the Looker API) to the Looker service attachment URI, which you can find by checking the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) on the instance configuration page of the console or by running the following command:
        
        gcloud looker instances describe INSTANCE_NAME --region=REGION--format=json

Replace the following:

    * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
    * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.
**Note:** Ensure that you're using the updated service attachment URI by following the instructions on the [Migrating Private Service Connect connections to the new service attachment URI](https://docs.cloud.google.com/looker/docs/looker-core-psc-migration) documentation page.
  * You can use any subnet that is hosted in the same region as the Looker (Google Cloud core) instance.

  * Global access lets you access your Looker (Google Cloud core) instance from any region. The following bullets explain whether and how you can enable global access:

    * If you're using the legacy service attachment URI, global access isn't supported.
    * If you're using the [new enhanced service attachment URI](https://docs.cloud.google.com/looker/docs/looker-core-psc-migration#identifying_your_service_attachment_uri), you can enable global access one of two ways: 
      * If you're using a Private Service Connect network endpoint group (NEG), you can enable global access on the [load balancer front end](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access).
      * Otherwise, you can enable global access [on the Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#specifications-global-access).



### Create a custom domain for a Private Service Connect instance

If you chose hybrid connections when setting up the instance, follow the instructions on the [Set up a custom domain for a Looker (Google Cloud core) instance that uses public connections](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) documentation page to set up a custom domain.

## Troubleshooting instance creation issues

For troubleshooting help, see the [Troubleshooting Looker (Google Cloud core) instance creation failures](https://docs.cloud.google.com/looker/docs/looker-core-instance-creation-troubleshooting) documentation page.

## What's next

  * If you chose only private connections when setting up the instance, follow the instructions on the [Private inbound access to a Looker (Google Cloud core) instance using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access) documentation page to set up a custom domain.
  * If you are using hybrid connections, [set up an IP allowlist](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist) to restrict inbound traffic to certain IP addresses.
  * You can use Private Service Connect to [set up public access over the internet](https://docs.cloud.google.com/looker/docs/looker-core-psc-access-public).
  * Alternatively, you can use Private Service Connect to [set up private inbound access](https://docs.cloud.google.com/looker/docs/looker-core-psc-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
