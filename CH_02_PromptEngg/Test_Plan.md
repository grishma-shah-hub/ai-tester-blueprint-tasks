# Test Plan: VWO Login Page

**Target URL:** https://app.vwo.com/#/login (redirects to https://app.wingify.com)
**Document Type:** Test Plan (no test cases/scripts included)
**Prepared for:** QA execution team
**Status:** Draft — audit-ready; items marked "To be verified" require confirmation before or during execution

---

## 1. Scope

### In Scope
UI-driven functional, negative, usability, security-adjacent, compatibility, accessibility, and regression testing of the login experience at `https://app.vwo.com/#/login`, limited to what is explicitly confirmed on the page plus the functional expectations supplied for this plan:

- Email + password authentication and landing on the dashboard for an existing user
- Password field behavior, including default masking and the show/hide (eye icon) toggle
- "Forgot Password?" recovery flow, accessible without an active session
- "Remember me" checkbox and its effect on session persistence across browser restarts
- "Sign in with Google" as a functional-equivalent authentication path
- "Sign in using SSO" as a functional-equivalent authentication path (provider unconfirmed)
- "Sign in with Passkey" as a functional-equivalent authentication path, across platform and roaming authenticators where feasible
- "Start a FREE TRIAL" signup path, validated as separate from the existing-user login path
- Privacy Policy / Terms links (navigation-level validation)
- The `app.vwo.com` → `app.wingify.com` domain migration and its effect on bookmarked links, in-progress OAuth redirects, and pre-migration password-reset emails
- Cross-browser and cross-device compatibility of the above, per the matrix in Section 5
- Basic accessibility of login page controls (keyboard navigation, focus states, zoom behavior)
- Baseline security-adjacent UI checks (HTTPS enforcement, no mixed content, password not exposed in page source)

### Out of Scope
- Backend authentication architecture, database design, or API-level/contract testing
- Confirmation or configuration of the specific SSO identity provider (e.g., Okta, Azure AD) — provider is unconfirmed; SSO-provider-specific behavior is excluded until confirmed (see Section 6, Risk R-01)
- Formal penetration testing or vulnerability scanning (only UI-observable security-adjacent checks are included, per Performance/Security Expectations)
- Any SLA or performance certification — the 3-second page-load figure is treated as a draft benchmark, not a confirmed SLA
- Post-authentication application functionality beyond confirming the dashboard landing occurs
- Native mobile app login (mobile browser testing is in scope; native apps are not)
- Google's and the SSO provider's own hosted consent/login screens (only the trigger, handoff, and return-to-VWO behavior are in scope)

---

## 2. Objectives

1. Confirm that an existing user can authenticate via email + password and land on their dashboard.
2. Confirm that a user can recover access via "Forgot Password?" without requiring an existing session.
3. Confirm "Remember me" persists the session across a browser restart when checked, and does not persist it when unchecked.
4. Confirm "Start a FREE TRIAL" routes new users into a signup flow that is fully separate from the existing-user login path.
5. Confirm Google sign-in, SSO, and Passkey each function as authentication paths equivalent in outcome to email/password login, including handling of consent-denial/cancel scenarios.
6. Establish and track the dependency on the product/dev team to confirm the SSO identity provider before SSO test execution can be considered complete.
7. Validate Passkey against both platform authenticators (Face ID/Touch ID/Windows Hello) and roaming authenticators (security keys) to the extent feasible in the test environment.
8. Confirm the domain migration from `app.vwo.com` to `app.wingify.com` does not break bookmarked links, in-progress OAuth redirects, or old password-reset emails.
9. Validate the login page across the confirmed browser, device, and responsive-breakpoint matrix (Section 5), treating each as unconfirmed until tested — not assumed passing.
10. Validate baseline security-adjacent UI behavior: HTTPS enforcement, absence of mixed-content warnings, and password value never appearing in page source.
11. Determine (not assume) whether repeated failed login attempts trigger lockout, CAPTCHA, or rate limiting, and document the observed behavior.
12. Determine (not assume) the session/token expiry duration associated with "Remember me."

---

## 3. Features to be Tested

