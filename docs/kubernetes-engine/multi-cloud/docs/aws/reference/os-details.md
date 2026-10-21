---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/os-details/
title: Operating system details \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:49.345821+00:00
---

# Operating system details  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/os-details/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/apis)



Send feedback 

#  Operating system details Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS manages the AWS EC2 instances and the operating system that runs on them. In Kubernetes versions 1.26 and higher, GKE on AWS uses Ubuntu 22.04 LTS base images for Linux nodes. In Kubernetes versions 1.25 and lower, GKE on AWS uses Ubuntu 20.04 LTS.

The base Ubuntu Amazon Machine Image (AMI) is maintained by Canonical. Google tests these images as part of the GKE on AWS release process. When a cluster or node pool is upgraded, the underlying EC2 instances are terminated and recreated with the latest operating system version.

When an instance of either OS launches, GKE on AWS performs additional configuration including:

  * Optimizing network settings for Kubernetes
  * Disabling the [Amazon SSM agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html)
  * Disabling unattended apt package upgrades and reboots (Ubuntu only)
  * Installing GKE on AWS and Kubernetes binaries



The tables below list the AMI image IDs by region and operating system.

## Verifying AMI ownership

You can find the AMI ID for an AWS region in Ubuntu AMI IDs by region. To confirm that Canonical published these AMIs, verify that the `OwnerID` of the AMI has an `OwnerID` value of `099720109477`.

To verify the `OwnerID` field or determine the generic AMI name, find the AMI ID in the regional image name tables below and run:
    
    
    aws ec2 describe-images --image-ids AMI_ID
    

Replace AMI_ID with the ID of the AMI in your AWS region.

The output from this command includes the Owner ID and the AMI name for this image.

**Note:** GKE on AWS is not affected by the [dockershim deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd) as clusters use the containerd runtime.

