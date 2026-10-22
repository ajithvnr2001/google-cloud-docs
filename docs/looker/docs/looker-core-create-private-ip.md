---
url: https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip/
title: Create a private connections (private services access) Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:44.442659+00:00
---

# Create a private connections (private services access) Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create a private connections (private services access) Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** For instructions on how to create a public secure connections instance, see the [Create a public secure connections Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) documentation page. For instructions on how to create a Looker (Google Cloud core) Private Service Connect instance, see the [Create a Looker (Google Cloud core) Private Service Connect instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc) documentation page.

You can configure a Looker (Google Cloud core) production or [non-production instance](https://docs.cloud.google.com/looker/docs/looker-core-overview#staging_environments_and_testing) to use [private connections with private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa).

Using private services access, your Looker (Google Cloud core) instance communicates directly with other resources in your Virtual Private Cloud (VPC) without traversing the public internet or using external IP addresses. This configuration limits attack vectors, prevents inbound traffic from the public internet, and reduces network latency.

Private connectivity enables the use of features such as [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc). However, private connections aren't compatible with all Looker (Google Cloud core) features. For more information, see the [feature compatibility](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_connection_type) table.

Looker (Google Cloud core) supports private connections (PSA) for **Enterprise** or **Embed** [instance editions](https://docs.cloud.google.com/looker/docs/looker-core-overview#editions).

## Required roles and permissions

To set up a private connections (PSA) instance, you must have the following IAM permissions:

  1. To create a Looker (Google Cloud core) instance, you must have the [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.Admin`) role.
  2. To get the permissions that you need to create allocated IP address ranges and manage private connections, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create allocated IP address ranges and manage private connections. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create allocated IP address ranges and manage private connections:

     * See available networks in the **Network** drop-down: 
       * `compute.addresses.list`
       * `compute.globalAddresses.list`
       * `compute.networks.list`
       * `compute.globalAddresses.list`
     * Create a new VPC network: 
       * `compute.addresses.create`
       * `compute.globalAddresses.create`
       * `serviceusage.services.enable`
     * Allocate a private IP range and set up a private services access connection: `compute.networks.addPeering`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to create allocated IP address ranges and manage private connections. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

If you are using a private network that has already been set up, you don't need these permissions.




You may also need additional IAM roles to set up VPC Service Controls or customer-managed encryption keys (CMEK). Learn more by visiting the [VPC Service Controls support for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) or the [Enable CMEK for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek) documentation pages for those features.

You may also need additional IAM roles to set up Workforce Identity Federation, VPC Service Controls, or customer-managed encryption keys (CMEK). Learn more by visiting the [Use Workforce Identity Federation for Looker (Google Cloud core) user authentication](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity), [VPC Service Controls support for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc), or [Enable CMEK for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek) documentation pages for those features.

## Before you begin

  1. [Work with Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to ensure that your [annual contract](https://cloud.google.com/looker/pricing) is completed and that you have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) allocated in your project.
  2. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console).
  3. In the Google Cloud console, on the project selector page, [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) or navigate to an existing one in which you want to create the Looker (Google Cloud core) instance. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Enable the Looker API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=looker.googleapis.com)

**Caution:** Disabling the Looker API after instance creation will affect Looker (Google Cloud core) features. For example, disabling the API will disable the ability to create [instance backups](https://docs.cloud.google.com/looker/docs/looker-core-backup-restore).
  5. Enable the [Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicenetworking.googleapis.com)

  6. Enable the [Compute Engine API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When you enable the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  7. [Set up an OAuth client and create authorization credentials](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth). The OAuth client lets you authenticate and access the instance. You must set up OAuth to create a Looker (Google Cloud core) instance, even if you are using a different [authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication) to authenticate users into your instance.



## Create and configure a VPC network

**Important:** If you are creating a Looker (Google Cloud core) instance in a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), follow the steps in the Creating an instance in a Shared VPC section.

Before you can create a private connection, you must first create and configure a Virtual Private Cloud (VPC) network. Looker (Google Cloud core) supports multiple private connections (PSA) instances in the same VPC, either in the same region or in different regions.

  1. [Create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) in your project. Alternatively, if you are using a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) instead of creating a new VPC network, complete the steps in the following section, Creating an instance in a Shared VPC, in addition to completing the remaining steps in this section for the Shared VPC.
  2. [Allocate an IPv4 IP range (CIDR block)](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#procedure) in your VPC for a private services access connection to Looker (Google Cloud core).
     * Before allocating your range, consider the [constraints](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#considerations).
     * When [setting the IP address range size](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#ip_address_range_size), be aware that the minimum size is a `/22` block.
     * Looker (Google Cloud core) supports all IPv4 ranges within [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918), which specifies IP addresses that are assigned to be used internally (that is, within an organization) and won't route on the Internet. Specifically, these are the following:
       * `10.0.0.0/8`
       * `172.16.0.0/12`
       * `192.168.0.0/16`
     * Class E IPv4 ranges (`240.0.0.0/4`) are reserved for future use as noted in [RFC 5735](https://datatracker.ietf.org/doc/html/rfc5735) and [RFC 1112](https://datatracker.ietf.org/doc/html/rfc1112) and aren't supported for Looker (Google Cloud core).
**Note:** In addition to Class E IPv4 ranges, some other IPv4 ranges outside of RFC 1918 may not be supported by Looker (Google Cloud core) or its dependencies. If you want to use a range outside of RFC 1918, you may want to test it first. When a Looker (Google Cloud core) instance is created for the first time in a region within a VPC, Looker creates a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets). The proxy-only subnet uses a `/26` range subnet of the `/22` subnet that you reserve when you create the Looker (Google Cloud core) instance. Any subsequent private connections (PSA) Looker (Google Cloud core) instances in the same VPC and in the same region use the same proxy-only subnet. 
  3. Add the [private services access connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#creating-connection) to your VPC network using the IP range allocated in the previous step for the **Assigned allocation**.
  4. Once your VPC network is created, return to the **Create Looker instance** page in your Google Cloud project. You may need to refresh the page so that your VPC network is recognized.



Once you have completed these steps, you can begin to create your instance by following the steps on the [Create a Looker (Google Cloud core) instance ](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) documentation page, starting with the [Before you begin](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#before_you_begin) section.

### Multiple private connections instances in the same VPC

If two or more private connections Looker (Google Cloud core) instances are located in the same region and in the same VPC, and you delete the first Looker (Google Cloud core) instance that was created in the region, the proxy-only subnet is not released because it is still in use by the remaining instances. If you attempt to create a new private connections (PSA) Looker (Google Cloud core) instance that uses the same address range that you used for the deleted instance (which contains the proxy-only subnet's IP address range), instance creation will fail, and you will see an "IP ranges exhausted" error. To check if an IP range is in use, check VPC peering for Service Networking, and check the import routes to see if they're using the IP range that you are interested in.

### Create an instance in a Shared VPC

If you are creating a Looker (Google Cloud core) instance in a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), complete the following steps in the Shared VPC's host project:

  1. [Enable the Looker API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) in the Shared VPC's host project in the Google Cloud console. When you enable the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=looker.googleapis.com)

  2. Create a [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) in the Shared VPC's host project, using the gcloud [`services identity create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create):
         
         gcloud beta services identity create --service=looker.googleapis.com \
         --project=SHARED_HOST_PROJECT_ID
         

Replace SHARED_HOST_PROJECT_ID with the Shared VPC's host project's ID.

  3. [Grant](https://docs.cloud.google.com/compute/docs/access/service-accounts#usingroles) the service account in the Shared VPC's host project an IAM role that contains the [`compute.globalAddresses.get`](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.globalAddresses.get) IAM permission. Next, run the [`add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding):
         
         gcloud projects add-iam-policy-binding SHARED_HOST_PROJECT_ID \
             --member=serviceAccount:SA_EMAIL --role=ROLE_NAME

Replace the following:

     * `SHARED_HOST_PROJECT_ID`: The Shared VPC's host project's ID.

     * `SA_EMAIL`: The email address of the service account that you created in the Shared VPC's host project.

     * `ROLE_NAME`: The name of the role that contains the `compute.globalAddresses.get` permission. Use one of the following formats:

       * Predefined roles: `roles/SERVICE.IDENTIFIER`
       * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
       * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/roles-permissions).




After creating the service account and granting it the IAM permission, wait a few minutes for the service account and permission to propagate.

In addition, allocate an IPv4 IP range in the Shared VPC and add the private services access connection to the Shared VPC as described in the previous section, Create and configure a VPC network.

**Note:** If you are using VPC Service Controls, and the Shared VPC host project and the Looker (Google Cloud core) service project are in different VPC Service Controls perimeters, you must create a [VPC Service Controls perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/create-perimeter-bridges) between the two perimeters to allow instance creation.

## Create the private connections instance

> Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.

**Important:** If you want to use customer-managed encryption keys (CMEK) with the Looker (Google Cloud core) instance that you are creating, see the [Enable CMEK for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-cmek) documentation page for information on the additional setup that's required prior to instance creation.

If you want a private connections (PSA) instance, you have to use Google Cloud CLI or Terraform and you must configure the instance as private connections (PSA) when you create it. Private connections cannot be added to or removed from an instance after the instance is created.

To create a private connections (PSA) instance using Google Cloud CLI, perform the following steps:

  1. If you are using [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek), then follow the instructions for creating a service account, key ring, and key before creating your Looker (Google Cloud core) instance.
  2. Use the `gcloud looker instances create` command to create the instance:
         
         gcloud looker instances create INSTANCE_NAME \
         --project=PROJECT_ID \
         --oauth-client-id=OAUTH_CLIENT_ID \
         --oauth-client-secret=OAUTH_CLIENT_SECRET \
         --region=REGION \
         --edition=EDITION \
         --private-ip-enabled \
         --consumer-network=CONSUMER_NETWORK --reserved-range=RESERVED_RANGE
         [--no-public-ip-enabled]\
         [--public-ip-enabled]\
         [--release-channel=RELEASE_CHANNEL]
         

Replace the following:

     * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it isn't associated with the instance URL.
     * `PROJECT_ID`: the name of the Google Cloud project in which you are creating the Looker (Google Cloud core) instance.
     * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret). After the instance has been created, [enter the instance's URL in the **Authorized redirect URIs** section of the OAuth client](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client).
     * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. Available regions are listed on the [Looker (Google Cloud core) locations](https://docs.cloud.google.com/looker/docs/looker-core-locations) documentation page.
     * `EDITION`: the edition, environment type (production or [non-production](https://docs.cloud.google.com/looker/docs/looker-core-overview#staging_environments_and_testing)), and whether this is a [trial edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#trials) for the instance. For a private connections (PSA) instance, this should be `core-enterprise-annual`, `core-embed-annual`, `nonprod-core-enterprise-annual`, `nonprod-core-embed-annual`, `core-trial-enterprise`, or `core-trial-embed`. Make sure that you choose the same edition type as listed in your [annual contract](https://cloud.google.com/looker/pricing) and that you have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) allocated. Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](https://docs.cloud.google.com/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
     * `CONSUMER_NETWORK`: [your VPC network or Shared VPC](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip#create-vpc) network in the format `projects/PROJECT_ID/global/networks/NETWORK_NAME`. Must be set if you're creating a private connections (PSA) instance.
     * `RESERVED_RANGE`: the range of IP addresses within the VPC in which Google will provision a subnetwork for your Looker (Google Cloud core) instance.
     * `RELEASE_CHANNEL`: the [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) for the instance. Available values are `rapid`, `regular`, and `no-channel`. The default during the preview is `no-channel`. If you don't include this flag in your `create` command, the instance will be created with the default channel. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

You may include the following flags:

     * `--private-ip-enabled` enables private connections (PSA). This must be included to create a private connections (PSA) instance.
     * `--public-ip-enabled` enables public IP.
     * `--no-public-ip-enabled` disables public IP.
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

     * `MAINTENANCE_WINDOW_DAY`: Must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the [Manage maintenance policies for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#maintenance_settings) documentation page for more information about maintenance window settings.
     * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: Must be in UTC time in 24-hour format (for example, `13:00`, `17:45`). 
     * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: Must be in the format `YYYY-MM-DD`. You cannot set a deny maintenance period if you are also enrolling the instance in the Rapid release channel or using the [Accelerated Security Patching (ASP) configuration flag](https://docs.cloud.google.com/looker/docs/looker-core-release-process#asp-flag) with the Regular release channel.
     * `KMS_KEY_ID`: Must be the key that is created when setting up [customer-managed encryption keys (CMEK).](https://docs.cloud.google.com/looker/docs/looker-core-cmek#copy_or_write_down_the_kms_key_id_and_the_kms_keyring_id)

The following flags enable other settings:

     * `--accelerated-security-patch-enabled` and `--no-accelerated-security-patch-enabled`: Include one of these flags if your instance is on the `regular` channel and you want to receive or disable security patches bi-weekly. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).
     * `--fips-enabled`: [Enable FIPS 140-3 level 1 compliance](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode).
     * Replace the `--catalog-integration-enabled` flag with the `--no-catalog-integration-enabled` flag to disable the [ Looker (Google Cloud core) and Knowledge Catalog integration](https://docs.cloud.google.com/looker/docs/looker-core-dataplex).
**Tip:** You must have [quota](https://docs.cloud.google.com/docs/quotas/view-manage) for the proper edition type to create an instance. If you don't have quota, [contact Sales](https://cloud.google.com/contact/form?direct=true&e=13802955) to allocate quota to your project. For more troubleshooting help, see the [Troubleshooting Looker (Google Cloud core) instance creation failures](https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-instance-creation-troubleshooting) documentation page.

**Note:** If you create a private connections (PSA) instance using Terraform, the network name must follow the format: `projects/<project>/global/networks/<network>`.

As the instance is being created, you can view its status on the [**Instances**](https://docs.cloud.google.com/looker/docs/looker-core-view-console) page within the console. You can also see your instance creation activity by clicking on the notifications icon in the Google Cloud console menu.

**Note:** If the instance creation process fails, wait 72 hours before retrying to create the instance if you will be using the same IP range. Cloud SQL requires 72 hours to release the allocated IP range. If you chose hybrid connections when setting up the instance, you can set up inbound access through the web URL for the instance. That URL can be found on the **Instances** page of the Google Cloud console, or the **Custom domain** tab of the instance details page, if you set up a custom domain. You can [set up an IP allowlist](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist) to restrict inbound connections to traffic from certain IP addresses. 

If you create a private connections (PSA) only instance, a URL **won't** appear on the **Instances** page. See the following Access a private services access instance after creation section for more information about how to set up access to your private connections (PSA) instance.

## Access a private services access instance after creation

If you create an instance that is enabled only for private connections, you will **not** receive a URL for the instance. To access the instance, you must configure a custom domain for the instance and add that custom domain to the instance's OAuth credentials. Follow the instructions on the [Access a Looker (Google Cloud core) instance using private services access](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-private-ip) documentation page to create and access a custom domain.

If you create an instance that uses a hybrid networking configuration, follow the instructions on the [Set up a custom domain for a Looker (Google Cloud core) instance that uses public connections](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) documentation page to create and access a custom domain.

## Troubleshooting instance creation issues

For troubleshooting help, see the [Troubleshooting Looker (Google Cloud core) instance creation failures](https://docs.cloud.google.com/looker/docs/looker-core-instance-creation-troubleshooting) documentation page.

## What's next

  * If you are using hybrid connections, [set up an IP allowlist](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist) to restrict inbound traffic to certain IP addresses.
  * If you are using hybrid connections or public connections, [set up a custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
