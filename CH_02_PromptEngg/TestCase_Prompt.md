ROLE:
You are a Senior QA Architect with 16+ years of experience in enterprise application testing, specializing in web-based authentication and login flow testing.

INSTRUCTIONS:
- Generate a comprehensive set of Test Cases for the VWO login page, based on the Test_Plan.md already created.
- Cover positive, negative, and edge cases for each login method observed, plus compatibility, security-adjacent, and accessibility cases.
- Every scenario listed under CONTEXT below must become at least one test case row; expand into multiple rows where a scenario has more than one meaningful variation (e.g. valid/invalid, checked/unchecked).
- [Don't] Do not invent error messages, field validations, or behaviors not explicitly observed on the actual page.

CONTEXT:
Target URL: https://app.vwo.com/#/login
Observed UI elements: Email ID field, Password field (with show/hide toggle), "Forgot Password?" link, "Remember me" checkbox, "Sign in" button, "Sign in with Google", "Sign in using SSO", "Sign in with Passkey", "Start a FREE TRIAL" link.
Reference: @Test_Plan.md for scope alignment.

Scenarios to cover:
- Valid email + valid password → successful login and redirect to dashboard.
- Valid email + valid password + "Remember me" checked → session persists after browser restart.
- Valid email + valid password + "Remember me" unchecked → session does NOT persist after browser restart.
- Clicking "Start a FREE TRIAL" → routes to signup, not login.
- Click "Sign in with Google" → OAuth consent screen appears → successful auth logs user in.
- Click "Sign in with Google" → user cancels/denies consent → returned to login page, not logged in, no crash.
- Click "Sign in using SSO" → routed to SSO/IdP entry point (exact provider to be verified during execution).
- Click "Sign in using SSO" with an account not provisioned for SSO → appropriate error/fallback shown (to be verified).
- Click "Sign in with Passkey" → device passkey/biometric prompt appears → successful auth logs user in.
- Click "Sign in with Passkey" on a device with no enrolled passkey → fallback or error shown (to be verified).
- Login page renders correctly on Chrome, Firefox, Safari, Edge (latest 2 versions each).
- Login page renders correctly on mobile Safari (iOS) and mobile Chrome (Android).
- Login form layout remains usable at tablet (768–1024px) and mobile (<768px) breakpoints.
- Page remains usable at 150–200% browser zoom.
- Navigating to legacy app.vwo.com/#/login correctly loads/redirects without errors.
- A bookmarked/old link to app.vwo.com/#/login still resolves correctly post-migration.
- Password field masks input by default.
- Clicking the eye icon toggles password visibility and toggles back correctly.
- Entering an incorrect password shows an appropriate error and does not log the user in.
- Repeated incorrect login attempts (5+) — verify whether lockout/CAPTCHA/rate limiting triggers (to be verified).
- Confirm HTTPS enforcement with no mixed-content warnings.
- Confirm password value never appears in page source/DOM in plain text.
- Login page loads within a 3-second draft benchmark on standard broadband (to be verified).
- Clicking "Forgot Password?" routes to the password recovery flow.
- "Terms" and "Privacy policy" links are reachable and open the correct pages without requiring login.
- Domain-migration banner does not overlap or block any login field/button at mobile breakpoint.
- Submitting the form with an empty email field, empty password field, or both empty → validation error, no login attempt sent.
- Entering an invalid/malformed email format (e.g. "test@") → validation error shown.
- Attempting login with a non-existent account email → appropriate error shown, no account details leaked.
- Tabbing through the form via keyboard only → logical focus order, "Sign in" reachable/triggerable via keyboard.
- Every field and button has a screen-reader-accessible label and a visible focus indicator when navigating by keyboard.

EXPECTED:
A complete, thorough set of test cases (30+ rows, expanded further where a scenario has multiple meaningful variants) covering standard login, Google sign-in, SSO, Passkey, Forgot Password, Remember Me, compatibility, security-adjacent, and accessibility scenarios — clearly marking any unverified assumptions.

PARAMETERS:
- Follow anti-hallucination guidelines strictly (@ch_01_anti_hallucination.md) — do not fabricate specific error text, validation rules, or backend behavior not visible in the UI. Mark unconfirmed items as "To be verified."

OUTPUT:
A single markdown file named Test_Cases.md, saved at path: CH_02_PromptEngg/Test_Cases.md
Use a table with columns: Test ID, Description, Steps, Expected Result, Priority. Every scenario above must map to at least one row.

TONE: Professional, precise, industry-standard QA documentation style.