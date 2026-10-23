---
url: https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles/
title: Configure IAM roles in ingress and egress rules \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:51.426825+00:00
---

# Configure IAM roles in ingress and egress rules  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Configure IAM roles in ingress and egress rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Identity and Access Management (IAM) roles in ingress and egress rules to allow access to resources protected by service perimeters.

VPC Service Controls uses [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to allow access to and from the resources and clients protected by service perimeters. Optionally, you can constrain your ingress and egress rules using [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles). When you specify an IAM role in a rule, the rule only allows actions associated with the permissions that are part of the IAM role.

## Before you begin

  * Verify that you have the permissions required to complete this guide.

  * Read about [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

  * If you want to use a [custom role](https://docs.cloud.google.com/iam/docs/roles-overview#custom) in the ingress and egress rules, make sure that you have the [required permissions](https://docs.cloud.google.com/iam/docs/creating-custom-roles#required-roles).




## Configure IAM roles in ingress rules

### Console

When you [update an ingress policy of a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console) or [set an ingress policy during perimeter creation](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console_1) using the Google Cloud console, you can configure the ingress rule to use IAM roles:

  1. When you create a perimeter or edit a perimeter in the Google Cloud console, select **Ingress policy**.

  2. In the **Ingress rules** pane, select an existing ingress rule or click **Add an ingress rule**.

  3. In the **To** section of your ingress policy, select **Select IAM roles** from the **Operations or IAM roles** list.

  4. Click **Add IAM roles**.

  5. In the **Add IAM roles** pane, select the IAM roles that you want to allow.

For information about supported IAM roles, see [Supported roles](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#supported-roles).

  6. Click **Add selected IAM roles**.

  7. Click **Done**.




For information about the other ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

### gcloud

You can configure an ingress rule to use IAM roles using a JSON file or a YAML file. The following sample uses the YAML format:
    
    
    - ingressFrom:
        identityType: ANY_IDENTITY | ANY_USER_ACCOUNT | ANY_SERVICE_ACCOUNT
        *OR*
        identities:
        - PRINCIPAL_IDENTIFIER
        sources:
        - resource: RESOURCE
          *OR*
        - accessLevel: ACCESS_LEVEL
      ingressTo:
        operations:
        - serviceName: SERVICE_NAME
          methodSelectors:
          - method: METHOD_NAME
        *OR*
        roles:
        - ROLE_NAME
        resources:
        - projects/PROJECT_NUMBER
    

Replace `ROLE_NAME` with the IAM roles that define the scope of access for the services specified in the rule. Specify a single role or a combination of roles that include all the permissions required to access the services. To specify a role, use the role name formats mentioned in [Role components](https://docs.cloud.google.com/iam/docs/roles-overview#components), except the following format: `projects/PROJECT_ID/roles/IDENTIFIER`.

For information about supported IAM roles, see [Supported roles](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#supported-roles).

For information about the other ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

After you update an existing ingress rule to configure IAM roles, you need to update the rule policies of the service perimeter:
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID --set-ingress-policies=RULE_POLICY.yaml
    

Replace the following:

  * `PERIMETER_ID`: the ID of the service perimeter that you want to update.
  * `RULE_POLICY`: the path of the modified ingress rule file.



For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#updating).

## Configure IAM roles in egress rules

### Console

When you [update an egress policy of a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console) or [set an egress policy during perimeter creation](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console_1) using the Google Cloud console, you can configure the egress rule to use IAM roles:

  1. When you create a perimeter or edit a perimeter in the Google Cloud console, select **Egress policy**.

  2. In the **Egress rules** pane, select an existing egress rule or click **Add an egress rule**.

  3. In the **To** section of your egress policy, select **Select IAM roles** from the **Operations or IAM roles** list.

  4. Click **Add IAM roles**.

  5. In the **Add IAM roles** pane, select the IAM roles that you want to allow.

For information about supported IAM roles, see [Supported roles](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#supported-roles).

  6. Click **Add selected IAM roles**.

  7. Click **Done**.




For information about the other egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

### gcloud

You can configure an egress rule to use IAM roles using a JSON file or a YAML file. The following sample uses the YAML format:
    
    
    - egressTo:
        operations:
        - serviceName: SERVICE_NAME
          methodSelectors:
          - method: METHOD_NAME
        *OR*
        roles:
        - ROLE_NAME
        resources:
        - projects/PROJECT_NUMBER
      egressFrom:
        identityType: ANY_IDENTITY | ANY_USER_ACCOUNT | ANY_SERVICE_ACCOUNT
        *OR*
        identities:
        - PRINCIPAL_IDENTIFIER
        sources:
        - resource: RESOURCE
          *OR*
        - accessLevel: ACCESS_LEVEL
        sourceRestriction: RESTRICTION_STATUS
    

Replace `ROLE_NAME` with the IAM roles that define the scope of access for the services specified in the rule. Specify a single role or a combination of roles that include all the permissions required to access the services. To specify a role, use the role name formats mentioned in [Role components](https://docs.cloud.google.com/iam/docs/roles-overview#components), except the following format: `projects/PROJECT_ID/roles/IDENTIFIER`.

For information about supported IAM roles, see [Supported roles](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#supported-roles).

For information about the other egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

After you update an existing egress rule to configure IAM roles, you need to update the rule policies of the service perimeter:
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID --set-egress-policies=RULE_POLICY.yaml
    

Replace the following:

  * `PERIMETER_ID`: the ID of the service perimeter that you want to update.
  * `RULE_POLICY`: the path of the modified egress rule file.



For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#updating).

## Supported roles

When you configure ingress and egress rules, use only IAM roles that contain supported permissions. This requirement applies to both [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) and [custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom). VPC Service Controls categorizes the support status of IAM roles based on their underlying permissions:

  * **Supported:** All permissions in the role are supported.

  * **Partially supported:** Only some permissions in the role are supported.

  * **Unsupported:** No permissions in the role are supported.




To identify the support status of an IAM role and the associated supported permissions, see [Get the support status of an IAM role](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#check-role).

### Considerations

Review the following considerations before using an IAM role in ingress or egress rules:

  * Using a partially supported IAM role in ingress or egress rules makes those rules ineffective for requests or actions specific to the underlying unsupported [permissions](https://docs.cloud.google.com/iam/docs/roles-permissions).

To get the list of supported permissions, see [List supported permissions](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#list-permissions).

  * Using an unsupported IAM role in ingress or egress rules makes those rules ineffective.

  * You can't use custom roles that you have created at the project level. In other words, you can't use a custom role that is in the following format: `projects/PROJECT_ID/roles/IDENTIFIER`.




### Required roles

To get the permission that you need to run the `supported-permissions describe` command, ask your administrator to grant you the [Role Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) (`roles/iam.roleViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `iam.roles.get` permission, which is required to run the `supported-permissions describe` command. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Get the support status of an IAM role

To check the support status of an IAM role and retrieve the list of permissions supported by VPC Service Controls in the IAM role, run the following command:
    
    
    gcloud access-context-manager supported-permissions describe ROLE_NAME
    

Replace `ROLE_NAME` with the name of an IAM role. For example, `roles/bigquery.dataViewer`.

You get a response with the support status and a list of supported permissions.

This response includes the following values:

Value | Description  
---|---  
`ROLE_NAME` | The name of the IAM role. For example, `roles/bigquery.dataViewer`.   
`SUPPORT_STATUS` | The support status for the IAM role in ingress and egress rules. The following are the possible values:  


  * `SUPPORTED`: All underlying permissions in the IAM role are supported in ingress and egress rules.
  * `PARTIALLY_SUPPORTED`: Some underlying permissions in the IAM role aren't supported in ingress and egress rules.
  * `NOT_SUPPORTED`: All underlying permissions in the IAM role aren't supported in ingress and egress rules.

  
`LIST_OF_SUPPORTED_PERMISSIONS` | A list of all permissions supported by VPC Service Controls for the specified IAM role. For example, `bigquery.datasets.get`.   
  
### List supported permissions

To retrieve the complete list of all permissions supported by VPC Service Controls, run the following command:
    
    
    gcloud access-context-manager supported-permissions list
    

You get a response with a list of permissions.
    
    
    PERMISSION
    PERMISSIONS_LIST
    .
    .
    .
    

In this response, `PERMISSIONS_LIST` contains all permissions supported by VPC Service Controls in ingress and egress rules.

## Supported products

VPC Service Controls supports IAM roles of the following Google Cloud services in ingress and egress rules.

The support status of these IAM roles can vary as explained in [Supported roles](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#supported-roles). To identify the support status of an IAM role and the associated supported permissions, see [Get the support status of an IAM role](https://docs.cloud.google.com/vpc-service-controls/docs/configure-iam-roles#check-role).

Product | Service name  
---|---  
Artifact Registry | `artifactregistry.googleapis.com`  
BigQuery | `bigquery.googleapis.com`  
BigQuery Data Transfer Service | `bigquerydatatransfer.googleapis.com`  
Bigtable | `bigtable.googleapis.com`  
Binary Authorization | `binaryauthorization.googleapis.com`  
Managed Service for Apache Airflow | `composer.googleapis.com`  
Cloud Key Management Service | `cloudkms.googleapis.com`  
Cloud Logging | `logging.googleapis.com`  
Cloud Monitoring | `monitoring.googleapis.com`  
Cloud Run | `run.googleapis.com`  
Cloud Run functions | `cloudfunctions.googleapis.com`  
Cloud SQL | `sqladmin.googleapis.com`  
Cloud Storage ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `storage.googleapis.com`  
Compute Engine | `compute.googleapis.com`  
Dataflow | `dataflow.googleapis.com`  
Managed Service for Apache Spark | `dataproc.googleapis.com`  
Google Kubernetes Engine | `container.googleapis.com`  
Identity and Access Management | `iam.googleapis.com`  
Pub/Sub | `pubsub.googleapis.com`  
Resource Manager | `cloudresourcemanager.googleapis.com`  
Secret Manager | `secretmanager.googleapis.com`  
Spanner | `spanner.googleapis.com`  
AI Platform | `aiplatform.googleapis.com`  
BigQuery sharing | `analyticshub.googleapis.com`  
Apigee Connect | `apigeeconnect.googleapis.com`  
API keys | `apikeys.googleapis.com`  
Batch | `batch.googleapis.com`  
BigQuery Data Policy | `bigquerydatapolicy.googleapis.com`  
BigQuery Migration Service | `bigquerymigration.googleapis.com`  
Gemini Code Assist | `cloudaicompanion.googleapis.com`  
Cloud Asset Inventory | `cloudasset.googleapis.com`  
Cloud Build | `cloudbuild.googleapis.com`  
Cloud Quotas | `cloudquotas.googleapis.com`  
Cloud Trace | `cloudtrace.googleapis.com`  
Customer Experience Insights | `contactcenterinsights.googleapis.com`  
Artifact Analysis | `containeranalysis.googleapis.com`  
Container Security API | `containersecurity.googleapis.com`  
Cloud Data Fusion | `datafusion.googleapis.com`  
Data Lineage API | `datalineage.googleapis.com`  
Dataflow Data Pipelines | `datapipelines.googleapis.com`  
Knowledge Catalog | `dataplex.googleapis.com`  
Developer Connect | `developerconnect.googleapis.com`  
Discovery Engine | `discoveryengine.googleapis.com`  
Sensitive Data Protection | `dlp.googleapis.com`  
Cloud DNS | `dns.googleapis.com`  
Document AI | `documentai.googleapis.com`  
Firebase App Check | `firebaseappcheck.googleapis.com`  
Firebase Data Connect | `firebasedataconnect.googleapis.com`  
Firestore | `firestore.googleapis.com`  
Fleets | `gkehub.googleapis.com`  
GKE Multi-Cloud | `gkemulticloud.googleapis.com`  
Cloud Healthcare API | `healthcare.googleapis.com`  
Identity-Aware Proxy | `iap.googleapis.com`  
Identity Platform | `identitytoolkit.googleapis.com`  
Cloud KMS Inventory API | `kmsinventory.googleapis.com`  
Kubernetes Metadata API | `kubernetesmetadata.googleapis.com`  
Google Cloud NetApp Volumes | `netapp.googleapis.com`  
Connectivity Tests | `networkmanagement.googleapis.com`  
Network Services API | `networkservices.googleapis.com`  
Organization Policy Service | `orgpolicy.googleapis.com`  
VM Manager | `osconfig.googleapis.com`  
Certificate Authority Service | `privateca.googleapis.com`  
Public Certificate Authority | `publicca.googleapis.com`  
Pub/Sub Lite | `pubsublite.googleapis.com`  
Recommender | `recommender.googleapis.com`  
Memorystore for Redis | `redis.googleapis.com`  
AI Commerce Search API | `retail.googleapis.com`  
Security Command Center | `securitycenter.googleapis.com`  
Service Control | `servicecontrol.googleapis.com`  
Service Directory | `servicedirectory.googleapis.com`  
Service Usage | `serviceusage.googleapis.com`  
Speech-to-Text | `speech.googleapis.com`  
Storage Transfer Service | `storagetransfer.googleapis.com`  
Telemetry API | `telemetry.googleapis.com`  
Traffic Director API | `trafficdirector.googleapis.com`  
Serverless VPC Access | `vpcaccess.googleapis.com`  
Workflow executions | `workflowexecutions.googleapis.com`  
  
Support for Cloud Storage IAM roles in ingress and egress rules is available in [Preview](https://cloud.google.com/products/#product-launch-stages) and VPC Service Controls supports only custom roles for Cloud Storage.

## Limitations

  * When you use IAM roles in ingress or egress rules, violation errors might appear as insufficient IAM permissions. If you already have the required IAM permissions, check the [VPC Service Controls audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) to identify the reason for the violation.

  * You can't use a role-based ingress or egress rule to allow requests to [set the IAM allow policy of a project](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/setIamPolicy) across the perimeter boundary.

To overcome this limitation, do the following:

    1. Check the [ VPC Service Controls audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) to find the underlying method causing the violation. 
    2. Determine whether this method is [supported for service method restrictions](https://docs.cloud.google.com/vpc-service-controls/docs/supported-method-restrictions). 
    3. If the method is supported, you can [create an ingress or egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) to allow access to this method using the `methodSelectors ` attribute. 
  * If VPC Service Controls prevents you from loading the editing page of a service in the Google Cloud console, check the [VPC Service Controls audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging). If the logs show that VPC Service Controls blocked the `TestIamPermissions` method, using IAM roles in ingress rules might not resolve the issue. This limitation doesn't affect the view-only page for these services.

  * When a request involves multiple resource types from different projects, the ingress or egress rule that uses IAM roles might not work. For example, when you launch a Dataflow template that reads text from Cloud Storage in a different project.

To overcome this limitation, do the following:

    1. Check the [ VPC Service Controls audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) to find the underlying method causing the violation. 
    2. Determine whether this method is [supported for service method restrictions](https://docs.cloud.google.com/vpc-service-controls/docs/supported-method-restrictions). 
    3. If the method is supported, you can [create an ingress or egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) to allow access to this method using the `methodSelectors ` attribute. 
  * If you delete a custom role after you reference the role in the ingress or egress rule of two or more perimeters of an access policy, all perimeters under this access policy become uneditable, and you might encounter a `Custom role in Ingress/Egress rules does not exist: CUSTOM_ROLE_NAME` error. To overcome this issue, remove all occurrences of the deleted custom role from the rules by [bulk replacing all impacted perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/bulk-operations#bulk_replace_service_perimeters).

  * Cloud Key Management Service (`cloudkms.googleapis.com`)

    * If you use the [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) feature of Cloud KMS, you can't use Cloud KMS roles in ingress and egress rules to allow Cloud KMS requests, such as creating keys, encrypting and decrypting data, across the perimeter boundary.
  * Cloud Storage (`storage.googleapis.com`)

    * VPC Service Controls supports [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) for Cloud Storage in ingress and egress rules, but doesn't support the [predefined Cloud Storage roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles). If you attempt to use a predefined Cloud Storage role in an ingress or egress rule, VPC Service Controls returns an `INVALID_ARGUMENT` error.

    * When you make any of the following API requests to Cloud Storage objects in projects protected by VPC Service Controls, you must configure ingress and egress rules allowing the `storage.objects.delete` and `storage.objects.create` permissions.

      * [bulkRestore](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/bulkRestore)

      * [compose](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose)

      * [copy](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/copy)

      * [delete](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/delete)

      * [insert](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert)

      * [move](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/move)

      * [restore](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/restore)

      * [rewrite](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite)




## What's next

  * [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).
  * Watch a video to [learn about integrating IAM roles into ingress and egress rules](https://youtu.be/fNkByC_zPoM). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
