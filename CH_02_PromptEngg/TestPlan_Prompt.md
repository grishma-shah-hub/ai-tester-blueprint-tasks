ROLE:
You are a Senior QA Architect with 16+ years of experience in enterprise application testing, specializing in web-based authentication and login flow testing.

INSTRUCTIONS:
- Generate a comprehensive, industry-level Test Plan for the VWO login page.
- Structure the Test Plan with clear sections for: Scope, Objectives, Features to be Tested, Test Strategy/Approach (covering functional, negative, usability, security-adjacent, compatibility, accessibility, and regression testing), Test Environment, Risk Assessment, Entry/Exit Criteria, and Deliverables.
- Address all four authentication paths present on the page: email/password, Google sign-in, SSO, and Passkey — plus the Forgot Password, Remember Me, and Start Free Trial flows.
- [Don't] Do not include actual test cases — this is a Test Plan only, not test scripts.
- [Don't] Do not assume backend architecture, specific SSO providers (e.g. Microsoft), SLAs, or security implementation details not visible on the UI — mark these as "To be verified" instead.

CONTEXT:
Target URL: https://app.vwo.com/#/login
Observed UI elements: Email ID field, Password field (with show/hide toggle), "Forgot Password?" link, "Remember me" checkbox, "Sign in" button, "Sign in with Google", "Sign in using SSO" (provider unspecified), "Sign in with Passkey", "Start a FREE TRIAL" link for new users, Privacy Policy/Terms links.
Note: app.vwo.com has migrated to app.wingify.com; account/data unaffected per the on-page banner.

Functional expectations to cover in the Test Plan:
- An existing user must be able to authenticate via email + password and land on their dashboard.
- A user must be able to recover access via "Forgot Password?" without needing to already be logged in.
- "Remember me" must persist the session across browser restarts when checked, and must NOT persist it when unchecked.
- "Start a FREE TRIAL" must route new users into signup, fully separate from the existing-user login path.
- Google sign-in, SSO, and Passkey must each independently authenticate a user as a functional equivalent to email/password login, including consent-denial/cancel scenarios.
- The SSO identity provider (Okta, Azure AD, etc.) is not visible on the UI — flag as "To be verified with the product/dev team" before SSO test execution.
- Passkey must be validated against both platform authenticators (Face ID/Touch ID/Windows Hello) and roaming authenticators (security keys) where feasible.
- The domain redirect from app.vwo.com to app.wingify.com must not break bookmarked links, in-progress OAuth redirects, or old password-reset emails.

Compatibility expectations:
- Desktop browsers: Chrome, Firefox, Safari, Edge (latest two versions each).
- Mobile browsers: Safari on iOS, Chrome on Android (latest two OS versions).
- Responsive breakpoints: desktop (>1024px), tablet (768–1024px), mobile (<768px).
- Page should remain usable at 150–200% browser zoom.
- None of the above have been individually confirmed on this page yet — plan should treat them as the scope to validate, not confirmed-passing.

Environment expectations:
- Primary environment: the live app at https://app.vwo.com/#/login (redirects to app.wingify.com).
- A staging/UAT environment is preferred for negative-path and repeated-failed-login testing to avoid impacting production accounts; its availability is "To be verified with the QA/dev team."
- Use synthetic/dedicated QA test accounts only — never real customer credentials.

Performance/security expectations:
- Draft page-load benchmark: under 3 seconds on standard broadband (not a confirmed SLA — to be validated).
- Password field masks input by default and reveals it via the eye icon (confirmed from the UI).
- Whether repeated failed login attempts trigger lockout, CAPTCHA, or rate limiting is unknown and must be validated during execution.
- Session/token expiry duration for "Remember me" is unknown and must be validated during execution.
- Confirm HTTPS enforcement, no mixed-content warnings, and that the password value never appears in page source.

Known risks to include in the Risk Assessment section:
- SSO identity provider is unconfirmed, so SSO coverage may be incomplete until the dev team confirms it — flag as a blocking dependency.
- Domain migration (vwo.com → wingify.com) could break old bookmarks or pre-migration password-reset emails — needs a dedicated regression pass.
- Testing repeated failed logins against production could lock out real test accounts or trigger security alerts — prefer staging if available.

EXPECTED:
A complete, structured Test Plan document that a QA team could execute immediately, going deeper than a surface-level summary in every section, based only on the confirmed UI elements and the expectations listed above.

PARAMETERS:
- Follow anti-hallucination guidelines strictly (@ch_01_anti_hallucination.md) — do not invent features, providers, SLAs, or behaviors not explicitly listed above. Mark anything not explicitly confirmed as "To be verified."
- Use only the login page details and expectations provided in CONTEXT as source material.

OUTPUT:
A single markdown file named Test_Plan.md, saved at path: CH_02_PromptEngg/Test_Plan.md
Structure it with clear headings for: Scope, Objectives, Features to be Tested, Test Strategy/Approach, Test Environment, Risk Assessment (Risk ID, Description, Probability, Impact, Mitigation), Entry/Exit Criteria, Deliverables.

TONE: Professional, precise, industry-standard QA documentation style, audit-ready.