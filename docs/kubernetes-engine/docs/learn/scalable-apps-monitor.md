---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-monitor/
title: Learning Path: Scalable applications - Monitor with Prometheus \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:45.968278+00:00
---

# Learning Path: Scalable applications - Monitor with Prometheus  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Scalable applications - Monitor with Prometheus Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This set of tutorials is for IT administrators and Operators who want to deploy, run, and manage modern application environments that run on Google Kubernetes Engine (GKE). As you progress through this set of tutorials you learn how to configure monitoring and alerts, scale workloads, and simulate failure, all using the Cymbal Bank sample microservices application:

  1. [Create a cluster and deploy a sample application](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment)
  2. Monitor with Google Cloud Managed Service for Prometheus (this tutorial)
  3. [Scale workloads](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-autoscale)
  4. [Simulate a failure](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-failure)
  5. [Centralize change management](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-centralize)



## Overview and objectives

The Cymbal Bank sample application used in this set of tutorials is made up of a number of microservices that all run in the GKE cluster. Problems with any of these services could result in a bad experience for the bank's customers, such as not being able to access the bank application. Learning about problems with the services as soon as possible means you can quickly start to troubleshoot and resolve the issues.

In this tutorial, you learn how to monitor workloads in a GKE cluster using Google Cloud Managed Service for Prometheus and Cloud Monitoring. You learn how to complete the following tasks:

  * Create a Slack webhook for Alertmanager.

  * Configure Prometheus to monitor the status of a sample microservices-based application.

  * Simulate an outage and review the alerts sent using the Slack webhook.




## Costs

