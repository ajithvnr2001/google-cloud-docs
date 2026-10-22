---
url: https://docs.cloud.google.com/iam/docs/best-practices-for-using-service-accounts-in-deployment-pipelines/
title: Best practices for using service accounts in pipelines \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:01.014391+00:00
---

# Best practices for using service accounts in pipelines  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/best-practices-for-using-service-accounts-in-deployment-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Best practices for using service accounts in pipelines Stay organized with collections  Save and categorize content based on your preferences. 

Deployment pipelines let you automate the process of taking code or pre-built artifacts and deploying them to a Google Cloud environment, and they can be an alternative to using interactive tools like the Google Cloud console or the Google Cloud CLI.

Deployment pipelines differ from interactive tools like the Google Cloud console or the gcloud CLI in the way they interact with Identity and Access Management, and you must take these differences into consideration when securing your Google Cloud resources.

Before Google Cloud lets you access a resource, it performs an access check. To perform this check, IAM typically considers:

  * Your identity and any associated Principal Access Boundary policies
  * The resource you're trying to access and its IAM allow and deny policies
  * The context of your request (possibly including time and location)



In a deployment pipeline, you rarely call Google Cloud APIs directly. Instead, you use tools to access Google Cloud resources. Tools like the Google Cloud console or the gcloud CLI require that you first _authorize_ the tool to access resources on your behalf. By providing this authorization, you give the tool permission to use _your_ identity when making API calls.

Like the Google Cloud console or the gcloud CLI, a deployment pipeline acts _on your behalf_ : it takes your changes, expressed as source code, and deploys them to Google Cloud. But unlike the Google Cloud console or the gcloud CLI, a deployment pipeline typically doesn't use your identity to perform the deployment:

  1. As a user, you typically don't interact with a deployment pipeline directly. Instead, you interact with a source control system (SCM) by pushing code changes to a source repository, or approving code reviews.

  2. The deployment pipeline reads submitted code changes from the SCM system and deploys them to Google Cloud.

To perform the deployment, the deployment pipeline typically can't use your identity because:

     1. The source code and its metadata might not indicate that you were the author, or the author information isn't tamper-proof (as in the case of unsigned Git commits)
     2. The identity you used to submit source code might be different from your identity for Google Cloud, and the two identities can't be mapped

Most deployment pipelines therefore perform deployments under their own identity by using a service account.

  3. When the deployment pipeline accesses Google Cloud, IAM allows or denies access solely based on the identity of the service account used by the pipeline, not the identity of your user account.




