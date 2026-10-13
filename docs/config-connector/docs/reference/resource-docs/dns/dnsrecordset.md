---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/dns/dnsrecordset/
title: DNSRecordSet \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:06.968307+00:00
---

# DNSRecordSet  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/dns/dnsrecordset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DNSRecordSet

**Property** | **Value**  
---|---  
Google Cloud Service Name | Cloud DNS  
Google Cloud Service Documentation | [/dns/docs/](https://docs.cloud.google.com/dns/docs)  
Google Cloud REST Resource Name | v1beta2.resourceRecordSets  
Google Cloud REST Resource Documentation | [/dns/docs/reference/v1beta2/resourceRecordSets](https://docs.cloud.google.com/dns/docs/reference/v1beta2/resourceRecordSets)  
Config Connector Resource Short Names | dnsrecordset  
gcpdnsrecordset  
gcpdnsrecordsets  
Config Connector Service Name | dns.googleapis.com  
Config Connector Resource Fully Qualified Name | dnsrecordsets.dns.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    managedZoneRef:
      external: string
      name: string
      namespace: string
    name: string
    routingPolicy:
      enableGeoFencing: boolean
      geo:
      - healthCheckedTargets:
          externalEndpoints:
          - string
          internalLoadBalancers:
          - ipAddressRef:
              external: string
              name: string
              namespace: string
            ipProtocol: string
            loadBalancerType: string
            networkRef:
              external: string
              name: string
              namespace: string
            port: string
            projectRef:
              external: string
              name: string
              namespace: string
            regionRef:
              external: string
              name: string
              namespace: string
        location: string
        rrdatasRefs:
        - external: string
          kind: string
          name: string
          namespace: string
      healthCheckRef:
        external: string
        name: string
        namespace: string
      primaryBackup:
        backupGeo:
        - healthCheckedTargets:
            externalEndpoints:
            - string
            internalLoadBalancers:
            - ipAddressRef:
                external: string
                name: string
                namespace: string
              ipProtocol: string
              loadBalancerType: string
              networkRef:
                external: string
                name: string
                namespace: string
              port: string
              projectRef:
                external: string
                name: string
                namespace: string
              regionRef:
                external: string
                name: string
                namespace: string
          location: string
          rrdatasRefs:
          - external: string
            kind: string
            name: string
            namespace: string
        enableGeoFencingForBackups: boolean
        primary:
          externalEndpoints:
          - string
          internalLoadBalancers:
          - ipAddressRef:
              external: string
              name: string
              namespace: string
            ipProtocol: string
            loadBalancerType: string
            networkRef:
              external: string
              name: string
              namespace: string
            port: string
            projectRef:
              external: string
              name: string
              namespace: string
            regionRef:
              external: string
              name: string
              namespace: string
        trickleRatio: float
      wrr:
      - healthCheckedTargets:
          externalEndpoints:
          - string
          internalLoadBalancers:
          - ipAddressRef:
              external: string
              name: string
              namespace: string
            ipProtocol: string
            loadBalancerType: string
            networkRef:
              external: string
              name: string
              namespace: string
            port: string
            projectRef:
              external: string
              name: string
              namespace: string
            regionRef:
              external: string
              name: string
              namespace: string
        rrdatasRefs:
        - external: string
          kind: string
          name: string
          namespace: string
        weight: float
    rrdatas:
    - string
    rrdatasRefs:
    - external: string
      kind: string
      name: string
      namespace: string
    ttl: integer
    type: string
    

Fields  
---  
`managedZoneRef` _Required_ |  `object` DNSManagedZoneRef is a reference to a DNSManagedZone.  
`managedZoneRef.external` _Optional_ |  `string` A reference to an externally managed DNSManagedZone resource. Should be in the format "projects/{{projectID}}/managedZones/{{zone_number}}".  
`managedZoneRef.name` _Optional_ |  `string` The name of a DNSManagedZone resource.  
`managedZoneRef.namespace` _Optional_ |  `string` The namespace of a DNSManagedZone resource.  
`name` _Required_ |  `string` Immutable. The DNS name this record set will apply to.  
`routingPolicy` _Optional_ |  `object` The configuration for steering traffic based on query. You can specify either Weighted Round Robin(WRR) type or Geolocation(GEO) type.  
`routingPolicy.enableGeoFencing` _Optional_ |  `boolean` Specifies whether to enable fencing for geo queries.  
`routingPolicy.geo` _Optional_ |  `list (object)` The configuration for Geo location based routing policy.  
`routingPolicy.geo[]` _Optional_ |  `object`  
`routingPolicy.geo[].healthCheckedTargets` _Optional_ |  `object` For A and AAAA types only. The list of targets to be health checked. These can be specified along with `rrdatas` within this item.  
`routingPolicy.geo[].healthCheckedTargets.externalEndpoints` _Optional_ |  `list (string)` The Internet IP addresses to be health checked.  
`routingPolicy.geo[].healthCheckedTargets.externalEndpoints[]` _Optional_ |  `string`  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers` _Optional_ |  `list (object)` The list of internal load balancers to health check.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[]` _Optional_ |  `object`  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef` _Required*_ |  `object` ComputeAddressRef is a reference to a Google Cloud ComputeAddress.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.external` _Optional_ |  `string` A reference to an externally managed ComputeAddress resource. Should be in the format "projects/{{projectID}}/global/addresses/{{addressID}}" or "projects/{{projectID}}/regions/{{region}}/addresses/{{addressID}}".  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.name` _Optional_ |  `string` The name of a ComputeAddress resource.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.namespace` _Optional_ |  `string` The namespace of a ComputeAddress resource.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].ipProtocol` _Required*_ |  `string` The configured IP protocol of the load balancer. This value is case-sensitive. Possible values: ["tcp", "udp"].  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].loadBalancerType` _Required*_ |  `string` The type of load balancer. This value is case-sensitive. Possible values: ["regionalL4ilb", "regionalL7ilb", "globalL7ilb"].  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].networkRef` _Required*_ |  `object` ComputeNetworkRef is a reference to a Google Cloud ComputeNetwork.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].networkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeNetwork resource. Should be in the format "projects/{{projectID}}/global/networks/{{networkID}}".  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].networkRef.name` _Optional_ |  `string` The name of a ComputeNetwork resource.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].networkRef.namespace` _Optional_ |  `string` The namespace of a ComputeNetwork resource.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].port` _Required*_ |  `string` The configured port of the load balancer.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].projectRef` _Required*_ |  `object` ProjectRef is a reference to a Google Cloud Project.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].regionRef` _Optional_ |  `object`  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].regionRef.external` _Optional_ |  `string` The compute region name, when not managed by Config Connector.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].regionRef.name` _Optional_ |  `string` Name of a ComputeRegion object.  
`routingPolicy.geo[].healthCheckedTargets.internalLoadBalancers[].regionRef.namespace` _Optional_ |  `string` Namespace of a ComputeRegion object  
`routingPolicy.geo[].location` _Required*_ |  `string` The location name defined in Google Cloud.  
`routingPolicy.geo[].rrdatasRefs` _Optional_ |  `list (object)`  
`routingPolicy.geo[].rrdatasRefs[]` _Optional_ |  `object`  
`routingPolicy.geo[].rrdatasRefs[].external` _Optional_ |  `string` Allowed value: The `address` field of a `ComputeAddress` resource.  
`routingPolicy.geo[].rrdatasRefs[].kind` _Optional_ |  `string` Kind of the referent. Allowed values: ComputeAddress  
`routingPolicy.geo[].rrdatasRefs[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`routingPolicy.geo[].rrdatasRefs[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`routingPolicy.healthCheckRef` _Optional_ |  `object`  
`routingPolicy.healthCheckRef.external` _Optional_ |  `string` The compute health check name, when not managed by Config Connector.  
`routingPolicy.healthCheckRef.name` _Optional_ |  `string` Name of a ComputeHealthCheck object.  
`routingPolicy.healthCheckRef.namespace` _Optional_ |  `string` Namespace of a ComputeHealthCheck object  
`routingPolicy.primaryBackup` _Optional_ |  `object` The configuration for a primary-backup policy with global to regional failover. Queries are responded to with the global primary targets, but if none of the primary targets are healthy, then we fallback to a regional failover policy.  
`routingPolicy.primaryBackup.backupGeo` _Required*_ |  `list (object)` The backup geo targets, which provide a regional failover policy for the otherwise global primary targets.  
`routingPolicy.primaryBackup.backupGeo[]` _Required*_ |  `object`  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets` _Optional_ |  `object` For A and AAAA types only. The list of targets to be health checked. These can be specified along with `rrdatas` within this item.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.externalEndpoints` _Optional_ |  `list (string)` The Internet IP addresses to be health checked.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.externalEndpoints[]` _Optional_ |  `string`  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers` _Optional_ |  `list (object)` The list of internal load balancers to health check.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[]` _Optional_ |  `object`  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef` _Required*_ |  `object` ComputeAddressRef is a reference to a Google Cloud ComputeAddress.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.external` _Optional_ |  `string` A reference to an externally managed ComputeAddress resource. Should be in the format "projects/{{projectID}}/global/addresses/{{addressID}}" or "projects/{{projectID}}/regions/{{region}}/addresses/{{addressID}}".  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.name` _Optional_ |  `string` The name of a ComputeAddress resource.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.namespace` _Optional_ |  `string` The namespace of a ComputeAddress resource.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].ipProtocol` _Required*_ |  `string` The configured IP protocol of the load balancer. This value is case-sensitive. Possible values: ["tcp", "udp"].  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].loadBalancerType` _Required*_ |  `string` The type of load balancer. This value is case-sensitive. Possible values: ["regionalL4ilb", "regionalL7ilb", "globalL7ilb"].  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].networkRef` _Required*_ |  `object` ComputeNetworkRef is a reference to a Google Cloud ComputeNetwork.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].networkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeNetwork resource. Should be in the format "projects/{{projectID}}/global/networks/{{networkID}}".  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].networkRef.name` _Optional_ |  `string` The name of a ComputeNetwork resource.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].networkRef.namespace` _Optional_ |  `string` The namespace of a ComputeNetwork resource.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].port` _Required*_ |  `string` The configured port of the load balancer.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].projectRef` _Required*_ |  `object` ProjectRef is a reference to a Google Cloud Project.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].regionRef` _Optional_ |  `object`  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].regionRef.external` _Optional_ |  `string` The compute region name, when not managed by Config Connector.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].regionRef.name` _Optional_ |  `string` Name of a ComputeRegion object.  
`routingPolicy.primaryBackup.backupGeo[].healthCheckedTargets.internalLoadBalancers[].regionRef.namespace` _Optional_ |  `string` Namespace of a ComputeRegion object  
`routingPolicy.primaryBackup.backupGeo[].location` _Required*_ |  `string` The location name defined in Google Cloud.  
`routingPolicy.primaryBackup.backupGeo[].rrdatasRefs` _Optional_ |  `list (object)`  
`routingPolicy.primaryBackup.backupGeo[].rrdatasRefs[]` _Optional_ |  `object`  
`routingPolicy.primaryBackup.backupGeo[].rrdatasRefs[].external` _Optional_ |  `string` Allowed value: The `address` field of a `ComputeAddress` resource.  
`routingPolicy.primaryBackup.backupGeo[].rrdatasRefs[].kind` _Optional_ |  `string` Kind of the referent. Allowed values: ComputeAddress  
`routingPolicy.primaryBackup.backupGeo[].rrdatasRefs[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`routingPolicy.primaryBackup.backupGeo[].rrdatasRefs[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`routingPolicy.primaryBackup.enableGeoFencingForBackups` _Optional_ |  `boolean` Specifies whether to enable fencing for backup geo queries.  
`routingPolicy.primaryBackup.primary` _Required*_ |  `object` The list of global primary targets to be health checked.  
`routingPolicy.primaryBackup.primary.externalEndpoints` _Optional_ |  `list (string)` The Internet IP addresses to be health checked.  
`routingPolicy.primaryBackup.primary.externalEndpoints[]` _Optional_ |  `string`  
`routingPolicy.primaryBackup.primary.internalLoadBalancers` _Optional_ |  `list (object)` The list of internal load balancers to health check.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[]` _Optional_ |  `object`  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].ipAddressRef` _Required*_ |  `object` ComputeAddressRef is a reference to a Google Cloud ComputeAddress.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].ipAddressRef.external` _Optional_ |  `string` A reference to an externally managed ComputeAddress resource. Should be in the format "projects/{{projectID}}/global/addresses/{{addressID}}" or "projects/{{projectID}}/regions/{{region}}/addresses/{{addressID}}".  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].ipAddressRef.name` _Optional_ |  `string` The name of a ComputeAddress resource.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].ipAddressRef.namespace` _Optional_ |  `string` The namespace of a ComputeAddress resource.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].ipProtocol` _Required*_ |  `string` The configured IP protocol of the load balancer. This value is case-sensitive. Possible values: ["tcp", "udp"].  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].loadBalancerType` _Required*_ |  `string` The type of load balancer. This value is case-sensitive. Possible values: ["regionalL4ilb", "regionalL7ilb", "globalL7ilb"].  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].networkRef` _Required*_ |  `object` ComputeNetworkRef is a reference to a Google Cloud ComputeNetwork.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].networkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeNetwork resource. Should be in the format "projects/{{projectID}}/global/networks/{{networkID}}".  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].networkRef.name` _Optional_ |  `string` The name of a ComputeNetwork resource.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].networkRef.namespace` _Optional_ |  `string` The namespace of a ComputeNetwork resource.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].port` _Required*_ |  `string` The configured port of the load balancer.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].projectRef` _Required*_ |  `object` ProjectRef is a reference to a Google Cloud Project.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].regionRef` _Optional_ |  `object`  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].regionRef.external` _Optional_ |  `string` The compute region name, when not managed by Config Connector.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].regionRef.name` _Optional_ |  `string` Name of a ComputeRegion object.  
`routingPolicy.primaryBackup.primary.internalLoadBalancers[].regionRef.namespace` _Optional_ |  `string` Namespace of a ComputeRegion object  
`routingPolicy.primaryBackup.trickleRatio` _Optional_ |  `float` Specifies the percentage of traffic to send to the backup targets even when the primary targets are healthy.  
`routingPolicy.wrr` _Optional_ |  `list (object)` The configuration for Weighted Round Robin based routing policy.  
`routingPolicy.wrr[]` _Optional_ |  `object`  
`routingPolicy.wrr[].healthCheckedTargets` _Optional_ |  `object` The list of targets to be health checked. Note that if DNSSEC is enabled for this zone, only one of `rrdatas` or `health_checked_targets` can be set.  
`routingPolicy.wrr[].healthCheckedTargets.externalEndpoints` _Optional_ |  `list (string)` The Internet IP addresses to be health checked.  
`routingPolicy.wrr[].healthCheckedTargets.externalEndpoints[]` _Optional_ |  `string`  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers` _Optional_ |  `list (object)` The list of internal load balancers to health check.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[]` _Optional_ |  `object`  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef` _Required*_ |  `object` ComputeAddressRef is a reference to a Google Cloud ComputeAddress.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.external` _Optional_ |  `string` A reference to an externally managed ComputeAddress resource. Should be in the format "projects/{{projectID}}/global/addresses/{{addressID}}" or "projects/{{projectID}}/regions/{{region}}/addresses/{{addressID}}".  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.name` _Optional_ |  `string` The name of a ComputeAddress resource.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].ipAddressRef.namespace` _Optional_ |  `string` The namespace of a ComputeAddress resource.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].ipProtocol` _Required*_ |  `string` The configured IP protocol of the load balancer. This value is case-sensitive. Possible values: ["tcp", "udp"].  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].loadBalancerType` _Required*_ |  `string` The type of load balancer. This value is case-sensitive. Possible values: ["regionalL4ilb", "regionalL7ilb", "globalL7ilb"].  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].networkRef` _Required*_ |  `object` ComputeNetworkRef is a reference to a Google Cloud ComputeNetwork.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].networkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeNetwork resource. Should be in the format "projects/{{projectID}}/global/networks/{{networkID}}".  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].networkRef.name` _Optional_ |  `string` The name of a ComputeNetwork resource.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].networkRef.namespace` _Optional_ |  `string` The namespace of a ComputeNetwork resource.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].port` _Required*_ |  `string` The configured port of the load balancer.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].projectRef` _Required*_ |  `object` ProjectRef is a reference to a Google Cloud Project.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].regionRef` _Optional_ |  `object`  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].regionRef.external` _Optional_ |  `string` The compute region name, when not managed by Config Connector.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].regionRef.name` _Optional_ |  `string` Name of a ComputeRegion object.  
`routingPolicy.wrr[].healthCheckedTargets.internalLoadBalancers[].regionRef.namespace` _Optional_ |  `string` Namespace of a ComputeRegion object  
`routingPolicy.wrr[].rrdatasRefs` _Optional_ |  `list (object)`  
`routingPolicy.wrr[].rrdatasRefs[]` _Optional_ |  `object`  
`routingPolicy.wrr[].rrdatasRefs[].external` _Optional_ |  `string` Allowed value: The `address` field of a `ComputeAddress` resource.  
`routingPolicy.wrr[].rrdatasRefs[].kind` _Optional_ |  `string` Kind of the referent. Allowed values: ComputeAddress  
`routingPolicy.wrr[].rrdatasRefs[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`routingPolicy.wrr[].rrdatasRefs[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`routingPolicy.wrr[].weight` _Required*_ |  `float` The ratio of traffic routed to the target.  
`rrdatas` _Optional_ |  `list (string)` DEPRECATED. Although this field is still available, there is limited support. We recommend that you use `spec.rrdatasRefs` instead.  
`rrdatas[]` _Optional_ |  `string`  
`rrdatasRefs` _Optional_ |  `list (object)`  
`rrdatasRefs[]` _Optional_ |  `object`  
`rrdatasRefs[].external` _Optional_ |  `string` Allowed value: The `address` field of a `ComputeAddress` resource.  
`rrdatasRefs[].kind` _Optional_ |  `string` Kind of the referent. Allowed values: ComputeAddress  
`rrdatasRefs[].name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`rrdatasRefs[].namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`ttl` _Optional_ |  `integer` The time-to-live of this record set (seconds).  
`type` _Required_ |  `string` The DNS record set type.  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    observedGeneration: integer
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the DNSRecordSet's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
  
## Sample YAML(s)

### DNS A Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-a
    spec:
      name: "www.example.com."
      type: "A"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-a
      rrdatas:
      - "8.8.8.8"
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-a
    spec:
      dnsName: "example.com."
    

### DNS A Record Set With Compute Address Reference
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-computeaddressreference
    spec:
      name: "www.compute-address-reference-example.com."
      type: A
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-computeaddressreference
      rrdatasRefs:
        - name: dnsrecordset-dep-computeaddressreference
          kind: ComputeAddress
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: dnsrecordset-dep-computeaddressreference
    spec:
      addressType: INTERNAL
      description: a test global address
      location: global
      ipVersion: IPV4
      purpose: VPC_PEERING
      prefixLength: 16
      networkRef:
        name: dnsrecordset-dep-computeaddressreference
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      name: dnsrecordset-dep-computeaddressreference
    spec:
      routingMode: REGIONAL
      autoCreateSubnetworks: false
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-computeaddressreference
    spec:
      dnsName: "compute-address-reference-example.com."
    

### DNS Aaaa Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-aaaa
    spec:
      name: "www.example.com."
      type: "AAAA"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-aaaa
      rrdatas:
      - "8888:8888:8888:8888::"
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-aaaa
    spec:
      dnsName: "example.com."
    

### DNS Cname Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-cname
    spec:
      name: "*.example.com."
      type: "CNAME"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-cname
      rrdatas:
      - ".www.example.com."
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-cname
    spec:
      dnsName: "example.com."
    

### DNS Mx Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-mx
    spec:
      name: "mail.example.com."
      type: "MX"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-mx
      rrdatas:
      - "5 gmr-stmp-in.l.google.com."
      - "10 alt1.gmr-stmp-in.l.google.com."
      - "10 alt2.gmr-stmp-in.l.google.com."
      - "10 alt3.gmr-stmp-in.l.google.com."
      - "10 alt4.gmr-stmp-in.l.google.com."
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-mx
    spec:
      dnsName: "example.com."
    

### DNS Ns Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-ns
    spec:
      name: "example.com."
      type: "NS"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-ns
      rrdatas:
      - "ns-cloud-a1.googledomains.com."
      - "ns-cloud-a2.googledomains.com."
      - "ns-cloud-a3.googledomains.com."
      - "ns-cloud-a4.googledomains.com."
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-ns
    spec:
      dnsName: "example.com."
    

### DNS Routing Policy Geo
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-rp-geo
    spec:
      name: "www.kcc-sample-dnsrecordset-rp-geo.com."
      type: "A"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-rp-geo
      routingPolicy:
        geo:
          - location: us-central1
            rrdatasRefs:
              - external: "1.2.3.4"
              - external: "1.2.3.5"
          - location: us-west1
            rrdatasRefs:
              - external: "2.3.4.5"
              - external: "2.3.4.6"
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-rp-geo
    spec:
      dnsName: "kcc-sample-dnsrecordset-rp-geo.com."
    

### DNS Routing Policy Geo Health Checks
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-rp-geo-hc
    spec:
      name: "www.example.com."
      type: "A"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-rp-geo-hc
      routingPolicy:
        geo:
          - location: us-central1
            healthCheckedTargets:
              internalLoadBalancers:
                - ipAddressRef:
                    name: dnsrecordset-dep-rp-geo-hc
                  ipProtocol: tcp
                  loadBalancerType: regionalL4ilb
                  networkRef:
                    name: dnsrecordset-dep-rp-geo-hc
                  port: '80'
                  projectRef:
                    external: ${PROJECT_ID?}
                  regionRef:
                    name: dnsrecordset-dep-rp-geo-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: dnsrecordset-dep-rp-geo-hc
    spec:
      addressType: INTERNAL
      location: us-central1
      ipVersion: IPV4
      purpose: SHARED_LOADBALANCER_VIP
      subnetworkRef:
        name: dnsrecordset-dep-rp-geo-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeBackendService
    metadata:
      name: dnsrecordset-dep-rp-geo-hc
    spec:
      healthChecks:
      - healthCheckRef:
          name: dnsrecordset-dep-rp-geo-hc
      loadBalancingScheme: INTERNAL
      location: us-central1
      protocol: TCP
      backend:
      - balancingMode: CONNECTION
        group:
          instanceGroupRef:
            name: dnsrecordset-dep-rp-geo-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeForwardingRule
    metadata:
      name: dnsrecordset-dep-rp-geo-hc
    spec:
      backendServiceRef:
        name: dnsrecordset-dep-rp-geo-hc
      ipAddress:
        addressRef:
          name: dnsrecordset-dep-rp-geo-hc
      ipProtocol: "TCP"
      loadBalancingScheme: INTERNAL
      location: us-central1
      networkRef:
        name: dnsrecordset-dep-rp-geo-hc
      subnetworkRef:
        name: dnsrecordset-dep-rp-geo-hc
      ports:
        - '80'
      allowGlobalAccess: true
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeHealthCheck
    metadata:
      name: dnsrecordset-dep-rp-geo-hc
    spec:
      httpHealthCheck:
        port: 80
      location: us-central1
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeInstanceGroup
    metadata:
      name: dnsrecordset-dep-rp-geo-hc
    spec:
      zone: us-central1-a
      networkRef:
        name: dnsrecordset-dep-rp-geo-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      name: dnsrecordset-dep-rp-geo-hc
    spec:
      routingMode: REGIONAL
      autoCreateSubnetworks: false
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      name: dnsrecordset-dep-rp-geo-hc
    spec:
      ipCidrRange: 10.2.0.0/28
      region: us-central1
      networkRef:
        name: dnsrecordset-dep-rp-geo-hc
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-rp-geo-hc
    spec:
      dnsName: "example.com."
      visibility: private
      privateVisibilityConfig:
        networks:
          - networkRef:
              name: dnsrecordset-dep-rp-geo-hc
    

### DNS Routing Policy Geo With Compute Address Reference
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-rp-geo-reference
    spec:
      name: "www.example.com."
      type: "A"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-rp
      routingPolicy:
        geo:
          - location: us-central1
            rrdatasRefs:
              - name: dnsrecordset-dep-computeaddressreference1
                kind: ComputeAddress
          - location: us-west1
            rrdatasRefs:
              - name: dnsrecordset-dep-computeaddressreference2
                kind: ComputeAddress
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: dnsrecordset-dep-computeaddressreference1
    spec:
      addressType: INTERNAL
      description: a test global address
      location: global
      ipVersion: IPV4
      purpose: VPC_PEERING
      prefixLength: 16
      networkRef:
        name: dnsrecordset-dep-computenetworkreference
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: dnsrecordset-dep-computeaddressreference2
    spec:
      addressType: INTERNAL
      description: a test global address
      location: global
      ipVersion: IPV4
      purpose: VPC_PEERING
      prefixLength: 16
      networkRef:
        name: dnsrecordset-dep-computenetworkreference
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      name: dnsrecordset-dep-computenetworkreference
    spec:
      routingMode: REGIONAL
      autoCreateSubnetworks: false
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-rp
    spec:
      dnsName: "example.com."
      visibility: private
      privateVisibilityConfig:
        networks:
        - networkRef:
            name: dnsrecordset-dep-computenetworkreference
    

### DNS Routing Policy Primary Backup
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-rp-pb-hc
    spec:
      name: "www.example.com."
      type: "A"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-rp-pb-hc
      routingPolicy:
        primaryBackup:
          primary:
            internalLoadBalancers:
              - ipAddressRef:
                  name: dnsrecordset-dep-rp-pb-hc
                ipProtocol: tcp
                loadBalancerType: globalL7ilb
                networkRef:
                  name: dnsrecordset-dep-rp-pb-hc
                port: '80'
                projectRef:
                  external: ${PROJECT_ID?}
          backupGeo:
            - location: us-central1
              rrdatasRefs:
                - external: "1.2.3.4"
                - external: "1.2.3.5"
            - location: us-west1
              rrdatasRefs:
                - external: "2.3.4.5"
                - external: "2.3.4.6"
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      addressType: INTERNAL
      location: us-central1
      ipVersion: IPV4
      purpose: SHARED_LOADBALANCER_VIP
      subnetworkRef:
        name: dnsrecordset-dep1-rp-pb-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeBackendService
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      healthChecks:
      - healthCheckRef:
          name: dnsrecordset-dep-rp-pb-hc
      loadBalancingScheme: INTERNAL_MANAGED
      location: global
      protocol: HTTP
      backend:
      - balancingMode: UTILIZATION
        group:
          instanceGroupRef:
            name: dnsrecordset-dep-rp-pb-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeForwardingRule
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      target:
        targetHTTPProxyRef:
          name: dnsrecordset-dep-rp-pb-hc
      ipAddress:
        addressRef:
          name: dnsrecordset-dep-rp-pb-hc
      ipProtocol: "TCP"
      loadBalancingScheme: INTERNAL_MANAGED
      location: global
      networkRef:
        name: dnsrecordset-dep-rp-pb-hc
      subnetworkRef:
        name: dnsrecordset-dep1-rp-pb-hc
      portRange: '80-80'
      allowGlobalAccess: true
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeHealthCheck
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      httpHealthCheck:
        port: 80
      location: global
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeInstanceGroup
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      zone: us-central1-a
      networkRef:
        name: dnsrecordset-dep-rp-pb-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      routingMode: REGIONAL
      autoCreateSubnetworks: false
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      name: dnsrecordset-dep1-rp-pb-hc
    spec:
      ipCidrRange: 10.2.0.0/28
      region: us-central1
      networkRef:
        name: dnsrecordset-dep-rp-pb-hc
    
    ---
    
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      name: dnsrecordset-dep2-rp-pb-hc
    spec:
      ipCidrRange: 10.3.0.0/26
      region: us-central1
      purpose: GLOBAL_MANAGED_PROXY
      role: ACTIVE
      networkRef:
        name: dnsrecordset-dep-rp-pb-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeTargetHTTPProxy
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      urlMapRef:
        name: dnsrecordset-dep-rp-pb-hc
      location: global
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeURLMap
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      defaultService:
        backendServiceRef:
          name: dnsrecordset-dep-rp-pb-hc
      location: global
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-rp-pb-hc
    spec:
      dnsName: "example.com."
      visibility: private
      privateVisibilityConfig:
        networks:
          - networkRef:
              name: dnsrecordset-dep-rp-pb-hc
    

### DNS Routing Policy Wrr
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-rp-wrr
    spec:
      name: "www.kcc-sample-dnsrecordset-rp-wrr.com."
      type: "A"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-rp-wrr
      routingPolicy:
        wrr:
          - weight: 0.5
            rrdatasRefs:
              - external: "1.2.3.4"
              - external: "1.2.3.5"
          - weight: 0.5
            rrdatasRefs:
              - external: "2.3.4.5"
              - external: "2.3.4.6"
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-rp-wrr
    spec:
      dnsName: "kcc-sample-dnsrecordset-rp-wrr.com."
    

### DNS Routing Policy Wrr Health Checks
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-rp-wrr-hc
    spec:
      name: "www.example.com."
      type: "A"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-rp-wrr-hc
      routingPolicy:
        wrr:
          - weight: 1
            healthCheckedTargets:
              internalLoadBalancers:
                - ipAddressRef:
                    name: dnsrecordset-dep-rp-wrr-hc
                  ipProtocol: tcp
                  loadBalancerType: regionalL4ilb
                  networkRef:
                    name: dnsrecordset-dep-rp-wrr-hc
                  port: '80'
                  projectRef:
                    external: ${PROJECT_ID?}
                  regionRef:
                    name: dnsrecordset-dep-rp-wrr-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeAddress
    metadata:
      name: dnsrecordset-dep-rp-wrr-hc
    spec:
      addressType: INTERNAL
      location: us-central1
      ipVersion: IPV4
      purpose: SHARED_LOADBALANCER_VIP
      subnetworkRef:
        name: dnsrecordset-dep-rp-wrr-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeBackendService
    metadata:
      name: dnsrecordset-dep-rp-wrr-hc
    spec:
      healthChecks:
      - healthCheckRef:
          name: dnsrecordset-dep-rp-wrr-hc
      loadBalancingScheme: INTERNAL
      location: us-central1
      protocol: TCP
      backend:
      - balancingMode: CONNECTION
        group:
          instanceGroupRef:
            name: dnsrecordset-dep-rp-wrr-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeForwardingRule
    metadata:
      name: dnsrecordset-dep-rp-wrr-hc
    spec:
      backendServiceRef:
        name: dnsrecordset-dep-rp-wrr-hc
      ipAddress:
        addressRef:
          name: dnsrecordset-dep-rp-wrr-hc
      ipProtocol: "TCP"
      loadBalancingScheme: INTERNAL
      location: us-central1
      networkRef:
        name: dnsrecordset-dep-rp-wrr-hc
      subnetworkRef:
        name: dnsrecordset-dep-rp-wrr-hc
      ports:
        - '80'
      allowGlobalAccess: true
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeHealthCheck
    metadata:
      name: dnsrecordset-dep-rp-wrr-hc
    spec:
      httpHealthCheck:
        port: 80
      location: us-central1
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeInstanceGroup
    metadata:
      name: dnsrecordset-dep-rp-wrr-hc
    spec:
      zone: us-central1-a
      networkRef:
        name: dnsrecordset-dep-rp-wrr-hc
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      name: dnsrecordset-dep-rp-wrr-hc
    spec:
      routingMode: REGIONAL
      autoCreateSubnetworks: false
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      name: dnsrecordset-dep-rp-wrr-hc
    spec:
      ipCidrRange: 10.2.0.0/28
      region: us-central1
      networkRef:
        name: dnsrecordset-dep-rp-wrr-hc
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-rp-wrr-hc
    spec:
      dnsName: "example.com."
      visibility: private
      privateVisibilityConfig:
        networks:
          - networkRef:
              name: dnsrecordset-dep-rp-wrr-hc
    

### DNS Srv Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-srv
    spec:
      name: "_example._tcp.example.com."
      type: "SRV"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-srv
      rrdatas:
      - "0 0 9 tcpserver.cnrm-dns-example.com."
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-srv
    spec:
      dnsName: "example.com."
    

### DNS Txt Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-txt
    spec:
      name: "example.com."
      type: "TXT"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-txt
      rrdatas:
      - "\"This is a sample DNS text record string\""
      - "Text records are normally split on spaces"
      - "To prevent this, \"quote your text like this\""
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-txt
    spec:
      dnsName: "example.com."
    

### Dnssec Dnskey Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-dnssecdnskey
    spec:
      name: "secure.example.com."
      type: "DNSKEY"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-dnssecdnskey
      rrdatas:
      - "256 3 8 AwEAAcAPhPM4CQHqg6hZ49y2P3IdKZuF44QNCc50vjATD7W+je4va6djY5JpnNP0pIohKNYiCFap/b4Y9jjJGSOkOfkfBR8neI7X5LisMEGUjwRcrG8J9UYP1S1unTNqRcWyDYFH2q3KnIO08zImh5DiFt8yfCdKoqZUN1dup5hy0UWz"
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-dnssecdnskey
    spec:
      dnsName: "secure.example.com."
      dnssecConfig:
        state: "transfer"
    

### Dnssec Ds Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-dnssecds
    spec:
      name: "host.secure.example.com."
      type: "DS"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-dnssecds
      rrdatas:
      - "31523 5 1 c8761ba5defc26ac7b78e076d7c47fa9f86b9fba"
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-dnssecds
    spec:
      dnsName: "secure.example.com."
      dnssecConfig:
        state: "on"
    

### Dnssec Ipsecvpnkey Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-dnssecipsecvpnkey
    spec:
      name: "service.secure.example.com."
      type: "IPSECKEY"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-dnssecipsecvpnkey
      rrdatas:
      - "10 1 2 192.0.2.3 AQNRU3mG7TVTO2BkR47usntb102uFJtugbo6BSGvgqt4AQ=="
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-dnssecipsecvpnkey
    spec:
      dnsName: "secure.example.com."
      dnssecConfig:
        state: "on"
    

### Dnssec Sshfp Record Set
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSRecordSet
    metadata:
      name: dnsrecordset-sample-dnssecsshfp
    spec:
      name: "host.secure.example.com."
      type: "SSHFP"
      ttl: 300
      managedZoneRef:
        name: dnsrecordset-dep-dnssecsshfp
      rrdatas:
      - "2 1 123456789abcdef67890123456789abcdef67890"
    ---
    apiVersion: dns.cnrm.cloud.google.com/v1beta1
    kind: DNSManagedZone
    metadata:
      name: dnsrecordset-dep-dnssecsshfp
    spec:
      dnsName: "secure.example.com."
      dnssecConfig:
        state: "on"
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
