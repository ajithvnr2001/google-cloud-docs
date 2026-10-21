---
url: https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts/
title: Example logs for service accounts \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:16.294356+00:00
---

# Example logs for service accounts  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Example logs for service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page shows examples of the audit logs that are generated when you manage or use a service account.

**Note:** Each example shows only the most relevant fields in the log entries.

For more information about enabling and viewing audit logs, see [IAM audit logging](https://docs.cloud.google.com/iam/docs/audit-logging).

## Logs for creating service accounts

When you create or modify a service account, Identity and Access Management (IAM) generates log entries. The following example shows a log entry for creating a service account:
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : "example-user@example.com"**
        },
        "methodName": "google.iam.admin.v1.CreateServiceAccount",
        **"response" : {
          "email": "my-service-account@my-project.iam.gserviceaccount.com",
          "@type": "type.googleapis.com/google.iam.admin.v1.ServiceAccount",
          "display_name": "My service account."
        }**
      },
      "resource": {
        "type": "service_account"
      }
    }

## Logs for granting roles

This section shows the log entries you receive when you grant roles that are related to service accounts.

**Note:** You might see log entries in which the service account `service-agent-manager@system.gserviceaccount.com` grants roles to other service agents. This behavior is normal and expected. For details, see [Service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).

### Logs for granting the Service Account User role

