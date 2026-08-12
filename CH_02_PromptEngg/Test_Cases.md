# Test Cases: VWO Login Page

**Target URL:** https://app.vwo.com/#/login (redirects to https://app.wingify.com)
**Reference:** `Test_Plan.md` (scope, strategy, environment, risks)
**Document Type:** Test Case Suite (execution-ready)
**Note:** Items not confirmed on the live UI are marked **"To be verified"** in the Expected Result column, per anti-hallucination guidelines. No specific error message text, validation rule, or backend behavior has been fabricated — where exact wording/behavior is unknown, the expected result states that an appropriate message/behavior should appear, without asserting its content.

---

## 1. Email/Password Login — Positive

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-001 | Valid email + valid password → successful login | 1. Navigate to login page. 2. Enter a valid, registered email. 3. Enter the correct password. 4. Click "Sign in." | User is authenticated and redirected to their dashboard. | High |
| TC-002 | Valid login with "Remember me" checked → session persists after browser restart | 1. Navigate to login page. 2. Enter valid email + password. 3. Check "Remember me." 4. Click "Sign in." 5. Close and reopen the browser. 6. Navigate to the app URL again. | User remains authenticated without being prompted to log in again. | High |
| TC-003 | Valid login with "Remember me" unchecked → session does NOT persist after browser restart | 1. Navigate to login page. 2. Enter valid email + password. 3. Leave "Remember me" unchecked. 4. Click "Sign in." 5. Close and reopen the browser. 6. Navigate to the app URL again. | User is not automatically authenticated and is required to log in again. | High |

## 2. Password Field Behavior

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-004 | Password field masks input by default | 1. Navigate to login page. 2. Click into the password field. 3. Type a password value. | Characters are displayed masked (e.g., dots/asterisks), not in plain text. | High |
| TC-005 | Eye icon toggles password visibility on | 1. Enter a value in the password field. 2. Click the eye icon. | Password value becomes visible in plain text. | Medium |
| TC-006 | Eye icon toggles password visibility back off | 1. With password visible (per TC-005), click the eye icon again. | Password value returns to masked display. | Medium |

## 3. Email/Password Login — Negative & Edge Cases

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-007 | Incorrect password for a valid email | 1. Enter a valid, registered email. 2. Enter an incorrect password. 3. Click "Sign in." | Login is rejected; an appropriate error message is shown (exact wording — To be verified); user is not logged in. | High |
| TC-008 | Login attempt with a non-existent account email | 1. Enter an email not associated with any account. 2. Enter any password. 3. Click "Sign in." | Login is rejected with an appropriate error message that does not reveal whether the email exists in the system (exact wording and non-disclosure behavior — To be verified); user is not logged in. | High |
| TC-009 | Submit with empty email field only | 1. Leave email field blank. 2. Enter a password. 3. Click "Sign in." | A validation error is shown for the missing email; no login request is sent to the server (exact validation message — To be verified). | Medium |
| TC-010 | Submit with empty password field only | 1. Enter a valid email. 2. Leave password field blank. 3. Click "Sign in." | A validation error is shown for the missing password; no login request is sent to the server (exact validation message — To be verified). | Medium |
| TC-011 | Submit with both email and password fields empty | 1. Leave both fields blank. 2. Click "Sign in." | Validation errors are shown for both fields; no login request is sent to the server (exact validation messages — To be verified). | Medium |
| TC-012 | Malformed/invalid email format | 1. Enter an invalid email format (e.g., "test@"). 2. Enter any password. 3. Click "Sign in." | A validation error is shown indicating the email format is invalid; no login request is sent (exact validation message — To be verified). | Medium |
| TC-013 | Repeated incorrect login attempts (5+) | 1. Enter a valid email with an incorrect password. 2. Click "Sign in." 3. Repeat at least 5 times. | System behavior after repeated failures (account lockout, CAPTCHA, rate limiting, or none of the above) is observed and documented — mechanism is unconfirmed and **To be verified**. Prefer staging/UAT environment for this test to avoid impacting production accounts (per Test_Plan Risk R-03). | High |

