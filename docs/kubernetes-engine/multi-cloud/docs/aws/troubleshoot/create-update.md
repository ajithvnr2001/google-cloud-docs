---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshoot/create-update/
title: Troubleshoot cluster creation or update issues \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:28.659684+00:00
---

# Troubleshoot cluster creation or update issues  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshoot/create-update/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Troubleshoot cluster creation or update issues Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues related to installing or upgrading GKE on AWS.

If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/getting-support). 

## Cluster creation failures

When you make a request to create a cluster, GKE on AWS first runs a set of _pre-flight tests_ to verify the request. If the cluster creation fails, it can be either because one of these pre-flight tests failed or because a step in the cluster creation process itself didn't complete.

If a pre-flight test fails, your cluster doesn't create any resources, and returns information on the error to you directly. For example, if you try to create a cluster with the name `invalid%%%name`, the pre-flight test for a valid cluster name fails and the request returns the following error:
    
    
    ERROR: (gcloud.container.aws.clusters.create) INVALID_ARGUMENT: must be
    between 1-63 characters, valid characters are /[a-z][0-9]-/, should start with a
    letter, and end with a letter or a number: "invalid%%%name",
    field: aws_cluster_id
    

Cluster creation can also fail after the pre-flight tests have passed. This can happen several minutes after cluster creation has begun, after GKE on AWS has created resources in Google Cloud and AWS. In this case, an AWS resource will exist in your Google Cloud project with its state set to `ERROR`.

To get details about the failure, run the following command:
    
    
    gcloud container aws clusters describe CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION \
        --format "value(state, errors)"
    

Replace the following:

  * CLUSTER_NAME with the name of the cluster whose state you're querying
  * GOOGLE_CLOUD_LOCATION with the name of the Google Cloud region that manages this AWS cluster



Alternatively, you can get details about the creation failure by describing the `Operation` resource associated with the create cluster API call.
    
    
    gcloud container aws operations describe OPERATION_ID
    

Replace OPERATION_ID with the ID of the operation that created the cluster. If you don't have the operation ID of your cluster creation request, you can fetch it with the following command:
    
    
    gcloud container aws operations list \
        --location GOOGLE_CLOUD_LOCATION
    

Use the timestamp or related information to identify the cluster creation operation of interest.

For example, if your cluster creation has failed because of an insufficiently permissioned AWS IAM role, this command and its results resemble the following example: 
    
    
    gcloud container aws operations describe b6a3d042-8c30-4524-9a99-6ffcdc24b370 \
      --location GOOGLE_CLOUD_LOCATION
    

The output is similar the following:
    
    
    done: true
    error:
      code: 9
      message: 'could not set deregistration_delay timeout for the target group: AccessDenied
        User: arn:aws:sts::0123456789:assumed-role/foo-1p-dev-oneplatform/multicloud-service-agent
        is not authorized to perform: elasticloadbalancing:ModifyTargetGroupAttributes
        on resource: arn:aws:elasticloadbalancing:us-west-2:0123456789:targetgroup/gke-4nrk57tlyjva-cp-tcp443/74b57728e7a3d5b9
        because no identity-based policy allows the elasticloadbalancing:ModifyTargetGroupAttributes
        action'
    metadata:
      '@type': type.googleapis.com/google.cloud.gkemulticloud.v1.OperationMetadata
      createTime: '2021-12-02T17:47:31.516995Z'
      endTime: '2021-12-02T18:03:12.590148Z'
      statusDetail: Cluster is being deployed
      target: projects/123456789/locations/us-west1/awsClusters/aws-prod1
    name: projects/123456789/locations/us-west1/operations/b6a3d042-8c30-4524-9a99-6ffcdc24b370
    

**Note:** After you resolve the failure, you must delete the cluster to release any resources that GKE on AWS created for it. You can then recreate the cluster.

### Cluster creation or operation fails with an authorization error

