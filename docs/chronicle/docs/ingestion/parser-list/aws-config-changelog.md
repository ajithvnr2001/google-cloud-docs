---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-config-changelog/
title: Change log for AWS_CONFIG \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:02.413133+00:00
---

# Change log for AWS_CONFIG  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-config-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_CONFIG

Date | Changes  
---|---  
2025-09-26 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped raw log fields `configItem.configuration.ipPermissions.ipv4Ranges.cidrIp`, `configItem.configuration.ipPermissions.ipRanges`, `configItem.configuration.ipPermissionsEgress.ipv4Ranges.cidrIp`, and `configItem.configuration.ipPermissionsEgress.ipRanges` to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped raw log fields `configItem.configuration.ipPermissions.ipv4Ranges.cidrIp`, `configItem.configuration.ipPermissions.ipRanges`, `configItem.configuration.ipPermissionsEgress.ipv4Ranges.cidrIp`, and `configItem.configuration.ipPermissionsEgress.ipRanges` to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `configItem.configuration.stackId`, `configItem.configuration.StandardsArn`, `configItem.configuration.VPCId`, `configItem.configuration.ResolverRuleId`, `configItem.configuration.ResolverRuleAssociationId`, `configItem.configuration.computePlatform`, `configItem.configuration.minimumHealthyHosts.type`, `configItem.configuration.minimumHealthyHosts.value`, `configItem.configuration.trafficRoutingConfig.type`, `configItem.configuration.trafficRoutingConfig.timeBasedCanary.canaryPercentage`, `configItem.configuration.trafficRoutingConfig.timeBasedCanary.canaryInterval`, `configItem.configuration.Id`, `configItem.configuration.ReplicateTo`, `configItem.configuration.GrowthType`, `configItem.configuration.Description`, `configItem.configuration.DeploymentDurationInMinutes`, `configItem.configuration.GrowthFactor`, `configItem.configuration.FinalBakeTimeInMinutes`, `configItem.configuration.Name`, `configItem.configuration.Features`, `configItem.configuration.Enable`, `configItem.configuration.FindingPublishingFrequency`, `configItem.configuration.DataSources.S3Logs.Enable`, `configItem.configuration.DataSources.Kubernetes.AuditLogs.Enable`, `configItem.configuration.entries`, `configItem.configuration.associations`, `configItem.configuration.routes`, `configItem.configuration.EventBusName`, `configItem.configuration.EventPattern.source`, `configItem.configuration.EventPattern.detail-type`, `configItem.configuration.EventPattern.detail.eventSource`, `configItem.configuration.EventPattern.detail.managementEvent`, `configItem.configuration.cidrBlockAssociationSet`, `configItem.configuration.AccountId`, `configItem.configuration.State`, `configItem.configuration.DomainName`, `configItem.configuration.ServiceType`, `configItem.configuration.TlsConfig.SecurityPolicy`, `configItem.configuration.AuthenticationType`, `configItem.configuration.RecordingGroup.AllSupported`, `configItem.configuration.RecordingGroup.IncludeGlobalResourceTypes`, `configItem.configuration.RecordingGroup.RecordingStrategy.UseOnly`, `configItem.configuration.accountState.state.status`, `configItem.configuration.accountState.resourceState.ec2.status`, `configItem.configuration.accountState.resourceState.ecr.status`, `configItem.configuration.accountState.resourceState.lambda.status`, `configItem.configuration.accountState.resourceState.lambdaCode.status`, `configItem.configuration.accountState.resourceState.codeRepository.status`, `configItem.configuration.stackName`, `configItem.configuration.stackStatus`, `configItem.configuration.driftInformation.stackDriftStatus`, `configItem.configuration.deploymentConfigId`, `configItem.configuration.lastUpdatedTime`, `configItem.configuration.parameters`, `configItem.configuration.outputs`, `configItem.supplementaryConfiguration.StackResourceSummaries`, `configItem.supplementaryConfiguration.unsupportedResources`, `configItem.configurationItemVersion`, `configItem.configuration.newInstancesProtectedFromScaleIn`, `configItem.configuration.serviceLinkedRoleARN`, `configItem.configuration.createdTime`, `configItem.configuration.vpczoneIdentifier`, `configItem.configuration.maxSize`, `configItem.configuration.minSize`, `configItem.configuration.desiredCapacity`, `configItem.configuration.defaultCooldown`, `configItem.configuration.ipPermissions`, `configItem.configuration.ipPermissionsEgress`, `configItem.supplementaryConfiguration.EnableTerminationProtection`, `configItem.configuration.DisabledStandardsControls.StandardsControlArn`, `configItem.configuration.disableRollback`, `configItem.configuration.WorkGroupConfiguration.EnforceWorkGroupConfiguration`, `configItem.configuration.WorkGroupConfiguration.EngineVersion.SelectedEngineVersion`, `configItem.configuration.WorkGroupConfiguration.EngineVersion.EffectiveEngineVersion`, `configItem.configuration.WorkGroupConfiguration.PublishCloudWatchMetricsEnabled`, `configItem.configuration.WorkGroupConfiguration.RequesterPaysEnabled`, `configItem.configuration.isDefault`, `configItem.configuration.networkAclId` and `configItem.configuration.DisabledStandardsControls.Reason` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-04 |  Enhancement:  
\- Modified conditional check to process logs only when message contains `Records` AND the fileVersion field is empty.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `configItem.resourceCreationTime` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `configItem.configurationItemCaptureTime` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `configuration.serviceLinkedRoleARN`, `configuration.createdTime`, `configuration.vpczoneIdentifier`, `configuration.maxSize`, `configuration.minSize`, `configuration.desiredCapacity`, `configuration.defaultCooldown`, `configurationItemVersion` and `configuration.newInstancesProtectedFromScaleIn` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.metadata.id: Newly mapped `configSnapshotId` raw log field to event.idm.read_only_udm.metadata.id.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `fileVersion` raw log field to event.idm.read_only_udm.metadata.product_version.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `configuration.availabilityZones` raw log field to event.idm.read_only_udm.principal.location.country_or_region.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `relationships.name`, `relationships.resourceType` and `relationships.resourceId` raw log fields to event.idm.read_only_udm.principal.resource.attribute.labels.  
\- event.idm.read_only_udm.target.location.name: Newly mapped `availabilityZone` raw log field to event.idm.read_only_udm.target.location.name.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `configuration.autoScalingGroupName`, `enabledMetric.granularity`, `enabledMetric.metric`, `configuration.healthCheckGracePeriod`, `configuration.healthCheckType`, `configuration.keyspaceName`, `configuration.launchTemplate`, `configuration.terminationPolicies`, `awsAccountId`, `configurationStateId`, `configuration.autoScalingGroupARN`, `launchTemplate.launchTemplateId`, `launchTemplateName`, `launchTemplate.version` and `configurationStateMd5Hash` raw log fields to event.idm.read_only_udm.target.resource.attribute.labels.   
2025-07-01 |  Enhancement:  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `awsRegion` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `eventCategory` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.id`: Newly mapped `eventID` raw log field with `event.idm.read_only_udm.metadata.id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.name`: Newly mapped `eventSource` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `eventType`, `lookupAttribute.attributeKey`, `lookupAttribute.attributeValue`, `userIdentity.invokedBy`, `requestParameters.encryptionContext.aws:cloudtrail:arn`, `digestPublicKeyFingerprint`, `logFile.hashAlgorithm`, `logFile.hashValue`, `logFile.s3Bucket`, `logFile.s3Object`, `tlsDetails.clientProvidedHostHeader` and `requestParameters.encryptionContext.aws:s3:arn` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `eventVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `managementEvent`, `readOnly`, `requestParameters.maxResults`, `userIdentity.sessionContext.attributes.mfaAuthenticated`, `digestS3Object`, `digestSignatureAlgorithm`, `digestS3Bucket` and `userIdentity.sessionContext.sessionIssuer.type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `recipientAccountId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `requestID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.last_discovered_time`: Newly mapped `requestParameters.endTime` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `requestParameters.startTime` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly added a conditional mapping based on the `sourceIPAddress` raw log field. A grok pattern is used to identify IP addresses. When an IP is found, it is mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`. Otherwise, the existing mapping to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` is used.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tlsDetails.cipherSuite` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tlsDetails.tlsVersion` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `userIdentity.accessKeyId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `userIdentity.accountId` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `userIdentity.arn` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `userIdentity.principalId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.creation_time`: Newly mapped `userIdentity.sessionContext.attributes.creationDate` raw log field with `event.idm.read_only_udm.principal.user.attribute.creation_time` UDM field.  
\- `event.idm.read_only_udm.intermediary.cloud.project.id`: Newly mapped `userIdentity.sessionContext.sessionIssuer.accountId` raw log field with `event.idm.read_only_udm.intermediary.cloud.project.id` UDM field.  
\- `event.idm.read_only_udm.intermediary.resource.name`: Newly mapped `userIdentity.sessionContext.sessionIssuer.arn` raw log field with `event.idm.read_only_udm.intermediary.resource.name` UDM field.  
\- `event.idm.read_only_udm.intermediary.resource.product_object_id`: Newly mapped `userIdentity.sessionContext.sessionIssuer.principalId` raw log field with `event.idm.read_only_udm.intermediary.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `userIdentity.sessionContext.sessionIssuer.userName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.type`: Newly mapped `userIdentity.type` raw log field with `event.idm.read_only_udm.principal.cloud.project.type` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `resource.ARN` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `resource.accountId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped `resource.type` raw log field with `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.id`: Newly mapped `requestParameters.keyId` raw log field with `event.idm.read_only_udm.security_result.about.resource.id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.labels`: Newly mapped `requestParameters.keySpec` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `awsAccountId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `digestEndTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `digestStartTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-04-14 |  Enhancement:  
\- Added mappings for numerous fields within `configurationItem.configuration.AWS:Application.Content` to the `event.idm.read_only_udm.additional.fields`.  
\- This includes adding a `for` loop for each of the following keys:  
\- `rpm-libs`  
\- `libcollection`  
\- `ethtool`  
\- `python3-certbot`  
\- `libmnl`  
\- `apr-util-openssl`  
\- `perl-overloading`  
\- `libselinux-utils`  
\- `python-josepy-doc`  
\- `libibverbs`  
\- `fstrm`  
\- `libseccomp`  
\- `python3-pyyaml`  
\- `libattr`  
\- `telnet`  
\- `quota`  
\- `efivar`  
\- `python3-libdnf`  
\- `glibc-all-langpacks`  
\- `keyutils-libs`  
\- `libgcc`  
\- `mod_lua`  
\- `fonts-srpm-macros`  
\- `libkcapi-hmaccalc`  
\- `python3-daemon`  
\- `perl-Encode`  
\- `selinux-policy`  
\- `fonts-filesystem`  
\- `python3-pyrsistent`  
\- `bind-license`  
\- `perl-IPC-Open3`  
\- `pcre2-syntax`  
\- `python-chevron`  
\- `perl-Getopt-Long`  
\- `at`  
\- `libunistring`  
\- `python3-docutils`  
\- `newrelic-infra`  
\- `python3-requests`  
\- `findutils`  
\- `bc`  
\- `glibc-common`  
\- `grub2-tools`  
\- `ntsysv`  
\- `gmp`  
\- `python-srpm-macros`  
\- `python3-attrs`  
\- `sed`  
\- `python3-acme`  
\- `python3-lockfile`  
\- `libref_array`  
\- `vim-minimal`  
\- `libcom_err`  
\- `c-ares`  
\- `perl-Pod-Escapes`  
\- `python3-chardet`  
\- `kbd-misc`  
\- `pkgconf-m4`  
\- `httpd-filesystem`  
\- `systemd`  
\- `gssproxy`  
\- `libpsl`  
\- `kernel`  
\- `words`  
\- `perl-Carp`  
\- `dnf-utils`  
\- `libassuan`  
\- `libxcrypt`  
\- `rsync`  
\- `chrony`  
\- `bash-completion`  
\- `popt`  
\- `libsepol`  
\- `gnupg2-minimal`  
\- `libpcap`  
\- `acl`  
\- `python3-distro`  
\- `python3-pyparsing`  
\- `util-linux`  
\- `perl-Term-Cap`  
\- `efivar-libs`  
\- `perl-Text-Tabs+Wrap`  
\- `pigz`  
\- `shadow-utils`  
\- `util-linux-core`  
\- `pam`  
\- `ed`  
\- `package-notes-srpm-macros`  
\- `info`  
\- `which`  
\- `libpkgconf`  
\- `sssd-common`  
\- `systemd-resolved`  
\- `containerd`  
\- `httpd-tools`  
\- `cryptsetup`  
\- `grub2-tools-minimal`  
\- `rust-srpm-macros`  
\- `perl-Class-Struct`  
\- `python3-netifaces`  
\- `xz-libs`  
\- `psmisc`  
\- `gperftools-libs`  
\- `perl-Exporter`  
\- `yum`  
\- `libsss_certmap`  
\- `awscli-2`  
\- `fluent-bit`  
\- `libtirpc`  
\- `nss-sysinit`  
\- `krb5-libs`  
\- `python3-libselinux`  
\- `rpcbind`  
\- `libkcapi`  
\- `libblkid`  
\- `python3-jinja2`  
\- `mod_http2`  
\- `elfutils-default-yama-scope`  
\- `filesystem`  
\- `cloud-utils-growpart`  
\- `binutils`  
\- `setup`  
\- `libmetalink`  
\- `openssl-libs`  
\- `pciutils`  
\- `perl-vars`  
\- `python3-certbot-nginx`  
\- `amazon-linux-repo-s3`  
\- `libsolv`  
\- `p11-kit`  
\- `openldap`  
\- `perl-MIME-Base64`  
\- `hwdata`  
\- `vim-enhanced`  
\- `libtdb`  
\- `bzip2`  
\- `dbus-libs`  
\- `libsss_idmap`  
\- `python3-pyOpenSSL`  
\- `sqlite-libs`  
\- `nss-softokn`  
\- `httpd-core`  
\- `perl-subs`  
\- `update-motd`  
\- `dnf`  
\- `gawk`  
\- `perl-Symbol`  
\- `cryptsetup-libs`  
\- `hunspell-en-GB`  
\- `httpd`  
\- `libgpg-error`  
\- `python3-jsonpatch`  
\- `tcsh`  
\- `inih`  
\- `psacct`  
\- `dnf-plugin-support-info`  
\- `rpm-sign-libs`  
\- `nginx-core`  
\- `python3-ruamel-yaml-clib`  
\- `glibc-gconv-extra`  
\- `groff-base`  
\- `amazon-linux-sb-keys`  
\- `crontabs`  
\- `libffi`  
\- `jq`  
\- `diffutils`  
\- `python3-prompt-toolkit`  
\- `dracut-config-ec2`  
\- `grubby`  
\- `libpath_utils`  
\- `libreport-filesystem`  
\- `file`  
\- `systemd-libs`  
\- `boost-thread`  
\- `net-tools`  
\- `libevent`  
\- `perl-Getopt-Std`  
\- `logrotate`  
\- `xxd`  
\- `libpq`  
\- `perl-interpreter`  
\- `gzip`  
\- `libcap`  
\- `ec2-instance-connect`  
\- `libgomp`  
\- `python3-urllib3`  
\- `inspectorssmplugin`  
\- `libtevent`  
\- `iptables-nft`  
\- `iproute`  
\- `elfutils-debuginfod-client`  
\- `libss`  
\- `libsmartcols`  
\- `screen`  
\- `libcomps`  
\- `python3-libcomps`  
\- `sssd-kcm`  
\- `kernel-livepatch-repo-s3`  
\- `libconfig`  
\- `mpfr`  
\- `vim-data`  
\- `sssd-client`  
\- `libacl`  
\- `nginx`  
\- `python3-ply`  
\- `perl-constant`  
\- `amazon-rpm-config`  
\- `perl-Text-ParseWords`  
\- `less`  
\- `lsof`  
\- `python3-pytz`  
\- `perl-Term-ANSIColor`  
\- `libbasicobjects`  
\- `pkgconf-pkg-config`  
\- `python3-dnf-plugins-core`  
\- `xxhash-libs`  
\- `libuv`  
\- `jansson`  
\- `python3-configargparse`  
\- `e2fsprogs`  
\- `perl-SelectSaver`  
\- `libverto-libev`  
\- `python3-pysocks`  
\- `perl-POSIX`  
\- `attr`  
\- `libtalloc`  
\- `nfs-utils`  
\- `libgcrypt`  
\- `lm_sensors-libs`  
\- `hunspell-filesystem`  
\- `perl-libs`  
\- `libfdisk`  
\- `perl-Storable`  
\- `kbd`  
\- `libcgroup`  
\- `boost-filesystem`  
\- `python3-libs`  
\- `libstdc++`  
\- `rpm`  
\- `cyrus-sasl-lib`  
\- `perl-File-stat`  
\- `dosfstools`  
\- `ocaml-srpm-macros`  
\- `openssh-server`  
\- `python3-pyserial`  
\- `libidn2`  
\- `libini_config`  
\- `perl-overload`  
\- `chkconfig`  
\- `rng-tools`  
\- `python3-ruamel-yaml`  
\- `libstoragemgmt`  
\- `python3-colorama`  
\- `hostname`  
\- `zram-generator`  
\- `man-pages`  
\- `gettext`  
\- `systemd-networkd`  
\- `openssh-clients`  
\- `dnf-data`  
\- `systemd-udev`  
\- `amazon-ssm-agent`  
\- `apr`  
\- `dbus-broker`  
\- `libuuid`  
\- `protobuf-c`  
\- `passwd`  
\- `efi-srpm-macros`  
\- `libdnf`  
\- `hunspell`  
\- `libuser`  
\- `alternatives`  
\- `perl-Errno`  
\- `zram-generator-defaults`  
\- `nss-util`  
\- `systemd-pam`  
\- `libmodulemd`  
\- `dwz`  
\- `lmdb-libs`  
\- `ghc-srpm-macros`  
\- `python3-hawkey`  
\- `hunspell-en`  
\- `perl-Fcntl`  
\- `mod_ssl`  
\- `audit`  
\- `python3-rpm`  
\- `libdhash`  
\- `python3-jmespath`  
\- `python3-cryptography`  
\- `perl-Scalar-List-Utils`  
\- `man-db`  
\- `sudo`  
\- `rpm-plugin-systemd-inhibit`  
\- `basesystem`  
\- `perl-mro`  
\- `rootfiles`  
\- `slang`  
\- `strace`  
\- `libmount`  
\- `python3-setuptools`  
\- `libnfsidmap`  
\- `cpio`  
\- `vim-common`  
\- `selinux-policy-targeted`  
\- `nginx-mimetypes`  
\- `libcurl-minimal`  
\- `crypto-policies`  
\- `libzstd`  
\- `kmod`  
\- `nano`  
\- `python3-dnf`  
\- `ncurses`  
\- `python3-libstoragemgmt`  
\- `libcap-ng`  
\- `libselinux`  
\- `go-srpm-macros`  
\- `dyninst`  
\- `e2fsprogs-libs`  
\- `rpm-plugin-selinux`  
\- `librepo`  
\- `python3-policycoreutils`  
\- `perl-Pod-Usage`  
\- `libnfnetlink`  
\- `keyutils`  
\- `oniguruma`  
\- `libutempter`  
\- `libverto`  
\- `libunwind`  
\- `cloud-init-cfg-ec2`  
\- `python3-pyrfc3339`  
\- `nspr`  
\- `iptables-libs`  
\- `perl-PathTools`  
\- `libpipeline`  
\- `efi-filesystem`  
\- `glibc`  
\- `libargon2`  
\- `libsss_nss_idmap`  
\- `perl-Pod-Simple`  
\- `python3-jsonschema`  
\- `aws-cfn-bootstrap`  
\- `xfsdump`  
\- `boost-system`  
\- `tcpdump`  
\- `docker`  
\- `sysstat`  
\- `cracklib-dicts`  
\- `coreutils`  
\- `curl-minimal`  
\- `perl-Socket`  
\- `expat`  
\- `dracut`  
\- `system-release`  
\- `fuse-libs`  
\- `python3-pycparser`  
\- `python3-pip-wheel`  
\- `readline`  
\- `libaio`  
\- `grep`  
\- `newt`  
\- `libsemanage`  
\- `glib2`  
\- `libxml2`  
\- `perl-HTTP-Tiny`  
\- `perl-parent`  
\- `grub2-pc-modules`  
\- `openssh`  
\- `traceroute`  
\- `xfsprogs`  
\- `libnl3`  
\- `bind-libs`  
\- `json-c`  
\- `libev`  
\- `pcre2`  
\- `cloud-init`  
\- `pkgconf`  
\- `generic-logos-httpd`  
\- `iputils`  
\- `libdb`  
\- `python3-jsonpointer`  
\- `tzdata`  
\- `cyrus-sasl-plain`  
\- `dnf-plugin-release-notification`  
\- `libedit`  
\- `sysctl-defaults`  
\- `zlib`  
\- `libnftnl`  
\- `amazon-chrony-config`  
\- `python3-setuptools-wheel`  
\- `libmaxminddb`  
\- `libnetfilter_conntrack`  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `configurationItem.supplementaryConfiguration.instanceStatus` , `configurationItem.configurationStateId` , `configurationItem.ARN` and `configurationItem.configuration.AWS:Network.Content` to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `configurationItem.configurationItemVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `messageType` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.   
2024-06-09 |  Enhancement:  
\- Added `on_error` to `configItem.configuration.configRuleList` fields before mapping it to UDM.   
2024-02-22 |  Enhancement:  
\- Mapped `configurationItem.relationships[n].resourceId`, `configurationItem.relationships[n].resourceType` and `configurationItem.relationships[n].name` to `additional.fields`.   
2022-05-27 |  Enhancement - Modified the value stored in `metadata.product_name` to `AWS Config`.   
2022-03-30 |  Enhancement-Corrected mapping for relationship.resourceId to parse for all log types and improve parsing percentage.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
