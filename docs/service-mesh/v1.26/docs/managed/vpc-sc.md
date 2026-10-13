---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/managed/vpc-sc/
title: VPC Service Controls for Cloud Service Mesh (Managed) \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:40.104183+00:00
---

# VPC Service Controls for Cloud Service Mesh (Managed)  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/managed/vpc-sc/

You are viewing archived v1.26 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  VPC Service Controls for Cloud Service Mesh (Managed)

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview).

Cloud Service Mesh (Managed) supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) as a generally available (GA) feature for new control planes.

To check whether your control plane supports VPC Service Controls GA, check the mesh feature state of your membership for the VPCSC_GA_SUPPORTED condition.
    
    
    gcloud container fleet mesh describe --project FLEET_PROJECT_ID

The output is similar to:
    
    
    (...)
    membershipStates:
      projects/FLEET_PROJECT_NUMBER/locations/MEMBERSHIP_LOCATION/memberships/MEMBERSHIP_ID:
        servicemesh:
          conditions:
          - code: VPCSC_GA_SUPPORTED
            details: This control plane supports VPC Service Controls GA.
            documentationLink: http://cloud.google.com/service-mesh/v1.26/docs/managed/VPC Service Controls
            severity: INFO
    (...)

If you have an existing control plane that does not report the VPCSC_GA_SUPPORTED condition and want to rely on VPC Service Controls, contact support.

## Before you begin

The VPC Service Controls org-policy and service perimeter are configured at the [organization level](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). Ensure that you have been granted the [proper roles for administering VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).

## Set up your VPC Service Controls service perimeter

Create or update your [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters):

  1. [Add your cluster project(s) and fleet project](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) to the service perimeter. Having a service mesh spread across multiple VPC Service Controls perimeters is not supported.

  2. Add restricted services to the service perimeter.

You must add specific services to the allowed and restricted services lists in the service perimeter, so that your Cloud Service Mesh cluster can access them. Access to these services is also restricted within your cluster's Virtual Private Cloud (VPC) network.

Not adding these services may cause the Cloud Service Mesh installation to fail or to not function properly. For example, if you don't add the **Mesh Configuration API** to the service perimeter, the installation will fail and the workloads won't receive their Envoy configuration from the managed control plane.

### Console

     1. Follow the steps in [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) to edit the perimeter.
     2. Click the **Edit VPC Service Perimeter** page.
     3. Under **Restricted Services** , **Services to protect** , click **Add Services**.
     4. On the **Specify services to restrict** dialog, click **Filter services** , and enter **Mesh Configuration API**.
     5. Select the service's checkbox.
     6. Click **Add Mesh Configuration API**.
     7. Repeat steps c - f, to add: 
        * **Cloud Service Mesh Certificate Authority API**
        * **GKE Hub API**
        * **Cloud IAM API**
        * **Cloud Monitoring API**
        * **Cloud Trace API**
        * **Cloud Monitoring API**
        * **Google Cloud Resource Manager API**
        * **Google Compute Engine API**
        * **Google Container Registry API**
        * **Artifact Registry API**
        * **Google Cloud Storage API**
        * **Cloud Logging API**
        * **Security Token Service API**
     8. Click **Save**.

### gcloud

To update the list of restricted services, use the `update` command and specify the services to add as a comma-delimited list:
    
    gcloud access-context-manager perimeters update PERIMETER_NAME \
      --add-restricted-services=meshconfig.googleapis.com,meshca.googleapis.com,gkehub.googleapis.com,iam.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com,monitoring.googleapis.com,cloudresourcemanager.googleapis.com,compute.googleapis.com,containerregistry.googleapis.com,artifactregistry.googleapis.com,storage.googleapis.com,logging.googleapis.com,sts.googleapis.com \
      --policy=POLICY_NAME

Where:

     * PERIMETER_NAME is the name of the service perimeter that you want to update.

     * POLICY_NAME is the numeric name of your organization's access policy. For example, `330193482019`.

  3. Click on **VPC Accessible services** and set it to 'All restricted services', so that services restricted at the step above are still accessible from within the VPC Service Controls perimeter.

  4. Unless you are installing Cloud Service Mesh from an in-perimeter network, add an ingress rule to allow the identity running the `asmcli` command access to the service perimeter.

For more information, see [Updating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).




## Install the managed Cloud Service Mesh in a VPC Service Controls perimeter

Follow the steps in [Configure managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/managed/provision-managed-anthos-service-mesh) page. Then, [verify the control plane has been successfully provisioned](https://docs.cloud.google.com/service-mesh/v1.26/docs/managed/provision-managed-anthos-service-mesh#verify_the_control_plane_has_been_provisioned) and there are no VPC Service Controls related errors.

## Troubleshooting

### Cannot create cluster with the latest GKE 1.22 image

There is a known issue preventing the creation of a cluster with the latest 1.22 image in a VPC Service Controls restricted environment. The workaround is to create this cluster first with the default GKE channel image, and then upgrade the image:
    
    
    gcloud container clusters create CLUSTER \
      --region REGION \
      --release-channel=rapid \
      --workload-pool=PROJECT_ID.svc.id.goog \
      --project PROJECT_ID
    
    
    gcloud container clusters upgrade CLUSTER \
      --region REGION \
      --master --cluster-version 1.22 \
      --project PROJECT_ID

### Containers are not able to download their images.

This may happen if the images are located outside of the service perimeter. Either move the images to a bucket located inside the perimeter, or update the perimeter to add an Egress rule. Typically, the Egress rule may allow selected identities to access the **Container Registry API** , **Artifact Registry API** , and **Cloud Storage API**.

### The Status field of the `ControlPlaneRevision` CRD displays VPC Service Controls errors

Run this command to get more info about the error:
    
    
    gcloud logging read --project=PROJECT_ID \
    'protoPayload.metadata.@type=type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata'

Where:

  * PROJECT_ID is the project ID of the project encountering errors.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
