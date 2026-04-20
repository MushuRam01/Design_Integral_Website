# Website Changes Required (Based on WEBSITE_RESTRUCTURE.md)

This document compares the current templates to the restructure plan and lists the required updates.

## 1) Current template structure (summary)

- Base layout: [templates/base.html](templates/base.html) provides header nav, footer, and global styles.
- Home: [templates/index.html](templates/index.html) contains a hero and a "Why Choose" features grid.
- Services: [templates/services.html](templates/services.html) has five generic service cards.
- Portfolio: [templates/portfolio.html](templates/portfolio.html) has category buttons and placeholder project cards.
- About: [templates/about_us.html](templates/about_us.html) has a single split section with placeholder image and generic copy.
- Contact: [templates/contact.html](templates/contact.html) has contact info and a form.

## 2) Global changes (site-wide)

- Replace all marketing copy to match the PDF messaging and tone.
- Update footer copy and links to match the PDF narrative and services (remove unrelated items like "Flask Systems").
- Add modular section styles (pillars, process flow, leadership cards, case study, engagement cards, brand strip, CTA band).
- Optionally move copy into a data structure (JSON/YAML or Python dict) and render with section partials for modular updates.

## 3) Home page changes

Update [templates/index.html](templates/index.html) from a 2-section page to a full storytelling flow:

- Replace hero text with:
  - Tagline: "Designing meaningful experiences"
  - Supporting copy: "We translate business vision into tangible experiences - through structured strategy and creative design thinking."
- Add sections in order:
  1) About snapshot (split feature)
  2) Philosophy and pillars (3 cards)
  3) Services overview (4 cards with bullets)
  4) 4D Approach (Discover, Define, Design, Deliver with bullets)
  5) Selected work (curated grid with named projects)
  6) Case study highlight (four-step template)
  7) Why Design Integral (five cards)
  8) Engagement model (three cards)
  9) Brands and associations (logo wall)
  10) Final CTA ("Let's Create Together" + contact details)
- Remove the current "Why Choose" section or refactor it into "Why Design Integral" using the PDF points.

## 4) Services page changes

Update [templates/services.html](templates/services.html):

- Replace the five current service cards with the four PDF disciplines:
  - Service Design
  - Experience Design
  - Industrial Design
  - Residential Interiors
- Each card should include the exact bullet list from the PDF.
- Remove or repurpose the existing icons to match the new service set.

## 5) Portfolio page changes

Update [templates/portfolio.html](templates/portfolio.html):

- Replace categories with the PDF groupings:
  - Retail and Experience
  - Residential
  - Industrial and Product
- Replace all placeholders with named projects from the PDF list.
- Add a case study teaser block using the four-step template.

## 6) About page changes

Update [templates/about_us.html](templates/about_us.html):

- Replace the single paragraph block with:
  - About positioning copy from the PDF
  - Philosophy statement and pillars
  - 4D process summary
  - Leadership profiles (3 cards with education, domains, strengths)
- Replace the image placeholder with leadership headshots or a studio image.

## 7) Contact page changes

Update [templates/contact.html](templates/contact.html):

- Ensure the "Let's Create Together" CTA aligns with the PDF.
- Use official contact details:
  - Narayanan Rajagopalan
  - +91 8861207642
  - narayanan@designintegral.com
  - www.designintegral.com

## 8) CSS changes

Update CSS to support new modules and layout rhythm:

- Add new section styles to [templates/css/index.css](templates/css/index.css) for pillars, process flow, engagement model, brand strip, case study, CTA band.
- Extend [templates/css/about_us.css](templates/css/about_us.css) for leadership cards and process summary.
- Update [templates/css/services.css](templates/css/services.css) to support bullet lists inside cards.
- Update [templates/css/portfolio.css](templates/css/portfolio.css) to support new categories and case study teaser.
- Update [templates/css/base.css](templates/css/base.css) to include global section spacing utilities and any shared card styles.

## 9) Assets required

- Hero background image
- Philosophy image or abstract visual
- Services icons or thumbnails (4)
- Leadership headshots (3)
- Project imagery (10+)
- Brand logos for the logo wall

## 10) Optional modularization (recommended)

- Create section partials (hero, split, card grid, process, leadership, case study).
- Store copy in a structured data file and load it into templates for easy changes.