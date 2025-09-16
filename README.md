## 🛒 Sauce Demo – QA Automation (Python + Behave + Selenium)

A clear, reliable test suite for the SauceDemo online store. It follows the real customer journey—log in → add items → see cart updates → check out → confirm order—so product teams can trust what’s shipped.


![image alt](https://github.com/onyxcollc/Sauce_Demo_Project/blob/916bca1086ff000fb376dfde5e8e984c26527486/Screenshot%202025-09-15%20195802.png)

---

## ✨ What makes this project special

Readable tests (BDD): Scenarios are written like short stories so anyone can understand what’s being tested.

Clean design (POM): Pages and actions are organized for reuse, making updates fast and low-risk.

Runs nonstop: Multiple features execute back-to-back without getting stuck on pop-ups or leftover tabs.

Stable & low-flakiness: Smart waits and stable selectors reduce random failures.

“Quiet” browser: Chrome prompts (like password popups) are silenced so tests stay focused on the app.

---

## ✅ User journeys covered

Login: valid users, invalid credentials, locked-out messaging

Shopping: add/remove products; verify the cart badge number updates correctly

Checkout: personal info, order overview, final confirmation screen

Navigation & safety: logout behavior and protections against skipping required steps

---

## 🧗 Key challenges & how I solved them

Chrome password/leak popups → Launched a clean browser profile and disabled those prompts, keeping flows uninterrupted.

State bleeding between scenarios → Automatically reset cookies, storage, and extra tabs so each scenario starts fresh.

Timing issues on dynamic elements → Used reliable waits so UI updates are fully loaded before checks.

Fragile selectors → Standardized on stable, test-friendly attributes to avoid breakage when styles change.

---

## 🏆 Wins for the team

Readable specs anyone can scan and approve

Consistent, repeatable runs across many features

Fewer flaky failures, faster debugging, and simpler maintenance

Foundation for CI (easy to plug into GitHub Actions and reporting tools like Allure)

---

## 🧭 How it’s organized (plain English)

Features: Human-readable scenarios (login, cart, checkout)

Steps: The glue that performs each step from the scenarios

Pages: Reusable actions for each screen (login, inventory, cart, checkout)

Support: Browser setup and test run rules (start/stop, cleanup between scenarios)

---

## 🚀 How to run (high level)

1. Set up a Python environment and install the listed requirements.

2. Run the test suite from the project root (all features or a single feature).

3. Optional: add a test report tool (e.g., Allure) and wire it to CI.


---

## 👤 Author

Nicholas Olumese — QA Engineer transitioning from UAT to Automation.
