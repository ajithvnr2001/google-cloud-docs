---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quickstart/
title: Deploy an application on GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:22.641883+00:00
---

# Deploy an application on GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quickstart/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Deploy an application on GKE on AWS Stay organized with collections  Save and categorize content based on your preferences. 

This page provides quickstart instructions to create a cluster and node pool, then deploy a sample application using GKE on AWS.

This page is for IT administrators and Operators who want to set up, monitor, and manage cloud infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Quickstart your cluster with Terraform

You can [use Terraform to create a cluster and node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster-with-terraform). Before creating your cluster, the Terraform scripts also prepare your AWS VPC.

You can learn more about Terraform in an AWS environment in the [Terraform cluster reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_aws_cluster) and [Terraform node pool reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_aws_node_pool).

After you create a VPC and cluster with Terraform, skip to Deploy an application to the cluster to deploy a sample application.

## Quickstart your cluster without Terraform

If you prefer to prepare your AWS VPC and create a cluster and node pool without Terraform, follow these instructions.

## Before you begin

Before creating a cluster, you must complete the [prerequisites](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/prerequisites). In particular, you must provide the following resources:

  * An AWS VPC where the cluster will run.
  * Up to three AWS subnets for the three control plane replicas. Each must be in a different AWS Availability Zone.
  * The AWS IAM role that GKE on AWS assumes when managing your cluster. This requires a specific set of [IAM permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles).
  * KMS symmetric CMK keys for at-rest encryption of cluster data (etcd) and configuration.
  * The AWS IAM instance profile for each control plane replica. This requires a specific set of [IAM permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles).
  * An EC2 SSH key pair (optional) if you need SSH access to the EC2 instances that run each control plane replica.



It is your responsibility to create and manage these resources, which can be shared between all your GKE on AWS clusters. All other underlying cluster-scoped AWS resources are managed by GKE on AWS.

### Set default settings for the gcloud CLI

Use the gcloud CLI to configure default settings for your default project and Google Cloud region.

Your project has a project ID as a unique identifier. When you create a project, you can use the automatically generated project ID or you can create your own.

Your Google Cloud region is a location where your clusters will be managed from. For example, `us-west1`. See [Management regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/gcp-managed-regions) for more details.

When you configure these default settings, you don't need to include them when you run the Google Cloud CLI. You can also specify settings or override default settings by passing the `--project` and `--location` flags to the Google Cloud CLI.

When you create GKE on AWS resources after configuring your default project and location, the resources are automatically created in that project and location.

**Note:** The gcloud CLI might return an error if these settings are either not configured or not specified.

To set defaults, follow these steps:

  1. Set the default project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

  2. Set the default management location:
         
         gcloud config set container_aws/location GOOGLE_CLOUD_LOCATION
         

Replace `GOOGLE_CLOUD_LOCATION` with your location, such as `us-west1`.


**Note:** the `container_aws/location` property was previously named `aws/location`. If you have previously set the property `aws/location`, its value is copied to `container_aws/location` next time you run a command.

### Select CIDR ranges for your cluster

Kubernetes requires two CIDR ranges to be provided for the cluster. These CIDR ranges should be chosen so that they do not overlap with CIDR ranges used by your VPC subnets. They should be large enough for the maximum expected size of your cluster.

  * **Pod address CIDR range** : When a new `Pod` is created, it is allocated an IP address from this range. Example range: 192.168.208.0/20

  * **Service address CIDR range** : When a new `Service` is created, it is allocated an IP address from this range. Example range: 192.168.224.0/20




## Create a cluster

Use the following command to create a cluster under GKE on AWS. For more information about this command including its optional parameters, see the [gcloud container aws create](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create) reference page.
    
    
    gcloud container aws clusters create aws-cluster-0 \
        --cluster-version 1.35.3-gke.300 \
        --aws-region AWS_REGION \
        --fleet-project FLEET_PROJECT_ID \
        --vpc-id VPC_ID \
        --subnet-ids CONTROL_PLANE_SUBNET_1,CONTROL_PLANE_SUBNET_2,CONTROL_PLANE_SUBNET_3 \
        --pod-address-cidr-blocks POD_CIDR_BLOCK \
        --service-address-cidr-blocks SERVICE_CIDR_BLOCK \
        --role-arn API_ROLE_ARN \
        --iam-instance-profile CONTROL_PLANE_PROFILE \
        --database-encryption-kms-key-arn DB_KMS_KEY_ARN \
        --config-encryption-kms-key-arn CONFIG_KMS_KEY_ARN \
        --tags "google:gkemulticloud:cluster=aws-cluster-0"
    

