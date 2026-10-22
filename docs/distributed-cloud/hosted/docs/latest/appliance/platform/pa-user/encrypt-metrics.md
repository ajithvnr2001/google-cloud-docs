---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/encrypt-metrics/
title: Encrypt metrics from your applications \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:00.899010+00:00
---

# Encrypt metrics from your applications  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/encrypt-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Encrypt metrics from your applications Stay organized with collections  Save and categorize content based on your preferences. 

All metrics data must be encrypted in transit to ensure security. The monitoring component of Google Distributed Cloud (GDC) air-gapped appliance provides in-transit encryption and authentication through mutual Transport Layer Security (mTLS). The mTLS method verifies the identity of both parties in a network connection, confirming they are who they claim to be.

This page explains how to set up mTLS for your metrics server.

## Before you begin

To manage `MonitoringTarget` custom resources, request the necessary permissions from your administrator.

### Required IAM roles

Contact your Project IAM Admin to request the following roles:

  * **MonitoringTarget Creator** (`monitoringtarget-creator`):create `MonitoringTarget` custom resources in the project namespace.
  * **MonitoringTarget Editor** (`monitoringtarget-editor`): edit or delete `MonitoringTarget` custom resources in the project namespace.
  * **MonitoringTarget Viewer** (`monitoringtarget-viewer`): view `MonitoringTarget` custom resources in the project namespace.



After obtaining the necessary permissions, complete these steps before enabling metrics encryption:

  1. Deploy your metrics server.
  2. [Collect metrics from your workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/collect-metrics).
  3. Ensure your `MonitoringTarget` custom resource shows a `Ready` status, like in the following example:
         
         apiVersion: monitoring.gdc.goog/v1
         kind: MonitoringTarget
         [...]
         status:
           conditions:
           - lastTransitionTime: "2023-10-27T15:27:51Z"
             message: ""
             observedGeneration: 1
             reason: Ready
             status: True
             type: Ready
         

  4. [Query and view metrics on dashboards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/query-and-view-metrics#query-and-view-metrics-on-dashboards) to confirm that your metrics server is sending the expected data.

**Note:** If metrics are not showing up, resolve any issues with your `MonitoringTarget` configuration before enabling mTLS. Review the [Collect metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/collect-metrics) documentation to ensure your configuration is correct.



## Mount the certificate

Your workload needs to use a certificate that is automatically generated when you enable mTLS on the `MonitoringTarget` custom resource. Add a volume and volume mount for this certificate using the following template:
    
    
    apiVersion: apps/v1
    kind: Deployment # or StatefulSet
    metadata:
      name: "SERVICE_NAME"
    spec:
      template:
        spec:
          containers:
            - name: "CONTAINER_NAME"
              volumeMounts:
              - mountPath: "/etc/ssl/MONITORING_TARGET_NAME-cert"
                name: "MONITORING_TARGET_NAME-cert"
                readOnly: true
          volumes:
          - name: "MONITORING_TARGET_NAME-cert"
            secret:
              secretName: "MONITORING_TARGET_NAME-cert"
      [...]
    

Replace the following:

  * `SERVICE_NAME`: the name of your `Deployment` or `StatefulSet` object.
  * `CONTAINER_NAME`: the name of the container where you are adding the volume mount.
  * `MONITORING_TARGET_NAME`: the name of your `MonitoringTarget` custom resource. The secret name is based on this name. For example, a `my-mon-target` resource creates a `my-mon-target-cert` secret name.



## Serve metrics

Your metrics server must serve metrics from an mTLS-enabled HTTP server. You might want to encrypt metrics in one of the following two scenarios:

  * **For applications you own** : Modify the source code to support mTLS and configure the metrics server with the mTLS certificate.
  * **For applications you don't own** : Consult the application's documentation to enable an HTTPS metrics endpoint. Apply the necessary configuration, like configuring command-line arguments or deploying a `config` file.



## Enable mTLS metrics collection

Add the following label to the `metadata` section of your `MonitoringTarget` custom resource to enable the collection of encrypted metrics:
    
    
    monitoring.gdc.goog/enable-mtls: "true"
    

The custom resource must look like the following example:
    
    
      apiVersion: monitoring.gdc.goog/v1
      kind: MonitoringTarget
      metadata:
        namespace: my-project-namespace
        name: "SERVICE_NAME"
        labels:
          monitoring.gdc.goog/enable-mtls: "true" # Enable mTLS metrics collection
      spec:
        [...]
    

To verify that you enabled mTLS authentication, check that your `MonitoringTarget` custom resource shows a `Ready` status for the certificate and the certificate secret, like in the following example:
    
    
    apiVersion: monitoring.gdc.goog/v1
    kind: MonitoringTarget
    [...]
    status:
      conditions:
      - lastTransitionTime: "2023-11-09T11:15:10Z"
        message: "admin,user-vm-1,user-vm-2,org-1-system"
        observedGeneration: 2
        reason: Ready
        status: "True"
        type: Ready
      - lastTransitionTime: "2023-11-09T11:14:43Z"
        message: "Certificate is ready"
        observedGeneration: 2
        reason: Ready
        status: "True"
        type: CertificateReady
      - lastTransitionTime: "2023-11-09T11:15:10Z"
        message: "Successfully created secret"
        observedGeneration: 2
        reason: Ready
        status: "True"
        type: CertificateSecretReady
    

**Note:** Certificates reside in the org infrastructure cluster. Only certificate _secrets_ exist in Kubernetes clusters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
