---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack/
title: Send Security Command Center data to Elastic Stack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:44.733294+00:00
---

# Send Security Command Center data to Elastic Stack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Send Security Command Center data to Elastic Stack Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. **Note:** This content applies only to the `GoApp` service that was released in February 2022. To upgrade to the latest `GoApp` service, see Upgrade to the latest release.

This page explains how to automatically send [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) findings, assets, and security sources to [Elastic Stack](https://www.elastic.co/elastic-stack/) without using a Docker container. It also describes how to manage the exported data. Elastic Stack is a security information and event management (SIEM) platform that ingests data from one or more sources and lets security teams manage responses to incidents and perform real-time analytics. The Elastic Stack configuration discussed in this guide includes four components:

  * **Filebeat** : a lightweight agent installed on edge hosts, such as virtual machines (VM), that can be configured to collect and forward data
  * **Logstash** : a transformation service that ingests data, maps it into required fields, and forwards the results to Elasticsearch
  * **Elasticsearch** : a search database engine that stores data
  * **Kibana** : powers dashboards that let you visualize and analyze data



## Upgrade to the latest release

To upgrade to the latest release, you must deploy a Docker container image that includes the `GoApp` module. For more information, see [Exporting assets and findings with Docker and Elastic Stack](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker).

### Prerequisites and system cleanup

Before installing the new Docker container, clean up your legacy integration and establish required permissions and Pub/Sub topics:

  1. Delete the following files and directories: 
     * `/etc/systemd/system/go_script.service`
     * The `GoApp` directory
     * Logstash configurations
     * `logstash2.service`
     * `filebeat.service`
  2. Optional: To avoid issues when importing the new dashboards, remove the existing dashboards from Kibana: 
     1. Open the Kibana application.
     2. In the navigation menu, go to **Stack Management** , and then click **Saved Objects**.
     3. Search for _Google SCC_.
     4. Select all the dashboards that you want to remove.
     5. Click **Delete**.
  3. Add the **Logs Configuration Writer** (`roles/logging.configWriter`) role to the service account.
  4. Create a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/overview) for your audit logs.
  5. Optionally, if you are installing the Docker container in another cloud, [configure workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) instead of using service account keys. You must create [short-lived service account credentials](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) and download the credential configuration file.



