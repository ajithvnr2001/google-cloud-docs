---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/migrate/eligibility/
title: Understanding Cloud Service Mesh compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:39.258723+00:00
---

# Understanding Cloud Service Mesh compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/migrate/eligibility/

You are viewing v1.27 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understanding Cloud Service Mesh compatibility

This guide details how to evaluate a fleet's compatibility for control plane modernization by confirming that its configuration, infrastructure, and scale are compatible with the `TRAFFIC_DIRECTOR` control plane implementation.

## Opt in or out of compatibility checks

To initiate the compatibility checks, enable validation mode for the fleet, which triggers an ongoing audit of all Istio configurations, Infrastructure configurations, and scale parameters. Enabling these checks does not perform any changes to your fleet or clusters; it only enables compatibility reporting.

### Enable checks

To begin the compatibility audit, run the following `gcloud` command:
    
    
    gcloud alpha container fleet mesh update --modernization-compatibility validation-enabled --project FLEET_PROJECT_ID
    

Replace `FLEET_PROJECT_ID` with the ID of your Fleet Host project. Generally, the `FLEET_PROJECT_ID` has the same name as the project.

Once enabled, Cloud Service Mesh begins evaluating the fleet and all Cloud Service Mesh provisioned clusters in the fleet for modernization compatibility.

### Disable checks

To stop the reporting of compatibility results, run the following command:
    
    
    gcloud alpha container fleet mesh update --modernization-compatibility validation-disabled --project FLEET_PROJECT_ID
    

This command removes the modernization compatibility conditions from the membership states, as well as the `ModernizationCompatible` status from individual Istio CRs.

## Understand compatibility

Modernization compatibility is reported using conditions at both the fleet and membership (cluster) level. The system performs various checks at different times, with all checks running at least once a day. Allow up to one day for the status to update after enabling checks or applying fixes.

To view these results, retrieve the latest mesh status with the following command:
    
    
    gcloud container fleet mesh describe --project FLEET_PROJECT_ID
    

### Fleet-level compatibility

View the overall modernization status of your fleet under `state.servicemesh.conditions`.

  * **Fleet is compatible** : If your fleet is compatible, you will see a condition with code `MODERNIZATION_COMPATIBLE`:
        
        name: projects/project_id/locations/global/features/servicemesh
        state:
          servicemesh:
            conditions:
            - code: MODERNIZATION_COMPATIBLE
              details: 'Fleet is eligible for modernization.'
              documentationLink: https://cloud.google.com/service-mesh/...
              severity: INFO
        

  * **Fleet is not compatible** : If your fleet is not yet compatible for modernization, you will see a condition with code `MODERNIZATION_INCOMPATIBLE`:
        
        name: projects/project_id/locations/global/features/servicemesh
        state:
          servicemesh:
            conditions:
            - code: MODERNIZATION_INCOMPATIBLE
              details: 'Fleet is not yet eligible for modernization.'
              documentationLink: https://cloud.google.com/service-mesh/...
              severity: INFO
        

If your fleet is incompatible, review the conditions for specific gaps. Check for additional `WARNING` or `ERROR` severity fleet-level conditions as well as cluster-level conditions under `membershipStates.servicemesh` to resolve any blockers.




### Cluster-level compatibility

Look for conditions with `WARNING` or `ERROR` severity under `membershipStates.servicemesh` for each Cloud Service Mesh provisioned cluster in the fleet. If incompatibilities exist, the output is similar to this:
    
    
    ...
    membershipSpecs:
     projects/project_id/locations/global/memberships/cluster-a:
       mesh:
         management:MANAGEMENT_AUTOMATIC
    membershipStates:
      projects/project_id/locations/global/memberships/cluster-a:
        servicemesh:
          conditions:
         - code: MODERNIZATION_INCOMPATIBLE_POD_ANNOTATION
           details: 'Pod pod-a in namespace test-namespace: invalid annotations: ["status.sidecar.istio.io/port": failed to parse port - "invalid", port must be a number and should be in the range 1..65535]; unsupported annotations: ["ambient.istio.io/redirection"] .'
           documentationLink: https://cloud.google.com/service-mesh/...
           severity: WARNING
         - code: WORKLOAD_IDENTITY_REQUIRED
           details: 'Workload Identity is not enabled for the cluster or at least one of the node pools.'
           documentationLink: https://cloud.google.com/...
           severity: ERROR
    ...
    

Follow the `documentationLink` provided within each condition to understand and resolve the specific incompatibility.

## Resolve compatibility issues

### Resolve incompatible pod annotations

The `MODERNIZATION_INCOMPATIBLE_POD_ANNOTATION` code indicates that the cluster cannot be modernized to the `TRAFFIC_DIRECTOR` control plane because certain Pods have unsupported or invalid Istio annotations.

Example output from the `gcloud container fleet mesh describe` command with the condition `MODERNIZATION_INCOMPATIBLE_POD_ANNOTATION` set for membership:
    
    
    membershipStates:
      projects/project_id/locations/global/memberships/membership-a:
        servicemesh:
          conditions:
         - code: MODERNIZATION_INCOMPATIBLE_POD_ANNOTATION
           details: 'Pod pod-a in namespace test-namespace: invalid annotations: ["status.sidecar.istio.io/port": failed to parse port - "invalid", port must be a number and should be in the range 1..65535]; unsupported annotations: ["ambient.istio.io/redirection"] .'
           documentationLink: https://cloud.google.com/service-mesh/...
           severity: WARNING
    

