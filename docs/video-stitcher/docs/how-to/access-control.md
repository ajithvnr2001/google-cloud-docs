---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/access-control/
title: Access control with IAM \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:10.922519+00:00
---

# Access control with IAM  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/access-control/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

The Video Stitcher API uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) for access control.

You can configure access control for the Video Stitcher API at the project level. For example, you can grant access for developers to list and get all CDN keys registered within a project.

For a detailed description of IAM and its features, see the [IAM documentation](https://docs.cloud.google.com/iam/docs). In particular, see the section on [managing IAM policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Every Video Stitcher API method requires the caller to have the necessary permissions. For more information, see Permissions and Roles.

## Permissions

This section summarizes the Video Stitcher API permissions that IAM supports.

### Required permissions

The following tables list the IAM permissions that are associated with the Video Stitcher API.

**Note:** Method names are shortened in the table so that each method's full name begins with `projects.locations`.CDN keys method | Required permissions  
---|---  
`cdnKeys.create` | `videostitcher.cdnKeys.create` on the parent Google Cloud project.  
`cdnKeys.delete` | `videostitcher.cdnKeys.delete` on the CDN key resource.  
`cdnKeys.get` | `videostitcher.cdnKeys.get` on the CDN key resource.  
`cdnKeys.list` | `videostitcher.cdnKeys.list` on the parent Google Cloud project.  
`cdnKeys.update` | `videostitcher.cdnKeys.update` on the CDN key resource.  
Live configs method | Required permissions  
---|---  
`liveConfigs.create` | `videostitcher.liveConfigs.create` on the parent Google Cloud project.  
`liveConfigs.delete` | `videostitcher.liveConfigs.delete` on the live config resource.  
`liveConfigs.get` | `videostitcher.liveConfigs.get` on the live config resource.  
`liveConfigs.list` | `videostitcher.liveConfigs.list` on the parent Google Cloud project.  
`liveConfigs.update` | `videostitcher.liveConfigs.update` on the live config resource.  
VOD configs method | Required permissions  
---|---  
`vodConfigs.create` | `videostitcher.vodConfigs.create` on the parent Google Cloud project.  
`vodConfigs.delete` | `videostitcher.vodConfigs.delete` on the VOD config resource.  
`vodConfigs.get` | `videostitcher.vodConfigs.get` on the VOD config resource.  
`vodConfigs.list` | `videostitcher.vodConfigs.list` on the parent Google Cloud project.  
`vodConfigs.update` | `videostitcher.vodConfigs.update` on the VOD config resource.  
Slates method | Required permissions  
---|---  
`slates.create` | `videostitcher.slates.create` on the parent Google Cloud project.  
`slates.delete` | `videostitcher.slates.delete` on the slate resource.  
`slates.get` | `videostitcher.slates.get` on the slate resource.  
`slates.list` | `videostitcher.slates.list` on the parent Google Cloud project.  
`slates.update` | `videostitcher.slates.update` on the slate resource.  
Live sessions method | Required permissions  
---|---  
`liveSessions.create` | `videostitcher.liveSessions.create` on the parent Google Cloud project.  
`liveSessions.get` | `videostitcher.liveSessions.get` on the live session resource.  
Live ad tag details method | Required permissions  
---|---  
`liveSessions.liveAdTagDetails.get` | `videostitcher.liveAdTagDetails.get` on the live ad tag detail resource.  
`liveSessions.liveAdTagDetails.list` | `videostitcher.liveAdTagDetails.list` on the parent Google Cloud project.  
VOD sessions method | Required permissions  
---|---  
`vodSessions.create` | `videostitcher.vodSessions.create` on the parent Google Cloud project.  
`vodSessions.get` | `videostitcher.vodSessions.get` on the VOD session resource.  
VOD ad tag details method | Required permissions  
---|---  
`vodSessions.vodAdTagDetails.get` | `videostitcher.vodAdTagDetails.get` on the VOD ad tag detail resource.  
`vodSessions.vodAdTagDetails.list` | `videostitcher.vodAdTagDetails.list` on the parent Google Cloud project.  
VOD stitch details method | Required permissions  
---|---  
`vodSessions.vodStitchDetails.get` | `videostitcher.vodStitchDetails.get` on the VOD stitch detail resource.  
`vodSessions.vodStitchDetails.list` | `videostitcher.vodStitchDetails.list` on the parent Google Cloud project.  
  
## Roles

The following table lists the Video Stitcher API IAM roles, including the permissions associated with each role:

IAM role | Permissions  
---|---  
  
#### Video Stitcher Viewer 

(`roles/videostitcher.viewer`) Read-only access to video stitcher resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `videostitcher.cdnKeys.get` `videostitcher.cdnKeys.list` `videostitcher.liveAdTagDetails.*`

  * `videostitcher.liveAdTagDetails.get`
  * `videostitcher.liveAdTagDetails.list`

`videostitcher.liveConfigs.get` `videostitcher.liveConfigs.list` `videostitcher.liveSessions.get` `videostitcher.operations.get` `videostitcher.operations.list` `videostitcher.slates.get` `videostitcher.slates.list` `videostitcher.vodAdTagDetails.*`

  * `videostitcher.vodAdTagDetails.get`
  * `videostitcher.vodAdTagDetails.list`

`videostitcher.vodConfigs.get` `videostitcher.vodConfigs.list` `videostitcher.vodSessions.get` `videostitcher.vodStitchDetails.*`

  * `videostitcher.vodStitchDetails.get`
  * `videostitcher.vodStitchDetails.list`

  
  
#### Video Stitcher User 

(`roles/videostitcher.user`) Full access to video stitcher sessions.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `videostitcher.liveSessions.*`

  * `videostitcher.liveSessions.create`
  * `videostitcher.liveSessions.get`

`videostitcher.vodSessions.*`

  * `videostitcher.vodSessions.create`
  * `videostitcher.vodSessions.get`

  
  
#### Video Stitcher Admin 

(`roles/videostitcher.admin`) Full access to all video stitcher resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `videostitcher.*`

  * `videostitcher.cdnKeys.create`
  * `videostitcher.cdnKeys.createTagBinding`
  * `videostitcher.cdnKeys.delete`
  * `videostitcher.cdnKeys.deleteTagBinding`
  * `videostitcher.cdnKeys.get`
  * `videostitcher.cdnKeys.list`
  * `videostitcher.cdnKeys.listEffectiveTags`
  * `videostitcher.cdnKeys.listTagBindings`
  * `videostitcher.cdnKeys.update`
  * `videostitcher.liveAdTagDetails.get`
  * `videostitcher.liveAdTagDetails.list`
  * `videostitcher.liveConfigs.create`
  * `videostitcher.liveConfigs.createTagBinding`
  * `videostitcher.liveConfigs.delete`
  * `videostitcher.liveConfigs.deleteTagBinding`
  * `videostitcher.liveConfigs.get`
  * `videostitcher.liveConfigs.list`
  * `videostitcher.liveConfigs.listEffectiveTags`
  * `videostitcher.liveConfigs.listTagBindings`
  * `videostitcher.liveSessions.create`
  * `videostitcher.liveSessions.get`
  * `videostitcher.operations.cancel`
  * `videostitcher.operations.delete`
  * `videostitcher.operations.get`
  * `videostitcher.operations.list`
  * `videostitcher.slates.create`
  * `videostitcher.slates.createTagBinding`
  * `videostitcher.slates.delete`
  * `videostitcher.slates.deleteTagBinding`
  * `videostitcher.slates.get`
  * `videostitcher.slates.list`
  * `videostitcher.slates.listEffectiveTags`
  * `videostitcher.slates.listTagBindings`
  * `videostitcher.slates.update`
  * `videostitcher.vodAdTagDetails.get`
  * `videostitcher.vodAdTagDetails.list`
  * `videostitcher.vodConfigs.create`
  * `videostitcher.vodConfigs.createTagBinding`
  * `videostitcher.vodConfigs.delete`
  * `videostitcher.vodConfigs.deleteTagBinding`
  * `videostitcher.vodConfigs.get`
  * `videostitcher.vodConfigs.list`
  * `videostitcher.vodConfigs.listEffectiveTags`
  * `videostitcher.vodConfigs.listTagBindings`
  * `videostitcher.vodConfigs.update`
  * `videostitcher.vodSessions.create`
  * `videostitcher.vodSessions.get`
  * `videostitcher.vodStitchDetails.get`
  * `videostitcher.vodStitchDetails.list`

  
  
For more information about roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

### Recommendations

For the accounts responsible creating live or VOD sessions, the role should be set to `roles/videostitcher.user`.

For the accounts responsible for managing and editing CDN keys, live configs, VOD configs, and slates, the role should be set to `roles/videostitcher.admin`.

For the accounts with only access to view and not edit or create CDN keys, live configs, VOD configs, slates, or sessions, the role should be set to `roles/videostitcher.viewer`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
