---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite/
title: Pub/Sub Lite roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:56.150568+00:00
---

# Pub/Sub Lite roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Pub/Sub Lite roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Pub/Sub Lite. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Pub/Sub Lite roles

Role | Permissions  
---|---  
  
#### Pub/Sub Lite Admin 

(`roles/pubsublite.admin`) Full access to topics, subscriptions and reservations.  |  `pubsublite.*`

  * `pubsublite.locations.openKafkaStream`
  * `pubsublite.operations.get`
  * `pubsublite.operations.list`
  * `pubsublite.reservations.attachTopic`
  * `pubsublite.reservations.create`
  * `pubsublite.reservations.delete`
  * `pubsublite.reservations.get`
  * `pubsublite.reservations.list`
  * `pubsublite.reservations.listTopics`
  * `pubsublite.reservations.update`
  * `pubsublite.subscriptions.create`
  * `pubsublite.subscriptions.delete`
  * `pubsublite.subscriptions.get`
  * `pubsublite.subscriptions.getCursor`
  * `pubsublite.subscriptions.list`
  * `pubsublite.subscriptions.seek`
  * `pubsublite.subscriptions.setCursor`
  * `pubsublite.subscriptions.subscribe`
  * `pubsublite.subscriptions.update`
  * `pubsublite.topics.computeHeadCursor`
  * `pubsublite.topics.computeMessageStats`
  * `pubsublite.topics.computeTimeCursor`
  * `pubsublite.topics.create`
  * `pubsublite.topics.delete`
  * `pubsublite.topics.get`
  * `pubsublite.topics.getPartitions`
  * `pubsublite.topics.list`
  * `pubsublite.topics.listSubscriptions`
  * `pubsublite.topics.publish`
  * `pubsublite.topics.subscribe`
  * `pubsublite.topics.update`

  
  
#### Pub/Sub Lite Editor 

(`roles/pubsublite.editor`) Modify topics, subscriptions and reservations, publish and consume messages.  |  `pubsublite.*`

  * `pubsublite.locations.openKafkaStream`
  * `pubsublite.operations.get`
  * `pubsublite.operations.list`
  * `pubsublite.reservations.attachTopic`
  * `pubsublite.reservations.create`
  * `pubsublite.reservations.delete`
  * `pubsublite.reservations.get`
  * `pubsublite.reservations.list`
  * `pubsublite.reservations.listTopics`
  * `pubsublite.reservations.update`
  * `pubsublite.subscriptions.create`
  * `pubsublite.subscriptions.delete`
  * `pubsublite.subscriptions.get`
  * `pubsublite.subscriptions.getCursor`
  * `pubsublite.subscriptions.list`
  * `pubsublite.subscriptions.seek`
  * `pubsublite.subscriptions.setCursor`
  * `pubsublite.subscriptions.subscribe`
  * `pubsublite.subscriptions.update`
  * `pubsublite.topics.computeHeadCursor`
  * `pubsublite.topics.computeMessageStats`
  * `pubsublite.topics.computeTimeCursor`
  * `pubsublite.topics.create`
  * `pubsublite.topics.delete`
  * `pubsublite.topics.get`
  * `pubsublite.topics.getPartitions`
  * `pubsublite.topics.list`
  * `pubsublite.topics.listSubscriptions`
  * `pubsublite.topics.publish`
  * `pubsublite.topics.subscribe`
  * `pubsublite.topics.update`

  
  
#### Pub/Sub Lite Viewer 

(`roles/pubsublite.viewer`) View topics, subscriptions and reservations.  |  `pubsublite.operations.*`

  * `pubsublite.operations.get`
  * `pubsublite.operations.list`

`pubsublite.reservations.get` `pubsublite.reservations.list` `pubsublite.reservations.listTopics` `pubsublite.subscriptions.get` `pubsublite.subscriptions.getCursor` `pubsublite.subscriptions.list` `pubsublite.topics.get` `pubsublite.topics.getPartitions` `pubsublite.topics.list` `pubsublite.topics.listSubscriptions`  
  
#### Pub/Sub Lite Publisher 

(`roles/pubsublite.publisher`) Publish messages to a topic.  |  `pubsublite.locations.openKafkaStream` `pubsublite.topics.getPartitions` `pubsublite.topics.publish`  
  
#### Pub/Sub Lite Subscriber 

(`roles/pubsublite.subscriber`) Subscribe to and read messages from a topic.  |  `pubsublite.locations.openKafkaStream` `pubsublite.operations.get` `pubsublite.subscriptions.getCursor` `pubsublite.subscriptions.seek` `pubsublite.subscriptions.setCursor` `pubsublite.subscriptions.subscribe` `pubsublite.topics.computeHeadCursor` `pubsublite.topics.computeMessageStats` `pubsublite.topics.computeTimeCursor` `pubsublite.topics.getPartitions` `pubsublite.topics.subscribe`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Pub/Sub Lite Service Agent 

(`roles/pubsublite.serviceAgent`) Grants Pub/Sub Lite Service Agent access to project resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `pubsub.topics.publish` `pubsublite.subscriptions.get` `pubsublite.subscriptions.getCursor` `pubsublite.subscriptions.setCursor` `pubsublite.subscriptions.subscribe` `pubsublite.topics.computeHeadCursor` `pubsublite.topics.getPartitions` `pubsublite.topics.publish` `pubsublite.topics.subscribe`  
  
## Pub/Sub Lite permissions

Permission | Included in roles  
---|---  
  
#### `pubsublite.locations.openKafkaStream`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.publisher) (`roles/pubsublite.publisher`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)   
  
#### `pubsublite.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)   
  
#### `pubsublite.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `pubsublite.reservations.attachTopic`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.reservations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.reservations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.reservations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `pubsublite.reservations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `pubsublite.reservations.listTopics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `pubsublite.reservations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.subscriptions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.subscriptions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.subscriptions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 

  
  
#### `pubsublite.subscriptions.getCursor`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 

  
  
#### `pubsublite.subscriptions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `pubsublite.subscriptions.seek`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)   
  
#### `pubsublite.subscriptions.setCursor`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 

  
  
#### `pubsublite.subscriptions.subscribe`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 

  
  
#### `pubsublite.subscriptions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.topics.computeHeadCursor`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 

  
  
#### `pubsublite.topics.computeMessageStats`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)   
  
#### `pubsublite.topics.computeTimeCursor`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)   
  
#### `pubsublite.topics.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.topics.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
#### `pubsublite.topics.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `pubsublite.topics.getPartitions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.publisher) (`roles/pubsublite.publisher`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 

  
  
#### `pubsublite.topics.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `pubsublite.topics.listSubscriptions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.viewer) (`roles/pubsublite.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `pubsublite.topics.publish`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Pub/Sub Lite Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.publisher) (`roles/pubsublite.publisher`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 
  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 

  
  
#### `pubsublite.topics.subscribe`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Pub/Sub Lite Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.subscriber) (`roles/pubsublite.subscriber`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Pub/Sub Lite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.serviceAgent) (`roles/pubsublite.serviceAgent`) 

  
  
#### `pubsublite.topics.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Pub/Sub Lite Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.admin) (`roles/pubsublite.admin`)  [Pub/Sub Lite Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsublite#pubsublite.editor) (`roles/pubsublite.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
