---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine/
title: Connect from Google Kubernetes Engine \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:08.087437+00:00
---

# Connect from Google Kubernetes Engine  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Connect from Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-kubernetes-engine "View this page for the SQL Server database engine")

This page describes how to set up a connection from an application running in Google Kubernetes Engine (GKE) to a Cloud SQL instance.

**For step-by-step instructions on running a Google Kubernetes Engine sample web application connected to Cloud SQL,** see the [quickstart for connecting from Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-kubernetes).

Cloud SQL is a fully-managed database service that helps you set up, maintain, manage, and administer your relational databases in the cloud.

Google Kubernetes Engine is a simple way to automatically deploy, scale, and manage Kubernetes.

## About connecting Google Kubernetes Engine to Cloud SQL

To access a Cloud SQL instance from an application running in Google Kubernetes Engine, you can use either the Cloud SQL Auth Proxy (with public or private IP), or connect directly using a private IP address.

The Cloud SQL Auth Proxy is the recommended way to connect to Cloud SQL, even when using private IP. This is because the Cloud SQL Auth Proxy provides strong encryption and authentication using IAM, which can help keep your database secure.

Database connections consume resources on the server and the connecting application. Always use good connection management practices to minimize your application's footprint and reduce the likelihood of exceeding Cloud SQL [connection limits](https://docs.cloud.google.com/sql/docs/postgres/quotas#configurable-limits). For more information, see [Managing database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections). 

### Before you begin

To connect to Cloud SQL you must have:

  * A GKE cluster, with the `kubectl` command-line tool installed and configured to communicate with the cluster.

For help getting started with GKE, see [Deploy an app to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).

For connecting using private IP, the GKE cluster must be [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) and peered with the same Virtual Private Cloud (VPC) network as the Cloud SQL instance.

  * An instance created.

