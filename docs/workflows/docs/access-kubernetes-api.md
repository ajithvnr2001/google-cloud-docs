---
url: https://docs.cloud.google.com/workflows/docs/access-kubernetes-api/
title: Access Kubernetes API objects using a connector \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:45.457266+00:00
---

# Access Kubernetes API objects using a connector  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/access-kubernetes-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Access Kubernetes API objects using a connector Stay organized with collections  Save and categorize content based on your preferences. 

A Google Kubernetes Engine (GKE) cluster consists of a _control plane_ and worker machines called _nodes_. You can run your containerized Kubernetes workloads in a GKE cluster. Nodes are the worker machines that run your containerized applications and other workloads, and the control plane is the unified endpoint for your cluster. For more information, see [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).

The Kubernetes API server runs on the control plane, allowing you to interact with Kubernetes _objects_ in the cluster through Kubernetes API calls. Objects are persistent entities in the Kubernetes system and represent the state of your cluster. For more information, in the Kubernetes documentation, see [Objects in Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/), and the [API Overview](https://kubernetes.io/docs/reference/using-api/) which links to the "Kubernetes API reference" pages.

This document shows you how to use the Kubernetes API connector in a workflow to make requests to the Kubernetes service endpoint hosted on a GKE cluster's control plane. For example, you can use the connector to create Kubernetes Deployments, run Jobs, manage Pods, or access deployed apps through a proxy. For more information, see the [Kubernetes API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/Overview).

**Note:** The Kubernetes API is distinct from the Kubernetes Engine API, which is used to create and manage GKE clusters. To call the GKE API in a workflow, use the [Kubernetes Engine API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/Overview).

## Before you begin

Before you proceed with the tasks in this document, make sure that you have completed certain prerequisites.

### Enable APIs

Before you can access Kubernetes API objects using the Kubernetes API connector, you must enable the following APIs:

  * **Kubernetes Engine API** : to build and manage container-based applications using GKE
  * **Workflows APIs** : to manage workflow definitions and executions; enabling the Workflows API automatically enables the Workflow Executions API




###  Console 

Enable the APIs:

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,workflows.googleapis.com)

###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Enable the APIs:
         
         gcloud services enable container.googleapis.com workflows.googleapis.com




### Create a service account

Create a user-managed [service account](https://docs.cloud.google.com/workflows/docs/authentication) that acts as the identity of your workflow, and grant it the [Kubernetes Engine Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`) role so that the workflow can access Kubernetes API objects inside clusters.

**Note:** The Identity and Access Management (IAM) role affects which resources your service account can access in your project. You can revoke this role or grant additional roles later. In production environments, don't grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs.

###  Console 

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts)

  2. Select a project and then click **Create service account**.

  3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

In the **Service account description** field, enter a description. For example, `Service account for Kubernetes API`.

  4. Click **Create and continue**.

  5. In the **Select a role** list, filter for, and select the **Kubernetes Engine Developer** role.

  6. Click **Continue**.

  7. To finish creating the account, click **Done**.




###  gcloud 

  1. Create the service account:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account.

  2. Grant the `container.developer` role to your service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/container.developer

Replace `PROJECT_ID` with your Google Cloud project ID.




Note that you can use both IAM _and_ Kubernetes role-based access control (RBAC) to control access to your GKE cluster:

  * IAM is not specific to Kubernetes; it provides identity management for multiple Google Cloud products, and operates primarily at the level of the Google Cloud project.

  * Kubernetes RBAC is a core component of Kubernetes and lets you create and grant roles (sets of permissions) for any object or type of object within the cluster. If you primarily use GKE, and need fine-grained permissions for every object and operation within your cluster, Kubernetes RBAC is the best choice.




For more information, see [Access control](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control).

### Create a GKE cluster

To use the Kubernetes API connector, you must have already created a public or private GKE cluster. In a private cluster, nodes only have internal IP addresses, which means that nodes and Pods are isolated from the internet by default. For more information, see [Private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept).

