---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardduty-changelog/
title: Change log for GUARDDUTY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:46.854180+00:00
---

# Change log for GUARDDUTY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardduty-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GUARDDUTY

Date | Changes  
---|---  
2026-09-29 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `dataVal.publicIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.detail.createdAt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `data.detail.updatedAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.creation_time`: Newly mapped `data.detail.resource.instanceDetails.launchTime` raw log field with `event.idm.read_only_udm.principal.resource.attribute.creation_time` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `data.detail.type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data.detail.service.action.portProbeAction.blocked` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `data.detail.service.eventFirstSeen` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.security_result.last_discovered_time`: Newly mapped `data.detail.service.eventLastSeen` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `data.detail.service.additionalInfo.packetsIn` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `data.detail.service.additionalInfo.packetsOut` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `dataVal.publicDnsName` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2026-09-03 |  Enhancement:  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `detail.resource.s3BucketDetails.0.s3ObjectDetails.key` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `detail.resource.s3BucketDetails.0.s3ObjectDetails.hash` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `detail.resource.s3BucketDetails.0.s3ObjectDetails.objectArn` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `detail.resource.s3BucketDetails.0.s3ObjectDetails.eTag`, `detail.resource.s3BucketDetails.0.name`, `detail.resource.s3BucketDetails.0.type`, `detail.resource.s3BucketDetails.0.publicAccess.effectivePermission`, `detail.resource.s3BucketDetails.0.owner.id`, `detail.resource.s3BucketDetails.0.defaultServerSideEncryption.encryptionType`, `detail.resource.s3BucketDetails.0.tags` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicAcls`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicPolicy`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.ignorePublicAcls`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.restrictPublicBuckets`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicReadAccess`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicWriteAccess`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicAcls`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicPolicy`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.ignorePublicAcls`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.restrictPublicBuckets`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicReadAccess`, `detail.resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicWriteAccess` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `detail.service.malwareScanDetails.threats.name` and `detail.service.malwareScanDetails.threats.source` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Newly mapped `detail.resource.resourceType` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field.   
2026-08-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.location.region_longitude`: Removed mapping of `service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon` from `event.idm.read_only_udm.principal.location.region_longitude`, since this field is deprecated.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Mapped `service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_latitude`: Removed mapping of `service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat` from `event.idm.read_only_udm.principal.location.region_latitude`, since this field is deprecated.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Mapped `service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `service.additionalInfo.recentCredentials.ipAddressV6` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.attribute.creation_time`: Mapped the `resource.instanceDetails.launchTime` raw log field to the UDM `target.resource_ancestors.attribute.creation_time` field for IAMUser findings.  
\- `event.idm.read_only_udm.intermediary.user.attribute.labels`: Newly mapped `service.additionalInfo.recentCredentials.accessKeyId` raw log field with `event.idm.read_only_udm.intermediary.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `detail.resource.instanceDetails.iamInstanceProfile.arn` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `detail.resource.instanceDetails.iamInstanceProfile.id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-07-27 |  Enhancement:  
\- `event.idm.read_only_udm.target.location.country_or_region`: Removed mapping of `service.action.networkConnectionAction.remoteIpDetails.country.countryName` from `event.idm.read_only_udm.target.location.country_or_region`, as this information is more appropriate in the principal entity.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Mapped `service.action.networkConnectionAction.remoteIpDetails.country.countryName` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.location.city`: Removed mapping of `service.action.networkConnectionAction.remoteIpDetails.city.cityName` from `event.idm.read_only_udm.target.location.city`, as this information is more appropriate in the principal entity.  
\- `event.idm.read_only_udm.principal.location.city`: Mapped `service.action.networkConnectionAction.remoteIpDetails.city.cityName` raw log field to `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.cloud.vpc.id`: Removed mapping of `vpc_id` raw log field to `event.idm.read_only_udm.target.asset.attribute.cloud.vpc.id` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.target.asset.attribute.cloud.project.type`: Removed mapping of `partition` raw log field to `event.idm.read_only_udm.target.asset.attribute.cloud.project.type` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Mapped `vpc_id` and `partition` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `service.action.networkConnectionAction.localNetworkInterface` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- Updated the naming convention to avoid conflict with raw log fields:  
\- Changed the naming convention from `city_name` to `portProbeDetail_city_name`.   
2026-07-03 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset.first_discover_time`: Removed mapping of `service.eventFirstSeen` and `detail.service.eventFirstSeen` from `event.idm.read_only_udm.principal.asset.first_discover_time` UDM field in order to introduce more accurate mapping.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Mapped `service.eventFirstSeen` and `detail.service.eventFirstSeen` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.principal.asset.last_discover_time`: Removed mapping of `service.eventLastSeen` and `detail.service.eventLastSeen` from `event.idm.read_only_udm.principal.asset.last_discover_time` UDM field in order to introduce more accurate mapping.  
\- `event.idm.read_only_udm.security_result.last_discovered_time`: Mapped `service.eventLastSeen` and `detail.service.eventLastSeen` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.cloud.project.id`: Removed mapping of `id` from `event.idm.read_only_udm.target.asset.attribute.cloud.project.id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.labels`: Removed mapping of `service.additionalInfo.sample`, `service.additionalInfo.newPolicy.requireNumbers`, `service.additionalInfo.newPolicy.hardExpiry`, `service.additionalInfo.newPolicy.requireSymbols`, `service.additionalInfo.newPolicy.requireLowercaseCharacters`, `service.additionalInfo.newPolicy.requireUppercaseCharacters`, `service.additionalInfo.newPolicy.minimumPasswordLength`, `service.additionalInfo.newPolicy.allowUsersToChangePassword`, `service.additionalInfo.newPolicy.maxPasswordAge`, `service.additionalInfo.newPolicy.passwordReusePrevention` from `event.idm.read_only_udm.security_result.about.labels` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detail.service.detection.sequence.signals.signalIndicators.values`, `service.detection.sequence.signals.signalIndicators.values`, `detail.service.detection.sequence.sequenceIndicators.values` and `service.detection.sequence.sequenceIndicators.values` from `event.idm.read_only_udm.additional.fields` UDM field when `detail.service.detection.sequence.signals.signalIndicators.key`, `service.detection.sequence.signals.signalIndicators.key`, `detail.service.detection.sequence.sequenceIndicators.key` and `service.detection.sequence.sequenceIndicators.key` is `ATTACK_TECHNIQUE` or `ATTACK_TACTIC` in order to introduce more accurate mapping.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `service.additionalInfo.sample`, `service.additionalInfo.newPolicy.requireNumbers`, `service.additionalInfo.newPolicy.hardExpiry`, `service.additionalInfo.newPolicy.requireSymbols`, `service.additionalInfo.newPolicy.requireLowercaseCharacters`, `service.additionalInfo.newPolicy.requireUppercaseCharacters`, `service.additionalInfo.newPolicy.minimumPasswordLength`, `service.additionalInfo.newPolicy.allowUsersToChangePassword`, `service.additionalInfo.newPolicy.maxPasswordAge`, `service.additionalInfo.newPolicy.passwordReusePrevention`, `service.additionalInfo.agentDetails.agentVersion`, `service.additionalInfo.agentDetails.agentId`, `resource2.data.ec2Instance.launchTemplate.version`, `threats.source`, `service.detection.sequence.resources.ec2LaunchTemplate.ec2InstanceUids` and `service.detection.sequence.resources.ec2Instance.productCodes.productCodeType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Mapped `detail.service.detection.sequence.signals.signalIndicators.key`, `service.detection.sequence.signals.signalIndicators.key`, `detail.service.detection.sequence.sequenceIndicators.key` and `service.detection.sequence.sequenceIndicators.key` with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field when `detail.service.detection.sequence.signals.signalIndicators.key`, `service.detection.sequence.signals.signalIndicators.key`, `detail.service.detection.sequence.sequenceIndicators.key` and `service.detection.sequence.sequenceIndicators.key` is `ATTACK_TECHNIQUE`.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Mapped `detail.service.detection.sequence.signals.signalIndicators.key`, `service.detection.sequence.signals.signalIndicators.key`, `detail.service.detection.sequence.sequenceIndicators.key` and `service.detection.sequence.sequenceIndicators.key` with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field when `detail.service.detection.sequence.signals.signalIndicators.key`, `service.detection.sequence.signals.signalIndicators.key`, `detail.service.detection.sequence.sequenceIndicators.key` and `service.detection.sequence.sequenceIndicators.key` is `ATTACK_TACTIC`.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `threats.name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.about.file.full_path`: Newly mapped `itemPaths.nestedItemPath` raw log field with `event.idm.read_only_udm.security_result.about.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.about.file.sha256`: Newly mapped `itemPaths.hash` raw log field with `event.idm.read_only_udm.security_result.about.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `objectdetails.hash` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `objectdetails.objectArn`, `objectdetails.versionId`, `objectdetails.eTag`, `objectdetails.key`, `s3BucketDetail.defaultServerSideEncryption.kmsMasterKeyArn` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-06-22 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `ipaddr.privateIpAddress` and `service.action.awsApiCallAction.remoteIpDetails.ipAddressV4` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `caller_type` contains `Remote IP` its destination IP.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ipaddr.privateIpAddress` and `service.action.awsApiCallAction.remoteIpDetails.ipAddressV4` (when `caller_type` contains `Remote IP`) raw log fields to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Removed mapping of `service.action.awsApiCallAction.remoteIpDetails.country.countryName` from `event.idm.read_only_udm.target.location.country_or_region`, as this information is more appropriate in the principal entity.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `service.action.awsApiCallAction.remoteIpDetails.country.countryName` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.location.city`: Removed mapping of `service.action.awsApiCallAction.remoteIpDetails.city.cityName` from `event.idm.read_only_udm.target.location.city`, as this information is more appropriate in the principal entity.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `service.action.awsApiCallAction.remoteIpDetails.city.cityName` raw log field to `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.target.location.region_latitude`: Removed mapping of `service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat` from `event.idm.read_only_udm.target.location.region_latitude`, as this information is more appropriate in the principal entity.  
\- `event.idm.read_only_udm.principal.location.region_latitude`: Newly mapped `service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat` raw log field to `event.idm.read_only_udm.principal.location.region_latitude` UDM field.  
\- `event.idm.read_only_udm.target.location.region_longitude`: Removed mapping of `service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon` from `event.idm.read_only_udm.target.location.region_longitude`, as this information is more appropriate in the principal entity.  
\- `event.idm.read_only_udm.principal.location.region_longitude`: Newly mapped `service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon` raw log field to `event.idm.read_only_udm.principal.location.region_longitude` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Removed mapping of `service.action.portProbeAction.portProbeDetails[0].remoteIpDetails.country.countryName` from `event.idm.read_only_udm.target.location.country_or_region`, as this is now mapped to `event.idm.read_only_udm.principal.location.country_or_region` inside the loop for index 0.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `portProbeDetail.remoteIpDetails.country.countryName` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` when index is 0 within the `portProbeDetails` loop.  
\- `event.idm.read_only_udm.target.location.city`: Removed mapping of `service.action.portProbeAction.portProbeDetails[0].remoteIpDetails.city.cityName` from `event.idm.read_only_udm.target.location.city`, as this is now mapped to `event.idm.read_only_udm.principal.location.city` inside the loop for index 0.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `portProbeDetail.remoteIpDetails.city.cityName` raw log field to `event.idm.read_only_udm.principal.location.city` when index is 0 within the `portProbeDetails` loop.  
\- `event.idm.read_only_udm.target.location.region_latitude`: Removed mapping of `service.action.portProbeAction.portProbeDetails[0].remoteIpDetails.geoLocation.lat` from `event.idm.read_only_udm.target.location.region_latitude`, as this is now mapped to `event.idm.read_only_udm.principal.location.region_latitude` inside the loop for index 0.  
\- `event.idm.read_only_udm.principal.location.region_latitude`: Newly mapped `portProbeDetail.remoteIpDetails.geoLocation.lat` raw log field to `event.idm.read_only_udm.principal.location.region_latitude` when index is 0 within the `portProbeDetails` loop.  
\- `event.idm.read_only_udm.target.location.region_longitude`: Removed mapping of `service.action.portProbeAction.portProbeDetails[0].remoteIpDetails.geoLocation.lon` from `event.idm.read_only_udm.target.location.region_longitude`, as this is now mapped to `event.idm.read_only_udm.principal.location.region_longitude` inside the loop for index 0.  
\- `event.idm.read_only_udm.principal.location.region_longitude`: Newly mapped `portProbeDetail.remoteIpDetails.geoLocation.lon` raw log field to `event.idm.read_only_udm.principal.location.region_longitude` when index is 0 within the `portProbeDetails` loop.  
\- `event.idm.read_only_udm.target.port`: Changed mapping for `event.idm.read_only_udm.target.port` from `portProbeDetail.localPortDetails.port` for all items in the loop to only map when index is 0, as subsequent ports are now in labels.  
\- `event.idm.read_only_udm.principal.application`: Changed mapping for `event.idm.read_only_udm.principal.application` from `portProbeDetail.localPortDetails.portName` for all items in the loop to only map when index is 0, as subsequent applications are now in labels.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Removed mapping of `service.action.dnsRequestAction.domain` from `event.idm.read_only_udm.principal.administrative_domain`, as this field is not the correct representation for the raw log field. It is already mapped to `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `service.action.portProbeAction.blocked`, `service.action.dnsRequestAction.vpcOwnerAccountId` and `service.action.awsApiCallAction.remoteAccountDetails.affiliated` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `service.additionalInfo.anomalies.anomalousAPIs`, `service.additionalInfo.authenticationMethod`, `portProbeDetail.remoteIpDetails.organization.asn`, `portProbeDetail.remoteIpDetails.organization.asnOrg`, `portProbeDetail.remoteIpDetails.organization.isp`, `portProbeDetail.remoteIpDetails.organization.org`, `portProbeDetail.remoteIpDetails.country.countryName` (when index > 0), `portProbeDetail.remoteIpDetails.city.cityName` (when index > 0), `portProbeDetail.remoteIpDetails.geoLocation.lat` (when index > 0), `portProbeDetail.remoteIpDetails.geoLocation.lon` (when index > 0), `portProbeDetail.localPortDetails.port` (when index > 0), and `portProbeDetail.localPortDetails.portName` (when index > 0) raw log fields to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `ipaddr.privateDnsName`, `s3BucketDetail.name` (when index is 0), and `s3BucketDetail.arn` (when index is 0) raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-06-11 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `service.action.awsApiCallAction.remoteIpDetails.ipAddressV4` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `type` is `Policy:IAMUser/RootCredentialUsage`. Since this IP address in `remoteIpDetails` represents the entity initiating the API call, not the entity being acted upon.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `service.action.awsApiCallAction.remoteIpDetails.ipAddressV4` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `type` is `Policy:IAMUser/RootCredentialUsage`. Since, this IP represents the source of the AWS API call, making it the actor (principal) in this event, rather than the target.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `createdAt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Mapped `updatedAt` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2026-05-21 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `service.action.networkConnectionAction.localIpDetails.ipAddressV4` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it contains the target ip related data.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `service.action.networkConnectionAction.localIpDetails.ipAddressV4` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it is more appropriate to the target ip related data.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `service.action.networkConnectionAction.remoteIpDetails.ipAddressV4` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it contains the principal ip related data.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `service.action.networkConnectionAction.remoteIpDetails.ipAddressV4` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it is more appropriate to the principal ip related data.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `principalip` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it contains the target ip related data.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `principalip` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it is more appropriate to the target ip related data.  
\- `event.idm.read_only_udm.principal.port`: Removed mapping of `service.action.networkConnectionAction.localPortDetails.port` from `event.idm.read_only_udm.principal.port` UDM field when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it contains the target port related data.  
\- `event.idm.read_only_udm.target.port`: Mapped `service.action.networkConnectionAction.localPortDetails.port` raw log field to `event.idm.read_only_udm.target.port` UDM field when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it is more appropriate to the target port related data.  
\- `event.idm.read_only_udm.target.port`: Removed mapping of `service.action.networkConnectionAction.remotePortDetails.port` from `event.idm.read_only_udm.target.port` UDM field when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it contains the principal port related data.  
\- `event.idm.read_only_udm.principal.port`: Mapped `service.action.networkConnectionAction.remotePortDetails.port` raw log field to `event.idm.read_only_udm.principal.port` UDM field when `service.action.networkConnectionAction.connectionDirection` is `INBOUND` as it is more appropriate to the principal port related data.   
2026-05-07 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.service.detection.sequence.uid`, `detail.service.detection.sequence.description`, `detail.service.additionalInfo.type`, `data.resourceUids`, `data.endpointIds`, `data.signalIndicators.values`, `data.uid`, `data.type`, `data.description`, `data.name`, `data.createdAt`, `data.updatedAt`, `data.firstSeenAt`, `data.lastSeenAt`, `data.severity`, `data.count`, `data.id`, `data.domain`, `data.port`, `resource2.uid`, `resource2.cloudPartition`, `resource2.data.ec2Instance.availabilityZone`, `resource2.data.ec2Instance.imageDescription`, `resource2.data.ec2Instance.instanceState`, `resource2.data.ec2Instance.instanceType`, `resource2.name`, `resource2.accountId`, `resource2.data.ec2Instance.ec2NetworkInterfaceUids`, `prodcode.productCodeId`, `prodcode.productCodeType`, `resource2.data.ec2Image.ec2InstanceUids`, `resource2.resourceType`, `sequenceIndicator.values`, `detail.createdAt`, `detail.id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `data.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.asset.first_discover_time`: Newly mapped `detail.service.eventFirstSeen` raw log field with `event.idm.read_only_udm.principal.asset.first_discover_time` UDM field.  
\- `event.idm.read_only_udm.principal.asset.last_discover_time`: Newly mapped `detail.service.eventLastSeen` raw log field with `event.idm.read_only_udm.principal.asset.last_discover_time` UDM field.  
\- `event.idm.read_only_udm.network.direction`: If `data.connection.direction` is `Inbound`, set the value of `event.idm.read_only_udm.network.direction` to `INBOUND`.  
\- `event.idm.read_only_udm.network.direction`: If `data.connection.direction` is `Outbound`, set the value of `event.idm.read_only_udm.network.direction` to `OUTBOUND`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data.location`, `data.autonomousSystem`, `detail.associatedAttackSequenceArn` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.about.location.name`: Newly mapped `data_resources_region` log field with `event.idm.read_only_udm.security_result.about.location.name` UDM field.   
2026-01-29 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip`: Removed mapping of `portProbeDetail.remoteIpDetails.ipAddressV4` from `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `portProbeDetail.remoteIpDetails.ipAddressV4` from `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Mapped `portProbeDetail.remoteIpDetails.ipAddressV4` raw log field to `event.idm.read_only_udm.principal.ip` UDM field. As it is more appropriate when actionType is portProbe  
\- `event.idm.read_only_udm.principal.asset.ip`: Mapped `portProbeDetail.remoteIpDetails.ipAddressV4` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.As it is more appropriate when actionType is portProbe  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `principalip` from `event.idm.read_only_udm.principal.ip` UDM field when service.action.actionType is `PORT_PROBE`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `principalip` from `event.idm.read_only_udm.principal.asset.ip` UDM field when service.action.actionType is `PORT_PROBE`.  
\- `event.idm.read_only_udm.target.ip`: Mapped `principalip` raw log field to `event.idm.read_only_udm.target.ip` UDM field when service.action.actionType is `PORT_PROBE`.  
\- `event.idm.read_only_udm.target.asset.ip`: Mapped `principalip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field when service.action.actionType is `PORT_PROBE`.   
2026-01-27 |  Enhancement:  
\- event.idm.read_only_udm.target.ip & event.idm.read_only_udm.target.asset.ip: Removed mapping of `detail.service.action.awsApiCallAction.remoteIpDetails.ipAddressV4` and `service.action.awsApiCallAction.remoteIpDetails.ipAddressV4` from `event.idm.read_only_udm.target.ip` & `event.idm.read_only_udm.target.asset.ip` when event type is `Discovery:IAMUser/AnomalousBehavior` as it is better suited for `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip & event.idm.read_only_udm.principal.asset.ip: Mapped `detail.service.action.awsApiCallAction.remoteIpDetails.ipAddressV4` or `service.action.awsApiCallAction.remoteIpDetails.ipAddressV4` raw log field to `event.idm.read_only_udm.principal.ip` & `event.idm.read_only_udm.principal.asset.ip` when event type is `Discovery:IAMUser/AnomalousBehavior`.  
\- Modified logic to ensure `service.action.awsApiCallAction.remoteIpDetails.city.cityName` is used to populate the city in the UDM location fields.   
2026-01-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `service.action.networkConnectionAction.remoteIpDetails.geoLocation.lat`, `service.action.networkConnectionAction.remoteIpDetails.geoLocation.lon`, `service.action.networkConnectionAction.remoteIpDetails.organization.asn`, `service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg`, `service.action.networkConnectionAction.remoteIpDetails.organization.isp`, `service.action.networkConnectionAction.remoteIpDetails.organization.org` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `service.action.networkConnectionAction.remoteIpDetails.ipAddressV4` raw log field to `event.idm.read_only_udm.additional.fields` with key `attacker_ip` when `type` is `UnauthorizedAccess:EC2/MaliciousIPCaller.Custom`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `service.action.networkConnectionAction.remoteIpDetails.ipAddressV4` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field when `type` is `UnauthorizedAccess:EC2/MaliciousIPCaller.Custom` as it is supposed to be an attacker IP.   
2026-01-07 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `resource.resourceType` raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `resource1.cloudPartition`, `resource1.data.ec2Instance.availabilityZone`, `resource1.data.ec2Instance.imageDescription`, `resource1.data.ec2Instance.instanceState`, `resource1.data.ec2Instance.iamInstanceProfile.id`, `resource1.data.ec2Instance.iamInstanceProfile.arn`, `resource1.data.ec2Instance.instanceType`, `resource1.data.ec2Instance.outpostArn`, `resource1.data.ec2Instance.platform`, `resource1.data.ec2Instance.ec2NetworkInterfaceUids`, `resource1.data.ec2Instance.productCodes`, `resource1.data.iamInstanceProfile.ec2InstanceUids` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Modified conditional check for `endpoints_connection_direction` to also accept uppercase `INBOUND` and `OUTBOUND`.  
\- Renamed loop variable `reource` to `resource1` for clarity.   
2025-12-23 |  Enhancement:  
\- Added support to ensure that `service.detection.sequence.endpoints` raw log field is being mapped as expected.   
2025-11-11 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `Record.requestParameters.bucketName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `Record.additionalEventData.bytesTransferredIn` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `Record.additionalEventData.bytesTransferredOut` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `Record.userIdentity.userName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `Record.userIdentity.accountId` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Record_eventName`, `Record.requestParameters.encoding-type`, `Record.requestParameters.delimiter`, `Record.additionalEventData.SignatureVersion`, `Record.additionalEventData.x-amz-id-2` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Record.requestParameters.prefix`, `resource`, `Record.recipientAccountId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Record.additionalEventData.AuthenticationMethod` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a grok filter to parse and drop messages that are only numbers, whitespace, or tabs, tagging them as TAG_UNSUPPORTED.  
\- Refactored conditional checks for `data.detail.service.additionalInfo.value`, `data.detail.service.additionalInfo.type`, `data.detail.region`, `data.detail.partition`, and `data.detail.title` to first store the value in an intermediate variable.   
2025-10-18 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `awsAccountId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `digestS3Object` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `digestS3Bucket` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.artifact.last_https_certificate.thumbprint_sha256: Newly mapped `digestPublicKeyFingerprint` raw log field with `event.idm.read_only_udm.target.artifact.last_https_certificate.thumbprint_sha256` UDM field.  
\- event.idm.read_only_udm.target.artifact.last_https_certificate.cert_signature.signature_algorithm: Newly mapped `digestSignatureAlgorithm` raw log field with `event.idm.read_only_udm.target.artifact.last_https_certificate.cert_signature.signature_algorithm` UDM field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `previousDigestHashValue` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `newestEventTime` and `oldestEventTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `previousDigestHashAlgorithm`, `previousDigestS3Bucket`, `previousDigestS3Object`, logFile.hashAlgorithm, logFile.hashValue, logFile.s3Bucket, and logFile.s3Object raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.roles: Removed mapping where `resource_accessKeyDetails_userType` was `Unknown`.  
\- event.idm.read_only_udm.principal.location.city: Removed mapping where `remoteIpDetails_city_cityName` was `UNKNOWN`.  
\- event.idm.read_only_udm.principal.network.organization_name: Removed mapping where `remoteIPDetails_organization_asnOrg` was `UNKNOWN`.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Removed mapping of `remoteIPDetails_organization_isp` when its value was `UNKNOWN`.  
\- event.idm.read_only_udm.target.administrative_domain: Removed mapping where `remoteIPDetails_organization_org` was `UNKNOWN`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `probeVal.localPortDetails.portName` when its value was `Unknown`.  
\- event.idm.read_only_udm.principal.location.region_latitude: Removed mapping where `detail.service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lat` was `0`.  
\- event.idm.read_only_udm.principal.location.region_longitude: Removed mapping where `detail.service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lon` was `0`.  
\- event.idm.read_only_udm.metadata.event_type:  
\- Modified mapping for `event.idm.read_only_udm.metadata.event_type` when `has_principal` is `true` and `Record_recipientAccountId` is null, updated from `STAT_UPDATE` to `STATUS_UPDATE`.  
\- Modified mapping for `event.idm.read_only_udm.metadata.event_type` when `has_resource` is `true` set to `USER_RESOURCE_ACCESS`.   
2025-09-05 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `actor_id`, `resources_name`, `resources_accountId`, `sequenceIndicator.key`, `image`, `imageUid`, `createdAt`, `containerUids` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `actors_path`, `actors_sha256` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `associatedAttackSequenceArn` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `updatedAt` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.about.location.name: Newly mapped `resources_region` raw log field with `event.idm.read_only_udm.security_result.about.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `actors_name` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `INBOUND` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `status`,`vpcId`, raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.   
2025-08-29 |   
2025-08-08 |   
2025-07-03 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `detail.resource.instanceDetails.networkInterfaces.publicIp or privateIpAddress` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `detail.resource.instanceDetails.networkInterfaces.publicIp or privateIpAddress` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `detail.service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV4` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `detail.resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.groupid`: Newly mapped `detail.resource.instanceDetails.networkInterfaces.securityGroups.groupId` raw log field to `event.idm.read_only_udm.principal.user.groupid` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `detail.resource.instanceDetails.networkInterfaces.securityGroups.groupName` raw log field to `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `detail.resource.instanceDetails.networkInterfaces.subnetId`, and `detail.resource.instanceDetails.networkInterfaces.securityGroups.groupId` raw log fields to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detail.resource.instanceDetails.networkInterfaces.privateIpAddresses.privateDnsName`, `detail.service.action.portProbeAction.portProbeDetails.remoteIpDetails.city.cityName`, and `detail.service.action.portProbeAction.portProbeDetails.localPortDetails.portName` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `detail.service.action.portProbeAction.portProbeDetails` including `localPortDetails.port`, `remoteIpDetails.country.countryName`, `remoteIpDetails.geoLocation.lat`, `remoteIpDetails.geoLocation.lon`, `remoteIpDetails.organization.asn`, `remoteIpDetails.organization.asnOrg`, `remoteIpDetails.organization.isp`, `remoteIpDetails.organization.org` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- If `has_principal` is `true` and `has_target` is `true` and `has_network_dns` is `true` and `event_type` is in [`GENERIC_EVENT`, "`, `STATUS_UPDATE`, `NETWORK_DNS"], updated to `NETWORK_DNS`. Also set `event.idm.read_only_udm.network.application_protocol` to DNS.  
\- Else if `has_principal` is `true` and `has_target` is `true` and `event_type` is in [`GENERIC_EVENT`, "`, `STATUS_UPDATE"], updated to `NETWORK_CONNECTION`.  
\- Else if `has_principal` is `true` or `principal_ip_set` is `true` and `has_target` is `false` and `event_type` is in [`GENERIC_EVENT`, "`, `STATUS_UPDATE"], updated to `STATUS_UPDATE`.  
\- Else `event_type` is not in `NULL` and `principal_ip_set` or `has_principal` is `false` and `event_type` is not in `(?i)user|resource|read`, updated to `GENERIC_EVENT`.  
Buganizer Id: 435146508  
Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped Record.eventTime raw log field with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped Record.eventVersion and Record.apiVersion raw log field with event.idm.read_only_udm.metadata.product_version UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped Record.awsRegion raw log field with event.idm.read_only_udm.principal.location.country_or_region UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped Record.eventName raw log field with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped Record.eventType raw log field with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped Record.eventID raw log field with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped Record.eventSource raw log field with event.idm.read_only_udm.metadata.url_back_to_product UDM field.  
\- event.idm.read_only_udm.target.asset_id: Newly mapped Record.recipientAccountId raw log field with event.idm.read_only_udm.target.asset_id UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped Record.sourceIPAddress raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped Record.sourceIPAddress raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped Record.userAgent raw log field with event.idm.read_only_udm.network.http.user_agent UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped Record.userAgent raw log field with event.idm.read_only_udm.network.http.parsed_user_agent UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped Record.userIdentity.accessKeyId raw log field with event.idm.read_only_udm.target.user.userid UDM field.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped Record.userIdentity.accountId raw log field with event.idm.read_only_udm.target.user.product_object_id UDM field.  
\- event.idm.read_only_udm.principal.resource.type: Newly mapped Record.userIdentity.type raw log field with event.idm.read_only_udm.principal.resource.type UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped Record.userIdentity.principalId raw log field with event.idm.read_only_udm.principal.user.product_object_id UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped Record.userIdentity.arn raw log field with event.idm.read_only_udm.principal.resource.name UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped Record.userIdentity.sessionContext.sessionIssuer.userName raw log field with event.idm.read_only_udm.target.user.user_display_name UDM field.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped Record.tlsDetails.tlsVersion raw log field with event.idm.read_only_udm.network.tls.version UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped Record.tlsDetails.cipherSuite raw log field with event.idm.read_only_udm.network.tls.cipher UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped Record.eventCategory raw log field with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.creation_time: Newly mapped Record.userIdentity.sessionContext.attributes.creationDate raw log field with event.idm.read_only_udm.principal.user.attribute.creation_time UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped Record.userIdentity.sessionContext.sessionIssuer.type raw log field with key sessionIssuer_type to event.idm.read_only_udm.principal.user.attribute.labels UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped Record.userIdentity.sessionContext.sessionIssuer.principalId raw log field with key sessionIssuer_principalId to event.idm.read_only_udm.principal.user.attribute.labels UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped Record.userIdentity.sessionContext.sessionIssuer.arn raw log field with key sessionIssuer_arn to event.idm.read_only_udm.principal.user.attribute.labels UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped Record.userIdentity.sessionContext.sessionIssuer.accountId raw log field with key sessionIssuer_accountId to event.idm.read_only_udm.principal.user.attribute.labels UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped Record.userIdentity.sessionContext.attributes.mfaAuthenticated raw log field with key mfaAuthenticated to event.idm.read_only_udm.principal.user.attribute.labels UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped Record.tlsDetails.clientProvidedHostHeader raw log field with key tlsDetails_clientProvidedHostHeader to event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped Record.readOnly raw log field with key Record_readOnly to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped Record.managementEvent raw log field with key Record_managementEvent to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped Record.requestID raw log field with key Record_requestID to event.idm.read_only_udm.additional.fields UDM field.  
Buganizer Id: 428233222  
\- event.idm.read_only_udm.principal.ip: Newly mapped `remoteIpDetails_ipAddressV4` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `remoteIpDetails_city_cityName` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.principal.location.region_latitude: Newly mapped `remoteIPDetails_geoLocation_lat` raw log field with `event.idm.read_only_udm.principal.location.region_latitude` UDM field.  
\- event.idm.read_only_udm.principal.location.region_longitude: Newly mapped `remoteIPDetails_geoLocation_lon` raw log field with `event.idm.read_only_udm.principal.location.region_longitude` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `remoteIPDetails_organization_asn` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `remoteIPDetails_organization_isp` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.network.organization_name: Newly mapped `remoteIPDetails_organization_asnOrg` raw log field with `event.idm.read_only_udm.principal.network.organization_name` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `remoteIPDetails_organization_org` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `kubernetesApiCallAction_requestUri` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `kubernetesApiCallAction_statusCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `kubernetesApiCallAction_userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `kubernetesApiCallAction_userAgentOrg` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `unmapped_username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `resource_uid` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `remoteIpDetails_ipAddressV4` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-06-17 |  \- event.idm.read_only_udm.target.namespace: Newly mapped `resource.kubernetesDetails.kubernetesWorkloadDetails.namespace` raw log field with `event.idm.read_only_udm.target.namespace` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `resource.kubernetesDetails.kubernetesWorkloadDetails.name`, `resource.kubernetesDetails.kubernetesWorkloadDetails.uid`, `resource.kubernetesDetails.kubernetesWorkloadDetails.type`, `resource.kubernetesDetails.kubernetesWorkloadDetails.serviceAccountName`, `resource.kubernetesDetails.kubernetesUserDetails.uid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip & event.idm.read_only_udm.principal.asset.ip: Newly mapped values from `service.action.kubernetesApiCallAction.sourceIPs` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field and set `has_principal` to true.  
\- Added conditions to map `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when `has_principal` is true.  
\- Added null check condition for `detail_resource_accessKeyDetails_userName`, `detail_resource_accessKeyDetails_userType`, `resource_accessKeyDetails_principalId`, `resource_accessKeyDetails_userName`, `resource_accessKeyDetails_userType`, `service.action.networkConnectionAction.localIpDetails.ipAddressV4` log fields.  
\- Set `has_user` to `true` wherever `event.idm.read_only_udm.principal.user.userid` is mapped.  
\- Added null check conditions for `value_array` and `observationstext` fields.   
2025-05-26 |  \- `event.idm.read_only_udm.target.resource.attribute.labels` \- Newly mapped `service.runtimeDetails.process.lineage.executablePath`, `service.runtimeDetails.process.lineage.name`, `service.runtimeDetails.process.lineage.namespacePid`, `service.runtimeDetails.process.lineage.userId`, `service.runtimeDetails.process.lineage.uuid`, `service.runtimeDetails.process.lineage.euid`, `service.runtimeDetails.process.lineage.parentUuid`, `service.runtimeDetails.process.namespacePid`, `service.detectorId`, `service.runtimeDetails.process.lineage.startTime` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` \- Newly mapped `service.runtimeDetails.process.euid` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `service.runtimeDetails.process.executableSha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.process.file.names`: Newly mapped `service.runtimeDetails.process.name` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `service.runtimeDetails.process.executablePath` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `service.runtimeDetails.process.pid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Newly mapped `service.runtimeDetails.process.uuid` raw log field with `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.target.process.parent_process.product_specific_process_id`: Newly mapped `service.runtimeDetails.process.parentUuid` raw log field with `event.idm.read_only_udm.target.process.parent_process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `service.runtimeDetails.process.user`, `service.runtimeDetails.process.startTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path` : Newly mapped `service.runtimeDetails.process.pwd` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `service.runtimeDetails.process.userId` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.parent_process.pid`: Newly mapped `service.runtimeDetails.process.lineage.pid` raw log field with `event.idm.read_only_udm.target.process.parent_process.pid` UDM field.   
2025-05-21 |  \- event.idm.read_only_udm.principal.user.userid: Newly mapped `detail.resource.kubernetesDetails.kubernetesUserDetails.username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-04-25 |  \- `event.idm.read_only_udm.additional.fields`: Newly mapped `service.detection.sequence.signals`, `service.detection.sequence.actors`, `service.detection.sequence.endpoints` , `service.detection.sequence.resources`, `service.featureName`, `service.detectorId`, `service.resourceRole`, and `service.serviceName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `service.detection.sequence.endpoints.ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `service.detection.sequence.actors.user` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_version`: Newly mapped `schemaVersion` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- `event.idm.read_only_udm.principal.asset.first_discover_time`: Newly mapped `service.eventFirstSeen` raw log field with `event.idm.read_only_udm.principal.asset.first_discover_time` UDM field.  
\- `event.idm.read_only_udm.principal.asset.last_discover_time`: Newly mapped `service.eventLastSeen` raw log field with `event.idm.read_only_udm.principal.asset.last_discover_time` UDM field.   
2025-02-11 |  Enhancement:  
\- Added support for mapping `IamInstanceProfile Arn` to `target.resource.attribute.labels`.  
\- Added support for mapping `security_result.severity`.   
2025-01-27 |  Enhancement:  
\- Mapped `service.additionalInfo.value` to `security_result.about.resource.attribute.labels`.   
2025-01-16 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-11-28 |  Enhancement:  
\- Mapped `service.additionalInfo.unusualBehavior` and `service.additionalInfo.profiledBehavior` to `security_result.about.resource.attribute.labels`.   
2024-10-23 |  Enhancement:  
\- Added support to parse unparsed logs.   
2024-10-17 |  Enhancement:  
\- Mapped `resource.eksClusterDetails.status`, `resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser`, `resource.kubernetesDetails.kubernetesUserDetails.groups`, `resource.kubernetesDetails.kubernetesUserDetails.sessionName`, `service.action.kubernetesApiCallAction.verb`, `service.detection.anomaly.profiles.namespace.asnInfo`, `service.detection.anomaly.profiles.namespace.userAgent`, `service.detection.anomaly.profiles.namespace.dayOfWeek`, `service.detection.anomaly.profiles.namespace.impersonatedUsername`, `service.detection.anomaly.profiles.namespace.api`, `service.detection.anomaly.profiles.namespace.username`, `service.detection.anomaly.profiles.cluster.asnInfo`, `service.detection.anomaly.profiles.cluster.userAgent`, `service.detection.anomaly.profiles.cluster.dayOfWeek`, `service.detection.anomaly.profiles.cluster.impersonatedUsername`, `service.detection.anomaly.profiles.cluster.api`, `service.detection.anomaly.profiles.cluster.username`, `service.detection.anomaly.profiles.account.asnInfo`, `service.detection.anomaly.profiles.account.userAgent`, `service.detection.anomaly.profiles.account.dayOfWeek`, `service.detection.anomaly.profiles.account.impersonatedUsername`, `service.detection.anomaly.profiles.account.api`, `service.detection.anomaly.profiles.account.username`, `service.detection.anomaly.profiles.username.asnInfo`, `service.detection.anomaly.profiles.username.userAgent`, `service.detection.anomaly.profiles.username.dayOfWeek`, `service.detection.anomaly.profiles.username.impersonatedUsername`, `service.detection.anomaly.profiles.username.api`, `service.detection.anomaly.profiles.username.username`, `service.detection.anomaly.unusual.behavior.namespace.asnInfo`, `service.detection.anomaly.unusual.behavior.namespace.userAgent`, `service.detection.anomaly.unusual.behavior.namespace.dayOfWeek`, `service.detection.anomaly.unusual.behavior.namespace.impersonatedUsername`, `service.detection.anomaly.unusual.behavior.namespace.api`, `service.detection.anomaly.unusual.behavior.namespace.username`, `service.detection.anomaly.unusual.behavior.cluster.asnInfo`, `service.detection.anomaly.unusual.behavior.cluster.userAgent`, `service.detection.anomaly.unusual.behavior.cluster.dayOfWeek`, `service.detection.anomaly.unusual.behavior.cluster.impersonatedUsername`, `service.detection.anomaly.unusual.behavior.cluster.api`, `service.detection.anomaly.unusual.behavior.cluster.username`, `service.detection.anomaly.unusual.behavior.account.asnInfo`, `service.detection.anomaly.unusual.behavior.account.userAgent`, `service.detection.anomaly.unusual.behavior.account.dayOfWeek`, `service.detection.anomaly.unusual.behavior.account.impersonatedUsername`, `service.detection.anomaly.unusual.behavior.account.api`, `service.detection.anomaly.unusual.behavior.account.username`, `service.detection.anomaly.unusual.behavior.username.asnInfo`, `service.detection.anomaly.unusual.behavior.username.userAgent`, `service.detection.anomaly.unusual.behavior.username.dayOfWeek`, `service.detection.anomaly.unusual.behavior.username.impersonatedUsername`, `service.detection.anomaly.unusual.behavior.username.api`, and `service.detection.anomaly.unusual.behavior.username.username` to `additional.fields`.  
\- Mapped `service.action.kubernetesApiCallAction.statusCode` to `network.http.response_code`.  
\- Mapped `resource.eksClusterDetails.vpcId` to `principal.cloud.vpc.id`.  
\- Mapped `service.action.kubernetesApiCallAction.namespace` to `principal.namespace`.  
\- Mapped `service.action.kubernetesApiCallAction.requestUri` to `target.url`.   
2024-03-11 |  Enhancement:  
\- Mapped `service.action.awsApiCallAction.domainDetails.domain` to `network.dns.questions.name`.   
2024-03-05 |  Enhancement:  
\- Mapped `service.additionalInfo.value` to `security_result.about.labels`.  
\- Mapped `service.additionalInfo.value` to `security_result.about.resource.attribute.labels`.  
\- Mapped `service.action.awsApiCallAction.affectedResources.AWS_CloudTrail_Trail` to `principal.resource.attribute.labels`.   
2024-02-26 |  Bug Fix:  
\- Mapped `resource.eksClusterDetails.createdAt` to `target.resource.attribute.labels`.  
\- Mapped `resource.s3BucketDetails.createdAt` to `principal.resource.attribute.labels`.  
\- Mapped `resource.eksClusterDetails.tags` to `target.resource.attribute.labels`.  
\- Mapped `resource.s3BucketDetails.tags` to `principal.resource.attribute.labels`.  
\- If `type` is similar to `:Kubernetes` or `:S3`, then mapped `resource.accessKeyDetails.accessKeyId` to `target.resource.product_object_id`.  
\- If `service.action.actionType` is similar to `AWS_API_CALL` or `KUBERNETES_API_CALL`, then mapped `resource.accessKeyDetails.accessKeyId` to `target.resource.product_object_id`.  
\- If `service.action.actionType` is similar to `DNS_REQUEST`, then mapped `resource.instanceDetails.instanceId` to `target.resource.product_object_id`.   
2023-08-18 |  \- Mapped fields `security_result.attack_details.tactics`, `security_result.attack_details.techniques` based on field `type`.  
\- Mapped `metadata.event_type` to more specific event_types wherever possible instead of GENERIC_EVENT.  
\- Mapped fields `target.resource.resource_subtype`, `target.resource.resource_type` based on field `type`.  
\- For all logs having the `type` value `:EC2` -  
Mapped `resource.instanceDetails.instanceId` to `target.resource.product_object_id`.  
Mapped `resource.instanceDetails.instanceType` to `target.resource.attribute.labels`.  
Mapped `resource.instanceDetails.launchTime` to `target.resource.attribute.creation_time`.  
\- For all logs having the `type` value `:RDSV` -  
Mapped `resource.rdsDbInstanceDetails.dbInstanceIdentifier` to `target.resource.product_object_id`.  
Mapped `resource.rdsDbInstanceDetails.dbInstanceArn` to `target.resource.name`.  
Mapped `resource.rdsDbInstanceDetails.dbClusterIdentifier` to `target.resource_ancestors.product_object_id`.  
Mapped `resource.rdsDbUserDetails.user` to `principal.user.userid`.  
\- For all logs having the `type` value `:Kubernetes` -  
Mapped ` resource.eksClusterDetails.arn` to `target.resource.name`.  
\- For all logs having the `type` value `:Runtime` -  
Mapped `resource.eksClusterDetails.arn` to `target.resource_ancestors.name`.  
Mapped `resource.instanceDetails.instanceId` to `target.resource.product_object_id`.  
Mapped `resource.instanceDetails.instanceType` to `target.resource.attribute.labels`.  
Mapped `resource.instanceDetails.launchTime` to `target.resource.attribute.creation_time`.  
\- For all logs having the `type` value `:IAMUser` -  
Mapped `resource.accessKeyDetails.accessKeyId` to `target.resource.product_object_id`.  
Mapped `resource.instanceDetails.instanceId` to `target.resource_ancestors.product_object_id`.  
\- For all logs having the `type` value `:S3` -  
Mapped `resource.s3BucketDetails.arn` or `resource.s3BucketDetails.name` to `target.resource.name`.   
2023-08-02 |  \- If `resource.instanceDetails.networkInterfaces` is empty, then mapped `metadata.event_type` to `GENERIC_EVENT`.  
\- If `detail.resource.accessKeyDetails.principalId` or `resource.accessKeyDetails.principalId` are empty, then mapped `metadata.event_type` to `USER_RESOURCE_ACCESS`.   
2023-06-19 |  \- Added `security_result.attack_details` based on `type`.   
2023-02-07 |  Enhancement -  
\- Mapped `threatdetails.threatListName` to `security_result.threat_feed_name`.  
\- Mapped `service.additionalInfo.threatName` to `security_result.threat_name`.  
\- If `product_event_type` in [`Backdoor:EC2/C&CActivity.B`, `Backdoor:EC2/C&CActivity.B!DNS`, `Trojan:EC2/BlackholeTraffic`, `Trojan:EC2/BlackholeTraffic!DNS`] then mapped `T1071` to `technique_label.value`.  
\- If `product_event_type` in [`PenTest:IAMUser/KaliLinux`, `PenTest:IAMUser/ParrotLinux`, `PenTest:IAMUser/PentooLinux`, `PenTest:S3/KaliLinux`, `PenTest:S3/ParrotLinux`, `PenTest:S3/PentooLinux`, `Policy:IAMUser/RootCredentialUsage`, `UnauthorizedAccess:EC2/MaliciousIPCaller.Custom`, `UnauthorizedAccess:EC2/TorClient`] then mapped `T1078` to `technique_label.value`.  
\- If `product_event_type` is `Discovery:IAMUser/AnomalousBehavior` then mapped `T1087` to `technique_label.value`.  
\- If `product_event_type` is `Persistence:IAMUser/AnomalousBehavior` then mapped `T1098` to `technique_label.value`.  
\- If `product_event_type` in [`UnauthorizedAccess:EC2/RDPBruteForce`, `UnauthorizedAccess:EC2/SSHBruteForce`] then mapped `T1110` to `technique_label.value`.  
\- If `product_event_type` in [`InitialAccess:IAMUser/AnomalousBehavior`, `UnauthorizedAccess:IAMUser/MaliciousIPCaller`, `UnauthorizedAccess:IAMUser/MaliciousIPCaller.Custom`, `UnauthorizedAccess:IAMUser/TorIPCaller`, `UnauthorizedAccess:S3/MaliciousIPCaller.Custom`, `UnauthorizedAccess:S3/TorIPCaller`] then mapped `T1133` to `technique_label.value`.  
\- If `product_event_type` is `Trojan:EC2/DriveBySourceTraffic!DNS` then mapped `T1189` to `technique_label.value`.  
\- If `product_event_type` is `PrivilegeEscalation:IAMUser/AnomalousBehavior` then mapped `T1484` to `technique_label.value`.  
\- If `product_event_type` in [`Backdoor:EC2/Spambot`, `CryptoCurrency:EC2/BitcoinTool.B`, `CryptoCurrency:EC2/BitcoinTool.B!DNS`, `Impact:EC2/AbusedDomainRequest.Reputation`, `Impact:EC2/BitcoinDomainRequest.Reputation`, `Impact:EC2/MaliciousDomainRequest.Reputation`, `Impact:EC2/PortSweep`, `Impact:EC2/SuspiciousDomainRequest.Reputation`, `Impact:EC2/WinRMBruteForce`, `UnauthorizedAccess:EC2/TorRelay`] then mapped `T1496` to `technique_label.value`.  
\- If `product_event_type` in [`Backdoor:EC2/DenialOfService.Dns`, `Backdoor:EC2/DenialOfService.Tcp`, `Backdoor:EC2/DenialOfService.Udp`, `Backdoor:EC2/DenialOfService.UdpOnTcpPorts`, `Backdoor:EC2/DenialOfService.UnusualProtocol`] then mapped `T1498` to `technique_label.value`.  
\- If `product_event_type` in [`Discovery:S3/MaliciousIPCaller`, `Discovery:S3/MaliciousIPCaller.Custom`, `Discovery:S3/TorIPCaller`] then mapped `T1526` to `technique_label.value`.  
\- If `product_event_type` is `UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B` then mapped `T1538` to `technique_label.value`.  
\- If `product_event_type` is `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration` then mapped `T1552` to `technique_label.value`.  
\- If `product_event_type` is `CredentialAccess:IAMUser/AnomalousBehavior` then mapped `T1555` to `technique_label.value`.  
\- If `product_event_type` in [`DefenseEvasion:IAMUser/AnomalousBehavior`, `Policy:S3/AccountBlockPublicAccessDisabled`, `Policy:S3/BucketAnonymousAccessGranted`, `Policy:S3/BucketBlockPublicAccessDisabled`, `Policy:S3/BucketPublicAccessGranted`, `Stealth:IAMUser/CloudTrailLoggingDisabled`, `Stealth:IAMUser/PasswordPolicyChange`, `Stealth:S3/ServerAccessLoggingDisabled`] then mapped `T1562` to `technique_label.value`.  
\- If `product_event_type` in [`Impact:IAMUser/AnomalousBehavior`, `Impact:S3/MaliciousIPCaller`] then mapped `T1565` to `technique_label.value`.  
\- If `product_event_type` is `Trojan:EC2/PhishingDomainRequest!DNS` then mapped `T1566` to `technique_label.value`.  
\- If `product_event_type` in [`Exfiltration:IAMUser/AnomalousBehavior`, `Exfiltration:S3/MaliciousIPCaller`, `Exfiltration:S3/ObjectRead.Unusual`, `Trojan:EC2/DNSDataExfiltration`, `Trojan:EC2/DropPoint`, `Trojan:EC2/DropPoint!DNS`] then mapped `T1567` to `technique_label.value`.  
\- If `product_event_type` in [`Trojan:EC2/DGADomainRequest.C!DNS`, `Trojan:EC2/DGADomainRequest.B`] then mapped `T1568` to `technique_label.value`.  
\- If `product_event_type` == `UnauthorizedAccess:EC2/MetadataDNSRebind` then mapped `T1580` to "technique_label.  
\- If `product_event_type` in [`Recon:IAMUser/MaliciousIPCaller`, `Recon:IAMUser/MaliciousIPCaller.Custom`, `Recon:IAMUser/TorIPCaller`] then mapped `T1589` to `technique_label.value`.  
\- If `product_event_type` in [`Recon:EC2/PortProbeEMRUnprotectedPort`, `Recon:EC2/PortProbeUnprotectedPort`, `Recon:EC2/Portscan`] then mapped `T1595` to `technique_label.value`.  
\- If [technique_label][value] in [`T1595`, `T1592`, `T1589`, `T1590`, `T1591`, `T1598`, `T1597`, `T1596`, `T1593`, `T1594`] then mapped `Reconnaissance` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1583`, `T1586`, `T1584`, `T1587`, `T1585`, `T1588`] then mapped `ResourceDevelopment` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1189`, `T1190`, `T1133`, `T1200`, `T1566`, `T1091`, `T1195`, `T1199`, `T1078`] then mapped `InitialAccess` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1059`, `T1203`, `T1559`, `T1106`, `T1053`, `T1129`, `T1072`, `T1569`, `T1204`, `T1047`] then mapped `Execution` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1098`, `T1197`, `T1547`, `T1037`, `T1176`, `T1554`, `T1136`, `T1543`, `T1546`, `T1133`, `T1574`, `T1525`, `T1137`, `T1542`, `T1053`, `T1505`, `T1205`, `T1078`] then mapped `Persistence` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1548`, `T1134`, `T1547`, `T1037`, `T1543`, `T1484`, `T1546`, `T1068`, `T1574`, `T1055`, `T1053`, `T1078`] then mapped `PrivilegeEscalation` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1548`, `T1134`, `T1197`, `T1140`, `T1006`, `T1484`, `T1480`, `T1211`, `T1222`, `T1564`, `T1574`, `T1562`, `T1070`, `T1202`, `T1036`, `T1556`, `T1578`, `T1112`, `T1601`, `T1599`, `T1027`, `T1542`, `T1055`, `T1207`, `T1014`, `T1218`, `T1216`, `T1553`, `T1221`, `T1205`, `T1127`, `T1535`, `T1550`, `T1078`, `T1497`, `T1600`, `T1220`] then mapped `DefenseEvasion` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1110`, `T1555`, `T1212`, `T1187`, `T1606`, `T1056`, `T1557`, `T1556`, `T1040`, `T1003`, `T1528`, `T1558`, `T1539`, `T1111`, `T1552`] then mapped `CredentialAccess` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1087`, `T1010`, `T1217`, `T1580`, `T1538`, `T1526`, `T1482`, `T1083`, `T1046`, `T1135`, `T1040`, `T1201`, `T1120`, `T1069`, `T1057`, `T1012`, `T1018`, `T1518`, `T1082`, `T1016`, `T1049`, `T1033`, `T1007`, `T1124`, `T1497`] then mapped `Discovery` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1210`, `T1534`, `T1570`, `T1563`, `T1021`, `T1091`, `T1072`, `T1080`, `T1550`] then mapped `LateralMovement` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1560`, `T1123`, `T1119`, `T1115`, `T1530`, `T1602`, `T1213`, `T1005`, `T1039`, `T1025`, `T1074`, `T1114`, `T1056`, `T1185`, `T1557`, `T1113`, `T1125`] then mapped `Collection` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1071`, `T1092`, `T1132`, `T1001`, `T1568`, `T1573`, `T1008`, `T1105`, `T1104`, `T1095`, `T1571`, `T1572`, `T1090`, `T1219`, `T1205`, `T1102`] then mapped `CommandAndControl` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1020`, `T1030`, `T1048`, `T1041`, `T1011`, `T1052`, `T1567`, `T1029`, `T1537`] then mapped `Exfiltration` to `tatic_label.value`.  
\- If [technique_label][value] in [`T1531`, `T1485`, `T1486`, `T1565`, `T1491`, `T1561`, `T1499`, `T1495`, `T1490`, `T1498`, `T1496`, `T1489`, `T1529`] then mapped `Impact` to `tatic_label.value`.   
2022-11-10 |  Enhancement  
\- Mapped `service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.hash` to `principal.file.sha256`.  
\- Mapped `service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.filePath` to `principal.file.full_path`.  
\- Mapped `service.action.dnsRequestAction.domain` to `network.dns.questions.name`.  
\- Mapped `resource.kubernetesDetails.kubernetesUserDetails.username` to `principal.user.userid`.   
2022-09-12 |  Feature Request:  
\- Mapped `security_result.category`, `metadata.event_type`, `resource_type`, `resource_subtype` appropriately for logs types - `IAM`, `S3`, `KUBERNETES`, `MALWARE`, `EC2`.   
2022-08-11 |  Feature Request:  
\- Replaced `GENERIC_EVENT` type to `STATUS_UPDATE` or `USER_RESOURCE_ACCESS` event_type.   
2022-07-20 |  Enhancement:  
\- Changed mapping for `service.resourceRole` from `additional.resource_role` to `principal.resource.attribute.roles.name`.  
\- Changed mapping for `service.count` from `additional.fields` to `principal.resource.attribute.label`  
\- Changed mapping for `resource.instanceDetails.imageDescription` from `additional.fields` to `principal.resource.attribute.label`  
\- if `type` value in `Discovery:S3/MaliciousIPCaller`, `Policy:S3/BucketPublicAccessGranted`, `UnauthorizedAccess:S3/TorIPCaller`, `Policy:S3/BucketAnonymousAccessGranted`, `UnauthorizedAccess:EC2/TorRelay`:  
\- mapped `resource.instanceDetails.instanceId` to `target.resource.product_object_id`  
\- mapped `resource.instanceDetails.instanceType` to `target.resource.name`  
2022-07-08 |  Enhancement:  
\- Modified mapping for `network_interface.securityGroups.0.groupId` from `target.user.groupid` to `target.user.group_identifiers`.   
2022-05-27 |  Enhancement - Modified the value stored in metadata.product_name to `AWS GuardDuty` and metadata.vendor_name to `AMAZON`.   
2022-05-26 |  Enhancement - Modified mappings for following fields  
\- Changed mapping for field `region` from `target.location.country_or_region` to `target.location.name`  
\- Changed mapping for field `resource.instanceDetails.tags[n]` from `additional.fields[n]` to `target.asset.attribute.labels[n]`  
\- `service.action.networkConnectionAction.remoteIpDetails.country.countryName` mapped to `target.location.country_or_region`  
2022-03-31 |  Enhancement  
If service.action.networkConnectionAction.localPortDetails.portName is not `Unknown` value mapped to principal.application.  
Entire list within `tags` field mapped to key-value fields.  
`service.action.networkConnectionAction.protocol` mapped to network.ip_protocol  
`service.action.networkConnectionAction.blocked` mapped to security_result.action  
`severity` mapped to security_result.severity_details  
If service.action.actionType is AWS_API_CALL, `accessKeyId` mapped to target.resource.id.  
In s3BucketDetails:  
\- `arn` mapped to target.asset.attribute.cloud.project.product_object_id.  
\- `name` mapped to target.resource.name.  
\- `encryptionType` mapped to network.tls.supported_ciphers.  
\- "owner.id mapped to target.resource.attribute.labels.  
Under resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList:  
\- mapped `allowsPublicReadAccess` to additional.fields attribute.  
\- mapped `allowsPublicWriteAccess` to additional.fields attribute.  
\---  
Under resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy:  
\- mapped `allowsPublicReadAccess` to additional.fields attribute.  
\- mapped `allowsPublicWriteAccess` to additional.fields attribute.  
\---  
Under resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess:  
\- mapped `ignorePublicAcls` to additional.fields attribute.  
\- mapped `restrictPublicBuckets` to additional.fields attribute.  
\- mapped `blockPublicAcls` to additional.fields attribute.  
\- mapped `blockPublicPolicy` to additional.fields attribute.  
\---  
Under resource.s3BucketDetails.0.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess  
mapped ignorePublicAcls to additional.fields attribute.  
`restrictPublicBuckets` to additional.fields attribute.  
`blockPublicAcls` to additional.fields attribute.  
`blockPublicPolicy` to additional.fields attribute.  
Under service.action.awsApiCallAction.remoteIpDetails.organization:  
\- `asn` mapped to additional.fields attribute.  
\- `asnOrg` mapped to additional.fields attribute.  
\- `isp` mapped to additional.fields attribute.  
\- `org` mapped to additional.fields attribute.  
Under service.action.awsApiCallAction.affectedResources, mapped `AWS::S3::Bucket` additional.fields attribute.  
If service.action.actionType is DNS_REQUEST, `accessKeyId` mapped to target.resource.id.  
\- resource.instanceDetails.instanceId mapped to target.resource.id  
\- resource.instanceDetails.instanceType mapped to target.resource.name  
\- resource.instanceDetails.networkInterfaces.0.vpcId mapped to target.asset.attribute.cloud.vpc.id  
Values under resource.instanceDetails.tags mapped the following fields:  
\- target.user.userid if the key is `ApplicationOwner`.  
\- target.application if the key is `Application`.  
\- user.email_addresses if the key is `Contact`.  
\- additional.fields if the key is `Name`, `DAM_Project`, `Project`, or `ehc:C3Schedule`.  
service.action.dnsRequestAction.protocol mapped network.ip_protocol if value is not 0.  
service.action.networkConnectionAction.blocked mapped to security_result.action.  
`severity` mapped to security_result.severity_details.   
2022-03-25 |  Enhancement - Port udm is not a repeated field. This makes it unsuitable to capture a lot of ports from a log. This change uses about.port instead.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