For help creating a Cloud SQL instance, see [Creating Instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

  * A PostgreSQL user account configured on the instance.

Your application will use this account to connect to the database. For help with creating a user account, see [Creating a user](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating).


**Note:** Some of the kubectl commands will use a default namespace unless you use a `--namespace` flag. For more information, see the [Kubernetes documentation on Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### About Kubernetes Secrets

In Kubernetes, [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) are a secure way to pass configuration details to your application. You can create a Secret with details such as your database name, user, and password which can be injected into your application as env vars.

There are many different ways Secrets can be used, depending on the connection type:

  * A database credentials Secret includes the name of the database user you are connecting as, and the user's database password.
  * If connecting with the Cloud SQL Auth Proxy, a Secret can be used to hold your service account's credential file.
  * If connecting with private IP, a Secret can be used to specify the private IP address of your Cloud SQL instance.



For complete examples of how to use Secrets, see the GitHub repositories referenced later on this page.

#### Create a Secret object

  1. You create the Secret objects by using the [`kubectl create secret` command](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/#create-a-secret).

To create a database credentials Secret:
         
         kubectl create secret generic <YOUR-DB-SECRET> \
           --from-literal=username=<YOUR-DATABASE-USER> \
           --from-literal=password=<YOUR-DATABASE-PASSWORD> \
           --from-literal=database=<YOUR-DATABASE-NAME>
         

  2. Once created, you can view the objects in the **Configuration** section of the Google Kubernetes Engine page in the [Google Cloud console](https://console.cloud.google.com/kubernetes).




## Connect to Cloud SQL using the Cloud SQL Auth Proxy

When you connect using the Cloud SQL Auth Proxy, the Cloud SQL Auth Proxy is added to your pod using the `sidecar` container pattern. The Cloud SQL Auth Proxy container is in the same pod as your application, which enables the application to connect to the Cloud SQL Auth Proxy using `localhost`, increasing security and performance.

For more information about the Cloud SQL Auth Proxy, see [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy). For more information about working with pods, see [Pod Overview](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview) in the Kubernetes documentation.

For connecting using the Cloud SQL Auth Proxy you need the following:

  1. The instance connection name of your Cloud SQL instance.

The instance connection name is available in the **Cloud SQL Instance details** page of the Google Cloud console or from the `gcloud sql instances describe INSTANCE_ID` command.

  2. The location of the key file associated with a service account with the proper privileges for your Cloud SQL instance.

See [Creating a service account](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#create-service-account) for more information.

  3. The Cloud SQL Admin API is enabled.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)




### Provide the service account to the Cloud SQL Auth Proxy

The first step to running the Cloud SQL Auth Proxy in Google Kubernetes Engine is creating a Google Service Account (GSA) to represent your application. It is recommended that you create a service account unique to each application, instead of using the same service account everywhere. This model is more secure since it allows you to limit permissions on a per-application basis.

The service account for your application needs to meet the following criteria:

  * Belong to a project with the Cloud SQL Admin API enabled
  * Has been granted the Cloud SQL Client IAM role (or equivalent) for the project containing the instance you want to connect to
  * If connecting using private IP, you must use a VPC-native GKE cluster, in the same VPC as your Cloud SQL instance



You need to configure GKE to provide the service account to the Cloud SQL Auth Proxy. There are two recommended ways to do this:  workload identity or a service account key file.

#### Workload Identity

If you are using [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine), the preferred method is to use GKE's [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) feature. This method allows you to bind a [Kubernetes Service Account (KSA)](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) to a Google Service Account (GSA). The GSA will then be accessible to applications using the matching KSA.

A Google Service Account (GSA) is an IAM identity that represents your application in Google Cloud. In a similar fashion, a Kubernetes Service Account (KSA) is a an identity that represents your application in a Google Kubernetes Engine cluster.

Workload Identity binds a KSA to a GSA, causing any deployments with that KSA to authenticate as the GSA in their interactions with Google Cloud.

  1. [Enable Workload Identity for your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_cluster)
  2. Typically, each application has its own identity, represented by a KSA and GSA pair. Create a KSA for your application by running `kubectl apply -f service-account.yaml`:
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: <YOUR-KSA-NAME> # TODO(developer): replace these values

  3. Enable the IAM binding between your YOUR-GSA-NAME and YOUR-KSA-NAME:
         
         gcloud iam service-accounts add-iam-policy-binding \
         --role="roles/iam.workloadIdentityUser" \
         --member="serviceAccount:YOUR-GOOGLE-CLOUD-PROJECT.svc.id.goog[YOUR-K8S-NAMESPACE/YOUR-KSA-NAME]" \
         YOUR-GSA-NAME@YOUR-GOOGLE-CLOUD-PROJECT.iam.gserviceaccount.com

  4. Add an annotation to YOUR-KSA-NAME to complete the binding:
         
         kubectl annotate serviceaccount \
         YOUR-KSA-NAME \
         iam.gke.io/gcp-service-account=YOUR-GSA-NAME@YOUR-GOOGLE-CLOUD-PROJECT.iam.gserviceaccount.com

  5. Finally, make sure to specify the service account for the k8s object.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: <YOUR-DEPLOYMENT-NAME>
         spec:
           selector:
             matchLabels:
               app: <YOUR-APPLICATION-NAME>
           template:
             metadata:
               labels:
                 app: <YOUR-APPLICATION-NAME>
             spec:
               serviceAccountName: <YOUR-KSA-NAME>




#### Service account key file

Alternatively, if you can't use Workload Identity, the recommended pattern is to mount a service account key file into the Cloud SQL Auth Proxy pod and use the `--credentials-file` flag.

  1. Create a credential file for your service account key:
         
         gcloud iam service-accounts keys create ~/key.json \
         --iam-account=YOUR-SA-NAME@project-id.iam.gserviceaccount.com

  2. Turn your service account key into a k8s [Secret](https://kubernetes.io/docs/concepts/configuration/secret/):
         
         kubectl create secret generic YOUR-SA-SECRET \
         --from-file=service_account.json=~/key.json

  3. Mount the secret as a volume under the `spec:` for your k8s object:
         
         volumes:
           - name: <YOUR-SA-SECRET-VOLUME>
             secret:
               secretName: <YOUR-SA-SECRET>

  4. Follow the instructions in the next section to access the volume from the Cloud SQL Auth Proxy's pod.




### Run the Cloud SQL Auth Proxy in a sidecar pattern

We recommend running the Cloud SQL Auth Proxy in a `sidecar` pattern (as an additional container sharing a pod with your application). We recommend this over running as a separate service for several reasons:

  * Prevents your SQL traffic from being exposed locally; the Cloud SQL Auth Proxy provides encryption on outgoing connections, but you need to limit exposure for incoming connections.
  * Prevents a single point of failure; each application's access to your database is independent from the others, making it more resilient.
  * Limits access to the Cloud SQL Auth Proxy, allowing you to use IAM permissions for each application rather than exposing the database to the entire cluster.
  * Lets you scope resource requests more accurately; because the Cloud SQL Auth Proxy consumes resources linearly to usage, this pattern lets you scope and request resources to match your applications as the application scales.

  * Add the Cloud SQL Auth Proxy to the pod configuration under `initContainers`, unless you're using Cloud Service Mesh or Istio.

If you're using Cloud Service Mesh or Istio, then add the Cloud SQL Auth Proxy under the `containers` section instead.

### `initContainers`
        
        initContainers:
          - name: cloud-sql-proxy
            restartPolicy: Always
            # It is recommended to use the latest version of the Cloud SQL Auth Proxy
            # Make sure to update on a regular schedule!
            image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.14.1
            args:
              # If connecting from a VPC-native GKE cluster, you can use the
              # following flag to have the proxy connect over private IP
              # - "--private-ip"
        
              # If you are not connecting with Automatic IAM, you can delete
              # the following flag.
              - "--auto-iam-authn"
        
              # Enable structured logging with LogEntry format:
              - "--structured-logs"
        
              # Replace DB_PORT with the port the proxy should listen on
              - "--port=<DB_PORT>"
              - "<INSTANCE_CONNECTION_NAME>"
        
            securityContext:
              # The default Cloud SQL Auth Proxy image runs as the
              # "nonroot" user and group (uid: 65532) by default.
              runAsNonRoot: true
            # You should use resource requests/limits as a best practice to prevent
            # pods from consuming too many resources and affecting the execution of
            # other pods. You should adjust the following values based on what your
            # application needs. For details, see
            # https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
            resources:
              requests:
                # The proxy's memory use scales linearly with the number of active
                # connections. Fewer open connections will use less memory. Adjust
                # this value based on your application's requirements.
                memory: "2Gi"
                # The proxy's CPU use scales linearly with the amount of IO between
                # the database and the application. Adjust this value based on your
                # application's requirements.
                cpu: "1"

### `containers`
        
        - name: cloud-sql-proxy
          # It is recommended to use the latest version of the Cloud SQL Auth Proxy
          # Make sure to update on a regular schedule!
          image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.14.1
          args:
            # If connecting from a VPC-native GKE cluster, you can use the
            # following flag to have the proxy connect over private IP
            # - "--private-ip"
        
            # If you are not connecting with Automatic IAM, you can delete
            # the following flag.
            - "--auto-iam-authn"
        
            # Enable structured logging with LogEntry format:
            - "--structured-logs"
        
            # Replace DB_PORT with the port the proxy should listen on
            - "--port=<DB_PORT>"
            - "<INSTANCE_CONNECTION_NAME>"
        
          securityContext:
            # The default Cloud SQL Auth Proxy image runs as the
            # "nonroot" user and group (uid: 65532) by default.
            runAsNonRoot: true
          # You should use resource requests/limits as a best practice to prevent
          # pods from consuming too many resources and affecting the execution of
          # other pods. You should adjust the following values based on what your
          # application needs. For details, see
          # https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
          resources:
            requests:
              # The proxy's memory use scales linearly with the number of active
              # connections. Fewer open connections will use less memory. Adjust
              # this value based on your application's requirements.
              memory: "2Gi"
              # The proxy's CPU use scales linearly with the amount of IO between
              # the database and the application. Adjust this value based on your
              # application's requirements.
              cpu: "1"

  * If you're using a service account key, then specify your secret volume and add the `--credentials-file` flag to the command:
        
        # This flag specifies where the service account key can be found
          - "--credentials-file=/secrets/service_account.json"
        securityContext:
          # The default Cloud SQL Auth Proxy image runs as the
          # "nonroot" user and group (uid: 65532) by default.
          runAsNonRoot: true
        volumeMounts:
          - name: <YOUR-SA-SECRET-VOLUME>
            mountPath: /secrets/
            readOnly: true



  * If you're using [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins#using_with_the), then [add IAM policy bindings to the service account](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-policy-binding). Grant the Cloud SQL Instance User (`roles/cloudsql.instanceUser`) and the Cloud SQL Client (`roles/cloudsql.client`) roles to the service account used by the Cloud SQL Auth Proxy.

  * To log in to the instance with IAM database authentication automatically, start the Cloud SQL Auth Proxy with the `--auto-iam-authn` flag.



  * Finally, configure your application to connect using `127.0.0.1` on whichever DB_PORT you specified in the command section.



Complete sample configuration files:

### Workload identity
    
    
    # Copyright 2021 Google LLC
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
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: <YOUR-DEPLOYMENT-NAME>
    spec:
      selector:
        matchLabels:
          app: <YOUR-APPLICATION-NAME>
      template:
        metadata:
          labels:
            app: <YOUR-APPLICATION-NAME>
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
            - name: <YOUR-APPLICATION-NAME>
              # ... other container configuration
              env:
                - name: DB_USER
                  valueFrom:
                    secretKeyRef:
                      name: <YOUR-DB-SECRET>
                      key: username
                - name: DB_PASS
                  valueFrom:
                    secretKeyRef:
                      name: <YOUR-DB-SECRET>
                      key: password
                - name: DB_NAME
                  valueFrom:
                    secretKeyRef:
                      name: <YOUR-DB-SECRET>
                      key: database
          initContainers:
            - name: cloud-sql-proxy
              restartPolicy: Always
              # It is recommended to use the latest version of the Cloud SQL Auth Proxy
              # Make sure to update on a regular schedule!
              image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.14.1
              args:
                # If connecting from a VPC-native GKE cluster, you can use the
                # following flag to have the proxy connect over private IP
                # - "--private-ip"
    
                # If you are not connecting with Automatic IAM, you can delete
                # the following flag.
                - "--auto-iam-authn"
    
                # Enable structured logging with LogEntry format:
                - "--structured-logs"
    
                # Replace DB_PORT with the port the proxy should listen on
                - "--port=<DB_PORT>"
                - "<INSTANCE_CONNECTION_NAME>"
    
              securityContext:
                # The default Cloud SQL Auth Proxy image runs as the
                # "nonroot" user and group (uid: 65532) by default.
                runAsNonRoot: true
              # You should use resource requests/limits as a best practice to prevent
              # pods from consuming too many resources and affecting the execution of
              # other pods. You should adjust the following values based on what your
              # application needs. For details, see
              # https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
              resources:
                requests:
                  # The proxy's memory use scales linearly with the number of active
                  # connections. Fewer open connections will use less memory. Adjust
                  # this value based on your application's requirements.
                  memory: "2Gi"
                  # The proxy's CPU use scales linearly with the amount of IO between
                  # the database and the application. Adjust this value based on your
                  # application's requirements.
                  cpu: "1"
    

### Service account key
    
    
    # Copyright 2021 Google LLC
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
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: <YOUR-DEPLOYMENT-NAME>
    spec:
      selector:
        matchLabels:
          app: <YOUR-APPLICATION-NAME>
      template:
        metadata:
          labels:
            app: <YOUR-APPLICATION-NAME>
        spec:
          containers:
            - name: <YOUR-APPLICATION-NAME>
              # ... other container configuration
              env:
                - name: DB_USER
                  valueFrom:
                    secretKeyRef:
                      name: <YOUR-DB-SECRET>
                      key: username
                - name: DB_PASS
                  valueFrom:
                    secretKeyRef:
                      name: <YOUR-DB-SECRET>
                      key: password
                - name: DB_NAME
                  valueFrom:
                    secretKeyRef:
                      name: <YOUR-DB-SECRET>
                      key: database
          initContainers:
            - name: cloud-sql-proxy
              restartPolicy: Always
              # It is recommended to use the latest version of the Cloud SQL Auth Proxy
              # Make sure to update on a regular schedule!
              image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.14.1
              args:
                # If connecting from a VPC-native GKE cluster, you can use the
                # following flag to have the proxy connect over private IP
                # - "--private-ip"
    
                # If you are not connecting with Automatic IAM AuthN, you can delete
                # the following flag.
                - "--auto-iam-authn"
    
                # Enable structured logging with LogEntry format:
                - "--structured-logs"
    
                # Replace DB_PORT with the port the proxy should listen on
                - "--port=<DB_PORT>"
                - "<INSTANCE_CONNECTION_NAME>"
    
                # This flag specifies where the service account key can be found
                - "--credentials-file=/secrets/service_account.json"
              securityContext:
                # The default Cloud SQL Auth Proxy image runs as the
                # "nonroot" user and group (uid: 65532) by default.
                runAsNonRoot: true
              volumeMounts:
                - name: <YOUR-SA-SECRET-VOLUME>
                  mountPath: /secrets/
                  readOnly: true
              # Resource configuration depends on an application's requirements. You
              # should adjust the following values based on what your application
              # needs. For details, see https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
              resources:
                requests:
                  # The proxy's memory use scales linearly with the number of active
                  # connections. Fewer open connections will use less memory. Adjust
                  # this value based on your application's requirements.
                  memory: "2Gi"
                  # The proxy's CPU use scales linearly with the amount of IO between
                  # the database and the application. Adjust this value based on your
                  # application's requirements.
                  cpu: "1"
          volumes:
            - name: <YOUR-SA-SECRET-VOLUME>
              secret:
                secretName: <YOUR-SA-SECRET>
    

## Connect to Cloud SQL without the Cloud SQL Auth Proxy

While not as secure, it is possible to connect from a [VPC-native GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) to a Cloud SQL instance on the same VPC using private IP without the Cloud SQL Auth Proxy.

  1. Create a secret with your instance's private IP address:
         
         kubectl create secret generic <YOUR-PRIVATE-IP-SECRET> \
             --from-literal=db_host=<YOUR-PRIVATE-IP-ADDRESS>
         

  2. Next make sure you add the secret to your application's container:
         
         - name: DB_HOST
           valueFrom:
             secretKeyRef:
               name: <YOUR-PRIVATE-IP-SECRET>
               key: db_host

  3. Finally, configure your application to connect using the IP address from the `DB_HOST` env var. You will need to use the correct port for PostgreSQL: 5432




Complete sample configuration file:

### Private IP
    
    
    # Copyright 2021 Google LLC
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
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: <YOUR-DEPLOYMENT-NAME>
    spec:
      selector:
        matchLabels:
          app: <YOUR-APPLICATION-NAME>
      template:
        metadata:
          labels:
            app: <YOUR-APPLICATION-NAME>
        spec:
          containers:
          - name: <YOUR-APPLICATION-NAME>
            # ... other container configuration
            env:
            - name: DB_USER
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: username
            - name: DB_PASS
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: password
            - name: DB_NAME
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: database
            - name: DB_HOST
              valueFrom:
                secretKeyRef:
                  name: <YOUR-PRIVATE-IP-SECRET>
                  key: db_host
    

## Troubleshooting

Need help? For help troubleshooting the proxy, see [Troubleshooting Cloud SQL Auth Proxy connections](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#troubleshooting), or see our [Cloud SQL Support](https://docs.cloud.google.com/sql/docs/postgres/getting-support) page. 

## What's next

  * Learn more about [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip).

  * Learn more about the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) and the [proxy docker image](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#connecting-docker).

  * Get help [troubleshooting Cloud SQL Auth Proxy connections](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#troubleshooting).

  * Learn more about [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs).

  * Learn about [options for support](https://docs.cloud.google.com/sql/docs/postgres/support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
