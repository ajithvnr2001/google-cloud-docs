---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile
title: Cloud Bigtable V2 Client - Class AppProfile (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:32.363485+00:00
---

# Cloud Bigtable V2 Client - Class AppProfile (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class AppProfile (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class AppProfile.

A configuration object describing how Cloud Bigtable should treat traffic from a particular end user application.

Generated from protobuf message `google.bigtable.admin.v2.AppProfile`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`.  
`↳ etag` |  `string`   
Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.  
`↳ description` |  `string`   
Long form description of the use case for this AppProfile.  
`↳ multi_cluster_routing_use_any` |  `[AppProfile\MultiClusterRoutingUseAny](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.MultiClusterRoutingUseAny)`   
Use a multi-cluster routing policy.  
`↳ single_cluster_routing` |  `[AppProfile\SingleClusterRouting](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.SingleClusterRouting)`   
Use a single-cluster routing policy.  
`↳ priority` |  `int`   
This field has been deprecated in favor of `standard_isolation.priority`. If you set this field, `standard_isolation.priority` will be set instead. The priority of requests sent using this app profile.  
`↳ standard_isolation` |  `[AppProfile\StandardIsolation](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.StandardIsolation)`   
The standard options used for isolating this app profile's traffic from other use cases.  
`↳ data_boost_isolation_read_only` |  `[AppProfile\DataBoostIsolationReadOnly](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.DataBoostIsolationReadOnly)`   
Specifies that this app profile is intended for read-only usage via the Data Boost feature.  
  
### getName

The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply.

See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply.

See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Long form description of the use case for this AppProfile.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Long form description of the use case for this AppProfile.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMultiClusterRoutingUseAny

Use a multi-cluster routing policy.

**Returns**  
---  
**Type** | **Description**  
`[AppProfile\MultiClusterRoutingUseAny](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.MultiClusterRoutingUseAny)|null` |   
  
### hasMultiClusterRoutingUseAny

### setMultiClusterRoutingUseAny

Use a multi-cluster routing policy.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AppProfile\MultiClusterRoutingUseAny](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.MultiClusterRoutingUseAny)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSingleClusterRouting

Use a single-cluster routing policy.

**Returns**  
---  
**Type** | **Description**  
`[AppProfile\SingleClusterRouting](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.SingleClusterRouting)|null` |   
  
### hasSingleClusterRouting

### setSingleClusterRouting

Use a single-cluster routing policy.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AppProfile\SingleClusterRouting](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.SingleClusterRouting)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPriority

This field has been deprecated in favor of `standard_isolation.priority`.

If you set this field, `standard_isolation.priority` will be set instead. The priority of requests sent using this app profile.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Priority](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.Priority).  
  
### hasPriority

### setPriority

This field has been deprecated in favor of `standard_isolation.priority`.

If you set this field, `standard_isolation.priority` will be set instead. The priority of requests sent using this app profile.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Priority](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.Priority).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStandardIsolation

The standard options used for isolating this app profile's traffic from other use cases.

**Returns**  
---  
**Type** | **Description**  
`[AppProfile\StandardIsolation](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.StandardIsolation)|null` |   
  
### hasStandardIsolation

### setStandardIsolation

The standard options used for isolating this app profile's traffic from other use cases.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AppProfile\StandardIsolation](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.StandardIsolation)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataBoostIsolationReadOnly

Specifies that this app profile is intended for read-only usage via the Data Boost feature.

**Returns**  
---  
**Type** | **Description**  
`[AppProfile\DataBoostIsolationReadOnly](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.DataBoostIsolationReadOnly)|null` |   
  
### hasDataBoostIsolationReadOnly

### setDataBoostIsolationReadOnly

Specifies that this app profile is intended for read-only usage via the Data Boost feature.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AppProfile\DataBoostIsolationReadOnly](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.DataBoostIsolationReadOnly)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRoutingPolicy

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### getIsolation

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
