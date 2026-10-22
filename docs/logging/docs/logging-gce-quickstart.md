---
url: https://docs.cloud.google.com/logging/docs/logging-gce-quickstart/
title: Quickstart: Collect logs from Apache with the Ops Agent \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:35.367275+00:00
---

# Quickstart: Collect logs from Apache with the Ops Agent  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/logging-gce-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect logs from Apache with the Ops Agent

Learn how to collect and view `syslog` logs collected from an Apache web server installed on a Compute Engine virtual machine (VM) instance by using the Ops Agent. You can use a process similar to the one in this quickstart to [monitor other third-party applications](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party).

In this quickstart, you do the following:

  1. Create a Compute Engine VM instance and install the [Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent).
  2. Install an Apache web server.
  3. Configure the Ops Agent for the Apache web server.
  4. View your logs in the Logs Explorer.
  5. Create a log-based alert.
  6. Test your alert.
  7. Clean up.



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/welcome?walkthrough_id=logging--logging-gce-quickstart)

* * *

## Before you begin

  1. Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Compute Engine, Cloud Monitoring, Cloud Logging, and OS Config APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,monitoring.googleapis.com,logging.googleapis.com,osconfig.googleapis.com)

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Compute Engine, Cloud Monitoring, Cloud Logging, and OS Config APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,monitoring.googleapis.com,logging.googleapis.com,osconfig.googleapis.com)




### Required roles

To get the permissions that you need to create a Compute Engine instance, install Apache, and to view metric data, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
  * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`)
  * [OSPolicyAssignment Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/osconfig#osconfig.osPolicyAssignmentAdmin) (`roles/osconfig.osPolicyAssignmentAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a VM instance

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. Create a VM by clicking **Create instance**. Configure your instance by using the options in the navigation menu.
  3. In the **Machine configuration** option, do the following: 
     1. In the **Name** field, enter a descriptive name.
     2. In the **Machine type** preset drop-down, select **Shared-core > e2-small**.
  4. Verify that the **OS and storage** option displays **Debian GNU/Linux**. If not, click the **OS and storage** option and click **Change**. In the **Boot disk** dialog, set **Version** to **Debian GNU/Linux**.
  5. In the **Networking** option, for **Firewall** , select both **Allow HTTP traffic** and **Allow HTTPS traffic**.
  6. Verify that the **Observability** option displays **Install Ops Agent**. If not, click the **Observability** option and select **Install Ops Agent for Monitoring and Logging**.
  7. Click **Create**.



## Install an Apache web server

To install an Apache web server on your Compute Engine VM instance, do the following:

  1. On the **VM instances** page, locate your new VM, go to the **Connect** column, and then click **SSH**.

Having trouble connecting? Refer to [Troubleshooting SSH](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh).

  2. To update the package lists, copy the following command to your clipboard, paste the command into the SSH terminal, and then press enter:
         
         sudo apt-get update
         

  3. After you see the message "Reading package lists... Done", in the SSH terminal, run the following command to install an Apache2 web server:
         
         sudo apt-get install apache2 php7.0
         

When asked to continue the installation, enter `Y`. If the install command fails, then use `sudo apt-get install apache2 php`.

  4. When your command prompt returns, go to the **VM instances** page and copy the VM's external IP address into the following URL:
         
         http://EXTERNAL_IP
         

  5. To connect to your Apache web server, open a new browser tab, and then enter the URL from the previous step.

When the web server is successfully installed, the browser tab displays the Apache2 Debian default page.