An error showing an authorization failure usually indicates that one of the two AWS IAM roles you specified during the cluster creation command was created incorrectly. For example, if the API role didn't include the `elasticloadbalancing:ModifyTargetGroupAttributes` permission, cluster creation would fail with an error message resembling the following:
    
    
    ERROR: (gcloud.container.aws.clusters.create) could not set
    deregistration_delay timeout for the target group: AccessDenied User:
    arn:aws:sts::0123456789:assumed-role/cloudshell-user-dev-api-role/multicloud-
    service-agent is not authorized to perform:
    elasticloadbalancing:ModifyTargetGroupAttributes on resource:
    arn:aws:elasticloadbalancing:us-east-1:0123456789:targetgroup/gke-u6au6c65e4iq-
    cp-tcp443/be4c0f8d872bb60e because no identity-based policy allows the
    elasticloadbalancing:ModifyTargetGroupAttributes action
    

Even if a cluster appears to have been created successfully, an incorrectly specified IAM role might cause failures later during cluster operation, such as when using commands like `kubectl logs`.

To resolve such authorization errors, confirm the policies associated with the two IAM roles you specified during cluster creation are correct. Specifically, ensure that they match the descriptions in [Create AWS IAM roles](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_role), then delete and re-create the cluster. The individual role descriptions are available in [API Role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_role) and [Control plane role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_the_control_plane_role).

### Cluster creation or operation fails at the health checking stage

Sometimes the cluster creation fails during health checking with an Operation status that resembles the following:
    
    
    done: true
    error:
      code: 4
      message: Operation failed
    metadata:
      '@type': type.googleapis.com/google.cloud.gkemulticloud.v1.OperationMetadata
      createTime: '2022-06-29T18:26:39.739574Z'
      endTime: '2022-06-29T18:54:45.632136Z'
      errorDetail: Operation failed
      statusDetail: Health-checking cluster
      target: projects/123456789/locations/us-west1/awsClusters/aws-prod1
    name: projects/123456789/locations/us-west1/operations/8a7a3b7f-242d-4fff-b518-f361d41c6597
    

This failure might be because of missing IAM roles or incorrectly specified IAM roles. You can use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) to expose IAM issues.

For example:

  * If the API role didn't include the `kms:GenerateDataKeyWithoutPlaintext` permission for control plane main volume KMS key, you'll see following events:
        
        "eventName": "AttachVolume",
        "errorCode": "Client.InvalidVolume.NotFound",
        "errorMessage": "The volume 'vol-0ff75940ce333aebb' does not exist.",
        

and
        
        "errorCode": "AccessDenied",
        "errorMessage": "User: arn:aws:sts::0123456789:assumed-role/foo-1p-dev-oneplatform/multicloud-service-agent is not authorized to perform: kms:GenerateDataKeyWithoutPlaintext on resource: arn:aws:kms:us-west1:0123456789:key/57a61a45-d9c1-4038-9021-8eb08ba339ba because no identity-based policy allows the kms:GenerateDataKeyWithoutPlaintext action",
        

  * If the control plane role didn't include the `kms:CreateGrant` permission for control plane main volume KMS key, you'll see following events:
        
        "eventName": "AttachVolume",
        "errorCode": "Client.CustomerKeyHasBeenRevoked",
        "errorMessage": "Volume vol-0d022beb769c8e33b cannot be attached. The encrypted volume was unable to access the KMS key.",
        

and
        
        "errorCode": "AccessDenied",
        "errorMessage": "User: arn:aws:sts::0123456789:assumed-role/foo-controlplane/i-0a11fae03eb0b08c1 is not authorized to perform: kms:CreateGrant on resource: arn:aws:kms:us-west1:0123456789:key/57a61a45-d9c1-4038-9021-8eb08ba339ba because no identity-based policy allows the kms:CreateGrant action",
        

  * If you didn't give the service-linked role named `AWSServiceRoleForAutoScaling` with `kms:CreateGrant` permissions to use the control plane root volume KMS key, you'll see following events:
        
        "errorCode": "AccessDenied",
        "errorMessage": "User: arn:aws:sts::0123456789:assumed-role/AWSServiceRoleForAutoScaling/AutoScaling is not authorized to perform: kms:CreateGrant on resource: arn:aws:kms:us-west1:0123456789:key/c77a3a26-bc91-4434-bac0-0aa963cb0c31 because no identity-based policy allows the kms:CreateGrant action",
        

  * If you didn't give the service-linked role named `AWSServiceRoleForAutoScaling` with `kms:GenerateDataKeyWithoutPlaintext` permissions to use the control plane root volume KMS key, you'll see following events:
        
        "errorCode": "AccessDenied",
        "errorMessage": "User: arn:aws:sts::0123456789:assumed-role/AWSServiceRoleForAutoScaling/AutoScaling is not authorized to perform: kms:GenerateDataKeyWithoutPlaintext on resource: arn:aws:kms:us-west1:0123456789:key/c77a3a26-bc91-4434-bac0-0aa963cb0c31 because no identity-based policy allows the kms:CreateGrant action",
        




