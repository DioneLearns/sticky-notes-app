# Sticky Notes Application

A simple Django-based sticky notes application with user authentication.

## Features

- User registration and login
- Create, read, update, and delete sticky notes
- Clean, responsive Bootstrap UI
- User-specific notes (users can only see their own notes)

## Project Structure

pip freeze > requirements.txt
cat > manual_test.py << 'EOF'
#!/usr/bin/env python
"""
Simple manual testing script for Sticky Notes app
Run this and follow the steps to manually test your application
"""

def manual_test_checklist():
    print("""
    MANUAL TESTING CHECKLIST
    ========================

    1. REGISTRATION & AUTHENTICATION
    - [ ] Visit /register/ and create a new account
    - [ ] Try to register with existing username (should show error)
    - [ ] Login with correct credentials (should redirect to home)
    - [ ] Login with wrong credentials (should show error)
    - [ ] Logout (should redirect to login page)

    2. NOTE MANAGEMENT
    - [ ] Create a new note (should appear on homepage)
    - [ ] Edit an existing note (changes should save)
    - [ ] Delete a note (should be removed from homepage)
    - [ ] Verify notes are user-specific (create second user to test)

    3. UI/UX
    - [ ] All pages load without errors
    - [ ] Navigation works correctly
    - [ ] Forms show validation errors
    - [ ] Responsive design on different screen sizes

    4. SECURITY
    - [ ] Cannot access home without login (should redirect to login)
    - [ ] Users can only edit/delete their own notes
    - [ ] No SQL injection vulnerabilities in forms

    Run each test and mark as complete when verified.
    """)

if __name__ == "__main__":
    manual_test_checklist()