### Configure the Elastic data stream and Docker container

  1. Complete the steps in [Download the GoApp module](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker#downloadgoapp).
  2. Complete the steps in [Install the Docker container](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker#installdocker).
  3. Complete the steps in [Update permissions for audit logs](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker#updateperms).



### Visualization and dashboard setup

  1. Import all the dashboards, as described in [Import Kibana dashboards](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker#import-dashboards).



Use the instructions in [Exporting assets and findings with Docker and Elastic Stack](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker) to administer your SIEM integration.

## Manage service and logs

This section explains how to view `GoApp` module logs and make changes to the module's configuration.

This section applies only to the `GoApp` module that you installed from the `GoogleSCCElasticIntegration` installation package that was made available in February 2022. For up-to-date information, see Upgrade to the latest release. 

  1. Check the status of the service:
         
         systemctl | grep go_script
         

  2. Check the current working logs, which contain information on execution failures and other service information:
         
         sudo journalctl -f -u go_script.service
         

  3. Check historical and current working logs:
         
         sudo journalctl -u go_script.service
         

  4. To troubleshoot or check the logs of `go_script.service`:
         
         cat go.log
         




## Configure Elastic Stack applications

This section explains how to configure Elastic Stack applications to ingest Security Command Center data. The instructions assume you properly installed and enabled Elastic Stack, and that you have root privileges in the application environment.

This section applies only to the `GoApp` module that you installed from the `GoogleSCCElasticIntegration` installation package that was made available in February 2022. For up-to-date information, see Upgrade to the latest release. 

### View Logstash service logs

To view current logs, run the following command:
    
    
        sudo journalctl -f -u logstash2.service
    

To view historical logs, run the following command:
    
    
        sudo journalctl -u logstash2.service
    

### Set up Filebeat

This section applies only to the `GoApp` module that you installed from the `GoogleSCCElasticIntegration` installation package that was made available in February 2022. For up-to-date information, see Upgrade to the latest release. 

#### View Filebeat service logs

To view current logs, run the following command:
    
    
        sudo journalctl -f -u filebeat.service
    

To view historical logs, run the following command:
    
    
        sudo journalctl -u filebeat.service
    

## View Kibana dashboards

You can use custom dashboards in Elastic Stack to visualize and analyze your findings, assets, and security sources. The dashboards display critical findings and help your security team prioritize fixes.

This section applies only to the `GoApp` module that you installed from the `GoogleSCCElasticIntegration` installation package that was made available in February 2022. For up-to-date information, see Upgrade to the latest release. 

### Overview

The **Overview** dashboard contains a series of charts that displays the total number of findings in your organization by severity level, category, and state. Findings are compiled from Security Command Center's built-in services—[Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics), [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview), [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)—and any integrated services you enable.

Additional charts show which categories, projects, and assets are generating the most findings.

**Note:** You must be a [Security Command Center Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) customer to receive Event Threat Detection and Container Threat Detection findings.

### Assets

The **Assets** dashboard displays tables that show your Google Cloud assets. The tables show asset owners, asset counts by resource type and projects, and your most recently added and updated assets.

You can filter asset data by time range, resource name, resource type, owner, and project, and quickly drill down to findings for specific assets. If you click an asset name, you are redirected to Security Command Center's **Assets** page in the Google Cloud console and shown details for the selected asset.

### Findings

The **Findings** dashboard includes a table showing your most recent findings. You can filter the data by resource name, category, and severity.

Table columns include finding name, in the format of `organizations/<var>ORGANIZATION_ID</var>/sources/<var>SOURCE_ID</var>/findings/<var>FINDING_ID</var>`, category, resource name, event time, create time, parent name, parent URI, and security marks. The format of parent URI matches finding name. If you click a finding name, you are redirected to Security Command Center's **Findings** page in the Google Cloud console and shown details for the selected finding.

### Sources

The **Sources** dashboard shows the total number of findings and security sources, the number of findings by source name, and a table of all your security sources. Table columns include name, display name, and description.

### Edit dashboards

To customize the data that is displayed in your Kibana dashboards, you can add or remove columns.

#### Add columns

  1. Navigate to a dashboard.
  2. Click **Edit** , and then click **Edit visualization**.
  3. Under **Add sub-bucket** , select **Split rows**.
  4. In the list, select **Aggregation**.
  5. In the **Descending** drop-down menu, select ascending or descending. In the **Size** field, enter the maximum number of rows for the table.
  6. Select the column you want to add.
  7. Save the changes.



#### Remove columns

  1. Navigate to the dashboard.
  2. Click **Edit**.
  3. To hide a column, next to the column name, click the visibility, or eye, icon.
  4. To remove a column, next to the column name, click the **X** , or delete, icon.



## Uninstall the component

Uninstall the `GoApp` module and Elastic Stack applications when you no longer want to retrieve Security Command Center data for Elastic Stack.

This section applies only to the `GoApp` module that you installed from the `GoogleSCCElasticIntegration` installation package that was made available in February 2022. For up-to-date information, see Upgrade to the latest release. 

### Uninstall the GoApp module

  1. Delete `go_script.service` from `/etc/systemd/system/`.
  2. Remove feeds for assets and IAM policies.
  3. Remove Pub/Sub for assets, IAM policies, and findings.
  4. Delete the working directory.



### Uninstall Logstash

  1. Delete Logstash configurations.
  2. Delete `logstash2.service`.



### Uninstall Filebeat

  1. Delete Filebeat configurations.
  2. Delete `filebeat.service`.



## What's next

  * [Upgrade to the latest version](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-elastic-stack-docker) to integrate Security Command Center with Elastic Stack.

  * Learn more about setting up [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) in Security Command Center.

  * Read about [filtering finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications) in Security Command Center.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
