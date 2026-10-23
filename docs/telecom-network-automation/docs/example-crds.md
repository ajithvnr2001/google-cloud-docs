---
url: https://docs.cloud.google.com/telecom-network-automation/docs/example-crds/
title: Example custom resource definitions \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:38.416579+00:00
---

# Example custom resource definitions  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/example-crds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Example custom resource definitions Stay organized with collections  Save and categorize content based on your preferences. 

This page displays example custom resource definitions (CRD) for clusters in Telecom Network Automation.

## Example `WorkloadCluster` CRD
    
    
    apiVersion: apiextensions.k8s.io/v1 
    kind: CustomResourceDefinition 
    metadata: 
      annotations: 
        cert-manager.io/inject-ca-from: ${tna-namespace}/workloadcluster-serving-cert controller-gen.kubebuilder.io/version: v0.9.2 
        name: workloadclusters.infra.tna.cloud.google.com 
    spec: 
      conversion: 
        strategy: Webhook 
        webhook: 
          clientConfig: 
            service: 
              name: workloadcluster-webhook-service 
              namespace: ${tna-namespace} 
              path: /convert 
          conversionReviewVersions: 
          - v1 
      group: infra.tna.cloud.google.com 
      names: 
        kind: WorkloadCluster 
        listKind: WorkloadClusterList 
        plural: workloadclusters 
        singular: workloadcluster 
      scope: Cluster 
      versions: 
      - name: v1alpha1 
        schema: 
          openAPIV3Schema: 
          description: WorkloadCluster is the Schema for the workloadclusters
          API properties: 
            apiVersion: 
              description: 'APIVersion defines the versioned schema of this 
    representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md #resources'
              type: string 
            kind: 
              description: 'Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: 
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md #types-kinds' 
              type: string 
                metadata: 
              type: object 
                spec: 
                  description: WorkloadClusterSpec defines the desired state of WorkloadCluster 
                  properties: 
                    VPC: 
                      type: string 
                    adminUser: 
                      minLength: 1 
                      pattern: ^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$ 
                      type: string 
                    clusterIPv4CIDR: 
                      items: 
                        pattern: ^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$ 
                        type: string 
                      maxItems: 1 
                      minItems: 1 
                      type: array
                    controlPlane: 
                      properties: 
                        nodeCount: 
                          description: NodeCount specifies the number of nodes to serve as replicas of the Control Plane. 
                          enum: 
                          - 1 
                          - 3 
                          format: int64 
                          type: integer
                        sharedDeploymentPolicy: 
                          enum: 
                          - SHARED_DEPLOYMENT_POLICY_UNSPECIFIED 
                          - DISALLOWED 
                          - ALLOWED
                        type: string 
                    type: object 
                  defaultMaxPodsPerNode: 
                    format: int64 
                    type: integer 
                  externalLoadBalancerIpv4AddressPools: 
                    description: ExternalLoadBalancerIpv4AddressPools specifies address pools for cluster data plane external load balancing. 
                    items: 
                      type: string 
                      type: array 
                    gdceVPNConnectionName: 
                      type: string 
                    labels: 
                      additionalProperties: 
                        type: string 
                      type: object 
                    location:
                      description: Location is the region ( for example us-central1 ) where the underlying cloud resources are created 
                      minLength: 1 
                      pattern: ^[a-zA-Z0-9-._~%!$&'()*+,;=@]+$ 
                      type: string 
                    maintenancePolicy: 
                      description: 'EdgeMaintenancePolicy : Cluster-wide maintenance  policy configuration.' 
                      properties: 
                        endTime: 
                          description: 'EndTime: The time that the window ends. The end time must take place after the start time.' 
                            type: string 
                          recurrence: 
                            description: 'Recurrence: A rule (https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for how this window recurs. They go on for the span of time between the start and end time.'
                            type: string 
                            startTime: 
                              description: 'StartTime: The time that the window first starts.' 
                              type: string 
                            type: object 
                          natGatewayIP: 
                            type: string 
                          nodePools: 
                            items: 
                              properties:
                                labels:
                                  additionalProperties:
                                  type: string
                                description: 'Add validation for labels'
                                type: object 
                              name: 
                                minLength: 1 
                                pattern: ^[a-zA-Z0-9-._~%!$&'()*+,;=@]+$ 
                                type: string 
                              nodeCount: 
                                format: int64 
                                minimum: 1 
                                type: integer 
                              scaleDownGracePeriodSeconds: 
                                description: Number of seconds to wait for the workloads to 
                                get gracefully removed from the nodes selected for removal during scale down. This is useful for critical NF workloads that cannot tolerate disruption during pod re-scheduling done by kubernetes on node removal. The node resources like HugePages, Sriov VFs will be drained after this period and will initiate node removal from the underlying infrastructure.
                                format: int64 
                                type: integer
                              scaleDownTimestamp:
                                description: The timestamp at which the node pool scaledown was initiated.
                              format: date-time
                              type: string
                          required: 
                          - name 
                          - nodeCount 
                          type: object 
                        minItems: 1 
                        type: array 
                        serviceIPv4CIDR: 
                          items: 
                            pattern: ^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$ 
                            type: string 
                          maxItems: 1 
                          minItems: 1 
                          type: array
                        targetVersion:
                          enum:
                          - 1.5.0
                          type: string 
                      type: 
                        enum: 
                        - GKE 
                        - GDCE 
                        type: string 
                      vpnLabels:
                        additionalProperties:
                          type: string
                        type: object
                      zone:
                        description: This is the GDCE zone used by the local control plane and all the nodepools.
                        pattern: -edge
                        type: string
                      required:
                      - clusterIPv4CIDR
                      - location
                      - nodePools
                      - serviceIPv4CIDR
                      - type
                      type: object
                    status:
                      description: WorkloadClusterStatus defines the observed state of WorkloadCluster
                      properties:
                        conditions:
                          description: Conditions describes the reconciliation state of the object.
                          items:
                            description: "Condition contains details for one aspect of the 
                            current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, \n type ExampleStatus struct{ // Represents the observations of the ExampleStatus current state. // Known .status.conditions.type are: \"Available\", \"Progressing\", and \"Degraded\" // 
    
                            +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:\"conditions,omitempty\" 
                            patchStrategy:\"merge\" patchMergeKey:\"type\" 
                            protobuf:\"bytes,1,rep,name=conditions\"` \n // other fields }" 
                            properties:
                              lastTransitionTime:
                                description: lastTransitionTime is the last time the 
                                condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. 
                                format: date-time
                                type: string
                              message:
                                description: message is a human readable message indicating details about the transition. This may be an empty string.
                                maxLength: 32768
                                type: string
                              observedGeneration:
                                description: observedGeneration represents the 
                                .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the 
                                .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. 
                                format: int64
                                minimum: 0
                                type: integer
                              reason:
                                description: reason contains a programmatic identifier
                                indicating the reason for the last transition of the condition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.
                                maxLength: 1024
                                minLength: 1
                                pattern: ^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$
                                type: string
                              status:
                                description: status of the condition, one of True, False, Unknown. 
                                  enum: 
                                  - "True" 
                                  - "False" 
                                  - Unknown 
                                  type: string 
                              type: 
                                description: type of condition in CamelCase or in 
                                test.example.com/CamelCase. --- Many .condition.type values are consistent across 
                                resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt) 
                                maxLength: 316
                                pattern:
                                ^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][- A-Za-z0-9_.]*)?[A-Za-z0-9])$ 
                                type: string
                            required:
                            - lastTransitionTime
                            - message
                            - reason
                            - status
                            - type
                            type: object
                        type: array
                      endpoint:
                        description: Endpoint is the IP address of the Kubernetes API server.
                        type: string
                      observedGeneration:
                        format: int64
                        type: integer
                      ownedResources:
                        items:
                          properties:
                            group:
                              type: string
                            kind:
                              type: string
                            message:
                              type: string
                            name:
                              type: string
                            namespace:
                              type: string
                            reason:
                              type: string
                            status:
                              type: string
                            version:
                              type: string
                          required:
                          - group
                          - kind
                          - message
                          - name
                          - namespace
                          - reason
                          - status
                          - version
                          type: object
                        type: array
                    required: 
                    - observedGeneration 
                    type: object 
                type: object 
            served: true 
            storage: true 
            subresources: 
              status: {}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
