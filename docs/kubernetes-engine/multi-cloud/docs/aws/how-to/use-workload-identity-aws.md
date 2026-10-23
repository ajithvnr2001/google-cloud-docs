---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-workload-identity-aws/
title: Use workload identity with AWS \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:49.304684+00:00
---

# Use workload identity with AWS  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-workload-identity-aws/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Use workload identity with AWS Stay organized with collections  Save and categorize content based on your preferences. 

_Workload identity_ enables you to assign distinct, fine-grained identities and authorization for each application in your cluster. Workload identity is the recommended way for applications running within GKE on AWS to access AWS and Google Cloud services. For more information, see [Workload identity](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/workload-identity).

This topic explains how to create an OIDC provider, provision service accounts, and test a sample workload using workload identity. This page is for Identity and account admins, Operators, and Developers who want to create and manage policies related to user permissions. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Create an AWS IAM OIDC provider for your cluster

To use workload identity with your cluster, you first create an AWS IAM OIDC provider that references your cluster. If you already have an IAM OIDC provider for your cluster, you can skip this section.

To create the provider, follow these steps:

  1. Determine the OIDC issuer URI for your cluster:
         
         gcloud container aws clusters describe CLUSTER_NAME \
              --location=GOOGLE_CLOUD_LOCATION \
              --format='value(workloadIdentityConfig.issuerUri)'
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster
     * `GOOGLE_CLOUD_LOCATION`: the name of the Google Cloud location from which this node pool will be managed, as defined in [Google Cloud management regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/gcp-managed-regions)

The output includes your cluster's OIDC issuer URI. Save this value for the following step.

  2. Next, create an AWS IAM OIDC provider that references your cluster with the following command:
         
         aws iam create-open-id-connect-provider \
             --url ISSUER_URI \
             --client-id-list sts.amazonaws.com \
             --thumbprint-list 08745487e891c19e3078c1f2a07e452950ef36f6
         

Replace `ISSUER_URI` with your issuer URI from the previous step.

The [thumbprint](https://www.google.com/url?sa=D&q=https%3A%2F%2Fdocs.aws.amazon.com%2FIAM%2Flatest%2FUserGuide%2Fid_roles_providers_create_oidc_verify-thumbprint.html) of the Google Cloud service that serves the issuer URI is always `08745487e891c19e3078c1f2a07e452950ef36f6`.




## Configure an AWS IAM role with an attached IAM policy

To configure an AWS IAM role and attach a policy to it, follow these steps:

  1. Determine the issuer host by removing the `https://` prefix from the issuer URI. For example, if your URI is `https://oidc-provider.com/v1/projects/pid/locations/us-west1/awsClusters/awscluster`, the host is `oidc-provider.com/v1/projects/pid/locations/us-west1/awsClusters/awscluster`. Save this value. You'll need it later.

  2. Determine the provider's Amazon Resource Name (ARN) by running:
         
         aws iam list-open-id-connect-providers --output=text \
             --query 'OpenIDConnectProviderList[?ends_with(Arn, `ISSUER_HOST`) == `true`].Arn'
         

Replace `ISSUER_HOST` with the hostname from the issuer URI for the cluster.

  3. Next, create a trust policy to provide OIDC credentials to the Kubernetes service account. Create a file named `trust-policy.json` with the following contents:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "Federated": "PROVIDER_ARN"
               },
               "Action": "sts:AssumeRoleWithWebIdentity",
               "Condition": {
                 "StringEquals": {
                   "ISSUER_HOST:sub": "system:serviceaccount:NAMESPACE:KSA_NAME"
                 }
               }
             }
           ]
         }
         

Replace the following:

     * `PROVIDER_ARN`: the ARN of the cluster's IAM OIDC provider
     * `ISSUER_HOST`: the hostname from the issuer URI for the cluster. 
     * `NAMESPACE`: the Kubernetes namespace where the application runs 
     * `KSA_NAME`: the Kubernetes service account (KSA) to use for the application 
  4. Create an AWS IAM role:
         
         aws iam create-role --role-name=AWS_ROLE_NAME \
             --assume-role-policy-document file://trust-policy.json
         

Replace `AWS_ROLE_NAME` with the AWS IAM role name for the application.

  5. Attach an AWS IAM policy to the role:
         
         aws iam attach-role-policy --role-name=AWS_ROLE_NAME \
             --policy-arn=AWS_POLICY_ARN
         

Replace the following: 

     * `AWS_ROLE_NAME`: the AWS IAM role name for the application 

For example, to create a role named `ec2-readonly`, with the `arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess` policy, run the following command:
    
    aws iam attach-role-policy --role-name=ec2-readonly \
        --policy-arn=arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess
    




## Deploy a sample application

To test workload identity, follow these steps to deploy a sample application:

  1. Determine the role's ARN:
         
         aws iam get-role --role-name=AWS_ROLE_NAME --query 'Role.Arn'
         

