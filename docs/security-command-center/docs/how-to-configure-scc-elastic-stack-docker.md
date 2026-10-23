---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker/
title: Send Security Command Center data to Elastic Stack using Docker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:52.259677+00:00
---

# Send Security Command Center data to Elastic Stack using Docker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Send Security Command Center data to Elastic Stack using Docker Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to use a [Docker](https://www.docker.com/) container to host your [Elastic Stack](https://www.elastic.co/elastic-stack/) installation, and automatically send [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) findings, assets, audit logs, and security sources to Elastic Stack. It also describes how to manage the exported data.

Docker is a platform for managing applications in containers. Elastic Stack is a security information and event management (SIEM) platform that ingests data from one or more sources and lets security teams manage responses to incidents and perform real-time analytics. The Elastic Stack configuration discussed in this guide includes four components:

  * **Filebeat** : a lightweight agent installed on edge hosts, such as virtual machines (VM), that can be configured to collect and forward data
  * **Logstash** : a transformation service that ingests data, maps it into required fields, and forwards the results to Elasticsearch
  * **Elasticsearch** : a search database engine that stores data
  * **Kibana** : powers dashboards that let you visualize and analyze data



In this guide, you set up Docker, ensure that the required Security Command Center and Google Cloud services are properly configured, and use a custom module to send findings, assets, audit logs, and security sources to Elastic Stack.

The following figure illustrates the data path when using Elastic Stack with Security Command Center.