Replace the following:

  * `AWS_REGION`: the AWS region to create the cluster in.
  * `FLEET_PROJECT_ID`: the [Fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) host project where the cluster will be registered
  * `VPC_ID`: the ID of the AWS VPC for this cluster that you set up in the [Create your VPC](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-vpc#create_your_vpc) prerequisite step
  * `CONTROL_PLANE_SUBNET_1`, `CONTROL_PLANE_SUBNET_2`, `CONTROL_PLANE_SUBNET_3`: the subnet IDs for your cluster's three control plane instances that you created in the [Create private subnets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-vpc#create_private_subnets) prerequisite step
  * `POD_CIDR_BLOCK`: the CIDR address range for your cluster's pods
  * `SERVICE_CIDR_BLOCK`: the CIDR address range for your cluster's services
  * `API_ROLE_ARN`: the ARN of the IAM role for the GKE Multi-Cloud service that you created in the [Create GKE Multi-Cloud API role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_role) prerequisite step
  * `CONTROL_PLANE_PROFILE`: the profile name of the IAM instance associated with the cluster that you chose in the [Create control plane role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_the_control_plane_role) prerequisite step
  * `DB_KMS_KEY_ARN`: the Amazon Resource Name (ARN) of one of the AWS KMS keys that you created in the [Create an AWS KMS key](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-kms-key#create_an_aws_kms_key) prerequisite step
  * `CONFIG_KMS_KEY_ARN`: the Amazon Resource Name (ARN) of the other of the AWS KMS keys that you created in the [Create an AWS KMS key](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-kms-key#create_an_aws_kms_key) prerequisite step



If present, the `--tags` parameter applies the given AWS tag to all the underlying AWS resources managed by GKE on AWS. This example tags your control plane nodes with name of the cluster they belong to.

## Create a node pool

Use the following command to create a node pool:
    
    
    gcloud container aws node-pools create pool-0 \
        --cluster aws-cluster-0 \
        --node-version 1.35.3-gke.300 \
        --min-nodes 1 \
        --max-nodes 5 \
        --max-pods-per-node 110 \
        --root-volume-size 50 \
        --subnet-id NODEPOOL_SUBNET_ID \
        --iam-instance-profile NODEPOOL_PROFILE \
        --config-encryption-kms-key-arn CONFIG_KMS_KEY_ARN \
        --ssh-ec2-key-pair EC2_KEY_PAIR \
        --tags "google:gkemulticloud:cluster=aws-cluster-0"
    

Replace the following:

  * `NODEPOOL_SUBNET_ID`: the ID of one of the private subnets that you created in the [Create private subnets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-vpc#create_private_subnets) prerequisite step
  * `NODEPOOL_PROFILE`: the IAM instance profile name for the EC2 instances in the node pool that you chose in the [Create a node pool IAM role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_a_node_pool_iam_role) prerequisite step
  * `CONFIG_KMS_KEY_ARN`: the Amazon Resource Name (ARN) of the AWS KMS key to encrypt user data
  * `EC2_KEY_PAIR` (optional): the name of the EC2 key pair created for SSH access (optional) that you created in the [Create SSH key pair](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-ssh-keypair) prerequisite step

**Note:** if your nodepool's subnet is outside of your VPC's primary CIDR block, you must take additional steps to configure [security groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups).

## View your cluster status

After you create a cluster and node pool, you can view a cluster's status with the Google Cloud CLI or the Google Cloud console. To view the cluster's status, choose if you are using the Google Cloud CLI or Google Cloud console and follow these steps:

###  gcloud 

Use the `gcloud container aws clusters describe` command to get details about your cluster:
    
    
    gcloud container aws clusters describe CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the name of the Google Cloud location that manages the cluster



###  Google Cloud console 

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Your clusters are listed by their name and location.

  3. Click the cluster's name. A panel with information on the cluster, including its status and enabled features, appears.




## Get authentication credentials for the cluster

After creating your cluster, you need to get authentication credentials to interact with the cluster:
    
    
    gcloud container aws clusters get-credentials aws-cluster-0
    

This command configures `kubectl` to access the cluster you created using [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway/using). You need at least one node pool to use Connect gateway because it relies on the Connect agent, which runs as a Deployment in the cluster.

## Deploy an application to the cluster

Now that you have created a cluster, you can deploy a containerized application to it. For this quickstart, you can deploy our example web application, `hello-app`.

You use Kubernetes objects to create and manage your cluster's resources. You use the Deployment object for deploying stateless applications like web servers. [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) objects define rules and load balancers for accessing your application from the internet.

### Create the Deployment

To run `hello-app` in your cluster, you need to deploy the application by running the following command:
    
    
    kubectl create deployment hello-server --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

This Kubernetes command, [`kubectl create deployment`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create) creates a Deployment named `hello-server`. The Deployment's [Pod](https://kubernetes.io/docs/concepts/workloads/pods) runs the `hello-app` container image.

In this command:

  * `--image` specifies a container image to deploy. In this case, the command pulls the example image from an Artifact Registry repository, `us-docker.pkg.dev/google-samples/containers/gke/hello-app`. The `:1.0` indicates the specific image version to pull. If you don't specify a version, the image tagged with `latest` is used.



### Expose the Deployment

After deploying the application, you need to expose it to the internet so that users can access it. You can expose your application by creating a Service, a Kubernetes resource that exposes your application to external traffic.

To expose your application, run the following [`kubectl expose`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#expose) command:
    
    
    kubectl expose deployment hello-server --type LoadBalancer --port 80 --target-port 8080
    

Passing in the `--type LoadBalancer` flag creates an AWS load balancer for your container. The `--port` flag initializes public port 80 to the internet and the `--target-port` flag routes the traffic to port 8080 of the application.

Load balancers are billed according to AWS load balancer pricing.

### Inspect and view the application

  1. Inspect the running Pods by using `kubectl get pods`:
         
         kubectl get pods
         

You should see one `hello-server` Pod running on your cluster.

  2. Inspect the `hello-server` Service by using `kubectl get service`:
         
         kubectl get service hello-server
         

From this command's output, copy the Service's external IP address from the `EXTERNAL-IP` column.

**Note:** You might need to wait several minutes before the Service's external IP address is available. If the application's external IP is `<pending>`, run `kubectl get service` again.
  3. View the application from your web browser by using the external IP with the exposed port:
         
         http://EXTERNAL-IP
         




You have just deployed a containerized web application to GKE on AWS.

## Clean up

  1. Delete the application's Service and Deployment:
         
         kubectl delete service hello-server
         kubectl delete deployment hello-server
         

  2. Delete your node pool by running `gcloud container aws node-pools delete`:
         
         gcloud container aws node-pools delete pool-0 --cluster aws-cluster-0
         

  3. Delete your cluster by running `gcloud container aws clusters delete`:
         
         gcloud container aws clusters delete aws-cluster-0
         




## What's next

  * [Install Anthos Config Management](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/install-config-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