Replace `AWS_ROLE_NAME`.

  2. Create a manifest for a Kubernetes Namespace, KSA, and Pod. Copy the following manifest into a file named `workload-identity-test.yaml`:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: NAMESPACE
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: KSA_NAME
           namespace: NAMESPACE
         automountServiceAccountToken: false
         ---
         apiVersion: v1
         kind: Pod
         metadata:
           name: aws-cli-example
           namespace: NAMESPACE
         spec:
           serviceAccount: KSA_NAME
           containers:
           - name: aws-cli
             image: amazon/aws-cli:latest
             command:
             - /bin/bash
             - -c
             - "set -eu -o pipefail; while true; do aws ec2 describe-availability-zones; sleep 5; done"
             env:
             - name: AWS_ROLE_ARN
               value: AWS_ROLE_ARN
             - name: AWS_WEB_IDENTITY_TOKEN_FILE
               value: /var/run/secrets/aws-iam-token/serviceaccount/token
             - name: AWS_REGION
               value: AWS_REGION
             volumeMounts:
             - mountPath: /var/run/secrets/aws-iam-token/serviceaccount
               name: aws-iam-token
               readOnly: true
           volumes:
           - name: aws-iam-token
             projected:
               defaultMode: 420
               sources:
               - serviceAccountToken:
                   audience: sts.amazonaws.com
                   expirationSeconds: 86400
                   path: token
         

Replace the following:

     * `NAMESPACE`
     * `KSA_NAME`
     * `AWS_ROLE_ARN`: the ARN of the AWS IAM role for the application
     * `AWS_REGION`: the AWS region of the cluster
  3. Apply the manifest:
         
         kubectl apply -f workload-identity-test.yaml
         

Wait several minutes for the Pod to start, and proceed to the following section.




### Verify the sample application is working

To verify the sample application can access the EC2 API, look at the pod's logs:
    
    
    kubectl logs -f aws-cli-example -n NAMESPACE
    

If the Pod can access the EC2 API, the output includes information on EC2 availability zones and looks similar to the following:
    
    
    -------------------------------------------------
    |           DescribeAvailabilityZones           |
    +-----------------------------------------------+
    ||              AvailabilityZones              ||
    |+---------------------+-----------------------+|
    ||  GroupName          |  us-west-2            ||
    ||  NetworkBorderGroup |  us-west-2            ||
    ||  OptInStatus        |  opt-in-not-required  ||
    ||  RegionName         |  us-west-2            ||
    ||  State              |  available            ||
    ||  ZoneId             |  usw2-az1             ||
    ||  ZoneName           |  us-west-2a           ||
    |+---------------------+-----------------------+|
    ||              AvailabilityZones              ||
    |+---------------------+-----------------------+|
    ||  GroupName          |  us-west-2            ||
    ||  NetworkBorderGroup |  us-west-2            ||
    ||  OptInStatus        |  opt-in-not-required  ||
    ||  RegionName         |  us-west-2            ||
    ||  State              |  available            ||
    ||  ZoneId             |  usw2-az2             ||
    ||  ZoneName           |  us-west-2b           ||
    |+---------------------+-----------------------+|
    ||              AvailabilityZones              ||
    |+---------------------+-----------------------+|
    ||  GroupName          |  us-west-2            ||
    ||  NetworkBorderGroup |  us-west-2            ||
    ||  OptInStatus        |  opt-in-not-required  ||
    ||  RegionName         |  us-west-2            ||
    ||  State              |  available            ||
    ||  ZoneId             |  usw2-az3             ||
    ||  ZoneName           |  us-west-2c           ||
    |+---------------------+-----------------------+|
    ||              AvailabilityZones              ||
    |+---------------------+-----------------------+|
    ||  GroupName          |  us-west-2            ||
    ||  NetworkBorderGroup |  us-west-2            ||
    ||  OptInStatus        |  opt-in-not-required  ||
    ||  RegionName         |  us-west-2            ||
    ||  State              |  available            ||
    ||  ZoneId             |  usw2-az4             ||
    ||  ZoneName           |  us-west-2d           ||
    |+---------------------+-----------------------+|
    
    

## Clean up

To remove this sample application, follow these steps:

  1. Delete the sample application's manifest from your cluster:
         
         kubectl delete -f workload-identity-test.yaml
         

  2. Detach the AWS IAM policy from the role:
         
         aws iam detach-role-policy --role-name AWS_ROLE_NAME \
             --policy-arn arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess
         

Replace `AWS_ROLE_NAME` with the AWS IAM role name for the application.

  3. Delete the AWS IAM role:
         
         aws iam delete-role --role-name AWS_ROLE_NAME
         

Replace `AWS_ROLE_NAME` with the AWS IAM role name for the application.

  4. Delete the AWS IAM OIDC provider:
         
         aws iam delete-open-id-connect-provider --open-id-connect-provider-arn PROVIDER_ARN
         

Replace `PROVIDER_ARN` with the ARN of the IAM OIDC provider for the cluster.




## What's next

  * Learn about [Using workload identity with Google Cloud services](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-workload-identity-google).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
