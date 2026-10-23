---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment/
title: Learning Path: Scalable applications - Create a cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:11.618396+00:00
---

# Learning Path: Scalable applications - Create a cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Scalable applications - Create a cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This set of tutorials is for IT administrators and Operators who want to deploy, run, and manage modern application environments that run on Google Kubernetes Engine (GKE). As you progress through this set of tutorials you learn how to configure monitoring and alerts, scale workloads, and simulate failure, all using the Cymbal Bank sample microservices application:

  1. Create a cluster and deploy a sample application (this tutorial)
  2. [Monitor with Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-monitor)
  3. [Scale workloads](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-autoscale)
  4. [Simulate a failure](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-failure)
  5. [Centralize change management](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-centralize)



## Overview and objectives

Cymbal Bank uses Python and Java to run the various services, and includes a PostgreSQL backend. You don't need experience with these languages or database platform to complete the series of tutorials, as Cymbal Bank is just an example application to show how GKE can support the needs of your business.

In this tutorial, you learn how to create a single GKE cluster and deploy a sample microservices-based application named Cymbal Bank to a GKE cluster. You learn how to complete the following tasks:

  * Create a GKE cluster that uses Autopilot.

  * Deploy a sample microservices-based application named Cymbal Bank.

  * Use the Google Cloud console to explore the GKE resources used by the Cymbal Bank sample application.




## Costs