![Deployment pipeline](https://docs.cloud.google.com/static/iam/img/service-account-deployment-pipeline.svg)

Letting a deployment pipeline use a service account to access Google Cloud has some advantages:

  * The lifecycle of a service account is disconnected from the lifecycle of user accounts. By configuring a pipeline to use a service account, you ensure that code can be deployed even if the author of the code is no longer with your organization.
  * When you manage resources by using a deployment pipeline, you don't need to grant users any access to the resources, or you can limit permissions to read-only access. This approach can make it easier to manage IAM allow and deny policies and lets you force users to use the deployment pipeline to perform all modifications.



However, using a service account also introduces new threats. These include:

  * **Spoofing:** A bad actor could try to spoof the identity of the deployment pipeline or steal its credentials to gain access to resources.
  * **Privilege escalation** : The pipeline could be tricked into performing actions that it's not supposed to perform, effectively becoming a [_confused deputy_](https://wikipedia.org/wiki/Confused_deputy_problem).
  * **Non-repudiation:** After a pipeline has performed an operation, it might become difficult to reconstruct _why_ it was done, and which developer or code change it was triggered by.
  * **Tampering:** A pipeline could be abused for undermining the integrity or security controls of your cloud environments.
  * **Information disclosure:** Bad actors might attempt to use the deployment pipeline for exfiltrating confidential data.



## Protect against spoofing threats

To grant a deployment pipeline access to Google Cloud, you typically do the following:

  1. Create a service account
  2. Grant the service account access to the required resources
  3. Configure the deployment pipeline to use the service account



From an IAM perspective, the service account represents the deployment pipeline, but the deployment pipeline and the service account are two separate entities. If not secured properly, a bad actor might be able to use the same service account, which lets them "spoof" the identity of the deployment pipeline.

The following section describes best practices that can help you reduce the risk of such threats.

**Best practices** :

Avoid attaching service accounts to VM instances used by CI/CD systems.  
Use dedicated service accounts per deployment pipeline.  
Use Workload Identity Federation whenever possible.  
Use VPC Service Controls to reduce the impact of leaked credentials.  


### Avoid attaching service accounts to VM instances used by CI/CD systems

For applications deployed on Compute Engine that need access to Google Cloud resources, it's typically best to [attach a service account to the underlying VM instance](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#use-attached-service-accounts). For CI/CD systems that use Compute Engine VMs to run different deployment pipelines, this practice can be problematic if the same VM instance might be used to run different deployment pipelines that each require access to different resources.

Instead of using attached service accounts to let deployment pipelines access resources, let each deployment pipeline use a separate service account. Avoid attaching [a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) to VM instances used by CI/CD systems, or attach a service account that's limited to accessing essential services such as Cloud Logging only.

### Use dedicated service accounts per deployment pipeline

When you let multiple deployment pipelines use the same service account, IAM can't differentiate between the pipelines. The pipelines have access to the same resources, and audit logs might not contain sufficient information to determine which deployment pipeline triggered a resource to be accessed or changed.

To avoid such ambiguity, maintain a 1:1 relationship between deployment pipelines and service accounts. Create a dedicated service account for each deployment pipeline and make sure to do the following:

  * Incorporate the name or ID of the deployment pipeline into the service account's email address. Following a consistent naming scheme helps you determine which service accounts are connected to which deployment pipelines.
  * Only grant the service account access to the resources the specific deployment pipeline needs.



### Use Workload Identity Federation whenever possible

Some CI/CD systems like GitHub Actions or GitLab let deployment pipelines obtain OpenID Connect-compliant tokens that assert the identity of the deployment pipeline. You can let deployment pipelines use these tokens to impersonate a service account by [using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation).

Using Workload Identity Federation helps you avoid the [risks associated with using service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

### Use VPC Service Controls to reduce the impact of leaked credentials

If a bad actor manages to steal an access token or service account key from one of your deployment pipelines, they might attempt to use this credential and access your resources from a different machine that they control.

By default, IAM doesn't take the geolocation, source IP address, or origin Google Cloud project into account when making access decisions. A stolen credential might therefore be usable from anywhere.

You can impose restrictions on the sources from where your Google Cloud resources can be accessed by placing your projects in a [VPC service perimeter](https://docs.cloud.google.com/vpc-service-controls) and using [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules):

  * If your deployment pipeline runs on Google Cloud, you can configure an ingress rule to only allow access from the project that contains your CI/CD system.
  * If your deployment pipeline runs outside of Google Cloud, you can create an [access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) that only permits access from certain geo-locations or IP ranges. Then create an ingress rule that allows access for clients that satisfy this access level.

**Note:** Restricting access by IP range might be less effective or infeasible if you're using a Software as a Service (SaaS)-based system to run your deployment pipelines. This is because the source IP addresses used by SaaS providers may not be known in advance, or they might be shared across all their customers.

## Protect against tampering threats

For some data that you store on Google Cloud, you might find it particularly important to prevent unauthorized modification or deletion. If unauthorized modification or deletion is of particular concern, then you can characterize the data as high-integrity data.

To maintain the integrity of your data, you must ensure that the Google Cloud resources that you use to store and manage that data are configured securely, and must maintain their integrity.

Deployment pipelines can help you maintain the integrity of your data and resources, but they can also pose a risk: If the pipeline of one of its components doesn't meet the integrity requirements of the resources it manages, then the deployment pipeline turns into a weak spot that might enable bad actors to tamper with your data or resources.

The following section describes best practices that can help you reduce the risk of tampering threats.

**Best practices** :

Avoid letting deployment pipelines manage security controls.  


### Limit access to security controls

To ensure the security and integrity of your data and resources on Google Cloud, you use security controls such as:

  * Allow policies and deny policies
  * Organization policy constraints
  * VPC Service Controls perimeters, access levels, and ingress policies



These security controls are resources by themselves. Tampering with security controls endangers the integrity of the resources that the security controls apply to. As a result, you must consider the integrity of security controls to be at least as important as the integrity of the resources they apply to.

If you let a deployment pipeline manage security controls, then it's up to the deployment pipeline to maintain the integrity of security controls. As a result, you must consider the integrity of the deployment pipeline itself to be at least as important as the integrity of the security controls it manages, and the resources these controls apply to.

You can limit a deployment pipeline's impact on the integrity of your resources by doing the following:

  * Not granting deployment pipelines access to allow policies, deny policies, and other security controls, and restricting their access to other resources
  * Granting access to selected security controls only, such as the allow policies and deny policies of a specific resource or project, while not granting access to broader controls that affect multiple resources or projects



If your deployment pipeline, its components, and underlying infrastructure can't meet the integrity demands of certain security controls, it's best to avoid letting deployment pipelines manage these security controls.

## Protect against non-repudiation threats

At some point, you might notice suspicious activity affecting one of your resources on Google Cloud. In that event, you must be able to find out more about the activity and, ideally, be able to reconstruct the chain of events that led to it.

Cloud Audit Logs let you find out when resources were accessed or modified, and which users were involved. Although Cloud Audit Logs provide a starting point for analyzing suspicious activity, the information provided by these logs might not be sufficient: if you use deployment pipelines, you must also be able to correlate Cloud Audit Logs with logs produced by your deployment pipeline.

This section contains best practices that can help you maintain an audit trail across Google Cloud and your deployment pipelines.

**Best practices** :

Ensure that you can correlate deployment pipeline logs with Cloud Audit Logs.  
Align the retention periods of deployment pipeline logs and Cloud Audit Logs.  


### Ensure that you can correlate deployment pipeline logs with Cloud Audit Logs

Cloud Audit Logs contain timestamps and information about the user that initiated an activity. If you use a dedicated service account for each deployment pipeline, then this information lets you identify the deployment pipeline that initiated the activity and might also help you narrow down which code changes and pipeline runs could have been responsible. But identifying the exact pipeline run and code change that led to the activity can be difficult without more information that lets you correlate Cloud Audit Logs with the logs of your deployment pipeline.

You can enrich Cloud Audit Logs to contain more information in multiple ways, including:

  * When you use Terraform, specify a [request reason](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#request_reason) that indicates CI/CD pipeline run.
  * Add an `X-Goog-Request-Reason` [HTTP header](https://docs.cloud.google.com/apis/docs/system-parameters#definitions) to API requests and pass the ID of the deployment pipeline run.
  * Use a custom `User-Agent` that embeds the ID of the deployment pipeline run.



You can also enrich the logs emitted by your deployment pipeline:

  * Log API requests performed by each CI/CD pipeline run.
  * Whenever the API returns an operation ID, record the ID in the CI/CD system's logs.



### Align the retention periods of deployment pipeline logs and Cloud Audit Logs

To analyze suspicious activity related to a deployment pipeline, you typically need multiple types of logs, including [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity), [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access), and the logs of your deployment pipeline.

Cloud Logging only retains logs for a certain period of time. By default, this retention period is shorter for [Data Access audit logs](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) than for Admin Activity audit logs. The system that runs your deployment pipeline might also discard its logs after a certain time period. Depending on the nature of your deployment pipeline, and the importance of the resources that the deployment pipeline manages, these default retention periods might be insufficient or misaligned.

To ensure that logs are available when you need them, make sure that the log retention periods used by the different systems are aligned and sufficiently long.

If necessary, [customize the retention period](https://docs.cloud.google.com/logging/docs/buckets#custom-retention) for Data Access audit logs, or set up a custom [sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) to route logs to a custom storage location.

**Best practices** :

Avoid granting direct access to confidential data.  
Use VPC Service Controls to help prevent data exfiltration.  


## Protect against information disclosure threats

When a deployment pipeline's service account has access to confidential data, then a bad actor might attempt to use the deployment pipeline to exfiltrate that data. A deployment pipeline's access to data can be direct or indirect:

  * **Direct** : The deployment pipeline's service account might have permission to read confidential data from Cloud Storage, BigQuery, or other locations. This access might have been granted intentionally, but it might also be an accidental result of granting too much access.

If a bad actor gains access to a deployment pipeline with direct access to confidential data, they might try to use the service account's access token to access and exfiltrate the data.

  * **Indirect** : To deploy configuration or new software versions, a deployment pipeline's service account might have permission to create or redeploy compute resources, such as Compute Engine VM instances. Some of these resources might have an attached service account that grants access to confidential data.

In this situation, a bad actor might attempt to compromise the deployment pipeline so that it deploys malicious code to one of the compute resources, and let this code exfiltrate confidential data.




This section contains best practices that can help you limit the risk of disclosing confidential data.

### Avoid granting direct access to confidential data

To deploy infrastructure, configuration, or new software versions, a deployment pipeline often doesn't require access to existing data. Instead, it's often sufficient to limit access to resources that don't contain any data, or at least don't contain confidential data.

Ways to minimize access to existing, potentially confidential data include:

  * Instead of granting a deployment pipeline's service account access to an entire project, only grant access to specific resources.
  * Grant create access without allowing read access. For example, by granting the _Storage Object Creator_ role (`roles/storage.objectCreator`), you can allow a service account to upload new objects to a Cloud Storage bucket without granting permission to read existing data.
  * Limit infrastructure-as-code (IaC) to less-confidential resources—for example, use IaC for managing VM instances or networks, but not for managing confidential BigQuery datasets.



### Use VPC Service Controls to help prevent data exfiltration

You can reduce the risk of indirect data exfiltration by deploying your Google Cloud resources in a VPC Service Controls perimeter.

If your deployment pipeline runs outside of Google Cloud, or is part of a different perimeter, you can grant the pipeline's service account access to the perimeter by configuring an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). If possible, configure the ingress rule so that it only allows access from the IP addresses used by the deployment pipeline, and only permits access to the services that the deployment pipeline really needs.

## Protect against privilege escalation threats

When a deployment pipeline uses a service account to access Google Cloud resources, it does so irrespective of the developer or user who authored a code or configuration change. The disconnect between the pipeline's service account and the developer's identity makes deployment pipelines prone to [_confused deputy_](https://wikipedia.org/wiki/Confused_deputy_problem) attacks, in which a bad actor tricks the pipeline into performing an action that the bad actor isn't allowed to do themselves, and that the pipeline might not even be supposed to perform.

This section contains best practices that can help you reduce the risk of your deployment pipeline being abused for privilege escalation.

**Best practices** :

Limit access to the deployment pipeline and all inputs.  
Avoid letting a deployment pipeline modify policies.  
Don't reveal service account credentials in logs.  


### Limit access to the deployment pipeline and all inputs

Most deployment pipelines use a source code repository as their main source of input and might trigger automatically as soon as they detect a code change in certain branches (for example, the `main` branch). Deployment pipelines typically can't verify whether the code and configuration they find in the source code repository is authentic and trustworthy. The security of this architecture therefore depends on:

  * Controlling who can submit code and configuration to the repository and branches used by the deployment pipeline.
  * Enforcing criteria that must be met before changes can be committed—for example, successful code reviews, static analysis, or automated tests.



For these controls to be effective, you must also ensure that bad actors can't sidestep them by:

  * Modifying the configuration of the source code repository or the deployment pipeline.
  * Tampering with the infrastructure (such as VMs and storage) that underlies the deployment pipeline.
  * Modifying or replacing inputs outside of the source code repository, such as packages, container images, or libraries.



When managed by a deployment pipeline, your resources on Google Cloud can only be as secure as your deployment pipeline, its configuration, infrastructure, and inputs. Therefore, you must protect these components as well as you want your Google Cloud resources to be protected.

### Avoid letting a deployment pipeline modify policies

For most types of resources, IAM defines a `RESOURCE_TYPE.setIamPolicy` permission. This permission enables a user to modify a resource's allow policy, either to grant other users access or to modify and extend their own access. Unless constrained by a deny policy, granting a user or service account a `*.setIamPolicy` permission has the effect of granting them full access to the resource.

Whenever possible, avoid letting a deployment pipeline modify access to resources. When granting the pipeline's service account access to Google Cloud resources, use roles that don't include any `*.setIamPolicy` permission and avoid using the basic roles _Editor_ and _Owner_.

For some deployment pipelines, granting permission to modify allow policies or deny policies might be unavoidable: For example, a deployment pipeline's purpose might be to create new resources or manage access to existing resources. In these scenarios, you can still limit the extent to which the deployment can modify access by:

  * Only granting `*.setIamPolicy` permission for specific resources, and not for the entire project.
  * Using [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) to constrain the set of permissions that can be granted, or to limit which principals they can be granted to.
  * Using IAM Conditions [to restrict which roles the pipeline is allowed to grant](https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles), and only allowing roles that don't include `*.setIamPolicy` permissions.



### Don't reveal service account credentials in logs

The logs generated by a deployment pipeline are often accessible to a larger group of users, including users that don't have permission to modify the pipeline's configuration. It's possible that these logs accidentally reveal credentials by echoing the following:

  * Contents of environment variables
  * Command line arguments
  * Diagnostics output



If logs accidentally reveal credentials such as access tokens, then these credentials could be abused by bad actors to escalate their privileges. Ways to prevent logs from revealing credentials include the following:

  * Avoid passing access tokens or other credentials as command line arguments
  * Avoid storing credentials in environment variables
  * Configure your CI/CD system to automatically detect and mask tokens and other credentials if possible



## What's next

  * Learn more about [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) and [best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).
  * Review our [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations) and guidance on [authentication and authorization](https://docs.cloud.google.com/architecture/security-foundations/authentication-authorization).
  * Learn more about [best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
