---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/compute/computetargethttpsproxy/
title: ComputeTargetHTTPSProxy \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:25.174369+00:00
---

# ComputeTargetHTTPSProxy  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/compute/computetargethttpsproxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ComputeTargetHTTPSProxy

**Property** | **Value**  
---|---  
Google Cloud Service Name | Compute Engine  
Google Cloud Service Documentation | [/compute/docs/](https://docs.cloud.google.com/compute/docs)  
Google Cloud REST Resource Name | v1.targetHttpsProxies  
Google Cloud REST Resource Documentation | [/compute/docs/reference/rest/v1/targetHttpsProxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies)  
Config Connector Resource Short Names | computetargethttpsproxy  
gcpcomputetargethttpsproxies  
gcpcomputetargethttpsproxy  
Config Connector Service Name | compute.googleapis.com  
Config Connector Resource Fully Qualified Name | computetargethttpsproxies.compute.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    certificateManagerCertificates:
    - external: string
      name: string
      namespace: string
    certificateMapRef:
      external: string
      name: string
      namespace: string
    description: string
    httpKeepAliveTimeoutSec: integer
    location: string
    proxyBind: boolean
    quicOverride: string
    resourceID: string
    serverTlsPolicyRef:
      external: string
      name: string
      namespace: string
    sslCertificates:
    - external: string
      name: string
      namespace: string
    sslPolicyRef:
      external: string
      name: string
      namespace: string
    urlMapRef:
      external: string
      name: string
      namespace: string
    

Fields  
---  
`certificateManagerCertificates` _Optional_ |  `list (object)` URLs to certificate manager certificate resources that are used to authenticate connections between users and the load balancer. Currently, you may specify up to 15 certificates. Certificate manager certificates do not apply when the load balancing scheme is set to INTERNAL_SELF_MANAGED. sslCertificates and certificateManagerCertificates fields cannot be defined together.  
`certificateManagerCertificates[]` _Optional_ |  `object` CertificateManagerCertificateRef is a reference to a CertificateManagerCertificate.  
`certificateManagerCertificates[].external` _Optional_ |  `string` A reference to an externally managed CertificateManagerCertificate resource. Should be in the format "projects/{{projectID}}/locations/{{location}}/certificates/{{certificateID}}".  
`certificateManagerCertificates[].name` _Optional_ |  `string` The name of a CertificateManagerCertificate resource.  
`certificateManagerCertificates[].namespace` _Optional_ |  `string` The namespace of a CertificateManagerCertificate resource.  
`certificateMapRef` _Optional_ |  `object` A reference to the CertificateMap resource uri that identifies a certificate map associated with the given target proxy. This field can only be set for global target proxies. This field is only supported for EXTERNAL and EXTERNAL_MANAGED load balancing schemes. For INTERNAL_MANAGED, use certificateManagerCertificates instead. sslCertificates and certificateMap fields cannot be defined together.  
`certificateMapRef.external` _Optional_ |  `string` A reference to an externally managed CertificateManagerCertificateMap resource. Should be in the format "projects/{{projectID}}/locations/global/certificateMaps/{{certificateMapID}}".  
`certificateMapRef.name` _Optional_ |  `string` The name of a CertificateManagerCertificateMap resource.  
`certificateMapRef.namespace` _Optional_ |  `string` The namespace of a CertificateManagerCertificateMap resource.  
`description` _Optional_ |  `string` Immutable. An optional description of this resource.  
`httpKeepAliveTimeoutSec` _Optional_ |  `integer` Immutable. Specifies how long to keep a connection open, after completing a response, while there is no matching traffic (in seconds). If an HTTP keepalive is not specified, a default value (610 seconds) will be used. For Global external HTTP(S) load balancer, the minimum allowed value is 5 seconds and the maximum allowed value is 1200 seconds. For Global external HTTP(S) load balancer (classic), this option is not available publicly.  
`location` _Required_ |  `string` Location represents the geographical location of the ComputeTargetHTTPSProxy. Specify a region name or "global" for global resources. Reference: Google Cloud definition of regions/zones (https://cloud.google.com/compute/docs/regions-zones/)  
`proxyBind` _Optional_ |  `boolean` Immutable. This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set to INTERNAL_SELF_MANAGED.  
`quicOverride` _Optional_ |  `string` Specifies the QUIC override policy for this resource. This determines whether the load balancer will attempt to negotiate QUIC with clients or not. Can specify one of NONE, ENABLE, or DISABLE. If NONE is specified, Google manages whether QUIC is used. Default value: "NONE" Possible values: ["NONE", "ENABLE", "DISABLE"].  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`serverTlsPolicyRef` _Optional_ |  `object` Immutable. A URL referring to a networksecurity.ServerTlsPolicy resource that describes how the proxy should authenticate inbound traffic. serverTlsPolicy only applies to a global TargetHttpsProxy attached to globalForwardingRules with the loadBalancingScheme set to INTERNAL_SELF_MANAGED or EXTERNAL or EXTERNAL_MANAGED. For details which ServerTlsPolicy resources are accepted with INTERNAL_SELF_MANAGED and which with EXTERNAL, EXTERNAL_MANAGED loadBalancingScheme consult ServerTlsPolicy documentation. If left blank, communications are not encrypted.  
`serverTlsPolicyRef.external` _Optional_ |  `string` Allowed value: string of the format `projects/{{project}}/locations/{{location}}/serverTlsPolicies/{{value}}`, where {{value}} is the `name` field of a `NetworkSecurityServerTLSPolicy` resource.  
`serverTlsPolicyRef.name` _Optional_ |  `string` The name of a NetworkSecurityServerTLSPolicy resource.  
`serverTlsPolicyRef.namespace` _Optional_ |  `string` The namespace of a NetworkSecurityServerTLSPolicy resource.  
`sslCertificates` _Optional_ |  `list (object)` A list of ComputeSSLCertificate resources that are used to authenticate connections between users and the load balancer. At least one SSL certificate must be specified.  
`sslCertificates[]` _Optional_ |  `object` A reference to a ComputeSSLCertificate resource.  
`sslCertificates[].external` _Optional_ |  `string` Allowed value: string of the format `projects/{{project}}/global/sslCertificates/{{value}}` or `projects/{{project}}/regions/{{region}}/sslCertificates/{{value}}`, where {{value}} is the `name` field of a `ComputeSSLCertificate` resource.  
`sslCertificates[].name` _Optional_ |  `string` The name of a ComputeSSLCertificate resource.  
`sslCertificates[].namespace` _Optional_ |  `string` The namespace of a ComputeSSLCertificate resource.  
`sslPolicyRef` _Optional_ |  `object` A reference to the ComputeSSLPolicy resource that will be associated with the ComputeTargetHTTPSProxy resource. If not set, the ComputeTargetHTTPSProxy resource will not have any SSL policy configured.  
`sslPolicyRef.external` _Optional_ |  `string` A reference to an externally managed ComputeSSLPolicy resource. Should be in the format "projects/{{projectID}}/global/sslPolicies/{{sslPolicyID}}" or "projects/{{projectID}}/regions/{{region}}/sslPolicies/{{sslPolicyID}}".  
`sslPolicyRef.name` _Optional_ |  `string` The name of a ComputeSSLPolicy resource.  
`sslPolicyRef.namespace` _Optional_ |  `string` The namespace of a ComputeSSLPolicy resource.  
`urlMapRef` _Required_ |  `object` A reference to the ComputeURLMap resource that defines the mapping from URL to the BackendService.  
`urlMapRef.external` _Optional_ |  `string` A reference to an externally managed ComputeURLMap resource. Should be in the format "projects/{{projectID}}/global/urlMaps/{{urlMapID}}" or "projects/{{projectID}}/regions/{{region}}/urlMaps/{{urlMapID}}".  
`urlMapRef.name` _Optional_ |  `string` The name of a ComputeURLMap resource.  
`urlMapRef.namespace` _Optional_ |  `string` The namespace of a ComputeURLMap resource.  
  
### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    creationTimestamp: string
    externalRef: string
    observedGeneration: integer
    observedState:
      fingerprint: string
    proxyId: integer
    selfLink: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`creationTimestamp` |  `string` Creation timestamp in RFC3339 text format.  
`externalRef` |  `string` A unique specifier for the ComputeTargetHTTPSProxy resource in Google Cloud.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`observedState` |  `object` ObservedState is the state of the resource as most recently observed in Google Cloud.  
`observedState.fingerprint` |  `string` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.  
`proxyId` |  `integer` The unique identifier for the resource.  
`selfLink` |  `string` The SelfLink for the resource.  
  
## Sample YAML(s)

### Target Https Proxy With Certificate Manager Certificates
    
    
    # Copyright 2024 Google LLC
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
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeTargetHTTPSProxy
    metadata:
      name: computetargethttpsproxy-sample-certmgr
    spec:
      urlMapRef:
        name: computetargethttpsproxy-dep-certmgr
      certificateManagerCertificates:
        - name: computetargethttpsproxy-dep-certmgr
      location: global
      quicOverride: DISABLE
    ---
    apiVersion: certificatemanager.cnrm.cloud.google.com/v1beta1
    kind: CertificateManagerCertificate
    metadata:
      labels:
        label-one: "value-one"
      name: computetargethttpsproxy-dep-certmgr
    spec:
      scope: "ALL_REGIONS"  
      location : "global"
      projectRef:
        # Replace ${PROJECT_ID?} with your project ID.
        external: ${PROJECT_ID?}
      description:  ALL_REGIONS scoped self-managed certificate
      selfManaged:
        pemCertificate: |-
          -----BEGIN CERTIFICATE-----
          MIIDDzCCAfegAwIBAgIUDOiCLH9QNMMYnjPZVf4VwO9blsEwDQYJKoZIhvcNAQEL
          BQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wIBcNMjIwODI0MDg0MDUxWhgPMzAy
          MTEyMjUwODQwNTFaMBYxFDASBgNVBAMMC2V4YW1wbGUuY29tMIIBIjANBgkqhkiG
          9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvOT925GG4lKV9HvAHsbecMhGPAqjhVRC26iZ
          UJC8oSWOu95lWJSX5ZhbiF6Nz192wDGV/VAh3Lxj8RYtcn75eDxQKTcKouDld+To
          CGIStPFWbR6rbysLuZqFVEXVOTvp2QIegInfrvnGC4j7Qpic7zrFB9HzJx+0HpeE
          yO4gkdzJfEK/gMmolUgJrKX59o+0+Rj+Jq3EtcQxL1fVBVJSx0NvpoR1eYpnHMr/
          rJKZkUUZ2xE86hrtpiP6OEYQTi00rmf4GnZF5QfGGD0xuoQXtR7Tu+XhKibXIhxc
          D4RzPLX1QS040PXvmMPLDb4YlUQ6V3Rs42JDvkkDwIMXZvn8awIDAQABo1MwUTAd
          BgNVHQ4EFgQURuo1CCZZAUv7xi02f2nC5tRbf18wHwYDVR0jBBgwFoAURuo1CCZZ
          AUv7xi02f2nC5tRbf18wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOC
          AQEAqx3tDxurnYr9EUPhF5/LlDPYM+VI7EgrKdRnuIqUlZI0tm3vOGME0te6dBTC
          YLNaHLW3m/4Tm4M2eg0Kpz6CxJfn3109G31dCi0xwzSDHf5TPUWvqIVhq5WRgMIf
          n8KYBlQSmqdJBRztUIQH/UPFnSbxymlS4s5qwDgTH5ag9EEBcnWsQ2LZjKi0eqve
          MaqAvvB+j8RGZzYY4re94bSJI42zIZ6nMWPtXwRuDc30xl/u+E0jWIgWbPwSd6Km
          3wnJnGiU2ezPGq3zEU+Rc39VVIFKQpciNeYuF3neHPJvYOf58qW2Z8s0VH0MR1x3
          3DoO/e30FIr9j+PRD+s5BPKF2A==
          -----END CERTIFICATE-----
        pemPrivateKey:
          valueFrom:
            secretKeyRef:
              name: computetargethttpsproxy-dep-certmgr
              key: privateKey
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeBackendService
    metadata:
      name: computetargethttpsproxy-dep-certmgr
    spec:
      location: global
      portName: "http"
      protocol:  "HTTP"
      timeoutSec: 10
      loadBalancingScheme: "INTERNAL_MANAGED" 
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeURLMap
    metadata:
      name: computetargethttpsproxy-dep-certmgr
    spec:
      defaultService:
        backendServiceRef:
          name: computetargethttpsproxy-dep-certmgr
      hostRule:
        - hosts:
          - "mysite.com"
          pathMatcher: "allpaths"
      pathMatcher:
        - name: "allpaths"
          defaultService:
            backendServiceRef:
              name: computetargethttpsproxy-dep-certmgr
          pathRule:
            - paths:
               - "/*"
              service:
                backendServiceRef:
                  name: computetargethttpsproxy-dep-certmgr
      location: global
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: computetargethttpsproxy-dep-certmgr
    stringData:
     privateKey: |
        -----BEGIN PRIVATE KEY-----
        MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC85P3bkYbiUpX0
        e8Aext5wyEY8CqOFVELbqJlQkLyhJY673mVYlJflmFuIXo3PX3bAMZX9UCHcvGPx
        Fi1yfvl4PFApNwqi4OV35OgIYhK08VZtHqtvKwu5moVURdU5O+nZAh6Aid+u+cYL
        iPtCmJzvOsUH0fMnH7Qel4TI7iCR3Ml8Qr+AyaiVSAmspfn2j7T5GP4mrcS1xDEv
        V9UFUlLHQ2+mhHV5imccyv+skpmRRRnbETzqGu2mI/o4RhBOLTSuZ/gadkXlB8YY
        PTG6hBe1HtO75eEqJtciHFwPhHM8tfVBLTjQ9e+Yw8sNvhiVRDpXdGzjYkO+SQPA
        gxdm+fxrAgMBAAECggEAV4/A24TQpV4KFBw/WSTvnRFBeXinB1mhamhztWR6hCrA
        SPcVPKQY632eRI8sJmpGxl3V/Ogl4khT/cA9jfstEl7G++v/WrRsupCaPLSVnlnX
        KdsTNgOauk1WK9P5PMA4rPcuA4Cl91riQpubeWn8KWsxRWg90i+Ak8PB8lBsOaB1
        QzjigWlrRWSpodaw0MBIMZFDL2BYK8HEr+wyATYIyGvDQc9zCnMQIQIZyEPYepLO
        04Dw17YcjgnoJ5gLAFiTvDrCpTMewud1RQzvW5TAvG2piw34sf3QMGPM7aXNrfuZ
        4ZPC/MwVQgq9Nc+jeDsjApQmJKJ+3a8OdIPU89ArTQKBgQDCpHHQe1RzpHmIx47/
        9N5r+NPBhh8flDYmvgi6zPeBfrAaLWhidS8c7Voa6HwvMxbhryDEvc0YqI3vllfy
        xnRF+DfSryozW0gjrkXDGoOzqOJ3EuQwLSJnyX6La2lmufqsRFazwYJ5sxcjoGHK
        /sbwZkIUj1ejuH44ve+ZJQFfpwKBgQD4cLJrJhqImUDhHZRx9jBvxyeHy/RjmHK6
        70xQVDi9ZqeExHwtoSbolhXKLB1RtBnw+t5Csy7IDNBDsbUg9fXU8KyCTIdmsyws
        bDb5hdKsUF76rkKzlpttiXMRVWGS3CMKWahBpnL3lFB3tdtmskemkBTXVn4VgKAH
        xk9XnZ11nQKBgDbQSJ0FnkrSzscOK984/ko50Kh3NNyXyIgwjBTPFASLwNweXX8c
        sR/cV7usLQy9vnvf7cJ6EQAYt5/5Httnt+bceBwE6EV+N1qVAWBoXx6BOQV/dHN8
        wmun+tMYdJ5RUZ6hwCjvHedX3/RQfjnEdhHNOl6/31Zj5mfkVU0zdqeRAoGAcvIh
        erXMfPr7K6y16+xOCMmKHqhc0F/OZXMmSdxNzEPcqe8GzU3MZLxcJIg4oH7FqdtI
        Tm/86w4Spd9owHFMZlNcXYTu+LNZcsw2u0gRayxcZXuO3OyHySxZEuIAHSTBCZ7l
        3EoY0zfJ6zk249MEl6n+GouoFmbGpBI6z3zbR3kCgYEAlCNZVH4uJrP5beTOZTTR
        VJRk7BXvEC6HsM140YtIN7NHy2GtzrgmmY/ZAFB/hX8Ft4ex2MxbIp3hvxroTqGn
        bfu7uv97NoPQqbjtc3Mz8h2IaXTVDUnWYY5gDu6rM2w+Z75/sWIGiTWrsdYX4ohb
        ujngzJ7Ew7GgKSboj6mtlVM=
        -----END PRIVATE KEY-----
    

### Target Https Proxy With Ssl Certificates
    
    
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
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeTargetHTTPSProxy
    metadata:
      name: computetargethttpsproxy-sample
    spec:
      description: "A sample proxy"
      urlMapRef:
        name: computetargethttpsproxy-dep
      sslCertificates:
        - name: computetargethttpsproxy-dep
      sslPolicyRef:
        name: computetargethttpsproxy-dep
      quicOverride: ENABLE
      location: global
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeBackendService
    metadata:
      name: computetargethttpsproxy-dep
    spec:
      healthChecks:
        - healthCheckRef:
            name: computetargethttpsproxy-dep
      location: global
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeHealthCheck
    metadata:
      name: computetargethttpsproxy-dep
    spec:
      checkIntervalSec: 10
      httpHealthCheck:
        port: 80
      location: global
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSSLCertificate
    metadata:
      name: computetargethttpsproxy-dep
    spec:
      location: global
      certificate:
        valueFrom:
          secretKeyRef:
            name: computetargethttpsproxy-dep
            key: certificate
      privateKey:
        valueFrom:
          secretKeyRef:
            name: computetargethttpsproxy-dep
            key: privateKey
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSSLPolicy
    metadata:
      name: computetargethttpsproxy-dep
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeURLMap
    metadata:
      name: computetargethttpsproxy-dep
    spec:
      defaultService:
        backendServiceRef:
          name: computetargethttpsproxy-dep
      location: global
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: computetargethttpsproxy-dep
    stringData:
      certificate: |
        -----BEGIN CERTIFICATE-----
        MIIDJTCCAg0CFHdD3ZGYMCmF3O4PvMwsP5i8d/V0MA0GCSqGSIb3DQEBCwUAME8x
        CzAJBgNVBAYTAlVTMQswCQYDVQQIDAJXQTEhMB8GA1UECgwYSW50ZXJuZXQgV2lk
        Z2l0cyBQdHkgTHRkMRAwDgYDVQQDDAdFeGFtcGxlMB4XDTE5MDkyOTIyMjgyOVoX
        DTIwMDkyODIyMjgyOVowTzELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAldBMSEwHwYD
        VQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQxEDAOBgNVBAMMB0V4YW1wbGUw
        ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDWLvOZIail12i6NXIqOspV
        corkuS1Nl0ayrl0VuKHCvheun/s7lLLgEfifzRueYlSUtdGg4atWIwEKsbIE+AF9
        uUTzkq/t6zHxFAAWgVZ6/hW696jqcZX3yU+LCuHPLSN0ruqD6ZygnYDVciDmYwxe
        601xNfOOYRlm6dGRx6uTxGDZtfu8zsaNI0UxTugTp2x5cKB66SbgdlIJvc2Hb54a
        7qOsb9CIf+rrK2xUdJUj4ueUEIMxjnY2u/Dc71SgfBVn+yFfN9MHNdcTWPXEUClE
        Fxd/MB3dGn7hVavXyvy3NT4tWhBgYBphfEUudDFej5MmVq56JOEQ2UtaQ+Imscud
        AgMBAAEwDQYJKoZIhvcNAQELBQADggEBAMYTQyjVlo6TCYoyK6akjPX7vRiwCCAh
        jqsEu3bZqwUreOhZgRAyEXrq68dtXwTbwdisQmnhpBeBQuX4WWeas9TiycZ13TA1
        Z+h518D9OVXjrNs7oE3QNFeTom807IW16YydlrZMLKO8mQg6/BXfSHbLwuQHSIYS
        JD+uOfnkr08ORBbLGgBKKpy7ngflIkdSrQPmCYmYlvoy+goMAEVi0K3Y1wVzAF4k
        O4v8f7GXkNarsFT1QM82JboVV5uwX+uDmi858WKDHYGv2Ypv6yy93vdV0Xt/IBj3
        95/RDisBzcL7Ynpl34AAr5MLm7yCSsPrAmgevX4BOtcVc4rSXj5rcoE=
        -----END CERTIFICATE-----
      privateKey: |
        -----BEGIN RSA PRIVATE KEY-----
        MIIEpQIBAAKCAQEA1i7zmSGopddoujVyKjrKVXKK5LktTZdGsq5dFbihwr4Xrp/7
        O5Sy4BH4n80bnmJUlLXRoOGrViMBCrGyBPgBfblE85Kv7esx8RQAFoFWev4Vuveo
        6nGV98lPiwrhzy0jdK7qg+mcoJ2A1XIg5mMMXutNcTXzjmEZZunRkcerk8Rg2bX7
        vM7GjSNFMU7oE6dseXCgeukm4HZSCb3Nh2+eGu6jrG/QiH/q6ytsVHSVI+LnlBCD
        MY52Nrvw3O9UoHwVZ/shXzfTBzXXE1j1xFApRBcXfzAd3Rp+4VWr18r8tzU+LVoQ
        YGAaYXxFLnQxXo+TJlaueiThENlLWkPiJrHLnQIDAQABAoIBAQDMo/WZlQBG3Cay
        64fV83AI7jTozkkLvoMNC+3iaBMeN3P3I+HuDmhOEL2lKVq/HKJFp+bPuW50EWPY
        bOlzN+Zs0kygEMJJJxQDjCF9XzxarVPj3OcmgTpRkqWOaupPgYhD3zAws080YuiK
        h84Jcg+KzXWjunGn0vxrSPI0QDueJR2i03tEDBAtMZ0pvAsJ0gmXRdzGOc2uRzDm
        fbS3y/JIufClO28OzjJ5AJkbc9XgRDeCDOFY2D375bCg2boPYmP7Iw0HVU3RQhcr
        t+US27VQBRJF4cQ2CCyr0ZbdaPn41v+/A/qxF6ZPguyy+KoyQjCqK8iFArRQ48hJ
        cR2pFx4hAoGBAP2uXIJAdAemrOunv2CWlUHI2iHj/kJ1AXRMpiT+eF0US9E6tipE
        mL63HkUhiAs2nJnPi3RDxP+kAO2Z3anqjm1KCeGj+IYYZMavnkC8EVybv9lDwORy
        e2O1bfRc/tGa341KmvXLbp8oVMIYIvKz2cZmHGJ4V4DTq8dTvmqoE4/VAoGBANgk
        KWY5MJToZJJ5bV0mc2stmGt/IAZZPlKjVmKOjDyzqHRLAhsmbMyUhhgZtyj0dzSW
        ILEeaEJknYRrOB48D6IqkB8VnFJyHUG8l+Za41adqRQNid0S5n50/+eYbjZpYCrA
        SGmC2dhPZvRD6tOyEEJF5PZMvqxDcNRilc627HipAoGBAKzqrSQbyvtsIXKAZXLx
        McwlnIp9XlLubo9Xr+iHjIPl0chMvN8S4wscxwVYVeNO1nABiI03pJCcugU7XFz2
        BR952EJ2AnFlL0w/aR+3Eh6OC7eM927Amlrc0JZAzXESoE8vC3F/uWfDlgK3cRr+
        fPM/pxl37i1iGzVDYAhTiQIBAoGAPW25nmXumsOZoc+E945wCywAP7z3mxZOEip9
        6LDexnnBDJws0w6OqW4k1kCov6kLIBTy4aPkucniwrm+T0l+n/Y807jOntfz3LT+
        7ucx6XIRlbNrVTuD6rjR6j52RFyaikvvyJz50PJwLkgHO3dGC6/VrPKO1mKsdJA4
        R3HRr1ECgYEAobNQbQSLrSWZ1cozJbmNgRqqvxDNSEDi8LpXukOAw4pz1km7o3ob
        hCy1ksfFzsp5glYqwZd/Bahk64u3mII+rKoYwYLrH2l2aFDmMbdTfQUycpQZyi3+
        VtGS1PFoKx9fSFDNHhR5ZhfasQcuKHYfeFfO2/DoOxQkNCI1y4I2huo=
        -----END RSA PRIVATE KEY-----
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
