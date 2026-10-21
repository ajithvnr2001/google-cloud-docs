---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/observe-quota-enforcement/
title: Observe quota enforcement \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:07:15.878723+00:00
---

# Observe quota enforcement  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/observe-quota-enforcement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Observe quota enforcement Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to observe quota enforcement. The Google Distributed Cloud (GDC) air-gapped quota system protects services by preventing unforeseen spikes in usage that might overload services. To help you understand how service quotas are configured and enforced, you can use the Library Agent service to observe quota behaviors, such as rate limiting.

The Library Agent service exposes two APIs:

  * **GetShelf** : Retrieves details for a specific shelf and is not rate-limited.
  * **ListShelves** : Retrieves a list of all shelves and has a rate limit of two requests per minute.



This page is for developers within the application operator group, who are responsible for monitoring quotas and usage patterns for their project. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before interacting with the Library Agent service, ensure you have the correct permissions and the service endpoint:

  1. To get the permissions you need to interact with the Library Agent service, ask your Project IAM Admin to grant you the **LibraryAgent User** role in your project namespace. For example, the Project IAM Admin can bind the `libraryagent-user` role to your user account in your project namespace by applying a `RoleBinding` resource:
         
         kubectl apply -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: libraryagent-user-binding
           namespace: PROJECT_NAMESPACE
         subjects:
         - kind: User
           name: USER_EMAIL_ADDRESS
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: Role
           name: libraryagent-user
           apiGroup: rbac.authorization.k8s.io
         EOF
         

Replace the following:

     * `PROJECT_NAMESPACE`: the namespace of your project, such as `project-123`.
     * `USER_EMAIL_ADDRESS`: the email address associated with your user identity.
  2. Ask a Platform Admin who has access to the org admin cluster and who has the DNS Monitor (`dns-monitor-mp`) role to obtain the DNS name for the Library Agent service:
         
         kubectl get dnsregistration.network.private.gdc.goog -n libraryagent-system libraryagent -o jsonpath='{.status.fqdn}'
         

If you require editing the DNS registration, the PA must also have the DNS Debugger (`dns-debugger-mp`) role.




## Observe quota limits

To interact with the Library Agent APIs and observe rate limiting, follow these steps:

  1. Set environment variables for the DNS name and your authentication token:
         
         export DNS_NAME=LIBRARY_AGENT_DNS_NAME
         export TOKEN="$($HOME/gdcloud auth print-identity-token --audiences=https://$DNS_NAME)"
         

Replace `LIBRARY_AGENT_DNS_NAME` with the DNS name you obtained earlier.

  2. Call the `GetShelf` API to fetch a specific shelf by name. This method has no rate limit:
         
         curl -v -X GET \
         -H "Authorization: Bearer ${TOKEN?}" \
         --insecure \
         https://$DNS_NAME/v1alpha1/projects/PROJECT_NAMESPACE/shelves/Shelf1
         

Replace `PROJECT_NAMESPACE` with your project namespace.

You receive an `HTTP 200 OK` response.

  3. Call the `ListShelves` API to list all shelves in a location that is reflected in the DNS name. This method is rate-limited to two requests per minute:
         
         curl -v -X GET \
         -H "Authorization: Bearer ${TOKEN?}" \
         --insecure \
         https://$DNS_NAME/v1alpha1/projects/PROJECT_NAMESPACE/shelves
         

Replace `PROJECT_NAMESPACE` with your project namespace.

If you are within the limit of two requests per minute, you receive an `HTTP 200 OK` response.

  4. To observe quota enforcement, call the `ListShelves` API repeatedly until you exceed the rate limit:
         
         curl -v -X GET \
         -H "Authorization: Bearer ${TOKEN?}" \
         --insecure \
         https://$DNS_NAME/v1alpha1/projects/PROJECT_NAMESPACE/shelves
         

Replace `PROJECT_NAMESPACE` with your project namespace.

When you exceed the limit, you receive an `HTTP 429 Too Many Requests` response, indicating that the request was rate-limited by the quota system. The output is similar to the following:
         
         * Request completely sent off
         < HTTP/2 429
         < x-envoy-ratelimited: true
         < date: Thu, 24 Apr 2025 18:37:16 GMT
         < server: istio-envoy
         < x-envoy-upstream-service-time: 46
         <
         * Connection #0 to host libraryagent.org-1.zone1.google.gdch.test left intact
         

Rate limit enforcement is not always precise; it might take more than two requests in one minute to trigger the 429 error.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
