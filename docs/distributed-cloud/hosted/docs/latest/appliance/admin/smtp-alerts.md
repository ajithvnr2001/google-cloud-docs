---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/smtp-alerts/
title: Configure a Simple Mail Transfer Protocol (SMTP) notification channel for Prometheus alerts \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:39.807864+00:00
---

# Configure a Simple Mail Transfer Protocol (SMTP) notification channel for Prometheus alerts  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/smtp-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure a Simple Mail Transfer Protocol (SMTP) notification channel for Prometheus alerts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a Simple Mail Transfer Protocol (SMTP) notification channel for Prometheus alerts. If you choose not to set up this notification channel, you can still view alerts at infra-obs or platform-obs.

## Before you begin

[Configure the device and install software](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup)

## Configure notification channels

Work through the following steps to configure Slack or email notification channels:

  1. To create a custom alert notification channel, host the SMTP server in your network and have the SMTP configuration details (IP, username, password, receiver email) ready to create the alertmanager config. You can validate the correctness of the SMTP host IP by pinging it from [bm03](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#ssh-bm03).

**Note:** Perform the following steps for both of the namespaces (`infra-obs` and `platform-obs`) and any additional namespaces created by the user. 
  2. Create a file `cm.yml` with the following content:

The `smtp_smarthost` must have the IP address of the SMTP server hosted by the customer.
         
         apiVersion: v1
           kind: ConfigMap
           metadata:
             # The name must match the ConfigMap name specified in the ObservabilityPipeline custom resource.
             name: appl-alert-notification
             # The namespace must match the project namespace
             namespace: PROJECT_NAMESPACE
           data:
             # The file name must be alertmanager.yml
             alertmanager.yml: |
               global:
                 smtp_smarthost: SMTP HOST IP ADDRESS
                 smtp_from: FROM_EMAIL_ADDRESS
                 # Give empty string for unsecured smtp server in username and password and false in smtp_require_tls.
                 smtp_auth_username: USERNAME
                 smtp_auth_password: PASSWORD
                 smtp_require_tls: true
               route:
                 group_by: ['alertname', 'cluster', 'service']
                 group_wait: 30s
                 group_interval: 5m
                 repeat_interval: 3h
                 receiver: team-X-mails
               receivers:
                 - name: 'team-X-mails'
                   email_configs:
                     - to: **RECIEVER_EMAIL_ID**
         

  3. Update the required fields with the correct content.

  4. Run `kubectl apply -f cm.yaml`.

  5. Create an `ObservabilityPipeline` custom resource with the following:
         
         # Configure observability pipeline
           apiVersion: observability.gdc.goog/v1
           kind: ObservabilityPipeline
           metadata:
             # Choose namespace that matches the project's namespace
             namespace: PROJECT_NAMESPACE
             name: observability-config
           spec:
             # Configure Alertmanager
             alerting:
               # Permission: PA and AO
               # The alerts configuration must be in the key "alertmanager.yml" of the configMap
               alertmanagerConfig: CUSTOMIZED_CONFIGMAP_NAME
             ...
         

Replace the following:

     * PROJECT_NAMESPACE: The namespace of your project.
     * CUSTOMIZED_CONFIGMAP_NAME: The name you used for your configuration file in the `ConfigMap` object must match exactly with the name of the `ConfigMap` object. For example in step 2, if you used `appl-alert-notification` as the `ConfigMap` name, then use the same name for your configuration file in the `ObservabilityPipeline` object. 

**Note:** You must create a CR for both the namespaces, `infra-obs` as well as `platform-obs`. There must be a separate configmap and `ObservabilityPipeline` for each namespace.
  6. Update the namespace to the value used in the previous step.

  7. Run `kubectl apply -f ob.yaml.`

  8. All the alerts visible on the Grafana dashboard of the GDC trigger an email if they are in a `firing` state. Launch Grafana for the namespace which you used in the previous steps and check for alerts in a `firing` state. The alerts come to your email.


**Note:** Refer to [Configure notification channels for alerts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-notification-channels) for more information on configuring notification channels for the alerts you set up.

## What's next

  * [Manage PKI certificates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/web-tls-cert-config)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
