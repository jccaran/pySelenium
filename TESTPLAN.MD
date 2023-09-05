# Objective

Verify that the login page functions correctly, securely, and user-friendly.
# Scope

The login page of the web application: https://www.hudl.com/login

# Test Cases

## Functional Tests

1. Verify the login page is accessible from the landing page (https://www.hudl.com)
2. Verify the login page is accessible from the mobile landing page.
3. Login Page navigation is present - Email, Password, Continue
4. Verify additional links - Site Terms, Privacy Policy
5. Valid Login - Username, Password - Verify user is logged in and redirected to the home page
6. Invalid Login - Username, Bad Password - Verify user not logged in and error message is displayed
7. Invalid Login - Bad Username, Password - Verify user is not logged in and error message is displayed
8. Validate UI, API, and Database field lengths are consistent.
9. (Forgot Password workflow) Login with reset password.
10. (Forgot Password workflow) Reset password and cannot login with old password.
11. (New Account) Create new account and login.

## Security Tests
1. SQL Injection - Verify that the login page is not vulnerable to SQL injection attacks
2. Cross-Site Scripting - Verify that the login page is not vulnerable to XSS attacks
3. Brute Force - Verify that the login page is not vulnerable to brute force (API; multiple failed login limit)
4. Password Policy - Test password complexity and strength requirements (API)
5. Session Management - Session handling, logout, and timeout
6. There are others, depending on the needs of security and what the highest risk threats identified by OWASP
7. Password field is properly masked.

## Usability Tests
1. Verify login is responsive on various screen sizes and devices
2. Check for user-friendly error messages
3. Test keyboard navigation and tab order
4. Evaluate clarity of field labels and instructions

## Compatibility Tests
1. Verify login page is compatible with supported browsers and versions
2. Test compatibility on supported mobile devices and tablets (iOS and Android)

## Performance Tests
1. Page Load time, especially during high traffic (SLA?)
2. Response times for login requests (SLA?)
3. User concurrency and load for scalability (SLA?)

## Regression Tests
1. Verify updates to related pages (landing page, login page, etc.) do not impact login functionality.
2. Known critical bugs and issues have related test scenarios in automation.

## Integrations and other workflows
1. Login via Wyscout integration (landing page)
2. Login via VolleyMetrics integration (landing page
3. Login via WIMU CLoud integration (landing page)
4. Login via Facebook integration (Login page)
5. Login via Google integration (Login page)
6. Login via Apple integration (Login page)
7. Forgot Password workflow
8. Create Account workflow
