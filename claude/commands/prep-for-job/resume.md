# Generate ATS-Optimized Resume

Generate an ATS-optimized resume tailored to a specific job opportunity.

## Usage
```
/prep-for-job/resume @linkedin-export.pdf
```

## Input
$ARGUMENTS

## Instructions

You are an expert resume writer specializing in ATS optimization for software engineering roles.

### Step 1: Gather Inputs

**LinkedIn Profile:**
- If a LinkedIn PDF export is provided as argument, read it
- If not provided, prompt: "Please provide your current LinkedIn PDF export (File > Save as PDF)"
- Extract: contact info, work history, skills, education, achievements

**Active Job:**
- Already available in context from orchestrator (parsed in Step 1)
- Extract: job title, company name, required skills, responsibilities, tech stack

### Step 2: Create Output Directory

Create directory: `~/job-applications/[COMPANY_NAME]/`
- Sanitize company name (lowercase, hyphens for spaces)
- Example: `~/job-applications/instacart/`

### Step 3: Generate Resume Following MANDATORY Guidelines

**CRITICAL: NEVER fabricate information. Only use data from the LinkedIn profile or ask clarifying questions.**

#### 3.1 ATS Optimization Rules
- Use standard section headers that ATS can parse
- No tables, columns, or complex formatting
- Include exact keywords from job description
- Use standard fonts (the PDF converter will handle this)

#### 3.2 Required Sections (in order)

**Header:**
```
# [FULL NAME]
**[City, Province/State, Country]**
[Phone] | [Email] | linkedin.com/in/[handle] | [blog url]
```

**REQUIRED: Blog URL** - If not in source materials, ALWAYS ask: "What is your blog/portfolio URL?"

**Professional Title & Keywords:**
```
## [JOB TITLE MATCHING THE POSTING]
**[Keyword 1] | [Keyword 2] | [Keyword 3] | [Keyword 4] | [Keyword 5]**
```

**Summary Section (use exact header `## Summary`):**
```
## Summary
[2-3 sentences]
```
- Years of experience + key expertise
- Top achievement with metrics
- AI forward-looking statement: excitement to spearhead AI initiatives, integrate AI into development workflows
- **Include soft skills from JD** - Weave in exact phrases like "communication skills", "fast-paced environment", "high-agency", "attention to detail" naturally

**Technical Skills (bullet list format):**
- Use markdown bullet list (dashes), NOT bold-label format
- Format each category as: `- Category: skill1, skill2, skill3`
- Example:
  ```
  ## Technical Skills
  - Languages: TypeScript, JavaScript, Ruby, Python, SQL, HTML5, CSS3
  - Frontend: React, Next.js, Hotwire, Stimulus, Component-based UI Architecture
  - Backend: Node.js, Ruby on Rails, Sidekiq, REST APIs, GraphQL, Webhooks
  ```
- Prioritize skills mentioned in job description FIRST
- Group by category: Languages, Frameworks, Databases, Cloud/DevOps, Testing

**AI & Development Innovation:**
- Position AFTER Technical Skills, BEFORE Professional Experience
- 2-3 bullets showcasing AI-assisted development practices
- Claude Code workflows, AI pair programming, automated code generation
- Quantify productivity gains where possible
- Ask user: "What specific AI tools or workflows have you used? What productivity gains have you seen?"

**Professional Experience (reverse chronological):**
- Company name, job title, dates, location
- **Date format (ATS-optimized):** Use abbreviated months: "Dec 2021 - Dec 2025" not "December 2021 - December 2025"
- 3-5 bullet points per role using STAR method:
  - Start with action verb
  - Include context (Situation/Task)
  - Describe what YOU did (Action)
  - Quantify results (Result): %, $, time, scale

**Education (use exact header `## Education`):**
- Degree, institution, graduation year
- **Recent Learning** sub-section for courses/certifications (even basic/awareness level):
  - AI/ML: Andrew Ng courses, DeepLearning.AI, fast.ai
  - Cloud: AWS, GCP, Azure certifications
  - Platforms: Udemy, Coursera, LinkedIn Learning
- Ask user: "Any recent courses or certifications? Include even introductory ones - they show continuous learning."