Enabling GKE and deploying the Cymbal Bank sample application for this series of tutorials means that you incur per-cluster charges for GKE on Google Cloud as listed on our [Pricing page](https://cloud.google.com/kubernetes-engine/pricing) until you disable GKE or delete the project.

You are also responsible for other Google Cloud costs incurred while running the Cymbal Bank sample application, such as charges for Compute Engine VMs and load balancers.

## Before you begin

In this first tutorial in the series, complete all the following "Begin you begin" setup steps before you get started. You only need to complete the following "Before you begin" steps once.

### Configure your shell and tools

In this series of tutorials, you use the following tools to deploy and manage your environment:

  * gcloud CLI: create and manage GKE clusters and fleets, along with other Google Cloud services.
  * `kubectl`: manage Kubernetes, the cluster orchestration system used by GKE.



To run the commands on this page, set up the Google Cloud CLI and `kubectl` in one of the following development environments:

###  Cloud Shell 

To use an online terminal with the gcloud CLI and `kubectl` already set up, activate Cloud Shell:

At the bottom of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

### Local shell

To use a local development environment, follow these steps:

  * [ Install the gcloud CLI.](https://docs.cloud.google.com/sdk/docs/install)
  * [ Initialize the gcloud CLI.](https://docs.cloud.google.com/sdk/docs/initialize)
  * Install `kubectl` the gcloud CLI:
        
        gcloud components install kubectl
        




### Set up your project

Take the following steps to set up a Google Cloud project, including enabling billing and GKE services. This is the project where you will enable GKE.

You might need a Google Cloud administrator in your organization to grant you access to create or use a project and enable APIs.

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page:

[Go to the Google Kubernetes Engine page](https://console.cloud.google.com/projectselector/kubernetes)

  2. Create or select a project. This is the project where you enable GKE.

  3. If prompted, **Enable** the GKE API.

  4. Wait for the API and related services to be enabled. This can take several minutes.

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Grant IAM roles

If you are the project owner (such as if you created the project yourself), you already have all the permissions necessary to complete these tutorials. If you are not the owner, ensure that your Google Cloud account has the required [IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions) to your selected project for this set of tutorials. Again, you might need a Google Cloud administrator in your organization to help grant the required roles.

In the following commands, replace `PROJECT_ID` with the automatically-generated ID of the project that you created or selected in the previous section. The project ID is often different from the project name. For example, your project might be _scalable-apps_ , but your project ID might be _scalable-apps-567123_.

Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/resourcemanager.projectIamAdmin, roles/iam.serviceAccountAdmin, roles/iam.serviceAccountUser, roles/iam.securityAdmin, roles/serviceusage.serviceUsageAdmin, roles/container.admin, roles/logging.logWriter, roles/gkehub.admin, roles/viewer, roles/monitoring.viewer`
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
  * `ROLE`: The IAM role that you grant to your user account.



### Clone the sample application

Clone the Git repository that includes all the sample manifests for Cymbal Bank:
    
    
      git clone https://github.com/GoogleCloudPlatform/bank-of-anthos
      cd bank-of-anthos/
    

## Create a cluster

With all of the prerequisite steps in the previous sections complete, you can now start to create a GKE cluster and deploy a sample application.

GKE is a managed Kubernetes service that you can use to deploy and operate containerized applications. A GKE environment consists of _nodes_ , which are Compute Engine virtual machines (VMs), that are grouped together to form a _cluster_.

  * Create a GKE cluster that you use in the rest of the tutorials in this series:
        
        gcloud container clusters create-auto scalable-apps \
          --project=PROJECT_ID \
          --location=CONTROL_PLANE_LOCATION
        

Replace the following:

    * `PROJECT_ID` with the automatically-generated ID of the project that you created in the previous section. The project ID is often different from the project name. For example, your project might be _scalable-apps_ , but your project ID might be _scalable-apps-567123_.
    * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region, such as `us-central1`.

It takes a few minutes to create the cluster and verify everything works correctly.




In this set of tutorials, you use Autopilot mode clusters and some default IP address ranges when you create clusters. A production deployment of your own applications requires more careful IP address planning. In Autopilot mode, Google manages your cluster configuration, including autoscale, security, and other preconfigured settings. Clusters in Autopilot mode are optimized to run most production workloads and provision compute resources based on your Kubernetes manifests.

## Deploy Cymbal Bank

You package apps (also called _workloads_) into containers. You deploy sets of containers as _Pods_ to your nodes.

In this series of tutorials, you deploy a sample microservices-based application named Cymbal Bank to one or more GKE clusters. Cymbal Bank uses Python and Java to run the various services, and includes a PostgreSQL backend. You don't need experience with these languages or database platform to complete the series of tutorials. Cymbal Bank is just an example application to show how GKE can support the needs of your business.

When you use Cymbal Bank as part of this set of tutorials, the following services are deployed into your GKE cluster:

Service | Language | Description  
---|---|---  
`frontend` | Python | Exposes an HTTP server to serve the website. Contains login page, signup page, and home page.  
`ledger-writer` | Java | Accepts and validates incoming transactions before writing them to the ledger.  
`balance-reader` | Java | Provides efficient readable cache of user balances, as read from `ledger-db`.  
`transaction-history` | Java | Provides efficient readable cache of past transactions, as read from `ledger-db`.  
`ledger-db` | PostgreSQL | Ledger of all transactions. Option to pre-populate with transactions for demo users.  
`user-service` | Python | Manages user accounts and authentication. Signs JWTs used for authentication by other services.  
`contacts` | Python | Stores list of other accounts associated with a user. Used for drop down in "Send Payment" and "Deposit" forms.  
`accounts-db` | PostgreSQL | Database for user accounts and associated data. Option to pre-populate with demo users.  
`loadgenerator` | Python / Locust | Continuously sends requests imitating users to the frontend. Periodically creates new accounts and simulates transactions between them.  
  
To deploy Cymbal Bank into your GKE cluster, complete the following steps:

  1. Cymbal Bank uses JSON Web Tokens (JWTs) to handle user authentication. JWTs use asymmetric key pairs to sign and verify tokens. In Cymbal Bank, `userservice` creates and signs tokens with an RSA private key when a user signs in, and the other services use the corresponding public key to validate the user.

Create an RS256 JWT that's 4,096 bits in strength:
         
         openssl genrsa -out jwtRS256.key 4096
         openssl rsa -in jwtRS256.key -outform PEM -pubout -out jwtRS256.key.pub
         

If needed, [download and install the OpenSSL tools](https://www.openssl.org/source/) for your platform.

  2. A Kubernetes Secret can store sensitive data like keys or passwords. Workloads that run in your cluster can then access the Secret to get the sensitive data instead of hard-coding it in the application.

Create a Kubernetes Secret from the key file you created in the previous step for Cymbal Bank to use with authentication requests:
         
         kubectl create secret generic jwt-key --from-file=./jwtRS256.key --from-file=./jwtRS256.key.pub
         

  3. Deploy Cymbal Bank to your cluster. The following command deploys all the manifest files in the `kubernetes-manifests` directory. Each manifest file deploys and configures one of the Services:
         
         kubectl apply -f kubernetes-manifests/accounts-db.yaml
         kubectl apply -f kubernetes-manifests/balance-reader.yaml
         kubectl apply -f kubernetes-manifests/config.yaml
         kubectl apply -f kubernetes-manifests/contacts.yaml
         kubectl apply -f extras/postgres-hpa/kubernetes-manifests/frontend.yaml
         kubectl apply -f kubernetes-manifests/ledger-db.yaml
         kubectl apply -f kubernetes-manifests/ledger-writer.yaml
         kubectl apply -f extras/postgres-hpa/loadgenerator.yaml
         kubectl apply -f kubernetes-manifests/transaction-history.yaml
         kubectl apply -f kubernetes-manifests/userservice.yaml
         

You might see messages in the `kubectl` output as the manifests are applied to your cluster about Autopilot limits. Autopilot uses the resource requests that you specify in your workload configuration to configure the nodes that run your workloads. Autopilot enforces minimum and maximum resource requests based on the compute class or the hardware configuration that your workloads use. If you don't specify requests for some containers, Autopilot assigns default values to let those containers run correctly.

Review the following sample manifest for the `frontend` Service:
         
         # Copyright 2026 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #     https://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: v1
         kind: Service
         metadata:
           labels:
             application: bank-of-anthos
             environment: development
             team: frontend
             tier: web
           name: frontend
         spec:
           ports:
             - name: http
               port: 80
               targetPort: 8080
           selector:
             app: frontend
             application: bank-of-anthos
             environment: development
             team: frontend
             tier: web
           type: LoadBalancer
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             application: bank-of-anthos
             environment: development
             team: frontend
             tier: web
           name: frontend
         spec:
           selector:
             matchLabels:
               app: frontend
               application: bank-of-anthos
               environment: development
               team: frontend
               tier: web
           template:
             metadata:
               annotations:
                 proxy.istio.io/config: '{ "holdApplicationUntilProxyStarts": true }'
               labels:
                 app: frontend
                 application: bank-of-anthos
                 environment: development
                 team: frontend
                 tier: web
             spec:
               containers:
                 - env:
                     - name: VERSION
                       value: v0.6.11
                     - name: PORT
                       value: "8080"
                     - name: ENABLE_TRACING
                       value: "true"
                     - name: SCHEME
                       value: http
                     - name: LOG_LEVEL
                       value: info
                     - name: DEFAULT_USERNAME
                       valueFrom:
                         configMapKeyRef:
                           key: DEMO_LOGIN_USERNAME
                           name: demo-data-config
                     - name: DEFAULT_PASSWORD
                       valueFrom:
                         configMapKeyRef:
                           key: DEMO_LOGIN_PASSWORD
                           name: demo-data-config
                     - name: REGISTERED_OAUTH_CLIENT_ID
                       valueFrom:
                         configMapKeyRef:
                           key: DEMO_OAUTH_CLIENT_ID
                           name: oauth-config
                           optional: true
                     - name: ALLOWED_OAUTH_REDIRECT_URI
                       valueFrom:
                         configMapKeyRef:
                           key: DEMO_OAUTH_REDIRECT_URI
                           name: oauth-config
                           optional: true
                   envFrom:
                     - configMapRef:
                         name: environment-config
                     - configMapRef:
                         name: service-api-config
                   image: us-central1-docker.pkg.dev/bank-of-anthos-ci/bank-of-anthos/frontend:v0.6.11@sha256:5746f018f3d85475e25b8283bf8fb476e2501196bbe71e3ce144527e7280e7ae
                   livenessProbe:
                     httpGet:
                       path: /ready
                       port: 8080
                     initialDelaySeconds: 60
                     periodSeconds: 15
                     timeoutSeconds: 30
                   name: front
                   readinessProbe:
                     httpGet:
                       path: /ready
                       port: 8080
                     initialDelaySeconds: 10
                     periodSeconds: 5
                     timeoutSeconds: 10
         ** resources:**
         ** limits:**
         ** cpu: 250m**
         ** memory: 128Mi**
         ** requests:**
         ** cpu: 100m**
         ** memory: 64Mi**
                   securityContext:
                     allowPrivilegeEscalation: false
                     capabilities:
                       drop:
                         - all
                     privileged: false
                     readOnlyRootFilesystem: true
                   volumeMounts:
                     - mountPath: /tmp
                       name: tmp
                     - mountPath: /tmp/.ssh
                       name: publickey
                       readOnly: true
               securityContext:
                 fsGroup: 1000
                 runAsGroup: 1000
                 runAsNonRoot: true
                 runAsUser: 1000
               serviceAccountName: bank-of-anthos
               terminationGracePeriodSeconds: 5
               volumes:
                 - emptyDir: {}
                   name: tmp
                 - name: publickey
                   secret:
                     items:
                       - key: jwtRS256.key.pub
                         path: publickey
                     secretName: jwt-key

This manifest for the `frontend` Service requests `100m` of CPU and `64Mi`, and sets limits of `250m` of CPU and `128Mi` per Pod.

When you deploy a workload in an Autopilot cluster, GKE validates the workload configuration against the allowed minimum and maximum values for the selected compute class or hardware configuration (such as GPUs). If your requests are less than the minimum, Autopilot automatically modifies your workload configuration to bring your requests within the allowed range. These messages indicate that the appropriate limits are being automatically assigned.

  4. Wait for the Pods to be ready. Use `kubectl` to check on the status of the Pods:
         
         kubectl get pods
         

The `STATUS` column changes from `Pending` to `ContainerCreating`. It takes a few minutes for all of the Pods to be in a `Running` state, as shown in the following example output:
         
         NAME                                  READY   STATUS    RESTARTS   AGE
         accounts-db-6f589464bc-6r7b7          1/1     Running   0          99s
         balancereader-797bf6d7c5-8xvp6        1/1     Running   0          99s
         contacts-769c4fb556-25pg2             1/1     Running   0          98s
         frontend-7c96b54f6b-zkdbz             1/1     Running   0          98s
         ledger-db-5b78474d4f-p6xcb            1/1     Running   0          98s
         ledgerwriter-84bf44b95d-65mqf         1/1     Running   0          97s
         loadgenerator-559667b6ff-4zsvb        1/1     Running   0          97s
         transactionhistory-5569754896-z94cn   1/1     Running   0          97s
         userservice-78dc876bff-pdhtl          1/1     Running   0          96s
         

When all the Pods are in the `Running` state, continue to the next step. Again, it takes a few minutes for all of the Pods to be in a `Running` state. It's normal for some of the Pods to report a `READY` status of `0/1` until Cymbal Bank is ready to correctly serve traffic.

  5. The `frontend` service exposes an HTTP server to serve the Cymbal Bank website, including the sign-in page, sign-up page, and home page. An Ingress object defines rules for routing HTTP(S) traffic to applications running in a cluster using a Google Cloud HTTP(S) Load Balancer.

Get the external IP address for the `frontend` Ingress:
         
         kubectl get ingress frontend | awk '{print $4}'
         

  6. In a web browser window, open the IP address shown in the output of the `kubectl get ingress` command to access your instance of Cymbal Bank.

The default credentials are automatically populated, so you can sign in to the app and explore some of the sample transactions and balances. There are no specific actions you need to take, other than to confirm that the Cymbal Bank runs successfully. It might take a minute or two for all the services to be correctly communicating and let you sign in.


**Objective:** Congratulations! You now have a working GKE cluster that uses Autopilot, and have deployed the sample Cymbal Bank microservices application.

## Explore your deployment

After you create a GKE cluster and deploy workloads, you might need to change settings or review the performance of your application. In this section, you learn how to use the Google Cloud console to review the resources that are part of your cluster and the Cymbal Bank sample application.

### Clusters

In this tutorial, you created one GKE cluster and deployed the Cymbal Bank workloads.

  1. In the Google Kubernetes Engine page of the Google Cloud console, go to the **Clusters** page.

[Go to the Clusters page](https://console.cloud.google.com/kubernetes/list)

  2. Click the newly deployed **scalable-apps** cluster. In the cluster details page that opens, you can view basic cluster details along with the cluster's networking and security configurations. You can also see which GKE features are enabled in this cluster in the **Features** section.




### Observability

You can view basic metrics for the health and performance of your cluster. In the next tutorial in this series, you enable Google Cloud Managed Service for Prometheus for more granular monitoring and observability.

  1. Select your cluster from the Google Kubernetes Engine **Clusters** page of the Google Cloud console, then go to the **Observability** tab.

  2. Examine some of the metric graphics for things like _CPU_ and _Memory_. This view lets you monitor the performance of the different parts of your cluster workloads without needing to deploy additional monitoring capabilities.

  3. To view logs streamed from your cluster, select the **Logs** tab. You can filter by _Severity_ of logs, or create your own filters to view specific namespaces, Services, or Pods. Like with Pod warnings and events, this collated view of logs from your cluster can help debug issues quickly using the Google Cloud console.

It's normal to see log entries as Cymbal Bank is first deployed when some services can't communicate yet.

  4. Select the **App Errors** tab. As your workloads run, you can view the collated warnings and events in the Google Cloud console. This approach can help debug issues without having to connect to the cluster, Nodes, or Pods individually.

Again, it's normal to see events logged as Cymbal Bank is first deployed when some Services can't communicate yet.




### Workloads

The GKE page of the Google Cloud console has a **Workloads** section that shows an aggregated view of the workloads that run on all your GKE clusters.

  1. In the Google Kubernetes Engine page of the Google Cloud console, go to the **Workloads** page.

[Go to the Workloads page](https://console.cloud.google.com/kubernetes/workload)

The **Overview** tab shows a list of workloads and namespaces from the GKE cluster. You can filter by namespaces to see what workloads run in each namespace.




### Services & Ingress

The **Services & Ingress** view shows the project's Service and Ingress resources. A Service exposes a set of Pods as a network service with an endpoint, while an Ingress manages external access to the services in a cluster.

  1. In the Google Kubernetes Engine page of the Google Cloud console, go to the **Gateways, Services & Ingress** page.

[Go to the Gateways, Services & Ingress page](https://console.cloud.google.com/kubernetes/gateways)

  2. To find the Cymbal Bank ingress, click the tab for **Ingress** and find the ingress with the name `frontend`. An ingress manages inbound traffic for your application. You can view information on the load balancer, ports, and external endpoints.

  3. Click the _IP address_ for the `frontend` ingress, such as `198.51.100.143:80`. This address opens to the Cymbal Bank web interface.




## Clean up

The set of tutorials for Cymbal Bank is designed to be completed one after the other. As your progress through the set of tutorials, you learn new skills and use additional Google Cloud products and services.

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

Learn how to [monitor your workloads in GKE using Google Cloud Managed Service for Prometheus and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-monitor) in the next tutorial.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