[ ![Security Command Center and Elastic Stack integration \(click to enlarge\)](https://docs.cloud.google.com/static/security-command-center/images/scc-elastic-stack.png)](https://docs.cloud.google.com/static/security-command-center/images/scc-elastic-stack.png) Security Command Center and Elastic Stack integration (click to enlarge)

## Configure authentication and authorization

Before connecting to Elastic Stack, you need to create an Identity and Access Management (IAM) service account in each Google Cloud organization that you want to connect and grant the account both the organization-level and project-level IAM roles that Elastic Stack needs.

### Create a service account and grant IAM roles

The following steps use the Google Cloud console. For other methods, see the links at the end of this section.

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

  1. In the same project in which you create your Pub/Sub topics, use the **Service Accounts** page in the Google Cloud console to create a service account. For instructions, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts). 
  2. Grant the service account the following roles:

     * **Pub/Sub Admin** (`roles/pubsub.admin`)
     * **Cloud Asset Owner** (`roles/cloudasset.owner`) 
  3. Copy the name of the service account that you just created.

  4. Use the project selector in the Google Cloud console to switch to the organization level.

  5. Open the **IAM** page for the organization:

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  6. On the IAM page, click **Grant access**. The grant access panel opens.

  7. In the **Grant access** panel, complete the following steps:

     1. In the **Add principals** section in the **New principals** field, paste the name of the service account.
     2. In the **Assign roles** section, use the **Role** field to grant the following IAM roles to the service account: 

     3. **Security Center Admin Editor** (`roles/securitycenter.adminEditor`) 
     4. **Security Center Notification Configurations Editor** (`roles/securitycenter.notificationConfigEditor`)
     5. **Organization Viewer** (`roles/resourcemanager.organizationViewer`)
     6. **Cloud Asset Viewer** (`roles/cloudasset.viewer`) 
     7. **Logs Configuration Writer** (`roles/logging.configWriter`) 
  8. Click **Save**. The service account appears on the **Permissions** tab of the **IAM** page under **View by principals**.

By inheritance, the service account also becomes a principal in all child projects of the organization. The roles that are applicable at the project level are listed as inherited roles.




For more information about creating service accounts and granting roles, see the following topics:

  * [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)
  * [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



### Provide the credentials to Elastic Stack

Depending on where you are hosting Elastic Stack, how you provide the IAM credentials to Elastic Stack differs.

  * If you are hosting the Docker container in Google Cloud, consider the following:

    * [Add the service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) to the VM that will host your Kubernetes nodes. If you are using multiple Google Cloud organizations, add this service account to the other organizations and grant it the organization-level IAM roles described in Create a service account and grant IAM roles.

    * If you deploy the Docker container in a service perimeter, create the ingress and egress rules. For instructions, see [Granting perimeter access in VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications#grant-perimeter-access).

  * If you are hosting the Docker container in your on-premises environment, [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for each Google Cloud organization. You need the service account keys in JSON format to complete this guide.

To learn about best practices for storing your service account keys securely, see [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

  * If you are installing the Docker container in another cloud, [configure workload identity federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation) and [download the credentials configuration files](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation). If you are using multiple Google Cloud organizations, add this service account to the other organizations and grant it the organization-level IAM roles described in Create a service account and grant IAM roles.




## Configure notifications

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

  1. [Set up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) as follows:

     1. Enable the Security Command Center API.
     2. Create a filter to export findings and assets.
     3. Create four [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) topics: one each for findings, resources, audit logs, and assets. The `NotificationConfig` must use the Pub/Sub topic that you create for findings.

You need your organization ID, project ID, and Pub/Sub topic names from this task to configure Elastic Stack.

  2. [Enable the Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) for your project.




## Install the Docker and Elasticsearch components

Follow these steps to install the Docker and Elasticsearch components in your environment.

### Install Docker Engine and Docker Compose

You can install Docker for use on-premises or with a cloud provider. To get started, complete the following guides in Docker's product documentation:

  * [Install Docker Engine (Linux)](https://docs.docker.com/engine/install/)
  * [Install Docker Compose](https://docs.docker.com/compose/install/)



### Install Elasticsearch and Kibana

The Docker image that you installed in Install Docker includes Logstash and Filebeat. If you don't already have Elasticsearch and Kibana installed, use the following guides to install the applications:

  * [Installing Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)

  * [Install Kibana](https://www.elastic.co/guide/en/kibana/current/install.html)




You need the following information from those tasks to complete this guide:

  * Elastic Stack: host, port, certificate, username, and password
  * Kibana: host, port, certificate, username, and password



### Download the GoApp module

This section explains how to download the `GoApp` module. The module automates the process of scheduling Security Command Center API calls and regularly retrieves Security Command Center data for use in Elastic Stack.

To install `GoApp`, do the following:

  1. In a terminal window, install [wget](https://www.gnu.org/software/wget/), a free software utility used to retrieve content from web servers.

For Ubuntu and Debian distributions, run the following:
         
         apt-get install wget
         

For RHEL, CentOS, and Fedora distributions, run the following:
         
         yum install wget
         

  2. Install `unzip`, a free software utility used to extract the contents of ZIP files.

For Ubuntu and Debian distributions, run the following:
         
         apt-get install unzip
         

For RHEL, CentOS, and Fedora distributions, run the following:
         
         yum install unzip
         

  3. Create a directory for the GoogleSCCElasticIntegration installation package:
         
         mkdir GoogleSCCElasticIntegration
         

  4. Download the GoogleSCCElasticIntegration installation package:
         
         wget -c https://storage.googleapis.com/security-center-elastic-stack/GoogleSCCElasticIntegration-Installation.zip
         

  5. Extract the contents of the GoogleSCCElasticIntegration installation package into the `GoogleSCCElasticIntegration` directory:
         
         unzip GoogleSCCElasticIntegration-Installation.zip -d GoogleSCCElasticIntegration
         

  6. Create a working directory to store and run `GoApp` module components:
         
         mkdir WORKING_DIRECTORY
         

Replace `WORKING_DIRECTORY` with the directory name.

  7. Navigate to the `GoogleSCCElasticIntegration` installation directory:
         
         cd ROOT_DIRECTORY/GoogleSCCElasticIntegration/
         

Replace `ROOT_DIRECTORY` with the path to the directory that contains the `GoogleSCCElasticIntegration` directory.

  8. Move `install`, `config.yml`, `dashboards.ndjson`, and the `templates` folder (with the `filebeat.tmpl`, `logstash.tmpl`, and `docker.tmpl` files) into your working directory.
         
         mv install/install install/config.yml install/templates/docker.tmpl install/templates/filebeat.tmpl install/templates/logstash.tmpl install/dashboards.ndjson WORKING_DIRECTORY
         

Replace `WORKING_DIRECTORY` with the path to your working directory.




### Install the Docker container

**Note:** To complete the tasks in this section, be sure Docker, Docker Compose, Elasticsearch, and Kibana are running.

To set up the Docker container, you download and install a preformatted image from Google Cloud that contains Logstash and Filebeat. For information about the Docker image, go to the Artifact Registry repository in the Google Cloud console.

[Go to Artifact Registry](https://console.cloud.google.com/artifacts/docker/security-center-gcr-host/us/us.gcr.io/googlescc_elk)

During installation, you configure the `GoApp` module with Security Command Center and Elastic Stack credentials.

  1. Navigate to your working directory:
         
         cd /WORKING_DIRECTORY
         

Replace `WORKING_DIRECTORY` with the path to your working directory.

  2. Verify that the following files appear in your working directory:
         
         ├── config.yml
           ├── install
           ├── dashboards.ndjson
           ├── templates
               ├── filebeat.tmpl
               ├── docker.tmpl
               ├── logstash.tmpl
         

  3. In a text editor, open the `config.yml` file and add requested variables. If a variable isn't required, you can leave it blank.

Variable  | Description  | Required   
---|---|---  
`elasticsearch` | The section for your Elasticsearch configuration. | Required  
`host` | The IP address of your Elastic Stack host. | Required  
`password` | Your Elasticsearch password. | Optional  
`port` | The port for your Elastic Stack host. | Required  
`username` | Your Elasticsearch username. | Optional  
`cacert` | The certificate for the Elasticsearch server (for example, `path/to/cacert/elasticsearch.cer`). | Optional  
`http_proxy` | A link with the username, password, IP address, and port for your proxy host (for example, `http://USER:PASSWORD@PROXY_IP:PROXY_PORT`). | Optional  
`kibana` | The section for your Kibana configuration. | Required  
`host` | The IP address or hostname to which the Kibana server will bind. | Required  
`password` | Your Kibana password. | Optional  
`port` | The port for the Kibana server. | Required  
`username` | Your Kibana username. | Optional  
`cacert` | The certificate for the Kibana server (for example, `path/to/cacert/kibana.cer`). | Optional  
`cron` | The section for your cron configuration. | Optional  
`asset` | The section for your asset cron configuration (for example, `0 */45 * * * *`). | Optional  
`source` | The section for your source cron configuration (for example, `0 */45 * * * *`). For more information, see [Cron expression generator](https://crontab.cronhub.io/). | Optional  
`organizations` | The section for your Google Cloud organization configuration. To add multiple Google Cloud organizations, copy everything from `- id:` to `subscription_name` under `resource`. | Required  
`id` | Your organization ID. | Required  
`client_credential_path` | One of: 
     * The path to your JSON file, if you are using service account keys.
     * The credential configuration file, if you are using Workload Identity Federation.
     * Don't specify anything if this is the Google Cloud organization that you are installing the Docker container in.
| Optional, depending on your environment  
`update` | Whether you are upgrading from a previous version, either `n` for no or `y` for yes | Optional  
`project` | The section for your project ID. | Required  
`id` | The ID for the project that contains the Pub/Sub topic. | Required  
`auditlog` | The section for the Pub/Sub topic and subscription for audit logs. | Optional  
`topic_name` | The name of the Pub/Sub topic for audit logs | Optional  
`subscription_name` | The name of the Pub/Sub subscription for audit logs | Optional  
`findings` | The section for the Pub/Sub topic and subscription for findings. | Optional  
`topic_name` | The name of the Pub/Sub topic for findings. | Optional  
`start_date` | The optional date to start migrating findings, for example, `2021-04-01T12:00:00+05:30` | Optional  
`subscription_name` | The name of the Pub/Sub subscription for findings. | Optional  
`asset` | The section for the asset configuration. | Optional  
`iampolicy` | The section for the Pub/Sub topic and subscription for IAM policies. | Optional  
`topic_name` | The name of the Pub/Sub topic for IAM policies. | Optional  
`subscription_name` | The name of the Pub/Sub subscription for IAM policies. | Optional  
`resource` | The section for the Pub/Sub topic and subscription for resources. | Optional  
`topic_name` | The name of the Pub/Sub topic for resources. | Optional  
`subscription_name` | The name of the Pub/Sub subscription for resources. | Optional  
  
#### Example `config.yml` file

The following example shows a `config.yml` file that includes two Google Cloud organizations.
    
    elasticsearch:
      host: 127.0.0.1
      password: changeme
      port: 9200
      username: elastic
      cacert: path/to/cacert/elasticsearch.cer
    http_proxy: http://user:password@proxyip:proxyport
    kibana:
      host: 127.0.0.1
      password: changeme
      port: 5601
      username: elastic
      cacert: path/to/cacert/kibana.cer
    cron:
      asset: 0 */45 * * * *
      source: 0 */45 * * * *
    organizations:
      – id: 12345678910
        client_credential_path:
        update:
        project:
          id: project-id-12345
        auditlog:
          topic_name: auditlog.topic_name
          subscription_name: auditlog.subscription_name
        findings:
          topic_name: findings.topic_name
          start_date: 2021-05-01T12:00:00+05:30
          subscription_name: findings.subscription_name
        asset:
          iampolicy:
            topic_name: iampolicy.topic_name
            subscription_name: iampolicy.subscription_name
          resource:
            topic_name: resource.topic_name
            subscription_name: resource.subscription_name
      – id: 12345678911
        client_credential_path:
        update:
        project:
          id: project-id-12346
        auditlog:
          topic_name: auditlog2.topic_name
          subscription_name: auditlog2.subscription_name
        findings:
          topic_name: findings2.topic_name
          start_date: 2021-05-01T12:00:00+05:30
          subscription_name: findings1.subscription_name
        asset:
          iampolicy:
            topic_name: iampolicy2.topic_name
            subscription_name: iampolicy2.subscription_name
          resource:
            topic_name: resource2.topic_name
            subscription_name: resource2.subscription_name
    

  4. Run the following commands to install the Docker image and configure the `GoApp` module.
         
         chmod +x install
         ./install
         

The `GoApp` module downloads the Docker image, installs the image, and sets up the container. 

  5. When the process is finished, copy the email address of the WriterIdentity service account from the installation output.
         
         docker exec googlescc_elk ls
         docker exec googlescc_elk cat Sink_&#125;&#125;HashId&#123;&#123;
         

Your working directory should have the following structure:
         
         ├── config.yml
           ├── dashboards.ndjson
           ├── docker-compose.yml
           ├── install
           ├── templates
               ├── filebeat.tmpl
               ├── logstash.tmpl
               ├── docker.tmpl
           └── main
               ├── client_secret.json
               ├── filebeat
               │          └── config
               │                   └── filebeat.yml
               ├── GoApp
               │       └── .env
               └── logstash
                          └── pipeline
                                     └── logstash.conf
         




### Update permissions for audit logs

To update permissions so that audit logs can flow to your SIEM:

  1. Navigate to the Pub/Sub topics page.

[Go to Pub/Sub](https://console.cloud.google.com/project/_/cloudpubsub/topic/list)

  2. Select your project that includes your Pub/Sub topics.

  3. Select the Pub/Sub topic that you created for audit logs.

  4. In **Permissions** , add the WriterIdentity service account (that you copied in step 4 of the installation procedure) as a new principal and assign it the **Pub/Sub Publisher** role. The audit log policy is updated.




The Docker and Elastic Stack configurations are complete. You can now set up Kibana.

### View Docker logs

  1. Open a terminal, and run the following command to see your container information, including container IDs. Note the ID for the container where Elastic Stack is installed.
         
         docker container ls
         

  2. To start a container and view its logs, run the following commands:
         
         docker exec -it CONTAINER_ID /bin/bash
         cat go.log
         

Replace `CONTAINER_ID` with the ID of the container where Elastic Stack is installed.




## Set up Kibana

Complete these steps when you are installing the Docker container for the first time.

  1. Open `kibana.yml` in a text editor.
         
         sudo vim KIBANA_DIRECTORY/config/kibana.yml
         

Replace `KIBANA_DIRECTORY` with the path to your Kibana installation folder.

  2. Update the following variables:

     * `server.port`: the port to use for Kibana's backend server; default is 5601
     * `server.host`: the IP address or hostname to which the Kibana server will bind
     * `elasticsearch.hosts`: the IP address and port of the Elasticsearch instance to use for queries
     * `server.maxPayloadBytes`: the maximum payload size in bytes for incoming server requests; default is 1,048,576
     * `url_drilldown.enabled`: a Boolean value that controls the ability to navigate from Kibana dashboard to internal or external URLs; default is `true`

The completed configuration resembles the following:
    
    server.port: PORT
      server.host: "HOST"
      elasticsearch.hosts: ["http://ELASTIC_IP_ADDRESS:ELASTIC_PORT"]
      server.maxPayloadBytes: 5242880
      url_drilldown.enabled: true
    




### Import Kibana dashboards

  1. Open the Kibana application.
  2. In the navigation menu, go to **Stack Management** , and then click **Saved Objects**.
  3. Click **Import** , navigate to the working directory and select **dashboards.ndjson**. The dashboards are imported and index patterns are created.



## Upgrade the Docker container

If you deployed a previous version of the `GoApp` module, you can upgrade to a newer version. When you upgrade the Docker container to a newer version, you can keep your existing service account setup, Pub/Sub topics, and Elasticsearch components.

If you are upgrading from an integration that didn't use a Docker container, see [Upgrade to the latest release](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack#upgrade-latest).

**Note:** To complete the tasks in this section, verify that Docker, Docker Compose, Elasticsearch, and Kibana are running.

### Prerequisites and system cleanup

Before configuring the new Docker container, verify your permissions, prepare your Pub/Sub topics, and remove the existing container and dashboards:

  1. If you are upgrading from v1, complete these actions:

     1. Add the **Logs Configuration Writer** (`roles/logging.configWriter`) role to the service account.

     2. Create a [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) topic for your audit logs.

  2. If you are installing the Docker container in another cloud, [configure workload identity federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation) and [download the credentials configuration file](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation).

  3. Optionally, to avoid issues when importing the new dashboards, remove the existing dashboards from Kibana:

     1. Open the Kibana application.
     2. In the navigation menu, go to **Stack Management** , and then click **Saved Objects**.
     3. Search for _Google SCC_.
     4. Select all the dashboards that you want to remove.
     5. Click **Delete**.
  4. Remove the existing Docker container:

     1. Open a terminal and stop the container:
            
            docker stop CONTAINER_ID
            

Replace `CONTAINER_ID` with the ID of the container where Elastic Stack is installed.

     2. Remove the Docker container:
            
            docker rm CONTAINER_ID
            

If necessary, add `-f` before the container ID to remove the container forcefully.




### Configure the Elastic data stream and Docker container

  1. Complete steps 1 through 7 in Download the GoApp module.

  2. Move the existing `config.env` file from your previous installation into the `\update` directory.

  3. If necessary, give executable permission to run `./update`:
         
         chmod +x ./update
         ./update
         

  4. Run `./update` to convert `config.env` to `config.yml`.

  5. Verify that the `config.yml` file includes your existing configuration. If not, re-run `./update`.

  6. To support multiple Google Cloud organizations, add another organization configuration to the `config.yml` file.

  7. Move the `config.yml` file into your working directory, where the `install` file is located.

  8. Complete the steps in Install Docker.

  9. Complete the steps in Update permissions for audit logs.




### Set up visualization

Import the new dashboards, as described in Import Kibana dashboards. This step overwrites your existing Kibana dashboards.

## View and edit Kibana dashboards

You can use custom dashboards in Elastic Stack to visualize and analyze your findings, assets, and security sources. The dashboards display critical findings and help your security team prioritize fixes.

### Overview dashboard

The **Overview** dashboard contains a series of charts that displays the total number of findings in your Google Cloud organizations by severity level, category, and state. Findings are compiled from Security Command Center's built-in services, such as [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics), [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview), [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview), and any integrated services you enable.

To filter content by criteria such as misconfigurations or vulnerabilities, you can select the **Finding class**.

Additional charts show which categories, projects, and assets are generating the most findings.

**Note:** You must be a [Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/service-tiers) customer to receive findings from certain Security Command Center services, such as Event Threat Detection and Container Threat Detection.

### Assets dashboard

The **Assets** dashboard displays tables that show your Google Cloud assets. The tables show asset owners, asset counts by resource type and projects, and your most recently added and updated assets.

You can filter asset data by organization, asset name, asset type, and parents, and quickly drill down to findings for specific assets. If you click an asset name, you are redirected to Security Command Center's **Assets** page in the Google Cloud console and shown details for the selected asset.

### Audit logs dashboard

The **Audit logs** dashboard displays a series of charts and tables that show audit log information. The audit logs that are included in the dashboard are the administrator activity, data access, system events, and policy denied audit logs. The table includes the time, severity, log type, log name, service name, resource name, and resource type.

You can filter the data by organization, source (such as a project), severity, log type, and resource type.

### Findings dashboard

The **Findings** dashboard includes charts showing your most recent findings. The charts provide information about the number of findings, their severity, category, and state. You can also view active findings over time, and which projects or resources have the most findings.

You can filter the data by organization and finding class.

If you click a finding name, you are redirected to Security Command Center's **Findings** page in the Google Cloud console and shown details for the selected finding.

### Sources dashboard

The **Sources** dashboard shows the total number of findings and security sources, the number of findings by source name, and a table of all your security sources. Table columns include name, display name, and description.

### Add columns

  1. Navigate to a dashboard.
  2. Click **Edit** , and then click **Edit visualization**.
  3. Under **Add sub-bucket** , select **Split rows**.
  4. In the list, select **Terms** aggregation.
  5. In the **Descending** drop-down menu, select ascending or descending. In the **Size** field, enter the maximum number of rows for the table.
  6. Select the column you want to add and click **Update**.
  7. Save the changes.



### Hide or remove columns

  1. Navigate to the dashboard.
  2. Click **Edit**.
  3. To hide a column, next to the column name, click the visibility, or eye, icon.
  4. To remove a column, next to the column name, click the **X** , or delete, icon.



## Uninstall the integration with Elasticsearch

To remove the integration between Security Command Center and Elasticsearch, complete the following sections.

### Remove dashboards, indexes, and index patterns

Remove dashboards when you want to uninstall this solution.

  1. Navigate to the dashboards.

  2. Search for _Google SCC_ and select all the dashboards.

  3. Click **Delete dashboards**.

  4. Navigate to **Stack Management > Index Management**.

  5. Close the following indexes:

     * **gccassets**
     * **gccfindings**
     * **gccsources**
     * **gccauditlogs**
  6. Navigate to **Stack Management > Index Patterns**.

  7. Close the following patterns:

     * **gccassets**
     * **gccfindings**
     * **gccsources**
     * **gccauditlogs**



### Uninstall Docker

  1. [Delete the NotificationConfig](https://docs.cloud.google.com/security-command-center/docs/how-to-api-manage-notifications#delete-config) for Pub/Sub. To find the name of the NotificationConfig, run:
         
         docker exec googlescc_elk ls
         docker exec googlescc_elk cat NotificationConf_&#125;&#125;HashId&#123;&#123;
         

  2. Remove Pub/Sub feeds for assets, findings, IAM policies, and audit logs. To find the names for the feeds, run:
         
         docker exec googlescc_elk ls
         docker exec googlescc_elk cat Feed_&#125;&#125;HashId&#123;&#123;
         

  3. Remove the sink for the audit logs. To find the name for the sink, run:
         
         docker exec googlescc_elk ls
         docker exec googlescc_elk cat Sink_&#125;&#125;HashId&#123;&#123;
         

  4. To see your container information, including container IDs, open the terminal and run the following command:
         
         docker container ls
         

  5. Stop the container:
         
         docker stop CONTAINER_ID
         

Replace `CONTAINER_ID` with the ID of the container where Elastic Stack is installed.

  6. Remove the Docker container:
         
         docker rm CONTAINER_ID
         

If necessary, add `-f` before the container ID to remove the container forcefully.

  7. Remove the Docker image:
         
         docker rmi us.gcr.io/security-center-gcr-host/googlescc_elk_v3:latest
         

  8. Delete the working directory and the `docker-compose.yml` file:
         
         rm -rf ./main docker-compose.yml
         




## What's next

  * Learn more about setting up [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) in Security Command Center.

  * Read about [filtering finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications) in Security Command Center.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
