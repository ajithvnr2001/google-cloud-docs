---
url: https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards/
title: Scheduling and sending dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:27.665256+00:00
---

# Scheduling and sending dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Scheduling and sending dashboards Stay organized with collections  Save and categorize content based on your preferences. 

This page is about scheduling and sending a [dashboard](https://docs.cloud.google.com/looker/docs/viewing-dashboards). To learn about scheduling Looks or Explores, visit the [Using the Looker Scheduler to deliver content](https://docs.cloud.google.com/looker/docs/scheduling) documentation page.

Looker lets you schedule immediate or recurring deliveries of dashboards with the **Schedule delivery** dashboard menu option.

Depending on how your Looker admin has set up your [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) for data delivery, you may be able to deliver your content to one or more of Looker's built-in delivery destinations:

  * Email
  * Webhook
  * Amazon S3 bucket
  * SFTP server



You may also be able to schedule a data delivery to a third-party service that is integrated with Looker, such as [Slack](https://slack.com/).

If there are valid results [in cache](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#how_looker_uses_cached_queries), Looker will deliver cached results. If there are no results or if the cached results have expired, Looker will rerun the query and cache those results.

## Starting a delivery from a dashboard

**Note:** If you're a Looker developer, you must turn off [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode) to schedule or send. Deliveries are executed using [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode) LookML.

Make sure that the dashboard is not in [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards). Select the **Dashboard actions** three-dot menu in the upper right of the dashboard and choose **Schedule delivery**. If you don't see the **Schedule delivery** option, talk to your Looker admin about your assigned permissions.

![](https://docs.cloud.google.com/static/looker/docs/images/scheduling-dboard-beta-2408.png)

Once you select **Schedule delivery** , either an existing schedules window appears or a **Schedule Delivery** or **Send** window appears, depending on whether you have already created existing schedules on the dashboard.

## Starting a delivery from a folder

You can also start a delivery of a dashboard from [the folder](https://docs.cloud.google.com/looker/docs/finding-content#navigating_to_dashboards_and_looks_from_folders) where the dashboard is located.

Select **Schedule delivery** from the three-dot menu on the right side of that dashboard's row (in list view) or from the three-dot menu at the top right of the thumbnail (in grid view).

## Existing schedules window

If you have already created schedules for this dashboard, an existing schedules window appears. This window shows the schedules that you have set along with information about each schedule, such as destination and format. Deliveries that use the **Send now** recurrence and schedules that were created by other people don't appear in this window.

![The existing schedule window showing a scheduled dashboard delivery called Order Analysis.](https://docs.cloud.google.com/static/looker/docs/images/existing-dboard-beta-schedules-2220.png)

You can perform the following functions in the existing schedules window:

  * Select **Send now** to send an immediate delivery of existing scheduled content without disrupting the scheduled cadence.

  * Select the three-dot menu to edit, duplicate, or delete a schedule.

  * Select **Done** to exit the window.

  * Select **New** to open the **Schedule Delivery** or **Send** window and create a new schedule or immediately send a new delivery.




## Schedule Delivery window

If you select **New** from the existing schedules window, or, if you don't have any pre-existing schedules for the dashboard, the **Schedule Delivery** or **Send** window opens. This window lets you customize recurrence, destination, format, filters, and more:

![The Schedule Delivery window shows options to customize the name, recurrence, destination, and format of a dashboard delivery.](https://docs.cloud.google.com/static/looker/docs/images/schedule-send-window-2220.png)

The **Settings** tab in the **Schedule Delivery** or **Send** window lets you customize your delivery's recurrence, destination, format, and more.

### Naming a delivery

The top of the **Schedule Delivery** or **Send** window shows the name that is automatically given to the delivery. The name defaults to the dashboard's name. To edit the delivery's name, select the name (indicated by the dotted underscore), and make your edits.

Depending on the destination of your delivery, the title may also appear in other places:

  * For email deliveries, the title is used for the email's subject line and as part of the filename if you select a format that uses an email attachment.
  * For webhooks, the title is included in the webhook payload under the **Title** field.
  * For deliveries to an Amazon S3 bucket, the title is used in the filename of the delivery and in any error emails that are sent. The filename of the delivery follows the format `TITLE_TIMESTAMP_HASH`, where `HASH` is a random six-character identifier and `TIMESTAMP` follows the pattern `YYYY-MM-DDTHHMM` (for example, the timestamp portion would look like `2019-05-31T0933` for May 31, 2019 at 9:33 AM). The timestamp's timezone will match the **Delivery time zone**.
  * For SFTP deliveries, the title is included in the filename of the delivery. The filename of the delivery follows the format `TITLE_TIMESTAMP_HASH`, where `HASH` is a random six-character identifier and `TIMESTAMP` follows the pattern `YYYY-MM-DDTHHMM` (for example, the timestamp portion would look like `2019-05-31T0933` for May 31, 2019 at 9:33 AM). The timestamp's timezone will match the **Delivery time zone**.
  * For deliveries to integrated services that generate a file attachment, the title is included in the filename of the delivery.



### Recurrence

Customize the timing of your delivery in the **Recurrence** section.

#### Send now

If you select **Send now** from the **Recurrence** drop-down menu, a one-time delivery of the dashboard is sent after you fill in the required fields and select the **Send now** button at the bottom of the window.

#### Time-based and date-based schedules

Select one of the following options from the **Recurrence** drop-down menu:

  * **Monthly**
  * **Weekly**
  * **Daily**
  * **Hourly**
  * **Minutes**
  * **Specific months**
  * **Specific days**



Timing options change depending on the option that you choose. For example, the **Hourly** settings include a **Start** time and an **End** time. Looker will send the delivery every hour starting at the **Start** time and ending at the **End** time.

The **Time** , **Start** , and **End** fields use a 24-hour clock. If the time you want isn't available in the drop-down menu, select the field and manually enter the time, such as 9:15 or 15:37.

**Hourly** and **Minutes** schedules repeat daily within the **Start** and **End** timeframe that you set. The end time for **Hourly** and **Minutes** intervals is not inclusive. The last delivery is sent at the last selected interval prior to the specified end time. For example, if a dashboard is scheduled **Hourly** between 12:00 AM and 11:00 PM, then it is sent on the hour, every hour, from 12:00 AM to 10:00 PM If a recurrence is every 30 minutes between 12:00 AM and 11:00 PM, then the last delivery is sent at 10:30 PM.

#### Schedules triggered by datagroup updates

If your LookML developer has configured [datagroups](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup), you can schedule delivery of a dashboard to occur after a datagroup has been triggered, has managed the cache, and has [rebuilt relevant PDTs](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt).

Select **Datagroup update** from the **Recurrence** drop-down menu. This reveals a **Datagroup** field with a drop-down menu. Select the datagroup whose update should prompt delivery.

To schedule a dashboard using a datagroup update trigger, the dashboard must contain at least one tile that is based on a model file that includes a [datagroup parameter](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#creating_a_datagroup_to_schedule_deliveries_on_the_last_day_of_every_month). The **Datagroup** drop-down menu lists all datagroups defined in the models that are included in the dashboard, even if the datagroups are not used to handle caching for queries or PDTs. Even if the datagroup is used in only one tile's model, the entire dashboard will be sent when the selected datagroup update completes.

Schedules based on datagroups only send after the regeneration process has completed for all PDTs that are persisted with that datagroup parameter, ensuring that your delivery includes the most up-to-date data.

### Destination

**Note:** Depending on how your Looker admin has configured your permissions, some destination options may not be visible.

The **Destination** setting may display several destination options for dashboard deliveries. Once you've selected a data destination, a new setting field appears for you to add specific details about that destination, such as an email address or a webhook URL. See the following sections for information about each destination's settings.

**Note:** The [Google Sheets destination](https://docs.cloud.google.com/looker/docs/connected-sheets) isn't supported for dashboard scheduling. Dashboards require formats that support multiple tiles or archives (such as PDF, PNG, or ZIP), while the Google Sheets action only supports streaming the results of a single query in plain CSV format. To deliver data to Google Sheets, schedule the delivery from the Look or Explore UI instead, ensuring that the output format is set to plain CSV.

#### Email

When **Email** is selected in the **Destination** field, a new **Email addresses** field appears. This is a required field.

Enter the email addresses of the recipients in the **Email addresses** field. If you're entering multiple email addresses, select the Enter key, or add a comma, after each address. There is no limit to the number of recipients that you can add.

Depending on the settings for your Looker instance and your assigned permissions, you may be able to send emails to email addresses that are unassociated with any user account on your Looker instance. These emails are classified as external. The **All** and **External** indicators at the right of the field show both the number of all email recipients and the number of just the external email recipients. Select each indicator to toggle between showing all email recipients and showing only external email recipients. To enable you to deliver content to external users, your Looker admin must have granted you permissions to [deliver content to external users](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_external_look_emails) or have added those recipients' email domains to the [Email Domain Allowlist for Scheduled Content](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content).

If a recipient is another Looker user, that person will see the option to link back to the dashboard from the email, unless your Looker admin has set your Looker instance's [emailed data policy](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails#emailed_data_policy) to [**Send Data Only**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails#send_data_only) or the **Include links** option is deselected.

Emailed deliveries may not exceed 20 MB (for formats that are delivered in the email body) and 15 MB (for formats that are delivered as an attachment).

See the Advanced options section on this page for more information about email deliveries.

#### Webhook

Webhooks are a way to trigger exchanges between internet-based services. With a web service like [Zapier](https://zapier.com), webhooks can let Looker data be delivered to a wide range of applications; for example, you may be able to schedule periodic delivery of a dashboard to a webhook.

To set up a webhook, go to your web service and do the following:

  * Obtain a URL to which Looker should send an HTTPS request.
  * Specify a destination application for your Looker data delivery. The destination application may require additional configuration in order to receive data from Looker.



The exact procedure differs depending on what web service and destination application you're using to deliver the data. See [the Scheduling Looks and Dashboards Using Webhooks](https://discuss.google.dev/t/scheduling-looks-and-dashboards-using-webhooks-3-46/114105) Community post for guidelines on setting up another application to receive the webhook data from Looker.

When **Webhook** is selected in the **Destination** field, a new **Webhook URL** field appears. This is a required field.

Enter the URL where Looker should send an HTTPS request for this delivery in the **Webhook URL** field. You can obtain this URL from the web service you're using to handle your webhook.

**Note:** Looker will attempt delivery to a webhook for a maximum of 30 minutes. Ensure that the destination can respond within 30 minutes to the webhook delivery attempt.

#### Amazon S3

Amazon S3 buckets are a common way to store large amounts of data. You or your company will need to have created an S3 bucket with Amazon before Looker can use it.

When **Amazon S3** is selected in the **Destination** field, several new fields appear and prompt you for information about your Amazon S3 bucket:

  * **Bucket** : The name of your Amazon S3 bucket. This is a required field.
  * **Optional Path** : The folder, if any, that you want to save your data to.
  * **Access Key** : The Access Key ID to your S3 bucket, provided by Amazon. This is a required field.
  * **Secret Key** : The Secret Access Key to your S3 bucket, provided by Amazon. This is a required field.
  * **Region** : The Amazon services region where your S3 bucket is hosted.



Check out the [Scheduling (unlimited) Results to S3](https://discuss.google.dev/t/scheduling-unlimited-results-to-s3/115075) Community post for more details about delivering data using an Amazon S3 bucket.

#### SFTP

Choose **SFTP** in the **Where should this data go?** section to deliver your content to an [SFTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol#Simple_File_Transfer_Protocol) server. Sending results to an SFTP server is a good method to use when your data or visualization is too large to send using email. If you choose this delivery option, Looker prompts you for the SFTP server address, username, and password as described next.

Note the following about SFTP deliveries:

  * To receive SFTP deliveries from Looker, be sure your network admin has added [Looker's IP addresses](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_1:_ip_address_whitelist) to your SFTP server's IP allowlist or inbound traffic rules.
  * When delivering to an SFTP server, only alphanumeric, underscore (_), and hyphen (-) characters are supported in the filename of the delivery. Looker will strip any characters other than `A-Z`, `a-z`, `0-9`, `_` or `-` characters from what you enter in the **Give your schedule a name** field.



When you choose to **SFTP** , Looker prompts you for the URL and login information for the server:

  * **Address** : The URL or IP address of the SFTP server to which you want to send your data. For example:

    * `sftp://files.looker.com/Marketing/In/`
    * `sftp://192.168.0.10/Marketing/In/`

This example URL ends with the `/` character. This indicates that the file will be saved in a folder named `In`. If you leave out the trailing `/`, the file will be saved in the `Marketing` folder, and "`In`" will be prepended to the filename. You must have write access to the folder in which you want to create the file.

  * **Username** and **Password** : Login credentials for the SFTP server

  * **Preferred key exchange algorithm** : This field is optional. To configure it, choose the preferred SSH key exchange algorithm for establishing the connection. The supported options are:

    * `ecdh-sha2-nistp521`
    * `ecdh-sha2-nistp384`
    * `ecdh-sha2-nistp256`
    * `diffie-hellman-group-exchange-sha256`
    * `diffie-hellman-group14-sha256`
    * `diffie-hellman-group14-sha1`

If the connection is not established within five minutes, choose a different algorithm. Some algorithms take a long time to generate an SSH key. This option lets you use an algorithm that might take less time. Choosing one of the algorithms makes it the preferred algorithm for establishing the SSH connection. If the algorithm is not supported by the server, all the other algorithms are used in subsequent attempts. When this field is set to **Default** , the original order of algorithms in the connection library is used.




SFTP support is limited to username and password credentials. SSH private key credentials are not supported.

The host key algorithms supported by Looker SFTP deliveries are as follows:

  * `ssh-ed25519-cert-v01@openssh.com`
  * `ssh-ed25519`
  * `ecdsa-sha2-nistp521-cert-v01@openssh.com`
  * `ecdsa-sha2-nistp384-cert-v01@openssh.com`
  * `ecdsa-sha2-nistp256-cert-v01@openssh.com`
  * `ecdsa-sha2-nistp521`
  * `ecdsa-sha2-nistp384`
  * `ecdsa-sha2-nistp256`
  * `ssh-rsa-cert-v01@openssh.com`
  * `ssh-rsa-cert-v00@openssh.com`
  * `ssh-rsa`
  * `rsa-sha2-256`
  * `rsa-sha2-512`



The encryption algorithms (ciphers) supported by Looker SFTP deliveries are as follows:

  * `aes256-ctr`
  * `aes192-ctr`
  * `aes128-ctr`
  * `aes256-gcm@openssh.com`
  * `aes128-gcm@openssh.com`



The message authentication code algorithms supported by Looker SFTP deliveries are as follows::

  * `hmac-sha2-512-etm@openssh.com`
  * `hmac-sha2-256-etm@openssh.com`
  * `hmac-sha2-512`
  * `hmac-sha2-256`
  * `hmac-sha1`



Looker uploads the file to the specified directory on your SFTP server, using the following convention for the filename:
    
    
    <name>_<timestamp>_<token>.<file extension>
    

  * `<name>` is the name that you provided in the **Give your schedule a name** field, after Looker removes all characters other than `A-Z`, `a-z`, `0-9`, `_` or `-`
  * `<timestamp>` is the timestamp the schedule was sent, in the format `%Y-%m-%dT%H%M`
  * `<token>` is a token that consists of a random six-character string
  * `<file extension>` is the file extension



For example: `Test_Schedule_2019-04-11T1130_HWkvys.csv`

### Integrated service destinations

You can schedule or send dashboard deliveries to a service that is integrated with Looker, such as Slack, Dropbox, Google Drive, and others. Integrations must be [enabled by your Looker admin](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions). Looker admins must specifically give permissions for [users](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#send_to_integration) and [embed users](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#send_to_integration) to send and schedule data to third-party integrations.

When an integrated service is selected in the **Destination** field of the Scheduler, several new fields may appear and prompt you for more information.

The following list shows the Looker Action Hub services to which you can deliver the contents of a dashboard.

Here is how to use the list:

  * The URLs shown in the **Link to README file** column provide instructions for enabling and configuring the integrated service to work with Looker.
  * The URLs shown in the **How to use this integration** column provide instructions for how to send data from Looker to the integrated service. Some of these articles also contain enablement instructions.
  * **Required LookML tags** lists any required tags that must be used with the [`tags`](https://docs.cloud.google.com/looker/docs/reference/param-field-tags) parameter in the content's underlying model.
  * **Action type** indicates what level of data the integrated service is sending: field, query, or dashboard. A field-level action sends the value of a single, specified cell in a data table. A query-level action sends the results of an entire query, such as all rows in an Explore or a Look. A dashboard-level action sends an image of a dashboard.
  * **Uses Google OAuth authentication** indicates whether the integrated service uses Google OAuth credentials for authentication.
  * **Uses data streaming** indicates whether the integrated service supports streamed query results. Dashboards cannot stream data.

Integrated service | Description | Link to README file | How to use this integration | Required LookML tags | Uses Google OAuth authentication (Yes/No) | Uses data streaming (Yes/No)  
---|---|---|---|---|---|---  
Azure Storage | Send and store a data file on Azure Storage. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/azure/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Azure-Storage/td-p/565929) | None | No | No  
DigitalOcean Spaces | Send to and store a data file in DigitalOcean Storage. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/digitalocean/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Digital-Ocean-Storage/td-p/583736) | None | No | No  
Dropbox | Send and store a data file on Dropbox. | No README available | [View documentation](https://docs.cloud.google.com/looker/docs/delivering-dropbox) | None | Yes | No  
Google Cloud Storage | Write data files to a Google Cloud Storage bucket. | [View README on GitHub](https://github.com/looker-open-source/actions/blob/master/src/actions/google/gcs/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Administering-Looker/Looker-Actions-Google-Cloud-Storage/td-p/591972) | None | No | No  
Google Drive | Send data to Google Drive. | No README available | [View documentation](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-google-drive-integration) | None | Yes | No  
SendGrid | Send data and schedule results to send to a email address using SendGrid's API. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/sendgrid/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Sendgrid/td-p/591971) | None | No | No  
Slack | Send Looker content in direct messages, public channels, and private channels in Slack using OAuth. It is available for Looker-hosted deployments on 6.24+ with the [IP Allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist\)) feature disabled. | No README available | [View documentation](https://docs.cloud.google.com/looker/docs/scheduling-slack) | None | Yes | No  
Slack Attachment (API Token) | Send data directly into a Slack channel along with user credentials. You may also want to reference [Lookerbot documentation](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-lookerbot-for-slack) for additional Slack functionality. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/slack/legacy_slack/README.md) | [View documentation](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-looker-slack-attachment-api-token-action) | None | No | No  
Teams — Incoming Webhook | Send data to Microsoft Teams using an incoming webhook. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/teams/README.md) | See README | None | No | No  
  
### Format

The **Format** field contains a drop-down menu of available formats:

  * **CSV zip file** : The unformatted data from the dashboard delivered as a collection of comma-separated values (CSV) files in a zipped directory. For deliveries to email, the ZIP file is delivered as an email attachment.
  * **PDF** : An image of the dashboard as a single PDF file. The default layout displays tiles as they are arranged in the dashboard, but other layout and sizing options are available under **Advanced options**. For deliveries to email, the file is delivered as an email attachment.

**Important** : Starting in Looker 26.4, table charts, scatterplot charts, and Google Maps charts that have [increased row limits](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits) are subject to the following limitations when you download, send, or schedule dashboards in PDF format: 
    * The query results for each table chart on a dashboard will display up to 50,000 rows, to a maximum total limit of 200,000 cells per dashboard. 
    * If the combined total of cells for table charts on a dashboard is greater than 200,000 cells, table chart results may be trimmed. If the maximum is reached, users will see a warning that will also be displayed at the bottom of the rendered PDF. 
    * Table charts on a dashboard PDF will display more rows than are displayed on the dashboard tile thumbnail only when the **Expand tables to show all rows** option is selected. 
    * Scatterplot charts and Google Maps charts support up to 50,000 data points (rows) in PDF downloads. The charts will render as the they appear in the tile thumbnail, [or fail](https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-chromium-renderer) based on standard renderer limitations. 
  * **PNG visualization** : An image of the dashboard as a single PNG file. The default layout displays tiles as they are arranged in the dashboard, but other layout options are available under **Advanced options**. For deliveries to email, the image appears inline within the body of the email.


**Note:** If you have selected email as a destination and your Looker admin has set your Looker instance's [emailed data policy](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails#emailed_data_policy) to [**Send Link Only**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails#send_link_only), the option to select a data format is not available.

### Download Tabs

If your [dashboard has tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards), you can select an option from the **Download Tabs** menu when downloading a dashboard as a PDF. You can choose to send the entire dashboard, the tab that is open, or a custom selection of tabs. If you choose **Custom** , you can specify the tabs to download in the **Select Tabs** field. If multiple tabs are selected (for example, if **Whole dashboard** , or if one or more tabs are specified for the **Custom** option), all tabs will appear on the same page. The contents of each tab will be organized under a content header with the name of the tab.

### Advanced options

The **Advanced options** tab provides additional customization for your delivery. The options available depend on the selected destination and format of your delivery.

#### Custom message

This option is available only for the email destination.

Enter a message you would like included in the body of emails to recipients. Looker limits the number of characters in a custom message to 1,500.

#### Run schedule as recipient

This option is available only for the email destination.

The **Run schedule as recipient** option lets users specify a list of recipients who will each receive the content delivery as if each one of them had run the query, based on each person's permissions. This means that each user's [access filters](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) and [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) will be applied to the data that is included in each email.

If a user is a Looker admin, the **Run schedule as recipient** option lets the admin specify a list of users who will each receive the content delivery as if each one of them ran the query, based on each person's permissions. Non-admin users may also enter their own email address to receive a delivery as if they had queried the content, based on their permissions. This means that each user's [access filters](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) and [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) will be applied to the data that is included in each email.

In the following example, a Looker admin needs to schedule a data delivery that lists counts of users per state.

![](https://docs.cloud.google.com/static/looker/docs/images/delivery-run-as-recip-full-2316.png)

User A has an access filter set as `users.state = 'California'`. When **Run schedule as recipient** is selected, the scheduled query will apply the access filter `users.state = 'California'` and send filtered results to user A. The filtered results will include data only about California.

![](https://docs.cloud.google.com/static/looker/docs/images/delivery-run-as-recip-access-filter-2308.png)

In the **Advanced options** tab, select the **Run schedule as recipient** checkbox and then add email addresses for your recipients in the **Email addresses** text field under the **Settings** tab. This option takes into account the permissions of the user creating the schedule as well as the types of email addresses added to the **Email addresses** field. In some cases, the **Run schedule as recipient** option is not available:

  * When a user adds the email of a disabled user
  * When a user adds an email that does not belong to a Looker user, as indicated by the **External** count next to the list of email addresses.

![An example schedule showing the External count of email addresses for recipients who are not Looker users.](https://docs.cloud.google.com/static/looker/docs/images/schedule-send-window-external-2220.png)




In these situations, regardless of whether you selected an option before or after you entered the external email address, the **Run schedule as recipient** option will remain enabled, but the schedule cannot be saved until you deselect **Run schedule** as recipient or remove the external email address from the list of recipients.

In the special case where a user is listed as a recipient on a schedule that has **Run schedule as recipient** enabled and then that user's account is disabled, the schedule will fail to deliver to the disabled user starting the next time it runs. If that user's account is deleted, the entire schedule will fail to deliver to any recipients. A Looker admin or user with the `see_schedules` permission will be able to diagnose this failure in the **Scheduler History** page in the **Admin** panel.

#### Include links

This option is available only for the email destination.

If your Looker admin has set your Looker instance's [emailed data policy](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails#emailed_data_policy) to [**Send Links and Data**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails#send_links_and_data), the **Schedule Delivery** or **Send** window displays the **Include links** option. Select this option to include in the data delivery emails a **View full dashboard** link that goes to the dashboard in Looker. Dashboard links don't include any [`hide_filter` parameters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#hiding_dashboard_filters).

Recipients must log in to Looker and have permissions to access the models on which the delivered dashboard is based to view that content in Looker. If you want to remove this link from your data delivery emails, clear the **Include links** checkbox.

#### Include custom link

This option is available only for the email destination, and only for embedded dashboards. It is displayed when the **Include links** option is selected.

The **Include custom link** option lets you configure a custom URL to which the **View full dashboard** link will connect, instead of linking to the dashboard in Looker. You can also optionally change the **View full dashboard** link text.

To use this option, a Looker admin or a user with either the `schedule_look_emails` or the `create_alerts` permission first must specify allowed domains for the custom link and select the format of the custom link URL in the [**Embed**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#alerts_and_scheduling_custom_url) page in the **Admin** menu.

##### Domain

Select the URL domain from the list of domains configured on the [allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#embed_domain_for_schedules_and_alerts_allowlist). For example, `app.customer.com`.

##### Path

The **Path** option is displayed only if **User defined URL** is selected in the **Select content path** field on the [**Embed**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#alerts_and_scheduling_custom_url) page in the **Admin** menu.

Enter a custom path for the link URL here. For example, if you want your custom link to point to the URL `app.customer.com/my_embed_app`, enter the path `/my_embed_app` here.

##### URL label

Use this field to enter new link text, which will replace the text **View full dashboard** in email deliveries. This field will display any text that is entered in the **URL label** field in the [**Embed**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#alerts_and_scheduling_custom_url) page in the **Admin** menu by default and can be changed in this field.

#### Results

This field is available only for CSV ZIP file formats of dashboard deliveries. It contains two options: **With visualizations options applied** or **As displayed in the data table**. You can choose one or the other.

Choose the **With visualizations options applied** option to apply some of the visualization settings from the dashboard tiles to your dashboard delivery. This causes the files in your delivery to appear similar to [table charts](https://docs.cloud.google.com/looker/docs/legacy-table-options). Any of the following settings in the [**Plot**](https://docs.cloud.google.com/looker/docs/legacy-table-options#plot_menu_options), [**Series**](https://docs.cloud.google.com/looker/docs/legacy-table-options#series_menu_options), and [**Formatting**](https://docs.cloud.google.com/looker/docs/legacy-table-options#formatting_menu_options) menus that are configured for a visualization will be applied to the data delivery:

  * [Show Row Numbers](https://docs.cloud.google.com/looker/docs/legacy-table-options#show_row_numbers)
  * [Hide Totals](https://docs.cloud.google.com/looker/docs/legacy-table-options#hide_totals)
  * [Hide Row Totals](https://docs.cloud.google.com/looker/docs/legacy-table-options#hide_row_totals)
  * [Limit Displayed Rows](https://docs.cloud.google.com/looker/docs/legacy-table-options#limit_displayed_rows) to a maximum of 500 rows shown or hidden
  * [Show Full Field Name](https://docs.cloud.google.com/looker/docs/legacy-table-options#show_full_field_name)
  * [Custom labels](https://docs.cloud.google.com/looker/docs/legacy-table-options#customizations) for each column



Choose the **As displayed in the data table** option to deliver the data as it appears in the data table of each dashboard tile's **Explore from here** window.

#### Values

This field is available only for CSV ZIP file formats of dashboard deliveries. It contains two options: **Formatted** or **Unformatted**. You can choose one or the other.

  * Select **Formatted** if you want the data to appear similar to how it appears in the [**Explore** experience](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_page) in Looker, although some features (such as [linking](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#using_links_and_actions)) aren't supported by all file types.
  * Select **Unformatted** if you don't want to apply any special formatting of your query results, such as rounding long numbers or adding special characters, that your Looker developers may have put in place. This is often preferred when data is being fed into another tool for processing.



#### Expand tables to show all rows

This option is available only for PDF formats of dashboard deliveries.

Select the **Expand tables to show all rows** box to display all rows of any table visualizations in the dashboard — rather than just those rows that display in the dashboard tile thumbnails.

Starting in Looker 26.4, the query results for each table chart on a dashboard PDF can display up to 50,000 rows, to a maximum total limit of 200,000 cells per dashboard, if your admin has [increased the row limit setting](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits). If the combined cell total for the table charts on a dashboard is greater than 200,000 cells, table chart results may be trimmed. If this maximum is reached, users will see a warning that will also be displayed at the bottom of the rendered PDF.

If the **Expand Tables to Show All Rows** option is selected, dashboard tiles that contain table visualizations may look slightly different in delivered PDFs than they do inside Looker. The following differences may be noticeable in the PDF:

  * Customizations to background colors and font sizes are removed from column headers and subtotal rows.
  * Tables appear in the [white theme](https://docs.cloud.google.com/looker/docs/table-options#table_theme).
  * The [sort icon](https://docs.cloud.google.com/looker/docs/table-options#sorting_columns) does not appear on pivoted tables that were not manually sorted.
  * Tables with [**Size Columns to Fit**](https://docs.cloud.google.com/looker/docs/table-options#size_columns_to_fit) enabled stretch to the full width of the tile.
  * Tables with [row grouping](https://docs.cloud.google.com/looker/docs/table-options#grouping-menu-options) enabled appear as flat data, and the grouping column expands to display all columns.



Additionally, for tables with more than 20,000 cells, the following differences may be noticeable in the PDF:

  * [Conditional formatting](https://docs.cloud.google.com/looker/docs/table-options#enable_conditional_formatting) options other than **Background color** no longer appear.
  * [Cell visualizations](https://docs.cloud.google.com/looker/docs/table-options#cell_visualization) on numeric columns no longer appear.



If you don't see the **Expand tables to show all rows** option when you've chosen **PDF** in the **Format** field, talk to your Looker admin about installing the appropriate version of the [Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium) for your Looker instance.

#### Arrange dashboard tiles in a single column

This option is available only for the PDF and PNG visualization formats of dashboard deliveries. When Slack is selected as the delivery destination only PDFs are supported.

Select the **Arrange dashboard tiles in a single column** box to format your PDF or your PNG visualization in a single column layout. This layout displays dashboard tiles in a single vertical column. Leave the box unchecked to show the tiles as they are arranged in the dashboard.

### Paper size

This option is available only for PDF formats of dashboard deliveries.

You have the option to specify the optimal size and orientation of dashboard PDFs by selecting from the **Paper size** drop-down menu. Large visualizations or groups of overlapping dashboard tiles may need to be resized to fit cleanly on a PDF page. If you don't see the **Paper size** option, talk to your Looker admin about installing the latest version of the [Chromium renderer](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium) for your Looker instance.

#### Table resolution

This option is available only for the PNG visualization format and when the **Arrange dashboard tiles in a single column** box is checked.

You can customize the width of your visualization by using the **Table resolution** drop-down menu. Your width options are:

  * **Normal** : 800 pixels
  * **Wide** : 1680 pixels



For deliveries to email, if you choose **Wide** and the visualization width exceeds the limit set by your email client, email delivery recipients may need to scroll horizontally to see the entire visualization.

#### Delivery time zone

By default, Looker uses the time zone associated with your account to determine when to send your data delivery. If you don't have a time zone associated with your account, Looker uses your [Application Time Zone](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#application_time_zone) setting.

If you want to specify a different time zone, select the time zone from the drop-down menu. The time zone you select does not affect the data in your Look or dashboard, just the timing of the delivery.

### Filters

The **Filters** tab in the **Schedule Delivery** or **Send** window shows any filters applied to the dashboard as well as their values. In this tab, you can edit the values for any existing filters applied to the dashboard, and the new values will be applied to the delivery. The dashboard itself won't be affected.

You cannot add filters to your schedule in the **Filters** tab, only view and edit the values for existing dashboard filters.

For example, you might send regional teams results that are filtered for their states of interest.

![](https://docs.cloud.google.com/static/looker/docs/images/dash-beta-schedule-filters-2308.png)

If a dashboard filter [requires](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#requiring_a_filter_value) a filter value, you must enter a value in the **Filters** tab to create or save any edits to the delivery.

#### When dashboard filters change

Sometimes dashboard filters change after a schedule is created. The following table explains how that affects filters applied to the scheduled deliveries.

Action | Effect on Schedule Filter  
---|---  
A schedule is created with a filter. Later, the filter value is changed on the dashboard. | No effect on the schedule filter value. It remains the value set in the **Filters** tab, even if that value is **is any value**.  
A schedule is created with a filter. Later, the filter is renamed in the dashboard. | The filter is removed from the delivered data.  
A schedule is created with a filter. Later, the filter is deleted in the dashboard. | The filter is removed from the delivered data.  
A schedule is created. Later, a new (non-required or [required](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#requiring_a_filter_value)) filter is added to the dashboard. | The filter is applied to the delivered data, using the filter value set in the **Filters** tab. If no value is set in the **Filters** tab, the value is interpreted as **is any value** , essentially removing the filter.  
  
**Note:** Dashboard filters that are renamed in or removed from a dashboard are no longer applied to delivered data. Schedule creators should be aware that renaming or removing filters could cause deliveries to expose unfiltered data.

#### Using user attribute filters

If your Looker admin has configured user-specific values, called user attributes, and you have edit privileges for a dashboard, you can create a dashboard filter that uses the [**matches a user attribute** filter option](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#matches_a_user_attribute). A filter of this type automatically customizes the filter value for each dashboard viewer. With this kind of filter, you can deliver customized results to each delivery's recipients. To read more about user attributes, visit the [User attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) documentation page.

### Testing a schedule

If you set the **Recurrence** field to anything other than **Send now** , a **Test now** button appears at the bottom of the **Schedule Delivery** or **Send** window.

**Note:** The **Test now** button won't appear for users whose accounts don't have an associated email address. In addition, [embed](https://docs.cloud.google.com/looker/docs/signed-embedding) users, who often lack associated emails, won't see the **Test now** button.

Select the **Test now** button to send a one-time test delivery of the schedule only to yourself. A green checkmark appears to confirm that a test has been sent. If the **Test now** button is not available, you can set the **Recurrence** field to **Send now** to send a one-time test delivery.

The **Test now** option doesn't take into account some **Advanced options** settings, but does respect any selected filters.

### Saving a schedule or sending now

If you set the **Recurrence** field to **Send now** , select the **Send now** button at the bottom of the window for a one-time delivery to the listed destination.

If you set the **Recurrence** field to anything other than **Send now** , select the **Save** button to save your schedule and close the window.

Select the **Cancel** button to exit the window without saving or sending the schedule.

Your saved schedules for a dashboard appear in its existing schedules window. Your saved schedules for all content appear on the [**Schedules** page](https://docs.cloud.google.com/looker/docs/user-schedules) of your user profile.

## Editing a schedule

You can edit only the schedules you have created. To edit a schedule:

  1. Select the three-dot **Dashboard actions** menu at the top right of the dashboard.
  2. Select **Schedule delivery** from the drop-down menu.
  3. In the existing schedules window, select the three-dot menu that applies to the schedule that you want to edit.
  4. Choose **Edit** from the drop-down menu.
  5. The **Schedule Delivery** or **Send** window appears for that schedule. Make your edits in this window.
  6. Select **Save** when your edits are complete, or select **Cancel** to cancel your edits.



## Duplicating a schedule

You may want to duplicate a schedule and then edit it. To duplicate a schedule:

  1. Select the three-dot **Dashboard actions** menu at the top right of the dashboard.
  2. Select **Schedule delivery** from the drop-down menu.
  3. In the existing schedules window, select the three-dot menu that applies to the schedule that you want to edit.
  4. Choose **Duplicate** from the drop-down menu.
  5. The **Schedule Delivery** or **Send** window appears for the duplicate schedule. "Copy" is appended to the schedule name.
  6. Make your edits.
  7. Select **Save** when your edits are complete, or select **Cancel** to cancel your edits and delete the duplicated schedule.



The original schedule remains unchanged when you make a duplicate.

The filters in a duplicate schedule will be set to the same values as are present in the **Filters** tab of the original schedule, although you can edit these values. If any filters have changed since the creation of the original schedule, the filters will be affected as shown in the **When dashboard filters change** section. If a required filter was later added to the dashboard that the original schedule is based on, you need to select a value for that filter before saving the duplicated schedule.

## Deleting a schedule

You can delete only the schedules you have created. To delete a schedule:

  1. Select the three-dot menu at the top right of the dashboard.
  2. Select **Schedule delivery** from the drop-down menu.
  3. In the existing schedules window, select the three-dot menu that applies to the schedule that you want to edit.
  4. Choose **Delete** from the drop-down menu.
  5. A new window appears. Select **Delete** to delete the schedule, or select **Cancel** to keep the schedule.



You can also delete a schedule from the [**Schedules** page](https://docs.cloud.google.com/looker/docs/user-schedules) of your user profile.

## Effects of deleting a dashboard that has a schedule

If you delete a dashboard, any schedules that are affiliated with that dashboard will also be deleted. The schedule owner will see immediately that the name of the dashboard has been deleted for the schedule or **Schedules You've Created** user page. After the next time the schedule query runs, its status will show as **Disabled**.

## Scheduling challenges

**Note:** Looker schedules data deliveries according to the time zone that is indicated in the [**Application Time Zone**](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#application_time_zone) setting on the Admin **Settings** page, or, if enabled, the schedule creator's [User Specific Time Zone](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#user_specific_time_zones) setting.

At times a scheduled email delivery could fail to reach one or more of its recipients. This could happen if the underlying model has an error, if the recipient does not have access to the data, or if there are rendering problems or page errors.

Note the following limitations of content delivery:

  * If your company has set up its own [email settings](https://docs.cloud.google.com/looker/docs/admin-panel-platform-smtp) in the **Admin** section of Looker, your Looker admins will need to make sure that the settings are correct and that your email provider is functioning properly. An external SMTP server may have its own daily or per-message recipient limits.
  * Depending on the **Limit** setting, the data delivery will be limited either to 5,000 rows or to a maximum file size of 15 MB for email with attachments and 20 MB for emails with inline content. Emails with more rows or data than these limits won't be sent.
  * Although Looker doesn't hardcode a limit for the number of recipients that you can specify in an email delivery, if you configure your delivery to "Run as recipient," the delivery triggers a separate query for each individual. This load can severely impact database performance and is not recommended for large recipient lists. We recommend using email groups or aliases whenever possible.
  * If an email does not send at the expected time — but does eventually arrive — it is likely because you're competing with other Lookertasks. These tasks can include other scheduled emails, many people exploring data at the same time, or persistent derived tables being built. If this happens, check with your Looker admins about competing tasks.
  * If a specific email keeps disappearing from your distribution list, it's likely because a user is unsubscribing from that scheduled email. This can be a particular challenge if you use a group email alias to send to multiple people, because any individual recipient can unsubscribe that entire email alias. For more information about un-subscriptions, see this Looker Community post on [monitoring scheduler unsubscribe events](https://discuss.google.dev/t/monitoring-scheduler-unsubscribe-events/116204).



If your delivery to an SFTP server fails, consider the following possibilities:

  * When Looker attempts to deliver to an SFTP server, the delivery might be marked as completed in the schedule panel and logs even if it fails to arrive because of network configuration issues, such as an incorrect IP allowlist on the destination server or a closed outbound port on the Looker instance. Because the schedule history might show a `Success` status despite these errors, always check your destination SFTP server logs if you suspect that a delivery is missing.

  * Looker stores [SFTP fingerprints](https://docs.cloud.google.com/looker/docs/managing-business-user-features#storing_sftp_fingerprints) for your SFTP server. If you encounter errors with your SFTP delivery, the SFTP fingerprints could be invalid. In this case, contact your Looker admin.

  * The error `Net::SSH::Exception. message: could not settle on host_key algorithm` is caused by an incompatibility between the host key algorithms that are offered by older Looker versions (earlier than Looker 26.2) and the modern security algorithms that are strictly enforced by the target SFTP server (such as Red Hat 9 or Azure Blob Storage SFTP). If you receive this error, you can resolve it by upgrading Looker to version 26.2 or later to support modern SHA-2 algorithms (like `ecdsa-sha2-nistp256`, `rsa-sha2-256`, and `rsa-sha2-512`). Alternatively, configure the target SFTP server to allow at least one host key or encryption algorithm that's supported by your current version of Looker.

  * The error `OpenSSL::Cipher::CipherError. Error: authentication tag already generated by cipher` may occur when data is delivered with SFTP after Looker has been upgraded to version 26.2.14 or later, or when your instance connects to host services like Azure Blob Storage SFTP or through a proxy. This error is caused by a known JRuby issue during cipher negotiation. To resolve this error, restrict the encryption algorithms (ciphers) that are allowed on the destination SFTP server to `aes256-ctr`. For example, edit the SFTP server's `sshd_config` file to add or restrict the `Ciphers` directive: `Ciphers aes256-ctr`.

  * If you receive the error `Java::JavaLang::NullPointerExceptions` when you're delivering data to an SFTP server, this error may be caused by a [bug in JRuby](https://github.com/jruby/jruby-openssl/issues/105) that prevents the use of [elliptic-curve (EC) algorithms](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) or host keys for SSH connections from Looker to SFTP destinations. To avoid issues with sending data to SFTP destinations, don't use EC algorithms in the `~/.ssh/config` or `/etc/ssh_config` files or store EC host keys in `~/.ssh` on your Looker host.

  * The error `Net::SFTP::StatusException (2, 'no such file')` occurs if Looker cannot correctly construct the destination path on the SFTP server. Common causes include the **Address** field using a relative path instead of an absolute path, the **Address** field missing a trailing slash (`/`), or the Look, dashboard, or schedule name containing spaces or special characters (such as `/`) that cause path construction failures. To resolve this error, follow these steps:

    * Use absolute paths: Log in to the SFTP server, run `pwd` to retrieve the full absolute path, and enter this value in the **Address** field of your schedule, ensuring that it ends with a trailing slash (`/`).
    * Remove special characters: Remove forward slashes (`/`) from Look, dashboard, and schedule names.
    * Use machine-friendly names: Rename the schedule to use underscores instead of spaces (for example, `Report_Name`).
  * The error `Net::SSH::Exception. Error: could not settle on kex algorithm` occurs when Looker and the remote SFTP server cannot agree on a mutually supported key exchange (KEX) algorithm, usually because deprecated algorithms are being used on one side. To resolve this error, review the key exchange algorithms that are supported by your SFTP server and ensure that they align with Looker's supported KEX algorithms (such as `ecdh-sha2-nistp256`, `ecdh-sha2-nistp384`, or `ecdh-sha2-nistp521`).

  * If your scheduled SFTP delivery fails with the error `Net::SSH::Exception: could not settle on encryption_client algorithm`, your SFTP server and Looker couldn't agree on a shared encryption cipher. Looker has removed support for older, less secure ciphers such as CBC (for example, `aes256-cbc` and `3des-cbc`). To resolve this error, provide this error message to your SFTP server administrator and ask them to update the server's `sshd_config` file to enable support for at least one of the encryption and key exchange algorithms that are compatible with Looker.




## Delivery considerations for admins

Looker admins can see, edit, reassign, and delete any users' schedules. Additionally, Looker admins should bear some things in mind when setting up data delivery for their Looker instance and granting users permissions to send or schedule data deliveries. For more information, visit the following documentation pages:

  * [Admin settings - Schedules](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule)
  * [Admin settings - Schedule History](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule-history)
  * [Managing business user features](https://docs.cloud.google.com/looker/docs/managing-business-user-features#sharing_content)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