## 4. Google Sign-In

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-014 | Google sign-in — successful authentication | 1. Click "Sign in with Google." 2. Complete the Google OAuth consent screen with a valid, linked Google account. | User is redirected back to VWO and authenticated, landing on their dashboard. | High |
| TC-015 | Google sign-in — user cancels/denies consent | 1. Click "Sign in with Google." 2. On the Google consent screen, cancel or deny consent. | User is returned to the VWO login page without being logged in; no application crash or broken state occurs. | High |

## 5. SSO Sign-In

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-016 | SSO sign-in — routing to identity provider entry point | 1. Click "Sign in using SSO." | User is routed to an SSO/identity-provider entry point. The specific identity provider is unconfirmed on the UI and **To be verified with the product/dev team** before full execution. | High |
| TC-017 | SSO sign-in — account not provisioned for SSO | 1. Click "Sign in using SSO." 2. Attempt to authenticate with an account/email that is not provisioned for SSO. | An appropriate error or fallback behavior is expected; exact message/fallback path is unconfirmed and **To be verified**. | Medium |

## 6. Passkey Sign-In

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-018 | Passkey sign-in — successful authentication | 1. Click "Sign in with Passkey." 2. Complete the device's passkey/biometric prompt (e.g., Face ID, Touch ID, Windows Hello, or security key) with an enrolled passkey. | User is authenticated and redirected to their dashboard. | High |
| TC-019 | Passkey sign-in — no enrolled passkey on device | 1. Click "Sign in with Passkey" on a device/browser with no enrolled passkey for the account. | A fallback path or error message is expected; exact behavior is unconfirmed and **To be verified**. | Medium |

## 7. Forgot Password

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-020 | "Forgot Password?" link routes to recovery flow | 1. From the login page (without logging in), click "Forgot Password?" | User is routed to the password recovery flow, accessible without an active session. Exact recovery flow steps beyond this navigation — To be verified. | High |

## 8. Start Free Trial / Signup Separation

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-021 | "Start a FREE TRIAL" routes to signup, not login | 1. From the login page, click "Start a FREE TRIAL." | User is routed to a signup flow for new users, distinct and separate from the existing-user login path. | High |

## 9. Legal Links

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-022 | "Terms" link reachable without login | 1. From the login page (without logging in), click the "Terms" link. | The correct Terms page opens without requiring authentication. | Low |
| TC-023 | "Privacy policy" link reachable without login | 1. From the login page (without logging in), click the "Privacy policy" link. | The correct Privacy Policy page opens without requiring authentication. | Low |

## 10. Domain Migration

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-024 | Legacy URL loads/redirects without errors | 1. Navigate directly to `app.vwo.com/#/login`. | Page correctly loads or redirects to `app.wingify.com` without errors, per the on-page migration banner. | High |
| TC-025 | Bookmarked/old link resolves correctly post-migration | 1. Use a previously bookmarked link to `app.vwo.com/#/login` (simulating a pre-migration bookmark). 2. Navigate to it. | Link resolves correctly to a working login page post-migration, with account/data unaffected per the on-page banner. | High |
| TC-026 | Migration banner does not overlap/block fields at mobile breakpoint | 1. Load the login page at a mobile viewport (<768px). 2. Observe the domain-migration banner alongside the login form. | Banner does not overlap or obstruct any login field or button; all elements remain usable. | Medium |

## 11. Compatibility — Desktop Browsers

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-027 | Login page renders correctly on Chrome (latest 2 versions) | 1. Open the login page in Chrome (current and previous major version). | Page layout, fields, and buttons render correctly and are functional. Not pre-confirmed — result to be recorded per version. | High |
| TC-028 | Login page renders correctly on Firefox (latest 2 versions) | 1. Open the login page in Firefox (current and previous major version). | Page layout, fields, and buttons render correctly and are functional. Not pre-confirmed — result to be recorded per version. | High |
| TC-029 | Login page renders correctly on Safari (latest 2 versions) | 1. Open the login page in Safari (current and previous major version). | Page layout, fields, and buttons render correctly and are functional. Not pre-confirmed — result to be recorded per version. | High |
| TC-030 | Login page renders correctly on Edge (latest 2 versions) | 1. Open the login page in Edge (current and previous major version). | Page layout, fields, and buttons render correctly and are functional. Not pre-confirmed — result to be recorded per version. | High |

