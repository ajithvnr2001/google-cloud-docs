---
url: https://docs.cloud.google.com/build/docs/configuring-notifications/automate/
title: Automating configuration for notifications \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:01.981914+00:00
---

# Automating configuration for notifications  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-notifications/automate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Automating configuration for notifications Stay organized with collections  Save and categorize content based on your preferences. 

You can configure Cloud Build to send you build notifications to Slack, Google Chat, an SMTP server, an HTTP endpoint, or a BigQuery instance using [Cloud Build notifiers](http://github.com/GoogleCloudPlatform/cloud-build-notifiers). This page explains how you can automate the configuration process for your desired notifier.

## Automating notification configuration

Cloud Build provides a [setup script](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/setup.sh) that you can use to automate notification configuration. To configure notifications using the setup script:

### Slack

### Setting up

The following sections describe steps you need to complete before automating notification configuration for your notifier.

#### Enabling APIs

Enable the Cloud Build, Compute Engine, Cloud Run, Pub/Sub, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,compute.googleapis.com,run.googleapis.com,pubsub.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/configuring-notifications/automate)

#### Obtaining and storing credentials

  1. Create a [Slack app](https://api.slack.com/apps?new_app=1) for the Slack workspace to which you want to send notifications.

  2. Activate [incoming webhooks](https://api.slack.com/messaging/webhooks) to post messages from Cloud Build to Slack.

  3. Navigate to your Slack app to locate the URL for the incoming webhook. Your URL will look similar to the following:
         
         http://hooks.slack.com/services/...
         

  4. Store your incoming webhook URL in Secret Manager:

     1. Open the Secret Manager page in the Google Cloud console:

[Open the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

     2. Click **Create secret**.

     3. Enter a name for your secret.

     4. Under **Secret value** , add your incoming webhook URL for your Slack app.

     5. To save your secret, click **Create secret**.




#### Writing a notifier configuration file

Write a notifier configuration file to configure your Slack notifier and filter on build events:

In the following example notifier configuration file, the `filter` field uses [Common Expression Language](https://github.com/google/cel-spec) with the available variable, `build`, to filter build events with a `SUCCESS` status:
    
    
      apiVersion: cloud-build-notifiers/v1
      kind: SlackNotifier
      metadata:
        name: example-slack-notifier
      spec:
        notification:
          filter: build.status == Build.Status.SUCCESS
          delivery:
            webhookUrl:
              secretRef: webhook-url
          template:
            type: golang
            uri: gs://example-gcs-bucket/slack.json
        secrets:
        - name: webhook-url
          value: projects/project-id/secrets/secret-name/versions/latest
    

Where:

  * `webhook-url` is the configuration variable used in this example to reference the Slack webhook URL path stored in Secret Manager. The variable name you specify here should match the `name` field under `secrets`.
  * `project-id` is the ID of your Google Cloud project.
  * `secret-name` is the name of your secret that contains your Slack webhook URL.
  * The `uri` field references the `slack.json` file. This file contains a JSON template hosted on Cloud Storage and represents your notification message to your Slack space.



To view the example, see the [notifier configuration file](http://github.com/GoogleCloudPlatform/cloud-build-notifiers/tree/master/slack/slack.yaml.example) for the Slack notifier.

### Running the automation script

To automate notification configuration for your notifier:

  1. Clone the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers).

  2. Configure the Google Cloud CLI with your project ID and region: 
         
         gcloud config set project project-id
         gcloud config set run/region region
         

Where:

     * `project-id` is your Google Cloud project ID.
     * `region` is the [region](https://docs.cloud.google.com/build/docs/locations) to deploy the notifier.
  3. Run the following command in the root of the repository:



    
    
        ./setup.sh slack config-path -t template-path -s secret-name
    

Where:

  * `config-path` is the path to your notifiers configuration file.
  * `template-path` is the path to your notifiers template file. Your notifiers template file contains the JSON template hoted on Cloud Storage and represents your notification message. You can include your notifiers template file as a path using this variable or within the `uri` field of your notifiers configuration file. 
  * `secret-name` is the name of your secret stored in Secret Manager.




After running the script, you will see the following message:
    
    
    ** NOTIFIER SETUP COMPLETE **
    

Your notifier is now set up. You can view the complete script in the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers) or run `./setup.sh --help` for usage instructions associated with the script.

### SMTP

### Setting up

The following sections describe steps you need to complete before automating notification configuration for your notifier.

#### Enabling APIs

Enable the Cloud Build, Compute Engine, Cloud Run, Pub/Sub, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,compute.googleapis.com,run.googleapis.com,pubsub.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/configuring-notifications/automate)

#### Storing credentials

  1. Store the sender's email account password in Secret Manager:

  2. Open the Secret Manager page in the Google Cloud console:

[Open the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

  3. Click **Create secret**.

  4. Enter a name for your secret.

  5. Under **Secret value** , add the sender's email account password.

  6. To save your secret, click **Create secret**.




#### Writing a notifier configuration file

Write a notifier configuration file to configure your SMTP notifier and filter on build events:

In the following example notifier configuration file, the `filter` field uses [Common Expression Language](https://github.com/google/cel-spec) with the available variable, `build`, to filter build events with a `SUCCESS` status:
    
    
     apiVersion: cloud-build-notifiers/v1
     kind: SMTPNotifier
     metadata:
       name: example-smtp-notifier
     spec:
       notification:
         filter: build.status == Build.Status.SUCCESS
         delivery:
           server: server-host-name
           port: "port"
           sender: sender-email
           from: from-email
           recipients:
             - recipient-email
             # optional: more emails here
           password:
             secretRef: smtp-password
          template:
            type: golang
            uri: gs:example-gcs-bucket/smtp.html
       secrets:
       - name: smtp-password
         value: projects/project-id/secrets/secret-name/versions/latest
    

Where:

  * `server-host-name` is the address of your SMTP server.
  * `port` is the port that will handle SMTP requests. This value should be specified as a string.
  * `sender-email` is the email address of the sender account that is seen by the specified server-host-name.
  * `from-email` is the email address that is seen by recipients.
  * `recipient-email` is a list of one or more email addresses to receive messages from the sender.
  * `smtp-password` is the configuration variable used in this example to reference the sender's email account password stored in Secret Manager. The variable name you specify here should match the `name` field under `secrets`.
  * `project-id` is the ID of your Google Cloud project.
  * `secret-name` is the name of your secret that contains the password to the sender's email account.
  * The `uri` field references the `smtp.html` file. This files refers to a html template hosted on Cloud Storage and represents your notification email.



To view the example, see the [notifier configuration file](http://github.com/GoogleCloudPlatform/cloud-build-notifiers/tree/master/smtp/smtp.yaml.example) for the SMTP notifier.

### Running the automation script

To automate notification configuration for your notifier:

  1. Clone the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers).

  2. Configure the Google Cloud CLI with your project ID and region: 
         
         gcloud config set project project-id
         gcloud config set run/region region
         

Where:

     * `project-id` is your Google Cloud project ID.
     * `region` is the [region](https://docs.cloud.google.com/build/docs/locations) to deploy the notifier.
  3. Run the following command in the root of the repository:



    
    
        ./setup.sh smtp config-path -t template-path -s secret-name
    

Where:

  * `config-path` is the path to your notifiers configuration file.
  * `template-path` is the path to your notifiers template file. Your notifiers template file contains the JSON template hoted on Cloud Storage and represents your notification message. You can include your notifiers template file as a path using this variable or within the `uri` field of your notifiers configuration file. 
  * `secret-name` is the name of your secret stored in Secret Manager.




After running the script, you will see the following message:
    
    
    ** NOTIFIER SETUP COMPLETE **
    

Your notifier is now set up. You can view the complete script in the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers) or run `./setup.sh --help` for usage instructions associated with the script.

### BigQuery

### Setting up

The following sections describe steps you need to complete before automating notification configuration for your notifier.

#### Enabling APIs

Enable the Cloud Build, Cloud Run, Pub/Sub, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,pubsub.googleapis.com,bigquery.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/configuring-notifications/automate)

#### Granting permissions

Give your Cloud Run service account permission to create and write BigQuery tables and permission to fetch Artifact Registry data related to your build:

  1. Go to the IAM page in the Google Cloud console:

[Open the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Locate the **Compute Engine default service account** associated with with your project:

Your **Compute Engine default service account** will look similar to the following, where project-number is your project number:
         
         project-number-compute@developer.gserviceaccount.com
         

  3. Click on the pencil icon in the row containing your **Compute Engine default service account**.

You will see the **Edit access** tab.

     1. Click **Add another role**.

     2. Add the following roles:

        * **Artifact Registry Reader**
        * **BigQuery Data Editor**

The **Artifact Registry Reader** role enables you to fetch data for your images. The **BigQuery Data Editor** gives you read and write access to your data.

     3. Click **Save**.




#### Writing a notifier configuration file

Write a notifier configuration file to configure your BigQuery notifier and filter on build events:

In the following example notifier config file, the `filter` field uses [Common Expression Language](https://github.com/google/cel-spec) with the variable, `build`, to filter build events with a specified trigger ID:
    
    
     apiVersion: cloud-build-notifiers/v1
     kind: BigQueryNotifier
     metadata:
       name: example-bigquery-notifier
     spec:
       notification:
         filter: build.build_trigger_id == "123e4567-e89b-12d3-a456-426614174000"
         delivery:
           table: projects/project-id/datasets/dataset-name/tables/table-name
         template:
           type: golang
           uri: gs://example-gcs-bucket/bq.json
    

Where:

  * `project-id` is the ID of your Google Cloud project.
  * `dataset-name` is the name you want to give your dataset.
  * `table-name` is the name you want to give your table.



The table-name in your notifier config file can refer to:

  * a nonexistent table
  * an empty table without a schema
  * an existing table with a schema that matches the schema specifications in the BigQuery notifier

**Note:** References to an existing table with a schema specification not matching the BigQuery notifier will result in an error.
  * The `uri` field references the `bq.json` file. This file refers to a JSON template hosted on Cloud Storage and represents the information to insert into your bigquery table.




To view the example, see the [notifier config file](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/bigquery/bigquery.yaml.example) for the BigQuery notifier.

### Running the automation script

To automate notification configuration for your notifier:

  1. Clone the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers).

  2. Configure the Google Cloud CLI with your project ID and region: 
         
         gcloud config set project project-id
         gcloud config set run/region region
         

Where:

     * `project-id` is your Google Cloud project ID.
     * `region` is the [region](https://docs.cloud.google.com/build/docs/locations) to deploy the notifier.
  3. Run the following command in the root of the repository:
         
         ./setup.sh bigquery -t config-path -t template-path
         

Where:

     * `config-path` is the path to your notifiers configuration file.
     * `template-path` is the path to your notifiers template file. Your notifiers template file contains the JSON template hoted on Cloud Storage and represents your notification message. You can include your notifiers template file as a path using this variable or within the `uri` field of your notifiers configuration file.

After running the script, you will see the following message:
    
    ** NOTIFIER SETUP COMPLETE **
    

Your notifier is now set up. You can view the complete script in the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers) or run `./setup.sh --help` for usage instructions associated with the script.




### HTTP

### Setting up

The following sections describe steps you need to complete before automating notification configuration for your notifier.

#### Enabling APIs

Enable the Cloud Build, Cloud Run, and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com,pubsub.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/configuring-notifications/automate)

#### Writing a notifier configuration file

Write a notifier configuration file to configure your HTTP notifier and filter on build events:

In the following example notifier configuration file, the `filter` field uses [Common Expression Language](https://github.com/google/cel-spec) with the available variable, `build`, to filter build events with a `SUCCESS` status:
    
    
        apiVersion: cloud-build-notifiers/v1
        kind: HTTPNotifier
        metadata:
          name: example-http-notifier
        spec:
          notification:
            filter: build.status == Build.Status.SUCCESS
            delivery:
              # The `http(s)://` protocol prefix is required.
              url: url
            template:
              type: golang
              uri: gs://example-gcs-bucket/http.json
    

Where:

  * `url` is the configuration variable used in this example to specify the URL for your request.
  * url is the URL you want to specify as your recipient server.
  * The `uri` field references the `http.json` file. This file refers to a JSON template hosted on Cloud Storage and represents the json payload to the webhook endpoint.



To view the example, see the [notifier configuration file](http://github.com/GoogleCloudPlatform/cloud-build-notifiers/tree/master/http/http.yaml.example) for the HTTP notifier.

### Running the automation script

To automate notification configuration for your notifier:

  1. Clone the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers).

  2. Configure the Google Cloud CLI with your project ID and region: 
         
         gcloud config set project project-id
         gcloud config set run/region region
         

Where:

     * `project-id` is your Google Cloud project ID.
     * `region` is the [region](https://docs.cloud.google.com/build/docs/locations) to deploy the notifier.
  3. Run the following command in the root of the repository:
         
         ./setup.sh http -t config-path
         

Where:

     * `config-path` is the path to your notifiers configuration file.



After running the script, you will see the following message:
    
    
    ** NOTIFIER SETUP COMPLETE **
    

Your notifier is now set up. You can view the complete script in the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers) or run `./setup.sh --help` for usage instructions associated with the script.

### Google Chat

### Setting up

The following sections describe steps you need to complete before automating notification configuration for your notifier.

#### Enabling APIs

Enable the Cloud Build, Compute Engine, Cloud Run, Pub/Sub, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,compute.googleapis.com,run.googleapis.com,pubsub.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/configuring-notifications/automate)

#### Obtaining and storing credentials

  1. Create a [space](https://support.google.com/chat/answer/7653861) in Google Chat.

  2. Within the created space, [create an incoming webhook](https://developers.google.com/chat/how-tos/webhooks) to post messages from Cloud Build to Google Chat. Your URL will look similar to the following:

https://chat.googleapis.com/v1/spaces/...

  3. Store your incoming webhook URL in Secret Manager:

     1. Open the Secret Manager page in the Google Cloud console:

[Open the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

     2. Click **Create secret**.

     3. Enter a name for your secret.

     4. Under **Secret value** , add your incoming webhook URL for your Google Chat space.

     5. To save your secret, click **Create secret**.




#### Writing a notifier configuration file

Write a notifier configuration file to configure your Google Chat notifier and filter on build events:

In the following example notifier configuration file, the `filter` field uses [Common Expression Language](https://github.com/google/cel-spec) with the available variable, `build`, to filter build events with a `SUCCESS` status:
    
    
      apiVersion: cloud-build-notifiers/v1
      kind: GoogleChatNotifier
      metadata:
        name: example-googlechat-notifier
      spec:
        notification:
          filter: build.status == Build.Status.SUCCESS
          delivery:
            webhookUrl:
              secretRef: webhook-url
        secrets:
        - name: webhook-url
          value: projects/project-id/secrets/secret-name/versions/latest
    

Where:

  * `webhook-url` is the configuration variable used in this example to reference the Google Chat webhook URL path stored in Secret Manager. The variable name you specify here should match the `name` field under `secrets`.
  * `project-id` is the ID of your Google Cloud project.
  * `secret-name` is the name of your secret that contains your Google Chat webhook URL.



To view the example, see the [notifier configuration file](http://github.com/GoogleCloudPlatform/cloud-build-notifiers/tree/master/googlechat/googlechat.yaml.example) for the Google Chat notifier.

### Running the automation script

To automate notification configuration for your notifier:

  1. Clone the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers).

  2. Configure the Google Cloud CLI with your project ID and region: 
         
         gcloud config set project project-id
         gcloud config set run/region region
         

Where:

     * `project-id` is your Google Cloud project ID.
     * `region` is the [region](https://docs.cloud.google.com/build/docs/locations) to deploy the notifier.
  3. Run the following command in the root of the repository:



    
    
    ./setup.sh googlechat config-path -s secret-name
    

Where:

  * `config-path` is the path to your notifiers configuration file.
  * `secret-name` is the name of your secret stored in Secret Manager.



After running the script, you will see the following message:
    
    
    ** NOTIFIER SETUP COMPLETE **
    

Your notifier is now set up. You can view the complete script in the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers) or run `./setup.sh --help` for usage instructions associated with the script.

### GitHub Issues

### Setting up

The following sections describe steps you need to complete before automating notification configuration for your notifier.

#### Enabling APIs

Enable the Cloud Build, Compute Engine, Cloud Run, Pub/Sub, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,compute.googleapis.com,run.googleapis.com,pubsub.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/configuring-notifications/automate)

#### Obtaining and storing credentials

  1. Create a [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token):

     1. Go to the [GitHub settings](https://github.com/settings/tokens/new) for creating a new token.
     2. Select the `repo` scope.

**Note:** this grants [full access](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes) to repos, including private repos.
     3. Click **Generate token**

  2. Store your token in Secret Manager:

     1. Open the Secret Manager page in the Google Cloud console:

[Open the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

     2. Click **Create secret**.

     3. Enter a name for your secret.

     4. Under **Secret value** , add your GitHub token.

     5. To save your secret, click **Create secret**.




#### Writing a template configuration file

Write a template configuration file to describe the format created GitHub Issues should take: 

In the following example template configuration file, the `title` and `body` fields use substitution variables from the build: 
    
    
    {
        "title": "Build {{.Build.BuildTriggerId}}: {{.Build.Status}}",
        "body": "[{{.Build.ProjectId}}] {{.Build.BuildTriggerId}} status: **{{.Build.Status}}**\n\n[View Logs]({{.Build.LogUrl}})"
    }
    

To view the example, see the [template configuration file](http://github.com/GoogleCloudPlatform/cloud-build-notifiers/tree/master/githubissues/githubissues.json) for the GitHub Issues notifier.

Additional fields can be set from the available body parameters from the [GitHub API endpoint for creating an issue](https://docs.github.com/en/rest/issues/issues#create-an-issue). 

#### Writing a notifier configuration file

Write a notifier configuration file to configure your Google Chat notifier and filter on build events:

In the following example notifier configuration file, the `filter` field uses [Common Expression Language](https://github.com/google/cel-spec) with the available variable, `build`, to filter build events with a `SUCCESS` status:
    
    
    apiVersion: cloud-build-notifiers/v1
    kind: GitHubIssuesNotifier
    metadata:
      name: example-githubissues-notifier
    spec:
      notification:
        filter: build.status == Build.Status.FAILURE
        template: 
          type: golang
          uri: gs://project-id-notifiers-config/template-file-name
        delivery:
          githubToken:
            secretRef: github-token
          githubRepo: myuser/myrepo
      secrets:
      - name: github-token
        value: projects/project-id/secrets/secret-name/versions/latest
    

Where:

  * `githubToken` is the configuration variable used in this example to reference the GitHub token stored in Secret Manager. The variable name you specify here should match the `name` field under `secrets`.
  * `project-id-notifiers-config` is the location where your template will be uploaded, and the bucket will be created if it doesn't already exist.
  * `template-file-name` is the name of your template file.
  * `myuser/myrepo` is the name of the repo that issues will be created against.
  * `project-id` is the ID of your Google Cloud project.
  * `secret-name` is the name of your secret that contains your GitHub token.



To view the example, see the [notifier configuration file](http://github.com/GoogleCloudPlatform/cloud-build-notifiers/tree/master/githubissues/githubissues.yaml.example) for the Google Chat notifier.

For additional fields you can filter by, see the [Build](https://cloud.google.com/build/docs/api/reference/rest/v1/projects.builds) resource. For additional filtering examples, see the [Using CEL to filter build events](https://docs.cloud.google.com/build/docs/configuring-notifications/configure-githubissues#using_cel_to_filter_build_events).

### Running the automation script

To automate notification configuration for your notifier:

  1. Clone the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers).

  2. Configure the Google Cloud CLI with your project ID and region: 
         
         gcloud config set project project-id
         gcloud config set run/region region
         

Where:

     * `project-id` is your Google Cloud project ID.
     * `region` is the [region](https://docs.cloud.google.com/build/docs/locations) to deploy the notifier.
  3. Run the following command in the root of the repository:



    
    
        ./setup.sh githubissues config-path -t template-path -s secret-name
    

Where:

  * `config-path` is the path to your notifiers configuration file.
  * `template-path` is the path to your notifiers template file. Your notifiers template file contains the JSON template hoted on Cloud Storage and represents your notification message. You can include your notifiers template file as a path using this variable or within the `uri` field of your notifiers configuration file. 
  * `secret-name` is the name of your secret stored in Secret Manager.




After running the script, you will see the following message:
    
    
    ** NOTIFIER SETUP COMPLETE **
    

Your notifier is now set up. You can view the complete script in the [cloud-build-notifiers repository](http://github.com/GoogleCloudPlatform/cloud-build-notifiers) or run `./setup.sh --help` for usage instructions associated with the script.

## What's next

  * Learn about [Cloud Build notifiers](https://docs.cloud.google.com/build/docs/configuring-notifications/notifiers).
  * Learn how to [subscribe to build notifications](https://docs.cloud.google.com/build/docs/subscribe-build-notifications).
  * Learn how to write a [Cloud Build build configuration file](https://docs.cloud.google.com/build/docs/build-config).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