| # | Feature / Flow | Expected Behavior (per source material) | Unknowns / To Be Verified |
|---|---|---|---|
| 1 | Email ID field | Accepts input; participates in Sign in flow | Field-level format/length validation rules |
| 2 | Password field | Masked by default (confirmed); eye icon reveals/hides value (confirmed) | Password complexity policy |
| 3 | "Sign in" button (email/password) | Authenticates an existing user and lands them on their dashboard | Exact error messaging for invalid credentials |
| 4 | "Forgot Password?" link | Initiates password recovery without requiring an active session | Recovery flow steps beyond the link itself; reset-email domain (see Risk R-02) |
| 5 | "Remember me" checkbox | When checked: persists session across browser restart. When unchecked: does not persist | Session/token expiry duration |
| 6 | "Sign in with Google" | Functionally equivalent authentication outcome to email/password; must handle consent-denial/cancel | Google's own consent-screen behavior (third-party, out of scope) |
| 7 | "Sign in using SSO" | Functionally equivalent authentication outcome to email/password; must handle consent-denial/cancel | Identity provider unconfirmed — blocking dependency (Risk R-01) |
| 8 | "Sign in with Passkey" | Functionally equivalent authentication outcome to email/password; validate platform authenticators (Face ID/Touch ID/Windows Hello) and roaming authenticators (security keys) | Device/browser passkey support matrix; feasibility of roaming-authenticator testing in the available environment |
| 9 | "Start a FREE TRIAL" link | Routes new users into signup, separate from the existing-user login path | Signup flow content itself (beyond confirming separation from login) |
| 10 | Privacy Policy / Terms links | Navigate to respective legal pages | Destination content ownership is outside QA scope |
| 11 | Domain migration (app.vwo.com → app.wingify.com) | Existing account/data unaffected per on-page banner (confirmed); bookmarks, in-progress OAuth redirects, and old password-reset emails must not break | Actual redirect implementation details |
| 12 | Failed-login handling | N/A — behavior not yet known | Lockout, CAPTCHA, or rate-limiting presence and thresholds — must be validated during execution, preferably in staging (Risk R-03) |
| 13 | Transport/page security (UI-observable) | HTTPS enforced; no mixed-content warnings; password value never appears in page source | Any deeper security implementation is out of scope |

---

## 4. Test Strategy / Approach

### 4.1 Functional Testing
- Validate the primary success path for each of the four authentication methods (email/password, Google, SSO, Passkey) resulting in a landed, authenticated dashboard session.
- Validate "Forgot Password?" is reachable and initiates recovery without an existing session.
- Validate "Remember me" checked vs. unchecked behavior across a browser restart.
- Validate "Start a FREE TRIAL" leads to a signup flow distinct from the login path, with no cross-contamination between new-user and existing-user flows.

### 4.2 Negative Testing
- Invalid/empty email or password combinations on the email/password path.
- Cancel/deny-consent scenarios on Google sign-in, SSO, and Passkey — each must be confirmed to fail gracefully (return to login, no partial/inconsistent authenticated state).
- Repeated failed login attempts, to observe and document whether lockout, CAPTCHA, or rate limiting occurs (execution environment per Risk R-03 — staging preferred).
- Access to "Forgot Password?" flow attempted both with and without an existing session, to confirm no session is required.
- Navigation to the legacy `app.vwo.com` login URL and any bookmarked deep links, to confirm redirect integrity to `app.wingify.com`.

### 4.3 Usability Testing
- Clarity and visibility of field labels, placeholder text, and button states (enabled/disabled) across all four authentication entry points.
- Password show/hide toggle behaves predictably and does not obscure other field content.
- Error and success messaging is visible, understandable, and appropriately timed.
- "Start a FREE TRIAL" and "Sign in" are visually and functionally distinguishable so a returning user cannot mistakenly create a duplicate account.

### 4.4 Security-Adjacent Testing (UI-observable only)
- Confirm the page is served over HTTPS with no mixed-content warnings in the browser console.
- Confirm the password value never appears in page source (view-source / DOM inspection at the UI level only — not a code-level security audit).
- Observe and document failed-login-attempt handling (lockout/CAPTCHA/rate-limiting), without assuming a specific mechanism exists.
- No deeper security implementation (token handling, encryption, backend session storage) is assessed — out of scope, per Section 1.

