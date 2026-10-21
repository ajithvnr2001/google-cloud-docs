---
url: https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting/
title: Troubleshoot common issues \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:22.186130+00:00
---

# Troubleshoot common issues  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Troubleshoot common issues Stay organized with collections  Save and categorize content based on your preferences. 

This page lists various issues that you might encounter when configuring VPC Service Controls.

## Unexpected scoped policy behavior

You might notice some unexpected VPC Service Controls violations that your scoped policy should allow. It is a known issue that if you don't have an organization-level access policy, then you might experience some unexpected issues with your scoped access policies.

To overcome this issue, create an access policy at the organization level using the following command:
    
    
    gcloud access-context-manager policies create --organization <var>ORGANIZATION_ID</var> --title <var>POLICY_TITLE</var>
    

Replace the following:

  * ORGANIZATION_ID: The organization ID.
  * POLICY_TITLE: A human-readable title for your access policy.



For more information, see [Create an access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy).

## Shared VPC

When using Shared VPC, a service perimeter that includes projects that belong to a Shared VPC network must also include the project that _hosts_ the network. When projects that belong to a Shared VPC network are not in the same perimeter as the host project, services might not work as expected or might be blocked entirely.

Ensure that the Shared VPC network host is in the same service perimeter as the projects connected to the network.

## Unable to add a VPC network

The following error can occur when you try to add a VPC network to a service perimeter:
    
    
    ERROR: (gcloud.access-context-manager.perimeters.update) PERMISSION_DENIED: Permission 'compute.networks.get' denied on resource '//compute.googleapis.com/projects/PROJECT_NAME/global/networks/VPC_NETWORK_NAME' (or it may not exist)
    

This error occurs due to one of the following reasons:

  * The VPC network doesn't exist.
  * The VPC network exists, but doesn't have a subnet.
  * The caller doesn't have the required permission.



