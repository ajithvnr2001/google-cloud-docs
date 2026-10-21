---
url: https://docs.cloud.google.com/vpc-service-controls/docs/troubleshoot-services-within-perimeter/
title: Troubleshoot common VPC Service Controls issues with Google Cloud services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:22.884220+00:00
---

# Troubleshoot common VPC Service Controls issues with Google Cloud services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/troubleshoot-services-within-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Troubleshoot common VPC Service Controls issues with Google Cloud services Stay organized with collections  Save and categorize content based on your preferences. 

This page provides solutions to issues that you might encounter when using a Google Cloud service that is within a VPC Service Controls perimeter.

## Memorystore for Redis issues

If a customer-managed encryption key (CMEK) protects your Memorystore for Redis instance, then you might encounter ingress errors in the logs from the following service agents that belong to the internal Google-managed tenant project:

  * `service-TENANT_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`
  * `service-TENANT_PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`



The TENANT_PROJECT_NUMBER refers to the internal tenant project number, not your customer project number.

To resolve this issue, add an ingress rule to the service perimeter that protects the Cloud Key Management Service (Cloud KMS) key. This rule must let the service agents access the `cloudkms.googleapis.com` service. For more information about ingress rules, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

## Cloud Build issues

Using Cloud Build resources within a VPC Service Controls perimeter has some known limitations. For more information, see [Limitations of using VPC Service Controls with Cloud Build](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_build).

### Cloud Build service account blocked from accessing protected resources

Cloud Build uses the Cloud Build service account to execute builds on your behalf. By default, when you run a build on Cloud Build, the build runs in a [tenant project](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant) outside of your project.