### 4.5 Compatibility Testing
- **Desktop browsers:** Chrome, Firefox, Safari, Edge — latest two versions each.
- **Mobile browsers:** Safari on iOS, Chrome on Android — latest two OS versions each.
- **Responsive breakpoints:** Desktop (>1024px), Tablet (768–1024px), Mobile (<768px).
- **Zoom:** Page usability confirmed at 150–200% browser zoom.
- None of the above are treated as pre-confirmed; each combination is in scope to validate, not assumed passing, per source material.

### 4.6 Accessibility Testing (baseline)
- Keyboard-only navigation through all interactive login elements (fields, checkbox, links, buttons) in a logical tab order.
- Visible focus indicators on all interactive elements.
- Form labels correctly associated with their inputs for assistive technology.
- Usability retained at the specified zoom levels (see 4.5), which also supports low-vision accessibility.
- Depth of this accessibility pass is baseline-level; a formal WCAG conformance audit is not defined in the source material — To be verified if required.

### 4.7 Regression Testing
- Dedicated regression pass on the domain migration (`app.vwo.com` → `app.wingify.com`): bookmarked links, in-progress OAuth redirects (Google/SSO), and pre-migration password-reset emails must all continue to function post-migration.
- Re-validation of all four authentication paths and supporting flows (Forgot Password, Remember Me, Start Free Trial) after any future change to the login page, using this plan as the baseline scope.

### 4.8 Per-Authentication-Method Notes
- **Email/Password:** Fully testable end-to-end on this page.
- **Google Sign-in:** Testable through invocation and the return-to-VWO handoff; Google's own hosted screens are third-party and outside this plan's control, though consent-denial/cancel handling on return is in scope.
- **SSO:** Testable through invocation and the return-to-VWO handoff; the identity provider's hosted screens are outside scope until the provider is confirmed (Risk R-01). Consent-denial/cancel handling on return is in scope.
- **Passkey:** Testable at the UI trigger and platform-prompt level; underlying platform/browser passkey support is device-dependent. Roaming-authenticator (security key) testing is included where feasible with available hardware — feasibility itself is To be verified.

### 4.9 Manual vs. Automated
Execution mode is not prescribed in the source material and is left to the team producing the detailed test case suite. Note that Google sign-in, SSO, and Passkey flows involve third-party or platform-native UI (consent screens, biometric prompts, security-key interaction) that may constrain straightforward automation — To be verified during test case design.

---

## 5. Test Environment

| Item | Detail | Status |
|---|---|---|
| Primary environment | https://app.vwo.com/#/login (redirects to https://app.wingify.com) | Confirmed |
| Staging/UAT environment | Preferred for negative-path and repeated-failed-login testing, to avoid impacting production accounts | Availability — To be verified with QA/dev team |
| Desktop browsers | Chrome, Firefox, Safari, Edge — latest two versions each | In scope to validate; not pre-confirmed |
| Mobile browsers | Safari on iOS, Chrome on Android — latest two OS versions each | In scope to validate; not pre-confirmed |
| Responsive breakpoints | Desktop (>1024px), Tablet (768–1024px), Mobile (<768px) | In scope to validate; not pre-confirmed |
| Zoom levels | 150–200% browser zoom | In scope to validate; not pre-confirmed |
| Test accounts | Synthetic/dedicated QA test accounts only — never real customer credentials | Confirmed as a requirement; specific accounts (email/password, Google-linked, SSO-linked, Passkey-enrolled) — To be provisioned |
| Passkey hardware | Platform authenticators (Face ID/Touch ID/Windows Hello) and roaming authenticators (security keys) | Availability of specific test devices/hardware — To be verified |
| Network conditions | Standard broadband, for page-load benchmarking | Assumed baseline per draft benchmark; not a confirmed SLA |

---

## 6. Risk Assessment

