---
url: https://docs.cloud.google.com/looker/docs/looker-2-release-notes/
title: 2.x Release Notes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:21:33.953923+00:00
---

# 2.x Release Notes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-2-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  2.x Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

## Looker 2.4 2014-07-14

### LookML / Projects

  * New field parameter `format:` for [printf-style formatting](https://docs.cloud.google.com/looker/docs/reference/param-field-format)



### Explore

  * Totals working in all dialects, implemented as a separate SQL query



### Data Visualization

  * New element parameter `show_applied_filters: false` to turn off dynamic filters in title of a dashboard element
  * New dashboard parameter `refresh: N minutes` to refresh data every N minutes if the page is open



### Enterprise, Platform, and Security

  * LDAP authentication
  * Two-factor authentication



### Bug Fixes and Tweaks

  * Add/delete projects moved to admin panel



## Looker 2.2 2014-06-09

### Data Visualization

  * [Custom map visualizations](https://docs.cloud.google.com/looker/docs/visualization-types#maps)
  * [Dimensional scatter plot](https://docs.cloud.google.com/looker/docs/scatter-options)
  * Automatic x_axis_scale detection
  * x_padding_left and x_padding_right option for charts
  * Specify colors, series_colors, series_labels, reference lines, and more in looker_type charts
  * Plot geo coordinates (lat/long) on world map



### LookML / Projects

  * Redesigned Projects experience
  * LookML project search with regular expressions & find and replace
  * JGit bundled with Looker (replaces server-based git)
  * [Liquid templating](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) (replaces ERB)
  * [More flexible join syntax](https://docs.cloud.google.com/looker/docs/reference/param-explore-join)
  * Top nav menus update upon LookML file save (instead of after page reload)
  * Declare a base_view as hidden: true
  * [Table Calculations](https://docs.cloud.google.com/looker/docs/table-calculations): type: running_total
  * Line-by-line git diffs in LookML editor (yellow for modified, green for added, red for deleted)



### Explore

  * Jump to LookML error link from Explore page
  * Improved and more flexible number filter syntax (e.g. >, <, != operators)
  * SQL Runner moved to Explore menu
  * SQL tab updates live as query is constructed in UI (with EXPLAIN)



### Enterprise, Platform, and Security

  * Improved admin audit and Looker usage panels
  * Embeddable iframe code added to public URL box



### Bug Fixes and Tweaks

  * Lots of looker_ (area, column, etc.) and reference line bug fixes. Thanks to the beta testers!
  * Improved login and auto logout flow
  * Convert "yyyymmdd" format to valid time field
  * Year filters now use date syntax (instead of integer)
  * Dozens of other bug fixes and tweaks!



## Looker 2.0 2014-04-28

### Data Visualization (Beta)

  * Maps (US & World) chart types: [Coordinates Plot](https://docs.cloud.google.com/looker/docs/visualization-types), [Choropleth](https://docs.cloud.google.com/looker/docs/visualization-types)
  * New Cartesian chart types: [Single Record](https://docs.cloud.google.com/looker/docs/visualization-types), [Donut](https://docs.cloud.google.com/looker/docs/visualization-types), [Donut Multiples](https://docs.cloud.google.com/looker/docs/visualization-types)
  * Updated Cartesian chart types: [looker_column](https://docs.cloud.google.com/looker/docs/visualization-types), [looker_line](https://docs.cloud.google.com/looker/docs/visualization-types), [looker_area](https://docs.cloud.google.com/looker/docs/visualization-types), [looker_pie](https://docs.cloud.google.com/looker/docs/visualization-types)
  * Reference Lines: static, median, mean, min, max, ranges, standard deviation, variance
  * Additional formatting parameters (interpolation, colors, hide_points, hide_legend)
  * Automatically detect and format date axes



### LookML

  * [Developer vs. Production Mode SQL option in PDTs](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode)
  * Field name validation before query run
  * Generate files as .model.lookml, .view.lookml, .dashboard.lookml
  * When on, user access filters block filter suggestions
  * select_filter aliased to suggest_filter in dashboard filters



### Enterprise and Security

  * Auto user log out (with warning) unless trusted computer



### SQL Dialects

  * Support for Teradata Aster 6.0
  * (Beta) Support for Oracle Database 11g



### Bug Fixes and Tweaks

  * Persistent derived table fixes
  * Drilling into a dashboard chart keeps filters applied
  * Timezone conversion in Redshift
  * Warn when changing timezone that it affects all users
  * Show conditional filters in dashboard URL
  * Return 401 error as JSON API responses when authentication fails
  * Add link to SQL Runner from connections page
  * MS SQL Server suggest fix



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
