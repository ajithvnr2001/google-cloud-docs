---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/http-load-balancing/
title: Set up an HTTP Load Balancer \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:27.625012+00:00
---

# Set up an HTTP Load Balancer  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/http-load-balancing/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Set up an HTTP Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set up an AWS [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) (ALB).

For more information on the other types of load balancers that GKE on AWS supports, see [Load balancer overview](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancers).

This page is for Networking specialists who want to install, configure, and support network equipment. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before GKE on AWS can create an ALB, you must:

  * [Create a GKE on AWS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster) and configure access to it with `kubectl`.
  * [Register the cluster's OIDC provider](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-workload-identity-aws#create_an_aws_iam_oidc_provider_for_your_cluster) with AWS.



## Overview

Creating the first ALB in a cluster involves the following steps:

  * Identify and tag or annotate the subnets within your VPC that you want the ALBs provisioned in.
  * Create an AWS role giving the ALB controller access to AWS resources.
  * Install the open source `aws-load-balancer-controller`.
  * Create and deploy an ALB configuration.



To create subsequent ALBs, you need only create and deploy another ALB configuration.

## Create an Application Load Balancer

### Tag the subnets for your ALB

Before creating an ALB, you must tell AWS what subnets to run it in. The usual method is to tag the subnet with a tag that identifies it as available to the auto-discovery process. Alternatively, you can add an annotation to the Ingress object to explicitly list the subnets for it to run in.

To tag your selected subnets as available for auto-discovery, see [tag your service load balancer subnets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancer-subnets#tag_your_subnets_for_their_intended_use).

To annotate the Ingress object with a list of subnets, add an annotation named `alb.ingress.kubernetes.io/subnets` to the Kubernetes Ingress object. Set the annotation's value to a comma-separated list of subnet IDs or subnet names— for example `subnet-012345678abcdef,subnet- abcdef123456789,subnet-123456789abcdef`.

### Create AWS IAM permissions

Download the [IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for the AWS Load Balancer Controller. This policy enumerates the permissions the load balancer controller needs to function. You can review the policy on [GitHub](https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.4.4/docs/install/iam_policy.json). This command saves the policy to a file named `iam_policy.json`.
    
    
      curl -Lo iam_policy.json \
        https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.4.4/docs/install/iam_policy.json
    

  1. Use this file to create an IAM policy named `AWSLoadBalancerControllerIAMPolicy`:
         
         aws iam create-policy \
           --policy-name AWSLoadBalancerControllerIAMPolicy \
           --policy-document file://iam_policy.json
         




### Grant access to your load balancer

Create an AWS IAM role for the controller's service account by following the instructions in [create an AWS IAM role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-workload-identity-aws#configure_an_aws_iam_role_with_an_attached_iam_policy). In these instructions, replace the following:

  * `AWS_POLICY_ARN`: the ARN of the AWSLoadBalancerControllerIAPolicy created in the previous step
  * `KSA_NAME`: `"aws-load-balancer-controller"`
  * `K8S_NAMESPACE`: `"kube-system"`
  * `AWS_ROLE_NAME`: `"AWSLBControllerRole"`



To retrieve the policy's ARN, run this command:
    
    
    aws iam list-policies \
      --query 'Policies[?PolicyName==`AWSLoadBalancerControllerIAMPolicy`].Arn' \
      --output text
    

### Install the AWS load balancer controller

  1. To complete these steps, extract and save the following values. You'll need them later.

Find your cluster's UID by running the following command:
         
         gcloud container aws clusters describe CLUSTER_NAME \
             --location GOOGLE_CLOUD_LOCATION \
             --format "value(uid)"
         

Find your cluster's VPC ID by running the following command:
         
         gcloud container aws clusters describe CLUSTER_NAME \
             --location GOOGLE_CLOUD_LOCATION \
             --format "value(networking.vpcId)"
         

Find the ARN of the role named `AWSLBControllerRole` by running the following command:
         
         aws iam get-role --role-name AWSLBControllerRole --query Role.Arn --output text
         

Find your cluster's AWS region by running the following command:
         
         gcloud container aws clusters describe CLUSTER_NAME \
           --location GOOGLE_CLOUD_LOCATION \
           --format "value(awsRegion)"
         

Replace:

     * `GOOGLE_CLOUD_LOCATION` with the name of the Google region associated with your cluster
     * `CLUSTER_NAME` with the name of your cluster
  2. Install `cert-manager` with the following command:
         
         kubectl apply \
           --validate=false \
           -f https://github.com/jetstack/cert-manager/releases/download/v1.10.0/cert-manager.yaml
         

  3. Download the manifest for `aws-load-balancer-controller` and save it to local file `v2_4_4_full.yaml` with the following command:
         
         curl -Lo v2_4_4_full.yaml https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/download/v2.4.4/v2_4_4_full.yaml
         

  4. Edit the file `v2_4_4_full.yaml` and search for `kind: Deployment`. Replace the `Deployment` object with this modified version:
         
         kind: Deployment
         metadata:
           labels:
             app.kubernetes.io/component: controller
             app.kubernetes.io/name: aws-load-balancer-controller
           name: aws-load-balancer-controller
           namespace: kube-system
         spec:
           replicas: 1
           selector:
             matchLabels:
               app.kubernetes.io/component: controller
               app.kubernetes.io/name: aws-load-balancer-controller
           template:
             metadata:
               labels:
                 app.kubernetes.io/component: controller
                 app.kubernetes.io/name: aws-load-balancer-controller
             spec:
               containers:
               - args:
                 - --cluster-name=CLUSTER_UID
                 - --aws-region=AWS_REGION
                 - --aws-vpc-id=AWS_VPC_ID
                 - --ingress-class=alb
                 - --disable-restricted-sg-rules=true
                 image: amazon/aws-alb-ingress-controller:v2.4.4
                 env:
                 - name: AWS_ROLE_ARN
                   value: AWS_ROLE_ARN
                 - name: AWS_WEB_IDENTITY_TOKEN_FILE
                   value: /var/run/secrets/aws-load-balancer-controller/serviceaccount/token
                 livenessProbe:
                   failureThreshold: 2
                   httpGet:
                     path: /healthz
                     port: 61779
                     scheme: HTTP
                   initialDelaySeconds: 30
                   timeoutSeconds: 10
                 name: controller
                 ports:
                 - containerPort: 9443
                   name: webhook-server
                   protocol: TCP
                 resources:
                   limits:
                     cpu: 200m
                     memory: 500Mi
                   requests:
                     cpu: 100m
                     memory: 200Mi
                 securityContext:
                   allowPrivilegeEscalation: false
                   readOnlyRootFilesystem: true
                   runAsNonRoot: true
                 volumeMounts:
                 - mountPath: /tmp/k8s-webhook-server/serving-certs
                   name: cert
                   readOnly: true
                 - mountPath: /var/run/secrets/aws-load-balancer-controller/serviceaccount
                   name: aws-iam-token
                   readOnly: true
               priorityClassName: system-cluster-critical
               securityContext:
                 fsGroup: 1337
               serviceAccountName: aws-load-balancer-controller
               terminationGracePeriodSeconds: 10
               volumes:
               - name: cert
                 secret:
                   defaultMode: 420
                   secretName: aws-load-balancer-webhook-tls
               - name: aws-iam-token
                 projected:
                   defaultMode: 420
                   sources:
                   - serviceAccountToken:
                       audience: sts.amazonaws.com
                       expirationSeconds: 86400
                       path: token
         ---
         

Replace the following:

     * `CLUSTER_UID`: your cluster's UID— for example, `bbc7d232-21f6-4bb1-90dd-4b064cf8ccf8`
     * `AWS_VPC_ID`: the ID of your AWS VPC— for example, `vpc-1234567890abc`.
     * `AWS_ROLE_ARN`: the ARN of the role named `AWSLBControllerRole`
     * `AWS_REGION`: your cluster's AWS region— for example, `us-east-1`
  5. Apply the modified manifest to your cluster with the following command:
         
         kubectl apply -f v2_4_4_full.yaml
         

  6. Confirm that the load balancer controller is running with the following command:
         
         kubectl get deployment -n kube-system aws-load-balancer-controller
         

The output should look similar to the following, which shows that the `aws-load-balancer-controller` Deployment is available.
         
         NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
         aws-load-balancer-controller   1/1     1            1           51s
         




## Create an example ALB

This section demonstrates how to create an example ALB that serves a remake of the game [2048](https://wikipedia.org/wiki/2048_%28video_game%29).

  1. Copy the following YAML configuration into a file named `2048.yaml`. The configuration creates a Kubernetes Namespace, Service, and Deployment. The Deployment is exposed through an Ingress ALB.
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: game-2048
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           namespace: game-2048
           name: deployment-2048
         spec:
           selector:
             matchLabels:
               app.kubernetes.io/name: app-2048
           replicas: 5
           template:
             metadata:
               labels:
                 app.kubernetes.io/name: app-2048
             spec:
               containers:
               - image: alexwhen/docker-2048
                 imagePullPolicy: Always
                 name: app-2048
                 ports:
                 - containerPort: 80
         ---
         apiVersion: v1
         kind: Service
         metadata:
           namespace: game-2048
           name: service-2048
         spec:
           ports:
             - port: 80
               targetPort: 80
               protocol: TCP
           type: NodePort
           selector:
             app.kubernetes.io/name: app-2048
         ---
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           namespace: game-2048
           name: ingress-2048
           annotations:
             alb.ingress.kubernetes.io/scheme: internet-facing
         spec:
           ingressClassName: alb
           rules:
             - http:
                 paths:
                   - path: /
                     pathType: Prefix
                     backend:
                       service:
                         name: service-2048
                         port:
                           number: 80
         

  2. Apply the configuration to your cluster with the following command:
         
         kubectl apply -f 2048.yaml
         

  3. Check the status of the Ingress resource with the following command:
         
         kubectl get ingress -n game-2048 ingress-2048
         

The command output resembles the following. The `ADDRESS` column contains the endpoint of your Ingress resource.
         
         NAME           CLASS    HOSTS   ADDRESS                                                                   PORTS   AGE
          ingress-2048   <none>   *       k8s-game2048-ingress2-e2c347319a-1195690687.us-west-2.elb.amazonaws.com   80      2m19s
          ```
         

  4. Navigate to the ALB endpoint in a browser— for example: `http://k8s-game2048-ingress2-e2c347319a-1195690687.us-west-2.elb.amazonaws.com`. The 2048 game displays, demonstrating that you have successfully deployed and configured your ALB load balancer.




### Cleaning up

To remove the sample ALB and Deployment created in the previous step, delete the manifest with the following command:
    
    
    kubectl delete -f 2048.yaml
    

## What's next

  * Learn about [Ingress annotations](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.4/guide/ingress/annotations/)
  * Learn about [AWS Load Balancer Controller](https://github.com/kubernetes-sigs/aws-load-balancer-controller) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
