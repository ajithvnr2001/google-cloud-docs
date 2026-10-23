---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/batch-ml-workload/
title: Deploy a batch machine learning workload \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:32.734471+00:00
---

# Deploy a batch machine learning workload  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/batch-ml-workload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Deploy a batch machine learning workload Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial demonstrates how to use Google Kubernetes Engine (GKE) to manage fault-tolerant batch workloads while keeping your costs low. Follow this tutorial to learn how to use [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) and cost-optimized [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods), as well as how to configure an in-cluster [Redis](https://redis.io/) job queue on GKE. 

## Background

A batch workload is a process typically designed to have a start and a completion point. You should consider batch workloads on GKE if your architecture involves ingesting, processing, and outputting data instead of using raw data. Areas like machine learning, artificial intelligence, and high performance computing (HPC) feature different kinds of batch workloads, such as offline model training, batched prediction, data analytics, simulation of physical systems, and video processing.

By designing containerized batch workloads, you can leverage the following GKE benefits:

  * An open standard, broad community, and managed service.
  * Cost efficiency from effective workload and infrastructure orchestration and specialized compute resources.
  * Isolation and portability of containerization, allowing the use of cloud as overflow capacity while maintaining data security.
  * Availability of burst capacity, followed by rapid scale down of GKE clusters.



## Objectives

This tutorial is for machine learning engineers or data scientists who want to learn how to run batch machine learning workloads on GKE, on the following cost-efficient and scalable architecture:

