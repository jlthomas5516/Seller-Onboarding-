# CipherRounds — Objective Vendor Comparison

**Purpose:** Support a prospect follow-up with an objective, side-by-side view of digital rounding platforms — capabilities, implementation, support, and operational resources — not marketing collateral.

**Prepared for:** Jen (prospect contact)  
**Prepared by:** CipherHealth  
**Date:** August 14, 2026  
**Classification:** CIPHERHEALTH CONFIDENTIAL — share externally only with prospect approval

---

## Draft reply email

**Subject:** Rounding platform comparison + staying in touch

Hi Jen,

Thank you for the candid update — it’s helpful to know the CNOs see value and that the gating factors are alignment, funding, and operational support rather than product fit. That tracks with what we see at similar systems, and we’re glad Caryn and you are continuing those internal conversations. No pressure from our side on timing; we’ll stay available when it’s useful.

In the meantime, attached is an objective comparison of CipherRounds against the rounding options we most often see evaluated alongside us: **NRC Health**, **GetWell Rounds+**, **Epic-native rounding**, and **paper/manual programs**. It focuses on what you asked for:

- Capabilities (what each platform actually does in daily workflow)
- Implementation requirements (IT, EHR, hardware, timeline)
- Support model (who does what after go-live)
- Resource needs (clinical, operational, and IT FTE expectations)

We pulled this together from our implementation playbooks, published vendor documentation, and third-party market summaries — not from sales decks. Where a row reflects CipherHealth-specific delivery (for example, typical IT hours or clinical partnership structure), we’ve labeled it clearly. Where we could not verify a competitor claim from public sources, we’ve marked it **Unverified** rather than guess.

If it would help your internal stakeholders, we can also walk through the comparison on a 30-minute call and tailor the “resource needs” section to your unit count and current rounding model.

Thanks again, and please reach out whenever the internal work moves forward.

Best,  
[Your name]

**Attachment:** This document (or a formatted PDF export)

---

## How to read this document

### Scope

This comparison covers **inpatient digital rounding** — structured leader/nurse/patient/location rounds with real-time issue capture, routing, and reporting. It does **not** fully compare:

- Post-discharge outreach (CipherOutreach is noted only where it affects total platform footprint)
- In-room bedside entertainment/education platforms (GetWell Inpatient, Oneview) except where they integrate with rounding
- HCAHPS survey vendors (Press Ganey, Qualtrics) unless they also offer structured rounding workflows

### Sources

| Source type | Used for |
|---|---|
| CipherHealth AE onboarding library (internal) | CipherRounds capabilities, implementation benchmarks, support model, outcomes context |
| Vendor public product pages | NRC Health, GetWell, Epic positioning |
| AVIA Marketplace product profiles | Cross-vendor capability lists where available |
| Third-party market analysis (Ouva 2026 patient engagement guide) | Category framing and neutral vendor summaries |

### Legend

- **●** = Core / native capability  
- **◐** = Partial, add-on, or depends on configuration  
- **○** = Not a primary focus or typically requires a separate product  
- **Unverified** = Could not confirm from public documentation; validate in RFP/demo

---

## Master side-by-side (shareable)

**Vendors:** CipherRounds · NRC Health Rounding · GetWell Rounds+ · Epic-native · Paper/manual  
**Legend:** ● Core · ◐ Partial / config-dependent · ○ Not primary · — Not applicable

### At a glance

