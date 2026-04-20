# Design Integral Website Restructure Guide

This guide maps every element from the content guide PDF into a modular site structure. It is designed to make content changes easy by isolating copy and media into reusable sections.

## 1) Core messaging and tone

Use this copy across hero areas, openers, and CTAs.

- Primary tagline: Designing meaningful experiences
- Positioning: We don't just design spaces. We craft experiences that endure.
- Core statement: Great design is not just seen - it is felt. Every space, product, and interaction must deliver trust, clarity, and delight.
- Human focus: Designing with the human at the centre
- Outcome promise: We translate business vision into tangible experiences - through structured strategy and creative design thinking.
- Why it matters: Every touchpoint shapes perception. We ensure yours builds trust, clarity, and lasting recall.

## 2) Content inventory (from the PDF)

This is the full content set that must appear somewhere on the site.

### 2.1 Philosophy pillars

- User Journey Mapping - designing with the human at the centre
- Functional Intelligence - every element earns its place
- Emotional Resonance - spaces and products that people remember

### 2.2 Services (four disciplines)

Service Design
- Customer Journey Mapping
- Process Design and Optimisation
- Experience Strategy

Experience Design
- Branded Environments
- Experience Centres

Industrial Design
- Product Concept Development
- Prototyping and Detailing
- Material and Finish Strategy

Residential Interiors
- Interior Design
- Space Planning
- Custom Furniture and Detailing

### 2.3 Approach

Discover -> Define -> Design -> Deliver

4D methodology details

Discover
- Deep dive into client brief, brand DNA, business objectives
- Stakeholder interviews and user research
- Site analysis, competitive benchmarking
- Identify unmet needs and latent opportunities

Define
- Synthesise research into clear problem statements
- Strategic framing and design principles
- Establish success metrics and project scope
- Align all stakeholders on a shared vision

Design
- Concept ideation and creative exploration
- Spatial planning, visualisation, and mood boarding
- Iterative prototyping and design development
- Material, finish, and detail refinement

Deliver
- Execution oversight and site coordination
- Vendor and contractor management
- Quality assurance at every milestone
- Handover, review, and post-delivery support

### 2.4 Leadership

Founder and Design Principal
- Name: Narayanan Rajagopalan
- Experience: 20+ years design and build leadership
- Education: B.Arch (Pune), M.Des NID Ahmedabad, IIMB / C-DAC / MET
- Domains: Retail, Residential, Product, Experience
- Associated with: Featherlite, Grottini, Hettich, Tata Elxsi, HomeLane

Partner and Operations Head
- Name: Ranjan Ray
- Experience: 20+ years, turnkey expert, end-to-end project execution
- Education: B.Arch SPA Delhi, M.Des NID Ahmedabad
- Domains: Retail, Commercial, Residential
- Strength: Site coordination, vendor and delivery management

Associate and Design Lead
- Name: Kundhavi Nagaraj
- Experience: 8 years, retail experience design specialist
- Education: B.Arch, M.Des Barcelona
- Expertise: Retail environments and brand experience
- Edge: European design sensibility, Indian market insight

### 2.5 Selected work (curated)

Retail and Experience
- Airport Retail Kiosks
- Brand Experience Stores
- Exhibitions

Residential
- Premium Apartments
- Villas with Custom Interiors
- Space Optimisation Projects

Industrial and Product
- Custom Display Systems
- Furniture Design
- Retail Fixtures

Notable projects mentioned
- Baxter Experience Center - Bangalore
- Tata Steel Safety Training Center - Jamshedpur, Kalinganagar (copyright Tata Elxsi)
- Air India Exhibition - modular 2000 sft exhibition kit (copyright Tata Elxsi)
- Caravan Craft retail environments - Pune and Bangalore
- Featherlite showroom - Mumbai
- Pablosky retail environments - Spain (copyright Grottini)
- Freeway retail environments - Italy (copyright Grottini)
- Renascimento retail environments - Italy (copyright Grottini)
- Twin Birds womens clothing brand - India
- Claro eyewear brand - Italy (copyright Grottini)
- Modular Desking System
- Theme Based Living - HomeLane
- Hero Palatial - Theme Based Living
- Twin Birds retail kiosk - Whitefield