The worker VMs of Cloud Build that generate build outputs are outside of the VPC Service Controls perimeter, even if your project is inside the perimeter. Therefore, for your builds to access resources within the perimeter, you must grant the Cloud Build service account access to the VPC Service Controls perimeter by either adding it to the [access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) or [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

For more information, see [Granting the Cloud Build service account access to the VPC Service Controls perimeter](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls#grant-build-access).

## Cloud Storage issues

### Denials when targeting a non-existent logging Cloud Storage bucket

If the specified logging bucket doesn't exist, VPC Service Controls denies access with the `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violation reason.

You can review the log of the access denial using the VPC Service Controls Unique Identifier (`vpcServiceControlUniqueIdentifier`). The following is a sample log with the `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violation reason:
    
    
    "serviceName": "storage.googleapis.com",
    "methodName": "google.storage.buckets.update",
    "resourceName": "projects/325183452875",
    "metadata": {
      "violationReason": "RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER",
      ...
      "egressViolations": [
        {
          "sourceType": "Resource",
          "targetResource": "projects/0/buckets/this-bucket-does-not-exist",
          "source": "projects/325183452875/buckets/bucket-in-same-project",
          "servicePerimeter": "accessPolicies/875573620132/servicePerimeters/prod_perimeter"
        }]}
    

If the `targetResource` field in the `egressViolations` object shows a target with `projects/0/buckets`, then this always triggers a denial as `projects/0` doesn't exist and it is considered outside the service perimeter.

### Denials when accessing Google-owned public Cloud Storage buckets

A service perimeter cannot contain projects from different organizations. A perimeter can only contain projects from its parent organization. There are certain limitations when you want to access Cloud Storage buckets from projects within a VPC Service Controls perimeter that resides in a different organization.

A typical example is when you want to access Google-owned Cloud Storage buckets. Since your project and the Google-owned project that contains the target bucket aren't in the same perimeter, VPC Service Controls denies the request with the `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violation reason.

To resolve this issue, you can create ingress and egress rules.

### Accessing a publicly accessible Cloud Storage bucket from within a perimeter

If you are trying to access a publicly accessible Cloud Storage bucket from within a service perimeter, VPC Service Controls might block your requests by throwing an egress violation.

In order to ensure consistent successful access to the object as needed, we should apply an egress rule to the affected service perimeter.

## Security Command Center issues

This section lists the issues you might encounter while using Security Command Center resources that are inside a VPC Service Controls perimeter.

### Security Command Center blocked from sending notification to Pub/Sub

Trying to publish Security Command Center notifications to a Pub/Sub topic inside a VPC Service Controls perimeter fails with a `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violation.

We recommend activating Security Command Center at the organization-level. VPC Service Controls doesn't consider a parent organization as part of its child projects' perimeter. For this to work, you must grant perimeter access to Security Command Center.

As a workaround, you can do either of the following:

  * Use a Pub/Sub topic in a project that isn't in a service perimeter.
  * Remove the Pub/Sub API from the service perimeter until the notification setup is complete.



For more information about enabling Security Command Center notifications that are sent to a Pub/Sub topic, see [Enabling finding notifications for Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).

### Security Command Center blocked from scanning Compute Engine resources inside a perimeter

Security Command Center scans Compute Engine resources in your projects using the per-product, per-project service account (P4SA) `service-{project_number}@gcp-sa-computescanning.iam.gserviceaccount.com`. In order for Security Command Center to be able to access resources inside the perimeter, the P4SA needs to be added into your access level or ingress rule. Otherwise, you might see a `NO_MATCHING_ACCESS_LEVEL` error.

### Security Command Center blocked from scanning resources inside a service perimeter

Security Health Analytics scans resources in your projects using the P4SA (per-product, per-project service account) `service-org-`ORGANIZATION_ID`@security-center-api.iam.gserviceaccount.com`. In order for Security Command Center to be able to access resources inside the perimeter, the P4SA account needs to be added into your access level or ingress rule. Otherwise, you will see the `NO_MATCHING_ACCESS_LEVEL` error.

## Google Kubernetes Engine issues

This section lists the issues you might encounter while using Google Kubernetes Engine resources that are inside a VPC Service Controls perimeter.

### Autoscaler not working in perimeters with accessible services and restricted services enabled

The `autoscaling.googleapis.com` isn't integrated with VPC Service Controls, therefore it cannot be added to the restricted services neither to the accessible services. It isn't possible to allow the `autoscaling.googleapis.com` API in the accessible services. Therefore, the [autoscaler of clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) that exist in a perimeter with accessible services enabled might not work.

We suggest against using accessible services. When using restricted Virtual IP (VIP), make an exception for `autoscaling.googleapis.com` to go to Private VIP in a perimeter that contains a cluster with autoscaling.

## BigQuery issues

This section lists the issues you might encounter while using BigQuery resources that are inside a VPC Service Controls perimeter.

### VPC Service Controls perimeter restrictions don't apply to BigQuery query result export

If you are trying to restrict the export of protected data from BigQuery to Google Drive, Google Sheets, or Data Studio, you might see some deviation from expected behavior. When you run a query from the BigQuery UI, the results are stored in your machine's local memory, such as the browser cache. This means that the results are now outside VPC Service Controls, so you can possibly save the results to a CSV file or to Google Drive.

In this scenario, VPC Service Controls is working as intended since the result is being exported from local machine which is outside the service perimeter, but the overall restriction of BigQuery data is being circumvented.

To overcome this issue, restrict IAM permissions for users by removing the `bigquery.tables.export` permission. Note that doing this disables all the export options.

## GKE Enterprise issues

This section lists the issues you might encounter while using GKE Enterprise resources that are inside a VPC Service Controls perimeter.

To troubleshoot errors related to the use of VPC Service Controls with Cloud Service Mesh, see [Troubleshoot VPC Service Controls issues for managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc#troubleshooting).

### GKE Enterprise Config Controller setup generates an egress violation

The process of setting up GKE Enterprise Config Controller is expected to fail if there is no egress configuration that allows to reach `containerregistry.googleapis.com` with the method `google.containers.registry.read` in a project outside the perimeter.

To resolve this error, create the following egress rule:
    
    
    From:
      Identities:ANY_IDENTITY
    To:
      Projects =
        NNNNNNNNNNNN
      Service =
      Service name: containerregistry.googleapis.com
      Service methods:
        containers.registry.read
    

The egress violation disappears after you have added the rule to the violated perimeter.

## Container Registry issues

This section lists the issues you might encounter while using Container Registry resources that are inside a VPC Service Controls perimeter.

### Container Registry API requests blocked by VPC Service Controls despite being allowed in an ingress or egress rule

If you have allowed access to Container Registry using ingress rules with the `identity_type` field set to `ANY_USER_ACCOUNT` or `ANY_SERVICE_ACCOUNT`, access is blocked by VPC Service Controls.

To resolve this issue, update the `identity_type` field to `ANY_IDENTITY` in the ingress or egress rule.

### Egress errors from a service agent while copying Artifact Registry-owned Docker image to a project in a perimeter

When you try to copy an Artifact Registry-owned image to your project that is within a VPC Service Controls perimeter, you might encounter egress errors in the logs from the service agent `cloud-cicd-artifact-registry-copier@system.gserviceaccount.com`. This egress error usually occurs when the perimeter policy is in the dry-run mode.

You can resolve this issue by creating an egress rule that allows the service agent `cloud-cicd-artifact-registry-copier@system.gserviceaccount.com` access to the `storage.googleapis.com` service in the project mentioned in the VPC Service Controls error logs.

## Gemini Enterprise Agent Platform issues

This section lists the issues you might encounter while using Gemini Enterprise Agent Platform resources that are inside a VPC Service Controls perimeter.

### User-managed notebooks API requests blocked by VPC Service Controls despite being allowed in an ingress or egress rule

If you have allowed access to [User-managed notebooks API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/reference/rest) using an [ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) and you have set the `identity_type` as `ANY_USER_ACCOUNT` or `ANY_SERVICE_ACCOUNT`, VPC Service Controls blocks access to the API.

To resolve this issue, update the `identity_type` field to `ANY_IDENTITY` in the ingress or egress rule.

## Spanner issues

Spanner database backup is blocked by the `NO_MATCHING_ACCESS_LEVEL` violation from the per-product, per-project service account (P4SA) `service-`PROJECT_NUMBER`@gcf-admin-robot.iam.gserviceaccount.com`.

To resolve this issue, add an ingress rule with the aforementioned service agent or add it to an access level.

## AlloyDB for PostgreSQL issues

If your AlloyDB for PostgreSQL cluster is protected by a CMEK, you might encounter ingress errors in the logs from service agents `service-`PROJECT_NUMBER`@compute-system.iam.gserviceaccount.com` and `service-`PROJECT_NUMBER`@gs-project-accounts.iam.gserviceaccount.com`.

To resolve this issue, add an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) with the aforementioned service agents access to the `cloudkms.googleapis.com` service in the project mentioned in the VPC Service Controls error logs.

## What's next

  * Learn about the [known limitations of using VPC Service Controls with various Google Cloud services](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#service-limitations).
  * Learn how [VPC Service Controls unique identifier helps troubleshoot issues related to service perimeters](https://cloud.google.com/blog/products/identity-security/unique-identifier-helps-troubleshooting-vpc-service-controls-perimeter).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