You can also specify the _mode of operation_ which offers you different levels of flexibility, responsibility, and control. For example, you can create an Autopilot cluster which is a mode of operation in GKE in which Google manages your cluster configuration, including your nodes, scaling, security, and other preconfigured settings. For more information, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

If you have not yet created a GKE cluster, you can [deploy a web server containerized application](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster) to a GKE cluster. Or, to try out the instructions in this document, you can create an Autopilot cluster by completing the following.

### Console

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. If you are asked to select a cluster mode, select **Autopilot**.

  4. In the **Cluster basics** section, complete the following:

     1. Enter the **Name** for your cluster, such as `hello-cluster`.
     2. Select a [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`.
  5. Click **Next: Networking**.

  6. In the **IPv4 network access** section, to create a cluster with a publicly accessible endpoint, choose **Public cluster**.

  7. For all the other settings, accept the defaults.

  8. Click **Create**.




It might take several minutes for the creation of the cluster to complete. Once the cluster is created, a checkmark check_circle indicates that it is running.

### gcloud

Run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID

Replace the following:

  * `CLUSTER_NAME`: the name of your GKE cluster, such as `hello-cluster`
  * `LOCATION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`
  * `PROJECT_ID`: your Google Cloud project ID



It might take several minutes for the creation of the cluster to complete. Once the cluster is created, the output should be similar to the following:
    
    
    Creating cluster hello-cluster...done.
    Created [https://container.googleapis.com/v1/projects/MY_PROJECT/zones/us-central1/clusters/hello-cluster].
    [...]
    STATUS: RUNNING
    

## Use the connector to send an HTTP request

You can use the Kubernetes API connector to send an HTTP request to a GKE cluster's control plane. For example, the following workflow creates a Deployment named `nginx-deployment` in the specified Kubernetes cluster. The Deployment describes a required state; in this case, to run three Pods with the `nginx:1.14.2` image and expose their service on port 80. (If not specified, the `project` and `location` default to that of the workflow.)

For more information, see the reference page for the Kubernetes API connector function, [gke.request](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/request).

Note the following:

  * The `path` field corresponds to the Kubernetes API method path. For more information, in the Kubernetes documentation, see the [API Overview](https://kubernetes.io/docs/reference/using-api/) which links to the "Kubernetes API reference" pages.
  * You can [catch and handle HTTP request errors](https://docs.cloud.google.com/workflows/docs/http-requests#http-errors) in your workflow. For more information, see [Workflow errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types).



### Deploy your workflow

Before executing a workflow, you must create and deploy it.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter a name for the new workflow, such as `kubernetes-api-request`.

  4. In the **Region** list, select **us-central1**.

  5. Select the **Service account** you previously created.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:

### YAML
         
         main:
           steps:
             - create_deployment:
                 call: gke.request
                 args:
                   cluster_id: "CLUSTER_NAME"
                   project: "PROJECT_ID"
                   location: "LOCATION"
                   method: "POST"
                   path: "/apis/apps/v1/namespaces/default/deployments"
                   body:
                     kind: Deployment
                     metadata:
                       name: nginx-deployment
                       labels:
                         app: nginx
                     spec:
                       replicas: 3
                       selector:
                         matchLabels:
                           app: nginx
                       template:
                         metadata:
                           labels:
                             app: nginx
                         spec:
                           containers:
                             - name: nginx
                               image: nginx:1.14.2
                               ports:
                                 - containerPort: 80
                 result: result
             - returnResult:
                 return: '${result}'

### JSON
         
         {
           "main": {
             "steps": [
               {
                 "create_deployment": {
                   "call": "gke.request",
                   "args": {
                     "cluster_id": "CLUSTER_NAME",
                     "project": "PROJECT_ID",
                     "location": "LOCATION",
                     "method": "POST",
                     "path": "/apis/apps/v1/namespaces/default/deployments",
                     "body": {
                       "kind": "Deployment",
                       "metadata": {
                         "name": "nginx-deployment",
                         "labels": {
                           "app": "nginx"
                         }
                       },
                       "spec": {
                         "replicas": 3,
                         "selector": {
                           "matchLabels": {
                             "app": "nginx"
                           }
                         },
                         "template": {
                           "metadata": {
                             "labels": {
                               "app": "nginx"
                             }
                           },
                           "spec": {
                             "containers": [
                               {
                                 "name": "nginx",
                                 "image": "nginx:1.14.2",
                                 "ports": [
                                   {
                                     "containerPort": 80
                                   }
                                 ]
                               }
                             ]
                           }
                         }
                       }
                     }
                   },
                   "result": "result"
                 }
               },
               {
                 "returnResult": {
                   "return": "${result}"
                 }
               }
             ]
           }
         }
         

Replace the following:

     * `CLUSTER_NAME`: the name of your GKE cluster, such as `hello-cluster`
     * `PROJECT_ID`: your Google Cloud project ID
     * `LOCATION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`
  8. Click **Deploy**.




### gcloud

  1. Create a source code file for your workflow:
         
         touch kubernetes-api-request.JSON_OR_YAML

Replace `JSON_OR_YAML` with `yaml` or `json` depending on the format of your workflow.

  2. In a text editor, copy the following workflow to your source code file:

### YAML
         
         main:
           steps:
             - create_deployment:
                 call: gke.request
                 args:
                   cluster_id: "CLUSTER_NAME"
                   project: "PROJECT_ID"
                   location: "LOCATION"
                   method: "POST"
                   path: "/apis/apps/v1/namespaces/default/deployments"
                   body:
                     kind: Deployment
                     metadata:
                       name: nginx-deployment
                       labels:
                         app: nginx
                     spec:
                       replicas: 3
                       selector:
                         matchLabels:
                           app: nginx
                       template:
                         metadata:
                           labels:
                             app: nginx
                         spec:
                           containers:
                             - name: nginx
                               image: nginx:1.14.2
                               ports:
                                 - containerPort: 80
                 result: result
             - returnResult:
                 return: '${result}'

### JSON
         
         {
           "main": {
             "steps": [
               {
                 "create_deployment": {
                   "call": "gke.request",
                   "args": {
                     "cluster_id": "CLUSTER_NAME",
                     "project": "PROJECT_ID",
                     "location": "LOCATION",
                     "method": "POST",
                     "path": "/apis/apps/v1/namespaces/default/deployments",
                     "body": {
                       "kind": "Deployment",
                       "metadata": {
                         "name": "nginx-deployment",
                         "labels": {
                           "app": "nginx"
                         }
                       },
                       "spec": {
                         "replicas": 3,
                         "selector": {
                           "matchLabels": {
                             "app": "nginx"
                           }
                         },
                         "template": {
                           "metadata": {
                             "labels": {
                               "app": "nginx"
                             }
                           },
                           "spec": {
                             "containers": [
                               {
                                 "name": "nginx",
                                 "image": "nginx:1.14.2",
                                 "ports": [
                                   {
                                     "containerPort": 80
                                   }
                                 ]
                               }
                             ]
                           }
                         }
                       }
                     }
                   },
                   "result": "result"
                 }
               },
               {
                 "returnResult": {
                   "return": "${result}"
                 }
               }
             ]
           }
         }
         

Replace the following:

     * `CLUSTER_NAME`: the name of your GKE cluster, such as `hello-cluster`
     * `LOCATION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`
  3. Deploy the workflow:
         
         gcloud workflows deploy kubernetes-api-request \
             --source=kubernetes-api-request.JSON_OR_YAML \
             --location=LOCATION \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com




### Execute your workflow

After successfully deploying your workflow, you can execute it. Executing a workflow runs the current workflow definition associated with the workflow.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, select your workflow to go to its details page.

  3. On the **Workflow details** page, click _play_arrow_ **Execute**.

  4. Click **Execute** again.

  5. View the results of the workflow in the **Output** pane.

If successful, the execution state should be `Succeeded` and the body of the response is returned.




### gcloud

Execute the workflow:
    
    
    gcloud workflows run kubernetes-api-request \
        --location=LOCATION

If successful, the state should be `SUCCEEDED` and the body of the response is returned.

## Use the connector to run a Kubernetes Job

You can use the Kubernetes API connector to deploy and run a Kubernetes Job in a GKE cluster. The following workflow creates a Kubernetes Job that runs a Bash script that iterates through a sequence of numbers. The workflow waits for up to 90 seconds for the Kubernetes Job to complete; otherwise, an error is raised. If the Job completes, it is then deleted.

Note that a Job is considered complete if its status includes a condition type of `Complete`. For example:
    
    
      "status": {
        "conditions": [
          {
            "type": "Complete",
            "status": "True"
          }
        ]
      }

If the Job fails, a `FailedJobError` tag is returned. For example: 
    
    
    {
      "tags": ["FailedJobError"]
      "job": {...}
      "message":"Kubernetes job failed"
    }

For more information, see the reference pages for the following Kubernetes API connector functions:

  * [gke.create_job](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/create_job)
  * [gke.await_job](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/await_job)
  * [gke.delete_job](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/delete_job)



### Deploy your workflow

Before executing a workflow, you must create and deploy it.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter a name for the new workflow, such as `kubernetes-api-job`.

  4. In the **Region** list, select **us-central1**.

  5. Select the **Service account** you previously created.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:

### YAML
         
         main:
           steps:
             - init:
                 assign:
                   - project: "PROJECT_ID"
                   - location: "LOCATION"
                   - cluster_id: "CLUSTER_NAME"
                   - job_name: "JOB_NAME"
                   - namespace: "default"
             - create_job:
                 call: gke.create_job
                 args:
                   cluster_id: '${cluster_id}'
                   location: '${location}'
                   project: '${project}'
                   namespace: '${namespace}'
                   job:
                     apiVersion: batch/v1
                     kind: Job
                     metadata:
                       name: "${job_name}"
                     spec:
                       template:
                         spec:
                           containers:
                             - name: counter
                               image: centos:7
                               command:
                                 - "bin/bash"
                                 - "-c"
                                 - "for i in 9 8 7 6 5 4 3 2 1 ; do echo $i ; done"
                           restartPolicy: Never
                 result: job
             - wait_for_job:  # if job fails, raise error with "FailedJobError" tag and "job" field
                 call: gke.await_job
                 args:
                   cluster_id: '${cluster_id}'
                   job_name: '${job_name}'
                   location: '${location}'
                   project: '${project}'
                   timeout: 90  # 90 seconds
                 result: completed_job
             - cleanup_job:
                 call: gke.delete_job
                 args:
                   cluster_id: '${cluster_id}'
                   job_name: '${job_name}'
                   location: '${location}'
                   project: '${project}'
                   query:
                     propagationPolicy: "Foreground"  # delete child Pods
             - return_job:
                 return: '${completed_job}'

### JSON
         
         {
           "main": {
             "steps": [
               {
                 "init": {
                   "assign": [
                     {
                       "project": "PROJECT_ID"
                     },
                     {
                       "location": "LOCATION"
                     },
                     {
                       "cluster_id": "CLUSTER_NAME"
                     },
                     {
                       "job_name": "JOB_NAME"
                     },
                     {
                       "namespace": "default"
                     }
                   ]
                 }
               },
               {
                 "create_job": {
                   "call": "gke.create_job",
                   "args": {
                     "cluster_id": "${cluster_id}",
                     "location": "${location}",
                     "project": "${project}",
                     "namespace": "${namespace}",
                     "job": {
                       "apiVersion": "batch/v1",
                       "kind": "Job",
                       "metadata": {
                         "name": "${job_name}"
                       },
                       "spec": {
                         "template": {
                           "spec": {
                             "containers": [
                               {
                                 "name": "counter",
                                 "image": "centos:7",
                                 "command": [
                                   "bin/bash",
                                   "-c",
                                   "for i in 9 8 7 6 5 4 3 2 1 ; do echo $i ; done"
                                 ]
                               }
                             ],
                             "restartPolicy": "Never"
                           }
                         }
                       }
                     }
                   },
                   "result": "job"
                 }
               },
               {
                 "wait_for_job": {
                   "call": "gke.await_job",
                   "args": {
                     "cluster_id": "${cluster_id}",
                     "job_name": "${job_name}",
                     "location": "${location}",
                     "project": "${project}",
                     "timeout": 90
                   },
                   "result": "completed_job"
                 }
               },
               {
                 "cleanup_job": {
                   "call": "gke.delete_job",
                   "args": {
                     "cluster_id": "${cluster_id}",
                     "job_name": "${job_name}",
                     "location": "${location}",
                     "project": "${project}",
                     "query": {
                       "propagationPolicy": "Foreground"
                     }
                   }
                 }
               },
               {
                 "return_job": {
                   "return": "${completed_job}"
                 }
               }
             ]
           }
         }
         

Replace the following:

     * `LOCATION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`
     * `CLUSTER_NAME`: the name of your GKE cluster, such as `hello-cluster`
     * `JOB_NAME`: the name of the Kubernetes Job, such as `hello-job`
  8. Click **Deploy**.




### gcloud

  1. Create a source code file for your workflow:
         
         touch kubernetes-api-job.JSON_OR_YAML

Replace `JSON_OR_YAML` with `yaml` or `json` depending on the format of your workflow.

  2. In a text editor, copy the following workflow to your source code file:

### YAML
         
         main:
           steps:
             - init:
                 assign:
                   - project: "PROJECT_ID"
                   - location: "LOCATION"
                   - cluster_id: "CLUSTER_NAME"
                   - job_name: "JOB_NAME"
                   - namespace: "default"
             - create_job:
                 call: gke.create_job
                 args:
                   cluster_id: '${cluster_id}'
                   location: '${location}'
                   project: '${project}'
                   namespace: '${namespace}'
                   job:
                     apiVersion: batch/v1
                     kind: Job
                     metadata:
                       name: "${job_name}"
                     spec:
                       template:
                         spec:
                           containers:
                             - name: counter
                               image: centos:7
                               command:
                                 - "bin/bash"
                                 - "-c"
                                 - "for i in 9 8 7 6 5 4 3 2 1 ; do echo $i ; done"
                           restartPolicy: Never
                 result: job
             - wait_for_job:  # if job fails, raise error with "FailedJobError" tag and "job" field
                 call: gke.await_job
                 args:
                   cluster_id: '${cluster_id}'
                   job_name: '${job_name}'
                   location: '${location}'
                   project: '${project}'
                   timeout: 90  # 90 seconds
                 result: completed_job
             - cleanup_job:
                 call: gke.delete_job
                 args:
                   cluster_id: '${cluster_id}'
                   job_name: '${job_name}'
                   location: '${location}'
                   project: '${project}'
                   query:
                     propagationPolicy: "Foreground"  # delete child Pods
             - return_job:
                 return: '${completed_job}'

### JSON
         
         {
           "main": {
             "steps": [
               {
                 "init": {
                   "assign": [
                     {
                       "project": "PROJECT_ID"
                     },
                     {
                       "location": "LOCATION"
                     },
                     {
                       "cluster_id": "CLUSTER_NAME"
                     },
                     {
                       "job_name": "JOB_NAME"
                     },
                     {
                       "namespace": "default"
                     }
                   ]
                 }
               },
               {
                 "create_job": {
                   "call": "gke.create_job",
                   "args": {
                     "cluster_id": "${cluster_id}",
                     "location": "${location}",
                     "project": "${project}",
                     "namespace": "${namespace}",
                     "job": {
                       "apiVersion": "batch/v1",
                       "kind": "Job",
                       "metadata": {
                         "name": "${job_name}"
                       },
                       "spec": {
                         "template": {
                           "spec": {
                             "containers": [
                               {
                                 "name": "counter",
                                 "image": "centos:7",
                                 "command": [
                                   "bin/bash",
                                   "-c",
                                   "for i in 9 8 7 6 5 4 3 2 1 ; do echo $i ; done"
                                 ]
                               }
                             ],
                             "restartPolicy": "Never"
                           }
                         }
                       }
                     }
                   },
                   "result": "job"
                 }
               },
               {
                 "wait_for_job": {
                   "call": "gke.await_job",
                   "args": {
                     "cluster_id": "${cluster_id}",
                     "job_name": "${job_name}",
                     "location": "${location}",
                     "project": "${project}",
                     "timeout": 90
                   },
                   "result": "completed_job"
                 }
               },
               {
                 "cleanup_job": {
                   "call": "gke.delete_job",
                   "args": {
                     "cluster_id": "${cluster_id}",
                     "job_name": "${job_name}",
                     "location": "${location}",
                     "project": "${project}",
                     "query": {
                       "propagationPolicy": "Foreground"
                     }
                   }
                 }
               },
               {
                 "return_job": {
                   "return": "${completed_job}"
                 }
               }
             ]
           }
         }
         

Replace the following:

     * `LOCATION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`
     * `CLUSTER_NAME`: the name of your GKE cluster, such as `hello-cluster`
     * `JOB_NAME`: the name of the Kubernetes Job, such as `hello-job`
  3. Deploy the workflow:
         
         gcloud workflows deploy kubernetes-api-job \
             --source=kubernetes-api-job.JSON_OR_YAML \
             --location=LOCATION \
             --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com




### Execute your workflow

After successfully deploying your workflow, you can execute it. Executing a workflow runs the current workflow definition associated with the workflow.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, select your workflow to go to its details page.

  3. On the **Workflow details** page, click _play_arrow_ **Execute**.

  4. Click **Execute** again.

The workflow execution might take a couple of minutes.

  5. View the results of the workflow in the **Output** pane.

The results should be similar to the following:
         
         {
         ...
           },
           "status": {
             "completionTime": "2023-10-31T17:04:32Z",
             "conditions": [
               {
                 "lastProbeTime": "2023-10-31T17:04:33Z",
                 "lastTransitionTime": "2023-10-31T17:04:33Z",
                 "status": "True",
                 "type": "Complete"
               }
             ],
             "ready": 0,
             "startTime": "2023-10-31T17:04:28Z",
             "succeeded": 1,
             "uncountedTerminatedPods": {}
           }
         }
         




### gcloud

Execute the workflow:
    
    
    gcloud workflows run kubernetes-api-job \
        --location=LOCATION

The workflow execution might take a couple of minutes. The results should be similar to the following:
    
    
    {
    ...
      },
      "status": {
        "completionTime": "2023-10-31T17:04:32Z",
        "conditions": [
          {
            "lastProbeTime": "2023-10-31T17:04:33Z",
            "lastTransitionTime": "2023-10-31T17:04:33Z",
            "status": "True",
            "type": "Complete"
          }
        ],
        "ready": 0,
        "startTime": "2023-10-31T17:04:28Z",
        "succeeded": 1,
        "uncountedTerminatedPods": {}
      }
    }
    

## What's next

  * [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors)
  * [Invoke a Google Cloud service using a connector](https://docs.cloud.google.com/workflows/docs/invoke-connector-to-gcp-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