| | **CipherRounds** | **NRC Health** | **GetWell Rounds+** | **Epic-native** | **Paper / manual** |
|---|---|---|---|---|---|
| **What it is** | Purpose-built digital rounding for patient, staff, and location rounds with closed-loop recovery | Mobile-first rounding + PX/employee analytics (Nobl acquisition, 2024) | Configurable digital rounding/survey platform; part of broader GetWell suite | EHR modules + internal workflow build (Rover = clinical bedside, not PX rounding) | Clipboards, spreadsheets, memory |
| **Vendor category** | Care coordination / rounding specialist | Experience measurement + rounding | Inpatient engagement + rounding | System of record | None |
| **Typical buyer** | CNO, PX, CQO | CNO, PX, HR | CNO, COO (often existing GetWell shop) | CIO + CNO (“use Epic”) | Unit managers |
| **Incremental license cost** | Yes — enterprise SaaS | Yes — enterprise SaaS | Yes — enterprise SaaS | Often perceived as “free” (Epic already licensed) | None |
| **Hidden cost** | Low IT lift if certified integration | Analytics/HRIS integration + quarterly consulting cadence | Larger if GetWell Inpatient bundled; interface work | **High** internal Epic analyst + nursing ops time | Nurse/leader time, inconsistency, late recovery |

---

### Capabilities

| Capability | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Patient experience rounding** | ● Scripts mapped to HCAHPS domains; real-time routing | ● Leader rounding on patients + environment | ● Real-time surveys + dashboards | ◐ Custom Flowsheets/forms; no native PX rounding product | ◐ Varies by unit |
| **Leader / nurse-leader rounding** | ● | ● | ● | ◐ Build your own | ◐ |
| **Staff / employee rounding** | ● Recognition + staff listening | ● **Core strength** — employee voice, HRIS integrations | ● Employee experience use cases | ○ | ◐ |
| **Location / environmental / safety rounding** | ● CAUTI, CLABSI, falls, HAPI, environment checks | ● Listed as quality & safety use case | ● Quality, safety, regulatory checklists (100+ use cases) | ◐ Safety checks via custom build | ◐ |
| **Real-time service recovery** | ● Issue → owner in minutes; 200M+ interactions tracked start→resolution (platform) | ● Auto-alerts; vendor cites seamless resolution | ● Alerts, reminders, escalations to departments | ◐ Requires Epic workflow/In Basket build | ○ |
| **Ambient listening / AI documentation** | ● Keeps documentation off the nurse | ● Agentic AI summaries + sentiment/themes (2026 positioning) | ○ Not a primary Rounds+ feature | ○ | ○ |
| **Predictive “who to round on first”** | ◐ Program rules + analytics | ● **Core strength** — Predictable Experience heatmaps + predictive scores | ◐ Stronger if GetWell Inpatient data present | ◐ Manual prioritization or custom build | ○ |
| **Historical PX context at bedside** | ◐ Via EHR + platform data | ● **Core strength** — past HCAHPS/survey/round data in context | ◐ With Inpatient + EHR pre-population | ◐ If built into Epic workflow | ○ |
| **Surveys-by-text / batch outreach** | ◐ (CipherOutreach for outbound) | ◐ Real-time feedback focus | ● Text/email batch surveys to patients/staff | ◐ MyChart / SMS if configured | ○ |
| **HCAHPS domain mapping** | ● Built into round scripts | ● Analytics + benchmark comparison | ◐ Configurable forms | ◐ DIY | ○ |
| **Multi-language** | ● | ◐ Confirm in demo | ◐ Pediatric: parent/caregiver rounding | ◐ MyChart language support | ◐ |
| **EHR write-back (discrete fields)** | ● Near-real-time Epic Flowsheets (HL7-ORU); MDM for issues | ● EMR integrations (vendor-stated) | ● Epic, Cerner, Meditech + 6 others; ADT | ● Native chart | ○ |
| **Data latency to EHR** | Seconds (near-real-time) | Vendor-stated real-time | Real-time alerts; interface-dependent | Native — but recovery loop is separate | — |
| **Inpatient + post-discharge same vendor** | ● CipherOutreach on one platform | ○ Surveys/measurement core; not execution layer | ◐ GetWell Navigate (separate product) | ◐ Epic worklists / MyChart | ○ |
| **In-room bedside engagement (TV/tablet)** | ○ Not required | ○ | ● **GetWell Inpatient** — routes requests into Rounds+ | ○ | ○ |
| **Industry benchmarks in product** | ◐ Outcomes library + customer analytics | ● **Core strength** — NRC benchmarks, quarterly reviews | ◐ Embedded reporting | ○ | ○ |
| **Peer-reviewed / published outcomes** | ● 15+ years customer outcomes (HCAHPS, HAI, turnover) | ◐ Vendor-cited: +22 HCAHPS percentile pts, 30% call lights, 40% falls | ◐ Primarily workflow/PX improvement | ○ Limited for rounding | ○ |

