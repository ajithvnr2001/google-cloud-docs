---
url: https://docs.cloud.google.com/gemini/enterprise/AGENTS/
title: Gemini Enterprise Documentation Rules for AI Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:10.147664+00:00
---

# Gemini Enterprise Documentation Rules for AI Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/AGENTS/




#  Gemini Enterprise Documentation Rules for AI Agents Stay organized with collections  Save and categorize content based on your preferences. 

This file defines mandatory content and structure rules for AI agents working within the `third_party/devsite/cloud/en/gemini/enterprise` documentation directory.

## Centralized Stylesheet

The central stylesheet `third_party/devsite/cloud/en/gemini/enterprise/docs/css/_styles.html` manages all visual styling, card button alignments, grid layouts, chip colors, and hero section banner gradients.

  * Always include ` ` at the top of Markdown landing pages.
  * Do **NOT** add inline `<style>` tags or inline `style="..."` attributes to `<div>`, `<a>`, `<p>`, or `<span>` elements.
  * Use semantic CSS classes from `_styles.html`: 
    * **Grid Helpers** : `.card-grid-2col`, `.card-grid-3col`, `.card-grid-hero`
    * **Button Containers** : `.card-button-group`, `.card-button-single`
    * **Section Banners** : `.section-banner`, `.banner-discover`, `.banner-create`, `.banner-share`
    * **Internal Banners** : `.googler-welcome-banner`



## Card Sizing & Copy Length Rules (`get-started.md` and Landing Pages)

When creating, updating, or adding DevSite cards (`<div class="devsite-card-group">`):

  1. **Card Design & Chip Scope Rules**:

     * Category chips are **ONLY** used for cards within the Web App User Journey section of `get-started.md` (under `#web-app-user-journey`): 
       * **Assistant** : `card_chip_color="blue"`, `card_chip_label="Assistant"`
       * **Personalization** : `card_chip_color="cyan"`, `card_chip_label="Personalization"`
       * **Agents** : `card_chip_color="green"`, `card_chip_label="Agents"`
       * **Skills** : `card_chip_color="purple"`, `card_chip_label="Skills"`
       * **Notebooks** : `card_chip_color="yellow"`, `card_chip_label="Notebooks"`
     * All other cards (top app entry cards on `get-started.md`, `before-you-begin.md` prerequisite cards, `index.md` role cards) must be **chip-free** (omit `card_chip_color` and `card_chip_label`).
     * Do **NOT** pass `card_href` inside `_card.html` template includes. All navigation links must be placed in `card_buttons`.
  2. **Card Description Paragraphs** :

     * Must be **20 to 25 words (130–155 characters / ~3 lines)**.
     * Maintain symmetrical paragraph lengths within the same grid group.
  3. **Action Buttons** :

     * Navigation links are placed inside `card_buttons` as `<a href="..." class="button button-flat">Link</a>`.



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