![Display the Apache2 default page.](https://docs.cloud.google.com/static/monitoring/images/apache2-works.png)




## Collect Apache web server logs and metrics

In these steps, you configure the [Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent) to collect logs and metrics from your Apache web server: 

  1. Go to the SSH terminal for your VM instance. If you don't have a terminal open, then do the following:

     1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

     2. Locate your new VM and then click **SSH**. 
  2. Copy the following command, then paste it into the terminal for your instance, and then press enter:
         
         # Configures Ops Agent to collect telemetry from the app. You must restart the agent for the configuration to take effect.
         
         set -e
         
         # Check if the file exists
         if [ ! -f /etc/google-cloud-ops-agent/config.yaml ]; then
           # Create the file if it doesn't exist.
           sudo mkdir -p /etc/google-cloud-ops-agent
           sudo touch /etc/google-cloud-ops-agent/config.yaml
         fi
         
         # Create a back up of the existing file so existing configurations are not lost.
         sudo cp /etc/google-cloud-ops-agent/config.yaml /etc/google-cloud-ops-agent/config.yaml.bak
         
         # Configure the Ops Agent.
         sudo tee /etc/google-cloud-ops-agent/config.yaml > /dev/null << EOF
         metrics:
           receivers:
             apache:
               type: apache
           service:
             pipelines:
               apache:
                 receivers:
                   - apache
         logging:
           receivers:
             apache_access:
               type: apache_access
             apache_error:
               type: apache_error
           service:
             pipelines:
               apache:
                 receivers:
                   - apache_access
                   - apache_error
         EOF
         

The previous command creates the configuration to collect and ingest logs and metrics from the Apache web server. For more information, see [Configure the Ops Agent for Apache web server](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/apache). 

  3. Restart the Ops Agent: 
     1. To restart the agent, run the following command on your instance: 
            
            sudo systemctl restart google-cloud-ops-agent
            

     2. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
            
            sudo systemctl status "google-cloud-ops-agent*"
            




## View Apache web server logs

To view your logs in the Google Cloud console, use the Logs Explorer:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

Your most recent logs are displayed in the **Query results** pane.

  2. In the toolbar, ensure that **Show query** is enabled.

  3. To view your Apache web server logs, create and run a query:

     1. Expand the list of Google Cloud projects from the Google Cloud project selector, and then copy the Google Cloud project ID into your clipboard.

     2. In the following expression, paste the copied ID into the PROJECT_ID field, and then copy the expression into the query editor:
            
            resource.type="gce_instance"
            logName=("projects/PROJECT_ID/logs/apache_access" OR "projects/PROJECT_ID/logs/apache_error")
            

When the previous query is run, only `apache_access` and `apache_error` log entries are shown.

     3. Click **Run query**.

The results of the query are displayed in the **Query results** pane.




You've configured the Ops Agent to collect logs and metrics from your Apache web server, and you've viewed those logs. The next step is to create an alerting policy so that you're notified when a specific pattern appears in a log.

## Create an email notification channel

Before you create an alerting policy, configure the notification channels that you want the alerting policy to use. Cloud Monitoring supports many different types of notification channels, including email, Slack, PagerDuty, and Pub/Sub. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options). To get notifications by e-mail, do the following: 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar, click **Edit Notification Channels**.
  3. On the **Notification channels** page, scroll to **Email** , and then click **Add new**.
  4. Enter your email address, a display name such as `My email`, and then click **Save**.



##  Create a log-based alert

To be notified when a specific message appears in your log entries, create a log-based alert. In this section, you create a log-based alert so that you are notified when a `404 Not Found` message appears in your log entries.

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Query results** toolbar, click _add_alert_ **Create alert**. The log-based alert policy pane opens.

  3. In **Alert details** , for the **Alert Policy Name** field, enter `404 Not Found`.

  4. In **Choose logs to include in this alert** , do the following:

     1. Remove any content that is in the log filter field.
     2. Copy the following query and paste it into the log filter field:
            
            severity>=DEFAULT /help httpRequest.status=404
            

The previous log filter searches for log entries with a `severity` level of at least `DEFAULT`, that contain the text `/help`, and that contain an `httpRequest` status of `404`.

  5. In **Set notification frequency and autoclose duration** section, do the following:

     1. Set the **Time between notifications** field to **5 min**.
     2. Set the **Incident autoclose duration** field to **30 min**.
  6. In **Who should be notified?** , select your email from **Notification Channels** menu, and then click **Save**.




## Test the alerting policy

To test the alerting policy, do the following:

  1. Go to the SSH terminal for your VM instance. If you don't have a terminal open, then do the following:

     1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

     2. Locate your new VM and then click **SSH**.
  2. To search the server for the fake page `localhost/help`, run the following command:
         
         curl localhost/help
         

After you see a `404 Not Found` message in the terminal, an email notification is sent. It takes several minutes for this process to complete.

The email notification you receive looks similar to the following:

![The example log-based alert results in an email notification.](https://docs.cloud.google.com/static/logging/docs/images/logging-lba-notification-email.png)

  3. To view the new log entries, do the following:

     1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. In the toolbar, click **Jump to now**.



You've configured the Ops Agent to collect logs and metrics from your Apache web server, but you've only viewed logs. For information about how to view Apache web server metrics, see [Collect Apache web server metrics with the Ops Agent: Generate traffic](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine#generate_traffic).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you created a new project and you no longer need the project, then [delete the project](https://console.cloud.google.com/cloud-resource-manager).

If you used an existing project, then do the following:

  1. If you created a VM, then delete it:

     1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Select the checkbox for the instance that you want to delete. 
     3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 
  2. Delete the alerting policy that you created:

     1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

     2. Select the alerting policy that you created, and then click **Delete**. 



## What's next

  * To learn about the Ops Agent and supported integrations, see:

    * [Ops Agent overview](https://docs.cloud.google.com/logging/docs/agent/ops-agent).
    * [Monitor third-party applications](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party)
  * For information about viewing logs in the Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * For information about querying in the Logs Explorer, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).

  * For information about how to collect and view Apache web server metrics, see the quickstart [Collect Apache web server metrics with the Ops Agent](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine).

  * For more information about Monitoring and its relation to Cloud Logging, see [Monitoring](https://docs.cloud.google.com/monitoring/docs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
