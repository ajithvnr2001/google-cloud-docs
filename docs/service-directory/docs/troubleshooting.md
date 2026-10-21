---
url: https://docs.cloud.google.com/service-directory/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:13.193179+00:00
---

# Troubleshooting  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

## Why do I get a `not found` error when adding an endpoint?

If you are getting 404 errors when adding services or endpoints, ensure that you have created both the namespace and the service (in that order) before adding an endpoint. The service must exist before you can add additional endpoints.

## When I look up a service, why don't I get any of my endpoints?

Ensure that the project, region, namespace name, and service name are all correct in your request and match where you registered the endpoints. All Service Directory services live in a regional namespace, so services registered with one region do not match data in a separate region.

## I granted someone access to a service but they continue to get `permission denied`.

This could be for a couple of reasons. First, check that the region is correct. If you set a policy on a namespace or service, the policy only applies to that particular region. If the user is trying to register or lookup the same service in another region, they won't have access unless you grant them IAM access to that regional service as well. To debug access issues, try the [`TestIamPermissions`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions) method for services and namespaces.

## I added some endpoints and then removed the service backend. Why are the endpoints still there?

Service Directory does not do automatic health-checking or heartbeating, and does not remove endpoints unless you explicitly remove them. Ensure that you add code to your service backends/orchestrators that remove the endpoint from Service Directory once it no longer exists. We recommend the use of time-to-live annotation fields on endpoints to record the last time an endpoint was registered or updated.

## I am able to look up endpoints but every time I try to connect to them, it fails.

Service Directory does not ensure the reachability from the client. Services register their endpoints directly with Service Directory. However, the address registered with Service Directory may not be routable (especially if both the client and the server are on separate private networks). If the endpoint is routable from the client, then it could be due to an unhealthy endpoint. See the following question.

## How can I add health data for endpoints so that my clients know which one to connect to?

When using client-side load balancing, we recommend that service backends occasionally update an annotation field on the endpoint that clients can use to make decisions on which backend to connect to. Service Directory does not inspect or evaluate this data.

## I've created a namespace. Why can't I assign a Cloud DNS private zone to it?

Ensure that you have the `servicedirectory.namespaces.associatePrivateZone` IAM permission for the namespace as this permission lets you create the associated private zone. By default, the Project Editor, Project Owner, Service Directory Admin, and Service Directory Editor roles have this permission.

## When I do a DNS lookup of a service, why don't I get any of my endpoints?

There could be several reasons, such as the following:

  1. The associated namespace has been deleted. You can check this by running the [`get`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/get) command on the private zone. If the `serviceDirectoryConfig.deletionTime` is set, then the associated namespace and all of its endpoints have been deleted.
  2. Confirm that you are issuing the request from a network that is allowed to query the private zone. You can find the network list by running the [`get`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/get) command on the private zone.
  3. There are no (valid) endpoints for the service. Run the [`resolve`](https://docs.cloud.google.com/service-directory/docs/reference/rest/v1beta1/projects.locations.namespaces.services/resolve) command on the service through the Service Directory API to ensure that the service is not empty and has at least one valid endpoint IP. DNS support is only available for endpoints with valid IPv4 or IPv6 IP addresses.
  4. Make sure that you're querying the correct zone. For example, suppose that you create a Service Directory zone called **example.com** , and you have another (standard) private zone named **billing.example.com**. Then any DNS query to **billing.example.com** returns resource records that belong to the **billing.example.com** zone, and not the **billing** service in the Service Directory namespace that is associated with **example.com.** For more information, see [Name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order).



## Why are my GKE services not syncing to Service Directory?

There could be several reasons, such as the following:

  1. Confirm that you have a `ServiceDirectoryRegistrationPolicy` deployed in your GKE cluster for the namespace that you are trying to sync. Also, confirm that the services you are trying to sync match the label selector in your policy.
  2. There is already an existing Service Directory namespace that was created manually or by using some other integration with the same name as the GKE namespace you are trying to sync. You must rename or delete your existing Service Directory namespace so that there are no conflicts.
  3. Permissions from your Service Directory Service Account were removed. Make sure that `service-{PROJECT_NUMBER}@gcp-sa-servicedirectory.iam.gserviceaccount.com` has the `Service Directory Service Agent` IAM permission. For details about IAM, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).



## What's next

  * To learn more about features, see [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To get additional help, see [Get support](https://docs.cloud.google.com/service-directory/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