### 2.6 Case study template

Design in Action: From brief to brilliance

- Client Objective: understand brief, business goals, end user expectations
- Design Challenge: identify constraints, spatial or functional gaps
- Solution Approach: concept development, iterative design, material strategy
- Final Outcome: meeting expectations, delivering the right experience

### 2.7 Why Design Integral

- Experience-driven thinking (human-centred design at every step)
- Deep industry expertise (20+ years across diverse domains)
- End-to-end capability (concept to quality delivery)
- Detail-oriented execution (no element left to chance)
- Scalable solutions (built to grow with your business)

### 2.8 Engagement model

- Design Consulting: strategic advisory, audits, concept direction
- Design + Execution Support: concept through site supervision and delivery
- Turnkey Design Solutions: full end-to-end ownership (selective projects)

### 2.9 Brands and associations

- A logo wall of trusted brands and institutions (content is visual, list TBD)

### 2.10 Contact details

- Narayanan Rajagopalan
- Phone: +91 8861207642
- Email: narayanan@designintegral.com
- Website: www.designintegral.com

## 3) Modular site architecture

Use reusable sections so each page is assembled from consistent, swappable blocks.

### 3.1 Section modules

- Hero (headline, subhead, supporting paragraph, CTA row, background image)
- Split feature (left text, right image or vice versa)
- Pillar trio (three-card grid)
- Service grid (four primary service cards with bullet lists)
- Process flow (four steps horizontal or vertical)
- Leadership cards (photo, title, bio, key facts)
- Project grid (category filters + cards)
- Case study panel (four-step template)
- Engagement model cards (three cards)
- Brand strip (logo wall)
- CTA band (short statement + contact link)

### 3.2 Data-driven content (modular approach)

Keep copy in a structured data object, then render sections from it. The data can live in Python (for now) or in a JSON or YAML file loaded by the app. Example structure:

```yaml
site:
  tagline: "Designing meaningful experiences"
  positioning: "We don't just design spaces. We craft experiences that endure."
  trust_statement: "Every touchpoint shapes perception. We ensure yours builds trust, clarity, and lasting recall."

home:
  hero:
    title: "Design Integral"
    subtitle: "Designing meaningful experiences"
    support: "We translate business vision into tangible experiences through structured strategy and creative design thinking."
    ctas:
      - label: "View Projects"
        href: "/portfolio"
      - label: "Our Services"
        href: "/services"
  philosophy:
    headline: "Experience design at the core"
    quote: "Great design is not just seen - it is felt."
    pillars:
      - title: "User Journey Mapping"
        desc: "Designing with the human at the centre"
      - title: "Functional Intelligence"
        desc: "Every element earns its place"
      - title: "Emotional Resonance"
        desc: "Spaces and products that people remember"
```

The templates only render the data, so changing content later does not require HTML edits.

## 4) Page-by-page build plan (mapped to existing routes)

### 4.1 Home (primary storytelling hub)

Update [templates/index.html](templates/index.html) to include these sections in order:

1) Hero
- Title: Design Integral
- Tagline: Designing meaningful experiences
- Supporting text: We translate business vision into tangible experiences - through structured strategy and creative design thinking.
- CTA buttons: View Projects, Our Services

2) About snapshot (split feature)
- Header: About Design Integral
- Copy: We don't just design spaces. We craft experiences that endure.
- Subcopy: A multidisciplinary design consultancy crafting meaningful, functional, and emotionally resonant spaces and products.

3) Philosophy and pillars
- Quote: Great design is not just seen - it is felt.
- Pillars: User Journey Mapping, Functional Intelligence, Emotional Resonance

4) Services overview (four cards)
- Service Design, Experience Design, Industrial Design, Residential Interiors
- Each card has short bullets

