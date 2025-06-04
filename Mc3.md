# Mini Challenge 3

## Override password reset templates

### Acceptance Criteria

1. Override the password reset form template.
1.1. Email form: template_name = "registration/password_reset_form.html"
2. Override the email form submittal confirmation template.
2.1. Email form submitted successfully: template_name = "registration/password_reset_done.html"
3. Override the new password form template.
3.1. New password form: template_name = "registration/password_reset_confirm.html"
4. Override the password reset complete template.
4.1. Password reset complete: template_name = "registration/password_reset_complete.html"

## Note
If you want to override the email templates (optional) these are:
Email body: email_template_name = "registration/password_reset_email.html"
Email subject line: subject_template_name = "registration/password_reset_subject.txt"