### Waiting for nodes to join the cluster

If you receive the following error when creating a node pool, check that your VPC does not include an [Associated secondary IPv4 CIDR block](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#add-ipv4-cidr).
    
    
    errorDetail: Operation failed
    statusDetail: Waiting for nodes to join the cluster (0 out of 1 are ready)
    

To fix this issue, create a security group that includes all the CIDR blocks and add that group to your cluster. For more information, see [Node pools in VPC Secondary CIDR blocks](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups#node_pools_in_vpc_secondary_cidr_blocks).

### Get an instance's system log

If a control plane or node pool instance doesn't start, you can inspect its system log. To inspect the system log, do the following:

  1. Open the [AWS EC2 Instance console](https://console.aws.amazon.com/ec2/).
  2. Click **Instances**.
  3. Find the instance by name. GKE on AWS typically creates instances named `CLUSTER_NAME-cp` for control plane nodes or `CLUSTER_NAME-np` for node pool nodes.
  4. Choose **Actions** -> **Monitor and Troubleshoot** -> **Get System Log**. The instance's system log appears.



## Cluster update failures

When you update a cluster, just as when you create a new cluster, GKE on AWS first runs a set of _pre-flight tests_ to verify the request. If the cluster update fails, it can be either because one of these pre-flight tests failed or because a step in the cluster update process itself didn't complete.

If a pre-flight test fails, your cluster doesn't update any resources, and returns information on the error to you directly. For example, if you try to update a cluster to use an SSH key pair with name `test_ec2_keypair`, the pre-flight test tries to fetch the EC2 key pair and fails and the request returns the following error:
    
    
    ERROR: (gcloud.container.aws.clusters.update) INVALID_ARGUMENT: key pair
    "test_ec2_keypair" not found,
    field: aws_cluster.control_plane.ssh_config.ec2_key_pair
    

Cluster updates can also fail after the pre-flight tests have passed. This can happen several minutes after cluster update has begun, and your AWS resource in your Google Cloud project has its state set to `DEGRADED`.

To get details about the failure and the related operation, follow the steps described in cluster creation failures.

### Cluster update fails when updating control plane tags

The AWS update API [supports](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/release-notes#September_29_2022) updating control plane tags. To update tags, you need a cluster with Kubernetes version 1.24 or higher. You must also make sure your [AWS IAM role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_role) has the appropriate permissions as listed on the [update cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-cluster#prerequisites) page for updating control plane tags.

An error showing an authentication failure usually indicates you missed adding some IAM permission. For example, if the API role didn't include the `ec2:DeleteTags` permission, cluster update for tags might fail with an error message resembling the following (the `<encoded_auth_failure_message>` is redacted for brevity):
    
    
    ERROR: (gcloud.container.aws.clusters.update) could not delete tags:
    UnauthorizedOperation You are not authorized to perform this operation.
    Encoded authorization failure message: <encoded_auth_failure_message>
    

To debug the preceding encoded failure message, you could send a request to AWS STS [decode-authorization-message](https://docs.aws.amazon.com/cli/latest/reference/sts/decode-authorization-message.html) API as shown in the following command:
    
    
    aws sts decode-authorization-message --encoded-message
    <encoded_auth_failure_message> --query DecodedMessage --output
    text | jq '.' | less
    

The output is similar to the following:
    
    
    ...
    "principal": {
      "id": "AROAXMEL2SCNPG6RCJ72B:iam-session",
      "arn": "arn:aws:sts::1234567890:assumed-role/iam_role/iam-session"
    },
    "action": "ec2:DeleteTags",
    "resource": "arn:aws:ec2:us-west-2:1234567890:security-group-rule/sgr-00bdbaef24a92df62",
    ...
    

The preceding response indicates that you couldn't perform `ec2:DeleteTags` action on the EC2 security group rule resource of the AWS cluster. Update your [API Role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_role) accordingly and resend the update API request to update the control plane tags. 

## What's next

  * If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/getting-support). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
