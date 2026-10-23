---
url: https://docs.cloud.google.com/looker/docs/ci-style-validator/
title: Continuous Integration Style Validator \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:54.727325+00:00
---

# Continuous Integration Style Validator  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ci-style-validator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Continuous Integration Style Validator Stay organized with collections  Save and categorize content based on your preferences. 

The Continuous Integration (CI) Style Validator enforces LookML coding standards, naming conventions, and structural best practices across your LookML project by using the LookML Style Linter. By checking your LookML files against a configurable set of style rules, the Style Validator helps your team maintain a clean, consistent, and readable codebase.

To run the Style Validator, you must add a configuration file named `lkmlstyle.yaml` (or `lkmlstyle.yml`) to the root directory of your LookML project repository. See the Configuration file section of this page for details on configuring the style linter.

For information on configuring and running the Style Validator in a CI suite and viewing validation output, see the [Creating a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite), [Running Continuous Integration suites](https://docs.cloud.google.com/looker/docs/ci-run-suite), and [Viewing the results of a CI run](https://docs.cloud.google.com/looker/docs/ci-view-results) documentation pages.

## Before you begin

To use the Style Validator in Continuous Integration, you need the following:

  * A Looker instance running Looker 26.18 or later that meets the [requirements for CI](https://docs.cloud.google.com/looker/docs/continuous-integration#requirements) and is [enabled for CI](https://docs.cloud.google.com/looker/docs/continuous-integration#enable-ci).
  * A LookML project that is [configured with Git version control](https://docs.cloud.google.com/looker/docs/setting-up-git-connection).
  * The **Style Validator** toggle enabled in your [CI suite settings](https://docs.cloud.google.com/looker/docs/ci-create-suite) (the Style Validator is disabled by default). When you turn on the Style Validator, the **Only incremental errors** option is enabled by default.
  * A `lkmlstyle.yaml` (or `lkmlstyle.yml`) configuration file in the root directory of your LookML project repository. See the Configuration file section on this page.



## Configuration file

A configuration file is **required** to run the Style Validator in Looker CI. When the Style Validator runs, it automatically checks the root directory of your LookML project repository for a configuration file in the following priority order:

  1. `lkmlstyle.yaml`
  2. `lkmlstyle.yml`



If both files exist in the root directory, `lkmlstyle.yaml` takes precedence and `lkmlstyle.yml` is ignored.

If neither `lkmlstyle.yaml` nor `lkmlstyle.yml` is found in the project root directory (and no custom configuration is passed through the API), the style validation run fails with the error `"No style validator configuration provided"`.

**Note:** The Looker IDE treats `lkmlstyle.yaml` in the project root directory as a reserved project file and provides schema-based autocomplete and validation. Because the IDE check is based on the published JSON schema, a small number of configurations that pass validation in the IDE can still be rejected when the Style Validator runs.

To run all 25 standard built-in rules with their default settings, you can use the following minimal configuration information in your `lkmlstyle.yaml` file:
    
    
    schema_version: 1
    ruleset_version: "all-v1.0"
    

Otherwise, you can customize your configuration file. The configuration file can contain the following top-level parameters:

Parameter | Type | Required? | Default | Description  
---|---|---|---|---  
`schema_version` | Integer | Yes | None | Configuration schema version. Version `1` is the only supported version and must be explicitly specified.  
`ruleset_version` | String | Yes | None | Baseline ruleset edition to inherit. Supported values: `"all-v1.0"`, `"none"`.  
`ignore_files` | List of strings | No | `[]` | Glob patterns of files to exclude completely from style validation.  
`rules` | Map | No | `{}` | Global customizations (`severity` and `version`) for individual rules. Can also enable built-in rules that the baseline ruleset doesn't include, and change the severity of custom rules. See the Rule customizations section for examples.  
`overrides` | List of maps | No | `[]` | Scoped rule overrides that adjust or enable severities for specific matching file paths.  
`custom_rules` | List of maps | No | `[]` | Declarative, user-defined custom rules.  
  
### `ruleset_version`

The `ruleset_version` parameter defines the foundation of your style validation strategy:

  * **`"all-v1.0"`** (Recommended): Activates all 25 standard built-in LookML style rules at the `error` severity level. This option is ideal for teams that want comprehensive quality enforcement out of the box.
  * **`"none"`** : Starts with zero built-in rules enabled. This option is ideal for teams that want to adopt style validation incrementally, opt in to specific rules one by one, or run only custom organizational rules. To opt in to a built-in rule when `ruleset_version` is `"none"`, assign the rule a `warn` or `error` severity in the `rules` block or in an `overrides` block.



### `ignore_files`

The `ignore_files` parameter accepts a list of glob patterns for files that you want to bypass completely during style validation. Files matching these patterns aren't inspected for built-in or custom rules.

Supported wildcard syntax includes the following:

  * `*`: Matches any sequence of non-separator characters within a single directory level.
  * `**`: Matches any sequence of characters across multiple nested directory levels.
  * `?`: Matches any single character.
  * `{a,b}` and `[abc]`: Matches alternatives and character classes (Java glob syntax).



The following path matching rules apply to every glob pattern in the configuration file, including top-level `ignore_files` as well as `files` and `ignore_files` in `overrides`:

  * Paths are relative to the project root directory. A leading `./` or `/` is ignored.
  * A pattern without a slash (`/`) matches at any directory depth. For example, `*.ignore.lkml` matches both `x.ignore.lkml` and `views/x.ignore.lkml`.
  * A pattern ending in `/` matches everything under that directory.
  * A pattern ending in `.lkml` or `.lookml` also matches compound extensions. For example, `*.ignore.lkml` matches `x.ignore.view.lkml`.



The following example excludes vendor files, legacy LookML files, and LookML dashboards:
    
    
    ignore_files:
      - "vendor/**"
      - "legacy/**/*.lkml"
      - "*.ignore.lkml"
      - "dashboards/*.dashboard.lookml"
    

### `rules`

You can use the `rules` block to adjust the diagnostic severity of individual rules across your entire project:
    
    
    rules:
      boolean-dimension-name-prefix:
        severity: warn
      view-dimension-order:
        severity: disabled
      numeric-measure-value-format-presence:
        severity: error
    

Any built-in rule listed in `rules` (or in an `overrides` block) with a severity of `warn` or `error` is active, even when `ruleset_version` is set to `"none"`. For example, the following starter configuration starts with `ruleset_version: "none"` and enables only two built-in rules:
    
    
    schema_version: 1
    ruleset_version: "none"
    
    rules:
      join-relationship-presence:
        severity: error
      explore-label-presence:
        severity: warn
    

You can also use the `rules` block to change the severity of a custom rule by referencing its name.

#### `severity`

Each rule can be configured with one of the following case-insensitive severity levels:

  * **`error`** : Treated as a fatal violation. Errors cause the CI run to fail.
  * **`warn`** : Emitted as a non-blocking warning. Warnings appear in CI run reports, but they don't cause the CI run to fail.
  * **`disabled`** : Deactivates the rule completely and skips it during validation.

**Important:** Rule configurations must be defined as maps, such as `rule-name: { severity: warn }`. Shorthand scalar syntax, such as `rule-name: warn`, isn't supported and results in a configuration validation error. In the global `rules` block, `severity` is optional (it defaults to `error`, so `rule-name: {}` is valid) and an optional `version` key is allowed (every built-in rule is at version `1`, so `version` can be omitted). Inside `overrides` blocks, `severity` is required and is the only permitted key.**Warning:** Rule names in the global `rules` block aren't validated. A misspelled rule name is silently ignored, and the rule that you intended to modify keeps its default severity. Rule names in `overrides` blocks are validated.

### `overrides`

You can use the `overrides` parameter to modify rule severities for specific files or directories without changing severities across the rest of your LookML project. For example, you can use `overrides` to relax rules for staging views or legacy models, tighten rules for critical paths, or enable specific rules only for certain directories when `ruleset_version` is `"none"`.

Each entry in the `overrides` list supports the following fields:

Field | Type | Required? | Description  
---|---|---|---  
`files` | List of strings | Yes | Glob patterns matching the files that this override block applies to. Cannot be empty.  
`ignore_files` | List of strings | No | Glob patterns to exclude from this specific override block.  
`rules` | Map | Yes | Map of rule names to severity configurations. Cannot be empty. Only `severity` is permitted (and required) in override blocks. Rule names must be valid built-in or custom rule names.  
  
The following example disables dimension ordering checks and downgrades missing description errors to warnings for legacy views and dashboards:
    
    
    overrides:
      - files:
          - "views/legacy/**"
          - "dashboards/*.dashboard.lookml"
        ignore_files:
          - "views/legacy/core_*.view.lkml"
        rules:
          view-dimension-order:
            severity: disabled
          visible-dimension-description-presence:
            severity: warn
    

**Note:** Override rules can target both built-in rules and user-defined custom rules. Overrides cascade in order from top to bottom: when multiple override blocks match a file, the last matching block takes precedence for each overlapping rule.

### `custom_rules`

You can define declarative custom rules in the `custom_rules` section of your configuration file to enforce organization-specific naming conventions, required architectural patterns, and structural governance.

Every custom rule definition supports the following common parameters:

Field | Type | Required? | Description  
---|---|---|---  
`name` | String | Yes | Unique identifier, in dash-case format by convention, such as `finance-measure-prefix`. Must not collide with built-in rule names or other custom rules.  
`title` | String | Yes | Human-readable message reported when a violation occurs, formatted as `(<rule-name>) <title>`.  
`rule_type` | String | Yes | The archetype of the rule: `pattern_match`, `property`, `order`, `first_child`, or `unique`. Case-insensitive; `pattern` is accepted as an alias for `pattern_match`.  
`severity` | String | No | Diagnostic level: `error` (default), `warn`, or `disabled`. Can be overridden by `rules` and `overrides`.  
`rationale` | String | No | Documents why the rule exists.  
`select` | String or list | No | Abstract syntax tree (AST) node path to target, such as `"view.dimension"`, `"explore"`, or `["dimension", "dimension_group"]`. If omitted, the rule targets every node that matches `filters`.  
`filters` | Map | No | Property filters that must match on the targeted node, such as `primary_key: true`.  
`parent_filters` | Map | No | Property filters that must match on the immediate parent of the targeted node.  
  
Each rule type accepts only its own type-specific keys. Unknown keys, or keys that belong to a different rule type (such as `order_by` on a `pattern_match` rule), result in a configuration error.

#### `select`

The `select` parameter determines which LookML elements the custom rule evaluates:

  * **Direct element** : Target a specific LookML element type, such as `select: "dimension"`, `select: "measure"`, `select: "view"`, `select: "explore"`, `select: "join"`, `select: "model"`, or `select: "include"`.
  * **Nested parent-child path** : Target elements defined within a specific immediate parent, such as `select: "view.dimension"` (dimensions defined inside views) or `select: "explore.join"` (joins defined within Explores). The parent must be the immediate parent, and only the last two segments of a path are used (so `a.b.c` behaves like `b.c`).
  * **Multiple targets** : Target multiple element types using a comma-separated string or a list, such as `select: "dimension, dimension_group"` or `select: ["dimension", "dimension_group"]`.



Selector, filter, and child names are exact, case-sensitive LookML keywords. A misspelled name isn't reported as a configuration error; instead, the rule never matches.

#### `filters` and `parent_filters`

You can use `filters` and `parent_filters` to refine targeted nodes based on the LookML properties that are **explicitly declared** in the LookML file. 

**Important:** LookML defaults aren't applied: for example, `hidden: false` matches only LookML fields that literally declare `hidden: no`. But the default for `hidden` is `no`, so it's likely that your LookML won't declare `hidden: no`. Similarly for `type: "string"`, it's likely that `type: "string"` won't be present in your LookML project, since `string` is the default for `type`.

  * **Boolean equality** : Match explicitly declared Boolean properties, such as `primary_key: true` or `hidden: true`.
  * **String equality** : Match exact string values, such as `type: "yesno"` or `type: "count"`.
  * **One-of list** : Match any value in a list, such as `type: ["string", "number", "date"]`.
  * **Presence check** : Check whether a block or property is present by passing an empty string, such as `derived_table: ""`.
  * **Negation** : Prefix the key or value with `!` to negate the filter. A negated key must be enclosed in quotation marks because an unquoted leading `!` is YAML tag syntax and causes the configuration file to fail to parse: 
    * `"!hidden": true` or `hidden: "!true"` matches visible (non-hidden) items, including fields that don't declare `hidden`.
    * `type: ["!yesno", "!date"]` matches types that are neither `yesno` nor `date`.



#### `rule_type`

Each custom rule must specify one of the following five rule archetypes for the `rule_type` parameter:

  * `pattern_match`
  * `property`
  * `order`
  * `first_child`
  * `unique`



##### `pattern_match`

Enforces regular expression patterns on LookML entity names or property values. You must specify **exactly one** of `match` or `should_not_match` (if both are set, only `match` is applied and `should_not_match` is silently ignored):

  * `match` (String, regular expression): Pattern that the target must match.
  * `should_not_match` (String, regular expression): Pattern that the target must not match.



Patterns are Java regular expressions that are validated when the configuration file is loaded. Matching is **unanchored** (a substring match); for example, `match: "fin_"` passes for `my_fin_total`. Use `^` and `$` to match the entire value.

If `select` targets a property instead of an entity (for example, `select: "measure.sql"` or `select: "dimension.label"`), the regular expression is evaluated against the property's value rather than an entity name. The built-in `measure-sql-table-reference` and `dimension-label-redundant-yes-no` rules operate this way.

Example that enforces that currency measures end with `_usd` or `_eur`:
    
    
    - name: currency-measure-suffix
      title: "Currency measures must end with a currency code like _usd or _eur"
      rule_type: pattern_match
      severity: error
      select: "view.measure"
      filters:
        value_format_name: ["usd", "usd_0", "eur", "eur_0"]
      match: "^.*_(usd|eur)$"
    

Example that forbids temporary or draft dimensions:
    
    
    - name: forbid-temporary-dimensions
      title: "Dimensions must not start with 'tmp_' or 'test_'"
      rule_type: pattern_match
      severity: error
      select: "dimension"
      should_not_match: "^(tmp|test)_.*"
    

##### `property`

Enforces the mandatory presence or prohibition of specific child properties within LookML objects. You must specify **exactly one** of `requires_child` or `forbidden_child` (if both are set, only `requires_child` is applied and `forbidden_child` is silently ignored):

  * `requires_child` (String or list): Child property name or names that must be present. When you specify a list, the rule is satisfied if **any one** of the listed children is present.
  * `forbidden_child` (String or list): Child property name or names that must not be present. When you specify a list, the node is flagged if **any** listed child is present.
  * `child_filters` (Map, optional): Additional property filters that the required child must satisfy.



Example that requires descriptions on all visible dimensions:
    
    
    - name: require-visible-dimension-description
      title: "Visible dimensions must specify a description"
      rule_type: property
      severity: warn
      select: "view.dimension"
      filters:
        "!hidden": true
      requires_child: "description"
    

Example that forbids `sql_table_name` on derived tables:
    
    
    - name: forbid-sql-table-name-on-derived-views
      title: "Derived table views cannot specify sql_table_name"
      rule_type: property
      severity: error
      select: "view"
      filters:
        derived_table: ""
      forbidden_child: "sql_table_name"
    

##### `order`

Enforces alphabetical ordering of sibling elements within a container.

  * `order_by` (String, required): LookML type of the sibling children to order, typically `"dimension"` or `"measure"`. Only direct children of the selected node are compared, and `dimension_group` children aren't included under `"dimension"`.



Names are compared case-sensitively by character code: uppercase letters sort before lowercase letters, and `_` sorts between them.

Example that requires dimensions to be listed in alphabetical order within views:
    
    
    - name: custom-alphabetical-dimensions
      title: "Dimensions must be kept in alphabetical order within views"
      rule_type: order
      severity: error
      select: "view"
      order_by: "dimension"
    

**Note:** This example duplicates the built-in `view-dimension-order` rule. Under `all-v1.0`, disable the built-in rule if you use a custom rule like this; otherwise, each violation is reported twice.

##### `first_child`

Enforces that an element matching a specific filter appears as the first child of its category.

  * `position` (String, optional): Position constraint. Must be `"first"` (defaults to `"first"`).



For `first_child` rules, `select` must use the `parent.child_type` form, such as `"view.dimension"`. The `filters` parameter identifies the child that must appear first; it doesn't narrow which parent nodes are checked. The `parent_filters` parameter is accepted by the schema, but it is ignored for this rule type.

Example that requires the primary key dimension to be declared first in a view:
    
    
    - name: custom-primary-key-first-dimension
      title: "Primary key dimension must be the first dimension in the view"
      rule_type: first_child
      severity: error
      select: "view.dimension"
      filters:
        primary_key: true
      position: first
    

**Note:** This example duplicates the built-in `primary-key-first-dimension` rule. Under `all-v1.0`, disable the built-in rule if you use a custom rule like this; otherwise, each violation is reported twice.

##### `unique`

Enforces uniqueness of a property value across all matching nodes in the files validated during a CI run.

  * `unique_property` (String, required): Name of the property that must have unique values across matching nodes, such as `"sql_table_name"` or `"label"`.



Values are compared as exact strings, and both the first occurrence and every duplicate are reported. If a validation run checks only a subset of the project's files, duplicates in files outside that subset aren't detected.

Example that ensures unique table names across all views:
    
    
    - name: custom-sql-table-name-uniqueness
      title: "Each view must reference a unique sql_table_name"
      rule_type: unique
      severity: error
      select: "view"
      unique_property: "sql_table_name"
    

#### Custom rule constraints

When creating custom rules, adhere to the following constraints:

  1. **No collision with built-in rule names** : Custom rules cannot reuse any name from the built-in rules catalog, such as `boolean-dimension-name-prefix` or `sql-table-name-uniqueness`.
  2. **Unique custom names** : Every custom rule must have a distinct name within the `custom_rules` list.
  3. **Dash-case format** : Rule names should use dash-case format (`lowercase-words-with-hyphens`). 



### Configuration evaluation order

When the Style Validator evaluates a LookML file, configuration rules are applied in the following order:

  1. **File exclusion** : If the file matches any pattern in `ignore_files`, the file is skipped completely.
  2. **Active rules** : The active rules for the file consist of the rules from `ruleset_version` (`all-v1.0` or `none`), plus any built-in rule assigned a `warn` or `error` severity in `rules` or in a matching `overrides` block, plus all rules defined in `custom_rules`.
  3. **Severity resolution** : For each active rule, the first of the following settings that specifies a severity takes precedence: the last matching `overrides` block, then the global `rules` block, then the custom rule's own `severity`, and finally the default severity (`error`).
  4. **Disabled rules** : Rules whose resolved severity is `disabled` are skipped for that file.



## Example configuration file

The following example shows a complete `lkmlstyle.yaml` file that demonstrates baseline ruleset selection, file exclusions, global rule customizations, scoped overrides, and custom rules:
    
    
    # Schema version
    schema_version: 1
    
    # Baseline ruleset edition (all-v1.0 or none)
    ruleset_version: "all-v1.0"
    
    # Files completely ignored by the style validator
    ignore_files:
      - "vendor/**"
      - "*.ignore.lkml"
      - "legacy_dashboards/*.dashboard.lookml"
    
    # Built-in rule customizations
    rules:
      view-dimension-order:
        severity: warn
      numeric-measure-value-format-presence:
        severity: warn
      sql-table-name-uniqueness:
        severity: error
      # Replaced by the custom first_child rule below
      primary-key-first-dimension:
        severity: disabled
    
    # Directory/file scoped overrides
    overrides:
      - files:
          - "views/staging/**"
        rules:
          visible-dimension-description-presence:
            severity: disabled
          primary-key-visibility:
            severity: warn
    
    # Custom rules catalog
    custom_rules:
      # 1. Pattern Match: Finance dimensions must start with fin_
      - name: finance-dimension-prefix
        title: "Finance dimensions must be prefixed with fin_"
        rule_type: pattern_match
        severity: error
        rationale: "Ensures clarity in the field picker for finance metrics."
        select: "view.dimension"
        filters:
          view_label: "Finance"
        match: "^fin_[a-z0-9_]+$"
    
      # 2. Pattern Match: Forbid draft or test views
      - name: forbid-draft-views
        title: "Views cannot be named with draft_ or test_ prefixes"
        rule_type: pattern_match
        severity: error
        select: "view"
        should_not_match: "^(draft|test)_.*"
    
      # 3. Property: Require explicit relationship on joins
      - name: require-join-relationship
        title: "All joins must declare an explicit relationship"
        rule_type: property
        severity: error
        select: "explore.join"
        requires_child: "relationship"
    
      # 4. Property: Explores must not use sql_always_where
      - name: forbid-sql-always-where
        title: "Explores should use always_filter instead of sql_always_where"
        rule_type: property
        severity: warn
        select: "explore"
        forbidden_child: "sql_always_where"
    
      # 5. Order: Dimension groups inside views must be alphabetical
      - name: view-dimension-groups-alphabetical
        title: "Dimension groups must appear in alphabetical order within views"
        rule_type: order
        severity: warn
        select: "view"
        order_by: "dimension_group"
    
      # 6. First Child: Primary key must be the first dimension
      - name: custom-primary-key-first-dimension
        title: "The primary key must be defined as the first dimension in the view"
        rule_type: first_child
        severity: error
        select: "view.dimension"
        filters:
          primary_key: true
        position: first
    
      # 7. Unique: Views must not share the same label
      - name: unique-view-labels
        title: "Views must have unique labels"
        rule_type: unique
        severity: warn
        select: "view"
        unique_property: "label"
    

## Validation scope and results

The following sections describe which files the Style Validator checks and how validation results are reported:

  * Files validated
  * Pass or fail behavior and output



### Files validated

  * Only `.lkml` and `.lookml` files in the **root project** are validated. Imported (local or remote) dependency projects aren't validated.
  * Each file is validated based on its own content. `include:` statements aren't followed, and objects pulled in through an `include:` statement aren't validated as part of the including file.
  * CI runs triggered by [dbt Cloud CI jobs](https://docs.cloud.google.com/looker/docs/ci-create-suite#dbt-trigger) validate the production LookML branch rather than a development branch.



### Pass or fail behavior and output

  * A Style Validator run fails only if at least one diagnostic has the `error` severity. Warnings alone don't cause the run to fail.
  * On the [CI run results page](https://docs.cloud.google.com/looker/docs/ci-view-results), each diagnostic result includes the rule name, path, line number, a context snippet, and a link to the rule documentation. For more information on running suites and viewing results, see [Running Continuous Integration suites](https://docs.cloud.google.com/looker/docs/ci-run-suite) and [Viewing the results of a CI run](https://docs.cloud.google.com/looker/docs/ci-view-results).
  * An invalid configuration file produces a single `invalid-config` error on the configuration file at line 1, and the validation run fails.



## Incremental validation

You can enable incremental validation for the Style Validator by selecting the **Only incremental errors** checkbox (enabled by default) in the **Style Validator** section when you [create or edit a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite).

When incremental validation is enabled, the Style Validator reports only violations that are **new** on your development branch:

  1. It validates the development branch.
  2. It validates the target branch **using the development branch's configuration file**.
  3. It reports only the violations that aren't already present on the target branch.



Note the following behavior when incremental validation is enabled:

  * Pre-existing violations on the target branch don't cause the run to fail.
  * Because the development branch's configuration file is used to validate both branches, a configuration change on the development branch cannot hide pre-existing violations or make pre-existing LookML appear as new violations on its own.
  * The development branch must contain an `lkmlstyle.yaml` (or `lkmlstyle.yml`) configuration file; otherwise, the run fails with a missing configuration error.



When **Only incremental errors** is disabled, every violation found on the validated branch is reported.

## Built-in rules catalog

The following table lists all 25 standard built-in rules available in the `all-v1.0` ruleset:

Rule name | Target entity | Rule summary  
---|---|---  
`average-measure-name-prefix` | Measure | Measures with `type: average` or `average_distinct` must start with `avg_` or `average_`.  
`boolean-dimension-name-prefix` | Dimension | Yesno dimensions must start with `is_`, `has_`, or `does_`.  
`count-measure-name-prefix` | Measure | Measures with `type: count` or `count_distinct` must start with `count_`.  
`dimension-group-name-suffix` | Dimension group | Dimension groups shouldn't end with `_at`, `_date`, or `_time`.  
`dimension-label-redundant-yes-no` | Dimension | Yesno dimension labels shouldn't include a yes/no marker such as `(Yes / No)` or `(yes/no)` (any capitalization or spacing).  
`dimension-name-snake-case` | Dimension | Dimension and dimension group names must be in lowercase `snake_case`.  
`explore-fields-presence` | Explore | Explores should define the `fields:` property.  
`explore-label-presence` | Explore | Explores must define an explicit `label:` property.  
`includes-wildcard-usage` | Include | `include:` statements shouldn't use wildcards for view files (such as `*.view.lkml` or `/views/*.view`). Other wildcards aren't flagged.  
`join-relationship-presence` | Join | Explore `join:` declarations must specify a `relationship:`.  
`measure-name-snake-case` | Measure | Measure names must be in lowercase `snake_case`.  
`measure-sql-table-reference` | Measure | Measures must reference dimensions using `${dimension_name}`, not `${TABLE}.column`.  
`numeric-measure-value-format-presence` | Measure | Measures with `type: count`, `sum`, `average`, or `number` must specify `value_format:` or `value_format_name:`.  
`pdt-view-name-prefix` | View | Persistent derived tables (PDTs) should start with `pdt_`. A view counts as a PDT if its `derived_table` sets `datagroup_trigger`, `sql_trigger_value`, `interval_trigger`, or `persist_for`, or sets `materialized_view: yes`.  
`primary-key-first-dimension` | Dimension | The primary key dimension must be the first dimension defined in the view.  
`primary-key-visibility` | Dimension | Primary key dimensions should be hidden (`hidden: yes`).  
`sql-table-name-uniqueness` | View | Multiple views shouldn't point to the exact same `sql_table_name`.  
`sum-measure-name-prefix` | Measure | Measures with `type: sum` or `sum_distinct` must start with `sum_` or `total_`.  
`view-dimension-order` | View | Dimensions within a view must be organized in alphabetical order.  
`view-label-presence` | View | Views must define an explicit `label:`.  
`view-measure-order` | View | Measures within a view must be organized in alphabetical order.  
`view-name-snake-case` | View | View names must be in lowercase `snake_case` (a leading `+` for refinements is allowed).  
`view-primary-key-presence` | View | Views with `sql_table_name` or `derived_table` (and no `extends`) must define a primary key.  
`visible-dimension-description-presence` | Dimension | Visible dimensions must have a `description:`.  
`visible-measure-description-presence` | Measure | Visible measures must have a `description:`.  
  
## Troubleshooting

The following sections describe common configuration issues and supported syntax variations when troubleshooting the Style Validator:

  * Configuration errors
  * Silent configuration issues
  * Accepted syntax variations



### Configuration errors

The following issues are rejected when the configuration file is loaded and are reported as an `invalid-config` error:

  * Unknown top-level keys or unknown keys inside a rule configuration.
  * A missing `schema_version` or `ruleset_version`, or an unsupported value for either parameter.
  * Shorthand scalar severities, such as `rule-name: warn`.
  * An override block with missing or empty `files` or `rules`, or a rule configuration inside an override block without `severity`.
  * An unknown rule name in an override block.
  * A custom rule whose name duplicates another custom rule or a built-in rule.
  * A type-specific key used on the wrong `rule_type` (for example, `order_by` on a `pattern_match` rule).
  * An invalid regular expression.
  * A missing `order_by` parameter (for `order` rules) or `unique_property` parameter (for `unique` rules).
  * A `position` value other than `first` (for `first_child` rules).
  * An unquoted leading `!` in a filter key, such as `!hidden: true`, which is invalid YAML tag syntax and causes the configuration file to fail to parse.



### Silent configuration issues

**Warning:** The following configuration mistakes aren't reported as errors. Check for these issues if a rule doesn't behave as expected:

  * Misspelled rule names in the global `rules` block are silently ignored.
  * Misspelled LookML type names in `select`, `filters`, `parent_filters`, `requires_child`, `forbidden_child`, or `order_by` don't raise an error. Instead, the rule never matches (or, for `requires_child`, always fails).
  * Specifying both `match` and `should_not_match`, or both `requires_child` and `forbidden_child`: only the first parameter of each pair is applied, and the second is ignored.
  * Specifying `parent_filters` on a `first_child` rule has no effect and is ignored.
  * Filters match only properties that are explicitly declared in the LookML file, not LookML default values (see Filtering syntax).
  * Regular expression patterns in `pattern_match` rules are unanchored substring matches unless you anchor them with `^` and `$` (see `pattern_match`).



### Accepted syntax variations

  * Values for `severity` and `rule_type` are case-insensitive.
  * `rule_type: pattern` is accepted as an alias for `pattern_match`.
  * Leading and trailing whitespace in `ruleset_version` is ignored.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