A principal can gain the same permissions as a service account by _impersonating_ the service account. To allow a principal to impersonate a service account, you can [grant the Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`) to the principal for the service account.

The following example shows a log entry for granting the Service Account User role to a principal:
    
    
    {
      "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        **"methodName" : "google.iam.admin.v1.SetIAMPolicy",**
        "request": {
          "@type": "type.googleapis.com/google.iam.v1.SetIamPolicyRequest",
          "resource": "projects/-/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com"
        },
        **"resourceName" : "projects/-/serviceAccounts/123456789012345678901",**
        "response": {
          "@type": "type.googleapis.com/google.iam.v1.Policy",
          "bindings": [
            {
              **"members" : [
                "user:my-user@example.com"
              ],
              "role": "roles/iam.serviceAccountUser"**
            }
          ]
        }
      },
      "resource": {
        "type": "service_account"
      }
    }

When you [grant the Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) (`roles/iam.serviceAccountTokenCreator`), which allows a principal to create short-lived credentials, IAM generates a similar log entry.

### Logs for granting access to a service account on a resource

You can [grant a role to a service account on a specific resource](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access), which allows the service account to access the resource. If the service that owns the resource also supports audit logging, then granting a role to the service account generates an audit log entry. The log entry includes the field `protoPayload.authenticationInfo.principalEmail`, which identifies the principal that granted the role to the service account.

The following example shows an audit log entry for granting a role to a service account for a project. In this example, `example-user@example.com` granted the Organization Viewer role (`roles/resourcemanager.organizationViewer`) to the service account. The `protoPayload.serviceName` field is set to `cloudresourcemanager.googleapis.com`, because Resource Manager is the Google Cloud service that manages projects. Also, the `resource.type` field is set to `project`:
    
    
    {
      "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : "example-user@example.com"**
        },
        **"methodName" : "SetIamPolicy",**
        "request": {
          "@type": "type.googleapis.com/google.iam.v1.SetIamPolicyRequest",
          "resource": "my-project"
        },
        **"resourceName" : "projects/my-project",**
        "response": {
          "@type": "type.googleapis.com/google.iam.v1.Policy",
          "bindings": [
            {
              **"members" : [
                "serviceAccount:my-service-account@my-project.iam.gserviceaccount.com"
              ],
              "role": "roles/resourcemanager.organizationViewer"**
            }
          ]
        },
        **"serviceName" : "cloudresourcemanager.googleapis.com"**
      },
      "resource": {
        **"type" : "project"**
      }
    }

## Logs for attaching service accounts to resources

If a user has the Service Account User role (`roles/iam.serviceAccountUser`) on a service account, the user can [attach the service account to resources](https://docs.cloud.google.com/iam/docs/attach-service-accounts). When code running on the resource accesses Google Cloud services and resources, it uses the service account attached to the resource as its identity. For example, if you [attach a service account to a Compute Engine instance](https://docs.cloud.google.com/compute/docs/access/service-accounts#associating_a_service_account_to_an_instance), and the applications on the instance use a [client library](https://docs.cloud.google.com/apis/docs/client-libraries-explained) to call Google Cloud APIs, those applications automatically use the attached service account for authentication and authorization. 

This section shows some of the logs that are generated when you attach a service account to a resource.

### Logs for using the `iam.serviceAccounts.actAs` permission

Attaching a service account to a resource requires the `iam.serviceAccounts.actAs` permission. When a principal uses this permission to attach a service account to a resource, it generates an audit log.

The following example shows a log entry for a principal using the `iam.serviceAccounts.actAs` permission to attach a service account to a Compute Engine instance.
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "example-user@example.com"
        },
        "serviceName": "iam.googleapis.com",
        "methodName": "iam.serviceAccounts.actAs",
        "authorizationInfo": [
          {
            "resource": "projects/-/serviceAccounts/sample-service-account@sample-project.iam.gserviceaccount.com",
            "permission": "iam.serviceAccounts.actAs",
            "granted": true,
            "permissionType": "ADMIN_WRITE"
          }
        ],
        "resourceName": "projects/-/serviceAccounts/sample-service-account@sample-project.iam.gserviceaccount.com",
        "request": {
          "name": "sample-service-account@sample-project.iam.gserviceaccount.com",
          "project_number": "787155667719",
          "@type": "type.googleapis.com/CanActAsServiceAccountRequest"
        },
        "response": {
          "success": true,
          "@type": "type.googleapis.com/CanActAsServiceAccountResponse"
        }
      },
      "insertId": "vojt0vd4fdy",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "project_id": "sample-project",
          "method": "iam.serviceAccounts.actAs",
          "service": "iam.googleapis.com"
        }
      },
      "timestamp": "2024-08-05T21:56:56.097601933Z",
      "severity": "NOTICE",
      "logName": "projects/sample-project/logs/cloudaudit.googleapis.com%2Factivity",
      "receiveTimestamp": "2024-08-05T21:56:56.097601933Z"
    }

### Logs for setting up a Compute Engine instance to run as a service account

If a user has the Service Account User role (`roles/iam.serviceAccountUser`) on a service account, the user can [create a Compute Engine virtual machine (VM) instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using) that runs as that service account. In this scenario, the user creates the VM instance with their own credentials, and the request specifies a service account for the VM instance to use.

When a user creates a VM instance, Compute Engine creates multiple log entries. The following example shows the first log entry, which identifies the user who created the VM instance and the service account that the instance uses. In this example, the user `example-user@example.com` created an instance that uses the service account `my-service-account@my-project.iam.gserviceaccount.com`. As a result, the `protoPayload.authenticationInfo.principalEmail` field is set to `example-user@example.com`, and the `protoPayload.request.serviceAccounts[0].email` field is set to `my-service-account@my-project.iam.gserviceaccount.com`:
    
    
    {
      "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : "example-user@example.com"**
        },
        "methodName": "v1.compute.instances.insert",
        "request": {
          "@type": "type.googleapis.com/compute.instances.insert",
          **"serviceAccounts" : [
            {
              "email": "my-service-account@my-project.iam.gserviceaccount.com"
            }
          ]**
        },
        "resourceName": "projects/my-project/zones/us-central1-a/instances/my-instance"
      },
      "resource": {
        "type": "gce_instance"
      }
    }

## Logs for accessing Google Cloud with a service account key

This section shows the log entries you receive when you create a service account key, then use the key to access Google Cloud.

### Logs for creating a service account key

If you have the Service Account Key Admin role (`roles/iam.serviceAccountKeyAdmin`) on a service account, you can create a service account key, then use the key to [authenticate requests to Google Cloud services](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises#wlif-key).

The following example shows a log entry for creating a service account key. In this example, the user `example-user@example.com` created a key for the service account `my-service-account@my-project.iam.gserviceaccount.com`:
    
    
    {
      "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : "example-user@example.com",**
        },
        "methodName": "google.iam.admin.v1.CreateServiceAccountKey",
        "request": {
          "@type": "type.googleapis.com/google.iam.admin.v1.CreateServiceAccountKeyRequest",
          **"name" : "projects/-/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com"**
        },
        "resourceName": "projects/-/serviceAccounts/123456789012345678901"
      },
      "resource": {
        "type": "service_account"
      }
    }

### Logs for authenticating with a service account key

After you create a service account key, you can use the key to [request an OAuth 2.0 access token for a service account](https://developers.google.com/identity/protocols/oauth2/service-account#authorizingrequests), then use the access token to authenticate requests to Google Cloud services. In general, the audit logs for those services include the following information:

  * `protoPayload.authenticationInfo.principalEmail`: The email address of the service account that the access token represents.
  * `protoPayload.authenticationInfo.serviceAccountKeyName`: The service account key that was used to request the OAuth 2.0 access token. This field identifies the service account key by its [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names), which uses the format `//iam.googleapis.com/projects/project-id/serviceAccounts/service-account-email/keys/key-id`.

**Note:** Some Google Cloud services, including App Engine and Compute Engine, do not log the service account key name.

The following example shows an audit log entry for a request to create a Memorystore for Redis instance. The request was authenticated with an OAuth 2.0 access token for a service account. In this example, the service account is named `my-service-account@my-project.iam.gserviceaccount.com`, and the service account key ID is `c71e040fb4b71d798ce4baca14e15ab62115aaef`:
    
    
    {
      "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "my-service-account@my-project.iam.gserviceaccount.com",
          **"serviceAccountKeyName" : "//iam.googleapis.com/projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/c71e040fb4b71d798ce4baca14e15ab62115aaef"**
        },
        "methodName": "google.cloud.redis.v1.CloudRedis.CreateInstance",
        "request": {
          "@type": "type.googleapis.com/google.cloud.redis.v1.CreateInstanceRequest"
        }
      }
    }

## Logs for impersonating a service account to access Google Cloud

