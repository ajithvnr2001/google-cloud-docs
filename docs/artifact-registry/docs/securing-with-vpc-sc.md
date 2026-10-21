---
url: https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc/
title: Protect repositories in a service perimeter \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:26.845137+00:00
---

# Protect repositories in a service perimeter  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Protect repositories in a service perimeter Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) improves your ability to mitigate the risk of unauthorized copying or transfer of data from Google Cloud-managed services.

With VPC Service Controls, you can configure security perimeters around the resources of your Google Cloud-managed services and control the movement of data across the perimeter boundary.

## Using Artifact Registry with VPC Service Controls

If you are using Artifact Registry and Google Kubernetes Engine private clusters in a project within a service perimeter, you can access container images inside the service perimeter as well as [Google Cloud-provided images](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#artifacts).

Cached Docker Hub images stored on `mirror.gcr.io` are not included in the service perimeter unless an egress rule is added to allow egress to the Artifact Registry Docker cache that hosts `mirror.gcr.io`. 

To use `mirror.gcr.io` within a service perimeter, add the following egress rule:
    
    
    - egressTo:
        operations:
        - serviceName: artifactregistry.googleapis.com
          methodSelectors:
          - method: artifactregistry.googleapis.com/DockerRead
        resources:
        - projects/342927644502
      egressFrom:
        identityType: ANY_IDENTITY
    
    

To learn about ingress and egress rules, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

You can access Artifact Registry using the [IP addresses for the default Google APIs and services domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults), or using these special IP addresses:

  * `199.36.153.4/30` (`restricted.googleapis.com`)
  * `199.36.153.8/30` (`private.googleapis.com`)



For details about these options, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config). For an example configuration that uses `199.36.153.4/30` (`restricted.googleapis.com`), see the documentation for [registry access with a virtual IP](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-gke).

Ensure that Google Cloud services that need to access Artifact Registry are also in the service perimeter, including Binary Authorization, Artifact Analysis, and runtime environments such as Google Kubernetes Engine and Cloud Run. See the list of [supported services](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) for details about each service. 

For general instructions to add Artifact Registry to a service perimeter, see [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

### Access images in `gcr.io` repositories

To access images in Artifact Registry `gcr.io` repositories, when setting ingress or egress policies, use the identity type **ANY_IDENTITY**. You can't use the identity types **ANY_SERVICE_ACCOUNT** or **ANY_USER_ACCOUNT** for images in the `gcr.io` domain.

## Using Artifact Analysis with VPC Service Controls

To learn how to add Artifact Analysis to your perimeter, see the [securing Artifact Analysis in a service perimeter](https://docs.cloud.google.com/artifact-analysis/docs/aa-vpc-sc-service-perimeter).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
