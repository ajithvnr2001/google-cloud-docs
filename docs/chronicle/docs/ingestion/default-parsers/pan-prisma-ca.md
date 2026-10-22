---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-ca/
title: Collect Palo Alto Prisma Cloud alert logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:43.693502+00:00
---

# Collect Palo Alto Prisma Cloud alert logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Palo Alto Prisma Cloud alert logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts alert logs from Palo Alto Prisma Cloud in JSON format, transforming them into the UDM. The parser performs data normalization, type conversions, and conditional logic to populate the appropriate UDM fields. It also handles nested JSON structures and arrays within the log data to extract relevant information. The information in this document applies to the parser with the PAN_PRISMA_CA ingestion label.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to Palo Alto Prisma Cloud.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **PAN Prisma Cloud Alerts**.
  5. Select **Webhook** as the **Source type**.
  6. Select **Palo Alto Prisma Cloud Alerts payload** as the **Log type**.
  7. Click **Next**.
  8. Optional: Specify values for the following input parameters: 
     * **Split delimiter** : the delimiter that is used to separate log lines, such as `\n`.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.
  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  12. Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
  13. From the **Details** tab, copy the feed endpoint URL from the **Endpoint Information** field. You need to specify this endpoint URL in your client application.
  14. Click **Done**.



## Create an API key for the webhook feed

  1. Go to **Google Cloud console > Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials** , and then select **API key**.

  3. Restrict the API key access to the **Google Security Operations API**.




## Specify the endpoint URL

  1. In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
  2. Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
         
         X-goog-api-key = API_KEY
         X-Webhook-Access-Key = SECRET
         

**Recommendation** : Specify the API key as a header instead of specifying it in the URL.

  3. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
         
         ENDPOINT_URL?key=API_KEY&secret=SECRET
         

Replace the following:

     * `ENDPOINT_URL`: the feed endpoint URL.
     * `API_KEY`: the API key to authenticate to Google Security Operations.
     * `SECRET`: the secret key that you generated to authenticate the feed.



## Configure Palo Alto Prisma Cloud webhook to Google SecOps

  1. Sign in to Palo Alto Prisma Cloud.
  2. Select **Settings** > **Integrations & Notification** ((and_then)) **Integrations**.
  3. Click **Add Integration**.
  4. Select **Webhook**.
  5. Specify values for the following input parameters: 
     * **Integration Name** : Provide a unique and descriptive name (for example, **Google SecOps**)
     * **Webhook URL** : Enter the ENDPOINT_URL.
     * Optional: Provide a **Description** of the integration.
     * Optional: Enable **Custom Payload** > click **Next** to review or revise the custom payload.
  6. Click **Next**.
  7. **Test** and **Save Integration**.