For more information, see [Amazon EC2](https://ubuntu.com/server/docs/cloud-images/amazon-ec2) in the Ubuntu documentation.

## Ubuntu

### Kubernetes 1.35

#### 1.35.3-gke.300

Region | AMI ID  
---|---  
ap-east-1  | ami-0b3ed2667ca7e14ce (X86_64)   
ami-0e9c014b474168cb2 (ARM64)  
ap-northeast-1  | ami-07156ba1a53aca2d0 (X86_64)   
ami-02809709c9bc12daf (ARM64)  
ap-northeast-2  | ami-0c60e3183d3a23c58 (X86_64)   
ami-0aebcd61ae13ec5e9 (ARM64)  
ap-northeast-3  | ami-012aedcf01a9db7a1 (X86_64)   
ami-00f7db7b4acafc957 (ARM64)  
ap-south-1  | ami-0641ef6c785bf8b87 (X86_64)   
ami-0aec9bbd9b648b5e1 (ARM64)  
ap-southeast-1  | ami-0bd210a63ae3ac5c3 (X86_64)   
ami-00a03a9b82291be5c (ARM64)  
ap-southeast-2  | ami-095c7f83255819da5 (X86_64)   
ami-0814ca216898da640 (ARM64)  
ap-southeast-3  | ami-03c900e95fc8426dc (X86_64)   
ami-0bde7ef1876d5b811 (ARM64)  
ca-central-1  | ami-0bf852cde5226b1a7 (X86_64)   
ami-04ce723957219bbe9 (ARM64)  
eu-central-1  | ami-0ee60f419806ecb19 (X86_64)   
ami-0b9378214e8cfaa7c (ARM64)  
eu-north-1  | ami-08643f8d76c29f875 (X86_64)   
ami-0b5222b7a06c71e81 (ARM64)  
eu-south-1  | ami-018b95bfb6ed08cca (X86_64)   
ami-0bccd6ddbbe949b59 (ARM64)  
eu-west-1  | ami-038435014866b831d (X86_64)   
ami-037c650d992f8370f (ARM64)  
eu-west-2  | ami-0808900371df89649 (X86_64)   
ami-07f15b9ff047b9195 (ARM64)  
eu-west-3  | ami-0d4d1462c0f38c1e3 (X86_64)   
ami-0ab06a4d5b05ae794 (ARM64)  
sa-east-1  | ami-0dc2847f0decfb805 (X86_64)   
ami-065f0fa714ea36d9c (ARM64)  
us-east-1  | ami-0d22e1bb5879573b7 (X86_64)   
ami-0bfda2d910bf1ebbe (ARM64)  
us-east-2  | ami-081633c3a08bfeaa5 (X86_64)   
ami-0f2bacc821d20f28b (ARM64)  
us-west-1  | ami-0859185c5eebd2241 (X86_64)   
ami-0f06d8a409958b8a0 (ARM64)  
us-west-2  | ami-03c85c1c709f07fd5 (X86_64)   
ami-0e9a3364cc9c3ab6f (ARM64)  
  
### Kubernetes 1.34

#### 1.34.1-gke.4700

Region | AMI ID  
---|---  
ap-east-1  | ami-0b9fec08dc0addb28 (X86_64)   
ami-0237f3c3f997a75d3 (ARM64)  
ap-northeast-1  | ami-078ba0917d44c502a (X86_64)   
ami-0a18afef41c18d73a (ARM64)  
ap-northeast-2  | ami-08bd6c35171b07a54 (X86_64)   
ami-0720ab58a7976d46f (ARM64)  
ap-northeast-3  | ami-07b9a035e34376481 (X86_64)   
ami-0b0a3a5c6e2fe1dee (ARM64)  
ap-south-1  | ami-084a0102434a2b8ce (X86_64)   
ami-0fe9117a63f9531b1 (ARM64)  
ap-southeast-1  | ami-0650f6dfd2e1f1c7d (X86_64)   
ami-030f7d06c3f7ae991 (ARM64)  
ap-southeast-2  | ami-0ecde39013b8db0ca (X86_64)   
ami-094045b4a50ced5e3 (ARM64)  
ap-southeast-3  | ami-03dbd401bec8683a3 (X86_64)   
ami-0fce50686e5f8754c (ARM64)  
ca-central-1  | ami-0e802c992b3066d57 (X86_64)   
ami-0001847ae16a3c6ac (ARM64)  
eu-central-1  | ami-0f958c1ee2388ec77 (X86_64)   
ami-044f6eb79a1b449ff (ARM64)  
eu-north-1  | ami-0543f86ed7ee37929 (X86_64)   
ami-061b739e407e0a3b3 (ARM64)  
eu-south-1  | ami-065fcb63427fca6cd (X86_64)   
ami-0388e6b1e004ab6d1 (ARM64)  
eu-west-1  | ami-0b959b21072bb1bf7 (X86_64)   
ami-07d45acf9a967bd28 (ARM64)  
eu-west-2  | ami-0dc393a7b8e8153de (X86_64)   
ami-07a79c6f968fa2044 (ARM64)  
eu-west-3  | ami-0215893dd825dd94e (X86_64)   
ami-05a9bab003f867fc1 (ARM64)  
sa-east-1  | ami-0728d7773e1657944 (X86_64)   
ami-0ff2b112d8df5f7c2 (ARM64)  
us-east-1  | ami-0e1a9e23f5cef6b34 (X86_64)   
ami-08e978e1be40805df (ARM64)  
us-east-2  | ami-0b75f9e5c129e5242 (X86_64)   
ami-055d98701e5a510d0 (ARM64)  
us-west-1  | ami-0c87a8f77ed8585a8 (X86_64)   
ami-02a2c94a2e6498b1d (ARM64)  
us-west-2  | ami-034b226494c8bf8f0 (X86_64)   
ami-0c9c31b209efb242a (ARM64)  
  
#### 1.34.6-gke.200

Region | AMI ID  
---|---  
ap-east-1  | ami-0b3ed2667ca7e14ce (X86_64)   
ami-0e9c014b474168cb2 (ARM64)  
ap-northeast-1  | ami-07156ba1a53aca2d0 (X86_64)   
ami-02809709c9bc12daf (ARM64)  
ap-northeast-2  | ami-0c60e3183d3a23c58 (X86_64)   
ami-0aebcd61ae13ec5e9 (ARM64)  
ap-northeast-3  | ami-012aedcf01a9db7a1 (X86_64)   
ami-00f7db7b4acafc957 (ARM64)  
ap-south-1  | ami-0641ef6c785bf8b87 (X86_64)   
ami-0aec9bbd9b648b5e1 (ARM64)  
ap-southeast-1  | ami-0bd210a63ae3ac5c3 (X86_64)   
ami-00a03a9b82291be5c (ARM64)  
ap-southeast-2  | ami-095c7f83255819da5 (X86_64)   
ami-0814ca216898da640 (ARM64)  
ap-southeast-3  | ami-03c900e95fc8426dc (X86_64)   
ami-0bde7ef1876d5b811 (ARM64)  
ca-central-1  | ami-0bf852cde5226b1a7 (X86_64)   
ami-04ce723957219bbe9 (ARM64)  
eu-central-1  | ami-0ee60f419806ecb19 (X86_64)   
ami-0b9378214e8cfaa7c (ARM64)  
eu-north-1  | ami-08643f8d76c29f875 (X86_64)   
ami-0b5222b7a06c71e81 (ARM64)  
eu-south-1  | ami-018b95bfb6ed08cca (X86_64)   
ami-0bccd6ddbbe949b59 (ARM64)  
eu-west-1  | ami-038435014866b831d (X86_64)   
ami-037c650d992f8370f (ARM64)  
eu-west-2  | ami-0808900371df89649 (X86_64)   
ami-07f15b9ff047b9195 (ARM64)  
eu-west-3  | ami-0d4d1462c0f38c1e3 (X86_64)   
ami-0ab06a4d5b05ae794 (ARM64)  
sa-east-1  | ami-0dc2847f0decfb805 (X86_64)   
ami-065f0fa714ea36d9c (ARM64)  
us-east-1  | ami-0d22e1bb5879573b7 (X86_64)   
ami-0bfda2d910bf1ebbe (ARM64)  
us-east-2  | ami-081633c3a08bfeaa5 (X86_64)   
ami-0f2bacc821d20f28b (ARM64)  
us-west-1  | ami-0859185c5eebd2241 (X86_64)   
ami-0f06d8a409958b8a0 (ARM64)  
us-west-2  | ami-03c85c1c709f07fd5 (X86_64)   
ami-0e9a3364cc9c3ab6f (ARM64)  
  
### Kubernetes 1.33

#### 1.33.4-gke.900

Region | AMI ID  
---|---  
ap-east-1  | ami-0794e0b63174ff67e (X86_64)   
ami-0cbd8a064e19c8a35 (ARM64)  
ap-northeast-1  | ami-04543148ea1d7488f (X86_64)   
ami-030ae43edfb479c08 (ARM64)  
ap-northeast-2  | ami-0af67e52988cd3194 (X86_64)   
ami-0cbd1a6da73278157 (ARM64)  
ap-northeast-3  | ami-05368242a606c2533 (X86_64)   
ami-07c68e4b20fa3766a (ARM64)  
ap-south-1  | ami-03db203b6ba06c3f8 (X86_64)   
ami-081cc049e9c6d54c5 (ARM64)  
ap-southeast-1  | ami-034141bc10b1ffd7f (X86_64)   
ami-01980f04fb2f15408 (ARM64)  
ap-southeast-2  | ami-06feb4510473bb136 (X86_64)   
ami-0bdb8701c599144e4 (ARM64)  
ap-southeast-3  | ami-0f4d4362d14dcfa63 (X86_64)   
ami-0248e323e821b1a17 (ARM64)  
ca-central-1  | ami-01f1855ede13fadec (X86_64)   
ami-02c40d4446e1cdc76 (ARM64)  
eu-central-1  | ami-0c27f60facbe83181 (X86_64)   
ami-028b80ceb573b40ac (ARM64)  
eu-north-1  | ami-08cd66875f125b1dd (X86_64)   
ami-037f82a3d68aa2358 (ARM64)  
eu-south-1  | ami-0ec45153acd6da578 (X86_64)   
ami-0419c30a47e28c470 (ARM64)  
eu-west-1  | ami-009d01f25fe767f02 (X86_64)   
ami-04f4b670a031359a6 (ARM64)  
eu-west-2  | ami-0a7ef482c3b99e25b (X86_64)   
ami-01224c0ce6cb3f6b7 (ARM64)  
eu-west-3  | ami-01fb1049c5da37ebe (X86_64)   
ami-009de7f4ba04ec0b4 (ARM64)  
sa-east-1  | ami-0e8d890f462872632 (X86_64)   
ami-0bb719bcdef0906c5 (ARM64)  
us-east-1  | ami-05d4d1e67dfa32f36 (X86_64)   
ami-07f1b9d11a3909d54 (ARM64)  
us-east-2  | ami-0be1ebcf7067bc7be (X86_64)   
ami-03d316df94e93c7d1 (ARM64)  
us-west-1  | ami-0a3372013e92e9ef5 (X86_64)   
ami-0aea7fe8cca6c71d7 (ARM64)  
us-west-2  | ami-0270cabb708d1c059 (X86_64)   
ami-030f9c814ec5a5ba4 (ARM64)  
  
#### 1.33.5-gke.1900

Region | AMI ID  
---|---  
ap-east-1  | ami-0b9fec08dc0addb28 (X86_64)   
ami-0237f3c3f997a75d3 (ARM64)  
ap-northeast-1  | ami-078ba0917d44c502a (X86_64)   
ami-0a18afef41c18d73a (ARM64)  
ap-northeast-2  | ami-08bd6c35171b07a54 (X86_64)   
ami-0720ab58a7976d46f (ARM64)  
ap-northeast-3  | ami-07b9a035e34376481 (X86_64)   
ami-0b0a3a5c6e2fe1dee (ARM64)  
ap-south-1  | ami-084a0102434a2b8ce (X86_64)   
ami-0fe9117a63f9531b1 (ARM64)  
ap-southeast-1  | ami-0650f6dfd2e1f1c7d (X86_64)   
ami-030f7d06c3f7ae991 (ARM64)  
ap-southeast-2  | ami-0ecde39013b8db0ca (X86_64)   
ami-094045b4a50ced5e3 (ARM64)  
ap-southeast-3  | ami-03dbd401bec8683a3 (X86_64)   
ami-0fce50686e5f8754c (ARM64)  
ca-central-1  | ami-0e802c992b3066d57 (X86_64)   
ami-0001847ae16a3c6ac (ARM64)  
eu-central-1  | ami-0f958c1ee2388ec77 (X86_64)   
ami-044f6eb79a1b449ff (ARM64)  
eu-north-1  | ami-0543f86ed7ee37929 (X86_64)   
ami-061b739e407e0a3b3 (ARM64)  
eu-south-1  | ami-065fcb63427fca6cd (X86_64)   
ami-0388e6b1e004ab6d1 (ARM64)  
eu-west-1  | ami-0b959b21072bb1bf7 (X86_64)   
ami-07d45acf9a967bd28 (ARM64)  
eu-west-2  | ami-0dc393a7b8e8153de (X86_64)   
ami-07a79c6f968fa2044 (ARM64)  
eu-west-3  | ami-0215893dd825dd94e (X86_64)   
ami-05a9bab003f867fc1 (ARM64)  
sa-east-1  | ami-0728d7773e1657944 (X86_64)   
ami-0ff2b112d8df5f7c2 (ARM64)  
us-east-1  | ami-0e1a9e23f5cef6b34 (X86_64)   
ami-08e978e1be40805df (ARM64)  
us-east-2  | ami-0b75f9e5c129e5242 (X86_64)   
ami-055d98701e5a510d0 (ARM64)  
us-west-1  | ami-0c87a8f77ed8585a8 (X86_64)   
ami-02a2c94a2e6498b1d (ARM64)  
us-west-2  | ami-034b226494c8bf8f0 (X86_64)   
ami-0c9c31b209efb242a (ARM64)  
  
#### 1.33.10-gke.200

Region | AMI ID  
---|---  
ap-east-1  | ami-0b3ed2667ca7e14ce (X86_64)   
ami-0e9c014b474168cb2 (ARM64)  
ap-northeast-1  | ami-07156ba1a53aca2d0 (X86_64)   
ami-02809709c9bc12daf (ARM64)  
ap-northeast-2  | ami-0c60e3183d3a23c58 (X86_64)   
ami-0aebcd61ae13ec5e9 (ARM64)  
ap-northeast-3  | ami-012aedcf01a9db7a1 (X86_64)   
ami-00f7db7b4acafc957 (ARM64)  
ap-south-1  | ami-0641ef6c785bf8b87 (X86_64)   
ami-0aec9bbd9b648b5e1 (ARM64)  
ap-southeast-1  | ami-0bd210a63ae3ac5c3 (X86_64)   
ami-00a03a9b82291be5c (ARM64)  
ap-southeast-2  | ami-095c7f83255819da5 (X86_64)   
ami-0814ca216898da640 (ARM64)  
ap-southeast-3  | ami-03c900e95fc8426dc (X86_64)   
ami-0bde7ef1876d5b811 (ARM64)  
ca-central-1  | ami-0bf852cde5226b1a7 (X86_64)   
ami-04ce723957219bbe9 (ARM64)  
eu-central-1  | ami-0ee60f419806ecb19 (X86_64)   
ami-0b9378214e8cfaa7c (ARM64)  
eu-north-1  | ami-08643f8d76c29f875 (X86_64)   
ami-0b5222b7a06c71e81 (ARM64)  
eu-south-1  | ami-018b95bfb6ed08cca (X86_64)   
ami-0bccd6ddbbe949b59 (ARM64)  
eu-west-1  | ami-038435014866b831d (X86_64)   
ami-037c650d992f8370f (ARM64)  
eu-west-2  | ami-0808900371df89649 (X86_64)   
ami-07f15b9ff047b9195 (ARM64)  
eu-west-3  | ami-0d4d1462c0f38c1e3 (X86_64)   
ami-0ab06a4d5b05ae794 (ARM64)  
sa-east-1  | ami-0dc2847f0decfb805 (X86_64)   
ami-065f0fa714ea36d9c (ARM64)  
us-east-1  | ami-0d22e1bb5879573b7 (X86_64)   
ami-0bfda2d910bf1ebbe (ARM64)  
us-east-2  | ami-081633c3a08bfeaa5 (X86_64)   
ami-0f2bacc821d20f28b (ARM64)  
us-west-1  | ami-0859185c5eebd2241 (X86_64)   
ami-0f06d8a409958b8a0 (ARM64)  
us-west-2  | ami-03c85c1c709f07fd5 (X86_64)   
ami-0e9a3364cc9c3ab6f (ARM64)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