This tutorial covers the following steps:

  1. Create a GKE Autopilot cluster. You can alternatively use a GKE Standard cluster for this tutorial.
  2. Create a [Filestore](https://docs.cloud.google.com/filestore) [NFS](https://wikipedia.org/wiki/Network_File_System) volume.
  3. Create an in-cluster Redis job queue.
  4. Transfer datasets to the NFS volume and queue them to be consumed by the workload.
  5. Run a sample batch machine learning workload on the GKE cluster.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)
  * [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Filestore](https://docs.cloud.google.com/filestore/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=kubernetes--gke_batch_ml_workload)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, GKE, and Filestore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,container.googleapis.com,file.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine, GKE, and Filestore APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,container.googleapis.com,file.googleapis.com)

  8. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 




## Prepare the environment

  1. Clone the sample repository used in this tutorial:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         cd kubernetes-engine-samples/batch/aiml-workloads
         

  2. Create a GKE Autopilot cluster:
         
         gcloud container clusters create-auto batch-aiml \
             --location=us-central1
         

This step can take up to 5 minutes to complete.




## Set up dataset storage with a Network File System (NFS)

The machine learning workload requires a storage solution for the datasets and output files. In this section, you create a [Filestore](https://docs.cloud.google.com/filestore/docs) instance and provide access to the instanceby using a [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and a [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).

To learn more, see [how to design an optimal storage strategy](https://docs.cloud.google.com/architecture/storage-advisor) and [how to access Filestore instances from GKE clusters](https://docs.cloud.google.com/filestore/docs/csi-driver).

### Create a Filestore instance

  1. Create a Filestore instance:
         
         gcloud filestore instances create batch-aiml-filestore \
             --zone=us-central1-b \
             --tier=BASIC_HDD \
             --file-share=name="NFSVol",capacity=1TB \
             --network=name="default"
         

This command specifies the following options:

     * `tier`: The service tier for the Filestore instance. This sample uses the basic tier. To learn about the other options, refer to [Service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).

     * `network=name`: The name of the [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#networks) for the Filestore instance. The GKE cluster must be in the same VPC network as the Filestore instance.

     * `capacity`: The desired size of the volume. Specify the storage value in one of the supported units described in [Resource quantities](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/).

**Note:** This step can take up to 5 minutes to complete.
  2. Verify that the Filestore instance has been deployed:
         
         gcloud filestore instances list \
             --project=PROJECT_ID \
             --zone=us-central1-b
         

Replace `PROJECT_ID` with your Google Cloud project ID.

The output is similar to the following:
         
         INSTANCE_NAME: batch-aiml-filestore
         LOCATION: us-central1-b
         TIER: BASIC_HDD
         CAPACITY_GB: 1024
         FILE_SHARE_NAME: NFSVol
         **IP_ADDRESS: 203.0.113.54**
         STATE: READY
         CREATE_TIME: 2022-03-15T18:23:51
         

  3. Note the value in the `IP_ADDRESS` field to use in the following section.




### Create a PersistentVolume

A Kubernetes [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) specification allows the GKE cluster to connect to the Filestore instance.

  1. Update the `kubernetes-manifests/persistent-volume.yaml` file with the Filestore instance IP address:
         
         sed -i "\
           s/<FILESTORE_IP_ADDRESS>/IP_ADDRESS/g" \
           kubernetes-manifests/persistent-volume.yaml
         

Replace `IP_ADDRESS` with the IP address that you noted when [creating the Filestore instance](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/batch-ml-workload#create_a_instance) in the preceding section.

  2. Deploy the PersistentVolume:
         
         kubectl apply -f kubernetes-manifests/persistent-volume.yaml
         




### Create a PersistentVolumeClaim

A Kubernetes [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) allows Kubernetes Pods and Jobs to access the storage resources of a PersistentVolume.

Deploy the PersistentVolumeClaim:
    
    
    kubectl apply -f kubernetes-manifests/persistent-volume-claim.yaml
    

### Consume the PersistentVolumeClaim

With the PersistentVolume and PersistentVolumeClaim set up on the GKE cluster, you can configure the Redis server and the batch jobs to consume the PersistentVolumeClaim. This appears as a mountable storage volume.

Inspect the [`kubernetes-manifests/redis-pod.yaml`](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/batch/aiml-workloads/kubernetes-manifests/redis-pod.yaml) and [`kubernetes-manifests/workload.yaml`](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/batch/aiml-workloads/kubernetes-manifests/workload.yaml) files. The manifest configurations are similar to the following:
    
    
      spec:
      …
      containers:
      - name: workload
        image: "us-central1-docker.pkg.dev/gke-batch-aiml/batch-aiml-docker-repo/workload"
        **volumeMounts :
        - mountPath: /mnt/fileserver
          name: workload-pvc
      volumes:
      - name: workload-pvc
        persistentVolumeClaim:
          claimName: fileserver-claim
          readOnly: false**
    

In this manifest:

  * `spec.volumes` specifies the PersistentVolumeClaim to consume.
  * `spec.containers.volumeMounts` specifies the local file path where the Pod can access the Filestore fileshare.



## Set up a Redis job queue

The workload processes data in batches to iteratively train a fraud detection model. To manage the datasets currently being processed or still in the queue, you deploy the Redis server into the GKE cluster.

For this tutorial, you start a single instance of Redis. To deploy Redis scalably and redundantly, refer to [Create a multi-tier web application with Redis and PHP](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/guestbook).

  1. Deploy the Redis server specification.
         
         kubectl apply -f kubernetes-manifests/redis-pod.yaml
         

  2. Verify that the Pod is running:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME           READY   STATUS    RESTARTS   AGE
         redis-leader   1/1     Running   0          118s
         

The Pod might take up to two minutes to start running.

  3. Transfer the files containing the training and testing datasets to the NFS volume.
         
         sh scripts/transfer-datasets.sh
         

This script copies the files from the sample code repository to the `/mnt/fileserver/datasets/` directory on the `redis-leader` Pod.

  4. Populate the Redis queue.
         
         sh scripts/queue-jobs.sh
         

This script pushes the file paths for the training datasets to a list named `datasets` in the Redis database. This queue will be used by the workload to locate the next dataset to process.

  5. Deploy the Service to make the Redis server discoverable within the GKE cluster.
         
         kubectl apply -f ./kubernetes-manifests/redis-service.yaml
         




## Run the batch workload

At this point, you prepared the GKE cluster, the Redis job queue, and fileshare. Now, you can run your batched workload.

In this section, you use a container image of a sample workload for training a fraud detection model using batches of financial transaction data. The training process can be summarized as follows:

  1. A Redis client claims jobs (file paths to datasets) in the Redis queue, and removes them from the queue when completed.

  2. A model training manager class, [`FraudDetectionModelTrainer`](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/batch/aiml-workloads/src/model_training.py#L25), loads a new batch of data and, optionally, a saved state of a machine learning model. The dataset is used to refine the model (a process known as ["warm-start" training](https://arxiv.org/abs/1910.08475)).

  3. The new state of the model and a report of the batch details and performance scores are saved in the Filestore NFS volume, which can be accessed in the GKE cluster using a PersistentVolumeClaim.




To learn more, [explore the source code](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/batch/aiml-workloads/src).

### Define the Job

The following manifest describes the Kubernetes Job for the batch workload image. A Job controller in Kubernetes creates one or more Pods and helps ensure that they successfully execute a specific task.
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: workload
    spec:
    ** parallelism: 1**
      template:
        metadata:
          name: workload
        spec:
    ** nodeSelector:**
    ** cloud.google.com/gke-spot: "true"**
          containers:
          - name: workload
            image: "us-docker.pkg.dev/google-samples/containers/gke/batch-ml-workload"
            volumeMounts:
            - mountPath: /mnt/fileserver
              name: workload-pvc
          volumes:
          - name: workload-pvc
            persistentVolumeClaim:
              claimName: fileserver-claim
              readOnly: false
          restartPolicy: OnFailure

**Note:** If you configure a workload where batches can be run in parallel (e.g. classifying batches of images, long-running data analysis, etc), you can increase the `parallelism` value to allow that many Pods to run the job concurrently until the completion condition is met. The `nodeSelector` specification tells GKE to use Spot Pods.

### Deploy the workload

  1. Deploy the Job:
         
         kubectl apply -f ./kubernetes-manifests/workload.yaml
         

  2. Check if the status of the `workload-XXX` Pod is `Completed`:
         
         watch kubectl get pods
         

This might take a few seconds. You can return to the command line by pressing `Ctrl+C`.

The output is similar to the following:
         
         NAME             READY   STATUS      RESTARTS   AGE
         redis-leader     1/1     Running     0          16m
         workload-4p55d   0/1     Completed   0          83s
         

  3. Check the logs from the `workload` Job:
         
         kubectl logs job/workload
         

The output is similar to the following:
         
         Worker with sessionID: b50f9459-ce7f-4da8-9f84-0ab5c3233a72
         Initial queue state: empty=False
         Processing dataset: datasets/training/2018-04-04.pkl
         Processing dataset: datasets/training/2018-04-03.pkl
         Processing dataset: datasets/training/2018-04-02.pkl
         Processing dataset: datasets/training/2018-04-01.pkl
         Queue empty, exiting
         

The `.pkl` files are serializations of datasets containing a batch of credit card transactions, marked valid or fraudulent. The `workload` Job iterates over these files, unpacking the datasets and using them to train the machine learning model, before removing them from the Redis queue. The workload continues to process the data in batches, until the Redis queue is emptied, before exiting with success.




### Explore the NFS volume

During its operation the workload creates files in the mounted NFS volume, accessible across the cluster by other batch jobs or online applications.

  1. List the files created by the workload:
         
         kubectl exec --stdin --tty redis-leader -- /bin/sh -c "ls -1 /mnt/fileserver/output"
         

The output should be the following:
         
         model_cpt_2018-04-01.pkl
         model_cpt_2018-04-02.pkl
         model_cpt_2018-04-03.pkl
         model_cpt_2018-04-04.pkl
         report.txt
         

Checkpoints for the trained model (filenames like `model_cpt_XXX.pkl`) and a report of the model performance (`report.txt`) were created in the `/mnt/fileserver/output` directory on the NFS volume.

  2. Inspect the model performance report:
         
         kubectl exec --stdin --tty redis-leader -- /bin/sh -c "cat /mnt/fileserver/output/report.txt"
         

The following is a snippet from the output:
         
         Report generated on: 2022-02-09 14:19:42.303619
         Training dataset: 2018-04-04.pkl
         Model checkpoint: model_cpt_2018-04-04.pkl
         ---
         Accuracy on training data: 0.9981112277019937
         Accuracy on testing data: 0.9977204434773599
         

The file contains entries detailing the time of training, dataset used, accuracy achieved, and the filename of the model checkpoint associated with the training.




To learn more about NFS volumes, check out the [Filestore guides](https://docs.cloud.google.com/filestore/docs/how-to).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Remove individual resources

To remove the individual resources created for this tutorial, run the following commands.

  1. Delete the cluster:
         
         gcloud container clusters delete batch-aiml \
             --location=us-central1
         

  2. Delete the Filestore instance:
         
         gcloud filestore instances delete batch-aiml-filestore \
             --zone=us-central1-b
         




### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Check out the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

  * Explore [Persistent Volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) in more detail.

  * Learn more about [Jobs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/jobs).

  * Learn [how to use Spot VMs to run fault-tolerant workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms).

  * Explore other [Kubernetes Engine tutorials](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials). 

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
