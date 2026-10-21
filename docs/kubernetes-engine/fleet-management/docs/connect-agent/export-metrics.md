---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/export-metrics/
title: Export Connect Agent metrics to Cloud Monitoring \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:59:10.609485+00:00
---

# Export Connect Agent metrics to Cloud Monitoring  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/export-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Export Connect Agent metrics to Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to export Connect Agent metrics to Cloud Monitoring from Google Distributed Cloud, GKE on AWS, or any other registered Kubernetes cluster.

## Overview

In a Google Distributed Cloud or GKE on AWS cluster, Prometheus collects metrics and stores them locally within the cluster. Registering a cluster outside Google Cloud to a fleet creates a Deployment called Connect Agent in the cluster. Prometheus collects useful metrics from Connect Agent, like errors connecting to Google and the number of open connections. To make these metrics available to Cloud Monitoring, you must:

  * Expose the Connect Agent using a Service.
  * Deploy [`prometheus-to-sd`](https://github.com/GoogleCloudPlatform/k8s-stackdriver), a simple component that scrapes Prometheus metrics and exports them to Cloud Monitoring.



Afterwards, you view the metrics by using Monitoring in the Google Cloud console, or by port forwarding the Service and using `curl`.

## Creating a variable for Connect Agent's namespace

Connect Agent typically runs in the namespace `gke-connect`.

Connect Agent has a label, `hub.gke.io/project`. The HTTP server listens on port 8080.

Create a variable, `AGENT_NS`, for the namespace:
    
    
    AGENT_NS=$(kubectl get ns --kubeconfig KUBECONFIG -o jsonpath={.items..metadata.name} -l hub.gke.io/project=PROJECT_ID)

Replace the following:

  * `KUBECONFIG`: the kubeconfig file for your cluster
  * `PROJECT_ID`: the project ID



## Exposing Connect Agent Deployment

  1. Copy the following configuration to a YAML file named `gke-connect-agent.yaml`. This configuration creates a Service, `gke-connect-agent`, which exposes the Connect Agent Deployment.
         
         apiVersion: v1
         kind: Service
         metadata:
           labels:
             app: gke-connect-agent
           name: gke-connect-agent
         spec:
           ports:
           - port: 8080
             protocol: TCP
             targetPort: 8080
           selector:
             app: gke-connect-agent
           type: ClusterIP

  2. Apply the YAML file to the Connect Agent's namespace in your cluster, where `KUBECONFIG` is the path to the cluster's kubeconfig file:
         
         kubectl apply -n ${AGENT_NS} --kubeconfig KUBECONFIG -f gke-connect-agent.yaml

  3. Bind the `roles/monitoring.metricWriter` IAM role to the fleet Google service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/monitoring.metricWriter"

     * `PROJECT_ID` is your Google Cloud project ID. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `SERVICE_ACCOUNT_NAME` is the service account used when [registering the cluster](https://cloud.google.com/service-mesh/docs/register-cluster#creating_a_service_account_and_key_file).



## Deploying `prometheus-to-sd`

  1. Copy the following configuration to a YAML file, named `prometheus-to-sd.yaml` where:

     * `PROJECT_ID` is your Google Cloud project ID. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CLUSTER_NAME` is the of the Kubernetes cluster where Connect Agent runs.
     * `REGION` is the location that is geographically close to where your cluster runs. Choose a [Google Cloud zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) that is geographically close to where the cluster is physically located.
     * `ZONE` is the location near your on-prem datacenter. Choose a Google Cloud zone that is geographically close to where traffic flows.

This configuration creates two resources:

     * A ConfigMap, `prom-to-sd-user-config`, which declares several variables for use by the Deployment
     * A Deployment, `prometheus-to-monitoring`, which runs `prometheus-to-sd` in a single Pod.
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: prom-to-sd-user-config
    data:
      # The project that the Connect Agent uses. Accepts ID or number.
      project: PROJECT_ID
      # A name for the cluster, which shows up in Cloud Monitoring.
      cluster_name: CLUSTER_NAME
      # cluster_location must be valid (e.g. us-west1-a); shows up in Cloud Monitoring.
      cluster_location: REGION
      # A zone name to report (e.g. us-central1-a).
      zone: ZONE
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: prometheus-to-monitoring
    spec:
      progressDeadlineSeconds: 600
      replicas: 1
      revisionHistoryLimit: 2
      selector:
        matchLabels:
          run: prometheus-to-monitoring
      template:
        metadata:
          labels:
            run: prometheus-to-monitoring
        spec:
          containers:
            - args:
                - /monitor
                # 'gke-connect-agent' is the text that will show up in the Cloud Monitoring metric name.
                - --source=gke-connect-agent:http://gke-connect-agent:8080
                - --monitored-resource-types=k8s
                - --stackdriver-prefix=custom.googleapis.com
                - --project-id=$(PROM_PROJECT)
                - --cluster-name=$(PROM_CLUSTER_NAME)
                - --cluster-location=$(PROM_CLUSTER_LOCATION)
                - --zone-override=$(PROM_ZONE)
                # A node name to report. This is a dummy value.
                - --node-name=MyGkeConnectAgent
              env:
                - name: GOOGLE_APPLICATION_CREDENTIALS
                  value: /etc/creds/creds-gcp.json
                - name: PROM_PROJECT
                  valueFrom:
                    configMapKeyRef:
                      name: prom-to-sd-user-config
                      key: project
                - name: PROM_CLUSTER_NAME
                  valueFrom:
                    configMapKeyRef:
                      name: prom-to-sd-user-config
                      key: cluster_name
                - name: PROM_CLUSTER_LOCATION
                  valueFrom:
                    configMapKeyRef:
                      name: prom-to-sd-user-config
                      key: cluster_location
                - name: PROM_ZONE
                  valueFrom:
                    configMapKeyRef:
                      name: prom-to-sd-user-config
                      key: zone
              image: gcr.io/google-containers/prometheus-to-sd:v0.7.1
              imagePullPolicy: IfNotPresent
              name: prometheus-to-monitoring
              resources: {}
              terminationMessagePath: /dev/termination-log
              terminationMessagePolicy: File
              volumeMounts:
                - mountPath: /etc/creds
                  name: creds-gcp
                  readOnly: true
          restartPolicy: Always
          schedulerName: default-scheduler
          securityContext: {}
          terminationGracePeriodSeconds: 30
          volumes:
            - name: creds-gcp
              secret:
                defaultMode: 420
                # This secret is already set up for the Connect Agent.
                secretName: creds-gcp

  2. Apply the YAML file to the Connect Agent's namespace in your cluster, where `KUBECONFIG` is the path to the cluster's kubeconfig file:
         
         kubectl apply -n ${AGENT_NS} --kubeconfig KUBECONFIG -f prometheus-to-sd.yaml




## Viewing metrics

### Console

  1. Go to the Monitoring page in Google Cloud console.

[Go to the Monitoring page](https://console.cloud.google.com/monitoring)

  2. From the left menu, click **Metrics Explorer**.

  3. Connect Agent's metrics are prefixed with `custom.googleapis.com/gke-connect-agent/`, where `gke-connect-agent` is the string specified in the `--source` argument. For example, `custom.googleapis.com/gke-connect-agent/gkeconnect_dialer_connection_errors_total`




### cURL

  1. In a shell, use `kubectl` to port forward the `gke-connect-monitoring` Service:
         
         kubectl -n ${AGENT_NS} port-forward svc/gke-connect-monitoring 8080

  2. Open another shell, then run:
         
         curl localhost:8080/metrics




## Cleaning up

To delete the resources you created in this topic:
    
    
    AGENT_NS=$(kubectl get ns --kubeconfig KUBECONFIG -o jsonpath={.items..metadata.name} -l hub.gke.io/project)
    kubectl delete configmap prom-to-sd-user-config --kubeconfig KUBECONFIG -n ${AGENT_NS}
    kubectl delete service gke-connect-agent --kubeconfig KUBECONFIG -n ${AGENT_NS}
    kubectl delete deployment prometheus-to-monitoring --kubeconfig KUBECONFIG -n ${AGENT_NS}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