---

### Implementation

| Requirement | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Integration method** | HL7 ADT in; ORU/MDM/Flowsheet out; certified Epic | EMR + HRIS + recognition + data warehouse | HL7/ADT + EMR interface; optional GetWell product feeds | Native + possible Vendor Services for third-party | — |
| **Epic Flowsheet mapping** | ● Configurable **without custom code** (internal) | ● Vendor-stated EMR integration | ● Epic supported; interface project typical | ● Native | — |
| **Hardware required** | Mobile (BYOD or hospital device) | Mobile | Mobile/tablet; **Inpatient adds bedside TVs/tablets** | Mobile (Rover) or workstation | Paper |
| **In-room infrastructure** | None | None | Optional — significant if Inpatient | None | None |
| **Typical go-live timeline** | **4–8 weeks** (integrated program); 3–8 weeks scoping/build per program type | Phased — confirm in SOW | Rounds+ standalone: weeks; **Inpatient + Rounds+: months** | **Months** common for net-new workflow | Immediate |
| **Buyer IT hours (order of magnitude)** | **<25 hours** (CipherHealth benchmark) | Medium — EMR + analytics stack | Medium–high | **Highest** — Epic analyst, interfaces, testing | Minimal |
| **Custom code required** | No for standard Flowsheet programs | Confirm in SOW | Interface configuration typical | Often yes — workflows, reports, routing | No |
| **Certifications / security** | HITRUST CSF, SOC 2 Type II, HIPAA, TX-RAMP L2 | Confirm in RFP | HIPAA BAA, TLS 1.2+, ~99.95% SLA (AVIA) | Epic org security model | N/A |
| **Key dependencies** | ADT feed, program design, unit champions | Often existing NRC survey relationship; HRIS for employee rounding | Scope **Rounds+ only vs. full GetWell stack** | Epic module priority, internal build capacity | None |

---

### Support model

| Element | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Implementation owner** | CipherHealth Implementation (certified EHR) | NRC professional services | Get Well PS + training | Internal IT + Epic team | Internal |
| **Clinical program design** | CipherClinical (RNs/MSNs) + Clinical Advisory Board | NRC clinical/consulting; quarterly benchmark reviews | Get Well training + config | Internal nursing/PX leadership | Informal |
| **Post-go-live owner** | CSM + outcomes reviews | Customer success + quarterly data reviews | Customer success | Internal — no vendor CSM | None |
| **Analytics** | Cipher dashboards + annual outcomes review | **Benchmark-centric** reports + NRC analyst meetings | Rounds+ dashboards; richer with Inpatient | Epic SlicerDicer/report builds | Manual |
| **Expansion (new units)** | CSM + Implementation | NRC CS | Config + training | Epic project queue | Local |
| **Security / AI governance** | Dedicated security reviews; AI governance per deployment | Confirm in RFP | Standard SaaS security pack | Internal | — |

---

### Resource needs (operational)