**Key Achievements (optional):**
- 3-4 major career highlights with metrics

#### 3.3 STAR Method Examples

Good: "Led Ruby 2.0 to 3.0 migration for platform serving 80,000+ organizations, implementing staged rollout with comprehensive test coverage: zero production incidents"

Bad: "Responsible for Ruby upgrades" (no STAR, no metrics)

#### 3.4 Tailoring Rules
- Match professional title exactly or closely to job posting
- Reorder skills to match job requirements order
- Emphasize relevant experience, minimize unrelated work
- Mirror language/terminology from job description
- **Extract soft skills from JD** and include exact phrases:
  - Common soft skills: "communication skills", "cross-functional", "collaboration", "fast-paced", "attention to detail", "proactive", "high-agency", "problem-solving"
  - Include in Summary section and experience bullets where natural
  - Multi-word phrases must appear verbatim (not paraphrased)

#### 3.5 Content Density & 2-Page Calibration (LEARNED RULES)
**Target: the exported PDF fills 1.9-2.0 pages. Never less than 1.9, never more than 2.0.**

These rules exist because past runs failed two ways: (a) verbose content overflowed to 3 pages, and (b) over-aggressive trimming collapsed it to 1.5 pages of crushed, unreadable bullets that also hurt ATS.

- **One accomplishment per bullet.** NEVER merge multiple accomplishments into a run-on sentence with semicolons to save space. Distinct, keyword-rich bullets read better AND score better in ATS (ATS rewards discrete bullets).
- **Fix length with CONTENT, not by crushing bullets:**
  - **Too long (3 pages):** remove the least-relevant bullets/roles entirely (oldest, least JD-relevant first). Keep the surviving bullets full and well-written.
  - **Too short (<1.9 pages):** restore detail to existing bullets or add back a relevant bullet/role. Do NOT inflate with whitespace or filler.