Enabling GKE and deploying the Cymbal Bank sample application for this series of tutorials means that you incur per-cluster charges for GKE on Google Cloud as listed on our [Pricing page](https://cloud.google.com/kubernetes-engine/pricing) until you disable GKE or delete the project.

You are also responsible for other Google Cloud costs incurred while running the Cymbal Bank sample application, such as charges for Compute Engine VMs and Cloud Monitoring.

## Before you begin

To learn how to monitor your workloads, you must complete the [first tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment) to create a GKE cluster that uses Autopilot and deploy the Cymbal Bank sample microservices-based application.

We recommend that you complete this set of tutorials for scalable apps in order. As you progress through the set of tutorials, you learn new skills and use additional Google Cloud products and services.

To show an example of how a GKE Autopilot cluster can use Google Cloud Managed Service for Prometheus to generate messages to a communications platform, this tutorial uses Slack. In your own production deployments, you can use your organization's preferred communication tool to process and deliver messages when your GKE cluster has an issue.

  * [Join a Slack workspace](https://slack.com/intl/en-ca/help/articles/212675257-Join-a-Slack-workspace), either by registering with your email or by using an invitation sent by a Workspace Admin.

**Note:** If you are not an Admin for your Slack workspace, you might need approval from a Workspace Admin before your app is deployed to your workspace.



## Create a Slack application

An important part of setting up monitoring is making sure that you're notified when actionable events such as outages occur. A common pattern for this is to send notifications to a communication tool such as Slack, which is what you use in this tutorial. Slack provides a webhooks feature that lets external applications, like your production deployments, generate messages. You can use other communication tools in your organization to process and deliver messages when your GKE cluster has an issue.

GKE clusters that use Autopilot include a Google Cloud Managed Service for Prometheus instance. This instance can generate alerts when something happens to your applications. These alerts can then use a Slack webhook to send a message to your Slack workspace so you receive prompt notifications when there's a problem.

To set up Slack notifications based on alerts generated by Prometheus, you must create a Slack application, activate Incoming Webhooks for the application, and install the application to a Slack workspace.

  1. [Sign in to Slack](https://slack.com/signin) using your workspace name and your Slack account credentials.

  2. [Create a new Slack app](https://api.slack.com/apps?new_app=1)

     1. In the **Create an app** dialog, click **From scratch**.
     2. Specify an **App Name** and choose your Slack workspace.
     3. Click **Create App**.
     4. Under **Add features and functionality** , click **Incoming Webhooks**.
     5. Click the **Activate Incoming Webhooks** toggle.
     6. In the **Webhook URLs for Your Workspace** section, click **Add New Webhook to Workspace**.
     7. On the authorization page that opens, select a channel to receive notifications.
     8. Click **Allow**.
     9. A webhook for your Slack application is displayed in the **Webhook URLs for Your Workspace** section. Save the URL for later.



## Configure Alertmanager

In Prometheus, Alertmanager processes monitoring events that your deployments generate. Alertmanager can skip duplicate events, group related events, and send notifications, like using a Slack webhook. This section shows you how to configure Alertmanager to use your new Slack webhook. Specifying how you want Alertmanager to process events to send is covered in the next section of the tutorial, Configure Prometheus.

To configure Alertmanager to use your Slack webhook, complete the following steps:

  1. Change directories to the Git repository that includes all the sample manifests for Cymbal Bank from the previous tutorial:
         
         cd ~/bank-of-anthos/
         

If needed, change the directory location to where you previously cloned the repository.

  2. Update the Alertmanager sample YAML manifest with the webhook URL of your Slack application:
         
         sed -i "s@SLACK_WEBHOOK_URL@SLACK_WEBHOOK_URL@g" "extras/prometheus/gmp/alertmanager.yaml"
         

Replace `SLACK_WEBHOOK_URL` with the URL of the webhook from the previous section.

  3. To dynamically use your unique Slack webhook URL without changes to the application code, you can use a Kubernetes Secret. The application code reads the value of this Secret. In more complex applications, this ability lets you change, or rotate, values for security or compliance reasons.

Create a Kubernetes secret for Alertmanager using the sample YAML manifest that contains the Slack webhook URL:
         
         kubectl create secret generic alertmanager \
           -n gmp-public \
           --from-file=extras/prometheus/gmp/alertmanager.yaml
         

  4. Prometheus can use _exporters_ to get metrics from applications without code changes. The Prometheus blackbox exporter lets you probe endpoints like HTTP or HTTPS. This exporter works well when you don't want to, or can't, expose the inner workings of your application to Prometheus. The Prometheus blackbox exporter can work without changes to your application code to expose metrics to Prometheus.

Deploy the Prometheus blackbox exporter to your cluster:
         
         kubectl apply -f extras/prometheus/gmp/blackbox-exporter.yaml
         




## Configure Prometheus

After you have configured Alertmanager to use your Slack webhook, you need to tell Prometheus what to monitor in Cymbal Bank, and what kinds of event you want Alertmanager to notify you about using the Slack webhook.

In the Cymbal Bank sample application that you use in these tutorials, there are various microservices that run in the GKE cluster. One problem you probably want to know about as soon as possible is if one of the Cymbal Bank services has stopped responding normally to requests, potentially meaning your customers can't access the application. You can configure Prometheus to respond to events based on your organization's policies.

### Probes

You can configure Prometheus probes for the resources that you want to monitor. These probes can generate alerts based on the response that the probes receive. In the Cymbal Bank sample application, you can use HTTP probes that check for 200-level response codes from the Services. An HTTP 200-level response indicates that the Service is running correctly and can respond to requests. If there's a problem and the probe doesn't receive the expected response, you can define Prometheus rules that generate alerts for Alertmanager to process and perform additional actions.

  1. Create some Prometheus probes to monitor the HTTP status of the various microservices of the Cymbal Bank sample application. Review the following sample manifest:
         
         # Copyright 2023 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: frontend-probe
           labels:
             app.kubernetes.io/name: frontend-probe
         spec:
           selector:
             matchLabels:
               app: blackbox-exporter
           endpoints:
           - port: metrics
             path: /probe
             params:
               target: [frontend:80]
               module: [http_2xx]
             timeout: 30s
             interval: 60s
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: userservice-probe
           labels:
             app.kubernetes.io/name: userservice-probe
         spec:
           selector:
             matchLabels:
               app: blackbox-exporter
           endpoints:
           - port: metrics
             path: /probe
             params:
               target: [userservice:8080/ready]
               module: [http_2xx]
             timeout: 30s
             interval: 60s
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: balancereader-probe
           labels:
             app.kubernetes.io/name: balancereader-probe
         spec:
           selector:
             matchLabels:
               app: blackbox-exporter
           endpoints:
           - port: metrics
             path: /probe
             params:
               target: [balancereader:8080/ready]
               module: [http_2xx]
             timeout: 30s
             interval: 60s
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: contacts-probe
           labels:
             app.kubernetes.io/name: contacts-probe
         spec:
           selector:
             matchLabels:
               app: blackbox-exporter
           endpoints:
           - port: metrics
             path: /probe
             params:
               target: [contacts:8080/ready]
               module: [http_2xx]
             timeout: 30s
             interval: 60s
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: ledgerwriter-probe
           labels:
             app.kubernetes.io/name: ledgerwriter-probe
         spec:
           selector:
             matchLabels:
               app: blackbox-exporter
           endpoints:
           - port: metrics
             path: /probe
             params:
               target: [ledgerwriter:8080/ready]
               module: [http_2xx]
             timeout: 30s
             interval: 60s
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: transactionhistory-probe
           labels:
             app.kubernetes.io/name: transactionhistory-probe
         spec:
           selector:
             matchLabels:
               app: blackbox-exporter
           endpoints:
           - port: metrics
             path: /probe
             params:
               target: [transactionhistory:8080/ready]
               module: [http_2xx]
             timeout: 30s
             interval: 60s
         

As shown in this manifest file, it's best practice that each `PodMonitoring` Prometheus liveness probe monitors each Deployment separately.

  2. To create the Prometheus liveness probes, apply the manifest to your cluster:
         
         kubectl apply -f extras/prometheus/gmp/probes.yaml
         




### Rules

Prometheus needs to know what you want to do based on the response that the probes you created in the previous steps receive. You define this response using Prometheus rules.

In this tutorial, you create Prometheus rules to generate alerts depending on the response to the liveness probe. Alertmanager then processes the output of these rules to generate notifications using the Slack webhook.

  1. Create rules that generate events based on the response to the liveness probes. Review the following sample manifest:
         
         # Copyright 2023 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         ---
         apiVersion: monitoring.googleapis.com/v1
         kind: Rules
         metadata:
           name: uptime-rule
         spec:
           groups:
           - name: Micro services uptime
             interval: 60s
             rules:
             - alert: BalancereaderUnavailable
               expr: probe_success{job="balancereader-probe"} == 0
               for: 1m
               annotations:
                 summary: Balance Reader Service is unavailable
                 description: Check Balance Reader pods and its logs
               labels:
                 severity: 'critical'
             - alert: ContactsUnavailable
               expr: probe_success{job="contacts-probe"} == 0
               for: 1m
               annotations:
                 summary: Contacts Service is unavailable
                 description: Check Contacts pods and its logs
               labels:
                 severity: 'warning'
             - alert: FrontendUnavailable
               expr: probe_success{job="frontend-probe"} == 0
               for: 1m
               annotations:
                 summary: Frontend Service is unavailable
                 description: Check Frontend pods and its logs
               labels:
                 severity: 'critical'
             - alert: LedgerwriterUnavailable
               expr: probe_success{job="ledgerwriter-probe"} == 0
               for: 1m
               annotations:
                 summary: Ledger Writer Service is unavailable
                 description: Check Ledger Writer pods and its logs
               labels:
                 severity: 'critical'
             - alert: TransactionhistoryUnavailable
               expr: probe_success{job="transactionhistory-probe"} == 0
               for: 1m
               annotations:
                 summary: Transaction History Service is unavailable
                 description: Check Transaction History pods and its logs
               labels:
                 severity: 'critical'
             - alert: UserserviceUnavailable
               expr: probe_success{job="userservice-probe"} == 0
               for: 1m
               annotations:
                 summary: User Service is unavailable
                 description: Check User Service pods and its logs
               labels:
                 severity: 'critical'
         

This manifest describes a `PrometheusRule` and includes the following fields:

     * `spec.groups.[*].name`: the name of the rule group.
     * `spec.groups.[*].interval`: how often rules in the group are evaluated.
     * `spec.groups.[*].rules[*].alert`: the name of the alert.
     * `spec.groups.[*].rules[*].expr`: the PromQL expression to evaluate.
     * `spec.groups.[*].rules[*].for`: the amount of time alerts must return for before they are considered firing.
     * `spec.groups.[*].rules[*].annotations`: a list of annotations to add to each alert. This is only valid for alerting rules.
     * `spec.groups.[*].rules[*].labels`: the labels to add or overwrite.
  2. To create the rules, apply the manifest to your cluster:
         
         kubectl apply -f extras/prometheus/gmp/rules.yaml
         


**Objective:** Congratulations! You now have a managed Prometheus instance in your GKE cluster that's configured to monitor the Cymbal Bank sample application and send Slack messages to you when there's a problem.

## Simulate an outage

To make sure that your Prometheus probes, rules, and Alertmanager configuration are correct, you should test that alerts and notifications are sent when there's a problem. If you don't test this flow, you might not realize there's an outage of your production services when something goes wrong.

  1. To simulate an outage of one of the microservices, scale the `contacts` Deployment to zero. With zero instances of the Service, the Cymbal Bank sample application can't read contact information for customers:
         
         kubectl scale deployment contacts --replicas 0
         

GKE might take up to 5 minutes to scale down the Deployment.

  2. Check the status of the Deployments in your cluster and verify that the `contacts` Deployment scales down correctly:
         
         kubectl get deployments
         

In the following example output, the `contacts` Deployment has successfully scaled down to `0` instances:
         
         NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
         balancereader        1/1     1            1           17m
         blackbox-exporter    1/1     1            1           5m7s
         contacts             0/0     0            0           17m
         frontend             1/1     1            1           17m
         ledgerwriter         1/1     1            1           17m
         loadgenerator        1/1     1            1           17m
         transactionhistory   1/1     1            1           17m
         userservice          1/1     1            1           17m
         

  3. After the `contacts` Deployment has scaled down to zero, the Prometheus probe reports a HTTP error code. This HTTP error generates an alert for Alertmanager to then process.

Check your Slack workspace channel for an outage notification message with text similar to the following example:
         
         [FIRING:1] ContactsUnavailable
         Severity: Warning :warning:
         Summary: Contacts Service is unavailable
         Namespace: default
         Check Contacts pods and it's logs
         

  4. In a real outage scenario, after you receive the notification in Slack you would start to troubleshoot and restore services. For this tutorial, simulate this process and restore the `contacts` Deployment by scaling back up the number of replicas:
         
         kubectl scale deployment contacts --replicas 1
         

It might take up to 5 minutes to scale the Deployment and for the Prometheus probe to receive an HTTP 200 response. You check the status of the Deployments using the `kubectl get deployments` command.

When a healthy response to the Prometheus probe is received, Alertmanager clears the event. You should see an alert resolution notification message in your Slack workspace channel similar to the following example:
         
         [RESOLVED] ContactsUnavailable
         Severity: Warning :warning:
         Summary: Contacts Service is unavailable
         Namespace: default
         Check Contacts pods and it's logs
         


**Objective:** Congratulations! Your managed Prometheus instance in your GKE cluster can successfully monitor the Cymbal Bank sample application and send Slack messages to respond to events.

## Clean up

We recommend that you complete this set of tutorials for Cymbal Bank in order. As you progress through the set of tutorials, you learn new skills and use additional Google Cloud products and services.

If you want to take a break before you move on to the next tutorial and avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the project you created.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

Learn how to [scale your deployments in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-autoscale) in the next tutorial.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