| Resource | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **Executive sponsor** | CNO or PX exec | CNO + **often HR** (employee rounding) | CNO / COO | CNO + CIO | Nurse manager |
| **Program owner** | 0.25–0.5 FTE PX/nursing lead | 0.25–0.5 FTE PX + analytics admin | 0.25–0.5 FTE (+ Inpatient admin if bundled) | 0.25–0.5 FTE + **Epic analyst allocation** | ~0.1 FTE |
| **Unit champions** | 1 per pilot unit | 1 per pilot unit | 1 per pilot unit | 1 per pilot unit | Informal |
| **Frontline time per round** | ~2–5 min capture; ambient listening cuts after-round admin | Similar; AI summary reduces documentation | Similar | Often **higher** — manual charting | 5–10+ min |
| **IT — implementation** | Low | Medium | Medium–high | **High** | None |
| **IT — ongoing** | Low (SaaS) | Low–medium | Medium (devices + interfaces if Inpatient) | Medium (Epic maintenance) | None |
| **Change management** | Moderate | Moderate | **Higher** if Inpatient deployed | **High** — workflow redesign | Low |
| **Nursing FTE impact** | Designed to **reduce** admin (0.5 hr/day saved — site benchmark) | Vendor cites call-light reduction, fall reduction | Reduces documentation vs. paper | Often **adds** workflow steps unless carefully built | High variability |

---

### Documented outcomes (examples — not guarantees)

| Outcome area | CipherRounds | NRC Health | GetWell Rounds+ | Epic-native | Paper / manual |
|---|---|---|---|---|---|
| **HCAHPS / experience** | 99th percentile key domains; +389% RN responsiveness (Lenox Hill); +36% top-box (Providence) | Vendor-cited: **+22 percentile points** across domains | Workflow/PX improvement stories | Limited rounding-specific data | Unmeasured / variable |
| **Safety (HAI, falls)** | 30%+ CAUTI/CLABSI drop; 78%/85% falls reduction | Vendor-cited: **40% fall reduction** year 1 | Safety checklist use cases | Depends on internal program | Unmeasured |
| **Staff / retention** | 9.2% vs 15% turnover at >90% rounding; 42% burnout drop (Norton) | Vendor-cited: employee voice → retention | Employee rounding use cases | — | — |
| **Operational** | 0.5 hr/day saved per nurse; 57% complaint/grievance reduction (platform) | Vendor-cited: **30% call-light reduction** | Real-time recovery alerts | — | — |

---

### When each option wins (neutral)

| Primary goal | Best fit |
|---|---|
| Standardize patient + leader + location/safety rounding with closed-loop recovery; optionally combine with post-discharge on one platform | **CipherRounds** (+ CipherOutreach if transitions matter) |
| PX/employee listening, predictive prioritization, benchmark analytics; already an NRC survey customer | **NRC Health** |
| Full in-room engagement (education, requests, entertainment) with rounding as one module | **GetWell Inpatient + Rounds+** |
| Minimize new vendors; willing to spend internal Epic + nursing ops capacity | **Epic-native build** |
| No budget or alignment this cycle | **Paper/manual** |

**Bottom line:** These are not interchangeable. NRC leads on **measurement, prediction, and benchmarks**. GetWell leads when **in-room engagement** is already in scope. Epic-native minimizes **vendor spend** but shifts cost to **internal build and staffing**. CipherRounds is built for **operational rounding + recovery + safety** with a path to **post-discharge on the same coordination layer**.

---

## Detailed notes (by vendor)

### CipherRounds (CipherHealth)

- **Core job:** Execute rounding — patient, leader, staff, location — and close the loop before discharge.
- **Differentiators vs. others:** Same platform as CipherOutreach (pre-admission through post-discharge); ambient listening; safety rounding tied to HAC/VBP; near-real-time Flowsheet write-back without custom code; clinical SMEs co-design programs.
- **Implementation (internal benchmarks):** 4–8 weeks; <25 IT hours; HL7 ADT in / ORU+MDM out; 70%+ of customers on Epic (350+ hospitals).
- **Support:** Clinical Strategy, Solution Consulting, Implementation, CSM, Analytics, Security.

### NRC Health Rounding

- **Core job:** Make rounding intentional with **predictive prioritization**, **benchmark analytics**, and **employee + patient voice** in one relationship — especially if NRC already runs your HCAHPS/survey program.
- **Differentiators vs. others:** Predictable Experience (predicted in-stay experience scores); deep historical PX context at bedside; quarterly benchmark reviews with NRC analysts; Nobl acquisition (2024) for real-time rounding; HRIS integrations for employee rounding.
- **Tradeoffs:** Measurement and PX intelligence are the center of gravity; post-discharge **execution** (TCM calls, automated follow-up) is not the core product. Validate integration depth and timeline in SOW.