| Risk ID | Description | Probability | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | SSO identity provider is unconfirmed on the UI, so SSO test coverage may be incomplete until the dev/product team confirms the provider | High | High | Treat as a blocking dependency for full SSO sign-off; request provider confirmation from product/dev team before SSO execution begins; proceed with provider-agnostic handoff/consent-denial testing in the interim |
| R-02 | Domain migration (`app.vwo.com` → `app.wingify.com`) could break old bookmarks or pre-migration password-reset emails | Medium | High | Execute a dedicated regression pass (Section 4.7) covering bookmarked links, in-progress OAuth redirects, and pre-migration reset emails before sign-off |
| R-03 | Testing repeated failed logins against production could lock out real test accounts or trigger security alerts | Medium | Medium | Prefer staging/UAT environment for repeated-failed-login and negative-path testing; confirm staging availability with QA/dev team before execution; use synthetic accounts only |
| R-04 | Passkey roaming-authenticator (security key) testing may not be feasible depending on available test hardware | Medium | Medium | Confirm hardware availability during environment setup; if unavailable, document as a coverage gap rather than skipping silently |
| R-05 | Behavior of failed-login lockout/CAPTCHA/rate-limiting is unknown, which could affect test repeatability and account availability | Medium | Medium | Observe and document behavior early in execution (ideally in staging); adjust retry-based test design once actual behavior is known |
| R-06 | "Remember me" session/token expiry duration is unknown, which could affect test scheduling for cross-restart validation | Low | Medium | Determine actual expiry empirically during execution; design persistence tests to accommodate an unknown duration rather than assuming a fixed window |
| R-07 | Third-party dependencies (Google, unconfirmed SSO provider) may change their own hosted screens independently of VWO, affecting the return-to-VWO handoff | Low | Medium | Scope testing to the handoff and return behavior only; do not certify third-party screens as part of this plan |
| R-08 | Compatibility matrix (browsers, devices, breakpoints, zoom) is untested and unconfirmed; any combination could reveal defects | Medium | Medium | Execute the full matrix defined in Section 5 systematically rather than sampling, given no prior confirmation exists |

---

## 7. Entry Criteria

- The login page (`https://app.vwo.com/#/login`) is accessible and loads without blocking errors, with redirect to `https://app.wingify.com` functioning.
- All UI elements listed in Section 3 are rendered and available for interaction.
- Synthetic/dedicated QA test accounts are provisioned for each authentication path (email/password, Google-linked, SSO-linked once provider is confirmed, Passkey-enrolled).
- Staging/UAT environment availability has been confirmed with the QA/dev team (Risk R-03); if unavailable, an explicit risk-accepted decision to test negative paths on production has been documented.
- SSO identity provider has been confirmed by the product/dev team, or SSO execution is explicitly scoped to provider-agnostic handoff/consent-denial testing only (Risk R-01).
- A separate, detailed test case suite has been authored referencing this Test Plan (this document intentionally excludes test cases).

## 8. Exit Criteria

- All planned scenarios across the four authentication paths, Forgot Password, Remember Me, Start Free Trial, and domain-migration regression have been executed.
- No open Critical or High severity defects remain against the features in Section 3.
- Compatibility matrix in Section 5 has been executed across all listed browsers, devices, breakpoints, and zoom levels, with results documented (pass/fail per combination, not assumed).
- Baseline security-adjacent checks (HTTPS enforcement, no mixed content, password not in page source) have passed.
- Observed behavior for failed-login handling and "Remember me" expiry has been documented, even if the underlying mechanism differs from initial assumptions.
- All Risk Assessment items (Section 6) have been either resolved, formally accepted, or have a documented mitigation status.
- Test summary/execution report has been reviewed and signed off by QA lead / stakeholders.

---

## 9. Deliverables

1. This Test Plan document (`Test_Plan.md`)
2. Detailed test case suite covering all features in Section 3 (separate document — explicitly out of scope here)
3. Test data / synthetic account provisioning record
4. Compatibility execution matrix results (per Section 5)
5. Defect log / bug reports raised during execution
6. Risk resolution log tracking status of each item in Section 6 (especially R-01 SSO provider confirmation and R-03 staging availability)
7. Test execution summary / closure report
8. Regression checklist for the domain-migration pass (Section 4.7), retained for reuse in future releases

---

*This document was generated strictly from the UI elements, functional expectations, compatibility expectations, environment expectations, performance/security expectations, and known risks explicitly provided in the source request. No authentication providers, SLAs, backend behaviors, or security implementation details were assumed beyond what was confirmed; all such gaps are marked "To be verified."*