- **Spacing is the calibrator's job, not yours.** The build script (Step 6b) auto-tunes line-height to land the fill at 1.9-2.0 pages. Your job is to get the CONTENT volume right so the calibrator has something in range to find.
- Keep bullets readable: distinct action verb start, real metrics, MAX 40 words (constraint #7).
- A typical 2-page resume = header + title/keywords + Summary + Technical Skills (~8 rows) + AI Innovation (3-4 bullets) + 4 roles (3-5 bullets each) + Education + Recent Learning. Adjust role/bullet count to hit the page target.

### Step 4: Ask Clarifying Questions

Before generating, ALWAYS ask about:
1. **Blog/portfolio URL** (REQUIRED - never skip this question)
2. Any recent projects not on LinkedIn?
3. Specific AI/Claude Code achievements to highlight?
4. Metrics for key accomplishments if not in LinkedIn?
5. Any skills to emphasize or de-emphasize?

### Step 5: Generate and Save

1. Generate resume in Markdown format
2. Save to: `~/job-applications/[COMPANY_NAME]/RESUME.md`

### Step 6: Import to Google Docs

Import the resume to Google Docs and apply professional formatting via Apps Script.

**IMPORTANT: This step MUST use the Apps Script formatter. Do NOT attempt alternative approaches (HTML import, manual formatting, etc). If the script fails, follow the troubleshooting steps below.**

1. **Import markdown** using `import_to_google_doc`:
   - `user_google_email`: use the email from the resume header
   - `file_name`: "[COMPANY_NAME] - Resume"
   - `content`: the full RESUME.md content
   - `source_format`: "markdown"
   - Save the returned `Document ID` for the next step.

2. **Apply formatting** using `run_script_function`:
   - `script_id`: `1NcUu0AbvreKfwBlWztpNYonCp3vG5h7A4xvXaOj2HkfpMTgA3EHCMDkV`
   - `function_name`: `resumeFormatter`
   - `parameters`: `["<DOCUMENT_ID from step 1>"]`
   - `dev_mode`: `true`

   This applies: Arial font, H1 18pt, H2 12pt, H3 10.5pt, body 10pt, contact/keywords 9pt, compact spacing.

   **Troubleshooting (404 "Requested entity was not found"):**
   The Apps Script API can return intermittent 404 errors. Follow these steps IN ORDER:
   1. **Retry** the exact same `run_script_function` call 2-3 times (the API is intermittent)
   2. If still 404, ask the user to **archive all old deployments and create a fresh one**:
      - Open: https://script.google.com/d/1NcUu0AbvreKfwBlWztpNYonCp3vG5h7A4xvXaOj2HkfpMTgA3EHCMDkV/edit
      - Deploy > Manage deployments > Archive ALL existing deployments
      - Deploy > New deployment > API Executable > Deploy
      - Then retry `run_script_function` (must use `dev_mode: true`)
   3. If still failing, verify the script exists with `get_script_project` using the same script_id
   4. Check Apps Script API settings:
      - GCP API: https://console.developers.google.com/apis/api/script.googleapis.com/overview?project=558261890284
      - User settings: https://script.google.com/home/usersettings

3. **Verify**: The final Google Doc should fit in 2 pages. If it exceeds 2 pages, reduce content in the least relevant experience bullets and re-import.

### Step 6b: Export Print-Ready PDF (auto-calibrated to 1.9-2.0 pages)

Produce the final PDF that the user actually submits. This step is automatic via a
self-calibrating build script. **Always run it after RESUME.md is finalized.**

Pipeline: pandoc (markdown -> HTML) -> print CSS -> headless Chrome (-> PDF). It sweeps
line-height and picks the spacing that fills the last page ~88-97% (so total = 1.9-2.0
pages): no wasted whitespace, no overflow to a 3rd page. Arial 10pt, H1 19 / H2 12 / H3 11pt.

**Run:**
```bash
python3 ~/.me/claude/commands/prep-for-job/build_resume_pdf.py \
  ~/job-applications/[COMPANY_NAME]/RESUME.md \
  ~/job-applications/[COMPANY_NAME]/[Company]-Resume-[FullName].pdf
```

**Requirements** (all on macOS via Homebrew): `pandoc`, Google Chrome, `poppler`
(provides `pdfinfo` + `pdftoppm`), and Pillow (`pip3 install Pillow`).

**Reading the result:**
- `OK: 2 pages, last page NN% full` -> done.
- `UNDER-FILLED` -> content is too short for 2 pages. Go back to RESUME.md and ADD
  detail per rule 3.5 (restore trimmed bullets / expand). Do NOT inflate spacing. Re-run.
- `FAIL: could not reach exactly 2 pages` -> content too long. TRIM least-relevant
  bullets per rule 3.5 (do NOT crush into run-ons). Re-run.

**Verify visually** (optional): `pdftoppm -png -r 110 <pdf> /tmp/chk` then read the PNGs.

### Step 7: Save to HubSpot

Create a note on the deal using `hubspot-create-engagement`:

```json
{
  "type": "NOTE",
  "ownerId": [from hubspot-get-user-details],
  "associations": {
    "dealIds": [DEAL_ID]
  },
  "metadata": {
    "body": "<h2>📄 Optimized Resume</h2>[Full RESUME.md content as HTML]"
  }
}
```

**Note:** Convert markdown to HTML for better rendering in HubSpot.

### Step 8: Output Summary

```
## Resume Generated

**Target:** [Job Title] at [Company]

**Output:**
- ~/job-applications/[company]/RESUME.md
- ~/job-applications/[company]/[Company]-Resume-[FullName].pdf ([N] pages, [NN]% fill)
- Google Doc: [link]

**Keywords Matched:** [X] of [Y] from job description
```

### Important Constraints

1. **NEVER FABRICATE** - If information isn't in the LinkedIn profile, ASK the user
2. **Fill 1.9-2.0 pages exactly** - Never less than 1.9 (looks thin, wastes space), never more than 2.0. Fix length with content volume (add/remove bullets), NOT by crushing bullets into run-ons or inflating whitespace. The Step 6b script calibrates spacing automatically. See rule 3.5.
3. **Quantify everything** - If no metric exists, ask the user
4. **Match the job** - Every bullet should relate to job requirements where possible
5. **Active voice** - "Built", "Led", "Designed" not "Was responsible for"
6. **NO EM-DASH (—)** - Use "," or ":" instead. The character "—" is strictly forbidden.
7. **MAX 40 WORDS per bullet/paragraph** - Keep sentences concise for readability and ATS scanning.
