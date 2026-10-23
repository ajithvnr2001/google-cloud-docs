---
url: https://docs.cloud.google.com/looker/docs/looker-core-tls-cipher-suites/
title: Restrict TLS cipher suites on a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:23.115616+00:00
---

# Restrict TLS cipher suites on a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-tls-cipher-suites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Restrict TLS cipher suites on a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud supports multiple TLS cipher suites. To meet security or compliance requirements, you may want to deny requests from clients that use less secure TLS cipher suites.

The [`gcp.restrictTLSCipherSuites`](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-cipher-suites) organization policy constraint provides this capability.

## Before you begin

To get the permissions that you need to set, change, or delete organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Setting the organization policy

The `gcp.restrictTLSCipherSuites` organization policy constraint can be applied to Looker (Google Cloud core) instances that use a [public IP networking configuration](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections).

You can apply the constraint before or after you create the instance.

Follow the instructions on the [Restrict TLS cipher suites](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-cipher-suites#restrict) documentation page to set the organization policy. Looker (Google Cloud core) is compliant with the Google-managed [MODERN SSL policy profile](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#defining_an_ssl_policy) and supports the cipher suites that are in that profile.

If you set or change the organization policy after the Looker (Google Cloud core) instance is created, you must perform one of the following actions to apply the organization policy update to the Looker (Google Cloud core) instance:

  * [Restart](https://docs.cloud.google.com/looker/docs/looker-core-delete-restart#restart_a_instance) the instance.
  * [Edit](https://docs.cloud.google.com/looker/docs/looker-core-view-console#config_edit) a Looker (Google Cloud core) setting within the Google Cloud console or through the `gcloud` CLI.



## Policy violations

If you set the organization policy restraint to allow no [MODERN cipher suites](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#defining_an_ssl_policy) supported by Looker (Google Cloud core), you will be unable to create, update, or restart the Looker (Google Cloud core) instance and will receive the following error:
    
    
    com.google.apps.framework.request.FailedPreconditionException:
    Constraint`constraints/gcp.restrictTLSCipherSuites` is violated for resource
    `resourcemanager_projects``PROJECT_ID` Code: FAILED_PRECONDITION

This output includes the `PROJECT_ID` value, which is the ID of the project that is hosting the Looker (Google Cloud core) instance.

To address the violation, update the `gcp.restrictTLSCipherSuites` organization policy to allow at least one supported cipher suite.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
