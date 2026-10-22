---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/org-policy/policy-match-section/
title: Organization policy match section \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:33.200441+00:00
---

# Organization policy match section  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/org-policy/policy-match-section/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Organization policy match section Stay organized with collections  Save and categorize content based on your preferences. 

All organization policies have a `match` field, which defines the objects it applies to. All conditions specified must be matched before an object is in-scope affected by a policy.
    
    
    # excludedNamespaces <array>: ExcludedNamespaces is a list of namespace names.
    # If defined, a constraint only applies to resources not in a listed namespace.
    # ExcludedNamespaces also supports a prefix or suffix based glob.  For example,
    # `excludedNamespaces: [kube-*]` matches both `kube-system` and `kube-public`,
    # and `excludedNamespaces: [*-system]` matches both `kube-system` and
    # `gatekeeper-system`.
    excludedNamespaces:
      # <list item: string>: A string that supports globbing at its front or end.
      # Ex: "kube-*" will match "kube-system" or "kube-public", "*-system" will
      # match "kube-system" or "gatekeeper-system".  The asterisk is required for
      # wildcard matching.
      - <string>
    kinds:
      # <list item: object>: Kinds accepts a list of objects with apiGroups and
      # kinds fields that list the groups/kinds of objects to which the mutation
      # will apply. If multiple groups/kinds objects are specified, only one match
      # is needed for the resource to be in scope.
      - # apiGroups <array>: APIGroups is the API groups the resources belong to.
        # '*' is all groups. If '*' is present, the length of the slice must be
        # one. Required.
        apiGroups:
          - <string>
        kinds:
          - <string>
    # labelSelector <object>: LabelSelector is the combination of two optional
    # fields: `matchLabels` and `matchExpressions`.  These two fields provide
    # different methods of selecting or excluding k8s objects based on the label
    # keys and values included in object metadata.  All selection expressions from
    # both sections are ANDed to determine if an object meets the cumulative
    # requirements of the selector.
    labelSelector:
      # matchExpressions <array>: matchExpressions is a list of label selector
      # requirements. The requirements are ANDed.
      matchExpressions:
        # <list item: object>: A label selector requirement is a selector that
        # contains values, a key, and an operator that relates the key and values.
        - # key <string>: key is the label key that the selector applies to.
          key: <string>
          # operator <string>: operator represents a key's relationship to a set
          # of values. Valid operators are In, NotIn, Exists and DoesNotExist.
          operator: <string>
          # values <array>: values is an array of string values. If the operator
          # is In or NotIn, the values array must be non-empty. If the operator
          # is Exists or DoesNotExist, the values array must be empty. This array
          # is replaced during a strategic merge patch.
          values:
            - <string>
      # matchLabels <object>: matchLabels is a map of {key,value} pairs. A single
      # {key,value} in the matchLabels map is equivalent to an element of
      # matchExpressions, whose key field is "key", the operator is "In", and the
      # values array contains only "value". The requirements are ANDed.
      matchLabels:
        [key]: <string>
    # name <string>: Name is the name of an object.  If defined, it will match
    # against objects with the specified name.  Name also supports a prefix or
    # suffix glob.  For example, `name: pod-*` would match both `pod-a` and
    # `pod-b`, and `name: *-pod` would match both `a-pod` and `b-pod`.
    name: <string>
    # namespaceSelector <object>: NamespaceSelector is a label selector against an
    # object's containing namespace or the object itself, if the object is a
    # namespace.
    namespaceSelector:
      # matchExpressions <array>: matchExpressions is a list of label selector
      # requirements. The requirements are ANDed.
      matchExpressions:
        # <list item: object>: A label selector requirement is a selector that
        # contains values, a key, and an operator that relates the key and values.
        - # key <string>: key is the label key that the selector applies to.
          key: <string>
          # operator <string>: operator represents a key's relationship to a set
          # of values. Valid operators are In, NotIn, Exists and DoesNotExist.
          operator: <string>
          # values <array>: values is an array of string values. If the operator
          # is In or NotIn, the values array must be non-empty. If the operator
          # is Exists or DoesNotExist, the values array must be empty. This array
          # is replaced during a strategic merge patch.
          values:
            - <string>
      # matchLabels <object>: matchLabels is a map of {key,value} pairs. A single
      # {key,value} in the matchLabels map is equivalent to an element of
      # matchExpressions, whose key field is "key", the operator is "In", and the
      # values array contains only "value". The requirements are ANDed.
      matchLabels:
        [key]: <string>
    # namespaces <array>: Namespaces is a list of namespace names. If defined, a
    # constraint only applies to resources in a listed namespace.  Namespaces also
    # supports a prefix or suffix based glob.  For example, `namespaces: [kube-*]`
    # matches both `kube-system` and `kube-public`, and `namespaces: [*-system]`
    # matches both `kube-system` and `gatekeeper-system`.
    namespaces:
      # <list item: string>: A string that supports globbing at its front or end.
      # Ex: "kube-*" will match "kube-system" or "kube-public", "*-system" will
      # match "kube-system" or "gatekeeper-system".  The asterisk is required for
      # wildcard matching.
      - <string>
    # scope <string>: Scope determines if cluster-scoped and/or namespaced-scoped
    # resources are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults to
    # `*`)
    scope: <string>
    # source <string>: Source determines whether generated or original resources
    # are matched. Accepts `Generated`|`Original`|`All` (defaults to `All`). A
    # value of `Generated` will only match generated resources, while `Original`
    # will only match regular resources.
    # Allowed Values: All, Generated, Original
    source: <string>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