## 12. Compatibility — Mobile Browsers

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-031 | Login page renders correctly on mobile Safari (iOS, latest 2 OS versions) | 1. Open the login page in Safari on iOS (current and previous major OS version). | Page layout, fields, and buttons render correctly and are functional. Not pre-confirmed — result to be recorded per OS version. | High |
| TC-032 | Login page renders correctly on mobile Chrome (Android, latest 2 OS versions) | 1. Open the login page in Chrome on Android (current and previous major OS version). | Page layout, fields, and buttons render correctly and are functional. Not pre-confirmed — result to be recorded per OS version. | High |

## 13. Compatibility — Responsive Breakpoints & Zoom

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-033 | Login form usable at tablet breakpoint (768–1024px) | 1. Resize/emulate viewport to within 768–1024px. 2. Attempt to interact with all login fields and buttons. | Form layout remains usable; all elements are visible and interactable without overlap. | Medium |
| TC-034 | Login form usable at mobile breakpoint (<768px) | 1. Resize/emulate viewport to below 768px. 2. Attempt to interact with all login fields and buttons. | Form layout remains usable; all elements are visible and interactable without overlap. | Medium |
| TC-035 | Page usable at 150% browser zoom | 1. Set browser zoom to 150%. 2. Attempt to interact with all login fields and buttons. | Page remains usable; no critical content is clipped or inaccessible. | Low |
| TC-036 | Page usable at 200% browser zoom | 1. Set browser zoom to 200%. 2. Attempt to interact with all login fields and buttons. | Page remains usable; no critical content is clipped or inaccessible. | Low |

## 14. Security-Adjacent (UI-Observable)

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-037 | HTTPS enforcement with no mixed-content warnings | 1. Navigate to the login page. 2. Confirm the URL uses HTTPS. 3. Check the browser console/security indicator for mixed-content warnings. | Page is served over HTTPS; no mixed-content warnings appear. | High |
| TC-038 | Password value never appears in page source/DOM in plain text | 1. Enter a password value in the field. 2. Inspect the page source/DOM (view-source or browser dev tools) at the UI level. | Password value does not appear anywhere in plain text in the page source/DOM. | High |
| TC-039 | Page load time within draft benchmark | 1. Navigate to the login page on standard broadband. 2. Measure page load time. | Page loads within approximately 3 seconds (draft benchmark, not a confirmed SLA — result to be recorded and compared against this draft figure only). | Low |

## 15. Accessibility

| Test ID | Description | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-040 | Keyboard-only navigation through the form | 1. From the login page, use only the Tab key to move through all interactive elements. 2. Continue until "Sign in" is reached. 3. Trigger "Sign in" via keyboard (e.g., Enter/Space). | Focus moves through fields, checkbox, links, and buttons in a logical order; "Sign in" is reachable and triggerable via keyboard alone. | Medium |
| TC-041 | Screen-reader-accessible labels and visible focus indicators | 1. Navigate through each field and button using keyboard/screen reader. | Each field and button exposes an accessible label (e.g., via associated `<label>` or ARIA attribute) and displays a visible focus indicator when focused via keyboard. | Medium |

---

**Total test cases:** 41 (TC-001 through TC-041), covering all scenarios listed in the CONTEXT scenario list, with multi-variant scenarios (Remember Me checked/unchecked, empty-field combinations, browser/OS matrix, breakpoints, zoom levels, Google/SSO/Passkey success and failure paths) expanded into individual rows.

*This test case suite was derived strictly from the scenarios and UI elements listed in the source request and `Test_Plan.md`. No error message text, field validation rule, or backend/security behavior not explicitly observed has been fabricated; all such items are marked "To be verified."*
