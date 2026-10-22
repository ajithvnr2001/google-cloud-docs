---
url: https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical/
title: FHIR access data model and control system \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:42.533270+00:00
---

# FHIR access data model and control system  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/fhir-access-control-technical/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  FHIR access data model and control system Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Cloud Healthcare API FHIR access control system to manage and secure your healthcare data. You can use FHIR access control to define consent policies, control data access based on user roles and context, and enforce these policies in a FHIR store.

## Data model overview

The data model for access control is represented by [Consent resources](https://www.hl7.org/fhir/R4/consent.html). They define the rules that apply and which data the rules apply to.

### FHIR Consent

The access rules are expressed through [FHIR Consent](https://www.hl7.org/fhir/R4/consent.html) resources. [FHIR Consent](https://www.hl7.org/fhir/R4/consent.html) is a type of [FHIR Resource](https://www.hl7.org/fhir/R4/resourcelist.html) that captures a healthcare consumer's choices. It permits or denies a set of _actors_ to perform _actions_ affecting the consumer for a specific _purpose_ from a specified _environment_ over a period of time. For example, a consumer could be a healthcare patient, anyone acting on behalf of a healthcare patient, or another individual who enters into a consent agreement.

The _actions_ recorded in a FHIR Consent may be broad and deal with more than just the consumer's electronic health record (EHR) data, however for the purposes of consent within the Cloud Healthcare API, the focus is on actions related to data access and the enforcement of those actions is limited to reading FHIR data from a FHIR store.

A Consent resource has a [status](https://www.hl7.org/fhir/R4/consent-definitions.html#Consent.status) that indicates the current state of the consent. Although a FHIR store may contain many consents in different states, the Cloud Healthcare API only enforces consents that are in the _active_ state. Consents in any other state have no effect on enforcement. If a consent is given on behalf of a patient, the consent is recorded as being granted by a _performer_.

### Policy type

Cloud Healthcare API supports the following consent policy types:

  * **Patient consent** : is associated with a Patient using `Consent.patient` ([STU3](http://hl7.org/fhir/STU3/consent-definitions.html#Consent.patient), [R4](http://hl7.org/fhir/R4/consent-definitions.html#Consent.patient)) and binds as many data as defined by the patient compartment ([STU3](http://hl7.org/fhir/STU3/compartmentdefinition-patient.html), [R4](http://hl7.org/fhir/R4/compartmentdefinition-patient.html)).

  * **Admin policy** : is not associated with any Patient and must have an extension URL `https://g.co/fhir/medicalrecords/ConsentAdminPolicy`. This policy type could bind to a subset or all resources in the store specified by the resource criteria. Admin policy sets the default policy for all binding resources in the store.

  * **Admin cascading policy** : a type of Admin policy that requires the extension URL `https://g.co/fhir/medicalrecords/CascadingPolicy` and the Admin policy extension URL. You can bind this policy type to a compartment of resources that match the resource criteria. Has the following limitations:

    * Only supports Patient ([STU3](http://hl7.org/fhir/STU3/compartmentdefinition-patient.html), [R4](http://hl7.org/fhir/R4/compartmentdefinition-patient.html)) or Encounter ([STU3](http://hl7.org/fhir/STU3/compartmentdefinition-encounter.html), [R4](http://hl7.org/fhir/R4/compartmentdefinition-encounter.html)) as compartment base.
    * The FHIR store where the policy is enforced must have [`disableReferentialIntegrity`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.disable_referential_integrity) set to `false`. **Contact[Cloud Support](https://docs.cloud.google.com/support/docs#contacting_technical_support) to use this feature for non-referential integrity FHIR store.**



You can combine policy types at the same resource level to permit or deny access to a resource. If a patient's consent is missing, the Admin policy can approve access to a resource.

### Consent directive

Consent directives are instructions that are encoded within a FHIR Consent that permit or deny data access to an authorized entity such as a _grantee_ or an _accessor_. A single FHIR Consent may encode multiple consent directives. Each directive provides the following:

  * Enforcement type: a `permit` or `deny` instruction.

  * Action: the permission(s) covered by this directive. Only [`access`](http://hl7.org/fhir/R4/codesystem-consent-action.html#consent-action-access) is supported to provide read-only access.

  * Accessor criteria: a set of attributes that identify the API requester covered by the directive.

  * Resource criteria: a set of attributes that identify the resources covered by the directive.




#### Accessor criteria

The Cloud Healthcare API supports three properties of an accessor for use within a consent directive and to match against an accessor making a data access request. There must be a case-sensitive exact match to have a directive enforced on the accessor as part of access determination offered by the FHIR server.

These properties are encoded as follows:

  * **Actor** : represents an individual, group, or access role that identifies the accessor or a characteristic of the accessor.

  * **Purpose** : represents the intent of use of the data.

  * **Environment** : represents an abstract identifier that describes the environment or conditions under which the accessor is acting.




For example, an accessor may be represented by the following properties:

  * Actor: `Practitioner/123`

  * Purpose: [`ETREAT`](http://hl7.org/fhir/R4/v3/ActReason/cs.html#v3-ActReason-ETREAT) or access for emergency treatment purposes

  * Environment: `Application/abc`




In this example, these properties represent a doctor who is accessing data when performing emergency treatment using a software application called `abc`.

[provision.actor](https://www.hl7.org/fhir/R4/consent-definitions.html#Consent.provision.actor) and [provision.purpose](https://www.hl7.org/fhir/R4/consent-definitions.html#Consent.provision.purpose) are defined as part of the FHIR standard, whereas Environment is `https://g.co/fhir/medicalrecords/Environment`. Note that this link is not resolvable.

All consent directives must specify an `actor` to be enforced but need not always specify a `purpose` or an `environment`. For example, if no `environment` is specified in the consent directive, then the directive matches any `environment` that is not already covered by other consent directives.

#### Resource criteria

The Cloud Healthcare API supports the following elements as part of the consent resource:

  * **Resource type** ([STU3](http://hl7.org/fhir/STU3/resourcelist.html), [R4](http://hl7.org/fhir/R4/resourcelist.html)): represents the type that the consent policy binds to, for example, `Encounter`, `Observation`, or `Immunization`.

  * **Resource ID** ([STU3](http://hl7.org/fhir/STU3/resource-definitions.html#Resource.id), [R4](http://hl7.org/fhir/R4/resource-definitions.html#Resource.id)): represents the ID that the consent policy binds to.

  * **Data source** : represents the origin of the resource as identified by the resource [`meta.source`](https://www.hl7.org/fhir/R4/resource-definitions.html#Meta.source) (only available in R4).

  * **Data tag** : represents the custom label of the resource as described in the resource `meta.tag` ([STU3](https://www.hl7.org/fhir/STU3/resource-definitions.html#Meta.tag), [R4](https://www.hl7.org/fhir/R4/resource-definitions.html#Meta.tag)).

  * **Security label** : represents security labels that define affected resources as identified in the `meta.security` field ([STU3](https://www.hl7.org/fhir/STU3/resource-definitions.html#Meta.security), [R4](https://www.hl7.org/fhir/R4/resource-definitions.html#Meta.security)). The following code systems are supported:

    * [Confidentiality](http://terminology.hl7.org/CodeSystem/v3-Confidentiality): hierarchical values ranked from unrestricted to most restricted: `U`, `L`, `M`, `N`, `R`, `V`. If a consent permits a security label of `R` then it applies to all resources that are labeled `R` or lower. If a consent denies a security label `R` then it applies to all resources that are at least as sensitive as `R`.

    * [ActCode](http://terminology.hl7.org/CodeSystem/v3-ActCode): exact string matching on security code.


**Note:** Examples of how different policies can be represented through [Consent resource](http://hl7.org/fhir/R4/consent.html) can be found in [How-To Docs](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent#create-consent-resources).

## Access workflow

![authorization_flow](https://docs.cloud.google.com/static/healthcare-api/images/fhir_access_control_user_flow.png)

This figure illustrates the end-to-end journey of a request to a FHIR access control enabled store. An external token with the consent scope (left) is used by application (#3) when making a request to the FHIR store with access control enabled (right).

### Consent scope

When making a data access request, an accessor operates within a particular Consent Scope that represents their `actor`, `purpose`, and `environment` properties related to any FHIR HTTP request. The values for these properties must be a case-sensitive match with those provided within a consent for them to affect the enforcement's access determination.

An accessor can have multiple `actor` identifiers that are relevant for making an access determination. Likewise, there can be multiple `purposes` or `environments` that are relevant within a particular consent context. Therefore, all relevant accessor properties should be provided as part of a FHIR HTTP request to properly represent that accessor for consent purposes.

For example, the consent scope for a given data request may be the following:
    
    
    actor/Practitioner/444 actor/Group/999 purp/v3/TREAT purp/v3/ETREAT env/App/abc
    

This represents a nurse or a doctor known as practitioner `444` who is a member of group `999` which represents practitioners from a department within a specific hospital. The practitioner is there to provide regular treatment, but possibly also deal with emergency treatment as part of these actions. The practitioner is using a software application called `abc`.

The consent scope is provided as a Request consent scope as part of an accessor's data request.

## Request consent scope

FHIR requests use FHIR HTTP request headers to receive the accessor's consent scope. This consent scope contains a set of `actor`, `purpose`, and `environment` values to reflect the accessor's current identity, qualifications, intent of use, and environmental constraints in which the accessor operates. There may be more than one of each of these properties that represent an accessor's consent scope at any one time.

Consent consent scope entries are defined as follows:

  * `actor/{type}/{ID}`: an `actor` property where the resource `type` is provided along with the `ID`. Examples of `type` include the following:

    * `Practitioner`
    * `Group`
    * `Patient`

For example, if a store of the format `projects/PROJECT_ID/locations/us-central1/datasets/DATASET_ID/fhirStores/STORE_ID` calls the API, a local reference to a `Practitioner/123` actor resolves to `projects/PROJECT_ID/locations/us-central1/datasets/DATASET_ID/fhirStores/STORE_ID/fhir/Practitioner/123`.

  * `purp/v3/{value}`: a `purpose` property where `value` is a member of the [FHIR Purpose of Use (`v3`)](https://terminology.hl7.org/3.1.0/CodeSystem-v3-ActReason.html) value set or its extension. Examples of `value` include:

    * `TREAT`
    * `ETREAT`
    * `HRESCH`
  * `env/{type}/{value}`: an `environment` property where `type` and `value` are custom strings with no predefined taxonomy. Examples of `type` and `value` include:

    * `App/my_app_1`
    * `Net/VPN`



In addition, FHIR HTTP request headers can also receive special scopes, such as [`btg`](https://www.hl7.org/fhir/R4/security-labels.html#break-the-glass) and `bypass` which are defined as follows:

  * `btg`: Break the glass (or BTG) lets you, as a human user, skip consent checks in case of emergencies. It should be used in emergencies only and is subject to post-audit review. As a result, `btg` requires at least one `actor`.
  * `bypass`: Allows trusted users (such as an administrator) or trusted applications (such as a ML-training pipeline) to operate on the FHIR store without consent authorization. Hence, `bypass` requires at least one `actor` and one `env`.

**Note:** Requests using `btg` or `bypass` are annotated differently in the `consentMode` of the [audit logs](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent#audit_logs). To facilitate data governance checks, these two special privileges should only be used for their intended purposes.

## Access enforcement and access determination

In a complex healthcare environment where multiple policies and consents coexist, enforcing access and determining access permissions can be a daunting task. Various stakeholders may have different expectations and requirements regarding the use and disclosure of patient information. Navigating this intricate landscape necessitates a clear understanding of how access is enforced and the underlying logic that governs access determination.

### Aggregated consent policy

A healthcare consumer, such as a patient or an administrator, may have multiple consent directives contained within a single Consent resource. Consent resources may contain a mix of `permit` and `deny` [provision.type](https://www.hl7.org/fhir/R4/consent-definitions.html#Consent.provision.type) directives. By default, a user may have any number of Consent resources but up to 200 [`active`](https://www.hl7.org/fhir/R4/valueset-consent-state-codes.html) Consent resources are enforced at a time. See [Constraints and limitations](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent#constraints-and-limitations) for more details.

All the consent directives are extracted from `active` Consent resources for a given user to make a set of aggregated consent rules.

#### Consent directive properties

Consent enforcement is limited to at most one [purpose](https://www.hl7.org/fhir/R4/consent-definitions.html#Consent.provision.purpose) and at most one environment per [provision](https://www.hl7.org/fhir/R4/consent-definitions.html#Consent.provision.provision) entry.

The following rules describe the principles for the joint access control of patient consent, admin policy and admin cascading policy:

  * All resources are denied access by default if there is no matching directive.

  * If the requested resource does not exist, only resource type and resource ID are identifiable. All other resource criteria and the resource owner are unknown, the following rule applies in the listing order:

    * If the resource type belongs to the patient-compartment or encounter-compartment: the access is denied.

    * Otherwise:

      * If there is an admin policy denying the accessor criteria regardless of the other resource criteria, the access is denied.

      * If there is an admin policy permitting the accessor criteria for the identifiable resource criteria (i.e. resource type and resource id), a "resource not found" error is returned.

      * All other cases, the access is denied.

  * Admin policies are the default policies used for matching resources in the store.

  * Resources that don't belong to any patient are determined by only the admin policies.

  * Resources that are in the patient compartment ([STU3](http://hl7.org/fhir/STU3/compartmentdefinition-patient.html), [R4](http://hl7.org/fhir/R4/compartmentdefinition-patient.html)) or encounter compartment ([STU3](http://hl7.org/fhir/STU3/compartmentdefinition-encounter.html), [R4](http://hl7.org/fhir/R4/compartmentdefinition-encounter.html)) need at least one permit consent directive per patient **or** admin policy **or** admin cascading policy and no deny consent directive from patient **and** admin policy **and** admin cascading policy. This condition is needed from all the patients named on the resources to be accessed by the requestor.

    * Some resources may support multiple patient participants. For example, [Appointment](https://www.hl7.org/fhir/R4/appointment.html) provides a list of [participants](https://www.hl7.org/fhir/R4/appointment-definitions.html#Appointment.participant.actor) which may be patients. All patients named on such resources must permit access to the accessor using consent directives, otherwise the resources aren't returned. If a resource has a permission from an encounter cascading policy, where this encounter references a patient through the `subject` field ([STU3](http://hl7.org/fhir/STU3/encounter-definitions.html#Encounter.subject), [R4](https://hl7.org/fhir/R4/encounter-definitions.html#Encounter.subject)), then the resource is considered to be permitted by the patient.



The described rules are summarized by the following pseudo-code:

### Joint access control
    
    
    if resource does not exist
      if resource is a patient-compartment or encounter-compartment resource:
        return "deny"
      else:
        if there is any admin policy denies access for accessor criteria **regardless** of resource criteria other than resource type and resource ID:
          return "deny"
        else if there is any admin policy permits access for accessor criteria based on the **identifiable** resource criteria:
          return "resource not found"
        else:
          return "deny"
    else:
      let patients = list of patient references named in the patient compartment eligible fields of the requested resource
      if there is any matching deny from either patients's consents or admin policy or admin cascading policy:
        return "deny"
      if there is matching admin policy permits access:
        return "permit"
      if all patients have matching patient consents or admin cascading consent that permit access or are subject of encounters which permit the access through encounter cascading policy:
        return "permit"
      else:
        return "deny"
    end
    

The FHIR store checks consent permission at the per resource level. Any [reference](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-references) in a resource is not resolved and cascaded for consent access check purposes. For example, consider a patient identified by `Patient/f001` that allows a Practitioner to access their entire `MedicationRequest` resource, but not the `Patient/f001` resource itself due to the patient privacy. In this scenario, the Practitioner can see the entire `MedicationRequest` resource which includes a `subject` field referring to the `Patient/f001` resource, but cannot see the contents of the `Patient/f001` resource even, for example, when performing a FHIR search using `_include`.

### Conflict resolution

Conflicts are possible between various `permit` and `deny` directives. If two conflicting directives match a resource, the conflict is resolved using the _`deny` wins over `permit`_ model.

Only `active` consents are included for consent enforcement.

### Resource access enforcement logic

When making a consent-aware request to a FHIR store, access control occurs in the following order:

  1. The Cloud Healthcare API checks the permissions on the Google Cloud service account (or the principal) configured in the proxy. If the service account has the correct IAM permissions to perform the requested FHIR method on the FHIR store, the request proceeds.

  2. If consent enforcement is enabled in the [FHIR store configuration](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent#configure-a-fhir-store) and the [consent-aware HTTP headers](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent#http_headers) are present, then the Cloud Healthcare API enforces consent access policies for Patient Compartment resources. The enforcement of consent access policies is based on the consent scopes provided in the request, according to the consent directives captured by the most recent execution of `ApplyConsents` and `ApplyAdminConsents`.

**Note:** If the FHIR store configuration defines the consent header handling as `REQUIRED_ON_READ`, consent access control is enforced (and rejected) even without the consent aware headers.



The following rules apply when making a consent-aware request to a FHIR store:

  * Provide at least one `actor` consent scope relevant for the consenting actions taken.

  * Provide any additional `purpose` and `environment` scopes relevant for the consenting actions taken.

  * If the number of consent scope entries exceeds the [supported limits](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent#http_headers), an error is returned.

  * If you call a method that accesses multiple resources (for example, the [`fhir.Patient-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-everything), [`fhir.Encounter-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Encounter-everything), [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle), or [`fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) method), consent enforcement applies to each individual resource. However, there is a subtle difference between these multi-resource access methods:

    * `fhir.executeBundle` reading multiple resources receives "Consent access denied or the resource being accessed does not exist" for individual resource without consent permissions (see examples in the [Get FHIR resources with consent scope](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent#get_fhir_resources_with_consent-scope)).

    * `fhir.search` skips resources without consent permissions and **does not return** consent access denied error, even for searching by `_id` (see examples in the [Search FHIR resources with consent scope](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent#search_fhir_resources_with_consent-scope)).

    * `fhir.Patient-everything` and `fhir.Encounter-everything` behave similarly to `fhir.search`, except that they return "Consent access denied or the resource being accessed does not exist" if the caller does not have consent permission on the requested Patient or Encounter resource, respectively.




### Consent access determination

A consent directive has at most one `actor`, at most one `purpose`, and at most one `environment` whereas consent scope may have multiple of each. Some consent directives don't specify all three accessor properties, in which case any consent scope property value may match depending on conflict resolution rules. As result, a consent scope may match more than one consent directive.

If the consent scope of a request includes two or more entries of the same consent scope type (`actor`, `purpose`, or `environment`), then the consent scope possibly matches multiple consent directives. Some consent directives don't specify a `purpose` or an `environment`. Therefore the consent scope must be also matched against consent directives that don't specify these scope types.

For example, setting the consent scope to `actor/Practitioner/123 actor/Group/999 purp/v3/TREAT env/App/abc` matches against any of the following `permit` or `deny` consent directives:

  * `actor/Practitioner/123 purp/v3/TREAT env/App/abc`
  * `actor/Practitioner/123 purp/v3/TREAT`
  * `actor/Practitioner/123 env/App/abc`
  * `actor/Practitioner/123`
  * `actor/Group/999 purp/v3/TREAT env/App/abc`
  * `actor/Group/999 purp/v3/TREAT`
  * `actor/Group/999 env/App/abc`
  * `actor/Group/999`



## What's next

  * [Learn how to enforce access on a FHIR store](https://docs.cloud.google.com/healthcare-api/docs/fhir-consent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