To resolve these pod annotations:

  1. **Identify problematic annotations** : Check the `details` field of the status condition to find the unsupported or invalid annotation keys. Find all Pods with the problematic annotation keys.

  2. **Fix and verify** :

     1. Modify the YAML specifications for your Deployments or Pods to remove or modify the identified annotations, ensuring they do not include any [unsupported annotations](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/unsupported-istio-apis#pod). Re-apply the updated YAML to your cluster.
     2. Once all Pod annotations are corrected, the `MODERNIZATION_INCOMPATIBLE_POD_ANNOTATION` condition will no longer appear for that membership.



### Resolve incompatible configurations

The `MODERNIZATION_INCOMPATIBLE_CONFIG` code indicates that the cluster cannot be modernized to the `TRAFFIC_DIRECTOR` control plane due to incompatible configurations. These incompatibilities can stem from:

  * Specific Istio Custom Resources (CRs) using unsupported features or fields or containing invalid values.
  * Invalid or unsupported Istio MeshConfig settings.
  * Exceeding scalability limits.
  * Use of unsupported service or namespace annotations.



Example output from the `gcloud container fleet mesh describe` command with the condition `MODERNIZATION_INCOMPATIBLE_CONFIG` set for membership:
    
    
    membershipSpecs:
     projects/project_id/locations/global/memberships/membership-a:
       mesh:
         management:MANAGEMENT_AUTOMATIC
    membershipStates:
      projects/project_id/locations/global/memberships/membership-a:
        servicemesh:
          conditions:
         - code: MODERNIZATION_INCOMPATIBLE_CONFIG
           details: 'One or more configs have warnings. Due to the following reason(s): Istio sidecar scale exceeds limit, MeshConfig "accessLogFile" is unsupported. Invalid Config Types: [Gateway, ServiceEntry], where more details are shown on individual config resources.See documentation link for more detail.'
           documentationLink: https://cloud.google.com/service-mesh/...
           severity: WARNING
    

To resolve these configurations:

  1. **Analyze the condition details** : Check the `details` field of the status condition. It summarizes individual errors and identifies the resource types with configuration issues. For the provided details example, you would be required to address the scale and MeshConfig issues and inspect `Gateway` and `ServiceEntry` resources for errors.

  2. **Identify and investigate incompatible resources** : Use the following example script to list Istio Custom Resources (CRs) failing compatibility checks. This script is provided as an example; review and analyze it to ensure it meets your environment and operational requirements before running it in your cluster. The script requires [`kubectl`](https://kubernetes.io/docs/tasks/tools/) and [`jq`](https://jqlang.org/) to be installed. The output includes the specific error details found under `status.conditions` (type: `ModernizationCompatible`, status: `"False"`) of each resource.
         
         for resource in authorizationpolicies destinationrules envoyfilters gateways peerauthentications proxyconfigs requestauthentications serviceentries sidecars telemetries virtualservices wasmplugins workloadentries workloadgroups; do
           echo "--- Checking $resource ---"
           kubectl get $resource --all-namespaces -o json | \
           jq -r '.items[] | select(.status.conditions != null and any(.status.conditions[]; .type == "ModernizationCompatible" and .status == "False")) | {"kind": .kind, "name": .metadata.name, "namespace": .metadata.namespace, "message": [.status.conditions[] | select(.type == "ModernizationCompatible").message]}'
         done
         

**Example Output:**
         
         --- Checking serviceentries ---
         {
           "kind": "ServiceEntry",
           "name": "demo-service-entry",
           "namespace": "se",
           "message": [
             "WARNING: unsupported resolution type: DNS_ROUND_ROBIN"
           ]
         }
         ..
         --- Checking workloadentries ---
         {
           "kind": "WorkloadEntry",
           "name": "demo-we",
           "namespace": "default",
           "message": [
             "WARNING: This API is not supported"
           ]
         }
         

  3. **Fix and apply configurations** : Modify your YAML by removing the unsupported fields or replacing invalid values with compatible ones. For assistance, refer to the [Supported features of managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/supported-features-managed) and [Unsupported Istio APIs](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/unsupported-istio-apis) documentation. (For instance, in the provided example, update the `ServiceEntry` resolution from `DNS_ROUND_ROBIN` to `DNS`).

  4. **Verify fixes** : After applying fixes, allow up to 24 hours for periodic checks to update the status.

     * The `ModernizationCompatible` condition on the fixed resources should change to status: `"True"`. Check the resource's status using:
           
           kubectl get resource name -n namespace -o yaml
           

Example output:
           
           status:
             conditions:
             - lastTransitionTime: "2026-06-05T06:12:52.219963391Z"
               message: Resource is compatible for modernization
               reason: Compatible
               status: "True"
               type: ModernizationCompatible
           

     * Re-run the `gcloud container fleet mesh describe` command. Once all related issues are resolved, the `MODERNIZATION_INCOMPATIBLE_CONFIG` condition will no longer appear for that membership.




### Resolve incompatible fleet scale

The `MODERNIZATION_INCOMPATIBLE_FLEET_SCALE` code indicates that the fleet cannot be modernized to the `TRAFFIC_DIRECTOR` control plane because the scale of resources across the fleet exceeds the limits supported for modernization.

In this phase we support modernizing fleets with the following limits:

  * Up to 1500 data plane endpoints (proxies) across the fleet.
  * Up to 200 [Cloud Service Mesh services](https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-limits#csm_services_versus_kubernetes_services) across the fleet.

**Note:** The limits for modernization are lower than the steady-state scale limits supported by the `TRAFFIC_DIRECTOR` control plane. For more information about Cloud Service Mesh services and scaling, see [Scaling Limits for Cloud Service Mesh on GKE](https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-limits).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