To resolve this issue, complete the following steps:

  1. Verify if the VPC network specified in the error message exists by [viewing the networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#viewing-networks) in your project.

     * Before verifying the VPC network, make sure that the Compute Engine API is enabled in the project associated with the API call by completing the following steps:

       1. In the Google Cloud console, go to the **APIs & Services** page.  
[Go to APIs & Services](https://console.cloud.google.com/apis/dashboard)

       2. On the **APIs & Services** page, verify if the Compute Engine API is listed.

       3. If the Compute Engine API is missing, enable the API.  
[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  2. Verify if at least one subnet exists in the VPC network by [viewing the subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#listing_existing_subnets). If there are no subnets, [add a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) to the VPC network.

  3. Check if the caller has the following permission on the host project of the VPC network: `compute.networks.get`. This permission lets you view VPC networks in a project.

     * Ask the administrator of the organization that owns the host project of the VPC network to grant the caller an IAM role with the `compute.networks.get` permission on the host project. For example, the Compute Network Viewer role.

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




Ensure that you read the [limitations](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management#limitations) associated with using VPC networks in service perimeters.

## Requests between perimeters

Normally, access levels are used to allow requests from _outside_ a service perimeter for protected resources _inside_ a perimeter.

However, a request from a project in a perimeter for a protected resource in _another_ perimeter is denied, even if an access level normally allows the request.

For example, assume Project A in Perimeter 1 requests a resource from Project B. The resource in Project B is protected by Perimeter 2. Because Project A is in a perimeter, even if an access level for Perimeter 2 normally permits the request for the protected resource, the request is denied.

Use one of the following approaches to facilitate requests between perimeters:

  * Use [egress policy and ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies). To allow requests from _another_ perimeter to protected resources in your perimeter, the other perimeter must use an egress policy and you must set an ingress policy in your perimeter.

  * [Use perimeter bridges](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters). Bridges allow two or more projects in different perimeters to make requests to any services in those projects. These requests are permitted even if the services are protected by the respective perimeters.

  * Ensure that both the requesting service and the target resource are unprotected by the perimeters. In this scenario, the operation succeeds because the services are not protected.




## The email address is invalid or non-existent

When updating a perimeter that contains a deleted principal, you might encounter the `The email address is invalid or non-existent` error.

**Note:** You can enable support for deleted IAM principal syntax in ingress and egress rules. Doing so lets you retrieve and update perimeters that contain deleted principals, such as deleted users, service accounts, or groups, without encountering this error. This capability is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities#deleted-principals).

To fix this issue, you must remove the _invalid_ email address from all perimeters. Alternatively, you can use a bulk replace operation to remove the deleted principals:

  1. [Export all your perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/bulk-operations#get_a_list_of_service_perimeters). The following sample command exports a list of service perimeters in JSON format:
         
         gcloud access-context-manager perimeters list \
             --policy=POLICY_NAME \
             --format="json(name,title,description,perimeterType,status,\
         spec,useExplicitDryRunSpec)" \
             > my-perimeters.json

  2. Remove the _invalid_ email address from the `my-perimeters.json` file and save it as `my-perimeters-updated.json`.

  3. [Bulk replace all your perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/bulk-operations#bulk_replace_service_perimeters).




## Ingress and egress rules violations

The audit log contains information about the ingress and egress rules violations that help you understand perimeter violations.

### Ingress rule violation

An ingress rule violation indicates that an API client outside of the perimeter tried to access a resource inside the perimeter. The service perimeter rejects the request as there are no matching ingress rules or access levels.

An ingress rule violation in the audit log contains the following details:

  * The name of the perimeter in which the ingress rule violation occurred.
  * The resource inside the perimeter that the API client outside the perimeter tried to access.



In the following ingress rule violation example, an API client outside the perimeter tries to access the Cloud Storage bucket `prod-protected-storage-bucket` inside the perimeter `prod-perimeter`.
    
    
    ingressViolations: [
      0: {
        targetResource: "projects/1234/buckets/prod-protected-storage-bucket"
        servicePerimeter: "accessPolicies/123456789/servicePerimeters/prod-perimeter"
      }
    ]
    

To resolve this issue, [create an ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) for your perimeter. For more information about ingress rules, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

### Egress rule violation

An egress rule violation in the audit log indicates one of the following events:

  * An API client inside the perimeter tried to access a resource outside the perimeter.
  * An API request that involves a resource inside the perimeter and a resource outside the perimeter. For example, a Cloud Storage client that calls a copy command where one bucket is within the perimeter and the other bucket is outside the perimeter.



The service perimeter rejects the request because there are no matching egress rules. An egress rule violation in the audit log includes the following details:

  * The source type such as network or resource.
  * The source, which is a resource or network, whose perimeter encountered an egress violation.
  * The perimeter that encountered an egress violation.
  * The target resource outside the perimeter that the request tried to access.



In the following egress rule violation example, the API request includes a resource from projects/5678, which is inside the perimeter `prod-perimeter`, and an object from the Cloud Storage bucket `external-storage-bucket`, which is outside the perimeter.
    
    
    egressViolations: [
      0: {
        sourceType: "Resource"
        source: "projects/5678"
        targetResource: "projects/4321/buckets/external-storage-bucket/objects/corp-resources.json"
        servicePerimeter: "accessPolicies/123456789/servicePerimeters/prod-perimeter"
      }
    ]
    

To resolve this issue, [create an egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) for your perimeter. For more information about egress rules, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

## Debugging requests blocked by VPC Service Controls

The [VPC Service Controls audit log](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) is the primary tool for debugging a request blocked by VPC Service Controls.

When access has been blocked unexpectedly, consult the audit logs in the project protected by the service perimeter. These logs contain significant data about the requested resources and the reason why the request was denied. For information about diagnosing the audit logs, see [Access the violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter#accessing-troubleshooter) and [Resolve access denials with remediation suggestions](https://docs.cloud.google.com/vpc-service-controls/docs/remediation-suggestions) ([Preview](https://cloud.google.com/products#product-launch-stages)).

You can also use automated [remediation suggestions](https://docs.cloud.google.com/vpc-service-controls/docs/remediation-suggestions) in the violation analyzer to generate and apply least-privilege perimeter rules.

If you use [VPC Service Controls service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services#service-patterns) to manage access to unsupported Google services and encounter unexpected denials, the reason for this issue might be the following:

  * The [violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer) doesn't support these violations.
  * [Audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) for these violations might have limited metadata. Check the `protoPayload.request.url` field in the log entry.



Ensure your YAML configuration in the service perimeter accurately reflects the intended URL patterns.

The following sections list the `violationReason` values that you might encounter when using VPC Service Controls.

### NETWORK_NOT_IN_SAME_SERVICE_PERIMETER

The reason for this issue might be one of the following:

  * A client in a VPC network within a service perimeter tries to access a project that is not in the same perimeter. This request results in an egress violation. Create an egress rule to fix this issue.
  * A client in a VPC network that is outside a service perimeter tries to access a project that is protected by the service perimeter. This request results in an ingress violation. Create an ingress rule to fix this issue.



The client might send the request from a Compute Engine or Google Kubernetes Engine VM, or from an on-premises network through Cloud Interconnect or a VPN configured using a VPC network.

The following diagram shows that an egress violation occurs when a client in a VPC network within a service perimeter tries to access a project outside the perimeter:

![An egress violation due to NETWORK_NOT_IN_SAME_SERVICE_PERIMETER.](https://docs.cloud.google.com/static/vpc-service-controls/images/network-error-egress.png)

Here is an example of an egress violation:
    
    
    egressViolations: [
    {
      servicePerimeter: "accessPolicies/<POLICY_NAME>/servicePerimeters/<PERIMETER_NAME>"
      source: "projects/<NETWORK_PROJECT_NUMBER>"
      sourceType: "Network"
      targetResource: "projects/<RESOURCE_PROJECT_NUMBER>"
    }
    ]
    

Where:

  * `<POLICY_NAME>` is the numeric name of your access policy.
  * `<PERIMETER_NAME>` is the name of the service perimeter.
  * `<NETWORK_PROJECT_NUMBER>` is the project number of the Google Cloud project that holds your VPC network.
  * `<RESOURCE_PROJECT_NUMBER>` is the project number of the Google Cloud project that contains the resource.



The following diagram shows that an ingress violation occurs when a client outside the perimeter tries to access a project inside the perimeter:

![An ingress violation due to NETWORK_NOT_IN_SAME_SERVICE_PERIMETER.](https://docs.cloud.google.com/static/vpc-service-controls/images/network-error-ingress.png)

Here is an example of an ingress violation:
    
    
    ingressViolations: [
    {
              targetResource: "projects/<RESOURCE_PROJECT_NUMBER>",
          source: "projects/<NETWORK_PROJECT_NUMBER>"
              servicePerimeter: "accessPolicies/<POLICY_NAME>/servicePerimeters/<PERIMETER_NAME>"
    }
    ]
    

Where:

  * `<RESOURCE_PROJECT_NUMBER>` is the project number of the Google Cloud project that contains the resource.
  * `<NETWORK_PROJECT_NUMBER>` is the project number of the Google Cloud project that holds your VPC network.
  * `<POLICY_NAME>` is the numeric name of your access policy.
  * `<PERIMETER_NAME>` is the name of the service perimeter.



#### Resolution

To resolve this error, [create an ingress or egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) for your perimeter.

### RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER

This issue occurs when a single request is accessing multiple resources but the resources are not in the same service perimeter. This issue occurs irrespective of where the client is located and whether the client has access to the resources.

The following diagram shows a client accessing resources from a project outside the perimeter and from a project within the service perimeter:

![An egress violation due to a client accessing resources from a project outside the
perimeter.](https://docs.cloud.google.com/static/vpc-service-controls/images/resource-error-egress.png)

The following diagram shows a client accessing resources from projects which are in two different service perimeters but the perimeters do not communicate with each other:

![An egress violation due to a client accessing resources from projects which are
in two different service perimeters.](https://docs.cloud.google.com/static/vpc-service-controls/images/resource-error-ingress.png)

Here is an example of an egress violation:
    
    
    egressViolations: [
    {
      servicePerimeter: "accessPolicies/<POLICY_NAME>/servicePerimeters/<PERIMETER_NAME>"
      source: "projects/<RESOURCE_PROJECT_INSIDE_THIS_PERIMETER>"
      sourceType: "Resource"
      targetResource: "projects/<RESOURCE_PROJECT_OUTSIDE_THIS-PERIMETER>"
    }
    ]
    

Where:

  * `<POLICY_NAME>` is the numeric name of your access policy.
  * `<PERIMETER_NAME>` is the name of the service perimeter.
  * `<RESOURCE_PROJECT_INSIDE_THIS_PERIMETER>` is the project number of the Google Cloud project that is within the perimeter.
  * `<RESOURCE_PROJECT_OUTSIDE_THIS_PERIMETER>` is the project number of the Google Cloud project that is outside the perimeter.



#### Resolution

To resolve this issue, [create an egress rule for your perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

### NO_MATCHING_ACCESS_LEVEL

This issue occurs when the IP address, device requirement, or user identity doesn't match any ingress rules or access levels assigned to the perimeter. This means that a client that isn't a part of the Google Cloud network tries to access Google Cloud network resources from outside the perimeter. For example, the IP address corresponding to the `callerIp` field of the audit record doesn't match any CIDR ranges defined in the access levels for the service perimeter.

If the caller IP address is missing or appears as an internal IP address, then this violation might be due to a Google Cloud service that isn't integrated with VPC Service Controls. The reason could be that the Google Cloud service tries to access a protected service and fails, as expected.

To fix this issue, we recommend creating an ingress rule instead of an access level because an ingress rule provides granular access control.

The following diagram shows a client trying to access resources from outside the perimeter:

![An ingress violation due to NO_MATCHING_ACCESS_LEVEL.](https://docs.cloud.google.com/static/vpc-service-controls/images/access-level-error.png)

Here is an example of an ingress violation:
    
    
    authenticationInfo: {
      principalEmail: "EMAIL"
    }
    requestMetadata: {
    callerIp: "<PUBLIC_IP_ADDRESS>"
    deviceState: "Cross Organization"
    }
    ingressViolations: [
            {
              targetResource: "projects/<RESOURCE_PROJECT_NUMBER>",
              servicePerimeter: "accessPolicies/<POLICY_NAME>/servicePerimeters/<PERIMETER-NAME>"
            }
      ]
    
    

Where:

  * `<EMAIL>` is the email address of the service account or authenticated user.

If you use a Google Cloud service that [VPC Service Controls doesn't support](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products), email addresses that belong to the domain `google.com` are redacted and replaced with `google-internal`. `google-internal` refers to internal Google-owned identities.

  * `<PUBLIC_IP_ADDRESS>` is the IP address of the caller. For a caller from the internet, this will be the public IPv4 or IPv6 address.

  * `<RESOURCE_PROJECT_NUMBER>` is the project number of the Google Cloud project that contains the resource.

  * `<POLICY_NAME>` is the numeric name of your access policy.

  * `<PERIMETER_NAME>` is the name of the service perimeter.




Note that in this case, `metadata.accessLevels` could still be present since these access levels might not be specified in the violated perimeter.

### SERVICE_NOT_ALLOWED_FROM_VPC

This issue occurs when a client tries to access Google Cloud resources from a VPC network. The client might send the request from a Compute Engine or Google Kubernetes Engine VM, or from an on-premises network through Cloud Interconnect or a VPN configured using a VPC network.

To fix this issue, ensure that the service being called is allowed by the [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) configuration of the service perimeter.

**Note:** This violation reason is also used for violations involving requests to unsupported services allowed using service patterns. However, for unsupported services, the generated audit logs have limited metadata, and fields such as `methodName`, `authenticationInfo.principalEmail`, `metadata.resourceNames`, `metadata.accessLevels`, and `metadata.deviceState` are missing.**Note:** An API request that has a malformed resource field might cause a VPC Service Controls violation based on the request fields. For example, if a Pub/Sub CreateTopic request specifies the topic name `topic123` instead of the full path `projects/{project}/topics/topic123`, the `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violation occurs.

## Example scenarios

The following examples cover issues that you might encounter while using VPC Service Controls.

  * Cloud Storage access from on-premises
  * BigQuery access from VM outside of project
  * Cross-project BigQuery query
  * Move Cloud Storage file inside perimeter
  * Move Cloud Storage file outside perimeter
  * BigQuery dataset copy from VM inside perimeter
  * Managed Service for Apache Spark job reading from project
  * Unsupported service with restricted VIP
  * Log export to project outside perimeter
  * BigQuery extract to Cloud Storage



### Cloud Storage access from on-premises

In this example, VPC Service Controls blocks a request from an employee workstation (identified by `callerIp`) to a Cloud Storage bucket in project `corp-storage`.

The request generates the following audit log record:
    
    
    {
     insertId:  "222lvajc6f7"
     logName:  "projects/corp-storage/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail:  "someone@google.com"
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "projects/_"
       ]
       violationReason:  "NO_MATCHING_ACCESS_LEVEL"
      }
      methodName:  "google.storage.NoBillingOk"
      requestMetadata: {
       callerIp:  "b1d5:d26d:5b17:43fe:d358:586b:db59:9617"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/690885588241"
      serviceName:  "storage.googleapis.com"
      status: {
       code:  7
       details: [
        0: {
         @type:  "type.googleapis.com/google.rpc.PreconditionFailure"
         violations: [
          0: {
           type:  "VPC_SERVICE_CONTROLS"
          }
         ]
        }
       ]
       message:  "Request is prohibited by organization's policy"
      }
     }
     receiveTimestamp:  "2018-11-27T21:40:43.823209571Z"
     resource: {
      labels: {
       method:  "google.storage.NoBillingOk"
       project_id:  "corp-storage"
       service:  "storage.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-11-27T21:40:42.973784140Z"
    }
    

The `corp-storage` project is included in a service perimeter. The employee workstation is not a part of any networks within that perimeter. Because the employee workstation exists outside the perimeter, the request is blocked.

### BigQuery access from VM outside of project

In this example, a VM that belongs to project `458854174376` (`data-collector`) attempts to run a BigQuery query against a dataset in project `798816221974` (`corp-resources-protected`) and it is denied.

The VM uses the following query:
    
    
    bq --project=corp-resources-protected query 'select count(*) from babynames.yob2000'
    

The query returns the following output:
    
    
    BigQuery error in query operation: VPC Service Controls: Request is
    prohibited by organization's policy. Operation ID:
    33643962-6a0f-4091-9283-bcdf7e9271f0
    

The following audit log record is generated:
    
    
    {
     insertId:  "1ei551d2pdq"
     logName:  "projects/corp-resources-protected/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail:  "714877721106-compute@developer.gserviceaccount.com"
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "projects/1004338142803"
       ]
       violationReason:  "NETWORK_NOT_IN_SAME_SERVICE_PERIMETER"
      }
      methodName:  "bigquery.googleapis.com/bigquery.jobs.create"
      requestMetadata: {
       callerIp:  "10.105.0.2"
       callerNetwork:  "//compute.googleapis.com/projects/ameet-dataflow/global/networks/__unknown__"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/1004338142803"
      serviceName:  "bigquery.googleapis.com"
      status: {
       code:  7
       details: [
        0: {
         @type:  "type.googleapis.com/google.rpc.PreconditionFailure"
         violations: [
          0: {
           type:  "VPC_SERVICE_CONTROLS"
          }
         ]
        }
       ]
       message:  "Request is prohibited by organization's policy"
      }
     }
     receiveTimestamp:  "2018-11-28T23:06:13.579882505Z"
     resource: {
      labels: {
       method:  "bigquery.googleapis.com/bigquery.jobs.create"
       project_id:  "corp-resources-protected"
       service:  "bigquery.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-11-28T23:06:12.799656975Z"
    }
    

In this example, the `violationReason` is `NETWORK_NOT_IN_SAME_SERVICE_PERIMETER`. `callerNetwork` is included in addition to `callerIp`. The IP address is private and the network is provided to disambiguate it. The relevant resources at issue here are listed in two places: `VpcServiceControlAuditMetadata.resourceNames` and `requestMetadata.callerNetwork` (the project that owns the network).

The problem is that the `corp-resources-protected` project is inside a service perimeter, while `data-collector`, the project that includes the network that the VM belongs to, is not. In this case, access is denied as expected.

### Cross-project BigQuery query

In this example, a VM that belongs to the `perimeter-network` project attempts to query the BigQuery instances of two different projects: `corp-resources-protected`, which is in the same service perimeter as `perimeter-network`, and `corp-resources-public`, which is not.

The VM uses the following command:
    
    
    bq query --use_legacy_sql=false \
        'select count(priv.name),count(pub.name) from \
        `corp-resources-protected.babynames.yob2000` as priv, \
        `corp-resources-public.babynames.yob2000` as pub'
    

The query returns the following output:
    
    
    BigQuery error in query operation: Error processing job
    'example:bqjob_r211e6f6eec928ffb_000001675c996aa8_1': VPC Service Controls:
    Request is prohibited by organization's policy. Operation ID:
    dc4fc177-4850-4fc5-b2e7-8c33f302149a
    

The following audit log record is generated:
    
    
    {
     insertId:  "17kg4exd24ag"
     logName:  "projects/perimeter-network/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "projects/117961063178"
        1:  "projects/690885588241"
       ]
       violationReason:  "RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER"
      }
      methodName:  "bigquery.googleapis.com/bigquery.tables.getData"
      requestMetadata: {
       callerIp:  "130.211.225.66"
       callerNetwork:  "//compute.googleapis.com/projects/perimeter-network/global/networks/__unknown__"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/927005422713"
      serviceName:  "bigquery.googleapis.com"
      status: {
       code:  7
       details: [
        0: {
         @type:  "type.googleapis.com/google.rpc.PreconditionFailure"
         violations: [
          0: {
           type:  "VPC_SERVICE_CONTROLS"
          }
         ]
        }
       ]
       message:  "Request is prohibited by organization's policy"
      }
     }
     receiveTimestamp:  "2018-11-28T20:48:51.384237810Z"
     resource: {
      labels: {
       method:  "bigquery.googleapis.com/bigquery.tables.getData"
       project_id:  "perimeter-network"
       service:  "bigquery.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-11-28T20:48:50.561884949Z"
    }
    

Looking at `callerNetwork` and `VpcServiceControlAuditMetadata.resourceNames`, we can see three projects: `perimeter-network`, `117961063178` (`corp-resources-public`), and `690885588241` (`corp-resources-protected`). Recall that `corp-resources-public` is not in the same service perimeter as `perimeter-network` and `corp-resources-protected`.

The `violationReason`, `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` indicates that some resource in the request is outside of a perimeter that applies to the request. In this case, that resource is `corp-resources-public`.

### Move Cloud Storage file inside perimeter

In this example, a VM in project `perimeter-network` uses a command to move a file from one Cloud Storage bucket, located in project `corp-resources-protected`, to another bucket, located in project `corp-resources-public`.

The VM uses the following command:
    
    
    gcloud storage mv gs://corp-resources-private-1/yob2000.txt gs://corp-resources-public-1/babynames/
    

The command returns the following output:
    
    
    Copying gs://corp-resources-private-1/yob2000.txt [Content-Type=text/plain]...
    AccessDeniedException: 403 Request violates VPC Service Controls.
    

The following audit log record is generated:
    
    
    {
     insertId:  "1xxnssmd2hqo"
     logName:  "projects/perimeter-network/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail:  "storage-accessing@example.iam.gserviceaccount.com"
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "projects/_/buckets/corp-resources-public-1"
       ]
       violationReason:  "NETWORK_NOT_IN_SAME_SERVICE_PERIMETER"
      }
      methodName:  "google.storage.BillingRequiredRead"
      requestMetadata: {
       callerIp:  "130.211.225.66"
       callerNetwork:  "//compute.googleapis.com/projects/perimeter-network/global/networks/__unknown__"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/927005422713"
      serviceName:  "storage.googleapis.com"
      status: {…}
     }
     receiveTimestamp:  "2018-11-28T00:45:31.531623485Z"
     resource: {
      labels: {
       method:  "google.storage.BillingRequiredRead"
       project_id:  "perimeter-network"
       service:  "storage.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-11-28T00:45:31.351140381Z"
    }
    

In this case, the log is less clear because the method listed is `BillingRequiredRead` and the action taken is `move`. This is a limitation of VPC Service Controls's present audit log functionality.

While the reason is less clear, this audit log record indicates that some resource in the request is outside of a perimeter that applies to the request. In this case, that resource is `corp-resources-public`.

### Move Cloud Storage file outside perimeter

In this example, a VM in project `public-network` uses a command to move a file from one Cloud Storage bucket, located in project `corp-resources-protected`, to another bucket, located in project `corp-resources-public`.

The `corp-resources-protected` project is protected by a service perimeter. The `public-network` and `corp-resources-public` projects exist outside the perimeter.

The VM uses the following command:
    
    
    gcloud storage mv gs://corp-resources-private-1/yob2000.txt gs://corp-resources-public-1/babynames/
    

The command returns the following output:
    
    
    Copying gs://corp-resources-private-1/yob2000.txt [Content-Type=text/plain]...
    AccessDeniedException: 403 Request violates VPC Service Controls.
    

The following audit log record is generated:
    
    
    {
     insertId:  "10moqhsch9v"
     logName:  "projects/corp-resources-private/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail:  "user@example.biz"
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "projects/_/buckets/corp-resources-private-1/objects/yob2000.txt"
        1:  "projects/_/buckets/corp-resources-public-1/objects/out.txt"
       ]
       violationReason:  "RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER"
      }
      methodName:  "google.storage.Write"
      requestMetadata: {
       callerIp:  "2620:15c:2c4:203:63d6:5eb8:418d:c034"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/1004338142803"
      serviceName:  "storage.googleapis.com"
      status: {
       code:  7
       details: [
        0: {
         @type:  "type.googleapis.com/google.rpc.PreconditionFailure"
         violations: [
          0: {
           type:  "VPC_SERVICE_CONTROLS"
          }
         ]
        }
       ]
       message:  "Request is prohibited by organization's policy"
      }
     }
     receiveTimestamp:  "2018-11-30T16:34:46.948010626Z"
     resource: {
      labels: {
       method:  "google.storage.Write"
       project_id:  "corp-resources-private"
       service:  "storage.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-11-30T16:34:46.898098978Z"
    }
    

In this example, the audit log indicates that one cannot copy data across the boundary of a service perimeter (both resources are in the audit log record). Recall that the request originates from outside the perimeter (the VM in `public-network`), and that one of the buckets exists outside the perimeter (`corp-resources-public-1`).

From outside the perimeter, one is able to write to bucket `corp-resources-public-1`, so the check that failed in the previous example passes. However, the subsequent check to actually copy the data fails.

This example demonstrates how sometimes a single user operation results in multiple internal operations that must pass VPC Service Controls enforcement.

### BigQuery dataset copy from VM inside perimeter

In this example, a VM in project `927005422713` (`perimeter-network`) tries to copy a BigQuery dataset from project `corp-resources-private` to `corp-resources-public` (`117961063178`). `perimeter-network` and `corp-resources-private` share a perimeter, while `corp-resources-public` exists outside the perimeter.

The VM uses the following command:
    
    
    bq cp corp-resources-private:babynames.yob2000 \
        corp-resources-public:babynames.yob2000
    

The command returns the following output:
    
    
    BigQuery error in cp operation: VPC Service Controls: Request is prohibited by
    organization's policy. Operation ID: c00dbc44-460f-4bd0-9d09-cda98ac800f9
    

The following audit log record is generated:
    
    
    {
     insertId:  "146o5fd2hbp"
     logName:  "projects/perimeter-network/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "projects/117961063178"
       ]
       violationReason:  "RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER"
      }
      methodName:  "bigquery.googleapis.com/bigquery.tables.get"
      requestMetadata: {
       callerIp:  "131.201.221.16"
       callerNetwork:  "//compute.googleapis.com/projects/perimeter-network/global/networks/__unknown__"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/927005422713"
      serviceName:  "bigquery.googleapis.com"
      status: {
       code:  7
       details: [
        0: {
         @type:  "type.googleapis.com/google.rpc.PreconditionFailure"
         violations: [
          0: {
           type:  "VPC_SERVICE_CONTROLS"
          }
         ]
        }
       ]
       message:  "Request is prohibited by organization's policy"
      }
     }
     receiveTimestamp:  "2018-11-28T00:27:05.688803777Z"
     resource: {
      labels: {
       method:  "bigquery.googleapis.com/bigquery.tables.get"
       project_id:  "perimeter-network"
       service:  "bigquery.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-11-28T00:27:05.378584819Z"
    }
    

In this example, there is no single underlying API action that shows all the resources at play in this request due to limitations of the logging mechanism and the distributed architecture of BigQuery.

The audit log record indicates that the operation failed because in order to copy the data, BigQuery must access the target project (`corp-resources-public`) using the network in project `perimeter-network` (the source of the request). Recall that `corp-resources-public` is outside the perimeter that protects `perimeter-network`. The request is denied as an attempt to exfiltrate data to `corp-resources-public`.

This example illustrates that one conceptual operation, such as copying data, can trigger multiple attempts to access data from different storage systems, such as Cloud Storage, BigQuery, and Bigtable. Based on how the operation is executed, the generated audit log record differs from the original user command. Also, when multiple checks within a given service are made and potentially fail, the generated audit log record looks different from the original user command.

### Managed Service for Apache Spark job reading from project

This example shows how to debug indirect VPC Service Controls errors that occur when using data processing services like Managed Service for Apache Spark.

In this example, a Managed Service for Apache Spark cluster is running in a project protected by VPC Service Controls. `Hello-world.py` is a pyspark job that attempts to access data from Cloud Storage bucket inside the perimeter and then write it to another bucket that exists outside the perimeter. VPC Service Controls blocks the operation that writes data to a bucket outside the perimeter.

The following command is used to execute `Hello-world.py`:
    
    
    gcloud dataproc jobs submit pyspark hello-world.py --cluster test-cluster-new2
    

The command returns the following output:
    
    
    Job [50f16ca8-5102-442b-a545-eed5e4f5f5da] submitted.
    Waiting for job output...
    18/11/29 00:31:34 INFO org.spark_project.jetty.util.log: Logging initialized @2552ms
    18/11/29 00:31:34 INFO org.spark_project.jetty.server.Server: jetty-9.3.z-SNAPSHOT
    18/11/29 00:31:34 INFO org.spark_project.jetty.server.Server: Started @2640ms
    18/11/29 00:31:34 INFO org.spark_project.jetty.server.AbstractConnector: Started ServerConnector@1f1c18ec{HTTP/1.1,[http/1.1]}{0.0.0.0:4040}
    18/11/29 00:31:34 INFO com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystemBase: GHFS version: 1.6.4-hadoop2
    18/11/29 00:31:35 INFO org.apache.hadoop.yarn.client.RMProxy: Connecting to ResourceManager at test-cluster-new2-m/10.246.0.3:8032
    18/11/29 00:31:37 INFO org.apache.hadoop.yarn.client.api.impl.YarnClientImpl: Submitted application application_1522454176466_0005
    Traceback (most recent call last):
      File "/tmp/50f16ca8-5102-442b-a545-eed5e4f5f5da/hello-world.py", line 8, in <module>
        lear.saveAsTextFile("gs://corp-resources-public-1/out.txt")
      File "/usr/lib/spark/python/lib/pyspark.zip/pyspark/rdd.py", line 1553, in saveAsTextFile
      File "/usr/lib/spark/python/lib/py4j-0.10.4-src.zip/py4j/java_gateway.py", line 1133, in __call__
      File "/usr/lib/spark/python/lib/py4j-0.10.4-src.zip/py4j/protocol.py", line 319, in get_return_value
    py4j.protocol.Py4JJavaError: An error occurred while calling o49.saveAsTextFile.
    : java.io.IOException: Error accessing: bucket: corp-resources-public-1, object: out.txt
        at com.google.cloud.hadoop.gcsio.GoogleCloudStorageImpl.wrapException(GoogleCloudStorageImpl.java:1767)
    $sp(PairRDDFunctions.scala:961)
    
     (truncated)
    
    Caused by: com.google.api.client.googleapis.json.GoogleJsonResponseException: 403 Forbidden
    {
      "code" : 403,
      "errors" : [ {
        "domain" : "global",
        "message" : "Request violates VPC Service Controls.",
        "reason" : "vpcServiceControls"
      } ],
      "message" : "Request violates VPC Service Controls."
    }
        at com.google.api.client.googleapis.json.GoogleJsonResponseException.from(GoogleJsonResponseException.java:145)
    
     (truncated)
    
    18/11/29 00:31:43 INFO org.spark_project.jetty.server.AbstractConnector: Stopped Spark@1f1c18ec{HTTP/1.1,[http/1.1]}{0.0.0.0:4040}
    ERROR: (gcloud.dataproc.jobs.submit.pyspark) Job [50f16ca8-5102-442b-a545-eed5e4f5f5da] entered state [ERROR] while waiting for [DONE].
    

Note the IO exception that occurs when the `saveAsTextFile` method is called. Cloud Storage returns a `403` error with the message `Request violates VPC Service Controls`. The error indicates that the Cloud Storage audit log operation must be reviewed.

In the audit logs for the `perimeter-network` project, where the command was executed, there is an audit log record for the `saveAsTextFile` operation:
    
    
    {
     insertId:  "qdj1o9d1run"
     logName:  "projects/corp-resources-private/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail:  "1004338142803-compute@developer.gserviceaccount.com"
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "projects/_/buckets/corp-resources-public-1/objects/out.txt"
       ]
       violationReason:  "RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER"
      }
      methodName:  "google.storage.BillingRequiredRead"
      requestMetadata: {
       callerIp:  "10.246.0.3"
       callerNetwork:  "//compute.googleapis.com/projects/corp-resources-private/global/networks/__unknown__"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/1004338142803"
      serviceName:  "storage.googleapis.com"
      status: {
       code:  7
       details: [
        0: {
         @type:  "type.googleapis.com/google.rpc.PreconditionFailure"
         violations: [
          0: {
           type:  "VPC_SERVICE_CONTROLS"
          }
         ]
        }
       ]
       message:  "Request is prohibited by organization's policy"
      }
     }
     receiveTimestamp:  "2018-11-29T00:31:43.666227930Z"
     resource: {
      labels: {
       method:  "google.storage.BillingRequiredRead"
       project_id:  "corp-resources-private"
       service:  "storage.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-11-29T00:31:43.608250320Z"
    }
    

Due to audit log limitations, the `methodName` for Cloud Storage is listed as `Read` even though it is actually a `write` operation. The audit log record indicates that the operation failed because a network in project `corp-resources-private` was attempting to access the data (writing, in this case) of a resource in bucket `corp-resources-public-1`. Due to the limitations of the Cloud Storage audit log, it is not clear which project bucket `corp-resources-public-1` belongs to.

To identify the project that contains `corp-resources-public-1`, use the following command:
    
    
    gcloud storage ls gs://corp-resources-public-1 --buckets --log-http 2>&1 | grep projectNumber
    

The command returns the following output: `"projectNumber": "117961063178",`

`117961063178` is project `corp-resources-public`, which is outside perimeter. Thus, the failure is expected.

### Error due to unsupported services

Some Google Cloud services depend on other Google Cloud services as part of their implementation. If an unsupported service such as App Engine is used inside a project that is protected by a perimeter, the service's resources might not be accessible.

For information about known problematic cases, see [Known service limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#service-limitations).

### Unsupported service with restricted VIP

Attempting to access an API that is not supported by the VPC Service Controls restricted VIP results in a `403` error. For example, VPC Service Controls does not support App Engine, so the App Engine Admin API is not available when using the restricted VIP.

For example, suppose the following command is used to list all App Engine services within a service perimeter:
    
    
    gcloud app services list
    

The command returns one of the following outputs:
    
    
    ERROR: (gcloud.app.services.list) User [***] does not have permission to access apps instance [***] (or it may not exist): <!DOCTYPE html>
    <html lang=en>
      <meta charset=utf-8>
      <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
      <title>Error 403 (Forbidden)!!1</title>
      <style>
        *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){ #logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){ #logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}
      </style>
      <a href=//www.google.com/><span id=logo aria-label=Google></span></a>
      <p><b>403.</b> <ins>That's an error.</ins>
      <p>Your client does not have permission to get URL <code>/v1/apps/***/services</code> from this server.  <ins>That's all we know.</ins>
    
    
    
    The service that you're trying to access isn't available on Google's Restricted VIPs. For a list of services that support VPC Service Controls, see https://cloud.google.com/vpc-service-controls/docs/supported-products.
    

This type of error is expected for services that are not supported by VPC Service Controls and not available on the restricted VIP. If this error occurs for a service that _is_ supported by VPC Service Controls, then we recommend that you check the [known service limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#service-limitations) for that service to see if it is a known limitation. Otherwise, [the issue must be reported](https://docs.cloud.google.com/support/docs/issue-trackers).

### Log export to project outside perimeter

In this example, a log export is blocked by VPC Service Controls. The export destination, project `corp-resources-public`, is outside of the VPC Service Controls perimeter, while the sink is created on project `perimeter-network`, which is inside the perimeter.

**Note:** This example specifically describes a log export to BigQuery, but exports to other features, such as Cloud Storage and Pub/Sub behave the same way.

For example, suppose the following command is used:
    
    
    gcloud logging sinks describe example-sink
    

The command returns the following output:
    
    
    destination: bigquery.googleapis.com/projects/corp-resources-public/datasets/logs
    filter: |-
      resource.type="audited_resource"
      resource.labels.service="bigquery.googleapis.com"
    name: example-sink
    outputVersionFormat: V2
    writerIdentity: serviceAccount:p927005422713-439672@gcp-sa-logging.iam.gserviceaccount.com
    
    

The following audit log record is generated:
    
    
    {
     insertId:  "e5i2i8cbqw"
     logName:  "projects/perimeter-network/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail:  "p927005422713-439672@gcp-sa-logging.iam.gserviceaccount.com"
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "corp-resources-public"
       ]
       violationReason:  "RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER"
      }
      methodName:  "google.cloud.bigquery.v2.TableDataService.InsertAll"
      requestMetadata: {
       callerIp:  "2002:a49:8c51::"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/927005422713"
      serviceName:  "bigquery.googleapis.com"
      status: {
       code:  7
       details: [
        0: {
         @type:  "type.googleapis.com/google.rpc.PreconditionFailure"
         violations: [
          0: {
           type:  "VPC_SERVICE_CONTROLS"
          }
         ]
        }
       ]
       message:  "Request is prohibited by organization's policy"
      }
     }
     receiveTimestamp:  "2018-11-29T17:32:19.287138882Z"
     resource: {
      labels: {
       method:  "google.cloud.bigquery.v2.TableDataService.InsertAll"
       project_id:  "perimeter-network"
       service:  "bigquery.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-11-29T17:32:19.054662413Z"
    }
    

The audit log record is generated for BigQuery, not for Logging. This is because BigQuery is the sink service that Logging is attempting to write to.

The export fails because `corp-resources-public` exists outside the perimeter that protects `perimeter-network`.

This example shows that for cases where one Google Cloud service calls another using a managed service account that is internal to Google Cloud, such as `p927005422713-439672@gcp-sa-logging.iam.gserviceaccount.com`, the "network project" (in this case, `perimeter-network`) of the request is derived from that identity. The same identity represents the log export resource itself.

This pattern is common in Google Cloud and applies to numerous cases of service-to-service interaction.

### BigQuery extract to Cloud Storage

This example describes how to debug failed BigQuery extractions to Cloud Storage.

In this example, `corp-resources-private` and `perimeter-network` are projects protected by a service perimeter. `corp-resources-public` is a project that exists outside the perimeter.

Suppose the following command was used:
    
    
    bq extract babynames.yob2000
    

The command returns the following output:
    
    
    gs://corp-resources-public-1/export.txt
    Waiting on bqjob_r47ee34109d02b41_000001676b27157c_1 ... (1s) Current status: DONE
    BigQuery error in extract operation: Error processing job 'corp-resources-private:bqjob_r47ee34109d02b41_000001676b27157c_1': Access
    Denied: BigQuery BigQuery: Permission denied while writing data.
    

In this case, the error does not specifically implicate VPC Service Controls. A similar error is shown if there is an Identity and Access Management failure.

The following audit log record is generated:
    
    
    {
     insertId:  "4gbh6pe8jld7"
     logName:  "projects/corp-resources-private/logs/cloudaudit.googleapis.com%2Fdata_access"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail:  "storage-accessing@example.iam.gserviceaccount.com"
      }
      methodName:  "jobservice.jobcompleted"
      requestMetadata: {
       callerIp:  "10.5.0.4"
       callerNetwork:  "//compute.googleapis.com/projects/perimeter-network/global/networks/__unknown__"
       callerSuppliedUserAgent:  "google-api-python-client/1.6.5 (gzip),gzip(gfe)"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/corp-resources-private/jobs/bqjob_r47ee34109d02b41_000001676b27157c_1"
      serviceData: {
       @type:  "type.googleapis.com/google.cloud.bigquery.logging.v1.AuditData"
       jobCompletedEvent: {
        eventName:  "extract_job_completed"
        job: {
         jobConfiguration: {
          extract: {
           destinationUris: [
            0:  "gs://corp-resources-public-1/export.txt"
           ]
           sourceTable: {
            datasetId:  "babynames"
            projectId:  "corp-resources-private"
            tableId:  "yob2000"
           }
          }
         }
         jobName: {
          jobId:  "bqjob_r47ee34109d02b41_000001676b27157c_1"
          location:  "US"
          projectId:  "corp-resources-private"
         }
         jobStatistics: {
          createTime:  "2018-12-01T19:03:03.908Z"
          endTime:  "2018-12-01T19:03:05.494Z"
          startTime:  "2018-12-01T19:03:04.013Z"
         }
         jobStatus: {
          additionalErrors: [
           0: {
            code:  7
            message:  "Access Denied: BigQuery BigQuery: Permission denied while writing data."
           }
          ]
          error: {
           code:  7
           message:  "Access Denied: BigQuery BigQuery: Permission denied while writing data."
          }
          state:  "DONE"
         }
        }
       }
      }
      serviceName:  "bigquery.googleapis.com"
      status: {
       code:  7
       message:  "Access Denied: BigQuery BigQuery: Permission denied while writing data."
      }
     }
     receiveTimestamp:  "2018-12-01T19:03:05.532169998Z"
     resource: {
      labels: {
       project_id:  "corp-resources-private"
      }
      type:  "bigquery_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-12-01T19:03:05.503Z"
    }
    

In this audit log record, `storage-accessing@example.iam.gserviceaccount.com` is identified as the identity attempting to run the operation. In this example, assume that `storage-accessing@example.iam.gserviceaccount.com` has the required IAM permissions to execute the command.

As IAM permissions are not the issue, the next step is to check for VPC Service Controls failures.

The audit log record for the destination service (Cloud Storage) contains detailed reasons for the failure:
    
    
    {
     insertId:  "1bq397kcfj1"
     logName:  "projects/corp-resources-private/logs/cloudaudit.googleapis.com%2Fpolicy"
     protoPayload: {
      @type:  "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail:  "storage-accessing@example.iam.gserviceaccount.com"
      }
      metadata: {
       @type:  "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
       resourceNames: [
        0:  "projects/1004338142803"
        1:  "projects/_/buckets/corp-resources-public-1"
       ]
       violationReason:  "RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER"
      }
      methodName:  "google.storage.BillingRequiredRead"
      requestMetadata: {
       callerIp:  "10.5.0.4"
       callerNetwork:  "//compute.googleapis.com/projects/perimeter-network/global/networks/__unknown__"
       destinationAttributes: {
       }
       requestAttributes: {
       }
      }
      resourceName:  "projects/1004338142803"
      serviceName:  "storage.googleapis.com"
      status: {
       code:  7
       details: [
        0: {
         @type:  "type.googleapis.com/google.rpc.PreconditionFailure"
         violations: [
          0: {
           type:  "VPC_SERVICE_CONTROLS"
          }
         ]
        }
       ]
       message:  "Request is prohibited by organization's policy"
      }
     }
     receiveTimestamp:  "2018-12-01T19:03:05.617451586Z"
     resource: {
      labels: {
       method:  "google.storage.BillingRequiredRead"
       project_id:  "corp-resources-private"
       service:  "storage.googleapis.com"
      }
      type:  "audited_resource"
     }
     severity:  "ERROR"
     timestamp:  "2018-12-01T19:03:05.420005215Z"
    }
    

From this log, it is clear that the two projects `1004338142803` (`corp-resources-private-1`) and `corp-resources-public` are both being used to complete the command. Because those projects do not share a perimeter, the extract job fails.

This example illustrates that in complex multi-service operations, the audit logs for both the source and destination services might contain useful debugging data.

### Perimeter access through Cloud NAT gateway

In this example, assume that project A from Org A is not configured within any perimeter. Project B is secured by a perimeter in a different organization. Private resources on project A use Cloud NAT gateway to reach the internet and Google APIs and services. An access level is configured on project B to allow access based on the external gateway IP addresses of project A.

A VM that belongs to project A (which can be a Google Kubernetes Engine node) attempts to access a protected resource in project B but the connection fails, and the following audit log record is generated in project B:
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "code": 7,
          "message": "Request is prohibited by organization's policy. vpcServiceControlsUniqueIdentifier: kmpY9Fgfuhgi2NE90lURjFWuiS1nGRqxCw4L12HdW8h46Un__-_LZw",
          "details": [
            {
              "@type": "type.googleapis.com/google.rpc.PreconditionFailure",
              "violations": [
                {
                  "type": "VPC_SERVICE_CONTROLS",
                  "description": "kmpY9Fgfuhgi2NE90lURjFWuiS1nGRqxCw4L12HdW8h46Un__-_LZw"
                }
              ]
            }
          ]
        },
        "authenticationInfo": {
          "principalEmail": "my-user@example.iam.gserviceaccount.com",
          "serviceAccountKeyName": "//iam.googleapis.com/projects/my-project/serviceAccounts/my-user@example.iam.gserviceaccount.com/keys/<code><var>ACCOUNT_KEY</var></code>"
        },
        "requestMetadata": {
          "callerIp": "gce-internal-ip",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "cloudfunctions.googleapis.com",
        "methodName": "google.cloud.functions.v1.CloudFunctionsService.ListFunctions",
        "resourceName": "<code><var>PROJECT_ID_1</var></code>",
        "metadata": {
          "violationReason": "NETWORK_NOT_IN_SAME_SERVICE_PERIMETER",
          "resourceNames": [
            "projects/<code><var>PROJECT_ID_2</var></code>/locations/-"
          ],
          "securityPolicyInfo": {
            "servicePerimeterName": "accessPolicies/<code><var>ACCESS_POLICY</var></code>/servicePerimeters/us_sandbox",
            "organizationId": "<code><var>ORGANIZATION_ID</var></code>"
          },
          "deviceState": "Unknown",
          "vpcServiceControlsUniqueId": "kmpY9Fgfuhgi2NE90lURjFWuiS1nGRqxCw4L12HdW8h46Un__-_LZw",
          "ingressViolations": [
            {
              "targetResource": "projects/<code><var>PROJECT_ID_1</var></code>",
              "servicePerimeter": "accessPolicies/<code><var>ACCESS_POLICY</var></code>/servicePerimeters/<code><var>PERIMETER_NAME</var></code>",
              "source": "<code><var>PROJECT_ID_2</var></code>"
            }
          ],
          "@type": "type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
        }
      },
      "insertId": "tzf7fd103i",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "cloudfunctions.googleapis.com",
          "method": "google.cloud.functions.v1.CloudFunctionsService.ListFunctions",
          "project_id": "<code><var>PROJECT_ID_2</var></code>"
        }
      },
      "timestamp": "2024-04-02T19:56:10.770681816Z",
      "severity": "ERROR",
      "logName": "projects/<code><var>PROJECT_ID_2</var></code>/logs/cloudaudit.googleapis.com%2Fpolicy",
      "receiveTimestamp": "2024-04-02T19:56:11.463811603Z"
    }
    

The `callerIp` resource does not record an external IP address. Instead of the Cloud NAT gateway external IP address, the `callerIp` resource shows `gce-internal-ip`.

The `callerIp` field is redacted to `gce-internal-ip` when the requests originate from a different project or organization and the source Compute Engine VM does not have an external IP address.

[Cloud NAT](https://docs.cloud.google.com/nat/docs/nat-product-interactions#interaction-pga) has an integration with [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) that automatically enables Private Google Access on the resource's subnet, and keeps the traffic to Google APIs and services internal as opposed to routing it to the internet using the Cloud NAT gateway external IP address.

In this case, as the traffic is routed within the internal Google network, the `RequestMetadata.caller_ip` field of the `AuditLog` object is redacted to `gce-internal-ip`. To fix this, instead of using the Cloud NAT gateway external IP address in the access level for [IP-based allowlist](https://docs.cloud.google.com/vpc-service-controls/docs/access-level-design#source-ip), configure an ingress rule to allow from the project or service account.

## What's next

  * Learn how to [retrieve VPC Service Controls errors from audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors).
  * Learn how to [troubleshoot common issues related to other Google Cloud services](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshoot-services-within-perimeter).
  * Learn how to [diagnose an access denial in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer) and view its comprehensive evaluation report.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