### GetWell Rounds+

- **Core job:** Flexible digital data collection — PX rounding, employee rounding, safety/regulatory audits, discharge data — on one configurable platform.
- **Differentiators vs. others:** 100+ use cases; surveys-by-text/email for batch reach; unlimited users/devices; **deepest value when GetWell Inpatient is deployed** (in-room requests route into Rounds+ for recovery).
- **Tradeoffs:** Scope creep risk — Rounds+ alone vs. Inpatient + Rounds+ is a very different project size. GetWell Navigate is a separate product for outpatient/post-discharge AI texting. No ambient listening as a headline capability.

### Epic-native (build inside Epic)

- **Core job:** Keep everything in the EHR; avoid incremental vendor spend.
- **Reality check:** Epic Rover is a **clinical bedside** tool (BCMA, vitals, specimen collection) — **not** a leader/PX rounding platform. PX rounding in Epic typically means custom Flowsheets, reports, and In Basket routing built by your Epic team.
- **Tradeoffs:** License may be “free,” but **labor is not** — Epic analyst time, workflow design, and ongoing maintenance. Passive documentation without purpose-built recovery/routing. Internal playbooks note Epic-native outreach reaches ~40% of patients vs. ~96% digital-first; data can lag 24 hours if batch-based.

### Paper / manual

- **Core job:** Zero software cost.
- **Tradeoffs:** Inconsistent coverage, issues surface after discharge, no closed-loop tracking, highest documentation burden, no cross-unit analytics. Status quo bias is the main “competitor” in stalled deals.

---

## Questions for Jen’s internal working group

These help tailor the comparison to their environment:

1. **Scope:** Patient-only rounding, or also leader, staff, and location/safety rounding?
2. **EHR:** Epic (which integration — Flowsheets, Rover, both)? Cerner/Meditech?
3. **Existing vendors:** NRC, GetWell, or Press Ganey/Qualtrics already in-house?
4. **Success metrics:** HCAHPS domains, HAC/safety, staff retention, grievances — which is the board-level priority?
5. **Operational constraint:** Is the blocker nursing FTE, IT queue, or vendor budget?
6. **Post-discharge:** Is rounding evaluation separate from TCM/TEAM/post-discharge outreach?

---

## Appendix A — CipherRounds capability checklist (for RFP alignment)

Use this as a line-item checklist against any vendor response.

- [ ] Patient, leader, staff, and location rounding in one platform  
- [ ] Real-time issue routing with ownership and resolution tracking  
- [ ] HCAHPS domain mapping in round scripts  
- [ ] Safety rounding (falls, HAPI, CAUTI/CLABSI, environment)  
- [ ] Ambient listening or equivalent documentation reduction  
- [ ] Bidirectional EHR integration with discrete Flowsheet write-back  
- [ ] Near-real-time data (not nightly batch only)  
- [ ] Multi-language rounding  
- [ ] Role-based analytics (unit, leader, domain, trend)  
- [ ] Clinical implementation support from licensed clinicians  
- [ ] Documented outcomes in peer-reviewed or enterprise case studies  
- [ ] HITRUST/SOC 2/HIPAA compliance artifacts  
- [ ] Optional post-discharge outreach on same platform  

---

## Appendix B — Document maintenance

| Item | Action |
|---|---|
| **Pricing** | Not included — requires scoped proposal based on bed count, modules, and integration |
| **Competitor rows marked Unverified** | Re-validate before formal RFP submission |
| **References** | Named customers cited only when cleared for that account |
| **Updates** | Refresh quarterly or when major competitor/Epic releases change the landscape |

---

*CipherHealth internal and confidential. Customer-facing shareable version should remove internal-only benchmarks marked explicitly as CipherHealth delivery data if your sponsor prefers.*