5) 4D Approach
- Title: Discover -> Define -> Design -> Deliver
- One sentence summary: A structured methodology that ensures every project is rooted in purpose, shaped by insight, and delivered with precision.
- Four cards with the 4D bullet lists

6) Selected work (curated grid)
- Use categories: Retail and Experience, Residential, Industrial and Product
- Add featured project cards with images and short captions (use the notable project list above)

7) Case study highlight
- Use the four-step template with a featured project (e.g., Tata Steel Safety Training Center)

8) Why Design Integral
- Five cards with the five reasons

9) Engagement model
- Three cards: Design Consulting, Design + Execution Support, Turnkey Design Solutions

10) Brands and associations
- Logo strip with a short line: Trusted by brands who believe design is a strategic advantage.

11) Final CTA
- Headline: Let's Create Together
- Subhead: Let's start with a conversation.
- Contact details and CTA link to the contact page

### 4.2 Services

Update [templates/services.html](templates/services.html) to align with the four core disciplines from the PDF.

- Replace current service titles with the four disciplines.
- Each card includes the exact bullet list for that discipline.
- Optional add-on: short intro block for each discipline with a photo or illustrative image.

### 4.3 Portfolio

Update [templates/portfolio.html](templates/portfolio.html) to match the curated work and project types.

- Categories should map to the PDF groupings:
  - Retail and Experience
  - Residential
  - Industrial and Product
- Populate project cards from the notable project list.
- Add a featured project section (case study teaser) with a short summary.

### 4.4 About Us

Update [templates/about_us.html](templates/about_us.html) to include:

- A short positioning paragraph (from the About section)
- Leadership profiles with the three bios and details
- The philosophy pillars and a short statement about human-centred design
- A compact 4D process summary

### 4.5 Contact

Update [templates/contact.html](templates/contact.html) to match the PDF contact details and the "Let's Create Together" CTA.

- Use Narayanan Rajagopalan name, phone, and email from the PDF
- Ensure the website address appears as text

## 5) CSS and layout alignment

Use existing CSS files as the base and add new sections in the relevant page CSS files. Reference these files for edits:

- Base layout and navigation: [templates/base.html](templates/base.html) and [templates/css/base.css](templates/css/base.css)
- Home page sections: [templates/index.html](templates/index.html) and [templates/css/index.css](templates/css/index.css)
- Services page: [templates/services.html](templates/services.html) and [templates/css/services.css](templates/css/services.css)
- Portfolio page: [templates/portfolio.html](templates/portfolio.html) and [templates/css/portfolio.css](templates/css/portfolio.css)
- About page: [templates/about_us.html](templates/about_us.html) and [templates/css/about_us.css](templates/css/about_us.css)
- Contact page: [templates/contact.html](templates/contact.html) and [templates/css/contact.css](templates/css/contact.css)

## 6) Assets checklist

Create or source visuals for these slots (use consistent cropping ratios).

- Hero background image (experience centre or spatial design context)
- Philosophy image (abstract or people-in-space)
- Services icons or illustrative thumbnails (4)
- Leadership headshots (3)
- Project images (10+ across categories)
- Brand logos (logo wall)

## 7) Implementation sequence (simple and modular)

1) Move all copy into a data structure and render sections from it.
2) Build reusable section partials (hero, split, card grid, process, leadership).
3) Assemble the home page from sections in the order above.
4) Replace services, portfolio, about, and contact copy to match the PDF.
5) Add and wire images, then refine CSS for spacing and visual rhythm.

## 8) Quick content map to existing templates

- Home: [templates/index.html](templates/index.html)
- Services: [templates/services.html](templates/services.html)
- Portfolio: [templates/portfolio.html](templates/portfolio.html)
- About: [templates/about_us.html](templates/about_us.html)
- Contact: [templates/contact.html](templates/contact.html)
- Base nav and footer: [templates/base.html](templates/base.html)

If you want, I can now translate this plan into actual template and CSS changes.