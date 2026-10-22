---
url: https://docs.cloud.google.com/looker/docs/looker-core-view-console/
title: View and edit the details of a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:45.069433+00:00
---

# View and edit the details of a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-view-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  View and edit the details of a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

You can find and edit information about a project's Looker (Google Cloud core) instances in the Google Cloud console.

## Viewing instance information

Looker (Google Cloud core) instances that are associated with the selected Google Cloud project are listed on the **Instances** page in the Google Cloud console — including instances that are created by other users in your organization.

### Required role

To view information on the **Instances** page, you must have the [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) or the [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`) role.

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

### The Instances page

The **Instances** page displays this information about each instance:

  * **Status** : 
    * A green circle with a check mark is shown if the instance was created successfully and is active.
    * A loading icon is shown if the instance creation is in progress.
  * **Name** : The name of the instance that was provided by the instance creator when the instance was created. Click the name to navigate to the **Details** tab, which shows additional information about the selected instance.
  * **Instance URL** : The URL at which an instance using public secure connections can be accessed. By default, instance URLs take the form `https://hostname.looker.app`, where the hostname is randomly assigned. Click the URL to navigate to the instance.

**Note:** If a Looker (Google Cloud core) instance uses private connections, a URL won't appear in this column. You must create a [custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-private-ip-overview) and then you can view the URL on the **Custom domain** tab.
  * **Version** : The Looker version that's running on the instance.

  * **Region** : The region in which the instance is hosted.

  * **Created Date** : The date on which the instance was created.




### Instance tabs

From the **Instances** page, click an instance's name to view more information about the instance. After you click the name, an instance configuration page appears with information in the following tabs:

  * **Details**
  * **Backups**
  * **Custom domain**
  * **Data Studio Pro**



#### **Details** tab

**Note:** OAuth application credentials are not shown on the **Details** tab but can be edited when you are editing instance settings.

The **Details** tab shows additional instance metadata:

  * **Platform Edition** : The instance's [edition](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#create_edition). Options are **Standard** , **Enterprise** , and **Embed**.
  * **Release Channel** : The [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) for the instance. Options are **Rapid** , **Regular** , and **No channel**. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).
  * **Create Time** : The time at which the instance was created.
  * **Update Time** : The time at which the instance was most recently updated.
  * **Public IP Enabled** : Whether the instance's network connection is enabled for public secure connections. If it's enabled, **true** is shown. If it's not enabled, **false** is shown.
  * **Private IP Enabled** : Whether the instance's network connection is enabled for [private connections (private services access)](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip) connection. If it's enabled, **true** is shown. If it's not enabled, **false** is shown. This setting shows **false** if the instance's network connection uses Private Service Connect.
  * **PSC Enabled** : Whether the instance's network connection is enabled for [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-create-psc). If it's enabled, **true** is shown. If it's not enabled, **false** is shown.
  * **PSC Configuration** : This setting appears if **PSC Enabled** is **true** , along with the following subsettings:

    * **Looker Service Attachment URI** : This setting displays the URI for the Private Service Connect [service attachment](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#service_attachment) for Looker (Google Cloud core).
    * **Allowed VPCs** : This setting contains a list of the VPCs that have [authorized northbound access](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#psc-access) into the Private Service Connect instance.
    * **PSC Endpoint** : This setting appears if the Looker (Google Cloud core) instance is using Private Service Connect to make [outbound (egress) connections to published services](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#local-fqdn). These subsettings are available:

      * **Local FQDN** : The fully qualified domain name of the published service that the instance is connecting to.
      * **Target Service Attachment URI** : The [service attachment URI](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#service_attachment_uri) for the published service that the Looker (Google Cloud core) instance is connecting to.
      * **Connection Status** : The status of the connection, which can be one of the following:

        * **ACCEPTED** : Connection is established and functioning normally.
        * **PENDING** : Connection is not established (Looker tenant project hasn't been allowlisted).
        * **NEEDS ATTENTION** : Issue with target service attachment, such at NAT subnet is exhausted.
        * **REJECTED** : Connection is not established (Looker tenant project is explicitly in the reject list).
        * **CLOSED** : Target service attachment doesn't exist, or prerequisites are missing — such as Cloud NAT for proxy-only subnets, TCP health checks, or the Looker tenant project ID in the service attachment's allowlist. This status is a terminal state. If the connection status reaches `CLOSED`, you must re-run the `gcloud looker instances update` command with the `--psc-service-attachment` flag to force Looker (Google Cloud core) to re-trigger the connection attempt.
        * **UNKNOWN** : Connection status is unspecified.
    * **Controlled Egress Enabled:** This field displays **true** if the Looker (Google Cloud core) instance is using the HTTPS protocol to connect to the Looker Marketplace or to an external service with a global FQDN. Otherwise, the field displays **false**.

    * **Controlled Egress Configuration** : This section appears if a connection has been enabled to the Looker Marketplace or to a global FQDN. The following fields appear:

      * **Marketplace Enabled** : This field displays **true** if an egress connection to Looker Marketplace has been created; otherwise, it displays **false**.
      * **Egress FQDNs** : This field displays the fully qualified domain names of any global FQDNs for which egress connections have been set up.
      * **Egress IPs** : This field displays the IP addresses that are used for internet egress traffic when controlled egress is enabled. The IP addresses are unique to your Looker (Google Cloud core) instance. These IP addresses are dynamic and may change without warning.
  * **IP Allowlist Configuration** : The **IP Allowlist Configuration** section appears for instances using public secure connections. The following subsettings are shown:

    * **IP Allowlist Enabled** : This field displays **true** if the [**Enable IP Allowlist** checkbox](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist#configure_an_ip_allowlist) is selected on the instance's **Edit** page. This field displays **false** if the checkbox is not enabled.
    * **Google Services Enabled** : This field displays **true** if the [**Link Google services with this instance** checkbox](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist#allowlist-services) is selected on the instance's **Edit** page.
    * **IP Allowlist Rules** : Each allowlist rule shows as an expandable or collapsible item in this section. Each item contains a **Description** field, which is the name of the rule, and an **IP Range** field, which is the IP range for the rule.
  * **Egress Public IP** : This field provides information about instances with a public secure connection. It shows the egress public IP address, which was automatically assigned when the instance was created. If no value has been assigned, **No value** is shown.

  * **Ingress Public IP** : This field provides information about instances with a public secure connection. It shows the ingress public IP address, which was automatically assigned when the instance was created.

  * **Ingress Private IP** : This field provides information about instances with private connections that use private services access. It shows the ingress private IP address for the instance. If the instance was created with a public secure connection or with Private Service Connect, **No value** is shown.

  * **Associated Network** : This field provides information about instances with private connections that use private services access. It shows the network that was selected to make a private connection. If the instance was created with public secure connections, **No value** is shown.

  * **Allocated IP Range** : This field provides information about instances with private connections that use private services access. It shows the range of IP addresses that was assigned by the instance creator or by Google when the instance was created. If the instance was created with Private Service Connect or with a public secure connection, **No value** is shown.

  * **Email Domain Allowlist** : The **Email Domain Allowlist** setting displays the email domains to which your Looker (Google Cloud core) users can [deliver](https://docs.cloud.google.com/looker/docs/scheduling) Looker content — [Looks](https://docs.cloud.google.com/looker/docs/viewing-looks), [dashboards](https://docs.cloud.google.com/looker/docs/dashboards), [queries](https://docs.cloud.google.com/looker/docs/delivering-looks-explores) with visualizations — or [alert notifications](https://docs.cloud.google.com/looker/docs/alerts-overview) through email. By default, there are no domains in the allowlist at the time of instance creation, and Looker (Google Cloud core) users who have the [appropriate Looker permissions to email content](https://docs.cloud.google.com/looker/docs/configuring-deliveries#granting_scheduling_permissions_for_users) can email content to any domain. To limit content deliveries and alert notifications to email addresses from a specific domain, [edit the instance configuration](https://docs.cloud.google.com/looker/docs/looker-core-view-console#edit_instance_settings) to restrict the domain(s) to which users can send emails. To learn more about the email domain allowlist and how it interacts with permissions and user attributes, see the [Email domain allowlist for scheduled content](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content) documentation.

**Note:** By default, Looker (Google Cloud core) instances that use private connections or hybrid connections allow email deliveries to external domains. To restrict the domains to which Looker users can send email deliveries, set up an email domain allowlist. 
  * **Maintenance Window** : The day of the week and the hour in which Looker (Google Cloud core) schedules maintenance, if a [maintenance window has been defined](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) for your instance. Maintenance windows last for one hour. If a maintenance window has not been defined, **No value** is shown. 

  * **Scheduled Maintenance** : The scheduled date and time of upcoming [maintenance for your instance](https://docs.cloud.google.com/looker/docs/looker-core-maintenance). If maintenance has not been scheduled, **No value** is shown. 

  * **Deny Maintenance Period** : A time period during which Looker (Google Cloud core) does not schedule maintenance, if a [deny maintenance period](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#configure_a_deny_maintenance_period) has been configured for your instance.

    * **Start Date** : The start date for the deny maintenance period. If a deny maintenance period has not been scheduled, **No value** is shown.
    * **End Date** : The end date for the deny maintenance period. If a deny maintenance period has not been scheduled, **No value** is shown.
    * **Time** : The time at which the deny maintenance period begins and ends on the start date and end date you specified. If a deny maintenance period has not been scheduled, **No value** is shown. 
  * **Last Deny Maintenance Period** : The start date and end date for the most recent deny maintenance period. You must allow at least 14 days of maintenance availability between any two deny maintenance periods.

    * **Start Date** : The start date for the most recent deny maintenance period. If a deny maintenance period was not scheduled previously, **No value** is shown.
    * **End Date** : The end date for the deny maintenance period. If a deny maintenance period was not scheduled previously, **No value** is shown.
    * **Time** : The time at which the previous deny maintenance period began and ended on the start date and end date for that deny maintenance period. If a deny maintenance period was not scheduled previously, **No value** is shown.
  * **Encryption** : This setting appears only if the instance was created with [CMEK](https://docs.cloud.google.com/kms/docs/cmek). When visible, it displays "Customer-managed encryption key (CMEK)" along with the key identifier and a link to the key. If the instance uses the [default Google-managed encryption](https://docs.cloud.google.com/docs/security/encryption-at-rest/default-encryption), this field is not shown. You may need a [Cloud KMS IAM role or permission](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) on [the key that's being used](https://docs.cloud.google.com/kms/docs/iam#granting_roles_on_a_resource) to see the status of the CMEK encryption key.

  * **Export schedule** : This field appears if a [scheduled export job](https://docs.cloud.google.com/looker/docs/looker-core-scheduled-export) is configured for the instance. If it is configured, the daily start time appears in the **Start time** field. The time is represented as your local time.

  * **FIPS 140-3 Validated Encryption Enabled** : This setting appears only if the instance is an [Enterprise](https://docs.cloud.google.com/looker/docs/looker-core-overview#enterprise_edition) or an [Embed](https://docs.cloud.google.com/looker/docs/looker-core-overview#embed_edition) edition. When visible, it displays whether the Looker (Google Cloud core) in Looker instance is compliant with the [Federal Information Processing Standard Publication (FIPS) 140-3](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode) standard. If it's compliant, **true** is shown. If it's not compliant, **false** is shown.

  * **Gemini Enabled** : Whether the Gemini in Looker is enabled for the instance. If it's enabled, **true** is shown. If it's not enabled, **false** is shown.

  * **Gemini AI Configuration** : This setting appears if **Gemini** is enabled, along with the following subsettings:

    * **Trusted Tester features** : If it's enabled, **true** is shown. If it's not enabled, **false** is shown.
    * **Trusted Tester data use** : If it's enabled, **true** is shown. If it's not enabled, **false** is shown.
  * **Catalog Integration Disabled** : This field displays **true** if the integration between Looker (Google Cloud core) and Knowledge Catalog is disabled. Otherwise, the field displays **false**.




#### **Backups** tab

The **Backups** tab lets you [view and manage the automatic and manual backups for the instance](https://docs.cloud.google.com/looker/docs/looker-core-backup-restore).

#### **Custom domain** tab

The **Custom domain** tab provides an optional means to customize the URL to access the instance with a [custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain).

#### **Data Studio Pro** tab

**Important:** Complimentary Data Studio Pro licenses are not available for Looker (Google Cloud core) instances that are created after **August 1, 2026**. For those instances, this tab isn't visible.

In the **Data Studio Pro** tab, you can [accept the complimentary Data Studio Pro licenses](https://docs.cloud.google.com/looker/docs/looker-core-lsp) that have been allocated to your Looker (Google Cloud core) instance. If the **Accept Data Studio Pro licenses** toggle is enabled, you have accepted the complimentary licenses.

This tab also indicates the name of the Google Cloud project that hosts your Data Studio Pro subscription content.

## Edit Looker (Google Cloud core) instance settings

**Note:** The edition and region of a Looker (Google Cloud core) instance cannot be edited. If you need to change one of these settings, you can use [export and import](https://docs.cloud.google.com/looker/docs/looker-core-import-export) to transfer Looker (Google Cloud core) instance data into a new instance with updated edition or region settings.

### Required role

To get the permissions that you need to edit Looker (Google Cloud core) instance settings, ask your administrator to grant you the [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project in which the instance was created. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You may also need additional IAM roles or permissions to edit specific instance settings.

### Editing settings

To modify instance settings, select one of the following options:

### console

On the instance **Details** tab, click **Edit** to modify these settings:

  * **Connections** : Your instance configuration _must_ specify a network connection. If you have an instance that uses hybrid connections, you can change the connection option to private connections, or if your instance uses private connections, you can change the connection option to hybrid connections. Otherwise, this setting cannot be edited.

**Note:** If you have a Looker (Google Cloud core) instance that uses private connections, and you would like to change your configuration to use hybrid connections, you must [configure the public custom domain A record](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain#create_a_dns_record) to point to the public IP address for the instance. This step ensures that the custom domain and certificate work correctly. If you want to maintain public and private access to the custom domain, you must use split DNS and manage both internal and external DNS systems.
  * **Configure inbound connections** : The fields in this section vary depending on the instance's networking setup:

    * If you have a public secure connections instance or a hybrid instance, you can create or edit an instance's IP allowlist, which allows _only_ the IP addresses listed in the allowlist to access the instance. 
      * Create the allowlist by checking the **Enable IP allowlist** checkbox and clicking **Add item** under **IP allowlist rules** to add a rule. In the **Rule name** field, add the name of the rule. In the **IP range** field, add the range of approved IP addresses, using an IP address and a subnet mask, as described in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). Add another rule to the allowlist by clicking **Add Item**. You can delete a rule by clicking the **Delete item** trash icon that appears when you hold the pointer over the rule. See the [Configure an IP allowlist for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist) documentation page for more information.
      * If you want to use other Google Cloud services with your Looker (Google Cloud core) instance, and your instance uses an IP allowlist, you must grant access to the IP ranges used by other Google Cloud services before you can connect with those services. Certain Google Cloud services can be automatically added to the allowlist by selecting the **Link Google services with this instance** checkbox. To learn more, visit the [Allow connections to Google services](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist#allowlist-services) documentation.
    * If you have a private connections instance that uses Private Service Connect, you can edit the VPCs that are allowed ingress into the instance. You can update the existing settings for a VPC. You can delete a VPC by clicking the **Delete item** trash icon that appears when you hold the pointer over the network. Or, you can add a VPC by clicking **Add Item** , selecting the project in which the network was created in the **Project** field, and then selecting the network in the **Network** drop-down menu.
  * **Configure outbound connections** : If you have a hybrid connections or private connections instance that uses Private Service Connect, you can configure outbound (egress) connections from your Looker (Google Cloud core) instance to external services.

    * **Enable Looker to connect to external services** : Select this checkbox to use HTTPS and a [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) to make a connection to the Looker Marketplace or a connection to a global FQDN.
    * **Enable connection to Looker Marketplace** : Select this checkbox to enable a connection to the Looker Marketplace.
    * **Global FQDN** : To connect to an external public domain by using [controlled egress](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#controlled-native-egress), click the **Add Item** button and add the fully qualified domain name in the **Global FQDN** field. To remove a global FQDN, select an item and click the **Delete Item** icon.
  * **Local FQDN** : If you have a hybrid connections or private connections instance that uses Private Service Connect, you can edit the [outbound service attachments](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#local-fqdn). You can update the existing settings for a service attachment. You can delete a service attachment by clicking the **Delete item** trash icon that appears when you hold the pointer over it. Or, you can add a service attachment by clicking **Add Item**. When adding a service attachment, enter the fully qualified domain name of the service in the **Local FQDN** field and the [service attachment URI](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#service_attachment_uri) in the **Target Service Attachment URI** field.

  * **Authentication:** You can edit the **Authentication** settings for your Looker (Google Cloud core) instance. The options are **Workforce Identity Federation (SAML/OIDC)** or **Google OAuth** for [primary authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication#primary-authentication-methods). If you choose to use Workforce Identity Federation for primary authentication, you can also enable the **Enable secondary OAuth** toggle to configure OAuth as a secondary authentication method.

**Note:** The integration between Looker (Google Cloud core) andWorkforce Identity Federation is in [preview](https://cloud.google.com/products#product-launch-stages) and is only supported for Looker (Google Cloud core) instances that use [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections).
  * **OAuth Application Credentials:** Additionally in the **Authentication** section, you can edit the **OAuth Application Credentials** settings. If the OAuth credentials are set to **Manual** , that means that custom OAuth credentials were added to your instance either during or after instance creation. The client ID and client secret are not shown; instead, the section displays `****` placeholders. If the OAuth credentials are set to **Looker managed** , Looker (Google Cloud core) provisioned OAuth credentials for your instance during instance creation and the client ID and client secret aren't shown.

Before you edit this setting, be sure to [set up the new credentials](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#before_you_create_a_instance) and [add the instance's domain](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client) to the **Authorized redirect URIs** field in the OAuth client. To edit this setting, set the OAuth credentials to **Manual** , if it is not already selected.

  * **Release Channel** : You can edit the [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) for the instance. Options are **Rapid** , **Regular** , and **No channel**. To edit the [Accelerated Security Patching (ASP) flag](https://docs.cloud.google.com/looker/docs/looker-core-release-process#asp-flag), you must use Google Cloud CLI.

  * **Maintenance Window** : You can optionally [specify the day of the week and the hour](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour. By default, the **Preferred Window** option in the **Maintenance Window** is set to **Any window**.

  * **Deny Maintenance Period** : You can optionally [specify a block of days](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#configure_a_deny_maintenance_period) in which Looker (Google Cloud core) does not schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between deny maintenance windows.

  * **Email Domain Allowlist** : When there are no domains in the **Allowed Domains** field, email domains are not restricted. To restrict domains, enter the domain or domains to be allowed in the format `domain.suffix`, and then click **Enter** on your keyboard. If you make changes to the **Email Domain Allowlist** setting for an instance, the Looker (Google Cloud core) instance must restart, and, if there are any running [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_pdts) within the instance, they will be [regenerated](https://docs.cloud.google.com/looker/docs/derived-tables#how_looker_builds_pdts). To learn more about the email domain allowlist setting and how it interacts with permissions and user attributes, see the [Email domain allowlist for scheduled content](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content) documentation page.

**Note:** By default, Looker (Google Cloud core) instances that use private connections or hybrid connections allow email deliveries to external domains. To restrict the domains to which Looker users can send email deliveries, set up an email domain allowlist.
  * **Gemini in Looker** : When the **Gemini** setting is enabled, Gemini in Looker features are available for the Looker (Google Cloud core) instance. When the **Trusted Tester features** setting is enabled, users on the instance can access the [Trusted Tester capabilities](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview) that are available for Gemini in Looker. When the **Trusted Tester data use** setting is enabled, Google is granted access to Gemini in Looker user data as described in the [Gemini for Google Cloud Trusted Tester Program terms](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview). To learn more about Gemini in Looker features and how to administer them for a Looker (Google Cloud core) instance, see the [Administer Gemini on your Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.

  * **Universal catalog integration** : You can optionally select the **Opt out of Dataplex Catalog integration** checkbox if you don't want Looker (Google Cloud core) to [integrate with Knowledge Catalog](https://docs.cloud.google.com/looker/docs/looker-core-dataplex). Looker (Google Cloud core) and Knowledge Catalog are integrated by default.




The integration between Looker (Google Cloud core) and Knowledge Catalog enables both metadata ingestion and [data lineage](https://docs.cloud.google.com/looker/docs/looker-core-lineage) (if the Data Lineage API is enabled).

When you have made your changes, click **Save**.

###  gcloud 

To update the settings, use the `gcloud looker instances update` command:
    
    
    
    gcloud looker instances update (INSTANCE_NAME : --region=REGION)
        [--allowed-email-domains=[ALLOWED_EMAIL_DOMAINS,...]]\
        [--oauth-client-id=OAUTH_CLIENT_ID]\
        [--oauth-client-secret=OAUTH_CLIENT_SECRET] [--public-ip-enabled] [--no-public-ip-enabled]\
        [--release-channel=RELEASE_CHANNEL]\
        [--accelerated-security-patch-enabled]\
        [--deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
          --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
          --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME]\
        [--maintenance-window-day=MAINTENANCE_WINDOW_DAY
          --maintenance-window-time=MAINTENANCE_WINDOW_TIME]\
        [--psc-service-attachment  domain=DOMAIN_1,attachment=SERVICE_ATTACHMENT_URI_1 \
        --psc-service-attachment domain=DOMAIN_2,attachment=SERVICE_ATTACHMENT_URI_2 \]
        [--psc-allowed-vpcs=ALLOWED_VPC_1,ALLOWED_VPC_2 ]\
        [--clear-psc-allowed-vpcs]\
        [--async]
    

Replace the following:

  * `INSTANCE_NAME`: the name for your Looker (Google Cloud core) instance; it is not associated with the instance URL.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.
  * `RELEASE_CHANNEL`: the [release channel](https://docs.cloud.google.com/looker/docs/looker-core-release-process#release_channels) for the instance. Available values are `rapid`, `regular`, and `no-channel`. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).
  * ALLOWED_EMAIL_DOMAINS: when there are no domains in `--allowed-email-domains`, email domains are not restricted. To restrict domains, add the domain or domains to be allowed in the format `domain.suffix`. If you make changes to the allowed email domains for an instance, the Looker (Google Cloud core) instance must restart, and, if there are any running [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_pdts) within the instance, they will be [regenerated](https://docs.cloud.google.com/looker/docs/derived-tables#how_looker_builds_pdts). To learn more about the email domain allowlist and how it interacts with permissions and user attributes, see the [Email domain allowlist for scheduled content](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content) documentation.

**Note:** By default, Looker (Google Cloud core) instances that use private connections or hybrid connections allow email deliveries to external domains. To restrict the domains to which Looker users can send email deliveries, set up an email domain allowlist.
  * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you have associated with your instance. Before you edit this setting, be sure to [set up the new credentials](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#before_you_create_a_instance) and [add the instance's domain](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client) to the **Authorized redirect URIs** field in the OAuth client.

  * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`.

  * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC time in 24-hour format (for example, 13:00, 17:45).

  * `MAINTENANCE_WINDOW_DAY`: must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the [Manage maintenance policies for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#maintenance_settings) documentation page for more information about maintenance window settings.

  * DOMAIN_1 and DOMAIN_2: The domain name(s) of any published services that you want to connect to a Looker (Google Cloud core) instance by using Private Service Connect. See the [Create a Looker (Google Cloud core) Private Service Connect instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#specify_southbound_connections) documentation page for more information.

  * `SERVICE_ATTACHMENT_URI_1` and `SERVICE_ATTACHMENT_URI_2`: The full service attachment URI(s) of any published services that you want to connect to a Looker (Google Cloud core) instance using Private Service Connect. See the [Create a Looker (Google Cloud core) Private Service Connect instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#specify_southbound_connections) documentation page for more information.

  * `ALLOWED_VPC_1` and `ALLOWED_VPC_2`: The VPCs that will be allowed ingress into a Looker (Google Cloud core) instance that uses Private Service Connect. See the [Create a Looker (Google Cloud core) Private Service Connect instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#update_allowed_vpcs) documentation page for more information.




You may also include the following flags:

  * `--public-ip-enabled` enables public IP.
  * `--no-public-ip-enabled` disables public IP.
  * `--clear-psc-allowed-vpcs` removes all VPCs from an instance that uses Private Service Connect.
  * `--no-catalog-integration-enabled` disables the [integration with Knowledge Catalog](https://docs.cloud.google.com/looker/docs/looker-core-dataplex).
  * `--catalog-integration-enabled` enables the [integration with Knowledge Catalog](https://docs.cloud.google.com/looker/docs/looker-core-dataplex).
  * `--accelerated-security-patch-enabled`: optionally include this flag if your instance is on the `regular` release channel and you want to receive security patches bi-weekly. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).



If you have an instance that uses private connections, you can add or remove a public secure connection. You cannot add or remove a private connection.

**Note:** If you have a Looker (Google Cloud core) instance that uses private connections (Private Service Connect) , and you would like to add a public IP option to your configuration, you must [configure the public custom domain A record](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain#create_a_dns_record) to point to the public IP address for the instance. This ensures the custom domain and certificate work correctly. If you want to maintain public and private access to the custom domain, you must use split DNS and manage both internal and external DNS systems.

Before you update OAuth credentials, be sure to [set up the new credentials](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#before_you_create_a_instance) and [add the instance's domain](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client) to the **Authorized redirect URIs** field in the OAuth client.

**Note:** If your `gcp.restrictTLSCipherSuites` organization policy constraint doesn't include any cipher suites that are in the [MODERN SSL policy profile](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#defining_an_ssl_policy), Looker will return an error when you click **Save** , and the instance update will fail. Update the policy to resolve the error and update the instance. See the [Restrict TLS cipher suites](https://docs.cloud.google.com/looker/docs/looker-core-tls-cipher-suites#policy_violations) documentation page for more information.

## What's next

  * [Looker (Google Cloud core) admin settings](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker)
  * [One-time data import or export for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-import-export)
  * [Delete or restart a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-delete-restart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