This section shows the log entries you receive when you create short-lived credentials for a service account, then use the credentials to impersonate the service account and access Google Cloud.

### Logs for creating short-lived credentials

If you have the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) for a service account, you can [create short-lived credentials](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) for the service account, then use the credentials to impersonate the service account. For example, you might create short-lived credentials to call a Google Cloud API from an application that does not run on Google Cloud.

IAM can generate audit logs when principals create short-lived credentials. To receive these audit logs, you must [enable IAM audit logs for Data Access activity](https://docs.cloud.google.com/iam/docs/audit-logging#enabling_audit_logging).

After you enable IAM audit logs for Data Access activity, IAM generates an audit log entry each time a principal creates short-lived credentials. The entry includes the following fields:

  * `protoPayload.authenticationInfo.principalEmail`: The principal that created the short-lived credentials.
  * `resource.labels.email_id`: The service account for which short-lived credentials were generated.



The following example shows an audit log entry for a request to generate a short-lived OAuth 2.0 access token. In this example, the user `example-user@example.com` created an access token for the service account `my-service-account@my-project.iam.gserviceaccount.com`:
    
    
    {
      "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Fdata_access",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : "example-user@example.com"**
        },
        "methodName": "GenerateAccessToken",
        "request": {
          "@type": "type.googleapis.com/google.iam.credentials.v1.GenerateAccessTokenRequest",
          "name": "projects/-/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com"
        },
        "serviceName": "iamcredentials.googleapis.com"
      },
      "resource": {
        "labels": {
          **"email_id" : "my-service-account@my-project.iam.gserviceaccount.com",**
          "project_id": "my-project",
          "unique_id": "123456789012345678901"
        },
        "type": "service_account"
      }
    }

### Logs for authenticating with short-lived credentials

After you create short-lived credentials for a service account, you can use the credentials to impersonate the service account when you call Google Cloud APIs.

Some of the methods you call might generate audit logs. In general, these log entries show the following identities:

  * The service account that the short-lived credentials are impersonating
  * The identity that created the short-lived credentials



**Note:** Some Google Cloud services, including App Engine and Google Kubernetes Engine, do not log the identity that created the short-lived credentials. 

For example, suppose that the user `example-user@example.com` creates short-lived credentials for the service account `my-service-account@my-project.iam.gserviceaccount.com`. The user then creates a new Pub/Sub topic, using the short-lived credentials to impersonate the service account. Pub/Sub generates a log entry that identifies the service account, as well as the user who is impersonating the service account:
    
    
    {
      "logName": "projects/my-project/logs/cloudaudit.googleapis.com%2Factivity",
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          **"principalEmail" : "my-service-account@my-project.iam.gserviceaccount.com",**
          "serviceAccountDelegationInfo": [
            {
              "firstPartyPrincipal": {
                **"principalEmail" : "example-user@example.com"**
              }
            }
          ]
        },
        "methodName": "google.pubsub.v1.Publisher.CreateTopic",
        "request": {
          "@type": "type.googleapis.com/google.pubsub.v1.Topic",
          "name": "projects/my-project/topics/my-topic"
        },
        "resourceName": "projects/my-project/topics/my-topic"
      },
      "resource": {
        "type": "pubsub_topic"
      }
    }

## Logs for actions taken by service agents

Sometimes, when a principal initiates an operation, a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agent) executes an action on the principal's behalf. However, when you're reviewing audit logs for a service agent, it can be hard to tell who the service agent was acting on behalf of, and why. 

To help you understand the context for a service agent's actions, some service agents include additional details in their audit logs, like the job the action is associated with and the principal that created the job. 

The following service agents include these additional details in their audit logs: 

  * [BigQuery Connection Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#bigquery-connection-service-agent)
  * [BigQuery Connection Delegation Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#bigquery-connection-delegation-service-agent)



These additional details are in the `serviceDelegationHistory` field of the audit log, which is nested in the `authenticationInfo` field. This field contains the following information: 

  * The original principal who created the job
  * The service agent that executed the action
  * The service that the service agent belongs to
  * The job ID



For example, suppose `example-user@example.com` creates a job using the BigQuery Connection API. This job requires one of the BigQuery Connection API's service agents to execute an action. In this case, the audit log for the service agent's action would contain a `serviceDelegationHistory` field similar to the following: 
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "bqcx-442188550395-jujw@gcp-sa-bigquery-condel.iam.gserviceaccount.com",
          **"serviceDelegationHistory" : {
            "originalPrincipal": "user:my-user@example.com",
            "serviceMetadata": [
              {
                "principalSubject": "serviceAccount:bqcx-442188550395-jujw@gcp-sa-bigquery-condel.iam.gserviceaccount.com",
                "serviceDomain": "bigquery.googleapis.com",
              }
            ]
          }**
        }
      }
    }

## What's next

  * [Configure and view the audit logs](https://docs.cloud.google.com/iam/docs/audit-logging) for IAM.
  * Get more information about [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).
  * Learn about [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).
  * [Create and manage service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  * [Create short-lived credentials](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) for impersonating service accounts.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