## Configure Palo Alto Prisma Cloud alerts

  1. In the Palo Alto Prisma Cloud console, go to **Alerts** > **View Alert Rules**.
  2. Select an existing alert rule to edit.
  3. Optional: [Create new Alert for **Cloud Infrastructure**](https://docs.prismacloud.io/en/enterprise-edition/content-collections/alerts/create-an-alert-rule-cloud-infrastructure).
  4. Optional: [Create new Alert for **Cloud Workload**](https://docs.prismacloud.io/en/enterprise-edition/content-collections/alerts/create-an-alert-rule-cloud-workloads).
  5. Go to **Configure Notifications**.
  6. Select **Webhook**.
  7. Optional: Select the Channels that you want to send notifications of alerts triggered by the alert rule.
  8. Click **Next**.
  9. Click **Save**.



## UDM mapping table

The following table lists the UDM fields mapped from Palo Alto Prisma Cloud Alert payload log fields:

Log field | UDM mapping  
---|---  
`_id` | `metadata.product_log_id`  
`account.cloudType` | `principal.resource.attribute.cloud.environment`  
`account.id` | `additional.fields`  
`account.name` | `additional.fields`  
`account_id_body` | `target.user.userid`  
`accountId` | `target.resource.product_object_id`  
`accountIDs` | `additional.fields`  
`accountName` | `target.resource.attribute.labels`  
`accountOwners` | `principal.user.email_addresses`,  
`principal.user.attribute.labels`  
`acknowledged` | `security_result.detection_fields`  
`additionalInfo.*` | `security_result.detection_fields`  
`aggregatedAlerts.*` | `about.resource.attribute.labels`,  
`target.resource.attribute.labels`  
`aggregatedAlerts.accountIDs` | `target.resource.attribute.labels`  
`aggregatedAlerts.clusters` | `target.resource.attribute.labels`  
`aggregatedAlerts.collections` | `target.resource.attribute.labels`  
`aggregatedAlerts.command` | `about.process.command_line`  
`aggregatedAlerts.complianceIssues.*` | `security_result.detection_fields`  
`aggregatedAlerts.container` | `about.resource.name`  
`aggregatedAlerts.containerID` | `about.resource.product_object_id`  
`aggregatedAlerts.forensics` | `about.url`  
`aggregatedAlerts.fqdn` | `about.domain.name`  
`aggregatedAlerts.host` | `about.hostname`  
`aggregatedAlerts.labels.aadpodidbinding` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.app_kubernetes.io_component` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.app_kubernetes.io_part_of` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.io.kubernetes.container.name` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.io.kubernetes.pod.namespace` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.io.kubernetes.pod.uid` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.networking/gateway-ingress` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.pod-template-hash` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.product` | `about.resource.attribute.labels`  
`aggregatedAlerts.labels.role` | `about.resource.attribute.labels`  
`aggregatedAlerts.namespaces` | `target.resource.attribute.labels`  
`aggregatedAlerts.region` | `about.resource.attribute.cloud.availability_zone`  
`aggregatedAlerts.user` | `about.user.userid`  
`aggregatedAlerts.vulnerabilities.accountIDs` | `extensions.vulns.vulnerabilities.about.resource.attribute.labels`  
`aggregatedAlerts.vulnerabilities.clusters` | `extensions.vulns.vulnerabilities.about.resource.attribute.labels`  
`aggregatedAlerts.vulnerabilities.collections` | `extensions.vulns.vulnerabilities.about.resource.attribute.labels`  
`aggregatedAlerts.vulnerabilities.distribution` | `extensions.vulns.vulnerabilities.name`  
`aggregatedAlerts.vulnerabilities.imageID` | `extensions.vulns.vulnerabilities.about.file.sha256`  
`aggregatedAlerts.vulnerabilities.imageName` | `extensions.vulns.vulnerabilities.about.file.full_path`  
`aggregatedAlerts.vulnerabilities.namespaces` | `extensions.vulns.vulnerabilities.about.resource.attribute.labels`  
`aggregatedAlerts.vulnerabilities.newVulnerabilities.vulnerabilities.cve` | `extensions.vulns.vulnerabilities.cve_id`  
`aggregatedAlerts.vulnerabilities.newVulnerabilities.vulnerabilities.link` | `extensions.vulns.vulnerabilities.about.url`  
`aggregatedAlerts.vulnerabilities.newVulnerabilities.vulnerabilities.packages` | `target.resource.attribute.labels`  
`aggregatedAlerts.vulnerabilities.newVulnerabilities.vulnerabilities.packageVersion` | `target.resource.attribute.labels`  
`aggregatedAlerts.vulnerabilities.newVulnerabilities.vulnerabilities.severity` | `extensions.vulns.vulnerabilities.severity`,  
`extensions.vulns.vulnerabilities.severity_details`  
`aggregatedAlerts.vulnerabilities.newVulnerabilities.vulnerabilities.sourcePackage` | `target.resource.attribute.labels`  
`aggregatedAlerts.vulnerabilities.newVulnerabilities.vulnerabilities.status` | `extensions.vulns.vulnerabilities.description`  
`alarmType` | `principal.asset.attribute.cloud.environment`,  
`security_result.detection_fields`  
`alertId` | `security_result.detection_fields`  
`alertRemediationCli` | `security_result.detection_fields`  
`alertRemediationCliDescription` | `security_result.detection_fields`  
`alertRemediationImpact` | `security_result.detection_fields`  
`alertRuleId` | `security_result.rule_id`  
`alertRuleName` | `security_result.rule_name`  
`alertStatus` | `security_result.detection_fields`  
`alertTime` | `security_result.first_discovered_time`  
`alertTs` | `security_result.first_discovered_time`  
`App` | `principal.application`  
`audits._id` | `additional.fields`  
`audits.accountID` | `about.resource.attribute.labels`  
`audits.attackTechniques` | `additional.fields`  
`audits.attackType` | `security_result.threat_name`,  
`security_result.detection_fields`  
`audits.cluster` | `about.resource.attribute.labels`  
`audits.command` | `about.process.command_line`  
`audits.container` | `additional.fields`  
`audits.containerId` | `about.resource.attribute.labels`  
`audits.containerName` | `about.resource.attribute.labels`  
`audits.count` | `additional.fields`  
`audits.effect` | `security_result.action_details`,  
`security_result.detection_fields`  
`audits.hostname` | `about.hostname`  
`audits.imageId` | `about.resource.attribute.labels`  
`audits.imageName` | `about.resource.attribute.labels`  
`audits.msg` | `metadata.description`,  
`about.resource.attribute.labels`  
`audits.namespace` | `about.namespace`  
`audits.os` | `about.platform_version`  
`audits.pid` | `about.process.pid`  
`audits.processPath` | `about.process.file.full_path`  
`audits.profileId` | `about.resource.attribute.labels`  
`audits.provider` | `about.resource.attribute.cloud.environment`  
`audits.region` | `about.location.country_or_region`  
`audits.ruleName` | `security_result.rule_name`,  
`security_result.detection_fields`  
`audits.severity` | `security_result.severity`,  
`security_result.severity_details`,  
`security_result.detection_fields`  
`audits.time` | `about.resource.attribute.labels`  
`audits.type` | `metadata.product_event_type`,  
`about.resource.attribute.labels`  
`audits.user` | `about.user.userid`  
`body` | `additional.fields`  
`callbackUrl` | `metadata.url_back_to_product`  
`category` | `security_result.category_details`  
`cluster` | `principal.resource.attribute.labels`  
`clusters` | `additional.fields`  
`cloudAccountGroups` | `target.user.group_identifiers`  
`cloudAccountOwners` | `target.user.email_addresses`,  
`target.user.attribute.labels`  
`cloudServiceName` | `target.resource.attribute.labels`  
`cloudType` | `principal.resource.attribute.cloud.environment`  
`collections` | `additional.fields`  
`command` | `principal.process.command_line`  
`complianceIssues.*` | `security_result.detection_fields`  
`complianceIssues.category` | `security_result.category_details`,  
`security_result.detection_fields`  
`complianceIssues.description` | `security_result.description`,  
`security_result.detection_fields`  
`complianceIssues.id` | `security_result.detection_fields`  
`complianceIssues.severity` | `security_result.severity`,  
`security_result.severity_details`,  
`security_result.detection_fields`  
`complianceIssues.title` | `security_result.action_details`,  
`security_result.detection_fields`  
`complianceIssues.type` | `security_result.detection_fields`  
`complianceMetadata.*` | `security_result.detection_fields`  
`container` | `target.resource.name`  
`containerID` | `principal.asset.asset_id`,  
`target.resource.product_object_id`  
`containerName` | `principal.resource.name`  
`data.allocationId` | `principal.resource.product_object_id`  
`data.attachments.*` | `additional.fields`  
`data.createTime` | `target.resource.attribute.creation_time`  
`data.publicIp` | `principal.ip`,  
`principal.asset.ip`  
`data.*` | `additional.fields`  
`deleted` | `additional.fields`  
`description` | `metadata.description`  
`dropped` | `security_result.detection_fields`  
`email_add` | `principal.user.email_addresses`  
`errorMessage` | `metadata.description`  
`firstSeen` | `principal.asset.first_seen_time`  
`forensics` | `security_result.url_back_to_product`  
`fqdn` | `principal.domain.name`  
`hasFinding` | `security_result.detection_fields`  
`host` | `principal.hostname`,  
`principal.asset.hostname`  
`hostname` | `principal.hostname`,  
`principal.asset.hostname`  
`id` | `metadata.product_log_id`  
`image` | `target.process.file.full_path`  
`imageID` | `principal.process.file.sha256`,  
`target.process.file.sha256`  
`imageName` | `principal.process.file.full_path`  
`incidentTime` | `security_result.first_discovered_time`  
`investigateOptions.*` | `security_result.detection_fields`  
`labels` | `additional.fields`  
`labels.aadpodidbinding` | `target.resource.attribute.labels`  
`labels.app` | `target.application`  
`labels.app_kubernetes.io_component` | `target.resource.attribute.labels`  
`labels.app_kubernetes.io_part_of` | `target.resource.attribute.labels`  
`labels.io.kubernetes.container.name` | `target.resource.attribute.labels`  
`labels.io.kubernetes.pod.name` | `target.hostname`,  
`target.asset.hostname`  
`labels.io.kubernetes.pod.namespace` | `target.resource.attribute.labels`  
`labels.io.kubernetes.pod.uid` | `target.resource.attribute.labels`  
`labels.networking/gateway-ingress` | `target.resource.attribute.labels`  
`labels.owner` | `target.user.userid`  
`labels.pod-template-hash` | `target.resource.attribute.labels`  
`labels.product` | `target.resource.attribute.labels`  
`labels.role` | `target.resource.attribute.labels`  
`lastModifiedBy` | `principal.user.email_addresses`  
`lastModifiedOn` | `security_result.detection_fields`  
`lastSeen` | `principal.asset.first_discover_time`  
`lastUpdated` | `security_result.detection_fields`  
`message` | `security_result.description`  
`msg_metadata.remediable` | `security_result.detection_fields`  
`msg_metadata.saveSearchId` | `security_result.detection_fields`  
`name` | `security_result.summary`  
`namespace` | `principal.namespace`  
`namespaces` | `additional.fields`  
`notificationRuleName` | `security_result.rule_name`  
`policy.complianceMetadata.*` | `security_result.detection_fields`  
`policy.description` | `security_result.detection_fields`  
`policy.deleted` | `additional.fields`  
`policy.hasSearchExecutionSupport` | `security_result.detection_fields`  
`policy.id` | `security_result.detection_fields`  
`policy.lastModifiedBy` | `principal.user.email_addresses`  
`policy.lastModifiedOn` | `security_result.detection_fields`  
`policy.name` | `security_result.description`  
`policy.policyId` | `security_result.detection_fields`  
`policy.policyType` | `security_result.detection_fields`  
`policy.policyTs` | `security_result.detection_fields`  
`policy.recommendation` | `security_result.detection_fields`  
`policy.remediable` | `security_result.detection_fields`  
`policy.severity` | `security_result.severity`,  
`security_result.severity_details`  
`policy.systemDefault` | `security_result.detection_fields`  
`policyDescription` | `security_result.detection_fields`  
`policyId` | `security_result.detection_fields`  
`policyLabels` | `additional.fields`  
`policyName` | `security_result.description`  
`policyRecommendation` | `security_result.detection_fields`  
`policyType` | `security_result.detection_fields`  
`profileID` | `additional.fields`  
`provider` | `target.resource.attribute.cloud.environment`  
`reason` | `security_result.summary`  
`recommendation` | `security_result.detection_fields`  
`remediable` | `security_result.detection_fields`  
`region` | `principal.location.country_or_region`,  
`principal.location.state`,  
`target.resource.attribute.cloud.availability_zone`  
`resource.account` | `additional.fields`  
`resource.accountId` | `target.resource.product_object_id`,  
`additional.fields`  
`resource.additionalInfo.*` | `security_result.detection_fields`  
`resource.cloudAccountGroups` | `target.user.group_identifiers`  
`resource.cloudAccountOwners` | `target.user.email_addresses`,  
`target.user.attribute.labels`  
`resource.cloudServiceName` | `target.resource.attribute.labels`  
`resource.cloudType` | `principal.resource.attribute.cloud.environment`,  
`principal.resource.attribute.labels`  
`resource.data.*` | `additional.fields`  
`resource.data.addonsConfig.dnsCacheConfig.enabled` | `additional.fields`  
`resource.data.addonsConfig.gcePersistentDiskCsiDriverConfig.enabled` | `additional.fields`  
`resource.data.addonsConfig.gcpFilestoreCsiDriverConfig.enabled` | `additional.fields`  
`resource.data.addonsConfig.gcsFuseCsiDriverConfig.enabled` | `additional.fields`  
`resource.data.addonsConfig.kubernetesDashboard.disabled` | `additional.fields`  
`resource.data.addonsConfig.networkPolicyConfig.disabled` | `additional.fields`  
`resource.data.allowed.IPProtocol` | `additional.fields`  
`resource.data.allowed.ports` | `additional.fields`  
`resource.data.arn` | `principal.resource.attribute.labels`  
`resource.data.attributes.access_logs.s3.enabled` | `additional.fields`  
`resource.data.attributes.deletion_protection.enabled` | `additional.fields`  
`resource.data.attributes.dns_record.client_routing_policy` | `additional.fields`  
`resource.data.attributes.load_balancing.cross_zone.enabled` | `additional.fields`  
`resource.data.attributes.secondary_ips.auto_assigned.per_subnet` | `additional.fields`  
`resource.data.attributes.zonal_shift.config.enabled` | `additional.fields`  
`resource.data.authenticatorGroupsConfig.enabled` | `target.group.attribute.labels`  
`resource.data.authenticatorGroupsConfig.securityGroup` | `target.group.email_addresses`  
`resource.data.authorizationRules.*` | `additional.fields`  
`resource.data.authorizationRules.properties.rights` | `additional.fields`  
`resource.data.autoscaling.autoscalingProfile` | `additional.fields`  
`resource.data.availabilityZones.*` | `additional.fields`  
`resource.data.blockDeviceMappings.deviceName` | `additional.fields`  
`resource.data.blockDeviceMappings.ebs.*` | `additional.fields`  
`resource.data.capacityReservationSpecification.capacityReservationPreference` | `additional.fields`  
`resource.data.Command.*` | `additional.fields`  
`resource.data.Command.ScriptLocation` | `target.process.file.full_path`  
`resource.data.conditions.*` | `additional.fields`  
`resource.data.controlPlaneEndpointsConfig.dnsEndpointConfig.*` | `additional.fields`  
`resource.data.controlPlaneEndpointsConfig.ipEndpointsConfig.*` | `additional.fields`  
`resource.data.controlPlaneEndpointsConfig.ipEndpointsConfig.authorizedNetworksConfig.privateEndpointEnforcementEnabled` | `additional.fields`  
`resource.data.controlPlaneEndpointsConfig.ipEndpointsConfig.privateEndpoint` | `target.ip`,  
`target.asset.ip`  
`resource.data.controlPlaneEndpointsConfig.ipEndpointsConfig.publicEndpoint` | `target.ip`,  
`target.asset.ip`  
`resource.data.cpuOptions.coreCount` | `additional.fields`  
`resource.data.cpuOptions.threadsPerCore` | `additional.fields`  
`resource.data.createDate` | `principal.resource.attribute.labels`  
`resource.data.createdDate` | `principal.resource.attribute.labels`  
`resource.data.createdTime` | `target.resource.attribute.creation_time`  
`resource.data.CreatedOn` | `target.resource.attribute.creation_time`  
`resource.data.createTime` | `target.resource.attribute.creation_time`  
`resource.data.creationTimestamp` | `principal.resource.attribute.labels`  
`resource.data.databaseEncryption.*` | `additional.fields`  
`resource.data.DefaultArguments.*` | `additional.fields`  
`resource.data.defaultMaxPodsConstraint.maxPodsPerNode` | `additional.fields`  
`resource.data.deleteRetentionPolicy.blob.*` | `additional.fields`  
`resource.data.description` | `principal.resource.attribute.labels`  
`resource.data.diagnosticSettings.*` | `additional.fields`  
`resource.data.diagnosticSettings.properties.*` | `additional.fields`  
`resource.data.diagnosticSettings.properties.logs.*` | `additional.fields`  
`resource.data.diagnosticSettings.properties.metrics.*` | `additional.fields`  
`resource.data.direction` | `principal.resource.attribute.labels`,  
`network.direction`  
`resource.data.disks.*` | `additional.fields`  
`resource.data.displayName` | `target.user.user_display_name`  
`resource.data.document.Statement.*` | `additional.fields`  
`resource.data.document.Statement.Action.*` | `additional.fields`  
`resource.data.document.Statement.Resource.*` | `additional.fields`  
`resource.data.document.Version` | `additional.fields`  
`resource.data.enclaveOptions.enabled` | `additional.fields`  
`resource.data.encryptionStatuses.*` | `additional.fields`  
`resource.data.endpoint` | `target.ip`,  
`target.asset.ip`  
`resource.data.enterpriseConfig.clusterTier` | `additional.fields`  
`resource.data.entities.policyRoles.*` | `additional.fields`  
`resource.data.ExecutionProperty.MaxConcurrentRuns` | `additional.fields`  
`resource.data.hibernationOptions.configured` | `additional.fields`  
`resource.data.id` | `principal.resource.attribute.labels`  
`resource.data.identity.type` | `additional.fields`  
`resource.data.instanceGroupUrls` | `additional.fields`  
`resource.data.ipAllocationPolicy.*` | `target.resource.attribute.labels`  
`resource.data.ipAllocationPolicy.networkTierConfig.networkTier` | `target.resource.attribute.labels`  
`resource.data.kind` | `principal.resource.attribute.labels`  
`resource.data.lastAccessedDate` | `principal.resource.attribute.labels`  
`resource.data.lastChangedDate` | `principal.resource.attribute.labels`  
`resource.data.listeners.*` | `additional.fields`  
`resource.data.listeners.rules.*` | `additional.fields`  
`resource.data.listeners.rules.actions.*` | `additional.fields`  
`resource.data.listeners.rules.actions.forwardConfig.targetGroups.*` | `additional.fields`  
`resource.data.loadBalancerName` | `target.resource.name`  
`resource.data.location` | `principal.resource.attribute.labels`  
`resource.data.locations` | `additional.fields`  
`resource.data.logConfig.enable` | `additional.fields`  
`resource.data.loggingConfig.componentConfig.enableComponents` | `additional.fields`  
`resource.data.loggingProperties.blob.*` | `additional.fields`  
`resource.data.loggingProperties.queue.*` | `additional.fields`  
`resource.data.loggingProperties.table.*` | `additional.fields`  
`resource.data.mail` | `target.user.email_addresses`  
`resource.data.maintenancePolicy.resourceVersion` | `additional.fields`  
`resource.data.maintenancePolicy.window.recurringWindow.recurrence` | `additional.fields`  
`resource.data.maintenancePolicy.window.recurringWindow.window.endTime` | `additional.fields`  
`resource.data.maintenancePolicy.window.recurringWindow.window.startTime` | `additional.fields`  
`resource.data.masterAuth.clusterCaCertificate` | `additional.fields`  
`resource.data.masterAuthorizedNetworksConfig.privateEndpointEnforcementEnabled` | `additional.fields`  
`resource.data.metadata.items` | `additional.fields`  
`resource.data.metadataOptions.*` | `additional.fields`  
`resource.data.monitoring.state` | `additional.fields`  
`resource.data.monitoringConfig.componentConfig.enableComponents` | `additional.fields`  
`resource.data.monitoringConfig.managedPrometheusConfig.enabled` | `additional.fields`  
`resource.data.msg_metadata.fingerprint` | `additional.fields`  
`resource.data.msg_metadata.kind` | `additional.fields`  
`resource.data.Name` | `target.resource.name`  
`resource.data.name` | `principal.resource.attribute.labels`  
`resource.data.network` | `principal.resource.attribute.labels`  
`resource.data.networkConfig.*` | `additional.fields`  
`resource.data.networkConfig.dnsConfig.clusterDns` | `additional.fields`  
`resource.data.networkConfig.dnsConfig.clusterDnsScope` | `additional.fields`  
`resource.data.networkConfig.gatewayApiConfig.channel` | `additional.fields`  
`resource.data.networkInterfaces.*` | `additional.fields`  
`resource.data.networkInterfaces.aliasIpRanges.*` | `additional.fields`  
`resource.data.networkInterfaces.attachment.*` | `additional.fields`  
`resource.data.networkInterfaces.groups.*` | `additional.fields`  
`resource.data.networkInterfaces.macAddress` | `target.mac`,  
`target.asset.mac`  
`resource.data.networkInterfaces.networkIP` | `target.ip`,  
`target.asset.ip`  
`resource.data.networkInterfaces.operator.managed` | `additional.fields`  
`resource.data.networkInterfaces.privateIpAddress` | `target.ip`,  
`target.asset.ip`  
`resource.data.networkPerformanceOptions.bandwidthWeighting` | `additional.fields`  
`resource.data.networkRuleSet.*` | `additional.fields`  
`resource.data.networkRuleSet.properties.*` | `additional.fields`  
`resource.data.nodeConfig.*` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.bootDisk.diskType` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.bootDisk.sizeGb` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.kubeletConfig.insecureKubeletReadonlyPortEnabled` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.kubeletConfig.maxParallelImagePulls` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.msg_metadata.disable-legacy-endpoints` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.nodeImageConfig.image` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.nodeImageConfig.imageProject` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.oauthScopes` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.resourceLabels.goog-gke-node-pool-provisioning-model` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.serviceAccount` | `target.user.email_addresses`,  
`target.user.userid`  
`resource.data.nodeConfig.shieldedInstanceConfig.enableIntegrityMonitoring` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.tags` | `target.resource.attribute.labels`  
`resource.data.nodeConfig.workloadMetadataConfig.mode` | `target.resource.attribute.labels`  
`resource.data.nodePoolAutoConfig.networkTags.tags` | `additional.fields`  
`resource.data.nodePoolAutoConfig.nodeKubeletConfig.insecureKubeletReadonlyPortEnabled` | `additional.fields`  
`resource.data.nodePoolDefaults.nodeConfigDefaults.loggingConfig.variantConfig.variant` | `additional.fields`  
`resource.data.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.insecureKubeletReadonlyPortEnabled` | `additional.fields`  
`resource.data.nodePools.*` | `additional.fields`  
`resource.data.nodePools.autoscaling.*` | `additional.fields`  
`resource.data.nodePools.config.*` | `additional.fields`  
`resource.data.nodePools.instanceGroupUrls` | `additional.fields`  
`resource.data.nodePools.locations` | `additional.fields`  
`resource.data.nodePools.management.*` | `additional.fields`  
`resource.data.nodePools.maxPodsConstraint.*` | `additional.fields`  
`resource.data.nodePools.networkConfig.*` | `additional.fields`  
`resource.data.nodePools.upgradeSettings.*` | `additional.fields`  
`resource.data.operator.hiddenByDefault` | `additional.fields`  
`resource.data.operator.managed` | `additional.fields`  
`resource.data.placement.*` | `additional.fields`  
`resource.data.podAutoscaling.hpaProfile` | `additional.fields`  
`resource.data.policyArn` | `principal.resource.attribute.labels`  
`resource.data.policyName` | `principal.resource.attribute.labels`  
`resource.data.privateClusterConfig.*` | `additional.fields`  
`resource.data.privateDnsName` | `target.hostname`,  
`target.asset.hostname`  
`resource.data.privateIpAddress` | `target.ip`,  
`target.asset.ip`  
`resource.data.properties.*` | `additional.fields`  
`resource.data.properties.aadProfile.enableAzureRBAC` | `additional.fields`  
`resource.data.properties.aadProfile.managed` | `additional.fields`  
`resource.data.properties.aadProfile.tenantID` | `additional.fields`  
`resource.data.properties.addonProfiles.azureKeyvaultSecretsProvider.config.enableSecretRotation` | `additional.fields`  
`resource.data.properties.addonProfiles.azureKeyvaultSecretsProvider.config.rotationPollInterval` | `additional.fields`  
`resource.data.properties.addonProfiles.azureKeyvaultSecretsProvider.enabled` | `additional.fields`  
`resource.data.properties.addonProfiles.azureKeyvaultSecretsProvider.identity.clientId` | `additional.fields`  
`resource.data.properties.addonProfiles.azureKeyvaultSecretsProvider.identity.objectId` | `additional.fields`  
`resource.data.properties.addonProfiles.azureKeyvaultSecretsProvider.identity.resourceId` | `additional.fields`  
`resource.data.properties.addonProfiles.azurepolicy.config.version` | `additional.fields`  
`resource.data.properties.addonProfiles.azurepolicy.enabled` | `additional.fields`  
`resource.data.properties.addonProfiles.azurepolicy.identity.clientId` | `additional.fields`  
`resource.data.properties.addonProfiles.azurepolicy.identity.objectId` | `additional.fields`  
`resource.data.properties.addonProfiles.azurepolicy.identity.resourceId` | `additional.fields`  
`resource.data.properties.addonProfiles.omsagent.config.logAnalyticsWorkspaceResourceID` | `additional.fields`  
`resource.data.properties.addonProfiles.omsagent.config.useAADAuth` | `additional.fields`  
`resource.data.properties.addonProfiles.omsagent.enabled` | `additional.fields`  
`resource.data.properties.addonProfiles.omsagent.identity.clientId` | `additional.fields`  
`resource.data.properties.addonProfiles.omsagent.identity.objectId` | `additional.fields`  
`resource.data.properties.addonProfiles.omsagent.identity.resourceId` | `additional.fields`  
`resource.data.properties.agentPoolProfiles.*` | `additional.fields`  
`resource.data.properties.agentPoolProfiles.availabilityZones` | `additional.fields`  
`resource.data.properties.agentPoolProfiles.nodeLabels.nodepool` | `additional.fields`  
`resource.data.properties.agentPoolProfiles.powerState.code` | `additional.fields`  
`resource.data.properties.agentPoolProfiles.tags.*` | `additional.fields`  
`resource.data.properties.apiServerAccessProfile.disableRunCommand` | `additional.fields`  
`resource.data.properties.apiServerAccessProfile.enablePrivateCluster` | `additional.fields`  
`resource.data.properties.apiServerAccessProfile.enablePrivateClusterPublicFQDN` | `additional.fields`  
`resource.data.properties.apiServerAccessProfile.privateDNSZone` | `additional.fields`  
`resource.data.properties.autoScalerProfile.*` | `additional.fields`  
`resource.data.properties.autoUpgradeProfile.upgradeChannel` | `additional.fields`  
`resource.data.properties.httpProxyConfig.effectiveNoProxy` | `additional.fields`  
`resource.data.properties.httpProxyConfig.httpProxy` | `additional.fields`  
`resource.data.properties.httpProxyConfig.httpsProxy` | `additional.fields`  
`resource.data.properties.httpProxyConfig.noProxy` | `additional.fields`  
`resource.data.properties.httpProxyConfig.trustedCa` | `additional.fields`  
`resource.data.properties.identityProfile.kubeletidentity.*` | `additional.fields`  
`resource.data.properties.linuxProfile.adminUsername` | `additional.fields`  
`resource.data.properties.linuxProfile.ssh.publicKeys.*` | `additional.fields`  
`resource.data.properties.networkProfile.*` | `target.resource.attribute.labels`  
`resource.data.properties.networkProfile.dnsServiceIP` | `target.ip`,  
`target.asset.ip`  
`resource.data.properties.networkProfile.ipFamilies` | `target.resource.attribute.labels`  
`resource.data.properties.networkProfile.serviceCidrs` | `target.resource.attribute.labels`  
`resource.data.properties.powerState.code` | `additional.fields`  
`resource.data.properties.principalId` | `target.user.product_object_id`  
`resource.data.properties.privateFQDN` | `target.hostname`,  
`target.asset.hostname`  
`resource.data.properties.privateLinkResources.*` | `additional.fields`  
`resource.data.properties.privateLinkResources.requiredMembers` | `additional.fields`  
`resource.data.properties.roleDefinition.*` | `additional.fields`  
`resource.data.properties.roleDefinition.properties.*` | `additional.fields`  
`resource.data.properties.roleDefinition.properties.assignableScopes` | `additional.fields`  
`resource.data.properties.roleDefinition.properties.permissions.actions` | `additional.fields`  
`resource.data.properties.roleDefinition.properties.permissions.notActions` | `additional.fields`  
`resource.data.properties.servicePrincipalProfile.clientId` | `additional.fields`  
`resource.data.properties.storageProfile.diskCSIDriver.enabled` | `additional.fields`  
`resource.data.properties.storageProfile.fileCSIDriver.enabled` | `additional.fields`  
`resource.data.properties.storageProfile.snapshotController.enabled` | `additional.fields`  
`resource.data.properties.windowsProfile.adminUsername` | `additional.fields`  
`resource.data.properties.windowsProfile.enableCSIProxy` | `additional.fields`  
`resource.data.rbacBindingConfig.enableInsecureBindingSystemAuthenticated` | `additional.fields`  
`resource.data.rbacBindingConfig.enableInsecureBindingSystemUnauthenticated` | `additional.fields`  
`resource.data.releaseChannel.channel` | `additional.fields`  
`resource.data.resourceGroup` | `principal.resource.attribute.labels`  
`resource.data.resourceLabels.gke-cluster` | `additional.fields`  
`resource.data.resourceLabels.goog-terraform-provisioned` | `additional.fields`  
`resource.data.roles` | `target.user.attribute.roles.name`  
`resource.data.scheduling.automaticRestart` | `additional.fields`  
`resource.data.scheduling.onHostMaintenance` | `additional.fields`  
`resource.data.scheduling.preemptible` | `additional.fields`  
`resource.data.secretVersionsToStages.terraform-20260122172341570100000002` | `principal.resource.attribute.labels`  
`resource.data.securityPostureConfig.mode` | `security_result.detection_fields`  
`resource.data.securityPostureConfig.vulnerabilityMode` | `security_result.detection_fields`  
`resource.data.selfLink` | `principal.resource.attribute.labels`  
`resource.data.shareDeleteRetentionPolicy.file.*` | `additional.fields`  
`resource.data.shieldedInstanceConfig.enableIntegrityMonitoring` | `additional.fields`  
`resource.data.shieldedInstanceConfig.enableSecureBoot` | `additional.fields`  
`resource.data.shieldedInstanceConfig.enableVtpm` | `additional.fields`  
`resource.data.shieldedInstanceIntegrityPolicy.updateAutoLearnPolicy` | `additional.fields`  
`resource.data.sku.*` | `additional.fields`  
`resource.data.sourceRanges` | `security_result.about.ip`  
`resource.data.state.code` | `additional.fields`  
`resource.data.state.name` | `additional.fields`  
`resource.data.tags` | `additional.fields`  
`resource.data.tags.*` | `additional.fields`  
`resource.data.tags.Creator` | `target.user.email_addresses`,  
`target.user.userid`  
`resource.data.tags.Email` | `target.user.email_addresses`,  
`target.user.userid`  
`resource.data.tags.items` | `additional.fields`  
`resource.data.targetGroups.*` | `target.resource.attribute.labels`  
`resource.data.targetGroups.loadBalancerArns` | `target.resource.attribute.labels`  
`resource.data.targetTags` | `additional.fields`  
`resource.data.type` | `principal.resource.attribute.labels`  
`resource.data.user` | `target.user.email_addresses`,  
`target.user.userid`  
`resource.data.userPrincipalName` | `target.user.userid`  
`resource.data.versionId` | `principal.resource.attribute.labels`  
`resource.data.workloadIdentityConfig.workloadPool` | `additional.fields`  
`resource.data.dnsname` | `target.hostname`,  
`target.asset.hostname`  
`resource.id` | `principal.resource.product_object_id`,  
`additional.fields`  
`resource.name` | `principal.resource.name`,  
`additional.fields`  
`resource.region` | `principal.location.country_or_region`,  
`principal.location.state`,  
`additional.fields`  
`resource.regionId` | `principal.resource.attribute.cloud.availability_zone`,  
`principal.location.country_or_region`,  
`additional.fields`  
`resource.resourceApiName` | `target.resource.attribute.labels`  
`resource.resourceConfigJsonAvailable` | `additional.fields`  
`resource.resourceDetailsAvailable` | `additional.fields`  
`resource.resourceId` | `principal.resource.product_object_id`  
`resource.resourceName` | `principal.resource.name`  
`resource.resourceTags.*` | `principal.resource.attribute.labels`  
`resource.resourceTs` | `metadata.event_timestamp`  
`resource.resourceType` | `target.resource.resource_subtype`,  
`additional.fields`  
`resource.rrn` | `target.resource.attribute.labels`  
`resource.unifiedAssetId` | `principal.asset.asset_id`  
`resource.url` | `principal.url`  
`resourceCloudService` | `principal.resource.attribute.labels`  
`resourceConfigJsonAvailable` | `additional.fields`  
`resourceDetailsAvailable` | `additional.fields`  
`resourceId` | `principal.resource.product_object_id`  
`resourceName` | `principal.resource.name`  
`resourceRegion` | `principal.location.country_or_region`  
`resourceRegionId` | `principal.resource.attribute.cloud.availability_zone`  
`resourceType` | `target.resource.resource_subtype`  
`rrn` | `target.resource.name`  
`saveSearchId` | `security_result.detection_fields`  
`sender` | `metadata.description`  
`sentTs` | `metadata.event_timestamp`  
`serialNum` | `additional.fields`  
`service` | `observer.application`  
`severity` | `security_result.severity`,  
`security_result.severity_details`  
`shouldCollect` | `additional.fields`  
`source` | `principal.application`  
`source_type` | `metadata.product_event_type`  
`startupProcess` | `principal.process.parent_process.command_line`  
`status` | `security_result.detection_fields`  
`systemDefault` | `additional.fields`  
`tags` | `principal.resource.attribute.labels`  
`time` | `metadata.event_timestamp`  
`title` | `additional.fields`  
`type` | `principal.resource.resource_subtype`,  
`security_result.category_details`  
`unifiedAssetId` | `principal.asset.asset_id`  
`url` | `security_result.url_back_to_product`  
`user` | `principal.user.userid`  
`vulnerabilities.accountIDs` | `extensions.vulns.vulnerabilities.about.resource.attribute.labels`  
`vulnerabilities.clusters` | `extensions.vulns.vulnerabilities.about.resource.attribute.labels`  
`vulnerabilities.collections` | `extensions.vulns.vulnerabilities.about.resource.attribute.labels`  
`vulnerabilities.distribution` | `extensions.vulns.vulnerabilities.name`  
`vulnerabilities.imageID` | `extensions.vulns.vulnerabilities.about.file.sha256`  
`vulnerabilities.imageName` | `extensions.vulns.vulnerabilities.about.file.full_path`  
`vulnerabilities.namespaces` | `extensions.vulns.vulnerabilities.about.resource.attribute.labels`  
`vulnerabilities.newVulnerabilities.vulnerabilities.cve` | `extensions.vulns.vulnerabilities.cve_id`  
`vulnerabilities.newVulnerabilities.vulnerabilities.link` | `extensions.vulns.vulnerabilities.about.url`  
`vulnerabilities.newVulnerabilities.vulnerabilities.packages` | `target.resource.attribute.labels`  
`vulnerabilities.newVulnerabilities.vulnerabilities.packageVersion` | `target.resource.attribute.labels`  
`vulnerabilities.newVulnerabilities.vulnerabilities.severity` | `extensions.vulns.vulnerabilities.severity`,  
`extensions.vulns.vulnerabilities.severity_details`  
`vulnerabilities.newVulnerabilities.vulnerabilities.sourcePackage` | `target.resource.attribute.labels`  
`vulnerabilities.newVulnerabilities.vulnerabilities.status` | `extensions.vulns.vulnerabilities.description`  
  
## UDM mapping delta reference

On September 15, 2026, Google SecOps released a new version of the Palo Alto Prisma Cloud Alert payload parser, which includes significant changes to the mapping of Palo Alto Prisma Cloud Alert payload log fields to UDM fields.

### Log-field mapping delta

The following table lists the mapping delta for Palo Alto Prisma Cloud Alert payload log-to-UDM fields exposed prior to September 15, 2026 and subsequently (listed in the **Old mapping** and **Current mapping** columns respectively):

Log field | Old mapping | Current mapping | Reason for change  
---|---|---|---  
`_id` | `additional.fields` | `metadata.product_log_id` | Mapped to product log ID for distinct event identification.  
`account.cloudType` | `principal.cloud.environment` | `principal.resource.attribute.cloud.environment` | Realigned cloud environment context to resource attributes.  
`accountId` | `target.resource.id`,  
`target.resource.product_object_id` | `target.resource.product_object_id` | Standardized cloud account identifier targets.  
`accountId` | `target1.cloud.project.id` | `target.resource.product_object_id` | Removed deprecated `target1` entity mapping.  
`aggregatedAlerts.category` | `security_result.category_details` | `about.resource.attribute.labels` | Moved generic category attributes to `about` resource labels.  
`aggregatedAlerts.command` | `principal.process.command_line`,  
`security_result.detection_fields` | `about.process.command_line` | Consolidated process execution details under `about.process`.  
`aggregatedAlerts.complianceIssues.category` | `security_result.category_details` | `security_result.detection_fields` | Preserved compliance metadata in detection fields.  
`aggregatedAlerts.complianceIssues.description` | `security_result.description`,  
`security_result.detection_fields` | `security_result.detection_fields` | Streamlined description mapping to prevent redundant fields.  
`aggregatedAlerts.complianceIssues.severity` | `security_result.severity`,  
`severity_details`,  
`security_result.detection_fields` | `security_result.detection_fields` | Standardized compliance severity tracking in detection fields.  
`aggregatedAlerts.complianceIssues.title` | `security_result.action_details`,  
`security_result.detection_fields` | `security_result.detection_fields` | Consolidated title metadata into detection fields.  
`aggregatedAlerts.container` | `target.resource.name` | `about.resource.name` | Shifted container details from target to `about` context.  
`aggregatedAlerts.containerID` | `target.resource.product_object_id` | `about.resource.product_object_id` | Realigned container ID mapping to `about` resource attributes.  
`aggregatedAlerts.forensics` | `principal.url` | `about.url` | Updated forensic link target to `about.url`.  
`aggregatedAlerts.fqdn` | `principal.domain.name` | `about.domain.name` | Corrected domain context mapping.  
`aggregatedAlerts.host` | `principal.hostname` | `about.hostname` | Shifted host entity context to `about.hostname`.  
`aggregatedAlerts.message` | `security_result.description` | `about.resource.attribute.labels` | Moved raw message strings into label key-value pairs.  
`aggregatedAlerts.region` | `target.cloud.availability_zone` | `about.resource.attribute.cloud.availability_zone` | Updated cloud region attribute mapping.  
`aggregatedAlerts.rule` | `security_result.rule_name` | `about.resource.attribute.labels` | Moved aggregated rule references to resource labels.  
`aggregatedAlerts.startupProcess` | `principal.process.parent_process.command_line` | `about.resource.attribute.labels` | Reclassified startup process details to resource labels.  
`aggregatedAlerts.time` | `metadata.event_timestamp` | `about.resource.attribute.labels` | Retained raw alert timestamp in resource labels.  
`aggregatedAlerts.type` | `security_result.category_details` | `about.resource.attribute.labels` | Reclassified alert type into resource labels.  
`aggregatedAlerts.user` | `principal.user.userid` | `about.user.userid` | Realigned user entity reference to `about.user`.  
`alertTs` | `security_result.detection_fields` | `security_result.first_discovered_time` | Corrected detection timestamp target field.  
`audits.attackType` | `security_result.threat_name` | `security_result.threat_name`,  
`security_result.detection_fields` | Added secondary mapping to detection fields.  
`audits.command` | `principal.process.command_line` | `about.process.command_line` | Shifted process command-line target to `about`.  
`audits.effect` | `security_result.action_details` | `security_result.action_details`,  
`security_result.detection_fields` | Added secondary mapping to detection fields.  
`audits.msg` | `metadata.description` | `metadata.description`,  
`about.resource.attribute.labels` | Expanded audit message tracking to resource labels.  
`audits.os` | `principal.platform_version` | `about.platform_version` | Corrected operating system platform target.  
`audits.pid` | `principal.process.pid` | `about.process.pid` | Realigned process ID mapping to `about.process`.  
`audits.processPath` | `principal.process.file.full_path` | `about.process.file.full_path` | Realigned process executable path to `about.process`.  
`audits.ruleName` | `security_result.rule_name` | `security_result.rule_name`,  
`security_result.detection_fields` | Preserved rule name across security result and detection fields.  
`audits.severity` | `security_result.severity` | `security_result.severity`,  
`security_result.detection_fields` | Preserved audit severity across security result and detection fields.  
`audits.type` | `metadata.product_event_type` | `metadata.product_event_type`,  
`about.resource.attribute.labels` | Added event type to resource labels for enhanced filtering.  
`audits.user` | `principal.user.userid` | `about.user.userid` | Realigned audit user identifier to `about.user`.  
`cloudType` | `principal.cloud.environment` | `principal.resource.attribute.cloud.environment` | Updated root cloud environment target.  
`complianceMetadata.requirementId` | `security_result.rule_id` | `security_result.detection_fields` | Moved compliance requirement ID to detection fields.  
`complianceMetadata.requirementName` | `security_result.summary` | `security_result.detection_fields` | Moved compliance requirement name to detection fields.  
`complianceMetadata.standardName` | `security_result.rule_name` | `security_result.detection_fields` | Moved compliance standard name to detection fields.  
`containerName` | `principal.application`,  
`principal.resource.name` | `principal.resource.name` | Removed ambiguous application entity mapping.  
`imageID` | `principal.resource.attribute.labels` | `principal.process.file.sha256` | Mapped container image hash directly to process SHA256.  
`imageName` | `principal.resource.attribute.labels` | `principal.process.file.full_path` | Mapped container image name to process file path.  
`policy.complianceMetadata.requirementId` | `security_result.rule_id` | `security_result.detection_fields` | Moved policy compliance requirement ID to detection fields.  
`policy.complianceMetadata.requirementName` | `security_result.summary` | `security_result.detection_fields` | Moved policy compliance requirement name to detection fields.  
`policy.complianceMetadata.standardName` | `security_result.rule_name` | `security_result.detection_fields` | Moved policy compliance standard name to detection fields.  
`provider` | `target.resource.attribute.labels` | `target.resource.attribute.cloud.environment` | Standardized cloud provider environment context.  
`resource.account` | `target.resource.product_object_id` | `additional.fields` | Moved generic account string to additional fields.  
`resource.accountId` | `target.resource.id`,  
`target.resource.product_object_id` | `target.resource.product_object_id` | Standardized resource account ID mapping.  
`resource.accountId` | `target1.cloud.project.id` | `target.resource.product_object_id` | Removed legacy `target1` entity reference.  
`resource.cloudAccountGroups` | `principal.resource.attribute.labels` | `target.user.group_identifiers` | Corrected account group mapping to user group identifiers.  
`resource.cloudType` | `principal.cloud.environment` | `principal.resource.attribute.cloud.environment` | Standardized resource cloud environment attributes.  
`resource.data.isAttached` | `security_result.detection_fields` | `additional.fields` | Shifted resource state flags to additional fields.  
`resource.data.isDefaultVersion` | `security_result.detection_fields` | `additional.fields` | Shifted version flags to additional fields.  
`resource.data.isPermissionBoundarySet` | `security_result.detection_fields` | `additional.fields` | Shifted permission flags to additional fields.  
`resource.resourceApiName` | `principal.resource.attribute.labels` | `target.resource.attribute.labels` | Realigned resource API labels to target resource.  
`resource.resourceId` | `principal.resource.attribute.labels` | `principal.resource.product_object_id` | Promoted resource ID to product object ID.  
`resource.resourceName` | `principal.resource.attribute.labels` | `principal.resource.name` | Promoted resource name to native UDM resource name.  
`resource.resourceTs` | `principal.resource.attribute.labels` | `metadata.event_timestamp` | Corrected event timestamp source extraction field.  
`resource.rrn` | `principal.resource.attribute.labels` | `target.resource.attribute.labels` | Realigned resource RRN to target labels.  
`resourceRegionId` | `principal.cloud.availability_zone` | `principal.resource.attribute.cloud.availability_zone` | Realigned cloud region ID to resource attributes.  
`resourceType` | `principal.resource.resource_subtype` | `target.resource.resource_subtype` | Standardized target resource subtype.  
`type` | `principal.resource.type` | `principal.resource.resource_subtype` | Mapped type string to resource subtype.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-prisma-ca-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
