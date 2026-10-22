---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/aws-iam-role-list/
title: AWS IAM role list \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:04.182194+00:00
---

# AWS IAM role list  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/aws-iam-role-list/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/apis)



Send feedback 

#  AWS IAM role list Stay organized with collections  Save and categorize content based on your preferences. 

The tables on this page list all of the permissions used in creating the default AWS IAM roles. To create these policies with default permissions, see [Create AWS IAM roles](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles).

GKE Multi-Cloud API service agent role
    The GKE Multi-Cloud API uses this AWS IAM role to manage resources using AWS APIs. This role is used by a Google-managed service account known as a [service agent](https://docs.cloud.google.com/iam/docs/service-agents).
Control plane AWS IAM role
    Your cluster control plane uses this role to control node pools.
Node pool AWS IAM role
    The control plane uses this role to create node pool VMs.

Depending upon your organization's requirements, you can choose to create custom AWS IAM policies for GKE on AWS to manage your clusters. These policies will replace the default versions. You then apply these policies to AWS IAM roles and provide them when you create a cluster.

For more information on the purpose of each role, see [AWS IAM roles for GKE on AWS](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/aws-iam-roles).

To create these policies, choose the level that you wish to restrict your resources at. For example, you can restrict a policy to a particular AWS VPC using the VPC's Amazon Resource Name (ARN). For more information, see [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html).

## IAM policies for GKE Multi-Cloud service agents

Resource Type | ARN | Permission Required | Purpose | Reference  
---|---|---|---|---  
Security Group | `arn:aws:ec2:*:*:security-group/sg-*` | `ec2:DescribeSecurityGroups` (Create, Update, Delete)  
`ec2:CreateSecurityGroup` (Create)  
`ec2:CreateTags` (Create)  
`ec2:RevokeSecurityGroupEgress` (Create)  
`ec2:DeleteSecurityGroup` (Delete) | Control plane security group |   
Security Group | Node pool security group |   
Security Group Rule | `arn:aws:ec2:*:*:security-group-rule/sgr-*` | `ec2:AuthorizeSecurityGroupEgress` (Create)  
`ec2:RevokeSecurityGroupEgress` (Delete)  
`ec2:CreateTags` (Create) | Control plane egress security group rule |   
Security Group Rule | `ec2:AuthorizeSecurityGroupIngress` (Create)  
`ec2:RevokeSecurityGroupIngress` (Delete)  
`ec2:CreateTags` (Create) | Control plane ingress security group rule |   
Security Group Rule | `ec2:AuthorizeSecurityGroupEgress` (Create)  
`ec2:RevokeSecurityGroupEgress` (Delete)  
`ec2:CreateTags` (Create) | Control plane egress security group rule |   
Security Group Rule | `ec2:AuthorizeSecurityGroupIngress` (Create)  
`ec2:RevokeSecurityGroupIngress` (Delete)  
`ec2:CreateTags` (Create) | Control plane ingress security group rule |   
Network Load Balancer | `arn:aws:elasticloadbalancing:*:*:loadbalancer/net/gke-*` | `elasticloadbalancing:DescribeLoadBalancers` (Create, Delete)   
`elasticloadbalancing:CreateLoadBalancer` (Create)  
`ec2:CreateSecurityGroup` (Create)  
`ec2:DescribeAccountAttributes` (Create)  
`ec2:DescribeInternetGateways` (Create)  
`ec2:DescribeSecurityGroups` (Create)  
`ec2:DescribeSubnets` (Create)  
`ec2:DescribeVpcs` (Create)  
`iam:CreateServiceLinkedRole` (Create)  
`elasticloadbalancing:DeleteLoadBalancer` (Delete) | Kubernetes api-server load balancer |  [Elastic Load Balancing API permissions](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/elb-api-permissions.html)  
Target Group | `arn:aws:elasticloadbalancing:*:*:targetgroup/gke-*` | `elasticloadbalancing:DescribeTargetGroups` (Create, Update, Delete)  
`elasticloadbalancing:DescribeTargetHealth` (Create, Update)  
`elasticloadbalancing:CreateTargetGroup` (Create)  
`elasticloadbalancing:ModifyTargetGroupAttributes` (Create)  
`ec2:DescribeInternetGateways` (Create)  
`ec2:DescribeVpcs` (Create)  
`elasticloadbalancing:DeleteTargetGroup` (Delete) | Target group for https |  [Elastic Load Balancing API permissions ](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/elb-api-permissions.html)  
Target Group | Target group for https for konnectivity agent |   
Listener | `arn:aws:elasticloadbalancing:*:*:listener/net/gke-*` | `elasticloadbalancing:CreateListener` (Create)  
`elasticloadbalancing:DeleteListener` (Delete) `elasticloadbalancing:DescribeListeners` (Delete)  
`elasticloadbalancing:DeleteListener` (Delete) | Listener for https |   
Listener | Listener for https for konnectivity agent |   
Volume | `arn:aws:ec2:*:*:volume/vol-*` |  `ec2:CreateVolume` (Create)  
`ec2:CreateTags` (Create)  
`ec2:DeleteVolume` (Delete) | etcd volumes |   
Network Interface | `arn:aws:ec2:*:*:network-interface/eni-*` | `ec2:DescribeNetworkInterfaces` Update  
`ec2:CreateNetworkInterface` (Create)  
`ec2:CreateTags` (Create)  
`ec2:ModifyNetworkInterfaceAttribute` (Update)  
`ec2:DeleteNetworkInterface` (Delete) | etcd NICs  |   
Launch Template | `arn:aws:ec2:*:*:launch-template/lt-*` | `ec2:CreateLaunchTemplate` (Create, Update)  
`ec2:CreateTags` (Create, Update)  
`ec2:DeleteLaunchTemplate` (Delete) | Launch template for control plane instances |   
Launch Template | Launch template for node pool instances |   
Auto Scaling Group | `arn:aws:autoscaling:*:*:autoScalingGroup:*:autoScalingGroupName/gke-*` | `autoscaling:DescribeAutoScalingGroups` (Create, Update, Delete)  
`autoscaling:CreateAutoScalingGroup` (Create)  
`autoscaling:CreateOrUpdateTags` (Update)  
`autoscaling:UpdateAutoScalingGroup` (Update, Delete)  
`autoscaling:TerminateInstanceInAutoScalingGroup` (Update)  
`autoscaling:DeleteTags` Update, (Delete)  
`autoscaling:DeleteAutoScalingGroup` (Delete)  
`iam:CreateServiceLinkedRole` (Create)  
`ec2:RunInstances` (Create)  
`iam:PassRole` （Create） | auto scaling groups for control plane instances |  [Required API permissions for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/security_iam_id-based-policy-examples.html#ec2-auto-scaling-api-permissions)  
Auto Scaling Group | `arn:aws:autoscaling:*:*:autoScalingGroup:*:autoScalingGroupName/gke-*` | auto scaling groups for node pool instances |  [Required permissions to create a service-linked role](https://docs.aws.amazon.com/autoscaling/ec2/userguide/security_iam_id-based-policy-examples.html#ec2-auto-scaling-slr-permissions)  
EC2 key pairs |  | `ec2:DescribeKeyPairs` (Create) | To ensure the EC2 key pair used to login into cluster machines exists. |   
Subnets |  | `ec2:DescribeSubnets` (Create) |  | Access to additional subnets in your VPC  
VPC |  | `ec2:DescribeVpcs` (Create) |  | Information on your AWS VPC  
EC2 Console output |  | `ec2:GetConsoleOutput` (Create, Update) | Check console logs for errors |   
KMS Key |  | `For more information on KMS key policies for GKE on AWS [ Creating KMS keys with specific permissions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-kms-key#specific-permissions) |  |  `  
  
## IAM policy for control plane role

Purpose | Permission Required | Reference  
---|---|---  
cluster autoscaler | `autoscaling:DescribeAutoScalingGroups` (Create, Update)  
`autoscaling:DescribeAutoScalingInstances` (Create, Update)  
`autoscaling:DescribeLaunchConfigurations` (Create, Update)  
`autoscaling:DescribeTags` (Create, Update)  
`ec2:DescribeInstanceTypes` (Create, Update)  
`ec2:DescribeLaunchTemplateVersions` (Create, Update)  
`autoscaling:SetDesiredCapacity`  
`autoscaling:TerminateInstanceInAutoScalingGroup` | [`https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md`](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md)  
cloud-provider-aws | `autoscaling:DescribeAutoScalingGroups`  
`autoscaling:DescribeLaunchConfigurations`  
`autoscaling:DescribeTags` (Create)  
`ec2:DescribeInstances` (Create)  
`ec2:DescribeRegions`  
`ec2:DescribeRouteTables`  
`ec2:DescribeSecurityGroups`  
`ec2:DescribeSubnets`  
`ec2:DescribeVolumes`  
`ec2:CreateSecurityGroup`  
`ec2:CreateTags`  
`ec2:CreateVolume`  
`ec2:ModifyInstanceAttribute`  
`ec2:ModifyVolume`  
`ec2:AttachVolume` (Create)  
`ec2:AuthorizeSecurityGroupIngress`  
`ec2:CreateRoute`  
`ec2:DeleteRoute`  
`ec2:DeleteSecurityGroup`  
`ec2:DeleteVolume`  
`ec2:DetachVolume`  
`ec2:RevokeSecurityGroupIngress`  
`ec2:DescribeVpcs`  
`elasticloadbalancing:AddTags`  
`elasticloadbalancing:AttachLoadBalancerToSubnets`  
`elasticloadbalancing:ApplySecurityGroupsToLoadBalancer`  
`elasticloadbalancing:CreateLoadBalancer`  
`elasticloadbalancing:CreateLoadBalancerPolicy`  
`elasticloadbalancing:CreateLoadBalancerListeners`  
`elasticloadbalancing:ConfigureHealthCheck`  
`elasticloadbalancing:DeleteLoadBalancer`  
`elasticloadbalancing:DeleteLoadBalancerListeners`  
`elasticloadbalancing:DescribeLoadBalancers`  
`elasticloadbalancing:DescribeLoadBalancerAttributes`  
`elasticloadbalancing:DetachLoadBalancerFromSubnets`  
`elasticloadbalancing:DeregisterInstancesFromLoadBalancer`  
`elasticloadbalancing:ModifyLoadBalancerAttributes`  
`elasticloadbalancing:RegisterInstancesWithLoadBalancer`  
`elasticloadbalancing:SetLoadBalancerPoliciesForBackendServer`  
`elasticloadbalancing:AddTags`  
`elasticloadbalancing:CreateListener`  
`elasticloadbalancing:CreateTargetGroup`  
`elasticloadbalancing:DeleteListener`  
`elasticloadbalancing:DeleteTargetGroup`  
`elasticloadbalancing:DescribeListeners`  
`elasticloadbalancing:DescribeLoadBalancerPolicies`  
`elasticloadbalancing:DescribeTargetGroups`  
`elasticloadbalancing:DescribeTargetHealth`  
`elasticloadbalancing:ModifyListener`  
`elasticloadbalancing:ModifyTargetGroup`  
`elasticloadbalancing:RegisterTargets`  
`elasticloadbalancing:DeregisterTargets`  
`elasticloadbalancing:SetLoadBalancerPoliciesOfListener`  
`iam:CreateServiceLinkedRole`  
`kms:DescribeKey` |   
[`https://github.com/kubernetes/cloud-provider-aws/blob/master/docs/prerequisites.md`](https://github.com/kubernetes/cloud-provider-aws/blob/master/docs/prerequisites.md)  
Create load balancers | `elasticloadbalancing:CreateLoadBalancer`  
`ec2:DescribeAccountAttributes`  
`ec2:DescribeInternetGateways`  
`ec2:DescribeSecurityGroups`  
`ec2:DescribeSubnets`  
`ec2:DescribeVpcs` | [`https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/elb-api-permissions.html`](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/elb-api-permissions.html)  
aws-ebs-csi-driver | `ec2:DescribeVolumesModifications  
ec2:DeleteTags  
`   
[ec2:DescribeAvailabilityZones](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/example-iam-policy.json)  
  
| [`https://github.com/kubernetes-sigs/aws-ebs-csi-driver/tree/master/docs#set-up-driver-permission`](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/tree/master/docs#set-up-driver-permission)  
gke-aws-controller-manager | `ec2:DescribeDhcpOptions`  
`ec2:DescribeInstances`  
`ec2:DescribeVpcs` |   
`elasticloadbalancing:ModifyTargetGroupAttributes` |  |   
`ec2:DescribeSnapshots`  
`ec2:CreateSnapshot`  
`ec2:DeleteSnapshot` |  CSI snapshotter | [Kubernetes external snapshotter](https://github.com/kubernetes-csi/external-snapshotter)  
GKE on AWS node agent  
Attach NIC to etcd | `ec2:AttachNetworkInterface` (Create, Update) |   
Read proxy configuration from Secrets Manager | `secretsmanager:GetSecretValue` (Create, Update) |   
Interact with KMS keys | `kms:Encrypt` (Create, Update)  
`kms:Decrypt` (Create, Update)  
`kms:CreateGrant` (Create, Update) |   
  
## IAM policy for node pool role

Purpose | Permission Required | Reference  
---|---|---  
Read proxy configuration from secrets manager | `secretsmanager:GetSecretValue` (Create, Update) |   
KMS key to decrypt node pool configuration encryption | `kms:Decrypt` (Create, Update)  | [Create an AWS KMS key](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-kms-key)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
