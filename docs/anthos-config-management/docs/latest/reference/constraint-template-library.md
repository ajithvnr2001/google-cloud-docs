---
url: https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library/
title: Constraint template library \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:31:39.584912+00:00
---

# Constraint template library  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/reference)



Send feedback 

#  Constraint template library Stay organized with collections  Save and categorize content based on your preferences. 

Constraint templates let you define how a constraint works but delegate defining the specifics of the constraint to an individual or group with subject matter expertise. In addition to separating concerns, this also separates the logic of the constraint from its definition.

All constraints contain a `match` section, which defines the objects a constraint applies to. For details on how to configure that section, see [Constraint match section](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/reference/match).

Not all constraint templates are available for all versions of Policy Controller and templates can change between versions. Use the following links to compare constraints from supported versions:

Links to supported versions of this page

  * [1.17 Constraint template library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/archive/1.17/reference/constraint-template-library)
  * [1.16 Constraint template library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/archive/1.16/reference/constraint-template-library)



To ensure that you receive full support, we recommend that you use constraint templates from a [supported version](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/get-support-policy-controller#version_support_policy) of Policy Controller.

To help you see how the constraint templates function, each template includes an example constraint and a resource that violates the constraint.

## Available constraint templates

Referential constraint template

**Constraint Template** | **Description** | **Referential**  
---|---|---  
[AllowedServicePortName](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#allowedserviceportname) | Requires that service port names have a prefix from a specified list. | No  
[AsmAuthzPolicyDefaultDeny](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicydefaultdeny) | Enforce the mesh level default deny AuthorizationPolicy. Reference to https://istio.io/latest/docs/ops/best-practices/security/#use-default-deny-patterns. | Yes  
[AsmAuthzPolicyDisallowedPrefix](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicydisallowedprefix) | Requires that principals and namespaces in Istio `AuthorizationPolicy` rules not have a prefix from a specified list. https://istio.io/latest/docs/reference/config/security/authorization-policy/ | No  
[AsmAuthzPolicyEnforceSourcePrincipals](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicyenforcesourceprincipals) | Requires that Istio AuthorizationPolicy "from" field, when defined, has source principles, which must be set to something other than "*". https://istio.io/latest/docs/reference/config/security/authorization-policy/ | No  
[AsmAuthzPolicyNormalization](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicynormalization) | Enforce the AuthorizationPolicy normalization. Reference to https://istio.io/latest/docs/reference/config/security/normalization/. | No  
[AsmAuthzPolicySafePattern](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmauthzpolicysafepattern) | Enforce the AuthorizationPolicy safe patterns. Reference to https://istio.io/latest/docs/ops/best-practices/security/#safer-authorization-policy-patterns. | No  
[AsmIngressgatewayLabel](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmingressgatewaylabel) | Enforce the istio ingressgateway label usage only on ingressgateway pods. | No  
[AsmPeerAuthnMeshStrictMtls](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmpeerauthnmeshstrictmtls) | Enforce the mesh level strict mtls PeerAuthentication. Reference to https://istio.io/latest/docs/ops/best-practices/security/#mutual-tls. | Yes  
[AsmPeerAuthnStrictMtls](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmpeerauthnstrictmtls) | Enforce all PeerAuthentications cannot overwrite strict mtls. Reference to https://istio.io/latest/docs/ops/best-practices/security/#mutual-tls. | No  
[AsmRequestAuthnProhibitedOutputHeaders](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmrequestauthnprohibitedoutputheaders) | In RequestAuthentication, enforce the `jwtRules.outPayloadToHeader` field to not contain well known HTTP request headers or custom prohibited headers. Reference to https://istio.io/latest/docs/reference/config/security/jwt/#JWTRule. | No  
[AsmSidecarInjection](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#asmsidecarinjection) | Enforce the istio proxy sidecar always been injected to workload pods. | No  
[DestinationRuleTLSEnabled](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#destinationruletlsenabled) | Prohibits disabling TLS for all hosts and host subsets in Istio DestinationRules. | No  
[DisallowedAuthzPrefix](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#disallowedauthzprefix) | Requires that principals and namespaces in Istio `AuthorizationPolicy` rules not have a prefix from a specified list. https://istio.io/latest/docs/reference/config/security/authorization-policy/ | No  
[GCPStorageLocationConstraintV1](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#gcpstoragelocationconstraintv1) | Restricts the permitted `locations` for StorageBucket Config Connector resources to the list of locations provided in the constraint. Bucket names in the `exemptions` list are exempt. | No  
[GkeSpotVMTerminationGrace](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#gkespotvmterminationgrace) | Requires Pods and Pod Templates with `nodeSelector` or `nodeAfffinty` of `gke-spot` to have a `terminationGracePeriodSeconds` of 15s or less. | Yes  
[K8sAllowedRepos](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sallowedrepos) | Requires container images to begin with a string from the specified list. | No  
[K8sAvoidUseOfSystemMastersGroup](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8savoiduseofsystemmastersgroup) | Disallows the use of 'system:masters' group. Has no effect during audit. | No  
[K8sBlockAllIngress](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sblockallingress) | Disallows the creation of Ingress objects (`Ingress`, `Gateway`, and `Service` types of `NodePort` and `LoadBalancer`). | No  
[K8sBlockCreationWithDefaultServiceAccount](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sblockcreationwithdefaultserviceaccount) | Disallows the creation of resources using a default service account. Has no effect during audit. | No  
[K8sBlockEndpointEditDefaultRole](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sblockendpointeditdefaultrole) | Many Kubernetes installations by default have a system:aggregate-to-edit ClusterRole which does not properly restrict access to editing Endpoints. This ConstraintTemplate forbids the system:aggregate-to-edit ClusterRole from granting permission to create/patch/update Endpoints. ClusterRole/system:aggregate-to-edit should not allow Endpoint edit permissions due to CVE-2021-25740, Endpoint & EndpointSlice permissions allow cross-Namespace forwarding, https://github.com/kubernetes/kubernetes/issues/103675 | No  
[K8sBlockLoadBalancer](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sblockloadbalancer) | Disallows all Services with type LoadBalancer. https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer | No  
[K8sBlockNodePort](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sblocknodeport) | Disallows all Services with type NodePort. https://kubernetes.io/docs/concepts/services-networking/service/#nodeport | No  
[K8sBlockObjectsOfType](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sblockobjectsoftype) | Disallows object of forbidden types. | No  
[K8sBlockProcessNamespaceSharing](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sblockprocessnamespacesharing) | Prohibits Pod specs with `shareProcessNamespace` set to `true`. This avoids scenarios where all containers in a Pod share a PID namespace and can access each other's filesystem and memory. | No  
[K8sBlockWildcardIngress](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sblockwildcardingress) | Users should not be able to create Ingresses with a blank or wildcard (*) hostname since that would enable them to intercept traffic for other services in the cluster, even if they don't have access to those services. | No  
[K8sContainerEphemeralStorageLimit](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8scontainerephemeralstoragelimit) | Requires containers to have an ephemeral storage limit set and constrains the limit to be within the specified maximum values. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | No  
[K8sContainerLimits](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8scontainerlimits) | Requires containers to have memory and CPU limits set and constrains limits to be within the specified maximum values. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | No  
[K8sContainerRatios](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8scontainerratios) | Sets a maximum ratio for container resource limits to requests. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | No  
[K8sContainerRequests](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8scontainerrequests) | Requires containers to have memory and CPU requests set and constrains requests to be within the specified maximum values. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | No  
[K8sCronJobAllowedRepos](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8scronjoballowedrepos) | Requires container images of CronJobs to begin with a string from the specified list. | No  
[K8sDisallowAnonymous](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sdisallowanonymous) | Disallows associating ClusterRole and Role resources to the system:anonymous user and system:unauthenticated group. | No  
[K8sDisallowInteractiveTTY](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sdisallowinteractivetty) | Requires that objects have the fields `spec.tty` and `spec.stdin` set to false or unset. | No  
[K8sDisallowedRepos](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sdisallowedrepos) | Disallowed container repositories that begin with a string from the specified list. | No  
[K8sDisallowedRoleBindingSubjects](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sdisallowedrolebindingsubjects) | Prohibits RoleBindings or ClusterRoleBindings with subjects matching any `disallowedSubjects` passed as parameters. | No  
[K8sDisallowedTags](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sdisallowedtags) | Requires container images to have an image tag different from the ones in the specified list. https://kubernetes.io/docs/concepts/containers/images/#image-names | No  
[K8sEmptyDirHasSizeLimit](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8semptydirhassizelimit) | Requires that any `emptyDir` volumes specify a `sizeLimit`. Optionally, a `maxSizeLimit` parameter can be supplied in the constraint to specify a maximum allowable size limit. | No  
[K8sEnforceCloudArmorBackendConfig](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8senforcecloudarmorbackendconfig) | Enforces Cloud Armor configuration on BackendConfig resources | No  
[K8sEnforceConfigManagement](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8senforceconfigmanagement) | Requires the presence and operation of Config Management. Constraints using this `ConstraintTemplate` will be audit only regardless of `enforcementAction` value. | Yes  
[K8sExternalIPs](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sexternalips) | Restricts Service externalIPs to an allowed list of IP addresses. https://kubernetes.io/docs/concepts/services-networking/service/#external-ips | No  
[K8sHorizontalPodAutoscaler](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8shorizontalpodautoscaler) | Disallow the following scenarios when deploying `HorizontalPodAutoscalers` 1. Deployment of HorizontalPodAutoscalers with `.spec.minReplicas` or `.spec.maxReplicas` outside the ranges defined in the constraint 2. Deployment of HorizontalPodAutoscalers where the difference between `.spec.minReplicas` and `.spec.maxReplicas` is less than the configured `minimumReplicaSpread` 3. Deployment of HorizontalPodAutoscalers that do not reference a valid `scaleTargetRef` (e.g. Deployment, ReplicationController, ReplicaSet, StatefulSet). | Yes  
[K8sHttpsOnly](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8shttpsonly) | Requires Ingress resources to be HTTPS only. Ingress resources must include the `kubernetes.io/ingress.allow-http` annotation, set to `false`. By default a valid TLS {} configuration is required, this can be made optional by setting the `tlsOptional` parameter to `true`. https://kubernetes.io/docs/concepts/services-networking/ingress/#tls | No  
[K8sImageDigests](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8simagedigests) | Requires container images to contain a digest. https://kubernetes.io/docs/concepts/containers/images/ | No  
[K8sLocalStorageRequireSafeToEvict](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8slocalstoragerequiresafetoevict) | Requires Pods using local storage (`emptyDir` or `hostPath`) to have the annotation `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"`. Cluster Autoscaler will not delete Pods without this annotation. | No  
[K8sMemoryRequestEqualsLimit](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8smemoryrequestequalslimit) | Promotes Pod stability by requiring that all containers' requested memory exactly equals the memory limit, so that Pods are never in a state where memory usage exceeds the requested amount. Otherwise, Kubernetes can terminate Pods requesting extra memory if memory is needed on the node. | No  
[K8sNoEnvVarSecrets](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8snoenvvarsecrets) | Prohibits secrets as environment variables in Pod container definitions. Use mounted secret files in data volumes instead: https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod | No  
[K8sNoExternalServices](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8snoexternalservices) | Prohibits the creation of known resources that expose workloads to external IPs. This includes Istio Gateway resources and Kubernetes Ingress resources. Kubernetes services are also disallowed unless they meet the following criteria: Any Service of type `LoadBalancer` in Google Cloud must have a `"networking.gke.io/load-balancer-type": "Internal"` annotation. Any Service of type `LoadBalancer` in AWS must have a `service.beta.kubernetes.io/aws-load-balancer-internal: "true` annotation. Any "external IPs" (external to the cluster) bound to the Service must be a member of a range of internal CIDRs as provided to the constraint. | No  
[K8sPSPAllowPrivilegeEscalationContainer](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspallowprivilegeescalationcontainer) | Controls restricting escalation to root privileges. Corresponds to the `allowPrivilegeEscalation` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#privilege-escalation | No  
[K8sPSPAllowedUsers](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspallowedusers) | Controls the user and group IDs of the container and some volumes. Corresponds to the `runAsUser`, `runAsGroup`, `supplementalGroups`, and `fsGroup` fields in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#users-and-groups | No  
[K8sPSPAppArmor](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspapparmor) | Configures an allow-list of AppArmor profiles for use by containers. This corresponds to specific annotations applied to a PodSecurityPolicy. For information on AppArmor, see https://kubernetes.io/docs/tutorials/clusters/apparmor/ | No  
[K8sPSPAutomountServiceAccountTokenPod](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspautomountserviceaccounttokenpod) | Controls the ability of any Pod to enable automountServiceAccountToken. | No  
[K8sPSPCapabilities](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspcapabilities) | Controls Linux capabilities on containers. Corresponds to the `allowedCapabilities` and `requiredDropCapabilities` fields in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#capabilities | No  
[K8sPSPFSGroup](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspfsgroup) | Controls allocating an FSGroup that owns the Pod's volumes. Corresponds to the `fsGroup` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems | No  
[K8sPSPFlexVolumes](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspflexvolumes) | Controls the allowlist of FlexVolume drivers. Corresponds to the `allowedFlexVolumes` field in PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#flexvolume-drivers | No  
[K8sPSPForbiddenSysctls](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspforbiddensysctls) | Controls the `sysctl` profile used by containers. Corresponds to the `allowedUnsafeSysctls` and `forbiddenSysctls` fields in a PodSecurityPolicy. When specified, any sysctl not in the `allowedSysctls` parameter is considered to be forbidden. The `forbiddenSysctls` parameter takes precedence over the `allowedSysctls` parameter. For more information, see https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ | No  
[K8sPSPHostFilesystem](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spsphostfilesystem) | Controls usage of the host filesystem. Corresponds to the `allowedHostPaths` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems | No  
[K8sPSPHostNamespace](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spsphostnamespace) | Disallows sharing of host PID and IPC namespaces by pod containers. Corresponds to the `hostPID` and `hostIPC` fields in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#host-namespaces | No  
[K8sPSPHostNetworkingPorts](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spsphostnetworkingports) | Controls usage of host network namespace by pod containers. Specific ports must be specified. Corresponds to the `hostNetwork` and `hostPorts` fields in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#host-namespaces | No  
[K8sPSPPrivilegedContainer](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspprivilegedcontainer) | Controls the ability of any container to enable privileged mode. Corresponds to the `privileged` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#privileged | No  
[K8sPSPProcMount](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspprocmount) | Controls the allowed `procMount` types for the container. Corresponds to the `allowedProcMountTypes` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#allowedprocmounttypes | No  
[K8sPSPReadOnlyRootFilesystem](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspreadonlyrootfilesystem) | Requires the use of a read-only root file system by pod containers. Corresponds to the `readOnlyRootFilesystem` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems | No  
[K8sPSPSELinuxV2](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspselinuxv2) | Defines an allow-list of seLinuxOptions configurations for pod containers. Corresponds to a PodSecurityPolicy requiring SELinux configs. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#selinux | No  
[K8sPSPSeccomp](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspseccomp) | Controls the seccomp profile used by containers. Corresponds to the `seccomp.security.alpha.kubernetes.io/allowedProfileNames` annotation on a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#seccomp | No  
[K8sPSPVolumeTypes](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspvolumetypes) | Restricts mountable volume types to those specified by the user. Corresponds to the `volumes` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems | No  
[K8sPSPWindowsHostProcess](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspwindowshostprocess) | Restricts running of Windows HostProcess containers / pods. See https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/ for more information. | No  
[K8sPSSRunAsNonRoot](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spssrunasnonroot) | Requires containers run as non-root users. For more information, see https://kubernetes.io/docs/concepts/security/pod-security-standards/ | No  
[K8sPodDisruptionBudget](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spoddisruptionbudget) | Disallow the following scenarios when deploying PodDisruptionBudgets or resources that implement the replica subresource (e.g. Deployment, ReplicationController, ReplicaSet, StatefulSet): 1. Deployment of PodDisruptionBudgets with .spec.maxUnavailable == 0 2. Deployment of PodDisruptionBudgets with .spec.minAvailable == .spec.replicas of the resource with replica subresource This will prevent PodDisruptionBudgets from blocking voluntary disruptions such as node draining. https://kubernetes.io/docs/concepts/workloads/pods/disruptions/ | Yes  
[K8sPodResourcesBestPractices](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spodresourcesbestpractices) | Requires that containers are not best-effort (by setting cpu and memory requests) and following burstable best practices (memory request must exactly equal limit). Optionally, annotation keys can be configured to permit skipping the various validations. | No  
[K8sPodsRequireSecurityContext](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spodsrequiresecuritycontext) | Requires all Pods to define securityContext. Requires all containers defined in Pods to have a SecurityContext defined at the Pod or container level. | No  
[K8sProhibitRoleWildcardAccess](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sprohibitrolewildcardaccess) | Requires that Roles and ClusterRoles not set resource access to a wildcard '"*"' value except for the exempted Roles and ClusterRoles provided as exemptions. Does not restrict wildcard access to subresources, such as '"*/status"'. | No  
[K8sReplicaLimits](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sreplicalimits) | Requires that objects with the field `spec.replicas` (Deployments, ReplicaSets, etc.) specify a number of replicas within defined ranges. | No  
[K8sRequireAdmissionController](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequireadmissioncontroller) | Requires either Pod Security Admission or an external policy control system | Yes  
[K8sRequireBinAuthZ](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequirebinauthz) | Requires the Binary Authorization Validating Admission Webhook. Constraints using this `ConstraintTemplate` will be audit only regardless of `enforcementAction` value. | Yes  
[K8sRequireCosNodeImage](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequirecosnodeimage) | Enforces the use of Container-Optimized OS from Google on Nodes. | No  
[K8sRequireDaemonsets](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequiredaemonsets) | Requires the list of daemonsets specified to be present. | Yes  
[K8sRequireDefaultDenyEgressPolicy](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequiredefaultdenyegresspolicy) | Requires that every namespace defined in the cluster has a default deny NetworkPolicy for egress. | Yes  
[K8sRequireNamespaceNetworkPolicies](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequirenamespacenetworkpolicies) | Requires that every namespace defined in the cluster has a NetworkPolicy. | Yes  
[K8sRequireValidRangesForNetworks](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequirevalidrangesfornetworks) | Enforces which CIDR blocks are allowed for network ingress and egress. | No  
[K8sRequiredAnnotations](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequiredannotations) | Requires resources to contain specified annotations, with values matching provided regular expressions. | No  
[K8sRequiredLabels](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequiredlabels) | Requires resources to contain specified labels, with values matching provided regular expressions. | No  
[K8sRequiredProbes](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequiredprobes) | Requires Pods to have readiness and/or liveness probes. | No  
[K8sRequiredResources](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequiredresources) | Requires containers to have defined resources set. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | No  
[K8sRestrictAdmissionController](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictadmissioncontroller) | Restrict dynamic admission controllers to permitted ones | No  
[K8sRestrictAutomountServiceAccountTokens](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictautomountserviceaccounttokens) | Restricts the use of service accounts tokens. | No  
[K8sRestrictLabels](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictlabels) | Disallows resources from containing specified labels unless there is an exception for the specific resource. | No  
[K8sRestrictNamespaces](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictnamespaces) | Restricts resources from using namespaces listed under the restrictedNamespaces parameter. | No  
[K8sRestrictNfsUrls](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictnfsurls) | Disallows resources from containing NFS URLS unless specified. | No  
[K8sRestrictRbacSubjects](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictrbacsubjects) | Restricts the use of names in RBAC subjects to permitted values. | No  
[K8sRestrictRoleBindings](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictrolebindings) | Restricts the subjects specified in ClusterRoleBindings and RoleBindings to a list of allowed subjects. | No  
[K8sRestrictRoleRules](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictrolerules) | Restricts rules that can be set on Role and ClusterRole objects. | No  
[K8sStorageClass](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sstorageclass) | Requires storage classes to be specified when used. Only Gatekeeper 3.9+ and non-ephemeral containers are supported. | Yes  
[K8sUniqueIngressHost](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8suniqueingresshost) | Requires all Ingress rule hosts to be unique. Does not handle hostname wildcards: https://kubernetes.io/docs/concepts/services-networking/ingress/ | Yes  
[K8sUniqueServiceSelector](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8suniqueserviceselector) | Requires Services to have unique selectors within a namespace. Selectors are considered the same if they have identical keys and values. Selectors may share a key/value pair so long as there is at least one distinct key/value pair between them. https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service | Yes  
[NoUpdateServiceAccount](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#noupdateserviceaccount) | Blocks updating the service account on resources that abstract over Pods. This policy is ignored in audit mode. | No  
[PolicyStrictOnly](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#policystrictonly) | Requires that `STRICT` Istio mutual TLS is always specified when using [PeerAuthentication](https://istio.io/latest/docs/reference/config/security/peer_authentication/). This constraint also ensures that the deprecated [Policy](https://istio.io/v1.4/docs/reference/config/security/istio.authentication.v1alpha1/#Policy) and MeshPolicy resources enforce `STRICT` mutual TLS. See: https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/#lock-down-mutual-tls-for-the-entire-mesh | No  
[RestrictNetworkExclusions](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#restrictnetworkexclusions) | Controls which inbound ports, outbound ports, and outbound IP ranges can be excluded from Istio network capture. Ports and IP ranges that bypass Istio network capture are not handled by the Istio proxy and are not subject to Istio mTLS authentication, authorization policy, and other Istio features. This constraint can be used to apply restrictions to the use of the following annotations:

  * `traffic.sidecar.istio.io/excludeInboundPorts`
  * `traffic.sidecar.istio.io/excludeOutboundPorts`
  * `traffic.sidecar.istio.io/excludeOutboundIPRanges`

See https://istio.io/latest/docs/reference/config/annotations/.  When restricting outbound IP ranges, the constraint calculates whether excluded IP ranges match or are a subset of the allowed IP range exclusions.  When using this constraint all inbound ports, outbound ports and outbound IP ranges must always be included by either setting the corresponding "include" annotations to `"*"` or leaving them unset. Setting any of the following annotations to anything other than `"*"` is not allowed: 

  * `traffic.sidecar.istio.io/includeInboundPorts`
  * `traffic.sidecar.istio.io/includeOutboundPorts`
  * `traffic.sidecar.istio.io/includeOutboundIPRanges`

This constraint always allows port 15020 to be excluded because the Istio sidecar injector always adds it to the `traffic.sidecar.istio.io/excludeInboundPorts` annotation so that it can be used for health checking. | No  
[SourceNotAllAuthz](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#sourcenotallauthz) | Requires that Istio AuthorizationPolicy rules have source principals set to something other than "*". https://istio.io/latest/docs/reference/config/security/authorization-policy/ | No  
[VerifyDeprecatedAPI](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#verifydeprecatedapi) | Verifies deprecated Kubernetes APIs to ensure all the API versions are up to date. This template does not apply to audit as audit looks at the resources which are already present in the cluster with non-deprecated API versions. | No  
  
### AllowedServicePortName

Allowed Service Port Names v1.0.1

Requires that service port names have a prefix from a specified list.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AllowedServicePortName
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # prefixes <array>: Prefixes of allowed service port names.
        prefixes:
          - <string>
    

#### Examples

##### port-name-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AllowedServicePortName
    metadata:
      name: port-name-constraint
    spec:
      enforcementAction: deny
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Service
      parameters:
        prefixes:
        - http-
        - http2-
        - grpc-
        - mongo-
        - redis-
        - tcp-

###### Allowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: helloworld
      name: port-name-http
    spec:
      ports:
      - name: http-helloport
        port: 5000
      selector:
        app: helloworld

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: helloworld
      name: port-name-tcp
    spec:
      ports:
      - name: foo-helloport
        port: 5000
      selector:
        app: helloworld
    
    
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: helloworld
      name: port-name-bad
    spec:
      ports:
      - name: helloport
        port: 5000
      selector:
        app: helloworld

### AsmAuthzPolicyDefaultDeny

ASM AuthorizationPolicy Default Deny v1.0.4

Enforce the mesh level default deny AuthorizationPolicy. Reference to https://istio.io/latest/docs/ops/best-practices/security/#use-default-deny-patterns.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # rootNamespace <string>: Anthos Service Mesh root namespace, default value
        # is "istio-system" if not specified.
        rootNamespace: <string>
        # strictnessLevel <string>: Level of AuthorizationPolicy strictness.
        # Allowed Values: Low, High
        strictnessLevel: <string>
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "security.istio.io"
            version: "v1beta1"
            kind: "AuthorizationPolicy"
    

#### Examples

##### asm-authz-policy-default-deny-with-input-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: asm-authz-policy-default-deny-with-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        rootNamespace: istio-system
        strictnessLevel: High

###### Allowed
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: asm-authz-policy-default-deny-with-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        rootNamespace: istio-system
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: default-deny-no-action
      namespace: istio-system
    spec: null
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: asm-authz-policy-default-deny-with-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        rootNamespace: istio-system
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: default-deny-with-action
      namespace: istio-system
    spec:
      action: ALLOW

###### Disallowed
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: asm-authz-policy-default-deny-with-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        rootNamespace: istio-system
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: not-default-deny
      namespace: istio-system
    spec:
      action: DENY
      rules:
      - to:
        - operation:
            notMethods:
            - GET
            - POST

##### asm-authz-policy-default-deny-no-input-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: asm-authz-policy-default-deny-no-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        strictnessLevel: High

###### Allowed
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: asm-authz-policy-default-deny-no-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: default-deny-no-action
      namespace: istio-system
    spec: null
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: asm-authz-policy-default-deny-no-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: default-deny-with-action
      namespace: istio-system
    spec:
      action: ALLOW

###### Disallowed
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDefaultDeny
    metadata:
      name: asm-authz-policy-default-deny-no-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: not-default-deny
      namespace: istio-system
    spec:
      action: DENY
      rules:
      - to:
        - operation:
            notMethods:
            - GET
            - POST

### AsmAuthzPolicyDisallowedPrefix

ASM AuthorizationPolicy Disallowed Prefixes v1.0.2

Requires that principals and namespaces in Istio `AuthorizationPolicy` rules not have a prefix from a specified list. https://istio.io/latest/docs/reference/config/security/authorization-policy/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDisallowedPrefix
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # disallowedNamespacePrefixes <array>: Disallowed prefixes for namespaces.
        disallowedNamespacePrefixes:
          - <string>
        # disallowedPrincipalPrefixes <array>: Disallowed prefixes for principals.
        disallowedPrincipalPrefixes:
          - <string>
    

#### Examples

##### asm-authz-policy-disallowed-prefix-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyDisallowedPrefix
    metadata:
      name: asm-authz-policy-disallowed-prefix-constraint
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - AuthorizationPolicy
      parameters:
        disallowedNamespacePrefixes:
        - bad-ns-prefix
        - worse-ns-prefix
        disallowedPrincipalPrefixes:
        - bad-principal-prefix
        - worse-principal-prefix

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: valid-authz-policy
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/sleep
        - source:
            namespaces:
            - test
      selector:
        matchLabels:
          app: httpbin

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: bad-source-principal
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/worse-principal-prefix-sleep
        - source:
            namespaces:
            - test
      selector:
        matchLabels:
          app: httpbin
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: bad-source-namespace
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/sleep
        - source:
            namespaces:
            - bad-ns-prefix-test
      selector:
        matchLabels:
          app: httpbin

### AsmAuthzPolicyEnforceSourcePrincipals

ASM AuthorizationPolicy Enforcement Principals v1.0.2

Requires that Istio AuthorizationPolicy "from" field, when defined, has source principles, which must be set to something other than "*". https://istio.io/latest/docs/reference/config/security/authorization-policy/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyEnforceSourcePrincipals
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### asm-authz-policy-enforce-source-principals-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyEnforceSourcePrincipals
    metadata:
      name: asm-authz-policy-enforce-source-principals-constraint
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - AuthorizationPolicy

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: valid-authz-policy
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/sleep
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: no-source-principals
    spec:
      rules:
      - from:
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: source-principals-wildcard
    spec:
      rules:
      - from:
        - source:
            principals:
            - '*'
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: source-principals-contains-wildcard
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/sleep
            - '*'
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin

### AsmAuthzPolicyNormalization

ASM AuthorizationPolicy Normalization v1.0.2

Enforce the AuthorizationPolicy normalization. Reference to https://istio.io/latest/docs/reference/config/security/normalization/.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyNormalization
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### asm-authz-policy-normalization-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicyNormalization
    metadata:
      name: asm-authz-policy-normalization-sample
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - AuthorizationPolicy

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: good-authz-policy
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            methods:
            - GET
            paths:
            - /test/foo
      - when:
        - key: source.ip
          values:
          - 10.1.2.3
          - 10.2.0.0/16
        - key: request.headers[User-Agent]
          values:
          - Mozilla/*
      selector:
        matchLabels:
          app: httpbin

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: bad-method-lowercase
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            methods:
            - get
      selector:
        matchLabels:
          app: httpbin
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: bad-request-header-whitespace
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            methods:
            - GET
      - when:
        - key: source.ip
          values:
          - 10.1.2.3
          - 10.2.0.0/16
        - key: request.headers[User-Ag ent]
          values:
          - Mozilla/*
      selector:
        matchLabels:
          app: httpbin
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: path-unnormalized
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            methods:
            - GET
            paths:
            - /test\/foo
      - when:
        - key: source.ip
          values:
          - 10.1.2.3
          - 10.2.0.0/16
        - key: request.headers[User-Agent]
          values:
          - Mozilla/*
      selector:
        matchLabels:
          app: httpbin

### AsmAuthzPolicySafePattern

ASM AuthorizationPolicy Safe Patterns v1.0.4

Enforce the AuthorizationPolicy safe patterns. Reference to https://istio.io/latest/docs/ops/best-practices/security/#safer-authorization-policy-patterns.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicySafePattern
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # strictnessLevel <string>: Level of AuthorizationPolicy strictness.
        # Allowed Values: Low, High
        strictnessLevel: <string>
    

#### Examples

##### asm-authz-policy-safe-pattern-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmAuthzPolicySafePattern
    metadata:
      name: asm-authz-policy-safe-pattern-sample
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - AuthorizationPolicy
      parameters:
        strictnessLevel: High

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: good-authz-policy-istio-ingress
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            hosts:
            - test.com
            - test.com:*
            methods:
            - GET
      selector:
        matchLabels:
          istio: ingressgateway
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: good-authz-policy-asm-ingress
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            hosts:
            - test.com
            - test.com:*
            methods:
            - GET
      selector:
        matchLabels:
          asm: ingressgateway

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: hosts-on-noningress
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            hosts:
            - test.com
            - test.com:*
            methods:
            - GET
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: invalid-hosts
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            hosts:
            - test.com
            methods:
            - GET
      selector:
        matchLabels:
          istio: ingressgateway
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: allow-negative-match
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            hosts:
            - test.com
            - test.com:*
            notMethods:
            - GET
      selector:
        matchLabels:
          istio: ingressgateway
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: deny-positive-match
    spec:
      action: DENY
      rules:
      - to:
        - operation:
            hosts:
            - test.com
            - test.com:*
            methods:
            - GET
      selector:
        matchLabels:
          istio: ingressgateway

### AsmIngressgatewayLabel

ASM Ingress Gateway Label v1.0.3

Enforce the istio ingressgateway label usage only on ingressgateway pods.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmIngressgatewayLabel
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### asm-ingressgateway-label-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmIngressgatewayLabel
    metadata:
      name: asm-ingressgateway-label-sample
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: sleep
        istio: istio
      name: sleep
    spec:
      containers:
      - image: curlimages/curl
        name: sleep
      - image: gcr.io/gke-release/asm/proxyv2:release
        name: istio-proxy
        ports:
        - containerPort: 15090
          name: http-envoy-prom
          protocol: TCP
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: istio-ingressgateway
        istio: ingressgateway
      name: istio-ingressgateway
    spec:
      containers:
      - image: gcr.io/gke-release/asm/proxyv2:release
        name: istio-proxy
        ports:
        - containerPort: 15090
          name: http-envoy-prom
          protocol: TCP
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: asm-ingressgateway
        asm: ingressgateway
      name: asm-ingressgateway
    spec:
      containers:
      - image: gcr.io/gke-release/asm/proxyv2:release
        name: istio-proxy
        ports:
        - containerPort: 15090
          name: http-envoy-prom
          protocol: TCP

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: sleep
        istio: ingressgateway
      name: sleep
    spec:
      containers:
      - image: curlimages/curl
        name: sleep
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: sleep
        asm: ingressgateway
      name: sleep
    spec:
      containers:
      - image: curlimages/curl
        name: sleep
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: sleep
        istio: ingressgateway
      name: sleep
    spec:
      containers:
      - image: curlimages/curl
        name: sleep
      - image: gcr.io/gke-release/asm/proxyv2:release
        name: istio-proxy
        ports:
        - containerPort: 15090
          name: http-envoy-prom
          protocol: TCP

### AsmPeerAuthnMeshStrictMtls

ASM Peer Authentication Mesh Strict mTLS v1.0.4

Enforce the mesh level strict mtls PeerAuthentication. Reference to https://istio.io/latest/docs/ops/best-practices/security/#mutual-tls.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnMeshStrictMtls
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # rootNamespace <string>: Anthos Service Mesh root namespace, default value
        # is "istio-system" if not specified.
        rootNamespace: <string>
        # strictnessLevel <string>: Level of PeerAuthentication strictness.
        # Allowed Values: Low, High
        strictnessLevel: <string>
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "security.istio.io"
            version: "v1beta1"
            kind: "PeerAuthentication"
    

#### Examples

##### asm-peer-authn-mesh-strict-mtls-with-input-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnMeshStrictMtls
    metadata:
      name: asm-peer-authn-mesh-strict-mtls-with-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        rootNamespace: asm-root
        strictnessLevel: High

###### Allowed
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnMeshStrictMtls
    metadata:
      name: asm-peer-authn-mesh-strict-mtls-with-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        rootNamespace: asm-root
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mesh-strict-mtls
      namespace: asm-root
    spec:
      mtls:
        mode: STRICT

###### Disallowed
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnMeshStrictMtls
    metadata:
      name: asm-peer-authn-mesh-strict-mtls-with-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        rootNamespace: asm-root
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mesh-permissive-mtls
      namespace: asm-root
    spec:
      mtls:
        mode: PERMISSIVE

##### asm-peer-authn-mesh-strict-mtls-no-input-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnMeshStrictMtls
    metadata:
      name: asm-peer-authn-mesh-strict-mtls-no-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        strictnessLevel: High

###### Allowed
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnMeshStrictMtls
    metadata:
      name: asm-peer-authn-mesh-strict-mtls-no-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mesh-strict-mtls
      namespace: istio-system
    spec:
      mtls:
        mode: STRICT

###### Disallowed
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnMeshStrictMtls
    metadata:
      name: asm-peer-authn-mesh-strict-mtls-no-input-constraint
    spec:
      enforcementAction: dryrun
      parameters:
        strictnessLevel: High
    ---
    # Referential Data
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mesh-permissive-mtls
      namespace: istio-system
    spec:
      mtls:
        mode: PERMISSIVE

### AsmPeerAuthnStrictMtls

ASM Peer Authentication Strict mTLS v1.0.3

Enforce all PeerAuthentications cannot overwrite strict mtls. Reference to https://istio.io/latest/docs/ops/best-practices/security/#mutual-tls.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnStrictMtls
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # strictnessLevel <string>: Level of PeerAuthentication strictness.
        # Allowed Values: Low, High
        strictnessLevel: <string>
    

#### Examples

##### asm-peer-authn-strict-mtls-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmPeerAuthnStrictMtls
    metadata:
      name: asm-peer-authn-strict-mtls-constraint
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - PeerAuthentication
      parameters:
        strictnessLevel: High

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: valid-strict-mtls-pa
      namespace: foo
    spec:
      mtls:
        mode: UNSET
      portLevelMtls:
        "80":
          mode: UNSET
        "443":
          mode: STRICT
      selector:
        matchLabels:
          app: bar

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: invalid-permissive-mtls-pa
      namespace: foo
    spec:
      mtls:
        mode: PERMISSIVE
      portLevelMtls:
        "80":
          mode: UNSET
        "443":
          mode: STRICT
      selector:
        matchLabels:
          app: bar
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: invalid-port-disable-mtls-pa
      namespace: foo
    spec:
      mtls:
        mode: UNSET
      portLevelMtls:
        "80":
          mode: DISABLE
        "443":
          mode: STRICT
      selector:
        matchLabels:
          app: bar

### AsmRequestAuthnProhibitedOutputHeaders

ASM RequestAuthentication Prohibited Output Headers v1.0.2

In RequestAuthentication, enforce the `jwtRules.outPayloadToHeader` field to not contain well known HTTP request headers or custom prohibited headers. Reference to https://istio.io/latest/docs/reference/config/security/jwt/#JWTRule.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmRequestAuthnProhibitedOutputHeaders
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # prohibitedHeaders <array>: User predefined prohibited headers.
        prohibitedHeaders:
          - <string>
    

#### Examples

##### asm-request-authn-prohibited-output-headers-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmRequestAuthnProhibitedOutputHeaders
    metadata:
      name: asm-request-authn-prohibited-output-headers-constraint
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - RequestAuthentication
      parameters:
        prohibitedHeaders:
        - Bad-Header
        - X-Bad-Header

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: RequestAuthentication
    metadata:
      name: valid-request-authn
      namespace: istio-system
    spec:
      jwtRules:
      - issuer: example.com
        outputPayloadToHeader: Good-Header
      selector:
        matchLabels:
          app: istio-ingressgateway

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: RequestAuthentication
    metadata:
      name: deny-predefined-output-header
      namespace: istio-system
    spec:
      jwtRules:
      - issuer: example.com
        outputPayloadToHeader: Host
      selector:
        matchLabels:
          app: istio-ingressgateway
    
    
    apiVersion: security.istio.io/v1beta1
    kind: RequestAuthentication
    metadata:
      name: deny-predefined-output-header
      namespace: istio-system
    spec:
      jwtRules:
      - issuer: example.com
        outputPayloadToHeader: X-Bad-Header
      selector:
        matchLabels:
          app: istio-ingressgateway

### AsmSidecarInjection

ASM Sidecar Injection v1.0.2

Enforce the istio proxy sidecar always been injected to workload pods.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmSidecarInjection
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # strictnessLevel <string>: Level of sidecar injection strictness.
        # Allowed Values: Low, High
        strictnessLevel: <string>
    

#### Examples

##### asm-sidecar-injection-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: AsmSidecarInjection
    metadata:
      name: asm-sidecar-injection-sample
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        strictnessLevel: High

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        sidecar.istio.io/inject: "true"
      name: sleep
    spec:
      containers:
      - image: curlimages/curl
        name: sleep
      - image: gcr.io/gke-release/asm/proxyv2:release
        name: istio-proxy
        ports:
        - containerPort: 15090
          name: http-envoy-prom
          protocol: TCP
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        "false": "false"
      name: sleep
    spec:
      containers:
      - image: curlimages/curl
        name: sleep
      - image: gcr.io/gke-release/asm/proxyv2:release
        name: istio-proxy
        ports:
        - containerPort: 15090
          name: http-envoy-prom
          protocol: TCP

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        sidecar.istio.io/inject: "false"
      name: sleep
    spec:
      containers:
      - image: curlimages/curl
        name: sleep

### DestinationRuleTLSEnabled

Destination Rule TLS Enabled v1.0.1

Prohibits disabling TLS for all hosts and host subsets in Istio DestinationRules.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: DestinationRuleTLSEnabled
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### dr-tls-enabled

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: DestinationRuleTLSEnabled
    metadata:
      name: dr-tls-enabled
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - networking.istio.io
          kinds:
          - DestinationRule

###### Disallowed
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: DestinationRule
    metadata:
      name: dr-subset-tls-disable
      namespace: default
    spec:
      host: myservice
      subsets:
      - name: v1
        trafficPolicy:
          tls:
            mode: DISABLE
      - name: v2
        trafficPolicy:
          tls:
            mode: SIMPLE
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: DestinationRule
    metadata:
      name: dr-traffic-tls-disable
      namespace: default
    spec:
      host: myservice
      trafficPolicy:
        tls:
          mode: DISABLE

### DisallowedAuthzPrefix

Disallow Istio AuthorizationPolicy Prefixes v1.0.2

Requires that principals and namespaces in Istio `AuthorizationPolicy` rules not have a prefix from a specified list. https://istio.io/latest/docs/reference/config/security/authorization-policy/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: DisallowedAuthzPrefix
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # disallowedprefixes <array>: Disallowed prefixes of principals and
        # namespaces.
        disallowedprefixes:
          - <string>
    

#### Examples

##### disallowed-authz-prefix-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: DisallowedAuthzPrefix
    metadata:
      name: disallowed-authz-prefix-constraint
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - AuthorizationPolicy
      parameters:
        disallowedprefixes:
        - badprefix
        - reallybadprefix

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: good
      namespace: foo
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/sleep
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
          version: v1

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: bad-source-principal
      namespace: foo
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/badprefix-sleep
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
          version: v1
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: bad-source-namespace
      namespace: foo
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/sleep
        - source:
            namespaces:
            - badprefix-test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
          version: v1

### GCPStorageLocationConstraintV1

GCP Storage Location Constraint v1.0.3

Restricts the permitted `locations` for StorageBucket Config Connector resources to the list of locations provided in the constraint. Bucket names in the `exemptions` list are exempt.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GCPStorageLocationConstraintV1
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptions <array>: A list of bucket names that are exempt from this
        # constraint.
        exemptions:
          - <string>
        # locations <array>: A list of locations that a bucket is permitted to
        # have.
        locations:
          - <string>
    

#### Examples

##### singapore-and-jakarta-only

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GCPStorageLocationConstraintV1
    metadata:
      name: singapore-and-jakarta-only
    spec:
      enforcementAction: deny
      match:
        kinds:
        - apiGroups:
          - storage.cnrm.cloud.google.com
          kinds:
          - StorageBucket
      parameters:
        exemptions:
        - my_project_id_cloudbuild
        locations:
        - asia-southeast1
        - asia-southeast2

###### Allowed
    
    
    apiVersion: storage.cnrm.cloud.google.com/v1beta1
    kind: StorageBucket
    metadata:
      name: bucket-in-permitted-location
    spec:
      location: asia-southeast1

###### Disallowed
    
    
    apiVersion: storage.cnrm.cloud.google.com/v1beta1
    kind: StorageBucket
    metadata:
      name: bucket-in-disallowed-location
    spec:
      location: us-central1
    
    
    apiVersion: storage.cnrm.cloud.google.com/v1beta1
    kind: StorageBucket
    metadata:
      name: bucket-without-specific-location
    spec: null

### GkeSpotVMTerminationGrace

Restricts terminationGracePeriodSeconds for GKE Spot VMs v1.1.3

Requires Pods and Pod Templates with `nodeSelector` or `nodeAfffinty` of `gke-spot` to have a `terminationGracePeriodSeconds` of 15s or less.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GkeSpotVMTerminationGrace
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # includePodOnSpotNodes <boolean>: Require `terminationGracePeriodSeconds`
        # of 15s or less for all `Pod` on a `gke-spot` Node.
        includePodOnSpotNodes: <boolean>
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: ""
            version: "v1"
            kind: "Node"
    

#### Examples

##### spotvm-termination-grace

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GkeSpotVMTerminationGrace
    metadata:
      name: spotvm-termination-grace
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        includePodOnSpotNodes: true

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
      nodeSelector:
        cloud.google.com/gke-spot: "true"
      terminationGracePeriodSeconds: 15
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
      nodeSelector:
        cloud.google.com/gke-spot: "true"
      terminationGracePeriodSeconds: 15
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-with-termGrace
    spec:
      Nodename: default
      containers:
      - image: nginx
        name: nginx
      terminationGracePeriodSeconds: 15
    ---
    # Referential Data
    apiVersion: v1
    kind: Node
    metadata:
      labels:
        cloud.google.com/gke-spot: "true"
      name: default
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-with-termGrace
    spec:
      Nodename: default
      containers:
      - image: nginx
        name: nginx
      terminationGracePeriodSeconds: 15
    ---
    # Referential Data
    apiVersion: v1
    kind: Node
    metadata:
      name: default
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-without-termGrace
    spec:
      Nodename: default
      containers:
      - image: nginx
        name: nginx
    ---
    # Referential Data
    apiVersion: v1
    kind: Node
    metadata:
      name: default

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-disallowed
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: cloud.google.com/gke-spot
                operator: In
                values:
                - "true"
      containers:
      - image: nginx
        name: nginx
      terminationGracePeriodSeconds: 30
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-disallowed
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: cloud.google.com/gke-spot
                operator: In
                values:
                - "true"
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
      nodeSelector:
        cloud.google.com/gke-spot: "true"
      terminationGracePeriodSeconds: 30
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-disallowed
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: cloud.google.com/gke-spot
                operator: In
                values:
                - "true"
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: example-without-termGrace
    spec:
      Nodename: default
      containers:
      - image: nginx
        name: nginx
    ---
    # Referential Data
    apiVersion: v1
    kind: Node
    metadata:
      labels:
        cloud.google.com/gke-spot: "true"
      name: default

### K8sAllowedRepos

Allowed Repositories v1.0.1

Requires container images to begin with a string from the specified list.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sAllowedRepos
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # repos <array>: The list of prefixes a container image is allowed to have.
        repos:
          - <string>
    

#### Examples

##### repo-is-openpolicyagent

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sAllowedRepos
    metadata:
      name: repo-is-openpolicyagent
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
        namespaces:
        - default
      parameters:
        repos:
        - openpolicyagent/

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 30Mi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
      initContainers:
      - image: nginx
        name: nginxinit
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
      initContainers:
      - image: nginx
        name: nginxinit
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
      ephemeralContainers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
      initContainers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 100m
            memory: 30Mi

### K8sAvoidUseOfSystemMastersGroup

Disallow the use of 'system:masters' group v1.0.0

Disallows the use of 'system:masters' group. Has no effect during audit.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sAvoidUseOfSystemMastersGroup
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowlistedUsernames <array>: allowlistedUsernames is the list of
        # usernames that are allowed to use system:masters group.
        allowlistedUsernames:
          - <string>
    

#### Examples

##### avoid-use-of-system-masters-group

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sAvoidUseOfSystemMastersGroup
    metadata:
      name: avoid-use-of-system-masters-group

###### Allowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: example-namespace

### K8sBlockAllIngress

Block all Ingress v1.0.4

Disallows the creation of Ingress objects (`Ingress`, `Gateway`, and `Service` types of `NodePort` and `LoadBalancer`).

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockAllIngress
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowList <array>: A list of regular expressions for the Ingress object
        # names that are exempt from the constraint.
        allowList:
          - <string>
    

#### Examples

##### block-all-ingress

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockAllIngress
    metadata:
      name: block-all-ingress
    spec:
      enforcementAction: dryrun
      parameters:
        allowList:
        - name1
        - name2
        - name3
        - my-*

###### Allowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
    spec:
      ports:
      - port: 80
        protocol: TCP
        targetPort: 9376
      selector:
        app.kubernetes.io/name: MyApp
      type: LoadBalancer
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: allowed-clusterip-service-example
    spec:
      ports:
      - port: 80
        protocol: TCP
        targetPort: 9376
      selector:
        app.kubernetes.io/name: MyApp
      type: ClusterIP

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: disallowed-service-example
    spec:
      ports:
      - port: 80
        protocol: TCP
        targetPort: 9376
      selector:
        app.kubernetes.io/name: MyApp
      type: LoadBalancer
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: disallowed-service-example
    spec:
      ports:
      - port: 80
        protocol: TCP
        targetPort: 9376
      selector:
        app.kubernetes.io/name: MyApp
      type: LoadBalancer
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: Gateway
    metadata:
      name: disallowed-gateway-example
    spec:
      gatewayClassName: istio
      listeners:
      - allowedRoutes:
          namespaces:
            from: All
        hostname: '*.example.com'
        name: default
        port: 80
        protocol: HTTP

### K8sBlockCreationWithDefaultServiceAccount

Block Creation with Default Service Account v1.0.2

Disallows the creation of resources using a default service account. Has no effect during audit.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockCreationWithDefaultServiceAccount
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### block-creation-with-default-serviceaccount

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockCreationWithDefaultServiceAccount
    metadata:
      name: block-creation-with-default-serviceaccount
    spec:
      enforcementAction: dryrun

###### Allowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: example-namespace

### K8sBlockEndpointEditDefaultRole

Block Endpoint Edit Default Role v1.0.0

Many Kubernetes installations by default have a system:aggregate-to-edit ClusterRole which does not properly restrict access to editing Endpoints. This ConstraintTemplate forbids the system:aggregate-to-edit ClusterRole from granting permission to create/patch/update Endpoints. ClusterRole/system:aggregate-to-edit should not allow Endpoint edit permissions due to CVE-2021-25740, Endpoint & EndpointSlice permissions allow cross-Namespace forwarding, https://github.com/kubernetes/kubernetes/issues/103675

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockEndpointEditDefaultRole
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### block-endpoint-edit-default-role

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockEndpointEditDefaultRole
    metadata:
      name: block-endpoint-edit-default-role
    spec:
      match:
        kinds:
        - apiGroups:
          - rbac.authorization.k8s.io
          kinds:
          - ClusterRole

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        rbac.authorization.kubernetes.io/autoupdate: "true"
      labels:
        kubernetes.io/bootstrapping: rbac-defaults
        rbac.authorization.k8s.io/aggregate-to-edit: "true"
      name: system:aggregate-to-edit
    rules:
    - apiGroups:
      - ""
      resources:
      - pods/attach
      - pods/exec
      - pods/portforward
      - pods/proxy
      - secrets
      - services/proxy
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - ""
      resources:
      - serviceaccounts
      verbs:
      - impersonate
    - apiGroups:
      - ""
      resources:
      - pods
      - pods/attach
      - pods/exec
      - pods/portforward
      - pods/proxy
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - ""
      resources:
      - configmaps
      - persistentvolumeclaims
      - replicationcontrollers
      - replicationcontrollers/scale
      - secrets
      - serviceaccounts
      - services
      - services/proxy
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - apps
      resources:
      - daemonsets
      - deployments
      - deployments/rollback
      - deployments/scale
      - replicasets
      - replicasets/scale
      - statefulsets
      - statefulsets/scale
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - autoscaling
      resources:
      - horizontalpodautoscalers
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - batch
      resources:
      - cronjobs
      - jobs
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - extensions
      resources:
      - daemonsets
      - deployments
      - deployments/rollback
      - deployments/scale
      - ingresses
      - networkpolicies
      - replicasets
      - replicasets/scale
      - replicationcontrollers/scale
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - policy
      resources:
      - poddisruptionbudgets
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - networking.k8s.io
      resources:
      - ingresses
      - networkpolicies
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        rbac.authorization.kubernetes.io/autoupdate: "true"
      labels:
        kubernetes.io/bootstrapping: rbac-defaults
        rbac.authorization.k8s.io/aggregate-to-edit: "true"
      name: system:aggregate-to-edit
    rules:
    - apiGroups:
      - ""
      resources:
      - pods/attach
      - pods/exec
      - pods/portforward
      - pods/proxy
      - secrets
      - services/proxy
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - ""
      resources:
      - serviceaccounts
      verbs:
      - impersonate
    - apiGroups:
      - ""
      resources:
      - pods
      - pods/attach
      - pods/exec
      - pods/portforward
      - pods/proxy
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - ""
      resources:
      - configmaps
      - persistentvolumeclaims
      - replicationcontrollers
      - replicationcontrollers/scale
      - secrets
      - serviceaccounts
      - services
      - services/proxy
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update
    - apiGroups:
      - apps
      resources:
      - daemonsets
      - deployments
      - deployments/rollback
      - deployments/scale
      - endpoints
      - replicasets
      - replicasets/scale
      - statefulsets
      - statefulsets/scale
      verbs:
      - create
      - delete
      - deletecollection
      - patch
      - update

### K8sBlockLoadBalancer

Block Services with type LoadBalancer v1.0.0

Disallows all Services with type LoadBalancer. https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockLoadBalancer
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### block-load-balancer

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockLoadBalancer
    metadata:
      name: block-load-balancer
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Service

###### Allowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service-allowed
    spec:
      ports:
      - port: 80
        targetPort: 80
      type: ClusterIP

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service-disallowed
    spec:
      ports:
      - nodePort: 30007
        port: 80
        targetPort: 80
      type: LoadBalancer

### K8sBlockNodePort

Block NodePort v1.0.0

Disallows all Services with type NodePort. https://kubernetes.io/docs/concepts/services-networking/service/#nodeport

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockNodePort
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### block-node-port

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockNodePort
    metadata:
      name: block-node-port
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Service

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service-disallowed
    spec:
      ports:
      - nodePort: 30007
        port: 80
        targetPort: 80
      type: NodePort

### K8sBlockObjectsOfType

Block Objects of Type v1.0.1

Disallows object of forbidden types.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockObjectsOfType
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        forbiddenTypes:
          - <string>
    

#### Examples

##### block-secrets-of-type-basic-auth

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockObjectsOfType
    metadata:
      name: block-secrets-of-type-basic-auth
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Secret
      parameters:
        forbiddenTypes:
        - kubernetes.io/basic-auth

###### Allowed
    
    
    apiVersion: v1
    data:
      password: ZHVtbXlwYXNz
      username: ZHVtbXl1c2Vy
    kind: Secret
    metadata:
      name: credentials
      namespace: default
    type: Opaque

###### Disallowed
    
    
    apiVersion: v1
    data:
      password: YmFzaWMtcGFzc3dvcmQ=
      username: YmFzaWMtdXNlcm5hbWU=
    kind: Secret
    metadata:
      name: secret-basic-auth
      namespace: default
    type: kubernetes.io/basic-auth

### K8sBlockProcessNamespaceSharing

Block Process Namespace Sharing v1.0.1

Prohibits Pod specs with `shareProcessNamespace` set to `true`. This avoids scenarios where all containers in a Pod share a PID namespace and can access each other's filesystem and memory.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockProcessNamespaceSharing
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### block-process-namespace-sharing

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockProcessNamespaceSharing
    metadata:
      name: block-process-namespace-sharing

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: good-pod
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: bad-pod
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
      shareProcessNamespace: true

### K8sBlockWildcardIngress

Block Wildcard Ingress v1.0.1

Users should not be able to create Ingresses with a blank or wildcard (*) hostname since that would enable them to intercept traffic for other services in the cluster, even if they don't have access to those services.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockWildcardIngress
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### block-wildcard-ingress

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sBlockWildcardIngress
    metadata:
      name: block-wildcard-ingress
    spec:
      match:
        kinds:
        - apiGroups:
          - extensions
          - networking.k8s.io
          kinds:
          - Ingress

###### Allowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: non-wildcard-ingress
    spec:
      rules:
      - host: myservice.example.com
        http:
          paths:
          - backend:
              service:
                name: example
                port:
                  number: 80
            path: /
            pathType: Prefix

###### Disallowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: wildcard-ingress
    spec:
      rules:
      - host: ""
        http:
          paths:
          - backend:
              service:
                name: example
                port:
                  number: 80
            path: /
            pathType: Prefix
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: wildcard-ingress
    spec:
      rules:
      - http:
          paths:
          - backend:
              service:
                name: example
                port:
                  number: 80
            path: /
            pathType: Prefix
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: wildcard-ingress
    spec:
      rules:
      - host: '*.example.com'
        http:
          paths:
          - backend:
              service:
                name: example
                port:
                  number: 80
            path: /
            pathType: Prefix
      - host: valid.example.com
        http:
          paths:
          - backend:
              service:
                name: example
                port:
                  number: 80
            path: /
            pathType: Prefix

### K8sContainerEphemeralStorageLimit

Container ephemeral storage limit v1.0.2

Requires containers to have an ephemeral storage limit set and constrains the limit to be within the specified maximum values. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerEphemeralStorageLimit
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # ephemeral-storage <string>: The maximum allowed ephemeral storage limit
        # on a Pod, exclusive.
        ephemeral-storage: <string>
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### container-ephemeral-storage-limit

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerEphemeralStorageLimit
    metadata:
      name: container-ephemeral-storage-limit
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        ephemeral-storage: 500Mi

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            ephemeral-storage: 100Mi
            memory: 1Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            ephemeral-storage: 100Mi
            memory: 1Gi
      initContainers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: init-opa
        resources:
          limits:
            cpu: 100m
            ephemeral-storage: 100Mi
            memory: 1Gi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 2Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            ephemeral-storage: 1Pi
            memory: 1Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            ephemeral-storage: 100Mi
            memory: 1Gi
      initContainers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: init-opa
        resources:
          limits:
            cpu: 100m
            ephemeral-storage: 1Pi
            memory: 1Gi

### K8sContainerLimits

Container Limits v1.0.1

Requires containers to have memory and CPU limits set and constrains limits to be within the specified maximum values. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerLimits
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # cpu <string>: The maximum allowed cpu limit on a Pod, exclusive.
        cpu: <string>
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # memory <string>: The maximum allowed memory limit on a Pod, exclusive.
        memory: <string>
    

#### Examples

##### container-must-have-limits

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerLimits
    metadata:
      name: container-must-have-limits
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        cpu: 200m
        memory: 1Gi

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 1Gi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 2Gi

### K8sContainerRatios

Container Ratios v1.0.1

Sets a maximum ratio for container resource limits to requests. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerRatios
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # cpuRatio <string>: The maximum allowed ratio of `resources.limits.cpu` to
        # `resources.requests.cpu` on a container. If not specified, equal to
        # `ratio`.
        cpuRatio: <string>
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # ratio <string>: The maximum allowed ratio of `resources.limits` to
        # `resources.requests` on a container.
        ratio: <string>
    

#### Examples

##### container-must-meet-ratio

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerRatios
    metadata:
      name: container-must-meet-ratio
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        ratio: "2"

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 200m
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 100Mi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 800m
            memory: 2Gi
          requests:
            cpu: 100m
            memory: 100Mi

##### container-must-meet-memory-and-cpu-ratio

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerRatios
    metadata:
      name: container-must-meet-memory-and-cpu-ratio
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        cpuRatio: "10"
        ratio: "1"

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: "4"
            memory: 2Gi
          requests:
            cpu: "1"
            memory: 2Gi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: "4"
            memory: 2Gi
          requests:
            cpu: 100m
            memory: 2Gi

### K8sContainerRequests

Container Requests v1.0.1

Requires containers to have memory and CPU requests set and constrains requests to be within the specified maximum values. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerRequests
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # cpu <string>: The maximum allowed cpu request on a Pod, exclusive.
        cpu: <string>
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # memory <string>: The maximum allowed memory request on a Pod, exclusive.
        memory: <string>
    

#### Examples

##### container-must-have-requests

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sContainerRequests
    metadata:
      name: container-must-have-requests
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        cpu: 200m
        memory: 1Gi

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          requests:
            cpu: 100m
            memory: 1Gi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          requests:
            cpu: 100m
            memory: 2Gi

### K8sCronJobAllowedRepos

CronJob Allowed Repositories v1.0.1

Requires container images of CronJobs to begin with a string from the specified list.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sCronJobAllowedRepos
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # repos <array>: The list of prefixes a container image is allowed to have.
        repos:
          - <string>
    

#### Examples

##### cronjob-restrict-repos

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sCronJobAllowedRepos
    metadata:
      name: cronjob-restrict-repos
    spec:
      match:
        kinds:
        - apiGroups:
          - batch
          kinds:
          - CronJob
      parameters:
        repos:
        - gke.gcr.io/

###### Allowed
    
    
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: hello
    spec:
      jobTemplate:
        spec:
          template:
            spec:
              containers:
              - image: gke.gcr.io/busybox:1.28
                name: hello
      schedule: '* * * * *'

###### Disallowed
    
    
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: hello
    spec:
      jobTemplate:
        spec:
          template:
            spec:
              containers:
              - image: busybox:1.28
                name: hello
      schedule: '* * * * *'

### K8sDisallowAnonymous

Disallow Anonymous Access v1.0.0

Disallows associating ClusterRole and Role resources to the system:anonymous user and system:unauthenticated group.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowAnonymous
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedRoles <array>: The list of ClusterRoles and Roles that may be
        # associated with the `system:unauthenticated` group and `system:anonymous`
        # user.
        allowedRoles:
          - <string>
    

#### Examples

##### no-anonymous

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowAnonymous
    metadata:
      name: no-anonymous
    spec:
      match:
        kinds:
        - apiGroups:
          - rbac.authorization.k8s.io
          kinds:
          - ClusterRoleBinding
        - apiGroups:
          - rbac.authorization.k8s.io
          kinds:
          - RoleBinding
      parameters:
        allowedRoles:
        - cluster-role-1

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: cluster-role-binding-1
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-role-1
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:authenticated
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:unauthenticated

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: cluster-role-binding-2
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-role-2
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:authenticated
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:unauthenticated

### K8sDisallowInteractiveTTY

Disallow Interactive TTY Containers v1.0.0

Requires that objects have the fields `spec.tty` and `spec.stdin` set to false or unset.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowInteractiveTTY
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### no-interactive-tty-containers

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowInteractiveTTY
    metadata:
      name: no-interactive-tty-containers
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-interactive-tty
      name: nginx-interactive-tty-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        stdin: false
        tty: false

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-privilege-escalation
      name: nginx-privilege-escalation-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        stdin: true
        tty: true

### K8sDisallowedRepos

Disallowed Repositories v1.0.0

Disallowed container repositories that begin with a string from the specified list.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowedRepos
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # repos <array>: The list of prefixes a container image is not allowed to
        # have.
        repos:
          - <string>
    

#### Examples

##### repo-must-not-be-k8s-gcr-io

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowedRepos
    metadata:
      name: repo-must-not-be-k8s-gcr-io
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        repos:
        - k8s.gcr.io/

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: kustomize-allowed
    spec:
      containers:
      - image: registry.k8s.io/kustomize/kustomize:v3.8.9
        name: kustomize

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: kustomize-disallowed
    spec:
      containers:
      - image: k8s.gcr.io/kustomize/kustomize:v3.8.9
        name: kustomize
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: kustomize-disallowed
    spec:
      containers:
      - image: registry.k8s.io/kustomize/kustomize:v3.8.9
        name: kustomize
      initContainers:
      - image: k8s.gcr.io/kustomize/kustomize:v3.8.9
        name: kustomizeinit
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: kustomize-disallowed
    spec:
      containers:
      - image: k8s.gcr.io/kustomize/kustomize:v3.8.9
        name: kustomize
      initContainers:
      - image: k8s.gcr.io/kustomize/kustomize:v3.8.9
        name: kustomizeinit
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: kustomize-disallowed
    spec:
      containers:
      - image: k8s.gcr.io/kustomize/kustomize:v3.8.9
        name: kustomize
      ephemeralContainers:
      - image: k8s.gcr.io/kustomize/kustomize:v3.8.9
        name: kustomize
      initContainers:
      - image: k8s.gcr.io/kustomize/kustomize:v3.8.9
        name: kustomize

### K8sDisallowedRoleBindingSubjects

Disallowed Rolebinding Subjects v1.0.1

Prohibits RoleBindings or ClusterRoleBindings with subjects matching any `disallowedSubjects` passed as parameters.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowedRoleBindingSubjects
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # disallowedSubjects <array>: A list of subjects that cannot appear in a
        # RoleBinding.
        disallowedSubjects:
          - # apiGroup <string>: The Kubernetes API group of the disallowed role
            # binding subject. Currently ignored.
            apiGroup: <string>
            # kind <string>: The kind of the disallowed role binding subject.
            kind: <string>
            # name <string>: The name of the disallowed role binding subject.
            name: <string>
    

#### Examples

##### disallowed-rolebinding-subjects

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowedRoleBindingSubjects
    metadata:
      name: disallowed-rolebinding-subjects
    spec:
      parameters:
        disallowedSubjects:
        - apiGroup: rbac.authorization.k8s.io
          kind: Group
          name: system:unauthenticated

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: good-clusterrolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: my-role
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:authenticated

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: bad-clusterrolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: my-role
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:unauthenticated

### K8sDisallowedTags

Disallow tags v1.0.1

Requires container images to have an image tag different from the ones in the specified list. https://kubernetes.io/docs/concepts/containers/images/#image-names

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowedTags
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # tags <array>: Disallowed container image tags.
        tags:
          - <string>
    

#### Examples

##### container-image-must-not-have-latest-tag

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDisallowedTags
    metadata:
      name: container-image-must-not-have-latest-tag
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
        namespaces:
        - default
      parameters:
        exemptImages:
        - openpolicyagent/opa-exp:latest
        - openpolicyagent/opa-exp2:latest
        tags:
        - latest

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-exempt-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa-exp:latest
        name: opa-exp
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/init:v1
        name: opa-init
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa-exp2:latest
        name: opa-exp2

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa
        name: opa
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-disallowed-2
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:latest
        name: opa
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-disallowed-ephemeral
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
      ephemeralContainers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:latest
        name: opa
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-disallowed-3
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa-exp:latest
        name: opa
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/init:latest
        name: opa-init
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa-exp2:latest
        name: opa-exp2
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/monitor:latest
        name: opa-monitor

### K8sEmptyDirHasSizeLimit

Empty Directory has Size Limit v1.0.5

Requires that any `emptyDir` volumes specify a `sizeLimit`. Optionally, a `maxSizeLimit` parameter can be supplied in the constraint to specify a maximum allowable size limit.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sEmptyDirHasSizeLimit
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptVolumesRegex <array>: Exempt Volume names as regex match.
        exemptVolumesRegex:
          - <string>
        # maxSizeLimit <string>: When set, the declared size limit for each volume
        # must be less than `maxSizeLimit`.
        maxSizeLimit: <string>
    

#### Examples

##### empty-dir-has-size-limit

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sEmptyDirHasSizeLimit
    metadata:
      name: empty-dir-has-size-limit
    spec:
      match:
        excludedNamespaces:
        - istio-system
        - kube-system
        - gatekeeper-system
      parameters:
        exemptVolumesRegex:
        - ^istio-[a-z]+$
        maxSizeLimit: 4Gi

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: good-pod
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
      volumes:
      - emptyDir:
          sizeLimit: 2Gi
        name: good-pod-volume
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: exempt-pod
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
      volumes:
      - emptyDir: {}
        name: istio-envoy

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: bad-pod
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
      volumes:
      - emptyDir: {}
        name: bad-pod-volume

### K8sEnforceCloudArmorBackendConfig

Enforce Cloud Armor on BackendConfig Resources v1.0.2

Enforces Cloud Armor configuration on BackendConfig resources

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sEnforceCloudArmorBackendConfig
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### enforce-cloudarmor-backendconfig

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sEnforceCloudArmorBackendConfig
    metadata:
      name: enforce-cloudarmor-backendconfig
    spec:
      enforcementAction: dryrun

###### Allowed
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: my-backendconfig
      namespace: examplenamespace
    spec:
      securityPolicy:
        name: example-security-policy
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: second-backendconfig
    spec:
      securityPolicy:
        name: my-security-policy

###### Disallowed
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: my-backendconfig
      namespace: examplenamespace
    spec:
      securityPolicy:
        name: null
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: my-backendconfig
      namespace: examplenamespace
    spec:
      securityPolicy:
        name: ""
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: my-backendconfig
    spec:
      logging:
        enable: true
        sampleRate: 0.5

### K8sEnforceConfigManagement

Enforce Config Management v1.1.6

Requires the presence and operation of Config Management. Constraints using this `ConstraintTemplate` will be audit only regardless of `enforcementAction` value.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sEnforceConfigManagement
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # requireDriftPrevention <boolean>: Require Config Sync drift prevention to
        # prevent config drift.
        requireDriftPrevention: <boolean>
        # requireRootSync <boolean>: Require a Config Sync `RootSync` object for
        # cluster config management.
        requireRootSync: <boolean>
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "configsync.gke.io"
            version: "v1beta1"
            kind: "RootSync"
    

#### Examples

##### enforce-config-management

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sEnforceConfigManagement
    metadata:
      name: enforce-config-management
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - configmanagement.gke.io
          kinds:
          - ConfigManagement

###### Allowed
    
    
    apiVersion: configmanagement.gke.io/v1
    kind: ConfigManagement
    metadata:
      annotations:
        configmanagement.gke.io/managed-by-hub: "true"
        configmanagement.gke.io/update-time: "1663586155"
      name: config-management
    spec:
      binauthz:
        enabled: true
      clusterName: tec6ea817b5b4bb2-cluster
      enableMultiRepo: true
      git:
        proxy: {}
        syncRepo: git@test-git-server.config-management-system-test:/git-server/repos/sot.git
      hierarchyController: {}
      policyController:
        auditIntervalSeconds: 60
        enabled: true
        monitoring:
          backends:
          - prometheus
          - cloudmonitoring
        mutation: {}
        referentialRulesEnabled: true
        templateLibraryInstalled: true
    status:
      configManagementVersion: v1.12.2-rc.2
      healthy: true

###### Disallowed
    
    
    apiVersion: configmanagement.gke.io/v1
    kind: ConfigManagement
    metadata:
      annotations:
        configmanagement.gke.io/managed-by-hub: "true"
        configmanagement.gke.io/update-time: "1663586155"
      name: config-management
    spec:
      binauthz:
        enabled: true
      clusterName: tec6ea817b5b4bb2-cluster
      enableMultiRepo: true
      git:
        syncRepo: git@test-git-server.config-management-system-test:/git-server/repos/sot.git
      hierarchyController: {}
      policyController:
        auditIntervalSeconds: 60
        enabled: true
        monitoring:
          backends:
          - prometheus
          - cloudmonitoring
        mutation: {}
        referentialRulesEnabled: true
        templateLibraryInstalled: true
    status:
      configManagementVersion: v1.12.2-rc.2

### K8sExternalIPs

External IPs v1.0.0

Restricts Service externalIPs to an allowed list of IP addresses. https://kubernetes.io/docs/concepts/services-networking/service/#external-ips

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sExternalIPs
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedIPs <array>: An allow-list of external IP addresses.
        allowedIPs:
          - <string>
    

#### Examples

##### external-ips

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sExternalIPs
    metadata:
      name: external-ips
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Service
      parameters:
        allowedIPs:
        - 203.0.113.0

###### Allowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: allowed-external-ip
    spec:
      externalIPs:
      - 203.0.113.0
      ports:
      - name: http
        port: 80
        protocol: TCP
        targetPort: 8080
      selector:
        app: MyApp

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: disallowed-external-ip
    spec:
      externalIPs:
      - 1.1.1.1
      ports:
      - name: http
        port: 80
        protocol: TCP
        targetPort: 8080
      selector:
        app: MyApp

### K8sHorizontalPodAutoscaler

Horizontal Pod Autoscaler v1.0.1

Disallow the following scenarios when deploying `HorizontalPodAutoscalers` 1\. Deployment of HorizontalPodAutoscalers with `.spec.minReplicas` or `.spec.maxReplicas` outside the ranges defined in the constraint 2. Deployment of HorizontalPodAutoscalers where the difference between `.spec.minReplicas` and `.spec.maxReplicas` is less than the configured `minimumReplicaSpread` 3\. Deployment of HorizontalPodAutoscalers that do not reference a valid `scaleTargetRef` (e.g. Deployment, ReplicationController, ReplicaSet, StatefulSet).

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sHorizontalPodAutoscaler
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # enforceScaleTargetRef <boolean>: If set to true it validates the HPA
        # scaleTargetRef exists
        enforceScaleTargetRef: <boolean>
        # minimumReplicaSpread <integer>: If configured it enforces the minReplicas
        # and maxReplicas in an HPA must have a spread of at least this many
        # replicas
        minimumReplicaSpread: <integer>
        # ranges <array>: Allowed ranges for numbers of replicas.  Values are
        # inclusive.
        ranges:
          # <list item: object>: A range of allowed replicas.  Values are
          # inclusive.
          - # max_replicas <integer>: The maximum number of replicas allowed,
            # inclusive.
            max_replicas: <integer>
            # min_replicas <integer>: The minimum number of replicas allowed,
            # inclusive.
            min_replicas: <integer>
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "apps"
            version: "v1"
            kind: "Deployment"
          OR
          - group: "apps"
            version: "v1"
            kind: "StatefulSet"
    

#### Examples

##### horizontal-pod-autoscaler

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sHorizontalPodAutoscaler
    metadata:
      name: horizontal-pod-autoscaler
    spec:
      enforcementAction: deny
      match:
        kinds:
        - apiGroups:
          - autoscaling
          kinds:
          - HorizontalPodAutoscaler
      parameters:
        enforceScaleTargetRef: true
        minimumReplicaSpread: 1
        ranges:
        - max_replicas: 6
          min_replicas: 3

###### Allowed
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: nginx-hpa-allowed
      namespace: default
    spec:
      maxReplicas: 6
      metrics:
      - resource:
          name: cpu
          target:
            averageUtilization: 900
            type: Utilization
        type: Resource
      minReplicas: 3
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: nginx-deployment
    ---
    # Referential Data
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: nginx-deployment
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment
      template:
        metadata:
          labels:
            app: nginx
            example: allowed-deployment
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80

###### Disallowed
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: nginx-hpa-disallowed-replicas
      namespace: default
    spec:
      maxReplicas: 7
      metrics:
      - resource:
          name: cpu
          target:
            averageUtilization: 900
            type: Utilization
        type: Resource
      minReplicas: 2
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: nginx-deployment
    ---
    # Referential Data
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: nginx-deployment
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment
      template:
        metadata:
          labels:
            app: nginx
            example: allowed-deployment
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: nginx-hpa-disallowed-replicaspread
      namespace: default
    spec:
      maxReplicas: 4
      metrics:
      - resource:
          name: cpu
          target:
            averageUtilization: 900
            type: Utilization
        type: Resource
      minReplicas: 4
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: nginx-deployment
    ---
    # Referential Data
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: nginx-deployment
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment
      template:
        metadata:
          labels:
            app: nginx
            example: allowed-deployment
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80
    
    
    apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: nginx-hpa-disallowed-scaletarget
      namespace: default
    spec:
      maxReplicas: 6
      metrics:
      - resource:
          name: cpu
          target:
            averageUtilization: 900
            type: Utilization
        type: Resource
      minReplicas: 3
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: nginx-deployment-missing
    ---
    # Referential Data
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: nginx-deployment
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment
      template:
        metadata:
          labels:
            app: nginx
            example: allowed-deployment
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80

### K8sHttpsOnly

HTTPS Only v1.0.2

Requires Ingress resources to be HTTPS only. Ingress resources must include the `kubernetes.io/ingress.allow-http` annotation, set to `false`. By default a valid TLS {} configuration is required, this can be made optional by setting the `tlsOptional` parameter to `true`. https://kubernetes.io/docs/concepts/services-networking/ingress/#tls

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sHttpsOnly
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # tlsOptional <boolean>: When set to `true` the TLS {} is optional,
        # defaults to false.
        tlsOptional: <boolean>
    

#### Examples

##### ingress-https-only

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sHttpsOnly
    metadata:
      name: ingress-https-only
    spec:
      match:
        kinds:
        - apiGroups:
          - extensions
          - networking.k8s.io
          kinds:
          - Ingress

###### Allowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      annotations:
        kubernetes.io/ingress.allow-http: "false"
      name: ingress-demo-allowed
    spec:
      rules:
      - host: example-host.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix
      tls:
      - {}

###### Disallowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: ingress-demo-disallowed
    spec:
      rules:
      - host: example-host.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix

##### ingress-https-only-tls-optional

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sHttpsOnly
    metadata:
      name: ingress-https-only-tls-optional
    spec:
      match:
        kinds:
        - apiGroups:
          - extensions
          - networking.k8s.io
          kinds:
          - Ingress
      parameters:
        tlsOptional: true

###### Allowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      annotations:
        kubernetes.io/ingress.allow-http: "false"
      name: ingress-demo-allowed-tls-optional
    spec:
      rules:
      - host: example-host.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix

###### Disallowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: ingress-demo-disallowed-tls-optional
    spec:
      rules:
      - host: example-host.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix

### K8sImageDigests

Image Digests v1.0.1

Requires container images to contain a digest. https://kubernetes.io/docs/concepts/containers/images/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sImageDigests
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### container-image-must-have-digest

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sImageDigests
    metadata:
      name: container-image-must-have-digest
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
        namespaces:
        - default

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2@sha256:04ff8fce2afd1a3bc26260348e5b290e8d945b1fad4b4c16d22834c2f3a1814a
        name: opa

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
      initContainers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opainit
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
      ephemeralContainers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
      initContainers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opainit

### K8sLocalStorageRequireSafeToEvict

Local Storage Requires Safe to Evict v1.0.1

Requires Pods using local storage (`emptyDir` or `hostPath`) to have the annotation `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"`. Cluster Autoscaler will not delete Pods without this annotation.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sLocalStorageRequireSafeToEvict
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### local-storage-require-safe-to-evict

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sLocalStorageRequireSafeToEvict
    metadata:
      name: local-storage-require-safe-to-evict
    spec:
      match:
        excludedNamespaces:
        - kube-system
        - istio-system
        - gatekeeper-system

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        cluster-autoscaler.kubernetes.io/safe-to-evict: "true"
      name: good-pod
      namespace: default
    spec:
      containers:
      - image: redis
        name: redis
        volumeMounts:
        - mountPath: /data/redis
          name: redis-storage
      volumes:
      - emptyDir: {}
        name: redis-storage

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: bad-pod
      namespace: default
    spec:
      containers:
      - image: redis
        name: redis
        volumeMounts:
        - mountPath: /data/redis
          name: redis-storage
      volumes:
      - emptyDir: {}
        name: redis-storage

### K8sMemoryRequestEqualsLimit

Memory Request Equals Limit v1.0.4

Promotes Pod stability by requiring that all containers' requested memory exactly equals the memory limit, so that Pods are never in a state where memory usage exceeds the requested amount. Otherwise, Kubernetes can terminate Pods requesting extra memory if memory is needed on the node.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sMemoryRequestEqualsLimit
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptContainersRegex <array>: Exempt Container names as regex match.
        exemptContainersRegex:
          - <string>
    

#### Examples

##### container-must-request-limit

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sMemoryRequestEqualsLimit
    metadata:
      name: container-must-request-limit
    spec:
      match:
        excludedNamespaces:
        - kube-system
        - resource-group-system
        - asm-system
        - istio-system
        - config-management-system
        - config-management-monitoring
      parameters:
        exemptContainersRegex:
        - ^istio-[a-z]+$

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: good-pod
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 100m
            memory: 4Gi
          requests:
            cpu: 50m
            memory: 4Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: exempt-pod
      namespace: default
    spec:
      containers:
      - image: auto
        name: istio-proxy
        resources:
          limits:
            cpu: 100m
            memory: 4Gi
          requests:
            cpu: 50m
            memory: 2Gi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: bad-pod
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 100m
            memory: 4Gi
          requests:
            cpu: 50m
            memory: 2Gi

### K8sNoEnvVarSecrets

No Environment Variable Secrets v1.0.1

Prohibits secrets as environment variables in Pod container definitions. Use mounted secret files in data volumes instead: https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sNoEnvVarSecrets
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### no-secrets-as-env-vars-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sNoEnvVarSecrets
    metadata:
      name: no-secrets-as-env-vars-sample
    spec:
      enforcementAction: dryrun

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: allowed-example
    spec:
      containers:
      - image: redis
        name: test
        volumeMounts:
        - mountPath: /etc/test
          name: test
          readOnly: true
      volumes:
      - name: test
        secret:
          secretName: mysecret

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: disallowed-example
    spec:
      containers:
      - env:
        - name: MY_PASSWORD
          valueFrom:
            secretKeyRef:
              key: password
              name: mysecret
        image: redis
        name: test

### K8sNoExternalServices

No External Services v1.0.3

Prohibits the creation of known resources that expose workloads to external IPs. This includes Istio Gateway resources and Kubernetes Ingress resources. Kubernetes services are also disallowed unless they meet the following criteria: Any Service of type `LoadBalancer` in Google Cloud must have a `"networking.gke.io/load-balancer-type": "Internal"` annotation. Any Service of type `LoadBalancer` in AWS must have a `service.beta.kubernetes.io/aws-load-balancer-internal: "true` annotation. Any "external IPs" (external to the cluster) bound to the Service must be a member of a range of internal CIDRs as provided to the constraint.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sNoExternalServices
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # cloudPlatform <string>: The hosting cloud platform. Only `GCP` and `AWS`
        # are supported currently.
        cloudPlatform: <string>
        # internalCIDRs <array>: A list of CIDRs that are only accessible
        # internally, for example: `10.3.27.0/24`. Which IP ranges are
        # internal-only is determined by the underlying network infrastructure.
        internalCIDRs:
          - <string>
    

#### Examples

##### no-external

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sNoExternalServices
    metadata:
      name: no-external
    spec:
      parameters:
        internalCIDRs:
        - 10.0.0.1/32

###### Allowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: good-service
      namespace: default
    spec:
      externalIPs:
      - 10.0.0.1
      ports:
      - port: 8888
        protocol: TCP
        targetPort: 8888
    
    
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        networking.gke.io/load-balancer-type: Internal
      name: allowed-internal-load-balancer
      namespace: default
    spec:
      type: LoadBalancer

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: bad-service
      namespace: default
    spec:
      externalIPs:
      - 10.0.0.2
      ports:
      - port: 8888
        protocol: TCP
        targetPort: 8888

##### no-external-aws

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sNoExternalServices
    metadata:
      name: no-external-aws
    spec:
      parameters:
        cloudPlatform: AWS

###### Allowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-internal: "true"
      name: good-aws-service
      namespace: default
    spec:
      type: LoadBalancer

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        cloud.google.com/load-balancer-type: Internal
      name: bad-aws-service
      namespace: default
    spec:
      type: LoadBalancer

### K8sPSPAllowPrivilegeEscalationContainer

Allow Privilege Escalation in Container v1.0.1

Controls restricting escalation to root privileges. Corresponds to the `allowPrivilegeEscalation` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#privilege-escalation

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAllowPrivilegeEscalationContainer
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### psp-allow-privilege-escalation-container-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAllowPrivilegeEscalationContainer
    metadata:
      name: psp-allow-privilege-escalation-container-sample
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-privilege-escalation
      name: nginx-privilege-escalation-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          allowPrivilegeEscalation: false

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-privilege-escalation
      name: nginx-privilege-escalation-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          allowPrivilegeEscalation: true
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-privilege-escalation
      name: nginx-privilege-escalation-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx
        securityContext:
          allowPrivilegeEscalation: true

### K8sPSPAllowedUsers

Allowed Users v1.0.2

Controls the user and group IDs of the container and some volumes. Corresponds to the `runAsUser`, `runAsGroup`, `supplementalGroups`, and `fsGroup` fields in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#users-and-groups

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAllowedUsers
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # fsGroup <object>: Controls the fsGroup values that are allowed in a Pod
        # or container-level SecurityContext.
        fsGroup:
          # ranges <array>: A list of group ID ranges affected by the rule.
          ranges:
            # <list item: object>: The range of group IDs affected by the rule.
            - # max <integer>: The maximum group ID in the range, inclusive.
              max: <integer>
              # min <integer>: The minimum group ID in the range, inclusive.
              min: <integer>
          # rule <string>: A strategy for applying the fsGroup restriction.
          # Allowed Values: MustRunAs, MayRunAs, RunAsAny
          rule: <string>
        # runAsGroup <object>: Controls which group ID values are allowed in a Pod
        # or container-level SecurityContext.
        runAsGroup:
          # ranges <array>: A list of group ID ranges affected by the rule.
          ranges:
            # <list item: object>: The range of group IDs affected by the rule.
            - # max <integer>: The maximum group ID in the range, inclusive.
              max: <integer>
              # min <integer>: The minimum group ID in the range, inclusive.
              min: <integer>
          # rule <string>: A strategy for applying the runAsGroup restriction.
          # Allowed Values: MustRunAs, MayRunAs, RunAsAny
          rule: <string>
        # runAsUser <object>: Controls which user ID values are allowed in a Pod or
        # container-level SecurityContext.
        runAsUser:
          # ranges <array>: A list of user ID ranges affected by the rule.
          ranges:
            # <list item: object>: The range of user IDs affected by the rule.
            - # max <integer>: The maximum user ID in the range, inclusive.
              max: <integer>
              # min <integer>: The minimum user ID in the range, inclusive.
              min: <integer>
          # rule <string>: A strategy for applying the runAsUser restriction.
          # Allowed Values: MustRunAs, MustRunAsNonRoot, RunAsAny
          rule: <string>
        # supplementalGroups <object>: Controls the supplementalGroups values that
        # are allowed in a Pod or container-level SecurityContext.
        supplementalGroups:
          # ranges <array>: A list of group ID ranges affected by the rule.
          ranges:
            # <list item: object>: The range of group IDs affected by the rule.
            - # max <integer>: The maximum group ID in the range, inclusive.
              max: <integer>
              # min <integer>: The minimum group ID in the range, inclusive.
              min: <integer>
          # rule <string>: A strategy for applying the supplementalGroups
          # restriction.
          # Allowed Values: MustRunAs, MayRunAs, RunAsAny
          rule: <string>
    

#### Examples

##### psp-pods-allowed-user-ranges

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAllowedUsers
    metadata:
      name: psp-pods-allowed-user-ranges
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        fsGroup:
          ranges:
          - max: 200
            min: 100
          rule: MustRunAs
        runAsGroup:
          ranges:
          - max: 200
            min: 100
          rule: MustRunAs
        runAsUser:
          ranges:
          - max: 200
            min: 100
          rule: MustRunAs
        supplementalGroups:
          ranges:
          - max: 200
            min: 100
          rule: MustRunAs

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-users
      name: nginx-users-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          runAsGroup: 199
          runAsUser: 199
      securityContext:
        fsGroup: 199
        supplementalGroups:
        - 199

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-users
      name: nginx-users-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          runAsGroup: 250
          runAsUser: 250
      securityContext:
        fsGroup: 250
        supplementalGroups:
        - 250
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-users
      name: nginx-users-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx
        securityContext:
          runAsGroup: 250
          runAsUser: 250
      securityContext:
        fsGroup: 250
        supplementalGroups:
        - 250

### K8sPSPAppArmor

App Armor v1.0.0

Configures an allow-list of AppArmor profiles for use by containers. This corresponds to specific annotations applied to a PodSecurityPolicy. For information on AppArmor, see https://kubernetes.io/docs/tutorials/clusters/apparmor/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAppArmor
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedProfiles <array>: An array of AppArmor profiles. Examples:
        # `runtime/default`, `unconfined`.
        allowedProfiles:
          - <string>
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### psp-apparmor

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAppArmor
    metadata:
      name: psp-apparmor
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        allowedProfiles:
        - runtime/default

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        container.apparmor.security.beta.kubernetes.io/nginx: runtime/default
      labels:
        app: nginx-apparmor
      name: nginx-apparmor-allowed
    spec:
      containers:
      - image: nginx
        name: nginx

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        container.apparmor.security.beta.kubernetes.io/nginx: unconfined
      labels:
        app: nginx-apparmor
      name: nginx-apparmor-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        container.apparmor.security.beta.kubernetes.io/nginx: unconfined
      labels:
        app: nginx-apparmor
      name: nginx-apparmor-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx

### K8sPSPAutomountServiceAccountTokenPod

Automount Service Account Token for Pod v1.0.1

Controls the ability of any Pod to enable automountServiceAccountToken.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAutomountServiceAccountTokenPod
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        <object>
    

#### Examples

##### psp-automount-serviceaccount-token-pod

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAutomountServiceAccountTokenPod
    metadata:
      name: psp-automount-serviceaccount-token-pod
    spec:
      match:
        excludedNamespaces:
        - kube-system
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-not-automountserviceaccounttoken
      name: nginx-automountserviceaccounttoken-allowed
    spec:
      automountServiceAccountToken: false
      containers:
      - image: nginx
        name: nginx

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-automountserviceaccounttoken
      name: nginx-automountserviceaccounttoken-disallowed
    spec:
      automountServiceAccountToken: true
      containers:
      - image: nginx
        name: nginx

### K8sPSPCapabilities

Capabilities v1.0.2

Controls Linux capabilities on containers. Corresponds to the `allowedCapabilities` and `requiredDropCapabilities` fields in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#capabilities

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPCapabilities
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedCapabilities <array>: A list of Linux capabilities that can be
        # added to a container.
        allowedCapabilities:
          - <string>
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # requiredDropCapabilities <array>: A list of Linux capabilities that are
        # required to be dropped from a container.
        requiredDropCapabilities:
          - <string>
    

#### Examples

##### capabilities-demo

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPCapabilities
    metadata:
      name: capabilities-demo
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
        namespaces:
        - default
      parameters:
        allowedCapabilities:
        - something
        requiredDropCapabilities:
        - must_drop

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
        securityContext:
          capabilities:
            add:
            - something
            drop:
            - must_drop
            - another_one

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
        securityContext:
          capabilities:
            add:
            - disallowedcapability
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      ephemeralContainers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 30Mi
        securityContext:
          capabilities:
            add:
            - disallowedcapability

### K8sPSPFSGroup

FS Group v1.0.2

Controls allocating an FSGroup that owns the Pod's volumes. Corresponds to the `fsGroup` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPFSGroup
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # ranges <array>: GID ranges affected by the rule.
        ranges:
          - # max <integer>: The maximum GID in the range, inclusive.
            max: <integer>
            # min <integer>: The minimum GID in the range, inclusive.
            min: <integer>
        # rule <string>: An FSGroup rule name.
        # Allowed Values: MayRunAs, MustRunAs, RunAsAny
        rule: <string>
    

#### Examples

##### psp-fsgroup

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPFSGroup
    metadata:
      name: psp-fsgroup
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        ranges:
        - max: 1000
          min: 1
        rule: MayRunAs

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: fsgroup-disallowed
    spec:
      containers:
      - command:
        - sh
        - -c
        - sleep 1h
        image: busybox
        name: fsgroup-demo
        volumeMounts:
        - mountPath: /data/demo
          name: fsgroup-demo-vol
      securityContext:
        fsGroup: 500
      volumes:
      - emptyDir: {}
        name: fsgroup-demo-vol

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: fsgroup-disallowed
    spec:
      containers:
      - command:
        - sh
        - -c
        - sleep 1h
        image: busybox
        name: fsgroup-demo
        volumeMounts:
        - mountPath: /data/demo
          name: fsgroup-demo-vol
      securityContext:
        fsGroup: 2000
      volumes:
      - emptyDir: {}
        name: fsgroup-demo-vol

### K8sPSPFlexVolumes

FlexVolumes v1.0.1

Controls the allowlist of FlexVolume drivers. Corresponds to the `allowedFlexVolumes` field in PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#flexvolume-drivers

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPFlexVolumes
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedFlexVolumes <array>: An array of AllowedFlexVolume objects.
        allowedFlexVolumes:
          - # driver <string>: The name of the FlexVolume driver.
            driver: <string>
    

#### Examples

##### psp-flexvolume-drivers

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPFlexVolumes
    metadata:
      name: psp-flexvolume-drivers
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        allowedFlexVolumes:
        - driver: example/lvm
        - driver: example/cifs

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-flexvolume-driver
      name: nginx-flexvolume-driver-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        volumeMounts:
        - mountPath: /test
          name: test-volume
          readOnly: true
      volumes:
      - flexVolume:
          driver: example/lvm
        name: test-volume

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-flexvolume-driver
      name: nginx-flexvolume-driver-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        volumeMounts:
        - mountPath: /test
          name: test-volume
          readOnly: true
      volumes:
      - flexVolume:
          driver: example/testdriver
        name: test-volume

### K8sPSPForbiddenSysctls

Forbidden Sysctls v1.1.3

Controls the `sysctl` profile used by containers. Corresponds to the `allowedUnsafeSysctls` and `forbiddenSysctls` fields in a PodSecurityPolicy. When specified, any sysctl not in the `allowedSysctls` parameter is considered to be forbidden. The `forbiddenSysctls` parameter takes precedence over the `allowedSysctls` parameter. For more information, see https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPForbiddenSysctls
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedSysctls <array>: An allow-list of sysctls. `*` allows all sysctls
        # not listed in the `forbiddenSysctls` parameter.
        allowedSysctls:
          - <string>
        # forbiddenSysctls <array>: A disallow-list of sysctls. `*` forbids all
        # sysctls.
        forbiddenSysctls:
          - <string>
    

#### Examples

##### psp-forbidden-sysctls

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPForbiddenSysctls
    metadata:
      name: psp-forbidden-sysctls
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        allowedSysctls:
        - '*'
        forbiddenSysctls:
        - kernel.*

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-forbidden-sysctls
      name: nginx-forbidden-sysctls-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
      securityContext:
        sysctls:
        - name: net.core.somaxconn
          value: "1024"

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-forbidden-sysctls
      name: nginx-forbidden-sysctls-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
      securityContext:
        sysctls:
        - name: kernel.msgmax
          value: "65536"
        - name: net.core.somaxconn
          value: "1024"

### K8sPSPHostFilesystem

Host Filesystem v1.0.2

Controls usage of the host filesystem. Corresponds to the `allowedHostPaths` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPHostFilesystem
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedHostPaths <array>: An array of hostpath objects, representing
        # paths and read/write configuration.
        allowedHostPaths:
          - # pathPrefix <string>: The path prefix that the host volume must
            # match.
            pathPrefix: <string>
            # readOnly <boolean>: when set to true, any container volumeMounts
            # matching the pathPrefix must include `readOnly: true`.
            readOnly: <boolean>
    

#### Examples

##### psp-host-filesystem

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPHostFilesystem
    metadata:
      name: psp-host-filesystem
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        allowedHostPaths:
        - pathPrefix: /foo
          readOnly: true

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-host-filesystem-disallowed
      name: nginx-host-filesystem
    spec:
      containers:
      - image: nginx
        name: nginx
        volumeMounts:
        - mountPath: /cache
          name: cache-volume
          readOnly: true
      volumes:
      - hostPath:
          path: /foo/bar
        name: cache-volume

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-host-filesystem-disallowed
      name: nginx-host-filesystem
    spec:
      containers:
      - image: nginx
        name: nginx
        volumeMounts:
        - mountPath: /cache
          name: cache-volume
          readOnly: true
      volumes:
      - hostPath:
          path: /tmp
        name: cache-volume
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-host-filesystem-disallowed
      name: nginx-host-filesystem
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx
        volumeMounts:
        - mountPath: /cache
          name: cache-volume
          readOnly: true
      volumes:
      - hostPath:
          path: /tmp
        name: cache-volume

### K8sPSPHostNamespace

Host Namespace v1.0.1

Disallows sharing of host PID and IPC namespaces by pod containers. Corresponds to the `hostPID` and `hostIPC` fields in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#host-namespaces

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPHostNamespace
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        <object>
    

#### Examples

##### psp-host-namespace-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPHostNamespace
    metadata:
      name: psp-host-namespace-sample
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-host-namespace
      name: nginx-host-namespace-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
      hostIPC: false
      hostPID: false

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-host-namespace
      name: nginx-host-namespace-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
      hostIPC: true
      hostPID: true

### K8sPSPHostNetworkingPorts

Host Networking Ports v1.0.2

Controls usage of host network namespace by pod containers. Specific ports must be specified. Corresponds to the `hostNetwork` and `hostPorts` fields in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#host-namespaces

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPHostNetworkingPorts
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # hostNetwork <boolean>: Determines if the policy allows the use of
        # HostNetwork in the pod spec.
        hostNetwork: <boolean>
        # max <integer>: The end of the allowed port range, inclusive.
        max: <integer>
        # min <integer>: The start of the allowed port range, inclusive.
        min: <integer>
    

#### Examples

##### psp-host-network-ports-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPHostNetworkingPorts
    metadata:
      name: psp-host-network-ports-sample
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        hostNetwork: true
        max: 9000
        min: 80

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-host-networking-ports
      name: nginx-host-networking-ports-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 9000
          hostPort: 80
      hostNetwork: false

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-host-networking-ports
      name: nginx-host-networking-ports-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 9001
          hostPort: 9001
      hostNetwork: true
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-host-networking-ports
      name: nginx-host-networking-ports-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 9001
          hostPort: 9001
      hostNetwork: true

### K8sPSPPrivilegedContainer

Privileged Container v1.0.1

Controls the ability of any container to enable privileged mode. Corresponds to the `privileged` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#privileged

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPPrivilegedContainer
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### psp-privileged-container-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPPrivilegedContainer
    metadata:
      name: psp-privileged-container-sample
    spec:
      match:
        excludedNamespaces:
        - kube-system
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-privileged
      name: nginx-privileged-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          privileged: false

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-privileged
      name: nginx-privileged-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          privileged: true
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-privileged
      name: nginx-privileged-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx
        securityContext:
          privileged: true

### K8sPSPProcMount

Proc Mount v1.0.3

Controls the allowed `procMount` types for the container. Corresponds to the `allowedProcMountTypes` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#allowedprocmounttypes

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPProcMount
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # procMount <string>: Defines the strategy for the security exposure of
        # certain paths in `/proc` by the container runtime. Setting to `Default`
        # uses the runtime defaults, where `Unmasked` bypasses the default
        # behavior.
        # Allowed Values: Default, Unmasked
        procMount: <string>
    

#### Examples

##### psp-proc-mount

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPProcMount
    metadata:
      name: psp-proc-mount
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        procMount: Default

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-proc-mount
      name: nginx-proc-mount-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          procMount: Default

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-proc-mount
      name: nginx-proc-mount-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          procMount: Unmasked
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-proc-mount
      name: nginx-proc-mount-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx
        securityContext:
          procMount: Unmasked

### K8sPSPReadOnlyRootFilesystem

Read Only Root Filesystem v1.0.1

Requires the use of a read-only root file system by pod containers. Corresponds to the `readOnlyRootFilesystem` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPReadOnlyRootFilesystem
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### psp-readonlyrootfilesystem

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPReadOnlyRootFilesystem
    metadata:
      name: psp-readonlyrootfilesystem
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-readonlyrootfilesystem
      name: nginx-readonlyrootfilesystem-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          readOnlyRootFilesystem: true

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-readonlyrootfilesystem
      name: nginx-readonlyrootfilesystem-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          readOnlyRootFilesystem: false
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-readonlyrootfilesystem
      name: nginx-readonlyrootfilesystem-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx
        securityContext:
          readOnlyRootFilesystem: false

### K8sPSPSELinuxV2

SELinux V2 v1.0.3

Defines an allow-list of seLinuxOptions configurations for pod containers. Corresponds to a PodSecurityPolicy requiring SELinux configs. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#selinux

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPSELinuxV2
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedSELinuxOptions <array>: An allow-list of SELinux options
        # configurations.
        allowedSELinuxOptions:
          # <list item: object>: An allowed configuration of SELinux options for a
          # pod container.
          - # level <string>: An SELinux level.
            level: <string>
            # role <string>: An SELinux role.
            role: <string>
            # type <string>: An SELinux type.
            type: <string>
            # user <string>: An SELinux user.
            user: <string>
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### psp-selinux-v2

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPSELinuxV2
    metadata:
      name: psp-selinux-v2
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        allowedSELinuxOptions:
        - level: s0:c123,c456
          role: object_r
          type: svirt_sandbox_file_t
          user: system_u

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-selinux
      name: nginx-selinux-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          seLinuxOptions:
            level: s0:c123,c456
            role: object_r
            type: svirt_sandbox_file_t
            user: system_u

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-selinux
      name: nginx-selinux-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          seLinuxOptions:
            level: s1:c234,c567
            role: sysadm_r
            type: svirt_lxc_net_t
            user: sysadm_u
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-selinux
      name: nginx-selinux-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx
        securityContext:
          seLinuxOptions:
            level: s1:c234,c567
            role: sysadm_r
            type: svirt_lxc_net_t
            user: sysadm_u

### K8sPSPSeccomp

Seccomp v1.0.1

Controls the seccomp profile used by containers. Corresponds to the `seccomp.security.alpha.kubernetes.io/allowedProfileNames` annotation on a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#seccomp

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPSeccomp
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedLocalhostFiles <array>: When using securityContext naming scheme
        # for seccomp and including `Localhost` this array holds the allowed
        # profile JSON files. Putting a `*` in this array will allows all JSON
        # files to be used. This field is required to allow `Localhost` in
        # securityContext as with an empty list it will block.
        allowedLocalhostFiles:
          - <string>
        # allowedProfiles <array>: An array of allowed profile values for seccomp
        # on Pods/Containers. Can use the annotation naming scheme:
        # `runtime/default`, `docker/default`, `unconfined` and/or
        # `localhost/some-profile.json`. The item `localhost/*` will allow any
        # localhost based profile. Can also use the securityContext naming scheme:
        # `RuntimeDefault`, `Unconfined` and/or `Localhost`. For securityContext
        # `Localhost`, use the parameter `allowedLocalhostProfiles` to list the
        # allowed profile JSON files. The policy code will translate between the
        # two schemes so it is not necessary to use both. Putting a `*` in this
        # array allows all Profiles to be used. This field is required since with
        # an empty list this policy will block all workloads.
        allowedProfiles:
          - <string>
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
    

#### Examples

##### psp-seccomp

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPSeccomp
    metadata:
      name: psp-seccomp
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        allowedProfiles:
        - runtime/default
        - docker/default

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        container.seccomp.security.alpha.kubernetes.io/nginx: runtime/default
      labels:
        app: nginx-seccomp
      name: nginx-seccomp-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        seccomp.security.alpha.kubernetes.io/pod: runtime/default
      labels:
        app: nginx-seccomp
      name: nginx-seccomp-allowed2
    spec:
      containers:
      - image: nginx
        name: nginx

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        seccomp.security.alpha.kubernetes.io/pod: unconfined
      labels:
        app: nginx-seccomp
      name: nginx-seccomp-disallowed2
    spec:
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        container.seccomp.security.alpha.kubernetes.io/nginx: unconfined
      labels:
        app: nginx-seccomp
      name: nginx-seccomp-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        container.seccomp.security.alpha.kubernetes.io/nginx: unconfined
      labels:
        app: nginx-seccomp
      name: nginx-seccomp-disallowed
    spec:
      ephemeralContainers:
      - image: nginx
        name: nginx

### K8sPSPVolumeTypes

Volume Types v1.0.2

Restricts mountable volume types to those specified by the user. Corresponds to the `volumes` field in a PodSecurityPolicy. For more information, see https://kubernetes.io/docs/concepts/policy/pod-security-policy/#volumes-and-file-systems

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPVolumeTypes
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # volumes <array>: `volumes` is an array of volume types. All volume types
        # can be enabled using `*`.
        volumes:
          - <string>
    

#### Examples

##### psp-volume-types

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPVolumeTypes
    metadata:
      name: psp-volume-types
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        volumes:
        - configMap
        - emptyDir
        - projected
        - secret
        - downwardAPI
        - persistentVolumeClaim
        - flexVolume

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-volume-types
      name: nginx-volume-types-allowed
    spec:
      containers:
      - image: nginx
        name: nginx
        volumeMounts:
        - mountPath: /cache
          name: cache-volume
      - image: nginx
        name: nginx2
        volumeMounts:
        - mountPath: /cache2
          name: demo-vol
      volumes:
      - emptyDir: {}
        name: cache-volume
      - emptyDir: {}
        name: demo-vol

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx-volume-types
      name: nginx-volume-types-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx
        volumeMounts:
        - mountPath: /cache
          name: cache-volume
      - image: nginx
        name: nginx2
        volumeMounts:
        - mountPath: /cache2
          name: demo-vol
      volumes:
      - hostPath:
          path: /tmp
        name: cache-volume
      - emptyDir: {}
        name: demo-vol

### K8sPSPWindowsHostProcess

Restricts Windows HostProcess containers / pods. v1.0.0

Restricts running of Windows HostProcess containers / pods. See https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/ for more information.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPWindowsHostProcess
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### restrict-windows-hostprocess

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPWindowsHostProcess
    metadata:
      name: restrict-windows-hostprocess
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nanoserver-ping-loop
    spec:
      containers:
      - command:
        - ping
        - -t
        - 127.0.0.1
        image: mcr.microsoft.com/windows/nanoserver:1809
        name: ping-loop
      nodeSelector:
        kubernetes.io/os: windows

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nanoserver-ping-loop-hostprocess-container
    spec:
      containers:
      - command:
        - ping
        - -t
        - 127.0.0.1
        image: mcr.microsoft.com/windows/nanoserver:1809
        name: ping-test
        securityContext:
          windowsOptions:
            hostProcess: true
            runAsUserName: NT AUTHORITY\SYSTEM
      hostNetwork: true
      nodeSelector:
        kubernetes.io/os: windows
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nanoserver-ping-loop-hostprocess-pod
    spec:
      containers:
      - command:
        - ping
        - -t
        - 127.0.0.1
        image: mcr.microsoft.com/windows/nanoserver:1809
        name: ping-test
      hostNetwork: true
      nodeSelector:
        kubernetes.io/os: windows
      securityContext:
        windowsOptions:
          hostProcess: true
          runAsUserName: NT AUTHORITY\SYSTEM

### K8sPSSRunAsNonRoot

Requires containers run as non-root users. v1.0.0

Requires containers run as non-root users. For more information, see https://kubernetes.io/docs/concepts/security/pod-security-standards/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSSRunAsNonRoot
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### restrict-runasnonroot

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSSRunAsNonRoot
    metadata:
      name: restrict-runasnonroot
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-pod-allowed
    spec:
      containers:
      - image: nginx
        name: nginx-container-allowed
        securityContext:
          runAsNonRoot: true
      securityContext:
        runAsNonRoot: true
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-allowed
    spec:
      containers:
      - image: nginx
        name: nginx-allowed
      securityContext:
        runAsNonRoot: true

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-pod-allowed
    spec:
      containers:
      - image: nginx
        name: nginx-container-disallowed
        securityContext:
          runAsNonRoot: false
      securityContext:
        runAsNonRoot: true
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-pod-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx-container-allowed
        securityContext:
          runAsNonRoot: true
      securityContext:
        runAsNonRoot: false
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-pod-disallowed
    spec:
      containers:
      - image: nginx
        name: nginx-container-disallowed
      securityContext:
        runAsNonRoot: false

### K8sPodDisruptionBudget

Pod Disruption Budget v1.0.3

Disallow the following scenarios when deploying PodDisruptionBudgets or resources that implement the replica subresource (e.g. Deployment, ReplicationController, ReplicaSet, StatefulSet): 1. Deployment of PodDisruptionBudgets with .spec.maxUnavailable == 0 2. Deployment of PodDisruptionBudgets with .spec.minAvailable == .spec.replicas of the resource with replica subresource This will prevent PodDisruptionBudgets from blocking voluntary disruptions such as node draining. https://kubernetes.io/docs/concepts/workloads/pods/disruptions/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPodDisruptionBudget
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "policy"
            version: "v1"
            kind: "PodDisruptionBudget"
    

#### Examples

##### pod-distruption-budget

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPodDisruptionBudget
    metadata:
      name: pod-distruption-budget
    spec:
      match:
        kinds:
        - apiGroups:
          - apps
          kinds:
          - Deployment
          - ReplicaSet
          - StatefulSet
        - apiGroups:
          - policy
          kinds:
          - PodDisruptionBudget
        - apiGroups:
          - ""
          kinds:
          - ReplicationController

###### Allowed
    
    
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: nginx-pdb-allowed
      namespace: default
    spec:
      maxUnavailable: 1
      selector:
        matchLabels:
          foo: bar
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: nginx-deployment-allowed-1
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment-1
      template:
        metadata:
          labels:
            app: nginx
            example: allowed-deployment-1
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80
    ---
    # Referential Data
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: inventory-nginx-pdb-allowed-1
      namespace: default
    spec:
      minAvailable: 2
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment-1
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: nginx-deployment-allowed-2
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment-2
      template:
        metadata:
          labels:
            app: nginx
            example: allowed-deployment-2
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80
    ---
    # Referential Data
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: inventory-nginx-pdb-allowed-2
      namespace: default
    spec:
      maxUnavailable: 1
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment-2
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: nginx-deployment-allowed-3
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
          example: allowed-deployment-3
      template:
        metadata:
          labels:
            app: nginx
            example: allowed-deployment-3
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80
    ---
    # Referential Data
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: inventory-nginx-pdb-allowed-3
      namespace: default
    spec:
      minAvailable: 2
      selector:
        matchLabels:
          app: nginx
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: non-matching-nginx
      name: nginx-deployment-allowed-4
      namespace: default
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: non-matching-nginx
          example: allowed-deployment-4
      template:
        metadata:
          labels:
            app: non-matching-nginx
            example: allowed-deployment-4
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80
    ---
    # Referential Data
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: inventory-mongo-pdb-allowed-3
      namespace: default
    spec:
      minAvailable: 2
      selector:
        matchLabels:
          app: mongo
          example: non-matching-deployment-3

###### Disallowed
    
    
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: nginx-pdb-disallowed
      namespace: default
    spec:
      maxUnavailable: 0
      selector:
        matchLabels:
          foo: bar
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: nginx-deployment-disallowed
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
          example: disallowed-deployment
      template:
        metadata:
          labels:
            app: nginx
            example: disallowed-deployment
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80
    ---
    # Referential Data
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: inventory-nginx-pdb-disallowed
      namespace: default
    spec:
      minAvailable: 3
      selector:
        matchLabels:
          app: nginx
          example: disallowed-deployment

### K8sPodResourcesBestPractices

Requires Containers are not Best-effort and Following Burstable Best Practices v1.0.5

Requires that containers are not best-effort (by setting cpu and memory requests) and following burstable best practices (memory request must exactly equal limit). Optionally, annotation keys can be configured to permit skipping the various validations.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPodResourcesBestPractices
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: A list of exempt Images.
        exemptImages:
          - <string>
        # skipBestEffortValidationAnnotationKey <string>: Optional annotation key
        # to skip best-effort container validation.
        skipBestEffortValidationAnnotationKey: <string>
        # skipBurstableValidationAnnotationKey <string>: Optional annotation key to
        # skip burstable container validation.
        skipBurstableValidationAnnotationKey: <string>
        # skipResourcesBestPracticesValidationAnnotationKey <string>: Optional
        # annotation key to skip both best-effort and burstable validation.
        skipResourcesBestPracticesValidationAnnotationKey: <string>
    

#### Examples

##### gke-pod-resources-best-practices

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPodResourcesBestPractices
    metadata:
      name: gke-pod-resources-best-practices
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        skipBestEffortValidationAnnotationKey: skip_besteffort_validation
        skipBurstableValidationAnnotationKey: skip_burstable_validation
        skipResourcesBestPracticesValidationAnnotationKey: skip_resources_best_practices_validation

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-cpu-requests-memory-limits
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            memory: 500Mi
          requests:
            cpu: 250m
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-limits-only
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 250m
            memory: 100Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-requests-memory-limits
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            memory: 100Mi
          requests:
            cpu: 250m
            memory: 100Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        skip_besteffort_validation: "true"
        skip_burstable_validation: "true"
        skip_resources_best_practices_validation: "false"
      name: pod-skip-validation
    spec:
      containers:
      - image: nginx
        name: nginx

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-not-setting-cpu-burstable-on-memory
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            memory: 500Mi
          requests:
            memory: 100Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-not-setting-requests
    spec:
      containers:
      - image: nginx
        name: nginx
      restartPolicy: OnFailure
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-cpu-not-burstable-on-memory
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            memory: 500Mi
          requests:
            cpu: 250m
            memory: 100Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-memory-requests-cpu-limits
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 30m
          requests:
            memory: 100Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-only-cpu-limits
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 250m
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-only-cpu-requests
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          requests:
            cpu: 250m
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-only-cpu
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            cpu: 500m
          requests:
            cpu: 250m
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-only-memory-limits
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            memory: 250Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-only-memory-requests
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          requests:
            memory: 100Mi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: pod-setting-only-memory
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          limits:
            memory: 100Mi
          requests:
            memory: 100Mi

### K8sPodsRequireSecurityContext

Pods Require Security Context v1.1.1

Requires all Pods to define securityContext. Requires all containers defined in Pods to have a SecurityContext defined at the Pod or container level.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPodsRequireSecurityContext
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: A list of exempt Images.
        exemptImages:
          - <string>
    

#### Examples

##### pods-require-security-context-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPodsRequireSecurityContext
    metadata:
      name: pods-require-security-context-sample
    spec:
      enforcementAction: dryrun
      parameters:
        exemptImages:
        - nginix-exempt
        - alpine*

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: allowed-example
    spec:
      containers:
      - image: nginx
        name: nginx
        securityContext:
          runAsUser: 2000
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: allowed-example-exemptImage
    spec:
      containers:
      - image: nginix-exempt
        name: nginx
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: allowed-example-exemptImage-wildcard
    spec:
      containers:
      - image: alpine17
        name: alpine

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: disallowed-example
    spec:
      containers:
      - image: nginx
        name: nginx

### K8sProhibitRoleWildcardAccess

Prohibit Role Wildcard Access v1.0.5

Requires that Roles and ClusterRoles not set resource access to a wildcard '"_"' value except for the exempted Roles and ClusterRoles provided as exemptions. Does not restrict wildcard access to subresources, such as '"_ /status"'.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sProhibitRoleWildcardAccess
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptions <object>: The list of exempted Roles and/or ClusterRoles name
        # that are allowed to set  resource access to a wildcard.
        exemptions:
          clusterRoles:
            - # name <string>: The name of the ClusterRole to be exempted.
              name: <string>
              # regexMatch <boolean>: The flag to allow a regular expression
              # based match on the name.
              regexMatch: <boolean>
          roles:
            - # name <string>: The name of the Role to be exempted.
              name: <string>
              # namespace <string>: The namespace of the Role to be exempted.
              namespace: <string>
    

#### Examples

##### prohibit-role-wildcard-access-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sProhibitRoleWildcardAccess
    metadata:
      name: prohibit-role-wildcard-access-sample
    spec:
      enforcementAction: dryrun

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: cluster-role-example
    rules:
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - get

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: cluster-role-bad-example
    rules:
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - '*'

##### prohibit-wildcard-except-exempted-cluster-role

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sProhibitRoleWildcardAccess
    metadata:
      name: prohibit-wildcard-except-exempted-cluster-role
    spec:
      enforcementAction: dryrun
      parameters:
        exemptions:
          clusterRoles:
          - name: cluster-role-allowed-example
          roles:
          - name: role-allowed-example
            namespace: role-ns-allowed-example

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: cluster-role-allowed-example
    rules:
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - '*'
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      name: role-allowed-example
      namespace: role-ns-allowed-example
    rules:
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - '*'

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: cluster-role-not-allowed-example
    rules:
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - '*'
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      name: role-not-allowed-example
      namespace: role-ns-not-allowed-example
    rules:
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - '*'

### K8sReplicaLimits

Replica Limits v1.0.2

Requires that objects with the field `spec.replicas` (Deployments, ReplicaSets, etc.) specify a number of replicas within defined ranges.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sReplicaLimits
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # ranges <array>: Allowed ranges for numbers of replicas.  Values are
        # inclusive.
        ranges:
          # <list item: object>: A range of allowed replicas.  Values are
          # inclusive.
          - # max_replicas <integer>: The maximum number of replicas allowed,
            # inclusive.
            max_replicas: <integer>
            # min_replicas <integer>: The minimum number of replicas allowed,
            # inclusive.
            min_replicas: <integer>
    

#### Examples

##### replica-limits

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sReplicaLimits
    metadata:
      name: replica-limits
    spec:
      match:
        kinds:
        - apiGroups:
          - apps
          kinds:
          - Deployment
      parameters:
        ranges:
        - max_replicas: 50
          min_replicas: 3

###### Allowed
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: allowed-deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80

###### Disallowed
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: disallowed-deployment
    spec:
      replicas: 100
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80

### K8sRequireAdmissionController

Require Admission Controller v1.0.0

Requires either Pod Security Admission or an external policy control system

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireAdmissionController
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # permittedValidatingWebhooks <array>: List of permitted validating
        # webhooks which are valid external policy control systems
        permittedValidatingWebhooks:
          - <string>
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "admissionregistration.k8s.io"
            version: "v1" OR "v1beta1"
            kind: "ValidatingWebhookConfiguration"
    

#### Examples

##### require-admission-controller

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireAdmissionController
    metadata:
      name: require-admission-controller
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Namespace

###### Allowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      labels:
        pod-security.kubernetes.io/enforce: baseline
        pod-security.kubernetes.io/enforce-version: v1.28
      name: allowed-namespace

###### Disallowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: disallowed-namespace

### K8sRequireBinAuthZ

Requires Binary Authorization v1.0.2

Requires the Binary Authorization Validating Admission Webhook. Constraints using this `ConstraintTemplate` will be audit only regardless of `enforcementAction` value.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireBinAuthZ
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "admissionregistration.k8s.io"
            version: "v1" OR "v1beta1"
            kind: "ValidatingWebhookConfiguration"
    

#### Examples

##### require-binauthz

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireBinAuthZ
    metadata:
      name: require-binauthz
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Namespace

###### Allowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: default
    ---
    # Referential Data
    apiVersion: admissionregistration.k8s.io/v1
    kind: ValidatingWebhookConfiguration
    metadata:
      name: binauthz-admission-controller
    webhooks:
    - admissionReviewVersions:
      - v1
      - v1beta1
      clientConfig:
        url: https://binaryauthorization.googleapis.com/internal/projects/ap-bps-experimental-gke/policy/locations/us-central1/clusters/acm-test-cluster:admissionReview
      name: imagepolicywebhook.image-policy.k8s.io
      rules:
      - operations:
        - CREATE
        - UPDATE
      - apiVersion:
        - v1
      sideEffects: None

###### Disallowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: default

### K8sRequireCosNodeImage

Require COS Node Image v1.1.1

Enforces the use of Container-Optimized OS from Google on Nodes.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireCosNodeImage
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptOsImages <array>: A list of exempt OS Images.
        exemptOsImages:
          - <string>
    

#### Examples

##### nodes-have-consistent-time

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireCosNodeImage
    metadata:
      name: nodes-have-consistent-time
    spec:
      enforcementAction: dryrun
      parameters:
        exemptOsImages:
        - Debian
        - Ubuntu*

###### Allowed
    
    
    apiVersion: v1
    kind: Node
    metadata:
      name: allowed-example
    status:
      nodeInfo:
        osImage: Container-Optimized OS from Google
    
    
    apiVersion: v1
    kind: Node
    metadata:
      name: example-exempt
    status:
      nodeInfo:
        osImage: Debian
    
    
    apiVersion: v1
    kind: Node
    metadata:
      name: example-exempt-wildcard
    status:
      nodeInfo:
        osImage: Ubuntu 18.04.5 LTS

###### Disallowed
    
    
    apiVersion: v1
    kind: Node
    metadata:
      name: disallowed-example
    status:
      nodeInfo:
        osImage: Debian GNUv1.0

### K8sRequireDaemonsets

Required Daemonsets v1.1.2

Requires the list of daemonsets specified to be present.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireDaemonsets
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # requiredDaemonsets <array>: A list of names and namespaces of the
        # required daemonsets.
        requiredDaemonsets:
          - # name <string>: The name of the required daemonset.
            name: <string>
            # namespace <string>: The namespace for the required daemonset.
            namespace: <string>
        # restrictNodeSelector <boolean>: The daemonsets cannot include
        # `NodeSelector`.
        restrictNodeSelector: <boolean>
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "extensions"
            version: "v1beta1"
            kind: "DaemonSet"
          OR
          - group: "apps"
            version: "v1beta2" OR "v1"
            kind: "DaemonSet"
    

#### Examples

##### require-daemonset

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireDaemonsets
    metadata:
      name: require-daemonset
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Namespace
      parameters:
        requiredDaemonsets:
        - name: clamav
          namespace: pci-dss-av
        restrictNodeSelector: true

###### Allowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: pci-dss-av
    ---
    # Referential Data
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: other
      namespace: pci-dss-av
    spec:
      selector:
        matchLabels:
          name: other
      template:
        spec:
          containers:
          - image: us.gcr.io/{your-project-id}/other:latest
            name: other
    ---
    # Referential Data
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      labels:
        k8s-app: clamav-host-scanner
      name: clamav
      namespace: pci-dss-av
    spec:
      selector:
        matchLabels:
          name: clamav
      template:
        metadata:
          labels:
            name: clamav
        spec:
          containers:
          - image: us.gcr.io/{your-project-id}/clamav:latest
            livenessProbe:
              exec:
                command:
                - /health.sh
              initialDelaySeconds: 60
              periodSeconds: 30
            name: clamav-scanner
            resources:
              limits:
                memory: 3Gi
              requests:
                cpu: 500m
                memory: 2Gi
            volumeMounts:
            - mountPath: /data
              name: data-vol
            - mountPath: /host-fs
              name: host-fs
              readOnly: true
            - mountPath: /logs
              name: logs
          terminationGracePeriodSeconds: 30
          tolerations:
          - effect: NoSchedule
            key: node-role.kubernetes.io/master
          volumes:
          - emptyDir: {}
            name: data-vol
          - hostPath:
              path: /
            name: host-fs
          - hostPath:
              path: /var/log/clamav
            name: logs

###### Disallowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: pci-dss-av
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: pci-dss-av
    ---
    # Referential Data
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: other
      namespace: pci-dss-av
    spec:
      selector:
        matchLabels:
          name: other
      template:
        spec:
          containers:
          - image: us.gcr.io/{your-project-id}/other:latest
            name: other
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: pci-dss-av
    ---
    # Referential Data
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: clamav
      namespace: pci-dss-av
    spec:
      selector:
        matchLabels:
          name: clamav
      template:
        spec:
          containers:
          - image: us.gcr.io/{your-project-id}/other:latest
            name: clamav
          nodeSelector:
            cloud.google.com/gke-spot: "true"

### K8sRequireDefaultDenyEgressPolicy

Require Default Deny Egress Policy v1.0.3

Requires that every namespace defined in the cluster has a default deny NetworkPolicy for egress.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireDefaultDenyEgressPolicy
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "extensions"
            version: "v1beta1"
            kind: "NetworkPolicy"
          OR
          - group: "networking.k8s.io"
            version: "v1"
            kind: "NetworkPolicy"
    

#### Examples

##### require-default-deny-network-policies

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireDefaultDenyEgressPolicy
    metadata:
      name: require-default-deny-network-policies
    spec:
      enforcementAction: dryrun

###### Allowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: example-namespace
    ---
    # Referential Data
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: default-deny-egress
      namespace: example-namespace
    spec:
      podSelector: {}
      policyTypes:
      - Egress

###### Disallowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: example-namespace
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: example-namespace2
    ---
    # Referential Data
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: default-deny-egress
      namespace: example-namespace
    spec:
      podSelector: {}
      policyTypes:
      - Egress

### K8sRequireNamespaceNetworkPolicies

Require Namespace Network Policies v1.0.6

Requires that every namespace defined in the cluster has a NetworkPolicy.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireNamespaceNetworkPolicies
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "extensions"
            version: "v1beta1"
            kind: "NetworkPolicy"
          OR
          - group: "networking.k8s.io"
            version: "v1"
            kind: "NetworkPolicy"
    

#### Examples

##### require-namespace-network-policies-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireNamespaceNetworkPolicies
    metadata:
      name: require-namespace-network-policies-sample
    spec:
      enforcementAction: dryrun

###### Allowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: require-namespace-network-policies-example
    ---
    # Referential Data
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: test-network-policy
      namespace: require-namespace-network-policies-example

###### Disallowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: require-namespace-network-policies-example

### K8sRequireValidRangesForNetworks

Require Valid Ranges for Networks v1.0.2

Enforces which CIDR blocks are allowed for network ingress and egress.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireValidRangesForNetworks
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedEgress <array>: IP ranges in CIDR format (0.0.0.0/32) that are
        # allowed for egress.
        allowedEgress:
          - <string>
        # allowedIngress <array>: IP ranges in CIDR format (0.0.0.0/32) that are
        # allowed for ingress.
        allowedIngress:
          - <string>
    

#### Examples

##### require-valid-network-ranges

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequireValidRangesForNetworks
    metadata:
      name: require-valid-network-ranges
    spec:
      enforcementAction: dryrun
      parameters:
        allowedEgress:
        - 10.0.0.0/32
        allowedIngress:
        - 10.0.0.0/24

###### Allowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: test-network-policy
      namespace: default
    spec:
      egress:
      - ports:
        - port: 5978
          protocol: TCP
        to:
        - ipBlock:
            cidr: 10.0.0.0/32
      ingress:
      - from:
        - ipBlock:
            cidr: 10.0.0.0/29
        - ipBlock:
            cidr: 10.0.0.100/29
        - namespaceSelector:
            matchLabels:
              project: myproject
        - podSelector:
            matchLabels:
              role: frontend
        ports:
        - port: 6379
          protocol: TCP
      podSelector:
        matchLabels:
          role: db
      policyTypes:
      - Ingress
      - Egress

###### Disallowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: test-network-policy-disallowed
      namespace: default
    spec:
      egress:
      - ports:
        - port: 5978
          protocol: TCP
        to:
        - ipBlock:
            cidr: 1.1.2.0/31
      ingress:
      - from:
        - ipBlock:
            cidr: 1.1.2.0/24
        - ipBlock:
            cidr: 2.1.2.0/24
        - namespaceSelector:
            matchLabels:
              project: myproject
        - podSelector:
            matchLabels:
              role: frontend
        ports:
        - port: 6379
          protocol: TCP
      podSelector:
        matchLabels:
          role: db
      policyTypes:
      - Ingress
      - Egress

### K8sRequiredAnnotations

Required Annotations v1.0.1

Requires resources to contain specified annotations, with values matching provided regular expressions.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredAnnotations
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # annotations <array>: A list of annotations and values the object must
        # specify.
        annotations:
          - # allowedRegex <string>: If specified, a regular expression the
            # annotation's value must match. The value must contain at least one
            # match for the regular expression.
            allowedRegex: <string>
            # key <string>: The required annotation.
            key: <string>
        message: <string>
    

#### Examples

##### all-must-have-certain-set-of-annotations

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredAnnotations
    metadata:
      name: all-must-have-certain-set-of-annotations
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Service
      parameters:
        annotations:
        - allowedRegex: ^([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}|[a-z]{1,39})$
          key: a8r.io/owner
        - allowedRegex: ^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$
          key: a8r.io/runbook
        message: All services must have a `a8r.io/owner` and `a8r.io/runbook` annotations.

###### Allowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        a8r.io/owner: dev-team-alfa@contoso.com
        a8r.io/runbook: https://confluence.contoso.com/dev-team-alfa/runbooks
      name: allowed-service
    spec:
      ports:
      - name: http
        port: 80
        targetPort: 8080
      selector:
        app: foo

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: disallowed-service
    spec:
      ports:
      - name: http
        port: 80
        targetPort: 8080
      selector:
        app: foo

### K8sRequiredLabels

Required Labels v1.0.1

Requires resources to contain specified labels, with values matching provided regular expressions.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredLabels
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # labels <array>: A list of labels and values the object must specify.
        labels:
          - # allowedRegex <string>: If specified, a regular expression the
            # annotation's value must match. The value must contain at least one
            # match for the regular expression.
            allowedRegex: <string>
            # key <string>: The required label.
            key: <string>
        message: <string>
    

#### Examples

##### all-must-have-owner

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredLabels
    metadata:
      name: all-must-have-owner
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Namespace
      parameters:
        labels:
        - allowedRegex: ^[a-zA-Z]+.agilebank.demo$
          key: owner
        message: All namespaces must have an `owner` label that points to your company
          username

###### Allowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      labels:
        owner: user.agilebank.demo
      name: allowed-namespace

###### Disallowed
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: disallowed-namespace

### K8sRequiredProbes

Required Probes v1.0.1

Requires Pods to have readiness and/or liveness probes.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredProbes
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # probeTypes <array>: The probe must define a field listed in `probeType`
        # in order to satisfy the constraint (ex. `tcpSocket` satisfies
        # `['tcpSocket', 'exec']`)
        probeTypes:
          - <string>
        # probes <array>: A list of probes that are required (ex: `readinessProbe`)
        probes:
          - <string>
    

#### Examples

##### must-have-probes

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredProbes
    metadata:
      name: must-have-probes
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        probeTypes:
        - tcpSocket
        - httpGet
        - exec
        probes:
        - readinessProbe
        - livenessProbe

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: test-pod1
    spec:
      containers:
      - image: tomcat
        livenessProbe:
          initialDelaySeconds: 5
          periodSeconds: 10
          tcpSocket:
            port: 80
        name: tomcat
        ports:
        - containerPort: 8080
        readinessProbe:
          initialDelaySeconds: 5
          periodSeconds: 10
          tcpSocket:
            port: 8080
      volumes:
      - emptyDir: {}
        name: cache-volume

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: test-pod1
    spec:
      containers:
      - image: nginx:1.7.9
        name: nginx-1
        ports:
        - containerPort: 80
        volumeMounts:
        - mountPath: /tmp/cache
          name: cache-volume
      - image: tomcat
        name: tomcat
        ports:
        - containerPort: 8080
        readinessProbe:
          initialDelaySeconds: 5
          periodSeconds: 10
          tcpSocket:
            port: 8080
      volumes:
      - emptyDir: {}
        name: cache-volume
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: test-pod2
    spec:
      containers:
      - image: nginx:1.7.9
        livenessProbe:
          initialDelaySeconds: 5
          periodSeconds: 10
          tcpSocket:
            port: 80
        name: nginx-1
        ports:
        - containerPort: 80
        volumeMounts:
        - mountPath: /tmp/cache
          name: cache-volume
      - image: tomcat
        name: tomcat
        ports:
        - containerPort: 8080
        readinessProbe:
          initialDelaySeconds: 5
          periodSeconds: 10
          tcpSocket:
            port: 8080
      volumes:
      - emptyDir: {}
        name: cache-volume

### K8sRequiredResources

Required Resources v1.0.1

Requires containers to have defined resources set. https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredResources
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exemptImages <array>: Any container that uses an image that matches an
        # entry in this list will be excluded from enforcement. Prefix-matching can
        # be signified with `*`. For example: `my-image-*`. It is recommended that
        # users use the fully-qualified Docker image name (e.g. start with a domain
        # name) in order to avoid unexpectedly exempting images from an untrusted
        # repository.
        exemptImages:
          - <string>
        # limits <array>: A list of limits that should be enforced (`cpu`,
        # `memory`, or both).
        limits:
          # Allowed Values: cpu, memory
          - <string>
        # requests <array>: A list of requests that should be enforced (`cpu`,
        # `memory`, or both).
        requests:
          # Allowed Values: cpu, memory
          - <string>
    

#### Examples

##### container-must-have-limits-and-requests

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredResources
    metadata:
      name: container-must-have-limits-and-requests
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        limits:
        - cpu
        - memory
        requests:
        - cpu
        - memory

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 1Gi
          requests:
            cpu: 100m
            memory: 1Gi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          requests:
            cpu: 100m
            memory: 2Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            memory: 2Gi
          requests:
            cpu: 100m
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            memory: 2Gi

##### container-must-have-cpu-requests-memory-limits-and-requests

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredResources
    metadata:
      name: container-must-have-cpu-requests-memory-limits-and-requests
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        limits:
        - memory
        requests:
        - cpu
        - memory

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 1Gi
          requests:
            cpu: 100m
            memory: 1Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            memory: 2Gi
          requests:
            cpu: 100m
            memory: 2Gi

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          requests:
            cpu: 100m
            memory: 2Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            memory: 2Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources: {}

##### no-enforcements

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredResources
    metadata:
      name: no-enforcements
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-allowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            cpu: 100m
            memory: 1Gi
          requests:
            cpu: 100m
            memory: 1Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          requests:
            cpu: 100m
            memory: 2Gi
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources:
          limits:
            memory: 2Gi
          requests:
            cpu: 100m
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        owner: me.agilebank.demo
      name: opa-disallowed
    spec:
      containers:
      - args:
        - run
        - --server
        - --addr=localhost:8080
        image: openpolicyagent/opa:0.9.2
        name: opa
        resources: {}

### K8sRestrictAdmissionController

Restrict Admission Controller v1.0.0

Restrict dynamic admission controllers to permitted ones

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictAdmissionController
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # permittedMutatingWebhooks <array>: List of permitted mutating webhooks
        # (mutating admission controllers)
        permittedMutatingWebhooks:
          - <string>
        # permittedValidatingWebhooks <array>: List of permitted validating
        # webhooks (validating admission controllers)
        permittedValidatingWebhooks:
          - <string>
    

#### Examples

##### restrict-admission-controller

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictAdmissionController
    metadata:
      name: restrict-admission-controller
    spec:
      match:
        kinds:
        - apiGroups:
          - admissionregistration.k8s.io
          kinds:
          - MutatingWebhookConfiguration
          - ValidatingWebhookConfiguration
      parameters:
        permittedMutatingWebhooks:
        - allowed-mutating-webhook
        permittedValidatingWebhooks:
        - allowed-validating-webhook

###### Allowed
    
    
    apiVersion: admissionregistration.k8s.io/v1
    kind: ValidatingWebhookConfiguration
    metadata:
      name: allowed-validating-webhook

###### Disallowed
    
    
    apiVersion: admissionregistration.k8s.io/v1
    kind: ValidatingWebhookConfiguration
    metadata:
      name: disallowed-validating-webhook

### K8sRestrictAutomountServiceAccountTokens

Restrict Service Account Tokens v1.0.1

Restricts the use of service accounts tokens.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictAutomountServiceAccountTokens
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### restrict-serviceaccounttokens

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictAutomountServiceAccountTokens
    metadata:
      name: restrict-serviceaccounttokens
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
          - ServiceAccount

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: allowed-example-pod
    spec:
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: disallowed-example-serviceaccount

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: disallowed-example-pod
    spec:
      automountServiceAccountToken: true
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    automountServiceAccountToken: true
    kind: ServiceAccount
    metadata:
      name: allowed-example-serviceaccount

### K8sRestrictLabels

Restrict Labels v1.0.2

Disallows resources from containing specified labels unless there is an exception for the specific resource.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictLabels
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # exceptions <array>: Objects listed here are exempt from enforcement of
        # this constraint. All fields must be provided.
        exceptions:
          # <list item: object>: A single object's identification, based on group,
          # kind, namespace, and name.
          - # group <string>: The Kubernetes group of the exempt object.
            group: <string>
            # kind <string>: The Kubernetes kind of the exempt object.
            kind: <string>
            # name <string>: The name of the exempt object.
            name: <string>
            # namespace <string>: The namespace of the exempt object. For
            # cluster-scoped resources, use the empty string `""`.
            namespace: <string>
        # restrictedLabels <array>: A list of label keys strings.
        restrictedLabels:
          - <string>
    

#### Examples

##### restrict-label-example

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictLabels
    metadata:
      name: restrict-label-example
    spec:
      enforcementAction: dryrun
      parameters:
        exceptions:
        - group: ""
          kind: Pod
          name: allowed-example
          namespace: default
        restrictedLabels:
        - label-example

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        label-example: example
      name: allowed-example
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        label-example: example
      name: disallowed-example
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx

### K8sRestrictNamespaces

Restrict Namespaces v1.0.1

Restricts resources from using namespaces listed under the restrictedNamespaces parameter.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictNamespaces
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # restrictedNamespaces <array>: A list of Namespaces to restrict.
        restrictedNamespaces:
          - <string>
    

#### Examples

##### restrict-default-namespace-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictNamespaces
    metadata:
      name: restrict-default-namespace-sample
    spec:
      enforcementAction: dryrun
      parameters:
        restrictedNamespaces:
        - default

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: allowed-example
      namespace: test-namespace
    spec:
      containers:
      - image: nginx
        name: nginx

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: disallowed-example
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx

### K8sRestrictNfsUrls

Restrict NFS URLs v1.0.1

Disallows resources from containing NFS URLS unless specified.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictNfsUrls
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedNfsUrls <array>: A list of allowed NFS URLs
        allowedNfsUrls:
          - <string>
    

#### Examples

##### restrict-label-example

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictNfsUrls
    metadata:
      name: restrict-label-example
    spec:
      enforcementAction: dryrun
      parameters:
        allowedNfsUrls:
        - my-nfs-server.example.com/my-nfs-volume
        - my-nfs-server.example.com/my-wildcard-nfs-volume/*

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        label-example: example
      name: allowed-example
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        label-example: example
      name: allowed-example-nfs
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
      - name: test-volume
        nfs:
          path: /my-nfs-volume
          server: my-nfs-server.example.com
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        label-example: example
      name: allowed-example-nfs-wildcard
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
      - name: test-volume
        nfs:
          path: /my-nfs-volume/my-wildcard-nfs-volume/wildcard_matched_path
          server: my-nfs-server.example.com

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        label-example: example
      name: disallowed-example-nfs
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
      volumes:
      - name: test-volume
        nfs:
          path: /my-nfs-volume
          server: disallowed-nfs-server.example.com
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        label-example: example
      name: disallowed-example-nfs-mixed
      namespace: default
    spec:
      containers:
      - image: nginx
        name: nginx
      volumes:
      - name: test-volume-allowed
        nfs:
          path: /my-nfs-volume
          server: my-nfs-server.example.com
      - name: test-volume-disallowed
        nfs:
          path: /my-nfs-volume
          server: disallowed-nfs-server.example.com

### K8sRestrictRbacSubjects

Restrict RBAC Subjects v1.0.3

Restricts the use of names in RBAC subjects to permitted values.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictRbacSubjects
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedSubjects <array>: The list of names permitted in RBAC subjects.
        allowedSubjects:
          - # name <string>: The exact-name or the pattern of the allowed subject
            name: <string>
            # regexMatch <boolean>: The flag to allow a regular expression based
            # match on the name.
            regexMatch: <boolean>
    

#### Examples

##### restrict-rbac-subjects

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictRbacSubjects
    metadata:
      name: restrict-rbac-subjects
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - rbac.authorization.k8s.io
          kinds:
          - RoleBinding
          - ClusterRoleBinding
      parameters:
        allowedSubjects:
        - name: system:masters
        - name: ^.+@gcp-sa-[a-z-]+.iam.gserviceaccount.com$
          regexMatch: true
        - name: ^.+@system.gserviceaccount.com$
          regexMatch: true
        - name: ^.+@google.com$
          regexMatch: true

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: good-clusterrolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-admin
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: user@google.com
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:masters
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: service-1234567890@gcp-sa-ktd-control.iam.gserviceaccount.com

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: bad-clusterrolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-admin
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: user1@example.com
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: user2@example.com

### K8sRestrictRoleBindings

Restrict Role Bindings v1.0.3

Restricts the subjects specified in ClusterRoleBindings and RoleBindings to a list of allowed subjects.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictRoleBindings
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedSubjects <array>: The list of subjects that are allowed to bind to
        # the restricted role.
        allowedSubjects:
          - # apiGroup <string>: The Kubernetes API group of the subject.
            apiGroup: <string>
            # kind <string>: The Kubernetes kind of the subject.
            kind: <string>
            # name <string>: The name of the subject which is matched exactly as
            # provided as well as based on a regular expression.
            name: <string>
            # regexMatch <boolean>: The flag to allow a regular expression based
            # match on the name.
            regexMatch: <boolean>
        # restrictedRole <object>: The role that cannot be bound to unless
        # expressly allowed.
        restrictedRole:
          # apiGroup <string>: The Kubernetes API group of the role.
          apiGroup: <string>
          # kind <string>: The Kubernetes kind of the role.
          kind: <string>
          # name <string>: The name of the role.
          name: <string>
    

#### Examples

##### restrict-clusteradmin-rolebindings-sample

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictRoleBindings
    metadata:
      name: restrict-clusteradmin-rolebindings-sample
    spec:
      enforcementAction: dryrun
      parameters:
        allowedSubjects:
        - apiGroup: rbac.authorization.k8s.io
          kind: Group
          name: system:masters
        restrictedRole:
          apiGroup: rbac.authorization.k8s.io
          kind: ClusterRole
          name: cluster-admin

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: good-clusterrolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-admin
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:masters

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: bad-clusterrolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-admin
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: Group
      name: system:unauthenticated

##### restrict-clusteradmin-rolebindings-regex

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictRoleBindings
    metadata:
      name: restrict-clusteradmin-rolebindings-regex
    spec:
      enforcementAction: dryrun
      parameters:
        allowedSubjects:
        - apiGroup: rbac.authorization.k8s.io
          kind: User
          name: ^service-[0-9]+@gcp-sa-anthosconfigmanagement.iam.gserviceaccount.com$
          regexMatch: true
        restrictedRole:
          apiGroup: rbac.authorization.k8s.io
          kind: ClusterRole
          name: cluster-admin

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: good-clusterrolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-admin
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: service-123456789@gcp-sa-anthosconfigmanagement.iam.gserviceaccount.com

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: bad-clusterrolebinding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-admin
    subjects:
    - apiGroup: rbac.authorization.k8s.io
      kind: User
      name: someotherservice-123456789@gcp-sa-anthosconfigmanagement.iam.gserviceaccount.com

### K8sRestrictRoleRules

Restrict Role and ClusterRole rules. v1.0.4

Restricts rules that can be set on Role and ClusterRole objects.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictRoleRules
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedRules <array>: AllowedRules is the list of rules that are allowed
        # on Role or ClusterRole objects. If set, any item off this list will be
        # rejected.
        allowedRules:
          - # apiGroups <array>: APIGroups is the name of the APIGroup that
            # contains the resources. If multiple API groups are specified, any
            # action requested against one of the enumerated resources in any API
            # group will be allowed. "" represents the core API group and "*"
            # represents all API groups.
            apiGroups:
              - <string>
            # resources <array>: Resources is a list of resources this rule
            # applies to. '*' represents all resources.
            resources:
              - <string>
            # verbs <array>: Verbs is a list of Verbs that apply to ALL the
            # ResourceKinds contained in this rule. '*' represents all verbs.
            verbs:
              - <string>
        # disallowedRules <array>: DisallowedRules is the list of rules that are
        # NOT allowed on Role or ClusterRole objects. If set, any item on this list
        # will be rejected.
        disallowedRules:
          - # apiGroups <array>: APIGroups is the name of the APIGroup that
            # contains the resources. If multiple API groups are specified, any
            # action requested against one of the enumerated resources in any API
            # group will be disallowed. "" represents the core API group and "*"
            # represents all API groups.
            apiGroups:
              - <string>
            # resources <array>: Resources is a list of resources this rule
            # applies to. '*' represents all resources.
            resources:
              - <string>
            # verbs <array>: Verbs is a list of Verbs that apply to ALL the
            # ResourceKinds contained in this rule. '*' represents all verbs.
            verbs:
              - <string>
        # exemptions <object>: Exemptions is the list of Roles and/or ClusterRoles
        # names that are allowed to violate this policy.
        exemptions:
          clusterRoles:
            - # name <string>: Name is the name or a pattern of the ClusterRole
              # to be exempted.
              name: <string>
              # regexMatch <boolean>: RegexMatch is the flag to toggle exact vs
              # regex match of the ClusterRole name.
              regexMatch: <boolean>
          roles:
            - # name <string>: Name is the name of the Role to be exempted.
              name: <string>
              # namespace <string>: Namespace is the namespace of the Role to be
              # exempted.
              namespace: <string>
    

#### Examples

##### restrict-pods-exec

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRestrictRoleRules
    metadata:
      name: restrict-pods-exec
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - rbac.authorization.k8s.io
          kinds:
          - Role
          - ClusterRole
      parameters:
        disallowedRules:
        - apiGroups:
          - ""
          resources:
          - pods/exec
          verbs:
          - create

###### Allowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      name: allowed-role-example
    rules:
    - apiGroups:
      - ""
      resources:
      - pods
      verbs:
      - get
      - list
      - watch

###### Disallowed
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: disallowed-cluster-role-example
    rules:
    - apiGroups:
      - ""
      resources:
      - pods/exec
      verbs:
      - '*'

### K8sStorageClass

Storage Class v1.1.2

Requires storage classes to be specified when used. Only Gatekeeper 3.9+ and non-ephemeral containers are supported.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sStorageClass
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedStorageClasses <array>: An optional allow-list of storage classes.
        #  If specified, any storage class not in the `allowedStorageClasses`
        # parameter is disallowed.
        allowedStorageClasses:
          - <string>
        includeStorageClassesInMessage: <boolean>
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "storage.k8s.io"
            version: "v1"
            kind: "StorageClass"
    

#### Examples

##### storageclass

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sStorageClass
    metadata:
      name: storageclass
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - PersistentVolumeClaim
        - apiGroups:
          - apps
          kinds:
          - StatefulSet
      parameters:
        includeStorageClassesInMessage: true

###### Allowed
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: ok
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 8Gi
      storageClassName: somestorageclass
      volumeMode: Filesystem
    ---
    # Referential Data
    allowVolumeExpansion: true
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: somestorageclass
    provisioner: foo
    
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: volumeclaimstorageclass
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: volumeclaimstorageclass
      serviceName: volumeclaimstorageclass
      template:
        metadata:
          labels:
            app: volumeclaimstorageclass
        spec:
          containers:
          - image: registry.k8s.io/nginx-slim:0.8
            name: main
            volumeMounts:
            - mountPath: /usr/share/nginx/html
              name: data
      volumeClaimTemplates:
      - metadata:
          name: data
        spec:
          accessModes:
          - ReadWriteOnce
          resources:
            requests:
              storage: 1Gi
          storageClassName: somestorageclass
    ---
    # Referential Data
    allowVolumeExpansion: true
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: somestorageclass
    provisioner: foo

###### Disallowed
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: badstorageclass
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 8Gi
      storageClassName: badstorageclass
      volumeMode: Filesystem
    
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: badvolumeclaimstorageclass
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: badvolumeclaimstorageclass
      serviceName: badvolumeclaimstorageclass
      template:
        metadata:
          labels:
            app: badvolumeclaimstorageclass
        spec:
          containers:
          - image: registry.k8s.io/nginx-slim:0.8
            name: main
            volumeMounts:
            - mountPath: /usr/share/nginx/html
              name: data
      volumeClaimTemplates:
      - metadata:
          name: data
        spec:
          accessModes:
          - ReadWriteOnce
          resources:
            requests:
              storage: 1Gi
          storageClassName: badstorageclass
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: nostorageclass
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 8Gi
      volumeMode: Filesystem
    
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: novolumeclaimstorageclass
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: novolumeclaimstorageclass
      serviceName: novolumeclaimstorageclass
      template:
        metadata:
          labels:
            app: novolumeclaimstorageclass
        spec:
          containers:
          - image: registry.k8s.io/nginx-slim:0.8
            name: main
            volumeMounts:
            - mountPath: /usr/share/nginx/html
              name: data
      volumeClaimTemplates:
      - metadata:
          name: data
        spec:
          accessModes:
          - ReadWriteOnce
          resources:
            requests:
              storage: 1Gi

##### allowed-storageclass

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sStorageClass
    metadata:
      name: allowed-storageclass
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - PersistentVolumeClaim
        - apiGroups:
          - apps
          kinds:
          - StatefulSet
      parameters:
        allowedStorageClasses:
        - allowed-storage-class
        includeStorageClassesInMessage: true

###### Allowed
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: allowed-storage-class-pvc
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 8Gi
      storageClassName: allowed-storage-class
      volumeMode: Filesystem
    ---
    # Referential Data
    allowVolumeExpansion: true
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: allowed-storage-class
    provisioner: foo

###### Disallowed
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: disallowed-storage-class-pvc
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 8Gi
      storageClassName: disallowed-storage-class
      volumeMode: Filesystem
    ---
    # Referential Data
    allowVolumeExpansion: true
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: allowed-storage-class
    provisioner: foo

### K8sUniqueIngressHost

Unique Ingress Host v1.0.4

Requires all Ingress rule hosts to be unique. Does not handle hostname wildcards: https://kubernetes.io/docs/concepts/services-networking/ingress/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sUniqueIngressHost
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: "extensions"
            version: "v1beta1"
            kind: "Ingress"
          OR
          - group: "networking.k8s.io"
            version: "v1beta1" OR "v1"
            kind: "Ingress"
    

#### Examples

##### unique-ingress-host

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sUniqueIngressHost
    metadata:
      name: unique-ingress-host
    spec:
      match:
        kinds:
        - apiGroups:
          - extensions
          - networking.k8s.io
          kinds:
          - Ingress

###### Allowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: ingress-host-allowed
      namespace: default
    spec:
      rules:
      - host: example-allowed-host.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix
      - host: example-allowed-host1.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx2
                port:
                  number: 80
            path: /
            pathType: Prefix

###### Disallowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: ingress-host-disallowed
      namespace: default
    spec:
      rules:
      - host: example-host.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix
    ---
    # Referential Data
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: ingress-host-example
      namespace: default
    spec:
      rules:
      - host: example-host.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: ingress-host-disallowed2
      namespace: default
    spec:
      rules:
      - host: example-host2.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix
      - host: example-host3.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx2
                port:
                  number: 80
            path: /
            pathType: Prefix
    ---
    # Referential Data
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: ingress-host-example2
      namespace: default
    spec:
      rules:
      - host: example-host2.example.com
        http:
          paths:
          - backend:
              service:
                name: nginx
                port:
                  number: 80
            path: /
            pathType: Prefix

### K8sUniqueServiceSelector

Unique Service Selector v1.0.2

Requires Services to have unique selectors within a namespace. Selectors are considered the same if they have identical keys and values. Selectors may share a key/value pair so long as there is at least one distinct key/value pair between them. https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sUniqueServiceSelector
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Referential Constraint

This constraint is referential. Prior to use, you must [enable referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential) and [create a config](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#gatekeeper-config) that tells Policy Controller what kinds of objects to watch.

Your Policy Controller `Config` will require a `syncOnly` entry similar to:
    
    
    spec:
      sync:
        syncOnly:
          - group: ""
            version: "v1"
            kind: "Service"
    

#### Examples

##### unique-service-selector

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sUniqueServiceSelector
    metadata:
      labels:
        owner: admin.agilebank.demo
      name: unique-service-selector

###### Allowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: gatekeeper-test-service-disallowed
      namespace: default
    spec:
      ports:
      - port: 443
      selector:
        key: other-value

###### Disallowed
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: gatekeeper-test-service-disallowed
      namespace: default
    spec:
      ports:
      - port: 443
      selector:
        key: value
    ---
    # Referential Data
    apiVersion: v1
    kind: Service
    metadata:
      name: gatekeeper-test-service-example
      namespace: default
    spec:
      ports:
      - port: 443
      selector:
        key: value

### NoUpdateServiceAccount

Block updating Service Account v1.0.1

Blocks updating the service account on resources that abstract over Pods. This policy is ignored in audit mode.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: NoUpdateServiceAccount
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedGroups <array>: Groups that should be allowed to bypass the
        # policy.
        allowedGroups:
          - <string>
        # allowedUsers <array>: Users that should be allowed to bypass the policy.
        allowedUsers:
          - <string>
    

#### Examples

##### no-update-kube-system-service-account

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: NoUpdateServiceAccount
    metadata:
      name: no-update-kube-system-service-account
    spec:
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - ReplicationController
        - apiGroups:
          - apps
          kinds:
          - ReplicaSet
          - Deployment
          - StatefulSet
          - DaemonSet
        - apiGroups:
          - batch
          kinds:
          - CronJob
        namespaces:
        - kube-system
      parameters:
        allowedGroups: []
        allowedUsers: []

###### Allowed
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: policy-test
      name: policy-test
      namespace: kube-system
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: policy-test-deploy
      template:
        metadata:
          labels:
            app: policy-test-deploy
        spec:
          containers:
          - command:
            - /bin/bash
            - -c
            - sleep 99999
            image: ubuntu
            name: policy-test
          serviceAccountName: policy-test-sa-1

### PolicyStrictOnly

Require STRICT Istio mTLS Policy v1.0.4

Requires that `STRICT` Istio mutual TLS is always specified when using [PeerAuthentication](https://istio.io/latest/docs/reference/config/security/peer_authentication/). This constraint also ensures that the deprecated [Policy](https://istio.io/v1.4/docs/reference/config/security/istio.authentication.v1alpha1/#Policy) and MeshPolicy resources enforce `STRICT` mutual TLS. See: https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/#lock-down-mutual-tls-for-the-entire-mesh

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: PolicyStrictOnly
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### peerauthentication-strict-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: PolicyStrictOnly
    metadata:
      name: peerauthentication-strict-constraint
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - PeerAuthentication
        namespaces:
        - default

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mode-strict
      namespace: default
    spec:
      mtls:
        mode: STRICT
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mode-strict-port-level
      namespace: default
    spec:
      mtls:
        mode: STRICT
      portLevelMtls:
        "8080":
          mode: STRICT
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mode-strict-port-unset
      namespace: default
    spec:
      mtls:
        mode: STRICT
      portLevelMtls:
        "8080":
          mode: UNSET

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: empty-mtls
      namespace: default
    spec:
      mtls: {}
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: unspecified-mtls
      namespace: default
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mode-null
      namespace: default
    spec:
      mtls:
        mode: null
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mtls-null
      namespace: default
    spec:
      mtls: null
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mode-permissive
      namespace: default
    spec:
      mtls:
        mode: PERMISSIVE
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mode-strict-port-permissive
      namespace: default
    spec:
      mtls:
        mode: STRICT
      portLevelMtls:
        "8080":
          mode: PERMISSIVE
    
    
    apiVersion: security.istio.io/v1beta1
    kind: PeerAuthentication
    metadata:
      name: mode-strict-port-permissive
      namespace: default
    spec:
      mtls:
        mode: STRICT
      portLevelMtls:
        "8080":
          mode: PERMISSIVE
        "8081":
          mode: STRICT

##### deprecated-policy-strict-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: PolicyStrictOnly
    metadata:
      name: deprecated-policy-strict-constraint
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - authentication.istio.io
          kinds:
          - Policy
        namespaces:
        - default

###### Allowed
    
    
    apiVersion: authentication.istio.io/v1alpha1
    kind: Policy
    metadata:
      name: default-mode-strict
      namespace: default
    spec:
      peers:
      - mtls:
          mode: STRICT

###### Disallowed
    
    
    apiVersion: authentication.istio.io/v1alpha1
    kind: Policy
    metadata:
      name: default-mtls-empty
      namespace: default
    spec:
      peers:
      - mtls: {}
    
    
    apiVersion: authentication.istio.io/v1alpha1
    kind: Policy
    metadata:
      name: default-mtls-null
      namespace: default
    spec:
      peers:
      - mtls: null
    
    
    apiVersion: authentication.istio.io/v1alpha1
    kind: Policy
    metadata:
      name: peers-empty
      namespace: default
    spec:
      peers: []
    
    
    apiVersion: authentication.istio.io/v1alpha1
    kind: Policy
    metadata:
      name: policy-no-peers
      namespace: default
    spec:
      targets:
      - name: httpbin
    
    
    apiVersion: authentication.istio.io/v1alpha1
    kind: Policy
    metadata:
      name: policy-permissive
      namespace: default
    spec:
      peers:
      - mtls:
          mode: PERMISSIVE

### RestrictNetworkExclusions

Restrict Network Exclusions v1.0.2

Controls which inbound ports, outbound ports, and outbound IP ranges can be excluded from Istio network capture. Ports and IP ranges that bypass Istio network capture are not handled by the Istio proxy and are not subject to Istio mTLS authentication, authorization policy, and other Istio features. This constraint can be used to apply restrictions to the use of the following annotations:

  * `traffic.sidecar.istio.io/excludeInboundPorts`
  * `traffic.sidecar.istio.io/excludeOutboundPorts`
  * `traffic.sidecar.istio.io/excludeOutboundIPRanges`



See https://istio.io/latest/docs/reference/config/annotations/.

When restricting outbound IP ranges, the constraint calculates whether excluded IP ranges match or are a subset of the allowed IP range exclusions.

When using this constraint all inbound ports, outbound ports and outbound IP ranges must always be included by either setting the corresponding "include" annotations to `"*"` or leaving them unset. Setting any of the following annotations to anything other than `"*"` is not allowed:

  * `traffic.sidecar.istio.io/includeInboundPorts`
  * `traffic.sidecar.istio.io/includeOutboundPorts`
  * `traffic.sidecar.istio.io/includeOutboundIPRanges`



This constraint always allows port 15020 to be excluded because the Istio sidecar injector always adds it to the `traffic.sidecar.istio.io/excludeInboundPorts` annotation so that it can be used for health checking.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: RestrictNetworkExclusions
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # allowedInboundPortExclusions <array>: A list of ports that this
        # constraint will allow in the
        # `traffic.sidecar.istio.io/excludeInboundPorts` annotation.
        allowedInboundPortExclusions:
          - <string>
        # allowedOutboundIPRangeExclusions <array>: A list of IP ranges that this
        # constraint will allow in the
        # `traffic.sidecar.istio.io/excludeOutboundIPRanges` annotation. The
        # constraint calculates whether excluded IP ranges match or are a subset of
        # the ranges in this list.
        allowedOutboundIPRangeExclusions:
          - <string>
        # allowedOutboundPortExclusions <array>: A list of ports that this
        # constraint will allow in the
        # `traffic.sidecar.istio.io/excludeOutboundPorts` annotation.
        allowedOutboundPortExclusions:
          - <string>
    

#### Examples

##### restrict-network-exclusions

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: RestrictNetworkExclusions
    metadata:
      name: restrict-network-exclusions
    spec:
      enforcementAction: deny
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        allowedInboundPortExclusions:
        - "80"
        allowedOutboundIPRangeExclusions:
        - 169.254.169.254/32
        allowedOutboundPortExclusions:
        - "8888"

###### Allowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        app: nginx
      name: nothing-excluded
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        traffic.sidecar.istio.io/excludeInboundPorts: "80"
        traffic.sidecar.istio.io/excludeOutboundIPRanges: 169.254.169.254/32
        traffic.sidecar.istio.io/excludeOutboundPorts: "8888"
      labels:
        app: nginx
      name: allowed-port-and-ip-exclusions
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        traffic.sidecar.istio.io/excludeOutboundIPRanges: 169.254.169.254/32
        traffic.sidecar.istio.io/includeOutboundIPRanges: '*'
      labels:
        app: nginx
      name: all-ip-ranges-included-with-one-allowed-ip-excluded
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        traffic.sidecar.istio.io/includeInboundPorts: '*'
        traffic.sidecar.istio.io/includeOutboundIPRanges: '*'
        traffic.sidecar.istio.io/includeOutboundPorts: '*'
      labels:
        app: nginx
      name: everything-included-with-no-exclusions
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80

###### Disallowed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        traffic.sidecar.istio.io/excludeOutboundIPRanges: 1.1.2.0/24
      labels:
        app: nginx
      name: disallowed-ip-range-exclusion
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
        - containerPort: 443
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        traffic.sidecar.istio.io/excludeOutboundIPRanges: 169.254.169.254/32,1.1.2.0/24
      labels:
        app: nginx
      name: one-disallowed-ip-exclusion-and-one-allowed-exclusion
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
        - containerPort: 443
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      annotations:
        traffic.sidecar.istio.io/includeInboundPorts: 80,443
        traffic.sidecar.istio.io/includeOutboundIPRanges: 169.254.169.254/32
        traffic.sidecar.istio.io/includeOutboundPorts: "8888"
      labels:
        app: nginx
      name: disallowed-specific-port-and-ip-inclusions
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80

### SourceNotAllAuthz

Require Istio AuthorizationPolicy Source not all v1.0.1

Requires that Istio AuthorizationPolicy rules have source principals set to something other than "*". https://istio.io/latest/docs/reference/config/security/authorization-policy/

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: SourceNotAllAuthz
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
    

#### Examples

##### sourcenotall-authz-constraint

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: SourceNotAllAuthz
    metadata:
      name: sourcenotall-authz-constraint
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - security.istio.io
          kinds:
          - AuthorizationPolicy

###### Allowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: source-principals-good
      namespace: foo
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/sleep
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
          version: v1

###### Disallowed
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: source-principals-dne
      namespace: foo
    spec:
      rules:
      - from:
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
          version: v1
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: source-principals-all
      namespace: foo
    spec:
      rules:
      - from:
        - source:
            principals:
            - '*'
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
          version: v1
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: source-principals-someall
      namespace: foo
    spec:
      rules:
      - from:
        - source:
            principals:
            - cluster.local/ns/default/sa/sleep
            - '*'
        - source:
            namespaces:
            - test
        to:
        - operation:
            methods:
            - GET
            paths:
            - /info*
        - operation:
            methods:
            - POST
            paths:
            - /data
        when:
        - key: request.auth.claims[iss]
          values:
          - https://accounts.google.com
      selector:
        matchLabels:
          app: httpbin
          version: v1

### VerifyDeprecatedAPI

Verify deprecated APIs v1.0.0

Verifies deprecated Kubernetes APIs to ensure all the API versions are up to date. This template does not apply to audit as audit looks at the resources which are already present in the cluster with non-deprecated API versions.

#### Constraint schema
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: VerifyDeprecatedAPI
    metadata:
      name: example
    spec:
      # match <object>: lets you configure which resources are in scope for this
      # constraint. For more information, see the Policy Controller Constraint
      # match documentation:
      # https://cloud.google.com/anthos-config-management/docs/reference/match
      match:
        [match schema]
      parameters:
        # k8sVersion <number>: kubernetes version
        k8sVersion: <number>
        # kvs <array>: Deprecated api versions and corresponding kinds
        kvs:
          - # deprecatedAPI <string>: deprecated api
            deprecatedAPI: <string>
            # kinds <array>: impacted list of kinds
            kinds:
              - <string>
            # targetAPI <string>: target api
            targetAPI: <string>
    

#### Examples

##### verify-1.16

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: VerifyDeprecatedAPI
    metadata:
      name: verify-1.16
    spec:
      match:
        kinds:
        - apiGroups:
          - apps
          kinds:
          - Deployment
          - ReplicaSet
          - StatefulSet
          - DaemonSet
        - apiGroups:
          - extensions
          kinds:
          - PodSecurityPolicy
          - ReplicaSet
          - Deployment
          - DaemonSet
          - NetworkPolicy
      parameters:
        k8sVersion: 1.16
        kvs:
        - deprecatedAPI: apps/v1beta1
          kinds:
          - Deployment
          - ReplicaSet
          - StatefulSet
          targetAPI: apps/v1
        - deprecatedAPI: extensions/v1beta1
          kinds:
          - ReplicaSet
          - Deployment
          - DaemonSet
          targetAPI: apps/v1
        - deprecatedAPI: extensions/v1beta1
          kinds:
          - PodSecurityPolicy
          targetAPI: policy/v1beta1
        - deprecatedAPI: apps/v1beta2
          kinds:
          - ReplicaSet
          - StatefulSet
          - Deployment
          - DaemonSet
          targetAPI: apps/v1
        - deprecatedAPI: extensions/v1beta1
          kinds:
          - NetworkPolicy
          targetAPI: networking.k8s.io/v1

###### Allowed
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: allowed-deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80

###### Disallowed
    
    
    apiVersion: apps/v1beta1
    kind: Deployment
    metadata:
      labels:
        app: nginx
      name: disallowed-deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - image: nginx:1.14.2
            name: nginx
            ports:
            - containerPort: 80

##### verify-1.22

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: VerifyDeprecatedAPI
    metadata:
      name: verify-1.22
    spec:
      match:
        kinds:
        - apiGroups:
          - admissionregistration.k8s.io
          kinds:
          - MutatingWebhookConfiguration
          - ValidatingWebhookConfiguration
        - apiGroups:
          - apiextensions.k8s.io
          kinds:
          - CustomResourceDefinition
        - apiGroups:
          - apiregistration.k8s.io
          kinds:
          - APIService
        - apiGroups:
          - authentication.k8s.io
          kinds:
          - TokenReview
        - apiGroups:
          - authorization.k8s.io
          kinds:
          - SubjectAccessReview
        - apiGroups:
          - certificates.k8s.io
          kinds:
          - CertificateSigningRequest
        - apiGroups:
          - coordination.k8s.io
          kinds:
          - Lease
        - apiGroups:
          - extensions
          - networking.k8s.io
          kinds:
          - Ingress
        - apiGroups:
          - networking.k8s.io
          kinds:
          - IngressClass
        - apiGroups:
          - rbac.authorization.k8s.io
          kinds:
          - ClusterRole
          - ClusterRoleBinding
          - Role
          - RoleBinding
        - apiGroups:
          - scheduling.k8s.io
          kinds:
          - PriorityClass
        - apiGroups:
          - storage.k8s.io
          kinds:
          - CSIDriver
          - CSINode
          - StorageClass
          - VolumeAttachment
      parameters:
        k8sVersion: 1.22
        kvs:
        - deprecatedAPI: admissionregistration.k8s.io/v1beta1
          kinds:
          - MutatingWebhookConfiguration
          - ValidatingWebhookConfiguration
          targetAPI: admissionregistration.k8s.io/v1
        - deprecatedAPI: apiextensions.k8s.io/v1beta1
          kinds:
          - CustomResourceDefinition
          targetAPI: apiextensions.k8s.io/v1
        - deprecatedAPI: apiregistration.k8s.io/v1beta1
          kinds:
          - APIService
          targetAPI: apiregistration.k8s.io/v1
        - deprecatedAPI: authentication.k8s.io/v1beta1
          kinds:
          - TokenReview
          targetAPI: authentication.k8s.io/v1
        - deprecatedAPI: authorization.k8s.io/v1beta1
          kinds:
          - SubjectAccessReview
          targetAPI: authorization.k8s.io/v1
        - deprecatedAPI: certificates.k8s.io/v1beta1
          kinds:
          - CertificateSigningRequest
          targetAPI: certificates.k8s.io/v1
        - deprecatedAPI: coordination.k8s.io/v1beta1
          kinds:
          - Lease
          targetAPI: coordination.k8s.io/v1
        - deprecatedAPI: extensions/v1beta1
          kinds:
          - Ingress
          targetAPI: networking.k8s.io/v1
        - deprecatedAPI: networking.k8s.io/v1beta1
          kinds:
          - Ingress
          - IngressClass
          targetAPI: networking.k8s.io/v1
        - deprecatedAPI: rbac.authorization.k8s.io/v1beta1
          kinds:
          - ClusterRole
          - ClusterRoleBinding
          - Role
          - RoleBinding
          targetAPI: rbac.authorization.k8s.io/v1
        - deprecatedAPI: scheduling.k8s.io/v1beta1
          kinds:
          - PriorityClass
          targetAPI: scheduling.k8s.io/v1
        - deprecatedAPI: storage.k8s.io/v1beta1
          kinds:
          - CSIDriver
          - CSINode
          - StorageClass
          - VolumeAttachment
          targetAPI: storage.k8s.io/v1

###### Allowed
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      annotations:
        nginx.ingress.kubernetes.io/rewrite-target: /
      name: allowed-ingress
    spec:
      ingressClassName: nginx-example
      rules:
      - http:
          paths:
          - backend:
              service:
                name: test
                port:
                  number: 80
            path: /testpath
            pathType: Prefix

###### Disallowed
    
    
    apiVersion: networking.k8s.io/v1beta1
    kind: Ingress
    metadata:
      annotations:
        nginx.ingress.kubernetes.io/rewrite-target: /
      name: disallowed-ingress
    spec:
      ingressClassName: nginx-example
      rules:
      - http:
          paths:
          - backend:
              service:
                name: test
                port:
                  number: 80
            path: /testpath
            pathType: Prefix

##### verify-1.25

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: VerifyDeprecatedAPI
    metadata:
      name: verify-1.25
    spec:
      match:
        kinds:
        - apiGroups:
          - batch
          kinds:
          - CronJob
        - apiGroups:
          - discovery.k8s.io
          kinds:
          - EndpointSlice
        - apiGroups:
          - events.k8s.io
          kinds:
          - Event
        - apiGroups:
          - autoscaling
          kinds:
          - HorizontalPodAutoscaler
        - apiGroups:
          - policy
          kinds:
          - PodDisruptionBudget
          - PodSecurityPolicy
        - apiGroups:
          - node.k8s.io
          kinds:
          - RuntimeClass
      parameters:
        k8sVersion: 1.25
        kvs:
        - deprecatedAPI: batch/v1beta1
          kinds:
          - CronJob
          targetAPI: batch/v1
        - deprecatedAPI: discovery.k8s.io/v1beta1
          kinds:
          - EndpointSlice
          targetAPI: discovery.k8s.io/v1
        - deprecatedAPI: events.k8s.io/v1beta1
          kinds:
          - Event
          targetAPI: events.k8s.io/v1
        - deprecatedAPI: autoscaling/v2beta1
          kinds:
          - HorizontalPodAutoscaler
          targetAPI: autoscaling/v2
        - deprecatedAPI: policy/v1beta1
          kinds:
          - PodDisruptionBudget
          targetAPI: policy/v1
        - deprecatedAPI: policy/v1beta1
          kinds:
          - PodSecurityPolicy
          targetAPI: None
        - deprecatedAPI: node.k8s.io/v1beta1
          kinds:
          - RuntimeClass
          targetAPI: node.k8s.io/v1

###### Allowed
    
    
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: allowed-cronjob
      namespace: default
    spec:
      jobTemplate:
        spec:
          template:
            spec:
              containers:
              - command:
                - /bin/sh
                - -c
                - date; echo Hello from the Kubernetes cluster
                image: busybox:1.28
                imagePullPolicy: IfNotPresent
                name: hello
              restartPolicy: OnFailure
      schedule: '* * * * *'

###### Disallowed
    
    
    apiVersion: batch/v1beta1
    kind: CronJob
    metadata:
      name: disallowed-cronjob
      namespace: default
    spec:
      jobTemplate:
        spec:
          template:
            spec:
              containers:
              - command:
                - /bin/sh
                - -c
                - date; echo Hello from the Kubernetes cluster
                image: busybox:1.28
                imagePullPolicy: IfNotPresent
                name: hello
              restartPolicy: OnFailure
      schedule: '* * * * *'

##### verify-1.26

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: VerifyDeprecatedAPI
    metadata:
      name: verify-1.26
    spec:
      match:
        kinds:
        - apiGroups:
          - flowcontrol.apiserver.k8s.io
          kinds:
          - FlowSchema
          - PriorityLevelConfiguration
        - apiGroups:
          - autoscaling
          kinds:
          - HorizontalPodAutoscaler
      parameters:
        k8sVersion: 1.26
        kvs:
        - deprecatedAPI: flowcontrol.apiserver.k8s.io/v1beta1
          kinds:
          - FlowSchema
          - PriorityLevelConfiguration
          targetAPI: flowcontrol.apiserver.k8s.io/v1beta3
        - deprecatedAPI: autoscaling/v2beta2
          kinds:
          - HorizontalPodAutoscaler
          targetAPI: autoscaling/v2

###### Allowed
    
    
    apiVersion: flowcontrol.apiserver.k8s.io/v1beta3
    kind: FlowSchema
    metadata:
      name: allowed-flowcontrol
      namespace: default
    spec:
      matchingPrecedence: 1000
      priorityLevelConfiguration:
        name: exempt
      rules:
      - nonResourceRules:
        - nonResourceURLs:
          - /healthz
          - /livez
          - /readyz
          verbs:
          - '*'
        subjects:
        - group:
            name: system:unauthenticated
          kind: Group

###### Disallowed
    
    
    apiVersion: flowcontrol.apiserver.k8s.io/v1beta1
    kind: FlowSchema
    metadata:
      name: disallowed-flowcontrol
      namespace: default
    spec:
      matchingPrecedence: 1000
      priorityLevelConfiguration:
        name: exempt
      rules:
      - nonResourceRules:
        - nonResourceURLs:
          - /healthz
          - /livez
          - /readyz
          verbs:
          - '*'
        subjects:
        - group:
            name: system:unauthenticated
          kind: Group

##### verify-1.27

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: VerifyDeprecatedAPI
    metadata:
      name: verify-1.27
    spec:
      match:
        kinds:
        - apiGroups:
          - storage.k8s.io
          kinds:
          - CSIStorageCapacity
      parameters:
        k8sVersion: 1.27
        kvs:
        - deprecatedAPI: storage.k8s.io/v1beta1
          kinds:
          - CSIStorageCapacity
          targetAPI: storage.k8s.io/v1

###### Allowed
    
    
    apiVersion: storage.k8s.io/v1
    kind: CSIStorageCapacity
    metadata:
      name: allowed-csistoragecapacity
    storageClassName: standard

###### Disallowed
    
    
    apiVersion: storage.k8s.io/v1beta1
    kind: CSIStorageCapacity
    metadata:
      name: allowed-csistoragecapacity
      namespace: default
    storageClassName: standard

##### verify-1.29

###### Constraint
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: VerifyDeprecatedAPI
    metadata:
      name: verify-1.29
    spec:
      match:
        kinds:
        - apiGroups:
          - flowcontrol.apiserver.k8s.io
          kinds:
          - FlowSchema
          - PriorityLevelConfiguration
      parameters:
        k8sVersion: 1.29
        kvs:
        - deprecatedAPI: flowcontrol.apiserver.k8s.io/v1beta2
          kinds:
          - FlowSchema
          - PriorityLevelConfiguration
          targetAPI: flowcontrol.apiserver.k8s.io/v1beta3

###### Allowed
    
    
    apiVersion: flowcontrol.apiserver.k8s.io/v1beta3
    kind: FlowSchema
    metadata:
      name: allowed-flowcontrol
      namespace: default
    spec:
      matchingPrecedence: 1000
      priorityLevelConfiguration:
        name: exempt
      rules:
      - nonResourceRules:
        - nonResourceURLs:
          - /healthz
          - /livez
          - /readyz
          verbs:
          - '*'
        subjects:
        - group:
            name: system:unauthenticated
          kind: Group

###### Disallowed
    
    
    apiVersion: flowcontrol.apiserver.k8s.io/v1beta2
    kind: FlowSchema
    metadata:
      name: disallowed-flowcontrol
      namespace: default
    spec:
      matchingPrecedence: 1000
      priorityLevelConfiguration:
        name: exempt
      rules:
      - nonResourceRules:
        - nonResourceURLs:
          - /healthz
          - /livez
          - /readyz
          verbs:
          - '*'
        subjects:
        - group:
            name: system:unauthenticated
          kind: Group

## What's next

  * Learn more about [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller)
  * [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller)
  * Learn how to [use constraints instead of PodSecurityPolicies](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-constraints-to-enforce-pod-security)
  * View the open source library of constraint templates in the [gatekeeper-library repository](https://github.com/open-policy-agent/gatekeeper-library)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
