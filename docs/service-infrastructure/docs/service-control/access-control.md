---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/access-control/
title: Service Control API Access Control \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:26.803952+00:00
---

# Service Control API Access Control  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Service Control API Access Control Stay organized with collections  Save and categorize content based on your preferences. 

To invoke the Service Control API for a [managed service](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed), the caller must have the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) permissions on the service:

  * [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check) requires permission `servicemanagement.services.check`.
  * [`services.report`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report) requires permission `servicemanagement.services.report`.
  * [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) requires permission `servicemanagement.services.quota`.



The IAM roles `roles/servicemanagement.serviceController`, `roles/owner` and `roles/editor` include these permissions and can each be used to grant them. We recommend using the IAM role `roles/servicemanagement.serviceController` to run your managed services. While `roles/owner` and `roles/editor` also grant these permissions, the narrower role is better for security reasons.

## Resource model

IAM applies IAM policies on resources to control who can perform what actions on the resources. The Service Control API uses the following resources to provide its functionality:

  * **Service producer project** : A [service producer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer) project may own zero or more managed services. The service producer project is the parent of services in this hierarchy.
  * **Managed service** : A managed service may have zero or more [service consumers](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer).
  * **Service consumer** : A [service consumer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer) refers to a Google Cloud project that has enabled the service.



The IAM access control is applied to the resource model. If a role is granted at the service producer project level, it affects all managed services owned by the producer project. If a role is granted at the managed service level, it affects all service consumers of the managed service.

It is highly recommended that you only create one managed service per service producer project for security and isolation reasons. Otherwise, for example, if the service producer project runs out of quota for sending requests to the Service Control API, multiple managed services will be impacted.

If you have a multi-tenant service, you should grant the role `roles/servicemanagement.serviceController` at the managed service level. If you have a single-tenant service, in other words, a service where each service consumer gets its own instance of your managed service, you should grant the role at the service consumer level. For background data processing that affects all service consumers, you should grant the role at the managed service level.

## Grant roles

To call the Service Control API, you must grant the necessary roles to the callers. You can grant the roles via one of the following three approaches. You need to be an owner of the service producer project so that you can grant the necessary roles.

### Grant a role at the service producer project level

You can grant the necessary roles on the project that a managed service belongs to, following the instructions in [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access), or use the Google Cloud CLI [add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command to grant the roles.

For example, you can grant the roles to a service account, such as `foo@developer.gserviceaccount.com`:
    
    
    gcloud projects add-iam-policy-binding PRODUCER_PROJECT_ID --member serviceAccount:SERVICE_ACCOUNT --role roles/servicemanagement.serviceController
    

Similarly, you can grant the roles to a user account, such as `bar@gmail.com`:
    
    
    gcloud projects add-iam-policy-binding PRODUCER_PROJECT_ID --member user:USER_ACCOUNT --role roles/servicemanagement.serviceController
    

### Grant a role at the service level

You can grant the role `roles/servicemanagement.serviceController` at the service level using `curl`. The following example uses the `gcurl` alias, which you define by running the following `alias` command with authentication token:
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    

**Warning:** **The following example replaces all existing service-level IAM policies.** To grant the new role in addition to your existing IAM settings, you must include all existing IAM policies in the request body in addition to the new role.
    
    
    gcurl -d "{
      'policy': {
        'bindings': [ {
          role: 'roles/servicemanagement.serviceController',
          members: 'serviceAccount:SERVICE_ACCOUNT'
        } ]
      }
    }" https://servicemanagement.googleapis.com/v1/services/YOUR_SERVICE_NAME:setIamPolicy
    

### Grant a role at the service consumer level

You can grant the role `roles/servicemanagement.serviceController` at the service consumer level. Service consumer level permissions require that the request to the Service Control API must contain at least one valid service consumer project ID. The following example uses the `gcurl` alias, which you define by running the following `alias` command with authentication token:
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    

**Warning:** **The following example replaces all existing consumer project level IAM policies.** To grant the new role in addition to your existing IAM settings, you must include all existing IAM policies in the request body in addition to the new role.
    
    
    gcurl -d "{
      'policy': {
        'bindings': [ {
          role: 'roles/servicemanagement.serviceController',
          members: 'serviceAccount:SERVICE_ACCOUNT'
        } ]
      }
    }" https://servicemanagement.googleapis.com/v1/services/YOUR_SERVICE_NAME/consumers/CONSUMER_PROJECT_NUMBER:setIamPolicy
    

For more information, see [Cloud Auth Guide](https://docs.cloud.google.com/docs/authentication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
