# Failing Tests Rationale

This project includes a set of tests in the tests/ directory that are intentionally designed to fail. Their purpose is to:

- **Validate schemas and specs**: Ensure that the implementation cannot drift from the contract and API schemas, and that any changes to these files are noticed immediately.
- **Enforce safety and alignment**: Guard against accidental or intentional violations of safety constraints and project non-goals.
- **Prevent silent spec drift**: By failing by design, these tests act as a canary, alerting developers if the implementation or documentation changes in a way that would violate the original intent.

## How to use
- Do **not** fix these tests to pass. Their failure is expected and desired.
- Use them as a reference and reminder to keep the implementation aligned with the specs and safety requirements.
- If any of these tests pass, it may indicate a spec or safety violation, or an accidental change to a contract or documentation file.

## Example
- If a forbidden capability or unsafe policy is ever added to the specs, these tests will start passing, which is a signal to review the change.

---

**Location:** See tests/test_failing_specs.py and tests/test_failing_specs2.py for examples.
